# AgriFlow — Agricultural Produce Discovery & Verification Platform

> **"Discover. Verify. Connect."**

AgriFlow is a location-based agricultural produce discovery and verification platform designed for direct, trustworthy connections between **Farmers**, **Agriculture Officers**, and **Buyers**.

---

## 🌾 Core Purpose

AgriFlow builds a **verified local database of agricultural produce available or expected across specific local areas** (Country → State → District → Area/Village). 
- **Officers** maintain and verify local area supplies.
- **Farmers** record active cultivations and request local verification.
- **Buyers** discover verified supplies by location and volume with **zero login barriers**.

> **No unnecessary infrastructure**: AgriFlow operates without requiring IoT devices, blockchain, drones, cold-storage integrations, or fake API claims. It focuses purely on verified local supply and location discovery.

---

## 👥 User Roles & Access

| Role | Access | Key Capabilities |
| :--- | :--- | :--- |
| **Agriculture Officer** | Officer Portal & Dashboard | Maintain officer profile (Designation, Department, Assigned Area, District, State). Directly add verified local produce records. Review pending farmer requests in their jurisdiction. Verify or reject submissions. Update quantities or mark produce unavailable. |
| **Farmer** | Farmer Portal & Dashboard | Maintain farming profile (Land Area, Unit, Farming Type, Village, District, State). Add crop cultivation details and submit for verification. Automatic routing to assigned local AAO. Live status tracking (🟡 Pending → 🟢 Verified / 🔴 Rejected). |
| **Buyer / Public** | Public View Produce | **No login required.** Search by crop name, State, District, Area, Quantity range, and Availability date. View detailed quality grades and officer verification notes. Send direct purchase inquiries. |

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+ (tested on Python 3.14)
- Packages: `fastapi`, `uvicorn` (already installed)

### 2. Launch the Application
Run the batch file:
```cmd
run.bat
```
Or run directly via command prompt / PowerShell:
```cmd
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser at:
**`http://127.0.0.1:8000`**

---

## 🎯 13-Step Primary Demonstration Flow

AgriFlow includes pre-configured seed data for demonstrating produce discovery, officer verification, and buyer workflows.

### Step-by-Step Flow:
1. **Officer Login**: Sign in via the Login modal with `ravi.kumar@agri.tn.gov.in` / `officer123`.
2. **Officer Profile**: Review Ravi Kumar's profile (Assistant Agricultural Officer, Sankari, Salem, Tamil Nadu).
3. **Officer Adds Onion**: Click **+ Add Produce** → Onion, 15 Tons, Price: ₹ 22,000 / Ton, Sankari, Salem → status is immediately **✓ Verified**.
4. **Officer Adds Tomato**: Add Tomato, 16 Tons, Price: ₹ 18,000 / Ton, Sankari, Salem → status is immediately **✓ Verified**.
5. **Farmer Login**: Sign in via the Login modal with `9123456780` / `farmer123`.
6. **Farmer Adds Crop**: Click **+ Add Crop** → Onion, 2 Acres, 5 Tons expected, Harvest: 25 September, Sankari, Salem.
7. **Farmer Submits Request**: Status immediately becomes **🟡 Pending Verification** and auto-routes to Officer Ravi Kumar.
8. **Officer Sees Request**: Log in as Officer Ravi Kumar → view the pending request from Farmer Kumar in the verification queue.
9. **Officer Verifies It**: Click **VERIFY** → produce record status becomes **🟢 ✓ Verified**.
10. **Produce Becomes Searchable**: Real-time WebSocket notifies all clients instantly.
11. **Buyer Opens Discovery**: Navigate to "View Produce" (`http://127.0.0.1:8000/#produce`).
12. **Search Results**: Filter for **Onion** → **Salem** → **Sankari**:
    - **15 Tons** (Officer-recorded verified produce with price)
    - **5 Tons** (Farmer-submitted verified produce)
13. **Buyer Purchase Inquiry**: Click **View Details** on any produce and send a purchase request with contact details and requested quantity.

---

## 🧪 Automated Testing

To run the complete automated test suite covering all 13 steps and SQLite data integrity:
```cmd
python test_flow.py
```
Expected output:
```
=======================================================
>>> ALL 13 DEMO STEPS & CORE SYSTEM TESTS PASSED 100%! <<<
=======================================================
```

---

## 🛠️ Architecture & Tech Stack

- **Backend**: FastAPI (Asynchronous Python REST API + WebSockets)
- **Database**: SQLite3 (`agriflow.db`) with foreign keys and composite indexes on `(state, district, area)`
- **Authentication**: Salted PBKDF2 password hashing + persistent SQLite session tokens
- **Real-Time Sync**: WebSocket broadcaster (`/ws`) updating dashboards and search grids live
- **Frontend**: Responsive Single Page Application (HTML5, Tailwind CSS, Lucide Icons, Vanilla ES6)
- **Demo Dock**: Collapsible floating bar for seamless switching during hackathon presentations
