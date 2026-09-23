# -*- coding: utf-8 -*-
"""
Language definitions for AgriFlow - Group 5:
Konkani (kok), Maithili (mai), Dogri (doi), Bodo (brx),
Kashmiri (ks), Meitei/Manipuri (mni), Santali (sat)
"""

LOCALES_GROUP_5 = {
  "kok": {
    "lang": { "name": "Konkani", "nativeName": "कोंकणी", "code": "kok", "dir": "ltr" },
    "common": {
      "language": "भास", "login": "लॉगिन", "register": "नोंदणी", "logout": "लॉगआउट",
      "dashboard": "डॅशबोर्ड", "profile": "प्रोफायल", "save": "सांबाळा", "cancel": "रद्द करा",
      "close": "बंद करा", "submit": "सादर करा", "refresh": "ताजे करा", "search": "सोदा",
      "clearFilters": "फिल्टर्स काढा", "loading": "लोड जाता...", "viewDetails": "तपशील पळयात",
      "allStates": "सगळीं राज्यां", "allDistricts": "सगळे जिल्हे", "allAreas": "सगळे वाठार",
      "verified": "तपासिल्लें", "pending": "बाकी आसा", "rejected": "नाकारिल्लें",
      "available": "उपलब्ध", "unavailable": "अनुपलब्ध", "yes": "हय", "no": "ना",
      "continue": "फुडें वचा", "send": "धाडा", "back": "फाटीं", "next": "फुडलें",
      "previous": "फाटलें", "edit": "बदल करा", "delete": "काडून उडयात", "status": "स्थिती",
      "role": "भूमिका", "user": "वापरपी", "liveSync": "थेट सिंक", "reconnecting": "परत जोडटा...",
      "reset": "परत सेट करा", "actions": "कृती", "crop": "पीक", "quantity": "प्रमाण",
      "location": "सुवात", "date": "तारीख", "notes": "टिपणी"
    },
    "navigation": {
      "home": "मुखेल पान", "viewProduce": "उत्पादनां पळयात", "officerPortal": "अधिकारी पोर्टल",
      "farmerPortal": "शेतकार पोर्टल", "dashboard": "डॅशबोर्ड", "profile": "प्रोफायल",
      "requests": "मागण्या", "addProduce": "उत्पादन जोडा", "addCrop": "पीक जोडा",
      "myRequests": "म्हज्य मागण्या", "farmerRequests": "शेतकार मागण्या",
      "liveSync": "थेट सिंक", "publicBuyerView": "सार्वजनिक खरेदीदार दृश्य"
    },
    "auth": {
      "roleSelector": "तुमची भूमिका निवडा", "agricultureOfficer": "कृषी अधिकारी", "farmer": "शेतकार",
      "mobileOrEmail": "मोबाइल नंबर वा ईमेल", "password": "पासवर्ड", "signIn": "साइन इन",
      "fullName": "पूर्ण नांव", "mobileNumber": "मोबाइल नंबर", "emailOptional": "ईमेल (पर्यायी)",
      "createAccount": "खातें तयार करा", "designation": "हुद्दो", "department": "खातें",
      "assignedArea": "दिलेली सुवात", "district": "जिल्हो", "state": "राज्य",
      "village": "गांव", "landArea": "जमीन क्षेत्र (एकर)", "farmingType": "शेतीचो प्रकार",
      "welcomeBack": "परत येवकार, {{name}}!", "accountCreated": "खातें तयार जालें! येवकार, {{name}}.",
      "invalidCredentials": "चुकीची लॉगिन म्हायती", "requiredFields": "सगळी गरजेची म्हायती भरा (नांव, मोबाइल, पासवर्ड).",
      "demoLoginFailed": "डेमो लॉगिन अयशस्वी", "networkError": "नेटवर्क त्रुटी",
      "logoutSuccess": "तुमी भायर सरल्यात.",
      "officerLoginRequired": "अधिकारी पोर्टल वापरपाक कृषी अधिकारी म्हणून लॉगिन करा.",
      "farmerLoginRequired": "शेतकार पोर्टल वापरपाक शेतकार म्हणून लॉगिन करा.",
      "registrationFailed": "नोंदणी जाली ना. म्हायती तपासा.", "switchedRole": "{{role}} कडे बदललें"
    },
    "landing": {
      "verifiedPlatform": "प्रमाणित स्थानिक कृषी उत्पादन मंच", "title": "सोदा. तपासा. जोडा.",
      "subtitle": "अ‍ॅग्रीफ्लो शेतकारांक आनी अधिकाऱ्यांक स्थानिक पिकांची तपासिल्ली म्हायती दवरपाक मजत करता.",
      "searchVerifiedProduce": "तपासिल्लें उत्पादन सोदा", "findVerifiedProduce": "उत्पादन सोदा",
      "quickDiscovery": "वाठारानुसार रोकडें उत्पादन सोद", "cropName": "पिकाचें नांव",
      "cropPlaceholder": "उदा: कांदो, टोमॅटो...", "state": "राज्य", "district": "जिल्हो",
      "allStates": "सगळीं राज्यां", "allDistricts": "सगळे जिल्हे", "howItWorks": "अ‍ॅग्रीफ्लो कशें काम करता",
      "workflowIntro": "स्थानिक शेतीक खुल्या बाजाराकडे जोडपी पारदर्शक तपासणी पद्धत.",
      "sihPlatform": "SIH प्लॅटफॉर्म", "tagLine": "सोदा. तपासा. जोडा."
    },
    "howItWorks": {
      "farmerSubmission": "शेतकाराची नोंदणी",
      "farmerSubmissionDesc": "शेतकार शेताचे, जमिनीचे आनी येवपी पिकाचे तपशील तपासणी खातीर सादर करतात.",
      "officerVerification": "अधिकारी तपासणी",
      "officerVerificationDesc": "स्थानिक कृषी अधिकारी शेतांत वचून तपासणी करतात आनी प्रमाणित उत्पादन उजवाडायतात.",
      "publicDiscovery": "सार्वजनिक सोद आनी संपर्क",
      "publicDiscoveryDesc": "खरेदीदार कसल्याच लॉगिन अडखळी बगर प्रमाणित उत्पादनां सोदून काडूंक शकतात."
    },
    "roles": {
      "farmers": "शेतकारां खातीर", "officers": "कृषी अधिकाऱ्यां खातीर", "buyers": "खरेदीदार आनी व्यापाऱ्यां खातीर",
      "farmerTitle": "पिकांची थेट दृश्यता", "officerTitle": "अधिकार वाठार आनी विश्वास",
      "buyerTitle": "प्रमाणित पुरवठ्याचो सोद",
      "farmerItem1": "शेतकार प्रोफाइल आनी जमिनीची नोंद करा",
      "farmerItem2": "स्थानिक तपासणी खातीर येवपी पीक सादर करा",
      "farmerItem3": "थेट स्थिती पळयात: बाकी → तपासिल्लें / नाकारिल्लें",
      "officerItem1": "स्थानिक उत्पादनां थेट जोडा",
      "officerItem2": "शेतकारांच्या अर्जांची प्रत्यक्ष तपासणी करा",
      "officerItem3": "प्रमाण आनी उपलब्धता अद्ययावत करा",
      "buyerItem1": "लॉगिन बगर रोकडीं उत्पादनां सोदा",
      "buyerItem2": "राज्य, जिल्हो, वाठार आनी प्रमाणा प्रमाण फिल्टर करा",
      "buyerItem3": "विक्रेत्यांक थेट खरेदी विचारणा धाडा"
    },
    "produce": {
      "title": "प्रमाणित उत्पादन सोद",
      "subtitle": "स्थानिक कृषी अधिकाऱ्यांनी तपासिल्ली उपलब्ध आनी फुडलीं पिकां सोदा.",
      "searchCropName": "पिकाचें नांव सोदा", "state": "राज्य", "district": "जिल्हो", "areaBlock": "वाठार / ब्लॉक",
      "minQty": "उणें प्रमाण (टन)", "maxQty": "चડ प्रमाण (टन)", "availBefore": "उपलब्धता तारखे मेरेन/दिसा",
      "verifiedOnly": "फक्त तपासिल्लें (सुचोवप)", "clearFilters": "फिल्टर्स काढा",
      "count": "{{count}} प्रमाणित उत्पादन नोंद दिसता",
      "countPlural": "{{count}} प्रमाणित उत्पादन नोंदी दिसतात",
      "emptyTitle": "उत्पादन नोंदी मेळ्ळ्यो नात",
      "emptyDescription": "तुमचो सोद वाडयात वा लागींच्यो हेर पिकां पळोवपाक फिल्टर्स काढा.",
      "resetAllFilters": "सगळे फिल्टर्स परत सेट करा", "autoSynced": "WebSocket वरवीं थेट सिंक",
      "availableQuantity": "उपलब्ध प्रमाण", "quality": "दर्जो", "availability": "उपलब्धता",
      "sourceOfficer": "अधिकाऱ्यान तपासिल्लें", "sourceFarmer": "शेतकारान तपासिल्लें",
      "verifiedBadge": "✓ तपासिल्लें", "qualityGrade": "दर्जो श्रेणी", "verificationSource": "तपासणी मूळ",
      "fieldNotes": "अधिकारी तपासणी टिपणी",
      "purchaseTitle": "खरेदी विचारणा / मागणी धाडा",
      "purchaseSubtitle": "प्रमाणित शेतकाराकडे थेट जोडूंक तुमची गरज सादर करा.",
      "yourName": "तुमचें नांव / कंपनी", "contact": "संपर्क नंबर / ईमेल",
      "requestedQty": "गरजेचें प्रमाण", "message": "संदेश / गरजो", "sendRequest": "खरेदी विनंती धाडा",
      "notFound": "उत्पादन नोंद मेळ्ळी ना", "noLogin": "लॉगिनची गरज ना", "unitLabel": "एकक"
    },
    "officer": {
      "portal": "कृषी अधिकारी पोर्टल", "subtitle": "स्थानिक उत्पादनां व्यवस्थापित करा, शेतकार अर्ज तपासा",
      "profile": "प्रोफायल बदल करा", "totalRecords": "एकूण नोंदी", "totalRecordsHint": "तुमच्या वाठारांत",
      "availableQty": "उपलब्ध प्रमाण", "availableQtyHint": "तपासिल्लें पीक", "farmerRequests": "शेतकार अर्ज",
      "pending": "तपासणी बाकी", "verifiedRecords": "तपासिल्ल्यो नोंदी", "verifiedRecordsHint": "खरेदीदारांक उपलब्ध",
      "queueTitle": "शेतकार तपासणी अर्ज", "queueSubtitle": "तुमच्या वाठारांत तपासणी खातीर राविल्ले शेतकार",
      "queueEmpty": "सगळें काम जालें! कसलेच अर्ज बाकी नात.",
      "localProduceTitle": "स्थानिक कृषी उत्पादनां", "localProduceSubtitle": "तुमच्या अधिकारांत उजवाडायिल्लीं उत्पादनां",
      "addProduce": "+ उत्पादन जोडा", "editProduce": "उत्पादन बदला", "addProduceModalTitle": "+ स्थानिक उत्पादन जोडा",
      "modalSubtitle": "अधिकाऱ्यान थेट नोंद केल्लें उत्पादन तपासिल्लें म्हणून मानतले",
      "savePublish": "सांबाळा आनी उजवाडावंक", "verify": "तपासा", "reject": "नाकारा",
      "pendingBadge": "🟡 तपासणी बाकी", "directOfficerEntry": "अधिकाऱ्याची थेट नोंद",
      "markUnavailable": "अनुपलब्ध म्हणून खूण करा", "markAvailable": "उपलब्ध म्हणून खूण करा",
      "editProduceAction": "उत्पादन बदला", "deleteProduce": "नोंद काडून उडयात",
      "deleteConfirm": "तुमी ही उत्पादन नोंद काडून उडोवंक सोदतात?", "rejectTitle": "शेतकार अर्ज नाकारा",
      "rejectDescription": "नाकारपाचें कारण स्पश्ट करा",
      "rejectionReason": "कारण / दुरुस्ती गरज",
      "rejectionPlaceholder": "उदा: अपेक्षित पीक जमिनीच्या क्षेत्राकडे जुळना; परत मेजा.",
      "confirmRejection": "नकार पको करा", "fieldInspected": "अधिकाऱ्यान शेतांत वचून तपासलें",
      "verificationSuccess": "✓ शेतकार नोंद तपासली आनी उजवाडायली!",
      "rejectionSuccess": "अर्ज नाकारलो आनी शेतकाराक म्हायती धाडली.",
      "provideReason": "नाकारपाचें कारण सांगा", "noProduceYet": "तुमच्या वाठारांत अजून पिकां नोंद जाल्लीं नात.",
      "cropCol": "पीक", "qtyCol": "प्रमाण", "locationCol": "सुवात", "availDateCol": "उपलब्धता तारीख",
      "qualityCol": "दर्जो", "sourceCol": "मूळ", "statusCol": "स्थिती", "actionsCol": "कृती",
      "officerRecordedSuccess": "✓ अधिकाऱ्यान थेट नोंद केलें आनी तपासलें!",
      "updateProduceSuccess": "उत्पादन अद्ययावत जालें"
    },
    "farmer": {
      "portal": "शेतकार पोर्टल", "myProfile": "म्हजें शेतकार प्रोफायल",
      "assignedOfficer": "तुमचे नियुक्त स्थानिक कृषी अधिकारी", "assignedOfficerHint": "अर्ज हांगा वतात",
      "totalSubmissions": "एकूण अर्ज", "pending": "बाकी", "verified": "तपासिल्लें & चालू",
      "rejected": "नाकारिल्लें", "requestsTitle": "म्हज्यो पीक तपासणी विनंत्यो",
      "requestsSubtitle": "स्थानिक कृषी अधिकाऱ्या कडल्यान स्थिती जाणा जायात",
      "addCrop": "+ पीक म्हायती जोडा", "addCropButton": "+ पीक जोडा", "myCropDetails": "+ पिकाचे तपशील जोडा",
      "submittedToOfficer": "दिलेली म्हायती तपासणी खातीर स्थानिक अधिकाऱ्याकडे वतली",
      "submitToOfficer": "स्थानिक अधिकाऱ्याक सादर करा", "noCrops": "अजून पिकां नोंद करूंक नात",
      "noCropsDescription": "तपासणी खातीर पिकाचे तपशील जोडा.", "addFirstCrop": "पयलें पीक जोडा",
      "pendingStatus": "🟡 तपासणी बाकी", "verifiedStatus": "🟢 ✓ तपासिल्लें", "rejectedStatus": "🔴 नाकारिल्लें",
      "expectedHarvest": "अपेक्षित काढणी तारीख", "cultivatedArea": "लागवड क्षेत्र", "expectedYield": "अपेक्षित पीक",
      "cropStage": "पिकाचो पांवडो", "officerFeedback": "अधिकाऱ्याचो प्रतिसाद:", "submissionSuccess": "✓ पीक सादर जालें! तपासणी खातीर अधिकाऱ्याकडे धाडलें.",
      "verificationStatus": "बाकी → तपासिल्लें / नाकारिल्लें", "locationRouting": "सुवात मार्ग (स्थानिक अधिकाऱ्याक)",
      "additionalNotes": "हेर शेती नोंदी", "farmingNotesPlaceholder": "शेती पद्धती, उदक, सारें..."
    },
    "profile": {
      "title": "म्हजें प्रोफायल", "subtitle": "खात्याची म्हायती आनी शेती तपशील सांबाळा",
      "saveChanges": "बदल सांबाळा", "fullName": "पूर्ण नांव", "village": "गांव",
      "area": "वाठार / ब्लॉक", "district": "जिल्हो", "state": "राज्य", "landArea": "जमीन क्षेत्र",
      "landUnit": "जमीन एकक", "farmingType": "शेती प्रकार", "officialEmail": "अधिकृत ईमेल",
      "designation": "अधिकारी हुद्दो", "department": "खातें", "contactNumber": "संपर्क नंबर",
      "assignedArea": "दिलेली सुवात / ब्लॉक", "profileUpdated": "प्रोफायल अद्ययावत जालें"
    },
    "crops": {
      "onion": "कांदो", "tomato": "टोमॅटो", "potato": "बटाट", "rice": "भात / तांदूळ",
      "wheat": "गंव", "maize": "मको", "carrot": "गाजर", "cabbage": "कोबी",
      "cauliflower": "फुलकोबी", "garlic": "लोसूण", "ginger": "आलें", "banana": "केळें",
      "mango": "आंबो", "groundnut": "बिकणां", "sugarcane": "ऊस", "cotton": "कापूस"
    },
    "produce_types": {
      "tubers": "कंदमुळां", "vegetable": "भाजीपालो", "vegetable_bulbs": "भाजी / कंद",
      "field_crop": "शेतांतलें पीक", "cereals": "धान्य", "fruits": "फळां",
      "cash_crops": "रोकड पिकां", "spices": "मसाले"
    },
    "units": { "tons": "टन", "quintals": "क्विंटल", "kg": "किलो", "acres": "एकर", "hectares": "हेक्टर" },
    "qualities": {
      "gradeA": "ग्रेड A", "gradeB": "ग्रेड B", "gradeC": "ग्रेड C",
      "gradeAPremium": "ग्रेड A (उत्कृष्ट)", "gradeBStandard": "ग्रेड B (मध्यम)", "gradeCFair": "ग्रेड C (सादारण)"
    },
    "crop_stages": {
      "bulbDevelopment": "कंद वाड", "vegetative": "वाडपाचो पांवडो",
      "flowering": "फूल येवपाचो पांवडो", "readyForHarvest": "काढणी खातीर तयार", "preHarvest": "काढणी आदीं"
    },
    "statuses": {
      "verified": "तपासिल्लें", "pending": "बाकी", "rejected": "नाकारिल्लें",
      "available": "उपलब्ध", "unavailable": "अनुपलब्ध"
    },
    "sources": {
      "officerVerified": "अधिकाऱ्यान तपासिल्लें", "farmerVerified": "शेतकारान तपासिल्लें",
      "directOfficerEntry": "अधिकाऱ्याची थेट नोंद"
    },
    "notifications": {
      "newProduceAdded": "🌾 नवें उत्पादन जोडलें: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 उत्पादन अद्ययावत जालें: {{crop}}",
      "newFarmerSubmission": "📋 नवो शेतकार अर्ज: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ पीक तपासलें: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ शेतकार अर्ज नाकारलो: {{crop}}",
      "purchaseInquiry": "💼 खरेदी विचारणा: खरेदीदारान {{qty}} {{unit}} {{crop}} मागलां",
      "demoReset": "🔄 डेमो डेटा मूळ स्थितींत परत आयलो",
      "inquirySent": "✓ खरेदी विचारणा शेतकार/अधिकाऱ्याक धाडली!",
      "statusUpdated": "उत्पादन स्थिती अद्ययावत जाली", "deleted": "उत्पादन नोंद काडून उडयली"
    },
    "demo": {
      "controlsTitle": "SIH डेमो नियंत्रणां:", "officerBtn": "अधिकारी (रवी कुमार)",
      "farmerBtn": "शेतकार (कुमार)", "buyerBtn": "सार्वजनिक खरेदीदार दृश्य",
      "resetBtn": "डेमो परत सेट करा", "resetConfirm": "डेटाबेस मूळ स्थितींत परत सेट करचो?"
    }
  },
  "mai": {
    "lang": { "name": "Maithili", "nativeName": "मैथिली", "code": "mai", "dir": "ltr" },
    "common": {
      "language": "भाषा", "login": "लॉगिन", "register": "पंजीकरण", "logout": "लॉगआउट",
      "dashboard": "डैशबोर्ड", "profile": "प्रोफाइल", "save": "सहेजू", "cancel": "रद्द करू",
      "close": "बंद करू", "submit": "जमा करू", "refresh": "रिफ્રेश करू", "search": "खोजू",
      "clearFilters": "फिल्टर हटाउ", "loading": "लोड भ रहल अछि...", "viewDetails": "विवरण देखू",
      "allStates": "सब राज्य", "allDistricts": "सब जिला", "allAreas": "सब क्षेत्र",
      "verified": "प्रमाणित", "pending": "लंबित", "rejected": "अस्वीकृत",
      "available": "उपलब्ध", "unavailable": "अनुपलब्ध", "yes": "हँ", "no": "नहि",
      "continue": "जारी राखू", "send": "पठाउ", "back": "पाछाँ", "next": "आगाँ",
      "previous": "पाछिला", "edit": "संपादित करू", "delete": "हटाउ", "status": "स्थिति",
      "role": "भूमिका", "user": "प्रयोक्ता", "liveSync": "लाइव सिंक", "reconnecting": "पुनः जुड़ि रहल अछि...",
      "reset": "रीसेट", "actions": "कार्रवाई", "crop": "फसल", "quantity": "मात्रा",
      "location": "स्थान", "date": "तिथि", "notes": "टिप्पणी"
    },
    "navigation": {
      "home": "मुख्य पृष्ठ", "viewProduce": "उत्पाद देखू", "officerPortal": "अधिकारी पोर्टल",
      "farmerPortal": "किसान पोर्टल", "dashboard": "डैशबोर्ड", "profile": "प्रोफाइल",
      "requests": "अनुरोध", "addProduce": "उत्पाद जोड़ू", "addCrop": "फसल जोड़ू",
      "myRequests": "हमर अनुरोध", "farmerRequests": "किसानक अनुरोध",
      "liveSync": "लाइव सिंक", "publicBuyerView": "सार्वजनिक क्रेता दृश्य"
    },
    "auth": {
      "roleSelector": "अपन भूमिका चुनू", "agricultureOfficer": "कृषि पदाधिकारी", "farmer": "किसान",
      "mobileOrEmail": "मोबाइल नंबर वा ईमेल", "password": "पासवर्ड", "signIn": "साइन इन",
      "fullName": "पूरा नाम", "mobileNumber": "मोबाइल नंबर", "emailOptional": "ईमेल (वैकल्पिक)",
      "createAccount": "खाता बनाउ", "designation": "पद", "department": "विभाग",
      "assignedArea": "नियुक्त क्षेत्र", "district": "जिला", "state": "राज्य",
      "village": "गाम", "landArea": "जमीनक क्षेत्रफल (एकड़)", "farmingType": "खेतीक प्रकार",
      "welcomeBack": "पुनः स्वागत अछि, {{name}}!", "accountCreated": "खाता बनि गेल! स्वागत अछि, {{name}}.",
      "invalidCredentials": "अमान्य क्रेडेंशियल", "requiredFields": "कृपया सभ आवश्यक जानकारी भरू।",
      "demoLoginFailed": "डेमो लॉगिन विफल", "networkError": "नेटवर्क त्रुटि",
      "logoutSuccess": "अहाँ सफलतापूर्वक साइन आउट भ गेलाह।",
      "officerLoginRequired": "पदाधिकारी पोर्टल लेल कृषि पदाधिकारी रूपमे लॉगिन करू।",
      "farmerLoginRequired": "किसान पोर्टल लेल किसान रूपमे लॉगिन करू।",
      "registrationFailed": "पंजीकरण विफल रहल।", "switchedRole": "{{role}} मे बदलल गेल"
    },
    "landing": {
      "verifiedPlatform": "प्रमाणित स्थानीय कृषि उत्पाद मंच", "title": "खोजू। प्रमाणित करू। जुड़ू।",
      "subtitle": "एग्रीफ्लो किसान आ कृषि पदाधिकारीकें सत्यापित उपजक जानकारी रखबामे सहयोग करैत अछि।",
      "searchVerifiedProduce": "प्रमाणित उत्पाद खोजू", "findVerifiedProduce": "उत्पाद खोजू",
      "quickDiscovery": "क्षेत्रवार त्वरित खोज", "cropName": "फसलक नाम",
      "cropPlaceholder": "उदा: पियाज, टमाटर...", "state": "राज्य", "district": "जिला",
      "allStates": "सब राज्य", "allDistricts": "सब जिला", "howItWorks": "एग्रीफ्लो कोना काज करैत अछि",
      "workflowIntro": "स्थानीय कृषिकें खुला बजारसँ जोड़यवला पारदर्शी प्रमाणीकरण प्रक्रिया।",
      "sihPlatform": "SIH मंच", "tagLine": "खोजू। प्रमाणित करू। जुड़ू।"
    },
    "howItWorks": {
      "farmerSubmission": "किसानक प्रविष्टि",
      "farmerSubmissionDesc": "किसान अपन खेत, फसलक अवस्था आ संभावित उपज सत्यापन लेल दर्ज करैत छथि।",
      "officerVerification": "पदाधिकारी सत्यापन",
      "officerVerificationDesc": "स्थानीय कृषि पदाधिकारी खेतक निरीक्षण कऽ प्रमाणित उत्पाद प्रकाशित करैत छथि।",
      "publicDiscovery": "सार्वजनिक खोज आ संपर्क",
      "publicDiscoveryDesc": "क्रेता बिना कोनो लॉगिन बाधाक फसल, जिला आ मात्रा अनुसार सत्यापित उत्पाद खोजि सकैत छथि।"
    },
    "roles": {
      "farmers": "किसानक लेल", "officers": "कृषि पदाधिकारीक लेल", "buyers": "क्रेता आ व्यापारीक लेल",
      "farmerTitle": "फसलक सीधा प्रदर्शन", "officerTitle": "क्षेत्राधिकार आ विश्वास",
      "buyerTitle": "सत्यापित आपूर्तिक खोज",
      "farmerItem1": "खेती प्रोफाइल आ जमीनक पंजीकरण करू",
      "farmerItem2": "सत्यापन लेल आगामी उपज दर्ज करू",
      "farmerItem3": "वास्तविक स्थिति जानू: लंबित → प्रमाणित / अस्वीकृत",
      "officerItem1": "स्थानीय उत्पाद सोझे जोड़ू",
      "officerItem2": "किसानक आवेदनक खेत निरीक्षण करू",
      "officerItem3": "मात्रा आ उपलब्धता अपडेट करू",
      "buyerItem1": "बिना लॉगिन तुरंत उत्पाद खोजू",
      "buyerItem2": "राज्य, जिला, क्षेत्र आ मात्रा अनुसार फिल्टर करू",
      "buyerItem3": "सत्यापित किसानकें सोझे खरीद अनुरोध पठाउ"
    },
    "produce": {
      "title": "प्रमाणित उत्पाद खोज",
      "subtitle": "स्थानीय कृषि पदाधिकारी द्वारा प्रमाणित उपलब्ध आ आगामी कृषि उत्पाद खोजू।",
      "searchCropName": "फसलक नाम खोजू", "state": "राज्य", "district": "जिला", "areaBlock": "क्षेत्र / ब्लॉक",
      "minQty": "न्यूनतम मात्रा (टन)", "maxQty": "अधिकतम मात्रा (टन)", "availBefore": "उपलब्धता तिथिसँ पहिने/धरि",
      "verifiedOnly": "केवल प्रमाणित (अनुशंसित)", "clearFilters": "फिल्टर हटाउ",
      "count": "{{count}} प्रमाणित उत्पाद देखल जा रहल अछि",
      "countPlural": "{{count}} प्रमाणित उत्पाद देखल जा रहल अछि",
      "emptyTitle": "कोनो उत्पाद नहि भेटल",
      "emptyDescription": "अपन खोज बढ़ाउ वा फिल्टर हटाउ।",
      "resetAllFilters": "सब फिल्टर रीसेट करू", "autoSynced": "WebSocket द्वारा लाइव सिंक",
      "availableQuantity": "उपलब्ध मात्रा", "quality": "गुणवत्ता", "availability": "उपलब्धता",
      "sourceOfficer": "पदाधिकारी प्रमाणित", "sourceFarmer": "किसान प्रमाणित",
      "verifiedBadge": "✓ प्रमाणित", "qualityGrade": "गुणवत्ता ग्रेड", "verificationSource": "प्रमाणीकरण स्रोत",
      "fieldNotes": "खेत निरीक्षण टिप्पणी",
      "purchaseTitle": "खरीद पूछताछ / अनुरोध पठाउ",
      "purchaseSubtitle": "प्रमाणित किसान / पदाधिकारीसँ सोझे जुड़बाक लेल आवश्यकता दर्ज करू।",
      "yourName": "अहाँक नाम / कंपनी", "contact": "संपर्क नंबर / ईमेल",
      "requestedQty": "आवश्यक मात्रा", "message": "संदेश / आवश्यकता", "sendRequest": "खरीद अनुरोध पठाउ",
      "notFound": "उत्पाद नहि भेटल", "noLogin": "लॉगिनक आवश्यकता नहि", "unitLabel": "इकाई"
    },
    "officer": {
      "portal": "कृषि पदाधिकारी पोर्टल", "subtitle": "स्थानीय उत्पादक प्रबंधन करू, किसानक आवेदन सत्यापित करू",
      "profile": "प्रोफाइल संपादित करू", "totalRecords": "कुल उत्पाद", "totalRecordsHint": "अहाँक क्षेत्रमे",
      "availableQty": "उपलब्ध मात्रा", "availableQtyHint": "प्रमाणित उत्पाद", "farmerRequests": "किसानक अनुरोध",
      "pending": "खेत निरीक्षण बाकी", "verifiedRecords": "प्रमाणित उत्पाद", "verifiedRecordsHint": "क्रेता लेल उपलब्ध",
      "queueTitle": "किसान सत्यापन अनुरोध", "queueSubtitle": "अहाँक क्षेत्रमे निरीक्षणक बाट जोहि रहल किसान",
      "queueEmpty": "सभ काज समाप्त! कोनो अनुरोध लंबित नहि अछि।",
      "localProduceTitle": "स्थानीय कृषि उत्पाद", "localProduceSubtitle": "अहाँक क्षेत्राधिकारमे प्रकाशित उत्पाद",
      "addProduce": "+ उत्पाद जोड़ू", "editProduce": "उत्पाद संपादित करू", "addProduceModalTitle": "+ स्थानीय उत्पाद जोड़ू",
      "modalSubtitle": "पदाधिकारी द्वारा सोझे दर्ज कएल उत्पाद प्रमाणित मानल जायत",
      "savePublish": "सहेजू आ प्रकाशित करू", "verify": "सत्यापित करू", "reject": "अस्वीकार करू",
      "pendingBadge": "🟡 सत्यापन बाकी", "directOfficerEntry": "पदाधिकारीक सीधा प्रविष्टि",
      "markUnavailable": "अनुपलब्ध चिह्नित करू", "markAvailable": "उपलब्ध चिह्नित करू",
      "editProduceAction": "उत्पाद संपादित करू", "deleteProduce": "उत्पाद हटाउ",
      "deleteConfirm": "की अहाँ सचमुच ई उत्पाद हटाबय चाहैत छी?", "rejectTitle": "किसानक आवेदन अस्वीकार करू",
      "rejectDescription": "अस्वीकृतिक स्पष्ट कारण बताउ",
      "rejectionReason": "कारण / आवश्यक सुधार",
      "rejectionPlaceholder": "उदा: संभावित उपज जमीनक क्षेत्रफलसँ मेल नहि खाइत अछि; पुनः नापू।",
      "confirmRejection": "अस्वीकृति पुष्टि करू", "fieldInspected": "पदाधिकारी द्वारा खेत निरीक्षण कऽ सत्यापित",
      "verificationSuccess": "✓ किसानक आवेदन सत्यापित भेल आ सार्वजनिक कएल गेल!",
      "rejectionSuccess": "अनुरोध अस्वीकार भेल आ किसानकें सूचित कएल गेल।",
      "provideReason": "कृपया अस्वीकृतिक कारण बताउ", "noProduceYet": "अहाँक क्षेत्रमे अखन कोनो उत्पाद दर्ज नहि अछि।",
      "cropCol": "फसल", "qtyCol": "मात्रा", "locationCol": "स्थान", "availDateCol": "उपलब्धता तिथि",
      "qualityCol": "गुणवत्ता", "sourceCol": "स्रोत", "statusCol": "स्थिति", "actionsCol": "कार्रवाई",
      "officerRecordedSuccess": "✓ पदाधिकारी द्वारा सोझे दर्ज आ सत्यापित!",
      "updateProduceSuccess": "उत्पाद सफलतापूर्वक अपडेट भेल"
    },
    "farmer": {
      "portal": "किसान पोर्टल", "myProfile": "हमर कृषि प्रोफाइल",
      "assignedOfficer": "अहाँक स्थानीय कृषि पदाधिकारी", "assignedOfficerHint": "आवेदन एतय जाइत अछि",
      "totalSubmissions": "कुल आवेदन", "pending": "लंबित", "verified": "प्रमाणित & सक्रिय",
      "rejected": "अस्वीकृत", "requestsTitle": "हमर फसल सत्यापन अनुरोध",
      "requestsSubtitle": "कृषि पदाधिकारीसँ स्थिति जानू",
      "addCrop": "+ फसल विवरण जोड़ू", "addCropButton": "+ फसल जोड़ू", "myCropDetails": "+ खेतीक विवरण जोड़ू",
      "submittedToOfficer": "सत्यापन लेल स्थानीय कृषि पदाधिकारीकें पठाओल जायत",
      "submitToOfficer": "पदाधिकारीकें सबमिट करू", "noCrops": "अखन कोनो फसल जमा नहि अछि",
      "noCropsDescription": "स्थानीय सत्यापन लेल वर्तमान खेतीक विवरण जोड़ू।", "addFirstCrop": "पहिल फसल जोड़ू",
      "pendingStatus": "🟡 सत्यापन बाकी", "verifiedStatus": "🟢 ✓ प्रमाणित", "rejectedStatus": "🔴 अस्वीकृत",
      "expectedHarvest": "संभावित कटनी", "cultivatedArea": "खेतीक क्षेत्रफल", "expectedYield": "संभावित उपज",
      "cropStage": "फसलक अवस्था", "officerFeedback": "पदाधिकारीक टिप्पणी:", "submissionSuccess": "✓ फसल दर्ज भेल! सत्यापन लेल पठाओल गेल।",
      "verificationStatus": "लंबित → प्रमाणित / अस्वीकृत", "locationRouting": "स्थान मार्ग (स्थानीय पदाधिकारी लेल)",
      "additionalNotes": "अतिरिक्त खेती टिप्पणी", "farmingNotesPlaceholder": "खेती विधि, पटवन, खाद विवरण..."
    },
    "profile": {
      "title": "हमर प्रोफाइल", "subtitle": "अपन खाता आ खेतीक विवरण प्रबंधित करू",
      "saveChanges": "परिवर्तन सहेजू", "fullName": "पूरा नाम", "village": "गाम",
      "area": "क्षेत्र / ब्लॉक", "district": "जिला", "state": "राज्य", "landArea": "जमीनक क्षेत्रफल",
      "landUnit": "जमीनक इकाई", "farmingType": "खेतीक प्रकार", "officialEmail": "सरकारी ईमेल",
      "designation": "पदाधिकारीक पद", "department": "विभाग", "contactNumber": "संपर्क नंबर",
      "assignedArea": "नियुक्त क्षेत्र / ब्लॉक", "profileUpdated": "प्रोफाइल सफलतापूर्वक अपडेट भेल"
    },
    "crops": {
      "onion": "पियाज", "tomato": "टमाटर", "potato": "आलू", "rice": "धान / चाउर",
      "wheat": "गेहूँ", "maize": "मकई", "carrot": "गाजर", "cabbage": "कोबी",
      "cauliflower": "फूलकोबी", "garlic": "लहसुन", "ginger": "आदि", "banana": "केरा",
      "mango": "आम", "groundnut": "बादाम", "sugarcane": "ऊख", "cotton": "कपास"
    },
    "produce_types": {
      "tubers": "कंदमूल", "vegetable": "तरकारी", "vegetable_bulbs": "तरकारी / कंद",
      "field_crop": "खेतक फसल", "cereals": "अनाज", "fruits": "फल",
      "cash_crops": "नकदी फसल", "spices": "मसाला"
    },
    "units": { "tons": "टन", "quintals": "क्विंटल", "kg": "किलो", "acres": "एकड़", "hectares": "हेक्टेयर" },
    "qualities": {
      "gradeA": "ग्रेड A", "gradeB": "ग्रेड B", "gradeC": "ग्रेड C",
      "gradeAPremium": "ग्रेड A (उत्कृष्ट)", "gradeBStandard": "ग्रेड B (मानक)", "gradeCFair": "ग्रेड C (साधारण)"
    },
    "crop_stages": {
      "bulbDevelopment": "कंद विकास", "vegetative": "वानस्पतिक अवस्था",
      "flowering": "फूलक अवस्था", "readyForHarvest": "कटनी लेल तैयार", "preHarvest": "कटनीसँ पूर्व"
    },
    "statuses": {
      "verified": "प्रमाणित", "pending": "लंबित", "rejected": "अस्वीकृत",
      "available": "उपलब्ध", "unavailable": "अनुपलब्ध"
    },
    "sources": {
      "officerVerified": "पदाधिकारी प्रमाणित", "farmerVerified": "किसान प्रमाणित",
      "directOfficerEntry": "पदाधिकारीक सीधा प्रविष्टि"
    },
    "notifications": {
      "newProduceAdded": "🌾 नव उत्पाद जुड़ल: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 उत्पाद अपडेट भेल: {{crop}}",
      "newFarmerSubmission": "📋 नव किसान आवेदन: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ फसल सत्यापित: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ किसान अनुरोध अस्वीकृत: {{crop}}",
      "purchaseInquiry": "💼 खरीद पूछताछ: क्रेता {{qty}} {{unit}} {{crop}} मँगने छथि",
      "demoReset": "🔄 डेमो डेटा पुनः सेट भेल",
      "inquirySent": "✓ खरीद पूछताछ किसान / पदाधिकारीकें पठाओल गेल!",
      "statusUpdated": "उत्पाद स्थिति अपडेट भेल", "deleted": "उत्पाद हटाओल गेल"
    },
    "demo": {
      "controlsTitle": "SIH डेमो नियंत्रण:", "officerBtn": "पदाधिकारी (रवि कुमार)",
      "farmerBtn": "किसान (कुमार)", "buyerBtn": "सार्वजनिक क्रेता दृश्य",
      "resetBtn": "डेमो रीसेट", "resetConfirm": "की अहाँ डेटाबेসকें आरंभिक स्थितिमे रीसेट करब चाहैत छी?"
    }
  },
  "doi": {
    "lang": { "name": "Dogri", "nativeName": "डोगरी", "code": "doi", "dir": "ltr" },
    "common": {
      "language": "बोली/भाषा", "login": "लागइन", "register": "रजिस्टर", "logout": "लागआऊट",
      "dashboard": "डैशबोर्ड", "profile": "प्रोफाइल", "save": "संजोओ", "cancel": "रद्द करो",
      "close": "बंद करो", "submit": "जमा करो", "refresh": "ताज़ा करो", "search": "खोजो",
      "clearFilters": "फिल्टर हटाओ", "loading": "लोड होंदा ऐ...", "viewDetails": "तफसील दिक्खो",
      "allStates": "सब्भै रियासतां", "allDistricts": "सब्भै ज़िले", "allAreas": "सब्भै इलाके",
      "verified": "प्रमाणित", "pending": "बाकी", "rejected": "रद्द कीता",
      "available": "लभ्भदा", "unavailable": "नी लब्भदा", "yes": "हाँ", "no": "ना",
      "continue": "जारी रक्खो", "send": "भेजो", "back": "पिच्छें", "next": "अगला",
      "previous": "पिच्छला", "edit": "बदलो", "delete": "मिटाओ", "status": "हालत",
      "role": "रोल", "user": "वरतणदार", "liveSync": "लाइव सिंक", "reconnecting": "परतियै जुड़दा ऐ...",
      "reset": "मुड़ सैट करो", "actions": "कम्म", "crop": "फसल", "quantity": "मात्रा",
      "location": "जग़ा", "date": "तरीक", "notes": "नोट्स"
    },
    "navigation": {
      "home": "मुख पृष्ठ", "viewProduce": "पैदावार दिक्खो", "officerPortal": "अफसर पोर्टल",
      "farmerPortal": "ज़मींदार पोर्टल", "dashboard": "डैशबोर्ड", "profile": "प्रोफाइल",
      "requests": "दरखास्त", "addProduce": "पैदावार जोड़ो", "addCrop": "फसल जोड़ो",
      "myRequests": "मेरियां दरखास्तां", "farmerRequests": "ज़मींदार दरखास्तां",
      "liveSync": "लाइव सिंक", "publicBuyerView": "खरीददार दृश्य"
    },
    "auth": {
      "roleSelector": "अपनी भूमिका चुनो", "agricultureOfficer": "खेतीबाड़ी अफसर", "farmer": "ज़मींदार / किसान",
      "mobileOrEmail": "मोबाइल नंबर या ईमेल", "password": "पासवर्ड", "signIn": "साइन इन",
      "fullName": "पूरा नांऽ", "mobileNumber": "मोबाइल नंबर", "emailOptional": "ईमेल (मर्जी)",
      "createAccount": "खाता बनाओ", "designation": "अहुदा", "department": "महकमा",
      "assignedArea": "सौंपेआ इलाका", "district": "ज़िला", "state": "रियासत",
      "village": "ग्रांऽ", "landArea": "ज़मीन रकबा (एकड़)", "farmingType": "खेती दी किस्म",
      "welcomeBack": "स्वागत ऐ, {{name}}!", "accountCreated": "खाता बनी गेआ! स्वागत ऐ, {{name}}.",
      "invalidCredentials": "गलत जानकारी", "requiredFields": "सब्भै जरूरी खाने भरो।",
      "demoLoginFailed": "डेमो लागइन फेल", "networkError": "नेटवर्क खराबी",
      "logoutSuccess": "तुस साइन आऊट होई गे।",
      "officerLoginRequired": "खेतीबाड़ी अफसर तौर पर लागइन करो।", "farmerLoginRequired": "ज़मींदार तौर पर लागइन करो।",
      "registrationFailed": "रजिस्ट्रेशन नी होई सकी।", "switchedRole": "{{role}} च बदलेआ गेआ"
    },
    "landing": {
      "verifiedPlatform": "प्रमाणित स्थानीय पैदावार मंच", "title": "लभ्भो। परखो। जुड़ो।",
      "subtitle": "एग्रीफ्लो स्थानीय पैदावार दी प्रमाणित जानकारी रखन च मदद करदा ऐ।",
      "searchVerifiedProduce": "प्रमाणित पैदावार खोजो", "findVerifiedProduce": "पैदावार लभ्भो",
      "quickDiscovery": "इलाके मताबक पैदावार खोज", "cropName": "फसल दा नांऽ",
      "cropPlaceholder": "जियां: प्याज़, टमाटर...", "state": "रियासत", "district": "ज़िला",
      "allStates": "सब्भै रियासतां", "allDistricts": "सब्भै ज़िले", "howItWorks": "एग्रीफ्लो कियां कम्म करदा ऐ",
      "workflowIntro": "स्थानीय खेती गी खुले बजार कन्ने जोड़ने दी इक पारदर्शी प्रणाली।",
      "sihPlatform": "SIH मंच", "tagLine": "लभ्भो। परखो। जुड़ो।"
    },
    "howItWorks": {
      "farmerSubmission": "ज़मींदार दा इंदराज",
      "farmerSubmissionDesc": "ज़मींदार अपनी खेती, रकबे ते पैदावार दी जानकारी स्थानीय जांच लेई दर्ज करदे न।",
      "officerVerification": "अफसर दी जांच",
      "officerVerificationDesc": "स्थानीय खेतीबाड़ी अफसर मौके पर जाईयै तसदीक करदे न ते प्रमाणित पैदावार छापदे न।",
      "publicDiscovery": "लोक खोज ते राबता",
      "publicDiscoveryDesc": "खरीददार बिना रोक-टोक फसल, ज़िले ते मिकदार मताबक पैदावार लब्भी सकदे न।"
    },
    "roles": {
      "farmers": "ज़मींदारें लेई", "officers": "खेतीबाड़ी अफसरें लेई", "buyers": "खरीददारें लेई",
      "farmerTitle": "फसल दी सीधी पहुंच", "officerTitle": "अधिकार क्षेत्र ते भरोसा",
      "buyerTitle": "सच्ची पैदावार दी खोज",
      "farmerItem1": "खेती प्रोफाइल ते ज़मीन रजिस्टर करो",
      "farmerItem2": "जांच लेई औने आह्ली पैदावार जमा करो",
      "farmerItem3": "सच्ची हालत जानो: बाकी → प्रमाणित / रद्द",
      "officerItem1": "इलाके दी प्रमाणित पैदावार सिधै जोड़ो",
      "officerItem2": "ज़मींदारें दी दरखास्तां दी मौके पर पड़ताल करो",
      "officerItem3": "मात्रा ते उपलब्धता अपडेट करो",
      "buyerItem1": "बिना लागइन पैदावार लभ्भो",
      "buyerItem2": "रियासत, ज़िला ते मात्रा मताबक छांटो",
      "buyerItem3": "प्रमाणित किसानें गी सिद्धा संदेश भेजो"
    },
    "produce": {
      "title": "प्रमाणित पैदावार खोज",
      "subtitle": "स्थानीय खेतीबाड़ी अफसरें आसेआ जांची दी पैदावार लभ्भो।",
      "searchCropName": "फसल दा नांऽ खोजो", "state": "रियासत", "district": "ज़िला", "areaBlock": "इलाका / ब्लाक",
      "minQty": "घट्ट शा घट्ट (टन)", "maxQty": "मते शा मता (टन)", "availBefore": "उपलब्धता तरीक तोड़ी",
      "verifiedOnly": "सिर्फ प्रमाणित", "clearFilters": "फिल्टर हटाओ",
      "count": "{{count}} प्रमाणित पैदावार दिक्खने गी लब्भदी ऐ",
      "countPlural": "{{count}} प्रमाणित पैदावार दिक्खने गी लब्भदी ऐ",
      "emptyTitle": "कोई पैदावार नी लब्भी",
      "emptyDescription": "खोज दा दायरा बधाओ या फिल्टर हटाओ।",
      "resetAllFilters": "सब्भै फिल्टर मुड़ सैट करो", "autoSynced": "WebSocket राएं लाइव सिंक",
      "availableQuantity": "मौजूद मात्रा", "quality": "दर्जा", "availability": "उपलब्धता",
      "sourceOfficer": "अफसर आसेआ जांची दी", "sourceFarmer": "ज़मींदार आसेआ जांची दी",
      "verifiedBadge": "✓ प्रमाणित", "qualityGrade": "क्वालिटी दर्जा", "verificationSource": "जांच स्रोत",
      "fieldNotes": "अफसर दे फील्ड नोट्स",
      "purchaseTitle": "खरीद लेई पुच्छ-पड़ताल भेजो",
      "purchaseSubtitle": "प्रमाणित किसान कन्ने सीधे राबते लेई जरूरत लिखो।",
      "yourName": "तुंदा नांऽ / कंपनी", "contact": "फोन नंबर / ईमेल",
      "requestedQty": "लोड़दी मात्रा", "message": "सुनेहा / लोड़ां", "sendRequest": "खरीद दरखास्त भेजो",
      "notFound": "पैदावार नी लब्भी", "noLogin": "लागइन दी लोड़ नी", "unitLabel": "इकाई"
    },
    "officer": {
      "portal": "खेतीबाड़ी अफसर पोर्टल", "subtitle": "इलाके दी पैदावार सांभो, दरखास्तां जांचो",
      "profile": "प्रोफाइल बदलो", "totalRecords": "कुल रिकार्ड", "totalRecordsHint": "तुंदे इलाके च",
      "availableQty": "मौजूद मात्रा", "availableQtyHint": "प्रमाणित पैदावार", "farmerRequests": "ज़मींदार दरखास्तां",
      "pending": "जांच बाकी", "verifiedRecords": "प्रमाणित रिकार्ड", "verifiedRecordsHint": "खरीददारें लेई लब्भदा",
      "queueTitle": "ज़मींदार तसदीक दरखास्तां", "queueSubtitle": "तुंदे इलाके च जांच दी उडीक च ज़मींदार",
      "queueEmpty": "सब्भ कम्म खत्म! कोई दरखास्त बाकी नी ऐ।",
      "localProduceTitle": "इलाके दी खेती पैदावार", "localProduceSubtitle": "तुंदे अधिकार क्षेत्र च दर्ज पैदावार",
      "addProduce": "+ पैदावार जोड़ो", "editProduce": "पैदावार बदलो", "addProduceModalTitle": "+ स्थानीय पैदावार जोड़ो",
      "modalSubtitle": "अफसर आसेआ दर्ज पैदावार प्रमाणित मंनी जग",
      "savePublish": "संजोओ ते छापो", "verify": "तसदीक करो", "reject": "रद्द करो",
      "pendingBadge": "🟡 जांच बाकी", "directOfficerEntry": "अफसर दा सिद्धा इंदराज",
      "markUnavailable": "अनुपलब्ध दस्सो", "markAvailable": "उपलब्ध दस्सो",
      "editProduceAction": "पैदावार बदलो", "deleteProduce": "रिकार्ड मिटाओ",
      "deleteConfirm": "केह् तुस सचमुच ईह रिकार्ड मिटाना चांह्दे ओ?", "rejectTitle": "दरखास्त रद्द करो",
      "rejectDescription": "रद्द करने दा मुनासिब कारण दस्सो",
      "rejectionReason": "कारण / सुधार दी लोड़",
      "rejectionPlaceholder": "जियां: पैदावार रकबे कन्ने नी रलदी; मुड़ नापो।",
      "confirmRejection": "रद्द करने दी पुष्टि", "fieldInspected": "अफसर आसेआ मौके पर जाईयै तसदीक",
      "verificationSuccess": "✓ दरखास्त प्रमाणित होईयै छापी दित्ती!",
      "rejectionSuccess": "दरखास्त रद्द कीती गेई ते ज़मींदार गी दस्सी दित्ता।",
      "provideReason": "रद्द करने दा कारण दस्सो", "noProduceYet": "तुंदे इलाके च हूनें तोड़ी कोई पैदावार दर्ज नी होई।",
      "cropCol": "फसल", "qtyCol": "मात्रा", "locationCol": "जग़ा", "availDateCol": "उपलब्धता तरीक",
      "qualityCol": "दर्जा", "sourceCol": "स्रोत", "statusCol": "हालत", "actionsCol": "कम्म",
      "officerRecordedSuccess": "✓ अफसर आसेआ सिद्धा दर्ज ते प्रमाणित!",
      "updateProduceSuccess": "पैदावार अपडेट होई गेई"
    },
    "farmer": {
      "portal": "ज़मींदार पोर्टल", "myProfile": "मेरी खेती प्रोफाइल",
      "assignedOfficer": "तुंदे इलाके दे खेतीबाड़ी अफसर", "assignedOfficerHint": "दरखास्तां इत्थै औंदियां न",
      "totalSubmissions": "कुल दरखास्तां", "pending": "बाकी", "verified": "प्रमाणित ते चालू",
      "rejected": "रद्द कीती", "requestsTitle": "मेरी फसल तसदीक दरखास्तां",
      "requestsSubtitle": "अफसर कोला अपनी हालत पुच्छो",
      "addCrop": "+ फसल तफसील जोड़ो", "addCropButton": "+ फसल जोड़ो", "myCropDetails": "+ खेती फसल तफसील जोड़ो",
      "submittedToOfficer": "तफसील तसदीक लेई अफसर गी भेजी जग",
      "submitToOfficer": "अफसर गी भेजो", "noCrops": "अज्जै तोड़ी कोई फसल नी भेजी",
      "noCropsDescription": "तसदीक लेई अपनी फसल दी जानकारी जोड़ो।", "addFirstCrop": "पैहली फसल जोड़ो",
      "pendingStatus": "🟡 जांच बाकी", "verifiedStatus": "🟢 ✓ प्रमाणित", "rejectedStatus": "🔴 रद्द कीती",
      "expectedHarvest": "अंदाजन कटाई तरीक", "cultivatedArea": "खेती रकबा", "expectedYield": "अंदाजन पैदावार",
      "cropStage": "फसल दा दौर", "officerFeedback": "अफसर दी राय:", "submissionSuccess": "✓ फसल जमा होई गेई! तसदीक लेई भेजी दित्ती।",
      "verificationStatus": "बाकी → प्रमाणित / रद्द", "locationRouting": "जग़ा मताबक (स्थानीय अफसर लेई)",
      "additionalNotes": "होर खेती नोट्स", "farmingNotesPlaceholder": "खेती दे तरीके, सिंचाई, खाद तफसील..."
    },
    "profile": {
      "title": "मेरी प्रोफाइल", "subtitle": "अपने खाते ते खेती दी जानकारी सांभो",
      "saveChanges": "बदलाव संजोओ", "fullName": "पूरा नांऽ", "village": "ग्रांऽ",
      "area": "इलाका / ब्लाक", "district": "ज़िला", "state": "रियासत", "landArea": "ज़मीन रकबा",
      "landUnit": "रकबा इकाई", "farmingType": "खेती दी किस्म", "officialEmail": "सरकारी ईमेल",
      "designation": "अफसर अहुदा", "department": "महकमा", "contactNumber": "फोन नंबर",
      "assignedArea": "सौंपेआ इलाका / ब्लाक", "profileUpdated": "प्रोफाइल अपडेट होई गेई"
    },
    "crops": {
      "onion": "प्याज़", "tomato": "टमाटर", "potato": "आलू", "rice": "झोना / चौल",
      "wheat": "कणक", "maize": "छल्ली / मक्की", "carrot": "गाजर", "cabbage": "बंदगोभी",
      "cauliflower": "फुल्ल गोभी", "garlic": "थूम", "ginger": "अद्रक", "banana": "केला",
      "mango": "अंब", "groundnut": "मूँगफली", "sugarcane": "कमंद", "cotton": "कपास"
    },
    "produce_types": {
      "tubers": "जड़ आह्ली फसल", "vegetable": "सब्जी", "vegetable_bulbs": "सब्जी / गांठ",
      "field_crop": "खेत दी फसल", "cereals": "अनाज", "fruits": "फल",
      "cash_crops": "नकदी फसल", "spices": "मसाले"
    },
    "units": { "tons": "टन", "quintals": "क्विंटल", "kg": "किलो", "acres": "एकड़", "hectares": "हेक्टेयर" },
    "qualities": {
      "gradeA": "ग्रेड A", "gradeB": "ग्रेड B", "gradeC": "ग्रेड C",
      "gradeAPremium": "ग्रेड A (बढिया)", "gradeBStandard": "ग्रेड B (आम)", "gradeCFair": "ग्रेड C (ठीक-ठाक)"
    },
    "crop_stages": {
      "bulbDevelopment": "गांठ बन्ना", "vegetative": "बधने दी हालत",
      "flowering": "फुल्ल औना", "readyForHarvest": "कटाई लेई तैयार", "preHarvest": "कटाई शा पैहले"
    },
    "statuses": {
      "verified": "प्रमाणित", "pending": "बाकी", "rejected": "रद्द कीती",
      "available": "लभ्भदा", "unavailable": "नी लब्भदा"
    },
    "sources": {
      "officerVerified": "अफसर आसेआ जांची दी", "farmerVerified": "ज़मींदार आसेआ जांची दी",
      "directOfficerEntry": "अफसर दा सिद्धा इंदराज"
    },
    "notifications": {
      "newProduceAdded": "🌾 नई पैदावार जोड़ी: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 पैदावार अपडेट: {{crop}}",
      "newFarmerSubmission": "📋 नई ज़मींदार दरखास्त: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ फसल प्रमाणित: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ दरखास्त रद्द: {{crop}}",
      "purchaseInquiry": "💼 खरीद पुच्छ: खरीददारें {{qty}} {{unit}} {{crop}} मंग्या ऐ",
      "demoReset": "🔄 डेमो डाटा मुड़ सैट होई गेआ",
      "inquirySent": "✓ खरीद पुच्छ ज़मींदार / अफसर गी भेज दित्ती!",
      "statusUpdated": "हालत अपडेट होई गेई", "deleted": "रिकार्ड मिटाई दित्ता"
    },
    "demo": {
      "controlsTitle": "SIH डेमो कंट्रोल:", "officerBtn": "अफसर (रवि कुमार)",
      "farmerBtn": "ज़मींदार (कुमार)", "buyerBtn": "खरीददार दृश्य",
      "resetBtn": "डेमो मुड़ सैट", "resetConfirm": "केह् तुस डाटाबेस गी शुरू आह्ली स्थिति च लाना चांह्दे ओ?"
    }
  },
  "brx": {
    "lang": { "name": "Bodo", "nativeName": "बड़ो", "code": "brx", "dir": "ltr" },
    "common": {
      "language": "राव", "login": "हाबसिं", "register": "मुं थिसन", "logout": "ओंखारలాं",
      "dashboard": "डैशबर्ड", "profile": "महर", "save": "थिन", "cancel": "नेवसि",
      "close": "फोजोब", "submit": "होगार", "refresh": "गोदान खालाम", "search": "नायगिर",
      "clearFilters": "सायख'नाय बोखार", "loading": "गाखोगासिनो...", "viewDetails": "गुवारै नाय",
      "allStates": "गासै हादोरसा", "allDistricts": "गासै जिल्ला", "allAreas": "गासै ओनसोल",
      "verified": "आनजाद खालामबाय", "pending": "नेनानै दं", "rejected": "नेवसिबाय",
      "available": "मोननो हागौ", "unavailable": "मोननो हाया", "yes": "औ", "no": "नङा",
      "continue": "सालायलांबाय था", "send": "थिनहर", "back": "उनाव", "next": "थांमोखां",
      "previous": "सिगांनि", "edit": "सोलाय", "delete": "दानख'", "status": "थासारि",
      "role": "बिबान", "user": "बाहायग्रा", "liveSync": "थोंजों सिंक", "reconnecting": "फोनांजाब फिनगासिनो...",
      "reset": "फिन फज'", "actions": "हाबा", "crop": "फसल", "quantity": "बिबां",
      "location": "जायगा", "date": "अखथ'", "notes": "नोंद"
    },
    "navigation": {
      "home": "न'", "viewProduce": "दिहुननाय नाय", "officerPortal": "बिबानगिरि पर्टेल",
      "farmerPortal": "आबादारी पर्टेल", "dashboard": "डैशबर्ड", "profile": "महर",
      "requests": "आर'ज", "addProduce": "दिहुननाय दाजाब", "addCrop": "फसल दाजाब",
      "myRequests": "आंनि आर'ज", "farmerRequests": "आबादारी आर'ज",
      "liveSync": "थोंजों सिंक", "publicBuyerView": "बायग्रा नुथाय"
    },
    "auth": {
      "roleSelector": "नोंथांनि बिबान सायख'", "agricultureOfficer": "आबाद बिबानगिरि", "farmer": "आबादारी",
      "mobileOrEmail": "मबाइल अनजिमा एबा ईमेल", "password": "पासवर्ड", "signIn": "हाबसिं",
      "fullName": "आबुं मुं", "mobileNumber": "मबाइल अनजिमा", "emailOptional": "ईमेल (गनायथि)",
      "createAccount": "खाता खुलि", "designation": "बिबान", "department": "बिफान",
      "assignedArea": "होनाय ओनसोल", "district": "जिल्ला", "state": "हादोरसा",
      "village": "गामि", "landArea": "हा बिबां (एकर)", "farmingType": "आबाद रोखोम",
      "welcomeBack": "बरायबाय, {{name}}!", "accountCreated": "खाता खुलिबाय! बरायबाय, {{name}}.",
      "invalidCredentials": "गोरोन्थि हाबसिं मखनाय", "requiredFields": "गासै नांगौ बाहागोफोरखौ सुफुं (मुं, मबाइल, पासवर्ड)।",
      "demoLoginFailed": "डेमो हाबसिंनाय जायासै", "networkError": "नेटवर्क गोरोन्थि",
      "logoutSuccess": "नोंथाङा ओंखारलांबाय।",
      "officerLoginRequired": "आबाद बिबानगिरि बादियै हाबसिं।", "farmerLoginRequired": "आबादारी बादियै हाबसिं।",
      "registrationFailed": "मुं थिसननाय जायासै।", "switchedRole": "{{role}} आव सोलायबाय"
    },
    "landing": {
      "verifiedPlatform": "आनजाद खालामनाय आबाद दिहुनथाय मंच", "title": "नायगिर। आनजाद खालाम। फोनांजाब।",
      "subtitle": "एग्रीफ्लो आबादारी आरो बिबानगिरिफোরखौ आनजाद खालामनाय खौरां दोननायाव हेफाजाब होयो।",
      "searchVerifiedProduce": "आनजाद खालामनाय फसल नायगिर", "findVerifiedProduce": "दिहुनथाय नायगिर",
      "quickDiscovery": "ओनसोल बादियै गोख्रै नायगिर", "cropName": "फसल मुं",
      "cropPlaceholder": "जेरै: फियाज, बिलाथि...", "state": "हादोरसा", "district": "जिल्ला",
      "allStates": "गासै हादोरसा", "allDistricts": "गासै जिल्ला", "howItWorks": "एग्रीफ्लो बोरै खामानि मावो",
      "workflowIntro": "स्थानीय आबादखौ उदां हाथाइजों फोनांजाबग्रा रोखा आनजाद खान्थि।",
      "sihPlatform": "SIH मंच", "tagLine": "नायगिर। आनजाद खालाम। फोनांजाब।"
    },
    "howItWorks": {
      "farmerSubmission": "आबादारीनि गथायनाय",
      "farmerSubmissionDesc": "आबादारीफोरा गावनि आबाद, हा आरो दिहुननायनि खौरां आनजाद खालामनो थाखाय गथायो।",
      "officerVerification": "बिबानगिरिनि आनजाद",
      "officerVerificationDesc": "स्थानीय आबाद बिबानगिरिफोरा नायबिजिरना दिहुनथायखौ फोसावो।",
      "publicDiscovery": "बायग्रा नायगिरनाय आरो फोनांजाब",
      "publicDiscoveryDesc": "बायग्राफोरा जेबो हाबसिं बाधा गैयाबालसेल' आनजाद खालामनाय फसल मोनो।"
    },
    "roles": {
      "farmers": "आबादारीफोरनि थाखाय", "officers": "आबाद बिबानगिरिफोरनि थाखाय", "buyers": "बायग्रा आरो फालांगिरिफोरनि थाखाय",
      "farmerTitle": "फसलनि थोंजों नुथाय", "officerTitle": "गोहो ओनसोल आरो फोथायथि",
      "buyerTitle": "आनजाद खालामनाय दिहुनथाय नायगिरनाय",
      "farmerItem1": "आबाद महर आरो हा मुं थिसन",
      "farmerItem2": "आनजाद खालामनो थाखाय फसल गथाय",
      "farmerItem3": "गोथों थासारि मिथि: नेनानै दं → आनजाद जाबाय / नेवसिबाय",
      "officerItem1": "स्थानीय आनजाद खालामनाय फसल थोंजों दाजाब",
      "officerItem2": "आबादारीनि आर'जखौ नायबिजिर",
      "officerItem3": "बिबां आरो मोननाय थासारि गोदान खालाम",
      "buyerItem1": "हाबसिङाबालसेल' फसल नायगिर",
      "buyerItem2": "हादोरसा, जिल्ला, ओनसोल बादियै सायख'",
      "buyerItem3": "फसल होग्राफोरनो थोंजों बायनाय आर'ज थिनहर"
    },
    "produce": {
      "title": "आनजाद खालामनाय दिहुनथाय नायगिर",
      "subtitle": "आबाद बिबानगिरिफोरजों आनजाद खालामनाय फसल नायगिर।",
      "searchCropName": "फसल मुं नायगिर", "state": "हादोरसा", "district": "जिल्ला", "areaBlock": "ओनसोल / ब्लक",
      "minQty": "खमसिन बिबां (टन)", "maxQty": "बांसिन बिबां (टन)", "availBefore": "मोननाय अखथ' सिगां/आव",
      "verifiedOnly": "आनजाद खालामनाय ल' (मोजां)", "clearFilters": "सायख'नाय बोखार",
      "count": "{{count}} आनजाद खालामनाय दिहुनथाय नुदों",
      "countPlural": "{{count}} आनजाद खालामनाय दिहुनथाय नुदों",
      "emptyTitle": "जेबो दिहुनथाय मोनेखै",
      "emptyDescription": "नायगिरनायखौ फेहेर एबा सायख'नायखौ बोखार।",
      "resetAllFilters": "गासै सायख'नाय फिन फज'", "autoSynced": "WebSocket जों थोंजों सिंक",
      "availableQuantity": "मोननो हागौ बिबां", "quality": "गुण", "availability": "मोननाय",
      "sourceOfficer": "बिबानगिरि आनजाद", "sourceFarmer": "आबादारी आनजाद",
      "verifiedBadge": "✓ आनजाद जाबाय", "qualityGrade": "गुण थाखो", "verificationSource": "आनजाद फुंखा",
      "fieldNotes": "बिबानगिरिनि नायबिजिरनाय नोट",
      "purchaseTitle": "बायनो सोंनाय / आर'ज थिनहर",
      "purchaseSubtitle": "थोंजों फोनांजाब खालामनो गावनि गोनांथिखौ गथाय।",
      "yourName": "नोंथांनि मुं / कंपानि", "contact": "फोन अनजिमा / ईमेल",
      "requestedQty": "नांगौ बिबां", "message": "रादाब / गोनांथि", "sendRequest": "बायनो आर'ज थिनहर",
      "notFound": "दिहुनथाय मोनेखै", "noLogin": "हाबसिंनाय नाङा", "unitLabel": "सानगुदि"
    },
    "officer": {
      "portal": "आबाद बिबानगिरि पर्टेल", "subtitle": "ओनसोलनि दिहुनथाय सामलाय, आबादारी आर'ज आनजाद खालाम",
      "profile": "महर सोलाय", "totalRecords": "गासै दिहुनथाय", "totalRecordsHint": "नोंथांनि ओनसोलाव",
      "availableQty": "मोननो हागौ बिबां", "availableQtyHint": "आनजाद खालामनाय फसल", "farmerRequests": "आबादारी आर'ज",
      "pending": "नायबिजिरनो नेनानै दं", "verifiedRecords": "आनजाद खालामनाय फसल", "verifiedRecordsHint": "बायग्रानि थाखाय",
      "queueTitle": "आबादारी आनजाद आर'ज", "queueSubtitle": "नायबिजिरनो नेना थानाय आबादारीफोर",
      "queueEmpty": "गासै हाबा जोबबाय! जेबो आर'ज गैया।",
      "localProduceTitle": "स्थानीय आबाद दिहुनथाय", "localProduceSubtitle": "फोसावनाय फसलफोर",
      "addProduce": "+ दिहुनथाय दाजाब", "editProduce": "दिहुनथाय सोलाय", "addProduceModalTitle": "+ स्थानीय दिहुनथाय दाजाब",
      "modalSubtitle": "बिबानगिरिजों थोंजों दाजाबनाय फसल आनजाद जाबाय होनना गनायगोन",
      "savePublish": "थिन आरो फोसाव", "verify": "आनजाद खालाम", "reject": "नेवसि",
      "pendingBadge": "🟡 नेनानै दं", "directOfficerEntry": "बिबानगिरिनि थोंजों दाजाबनाय",
      "markUnavailable": "मोननो हाया दिनथि", "markAvailable": "मोननो हागौ दिनथि",
      "editProduceAction": "दिहुनथाय सोलाय", "deleteProduce": "दानख'",
      "deleteConfirm": "नोंथाङा थारैबो दानख'नो सानदों नामा?", "rejectTitle": "आर'ज नेवसि",
      "rejectDescription": "नेवसिनायनि जाहोन लिर",
      "rejectionReason": "जाहोन / सुध्रायनाय नांगौ",
      "rejectionPlaceholder": "जेरै: फसलनि बिबाङा हा बिबांजों मोलायासै; फिन सुनाय जा।",
      "confirmRejection": "नेवसिनाय रोखा खालाम", "fieldInspected": "नायबिजिरना आनजाद खालामबाय",
      "verificationSuccess": "✓ आबादारी आर'ज आनजाद जाबाय आरो फोसावबाय!",
      "rejectionSuccess": "आर'जखौ नेवसिबाय आरो आबादारीनो खौरां हरबाय।",
      "provideReason": "नेवसिनायनि जाहोन लिर", "noProduceYet": "ओनसोलाव दासिमबो फसल दाजाबाखै।",
      "cropCol": "फसल", "qtyCol": "बिबां", "locationCol": "जायगा", "availDateCol": "मोननाय अखथ'",
      "qualityCol": "गुण", "sourceCol": "फुंखा", "statusCol": "थासारि", "actionsCol": "हाबा",
      "officerRecordedSuccess": "✓ बिबानगिरिजों थोंजों दाजाबबाय आरो आनजाद जाबाय!",
      "updateProduceSuccess": "दिहुनथाय गोदान खालामबाय"
    },
    "farmer": {
      "portal": "आबादारी पर्टेल", "myProfile": "आंनि आबाद महर",
      "assignedOfficer": "नोंथांनि आबाद बिबानगिरि", "assignedOfficerHint": "आर'जफोर बेयाव थाङो",
      "totalSubmissions": "गासै आर'ज", "pending": "नेनानै दं", "verified": "आनजाद जाबाय & चोलिगासिनो",
      "rejected": "नेवसिबाय", "requestsTitle": "आंनि फसल आनजाद आर'ज",
      "requestsSubtitle": "बिबानगिरिनिफ्राय थासारि मिथि",
      "addCrop": "+ फसल गुवारै दाजाब", "addCropButton": "+ फसल दाजाब", "myCropDetails": "+ आबाद फसल खौरां दाजाब",
      "submittedToOfficer": "आनजाद खालामनो आबाद बिबानगिरिनो थिनहरगोन",
      "submitToOfficer": "बिबानगिरिनो गथाय", "noCrops": "दासिमबो फसल गथायाखै",
      "noCropsDescription": "आनजाद खालामनो आबाद खौरां दाजाब।", "addFirstCrop": "गिबि फसल दाजाब",
      "pendingStatus": "🟡 नेनानै दं", "verifiedStatus": "🟢 ✓ आनजाद जाबाय", "rejectedStatus": "🔴 नेवसिबाय",
      "expectedHarvest": "खामानि जोबनाय अखथ'", "cultivatedArea": "आबाद हा", "expectedYield": "मोननो हागौ दिहुनथाय",
      "cropStage": "फसलनि थाखो", "officerFeedback": "बिबानगिरिनि फिननाय:", "submissionSuccess": "✓ फसल गथायबाय! बिबानगिरिनो थिनहरबाय।",
      "verificationStatus": "नेनानै दं → आनजाद जाबाय / नेवसिबाय", "locationRouting": "जायगा लामा (बिबानगिरिनो)",
      "additionalNotes": "हेर आबाद नोट", "farmingNotesPlaceholder": "आबाद खान्थि, दै होनाय, सार खौरां..."
    },
    "profile": {
      "title": "आंनि महर", "subtitle": "गावनि खाता आरो आबाद खौरां सामलाय",
      "saveChanges": "सोलायनायफोरखौ थिन", "fullName": "आबुं मुं", "village": "गामि",
      "area": "ओनसोल / ब्लक", "district": "जिल्ला", "state": "हादोरसा", "landArea": "हा बिबां",
      "landUnit": "हा सानगुदि", "farmingType": "आबाद रोखोम", "officialEmail": "सोरखारि ईमेल",
      "designation": "बिबानगिरि बिबान", "department": "बिफान", "contactNumber": "फोन अनजिमा",
      "assignedArea": "होनाय ओनसोल / ब्लक", "profileUpdated": "महर सोलायनाय जाबाय"
    },
    "crops": {
      "onion": "फियाज", "tomato": "बिलाथि", "potato": "आलु", "rice": "माइ / मइरा",
      "wheat": "गहु", "maize": "गमकै / मक्का", "carrot": "गाजर", "cabbage": "बन्दाकवि",
      "cauliflower": "फुलकवि", "garlic": "नहरू", "ginger": "हाजिं", "banana": "थालिर",
      "mango": "थाfeature / थाइजौ", "groundnut": "बादाम", "sugarcane": "खोसौ", "cotton": "खुन्थाय"
    },
    "produce_types": {
      "tubers": "थाव / रोद", "vegetable": "मेगं-थायगं", "vegetable_bulbs": "मेगं / रोद",
      "field_crop": "फोथारनि फसल", "cereals": "मायरोम", "fruits": "फिथाय-सामथाय",
      "cash_crops": "खाउरी फसल", "spices": "मसाला"
    },
    "units": { "tons": "टन", "quintals": "कुइन्टाल", "kg": "किग्रा", "acres": "एकर", "hectares": "हेक्टर" },
    "qualities": {
      "gradeA": "थाखो A", "gradeB": "थाखो B", "gradeC": "थाखो C",
      "gradeAPremium": "थाखो A (गाहामसिन)", "gradeBStandard": "थाखो B (गेजेर)", "gradeCFair": "थाखो C (सादारण)"
    },
    "crop_stages": {
      "bulbDevelopment": "रोद जौगानाय", "vegetative": "देरनाय थाखो",
      "flowering": "बारनाय थाखो", "readyForHarvest": "दाननो खाथियाव", "preHarvest": "दाननाय सिगां"
    },
    "statuses": {
      "verified": "आनजाद जाबाय", "pending": "नेनानै दं", "rejected": "नेवसिबाय",
      "available": "मोननो हागौ", "unavailable": "मोननो हाया"
    },
    "sources": {
      "officerVerified": "बिबानगिरि आनजाद", "farmerVerified": "आबादारी आनजाद",
      "directOfficerEntry": "बिबानगिरिनि थोंजों दाजाबनाय"
    },
    "notifications": {
      "newProduceAdded": "🌾 गोदान फसल दाजाबबाय: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 फसल गोदान खालामबाय: {{crop}}",
      "newFarmerSubmission": "📋 गोदान आबादारी आर'ज: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ फसल आनजाद जाबाय: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ आर'ज नेवसिबाय: {{crop}}",
      "purchaseInquiry": "💼 बायनो सोंनाय: बायग्राया {{qty}} {{unit}} {{crop}} नांगौ होनदों",
      "demoReset": "🔄 डेमो डेटा फिन फज'बाय",
      "inquirySent": "✓ बायनो सोंनायखौ आबादारी / बिबानगिरिनो थिनहरबाय!",
      "statusUpdated": "थासारि गोदान खालामबाय", "deleted": "फसल दानख'बाय"
    },
    "demo": {
      "controlsTitle": "SIH डेमो सामलायनाय:", "officerBtn": "बिबानगिरि (रवि कुमार)",
      "farmerBtn": "आबादारी (कुमार)", "buyerBtn": "बायग्रा नुथाय",
      "resetBtn": "डेमो फिन फज'", "resetConfirm": "डेटाबेसखौ गिबि डेमो थासारियाव फज'नो सानदों नामा?"
    }
  },
  "ks": {
    "lang": { "name": "Kashmiri", "nativeName": "کٲشُر", "code": "ks", "dir": "rtl" },
    "common": {
      "language": "زَبان", "login": "لاگ اِن", "register": "رَجِسٹَر", "logout": "لاگ آؤٹ",
      "dashboard": "ڈیش بورڈ", "profile": "پروفائل", "save": "محفوظ کٔرِو", "cancel": "مَنسوخ",
      "close": "بَنٛد کٔرِو", "submit": "دَرٕج کٔرِو", "refresh": "تازٕ کٔرِو", "search": "تلاش کٔرِو",
      "clearFilters": "فِلٹَر کٔڈِو", "loading": "لوڈ گژھان چھُ...", "viewDetails": "تفصیلات وُچھِو",
      "allStates": "سٲری ریاستہٕ", "allDistricts": "سٲری ضِلہٕ", "allAreas": "سٲری علاقہٕ",
      "verified": "تَصدیٖق شُدٕ", "pending": "زیرِ التوا", "rejected": "مسترد",
      "available": "دَستیاب", "unavailable": "ناقابلِ دَستیاب", "yes": "آ", "no": "نہٕ",
      "continue": "جاری تھٲوِو", "send": "سوزِو", "back": "واپَس", "next": "برونٛہہ",
      "previous": "پٔتِم", "edit": "بَدلاو کٔرِو", "delete": "مِٹٲوِو", "status": "حٲلَتھ",
      "role": "کِردار", "user": "صٲرِف", "liveSync": "لائیو سِنک", "reconnecting": "دوبارٕ جُڑان...",
      "reset": "ری سیٹ", "actions": "عَمَل", "crop": "فَصٕل", "quantity": "تعداد/مقدار",
      "location": "جایہِ", "date": "تٲریٖخ", "notes": "نوٹس"
    },
    "navigation": {
      "home": "ہوم", "viewProduce": "پیداوار وُچھِو", "officerPortal": "افسر پورٹل",
      "farmerPortal": "کٔمیٖن پورٹل", "dashboard": "ڈیش بورڈ", "profile": "پروفائل",
      "requests": "دَرخواست", "addProduce": "پیداوار جوڑِو", "addCrop": "فَصٕل جوڑِو",
      "myRequests": "میانی درخواستہٕ", "farmerRequests": "کٔمیٖن درخواستہٕ",
      "liveSync": "لائیو سِنک", "publicBuyerView": "عوامی خریدار منظر"
    },
    "auth": {
      "roleSelector": "پَنُن کِردار چُناو کٔرِو", "agricultureOfficer": "زراعت افسر", "farmer": "کٔمیٖن / زمیندار",
      "mobileOrEmail": "موبائل نَمبَر یا ای میل", "password": "پاس ورڈ", "signIn": "سائن اِن",
      "fullName": "پوٗرٕ ناڤ", "mobileNumber": "موبائل نَمبَر", "emailOptional": "ای میل (اختیاری)",
      "createAccount": "اکاؤنٹ بَناوِو", "designation": "عہدٕ", "department": "محکمہٕ",
      "assignedArea": "مُقرر علاقہٕ", "district": "ضِلہٕ", "state": "ریاست",
      "village": "گام", "landArea": "زمین رقَبہٕ (ایکڑ)", "farmingType": "کاشتکاری ہُنٛد قٕسٕم",
      "welcomeBack": "خوش آمدید، {{name}}!", "accountCreated": "اکاؤنٹ بنیو! خوش آمدید، {{name}}.",
      "invalidCredentials": "غلط لاگ ان تفصیلات", "requiredFields": "مہرَبٲنی کٔرِتھ پرِیٛو سٲری ضروری خانے۔",
      "demoLoginFailed": "ڈیمو لاگ اِن ناکام", "networkError": "نیٹ ورک خرابی",
      "logoutSuccess": "تۄہی کٔر کامیابی سان لاگ آؤٹ۔",
      "officerLoginRequired": "افسر پورٹل خٲطرٕ زراعت افسر طور لاگ اِن گژھِو۔",
      "farmerLoginRequired": "زمیندار پورٹل خٲطرٕ کٔمیٖن طور لاگ اِن گژھِو۔",
      "registrationFailed": "رَجسٹریشن گٔیہِ ناکام۔", "switchedRole": "{{role}} پؠٹھ بدلاو آو کرنہٕ"
    },
    "landing": {
      "verifiedPlatform": "تصدیق شدہ مَقامی زرعی پیداوار پلیٹ فارم", "title": "ڈھوٗنڈِو۔ تَصدیٖق کٔرِو۔ جُڑِو۔",
      "subtitle": "ایگری فلو چھُ کٔمیٖنن تہٕ زراعت افسرن مَقامی پیداوار ہٕنٛز تصدیق شدہ معلومات تھاونس مَنٛز مدد کران۔",
      "searchVerifiedProduce": "تصدیق شدہ پیداوار کٔرِو تلاش", "findVerifiedProduce": "پیداوار لبِو",
      "quickDiscovery": "علاقے مُطٲبِق ژٹپٹ پیداوار تلاش", "cropName": "فصلُک ناڤ",
      "cropPlaceholder": "مثال: گَنٛڈٕ، رُوٛانٛگَن...", "state": "ریاست", "district": "ضِلہٕ",
      "allStates": "سٲری ریاستہٕ", "allDistricts": "سٲری ضِلہٕ", "howItWorks": "ایگری فلو کِتھ پٲٹھۍ چھُ کٲم کران",
      "workflowIntro": "مَقامی زراعت کُھلی منڈی سۭتۍ جوڑَن وٲلۍ شفاف تَصدیٖقی عَمَل۔",
      "sihPlatform": "SIH پلیٹ فارم", "tagLine": "ڈھوٗنڈِو۔ تَصدیٖق کٔرِو۔ جُڑِو।"
    },
    "howItWorks": {
      "farmerSubmission": "زمیندارُک اِندراج",
      "farmerSubmissionDesc": "زمیندار چھِ پَننۍ کاشت، زمینُک رقبہٕ تہٕ متوقع پیداوار تصدیق خٲطرٕ درج کران۔",
      "officerVerification": "افسر سٕنٛز تصدیق",
      "officerVerificationDesc": "مَقامی زراعت افسر چھِ فیلڈ معائنہٕ کٔرِتھ پیداوار شایع کران۔",
      "publicDiscovery": "عوامی تلاش تہٕ رابطہٕ",
      "publicDiscoveryDesc": "خریدار ہیکَن بغیر لاگ اِن کٔرِتھ فصل تہٕ مقدار مُطٲبِق تصدیق شدہ پیداوار لٔبِتھ।"
    },
    "roles": {
      "farmers": "زمیندارَن خٲطرٕ", "officers": "زراعت افسرَن خٲطرٕ", "buyers": "خریدارَن تہٕ تاجرَن خٲطرٕ",
      "farmerTitle": "فصلَن ہٕنٛز براہِ راست رسائی", "officerTitle": "اختیار تہٕ اعتماد",
      "buyerTitle": "تصدیق شدہ رسد ہٕنٛز تلاش",
      "farmerItem1": "کاشتکاری پروفائل تہٕ زمین کٔرِو درج",
      "farmerItem2": "تَصدیٖق خٲطرٕ پَنُن فصل کٔرِو پیش",
      "farmerItem3": "اصلی حٲلَتھ زٲنِو: زیر التوا → تصدیق شدہ / مسترد",
      "officerItem1": "مَقامی تصدیق شدہ پیداوار کٔرِو سیدھے جوڑِو",
      "officerItem2": "پَننہِ علاقٕکۍ کٔمیٖنن ہٕنٛز درخواستہٕ کٔرِو تصدیق",
      "officerItem3": "مقدار تہٕ دَستیابی کٔرِو اپ ڈیٹ",
      "buyerItem1": "بغیر لاگ اِن کٔرِو جلدی پیداوار تلاش",
      "buyerItem2": "ریاست، ضِلہٕ تہٕ مقدار مُطٲبِق کٔرِو فلٹر",
      "buyerItem3": "تصدیق شدہ زمیندارن سوزِو براہِ راست خریدی ہُنٛد پیغام"
    },
    "produce": {
      "title": "تصدیق شدہ پیداوار تلاش",
      "subtitle": "زراعت افسرن ہٕنٛز تصدیق شدہ دَستیاب تہٕ یِنہٕ وٲلۍ زرعی پیداوار کٔرِو تلاش۔",
      "searchCropName": "فصلُک ناڤ کٔرِو تلاش", "state": "ریاست", "district": "ضِلہٕ", "areaBlock": "علاقہٕ / بلاک",
      "minQty": "کم از کم مقدار (ٹن)", "maxQty": "زیٛادٕ کھۄتہٕ زیٛادٕ مقدار (ٹن)", "availBefore": "دَستیابی تٲریٖخ تام",
      "verifiedOnly": "صرف تصدیق شدہ (تجویز کٔرمٕژ)", "clearFilters": "فلٹر کٔڈِو",
      "count": "{{count}} تصدیق شدہ پیداوار ریکارڈ چھُ ہاونہٕ یِوان",
      "countPlural": "{{count}} تصدیق شدہ پیداوار ریکارڈ چھِ ہاونہٕ یِوان",
      "emptyTitle": "کانٛہہ پیداوار ریکارڈ میلِیو نہٕ",
      "emptyDescription": "پَنُن تلاش کٔرِو وسیع یا فلٹر کٔڈِو۔",
      "resetAllFilters": "سٲری فلٹر کٔرِو ری سیٹ", "autoSynced": "WebSocket ذٔریعہٕ لائیو سِنک",
      "availableQuantity": "دَستیاب مقدار", "quality": "معیار", "availability": "دَستیابی",
      "sourceOfficer": "افسر تصدیق شدہ", "sourceFarmer": "زمیندار تصدیق شدہ",
      "verifiedBadge": "✓ تصدیق شدہ", "qualityGrade": "معیار گریڈ", "verificationSource": "تصدیق ذٔریعہٕ",
      "fieldNotes": "افسر سٕنٛد فیلڈ نوٹس",
      "purchaseTitle": "خریدی پُچھ گَچھ / طلب سوزِو",
      "purchaseSubtitle": "تصدیق شدہ زمیندار یا افسر سۭتۍ جُڑنہٕ خٲطرٕ پَنٕنۍ ضرورت کٔرِو درج۔",
      "yourName": "تُہُند ناڤ / کَمپَنی", "contact": "رابطہٕ نَمبَر / ای میل",
      "requestedQty": "مطلوبہٕ مقدار", "message": "پیغام / ضَروریات", "sendRequest": "خریدی ہٕنٛز درخواست سوزِو",
      "notFound": "پیداوار ریکارڈ میلِیو نہٕ", "noLogin": "لاگ اِن ضۆروٗری نَہ", "unitLabel": "اکائی"
    },
    "officer": {
      "portal": "زراعت افسر پورٹل", "subtitle": "مَقامی پیداوار سَمبھالِو تہٕ کٔمیٖنن ہٕنٛز درخواستہٕ کٔرِو تصدیق",
      "profile": "پروفائل بدلاوِو", "totalRecords": "کُل ریکارڈ", "totalRecordsHint": "تُہندِس علاقَس مَنٛز",
      "availableQty": "دَستیاب مقدار", "availableQtyHint": "تصدیق شدہ پیداوار", "farmerRequests": "زمیندارن ہٕنٛز درخواستہٕ",
      "pending": "فیلڈ تصدیق باقی", "verifiedRecords": "تصدیق شدہ ریکارڈ", "verifiedRecordsHint": "خریدارن خٲطرٕ دَستیاب",
      "queueTitle": "زمیندار تصدیق درخواستہٕ", "queueSubtitle": "تُہندِس علاقَس مَنٛز معائنہٕ خٲطرٕ انتظار کرَن وٲلۍ زمیندار",
      "queueEmpty": "سۄروے کٲم مُکَمل! کانٛہہ درخواست باقی نہٕ۔",
      "localProduceTitle": "مَقامی علاقٕچ زرعی پیداوار", "localProduceSubtitle": "تُہندِس علاقَس مَنٛز شایع کٔرمٕژ پیداوار",
      "addProduce": "+ پیداوار جوڑِو", "editProduce": "پیداوار بدلاوِو", "addProduceModalTitle": "+ مَقامی پیداوار جوڑِو",
      "modalSubtitle": "افسر سٕنٛد دٔسۍ براہِ راست درج کٔرمٕژ پیداوار گژھِ تصدیق شدہ مَنٛنہٕ",
      "savePublish": "محفوظ کٔرِو تہٕ شایع کٔرِو", "verify": "تَصدیٖق کٔرِو", "reject": "مُستَرَد کٔرِو",
      "pendingBadge": "🟡 تصدیق باقی", "directOfficerEntry": "افسرُک براہِ راست اِندراج",
      "markUnavailable": "ناقابلِ دستياب نشان لگاوِو", "markAvailable": "دَستیاب نشان لگاوِو",
      "editProduceAction": "پیداوار بدلاوِو", "deleteProduce": "ریکارڈ مِٹٲوِو",
      "deleteConfirm": "کیا تۄہی چھِوا پۆز پٲٹھۍ یَتھ ریکارڈَس مِٹاوُن یژھان؟", "rejectTitle": "زمیندار درخواست مُستَرَد کٔرِو",
      "rejectDescription": "مہرَبٲنی کٔرِتھ لِکھِو مُستَرَد کرنُک واضح وجہ",
      "rejectionReason": "وجہ / درستی ہٕنٛز ضرورت",
      "rejectionPlaceholder": "مثال: متوقع پیداوار زمین کِس رقبَس سۭتۍ مِلان نہٕ؛ دوبارہ ناپِو।",
      "confirmRejection": "مُستَرَد پۆز کٔرِو", "fieldInspected": "افسر سٕنٛد دٔسۍ فیلڈ معائنہٕ کٔرِتھ تَصدیٖق",
      "verificationSuccess": "✓ درخواست گٔیہِ تَصدیٖق تہٕ شایع گٔیہِ!",
      "rejectionSuccess": "درخواست گٔیہِ مُستَرَد تہٕ زمیندارَس آو سُوٗزنہٕ।",
      "provideReason": "مہرَبٲنی کٔرِتھ دِیِو مُستَرَد کرنُک وجہ", "noProduceYet": "تُہندِس علاقَس مَنٛز چھُ نہٕ کانہہ ریکارڈ درج।",
      "cropCol": "فَصٕل", "qtyCol": "مقدار", "locationCol": "جایہِ", "availDateCol": "دَستیابی تٲریٖخ",
      "qualityCol": "معیار", "sourceCol": "ذٔریعہٕ", "statusCol": "حٲلَتھ", "actionsCol": "عَمَل",
      "officerRecordedSuccess": "✓ افسر سٕنٛد دٔسۍ براہِ راست درج تہٕ تصدیق!",
      "updateProduceSuccess": "پیداوار گٔیہِ اپ ڈیٹ"
    },
    "farmer": {
      "portal": "زمیندار پورٹل", "myProfile": "میٲنۍ زراعتی پروفائل",
      "assignedOfficer": "تُہنٛد مَقامی زراعت افسر", "assignedOfficerHint": "درخواستہٕ چھِ ییٚتین سوزنہٕ یِوان",
      "totalSubmissions": "کُل درخواستہٕ", "pending": "زیر التوا", "verified": "تصدیق شدہ تہٕ چالو",
      "rejected": "مُستَرَد", "requestsTitle": "میانی فصل تصدیق درخواستہٕ",
      "requestsSubtitle": "مَقامی زراعت افسر نِش پَنٕنۍ حٲلَتھ زٲنِو",
      "addCrop": "+ فصل ہٕنٛز تفصیل جوڑِو", "addCropButton": "+ فصل جوڑِو", "myCropDetails": "+ کاشتکاری فصل تفصیل جوڑِو",
      "submittedToOfficer": "درج کٔرمٕژ تفصیلات گژھِ تصدیق خٲطرٕ مَقامی افسرَس سوزنہٕ",
      "submitToOfficer": "مَقامی افسرَس کٔرِو پیش", "noCrops": "وُنہِ تام چھُ نہٕ کانٛہہ فصل درج کۄرمُت",
      "noCropsDescription": "تصدیق خٲطرٕ پَننۍ کاشت کٔرِو درج।", "addFirstCrop": "گۄڈنیُک فصل جوڑِو",
      "pendingStatus": "🟡 تصدیق باقی", "verifiedStatus": "🟢 ✓ تصدیق شدہ", "rejectedStatus": "🔴 مُستَرَد",
      "expectedHarvest": "متوقع کٹائی تٲریٖخ", "cultivatedArea": "کاشت کۄرمُت رقبہٕ", "expectedYield": "متوقع پیداوار",
      "cropStage": "فصلُک مرحلہٕ", "officerFeedback": "افسر سٕنٛز رائے:", "submissionSuccess": "✓ فصل آو جمع کرنہٕ! تصدیق خٲطرٕ سوزنہٕ آو।",
      "verificationStatus": "زیر التوا → تصدیق شدہ / مسترد", "locationRouting": "مقام رستہٕ (مَقامی افسر خٲطرٕ)",
      "additionalNotes": "اضافی نوٹس", "farmingNotesPlaceholder": "کاشتکاری طریقہٕ، آبپاشی، کھاد تفصیل..."
    },
    "profile": {
      "title": "میٲنۍ پروفائل", "subtitle": "پَننہِ اکاؤنٹ تہٕ زراعت ہٕنٛز تفصیلات سَمبھالِو",
      "saveChanges": "تبدیلیاں کٔرِو محفوظ", "fullName": "پوٗرٕ ناڤ", "village": "گام",
      "area": "علاقہٕ / بلاک", "district": "ضِلہٕ", "state": "ریاست", "landArea": "زمین رقَبہٕ",
      "landUnit": "زمین ہٕنٛز اکائی", "farmingType": "کاشتکاری ہُنٛد قٕسٕم", "officialEmail": "سرکاری ای میل",
      "designation": "افسر عہدٕ", "department": "محکمہٕ", "contactNumber": "رابطہٕ نَمبَر",
      "assignedArea": "مُقرر علاقہٕ / بلاک", "profileUpdated": "پروفائل گٔیہِ اپ ڈیٹ"
    },
    "crops": {
      "onion": "گَنٛڈٕ", "tomato": "رُوٛانٛگَن", "potato": "آلو", "rice": "دھان / تومُل",
      "wheat": "کَنٛکھ", "maize": "مکٲئی", "carrot": "گازٕر", "cabbage": "بَنٛد گۆبِی",
      "cauliflower": "پھوٗل گۆبِی", "garlic": "رۆہُن", "ginger": "ادرک", "banana": "کیلا",
      "mango": "آم", "groundnut": "مُوٛنٛگ پھلی", "sugarcane": "گنا", "cotton": "کپاس"
    },
    "produce_types": {
      "tubers": "مُولۍ والۍ فصل", "vegetable": "سَبزی", "vegetable_bulbs": "سَبزی / گانٛٹھۍ",
      "field_crop": "کھیتُک فصل", "cereals": "اناج", "fruits": "میوٕ",
      "cash_crops": "نقد فصل", "spices": "مَصالحہٕ"
    },
    "units": { "tons": "ٹن", "quintals": "کوئنٹل", "kg": "کلو", "acres": "ایکڑ", "hectares": "ہیکٹر" },
    "qualities": {
      "gradeA": "گریڈ A", "gradeB": "گریڈ B", "gradeC": "گریڈ C",
      "gradeAPremium": "گریڈ A (اعلیٰ)", "gradeBStandard": "گریڈ B (معیاری)", "gradeCFair": "گریڈ C (عام)"
    },
    "crop_stages": {
      "bulbDevelopment": "گانٛٹھ بَنُن", "vegetative": "بَڈھنُک دور",
      "flowering": "پوش یِنُک دور", "readyForHarvest": "کٹائی خٲطرٕ تیار", "preHarvest": "کٹائی برونٛہہ"
    },
    "statuses": {
      "verified": "تصدیق شدہ", "pending": "زیر التوا", "rejected": "مسترد",
      "available": "دَستیاب", "unavailable": "ناقابلِ دَستیاب"
    },
    "sources": {
      "officerVerified": "افسر تصدیق شدہ", "farmerVerified": "زمیندار تصدیق شدہ",
      "directOfficerEntry": "افسرُک براہِ راست اِندراج"
    },
    "notifications": {
      "newProduceAdded": "🌾 نٔو پیداوار جوڑنہٕ آمٕژ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 پیداوار گٔیہِ اپ ڈیٹ: {{crop}}",
      "newFarmerSubmission": "📋 کٔمیٖن سٕنٛز نٔو درخواست: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ فصل گۆو تصدیق: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ درخواست گٔیہِ مسترد: {{crop}}",
      "purchaseInquiry": "💼 خریدی پُچھ گَچھ: خریدارَن مَنٛگی {{qty}} {{unit}} {{crop}}",
      "demoReset": "🔄 ڈیمو ڈیٹا آو دوبارہ ری سیٹ کرنہٕ",
      "inquirySent": "✓ خریدی پُچھ گَچھ آو سوزنہٕ!",
      "statusUpdated": "حٲلَتھ گٔیہِ اپ ڈیٹ", "deleted": "ریکارڈ آو مِٹاونہٕ"
    },
    "demo": {
      "controlsTitle": "SIH ڈیمو کنٹرول:", "officerBtn": "افسر (روی کمار)",
      "farmerBtn": "زمیندار (کمار)", "buyerBtn": "عوامی خریدار منظر",
      "resetBtn": "ڈیمو ری سیٹ", "resetConfirm": "کیا تۄہی چِھوا اصل ڈیمو حالتَس مَنٛز لاگُن یژھان؟"
    }
  },
  "mni": {
    "lang": { "name": "Manipuri", "nativeName": "মণিপুরী", "code": "mni", "dir": "ltr" },
    "common": {
      "language": "ললোন্", "login": "লগইন", "register": "রেজিষ্টর", "logout": "লগআউট",
      "dashboard": "ডেশবোর্ড", "profile": "প্রোফাইল", "save": "সেভ তৌরো", "cancel": "কেন্সেল",
      "close": "থিংজিনলো", "submit": "সবমিট তৌরো", "refresh": "অনৌবা শেম্মু", "search": "থীবীযু",
      "clearFilters": "ফিল্টার মুত্থত্থু", "loading": "লোড তৌরি...", "viewDetails": "মকুপ শেন্না য়েংবীয়ু",
      "allStates": "ষ্টেট পুম্নমক", "allDistricts": "জিলা পুম্নমক", "allAreas": "মফম পুম্নমক",
      "verified": "চেক তৌরবা", "pending": "পেন্ডিং লৈরি", "rejected": "য়াদ্রে",
      "available": "ফংই", "unavailable": "ফংদে", "yes": "হয়ে", "no": "নত্তে",
      "continue": "চত্থবীয়ু", "send": "থাগৎলু", "back": "হন্নবা", "next": "মথংগী",
      "previous": "মমাংগী", "edit": "শেমদোকউ", "delete": "মুত্থত্থু", "status": "ফিভম",
      "role": "থৌদাং", "user": "শীজিন্নরিবা", "liveSync": "লাইভ সিঙ্ক", "reconnecting": "অমুক হন্না শম্নরি...",
      "reset": "রিসেট", "actions": "থবক", "crop": "মহৈ-মরোং", "quantity": "চাং/মশীং",
      "location": "মফম", "date": "তারিখ", "notes": "নোট"
    },
    "navigation": {
      "home": "য়ুম", "viewProduce": "পোত্থোক য়েংবীয়ু", "officerPortal": "অফিসার পোর্টাল",
      "farmerPortal": "লৌউমী পোর্টাল", "dashboard": "ডেশবোর্ড", "profile": "প্রোফাইল",
      "requests": "দরখস্ত", "addProduce": "পোত্থোক হাপচিনলু", "addCrop": "মহৈ-মরোং হাপচিনলু",
      "myRequests": "ঐগী দরখস্ত", "farmerRequests": "লৌউমীগী দরখস্ত",
      "liveSync": "লাইভ সিঙ্ক", "publicBuyerView": "লৈরিবশিংগী মিৎয়েং"
    },
    "auth": {
      "roleSelector": "নহাক্কী থৌদাং খল্লু", "agricultureOfficer": "লৌউ-শিংউ অফিসার", "farmer": "লৌউমী",
      "mobileOrEmail": "মোবাইল নম্বর নত্রগা ইমেইল", "password": "পাসওয়ার্ড", "signIn": "সাইন ইন",
      "fullName": "অপুম্বা মিং", "mobileNumber": "মোবাইল নম্বর", "emailOptional": "ইমেইল (অপশনেল)",
      "createAccount": "একাউণ্ট শেম্মু", "designation": "ফম", "department": "বিভাগ",
      "assignedArea": "পীজরবা মফম", "district": "জিলা", "state": "ষ্টেট",
      "village": "খুঙ্গং", "landArea": "লমগী পাক-চাউবা (একর)", "farmingType": "লৌউ-শিংউগী মখল",
      "welcomeBack": "তরাম্না ওকচরি, {{name}}!", "accountCreated": "একাউণ্ট শেম্লে! তরাম্না ওকচরি, {{name}}.",
      "invalidCredentials": "লানবা লগইন ইনফোর্মেসন", "requiredFields": "মথৌ তাবা পুম্নমক মেন্দুনো।",
      "demoLoginFailed": "ডেমো লগইন মাইপাকখিদ্রে", "networkError": "নেটৱার্ক অশোয়বা",
      "logoutSuccess": "লগআউট তৌখ্রে।",
      "officerLoginRequired": "অফিসার পোর্টালগীদমক লৌউ-শিংউ অফিসার ওইনা লগইন তৌবীয়ু।",
      "farmerLoginRequired": "লৌউমী পোর্টালগীদমক লৌউমী ওইনা লগইন তৌবীয়ু।",
      "registrationFailed": "রেজিষ্ট্রেসন মাইপাকখিদ্রে।", "switchedRole": "{{role}} দা হোংদোক্লে"
    },
    "landing": {
      "verifiedPlatform": "চেক তৌরবা লোকেল পোত্থোক প্লেটফর্ম", "title": "থীবীয়ু। চেক তৌবীয়ু। শম্নবীয়ু।",
      "subtitle": "এগ্রিফ্লোনা লৌউমী অমসুং লৌউ-শিংউ অফিসারশিংদা লোকেল পোত্থোকশিং চেক তৌবা পাউ থম্বদা মতেং পাংই।",
      "searchVerifiedProduce": "চেক তৌরবা পোত্থোক থীবীয়ু", "findVerifiedProduce": "পোত্থোক থীবীয়ু",
      "quickDiscovery": "মফম মতুং ইন্না থুনা থীবীয়ু", "cropName": "মহৈ-মরোংগী মিং",
      "cropPlaceholder": "উদাহরন: তিলহৌ, খামেন...", "state": "ষ্টেট", "district": "জিলা",
      "allStates": "ষ্টেট পুম্নমক", "allDistricts": "জিলা পুম্নমক", "howItWorks": "এগ্রিফ্লোনা করম্না থবক তৌবগে",
      "workflowIntro": "লোকেল লৌমীশিংবু হাংবা কৈথেলগা শম্নহনবা চেকিং প্রোসেস।",
      "sihPlatform": "SIH প্লেটফর্ম", "tagLine": "থীবীয়ু। চেক তৌবীয়ু। শম্নবীয়ু।"
    },
    "howItWorks": {
      "farmerSubmission": "লৌউমীগী দরখস্ত",
      "farmerSubmissionDesc": "লৌউমীশিংনা মখোয়গী লৌবু, মহৈ-মরোং অমসুং ফংগদবা চাং লোকেল চেকিংগীদমক থাগৎই।",
      "officerVerification": "অফিসারগী চেকিং",
      "officerVerificationDesc": "লোকেল লৌউ-শিংউ অফিসারশিংনা লমদা চত্তুনা য়েংশিন্দুনা পোত্থোকশিং ফোঙই।",
      "publicDiscovery": "মীয়াম্না থীবা অমসুং পাউ ফাওনবা",
      "publicDiscoveryDesc": "লৈরিবশিংনা লগইন তৌদনা মহৈ-মরোং, জিলা মতুং ইন্না চেক তৌরবা পোত্থোকশিং ফংই।"
    },
    "roles": {
      "farmers": "লৌউমীশিংগীদমক", "officers": "লৌউ-শিংউ অফিসারশিংগীদমক", "buyers": "লৈরিবশিং অমসুং ললোনবশিংগীদমক",
      "farmerTitle": "মহৈ-মরোংগী হকথেংনবা শক্তম", "officerTitle": "থৌদাং মফম অমসুং থাজবা",
      "buyerTitle": "চেক তৌরবা পোত্থোক থীবা",
      "farmerItem1": "লৌউ-শিংউগী প্রোফাইল অমসুং লম রেজিষ্টার তৌরো",
      "farmerItem2": "লোকেল চেকিংগীদমক ফংগদবা পোত্থোক থাগৎলু",
      "farmerItem3": "লাইভ ফিভম খঙবীয়ু: পেন্ডিং → চেক তৌরবা / য়াদ্রবা",
      "officerItem1": "লোকেল চেক তৌরবা পোত্থোকশিং হকথেংননা হাপচিল্লু",
      "officerItem2": "নহাক্কী ব্লোককী লৌউমীশিংগী আবেদন ফিল্ড ইনস্পেক্সন তৌরো",
      "officerItem3": "মশীং অমসুং ফংবগী ফিভম অপডেট তৌরো",
      "buyerItem1": "লগইন তৌদনা থুনা পোত্থোক থীবীয়ু",
      "buyerItem2": "ষ্টেট, জিলা, মফম অমসুং চাং মতুং ইন্না ফিল্টার তৌরো",
      "buyerItem3": "চেক তৌরবা লৌউমীশিংদা হকথেংননা পোত লৈবগী রিকুয়েষ্ট থাগৎলু"
    },
    "produce": {
      "title": "চেক তৌরবা পোত্থোক থীবা",
      "subtitle": "লোকেল লৌউ-শিংউ অফিসারশিংনা চেক তৌরবা ফংবা অমসুং ফংগদবা পোত্থোকশিং থীবীয়ু।",
      "searchCropName": "মহৈ-মরোংগী মিং থীবীয়ু", "state": "ষ্টেট", "district": "জিলা", "areaBlock": "মফম / ব্লোক",
      "minQty": "খ্বাইদগী নেম্বা চাং (টন)", "maxQty": "খ্বাইদগী য়াম্বা চাং (টন)", "availBefore": "ফংগদবা তারিখ ফাওবদা",
      "verifiedOnly": "চেক তৌরবশিংখক (রিকোমেন্ড তৌবা)", "clearFilters": "ফিল্টার মুত্থত্থু",
      "count": "{{count}} চেক তৌরবা পোত্থোক রেকর্ড উরে",
      "countPlural": "{{count}} চেক তৌরবা পোত্থোক রেকর্ডশিং উরে",
      "emptyTitle": "পোত্থোক রেকর্ড অমত্তা ফংদে",
      "emptyDescription": "থীবা পাকথোকহনবীয়ু নত্রগা ফিল্টার মুত্থত্থু।",
      "resetAllFilters": "ফিল্টার পুম্নমক রিসেট তৌরো", "autoSynced": "WebSocket কী লাইভ সিঙ্ক",
      "availableQuantity": "ফংলিবা চাং", "quality": "গুণ", "availability": "ফংবা",
      "sourceOfficer": "অফিসারনা চেক তৌবা", "sourceFarmer": "লৌউমীনা চেক তৌবা",
      "verifiedBadge": "✓ চেক তৌরবা", "qualityGrade": "গুণগী গ্রেড", "verificationSource": "চেক তৌবগী হৌরকফম",
      "fieldNotes": "অফিসারগী ফিল্ড ইন্সপেক্সন নোট",
      "purchaseTitle": "লৈনবা হংবা / রিকুয়েষ্ট থাগৎলু",
      "purchaseSubtitle": "চেক তৌরবা পুথোকপা মীগা হকথেংননা শম্ননবগীদমক নহাক্কী মথৌ তাবা থাগৎলু।",
      "yourName": "নহাক্কী মিং / কোম্পানী", "contact": "কন্টাক্ট নম্বর / ইমেইল",
      "requestedQty": "মথৌ তাবা চাং", "message": "পাউজেল / মথৌ তাবশিং", "sendRequest": "লৈনবা রিকুয়েষ্ট থাগৎলু",
      "notFound": "পোত্থোক রেকর্ড ফংদে", "noLogin": "লগইন তৌবা মথৌ তাদে", "unitLabel": "য়ুনিট"
    },
    "officer": {
      "portal": "লৌউ-শিংউ অফিসার পোর্টাল", "subtitle": "লোকেল পোত্থোক য়েংশিনবীয়ু, লৌউমীশিংগী আবেদন চেক তৌবীয়ু",
      "profile": "প্রোফাইল শেমদোকউ", "totalRecords": "অপুনবা রেকর্ড", "totalRecordsHint": "নহাক্কী মফমদা",
      "availableQty": "ফংলিবা চাং", "availableQtyHint": "চেক তৌরবা পোত্থোক", "farmerRequests": "লৌউমীগী দরখস্ত",
      "pending": "ফিল্ড ইন্সপেক্সন তৌদ্রি", "verifiedRecords": "চেক তৌরবা রেকর্ড", "verifiedRecordsHint": "লৈরিবশিংনা উবা ফংই",
      "queueTitle": "লৌউমীগী চেক তৌনবগী দরখস্ত", "queueSubtitle": "ফিল্ড ইন্সপেক্সন তৌনবগীদমক ঙাইরিবা লৌউমীশিং",
      "queueEmpty": "থবক পুম্নমক লোইরে! দরখস্ত লৈতে।",
      "localProduceTitle": "লোকেল লৌউ-শিংউ পোত্থোক", "localProduceSubtitle": "নহাক্কী মফমগী ফোঙলবা পোত্থোকশিং",
      "addProduce": "+ পোত্থোক হাপচিল্লু", "editProduce": "পোত্থোক শেমদোকউ", "addProduceModalTitle": "+ লোকেল পোত্থোক হাপচিল্লু",
      "modalSubtitle": "অফিসারনা হকথেংননা হাপচিনবা পোত্থোক চেক তৌরে হায়না লৌগনি",
      "savePublish": "সেভ তৌদুনা ফোঙউ", "verify": "চেক তৌরো", "reject": "য়াদ্রে",
      "pendingBadge": "🟡 চেক তৌদ্রি", "directOfficerEntry": "অফিসারনা হকথেংননা হাপচিনবা",
      "markUnavailable": "ফংদে হায়না তাকউ", "markAvailable": "ফংই হায়না তাকউ",
      "editProduceAction": "পোত্থোক শেমদোকউ", "deleteProduce": "রেকর্ড মুত্থত্থু",
      "deleteConfirm": "নহাক্না পোত্থোক রেকর্ড অসি মুত্থৎপা পাম্ব্রা?", "rejectTitle": "লৌউমীগী দরখস্ত য়াদ্রে",
      "rejectDescription": "য়াদবগী মরম ইবীয়ু",
      "rejectionReason": "মরম / শেমদোকপা মথৌ তাই",
      "rejectionPlaceholder": "উদাহরন: পুথোকপা য়াবা চাং অদু লমগী চাংগা চুনদে; অমুক হন্না ওনবীয়ু।",
      "confirmRejection": "য়াদবা চেৎশিলহল্লু", "fieldInspected": "লমদা য়েংশিন্দুনা চেক তৌখ্রে",
      "verificationSuccess": "✓ আবেদন চেক তৌরে অমসুং ফোঙলে!",
      "rejectionSuccess": "দরখস্ত য়াদ্রে অমসুং লৌউমীদসু পাউ পীখ্রে।",
      "provideReason": "য়াদবগী মরম তাকপীয়ু", "noProduceYet": "মফমসিদা পোত্থোক রেকর্ড তৌদ্রি।",
      "cropCol": "মহৈ-মরোং", "qtyCol": "চাং", "locationCol": "মফম", "availDateCol": "ফংগদবা তারিখ",
      "qualityCol": "গুণ", "sourceCol": "হৌরকফম", "statusCol": "ফিভম", "actionsCol": "থবক",
      "officerRecordedSuccess": "✓ অফিসারনা হকথেংননা হাপচিন্লে অমসুং চেক তৌরে!",
      "updateProduceSuccess": "পোত্থোক অপডেট তৌরে"
    },
    "farmer": {
      "portal": "লৌউমী পোর্টাল", "myProfile": "ঐগী লৌউ-শিংউ প্রোফাইল",
      "assignedOfficer": "নহাক্কী লোকেল লৌউ-শিংউ অফিসার", "assignedOfficerHint": "দরখস্তশিং মসিদা থাগৎকদবনি",
      "totalSubmissions": "অপুনবা দরখস্ত", "pending": "পেন্ডিং", "verified": "চেক তৌরবা & এক্টিভ",
      "rejected": "য়াদ্রে", "requestsTitle": "ঐগী মহৈ-মরোং চেক তৌনবগী দরখস্ত",
      "requestsSubtitle": "অফিসারদগী ফিভম খঙবীয়ু",
      "addCrop": "+ মহৈ-মরোংগী অকুপ্পা হাপচিল্লু", "addCropButton": "+ মহৈ-মরোং হাপচিল্লু", "myCropDetails": "+ লৌউ-শিংউগী অকুপ্পা মরম হাপচিল্লু",
      "submittedToOfficer": "চেক তৌনবগীদমক অফিসারদা থাগৎকনি",
      "submitToOfficer": "অফিসারদা থাগৎলু", "noCrops": "মহৈ-মরোং থাগৎত্রি",
      "noCropsDescription": "চেক তৌনবগীদমক হৌজিক লৌউরিবা মহৈ-মরোং হাপচিল্লু।", "addFirstCrop": "অহানবা মহৈ-মরোং হাপচিল্লু",
      "pendingStatus": "🟡 চেক তৌদ্রি", "verifiedStatus": "🟢 ✓ চেক তৌরবা", "rejectedStatus": "🔴 য়াদ্রে",
      "expectedHarvest": "ফংগদবা তারিখ", "cultivatedArea": "লৌউরিবা লম", "expectedYield": "ফংগদবা চাং",
      "cropStage": "মহৈ-মরোংগী থাক", "officerFeedback": "অফিসারগী পাউতাক:", "submissionSuccess": "✓ মহৈ-মরোং থাগৎলে! চেক তৌনবা থাখ্রে।",
      "verificationStatus": "পেন্ডিং → চেক তৌরবা / য়াদ্রবা", "locationRouting": "মফম লম্বী (লোকেল অফিসারগীদমক)",
      "additionalNotes": "অতোপ্পা নোটশিং", "farmingNotesPlaceholder": "লৌউবগী মওং, ঈথৈ-লৌথৈ, হারগী মরম..."
    },
    "profile": {
      "title": "ঐগী প্রোফাইল", "subtitle": "একাউণ্ট অমসুং লৌউ-শিংউগী মরমশিং য়েংশিনবীয়ু",
      "saveChanges": "অহোংবশিং সেভ তৌরো", "fullName": "অপুম্বা মিং", "village": "খুঙ্গং",
      "area": "মফম / ব্লোক", "district": "জিলা", "state": "ষ্টেট", "landArea": "লমগী পাক-চাউবা",
      "landUnit": "লমগী য়ুনিট", "farmingType": "লৌউবগী মখল", "officialEmail": "অফিসিয়েল ইমেইল",
      "designation": "অফিসারগী ফম", "department": "বিভাগ", "contactNumber": "কন্টাক্ট নম্বর",
      "assignedArea": "পীজরবা মফম / ব্লোক", "profileUpdated": "প্রোফাইল অপডেট তৌরে"
    },
    "crops": {
      "onion": "তিলহৌ", "tomato": "খামেন", "potato": "আলু", "rice": "ফৌ / চেং",
      "wheat": "গেহু", "maize": "চুজাক", "carrot": "গাজর", "cabbage": "কোবি",
      "cauliflower": "কোবিলেই", "garlic": "চনম", "ginger": "শিং", "banana": "লাফোই",
      "mango": "হাইনৌ", "groundnut": "চীনাবাদাম", "sugarcane": "চু", "cotton": "লশিং"
    },
    "produce_types": {
      "tubers": "হৌদোং / থুম্বাল", "vegetable": "হৱাই-চেংৱাই / মনা-মশিং", "vegetable_bulbs": "মনা-মশিং / কন্দ",
      "field_crop": "লমগী মহৈ-মরোং", "cereals": "ধান্য", "fruits": "উহৈ-ৱাহৈ",
      "cash_crops": "শেন পুথোকপা ফসল", "spices": "মসলা"
    },
    "units": { "tons": "টন", "quintals": "কুইন্টাল", "kg": "কেজি", "acres": "একর", "hectares": "হেক্টর" },
    "qualities": {
      "gradeA": "গ্রেড A", "gradeB": "গ্রেড B", "gradeC": "গ্রেড C",
      "gradeAPremium": "গ্রেড A (খ্বাইদগী ফবা)", "gradeBStandard": "গ্রেড B (ময়াম চুনবা)", "gradeCFair": "গ্রেড C (চাপ চাবা)"
    },
    "crop_stages": {
      "bulbDevelopment": "হৌদোং চাউখৎপা", "vegetative": "উম্লবা থাক",
      "flowering": "লৈ সাতপা থাক", "readyForHarvest": "য়োক্নবা শেম-শারে", "preHarvest": "য়োকপগী মমাং"
    },
    "statuses": {
      "verified": "চেক তৌরবা", "pending": "পেন্ডিং", "rejected": "য়াদ্রে",
      "available": "ফংই", "unavailable": "ফংদে"
    },
    "sources": {
      "officerVerified": "অফিসারনা চেক তৌবা", "farmerVerified": "লৌউমীনা চেক তৌবা",
      "directOfficerEntry": "অফিসারনা হকথেংননা হাপচিনবা"
    },
    "notifications": {
      "newProduceAdded": "🌾 অনৌবা পোত্থোক হাপচিন্লে: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 পোত্থোক অপডেট তৌরে: {{crop}}",
      "newFarmerSubmission": "📋 অনৌবা লৌউমী দরখস্ত: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ মহৈ-মরোং চেক তৌরে: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ দরখস্ত য়াদ্রে: {{crop}}",
      "purchaseInquiry": "💼 লৈনবা হংবা: লৈরিবনা {{qty}} {{unit}} {{crop}} নাংই হায়রে",
      "demoReset": "🔄 ডেমো ডাটা রিসেট তৌরে",
      "inquirySent": "✓ লৈনবা হংবা লৌউমী / অফিসারদা থাখ্রে!",
      "statusUpdated": "পোত্থোক ফিভম অপডেট তৌরে", "deleted": "পোত্থোক রেকর্ড মুত্থৎলে"
    },
    "demo": {
      "controlsTitle": "SIH ডেমো কন্ট્રોલ:", "officerBtn": "অফিসার (রবী কুমার)",
      "farmerBtn": "লৌউমী (কুমার)", "buyerBtn": "লৈরিবশিংগী মিৎয়েং",
      "resetBtn": "ডেমো রিসেট", "resetConfirm": "ডাটাবেস অসি হান্নগী ডেমো ফিভমদা রিসেট তৌবা পাম্ব্রা?"
    }
  },
  "sat": {
    "lang": { "name": "Santali", "nativeName": "ᱥᱟᱱᱛᱟᱲᱤ", "code": "sat", "dir": "ltr" },
    "common": {
      "language": "ᱯᱟᱹᱨᱥᱤ", "login": "ᱵᱚᱞᱚᱱ", "register": "ᱧᱩᱛᱩᱢ ᱚᱞ", "logout": "ᱚᱰᱚᱠ",
      "dashboard": "ᱰᱮᱥᱵᱚᱨᱰ", "profile": "ᱯᱨᱚᱯᱷᱟᱭᱤᱞ", "save": "ᱥᱟᱺᱪᱟᱣ", "cancel": "ᱵᱟᱹᱜᱤ",
      "close": "ᱵᱚᱸᱫᱽ", "submit": "ᱮᱢ", "refresh": "ᱱᱟᱣᱟ", "search": "ᱥᱮᱸᱫᱽᱨᱟ",
      "clearFilters": "ᱪᱷᱟᱹᱱᱤ ᱚᱪᱚᱜ", "loading": "ᱞᱟᱫᱮᱜ ᱠᱟᱱᱟ...", "viewDetails": "ᱵᱤᱵᱨᱚᱬ ᱧᱮᱞ",
      "allStates": "ᱥᱟᱱᱟᱢ ᱯᱚᱱᱚᱛ", "allDistricts": "ᱥᱟᱱᱟᱢ ᱦᱚᱱᱚᱛ", "allAreas": "ᱥᱟᱱᱟᱢ ᱡᱟᱭᱜᱟ",
      "verified": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ", "pending": "ᱛᱟᱺᱜᱤ ᱨᱮ", "rejected": "ᱵᱟᱹᱛᱤᱞ",
      "available": "ᱧᱟᱢᱚᱜᱼᱟ", "unavailable": "ᱵᱟᱝ ᱧᱟᱢᱚᱜᱼᱟ", "yes": "ᱦᱮᱸ", "no": "ᱵᱟᱝ",
      "continue": "ᱞᱟᱦᱟ", "send": "ᱠᱩᱞ", "back": "ᱛᱟᱭᱚᱢ", "next": "ᱞᱟᱦᱟᱸ",
      "previous": "ᱯᱟᱹᱦᱤᱞ", "edit": "ᱥᱟᱯᱲᱟᱣ", "delete": "ᱢᱮᱴᱟᱣ", "status": "ᱦᱟᱞᱚᱛ",
      "role": "ᱮᱱᱮᱢ", "user": "ᱵᱮᱵᱷᱟᱨᱤᱭᱟᱹ", "liveSync": "ᱞᱟᱭᱤᱵᱷ ᱥᱤᱝᱠ", "reconnecting": "ᱡᱚᱲᱟᱣᱜ ᱠᱟᱱᱟ...",
      "reset": "ᱨᱤᱥᱮᱴ", "actions": "ᱠᱟᱹᱢᱤ", "crop": "ᱯᱷᱚᱥᱚᱞ", "quantity": "ᱞᱮᱠᱷᱟ/ᱦᱟᱹᱴᱤᱧ",
      "location": "ᱡᱟᱭᱜᱟ", "date": "ᱢᱟᱹᱦᱤᱛ", "notes": "ᱱᱚᱴ"
    },
    "navigation": {
      "home": "ᱚᱲᱟᱜ", "viewProduce": "ᱟᱨᱡᱟᱣ ᱧᱮᱞ", "officerPortal": "ᱚᱯᱷᱤᱥᱟᱨ ᱯᱳᱨᱴᱟᱞ",
      "farmerPortal": "ᱪᱟᱹᱥᱤ ᱯᱳᱨᱴᱟᱞ", "dashboard": "ᱰᱮᱥᱵᱚᱨᱰ", "profile": "ᱯᱨᱚᱯᱷᱟᱭᱤᱞ",
      "requests": "ᱱᱮᱦᱚᱸᱨ", "addProduce": "ᱟᱨᱡᱟᱣ ᱥᱮᱞᱮᱫ", "addCrop": "ᱯᱷᱚᱥᱚᱞ ᱥᱮᱞᱮᱫ",
      "myRequests": "ᱤᱧᱟᱜ ᱱᱮᱦᱚᱸᱨ", "farmerRequests": "ᱪᱟᱹᱥᱤ ᱱᱮᱦᱚᱸᱨ",
      "liveSync": "ᱞᱟᱭᱤᱵᱷ ᱥᱤᱝᱠ", "publicBuyerView": "ᱠᱤᱨᱤᱧᱤᱭᱟᱹ ᱧᱮᱞ"
    },
    "auth": {
      "roleSelector": "ᱟᱢᱟᱜ ᱮᱱᱮᱢ ᱵᱟᱪᱷᱟᱣ", "agricultureOfficer": "ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ", "farmer": "ᱪᱟᱹᱥᱤ",
      "mobileOrEmail": "ᱢᱳᱵᱟᱭᱤᱞ ᱱᱚᱢᱵᱚᱨ ᱥᱮ ᱤᱢᱮᱞ", "password": "ᱯᱟᱥᱣᱟᱨᱰ", "signIn": "ᱥᱟᱭᱤᱱ ᱤᱱ",
      "fullName": "ᱯᱩᱨᱟᱹ ᱧᱩᱛᱩᱢ", "mobileNumber": "ᱢᱳᱵᱟᱭᱤᱞ ᱱᱚᱢᱵᱚᱨ", "emailOptional": "ᱤᱢᱮᱞ (ᱤᱪᱷᱟᱹ)",
      "createAccount": "ᱠᱷᱟᱛᱟ ᱵᱮᱱᱟᱣ", "designation": "ᱯᱚᱫᱽ", "department": "ᱵᱤᱵᱷᱟᱜᱽ",
      "assignedArea": "ᱮᱢ ᱟᱠᱟᱱ ᱡᱟᱭᱜᱟ", "district": "ᱦᱚᱱᱚᱛ", "state": "ᱯᱚᱱᱚᱛ",
      "village": "ᱟᱹᱛᱩ", "landArea": "ᱦᱟᱥᱟ (ᱮᱠᱚᱲ)", "farmingType": "ᱪᱟᱥ ᱦᱚᱨᱟ",
      "welcomeBack": "ᱥᱟᱹᱜᱩᱱ ᱫᱟᱨᱟᱢ, {{name}}!", "accountCreated": "ᱠᱷᱟᱛᱟ ᱵᱮᱱᱟᱣᱮᱱᱟ! ᱥᱟᱹᱜᱩᱱ ᱫᱟᱨᱟᱢ, {{name}}.",
      "invalidCredentials": "ᱵᱟᱹᱲᱤᱡ ᱞᱚᱜᱤᱱ ᱛᱟᱹᱞᱠᱟᱹ", "requiredFields": "ᱥᱟᱱᱟᱢ ᱞᱟᱹᱠᱛᱤᱭᱟᱱ ᱠᱷᱚᱸᱫᱽ ᱯᱮᱨᱮᱡᱽ ᱢᱮ (ᱧᱩᱛᱩᱢ, ᱢᱳᱵᱟᱭᱤᱞ, ᱯᱟᱥᱣᱟᱨᱰ)᱾",
      "demoLoginFailed": "ᱰᱮᱢᱳ ᱞᱚᱜᱤᱱ ᱵᱟᱝ ᱦᱩᱭᱞᱮᱱᱟ", "networkError": "ᱱᱮᱴᱣᱟᱨᱠ ᱵᱟᱹᱲᱤᱡ",
      "logoutSuccess": "ᱟᱢ ᱵᱟᱦᱨᱮ ᱚᱰᱚᱠ ᱮᱱᱟᱢ᱾",
      "officerLoginRequired": "ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ ᱞᱮᱠᱟᱛᱮ ᱵᱚᱞᱚᱱ ᱢᱮ᱾", "farmerLoginRequired": "ᱪᱟᱹᱥᱤ ᱞᱮᱠᱟᱛᱮ ᱵᱚᱞᱚᱱ ᱢᱮ᱾",
      "registrationFailed": "ᱧᱩᱛᱩᱢ ᱚᱞ ᱵᱟᱝ ᱦᱩᱭᱞᱮᱱᱟ᱾", "switchedRole": "{{role}} ᱛᱮ ᱵᱚᱫᱚᱞᱮᱱᱟ"
    },
    "landing": {
      "verifiedPlatform": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱴᱚᱴᱷᱟᱣᱟᱨᱤ ᱪᱟᱥ ᱟᱨᱡᱟᱣ ᱢᱮᱞᱟᱝᱠᱤ", "title": "ᱥᱮᱸᱫᱽᱨᱟᱭ ᱢᱮ᱾ ᱯᱚᱨᱠᱷᱟᱣ ᱢᱮ᱾ ᱡᱚᱲᱟᱣᱜ ᱢᱮ᱾",
      "subtitle": "ᱮᱜᱽᱨᱤᱯᱷᱞᱳ ᱪᱟᱹᱥᱤ ᱟᱨ ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ ᱠᱚ ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱪᱟᱥ ᱟᱨᱡᱟᱣ ᱨᱮᱱᱟᱜ ᱵᱤᱵᱨᱚᱬ ᱫᱚᱦᱚ ᱨᱮ ᱜᱚᱲᱚ ᱮᱢᱟᱭ᱾",
      "searchVerifiedProduce": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱟᱨᱡᱟᱣ ᱥᱮᱸᱫᱽᱨᱟᱭ ᱢᱮ", "findVerifiedProduce": "ᱟᱨᱡᱟᱣ ᱯᱟᱱᱛᱮ",
      "quickDiscovery": "ᱡᱟᱭᱜᱟ ᱞᱮᱠᱟᱛᱮ ᱞᱚᱜᱚᱱ ᱥᱮᱸᱫᱽᱨᱟ", "cropName": "ᱯᱷᱚᱥᱚᱞ ᱧᱩᱛᱩᱢ",
      "cropPlaceholder": "ᱡᱮᱞᱮᱠᱟ: ᱯᱮᱭᱟᱸᱡᱽ, ᱵᱤᱞᱟᱹᱛᱤ...", "state": "ᱯᱚᱱᱚᱛ", "district": "ᱦᱚᱱᱚᱛ",
      "allStates": "ᱥᱟᱱᱟᱢ ᱯᱚᱱᱚᱛ", "allDistricts": "ᱥᱟᱱᱟᱢ ᱦᱚᱱᱚᱛ", "howItWorks": "ᱮᱜᱽᱨᱤᱯᱷᱞᱳ ᱪᱮᱫ ᱞᱮᱠᱟᱛᱮ ᱠᱟᱹᱢᱤᱭᱟ",
      "workflowIntro": "ᱴᱚᱴᱷᱟᱣᱟᱨᱤ ᱪᱟᱥ ᱠᱷᱩᱞᱟᱹ ᱵᱟᱡᱟᱨ ᱥᱟᱶ ᱡᱚᱲᱟᱣ ᱞᱟᱹᱜᱤᱫ ᱢᱤᱫ ᱥᱟᱯᱷᱟ ᱯᱚᱨᱠᱷᱟᱣ ᱦᱚᱨᱟ᱾",
      "sihPlatform": "SIH ᱢᱮᱞᱟᱝᱠᱤ", "tagLine": "ᱥᱮᱸᱫᱽᱨᱟᱭ ᱢᱮ᱾ ᱯᱚᱨᱠᱷᱟᱣ ᱢᱮ᱾ ᱡᱚᱲᱟᱣᱜ ᱢᱮ᱾"
    },
    "howItWorks": {
      "farmerSubmission": "ᱪᱟᱹᱥᱤᱭᱟᱜ ᱮᱢ",
      "farmerSubmissionDesc": "ᱪᱟᱹᱥᱤ ᱠᱚ ᱟᱠᱚᱣᱟᱜ ᱪᱟᱥ ᱦᱟᱥᱟ, ᱯᱷᱚᱥᱚᱞ ᱦᱟᱞᱚᱛ ᱟᱨ ᱟᱨᱡᱟᱣ ᱯᱚᱨᱠᱷᱟᱣ ᱞᱟᱹᱜᱤᱫ ᱠᱚ ᱮᱢᱟ᱾",
      "officerVerification": "ᱚᱯᱷᱤᱥᱟᱨᱟᱜ ᱯᱚᱨᱠᱷᱟᱣ",
      "officerVerificationDesc": "ᱴᱚᱴᱷᱟᱣᱟᱨᱤ ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ ᱠᱚ ᱠᱷᱮᱛ ᱧᱮᱞ ᱠᱟᱛᱮ ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱟᱨᱡᱟᱣ ᱠᱚ ᱩᱪᱷᱟᱹᱱᱟ᱾",
      "publicDiscovery": "ᱦᱚᱲ ᱥᱮᱸᱫᱽᱨᱟ ᱟᱨ ᱡᱚᱯᱚᱲᱟᱣ",
      "publicDiscoveryDesc": "ᱠᱤᱨᱤᱧᱤᱭᱟᱹ ᱠᱚ ᱵᱤᱱᱟ ᱞᱚᱜᱤᱱ ᱛᱮ ᱯᱷᱚᱥᱚᱞ, ᱦᱚᱱᱚᱛ ᱟᱨ ᱦᱟᱹᱴᱤᱧ ᱞᱮᱠᱟᱛᱮ ᱟᱞᱜᱟ ᱛᱮᱠᱚ ᱧᱟᱢᱟ᱾"
    },
    "roles": {
      "farmers": "ᱪᱟᱹᱥᱤ ᱠᱚ ᱞᱟᱹᱜᱤᱫ", "officers": "ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ ᱠᱚ ᱞᱟᱹᱜᱤᱫ", "buyers": "ᱠᱤᱨᱤᱧᱤᱭᱟᱹ ᱟᱨ ᱵᱮᱯᱟᱨᱤ ᱠᱚ ᱞᱟᱹᱜᱤᱫ",
      "farmerTitle": "ᱯᱷᱚᱥᱚᱞ ᱨᱮᱱᱟᱜ ᱥᱚᱡᱷᱮ ᱧᱮᱞ", "officerTitle": "ᱴᱚᱴᱷᱟ ᱪᱟᱪᱞᱟᱣ ᱟᱨ ᱯᱟᱹᱛᱭᱟᱹᱣ",
      "buyerTitle": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱥᱟᱢᱟᱱ ᱥᱮᱸᱫᱽᱨᱟ",
      "farmerItem1": "ᱪᱟᱥ ᱯᱨᱚᱯᱷᱟᱭᱤᱞ ᱟᱨ ᱦᱟᱥᱟ ᱧᱩᱛᱩᱢ ᱚᱞ ᱢᱮ",
      "farmerItem2": "ᱴᱚᱴᱷᱟᱣᱟᱨᱤ ᱯᱚᱨᱠᱷᱟᱣ ᱞᱟᱹᱜᱤᱫ ᱟᱨᱡᱟᱣ ᱮᱢ ᱢᱮ",
      "farmerItem3": "ᱱᱤᱛᱚᱜᱟᱜ ᱦᱟᱞᱚᱛ ᱵᱟᱰᱟᱭ ᱢᱮ: ᱛᱟᱺᱜᱤ ᱨᱮ → ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ / ᱵᱟᱹᱛᱤᱞ",
      "officerItem1": "ᱴᱚᱴᱷᱟ ᱨᱮᱱᱟᱜ ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱪᱟᱥ ᱟᱨᱡᱟᱣ ᱥᱚᱡᱷᱮ ᱥᱮᱞᱮᱫ ᱢᱮ",
      "officerItem2": "ᱟᱢᱟᱜ ᱵᱞᱚᱠ ᱨᱤᱱ ᱪᱟᱹᱥᱤ ᱠᱚᱣᱟᱜ ᱟᱨᱫᱟᱥ ᱠᱷᱮᱛ ᱧᱮᱞ ᱠᱟᱛᱮ ᱯᱚᱨᱠᱷᱟᱣ ᱢᱮ",
      "officerItem3": "ᱦᱟᱹᱴᱤᱧ ᱟᱨ ᱧᱟᱢᱚᱜ ᱦᱟᱞᱚᱛ ᱱᱟᱣᱟ ᱢᱮ",
      "buyerItem1": "ᱵᱤᱱᱟ ᱞᱚᱜᱤᱱ ᱛᱮ ᱞᱚᱜᱚᱱ ᱟᱨᱡᱟᱣ ᱯᱟᱱᱛᱮᱭ ᱢᱮ",
      "buyerItem2": "ᱯᱚᱱᱚᱛ, ᱦᱚᱱᱚᱛ, ᱡᱟᱭᱜᱟ ᱟᱨ ᱦᱟᱹᱴᱤᱧ ᱞᱮᱠᱟᱛᱮ ᱪᱷᱟᱹᱱᱤ ᱢᱮ",
      "buyerItem3": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱪᱟᱹᱥᱤ ᱠᱚ ᱥᱚᱡᱷᱮ ᱠᱤᱨᱤᱧ ᱱᱮᱦᱚᱸᱨ ᱠᱩᱞ ᱢᱮ"
    },
    "produce": {
      "title": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱟᱨᱡᱟᱣ ᱥᱮᱸᱫᱽᱨᱟ",
      "subtitle": "ᱴᱚᱴᱷᱟᱣᱟᱨᱤ ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ ᱠᱚ ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱫ ᱧᱟᱢᱚᱜ ᱟᱨ ᱦᱤᱡᱩᱜ ᱠᱟᱱ ᱪᱟᱥ ᱟᱨᱡᱟᱣ ᱥᱮᱸᱫᱽᱨᱟᱭ ᱢᱮ᱾",
      "searchCropName": "ᱯᱷᱚᱥᱚᱞ ᱧᱩᱛᱩᱢ ᱥᱮᱸᱫᱽᱨᱟᱭ ᱢᱮ", "state": "ᱯᱚᱱᱚᱛ", "district": "ᱦᱚᱱᱚᱛ", "areaBlock": "ᱡᱟᱭᱜᱟ / ᱵᱞᱚᱠ",
      "minQty": "ᱠᱚᱢ ᱦᱟᱹᱴᱤᱧ (ᱴᱚᱱ)", "maxQty": "ᱰᱷᱮᱨ ᱦᱟᱹᱴᱤᱧ (ᱴᱚᱱ)", "availBefore": "ᱧᱟᱢᱚᱜ ᱢᱟᱹᱦᱤᱛ ᱦᱟᱹᱵᱤᱡ/ᱨᱮ",
      "verifiedOnly": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱜᱮ (ᱵᱷᱟᱹᱜᱤ)", "clearFilters": "ᱪᱷᱟᱹᱱᱤ ᱚᱪᱚᱜ",
      "count": "{{count}} ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱟᱨᱡᱟᱣ ᱨᱮᱠᱚᱨᱰ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ",
      "countPlural": "{{count}} ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱟᱨᱡᱟᱣ ᱨᱮᱠᱚᱨᱰ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ",
      "emptyTitle": "ᱪᱮᱫ ᱟᱨᱡᱟᱣ ᱨᱮᱠᱚᱨᱰ ᱵᱟᱝ ᱧᱟᱢ ᱞᱮᱱᱟ",
      "emptyDescription": "ᱥᱮᱸᱫᱽᱨᱟ ᱯᱟᱥᱱᱟᱣ ᱢᱮ ᱥᱮ ᱪᱷᱟᱹᱱᱤ ᱚᱪᱚᱜ ᱠᱟᱛᱮ ᱥᱩᱨ ᱨᱮᱱᱟᱜ ᱯᱷᱚᱥᱚᱞ ᱧᱮᱞ ᱢᱮ᱾",
      "resetAllFilters": "ᱥᱟᱱᱟᱢ ᱪᱷᱟᱹᱱᱤ ᱨᱤᱥᱮᱴ ᱢᱮ", "autoSynced": "WebSocket ᱛᱮ ᱞᱟᱭᱤᱵᱷ ᱥᱤᱝᱠ",
      "availableQuantity": "ᱧᱟᱢᱚᱜ ᱦᱟᱹᱴᱤᱧ", "quality": "ᱜᱩᱱ", "availability": "ᱧᱟᱢᱚᱜ",
      "sourceOfficer": "ᱚᱯᱷᱤᱥᱟᱨ ᱯᱚᱨᱠᱷᱟᱣ", "sourceFarmer": "ᱪᱟᱹᱥᱤ ᱯᱚᱨᱠᱷᱟᱣ",
      "verifiedBadge": "✓ ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ", "qualityGrade": "ᱜᱩᱱ ᱛᱷᱚᱠ", "verificationSource": "ᱯᱚᱨᱠᱷᱟᱣ ᱯᱷᱮᱰᱟᱛ",
      "fieldNotes": "ᱚᱯᱷᱤᱥᱟᱨᱟᱜ ᱠᱷᱮᱛ ᱧᱮᱞ ᱱᱚᱴ",
      "purchaseTitle": "ᱠᱤᱨᱤᱧ ᱠᱩᱠᱞᱤ / ᱱᱮᱦᱚᱸᱨ ᱠᱩᱞ ᱢᱮ",
      "purchaseSubtitle": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱪᱟᱹᱥᱤ / ᱚᱯᱷᱤᱥᱟᱨ ᱥᱟᱶ ᱡᱚᱲᱟᱣᱜ ᱞᱟᱹᱜᱤᱫ ᱟᱢᱟᱜ ᱞᱟᱹᱠᱛᱤ ᱮᱢ ᱢᱮ᱾",
      "yourName": "ᱟᱢᱟᱜ ᱧᱩᱛᱩᱢ / ᱠᱚᱢᱯᱟᱹᱱᱤ", "contact": "ᱯᱷᱳᱱ ᱱᱚᱢᱵᱚᱨ / ᱤᱢᱮᱞ",
      "requestedQty": "ᱞᱟᱹᱠᱛᱤᱭᱟᱱ ᱦᱟᱹᱴᱤᱧ", "message": "ᱠᱷᱚᱵᱚᱨ / ᱞᱟᱹᱠᱛᱤ", "sendRequest": "ᱠᱤᱨᱤᱧ ᱱᱮᱦᱚᱸᱨ ᱠᱩᱞ ᱢᱮ",
      "notFound": "ᱟᱨᱡᱟᱣ ᱨᱮᱠᱚᱨᱰ ᱵᱟᱝ ᱧᱟᱢ ᱞᱮᱱᱟ", "noLogin": "ᱞᱚᱜᱤᱱ ᱵᱟᱝ ᱞᱟᱹᱠᱛᱤᱜᱼᱟ", "unitLabel": "ᱮᱠᱚᱠ"
    },
    "officer": {
      "portal": "ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ ᱯᱳᱨᱴᱟᱞ", "subtitle": "ᱴᱚᱴᱷᱟ ᱨᱮᱱᱟᱜ ᱟᱨᱡᱟᱣ ᱥᱟᱢᱵᱽᱲᱟᱣ ᱢᱮ, ᱪᱟᱹᱥᱤ ᱠᱚᱣᱟᱜ ᱱᱮᱦᱚᱸᱨ ᱯᱚᱨᱠᱷᱟᱣ ᱢᱮ",
      "profile": "ᱯᱨᱚᱯᱷᱟᱭᱤᱞ ᱥᱟᱯᱲᱟᱣ", "totalRecords": "ᱢᱩᱴᱷ ᱨᱮᱠᱚᱨᱰ", "totalRecordsHint": "ᱟᱢᱟᱜ ᱴᱚᱴᱷᱟ ᱨᱮ",
      "availableQty": "ᱧᱟᱢᱚᱜ ᱦᱟᱹᱴᱤᱧ", "availableQtyHint": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱟᱨᱡᱟᱣ", "farmerRequests": "ᱪᱟᱹᱥᱤ ᱱᱮᱦᱚᱸᱨ",
      "pending": "ᱠᱷᱮᱛ ᱧᱮᱞ ᱛᱟᱺᱜᱤ ᱨᱮ", "verifiedRecords": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱨᱮᱠᱚᱨᱰ", "verifiedRecordsHint": "ᱠᱤᱨᱤᱧᱤᱭᱟᱹ ᱠᱚ ᱞᱟᱹᱜᱤᱫ",
      "queueTitle": "ᱪᱟᱹᱥᱤ ᱯᱚᱨᱠᱷᱟᱣ ᱱᱮᱦᱚᱸᱨ", "queueSubtitle": "ᱟᱢᱟᱜ ᱴᱚᱴᱷᱟ ᱨᱮ ᱠᱷᱮᱛ ᱧᱮᱞ ᱛᱟᱺᱜᱤ ᱨᱮ ᱢᱮᱱᱟᱜ ᱠᱚ ᱪᱟᱹᱥᱤ",
      "queueEmpty": "ᱥᱟᱱᱟᱢ ᱠᱟᱹᱢᱤ ᱯᱩᱨᱟᱹᱣ ᱮᱱᱟ! ᱪᱮᱫ ᱱᱮᱦᱚᱸᱨ ᱵᱟᱹᱱᱩᱜᱼᱟ᱾",
      "localProduceTitle": "ᱴᱚᱴᱷᱟᱣᱟᱨᱤ ᱪᱟᱥ ᱟᱨᱡᱟᱣ", "localProduceSubtitle": "ᱟᱢᱟᱜ ᱪᱟᱪᱞᱟᱣ ᱨᱮ ᱩᱪᱷᱟᱹᱱ ᱟᱠᱟᱱ ᱟᱨᱡᱟᱣ",
      "addProduce": "+ ᱟᱨᱡᱟᱣ ᱥᱮᱞᱮᱫ", "editProduce": "ᱟᱨᱡᱟᱣ ᱥᱟᱯᱲᱟᱣ", "addProduceModalTitle": "+ ᱴᱚᱴᱷᱟᱣᱟᱨᱤ ᱟᱨᱡᱟᱣ ᱥᱮᱞᱮᱫ",
      "modalSubtitle": "ᱚᱯᱷᱤᱥᱟᱨ ᱥᱚᱡᱷᱮ ᱚᱞ ᱟᱠᱟᱫ ᱟᱨᱡᱟᱣ ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ ᱞᱮᱠᱟᱛᱮ ᱞᱮᱠᱷᱟᱜᱼᱟ",
      "savePublish": "ᱥᱟᱺᱪᱟᱣ ᱟᱨ ᱩᱪᱷᱟᱹᱱ", "verify": "ᱯᱚᱨᱠᱷᱟᱣ", "reject": "ᱵᱟᱹᱛᱤᱞ",
      "pendingBadge": "🟡 ᱛᱟᱺᱜᱤ ᱨᱮ", "directOfficerEntry": "ᱚᱯᱷᱤᱥᱟᱨᱟᱜ ᱥᱚᱡᱷᱮ ᱚᱞ",
      "markUnavailable": "ᱵᱟᱝ ᱧᱟᱢᱚᱜ ᱪᱤᱱᱦᱟᱹ", "markAvailable": "ᱧᱟᱢᱚᱜ ᱪᱤᱱᱦᱟᱹ",
      "editProduceAction": "ᱟᱨᱡᱟᱣ ᱥᱟᱯᱲᱟᱣ", "deleteProduce": "ᱨᱮᱠᱚᱨᱰ ᱢᱮᱴᱟᱣ",
      "deleteConfirm": "ᱟᱢ ᱱᱚᱣᱟ ᱨᱮᱠᱚᱨᱰ ᱢᱮᱴᱟᱣ ᱥᱟᱱᱟᱭᱮᱫ ᱢᱮᱭᱟ ᱥᱮ?", "rejectTitle": "ᱪᱟᱹᱥᱤ ᱱᱮᱦᱚᱸᱨ ᱵᱟᱹᱛᱤᱞ",
      "rejectDescription": "ᱵᱟᱹᱛᱤᱞ ᱨᱮᱱᱟᱜ ᱠᱟᱨᱚᱱ ᱚᱞ ᱢᱮ",
      "rejectionReason": "ᱠᱟᱨᱚᱱ / ᱥᱩᱫᱷᱨᱟᱹᱣ ᱞᱟᱹᱠᱛᱤ",
      "rejectionPlaceholder": "ᱡᱮᱞᱮᱠᱟ: ᱟᱨᱡᱟᱣ ᱦᱟᱥᱟ ᱥᱟᱶ ᱵᱟᱝ ᱢᱤᱞᱟᱹᱣᱜ ᱠᱟᱱᱟ; ᱫᱚᱦᱲᱟ ᱡᱚᱠᱷᱟᱭ ᱢᱮ᱾",
      "confirmRejection": "ᱵᱟᱹᱛᱤᱞ ᱴᱷᱟᱹᱣᱠᱟᱹ", "fieldInspected": "ᱚᱯᱷᱤᱥᱟᱨ ᱠᱷᱮᱛ ᱧᱮᱞ ᱠᱟᱛᱮ ᱯᱚᱨᱠᱷᱟᱣ ᱠᱮᱫᱟᱭ",
      "verificationSuccess": "✓ ᱪᱟᱹᱥᱤ ᱟᱨᱫᱟᱥ ᱯᱚᱨᱠᱷᱟᱣ ᱮᱱᱟ ᱟᱨ ᱩᱪᱷᱟᱹᱱ ᱮᱱᱟ!",
      "rejectionSuccess": "ᱱᱮᱦᱚᱸᱨ ᱵᱟᱹᱛᱤᱞ ᱮᱱᱟ ᱟᱨ ᱪᱟᱹᱥᱤ ᱵᱟᱰᱟᱭ ᱚᱪᱚ ᱮᱱᱟᱭ᱾",
      "provideReason": "ᱵᱟᱹᱛᱤᱞ ᱨᱮᱱᱟᱜ ᱠᱟᱨᱚᱱ ᱮᱢ ᱢᱮ", "noProduceYet": "ᱟᱢᱟᱜ ᱴᱚᱴᱷᱟ ᱨᱮ ᱱᱤᱛ ᱦᱟᱹᱵᱤᱡ ᱪᱮᱫ ᱟᱨᱡᱟᱣ ᱵᱟᱝ ᱚᱞ ᱟᱠᱟᱱᱟ᱾",
      "cropCol": "ᱯᱷᱚᱥᱚᱞ", "qtyCol": "ᱦᱟᱹᱴᱤᱧ", "locationCol": "ᱡᱟᱭᱜᱟ", "availDateCol": "ᱧᱟᱢᱚᱜ ᱢᱟᱹᱦᱤᱛ",
      "qualityCol": "ᱜᱩᱱ", "sourceCol": "ᱯᱷᱮᱰᱟᱛ", "statusCol": "ᱦᱟᱞᱚᱛ", "actionsCol": "ᱠᱟᱹᱢᱤ",
      "officerRecordedSuccess": "✓ ᱚᱯᱷᱤᱥᱟᱨ ᱥᱚᱡᱷᱮ ᱚᱞ ᱠᱟᱛᱮ ᱯᱚᱨᱠᱷᱟᱣ ᱠᱮᱫᱟᱭ!",
      "updateProduceSuccess": "ᱟᱨᱡᱟᱣ ᱱᱟᱣᱟ ᱮᱱᱟ"
    },
    "farmer": {
      "portal": "ᱪᱟᱹᱥᱤ ᱯᱳᱨᱴᱟᱞ", "myProfile": "ᱤᱧᱟᱜ ᱪᱟᱥ ᱯᱨᱚᱯᱷᱟᱭᱤᱞ",
      "assignedOfficer": "ᱟᱢ ᱞᱟᱹᱜᱤᱫ ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ", "assignedOfficerHint": "ᱱᱮᱦᱚᱸᱨ ᱠᱚ ᱱᱚᱰᱮ ᱥᱮᱱᱚᱜᱼᱟ",
      "totalSubmissions": "ᱢᱩᱴᱷ ᱱᱮᱦᱚᱸᱨ", "pending": "ᱛᱟᱺᱜᱤ ᱨᱮ", "verified": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ & ᱪᱟᱹᱞᱩ",
      "rejected": "ᱵᱟᱹᱛᱤᱞ", "requestsTitle": "ᱤᱧᱟᱜ ᱯᱷᱚᱥᱚᱞ ᱯᱚᱨᱠᱷᱟᱣ ᱱᱮᱦᱚᱸᱨ",
      "requestsSubtitle": "ᱪᱟᱥ ᱚᱯᱷᱤᱥᱟᱨ ᱠᱷᱚᱱ ᱦᱟᱞᱚᱛ ᱵᱟᱰᱟᱭ ᱢᱮ",
      "addCrop": "+ ᱯᱷᱚᱥᱚᱞ ᱵᱤᱵᱨᱚᱬ ᱥᱮᱞᱮᱫ", "addCropButton": "+ ᱯᱷᱚᱥᱚᱞ ᱥᱮᱞᱮᱫ", "myCropDetails": "+ ᱪᱟᱥ ᱯᱷᱚᱥᱚᱞ ᱵᱤᱵᱨᱚᱬ ᱥᱮᱞᱮᱫ",
      "submittedToOfficer": "ᱯᱚᱨᱠᱷᱟᱣ ᱞᱟᱹᱜᱤᱫ ᱚᱯᱷᱤᱥᱟᱨ ᱴᱷᱮᱱ ᱠᱩᱞ ᱦᱩᱭᱩᱜᱼᱟ",
      "submitToOfficer": "ᱚᱯᱷᱤᱥᱟᱨ ᱴᱷᱮᱱ ᱮᱢ ᱢᱮ", "noCrops": "ᱱᱤᱛ ᱦᱟᱹᱵᱤᱡ ᱯᱷᱚᱥᱚᱞ ᱵᱟᱝ ᱮᱢ ᱟᱠᱟᱱᱟ",
      "noCropsDescription": "ᱯᱚᱨᱠᱷᱟᱣ ᱞᱟᱹᱜᱤᱫ ᱟᱢᱟᱜ ᱪᱟᱥ ᱵᱤᱵᱨᱚᱬ ᱥᱮᱞᱮᱫ ᱢᱮ᱾", "addFirstCrop": "ᱯᱩᱭᱞᱩ ᱯᱷᱚᱥᱚᱞ ᱥᱮᱞᱮᱫ ᱢᱮ",
      "pendingStatus": "🟡 ᱛᱟᱺᱜᱤ ᱨᱮ", "verifiedStatus": "🟢 ✓ ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ", "rejectedStatus": "🔴 ᱵᱟᱹᱛᱤᱞ",
      "expectedHarvest": "ᱟᱥᱟ ᱟᱨᱡᱟᱣ ᱢᱟᱹᱦᱤᱛ", "cultivatedArea": "ᱪᱟᱥ ᱦᱟᱥᱟ", "expectedYield": "ᱟᱥᱟ ᱟᱨᱡᱟᱣ",
      "cropStage": "ᱯᱷᱚᱥᱚᱞ ᱦᱟᱞᱚᱛ", "officerFeedback": "ᱚᱯᱷᱤᱥᱟᱨᱟᱜ ᱠᱟᱛᱷᱟ:", "submissionSuccess": "✓ ᱯᱷᱚᱥᱚᱞ ᱮᱢ ᱮᱱᱟ! ᱯᱚᱨᱠᱷᱟᱣ ᱞᱟᱹᱜᱤᱫ ᱠᱩᱞ ᱮᱱᱟ᱾",
      "verificationStatus": "ᱛᱟᱺᱜᱤ ᱨᱮ → ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ / ᱵᱟᱹᱛᱤᱞ", "locationRouting": "ᱡᱟᱭᱜᱟ ᱦᱚᱨ (ᱚᱯᱷᱤᱥᱟᱨ ᱞᱟᱹᱜᱤᱫ)",
      "additionalNotes": "ᱮᱴᱟᱜ ᱪᱟᱥ ᱱᱚᱴ", "farmingNotesPlaceholder": "ᱪᱟᱥ ᱦᱚᱨᱟ, ᱫᱟᱜ ᱯᱟᱴᱟᱣ, ᱥᱟᱨ ᱵᱤᱵᱨᱚᱬ..."
    },
    "profile": {
      "title": "ᱤᱧᱟᱜ ᱯᱨᱚᱯᱷᱟᱭᱤᱞ", "subtitle": "ᱟᱢᱟᱜ ᱠᱷᱟᱛᱟ ᱟᱨ ᱪᱟᱥ ᱵᱤᱵᱨᱚᱬ ᱥᱟᱢᱵᱽᱲᱟᱣ ᱢᱮ",
      "saveChanges": "ᱵᱚᱫᱚᱞ ᱥᱟᱺᱪᱟᱣ ᱢᱮ", "fullName": "ᱯᱩᱨᱟᱹ ᱧᱩᱛᱩᱢ", "village": "ᱟᱹᱛᱩ",
      "area": "ᱡᱟᱭᱜᱟ / ᱵᱞᱚᱠ", "district": "ᱦᱚᱱᱚᱛ", "state": "ᱯᱚᱱᱚᱛ", "landArea": "ᱦᱟᱥᱟ",
      "landUnit": "ᱦᱟᱥᱟ ᱮᱠᱚᱠ", "farmingType": "ᱪᱟᱥ ᱦᱚᱨᱟ", "officialEmail": "ᱥᱚᱨᱠᱟᱨᱤ ᱤᱢᱮᱞ",
      "designation": "ᱚᱯᱷᱤᱥᱟᱨ ᱯᱚᱫᱽ", "department": "ᱵᱤᱵᱷᱟᱜᱽ", "contactNumber": "ᱯᱷᱳᱱ ᱱᱚᱢᱵᱚᱨ",
      "assignedArea": "ᱮᱢ ᱟᱠᱟᱱ ᱡᱟᱭᱜᱟ / ᱵᱞᱚᱠ", "profileUpdated": "ᱯᱨᱚᱯᱷᱟᱭᱤᱞ ᱱᱟᱣᱟ ᱮᱱᱟ"
    },
    "crops": {
      "onion": "ᱯᱮᱭᱟᱸᱡᱽ", "tomato": "ᱵᱤᱞᱟᱹᱛᱤ", "potato": "ᱟᱹᱞᱩ", "rice": "ᱦᱩᱲᱩ / ᱪᱟᱣᱞᱮ",
      "wheat": "ᱜᱩᱦᱩᱢ", "maize": "ᱡᱚᱱᱰᱨᱟ", "carrot": "ᱜᱟᱡᱚᱨ", "cabbage": "ᱵᱟᱸᱫᱷᱟ ᱠᱚᱵᱤ",
      "cauliflower": "ᱯᱷᱩᱞ ᱠᱚᱵᱤ", "garlic": "ᱨᱟᱹᱥᱩᱱ", "ginger": "ᱟᱹᱫᱟᱹ", "banana": "ᱠᱟᱭᱨᱟ",
      "mango": "ᱩᱞ", "groundnut": "ᱪᱤᱱᱟᱵᱟᱫᱟᱢ", "sugarcane": "ᱟᱹᱠᱷ", "cotton": "ᱠᱟᱥᱠᱚᱢ"
    },
    "produce_types": {
      "tubers": "ᱫᱟᱜ ᱟᱹᱞᱩ", "vegetable": "ᱩᱛᱩ ᱟᱲᱟᱜ", "vegetable_bulbs": "ᱩᱛᱩ / ᱫᱟᱜ ᱟᱹᱞᱩ",
      "field_crop": "ᱵᱟᱹᱫᱽ ᱯᱷᱚᱥᱚᱞ", "cereals": "ᱡᱚᱢᱟᱜ ᱦᱩᱲᱩ", "fruits": "ᱡᱚ",
      "cash_crops": "ᱴᱟᱠᱟ ᱯᱷᱚᱥᱚᱞ", "spices": "ᱢᱚᱥᱞᱟ"
    },
    "units": { "tons": "ᱴᱚᱱ", "quintals": "ᱠᱩᱣᱤᱱᱴᱟᱞ", "kg": "ᱠᱤᱞᱳ", "acres": "ᱮᱠᱚᱲ", "hectares": "ᱦᱮᱠᱴᱚᱨ" },
    "qualities": {
      "gradeA": "ᱛᱷᱚᱠ A", "gradeB": "ᱛᱷᱚᱠ B", "gradeC": "ᱛᱷᱚᱠ C",
      "gradeAPremium": "ᱛᱷᱚᱠ A (ᱥᱚᱨᱮᱥ)", "gradeBStandard": "ᱛᱷᱚᱠ B (ᱥᱟᱫᱷᱟᱨᱚᱱ)", "gradeCFair": "ᱛᱷᱚᱠ C (ᱛᱟᱞᱟ)"
    },
    "crop_stages": {
      "bulbDevelopment": "ᱫᱟᱜ ᱟᱹᱞᱩ ᱦᱟᱨᱟ", "vegetative": "ᱦᱟᱨᱟᱜ ᱦᱟᱞᱚᱛ",
      "flowering": "ᱵᱟᱦᱟᱜ ᱦᱟᱞᱚᱛ", "readyForHarvest": "ᱜᱮᱫ ᱞᱟᱹᱜᱤᱫ ᱥᱟᱯᱲᱟᱣ", "preHarvest": "ᱜᱮᱫ ᱞᱟᱦᱟᱨᱮ"
    },
    "statuses": {
      "verified": "ᱯᱚᱨᱠᱷᱟᱣ ᱟᱠᱟᱱ", "pending": "ᱛᱟᱺᱜᱤ ᱨᱮ", "rejected": "ᱵᱟᱹᱛᱤᱞ",
      "available": "ᱧᱟᱢᱚᱜᱼᱟ", "unavailable": "ᱵᱟᱝ ᱧᱟᱢᱚᱜᱼᱟ"
    },
    "sources": {
      "officerVerified": "ᱚᱯᱷᱤᱥᱟᱨ ᱯᱚᱨᱠᱷᱟᱣ", "farmerVerified": "ᱪᱟᱹᱥᱤ ᱯᱚᱨᱠᱷᱟᱣ",
      "directOfficerEntry": "ᱚᱯᱷᱤᱥᱟᱨᱟᱜ ᱥᱚᱡᱷᱮ ᱚᱞ"
    },
    "notifications": {
      "newProduceAdded": "🌾 ᱱᱟᱣᱟ ᱟᱨᱡᱟᱣ ᱥᱮᱞᱮᱫ ᱮᱱᱟ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 ᱟᱨᱡᱟᱣ ᱱᱟᱣᱟ ᱮᱱᱟ: {{crop}}",
      "newFarmerSubmission": "📋 ᱱᱟᱣᱟ ᱪᱟᱹᱥᱤ ᱟᱨᱫᱟᱥ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ ᱯᱷᱚᱥᱚᱞ ᱯᱚᱨᱠᱷᱟᱣ ᱮᱱᱟ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ ᱱᱮᱦᱚᱸᱨ ᱵᱟᱹᱛᱤᱞ ᱮᱱᱟ: {{crop}}",
      "purchaseInquiry": "💼 ᱠᱤᱨᱤᱧ ᱠᱩᱠᱞᱤ: ᱠᱤᱨᱤᱧᱤᱭᱟᱹ {{qty}} {{unit}} {{crop}} ᱠᱷᱚᱡᱮᱫᱟᱭ",
      "demoReset": "🔄 ᱰᱮᱢᱳ ᱰᱮᱴᱟ ᱨᱤᱥᱮᱴ ᱮᱱᱟ",
      "inquirySent": "✓ ᱠᱤᱨᱤᱧ ᱠᱩᱠᱞᱤ ᱪᱟᱹᱥᱤ / ᱚᱯᱷᱤᱥᱟᱨ ᱴᱷᱮᱱ ᱠᱩᱞ ᱮᱱᱟ!",
      "statusUpdated": "ᱟᱨᱡᱟᱣ ᱦᱟᱞᱚᱛ ᱱᱟᱣᱟ ᱮᱱᱟ", "deleted": "ᱟᱨᱡᱟᱣ ᱨᱮᱠᱚᱨᱰ ᱢᱮᱴᱟᱣ ᱮᱱᱟ"
    },
    "demo": {
      "controlsTitle": "SIH ᱰᱮᱢᱳ ᱠᱚᱱᱴᱨᱚᱞ:", "officerBtn": "ᱚᱯᱷᱤᱥᱟᱨ (ᱨᱚᱵᱤ ᱠᱩᱢᱟᱨ)",
      "farmerBtn": "ᱪᱟᱹᱥᱤ (ᱠᱩᱢᱟᱨ)", "buyerBtn": "ᱠᱤᱨᱤᱧᱤᱭᱟᱹ ᱧᱮᱞ",
      "resetBtn": "ᱰᱮᱢᱳ ᱨᱤᱥᱮᱴ", "resetConfirm": "ᱰᱮᱴᱟᱵᱮᱥ ᱮᱛᱚᱦᱚᱵ ᱰᱮᱢᱳ ᱦᱟᱞᱚᱛ ᱨᱮ ᱨᱤᱥᱮᱴ ᱥᱟᱱᱟᱭᱮᱫ ᱢᱮᱭᱟ ᱥᱮ?"
    }
  }
}
