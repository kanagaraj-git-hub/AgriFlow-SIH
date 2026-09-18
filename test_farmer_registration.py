import urllib.request
import json
import sqlite3
import os

BASE_URL = "http://127.0.0.1:8000"
DB_PATH = os.path.join(os.path.dirname(__file__), "agriflow.db")

def make_request(path, method="GET", data=None, token=None):
    url = f"{BASE_URL}{path}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    encoded_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as resp:
            status_code = resp.getcode()
            body = resp.read().decode("utf-8")
            return status_code, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return e.code, json.loads(body) if body else {}

def test_farmer_registration():
    print("=== Testing Farmer Registration Flow End-to-End ===")
    
    # Unique test phone number to avoid collisions
    test_phone = "9842109876"
    
    # 1. Register a new farmer with all fields that the browser form submits
    farmer_payload = {
        "name": "Murugan Selvam",
        "phone": test_phone,
        "email": None,
        "password": "farmerpassword123",
        "role": "FARMER",
        "village": "Sankari South",
        "area": "Sankari",
        "district": "Salem",
        "state": "Tamil Nadu",
        "land_area": 3.5,
        "land_unit": "Acres",
        "farming_type": "Organic"
    }
    
    status, res = make_request("/api/auth/register", method="POST", data=farmer_payload)
    assert status == 200, f"Registration failed with status {status}: {res}"
    assert "token" in res, "No session token returned"
    assert res["user"]["role"] == "FARMER"
    assert res["user"]["name"] == "Murugan Selvam"
    assert res["user"]["phone"] == test_phone
    farmer_token = res["token"]
    farmer_id = res["user"]["id"]
    print(f"[PASS] 1. Farmer registered successfully. ID: {farmer_id}, Token: {farmer_token[:10]}...")

    # 2. Check /api/auth/me session verification
    status, me_res = make_request("/api/auth/me", token=farmer_token)
    assert status == 200, f"/api/auth/me failed: {me_res}"
    assert me_res["user"]["id"] == farmer_id
    assert me_res["user"]["role"] == "FARMER"
    assert me_res["profile"]["village"] == "Sankari South"
    assert me_res["profile"]["area"] == "Sankari"
    assert me_res["profile"]["district"] == "Salem"
    assert me_res["profile"]["state"] == "Tamil Nadu"
    assert me_res["profile"]["land_area"] == 3.5
    print("[PASS] 2. Farmer session validated via /api/auth/me")

    # 3. Check /api/farmer/dashboard
    status, dash_res = make_request("/api/farmer/dashboard", token=farmer_token)
    assert status == 200, f"Farmer dashboard failed: {dash_res}"
    assert dash_res["location"]["village"] == "Sankari South"
    assert dash_res["location"]["area"] == "Sankari"
    assert dash_res["stats"]["total_crops"] == 0
    # Verify the local officer was automatically matched!
    assert dash_res["assigned_officer"] is not None
    assert dash_res["assigned_officer"]["name"] == "Ravi Kumar"
    print(f"[PASS] 3. Farmer Dashboard loaded. Auto-matched AAO: {dash_res['assigned_officer']['name']} ({dash_res['assigned_officer']['designation']})")

    # 4. Check persistence in SQLite agriflow.db directly
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE id = ?", (farmer_id,))
    user_row = cursor.fetchone()
    assert user_row is not None, "User record not found in database"
    assert user_row["role"] == "FARMER"
    assert user_row["name"] == "Murugan Selvam"

    cursor.execute("SELECT * FROM farmer_profiles WHERE user_id = ?", (farmer_id,))
    profile_row = cursor.fetchone()
    assert profile_row is not None, "Farmer profile not found in database"
    assert profile_row["village"] == "Sankari South"
    assert profile_row["area"] == "Sankari"
    assert profile_row["district"] == "Salem"
    assert profile_row["state"] == "Tamil Nadu"
    assert profile_row["land_area"] == 3.5
    assert profile_row["land_unit"] == "Acres"
    assert profile_row["farming_type"] == "Organic"
    conn.close()
    print("[PASS] 4. Farmer record and profile verified directly in SQLite database")

    # 5. Verify duplicate phone error handling
    dup_status, dup_res = make_request("/api/auth/register", method="POST", data=farmer_payload)
    assert dup_status == 400, f"Expected 400 for duplicate, got {dup_status}"
    assert "already registered" in dup_res.get("detail", "")
    print("[PASS] 5. Duplicate phone registration correctly returns 400 error")

    # 6. Verify Officer login still works
    status, off_res = make_request("/api/auth/login", method="POST", data={
        "identifier": "ravi.kumar@agri.tn.gov.in",
        "password": "officer123",
        "role": "OFFICER"
    })
    assert status == 200, f"Officer login failed: {off_res}"
    assert off_res["user"]["role"] == "OFFICER"
    assert off_res["user"]["name"] == "Ravi Kumar"
    print("[PASS] 6. Agriculture Officer login still works perfectly")

    print("\n>>> ALL FARMER REGISTRATION & VERIFICATION TESTS PASSED 100%! <<<\n")

if __name__ == "__main__":
    test_farmer_registration()
