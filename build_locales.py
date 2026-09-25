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
    "warning": "Warning",
    "delete": "Delete",
    "status": "Status",
    "role": "Role",
    "user": "User",
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
    "farmerRequests": "Farmer Requests"
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
    "switchedRole": "Switched to {{role}}",
    "officerVerificationTitle": "Verify Agriculture Officer",
    "officerVerificationSubtitle": "Enter your Officer ID to verify your official credentials.",
    "officerVerificationBadge": "Official Agriculture Officer Verification",
    "officerId": "Officer ID",
    "officerName": "Officer Name",
    "officerIdPlaceholder": "Enter your Officer ID (e.g. AGRI-TN-0003)",
    "verifyOfficerId": "Verify Officer ID",
    "verifying": "Verifying...",
    "invalidOfficerId": "Officer ID Not Found",
    "invalidOfficerIdMsg": "Officer ID not found. Please enter a valid Agriculture Officer ID.",
    "officerAccountExists": "Officer account already exists",
    "officerAccountExistsMsg": "An AgriFlow account has already been created for this Officer ID. Please use Officer Login.",
    "accountAlreadyExists": "Officer account already exists",
    "accountAlreadyExistsMsg": "An AgriFlow account has already been created for this Officer ID. Please use Officer Login.",
    "officerIdVerified": "Officer ID verified",
    "otpVerification": "OTP Verification",
    "otpSentTo": "OTP sent to registered mobile number",
    "otpSentToMobile": "OTP sent to registered mobile number {{mobile}}",
    "enterOtp": "Enter OTP",
    "enterOtpPlaceholder": "Enter 6-digit OTP",
    "verifyOtp": "Verify OTP",
    "resendOtp": "Resend OTP",
    "resendOtpIn": "Resend in {{seconds}}s",
    "demoOtpLabel": "Demo OTP",
    "prototypeNotice": "Prototype Only",
    "demoOtpBanner": "Demo OTP — Prototype Only",
    "demoOtpSimulatedNotice": "Prototype only — in production this OTP will be sent to the officer's registered mobile number.",
    "demoRegistryNotice": "AgriFlow Demo Agriculture Officer Registry",
    "demoDataLabel": "AgriFlow Officer Registry — Demo Data",
    "officerDetailsVerified": "Officer Details Verified",
    "confirmOfficialDetailsTitle": "Confirm Official Details",
    "detailsLinkedToOfficerId": "These details are linked to your Officer ID.",
    "confirmDetails": "Confirm Details",
    "prototypeDemo": "Prototype Demo",
    "demoOfficerIdHint": "Use one of the provided demo Officer IDs for testing:",
    "officialRecordReadOnlyNotice": "Official identity details are retrieved from the AgriFlow Demo Registry and cannot be modified.",
    "proceedToCredentials": "Proceed to Create Credentials",
    "createLoginTitle": "Create Login Credentials",
    "createLoginSubtitle": "Set up your unique login ID and password for AgriFlow.",
    "createLoginId": "Login ID",
    "loginIdPlaceholder": "Choose unique login ID (e.g. ravikumar_tn)",
    "createPassword": "Password",
    "confirmPassword": "Confirm Password",
    "confirmPasswordPlaceholder": "Re-enter password",
    "createOfficerAccount": "Create Officer Account",
    "officerAccountCreatedSuccess": "Officer Account Created Successfully!",
    "proceedToLogin": "Proceed to Officer Login",
    "officerLogin": "Officer Login",
    "officerLoginId": "Officer ID / Login ID",
    "officerLoginIdLabel": "Officer ID / Login ID",
    "officerLoginPlaceholder": "e.g. AGRI-TN-0001 or ravikumar_tn",
    "verifiedOfficerInformation": "Verified Officer Information",
    "verifiedOfficerInfo": "Verified Officer Information",
    "verifiedRegistryBadge": "Verified from AgriFlow Demo Registry (Official Identity Fields Locked)",
    "editablePreferences": "Editable Application Preferences",
    "savePreferences": "Save Profile Preferences",
    "post": "Post / Designation",
    "workingPlace": "Working Place",
    "registeredMobile": "Mobile",
    "step1OfficerId": "1. Officer ID",
    "step2Otp": "2. OTP Verification",
    "step3Details": "3. Confirm Details",
    "step4Credentials": "4. Create Login",
    "step5Complete": "5. Complete",
    "viewDemoRegistry": "View Demo Registry",
    "closeDemoRegistry": "Close Registry",
    "useDemoId": "Use This ID",
    "available": "Available",
    "registered": "Registered",
    "passwordsDoNotMatch": "Passwords do not match.",
    "passwordLengthError": "Password must be at least 6 characters long.",
    "autoFillDemoOtp": "Auto-fill Demo OTP",
    "officialIdentityLocked": "Official Identity Fields Locked",
    "enterOfficerIdPrompt": "Please enter your Officer ID (e.g. AGRI-TN-0003).",
    "enterSixDigitOtp": "Please enter the 6-digit OTP code.",
    "invalidOtp": "Invalid OTP code.",
    "newDemoOtpGenerated": "New Demo OTP generated",
    "officialRegistryRecord": "Official Registry Record Verified",
    "otpExpired": "OTP expired",
    "otpExpiredNotice": "This OTP has expired. Please click Resend OTP to generate a new one.",
    "passwordMismatch": "Passwords do not match.",
    "resendOtpFailed": "Failed to resend OTP.",
    "verificationFailed": "Verification Failed"
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
    "profileUpdated": "Profile updated successfully",
    "verifiedOfficerInformation": "Verified Officer Information",
    "verifiedOfficerInfo": "Verified Officer Information",
    "verifiedRegistryBadge": "Verified from AgriFlow Demo Registry (Official Identity Fields Locked)",
    "editablePreferences": "Editable Application Preferences",
    "workingPlace": "Working Place / Area",
    "registeredMobile": "Registered Mobile",
    "officerId": "Officer ID",
    "post": "Post / Designation",
    "verifiedNotice": "Official identity details verified by AgriFlow."
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

OFFICER_AUTH_TRANSLATIONS = {
    "hi": {
        "officerVerificationTitle": "कृषि अधिकारी सत्यापन",
        "officerVerificationSubtitle": "अपने आधिकारिक क्रेडेंशियल्स को सत्यापित करने के लिए अपनी अधिकारी आईडी दर्ज करें।",
        "officerId": "अधिकारी आईडी",
        "officerIdPlaceholder": "अपनी अधिकारी आईडी दर्ज करें (उदा. AGRI-TN-0001)",
        "verifyOfficerId": "अधिकारी आईडी सत्यापित करें",
        "verifying": "सत्यापित किया जा रहा है...",
        "invalidOfficerId": "अमान्य अधिकारी आईडी",
        "invalidOfficerIdMsg": "कृपया एक मान्य पंजीकृत कृषि अधिकारी आईडी दर्ज करें।",
        "officerAccountExists": "अधिकारी खाता पहले से मौजूद है",
        "officerAccountExistsMsg": "इस अधिकारी आईडी के लिए पहले से ही एक एग्रीफ्लो खाता बनाया जा चुका है। कृपया अधिकारी लॉगिन का उपयोग करें।",
        "officerIdVerified": "अधिकारी आईडी सत्यापित",
        "otpVerification": "ओटीपी सत्यापन",
        "otpSentTo": "पंजीकृत मोबाइल नंबर पर ओटीपी भेजा गया",
        "otpSentToMobile": "पंजीकृत मोबाइल नंबर {{mobile}} पर ओटीपी भेजा गया",
        "enterOtp": "ओटीपी दर्ज करें",
        "enterOtpPlaceholder": "6-अंकों का ओटीपी दर्ज करें",
        "verifyOtp": "ओटीपी सत्यापित करें",
        "resendOtp": "ओटीपी पुनः भेजें",
        "resendOtpIn": "{{seconds}} सेकंड में पुनः भेजें",
        "demoOtpLabel": "डेमो ओटीपी",
        "prototypeNotice": "केवल प्रोटोटाइप",
        "demoOtpBanner": "डेमो ओटीपी — केवल प्रोटोटाइप",
        "demoRegistryNotice": "एग्रीफ्लो डेमो कृषि अधिकारी रजिस्ट्री",
        "demoDataLabel": "एग्रीफ्लो अधिकारी रजिस्ट्री — डेमो डेटा",
        "officerDetailsVerified": "अधिकारी विवरण सत्यापित",
        "officialRecordReadOnlyNotice": "आधिकारिक पहचान विवरण एग्रीफ्लो डेमो रजिस्ट्री से प्राप्त किए गए हैं और इन्हें बदला नहीं जा सकता है।",
        "proceedToCredentials": "क्रेडेंशियल बनाने के लिए आगे बढ़ें",
        "createLoginTitle": "लॉगिन क्रेडेंशियल बनाएं",
        "createLoginSubtitle": "एग्रीफ्लो के लिए अपनी विशिष्ट लॉगिन आईडी और पासवर्ड सेट करें।",
        "createLoginId": "लॉगिन आईडी बनाएं",
        "loginIdPlaceholder": "विशिष्ट लॉगिन आईडी चुनें (उदा. ravikumar_tn)",
        "createPassword": "पासवर्ड बनाएं",
        "confirmPassword": "पासवर्ड की पुष्टि करें",
        "confirmPasswordPlaceholder": "पासवर्ड दोबारा दर्ज करें",
        "createOfficerAccount": "अधिकारी खाता बनाएं",
        "officerAccountCreatedSuccess": "अधिकारी खाता सफलतापूर्वक बनाया गया!",
        "proceedToLogin": "अधिकारी लॉगिन पर जाएं",
        "officerLogin": "अधिकारी लॉगिन",
        "officerLoginId": "अधिकारी आईडी / लॉगिन आईडी",
        "officerLoginPlaceholder": "उदा. AGRI-TN-0001 या ravikumar_tn",
        "verifiedOfficerInformation": "सत्यापित अधिकारी जानकारी",
        "verifiedOfficerInfo": "सत्यापित अधिकारी जानकारी",
        "verifiedRegistryBadge": "एग्रीफ्लो डेमो रजिस्ट्री से सत्यापित (आधिकारिक पहचान फ़ील्ड लॉक हैं)",
        "editablePreferences": "संपादन योग्य प्राथमिकताएं",
        "savePreferences": "प्रोफ़ाइल प्राथमिकताएं सहेजें",
        "post": "पद / पदनाम",
        "workingPlace": "कार्य स्थल / क्षेत्र",
        "registeredMobile": "पंजीकृत मोबाइल",
        "step1OfficerId": "1. अधिकारी आईडी",
        "step2Otp": "2. ओटीपी सत्यापन",
        "step3Details": "3. विवरण की पुष्टि",
        "step4Credentials": "4. लॉगिन बनाएं",
        "step5Complete": "5. पूर्ण",
        "viewDemoRegistry": "डेमो रजिस्ट्री देखें",
        "closeDemoRegistry": "रजिस्ट्री बंद करें",
        "useDemoId": "इस आईडी का उपयोग करें",
        "available": "उपलब्ध",
        "registered": "पंजीकृत",
        "passwordsDoNotMatch": "पासवर्ड मेल नहीं खाते।",
        "passwordLengthError": "पासवर्ड कम से कम 6 अक्षरों का होना चाहिए।",
        "loginIdLengthError": "लॉगिन आईडी कम से कम 3 अक्षरों की होनी चाहिए।",
        "autoFillDemoOtp": "डेमो ओटीपी ऑटो-भरें",
        "officialIdentityLocked": "आधिकारिक पहचान फ़ील्ड लॉक हैं"
    },
    "ta": {
        "officerVerificationTitle": "வேளாண்மை அதிகாரி சரிபார்ப்பு",
        "officerVerificationSubtitle": "உங்கள் அதிகாரப்பூர்வ சான்றுகளை சரிபார்க்க உங்கள் அதிகாரி ஐடியை உள்ளிடவும்.",
        "officerId": "அதிகாரி ஐடி",
        "officerIdPlaceholder": "உங்கள் அதிகாரி ஐடியை உள்ளிடவும் (எ.கா. AGRI-TN-0001)",
        "verifyOfficerId": "அதிகாரி ஐடியை சரிபார்க்கவும்",
        "verifying": "சரிபார்க்கிறது...",
        "invalidOfficerId": "செல்லுபடியாகாத அதிகாரி ஐடி",
        "invalidOfficerIdMsg": "தயவுசெய்து சரியான பதிவுசெய்யப்பட்ட வேளாண்மை அதிகாரி ஐடியை உள்ளிடவும்.",
        "officerAccountExists": "அதிகாரி கணக்கு ஏற்கனவே உள்ளது",
        "officerAccountExistsMsg": "இந்த அதிகாரி ஐடிக்கு ஏற்கனவே ஒரு அக்ரிஃப்ளோ கணக்கு உருவாக்கப்பட்டுள்ளது. தயவுசெய்து அதிகாரி உள்நுழைவைப் பயன்படுத்தவும்.",
        "officerIdVerified": "அதிகாரி ஐடி சரிபார்க்கப்பட்டது",
        "otpVerification": "OTP சரிபார்ப்பு",
        "otpSentTo": "பதிவு செய்யப்பட்ட மொபைல் எண்ணுக்கு OTP அனுப்பப்பட்டது",
        "otpSentToMobile": "பதிவு செய்யப்பட்ட மொபைல் எண் {{mobile}}க்கு OTP அனுப்பப்பட்டது",
        "enterOtp": "OTP-ஐ உள்ளிடவும்",
        "enterOtpPlaceholder": "6-இலக்க OTP-ஐ உள்ளிடவும்",
        "verifyOtp": "OTP-ஐ சரிபார்க்கவும்",
        "resendOtp": "OTP-ஐ மீண்டும் அனுப்பவும்",
        "resendOtpIn": "{{seconds}} வினாடிகளில் மீண்டும் அனுப்பவும்",
        "demoOtpLabel": "டெமோ OTP",
        "prototypeNotice": "முன்மாதிரி பயன்பாட்டிற்கு மட்டுமே",
        "demoOtpBanner": "டெமோ OTP — முன்மாதிரி பயன்பாட்டிற்கு மட்டுமே",
        "demoRegistryNotice": "அக்ரிஃப்ளோ டெமோ வேளாண்மை அதிகாரி பதிவேடு",
        "demoDataLabel": "அக்ரிஃப்ளோ அதிகாரி பதிவேடு — டெமோ தரவு",
        "officerDetailsVerified": "அதிகாரி விவரங்கள் சரிபார்க்கப்பட்டன",
        "officialRecordReadOnlyNotice": "அதிகாரப்பூர்வ அடையாள விவரங்கள் அக்ரிஃப்ளோ டெமோ பதிவேட்டில் இருந்து பெறப்பட்டவை மற்றும் அவற்றை மாற்ற முடியாது.",
        "proceedToCredentials": "சான்றுகளை உருவாக்க தொடரவும்",
        "createLoginTitle": "உள்நுழைவு சான்றுகளை உருவாக்கவும்",
        "createLoginSubtitle": "அக்ரிஃப்ளோவிற்கான உங்கள் தனித்துவமான உள்நுழைவு ஐடி மற்றும் கடவுச்சொல்லை அமைக்கவும்.",
        "createLoginId": "உள்நுழைவு ஐடியை உருவாக்கவும்",
        "loginIdPlaceholder": "தனித்துவமான உள்நுழைவு ஐடியைத் தேர்ந்தெடுக்கவும் (எ.கா. ravikumar_tn)",
        "createPassword": "கடவுச்சொல்லை உருவாக்கவும்",
        "confirmPassword": "கடவுச்சொல்லை உறுதிப்படுத்தவும்",
        "confirmPasswordPlaceholder": "கடவுச்சொல்லை மீண்டும் உள்ளிடவும்",
        "createOfficerAccount": "அதிகாரி கணக்கை உருவாக்கவும்",
        "officerAccountCreatedSuccess": "அதிகாரி கணக்கு வெற்றிகரமாக உருவாக்கப்பட்டது!",
        "proceedToLogin": "அதிகாரி உள்நுழைவுக்குச் செல்லவும்",
        "officerLogin": "அதிகாரி உள்நுழைவு",
        "officerLoginId": "அதிகாரி ஐடி / உள்நுழைவு ஐடி",
        "officerLoginPlaceholder": "எ.கா. AGRI-TN-0001 அல்லது ravikumar_tn",
        "verifiedOfficerInformation": "சரிபார்க்கப்பட்ட அதிகாரி தகவல்",
        "verifiedOfficerInfo": "சரிபார்க்கப்பட்ட அதிகாரி தகவல்",
        "verifiedRegistryBadge": "அக்ரிஃப்ளோ டெமோ பதிவேட்டில் இருந்து சரிபார்க்கப்பட்டது (அடையாளப் புலங்கள் பூட்டப்பட்டுள்ளன)",
        "editablePreferences": "திருத்தக்கூடிய விருப்பத்தேர்வுகள்",
        "savePreferences": "சுயவிவர விருப்பத்தேர்வுகளைச் சேமிக்கவும்",
        "post": "பதவி / பதவிப்பெயர்",
        "workingPlace": "பணிபுரியும் இடம் / பகுதி",
        "registeredMobile": "பதிவு செய்யப்பட்ட மொபைல்",
        "step1OfficerId": "1. அதிகாரி ஐடி",
        "step2Otp": "2. OTP சரிபார்ப்பு",
        "step3Details": "3. விவரங்களை உறுதிப்படுத்தவும்",
        "step4Credentials": "4. உள்நுழைவை உருவாக்கவும்",
        "step5Complete": "5. முடிவு",
        "viewDemoRegistry": "டெமோ பதிவேட்டைக் காண்க",
        "closeDemoRegistry": "பதிவேட்டை மூடுக",
        "useDemoId": "இந்த ஐடியைப் பயன்படுத்தவும்",
        "available": "கிடைக்கிறது",
        "registered": "பதிவு செய்யப்பட்டது",
        "passwordsDoNotMatch": "கடவுச்சொற்கள் பொருந்தவில்லை.",
        "passwordLengthError": "கடவுச்சொல் குறைந்தது 6 எழுத்துகள் கொண்டதாக இருக்க வேண்டும்.",
        "loginIdLengthError": "உள்நுழைவு ஐடி குறைந்தது 3 எழுத்துகள் கொண்டதாக இருக்க வேண்டும்.",
        "autoFillDemoOtp": "டெமோ OTP-ஐ தானாக நிரப்பவும்",
        "officialIdentityLocked": "அடையாளப் புலங்கள் பூட்டப்பட்டுள்ளன"
    },
    "te": {
        "officerVerificationTitle": "వ్యవసాయ అధికారి ధృవీకరణ",
        "officerVerificationSubtitle": "మీ అధికారిక వివరాలను ధృవీకరించడానికి అధికారి ఐడిని నమోదు చేయండి.",
        "officerId": "అధికారి ఐడి",
        "officerIdPlaceholder": "మీ అధికారి ఐడిని నమోదు చేయండి (ఉదా. AGRI-TN-0001)",
        "verifyOfficerId": "అధికారి ఐడిని ధృవీకరించండి",
        "verifying": "ధృవీకరిస్తోంది...",
        "invalidOfficerId": "చెల్లని అధికారి ఐడి",
        "invalidOfficerIdMsg": "దయచేసి చెల్లుబాటు అయ్యే నమోదిత వ్యవసాయ అధికారి ఐడిని నమోదు చేయండి.",
        "officerAccountExists": "అధికారి ఖాతా ఇప్పటికే ఉంది",
        "officerAccountExistsMsg": "ఈ అధికారి ఐడి కోసం ఇప్పటికే ఖాతా సృష్టించబడింది. దయచేసి లాగిన్ ఉపయోగించండి.",
        "officerIdVerified": "అధికారి ఐడి ధృవీకరించబడింది",
        "otpVerification": "OTP ధృవీకరణ",
        "otpSentTo": "నమోదిత మొబైల్ నంబరుకు OTP పంపబడింది",
        "otpSentToMobile": "నమోదిత మొబైల్ నంబర్ {{mobile}}కి OTP పంపబడింది",
        "enterOtp": "OTP నమోదు చేయండి",
        "enterOtpPlaceholder": "6 అంకెల OTP నమోదు చేయండి",
        "verifyOtp": "OTP ధృవీకరించండి",
        "resendOtp": "OTP మళ్లీ పంపండి",
        "demoOtpLabel": "డెమో OTP",
        "prototypeNotice": "ప్రోటోటైప్ మాత్రమే",
        "demoOtpBanner": "డెమో OTP — ప్రోటోటైప్ కోసం మాత్రమే",
        "demoRegistryNotice": "అగ్రిఫ్లో డెమో వ్యవసాయ అధికారి రిజిస్ట్రీ",
        "demoDataLabel": "అగ్రిఫ్లో అధికారి రిజిస్ట్రీ — డెమో డేటా",
        "officerDetailsVerified": "అధికారి వివరాలు ధృవీకరించబడ్డాయి",
        "officialRecordReadOnlyNotice": "అధికారిక వివరాలు రిజిస్ట్రీ నుండి పొందబడ్డాయి మరియు సవరించలేరు.",
        "createLoginTitle": "లాగిన్ వివరాలను సృష్టించండి",
        "createLoginId": "లాగిన్ ఐడిని సృష్టించండి",
        "createPassword": "పాస్‌వర్డ్ సృష్టించండి",
        "confirmPassword": "పాస్‌వర్డ్ నిర్ధారించండి",
        "createOfficerAccount": "అధికారి ఖాతాను సృష్టించండి",
        "officerAccountCreatedSuccess": "అధికారి ఖాతా విజయవంతంగా సృష్టించబడింది!",
        "proceedToLogin": "అధికారి లాగిన్‌కి వెళ్లండి",
        "officerLogin": "అధికారి లాగిన్",
        "verifiedOfficerInformation": "ధృవీకరించబడిన అధికారి సమాచారం",
        "verifiedRegistryBadge": "డెమో రిజిస్ట్రీ నుండి ధృవీకరించబడింది (అధికారిక ఫీల్డ్‌లు లాక్ చేయబడ్డాయి)"
    },
    "kn": {
        "officerVerificationTitle": "ಕೃಷಿ ಅಧಿಕಾರಿ ಪರಿಶೀಲನೆ",
        "officerVerificationSubtitle": "ನಿಮ್ಮ ಅಧಿಕೃತ ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ನಿಮ್ಮ ಅಧಿಕಾರಿ ಐಡಿ ನಮೂದಿಸಿ.",
        "officerId": "ಅಧಿಕಾರಿ ಐಡಿ",
        "officerIdPlaceholder": "ಅಧಿಕಾರಿ ಐಡಿ ನಮೂದಿಸಿ (ಉದಾ. AGRI-TN-0001)",
        "verifyOfficerId": "ಅಧಿಕಾರಿ ಐಡಿ ಪರಿಶೀಲಿಸಿ",
        "verifying": "ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿದೆ...",
        "invalidOfficerId": "ಅಮಾನ್ಯ ಅಧಿಕಾರಿ ಐಡಿ",
        "invalidOfficerIdMsg": "ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ನೋಂದಾಯಿತ ಕೃಷಿ ಅಧಿಕಾರಿ ಐಡಿ ನಮೂದಿಸಿ.",
        "officerAccountExists": "ಅಧಿಕಾರಿ ಖಾತೆ ಈಗಾಗಲೇ ಅಸ್ತಿತ್ವದಲ್ಲಿದೆ",
        "officerAccountExistsMsg": "ಈ ಅಧಿಕಾರಿ ಐಡಿಗೆ ಈಗಾಗಲೇ ಖಾತೆ ರಚಿಸಲಾಗಿದೆ. ದಯವಿಟ್ಟು ಲಾಗಿನ್ ಬಳಸಿ.",
        "otpVerification": "OTP ಪರಿಶೀಲನೆ",
        "demoOtpBanner": "ಡೆಮೊ OTP — ಮಾದರಿಗೆ ಮಾತ್ರ",
        "officerDetailsVerified": "ಅಧಿಕಾರಿ ವಿವರಗಳು ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
        "createLoginId": "ಲಾಗಿನ್ ಐಡಿ ರಚಿಸಿ",
        "createPassword": "ಪಾಸ್‌ವರ್ಡ್ ರಚಿಸಿ",
        "confirmPassword": "ಪಾಸ್‌ವರ್ಡ್ ದೃಢೀಕರಿಸಿ",
        "createOfficerAccount": "ಅಧಿಕಾರಿ ಖಾತೆಯನ್ನು ರಚಿಸಿ",
        "officerAccountCreatedSuccess": "ಅಧಿಕಾರಿ ಖಾತೆ ಯಶಸ್ವಿಯಾಗಿ ರಚಿಸಲಾಗಿದೆ!",
        "proceedToLogin": "ಅಧಿಕಾರಿ ಲಾಗಿನ್‌ಗೆ ಹೋಗಿ",
        "officerLogin": "ಅಧಿಕಾರಿ ಲಾಗಿನ್",
        "verifiedOfficerInformation": "ಪರಿಶೀಲಿಸಿದ ಅಧಿಕಾರಿ ಮಾಹಿತಿ",
        "verifiedRegistryBadge": "ಡೆಮೊ ರಿಜಿಸ್ಟ್ರಿಯಿಂದ ಪರಿಶೀಲಿಸಲಾಗಿದೆ (ಅಧಿಕೃತ ಕ್ಷೇತ್ರಗಳನ್ನು ಲಾಕ್ ಮಾಡಲಾಗಿದೆ)"
    },
    "ml": {
        "officerVerificationTitle": "കൃഷി ഓഫീസർ സ്ഥിരീകരണം",
        "officerVerificationSubtitle": "നിങ്ങളുടെ ഔദ്യോഗിക വിവരങ്ങൾ പരിശോധിക്കാൻ ഓഫീസർ ഐഡി നൽകുക.",
        "officerId": "ഓഫീസർ ഐഡി",
        "officerIdPlaceholder": "ഓഫീസർ ഐഡി നൽകുക (ഉദാ. AGRI-TN-0001)",
        "verifyOfficerId": "ഓഫീസർ ഐഡി പരിശോധിക്കുക",
        "invalidOfficerId": "അസാധുവായ ഓഫീസർ ഐഡി",
        "invalidOfficerIdMsg": "സാധുവായ രജിസ്റ്റർ ചെയ്ത കൃഷി ഓഫീസർ ഐഡി നൽകുക.",
        "officerAccountExists": "ഓഫീസർ അക്കൗണ്ട് ഇതിനകം നിലവിലുണ്ട്",
        "otpVerification": "ഒടിപി പരിശോധന",
        "demoOtpBanner": "ഡെമോ ഒടിപി — പ്രോട്ടോടൈപ്പ് മാത്രം",
        "officerDetailsVerified": "ഓഫീസർ വിവരങ്ങൾ പരിശോധിച്ചു",
        "createLoginId": "ലോഗിൻ ഐഡി സൃഷ്ടിക്കുക",
        "createOfficerAccount": "ഓഫീസർ അക്കൗണ്ട് സൃഷ്ടിക്കുക",
        "verifiedOfficerInformation": "സ്ഥിരീകരിച്ച ഓഫീസർ വിവരങ്ങൾ"
    },
    "mr": {
        "officerVerificationTitle": "कृषी अधिकारी पडताळणी",
        "officerVerificationSubtitle": "आपले अधिकृत तपशील पडताळण्यासाठी अधिकारी आयडी प्रविष्ट करा.",
        "officerId": "अधिकारी आयडी",
        "officerIdPlaceholder": "अधिकारी आयडी प्रविष्ट करा (उदा. AGRI-TN-0001)",
        "verifyOfficerId": "अधिकारी आयडी पडताळा",
        "invalidOfficerId": "अवैध अधिकारी आयडी",
        "invalidOfficerIdMsg": "कृपया वैध नोंदणीकृत कृषी अधिकारी आयडी प्रविष्ट करा.",
        "officerAccountExists": "अधिकारी खाते आधीपासून अस्तित्वात आहे",
        "otpVerification": "ओटीपी पडताळणी",
        "demoOtpBanner": "डेमो ओटीपी — फक्त प्रोटोटाइप",
        "officerDetailsVerified": "अधिकारी तपशील पडताळले",
        "createLoginId": "लॉगिन आयडी तयार करा",
        "createOfficerAccount": "अधिकारी खाते तयार करा",
        "verifiedOfficerInformation": "पडताळलेली अधिकारी माहिती",
        "verifiedRegistryBadge": "डेमो नोंदवहीतून पडताळले (अधिकृत फील्ड लॉक आहेत)"
    },
    "bn": {
        "officerVerificationTitle": "কৃষি অফিসার যাচাইকরণ",
        "officerVerificationSubtitle": "আপনার অফিসিয়াল পরিচয়পত্র যাচাই করতে অফিসার আইডি লিখুন।",
        "officerId": "অফিসার আইডি",
        "officerIdPlaceholder": "অফিসার আইডি লিখুন (যেমন AGRI-TN-0001)",
        "verifyOfficerId": "অফিসার আইডি যাচাই করুন",
        "invalidOfficerId": "অবৈধ অফিসার আইডি",
        "invalidOfficerIdMsg": "অনুগ্রহ করে একটি বৈধ নিবন্ধিত কৃষি অফিসার আইডি লিখুন।",
        "officerAccountExists": "অফিসার অ্যাকাউন্ট ইতিমধ্যে বিদ্যমান",
        "otpVerification": "ওটিপি যাচাইকরণ",
        "demoOtpBanner": "ডেমো ওটিপি — শুধুমাত্র প্রোটোটাইপ",
        "officerDetailsVerified": "অফিসার বিবরণ যাচাইকৃত",
        "createLoginId": "লগইন আইডি তৈরি করুন",
        "createOfficerAccount": "অফিসার অ্যাকাউন্ট তৈরি করুন",
        "verifiedOfficerInformation": "যাচাইকৃত অফিসার তথ্য"
    },
    "gu": {
        "officerVerificationTitle": "કૃષિ અધિકારી ચકાસણી",
        "officerVerificationSubtitle": "તમારી સત્તાવાર ઓળખ ચકાસવા માટે અધિકારી આઈડી દાખલ કરો.",
        "officerId": "અધિકારી આઈડી",
        "officerIdPlaceholder": "અધિકારી આઈડી દાખલ કરો (દા.ત. AGRI-TN-0001)",
        "verifyOfficerId": "અધિકારી આઈડી ચકાસો",
        "invalidOfficerId": "અમાન્ય અધિકારી આઈડી",
        "invalidOfficerIdMsg": "કૃપા કરીને માન્ય રજિસ્ટર્ડ કૃષિ અધિકારી આઈડી દાખલ કરો.",
        "officerAccountExists": "અધિકારી એકાઉન્ટ પહેલેથી જ અસ્તિત્વમાં છે",
        "otpVerification": "ઓટીપી ચકાસણી",
        "demoOtpBanner": "ડેમો ઓટીપી — માત્ર પ્રોટોટાઇપ",
        "officerDetailsVerified": "અધિકારી વિગતો ચકાસાયેલ",
        "createLoginId": "લોગિન આઈડી બનાવો",
        "createOfficerAccount": "અધિકારી એકાઉન્ટ બનાવો",
        "verifiedOfficerInformation": "ચકાસાયેલ અધિકારી માહિતી"
    },
    "pa": {
        "officerVerificationTitle": "ਖੇਤੀਬਾੜੀ ਅਧਿਕਾਰੀ ਪੁਸ਼ਟੀਕਰਨ",
        "officerVerificationSubtitle": "ਆਪਣੇ ਅਧਿਕਾਰਤ ਵੇਰਵਿਆਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਅਧਿਕਾਰੀ ਆਈਡੀ ਦਰਜ ਕਰੋ।",
        "officerId": "ਅਧਿਕਾਰੀ ਆਈਡੀ",
        "officerIdPlaceholder": "ਅਧਿਕਾਰੀ ਆਈਡੀ ਦਰਜ ਕਰੋ (ਜਿਵੇਂ AGRI-TN-0001)",
        "verifyOfficerId": "ਅਧਿਕਾਰੀ ਆਈਡੀ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ",
        "invalidOfficerId": "ਅਵੈਧ ਅਧਿਕਾਰੀ ਆਈਡੀ",
        "invalidOfficerIdMsg": "ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ ਵੈਧ ਰਜਿਸਟਰਡ ਖੇਤੀਬਾੜੀ ਅਧਿਕਾਰੀ ਆਈਡੀ ਦਰਜ ਕਰੋ।",
        "officerAccountExists": "ਅਧਿਕਾਰੀ ਖਾਤਾ ਪਹਿਲਾਂ ਹੀ ਮੌਜੂਦ ਹੈ",
        "otpVerification": "ਓਟੀਪੀ ਪੁਸ਼ਟੀਕਰਨ",
        "demoOtpBanner": "ਡੈਮੋ ਓਟੀਪੀ — ਸਿਰਫ਼ ਪ੍ਰੋਟੋਟਾਈਪ",
        "officerDetailsVerified": "ਅਧਿਕਾਰੀ ਵੇਰਵਿਆਂ ਦੀ ਪੁਸ਼ਟੀ ਹੋਈ",
        "createLoginId": "ਲਾਗਇਨ ਆਈਡੀ ਬਣਾਓ",
        "createOfficerAccount": "ਅਧਿਕਾਰੀ ਖਾਤਾ ਬਣਾਓ",
        "verifiedOfficerInformation": "ਪੁਸ਼ਟੀ ਕੀਤੀ ਅਧਿਕਾਰੀ ਜਾਣਕਾਰੀ"
    },
    "ur": {
        "officerVerificationTitle": "زرعی افسر کی تصدیق",
        "officerVerificationSubtitle": "اپنی سرکاری اسناد کی تصدیق کے لیے اپنی آفیسر آئی ڈی درج کریں۔",
        "officerId": "آفیسر آئی ڈی",
        "officerIdPlaceholder": "اپنی آفیسر آئی ڈی درج کریں (مثلاً AGRI-TN-0001)",
        "verifyOfficerId": "آفیسر آئی ڈی کی تصدیق کریں",
        "invalidOfficerId": "غلط آفیسر آئی ڈی",
        "invalidOfficerIdMsg": "براہ کرم ایک درست رجسٹرڈ زرعی افسر کی آئی ڈی درج کریں۔",
        "officerAccountExists": "افسر کا اکاؤنٹ پہلے سے موجود ہے",
        "otpVerification": "او ٹی پی کی تصدیق",
        "demoOtpBanner": "ڈیمو او ٹی پی — صرف پروٹوٹائپ",
        "officerDetailsVerified": "افسر کی تفصیلات تصدیق شدہ",
        "createLoginId": "لاگ ان آئی ڈی بنائیں",
        "createOfficerAccount": "افسر کا اکاؤنٹ بنائیں",
        "verifiedOfficerInformation": "تصدیق شدہ افسر کی معلومات"
    },
    "or": {
        "officerVerificationTitle": "କୃଷି ଅଧିକାରୀ ଯାଞ୍ଚ",
        "officerVerificationSubtitle": "ଆପଣଙ୍କର ସରକାରୀ ପ୍ରମାଣପତ୍ର ଯାଞ୍ଚ କରିବାକୁ ଅଧିକାରୀ ଆଇଡି ପ୍ରବେଶ କରନ୍ତୁ।",
        "officerId": "ଅଧିକାରୀ ଆଇଡି",
        "officerIdPlaceholder": "ଅଧିକାରୀ ଆଇଡି ପ୍ରବେଶ କରନ୍ତୁ (ଯଥା AGRI-TN-0001)",
        "verifyOfficerId": "ଅଧିକାରୀ ଆଇଡି ଯାଞ୍ଚ କରନ୍ତୁ",
        "invalidOfficerId": "ଅବୈଧ ଅଧିକାରୀ ଆଇଡି",
        "invalidOfficerIdMsg": "ଦୟାକରି ଏକ ବୈଧ ପଞ୍ଜୀକୃତ କୃଷି ଅଧିକାରୀ ଆଇଡି ପ୍ରବେଶ କରନ୍ତୁ।",
        "officerAccountExists": "ଅଧିକାରୀ ଆକାଉଣ୍ଟ ପୂର୍ବରୁ ବିଦ୍ୟମାନ ଅଛି",
        "otpVerification": "ଓଟିପି ଯାଞ୍ଚ",
        "demoOtpBanner": "ଡେମୋ ଓଟିପି — କେବଳ ପ୍ରୋଟୋଟାଇପ୍",
        "officerDetailsVerified": "ଅଧିକାରୀ ବିବରଣୀ ଯାଞ୍ଚ ହୋଇଛି",
        "createLoginId": "ଲଗଇନ୍ ଆଇଡି ସୃଷ୍ଟି କରନ୍ତୁ",
        "createOfficerAccount": "ଅଧିକାରୀ ଆକାଉଣ୍ଟ ସୃଷ୍ଟି କରନ୍ତୁ",
        "verifiedOfficerInformation": "ଯାଞ୍ଚ ହୋଇଥିବା ଅଧିକାରୀ ସୂଚନା"
    },
    "as": {
        "officerVerificationTitle": "কৃষি বিষয়া সত্যাপন",
        "officerVerificationSubtitle": "আপোনাৰ চৰকাৰী পৰিচয় সত্যাপন কৰিবলৈ বিষয়া আইডি দিয়ক।",
        "officerId": "বিষয়াসকলৰ আইডি",
        "officerIdPlaceholder": "বিষয়া আইডি প্ৰবিষ্ট কৰক (যেনে AGRI-TN-0001)",
        "verifyOfficerId": "বিষয়াসকলৰ আইডি পৰীক্ষা কৰক",
        "invalidOfficerId": "অবৈধ বিষয়া আইডি",
        "invalidOfficerIdMsg": "অনুগ্ৰহ কৰি এটা বৈধ পঞ্জীয়নভুক্ত কৃষি বিষয়া আইডি প্ৰবিষ্ট কৰক।",
        "officerAccountExists": "বিষয়া একাউন্ট ইতিমধ্যে আছে",
        "otpVerification": "অ'টিপি সত্যাপন",
        "demoOtpBanner": "ডেমো অ'টিপি — কেৱল প্ৰ'ট'টাইপ",
        "officerDetailsVerified": "বিষয়া বিৱৰণ সত্যাপিত",
        "createLoginId": "লগইন আইডি তৈয়াৰ কৰক",
        "createOfficerAccount": "বিষয়া একাউন্ট সৃষ্টি কৰক",
        "verifiedOfficerInformation": "সত্যাপিত বিষয়া তথ্য"
    }
}

# Clean any demo blocks and enrich with all produce translations
for code, loc_data in ALL_LOCALES.items():

    if "demo" in loc_data:
        del loc_data["demo"]
    if "landing" in loc_data and "sihPlatform" in loc_data["landing"]:
        del loc_data["landing"]["sihPlatform"]
    if "common" in loc_data:
        loc_data["common"].pop("liveSync", None)
        loc_data["common"].pop("reconnecting", None)
    if "navigation" in loc_data:
        loc_data["navigation"].pop("liveSync", None)
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
        if code in OFFICER_AUTH_TRANSLATIONS:
            a.update(OFFICER_AUTH_TRANSLATIONS[code])
        a.setdefault("login", c.get("login", "Login"))
        a.setdefault("register", c.get("register", "Register"))
        a.setdefault("loginTab", a.get("login", c.get("login", "Login")))
        a.setdefault("registerTab", a.get("register", c.get("register", "Register")))
        a.setdefault("fullNamePlaceholder", a.get("fullName", "e.g. Ravi Kumar"))
        a.setdefault("passwordPlaceholder", "••••••••")
        if "officerAccountExists" in a and "accountAlreadyExists" not in a:
            a["accountAlreadyExists"] = a["officerAccountExists"]
        if "officerAccountExistsMsg" in a and "accountAlreadyExistsMsg" not in a:
            a["accountAlreadyExistsMsg"] = a["officerAccountExistsMsg"]
        if "officerLoginId" in a and "officerLoginIdLabel" not in a:
            a["officerLoginIdLabel"] = a["officerLoginId"]
        if "accountAlreadyExists" in a and "officerAccountExists" not in a:
            a["officerAccountExists"] = a["accountAlreadyExists"]
        if "accountAlreadyExistsMsg" in a and "officerAccountExistsMsg" not in a:
            a["officerAccountExistsMsg"] = a["accountAlreadyExistsMsg"]
        if "officerLoginIdLabel" in a and "officerLoginId" not in a:
            a["officerLoginId"] = a["officerLoginIdLabel"]

    if "profile" in loc_data:
        pr = loc_data["profile"]
        c = loc_data.get("common", {})
        a = loc_data.get("auth", {})
        if code in OFFICER_AUTH_TRANSLATIONS:
            p_trans = OFFICER_AUTH_TRANSLATIONS[code]
            for pk in ["verifiedOfficerInformation", "verifiedOfficerInfo", "verifiedRegistryBadge", "editablePreferences", "workingPlace", "registeredMobile", "officerId", "post"]:
                if pk in p_trans:
                    pr[pk] = p_trans[pk]
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
