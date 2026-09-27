import urllib.request
import urllib.parse
import json
import time
from database import init_db
from seed_data import seed_database

BASE_URL = "http://127.0.0.1:8000"

def make_request(path, method="GET", data=None, token=None):
    url = f"{BASE_URL}{path}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    encoded_data = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as resp:
            status_code = resp.getcode()
            body = resp.read().decode("utf-8")
            return status_code, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return e.code, json.loads(body) if body else {}

def run_tests():
    print("=== Testing AgriFlow Core System & 13-Step Demonstration Flow ===")
    
    # Step 0: Reset seed data
    status, res = make_request("/api/auth/reset-demo", method="POST")
    assert status == 200, f"Reset demo failed: {res}"
    print("[PASS] Step 0: Demo database reset and seeded successfully")

    # Step 1: Officer Verification & Registration (Ravi Kumar: AGRI-TN-0001)
    # 1a. Verify Officer ID in Demo Registry
    status, res = make_request("/api/auth/officer/verify-id", method="POST", data={
        "officer_id": "AGRI-TN-0001"
    })
    assert status == 200, f"Verify officer ID failed: {res}"
    assert res["officer_id"] == "AGRI-TN-0001"
    assert res["masked_mobile"] == "******3210"
    demo_otp = res["demo_otp"]
    print(f"[PASS] Step 1a: Officer ID AGRI-TN-0001 verified. Demo OTP: {demo_otp}")

    # 1b. Verify OTP
    status, res = make_request("/api/auth/officer/verify-otp", method="POST", data={
        "officer_id": "AGRI-TN-0001",
        "otp": demo_otp
    })
    assert status == 200, f"Verify OTP failed: {res}"
    verification_token = res["verification_token"]
    assert res["officer"]["name"] == "Ravi Kumar"
    print(f"[PASS] Step 1b: OTP verified. Details retrieved for {res['officer']['name']}")

    # 1c. Create Officer Account
    status, res = make_request("/api/auth/officer/create-account", method="POST", data={
        "officer_id": "AGRI-TN-0001",
        "verification_token": verification_token,
        "login_id": "ravi_kumar_officer",
        "password": "officer123",
        "confirm_password": "officer123"
    })
    assert status == 200, f"Create officer account failed: {res}"
    print(f"[PASS] Step 1c: Officer account created with Login ID: {res['user']['login_id']}")

    # 1d. Officer login using Officer ID / Login ID
    status, res = make_request("/api/auth/login", method="POST", data={
        "identifier": "AGRI-TN-0001",
        "password": "officer123",
        "role": "OFFICER"
    })
    assert status == 200, f"Officer login failed: {res}"
    officer_token = res["token"]
    print(f"[PASS] Step 1d: Officer Ravi Kumar logged in successfully. Token: {officer_token[:10]}...")

    # Step 2: Verify Officer profile
    status, res = make_request("/api/officer/profile", token=officer_token)
    assert status == 200, f"Get officer profile failed: {res}"
    assert res["name"] == "Ravi Kumar"
    assert res["assigned_area"] == "Sankari"
    assert res["district"] == "Salem"
    assert res["state"] == "Tamil Nadu"
    print(f"[PASS] Step 2: Officer profile verified: {res['name']} ({res['designation']}), {res['assigned_area']}, {res['district']}, {res['state']}")

    # Step 3: Officer adds Onion - 15 Tons
    status, res = make_request("/api/officer/produce", method="POST", data={
        "crop_name": "Onion",
        "quantity": 15.0,
        "unit": "Tons",
        "area": "Sankari",
        "village": "Sankari Town",
        "district": "Salem",
        "state": "Tamil Nadu",
        "produce_type": "Vegetable / Bulbs",
        "quality": "Grade A",
        "availability_date": "2026-09-16",
        "expected_harvest_date": "2026-09-16",
        "notes": "Direct officer field verification. Bulk Bellary red onions."
    }, token=officer_token)
    assert status == 200, f"Add Onion failed: {res}"
    officer_onion_id = res["produce"]["id"]
    print(f"[PASS] Step 3: Officer added Onion (15 Tons). Produce ID: {officer_onion_id}, Status: {res['produce']['verification_status']}")

    # Step 4: Officer adds Tomato - 16 Tons
    status, res = make_request("/api/officer/produce", method="POST", data={
        "crop_name": "Tomato",
        "quantity": 16.0,
        "unit": "Tons",
        "area": "Sankari",
        "village": "Sankari Rural",
        "district": "Salem",
        "state": "Tamil Nadu",
        "produce_type": "Vegetable",
        "quality": "Grade A",
        "availability_date": "2026-09-18",
        "expected_harvest_date": "2026-09-18",
        "notes": "Direct officer verification. High firmness."
    }, token=officer_token)
    assert status == 200, f"Add Tomato failed: {res}"
    print(f"[PASS] Step 4: Officer added Tomato (16 Tons). Status: {res['produce']['verification_status']}")

    # Step 5: Farmer Kumar logs in
    status, res = make_request("/api/auth/login", method="POST", data={
        "identifier": "9123456780",
        "password": "farmer123",
        "role": "FARMER"
    })
    assert status == 200, f"Farmer login failed: {res}"
    farmer_token = res["token"]
    print(f"[PASS] Step 5: Farmer Kumar logged in successfully.")

    # Step 6 & 7: Farmer Kumar adds crop and submits request:
    # Onion, 2 Acres, 5 Tons expected, Harvest: 25 September 2026, Sankari, Salem, Tamil Nadu
    status, res = make_request("/api/farmer/crops", method="POST", data={
        "crop_name": "Onion",
        "cultivated_area": 2.0,
        "cultivated_area_unit": "Acres",
        "expected_quantity": 5.0,
        "quantity_unit": "Tons",
        "expected_harvest_date": "2026-09-25",
        "crop_stage": "Bulb Development",
        "quality": "Grade A",
        "village": "Sankari West",
        "area": "Sankari",
        "district": "Salem",
        "state": "Tamil Nadu",
        "notes": "Drip irrigation cultivated across 2 acres."
    }, token=farmer_token)
    assert status == 200, f"Farmer crop submission failed: {res}"
    farmer_request_id = res["request"]["id"]
    print(f"[PASS] Step 6 & 7: Farmer Kumar submitted Onion (5 Tons) for verification. Request ID: {farmer_request_id}, Status: {res['request']['status']}")

    # Step 8: Officer Ravi Kumar sees the pending request
    status, res = make_request("/api/officer/requests", token=officer_token)
    assert status == 200, f"Officer get requests failed: {res}"
    pending_matching = [r for r in res if r["id"] == farmer_request_id]
    assert len(pending_matching) == 1, "Farmer request was not routed to Officer's dashboard"
    assert pending_matching[0]["status"] == "PENDING"
    print(f"[PASS] Step 8: Officer Ravi Kumar sees pending request #{farmer_request_id} from Kumar ({pending_matching[0]['crop_name']}, {pending_matching[0]['expected_quantity']} {pending_matching[0]['quantity_unit']})")

    # Step 9: Officer Ravi Kumar verifies it
    status, res = make_request(f"/api/officer/requests/{farmer_request_id}/verify", method="POST", data={
        "action": "VERIFY",
        "comment": "Field inspected by AAO Ravi Kumar. Verified crop quality and expected yield."
    }, token=officer_token)
    assert status == 200, f"Officer verification failed: {res}"
    assert res["request"]["status"] == "VERIFIED"
    assert res["produce"]["verification_status"] == "VERIFIED"
    print(f"[PASS] Step 9: Officer verified request #{farmer_request_id}. Produce #{res['produce']['id']} is now VERIFIED.")

    # Step 10 & 11: Buyer opens View Produce (no login needed!) and searches Onion -> Salem -> Sankari
    params = urllib.parse.urlencode({
        "crop": "Onion",
        "state": "Tamil Nadu",
        "district": "Salem",
        "area": "Sankari",
        "verified_only": "true"
    })
    status, res = make_request(f"/api/public/produce?{params}")
    assert status == 200, f"Public produce search failed: {res}"
    print(f"[PASS] Step 10 & 11: Buyer searched 'Onion' -> Salem -> Sankari. Found {len(res)} results.")

    # Step 12: Buyer sees both: officer-recorded produce and farmer-submitted verified produce!
    quantities = [r["quantity"] for r in res if r["crop_name"] == "Onion"]
    source_types = [r["source_type"] for r in res if r["crop_name"] == "Onion"]
    print(f"  Produce Quantities found: {quantities}")
    print(f"  Source Types found: {source_types}")
    assert 15.0 in quantities, "15 Tons officer-recorded onion not found in search results"
    assert 5.0 in quantities, "5 Tons farmer-submitted verified onion not found in search results"
    assert "officer_local" in source_types or "OFFICER_ENTRY" in source_types
    assert "farmer_verified" in source_types or "FARMER_VERIFIED" in source_types
    print(f"[PASS] Step 12: Buyer sees BOTH 15 Tons (Officer Recorded) + 5 Tons (Farmer Verified)!")

    # Step 13: Buyer opens details and sends a purchase request
    target_produce = next(r for r in res if r["quantity"] == 5.0)
    status, res = make_request(f"/api/public/produce/{target_produce['id']}")
    assert status == 200, f"Get produce details failed: {res}"
    print(f"  Viewing produce: {res['crop_name']} ({res['quantity']} {res['unit']}), Source: {res['source_display']}")

    # Send purchase request
    status, res = make_request("/api/public/purchase-requests", method="POST", data={
        "produce_id": target_produce["id"],
        "buyer_name": "Coimbatore Agro Traders (Buyer)",
        "buyer_contact": "+91 94433 22110",
        "requested_quantity": 3.0,
        "quantity_unit": "Tons",
        "message": "Interested in procuring 3 tons directly upon harvest on 25 September."
    })
    assert status == 200, f"Purchase request failed: {res}"
    print(f"[PASS] Step 13: Buyer purchase request submitted successfully: Inquiry ID #{res['request']['id']}")

    print("\n=======================================================")
    print(">>> ALL 13 DEMO STEPS & CORE SYSTEM TESTS PASSED 100%! <<<")
    print("=======================================================")

if __name__ == "__main__":
    run_tests()
