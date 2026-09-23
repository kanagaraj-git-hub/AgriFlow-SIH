# -*- coding: utf-8 -*-
"""
AgriFlow Master Locale Generator
Generates:
1. static/i18n/locales/{code}.json for all 23 languages
2. static/i18n/languages.js containing metadata and pre-cached dictionaries
"""

import json
import os
import sys
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

LOCALES_DIR = os.path.join(os.path.dirname(__file__), "static", "i18n", "locales")
os.makedirs(LOCALES_DIR, exist_ok=True)

# Master English dictionary
EN = {
  "lang": {
    "name": "English",
    "nativeName": "English",
    "code": "en",
    "dir": "ltr"
  },
  "common": {
    "language": "Language",
    "login": "Login",
    "register": "Register",
    "logout": "Logout",
    "dashboard": "Dashboard",
    "profile": "Profile",
    "save": "Save",
    "cancel": "Cancel",
    "close": "Close",
    "submit": "Submit",
    "refresh": "Refresh",
    "search": "Search",
    "clearFilters": "Clear Filters",
    "loading": "Loading...",
    "viewDetails": "View Details",
    "allStates": "All States",
    "allDistricts": "All Districts",
    "allAreas": "All Areas",
    "verified": "Verified",
    "pending": "Pending",
    "rejected": "Rejected",
    "available": "Available",
    "unavailable": "Unavailable",
    "yes": "Yes",
    "no": "No",
    "continue": "Continue",
    "send": "Send",
    "back": "Back",
    "next": "Next",
    "previous": "Previous",
    "edit": "Edit",
    "delete": "Delete",
    "status": "Status",
    "role": "Role",
    "user": "User",
    "liveSync": "Live Sync",
    "reconnecting": "Live Sync",
    "reset": "Reset",
    "actions": "Actions",
    "crop": "Crop",
    "quantity": "Quantity",
    "location": "Location",
    "date": "Date",
    "notes": "Notes",
    "category": "Category",
    "unit": "Unit",
    "grade": "Grade",
    "volume": "Volume",
    "state": "State",
    "district": "District",
    "area": "Area",
    "error": "Error",
    "success": "Success"
  },
  "navigation": {
    "home": "Home",
    "viewProduce": "View Produce",
    "officerPortal": "Officer Portal",
    "farmerPortal": "Farmer Portal",
    "dashboard": "Dashboard",
    "profile": "Profile",
    "requests": "Requests",
    "addProduce": "Add Produce",
    "addCrop": "Add Crop",
    "myRequests": "My Requests",
    "farmerRequests": "Farmer Requests",
    "liveSync": "Live Sync"
  },
  "auth": {
    "roleSelector": "Select Your Role",
    "selectRole": "Select Your Role",
    "agricultureOfficer": "Agriculture Officer",
    "farmer": "Farmer",
    "login": "Login",
    "register": "Register",
    "loginTab": "Login",
    "registerTab": "Register",
    "mobileOrEmail": "Mobile Number or Email",
    "identifier": "Mobile Number or Email",
    "identifierPlaceholder": "e.g. 9876543210 or email",
    "password": "Password",
    "passwordPlaceholder": "••••••••",
    "signIn": "Sign In",
    "fullName": "Full Name",
    "fullNamePlaceholder": "e.g. Ravi Kumar",
    "mobileNumber": "Mobile Number",
    "phonePlaceholder": "9876543210",
    "emailOptional": "Email (Optional)",
    "emailPlaceholder": "name@domain.com",
    "createAccount": "Create Account",
    "designation": "Designation",
    "department": "Department",
    "assignedArea": "Assigned Area",
    "district": "District",
    "state": "State",
    "village": "Village",
    "landArea": "Land Area (Acres)",
    "farmingType": "Farming Type",
    "conventional": "Conventional",
    "organic": "Organic",
    "naturalFarming": "Natural Farming",
    "officialEmail": "Official Email",
    "welcomeBack": "Welcome back, {{name}}!",
    "accountCreated": "Account created! Welcome, {{name}}.",
    "invalidCredentials": "Invalid login credentials",
    "requiredFields": "Please fill in all required fields (Name, Mobile, Password).",
    "demoLoginFailed": "Demo login failed",
    "networkError": "Network error",
    "logoutSuccess": "You have been signed out.",
    "officerLoginRequired": "Please log in as an Agriculture Officer to access the Officer Portal.",
    "farmerLoginRequired": "Please log in as a Farmer to access the Farmer Portal.",
    "registrationFailed": "Registration failed. Please check your details.",
    "switchedRole": "Switched to {{role}}"
  },
  "landing": {
    "verifiedPlatform": "Verified Local Produce Platform",
    "title": "Discover. Verify. Connect.",
    "tagline": "Discover. Verify. Connect.",
    "subtitle": "AgriFlow helps farmers and agriculture officers maintain verified local agricultural produce information, making it easier for buyers to discover available produce by location, crop, and quantity.",
    "searchVerifiedProduce": "Search Verified Produce",
    "findVerifiedProduce": "Find Verified Produce",
    "quickDiscovery": "Quick Produce Discovery by Area",
    "cropName": "Crop Name",
    "cropPlaceholder": "e.g. Onion, Tomato...",
    "state": "State",
    "district": "District",
    "allStates": "All States",
    "allDistricts": "All Districts",
    "howItWorks": "How AgriFlow Works",
    "workflowIntro": "A simple, transparent, and location-grounded verification workflow connecting local agriculture to open markets.",
    "tagLine": "Discover. Verify. Connect."
  },
  "howItWorks": {
    "farmerSubmission": "Farmer Submission",
    "farmerSubmissionDesc": "Farmers record their active cultivation details, land size, crop stages, and upcoming yields for location verification.",
    "officerVerification": "Officer Verification",
    "officerVerificationDesc": "Local Agriculture Officers review incoming farmer submissions, perform field verification, and publish verified produce.",
    "publicDiscovery": "Public Discovery & Contact",
    "publicDiscoveryDesc": "Buyers easily discover verified produce by crop, district, and volume with direct contact and zero login barriers."
  },
  "roles": {
    "officer": "Agriculture Officer",
    "farmer": "Farmer",
    "farmers": "For Farmers",
    "officers": "For Agriculture Officers",
    "buyers": "For Buyers & Traders",
    "farmerTitle": "Direct Visibility for Harvests",
    "officerTitle": "Jurisdiction Control & Trust",
    "buyerTitle": "Verified Supply Discovery",
    "farmerItem1": "Register farming profiles and cultivated lands",
    "farmerItem2": "Submit upcoming harvest yields for local verification",
    "farmerItem3": "Track real-time status: Pending → Verified / Rejected",
    "officerItem1": "Directly add verified local area agricultural produce",
    "officerItem2": "Review and field-verify farmer requests in your block",
    "officerItem3": "Update quantities, availability, and mark unavailable",
    "buyerItem1": "Discover produce with zero login barriers",
    "buyerItem2": "Filter by State, District, Area, and Volume",
    "buyerItem3": "Send direct purchase inquiries to verified suppliers"
  },
  "produce": {
    "loading": "Loading verified produce records...",
    "submitError": "Failed to submit request",
    "title": "Verified Produce Discovery",
    "subtitle": "Discover available and upcoming agricultural produce verified by local Agriculture Officers.",
    "searchCropName": "Search Crop Name",
    "state": "State",
    "district": "District",
    "areaBlock": "Area / Block",
    "minQty": "Min Qty (Tons)",
    "maxQty": "Max Qty (Tons)",
    "availBefore": "Available Before / On",
    "verifiedOnly": "Verified Only (Recommended)",
    "clearFilters": "Clear Filters",
    "count": "Showing {{count}} verified produce record",
    "countPlural": "Showing {{count}} verified produce records",
    "emptyTitle": "No Produce Records Found",
    "emptyDescription": "Try broadening your search or clearing filters to discover other available crops across nearby areas.",
    "resetAllFilters": "Reset All Filters",
    "autoSynced": "Auto-synced via WebSocket",
    "availableQuantity": "Available Quantity",
    "quality": "Quality",
    "availability": "Availability",
    "sourceOfficer": "Officer Verified",
    "sourceFarmer": "Farmer Verified",
    "verifiedBadge": "✓ VERIFIED",
    "qualityGrade": "Quality Grade",
    "verificationSource": "Verification Source",
    "fieldNotes": "Officer Verification & Field Notes",
    "purchaseTitle": "Send Purchase Inquiry / Procurement Request",
    "purchaseSubtitle": "Submit your requirement directly to connect with the verified producer / local officer.",
    "yourName": "Your Name / Company",
    "contact": "Contact Number / Email",
    "requestedQty": "Requested Quantity",
    "message": "Message / Requirements",
    "sendRequest": "Send Purchase Request",
    "notFound": "Produce record not found",
    "noLogin": "No login required",
    "unitLabel": "Unit",
    "price": "Price",
    "price_per_ton": "Price per Ton",
    "price_per_quintal": "Price per Quintal",
    "price_per_kg": "Price per kg",
    "pricePerTon": "Price per Ton",
    "pricePerQuintal": "Price per Quintal",
    "pricePerKg": "Price per kg",
    "enter_price": "Enter price per unit",
    "enterPrice": "Enter price per unit",
    "invalid_price": "Please enter a valid positive price",
    "invalidPrice": "Please enter a valid positive price",
    "price_per_selected_unit": "Price per selected unit",
    "pricePerUnit": "Price per selected unit",
    "price_on_inquiry": "On Inquiry",
    "priceOnInquiry": "On Inquiry",
    "viewDetails": "View Details",
    "viewProduct": "View Product",
    "verifiedByOfficer": "Verified by Officer",
    "officerVerified": "Officer Verified",
    "contactSeller": "Contact Seller",
    "agricultureOfficer": "Agriculture Officer",
    "assistantAgriOfficer": "Assistant Agricultural Officer",
    "assignedJurisdiction": "Assigned Jurisdiction",
    "grade": "Grade",
    "category": "Category",
    "crop": "Crop",
    "quantity": "Quantity",
    "unit": "Unit",
    "tons": "Tons",
    "verified": "Verified",
    "available": "Available",
    "unavailable": "Unavailable",
    "pending": "Pending",
    "rejected": "Rejected",
    "badge_verified": "✓ VERIFIED",
    "avail_qty": "Available Quantity",
    "btn_contact_seller": "Contact Seller"
  },
  "officer": {
    "portal": "Agriculture Officer Portal",
    "subtitle": "Maintain local jurisdiction produce, verify farmer submissions",
    "profile": "Edit Profile",
    "assistantAgriOfficer": "Assistant Agricultural Officer",
    "assignedJurisdiction": "Assigned Jurisdiction",
    "totalRecords": "Total Records",
    "totalRecordsHint": "In your assigned area",
    "availableQty": "Available Quantity",
    "availableQtyHint": "Verified local produce",
    "farmerRequests": "Farmer Requests",
    "pending": "Pending field verification",
    "pendingHint": "Pending field verification",
    "verifiedRecords": "Verified Records",
    "verifiedRecordsHint": "Published to buyers",
    "queueTitle": "Farmer Verification Requests",
    "queueSubtitle": "Farmers in your assigned area awaiting your field verification",
    "queueEmpty": "All caught up! No pending farmer submissions in your area.",
    "queueEmptyDesc": "No pending farmer submissions in your area.",
    "refreshRequests": "Refresh Requests",
    "localProduceTitle": "Local Area Agricultural Produce",
    "localProduceSubtitle": "Produce records maintained and published for your jurisdiction",
    "addProduce": "+ Add Produce",
    "editProduce": "Edit Local Produce",
    "addProduceModalTitle": "+ Add Local Produce",
    "modalSubtitle": "Produce entered directly by Agriculture Officer will be marked as",
    "savePublish": "Save & Publish Produce",
    "verify": "VERIFY",
    "reject": "REJECT",
    "pendingBadge": "🟡 Pending Verification",
    "directOfficerEntry": "Direct Officer Entry",
    "markUnavailable": "Mark Unavailable",
    "markAvailable": "Mark Available",
    "editProduceAction": "Edit Produce",
    "deleteProduce": "Delete produce record",
    "deleteConfirm": "Are you sure you want to delete this produce record?",
    "rejectTitle": "Reject Farmer Request",
    "rejectDescription": "Please provide a constructive reason for rejection",
    "rejectionReason": "Rejection Reason / Correction Required",
    "rejectionPlaceholder": "e.g. Yield estimate does not match cultivated land size; please re-measure.",
    "confirmRejection": "Confirm Rejection",
    "fieldInspected": "Field inspected and verified by AAO",
    "verificationSuccess": "✓ Farmer submission verified and published to public View Produce!",
    "rejectionSuccess": "Request rejected and feedback sent to farmer.",
    "provideReason": "Please provide a reason for rejection",
    "noProduceYet": "No produce records recorded yet in your area.",
    "cropCol": "Crop",
    "qtyCol": "Quantity",
    "priceCol": "Price",
    "locationCol": "Location",
    "availDateCol": "Available Date",
    "qualityCol": "Quality",
    "sourceCol": "Source",
    "statusCol": "Status",
    "actionsCol": "Actions",
    "officerRecordedSuccess": "✓ Produce recorded and verified directly by Officer!",
    "updateProduceSuccess": "Produce updated successfully"
  },
  "farmer": {
    "portal": "Farmer Portal",
    "myProfile": "My Farming Profile",
    "assignedOfficer": "Your Assigned Local Agriculture Officer",
    "assignedOfficerHint": "Verified Submissions Route Here",
    "verifiedRoute": "✓ Verified Submissions Route Here",
    "totalSubmissions": "Total Submissions",
    "cropRecords": "Crop records",
    "pending": "Pending",
    "pendingReview": "Awaiting officer review",
    "verified": "Verified & Active",
    "visibleToBuyers": "Visible to buyers",
    "rejected": "Rejected",
    "needsRevision": "Needs revision",
    "requestsTitle": "My Crop Verification Requests",
    "requestsSubtitle": "Track verification status from your local Agriculture Officer",
    "addCrop": "+ Add Crop Details",
    "addCropButton": "+ Add Crop",
    "myCropDetails": "+ Add Farming Crop Details",
    "submittedToOfficer": "Submitted details will be sent to your local Agriculture Officer for verification",
    "submitToOfficer": "Submit to Local Officer",
    "noCrops": "No crops submitted yet",
    "noCropsDescription": "Add your current cultivation details to request local verification.",
    "addFirstCrop": "Add First Crop",
    "pendingStatus": "🟡 Pending Verification",
    "verifiedStatus": "🟢 ✓ Verified",
    "rejectedStatus": "🔴 Rejected",
    "expectedHarvest": "Expected Harvest",
    "cultivatedArea": "Cultivated Area",
    "expectedYield": "Expected Yield",
    "expectedQty": "Expected Quantity",
    "cropStage": "Crop Stage",
    "officerFeedback": "Officer Feedback:",
    "submissionSuccess": "✓ Crop submitted! Sent to local Agriculture Officer for verification.",
    "verificationStatus": "Pending → Verified / Rejected",
    "locationRouting": "Location Routing (Routes to Local AAO)",
    "additionalNotes": "Additional Farming Notes",
    "farmingNotesPlaceholder": "Farming methods, irrigation, fertilizer details..."
  },
  "profile": {
    "title": "My Profile",
    "subtitle": "Manage your account information and jurisdictional/farming details",
    "saveChanges": "Save Profile Changes",
    "fullName": "Full Name",
    "village": "Village",
    "area": "Area / Block",
    "district": "District",
    "state": "State",
    "landArea": "Land Area",
    "landUnit": "Land Unit",
    "farmingType": "Farming Type",
    "officialEmail": "Official Email",
    "designation": "Officer Designation",
    "department": "Department",
    "contactNumber": "Contact Number",
    "assignedArea": "Assigned Area / Block",
    "profileUpdated": "Profile updated successfully"
  },
  "crops": {
    "onion": "Onion",
    "tomato": "Tomato",
    "potato": "Potato",
    "rice": "Rice / Paddy",
    "wheat": "Wheat",
    "maize": "Maize / Corn",
    "carrot": "Carrot",
    "cabbage": "Cabbage",
    "cauliflower": "Cauliflower",
    "garlic": "Garlic",
    "ginger": "Ginger",
    "banana": "Banana",
    "mango": "Mango",
    "groundnut": "Groundnut",
    "sugarcane": "Sugarcane",
    "cotton": "Cotton"
  },
  "produce_types": {
    "tubers": "Tubers",
    "vegetable": "Vegetable",
    "vegetable_bulbs": "Vegetable / Bulbs",
    "field_crop": "Field Crop",
    "cereals": "Cereals / Grains",
    "fruits": "Fruits",
    "cash_crops": "Cash Crops",
    "spices": "Spices"
  },
  "units": {
    "tons": "Tons",
    "quintals": "Quintals",
    "kg": "kg",
    "acres": "Acres",
    "hectares": "Hectares"
  },
  "qualities": {
    "gradeA": "Grade A",
    "gradeB": "Grade B",
    "gradeC": "Grade C",
    "gradeAPremium": "Grade A (Premium)",
    "gradeBStandard": "Grade B (Standard)",
    "gradeCFair": "Grade C (Fair)"
  },
  "crop_stages": {
    "bulbDevelopment": "Bulb Development",
    "vegetative": "Vegetative",
    "flowering": "Flowering",
    "readyForHarvest": "Ready for Harvest",
    "preHarvest": "Pre-Harvest"
  },
  "status": {
    "verified": "Verified",
    "pending": "Pending",
    "rejected": "Rejected",
    "available": "Available",
    "unavailable": "Unavailable",
    "Verified": "Verified",
    "Pending": "Pending",
    "Rejected": "Rejected",
    "Available": "Available",
    "Unavailable": "Unavailable"
  },
  "statuses": {
    "verified": "Verified",
    "pending": "Pending",
    "rejected": "Rejected",
    "available": "Available",
    "unavailable": "Unavailable",
    "Verified": "Verified",
    "Pending": "Pending",
    "Rejected": "Rejected",
    "Available": "Available",
    "Unavailable": "Unavailable"
  },
  "sources": {
    "officerVerified": "Officer Verified",
    "farmerVerified": "Farmer Verified",
    "directOfficerEntry": "Direct Officer Entry"
  },
  "notifications": {
    "newProduceAdded": "🌾 New produce added: {{crop}} ({{qty}} {{unit}}) in {{area}}",
    "produceUpdated": "🔄 Produce updated: {{crop}}",
    "newFarmerSubmission": "📋 New Farmer crop submission: {{crop}} ({{qty}} {{unit}}) in {{area}}",
    "cropVerified": "✅ Crop verified: {{crop}} ({{qty}} {{unit}}) in {{area}}",
    "farmerRequestRejected": "⚠️ Farmer request rejected: {{crop}}",
    "purchaseInquiry": "💼 Purchase Inquiry: Buyer requested {{qty}} {{unit}} of {{crop}}",
    "demoReset": "🔄 Demo data has been reset to initial state",
    "inquirySent": "✓ Purchase inquiry sent to producer / local officer!",
    "statusUpdated": "Produce status updated",
    "deleted": "Produce record deleted"
  }
}

from locales_group1 import LOCALES_GROUP_1
from locales_group2 import LOCALES_GROUP_2
from locales_group3 import LOCALES_GROUP_3
from locales_group4 import LOCALES_GROUP_4
from locales_group5 import LOCALES_GROUP_5
from update_locales_data import PRODUCE_TRANSLATIONS

ALL_LOCALES = { "en": EN }
ALL_LOCALES.update(LOCALES_GROUP_1)
ALL_LOCALES.update(LOCALES_GROUP_2)
ALL_LOCALES.update(LOCALES_GROUP_3)
ALL_LOCALES.update(LOCALES_GROUP_4)
ALL_LOCALES.update(LOCALES_GROUP_5)

EXTRA_TARGETED_PRODUCE = {
    "ta": {
        "viewProduct": "விளைபொருளைக் காண்க",
        "contactSeller": "விற்பனையாளரைத் தொடர்பு கொள்க",
        "assistantAgriOfficer": "உதவி வேளாண்மை அதிகாரி",
        "assignedJurisdiction": "ஒதுக்கப்பட்ட அதிகார வரம்பு",
        "grade": "தரம்",
        "category": "வகை",
        "volume": "அளவு"
    },
    "hi": {
        "viewProduct": "उत्पाद देखें",
        "contactSeller": "विक्रेता से संपर्क करें",
        "assistantAgriOfficer": "सहायक कृषि अधिकारी",
        "assignedJurisdiction": "आवंटित अधिकार क्षेत्र",
        "grade": "ग्रेड",
        "category": "श्रेणी",
        "volume": "मात्रा"
    },
    "ur": {
        "viewProduct": "پیداوار دیکھیں",
        "contactSeller": "بیچنے والے سے رابطہ کریں",
        "assistantAgriOfficer": "اسسٹنٹ اگریکلچرل آفیسر",
        "assignedJurisdiction": "مقررہ دائرہ اختیار",
        "grade": "گریڈ",
        "category": "قسم",
        "volume": "مقدار"
    },
    "te": {
        "viewProduct": "ఉత్పత్తిని చూడండి",
        "contactSeller": "విక్రేతను సంప్రదించండి",
        "assistantAgriOfficer": "సహాయ వ్యవసాయ అధికారి",
        "assignedJurisdiction": "కేటాయించిన పరిధి",
        "grade": "గ్రేడ్",
        "category": "వర్గం",
        "volume": "పరిమాణం"
    },
    "kn": {
        "viewProduct": "ಉತ್ಪನ್ನವನ್ನು ವೀಕ್ಷಿಸಿ",
        "contactSeller": "ಮಾರಾಟಗಾರರನ್ನು ಸಂಪರ್ಕಿಸಿ",
        "assistantAgriOfficer": "ಸಹಾಯಕ ಕೃಷಿ ಅಧಿಕಾರಿ",
        "assignedJurisdiction": "ನಿಯೋಜಿತ ಅಧಿಕಾರ ವ್ಯಾಪ್ತಿ",
        "grade": "ಗ್ರೇಡ್",
        "category": "ವರ್ಗ",
        "volume": "ಪ್ರಮಾಣ"
    },
    "ml": {
        "viewProduct": "ഉൽപ്പന്നം കാണുക",
        "contactSeller": "വിൽപ്പനക്കാരനെ ബന്ധപ്പെടുക",
        "assistantAgriOfficer": "അസിസ്റ്റന്റ് അഗ്രികൾച്ചറൽ ഓഫീസർ",
        "assignedJurisdiction": "നിയുക്ത അധികാരപരിധി",
        "grade": "ഗ്രേഡ്",
        "category": "വിഭാഗം",
        "volume": "അളവ്"
    },
    "bn": {
        "viewProduct": "পণ্য দেখুন",
        "contactSeller": "বিক্রেতার সাথে যোগাযোগ করুন",
        "assistantAgriOfficer": "সহকারী কৃষি কর্মকর্তা",
        "assignedJurisdiction": "নির্ধারিত এখতিয়ার",
        "grade": "গ্রেড",
        "category": "বিভাগ",
        "volume": "আয়তন"
    },
    "mr": {
        "viewProduct": "उत्पादन पहा",
        "contactSeller": "विक्रेत्याशी संपर्क साधा",
        "assistantAgriOfficer": "सहाय्यक कृषी अधिकारी",
        "assignedJurisdiction": "नियुक्त अधिकार क्षेत्र",
        "grade": "श्रेणी/दर्जा",
        "category": "प्रवर्ग",
        "volume": "प्रमाण"
    },
    "gu": {
        "viewProduct": "ઉત્પાદન જુઓ",
        "contactSeller": "વિક્રેતાનો સંપર્ક કરો",
        "assistantAgriOfficer": "મદદનીશ કૃષિ અધિકારી",
        "assignedJurisdiction": "સોંપાયેલ અધિકારક્ષેત્ર",
        "grade": "ગ્રેડ",
        "category": "શ્રેણી",
        "volume": "જથ્થો"
    }
}

# Clean any demo blocks and enrich with all produce translations
for code, loc_data in ALL_LOCALES.items():
    if "demo" in loc_data:
        del loc_data["demo"]
    if "landing" in loc_data and "sihPlatform" in loc_data["landing"]:
        del loc_data["landing"]["sihPlatform"]
    trans = PRODUCE_TRANSLATIONS.get(code, PRODUCE_TRANSLATIONS["en"])
    if "produce" in loc_data:
        loc_data["produce"].update(trans)
        if code in EXTRA_TARGETED_PRODUCE:
            loc_data["produce"].update(EXTRA_TARGETED_PRODUCE[code])
        
        p = loc_data["produce"]
        c = loc_data.get("common", {})
        u = loc_data.get("units", {})
        a = loc_data.get("auth", {})
        o = loc_data.get("officer", {})
        
        p.setdefault("viewDetails", c.get("viewDetails", "View Details"))
        p.setdefault("viewProduct", p.get("viewProduct", p.get("viewDetails", "View Product")))
        p.setdefault("verifiedByOfficer", p.get("sourceOfficer", "Verified by Officer"))
        p.setdefault("officerVerified", p.get("sourceOfficer", "Officer Verified"))
        p.setdefault("contactSeller", p.get("contactSeller", c.get("send", "Contact Seller")))
        p.setdefault("agricultureOfficer", a.get("agricultureOfficer", "Agriculture Officer"))
        p.setdefault("assistantAgriOfficer", o.get("assistantAgriOfficer", a.get("designation", "Assistant Agricultural Officer")))
        p.setdefault("assignedJurisdiction", o.get("assignedJurisdiction", a.get("assignedArea", "Assigned Jurisdiction")))
        p.setdefault("grade", p.get("qualityGrade", "Grade"))
        p.setdefault("category", c.get("crop", "Category"))
        p.setdefault("crop", c.get("crop", "Crop"))
        p.setdefault("quantity", c.get("quantity", "Quantity"))
        p.setdefault("unit", p.get("unitLabel", "Unit"))
        p.setdefault("tons", u.get("tons", "Tons"))
        p.setdefault("verified", c.get("verified", "Verified"))
        p.setdefault("available", c.get("available", "Available"))
        p.setdefault("unavailable", c.get("unavailable", "Unavailable"))
        p.setdefault("pending", c.get("pending", "Pending"))
        p.setdefault("rejected", c.get("rejected", "Rejected"))
        p.setdefault("badge_verified", p.get("verifiedBadge", "✓ VERIFIED"))
        p.setdefault("avail_qty", p.get("availableQuantity", "Available Quantity"))
        p.setdefault("btn_contact_seller", p.get("contactSeller", "Contact Seller"))
    
    if "officer" in loc_data:
        p = loc_data.get("produce", {})
        loc_data["officer"].setdefault("assistantAgriOfficer", p.get("assistantAgriOfficer", "Assistant Agricultural Officer"))
        loc_data["officer"].setdefault("assignedJurisdiction", p.get("assignedJurisdiction", "Assigned Jurisdiction"))
        loc_data["officer"]["priceCol"] = trans.get("priceCol", trans.get("price", "Price"))

    if "farmer" in loc_data:
        f = loc_data["farmer"]
        f.setdefault("expectedQty", f.get("expectedYield", "Expected Quantity"))
        f.setdefault("verifiedRoute", f.get("assignedOfficerHint", "✓ Verified Submissions Route Here"))
        f.setdefault("pendingReview", "Awaiting officer review")
        f.setdefault("visibleToBuyers", "Visible to buyers")
        f.setdefault("needsRevision", "Needs revision")

    if "auth" in loc_data:
        a = loc_data["auth"]
        c = loc_data.get("common", {})
        a.setdefault("login", c.get("login", "Login"))
        a.setdefault("register", c.get("register", "Register"))
        a.setdefault("loginTab", a.get("login", c.get("login", "Login")))
        a.setdefault("registerTab", a.get("register", c.get("register", "Register")))
        a.setdefault("fullNamePlaceholder", a.get("fullName", "e.g. Ravi Kumar"))
        a.setdefault("passwordPlaceholder", "••••••••")

    if "profile" in loc_data:
        pr = loc_data["profile"]
        c = loc_data.get("common", {})
        a = loc_data.get("auth", {})
        pr.setdefault("fullName", a.get("fullName", "Full Name"))
        pr.setdefault("district", c.get("district", "District"))
        pr.setdefault("state", c.get("state", "State"))
        pr.setdefault("village", a.get("village", "Village"))
        pr.setdefault("area", c.get("area", "Area / Block"))

    if code == "ta":
        if "roles" in loc_data:
            loc_data["roles"]["officer"] = "வேளாண் அதிகாரி"
            loc_data["roles"]["farmer"] = "விவசாயி"
            loc_data["roles"]["farmers"] = "விவசாயிகளுக்கு"
            loc_data["roles"]["officers"] = "வேளாண் அதிகாரிகளுக்கு"
            loc_data["roles"]["buyers"] = "வாங்குபவர்கள் மற்றும் வர்த்தகர்களுக்கு"
        if "auth" in loc_data:
            loc_data["auth"]["loginTab"] = "உள்நுழைக"
            loc_data["auth"]["registerTab"] = "பதிவுசெய்க"
            loc_data["auth"]["fullNamePlaceholder"] = "எ.கா. ரவி குமார்"
        if "farmer" in loc_data:
            loc_data["farmer"]["expectedQty"] = "எதிர்பார்க்கப்படும் மகசூல்"
            loc_data["farmer"]["pendingReview"] = "அதிகாரி ஆய்வுக்குக் காத்திருக்கிறது"
            loc_data["farmer"]["visibleToBuyers"] = "வாங்குவோருக்குத் தெரியும்"
            loc_data["farmer"]["needsRevision"] = "திருத்தம் தேவை"
            loc_data["farmer"]["verifiedRoute"] = "✓ சரிபார்க்கப்பட்ட சமர்ப்பிப்புகள் இங்கு செல்லும்"
        if "profile" in loc_data:
            loc_data["profile"]["title"] = "என் சுயவிவரம்"
            loc_data["profile"]["subtitle"] = "கணக்கு மற்றும் விவசாய/அதிகார வரம்பு விவரங்களை நிர்வகிக்கவும்"
            loc_data["profile"]["saveChanges"] = "சுயவிவர மாற்றங்களைச் சேமி"
    elif code == "hi":
        if "roles" in loc_data:
            loc_data["roles"]["officer"] = "कृषि अधिकारी"
            loc_data["roles"]["farmer"] = "किसान"
            loc_data["roles"]["farmers"] = "किसानों के लिए"
            loc_data["roles"]["officers"] = "कृषि अधिकारियों के लिए"
            loc_data["roles"]["buyers"] = "खरीदारों और व्यापारियों के लिए"
        if "auth" in loc_data:
            loc_data["auth"]["loginTab"] = "लॉग इन"
            loc_data["auth"]["registerTab"] = "पंजीकरण"
            loc_data["auth"]["fullNamePlaceholder"] = "उदा. रवि कुमार"
        if "farmer" in loc_data:
            loc_data["farmer"]["expectedQty"] = "अपेक्षित उपज"
            loc_data["farmer"]["pendingReview"] = "अधिकारी समीक्षा की प्रतीक्षा"
            loc_data["farmer"]["visibleToBuyers"] = "खरीदारों को दृश्यमान"
            loc_data["farmer"]["needsRevision"] = "संशोधन आवश्यक"
            loc_data["farmer"]["verifiedRoute"] = "✓ सत्यापित प्रस्तुतियाँ यहाँ भेजी जाती हैं"
        if "profile" in loc_data:
            loc_data["profile"]["title"] = "मेरी प्रोफ़ाइल"
            loc_data["profile"]["subtitle"] = "अपनी खाता जानकारी और अधिकार क्षेत्र/खेती विवरण प्रबंधित करें"
            loc_data["profile"]["saveChanges"] = "प्रोफ़ाइल परिवर्तन सहेजें"
    elif code == "ur":
        if "roles" in loc_data:
            loc_data["roles"]["officer"] = "زرعی افسر"
            loc_data["roles"]["farmer"] = "کسان"
            loc_data["roles"]["farmers"] = "کسانوں کے لیے"
            loc_data["roles"]["officers"] = "زرعی افسران کے لیے"
            loc_data["roles"]["buyers"] = "خریداروں اور تاجروں کے لیے"
        if "auth" in loc_data:
            loc_data["auth"]["loginTab"] = "لاگ ان"
            loc_data["auth"]["registerTab"] = "رجسٹر"
            loc_data["auth"]["fullNamePlaceholder"] = "مثال کے طور پر روی کمار"
        if "farmer" in loc_data:
            loc_data["farmer"]["expectedQty"] = "متوقع پیداوار"
            loc_data["farmer"]["pendingReview"] = "افسر کے جائزے کا انتظار"
            loc_data["farmer"]["visibleToBuyers"] = "خریداروں کو نظر آنے والا"
            loc_data["farmer"]["needsRevision"] = "نظر ثانی درکار ہے"
            loc_data["farmer"]["verifiedRoute"] = "✓ تصدیق شدہ اندراجات یہاں روٹ ہوتے ہیں"
        if "profile" in loc_data:
            loc_data["profile"]["title"] = "میری پروفائل"
            loc_data["profile"]["subtitle"] = "اپنے اکاؤنٹ کی معلومات اور متعلقہ تفصیلات کا انتظام کریں"
            loc_data["profile"]["saveChanges"] = "تبدیلیاں محفوظ کریں"

    st = loc_data.get("statuses", {})
    com = loc_data.get("common", {})
    status_dict = {
        "verified": st.get("verified", com.get("verified", "Verified")),
        "pending": st.get("pending", com.get("pending", "Pending")),
        "rejected": st.get("rejected", com.get("rejected", "Rejected")),
        "available": st.get("available", com.get("available", "Available")),
        "unavailable": st.get("unavailable", com.get("unavailable", "Unavailable")),
    }
    for k, v in list(status_dict.items()):
        status_dict[k.capitalize()] = v
    loc_data["status"] = status_dict
    loc_data["statuses"] = status_dict

expected_codes = [
    "en", "as", "bn", "brx", "doi", "gu", "hi", "kn", "ks", "kok",
    "mai", "ml", "mni", "mr", "ne", "or", "pa", "sa", "sat", "sd",
    "ta", "te", "ur"
]

print(f"Total languages collected: {len(ALL_LOCALES)}")

def sync_dict_keys(template_dict, target_dict, lang_code, path=""):
    """
    Ensure target_dict has exactly every key present in template_dict.
    If missing, fall back to template_dict's value.
    """
    result = {}
    for k, v in template_dict.items():
        sub_path = f"{path}.{k}" if path else k
        if k not in target_dict:
            result[k] = v
        elif isinstance(v, dict) and isinstance(target_dict[k], dict):
            result[k] = sync_dict_keys(v, target_dict[k], lang_code, sub_path)
        else:
            result[k] = target_dict[k]
    return result

# Write synchronized json files
synced_locales = {}
for code in expected_codes:
    raw_data = ALL_LOCALES.get(code, {})
    synced = sync_dict_keys(EN, raw_data, code)
    synced_locales[code] = synced
    
    file_path = os.path.join(LOCALES_DIR, f"{code}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(synced, f, ensure_ascii=False, indent=2)
    print(f"Wrote {code}.json ({synced['lang']['name']} - {synced['lang']['nativeName']})")

# Write static/i18n/languages.js
languages_meta = []
for code in expected_codes:
    loc = synced_locales[code]
    languages_meta.append({
        "code": code,
        "name": loc["lang"]["name"],
        "nativeName": loc["lang"]["nativeName"],
        "dir": loc["lang"].get("dir", "ltr")
    })

languages_js_path = os.path.join(os.path.dirname(__file__), "static", "i18n", "languages.js")
with open(languages_js_path, "w", encoding="utf-8") as f:
    f.write("// AgriFlow Centralized Language Definitions (English + 22 Eighth Schedule Indian Languages)\n")
    f.write("window.AgriFlowLanguages = ")
    f.write(json.dumps(languages_meta, ensure_ascii=False, indent=2))
    f.write(";\n\n")
    f.write("window.AgriFlowLocaleData = ")
    f.write(json.dumps(synced_locales, ensure_ascii=False, indent=2))
    f.write(";\n")

print(f"Successfully generated static/i18n/languages.js with {len(expected_codes)} languages!")
