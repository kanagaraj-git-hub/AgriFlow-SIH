"""
Comprehensive Automated Test Suite for AgriFlow Forgot Password Feature.
Tests:
  - Normal login regressions (Farmer & Officer)
  - Identifier & role validation (Invalid identifier, wrong role, missing fields)
  - Rate limiting & cooldown (30s resend prevention)
  - Simulated OTP generation & demo_otp field
  - OTP verification, invalid OTP rejection, attempt count tracking, 5-attempt lockout
  - Expired OTP rejection
  - OTP reuse prevention
  - Password policy validation (weak password < 6 chars, mismatch)
  - Reset token validation, expiration, and reuse prevention
  - Password hashing & update
  - Old password invalidation
  - Login with new password for Farmer
  - Full flow for Officer (AGRI-TN-0001 and login_id/mobile)
  - Resend OTP invalidation
  - Clean DB restoration to demo state
"""

import sys
import os
from datetime import datetime, timedelta, timezone
from fastapi.testclient import TestClient

from main import app
from database import get_db_connection, init_db
from seed_data import seed_database

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

client = TestClient(app)

def reset_db():
    init_db()
    seed_database()

def test_forgot_password():
    print("=" * 70)
    print("RUNNING AGRIFLOW FORGOT PASSWORD AUTOMATED TEST SUITE")
    print("=" * 70)

    # 0. Initialize and seed DB
    reset_db()
    print("[PASS] 0. Database initialized and seeded with pristine demo data")

    # 1. Verify Normal Login for Farmer and Officer
    print("\n--- 1. Testing Existing Normal Login ---")
    resp = client.post("/api/auth/login", json={"identifier": "9123456780", "password": "farmer123", "role": "FARMER"})
    assert resp.status_code == 200, f"Farmer login failed: {resp.text}"
    farmer_token = resp.json().get("token")
    assert farmer_token, "No token returned for Farmer"
    print("  [PASS] Farmer normal login works (9123456780 / farmer123)")

    resp = client.post("/api/auth/login", json={"identifier": "AGRI-TN-0001", "password": "officer123", "role": "OFFICER"})
    assert resp.status_code == 200, f"Officer login failed: {resp.text}"
    officer_token = resp.json().get("token")
    assert officer_token, "No token returned for Officer"
    print("  [PASS] Officer normal login works (AGRI-TN-0001 / officer123)")

    # 2. Identifier & Role Validation Edge Cases
    print("\n--- 2. Identifier & Role Validation ---")
    # 2a. Invalid identifier
    resp = client.post("/api/auth/forgot-password", json={"identifier": "0000000000", "role": "FARMER"})
    assert resp.status_code == 404, f"Expected 404, got {resp.status_code}"
    print("  [PASS] Non-existent identifier rejected with 404")

    # 2b. Wrong role (Farmer phone requested with role OFFICER)
    resp = client.post("/api/auth/forgot-password", json={"identifier": "9123456780", "role": "OFFICER"})
    assert resp.status_code == 404, f"Expected 404 for wrong role, got {resp.status_code}"
    print("  [PASS] Farmer identifier with OFFICER role rejected with 404")

    # 2c. Invalid role string
    resp = client.post("/api/auth/forgot-password", json={"identifier": "9123456780", "role": "ADMIN"})
    assert resp.status_code == 400, f"Expected 400 for invalid role, got {resp.status_code}"
    print("  [PASS] Invalid role rejected with 400")

    # 3. Farmer Forgot Password Flow
    print("\n--- 3. Farmer Forgot Password & Simulated OTP ---")
    # 3a. Valid request
    resp = client.post("/api/auth/forgot-password", json={"identifier": "9123456780", "role": "FARMER"})
    assert resp.status_code == 200, f"Forgot password request failed: {resp.text}"
    data = resp.json()
    otp1 = data.get("demo_otp")
    assert otp1 and len(otp1) == 6, f"Invalid demo_otp: {otp1}"
    assert data.get("masked_identifier") == "******6780"
    assert data.get("expires_in_seconds") == 300
    print(f"  [PASS] Forgot password initiated. Demo OTP: {otp1}, Masked: {data['masked_identifier']}")

    # 3b. Rate limiting / Cooldown: immediate re-request must fail with 429
    resp = client.post("/api/auth/forgot-password", json={"identifier": "9123456780", "role": "FARMER"})
    assert resp.status_code == 429, f"Expected 429 for rapid resend, got {resp.status_code}"
    print("  [PASS] Rapid resend blocked with 429 cooldown")

    # 3c. Invalid OTP rejection
    wrong_otp = "000000" if otp1 != "000000" else "111111"
    resp = client.post("/api/auth/verify-reset-code", json={"identifier": "9123456780", "role": "FARMER", "otp_code": wrong_otp})
    assert resp.status_code == 400, f"Expected 400 for wrong OTP, got {resp.status_code}"
    assert "Invalid verification code" in resp.json().get("detail", "")
    print("  [PASS] Incorrect OTP rejected with 400 and attempt tracking")

    # 3d. Multiple invalid attempts lockout (attempt remaining: 4, 3, 2, 1 -> lockout)
    for _ in range(4):
        resp = client.post("/api/auth/verify-reset-code", json={"identifier": "9123456780", "role": "FARMER", "otp_code": wrong_otp})
    assert resp.status_code == 400
    assert "Maximum verification attempts exceeded" in resp.json().get("detail", "")
    print("  [PASS] Maximum 5 verification attempts lockout enforced")

    # 3e. Expired OTP handling
    # Clear lockout by generating a new OTP, but artificially set expires_at in DB to past
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM password_reset_tokens WHERE role = 'FARMER'")
        conn.commit()

    resp = client.post("/api/auth/forgot-password", json={"identifier": "9123456780", "role": "FARMER"})
    assert resp.status_code == 200
    otp2 = resp.json().get("demo_otp")

    # Artificially expire the token in database
    past_time = (datetime.now(timezone.utc) - timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE password_reset_tokens SET expires_at = ? WHERE otp_code = ?", (past_time, otp2))
        conn.commit()

    resp = client.post("/api/auth/verify-reset-code", json={"identifier": "9123456780", "role": "FARMER", "otp_code": otp2})
    assert resp.status_code == 400
    assert "expired" in resp.json().get("detail", "").lower()
    print("  [PASS] Expired OTP rejected with 400")

    # 3f. Request new OTP and verify successfully
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM password_reset_tokens WHERE role = 'FARMER'")
        conn.commit()

    resp = client.post("/api/auth/forgot-password", json={"identifier": "9123456780", "role": "FARMER"})
    assert resp.status_code == 200
    otp3 = resp.json().get("demo_otp")

    resp = client.post("/api/auth/verify-reset-code", json={"identifier": "9123456780", "role": "FARMER", "otp_code": otp3})
    assert resp.status_code == 200, f"Verify reset code failed: {resp.text}"
    reset_data = resp.json()
    reset_token = reset_data.get("reset_token")
    assert reset_token, "No reset_token returned after valid OTP verification"
    print(f"  [PASS] Valid OTP verified. Issued reset_token: {reset_token[:12]}...")

    # 3g. Prevent OTP reuse
    resp = client.post("/api/auth/verify-reset-code", json={"identifier": "9123456780", "role": "FARMER", "otp_code": otp3})
    assert resp.status_code == 400
    assert "already been used" in resp.json().get("detail", "")
    print("  [PASS] OTP reuse rejected")

    # 4. Password Policy & Reset Execution
    print("\n--- 4. Password Policy & Reset Validation ---")
    # 4a. Password mismatch
    resp = client.post("/api/auth/reset-password", json={
        "reset_token": reset_token,
        "new_password": "newfarmerpassword123",
        "confirm_password": "differentpassword"
    })
    assert resp.status_code == 400
    assert "Passwords do not match" in resp.json().get("detail", "")
    print("  [PASS] Password mismatch rejected")

    # 4b. Weak password (< 6 chars)
    resp = client.post("/api/auth/reset-password", json={
        "reset_token": reset_token,
        "new_password": "123",
        "confirm_password": "123"
    })
    assert resp.status_code == 400
    assert "at least 6 characters" in resp.json().get("detail", "")
    print("  [PASS] Weak password (< 6 characters) rejected")

    # 4c. Invalid reset token
    resp = client.post("/api/auth/reset-password", json={
        "reset_token": "bogus-reset-token-xyz",
        "new_password": "validPassword123",
        "confirm_password": "validPassword123"
    })
    assert resp.status_code == 400
    assert "Invalid or expired" in resp.json().get("detail", "")
    print("  [PASS] Bogus reset token rejected")

    # 4d. Successful password reset
    new_farmer_pass = "farmerResetPass2026!"
    resp = client.post("/api/auth/reset-password", json={
        "reset_token": reset_token,
        "new_password": new_farmer_pass,
        "confirm_password": new_farmer_pass
    })
    assert resp.status_code == 200, f"Reset password failed: {resp.text}"
    assert resp.json().get("message")
    print(f"  [PASS] Farmer password successfully reset to '{new_farmer_pass}'")

    # 4e. Reset token reuse prevention
    resp = client.post("/api/auth/reset-password", json={
        "reset_token": reset_token,
        "new_password": "anotherPassword123",
        "confirm_password": "anotherPassword123"
    })
    assert resp.status_code == 400
    print("  [PASS] Reset token cannot be reused")

    # 4f. Confirm old password no longer works
    resp = client.post("/api/auth/login", json={"identifier": "9123456780", "password": "farmer123", "role": "FARMER"})
    assert resp.status_code in (400, 401), f"Expected 400/401 with old password, got {resp.status_code}"
    print("  [PASS] Old password 'farmer123' is no longer accepted (400/401)")

    # 4g. Confirm new password works for login
    resp = client.post("/api/auth/login", json={"identifier": "9123456780", "password": new_farmer_pass, "role": "FARMER"})
    assert resp.status_code == 200, f"Login with new password failed: {resp.text}"
    assert resp.json().get("token")
    print("  [PASS] Login with new password succeeded! JWT access token obtained")

    # 5. Agriculture Officer Forgot Password Flow
    print("\n--- 5. Agriculture Officer Forgot Password Flow ---")
    # 5a. Officer ID AGRI-TN-0001
    resp = client.post("/api/auth/forgot-password", json={"identifier": "AGRI-TN-0001", "role": "OFFICER"})
    assert resp.status_code == 200, f"Officer forgot password failed: {resp.text}"
    off_data = resp.json()
    off_otp = off_data.get("demo_otp")
    assert off_otp and len(off_otp) == 6
    print(f"  [PASS] Officer forgot password requested for AGRI-TN-0001. Demo OTP: {off_otp}")

    # 5b. Verify Officer OTP
    resp = client.post("/api/auth/verify-reset-code", json={"identifier": "AGRI-TN-0001", "role": "OFFICER", "otp_code": off_otp})
    assert resp.status_code == 200
    off_reset_token = resp.json().get("reset_token")
    assert off_reset_token
    print("  [PASS] Officer OTP verified. Reset token issued")

    # 5c. Reset Officer Password
    new_officer_pass = "officerResetPass2026!"
    resp = client.post("/api/auth/reset-password", json={
        "reset_token": off_reset_token,
        "new_password": new_officer_pass,
        "confirm_password": new_officer_pass
    })
    assert resp.status_code == 200
    print(f"  [PASS] Officer password successfully reset to '{new_officer_pass}'")

    # 5d. Old password no longer works
    resp = client.post("/api/auth/login", json={"identifier": "AGRI-TN-0001", "password": "officer123", "role": "OFFICER"})
    assert resp.status_code in (400, 401)
    print("  [PASS] Officer old password 'officer123' rejected (400/401)")

    # 5e. New password works
    resp = client.post("/api/auth/login", json={"identifier": "AGRI-TN-0001", "password": new_officer_pass, "role": "OFFICER"})
    assert resp.status_code == 200
    assert resp.json().get("token")
    print("  [PASS] Officer login with new password succeeded! JWT access token obtained")

    # 6. Test Resend Reset Code Endpoint & Cooldown
    print("\n--- 6. Resend Reset Code Endpoint & Invalidation ---")
    # Reset cooldown in DB for testing
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM password_reset_tokens WHERE role = 'OFFICER'")
        conn.commit()

    resp = client.post("/api/auth/forgot-password", json={"identifier": "AGRI-TN-0001", "role": "OFFICER"})
    assert resp.status_code == 200
    initial_otp = resp.json().get("demo_otp")

    # Calling resend immediately should hit cooldown (429)
    resp = client.post("/api/auth/resend-reset-code", json={"identifier": "AGRI-TN-0001", "role": "OFFICER"})
    assert resp.status_code == 429
    print("  [PASS] Resend endpoint enforces 30s rate limiting")

    # Simulate 31 seconds later by modifying created_at in DB
    past_time = (datetime.now(timezone.utc) - timedelta(seconds=35)).strftime('%Y-%m-%d %H:%M:%S')
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE password_reset_tokens SET created_at = ? WHERE otp_code = ?", (past_time, initial_otp))
        conn.commit()

    resp = client.post("/api/auth/resend-reset-code", json={"identifier": "AGRI-TN-0001", "role": "OFFICER"})
    assert resp.status_code == 200
    new_otp = resp.json().get("demo_otp")
    assert new_otp != initial_otp
    print(f"  [PASS] Resend succeeded after cooldown. New OTP: {new_otp}")

    # Check that previous initial_otp is now invalidated
    resp = client.post("/api/auth/verify-reset-code", json={"identifier": "AGRI-TN-0001", "role": "OFFICER", "otp_code": initial_otp})
    assert resp.status_code == 400
    print("  [PASS] Previous OTP invalidated after resend")

    # 7. Clean up and restore demo seed data
    print("\n--- 7. Cleanup & Seed Data Restoration ---")
    reset_db()
    # Confirm demo passwords work again
    resp = client.post("/api/auth/login", json={"identifier": "9123456780", "password": "farmer123", "role": "FARMER"})
    assert resp.status_code == 200, "Demo farmer password restoration failed"
    resp = client.post("/api/auth/login", json={"identifier": "AGRI-TN-0001", "password": "officer123", "role": "OFFICER"})
    assert resp.status_code == 200, "Demo officer password restoration failed"
    print("  [PASS] Demo credentials successfully restored to original seed state")

    print("\n" + "=" * 70)
    print("ALL FORGOT PASSWORD TESTS PASSED (100% SUCCESS)!")
    print("=" * 70)

if __name__ == "__main__":
    test_forgot_password()
