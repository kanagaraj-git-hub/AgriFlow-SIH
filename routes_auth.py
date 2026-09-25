import secrets
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from typing import Dict, Any, Optional
from database import get_db_connection
from auth import hash_password, verify_password, create_session, delete_session, get_current_user
from models import (
    UserRegister, UserLogin,
    OfficerVerifyRequest, OfficerVerifyOtpRequest,
    OfficerResendOtpRequest, OfficerCreateAccountRequest
)
from seed_data import seed_database
from ws_manager import ws_manager

router = APIRouter(prefix="/api/auth", tags=["Auth"])

def mask_phone(phone: str) -> str:
    if not phone or len(phone) < 4:
        return "******"
    return "******" + phone[-4:]

# =====================================================================
# AGRICULTURE OFFICER VERIFICATION & REGISTRATION FLOW (Sections 1-7, 10, 16)
# =====================================================================

@router.post("/officer/verify-id")
async def verify_officer_id(req: OfficerVerifyRequest):
    """
    Step 1: Verify Officer ID against AgriFlow Demo Agriculture Officer Registry.
    If valid and unregistered, generate a 6-digit Demo OTP.
    """
    officer_id = req.officer_id.strip().upper() if req.officer_id else ""
    if not officer_id:
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid registered Agriculture Officer ID."
        )

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Search mock Agriculture Officer Registry
    cursor.execute("SELECT * FROM officer_registry WHERE UPPER(officer_id) = ?", (officer_id,))
    officer = cursor.fetchone()
    if not officer:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Officer ID not found. Please enter a valid Agriculture Officer ID."
        )

    # 2. Check if officer account already exists
    cursor.execute("SELECT id FROM officer_accounts WHERE UPPER(officer_id) = ?", (officer_id,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(
            status_code=409,
            detail="An AgriFlow account has already been created for this Officer ID. Please use Officer Login."
        )

    # Check if registered in users table as well
    cursor.execute("SELECT id FROM users WHERE UPPER(COALESCE(officer_id, '')) = ?", (officer_id,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(
            status_code=409,
            detail="An AgriFlow account has already been created for this Officer ID. Please use Officer Login."
        )

    # 3. Generate 6-digit Demo OTP (expires in 5 minutes)
    otp_code = f"{secrets.randbelow(900000) + 100000:06d}"
    cursor.execute("""
    INSERT INTO otp_verifications (officer_id, otp_code, expires_at, attempts, verified)
    VALUES (?, ?, datetime('now', '+5 minutes'), 0, 0)
    """, (officer["officer_id"], otp_code))
    conn.commit()
    conn.close()

    masked = mask_phone(officer["mobile"])
    print(f"\n=======================================================")
    print(f"[AgriFlow Prototype] DEMO OTP FOR OFFICER {officer['officer_id']}: {otp_code}")
    print(f"Officer: {officer['full_name']} | Registered Mobile: {masked}")
    print(f"=======================================================\n")

    return {
        "status": "success",
        "officer_id": officer["officer_id"],
        "masked_mobile": masked,
        "message": f"OTP sent to registered mobile number {masked}",
        "demo_otp": otp_code,
        "expires_in_seconds": 300,
        "prototype_label": "Demo OTP — Prototype Only"
    }

@router.post("/officer/verify-otp")
async def verify_officer_otp(req: OfficerVerifyOtpRequest):
    """
    Step 2: Verify the 6-digit Demo OTP.
    Upon success, return verified read-only registry details and verification token.
    """
    officer_id = req.officer_id.strip().upper() if req.officer_id else ""
    otp_entered = req.otp.strip() if req.otp else ""

    if not officer_id or not otp_entered:
        raise HTTPException(status_code=400, detail="Officer ID and OTP are required.")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Find latest unverified OTP record for this officer
    cursor.execute("""
    SELECT id, otp_code, expires_at, attempts, verified,
           (datetime('now') > datetime(expires_at)) as is_expired
    FROM otp_verifications
    WHERE UPPER(officer_id) = ? AND verified = 0
    ORDER BY id DESC LIMIT 1
    """, (officer_id,))
    record = cursor.fetchone()

    if not record:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="No active OTP found. Please verify your Officer ID first."
        )

    if record["is_expired"]:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="OTP has expired. Please request a new OTP."
        )

    if record["attempts"] >= 5:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Maximum verification attempts exceeded. Please request a new OTP."
        )

    # Check OTP code
    if record["otp_code"] != otp_entered:
        new_attempts = record["attempts"] + 1
        cursor.execute("UPDATE otp_verifications SET attempts = ? WHERE id = ?", (new_attempts, record["id"]))
        conn.commit()
        conn.close()
        attempts_left = max(0, 5 - new_attempts)
        raise HTTPException(
            status_code=400,
            detail=f"Invalid OTP code. {attempts_left} attempts remaining."
        )

    # OTP is valid! Mark verified and generate verification token
    verification_token = secrets.token_urlsafe(32)
    cursor.execute("""
    UPDATE otp_verifications
    SET verified = 1, verification_token = ?
    WHERE id = ?
    """, (verification_token, record["id"]))

    # Fetch official registry record
    cursor.execute("SELECT * FROM officer_registry WHERE UPPER(officer_id) = ?", (officer_id,))
    officer = cursor.fetchone()
    conn.commit()
    conn.close()

    if not officer:
        raise HTTPException(status_code=404, detail="Officer record not found in registry.")

    return {
        "status": "success",
        "verification_token": verification_token,
        "officer": {
            "officer_id": officer["officer_id"],
            "full_name": officer["full_name"],
            "name": officer["full_name"],
            "designation": officer["designation"],
            "department": officer["department"],
            "state": officer["state"],
            "district": officer["district"],
            "working_place": officer["working_place"],
            "assigned_area": officer["working_place"],
            "masked_mobile": mask_phone(officer["mobile"])
        }
    }

@router.post("/officer/resend-otp")
async def resend_officer_otp(req: OfficerResendOtpRequest):
    """
    Resend OTP to the registered mobile number in prototype demo mode.
    """
    officer_id = req.officer_id.strip().upper() if req.officer_id else ""
    if not officer_id:
        raise HTTPException(status_code=400, detail="Officer ID is required.")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM officer_registry WHERE UPPER(officer_id) = ?", (officer_id,))
    officer = cursor.fetchone()
    if not officer:
        conn.close()
        raise HTTPException(status_code=404, detail="Invalid Officer ID.")

    cursor.execute("SELECT id FROM officer_accounts WHERE UPPER(officer_id) = ?", (officer_id,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=409, detail="Officer account already exists. Please login.")

    # Invalidate previous unverified OTPs
    cursor.execute("UPDATE otp_verifications SET verified = -1 WHERE UPPER(officer_id) = ? AND verified = 0", (officer_id,))

    # Generate new OTP
    otp_code = f"{secrets.randbelow(900000) + 100000:06d}"
    cursor.execute("""
    INSERT INTO otp_verifications (officer_id, otp_code, expires_at, attempts, verified)
    VALUES (?, ?, datetime('now', '+5 minutes'), 0, 0)
    """, (officer["officer_id"], otp_code))
    conn.commit()
    conn.close()

    masked = mask_phone(officer["mobile"])
    print(f"\n[AgriFlow Prototype] RESENT DEMO OTP FOR OFFICER {officer['officer_id']}: {otp_code}\n")

    return {
        "status": "success",
        "officer_id": officer["officer_id"],
        "masked_mobile": masked,
        "message": f"OTP resent to registered mobile number {masked}",
        "demo_otp": otp_code,
        "expires_in_seconds": 300,
        "prototype_label": "Demo OTP — Prototype Only"
    }

@router.post("/officer/create-account")
async def create_officer_account(req: OfficerCreateAccountRequest):
    """
    Step 4: Create login credentials after identity and OTP verification.
    Prevents duplicate registration and binds official registry details immutably.
    """
    officer_id = req.officer_id.strip().upper() if req.officer_id else ""
    login_id = req.login_id.strip() if req.login_id else ""
    pw = req.password
    cpw = req.confirm_password
    token = req.verification_token.strip() if req.verification_token else ""

    if not officer_id or not login_id or not pw or not cpw or not token:
        raise HTTPException(status_code=400, detail="All fields are required.")

    if pw != cpw:
        raise HTTPException(status_code=400, detail="Passwords do not match.")

    if len(pw) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters long.")

    if len(login_id) < 3:
        raise HTTPException(status_code=400, detail="Login ID must be at least 3 characters long.")

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Verify token
    cursor.execute("""
    SELECT id FROM otp_verifications
    WHERE UPPER(officer_id) = ? AND verification_token = ? AND verified = 1
      AND datetime('now') <= datetime(created_at, '+15 minutes')
    ORDER BY id DESC LIMIT 1
    """, (officer_id, token))
    otp_row = cursor.fetchone()
    if not otp_row:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired verification session. Please verify your Officer ID and OTP again."
        )

    # 2. Check duplicate officer account
    cursor.execute("SELECT id FROM officer_accounts WHERE UPPER(officer_id) = ?", (officer_id,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(
            status_code=409,
            detail="An AgriFlow account has already been created for this Officer ID. Please use the Officer Login."
        )

    # 3. Check login_id uniqueness
    cursor.execute("SELECT id FROM officer_accounts WHERE LOWER(login_id) = LOWER(?)", (login_id,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Login ID is already taken. Please choose another Login ID.")

    cursor.execute("""
    SELECT id FROM users
    WHERE LOWER(phone) = LOWER(?) OR LOWER(COALESCE(login_id, '')) = LOWER(?)
    """, (login_id, login_id))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Login ID is already taken. Please choose another Login ID.")

    # 4. Fetch officer official data
    cursor.execute("SELECT * FROM officer_registry WHERE UPPER(officer_id) = ?", (officer_id,))
    officer = cursor.fetchone()
    if not officer:
        conn.close()
        raise HTTPException(status_code=404, detail="Officer registry record not found.")

    pw_hash = hash_password(pw)

    # 5. Insert user record
    cursor.execute("""
    INSERT INTO users (role, name, email, phone, officer_id, login_id, password_hash)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        "OFFICER",
        officer["full_name"],
        None,
        officer["mobile"],
        officer["officer_id"],
        login_id,
        pw_hash
    ))
    user_id = cursor.lastrowid

    # 6. Insert officer profile
    cursor.execute("""
    INSERT INTO officer_profiles (user_id, officer_id, designation, department, assigned_area, district, state, contact)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        officer["officer_id"],
        officer["designation"],
        officer["department"],
        officer["working_place"],
        officer["district"],
        officer["state"],
        officer["mobile"]
    ))

    # 7. Insert officer account
    cursor.execute("""
    INSERT INTO officer_accounts (officer_id, login_id, password_hash, user_id)
    VALUES (?, ?, ?, ?)
    """, (
        officer["officer_id"],
        login_id,
        pw_hash,
        user_id
    ))

    # Mark mock officer record as Registered in backend
    cursor.execute("UPDATE officer_registry SET status = 'REGISTERED' WHERE UPPER(officer_id) = ?", (officer["officer_id"],))

    # 8. Invalidate verification token so it cannot be reused
    cursor.execute("UPDATE otp_verifications SET verification_token = NULL WHERE id = ?", (otp_row["id"],))

    conn.commit()
    conn.close()

    session_token = create_session(user_id, "OFFICER")

    return {
        "status": "success",
        "message": "Officer account created successfully",
        "token": session_token,
        "user": {
            "id": user_id,
            "role": "OFFICER",
            "name": officer["full_name"],
            "phone": officer["mobile"],
            "officer_id": officer["officer_id"],
            "login_id": login_id
        }
    }

# =====================================================================
# FARMER REGISTRATION (PRESERVED)
# =====================================================================

@router.post("/register")
async def register(req: UserRegister):
    # Reject direct registration if someone tries to claim OFFICER role
    if req.role.upper() == "OFFICER":
        raise HTTPException(
            status_code=400,
            detail="Agriculture Officers must register via Officer ID Verification."
        )

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

# =====================================================================
# LOGIN & SESSIONS
# =====================================================================

@router.post("/login")
async def login(req: UserLogin):
    conn = get_db_connection()
    cursor = conn.cursor()

    identifier = req.identifier.strip()
    query = """
        SELECT u.*, a.officer_id as acc_officer_id, a.login_id as acc_login_id
        FROM users u
        LEFT JOIN officer_accounts a ON u.id = a.user_id
        WHERE LOWER(u.phone) = LOWER(?)
           OR LOWER(COALESCE(u.email, '')) = LOWER(?)
           OR LOWER(COALESCE(u.officer_id, '')) = LOWER(?)
           OR LOWER(COALESCE(u.login_id, '')) = LOWER(?)
           OR LOWER(COALESCE(a.officer_id, '')) = LOWER(?)
           OR LOWER(COALESCE(a.login_id, '')) = LOWER(?)
    """
    cursor.execute(query, (identifier, identifier, identifier, identifier, identifier, identifier))
    users = cursor.fetchall()
    conn.close()

    if not users:
        raise HTTPException(status_code=400, detail="Invalid credentials. Mobile, email, or Officer ID not found.")

    matched_user = None
    for u in users:
        if req.role and u["role"] != req.role.upper():
            continue
        if verify_password(req.password, u["password_hash"]):
            matched_user = u
            break

    if not matched_user:
        raise HTTPException(status_code=400, detail="Invalid password or role selection mismatch.")

    # Update last_login if officer
    if matched_user["role"] == "OFFICER":
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE officer_accounts SET last_login = CURRENT_TIMESTAMP WHERE user_id = ?", (matched_user["id"],))
        conn.commit()
        conn.close()

    token = create_session(matched_user["id"], matched_user["role"])
    return {
        "token": token,
        "user": {
            "id": matched_user["id"],
            "role": matched_user["role"],
            "name": matched_user["name"],
            "phone": matched_user["phone"],
            "email": matched_user["email"],
            "officer_id": matched_user["officer_id"] or matched_user["acc_officer_id"],
            "login_id": matched_user["login_id"] or matched_user["acc_login_id"]
        }
    }

@router.post("/demo-login")
async def demo_login(data: Dict[str, str]):
    role = data.get("role", "OFFICER").upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    if role == "OFFICER":
        cursor.execute("""
            SELECT u.*, a.officer_id as acc_officer_id, a.login_id as acc_login_id
            FROM users u
            LEFT JOIN officer_accounts a ON u.id = a.user_id
            WHERE u.role = 'OFFICER'
            ORDER BY u.id ASC LIMIT 1
        """)
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
            cursor.execute("""
                SELECT u.*, a.officer_id as acc_officer_id, a.login_id as acc_login_id
                FROM users u
                LEFT JOIN officer_accounts a ON u.id = a.user_id
                WHERE u.role = 'OFFICER' LIMIT 1
            """)
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
            "email": user["email"],
            "officer_id": user["officer_id"] if "officer_id" in user.keys() else None,
            "login_id": user["login_id"] if "login_id" in user.keys() else None
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
            profile_data["is_verified_officer"] = True
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
