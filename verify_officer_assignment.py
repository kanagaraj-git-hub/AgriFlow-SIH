import urllib.request
import json
import sqlite3
import os

BASE_URL = "http://127.0.0.1:8000"
DB_PATH = os.path.join(os.path.dirname(__file__), "agriflow.db")

def req(path, method="GET", data=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    encoded = json.dumps(data).encode("utf-8") if data else None
    r = urllib.request.Request(f"{BASE_URL}{path}", data=encoded, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.getcode(), json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return e.code, json.loads(body) if body else {}

def validate_all():
    print("=================================================================")
    print("VERIFICATION OF 10-STEP AGRICULTURE OFFICER CONSISTENCY FLOW")
    print("=================================================================")

    # Reset seed data first
    code, r = req("/api/auth/reset-demo", "POST")
    assert code == 200, f"Reset demo failed: {r}"
    print("[INIT] Demo database reset and seeded successfully.")

    # 1. Login as farmer
    code, res = req("/api/auth/login", "POST", {
        "identifier": "9123456780",
        "password": "farmer123",
        "role": "FARMER"
    })
    assert code == 200, f"Farmer login failed: {res}"
    farmer_token = res["token"]
    print("[PASS] 1. Farmer login successful (Kumar: 9123456780).")

    # 2. Confirm farmer's location is Sankari, Salem, Tamil Nadu
    code, dash = req("/api/farmer/dashboard", "GET", token=farmer_token)
    assert code == 200
    loc = dash["location"]
    print(f"[PASS] 2. Farmer location confirmed: {loc['area']}, {loc['district']}, {loc['state']}")
    assert loc["area"] == "Sankari"
    assert loc["district"] == "Salem"
    assert loc["state"] == "Tamil Nadu"

    # 3. Confirm assigned officer is Ravi Kumar (Agriculture Officer, Sankari, Salem, Tamil Nadu)
    officer = dash["assigned_officer"]
    assert officer is not None, "No officer assigned!"
    print(f"[PASS] 3. Farmer Dashboard Assigned Officer: {officer['name']} ({officer['designation']})")
    print(f"     Jurisdiction: {officer['assigned_area']}, {officer['district']}, {officer['state']} | Contact: {officer['phone']}")
    assert officer["name"] == "Ravi Kumar"
    assert officer["designation"] == "Agriculture Officer"
    assert officer["assigned_area"] == "Sankari"
    assert officer["district"] == "Salem"
    assert officer["state"] == "Tamil Nadu"
    assert officer["phone"] == "9876543210"

    # 4. Submit a crop
    crop_payload = {
        "crop_name": "Turmeric",
        "cultivated_area": 1.5,
        "cultivated_area_unit": "Acres",
        "expected_quantity": 3.0,
        "quantity_unit": "Tons",
        "expected_harvest_date": "2026-10-15",
        "crop_stage": "Flowering",
        "quality": "Grade A",
        "village": "Sankari West",
        "area": "Sankari",
        "district": "Salem",
        "state": "Tamil Nadu",
        "notes": "Organic Salem Turmeric crop"
    }
    code, crop_res = req("/api/farmer/crops", "POST", crop_payload, token=farmer_token)
    assert code == 200, f"Crop submission failed: {crop_res}"
    request_id = crop_res["request"]["id"]
    produce_id = crop_res["request"]["produce_id"]
    print(f"[PASS] 4. Crop submitted! Request ID: {request_id}, Produce ID: {produce_id}")

    # 5. Login as Ravi Kumar
    code, off_res = req("/api/auth/login", "POST", {
        "identifier": "AGRI-TN-0001",
        "password": "officer123",
        "role": "OFFICER"
    })
    assert code == 200, f"Ravi Kumar login failed: {off_res}"
    assert off_res["user"]["name"] == "Ravi Kumar"
    officer_token = off_res["token"]
    print(f"[PASS] 5. Logged in as Ravi Kumar ({off_res['user']['officer_id']}).")

    # Confirm Officer Dashboard shows Ravi Kumar and Sankari, Salem, Tamil Nadu
    code, off_dash = req("/api/officer/dashboard", "GET", token=officer_token)
    assert code == 200
    j = off_dash["jurisdiction"]
    print(f"     Officer Dashboard Jurisdiction: {j['area']}, {j['district']}, {j['state']}")
    assert j["area"] == "Sankari"
    assert j["district"] == "Salem"
    assert j["state"] == "Tamil Nadu"

    # 6. Confirm the farmer request appears in Ravi Kumar's verification queue
    code, queue = req("/api/officer/requests", "GET", token=officer_token)
    assert code == 200
    matching = [r for r in queue if r["id"] == request_id]
    assert len(matching) == 1, f"Request {request_id} not found in Ravi Kumar's queue!"
    print(f"[PASS] 6. Pending request #{request_id} ({matching[0]['crop_name']}) found in Ravi Kumar's queue.")

    # 7. Verify the crop
    code, v_res = req(
        f"/api/officer/requests/{request_id}/verify",
        "POST",
        {"action": "VERIFY", "comment": "Field inspected and verified by Agriculture Officer Ravi Kumar."},
        token=officer_token
    )
    assert code == 200, f"Verification failed: {v_res}"
    print(f"[PASS] 7. Crop request #{request_id} verified by Ravi Kumar.")

    # 8. Open View Produce
    code, all_produce = req("/api/public/produce", "GET")
    assert code == 200
    print(f"[PASS] 8. View Produce list retrieved ({len(all_produce)} total items).")

    # 9. Confirm the produce shows the correct verification source and officer
    code, prod = req(f"/api/public/produce/{produce_id}", "GET")
    assert code == 200, f"Produce record not found: {prod}"
    print(f"[PASS] 9. Produce verified details:")
    print(f"     Crop: {prod['crop_name']} ({prod['quantity']} {prod['unit']})")
    print(f"     Verifying Officer: {prod.get('officer_name')} ({prod.get('officer_designation')})")
    print(f"     Source Display: {prod.get('source_display')}")
    assert prod["officer_name"] == "Ravi Kumar"
    assert prod["officer_designation"] == "Agriculture Officer"

    # 10. Ensure there is NO Priya Devi assignment for Sankari
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT u.name, op.assigned_area, op.district, op.state
        FROM officer_profiles op
        JOIN users u ON op.user_id = u.id
        WHERE LOWER(u.name) LIKE '%priya%' AND LOWER(op.assigned_area) = 'sankari'
    """)
    priya_sankari = c.fetchall()
    print(f"[PASS] 10. Checking for Priya Devi assignment in Sankari: {len(priya_sankari)} found.")
    assert len(priya_sankari) == 0, f"FAIL: Found Priya Devi in Sankari: {priya_sankari}"

    # Confirm Ravi Kumar is the only officer assigned to Sankari
    c.execute("""
        SELECT u.name, op.designation, op.assigned_area, op.district, op.state
        FROM officer_profiles op
        JOIN users u ON op.user_id = u.id
        WHERE LOWER(op.assigned_area) = 'sankari'
    """)
    sankari_officers = c.fetchall()
    print(f"      Officers assigned to Sankari ({len(sankari_officers)}):")
    for off in sankari_officers:
        print(f"      - {off[0]} | {off[1]} | {off[2]}, {off[3]}, {off[4]}")
    assert len(sankari_officers) == 1, f"Expected 1 officer for Sankari, found {len(sankari_officers)}"
    assert sankari_officers[0][0] == "Ravi Kumar"
    assert sankari_officers[0][1] == "Agriculture Officer"
    conn.close()

    print("\n=================================================================")
    print(">>> ALL 10 VALIDATION STEPS SUCCEEDED 100%! <<<")
    print("=================================================================\n")

if __name__ == "__main__":
    validate_all()
