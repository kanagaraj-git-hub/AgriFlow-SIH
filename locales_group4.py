# -*- coding: utf-8 -*-
"""
Language definitions for AgriFlow - Group 4:
Sanskrit (sa), Kashmiri (ks), Nepali (ne), Konkani (kok), Maithili (mai),
Bodo (brx), Dogri (doi), Meitei/Manipuri (mni), Santali (sat)
"""

LOCALES_GROUP_4 = {
  "sa": {
    "lang": { "name": "Sanskrit", "nativeName": "संस्कृतम्", "code": "sa", "dir": "ltr" },
    "common": {
      "language": "भाषा", "login": "प्रवेशः", "register": "पंजीकरणम्", "logout": "निर्गमः",
      "dashboard": "फलकम्", "profile": "विवरणम्", "save": "संरक्षतु", "cancel": "निरस्यतु",
      "close": "पिदधातु", "submit": "समर्पयतु", "refresh": "नवीकरोतु", "search": "अन्विष्यतु",
      "clearFilters": "शोधकानि अपनयतु", "loading": "प्रस्तूयते...", "viewDetails": "विवरणं पश्यतु",
      "allStates": "सर्वाणि राज्यानि", "allDistricts": "सर्वे मण्डलाः", "allAreas": "सर्वाणि क्षेत्राणि",
      "verified": "प्रमाणितम्", "pending": "प्रतीक्षारतम्", "rejected": "प्रत्याख्यातम्",
      "available": "उपलब्धम्", "unavailable": "अनुपलब्धम्", "yes": "आम्", "no": "न",
      "continue": "अनुवर्तताम्", "send": "प्रेषयतु", "back": "प्रतिनिवर्तताम्", "next": "अग्रिमम्",
      "previous": "पूर्वतनम्", "edit": "सम्पादयतु", "delete": "अपसारयतु", "status": "स्थितिः",
      "role": "भूमिका", "user": "प्रयोक्ता", "liveSync": "प्रत्यक्ष-समन्वयनम्", "reconnecting": "पुनर्योजनं क्रियते...",
      "reset": "पुनःस्थापयतु", "actions": "कार्याणि", "crop": "सस्यम्", "quantity": "परिमाणम्",
      "location": "स्थानम्", "date": "दिनाङ्कः", "notes": "टिप्पण्यः"
    },
    "navigation": {
      "home": "गृहम्", "viewProduce": "उत्पादनानि पश्यतु", "officerPortal": "अधिकारि-प्रवेशद्वारम्",
      "farmerPortal": "कृषक-प्रवेशद्वारम्", "dashboard": "फलकम्", "profile": "विवरणम्",
      "requests": "प्रार्थनाः", "addProduce": "उत्पादनं योजयतु", "addCrop": "सस्यं योजयतु",
      "myRequests": "मम प्रार्थनाः", "farmerRequests": "कृषक-प्रार्थनाः",
      "liveSync": "प्रत्यक्ष-समन्वयनम्", "publicBuyerView": "क्रेतृ-दृश्यम्"
    },
    "auth": {
      "roleSelector": "स्वभूमिकां वृणुध्वम्", "agricultureOfficer": "कृष्यधिकारी", "farmer": "कृषकः",
      "mobileOrEmail": "चलदूरभाष-संख्या वा ई-पत्रम्", "password": "कूटशब्दः", "signIn": "प्रविशतु",
      "fullName": "पूर्णनाम", "mobileNumber": "चलदूरभाष-संख्या", "emailOptional": "ई-पत्रम् (ऐच्छिकम्)",
      "createAccount": "उपयोक्तृखातं सृजतु", "designation": "पदनाम", "department": "विभागः",
      "assignedArea": "नियुक्तक्षेत्रम्", "district": "मण्डलम्", "state": "राज्यम्",
      "village": "ग्रामः", "landArea": "भूमिक्षेत्रम् (एकर्)", "farmingType": "कृषिप्रकारः",
      "welcomeBack": "पुनः स्वागतम्, {{name}}!", "accountCreated": "खातं सृष्टम्! स्वागतम्, {{name}}.",
      "invalidCredentials": "अमान्य-प्रवेशविवरणम्", "requiredFields": "कृपया सर्वाणि आवश्यकक्षेत्राणि पूरयन्तु।",
      "demoLoginFailed": "नमूना-प्रवेशः विफलः", "networkError": "जालदोषः",
      "logoutSuccess": "भवान् निर्गतवान्।",
      "officerLoginRequired": "कृष्यधिकारिरूपेण प्रविशतु।", "farmerLoginRequired": "कृषकरूपेण प्रविशतु।",
      "registrationFailed": "पंजीकरणं विफलम्।", "switchedRole": "{{role}} इति परिवर्तितम्"
    },
    "landing": {
      "verifiedPlatform": "प्रमाणित-स्थानीय-कृषि-उत्पाद-मञ्चः", "title": "अन्विष्यतु। प्रमाणीकरोतु। संयोजयतु।",
      "subtitle": "एग्रीफ्लो कृषकान् अधिकरिणश्च प्रमाणित-कृषि-उत्पादानां विवरणं रक्षितुं साहाय्यं करोति।",
      "searchVerifiedProduce": "प्रमाणितोत्पादनम् अन्विष्यतु", "findVerifiedProduce": "उत्पादनम् अन्विष्यतु",
      "quickDiscovery": "क्षेत्रानुसारं त्वरितोत्पादनान्वेषणम्", "cropName": "सस्यनाम",
      "cropPlaceholder": "उदा. पलाण्डुः, रक्तवार्ताकी...", "state": "राज्यम्", "district": "मण्डलम्",
      "allStates": "सर्वाणि राज्यानि", "allDistricts": "सर्वे मण्डलाः", "howItWorks": "एग्रीफ्लो कथं कार्यं करोति",
      "workflowIntro": "स्थानीयकृषिं मुक्तविपणिना सह योजयन्ती पारदर्शिनी प्रमाणीकरणप्रक्रिया।",
      "sihPlatform": "SIH मञ्चः", "tagLine": "अन्विष्यतु। प्रमाणीकरोतु। संयोजयतु।"
    },
    "howItWorks": {
      "farmerSubmission": "कृषक-समर्पणम्",
      "farmerSubmissionDesc": "कृषकाः स्वकृषिक्षेत्रस्य, सस्यावस्थायाः सम्भावितोत्पादनस्य च विवरणं प्रमाणीकरणाय समर्पयन्ति।",
      "officerVerification": "अधिकारि-प्रमाणीकरणम्",
      "officerVerificationDesc": "स्थानीयाः कृष्यधिकारिणः क्षेत्रावलोकनं कृत्वा उत्पादनानि प्रमाणीकुर्वन्ति।",
      "publicDiscovery": "सार्वजनिकान्वेषणं सम्पर्कश्च",
      "publicDiscoveryDesc": "क्रेतारः विना प्रवेशबाधया सस्य-मण्डल-परिमाणानुसारं प्रमाणितोत्पादनानि प्राप्नुवन्ति।"
    },
    "roles": {
      "farmers": "कृषकेभ्यः", "officers": "कृष्यधिकारिभ्यः", "buyers": "क्रेतृभ्यः वणिग्भ्यश्च",
      "farmerTitle": "सस्यानां प्रत्यक्षदर्शनम्", "officerTitle": "अधिकारक्षेत्रनियन्त्रणं विश्वासश्च",
      "buyerTitle": "प्रमाणित-आपूर्तेः अन्वेषणम्",
      "farmerItem1": "कृषिविवरणं कृषिक्षेत्रञ्च पञ्जीकरोतु",
      "farmerItem2": "स्थानीयप्रमाणीकरणाय सस्योत्पादनं समर्पयतु",
      "farmerItem3": "प्रत्यक्षस्थितिं पश्यतु: प्रतीक्षारतम् → प्रमाणितम् / निरस्तम्",
      "officerItem1": "स्थानिकप्रमाणितोत्पादनानि साक्षात् योजयतु",
      "officerItem2": "स्वमण्डले कृषकप्रार्थनानां क्षेत्रपरीक्षणं करोतु",
      "officerItem3": "परिमाणम् उपलभ्यताञ्च नवीकरोतु",
      "buyerItem1": "विना प्रवेशेन सद्यः उत्पादनानि पश्यतु",
      "buyerItem2": "राज्य-मण्डल-क्षेत्र-परिमाणानुसारं शोधयतु",
      "buyerItem3": "प्रमाणितविक्रेतृभ्यः साक्षात् क्रयणप्रार्थनां प्रेषयतु"
    },
    "produce": {
      "title": "प्रमाणित-उत्पादनान्वेषणम्",
      "subtitle": "स्थानिक-कृष्यधिकारिभिः प्रमाणितानि उपलब्ध-आगामि-कृषि-उत्पादनानि अन्विष्यन्तु।",
      "searchCropName": "सस्यनाम अन्विष्यतु", "state": "राज्यम्", "district": "मण्डलम्", "areaBlock": "क्षेत्रम् / ब्लॉक",
      "minQty": "न्यूनतमपरिमाणम् (टन्)", "maxQty": "अधिकतमपरिमाणम् (टन्)", "availBefore": "उपलभ्यतादिनाङ्कात् पूर्वम्/दिने",
      "verifiedOnly": "केवलम् प्रमाणितम् (अनुशंसितम्)", "clearFilters": "शोधकानि मार्जयतु",
      "count": "{{count}} प्रमाणितोत्पाद-विवरणं दृश्यते",
      "countPlural": "{{count}} प्रमाणितोत्पाद-विवरणानि दृश्यन्ते",
      "emptyTitle": "उत्पाद-विवरणं न लब्धम्",
      "emptyDescription": "अन्वेषणविस्तारं कुर्वन्तु अथवा शोधकानि अपनयन्तु।",
      "resetAllFilters": "सर्वशोधकानि पुनःस्थापयतु", "autoSynced": "WebSocket द्वारा प्रत्यक्षसमन्वितम्",
      "availableQuantity": "उपलब्धपरिमाणम्", "quality": "गुणवत्ता", "availability": "उपलभ्यता",
      "sourceOfficer": "अधिकारिप्रमाणितम्", "sourceFarmer": "कृषकप्रमाणितम्",
      "verifiedBadge": "✓ प्रमाणितम्", "qualityGrade": "गुणवत्ताश्रेणी", "verificationSource": "प्रमाणीकरणस्रोतः",
      "fieldNotes": "अधिकारिणः क्षेत्रनिरीक्षणटिप्पण्यः",
      "purchaseTitle": "क्रयणप्रार्थनां प्रेषयतु",
      "purchaseSubtitle": "प्रमाणितोत्पादकेन सह सम्पर्कं कर्तुम् आवश्यकतां समर्पयतु।",
      "yourName": "भवतः नाम / संस्था", "contact": "सम्पर्कसंख्या / ई-पत्रम्",
      "requestedQty": "अपेक्षितपरिमाणम्", "message": "सन्देशः / आवश्यकताः", "sendRequest": "क्रयणप्रार्थनां प्रेषयतु",
      "notFound": "उत्पादविवरणं न लब्धम्", "noLogin": "प्रवेशः नावश्यकः", "unitLabel": "मात्रकम्"
    },
    "officer": {
      "portal": "कृष्यधिकारि-प्रवेशद्वारम्", "subtitle": "स्थानिकक्षेत्रोत्पादनानि रक्षतु, कृषकप्रार्थनाः प्रमाणीकरोतु",
      "profile": "विवरणं सम्पादयतु", "totalRecords": "कुल-उत्पादनानि", "totalRecordsHint": "भवतः क्षेत्रे",
      "availableQty": "उपलब्धपरिमाणम्", "availableQtyHint": "प्रमाणितोत्पादनम्", "farmerRequests": "कृषकप्रार्थनाः",
      "pending": "क्षेत्रपरीक्षणं प्रतीक्षते", "verifiedRecords": "प्रमाणितविवरणानि", "verifiedRecordsHint": "क्रेतृभ्यः दृश्यमानम्",
      "queueTitle": "कृषक-प्रमाणीकरण-प्रार्थनाः", "queueSubtitle": "भवतः क्षेत्रे परीक्षणाय प्रतीक्षारताः कृषकाः",
      "queueEmpty": "सर्वं सम्पन्नम्! कापि प्रार्थना न वर्तते।",
      "localProduceTitle": "स्थानिककृषि-उत्पादनानि", "localProduceSubtitle": "भवदधिकारक्षेत्रे प्रकाशितानि उत्पादनानि",
      "addProduce": "+ उत्पादनं योजयतु", "editProduce": "उत्पादनं सम्पादयतु", "addProduceModalTitle": "+ स्थानीयोत्पादनं योजयतु",
      "modalSubtitle": "अधिकारिणा साक्षात् योजितम् उत्पादनं प्रमाणितं मन्यते",
      "savePublish": "संरक्ष्य प्रकाशयतु", "verify": "प्रमाणीकरोतु", "reject": "प्रत्याख्यातु",
      "pendingBadge": "🟡 परीक्षणं प्रतीक्षते", "directOfficerEntry": "अधिकारिणः साक्षात् प्रविष्टिः",
      "markUnavailable": "अनुपलब्धम् इति चिह्नीकरोतु", "markAvailable": "उपलब्धम् इति चिह्नीकरोतु",
      "editProduceAction": "उत्पादनं सम्पादयतु", "deleteProduce": "विवरणम् अपसारयतु",
      "deleteConfirm": "किं भवान् इदं विवरणम् अपसारयितुम् इच्छति?", "rejectTitle": "कृषकप्रार्थनां निरस्यतु",
      "rejectDescription": "कृपया निरसनस्य उचितं कारणं लिखतु",
      "rejectionReason": "निरसनकारणम् / संशोधनमावश्यकम्",
      "rejectionPlaceholder": "उदा. अनुमानितोत्पादनं भूमिक्षेत्रेण सह न सङ्गच्छते; पुनः मापयतु।",
      "confirmRejection": "निरसनं दृढीकरोतु", "fieldInspected": "अधिकारिणा क्षेत्रपरीक्षणं कृत्वा प्रमाणितम्",
      "verificationSuccess": "✓ कृषकप्रविष्टिः प्रमाणीकृता प्रकाशिता च!",
      "rejectionSuccess": "प्रार्थना निरस्ता, कृषकश्च सूचितः।",
      "provideReason": "कृपया निरसनकारणम् उल्लिखतु", "noProduceYet": "भवतः क्षेत्रे अद्यापि किमपि उत्पादनं न योजितम्।",
      "cropCol": "सस्यम्", "qtyCol": "परिमाणम्", "locationCol": "स्थानम्", "availDateCol": "उपलभ्यतादिनाङ्कः",
      "qualityCol": "गुणवत्ता", "sourceCol": "स्रोतः", "statusCol": "स्थितिः", "actionsCol": "कार्याणि",
      "officerRecordedSuccess": "✓ अधिकारिणा साक्षात् योजितं प्रमाणितञ्च!",
      "updateProduceSuccess": "उत्पादनविवरणं नवीकृतम्"
    },
    "farmer": {
      "portal": "कृषक-प्रवेशद्वारम्", "myProfile": "मम कृषिविवरणम्",
      "assignedOfficer": "भवते नियुक्तः स्थानीय-कृष्यधिकारी", "assignedOfficerHint": "प्रार्थनाः अत्र गच्छन्ति",
      "totalSubmissions": "कुलसमर्पणाणि", "pending": "प्रतीक्षारतम्", "verified": "प्रमाणितम् & सक्रियम्",
      "rejected": "प्रत्याख्यातम्", "requestsTitle": "मम सस्यप्रमाणीकरणप्रार्थनाः",
      "requestsSubtitle": "कृष्यधिकारिणः स्थितिं पश्यतु",
      "addCrop": "+ सस्यविवरणं योजयतु", "addCropButton": "+ सस्यं योजयतु", "myCropDetails": "+ कृषि-सस्यविवरणं योजयतु",
      "submittedToOfficer": "समर्पितविवरणं प्रमाणीकरणाय स्थानिकाधिकारिणे प्रेषयिष्यते",
      "submitToOfficer": "स्थानिकाधिकारिणे समर्पयतु", "noCrops": "अद्यापि किमपि सस्यं न समर्पितम्",
      "noCropsDescription": "प्रमाणीकरणाय स्वकृषिविवरणं योजयतु।", "addFirstCrop": "प्रथमं सस्यं योजयतु",
      "pendingStatus": "🟡 परीक्षणं प्रतीक्षते", "verifiedStatus": "🟢 ✓ प्रमाणितम्", "rejectedStatus": "🔴 प्रत्याख्यातम्",
      "expectedHarvest": "सम्भावित-लवनदिनाङ्कः", "cultivatedArea": "कृषिक्षेत्रम्", "expectedYield": "सम्भावितोत्पादनम्",
      "cropStage": "सस्यावस्था", "officerFeedback": "अधिकारिणः प्रतिपुष्टिः:", "submissionSuccess": "✓ सस्यं समर्पितम्! कृष्यधिकारिणे प्रेषितम्।",
      "verificationStatus": "प्रतीक्षारतम् → प्रमाणितम् / प्रत्याख्यातम्", "locationRouting": "स्थानमार्गः (स्थानिकाधिकारिणे)",
      "additionalNotes": "अतिरिक्तकृषितिप्पण्यः", "farmingNotesPlaceholder": "कृषिपद्धतयः, जलसेचनम्, उर्वरकविवरणम्..."
    },
    "profile": {
      "title": "मम विवरणम्", "subtitle": "स्वखातविवरणं कृषितथ्यानि च व्यवस्थापयतु",
      "saveChanges": "परिवर्तनानि संरक्षतु", "fullName": "पूर्णनाम", "village": "ग्रामः",
      "area": "क्षेत्रम् / ब्लॉक", "district": "मण्डलम्", "state": "राज्यम्", "landArea": "भूमिक्षेत्रम्",
      "landUnit": "भूमेः मात्रकम्", "farmingType": "कृषिप्रकारः", "officialEmail": "कार्यालयीयम् ई-पत्रम्",
      "designation": "अधिकारिपदनाम", "department": "विभागः", "contactNumber": "सम्पर्कसंख्या",
      "assignedArea": "नियुक्तक्षेत्रम् / ब्लॉक", "profileUpdated": "विवरणं सफलतया नवीकृतम्"
    },
    "crops": {
      "onion": "पलाण्डुः", "tomato": "रक्तवार्ताकी", "potato": "आलुकम्", "rice": "शालिः / तण्डुलः",
      "wheat": "गोधूमः", "maize": "महाकायः (मक्का)", "carrot": "गृञ्जनकम्", "cabbage": "दलशाकम्",
      "cauliflower": "पुष्पशाकम्", "garlic": "लशुनम्", "ginger": "आर्द्रकम्", "banana": "कदलीफलम्",
      "mango": "आम्रम्", "groundnut": "भूमुद्गः", "sugarcane": "इक्षुः", "cotton": "कार्पासः"
    },
    "produce_types": {
      "tubers": "कन्दमूलानि", "vegetable": "शाकम्", "vegetable_bulbs": "शाकम् / कन्दम्",
      "field_crop": "क्षेत्रसस्यम्", "cereals": "धान्यानि", "fruits": "फलानि",
      "cash_crops": "वाणिज्यसस्यानि", "spices": "उपस्कराः"
    },
    "units": { "tons": "टन्", "quintals": "क्विण्टल्", "kg": "किलोग्राम्", "acres": "एकर्", "hectares": "हेक्टेयर्" },
    "qualities": {
      "gradeA": "श्रेणी A", "gradeB": "श्रेणी B", "gradeC": "श्रेणी C",
      "gradeAPremium": "श्रेणी A (उत्कृष्टम्)", "gradeBStandard": "श्रेणी B (मानकम्)", "gradeCFair": "श्रेणी C (सामान्यम्)"
    },
    "crop_stages": {
      "bulbDevelopment": "कन्दविकासः", "vegetative": "वानस्पतिकवृद्धिः",
      "flowering": "पुष्पोद्गमः", "readyForHarvest": "लवनाय सज्जम्", "preHarvest": "लवनात् पूर्वम्"
    },
    "statuses": {
      "verified": "प्रमाणितम्", "pending": "प्रतीक्षारतम्", "rejected": "प्रत्याख्यातम्",
      "available": "उपलब्धम्", "unavailable": "अनुपलब्धम्"
    },
    "sources": {
      "officerVerified": "अधिकारिप्रमाणितम्", "farmerVerified": "कृषकप्रमाणितम्",
      "directOfficerEntry": "अधिकारिणः साक्षात् प्रविष्टिः"
    },
    "notifications": {
      "newProduceAdded": "🌾 नूतनोत्पादनं योजितम्: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 उत्पादनं नवीकृतम्: {{crop}}",
      "newFarmerSubmission": "📋 कृषकस्य नूतनप्रार्थना: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ सस्यं प्रमाणितम्: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ कृषकप्रार्थना निरस्ता: {{crop}}",
      "purchaseInquiry": "💼 क्रयणप्रार्थना: क्रेत्रा {{qty}} {{unit}} {{crop}} प्रार्थितम्",
      "demoReset": "🔄 नमूना-दत्तांशः पुनःस्थापितः",
      "inquirySent": "✓ क्रयणप्रार्थना उत्पादकाय/अधिकारिणे प्रेषिता!",
      "statusUpdated": "उत्पादस्थितिः नवीकृता", "deleted": "उत्पादविवरणम् अपसारितम्"
    },
    "demo": {
      "controlsTitle": "SIH नमूनानियन्त्रणानि:", "officerBtn": "अधिकारी (रवि कुमारः)",
      "farmerBtn": "कृषकः (कुमारः)", "buyerBtn": "क्रेतृ-दृश्यम्",
      "resetBtn": "पुनःस्थापयतु", "resetConfirm": "किं भवान् प्रारम्भिकस्थितौ पुनःस्थापयितुम् इच्छति?"
    }
  },
  "ne": {
    "lang": { "name": "Nepali", "nativeName": "नेपाली", "code": "ne", "dir": "ltr" },
    "common": {
      "language": "भाषा", "login": "लगइन", "register": "दर्ता", "logout": "लगआउट",
      "dashboard": "ड्यासबୋर्ड", "profile": "प्रोफाइल", "save": "बचत गर्नुहोस्", "cancel": "रद्द गर्नुहोस्",
      "close": "बन्द गर्नुहोस्", "submit": "बुझाउनुहोस्", "refresh": "ताजा गर्नुहोस्", "search": "खोज्नुहोस्",
      "clearFilters": "फिल्टरहरू हटाउनुहोस्", "loading": "लोड हुँदैछ...", "viewDetails": "विवरण हेर्नुहोस्",
      "allStates": "सबै राज्यहरू", "allDistricts": "सबै जिल्लाहरू", "allAreas": "सबै क्षेत्रहरू",
      "verified": "प्रमाणित", "pending": "प्रतीक्षारत", "rejected": "अस्वीकृत",
      "available": "उपलब्ध", "unavailable": "अनुपलब्ध", "yes": "हो", "no": "होइन",
      "continue": "जारी राख्नुहोस्", "send": "पठाउनुहोस्", "back": "पछाडि", "next": "अर्को",
      "previous": "अघिल्लो", "edit": "सम्पादन", "delete": "मेटाउनुहोस्", "status": "स्थिति",
      "role": "भूमिका", "user": "प्रयोगकर्ता", "liveSync": "प्रत्यक्ष सिंक", "reconnecting": "पुनः जोडिँदैछ...",
      "reset": "रिसेट", "actions": "कार्यहरू", "crop": "बाली", "quantity": "मात्रा",
      "location": "स्थान", "date": "मिति", "notes": "टिप्पणीहरू"
    },
    "navigation": {
      "home": "गृहपृष्ठ", "viewProduce": "उत्पादनहरू हेर्नुहोस्", "officerPortal": "अधिकारी पोर्टल",
      "farmerPortal": "किसान पोर्टल", "dashboard": "ड्यासबୋर्ड", "profile": "प्रोफाइल",
      "requests": "अनुरोधहरू", "addProduce": "उत्पादन थप्नुहोस्", "addCrop": "बाली थप्नुहोस्",
      "myRequests": "मेरा अनुरोधहरू", "farmerRequests": "किसानका अनुरोधहरू",
      "liveSync": "प्रत्यक्ष सिंक", "publicBuyerView": "सार्वजनिक खरिदकर्ता दृश्य"
    },
    "auth": {
      "roleSelector": "आफ्नो भूमिका छान्नुहोस्", "agricultureOfficer": "कृषि अधिकारी", "farmer": "किसान",
      "mobileOrEmail": "मोबाइल नम्बर वा इमेल", "password": "पासवर्ड", "signIn": "साइन इन",
      "fullName": "पूरा नाम", "mobileNumber": "मोबाइल नम्बर", "emailOptional": "इमेल (वैकल्पिक)",
      "createAccount": "खाता बनाउनुहोस्", "designation": "पद", "department": "विभाग",
      "assignedArea": "तोकिएको क्षेत्र", "district": "जिल्ला", "state": "राज्य",
      "village": "गाउँ", "landArea": "जग्गाको क्षेत्रफल (एकर)", "farmingType": "खेतीको प्रकार",
      "welcomeBack": "पुनः स्वागत छ, {{name}}!", "accountCreated": "खाता सिर्जना भयो! स्वागत छ, {{name}}.",
      "invalidCredentials": "अमान्य लगइन विवरण", "requiredFields": "कृपया सबै आवश्यक विवरणहरू भर्नुहोस्।",
      "demoLoginFailed": "डेमो लगइन असफल भयो", "networkError": "नेटवर्क त्रुटि",
      "logoutSuccess": "तपाईं सफलतापूर्वक साइन आउट हुनुभयो।",
      "officerLoginRequired": "अधिकारी पोर्टलका लागि कृषि अधिकारीको रूपमा लगइन गर्नुहोस्।",
      "farmerLoginRequired": "किसान पोर्टलका लागि किसानको रूपमा लगइन गर्नुहोस्।",
      "registrationFailed": "दर्ता असफल भयो। कृपया विवरण जाँच्नुहोस्।", "switchedRole": "{{role}} मा परिवर्तन गरियो"
    },
    "landing": {
      "verifiedPlatform": "प्रमाणित स्थानीय कृषि उत्पादन मञ्च", "title": "खोज्नुहोस्। प्रमाणित गर्नुहोस्। जोडिनुहोस्।",
      "subtitle": "एग्रीफ्लोले किसान र कृषि अधिकारीहरूलाई स्थानीय उत्पादनको प्रमाणित जानकारी राख्न मद्दत गर्दछ।",
      "searchVerifiedProduce": "प्रमाणित उत्पादन खोज्नुहोस्", "findVerifiedProduce": "उत्पादन पत्ता लगाउनुहोस्",
      "quickDiscovery": "क्षेत्र अनुसार छिटो उत्पादन खोज", "cropName": "बालीको नाम",
      "cropPlaceholder": "जस्तै: प्याज, गोलभेंडा...", "state": "राज्य", "district": "जिल्ला",
      "allStates": "सबै राज्यहरू", "allDistricts": "सबै जिल्लाहरू", "howItWorks": "एग्रीफ्लो कसरी काम गर्छ",
      "workflowIntro": "स्थानीय कृषिलाई खुला बजारसँग जोड्ने पारदर्शी प्रमाणीकरण कार्यप्रणाली।",
      "sihPlatform": "SIH मञ्च", "tagLine": "खोज्नुहोस्। प्रमाणित गर्नुहोस्। जोडिनुहोस्।"
    },
    "howItWorks": {
      "farmerSubmission": "किसानको प्रविष्टि",
      "farmerSubmissionDesc": "किसानहरूले आफ्नो खेती, जग्गा र सम्भावित उत्पादन स्थानीय प्रमाणीकरणका लागि पेश गर्छन्।",
      "officerVerification": "अधिकारी प्रमाणीकरण",
      "officerVerificationDesc": "स्थानीय कृषि अधिकारीहरूले खेतको निरीक्षण गरी उत्पादन प्रमाणित गर्छन्।",
      "publicDiscovery": "सार्वजनिक खोज र सम्पर्क",
      "publicDiscoveryDesc": "खरिदकर्ताहरूले लगइन नगरी सिधै प्रमाणित उत्पादनहरू फेला पार्न सक्छन्।"
    },
    "roles": {
      "farmers": "किसानहरूका लागि", "officers": "कृषि अधिकारीहरूका लागि", "buyers": "खरिदकर्ता तथा व्यापारीहरूका लागि",
      "farmerTitle": "बालीको प्रत्यक्ष पहुँच", "officerTitle": "क्षेत्राधिकार नियन्त्रण र विश्वास",
      "buyerTitle": "प्रमाणित आपूर्तिको खोज",
      "farmerItem1": "कृषि प्रोफाइल र जग्गा दर्ता गर्नुहोस्",
      "farmerItem2": "स्थानीय प्रमाणीकरणका लागि आगामी उत्पादन पेश गर्नुहोस्",
      "farmerItem3": "प्रत्यक्ष स्थिति थाहा पाउनुहोस्: प्रतीक्षारत → प्रमाणित / अस्वीकृत",
      "officerItem1": "स्थानीय क्षेत्रका प्रमाणित उत्पादनहरू सिधै थप्नुहोस्",
      "officerItem2": "आफ्नो क्षेत्रका किसानका अनुरोधहरूको स्थलगत प्रमाणीकरण गर्नुहोस्",
      "officerItem3": "मात्रा र उपलब्धता अद्यावधिक गर्नुहोस्",
      "buyerItem1": "लगइन बिना नै तुरुन्त उत्पादन खोज्नुहोस्",
      "buyerItem2": "राज्य, जिल्ला, क्षेत्र र मात्रा अनुसार फिल्टर गर्नुहोस्",
      "buyerItem3": "प्रमाणित उत्पादकहरूलाई सिधै खरिद सोधपुछ पठाउनुहोस्"
    },
    "produce": {
      "title": "प्रमाणित उत्पादन खोज",
      "subtitle": "स्थानीय कृषि अधिकारीहरूले प्रमाणित गरेका उपलब्ध र आगामी कृषि उत्पादनहरू खोज्नुहोस्।",
      "searchCropName": "बालीको नाम खोज्नुहोस्", "state": "राज्य", "district": "जिल्ला", "areaBlock": "क्षेत्र / ब्लक",
      "minQty": "न्यूनतम मात्रा (टन)", "maxQty": "अधिकतम मात्रा (टन)", "availBefore": "उपलब्धता मिति भित्र/सम्म",
      "verifiedOnly": "प्रमाणित मात्र (सिफारिस गरिएको)", "clearFilters": "फिल्टरहरू हटाउनुहोस्",
      "count": "{{count}} प्रमाणित उत्पादन रेकर्ड देखाइएको छ",
      "countPlural": "{{count}} प्रमाणित उत्पादन रेकर्डहरू देखाइएका छन्",
      "emptyTitle": "कुनै उत्पादन रेकर्ड फेला परेन",
      "emptyDescription": "आफ्नो खोजको दायरा बढाउनुहोस् वा फिल्टरहरू हटाउनुहोस्।",
      "resetAllFilters": "सबै फिल्टर रिसेट गर्नुहोस्", "autoSynced": "WebSocket मार्फत प्रत्यक्ष सिंक",
      "availableQuantity": "उपलब्ध मात्रा", "quality": "गुणस्तर", "availability": "उपलब्धता",
      "sourceOfficer": "अधिकारी प्रमाणित", "sourceFarmer": "किसान प्रमाणित",
      "verifiedBadge": "✓ प्रमाणित", "qualityGrade": "गुणस्तर ग्रेड", "verificationSource": "प्रमाणीकरण स्रोत",
      "fieldNotes": "अधिकारीको स्थलगत निरीक्षण टिप्पणीहरू",
      "purchaseTitle": "खरिद सोधपुछ / माग पठाउनुहोस्",
      "purchaseSubtitle": "प्रमाणित उत्पादक वा स्थानीय अधिकारीसँग सिधै जोडिन आफ्नो आवश्यकता पेश गर्नुहोस्।",
      "yourName": "तपाईंको नाम / कम्पनी", "contact": "सम्पर्क नम्बर / इमेल",
      "requestedQty": "माग गरिएको मात्रा", "message": "सन्देश / आवश्यकताहरू", "sendRequest": "खरिद अनुरोध पठाउनुहोस्",
      "notFound": "उत्पादन रेकर्ड फेला परेन", "noLogin": "लगइन आवश्यक छैन", "unitLabel": "इकाई"
    },
    "officer": {
      "portal": "कृषि अधिकारी पोर्टल", "subtitle": "स्थानीय उत्पादन व्यवस्थापन गर्नुहोस्, किसानका आवेदनहरू प्रमाणित गर्नुहोस्",
      "profile": "प्रोफाइल सम्पादन", "totalRecords": "कुल रेकर्डहरू", "totalRecordsHint": "तपाईंको क्षेत्रमा",
      "availableQty": "उपलब्ध मात्रा", "availableQtyHint": "प्रमाणित उत्पादन", "farmerRequests": "किसानका अनुरोधहरू",
      "pending": "स्थलगत प्रमाणीकरण बाँकी", "verifiedRecords": "प्रमाणित रेकर्डहरू", "verifiedRecordsHint": "खरिदकर्ताहरूका लागि उपलब्ध",
      "queueTitle": "किसान प्रमाणीकरण अनुरोधहरू", "queueSubtitle": "तपाईंको क्षेत्रमा स्थलगत प्रमाणीकरणको पर्खाइमा रहेका किसानहरू",
      "queueEmpty": "सबै काम सम्पन्न! कुनै पनि आवेदन बाँकी छैन।",
      "localProduceTitle": "स्थानीय क्षेत्रको कृषि उत्पादन", "localProduceSubtitle": "तपाईंको कार्यक्षेत्रमा प्रकाशित उत्पादनहरू",
      "addProduce": "+ उत्पादन थप्नुहोस्", "editProduce": "उत्पादन सम्पादन", "addProduceModalTitle": "+ स्थानीय उत्पादन थप्नुहोस्",
      "modalSubtitle": "अधिकारीले सिधै प्रविष्टि गरेको उत्पादन प्रमाणित मानिनेछ",
      "savePublish": "बचत र प्रकाशित गर्नुहोस्", "verify": "प्रमाणित गर्नुहोस्", "reject": "अस्वीकार गर्नुहोस्",
      "pendingBadge": "🟡 प्रमाणीकरण बाँकी", "directOfficerEntry": "अधिकारीको प्रत्यक्ष प्रविष्टि",
      "markUnavailable": "अनुपलब्ध चिन्ह लगाउनुहोस्", "markAvailable": "उपलब्ध चिन्ह लगाउनुहोस्",
      "editProduceAction": "उत्पादन सम्पादन", "deleteProduce": "रेकर्ड मेटाउनुहोस्",
      "deleteConfirm": "के तपाईं साँच्चै यो रेकर्ड मेटाउन चाहनुहुन्छ?", "rejectTitle": "किसान अनुरोध अस्वीकार गर्नुहोस्",
      "rejectDescription": "कृपया अस्वीकार गर्नुको उचित कारण खुलाउनुहोस्",
      "rejectionReason": "अस्वीकारको कारण / आवश्यक सुधार",
      "rejectionPlaceholder": "जस्तै: अनुमानित उत्पादन जग्गाको क्षेत्रफलसँग मेल खाँदैन; कृपया पुनः नाप्नुहोस्।",
      "confirmRejection": "अस्वीकार पुष्टि गर्नुहोस्", "fieldInspected": "अधिकारीद्वारा स्थलगत निरीक्षण गरी प्रमाणित",
      "verificationSuccess": "✓ किसानको प्रविष्टि प्रमाणित भई सार्वजनिक दृश्यमा प्रकाशित भयो!",
      "rejectionSuccess": "अनुरोध अस्वीकार गरियो र किसानलाई जानकारी दिइयो।",
      "provideReason": "कृपया अस्वीकारको कारण खुलाउनुहोस्", "noProduceYet": "तपाईंको क्षेत्रमा हालसम्म कुनै उत्पादन दर्ता भएको छैन।",
      "cropCol": "बाली", "qtyCol": "मात्रा", "locationCol": "स्थान", "availDateCol": "उपलब्धता मिति",
      "qualityCol": "गुणस्तर", "sourceCol": "स्रोत", "statusCol": "स्थिति", "actionsCol": "कार्यहरू",
      "officerRecordedSuccess": "✓ अधिकारीद्वारा सिधै दर्ता र प्रमाणित गरियो!",
      "updateProduceSuccess": "उत्पादन सफलतापूर्वक अद्यावधिक भयो"
    },
    "farmer": {
      "portal": "किसान पोर्टल", "myProfile": "मेरो कृषि प्रोफाइल",
      "assignedOfficer": "तपाईंलाई तोकिएका स्थानीय कृषि अधिकारी", "assignedOfficerHint": "आवेदनहरू यहाँ पठाइन्छ",
      "totalSubmissions": "कुल आवेदनहरू", "pending": "प्रतीक्षारत", "verified": "प्रमाणित र सक्रिय",
      "rejected": "अस्वीकृत", "requestsTitle": "मेरा बाली प्रमाणीकरण अनुरोधहरू",
      "requestsSubtitle": "स्थानीय कृषि अधिकारीबाट स्थिति थाहा पाउनुहोस्",
      "addCrop": "+ बाली विवरण थप्नुहोस्", "addCropButton": "+ बाली थप्नुहोस्", "myCropDetails": "+ खेती गरिएको बाली विवरण थप्नुहोस्",
      "submittedToOfficer": "पेश गरिएका विवरणहरू प्रमाणीकरणका लागि स्थानीय अधिकारीकहाँ पठाइनेछ",
      "submitToOfficer": "स्थानीय अधिकारीलाई बुझाउनुहोस्", "noCrops": "अहिलेसम्म कुनै बाली दर्ता गरिएको छैन",
      "noCropsDescription": "स्थानीय प्रमाणीकरणका लागि आफ्नो वर्तमान खेतीको विवरण थप्नुहोस्।", "addFirstCrop": "पहिलो बाली थप्नुहोस्",
      "pendingStatus": "🟡 प्रमाणीकरण बाँकी", "verifiedStatus": "🟢 ✓ प्रमाणित", "rejectedStatus": "🔴 अस्वीकृत",
      "expectedHarvest": "अनुमानित फसल मिति", "cultivatedArea": "खेती गरिएको क्षेत्रफल", "expectedYield": "अनुमानित उत्पादन",
      "cropStage": "बालीको अवस्था", "officerFeedback": "अधिकारीको प्रतिक्रिया:", "submissionSuccess": "✓ बाली पेश भयो! प्रमाणीकरणका लागि कृषि अधिकारीकहाँ पठाइयो।",
      "verificationStatus": "प्रतीक्षारत → प्रमाणित / अस्वीकृत", "locationRouting": "स्थान मार्ग (स्थानीय अधिकारीका लागि)",
      "additionalNotes": "थप कृषि टिप्पणीहरू", "farmingNotesPlaceholder": "खेतीका तरिकाहरू, सिँचाइ, मलको विवरण..."
    },
    "profile": {
      "title": "मेरो प्रोफाइल", "subtitle": "आफ्नो खाता र कृषिको विवरण व्यवस्थापन गर्नुहोस्",
      "saveChanges": "परिवर्तनहरू बचत गर्नुहोस्", "fullName": "पूरा नाम", "village": "गाउँ",
      "area": "क्षेत्र / ब्लक", "district": "जिल्ला", "state": "राज्य", "landArea": "जग्गाको क्षेत्रफल",
      "landUnit": "जग्गाको इकाई", "farmingType": "खेतीको प्रकार", "officialEmail": "सरकारी इमेल",
      "designation": "अधिकारी पद", "department": "विभाग", "contactNumber": "सम्पर्क नम्बर",
      "assignedArea": "तोकिएको क्षेत्र / ब्लक", "profileUpdated": "प्रोफाइल सफलतापूर्वक अद्यावधिक भयो"
    },
    "crops": {
      "onion": "प्याज", "tomato": "गोलभेंडा", "potato": "आलु", "rice": "धान / चामल",
      "wheat": "गहुँ", "maize": "मकै", "carrot": "गाजर", "cabbage": "बन्दागोभी",
      "cauliflower": "काउली", "garlic": "लसुन", "ginger": "अदुवा", "banana": "केरा",
      "mango": "आँप", "groundnut": "बदाम", "sugarcane": "उखु", "cotton": "कपास"
    },
    "produce_types": {
      "tubers": "कन्दमूल", "vegetable": "तरकारी", "vegetable_bulbs": "तरकारी / कन्दमूल",
      "field_crop": "खेतको बाली", "cereals": "अन्न", "fruits": "फलफूल",
      "cash_crops": "नगदे बाली", "spices": "मसला"
    },
    "units": { "tons": "टन", "quintals": "क्विन्टल", "kg": "किलोग्राम", "acres": "एकर", "hectares": "हेक्टर" },
    "qualities": {
      "gradeA": "ग्रेड A", "gradeB": "ग्रेड B", "gradeC": "ग्रेड C",
      "gradeAPremium": "ग्रेड A (उत्कृष्ट)", "gradeBStandard": "ग्रेड B (मानक)", "gradeCFair": "ग्रेड C (साधारण)"
    },
    "crop_stages": {
      "bulbDevelopment": "गाँठो विकास", "vegetative": "वानस्पतिक वृद्धि",
      "flowering": "फूल फुल्ने अवस्था", "readyForHarvest": "फसलका लागि तयार", "preHarvest": "फसल पूर्व"
    },
    "statuses": {
      "verified": "प्रमाणित", "pending": "प्रतीक्षारत", "rejected": "अस्वीकृत",
      "available": "उपलब्ध", "unavailable": "अनुपलब्ध"
    },
    "sources": {
      "officerVerified": "अधिकारी प्रमाणित", "farmerVerified": "किसान प्रमाणित",
      "directOfficerEntry": "अधिकारीको प्रत्यक्ष प्रविष्टि"
    },
    "notifications": {
      "newProduceAdded": "🌾 नयाँ उत्पादन थपियो: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 उत्पादन अद्यावधिक भयो: {{crop}}",
      "newFarmerSubmission": "📋 नयाँ किसान बाली आवेदन: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ बाली प्रमाणित भयो: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ किसानको अनुरोध अस्वीकृत: {{crop}}",
      "purchaseInquiry": "💼 खरिद सोधपुछ: खरिदकर्ताले {{qty}} {{unit}} {{crop}} माग गरेका छन्",
      "demoReset": "🔄 डेमो डाटा पुनःसेट भयो",
      "inquirySent": "✓ खरिद सोधपुछ उत्पादक वा अधिकारीलाई पठाइयो!",
      "statusUpdated": "उत्पादन स्थिति अद्यावधिक भयो", "deleted": "उत्पादन रेकर्ड मेटाइयो"
    },
    "demo": {
      "controlsTitle": "SIH डेमो नियन्त्रणहरू:", "officerBtn": "अधिकारी (रवि कुमार)",
      "farmerBtn": "किसान (कुमार)", "buyerBtn": "सार्वजनिक खरिदकर्ता दृश्य",
      "resetBtn": "डेमो रिसेट", "resetConfirm": "के तपाईं डाटाबेसलाई सुरुवाती डेमो स्थितिमा रिसेट गर्न चाहनुहुन्छ?"
    }
  }
}
