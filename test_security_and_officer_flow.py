import urllib.request
import urllib.parse
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def make_req(path, method="GET", data=None, token=None):
    url = f"{BASE_URL}{path}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    encoded = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=encoded, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.getcode(), json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"raw": body}

def run_tests():
    print("=================================================================")
    print("COMPREHENSIVE TEST: AGRICULTURE OFFICER AUTH & REGISTRY SECURITY")
    print("=================================================================")

    # Reset demo database
    status, res = make_req("/api/auth/reset-demo", method="POST")
    assert status == 200, f"Reset demo failed: {res}"
    print("[1] Database reset and seeded.")

    # 1. Invalid Officer ID
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={"officer_id": "INVALID-ID-9999"})
    assert status == 404, f"Expected 404, got {status}"
    assert res["detail"] == "Officer ID not found. Please enter a valid Agriculture Officer ID."
    print("[2] Invalid Officer ID test passed (404, 'Officer ID not found. Please enter a valid Agriculture Officer ID.')")

    # 2. Valid Available Officer ID (e.g. AGRI-TN-0003)
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={"officer_id": "AGRI-TN-0003"})
    assert status == 200, f"Expected 200, got {status}: {res}"
    assert res["officer_id"] == "AGRI-TN-0003"
    assert res["masked_mobile"] == "******3212"
    assert "demo_otp" in res
    assert res["prototype_label"] == "Demo OTP — Prototype Only"
    # Ensure it did NOT return registry list or other officers' data
    assert "officers" not in res
    assert "full_name" not in res
    otp1 = res["demo_otp"]
    print(f"[3] Valid Available Officer ID AGRI-TN-0003 verified. Demo OTP: {otp1}, Masked Mobile: {res['masked_mobile']}")

    # 3. Invalid OTP
    status, res = make_req("/api/auth/officer/verify-otp", method="POST", data={"officer_id": "AGRI-TN-0003", "otp": "999999" if otp1 != "999999" else "111111"})
    assert status == 400, f"Expected 400 for invalid OTP, got {status}"
    assert "Invalid OTP code" in res["detail"]
    print("[4] Invalid OTP test passed (400, 'Invalid OTP code')")

    # 4. Resend OTP
    status, res = make_req("/api/auth/officer/resend-otp", method="POST", data={"officer_id": "AGRI-TN-0003"})
    assert status == 200, f"Resend failed: {res}"
    otp2 = res["demo_otp"]
    print(f"[5] Resend OTP test passed. New OTP: {otp2}")

    # 4b. Expired OTP Test: Force expiration in DB
    import sqlite3
    conn = sqlite3.connect("agriflow.db")
    c = conn.cursor()
    c.execute("UPDATE otp_verifications SET expires_at = datetime('now', '-5 minutes') WHERE UPPER(officer_id) = 'AGRI-TN-0003' AND verified = 0")
    conn.commit()
    conn.close()

    status, res = make_req("/api/auth/officer/verify-otp", method="POST", data={"officer_id": "AGRI-TN-0003", "otp": otp2})
    assert status == 400, f"Expected 400 for expired OTP, got {status}"
    assert "expired" in res["detail"].lower()
    print("[5b] Expired OTP test passed (400, 'OTP has expired. Please request a new OTP.')")

    # Resend fresh OTP after expiry
    status, res = make_req("/api/auth/officer/resend-otp", method="POST", data={"officer_id": "AGRI-TN-0003"})
    assert status == 200
    otp2 = res["demo_otp"]

    # 5. Confirm Details upon Valid OTP
    status, res = make_req("/api/auth/officer/verify-otp", method="POST", data={"officer_id": "AGRI-TN-0003", "otp": otp2})
    assert status == 200, f"Valid OTP verification failed: {res}"
    token = res["verification_token"]
    officer = res["officer"]
    assert officer["officer_id"] == "AGRI-TN-0003"
    assert officer["name"] == "Senthil Nathan"
    assert officer["designation"] == "District Agriculture Officer"
    assert officer["working_place"] == "Pollachi"
    assert officer["district"] == "Coimbatore"
    assert officer["state"] == "Tamil Nadu"
    assert officer["masked_mobile"] == "******3212"
    print(f"[6] Confirm Details fetched verified official record:")
    print(f"    Name: {officer['name']}")
    print(f"    Post: {officer['designation']}")
    print(f"    Working Place: {officer['working_place']}")
    print(f"    District: {officer['district']}")
    print(f"    State: {officer['state']}")
    print(f"    Mobile: {officer['masked_mobile']}")

    # 6. Password creation validation (passwords mismatch)
    status, res = make_req("/api/auth/officer/create-account", method="POST", data={
        "officer_id": "AGRI-TN-0003",
        "verification_token": token,
        "login_id": "AGRI-TN-0003",
        "password": "mypassword1",
        "confirm_password": "mypassword2"
    })
    assert status == 400, f"Expected 400 for password mismatch, got {status}"
    assert "match" in res["detail"].lower()
    print("[7] Password mismatch validation passed (400)")

    # 7. Password creation validation (password too short)
    status, res = make_req("/api/auth/officer/create-account", method="POST", data={
        "officer_id": "AGRI-TN-0003",
        "verification_token": token,
        "login_id": "AGRI-TN-0003",
        "password": "123",
        "confirm_password": "123"
    })
    assert status == 400, f"Expected 400 for short password, got {status}"
    print("[8] Short password validation passed (400)")

    # 8. Successful Account Creation with Login ID = AGRI-TN-0003
    status, res = make_req("/api/auth/officer/create-account", method="POST", data={
        "officer_id": "AGRI-TN-0003",
        "verification_token": token,
        "login_id": "AGRI-TN-0003",
        "password": "officerpassword123",
        "confirm_password": "officerpassword123"
    })
    assert status == 200, f"Account creation failed: {res}"
    user = res["user"]
    assert user["officer_id"] == "AGRI-TN-0003"
    assert user["login_id"] == "AGRI-TN-0003"
    print(f"[9] Account creation successful for Login ID: {user['login_id']}")

    # 9. Duplicate Account Creation / Already Registered Check
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={"officer_id": "AGRI-TN-0003"})
    assert status == 409, f"Expected 409, got {status}: {res}"
    assert "Officer ID. Please use Officer Login." in res["detail"]
    print(f"[10] Already registered Officer ID blocked (409, '{res['detail']}')")

    # 10. Officer Login using Officer ID
    status, res = make_req("/api/auth/login", method="POST", data={
        "identifier": "AGRI-TN-0003",
        "password": "officerpassword123",
        "role": "OFFICER"
    })
    assert status == 200, f"Login failed: {res}"
    assert res["user"]["officer_id"] == "AGRI-TN-0003"
    officer_token = res["token"]
    print(f"[11] Officer login successful with Officer ID/Login ID AGRI-TN-0003. JWT: {officer_token[:15]}...")

    # 11. Security Check: Confirm complete registry is NOT returned by any public API
    status, res = make_req("/api/auth/officer-registry/demo-list")
    assert status == 404, f"Public registry endpoint should return 404, got {status}"
    print("[12] Security Check passed: /api/auth/officer-registry/demo-list returns 404 Not Found.")

    # 12. Security Check: Confirm frontend index.html and app.js do not contain the complete officer registry
    with open("static/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert "demo-registry-modal" not in html
    assert "View Demo Registry" not in html
    assert "AGRI-TN-0045" not in html
    print("[13] Security Check passed: static/index.html contains no officer registry list or modal.")

    with open("static/app.js", "r", encoding="utf-8") as f:
        js = f.read()
    assert "openDemoRegistryModal" not in js
    assert "demoRegistryCache" not in js
    assert "AGRI-TN-0045" not in js
    print("[14] Security Check passed: static/app.js contains no officer registry list or demo list fetch.")

    print("\n=================================================================")
    print("ALL 14 SECURITY & OFFICER FLOW VERIFICATION TESTS PASSED 100%!")
    print("=================================================================")

if __name__ == "__main__":
    run_tests()
