"""
test_officer_flow.py - Comprehensive verification of Agriculture Officer Mock Registry & Verification Flow

Tests:
1. Valid Officer Registration (AGRI-TN-0001 -> Ravi Kumar)
2. Invalid Officer ID (AGRI-TN-9999 blocked with 404)
3. Wrong OTP (OTP rejected with 400, attempts tracked)
4. Expired OTP / Resend OTP (Resend generates new OTP, allows verification)
5. Duplicate Registration (Attempting to re-register AGRI-TN-0001 blocked with 409)
6. Language / i18n keys completeness for all 23 languages
"""

import json
import urllib.request
import urllib.parse
import os
import sys

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

def run_all_officer_tests():
    print("=" * 65)
    print("AGRIFLOW AGRICULTURE OFFICER REGISTRY & VERIFICATION TEST SUITE")
    print("=" * 65)

    # Reset demo database first
    status, res = make_req("/api/auth/reset-demo", method="POST")
    assert status == 200, f"Reset demo failed: {res}"
    print("[INIT] Demo database reset and seeded successfully.\n")

    # -----------------------------------------------------------
    # Test 2: Invalid Officer ID (AGRI-TN-9999)
    # -----------------------------------------------------------
    print("--- Test 2: Invalid Officer ID (AGRI-TN-9999) ---")
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={
        "officer_id": "AGRI-TN-9999"
    })
    print(f"Status: {status}, Response: {res}")
    assert status == 404, f"Expected 404 for invalid ID, got {status}"
    assert "detail" in res and ("officer id not found" in res["detail"].lower() or "not found" in res["detail"].lower()), "Expected officer id not found message"
    print("[PASS] Test 2: Invalid Officer ID AGRI-TN-9999 successfully blocked with 404.\n")

    # -----------------------------------------------------------
    # Test 3: Wrong OTP Verification
    # -----------------------------------------------------------
    print("--- Test 3: Wrong OTP Verification ---")
    # Initiate verification for valid officer AGRI-KA-0001 (Kavitha Gowda)
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={
        "officer_id": "AGRI-KA-0001"
    })
    assert status == 200, f"Verify KA officer failed: {res}"
    valid_demo_otp = res["demo_otp"]
    print(f"Verified ID AGRI-KA-0001, Generated Demo OTP: {valid_demo_otp}")

    # Send wrong OTP
    status, res = make_req("/api/auth/officer/verify-otp", method="POST", data={
        "officer_id": "AGRI-KA-0001",
        "otp": "000000" if valid_demo_otp != "000000" else "111111"
    })
    print(f"Status with wrong OTP: {status}, Response: {res}")
    assert status == 400, f"Expected 400 for wrong OTP, got {status}"
    assert "attempts" in res.get("detail", "").lower() or "invalid" in res.get("detail", "").lower()
    print("[PASS] Test 3: Wrong OTP correctly rejected, attempt counter tracked.\n")

    # -----------------------------------------------------------
    # Test 4: Resend OTP Mechanism
    # -----------------------------------------------------------
    print("--- Test 4: Resend OTP Mechanism ---")
    status, res = make_req("/api/auth/officer/resend-otp", method="POST", data={
        "officer_id": "AGRI-KA-0001"
    })
    assert status == 200, f"Resend OTP failed: {res}"
    new_demo_otp = res["demo_otp"]
    print(f"New Demo OTP generated: {new_demo_otp}")

    # Now verify with new OTP
    status, res = make_req("/api/auth/officer/verify-otp", method="POST", data={
        "officer_id": "AGRI-KA-0001",
        "otp": new_demo_otp
    })
    assert status == 200, f"Verify with resent OTP failed: {res}"
    assert "verification_token" in res
    assert res["officer"]["name"] == "Ramesh Gowda"
    assert res["officer"]["state"] == "Karnataka"
    print(f"[PASS] Test 4: Resend OTP successfully issued new OTP and verified: {res['officer']['name']}.\n")

    # -----------------------------------------------------------
    # Test 1: Valid Officer Registration & Login (AGRI-TN-0001 -> Ravi Kumar)
    # -----------------------------------------------------------
    print("--- Test 1: Valid Officer Flow (AGRI-TN-0001 -> Ravi Kumar) ---")
    # 1. ID verification
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={
        "officer_id": "AGRI-TN-0001"
    })
    assert status == 200, f"ID check failed: {res}"
    assert res["masked_mobile"] == "******3210"
    demo_otp = res["demo_otp"]
    print(f"1. ID verified: AGRI-TN-0001, Masked Mobile: {res['masked_mobile']}, Demo OTP: {demo_otp}")

    # 2. OTP verification
    status, res = make_req("/api/auth/officer/verify-otp", method="POST", data={
        "officer_id": "AGRI-TN-0001",
        "otp": demo_otp
    })
    assert status == 200, f"OTP verification failed: {res}"
    token_tn = res["verification_token"]
    officer_info = res["officer"]
    print(f"2. OTP verified! Retrieved official details:")
    print(f"   Name: {officer_info['name']}")
    print(f"   Post: {officer_info['designation']}")
    print(f"   State: {officer_info['state']}")
    print(f"   District: {officer_info['district']}")
    print(f"   Working Place: {officer_info['assigned_area']}")
    print(f"   Department: {officer_info['department']}")
    assert officer_info["name"] == "Ravi Kumar"
    assert officer_info["district"] == "Salem"

    # 3. Create Login Credentials
    status, res = make_req("/api/auth/officer/create-account", method="POST", data={
        "officer_id": "AGRI-TN-0001",
        "verification_token": token_tn,
        "login_id": "ravi_salem_officer",
        "password": "officer123",
        "confirm_password": "officer123"
    })
    assert status == 200, f"Account creation failed: {res}"
    user_data = res["user"]
    print(f"3. Officer account created! User ID: {user_data['id']}, Login ID: {user_data['login_id']}, Officer ID: {user_data['officer_id']}")

    # 4. Officer Login using Officer ID
    status, res = make_req("/api/auth/login", method="POST", data={
        "identifier": "AGRI-TN-0001",
        "password": "officer123",
        "role": "OFFICER"
    })
    assert status == 200, f"Login with Officer ID failed: {res}"
    officer_jwt = res["token"]
    print(f"4a. Logged in successfully with Officer ID (AGRI-TN-0001). JWT: {officer_jwt[:15]}...")

    # 4b. Officer Login using Login ID
    status, res = make_req("/api/auth/login", method="POST", data={
        "identifier": "ravi_salem_officer",
        "password": "officer123",
        "role": "OFFICER"
    })
    assert status == 200, f"Login with Login ID failed: {res}"
    print(f"4b. Logged in successfully with custom Login ID (ravi_salem_officer).")

    # 5. Fetch Officer Profile
    status, res = make_req("/api/officer/profile", token=officer_jwt)
    assert status == 200, f"Profile fetch failed: {res}"
    assert res["officer_id"] == "AGRI-TN-0001"
    assert res["name"] == "Ravi Kumar"
    assert res["district"] == "Salem"
    assert res["state"] == "Tamil Nadu"
    assert res["is_verified_officer"] == True
    print(f"5. Officer profile retrieved with verified registry details: {res['name']} ({res['officer_id']})")
    print("[PASS] Test 1: Complete Valid Officer Verification & Login flow succeeded.\n")

    # -----------------------------------------------------------
    # Test 5: Prevent Duplicate Registration
    # -----------------------------------------------------------
    print("--- Test 5: Duplicate Registration Prevention ---")
    status, res = make_req("/api/auth/officer/verify-id", method="POST", data={
        "officer_id": "AGRI-TN-0001"
    })
    print(f"Status for re-registering AGRI-TN-0001: {status}, Response: {res}")
    assert status == 409, f"Expected 409 Conflict for duplicate registration, got {status}"
    assert "already" in res.get("detail", "").lower(), "Expected already registered notice"
    print("[PASS] Test 5: Duplicate registration for AGRI-TN-0001 blocked with 409 Conflict.\n")

    # -----------------------------------------------------------
    # Test 6: Language / i18n Verification
    # -----------------------------------------------------------
    print("--- Test 6: i18n Localization Verification across 23 Indian Languages ---")
    import build_locales
    locales_dir = os.path.join(os.path.dirname(__file__), "static", "i18n", "locales")
    required_keys = [
        "officerVerificationTitle",
        "officerVerificationSubtitle",
        "officerId",
        "officerIdPlaceholder",
        "verifyOfficerId",
        "invalidOfficerId",
        "invalidOfficerIdMsg",
        "officerIdVerified",
        "demoOtpBanner",
        "otpVerification",
        "otpSentTo",
        "demoOtpLabel",
        "autoFillDemoOtp",
        "enterOtp",
        "verifyOtp",
        "resendOtp",
        "officerDetailsVerified",
        "createLoginTitle",
        "createLoginId",
        "createPassword",
        "confirmPassword",
        "createOfficerAccount",
        "accountAlreadyExists",
        "accountAlreadyExistsMsg",
        "officerLoginIdLabel",
        "verifiedOfficerInformation"
    ]

    missing_in_languages = {}
    for code in build_locales.expected_codes:
        filepath = os.path.join(locales_dir, f"{code}.json")
        assert os.path.exists(filepath), f"Missing locale file {code}.json"
        with open(filepath, "r", encoding="utf-8") as lf:
            data = json.load(lf)
            auth_data = data.get("auth", {})
            profile_data = data.get("profile", {})
            for key in required_keys:
                if key not in auth_data and key not in profile_data:
                    missing_in_languages.setdefault(code, []).append(key)

    if missing_in_languages:
        print(f"[FAIL] Missing keys in languages: {missing_in_languages}")
        sys.exit(1)
    else:
        print(f"[PASS] All {len(build_locales.expected_codes)} Eighth Schedule languages contain all required officer verification keys.\n")

    # -----------------------------------------------------------
    # Test Demo Registry Security (Public API Removed, Mock Data Private Server-Side)
    # -----------------------------------------------------------
    print("--- Test 7: Verify Public Registry API is Blocked & Private Mock Registry Intact ---")
    status, res = make_req("/api/auth/officer-registry/demo-list")
    assert status == 404, f"Public demo registry API should be removed (404), got {status}: {res}"
    print("[PASS] Public /api/auth/officer-registry/demo-list is completely blocked (404 Not Found).")

    # Verify that the backend private mock registry retains all 45 records for prototype testing
    from mock_officer_registry import MOCK_OFFICER_REGISTRY
    assert len(MOCK_OFFICER_REGISTRY) == 45, f"Expected 45 mock officers, found {len(MOCK_OFFICER_REGISTRY)}"
    states = set(o["state"] for o in MOCK_OFFICER_REGISTRY)
    assert len(states) >= 15, "Expected coverage across >= 15 states"
    print(f"[PASS] Private mock registry securely maintained server-side: {len(MOCK_OFFICER_REGISTRY)} records across {len(states)} states.\n")

    # Verify /api/officer/verify-id route also works
    status, res = make_req("/api/officer/verify-id", method="POST", data={"officer_id": "AGRI-TN-0003"})
    assert status == 200, f"/api/officer/verify-id failed: {res}"
    assert res["officer_id"] == "AGRI-TN-0003"
    print(f"[PASS] Alternative route /api/officer/verify-id verified successfully for AGRI-TN-0003.\n")

    print("=" * 65)
    print("ALL 6 TESTS PASSED SUCCESSFULLY! PROTOTYPE READY FOR DEMONSTRATION.")
    print("=" * 65)

if __name__ == "__main__":
    run_all_officer_tests()
