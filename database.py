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
        area TEXT NOT NULL,
        village TEXT,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        produce_type TEXT DEFAULT 'Field Crop',
        quality TEXT DEFAULT 'Grade A',
        availability_date TEXT NOT NULL,
        expected_harvest_date TEXT,
        source_type TEXT NOT NULL CHECK(source_type IN ('OFFICER_ENTRY', 'FARMER_VERIFIED')),
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
        buyer_name TEXT NOT NULL,
        buyer_contact TEXT NOT NULL,
        requested_quantity REAL NOT NULL,
        quantity_unit TEXT NOT NULL DEFAULT 'Tons',
        message TEXT,
        status TEXT NOT NULL DEFAULT 'NEW',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (produce_id) REFERENCES produce_records(id) ON DELETE CASCADE
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

    # Indexes for fast location and produce searches
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_produce_location ON produce_records(state, district, area);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_produce_crop ON produce_records(crop_name);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_produce_status ON produce_records(verification_status);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_requests_status ON verification_requests(status);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_officer_location ON officer_profiles(state, district, assigned_area);")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database schema successfully initialized.")
