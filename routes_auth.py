from fastapi import APIRouter, HTTPException, Depends, status
from typing import Dict, Any, Optional
from database import get_db_connection
from auth import hash_password, verify_password, create_session, delete_session, get_current_user
from models import UserRegister, UserLogin
from seed_data import seed_database
from ws_manager import ws_manager

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/register")
async def register(req: UserRegister):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if phone or email already exists
    cursor.execute("SELECT id FROM users WHERE phone = ?", (req.phone.strip(),))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Mobile number is already registered")

    if req.email and req.email.strip():
        cursor.execute("SELECT id FROM users WHERE email = ?", (req.email.strip(),))
        if cursor.fetchone():
            conn.close()
            raise HTTPException(status_code=400, detail="Email is already registered")

    pw_hash = hash_password(req.password)
    cursor.execute("""
    INSERT INTO users (role, name, email, phone, password_hash)
    VALUES (?, ?, ?, ?, ?)
    """, (req.role.upper(), req.name.strip(), req.email.strip() if req.email and req.email.strip() else None, req.phone.strip(), pw_hash))
    user_id = cursor.lastrowid

    # Create role profile
    if req.role.upper() == "OFFICER":
        cursor.execute("""
        INSERT INTO officer_profiles (user_id, designation, department, assigned_area, district, state, contact)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            req.designation or "Agricultural Officer",
            req.department or "Department of Agriculture",
            req.assigned_area or "Sankari",
            req.district or "Salem",
            req.state or "Tamil Nadu",
            req.phone
        ))
    else:
        cursor.execute("""
        INSERT INTO farmer_profiles (user_id, village, area, district, state, land_area, land_unit, farming_type)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            req.village or "Sankari West",
            req.area or "Sankari",
            req.district or "Salem",
            req.state or "Tamil Nadu",
            req.land_area or 1.0,
            req.land_unit or "Acres",
            req.farming_type or "Conventional"
        ))

    conn.commit()
    conn.close()

    token = create_session(user_id, req.role.upper())
    return {
        "token": token,
        "user": {
            "id": user_id,
            "role": req.role.upper(),
            "name": req.name.strip(),
            "phone": req.phone.strip(),
            "email": req.email.strip() if req.email else None
        }
    }

@router.post("/login")
async def login(req: UserLogin):
    conn = get_db_connection()
    cursor = conn.cursor()

    identifier = req.identifier.strip()
    query = "SELECT * FROM users WHERE phone = ? OR email = ?"
    cursor.execute(query, (identifier, identifier))
    users = cursor.fetchall()
    conn.close()

    if not users:
        raise HTTPException(status_code=400, detail="Invalid credentials. Mobile or email not found.")

    matched_user = None
    for u in users:
        if req.role and u["role"] != req.role.upper():
            continue
        if verify_password(req.password, u["password_hash"]):
            matched_user = u
            break

    if not matched_user:
        raise HTTPException(status_code=400, detail="Invalid password or role selection mismatch.")

    token = create_session(matched_user["id"], matched_user["role"])
    return {
        "token": token,
        "user": {
            "id": matched_user["id"],
            "role": matched_user["role"],
            "name": matched_user["name"],
            "phone": matched_user["phone"],
            "email": matched_user["email"]
        }
    }

@router.post("/demo-login")
async def demo_login(data: Dict[str, str]):
    role = data.get("role", "OFFICER").upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    if role == "OFFICER":
        cursor.execute("SELECT * FROM users WHERE role = 'OFFICER' AND phone = '9876543210' LIMIT 1")
    else:
        cursor.execute("SELECT * FROM users WHERE role = 'FARMER' AND phone = '9123456780' LIMIT 1")
    
    user = cursor.fetchone()
    conn.close()

    if not user:
        # If demo users not found, reseed database automatically
        seed_database(clean=False)
        conn = get_db_connection()
        cursor = conn.cursor()
        if role == "OFFICER":
            cursor.execute("SELECT * FROM users WHERE role = 'OFFICER' LIMIT 1")
        else:
            cursor.execute("SELECT * FROM users WHERE role = 'FARMER' LIMIT 1")
        user = cursor.fetchone()
        conn.close()

    token = create_session(user["id"], user["role"])
    return {
        "token": token,
        "user": {
            "id": user["id"],
            "role": user["role"],
            "name": user["name"],
            "phone": user["phone"],
            "email": user["email"]
        }
    }

@router.get("/me")
async def get_current_user_profile(user: Dict[str, Any] = Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    profile_data = {}
    if user["role"] == "OFFICER":
        cursor.execute("SELECT * FROM officer_profiles WHERE user_id = ?", (user["id"],))
        p = cursor.fetchone()
        if p:
            profile_data = dict(p)
    else:
        cursor.execute("SELECT * FROM farmer_profiles WHERE user_id = ?", (user["id"],))
        p = cursor.fetchone()
        if p:
            profile_data = dict(p)

    conn.close()
    return {
        "user": user,
        "profile": profile_data
    }

@router.post("/logout")
async def logout(user: Dict[str, Any] = Depends(get_current_user)):
    delete_session(user["token"])
    return {"message": "Logged out successfully"}

@router.post("/reset-demo")
async def reset_demo_data():
    seed_database(clean=True)
    await ws_manager.broadcast({"type": "DEMO_RESET", "message": "Demo data reset to initial state"})
    return {"status": "success", "message": "Demo data reset successfully"}
