from fastapi import APIRouter, HTTPException, Depends, status
from typing import Dict, Any, List, Optional
from database import get_db_connection
from auth import require_officer
from models import OfficerProfileUpdate, ProduceCreate, ProduceUpdate, VerificationAction
from ws_manager import ws_manager

router = APIRouter(prefix="/api/officer", tags=["Officer"])

@router.get("/profile")
async def get_profile(user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.id as user_id, u.name, u.email, u.phone,
               p.designation, p.department, p.assigned_area, p.district, p.state, p.contact, p.photo_url
        FROM users u
        LEFT JOIN officer_profiles p ON u.id = p.user_id
        WHERE u.id = ?
    """, (user["id"],))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Officer profile not found")
    return dict(row)

@router.put("/profile")
async def update_profile(req: OfficerProfileUpdate, user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Update user name and email
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (req.name.strip(), req.email.strip() if req.email else None, user["id"]))

    # Update or insert officer profile
    cursor.execute("SELECT id FROM officer_profiles WHERE user_id = ?", (user["id"],))
    exists = cursor.fetchone()
    if exists:
        cursor.execute("""
            UPDATE officer_profiles
            SET designation = ?, department = ?, assigned_area = ?, district = ?, state = ?, contact = ?, photo_url = ?, updated_at = CURRENT_TIMESTAMP
            WHERE user_id = ?
        """, (
            req.designation.strip(),
            req.department.strip(),
            req.assigned_area.strip(),
            req.district.strip(),
            req.state.strip(),
            req.contact.strip(),
            req.photo_url.strip() if req.photo_url else None,
            user["id"]
        ))
    else:
        cursor.execute("""
            INSERT INTO officer_profiles (user_id, designation, department, assigned_area, district, state, contact, photo_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user["id"],
            req.designation.strip(),
            req.department.strip(),
            req.assigned_area.strip(),
            req.district.strip(),
            req.state.strip(),
            req.contact.strip(),
            req.photo_url.strip() if req.photo_url else None
        ))
    
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Officer profile updated successfully"}

@router.get("/dashboard")
async def get_dashboard(user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch officer's assigned jurisdiction
    cursor.execute("SELECT assigned_area, district, state FROM officer_profiles WHERE user_id = ?", (user["id"],))
    officer_profile = cursor.fetchone()
    area = officer_profile["assigned_area"] if officer_profile else "Sankari"
    district = officer_profile["district"] if officer_profile else "Salem"
    state = officer_profile["state"] if officer_profile else "Tamil Nadu"

    # 1. Total Local Produce Records
    cursor.execute("""
        SELECT COUNT(*) as count, COALESCE(SUM(quantity), 0) as total_quantity
        FROM produce_records
        WHERE LOWER(area) = LOWER(?) AND LOWER(district) = LOWER(?) AND verification_status = 'VERIFIED'
    """, (area, district))
    produce_stat = cursor.fetchone()

    # 2. Farmer Requests Pending
    cursor.execute("""
        SELECT COUNT(*) as count
        FROM verification_requests
        WHERE LOWER(area) = LOWER(?) AND LOWER(district) = LOWER(?) AND status = 'PENDING'
    """, (area, district))
    pending_stat = cursor.fetchone()

    # 3. Verified Records count
    cursor.execute("""
        SELECT COUNT(*) as count
        FROM produce_records
        WHERE LOWER(area) = LOWER(?) AND LOWER(district) = LOWER(?) AND verification_status = 'VERIFIED'
    """, (area, district))
    verified_stat = cursor.fetchone()

    # 4. Recently Added Crops
    cursor.execute("""
        SELECT id, crop_name, quantity, unit, area, village, district, state, availability_date, source_type, verification_status, created_at
        FROM produce_records
        WHERE LOWER(area) = LOWER(?) AND LOWER(district) = LOWER(?)
        ORDER BY id DESC LIMIT 5
    """, (area, district))
    recent_crops = [dict(r) for r in cursor.fetchall()]

    conn.close()

    return {
        "jurisdiction": {
            "area": area,
            "district": district,
            "state": state
        },
        "stats": {
            "total_records": produce_stat["count"] if produce_stat else 0,
            "total_quantity": round(produce_stat["total_quantity"] if produce_stat else 0.0, 2),
            "pending_requests": pending_stat["count"] if pending_stat else 0,
            "verified_records": verified_stat["count"] if verified_stat else 0
        },
        "recent_crops": recent_crops
    }

@router.get("/produce")
async def get_officer_produce(user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT assigned_area, district, state FROM officer_profiles WHERE user_id = ?", (user["id"],))
    prof = cursor.fetchone()
    area = prof["assigned_area"] if prof else "Sankari"
    district = prof["district"] if prof else "Salem"

    cursor.execute("""
        SELECT p.*, u.name as farmer_name, u.phone as farmer_phone
        FROM produce_records p
        LEFT JOIN users u ON p.farmer_id = u.id
        WHERE p.officer_id = ? OR (LOWER(p.area) = LOWER(?) AND LOWER(p.district) = LOWER(?))
        ORDER BY p.id DESC
    """, (user["id"], area, district))
    records = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return records

@router.post("/produce")
async def add_produce(req: ProduceCreate, user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    # When an officer submits, status is directly 'VERIFIED' and source_type is 'OFFICER_ENTRY'
    cursor.execute("""
        INSERT INTO produce_records (
            crop_name, quantity, unit, area, village, district, state,
            produce_type, quality, availability_date, expected_harvest_date,
            source_type, officer_id, verification_status, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'OFFICER_ENTRY', ?, 'VERIFIED', ?)
    """, (
        req.crop_name.strip(),
        req.quantity,
        req.unit.strip(),
        req.area.strip(),
        req.village.strip() if req.village else "",
        req.district.strip(),
        req.state.strip(),
        req.produce_type.strip() if req.produce_type else "Field Crop",
        req.quality.strip() if req.quality else "Grade A",
        req.availability_date.strip(),
        req.expected_harvest_date.strip() if req.expected_harvest_date else None,
        user["id"],
        req.notes.strip() if req.notes else ""
    ))
    new_id = cursor.lastrowid
    conn.commit()

    cursor.execute("SELECT * FROM produce_records WHERE id = ?", (new_id,))
    new_record = dict(cursor.fetchone())
    conn.close()

    # Broadcast real-time update
    await ws_manager.broadcast({
        "type": "PRODUCE_ADDED",
        "record": new_record
    })

    return {"status": "success", "produce": new_record}

@router.put("/produce/{id}")
async def update_produce(id: int, req: ProduceUpdate, user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produce_records WHERE id = ?", (id,))
    existing = cursor.fetchone()
    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Produce record not found")

    new_qty = req.quantity if req.quantity is not None else existing["quantity"]
    new_unit = req.unit if req.unit is not None else existing["unit"]
    new_quality = req.quality if req.quality is not None else existing["quality"]
    new_avail = req.availability_date if req.availability_date is not None else existing["availability_date"]
    new_status = req.verification_status if req.verification_status is not None else existing["verification_status"]
    new_notes = req.notes if req.notes is not None else existing["notes"]

    cursor.execute("""
        UPDATE produce_records
        SET quantity = ?, unit = ?, quality = ?, availability_date = ?, verification_status = ?, notes = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (new_qty, new_unit, new_quality, new_avail, new_status, new_notes, id))
    conn.commit()

    cursor.execute("SELECT * FROM produce_records WHERE id = ?", (id,))
    updated_record = dict(cursor.fetchone())
    conn.close()

    await ws_manager.broadcast({
        "type": "PRODUCE_UPDATED",
        "record": updated_record
    })

    return {"status": "success", "produce": updated_record}

@router.delete("/produce/{id}")
async def delete_produce(id: int, user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produce_records WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    await ws_manager.broadcast({
        "type": "PRODUCE_DELETED",
        "produce_id": id
    })

    return {"status": "success", "message": "Produce record deleted"}

@router.post("/produce/{id}/toggle-status")
async def toggle_produce_status(id: int, user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT verification_status FROM produce_records WHERE id = ?", (id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Produce record not found")
    
    current_status = row["verification_status"]
    new_status = "UNAVAILABLE" if current_status == "VERIFIED" else "VERIFIED"
    cursor.execute("UPDATE produce_records SET verification_status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (new_status, id))
    conn.commit()

    cursor.execute("SELECT * FROM produce_records WHERE id = ?", (id,))
    updated = dict(cursor.fetchone())
    conn.close()

    await ws_manager.broadcast({
        "type": "PRODUCE_UPDATED",
        "record": updated
    })

    return {"status": "success", "produce": updated}

@router.get("/requests")
async def get_farmer_requests(user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT assigned_area, district, state FROM officer_profiles WHERE user_id = ?", (user["id"],))
    prof = cursor.fetchone()
    area = prof["assigned_area"] if prof else "Sankari"
    district = prof["district"] if prof else "Salem"
    state = prof["state"] if prof else "Tamil Nadu"

    # Location-based matching: requests matching assigned_area + district + state or assigned to this officer
    cursor.execute("""
        SELECT r.*, u.name as farmer_name, u.phone as farmer_phone, u.email as farmer_email,
               fp.land_area, fp.land_unit, fp.farming_type
        FROM verification_requests r
        JOIN users u ON r.farmer_id = u.id
        LEFT JOIN farmer_profiles fp ON u.id = fp.user_id
        WHERE (r.officer_id = ? OR (LOWER(r.area) = LOWER(?) AND LOWER(r.district) = LOWER(?) AND LOWER(r.state) = LOWER(?)))
        ORDER BY CASE WHEN r.status = 'PENDING' THEN 0 ELSE 1 END, r.id DESC
    """, (user["id"], area, district, state))
    requests = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return requests

@router.post("/requests/{id}/verify")
async def verify_farmer_request(id: int, action_data: VerificationAction, user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM verification_requests WHERE id = ?", (id,))
    req_row = cursor.fetchone()
    if not req_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Verification request not found")

    # Update request status
    cursor.execute("""
        UPDATE verification_requests
        SET status = 'VERIFIED', officer_id = ?, officer_comment = ?, reviewed_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (user["id"], action_data.comment or "Verified by local Agriculture Officer upon field verification.", id))

    # Update or insert associated produce record as VERIFIED so it is discoverable publicly
    produce_id = req_row["produce_id"]
    if produce_id:
        cursor.execute("""
            UPDATE produce_records
            SET verification_status = 'VERIFIED',
                source_type = 'FARMER_VERIFIED',
                officer_id = ?,
                quantity = ?,
                unit = ?,
                availability_date = ?,
                notes = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (
            user["id"],
            req_row["expected_quantity"],
            req_row["quantity_unit"],
            req_row["expected_harvest_date"],
            f"Verified farmer harvest: {req_row['notes'] or ''}",
            produce_id
        ))
    else:
        cursor.execute("""
            INSERT INTO produce_records (
                crop_name, quantity, unit, area, village, district, state,
                produce_type, quality, availability_date, expected_harvest_date,
                source_type, farmer_id, officer_id, verification_status, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, 'Field Crop', ?, ?, ?, 'FARMER_VERIFIED', ?, ?, 'VERIFIED', ?)
        """, (
            req_row["crop_name"],
            req_row["expected_quantity"],
            req_row["quantity_unit"],
            req_row["area"],
            req_row["village"],
            req_row["district"],
            req_row["state"],
            req_row["quality"],
            req_row["expected_harvest_date"],
            req_row["expected_harvest_date"],
            req_row["farmer_id"],
            user["id"],
            f"Verified farmer submission: {req_row['notes'] or ''}"
        ))
        produce_id = cursor.lastrowid
        cursor.execute("UPDATE verification_requests SET produce_id = ? WHERE id = ?", (produce_id, id))

    conn.commit()

    cursor.execute("SELECT * FROM verification_requests WHERE id = ?", (id,))
    updated_req = dict(cursor.fetchone())
    cursor.execute("SELECT * FROM produce_records WHERE id = ?", (produce_id,))
    verified_produce = dict(cursor.fetchone())
    conn.close()

    # Broadcast real-time notifications
    await ws_manager.broadcast({
        "type": "REQUEST_VERIFIED",
        "request": updated_req,
        "produce": verified_produce
    })

    return {
        "status": "success",
        "message": "Farmer request successfully verified and produce published to public discovery",
        "request": updated_req,
        "produce": verified_produce
    }

@router.post("/requests/{id}/reject")
async def reject_farmer_request(id: int, action_data: VerificationAction, user: Dict[str, Any] = Depends(require_officer)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM verification_requests WHERE id = ?", (id,))
    req_row = cursor.fetchone()
    if not req_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Verification request not found")

    reason = action_data.comment.strip() if action_data.comment else "Crop details could not be verified in field inspection."

    cursor.execute("""
        UPDATE verification_requests
        SET status = 'REJECTED', officer_id = ?, officer_comment = ?, reviewed_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (user["id"], reason, id))

    produce_id = req_row["produce_id"]
    if produce_id:
        cursor.execute("""
            UPDATE produce_records
            SET verification_status = 'REJECTED', updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (produce_id,))

    conn.commit()

    cursor.execute("SELECT * FROM verification_requests WHERE id = ?", (id,))
    updated_req = dict(cursor.fetchone())
    conn.close()

    await ws_manager.broadcast({
        "type": "REQUEST_REJECTED",
        "request": updated_req
    })

    return {
        "status": "success",
        "message": "Farmer request rejected with reason provided",
        "request": updated_req
    }
