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

    # 1. Pre-register Demo Agriculture Officer: Priya Devi (AGRI-TN-0002)
    # AGRI-TN-0001 (Ravi Kumar) is intentionally left UNREGISTERED so evaluators
    # can test the complete new registration flow (Test 1 & Test 5).
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
    officer_id = cursor.lastrowid

    # 2. Officer Profile for Priya Devi
    cursor.execute("""
    INSERT INTO officer_profiles (user_id, officer_id, designation, department, assigned_area, district, state, contact, photo_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        officer_id,
        "AGRI-TN-0002",
        "Assistant Agriculture Officer",
        "Department of Agriculture & Farmers Welfare",
        "Sankari",
        "Salem",
        "Tamil Nadu",
        "9876543211",
        "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=crop&q=80"
    ))

    # Officer Account Record
    cursor.execute("""
    INSERT INTO officer_accounts (officer_id, login_id, password_hash, user_id)
    VALUES (?, ?, ?, ?)
    """, (
        "AGRI-TN-0002",
        "priya.devi",
        hash_password("officer123"),
        officer_id
    ))


    # 3. Create Farmer: Kumar
    cursor.execute("""
    INSERT INTO users (role, name, email, phone, password_hash)
    VALUES (?, ?, ?, ?, ?)
    """, (
        "FARMER",
        "Kumar",
        "kumar.farmer@example.com",
        "9123456780",
        hash_password("farmer123")
    ))
    farmer_id = cursor.lastrowid

    # 4. Farmer Profile
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

    # 5. Add Officer-recorded produce items as demo data
    # Demo Produce 1: Onion 15 Tons (Officer Verified)
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, officer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Onion",
        15.0,
        "Tons",
        "Sankari",
        "Sankari Town",
        "Salem",
        "Tamil Nadu",
        "Vegetable / Bulbs",
        "Grade A",
        "2026-09-16",
        "2026-09-16",
        "officer_local",
        officer_id,
        "VERIFIED",
        "Officer field verified: High-quality Bellary red onions harvested from local cluster."
    ))

    # Demo Produce 2: Tomato 16 Tons (Officer Verified)
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, officer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Tomato",
        16.0,
        "Tons",
        "Sankari",
        "Sankari Rural",
        "Salem",
        "Tamil Nadu",
        "Vegetable",
        "Grade A",
        "2026-09-18",
        "2026-09-18",
        "officer_local",
        officer_id,
        "VERIFIED",
        "Ripe firm tomatoes, ready for market procurement."
    ))

    # Demo Produce 3: Potato 8 Tons (Officer Verified)
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, officer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Potato",
        8.0,
        "Tons",
        "Sankari",
        "Sankari North",
        "Salem",
        "Tamil Nadu",
        "Tubers",
        "Grade B",
        "2026-09-20",
        "2026-09-20",
        "officer_local",
        officer_id,
        "VERIFIED",
        "Local fresh potato stock available for direct bulk dispatch."
    ))

    # 6. Sample Pending Farmer Request (Section 22 demo data)
    # Produce record placeholder for farmer submission
    cursor.execute("""
    INSERT INTO produce_records (
        crop_name, quantity, unit, area, village, district, state,
        produce_type, quality, availability_date, expected_harvest_date,
        source_type, farmer_id, verification_status, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Onion",
        5.0,
        "Tons",
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
        "PENDING",
        "Cultivated under drip irrigation across 2 acres. Expected yield 5 tons."
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
        officer_id,
        pending_produce_id,
        "Onion",
        2.0,
        "Acres",
        5.0,
        "Tons",
        "2026-09-25",
        "Bulb Development / Pre-Harvest",
        "Grade A",
        "Sankari West",
        "Sankari",
        "Salem",
        "Tamil Nadu",
        "Farmer submission awaiting local officer verification.",
        "PENDING"
    ))

    conn.commit()
    conn.close()
    print("AgriFlow demo data successfully seeded:")
    print("  - Pre-registered Demo Officer: Priya Devi (AGRI-TN-0002) | Login: priya.devi / officer123")
    print("  - Ready for Verification & Registration: Ravi Kumar (AGRI-TN-0001 - Salem, Sankari)")
    print("  - Farmer: Kumar (Sankari, Salem, Tamil Nadu) | Login: 9123456780 / farmer123")
    print("  - Produce: Onion (15T), Tomato (16T), Potato (8T) - Verified")
    print("  - Request: Kumar -> Onion (5T) - Pending Verification")


if __name__ == "__main__":
    seed_database(clean=True)
