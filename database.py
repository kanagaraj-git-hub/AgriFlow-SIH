import sqlite3
import os
from typing import Optional, List, Dict, Any

DB_PATH = os.path.join(os.path.dirname(__file__), "agriflow.db")

def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=10.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL CHECK(role IN ('OFFICER', 'FARMER')),
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Officer Profiles table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS officer_profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE,
        designation TEXT NOT NULL,
        department TEXT NOT NULL,
        assigned_area TEXT NOT NULL,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        contact TEXT NOT NULL,
        photo_url TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    # 3. Farmer Profiles table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS farmer_profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE,
        village TEXT NOT NULL,
        area TEXT NOT NULL,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        land_area REAL NOT NULL,
        land_unit TEXT NOT NULL DEFAULT 'Acres',
        farming_type TEXT NOT NULL DEFAULT 'Conventional',
        photo_url TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    # 4. Produce Records table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produce_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        crop_name TEXT NOT NULL,
        quantity REAL NOT NULL,
        unit TEXT NOT NULL DEFAULT 'Tons',
        price REAL,
        area TEXT NOT NULL,
        village TEXT,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        produce_type TEXT DEFAULT 'Field Crop',
        quality TEXT DEFAULT 'Grade A',
        availability_date TEXT NOT NULL,
        expected_harvest_date TEXT,
        source_type TEXT NOT NULL CHECK(source_type IN ('officer_local', 'farmer_verified', 'OFFICER_ENTRY', 'FARMER_VERIFIED')),
        farmer_id INTEGER,
        officer_id INTEGER,
        verification_status TEXT NOT NULL CHECK(verification_status IN ('VERIFIED', 'PENDING', 'REJECTED', 'UNAVAILABLE')),
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (farmer_id) REFERENCES users(id) ON DELETE SET NULL,
        FOREIGN KEY (officer_id) REFERENCES users(id) ON DELETE SET NULL
    );
    """)

    # 5. Verification Requests table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS verification_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_id INTEGER NOT NULL,
        officer_id INTEGER,
        produce_id INTEGER,
        crop_name TEXT NOT NULL,
        cultivated_area REAL,
        cultivated_area_unit TEXT DEFAULT 'Acres',
        expected_quantity REAL NOT NULL,
        quantity_unit TEXT NOT NULL DEFAULT 'Tons',
        expected_harvest_date TEXT,
        crop_stage TEXT DEFAULT 'Vegetative',
        quality TEXT DEFAULT 'Grade A',
        village TEXT,
        area TEXT NOT NULL,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        notes TEXT,
        status TEXT NOT NULL CHECK(status IN ('PENDING', 'VERIFIED', 'REJECTED')),
        officer_comment TEXT,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        reviewed_at TIMESTAMP,
        FOREIGN KEY (farmer_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (officer_id) REFERENCES users(id) ON DELETE SET NULL,
        FOREIGN KEY (produce_id) REFERENCES produce_records(id) ON DELETE SET NULL
    );
    """)

    # 6. Purchase Requests table (Buyer inquiries)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchase_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produce_id INTEGER NOT NULL,
        farmer_id INTEGER,
        buyer_name TEXT NOT NULL,
        buyer_contact TEXT NOT NULL,
        requested_quantity REAL NOT NULL,
        quantity_unit TEXT NOT NULL DEFAULT 'Tons',
        message TEXT,
        status TEXT NOT NULL DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (produce_id) REFERENCES produce_records(id) ON DELETE CASCADE,
        FOREIGN KEY (farmer_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    # 7. Sessions table (Token authentication)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        token TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL,
        role TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    # 8. Officer Registry table (Mock Agriculture Officer Registry)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS officer_registry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        officer_id TEXT NOT NULL UNIQUE,
        full_name TEXT NOT NULL,
        designation TEXT NOT NULL,
        department TEXT NOT NULL DEFAULT 'Department of Agriculture & Farmers Welfare',
        state TEXT NOT NULL,
        district TEXT NOT NULL,
        working_place TEXT NOT NULL,
        mobile TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'ACTIVE',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 9. Officer Accounts table (Verified Officer Account Credentials)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS officer_accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        officer_id TEXT NOT NULL UNIQUE,
        login_id TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        user_id INTEGER NOT NULL UNIQUE,
        account_status TEXT DEFAULT 'ACTIVE',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (officer_id) REFERENCES officer_registry(officer_id)
    );
    """)

    # 10. OTP Verifications table (Prototype OTP verification)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS otp_verifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        officer_id TEXT NOT NULL,
        otp_code TEXT NOT NULL,
        verification_token TEXT,
        expires_at TIMESTAMP NOT NULL,
        attempts INTEGER DEFAULT 0,
        verified INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 11. Password Reset Tokens table (Secure temporary OTP and reset token)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS password_reset_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        role TEXT NOT NULL,
        otp_code TEXT NOT NULL,
        reset_token TEXT,
        expires_at TIMESTAMP NOT NULL,
        attempts INTEGER DEFAULT 0,
        verified INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    # Check and migrate columns safely for existing databases
    cursor.execute("PRAGMA table_info(produce_records)")
    columns = [row["name"] for row in cursor.fetchall()]
    if "price" not in columns:
        cursor.execute("ALTER TABLE produce_records ADD COLUMN price REAL")

    cursor.execute("PRAGMA table_info(users)")
    user_cols = [row["name"] for row in cursor.fetchall()]
    if "officer_id" not in user_cols:
        cursor.execute("ALTER TABLE users ADD COLUMN officer_id TEXT")
    if "login_id" not in user_cols:
        cursor.execute("ALTER TABLE users ADD COLUMN login_id TEXT")

    cursor.execute("PRAGMA table_info(officer_profiles)")
    officer_cols = [row["name"] for row in cursor.fetchall()]
    if "officer_id" not in officer_cols:
        cursor.execute("ALTER TABLE officer_profiles ADD COLUMN officer_id TEXT")

    cursor.execute("PRAGMA table_info(purchase_requests)")
    pr_cols = [row["name"] for row in cursor.fetchall()]
    if "farmer_id" not in pr_cols:
        cursor.execute("ALTER TABLE purchase_requests ADD COLUMN farmer_id INTEGER")
    if "updated_at" not in pr_cols:
        cursor.execute("ALTER TABLE purchase_requests ADD COLUMN updated_at TIMESTAMP")

    # Migrate produce_records table schema if it lacks 'officer_local' constraint
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='produce_records'")
    p_sql_row = cursor.fetchone()
    if p_sql_row and "officer_local" not in p_sql_row["sql"]:
        cursor.execute("PRAGMA foreign_keys = OFF")
        cursor.execute("""
        CREATE TABLE produce_records_migration (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop_name TEXT NOT NULL,
            quantity REAL NOT NULL,
            unit TEXT NOT NULL DEFAULT 'Tons',
            price REAL,
            area TEXT NOT NULL,
            village TEXT,
            district TEXT NOT NULL,
            state TEXT NOT NULL,
            produce_type TEXT DEFAULT 'Field Crop',
            quality TEXT DEFAULT 'Grade A',
            availability_date TEXT NOT NULL,
            expected_harvest_date TEXT,
            source_type TEXT NOT NULL CHECK(source_type IN ('officer_local', 'farmer_verified', 'OFFICER_ENTRY', 'FARMER_VERIFIED')),
            farmer_id INTEGER,
            officer_id INTEGER,
            verification_status TEXT NOT NULL CHECK(verification_status IN ('VERIFIED', 'PENDING', 'REJECTED', 'UNAVAILABLE')),
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (farmer_id) REFERENCES users(id) ON DELETE SET NULL,
            FOREIGN KEY (officer_id) REFERENCES users(id) ON DELETE SET NULL
        )
        """)
        cursor.execute("""
        INSERT INTO produce_records_migration (
            id, crop_name, quantity, unit, price, area, village, district, state,
            produce_type, quality, availability_date, expected_harvest_date,
            source_type, farmer_id, officer_id, verification_status, notes,
            created_at, updated_at
        )
        SELECT id, crop_name, quantity, unit, price, area, village, district, state,
               produce_type, quality, availability_date, expected_harvest_date,
               CASE
                   WHEN source_type = 'OFFICER_ENTRY' THEN 'officer_local'
                   WHEN source_type = 'FARMER_VERIFIED' THEN 'farmer_verified'
                   ELSE source_type
               END,
               farmer_id, officer_id, verification_status, notes,
               created_at, updated_at
        FROM produce_records
        """)
        cursor.execute("DROP TABLE produce_records")
        cursor.execute("ALTER TABLE produce_records_migration RENAME TO produce_records")
        cursor.execute("PRAGMA foreign_keys = ON")

    # Safely migrate existing produce records to normalized source_types ('officer_local' & 'farmer_verified')
    cursor.execute("UPDATE produce_records SET source_type = 'officer_local' WHERE source_type = 'OFFICER_ENTRY'")
    cursor.execute("UPDATE produce_records SET source_type = 'farmer_verified' WHERE source_type = 'FARMER_VERIFIED'")

    # Backfill farmer_id in purchase_requests from associated produce_records
    cursor.execute("""
        UPDATE purchase_requests
        SET farmer_id = (SELECT farmer_id FROM produce_records WHERE produce_records.id = purchase_requests.produce_id)
        WHERE farmer_id IS NULL AND produce_id IN (SELECT id FROM produce_records WHERE farmer_id IS NOT NULL)
    """)

    # Migrate legacy status 'NEW' to 'pending'
    cursor.execute("UPDATE purchase_requests SET status = 'pending' WHERE LOWER(status) IN ('new', 'pending')")

    # Indexes for fast location and produce searches
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_produce_location ON produce_records(state, district, area);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_produce_crop ON produce_records(crop_name);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_produce_status ON produce_records(verification_status);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_produce_source ON produce_records(source_type);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_purchase_farmer ON purchase_requests(farmer_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_purchase_produce ON purchase_requests(produce_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_requests_status ON verification_requests(status);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_officer_location ON officer_profiles(state, district, assigned_area);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_officer_reg_id ON officer_registry(officer_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_officer_acc_officer_id ON officer_accounts(officer_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_officer_acc_login_id ON officer_accounts(login_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_reset_user ON password_reset_tokens(user_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_reset_token ON password_reset_tokens(reset_token);")

    # Automatically populate officer_registry if empty
    cursor.execute("SELECT COUNT(*) as cnt FROM officer_registry")
    if cursor.fetchone()["cnt"] == 0:
        seed_mock_officer_registry(cursor)

    conn.commit()
    conn.close()

def seed_mock_officer_registry(cursor):
    """Seed the mock officer registry with predefined demo records across India."""
    try:
        from mock_officer_registry import MOCK_OFFICER_REGISTRY
        for rec in MOCK_OFFICER_REGISTRY:
            cursor.execute("""
            INSERT OR IGNORE INTO officer_registry (
                officer_id, full_name, designation, department, state, district, working_place, mobile, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                rec["officer_id"],
                rec["full_name"],
                rec["designation"],
                rec.get("department", "Department of Agriculture & Farmers Welfare"),
                rec["state"],
                rec["district"],
                rec["working_place"],
                rec["mobile"],
                rec.get("status", "ACTIVE")
            ))
    except Exception as e:
        print(f"Warning: Failed to seed mock officer registry: {e}")


if __name__ == "__main__":
    init_db()
    print("Database schema successfully initialized.")
