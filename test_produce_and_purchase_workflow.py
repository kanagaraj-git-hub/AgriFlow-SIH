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
    
    encoded_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as resp:
            status_code = resp.getcode()
            body = resp.read().decode("utf-8")
            return status_code, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            parsed = json.loads(body)
        except Exception:
            parsed = {"detail": body}
        return e.code, parsed

def run_tests():
    print("=================================================================")
    print("COMPREHENSIVE TEST: OFFICER LOCAL VS FARMER VERIFIED PRODUCE WORKFLOW")
    print("=================================================================")

    # Reset seed data
    status, res = make_req("/api/auth/reset-demo", method="POST")
    assert status == 200, f"Reset demo failed: {res}"
    print("[0] Database reset and reseeded.")

    # Setup 1: Log in Officer (Ravi Kumar AGRI-TN-0001)
    # First create account or login if seeded
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={"officer_id": "AGRI-TN-0001"})
    if status == 200:
        demo_otp = res["demo_otp"]
        status, res = make_req("/api/auth/officer/verify-otp", method="POST", data={"officer_id": "AGRI-TN-0001", "otp": demo_otp})
        assert status == 200
        verification_token = res["verification_token"]
        status, res = make_req("/api/auth/officer/create-account", method="POST", data={
            "officer_id": "AGRI-TN-0001",
            "verification_token": verification_token,
            "login_id": "ravi_officer_test",
            "password": "officerpassword123",
            "confirm_password": "officerpassword123"
        })
        assert status == 200, f"Officer create account failed: {res}"
        officer_token = res["token"]
    else:
        # Login
        status, res = make_req("/api/auth/login", method="POST", data={
            "identifier": "AGRI-TN-0001",
            "password": "officerpassword123",
            "role": "OFFICER"
        })
        assert status == 200, f"Officer login failed: {res}"
        officer_token = res["token"]

    print("[0b] Officer Ravi Kumar logged in.")

    # Setup 2: Log in Farmer 1 (Kumar: 9123456780 / farmer123)
    status, res = make_req("/api/auth/login", method="POST", data={
        "identifier": "9123456780",
        "password": "farmer123",
        "role": "FARMER"
    })
    assert status == 200, f"Farmer Kumar login failed: {res}"
    farmer1_token = res["token"]
    farmer1_id = res["user"]["id"]
    print(f"[0c] Farmer 1 (Kumar, ID: {farmer1_id}) logged in.")

    # Setup 3: Register & Log in Farmer 2 (Muthu: 9876543299 / farmerpassword123)
    status, res = make_req("/api/auth/register", method="POST", data={
        "name": "Muthu Vel",
        "phone": "9876543299",
        "password": "farmerpassword123",
        "role": "FARMER",
        "area": "Sankari",
        "district": "Salem",
        "state": "Tamil Nadu",
        "land_area": 2.0,
        "land_unit": "Acres"
    })
    assert status == 200, f"Farmer 2 registration failed: {res}"
    farmer2_token = res["token"]
    farmer2_id = res["user"]["id"]
    print(f"[0d] Farmer 2 (Muthu, ID: {farmer2_id}) registered & logged in.")

    # -------------------------------------------------------------
    # TEST 1: Officer creates local produce.
    # Expected:
    # source_type = "officer_local"
    # Public: View Details works.
    # Purchase Request: NOT visible / Backend purchase-request API rejects attempts for this record.
    # -------------------------------------------------------------
    print("\n--- TEST 1: Officer Creates Local Produce ---")
    status, res = make_req("/api/officer/produce", method="POST", token=officer_token, data={
        "crop_name": "Field Crop",
        "category": "Grains",
        "quantity": 12.0,
        "unit": "Tons",
        "price": 1200.0,
        "area": "Sankari",
        "district": "Salem",
        "state": "Tamil Nadu",
        "quality": "Grade A",
        "availability_date": "2026-09-30",
        "notes": "Direct local aggregated availability reported by Agriculture Officer"
    })
    assert status == 200, f"Officer add produce failed: {res}"
    officer_produce_id = res["produce"]["id"]
    assert res["produce"]["source_type"] == "officer_local", f"Expected 'officer_local', got {res['produce'].get('source_type')}"
    print(f"[PASS] Officer local produce created with ID {officer_produce_id}, source_type: {res['produce']['source_type']}")

    # Public View Details check
    status, details = make_req(f"/api/public/produce/{officer_produce_id}")
    assert status == 200, f"Public view details failed: {details}"
    assert details["source_type"] == "officer_local"
    assert details["record_type"] == "officer_local"
    assert "Officer" in details["record_type_display"]
    print(f"[PASS] Public View Details works for officer_local. Record type display: {details['record_type_display']}")

    # Backend purchase-request API rejects attempt for officer_local record
    status, pr_res = make_req("/api/public/purchase-requests", method="POST", data={
        "produce_id": officer_produce_id,
        "buyer_name": "Test Aggregator",
        "buyer_contact": "9998887776",
        "requested_quantity": 5.0,
        "requested_unit": "Tons",
        "message": "Attempting purchase request for officer local record"
    })
    assert status == 400, f"Expected status 400 for officer_local purchase request, got {status}: {pr_res}"
    assert "officer local" in pr_res.get("detail", "").lower() or "only for verified farmer" in pr_res.get("detail", "").lower()
    print(f"[PASS] Backend rejected purchase request on officer_local produce: {pr_res['detail']}")

    # -------------------------------------------------------------
    # TEST 2: Farmer submits produce. Officer verifies and publishes.
    # Expected: source_type = "farmer_verified", Purchase Request: VISIBLE
    # -------------------------------------------------------------
    print("\n--- TEST 2: Farmer Submits Produce & Officer Verifies ---")
    status, crop_sub = make_req("/api/farmer/crops", method="POST", token=farmer1_token, data={
        "crop_name": "Onion",
        "cultivated_area": 2.0,
        "cultivated_area_unit": "Acres",
        "expected_quantity": 5.0,
        "quantity_unit": "Tons",
        "expected_harvest_date": "2026-09-25",
        "crop_stage": "Harvest Ready",
        "area": "Sankari",
        "district": "Salem",
        "state": "Tamil Nadu",
        "notes": "Red Onion Grade A"
    })
    assert status == 200, f"Farmer crop submission failed: {crop_sub}"
    farmer_crop_req_id = crop_sub["request"]["id"]
    print(f"[PASS] Farmer submitted crop with verification request ID {farmer_crop_req_id}")

    # Officer verifies and publishes
    status, verify_res = make_req(f"/api/officer/requests/{farmer_crop_req_id}/verify", method="POST", token=officer_token, data={
        "action": "VERIFY",
        "quality_grade": "Grade A",
        "verified_quantity": 5.0,
        "officer_comment": "Field inspected and certified Grade A Onion.",
        "unit_price": 2800.0,
        "price_unit": "Ton"
    })
    assert status == 200, f"Officer verification failed: {verify_res}"
    farmer_produce_id = verify_res["produce"]["id"]
    print(f"[PASS] Officer verified request #{farmer_crop_req_id}. Published produce ID: {farmer_produce_id}")

    # Check produce record details
    status, f_details = make_req(f"/api/public/produce/{farmer_produce_id}")
    assert status == 200
    assert f_details["source_type"] == "farmer_verified", f"Expected farmer_verified, got {f_details['source_type']}"
    assert f_details["record_type"] == "farmer_verified"
    assert f_details["farmer_id"] == farmer1_id
    print(f"[PASS] Verified produce has source_type: {f_details['source_type']}, farmer_id: {f_details['farmer_id']}")

    # -------------------------------------------------------------
    # TEST 3: Buyer submits request for farmer_verified produce.
    # Expected: Request successfully created with all fields and pending status.
    # -------------------------------------------------------------
    # -------------------------------------------------------------
    print("\n--- TEST 3: Buyer Submits Purchase Request for Farmer Verified Produce ---")
    status, pr_created = make_req("/api/public/purchase-requests", method="POST", data={
        "produce_id": farmer_produce_id,
        "buyer_name": "ABC Traders",
        "buyer_contact": "9845112233 / buyer@abctraders.com",
        "requested_quantity": 2.0,
        "requested_unit": "Tons",
        "message": "Need delivery to Salem."
    })
    assert status == 200, f"Purchase request failed: {pr_created}"
    pr_row = pr_created["request"]
    pr_id = pr_row["id"]
    assert pr_row["produce_id"] == farmer_produce_id
    assert pr_row["farmer_id"] == farmer1_id
    assert pr_row["buyer_name"] == "ABC Traders"
    assert pr_row["buyer_contact"] == "9845112233 / buyer@abctraders.com"
    assert pr_row["requested_quantity"] == 2.0
    assert pr_row["quantity_unit"] == "Tons"
    assert pr_row["message"] == "Need delivery to Salem."
    assert pr_row["status"].lower() == "pending"
    assert "associated with this verified produce" in pr_created.get("message", "")
    print(f"[PASS] Purchase request #{pr_id} created successfully with status: {pr_row['status']}")

    # -------------------------------------------------------------
    # TEST 4: Farmer logs in & sees purchase request in Farmer Portal
    # -------------------------------------------------------------
    print("\n--- TEST 4: Farmer Sees Purchase Request in Farmer Portal ---")
    status, farmer1_requests = make_req("/api/farmer/purchase-requests", token=farmer1_token)
    assert status == 200, f"Get farmer purchase requests failed: {farmer1_requests}"
    found = [r for r in farmer1_requests if r["id"] == pr_id]
    assert len(found) == 1, f"Expected to find request #{pr_id} in Farmer 1 list, got {farmer1_requests}"
    req_item = found[0]
    assert req_item["buyer_name"] == "ABC Traders"
    assert req_item["crop_name"] == "Onion"
    assert req_item["requested_quantity"] == 2.0
    assert req_item["requested_unit"] == "Tons"
    assert req_item["message"] == "Need delivery to Salem."
    assert req_item["status"].lower() == "pending"
    print(f"[PASS] Farmer 1 sees purchase request #{pr_id} from {req_item['buyer_name']} for {req_item['crop_name']}")

    # -------------------------------------------------------------
    # TEST 5: Different farmer logs in. Cannot see the first farmer's purchase request.
    # -------------------------------------------------------------
    print("\n--- TEST 5: Different Farmer Isolation ---")
    status, farmer2_requests = make_req("/api/farmer/purchase-requests", token=farmer2_token)
    assert status == 200
    found_f2 = [r for r in farmer2_requests if r["id"] == pr_id]
    assert len(found_f2) == 0, f"Farmer 2 should NOT see request #{pr_id}, but found: {found_f2}"
    print("[PASS] Farmer 2 cannot see Farmer 1's purchase requests (Strict farmer_id isolation verified)")

    # -------------------------------------------------------------
    # TEST 6: Buyer tries to manipulate produce_id or farmer_id.
    # Backend determines the correct farmer from produce record and does not trust client-supplied farmer_id.
    # -------------------------------------------------------------
    print("\n--- TEST 6: Client Manipulation / Security Verification ---")
    # Client tries to pass a spoofed farmer_id (e.g., 9999 or farmer2_id)
    status, spoof_res = make_req("/api/public/purchase-requests", method="POST", data={
        "produce_id": farmer_produce_id,
        "farmer_id": 99999,  # Spoofed!
        "buyer_name": "Spoof Attacker",
        "buyer_contact": "hacker@test.com",
        "requested_quantity": 1.0,
        "requested_unit": "Tons",
        "message": "Attempting to spoof farmer_id"
    })
    assert status == 200
    # Backend must have assigned it to farmer1_id (the true produce owner), NOT 99999!
    assert spoof_res["request"]["farmer_id"] == farmer1_id, f"Expected {farmer1_id}, got {spoof_res['request']['farmer_id']}"
    print(f"[PASS] Client-supplied farmer_id safely ignored; backend bound request to true owner farmer_id: {spoof_res['request']['farmer_id']}")

    # Client tries non-existent produce_id
    status, missing_res = make_req("/api/public/purchase-requests", method="POST", data={
        "produce_id": 999999,
        "buyer_name": "Ghost Produce Buyer",
        "buyer_contact": "ghost@test.com",
        "requested_quantity": 1.0,
        "requested_unit": "Tons",
        "message": "Ghost produce"
    })
    assert status == 404, f"Expected 404 for missing produce, got {status}: {missing_res}"
    print(f"[PASS] Backend rejected request for non-existent produce (404)")

    # -------------------------------------------------------------
    # TEST 7: Existing officer-local produce.
    # Expected: No Purchase Request allowed.
    # -------------------------------------------------------------
    print("\n--- TEST 7: Existing Officer-Local Produce ---")
    # Find seeded officer produce (Priya Devi's produce #1)
    status, seeded_produce_list = make_req("/api/public/produce?crop_name=Onion")
    assert status == 200
    officer_seed_records = [p for p in seeded_produce_list if p.get("source_type") in ("officer_local", "OFFICER_ENTRY")]
    assert len(officer_seed_records) > 0, "No seeded officer produce found"
    seed_officer_prod = officer_seed_records[0]
    print(f"[PASS] Found seeded officer produce ID: {seed_officer_prod['id']} ({seed_officer_prod['crop_name']})")

    status, err_pr = make_req("/api/public/purchase-requests", method="POST", data={
        "produce_id": seed_officer_prod["id"],
        "buyer_name": "Seed Tester",
        "buyer_contact": "tester@test.com",
        "requested_quantity": 1.0,
        "requested_unit": "Tons",
        "message": "Testing seeded officer produce"
    })
    assert status == 400
    print(f"[PASS] Seeded officer produce rejected for purchase request (400, '{err_pr['detail']}')")

    # -------------------------------------------------------------
    # TEST 8: Existing farmer-verified produce & Accept/Reject workflow
    # -------------------------------------------------------------
    print("\n--- TEST 8: Existing Farmer-Verified Produce & Accept/Reject Workflow ---")
    farmer_seed_records = [p for p in seeded_produce_list if p.get("source_type") in ("farmer_verified", "FARMER_VERIFIED")]
    assert len(farmer_seed_records) > 0, "No seeded farmer produce found"
    seed_farmer_prod = farmer_seed_records[0]
    print(f"[PASS] Found seeded farmer produce ID: {seed_farmer_prod['id']} ({seed_farmer_prod['crop_name']})")

    # Submit request for seeded farmer produce
    status, seed_pr = make_req("/api/public/purchase-requests", method="POST", data={
        "produce_id": seed_farmer_prod["id"],
        "buyer_name": "Global Foods Ltd",
        "buyer_contact": "procurement@globalfoods.com",
        "requested_quantity": 3.0,
        "requested_unit": "Tons",
        "message": "Urgent procurement requirement"
    })
    assert status == 200, f"Request for seeded farmer produce failed: {seed_pr}"
    test8_pr_id = seed_pr["request"]["id"]
    print(f"[PASS] Purchase request #{test8_pr_id} submitted for seeded farmer produce")

    # Now test farmer Accept action
    status, accept_res = make_req(f"/api/farmer/purchase-requests/{pr_id}/accept", method="POST", token=farmer1_token)
    assert status == 200, f"Farmer accept failed: {accept_res}"
    assert accept_res["request"]["status"] == "accepted"
    print(f"[PASS] Farmer accepted purchase request #{pr_id} -> status: {accept_res['request']['status']}")

    # Now test farmer Reject action on the other request
    status, reject_res = make_req(f"/api/farmer/purchase-requests/{test8_pr_id}/reject", method="POST", token=farmer1_token)
    assert status == 200, f"Farmer reject failed: {reject_res}"
    assert reject_res["request"]["status"] == "rejected"
    print(f"[PASS] Farmer rejected purchase request #{test8_pr_id} -> status: {reject_res['request']['status']}")

    # Verify farmer cannot accept/reject another farmer's request
    status, unauthorized_act = make_req(f"/api/farmer/purchase-requests/{pr_id}/accept", method="POST", token=farmer2_token)
    assert status == 404 or status == 403, f"Farmer 2 should not be able to modify Farmer 1 request, got {status}"
    print(f"[PASS] Farmer 2 blocked from modifying Farmer 1 purchase request ({status})")

    # Dashboard counters check
    status, dash = make_req("/api/farmer/dashboard", token=farmer1_token)
    assert status == 200
    assert "total_purchase_requests" in dash["stats"]
    assert "pending_purchase_requests" in dash["stats"]
    print(f"[PASS] Farmer dashboard includes total_purchase_requests: {dash['stats']['total_purchase_requests']}, pending: {dash['stats']['pending_purchase_requests']}")

    print("\n=================================================================")
    print(">>> ALL 8 PRODUCE & PURCHASE REQUEST WORKFLOW TESTS PASSED 100%! <<<")
    print("=================================================================")

if __name__ == "__main__":
    run_tests()
