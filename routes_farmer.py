from fastapi import APIRouter, HTTPException, Depends, status
from typing import Dict, Any, List, Optional
from database import get_db_connection
from auth import require_farmer
from models import FarmerProfileUpdate, FarmerCropSubmission
from ws_manager import ws_manager

router = APIRouter(prefix="/api/farmer", tags=["Farmer"])

@router.get("/profile")
async def get_profile(user: Dict[str, Any] = Depends(require_farmer)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.id as user_id, u.name, u.email, u.phone,
               fp.village, fp.area, fp.district, fp.state, fp.land_area, fp.land_unit, fp.farming_type, fp.photo_url
        FROM users u
        LEFT JOIN farmer_profiles fp ON u.id = fp.user_id
        WHERE u.id = ?
    """, (user["id"],))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Farmer profile not found")
    return dict(row)

@router.put("/profile")
async def update_profile(req: FarmerProfileUpdate, user: Dict[str, Any] = Depends(require_farmer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (req.name.strip(), req.email.strip() if req.email else None, user["id"]))

    cursor.execute("SELECT id FROM farmer_profiles WHERE user_id = ?", (user["id"],))
    exists = cursor.fetchone()
    if exists:
        cursor.execute("""
            UPDATE farmer_profiles
            SET village = ?, area = ?, district = ?, state = ?, land_area = ?, land_unit = ?, farming_type = ?, photo_url = ?, updated_at = CURRENT_TIMESTAMP
            WHERE user_id = ?
        """, (
            req.village.strip(),
            req.area.strip(),
            req.district.strip(),
            req.state.strip(),
            req.land_area,
            req.land_unit.strip(),
            req.farming_type.strip(),
            req.photo_url.strip() if req.photo_url else None,
            user["id"]
        ))
    else:
        cursor.execute("""
            INSERT INTO farmer_profiles (user_id, village, area, district, state, land_area, land_unit, farming_type, photo_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user["id"],
            req.village.strip(),
            req.area.strip(),
            req.district.strip(),
            req.state.strip(),
            req.land_area,
            req.land_unit.strip(),
            req.farming_type.strip(),
            req.photo_url.strip() if req.photo_url else None
        ))
    
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Farmer profile updated successfully"}

@router.get("/dashboard")
async def get_dashboard(user: Dict[str, Any] = Depends(require_farmer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT village, area, district, state FROM farmer_profiles WHERE user_id = ?", (user["id"],))
    f_prof = cursor.fetchone()
    area = f_prof["area"] if f_prof else "Sankari"
    district = f_prof["district"] if f_prof else "Salem"
    state = f_prof["state"] if f_prof else "Tamil Nadu"

    # Total Crops Added
    cursor.execute("SELECT COUNT(*) as count FROM verification_requests WHERE farmer_id = ?", (user["id"],))
    total_crops = cursor.fetchone()["count"]

    # Pending Requests
    cursor.execute("SELECT COUNT(*) as count FROM verification_requests WHERE farmer_id = ? AND status = 'PENDING'", (user["id"],))
    pending_count = cursor.fetchone()["count"]

    # Verified Requests
    cursor.execute("SELECT COUNT(*) as count FROM verification_requests WHERE farmer_id = ? AND status = 'VERIFIED'", (user["id"],))
    verified_count = cursor.fetchone()["count"]

    # Rejected Requests
    cursor.execute("SELECT COUNT(*) as count FROM verification_requests WHERE farmer_id = ? AND status = 'REJECTED'", (user["id"],))
    rejected_count = cursor.fetchone()["count"]

    # Local Officer Information for this farmer
    cursor.execute("""
        SELECT u.name, u.phone, u.email, op.designation, op.department, op.assigned_area, op.district, op.state
        FROM officer_profiles op
        JOIN users u ON op.user_id = u.id
        WHERE LOWER(op.assigned_area) = LOWER(?) AND LOWER(op.district) = LOWER(?) AND LOWER(op.state) = LOWER(?)
        LIMIT 1
    """, (area, district, state))
    officer_row = cursor.fetchone()
    officer_info = dict(officer_row) if officer_row else None

    # Fallback to district officer if exact area officer not found
    if not officer_info:
        cursor.execute("""
            SELECT u.name, u.phone, u.email, op.designation, op.department, op.assigned_area, op.district, op.state
            FROM officer_profiles op
            JOIN users u ON op.user_id = u.id
            WHERE LOWER(op.district) = LOWER(?) AND LOWER(op.state) = LOWER(?)
            LIMIT 1
        """, (district, state))
        fallback_officer = cursor.fetchone()
        officer_info = dict(fallback_officer) if fallback_officer else None

    conn.close()

    return {
        "location": {
            "village": f_prof["village"] if f_prof else "",
            "area": area,
            "district": district,
            "state": state
        },
        "stats": {
            "total_crops": total_crops,
            "pending_count": pending_count,
            "verified_count": verified_count,
            "rejected_count": rejected_count
        },
        "assigned_officer": officer_info
    }

@router.get("/requests")
async def get_requests(user: Dict[str, Any] = Depends(require_farmer)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.*, u.name as officer_name, op.designation as officer_designation
        FROM verification_requests r
        LEFT JOIN users u ON r.officer_id = u.id
        LEFT JOIN officer_profiles op ON u.id = op.user_id
        WHERE r.farmer_id = ?
        ORDER BY r.id DESC
    """, (user["id"],))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

@router.post("/crops")
async def submit_crop(req: FarmerCropSubmission, user: Dict[str, Any] = Depends(require_farmer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Step 1: Find matched local agriculture officer based on Area + District + State
    cursor.execute("""
        SELECT op.user_id
        FROM officer_profiles op
        WHERE LOWER(op.assigned_area) = LOWER(?) AND LOWER(op.district) = LOWER(?) AND LOWER(op.state) = LOWER(?)
        LIMIT 1
    """, (req.area.strip(), req.district.strip(), req.state.strip()))
    officer = cursor.fetchone()

    # Fallback to district level officer if exact area match is not yet registered
    if not officer:
        cursor.execute("""
            SELECT op.user_id
            FROM officer_profiles op
            WHERE LOWER(op.district) = LOWER(?) AND LOWER(op.state) = LOWER(?)
            LIMIT 1
        """, (req.district.strip(), req.state.strip()))
        officer = cursor.fetchone()

    officer_id = officer["user_id"] if officer else None

    # Step 2: Create produce record with status = 'PENDING'
    cursor.execute("""
        INSERT INTO produce_records (
            crop_name, quantity, unit, area, village, district, state,
            produce_type, quality, availability_date, expected_harvest_date,
            source_type, farmer_id, officer_id, verification_status, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, 'Field Crop', ?, ?, ?, 'FARMER_VERIFIED', ?, ?, 'PENDING', ?)
    """, (
        req.crop_name.strip(),
        req.expected_quantity,
        req.quantity_unit.strip(),
        req.area.strip(),
        req.village.strip() if req.village else "",
        req.district.strip(),
        req.state.strip(),
        req.quality.strip() if req.quality else "Grade A",
        req.expected_harvest_date.strip(),
        req.expected_harvest_date.strip(),
        user["id"],
        officer_id,
        req.notes.strip() if req.notes else ""
    ))
    produce_id = cursor.lastrowid

    # Step 3: Create verification request
    cursor.execute("""
        INSERT INTO verification_requests (
            farmer_id, officer_id, produce_id, crop_name, cultivated_area,
            cultivated_area_unit, expected_quantity, quantity_unit,
            expected_harvest_date, crop_stage, quality, village, area, district, state, notes, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'PENDING')
    """, (
        user["id"],
        officer_id,
        produce_id,
        req.crop_name.strip(),
        req.cultivated_area,
        req.cultivated_area_unit.strip(),
        req.expected_quantity,
        req.quantity_unit.strip(),
        req.expected_harvest_date.strip(),
        req.crop_stage.strip() if req.crop_stage else "Vegetative",
        req.quality.strip() if req.quality else "Grade A",
        req.village.strip() if req.village else "",
        req.area.strip(),
        req.district.strip(),
        req.state.strip(),
        req.notes.strip() if req.notes else ""
    ))
    request_id = cursor.lastrowid
    conn.commit()

    cursor.execute("SELECT * FROM verification_requests WHERE id = ?", (request_id,))
    new_request = dict(cursor.fetchone())
    conn.close()

    # Broadcast WebSocket notification so officer's dashboard immediately reflects this new request!
    await ws_manager.broadcast({
        "type": "REQUEST_SUBMITTED",
        "request": new_request,
        "officer_id": officer_id
    })

    return {
        "status": "success",
        "message": "Crop submitted successfully and routed to local Agriculture Officer for verification.",
        "request": new_request
    }
