import sqlite3
from database import get_db_connection, init_db
from auth import hash_password

def seed_database(clean: bool = True):
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()

    if clean:
        cursor.execute("DELETE FROM purchase_requests;")
        cursor.execute("DELETE FROM verification_requests;")
        cursor.execute("DELETE FROM produce_records;")
        cursor.execute("DELETE FROM farmer_profiles;")
        cursor.execute("DELETE FROM officer_profiles;")
        cursor.execute("DELETE FROM officer_accounts;")
        cursor.execute("DELETE FROM otp_verifications;")
        cursor.execute("DELETE FROM sessions;")
        cursor.execute("DELETE FROM users;")

    # Ensure mock officer registry is populated
    from database import seed_mock_officer_registry
    seed_mock_officer_registry(cursor)

    # 1. Pre-register Demo Agriculture Officer: Priya Devi (AGRI-TN-0002) for Hosur, Krishnagiri
    # (used to test duplicate registration prevention in Step 3 / Test 5)
    # AGRI-TN-0001 (Ravi Kumar - Sankari, Salem) is in the official registry and
    # left UNREGISTERED so that the 4-step registration wizard can be demonstrated cleanly in Section 7!
    cursor.execute("""
    INSERT INTO users (role, name, email, phone, officer_id, login_id, password_hash)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        "OFFICER",
        "Priya Devi",
        "priya.devi@agri.tn.gov.in",
        "9876543211",
        "AGRI-TN-0002",
        "priya.devi",
        hash_password("officer123")
    ))
    priya_user_id = cursor.lastrowid

    cursor.execute("""
    INSERT INTO officer_profiles (user_id, officer_id, designation, department, assigned_area, district, state, contact, photo_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        priya_user_id,
        "AGRI-TN-0002",
        "Assistant Agriculture Officer",
        "Department of Agriculture & Farmers Welfare",
        "Hosur",
        "Krishnagiri",
        "Tamil Nadu",
        "9876543211",
        "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=crop&q=80"
    ))

    cursor.execute("""
    INSERT INTO officer_accounts (officer_id, login_id, password_hash, user_id)
    VALUES (?, ?, ?, ?)
    """, (
        "AGRI-TN-0002",
        "priya.devi",
        hash_password("officer123"),
        priya_user_id
    ))

    # 2. Create Farmer: Kanagaraj (Salem, Sankari, Tamil Nadu)
    cursor.execute("""
    INSERT INTO users (role, name, email, phone, password_hash)
    VALUES (?, ?, ?, ?, ?)
    """, (
        "FARMER",
        "Kanagaraj",
        "kanagaraj.farmer@example.com",
        "9123456780",
        hash_password("farmer123")
    ))
    farmer_id = cursor.lastrowid

    # Farmer Profile for Kanagaraj
    cursor.execute("""
    INSERT INTO farmer_profiles (user_id, village, area, district, state, land_area, land_unit, farming_type, photo_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        farmer_id,
        "Sankari West",
        "Sankari",
        "Salem",
        "Tamil Nadu",
        2.5,
        "Acres",
        "Natural / Organic",
        "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=crop&q=80"
    ))

    # 3. Officer-recorded produce items (Section 10 & 11 & 13 demo data)
    # Demo Produce 1: Onion 15 Tons (Officer Verified - Section 10 & 11)
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, price, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, officer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Onion",
        15.0,
        "Tons",
        22000.0,
        "Sankari",
        "Sankari Town",
        "Salem",
        "Tamil Nadu",
        "Vegetable / Bulbs",
        "Grade A",
        "2026-09-16",
        "2026-09-16",
        "officer_local",
        None,
        "VERIFIED",
        "Officer field verified: High-quality Bellary red onions harvested from local cluster."
    ))

    # Demo Produce 2: Tomato 16 Tons (Officer Verified - Section 10)
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, price, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, officer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Tomato",
        16.0,
        "Tons",
        18000.0,
        "Sankari",
        "Sankari Rural",
        "Salem",
        "Tamil Nadu",
        "Vegetable",
        "Grade A",
        "2026-09-18",
        "2026-09-18",
        "officer_local",
        None,
        "VERIFIED",
        "Ripe firm tomatoes, ready for market procurement."
    ))

    # Demo Produce 3: Mango 4 Tons (Officer Verified - Section 13)
    # Highlighted in Section 13 as officer-entered availability record with purchase requests disabled
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, price, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, officer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Mango",
        4.0,
        "Tons",
        45000.0,
        "Sankari",
        "Sankari South",
        "Salem",
        "Tamil Nadu",
        "Fruits / Orchard",
        "Grade A",
        "2026-09-20",
        "2026-09-20",
        "officer_local",
        None,
        "VERIFIED",
        "Officer local survey: Fresh local Alphonso/Banganapalli mango cluster harvest in Sankari block."
    ))

    # 4. Farmer-Verified Produce: Onion 5 Tons (Section 12 demo data)
    # Highlighted in Section 12 as verified farmer produce eligible for Buyer Purchase Inquiry
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, price, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, farmer_id, officer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Onion",
        5.0,
        "Tons",
        24000.0,
        "Sankari",
        "Sankari West",
        "Salem",
        "Tamil Nadu",
        "Field Crop",
        "Grade A",
        "2026-09-25",
        "2026-09-25",
        "farmer_verified",
        farmer_id,
        None,
        "VERIFIED",
        "Cultivated under drip irrigation across 2 acres by Farmer Kanagaraj. Verified by local Agriculture Officer."
    ))

    # 5. Pending Farmer Verification Request: Carrot 5.6 Tons, 0.6 Acres (Section 6 & 9 demo data)
    # Matches Farmer: Kanagaraj, Crop: Carrot, Cultivated Area: 0.6 Acres, Expected Yield: 5.6 Tons, Sankari, Salem
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, farmer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Carrot",
        5.6,
        "Tons",
        "Sankari",
        "Sankari West",
        "Salem",
        "Tamil Nadu",
        "Field Crop",
        "Grade A",
        "2026-10-15",
        "2026-10-15",
        "farmer_verified",
        farmer_id,
        "PENDING",
        "Drip irrigation carrot cultivation across 0.6 acres. Awaiting local officer field verification."
    ))
    pending_produce_id = cursor.lastrowid

    cursor.execute("""
    INSERT INTO verification_requests (
        farmer_id, officer_id, produce_id, crop_name, cultivated_area, cultivated_area_unit,
        expected_quantity, quantity_unit, expected_harvest_date, crop_stage, quality,
        village, area, district, state, notes, status
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        farmer_id,
        None,
        pending_produce_id,
        "Carrot",
        0.6,
        "Acres",
        5.6,
        "Tons",
        "2026-10-15",
        "Vegetative Stage",
        "Grade A",
        "Sankari West",
        "Sankari",
        "Salem",
        "Tamil Nadu",
        "Drip irrigation carrot cultivation across 0.6 acres. Farmer submission awaiting local officer verification.",
        "PENDING"
    ))

    conn.commit()
    conn.close()
    print("AgriFlow demo data successfully seeded:")
    print("  - Officer Ready for Registration Demo (Section 7): Ravi Kumar (AGRI-TN-0001 - Sankari, Salem, Tamil Nadu)")
    print("  - Secondary Demo Officer: Priya Devi (AGRI-TN-0002) | Hosur, Krishnagiri | Login: priya.devi / officer123")
    print("  - Farmer: Kanagaraj (Sankari, Salem, Tamil Nadu) | Login: 9123456780 / farmer123")
    print("  - Produce: Onion (15T), Tomato (16T), Mango (4T - Officer Local), Onion (5T - Farmer Verified)")
    print("  - Pending Request: Kanagaraj -> Carrot (0.6 Acres, 5.6T) awaiting Officer Ravi Kumar verification")


if __name__ == "__main__":
    seed_database(clean=True)
