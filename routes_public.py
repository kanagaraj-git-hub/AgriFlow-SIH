from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List, Dict, Any
from database import get_db_connection
from models import PurchaseRequestCreate
from ws_manager import ws_manager

router = APIRouter(prefix="/api/public", tags=["Public"])

@router.get("/produce")
async def search_produce(
    crop: Optional[str] = Query(None, description="Crop name to search"),
    state: Optional[str] = Query(None, description="State filter"),
    district: Optional[str] = Query(None, description="District filter"),
    area: Optional[str] = Query(None, description="Area/Block/Village filter"),
    min_qty: Optional[float] = Query(None, description="Minimum quantity"),
    max_qty: Optional[float] = Query(None, description="Maximum quantity"),
    availability_date: Optional[str] = Query(None, description="Availability date"),
    verified_only: bool = Query(True, description="Filter for verified produce only")
):
    conn = get_db_connection()
    cursor = conn.cursor()

    conditions = []
    params = []

    if verified_only:
        conditions.append("p.verification_status = 'VERIFIED'")
    else:
        conditions.append("p.verification_status != 'UNAVAILABLE'")

    if crop and crop.strip():
        conditions.append("LOWER(p.crop_name) LIKE LOWER(?)")
        params.append(f"%{crop.strip()}%")

    if state and state.strip() and state != "All":
        conditions.append("LOWER(p.state) = LOWER(?)")
        params.append(state.strip())

    if district and district.strip() and district != "All":
        conditions.append("LOWER(p.district) = LOWER(?)")
        params.append(district.strip())

    if area and area.strip() and area != "All":
        conditions.append("LOWER(p.area) = LOWER(?)")
        params.append(area.strip())

    if min_qty is not None:
        conditions.append("p.quantity >= ?")
        params.append(min_qty)

    if max_qty is not None:
        conditions.append("p.quantity <= ?")
        params.append(max_qty)

    if availability_date and availability_date.strip():
        conditions.append("p.availability_date <= ?")
        params.append(availability_date.strip())

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

    query = f"""
        SELECT p.*,
               u_off.name as officer_name, op.designation as officer_designation,
               u_farm.name as farmer_name
        FROM produce_records p
        LEFT JOIN users u_off ON p.officer_id = u_off.id
        LEFT JOIN officer_profiles op ON u_off.id = op.user_id
        LEFT JOIN users u_farm ON p.farmer_id = u_farm.id
        {where_clause}
        ORDER BY p.id DESC
    """

    cursor.execute(query, tuple(params))
    records = [dict(r) for r in cursor.fetchall()]
    conn.close()

    # Format source badges and clean display names
    for r in records:
        if r["source_type"] in ("officer_local", "OFFICER_ENTRY"):
            r["source_display"] = f"Agriculture Officer Verified ({r.get('officer_name') or 'Officer'})"
            r["record_type"] = "officer_local"
            r["record_type_display"] = "Local Officer Availability"
        else:
            r["source_display"] = f"Farmer Verified ({r.get('farmer_name') or 'Farmer'})"
            r["record_type"] = "farmer_verified"
            r["record_type_display"] = "Verified Farmer Produce"

    return records

@router.get("/produce/{id}")
async def get_produce_details(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT p.*,
               u_off.name as officer_name, op.designation as officer_designation, op.department as officer_department,
               u_farm.name as farmer_name, fp.farming_type, fp.land_area, fp.land_unit
        FROM produce_records p
        LEFT JOIN users u_off ON p.officer_id = u_off.id
        LEFT JOIN officer_profiles op ON u_off.id = op.user_id
        LEFT JOIN users u_farm ON p.farmer_id = u_farm.id
        LEFT JOIN farmer_profiles fp ON u_farm.id = fp.user_id
        WHERE p.id = ?
    """
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Produce record not found")

    rec = dict(row)
    if rec["source_type"] in ("officer_local", "OFFICER_ENTRY"):
        rec["source_display"] = f"Agriculture Officer Verified ({rec.get('officer_name') or 'District Officer'})"
        rec["record_type"] = "officer_local"
        rec["record_type_display"] = "Local Officer Availability"
    else:
        rec["source_display"] = f"Farmer Verified ({rec.get('farmer_name') or 'Local Farmer'})"
        rec["record_type"] = "farmer_verified"
        rec["record_type_display"] = "Verified Farmer Produce"

    return rec

@router.post("/purchase-requests")
async def create_purchase_request(req: PurchaseRequestCreate):
    """
    Submit a purchase request from a buyer for a verified farmer-listed produce item.
    Enforces security:
    1. Produce must exist.
    2. Produce source_type must be 'farmer_verified'. (officer_local is rejected)
    3. Produce must have a valid farmer_id.
    4. Destination farmer is always retrieved from database produce record, never trusted from client.
    """
    if not req.buyer_name or not req.buyer_name.strip():
        raise HTTPException(status_code=400, detail="Buyer name or company is required.")
    if not req.buyer_contact or not req.buyer_contact.strip():
        raise HTTPException(status_code=400, detail="Buyer contact information is required.")
    if req.requested_quantity <= 0:
        raise HTTPException(status_code=400, detail="Requested quantity must be greater than zero.")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, crop_name, quantity, unit, area, district, state, source_type, farmer_id, verification_status
        FROM produce_records
        WHERE id = ?
    """, (req.produce_id,))
    produce = cursor.fetchone()
    if not produce:
        conn.close()
        raise HTTPException(status_code=404, detail="Produce record not found")

    # Reject officer local produce (Requirement 3, 8, 10)
    if produce["source_type"] in ("officer_local", "OFFICER_ENTRY"):
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Purchase requests cannot be submitted for officer local records. They are only available for verified farmer-listed produce."
        )

    # Require farmer_verified with valid farmer_id (Requirement 4, 5, 10)
    if produce["source_type"] not in ("farmer_verified", "FARMER_VERIFIED") or not produce["farmer_id"]:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="This produce record is not associated with a verified farmer."
        )

    if produce["verification_status"] != "VERIFIED":
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Cannot submit purchase request for unverified produce."
        )

    farmer_id = produce["farmer_id"]

    cursor.execute("""
        INSERT INTO purchase_requests (
            produce_id, farmer_id, buyer_name, buyer_contact,
            requested_quantity, quantity_unit, message, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, 'pending')
    """, (
        req.produce_id,
        farmer_id,
        req.buyer_name.strip(),
        req.buyer_contact.strip(),
        req.requested_quantity,
        req.quantity_unit.strip() if req.quantity_unit else produce["unit"],
        req.message.strip() if req.message else ""
    ))
    req_id = cursor.lastrowid
    conn.commit()

    cursor.execute("SELECT * FROM purchase_requests WHERE id = ?", (req_id,))
    new_request = dict(cursor.fetchone())
    new_request["requested_unit"] = new_request.get("quantity_unit")
    conn.close()

    await ws_manager.broadcast({
        "type": "PURCHASE_REQUEST_RECEIVED",
        "produce_id": req.produce_id,
        "farmer_id": farmer_id,
        "crop_name": produce["crop_name"],
        "request": new_request
    })

    return {
        "status": "success",
        "message": "Purchase request sent successfully. Your request has been sent to the farmer associated with this verified produce.",
        "request": new_request
    }

@router.get("/locations")
async def get_locations():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Collect distinct states, districts, areas from produce_records and officer_profiles
    cursor.execute("""
        SELECT DISTINCT state, district, area FROM produce_records
        UNION
        SELECT DISTINCT state, district, assigned_area as area FROM officer_profiles
        ORDER BY state, district, area
    """)
    rows = cursor.fetchall()
    conn.close()

    locations: Dict[str, Dict[str, List[str]]] = {}
    for r in rows:
        st = r["state"]
        dt = r["district"]
        ar = r["area"]
        if not st: continue
        if st not in locations:
            locations[st] = {}
        if dt not in locations[st]:
            locations[st][dt] = []
        if ar and ar not in locations[st][dt]:
            locations[st][dt].append(ar)

    return locations
