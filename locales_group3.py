# -*- coding: utf-8 -*-
"""
Language definitions for AgriFlow - Group 3:
Punjabi (pa), Odia (or), Assamese (as), Urdu (ur - RTL), Sindhi (sd - RTL)
"""

LOCALES_GROUP_3 = {
  "pa": {
    "lang": { "name": "Punjabi", "nativeName": "ਪੰਜਾਬੀ", "code": "pa", "dir": "ltr" },
    "common": {
      "language": "ਭਾਸ਼ਾ", "login": "ਲਾਗਇਨ", "register": "ਰਜਿਸਟਰ", "logout": "ਲਾਗਆਉਟ",
      "dashboard": "ਡੈਸ਼ਬੋਰਡ", "profile": "ਪ੍ਰੋਫਾਈਲ", "save": "ਸੰਭਾਲੋ", "cancel": "ਰੱਦ ਕਰੋ",
      "close": "ਬੰਦ ਕਰੋ", "submit": "ਜਮ੍ਹਾ ਕਰੋ", "refresh": "ਤਾਜ਼ਾ ਕਰੋ", "search": "ਖੋਜੋ",
      "clearFilters": "ਫਿਲਟਰ ਸਾਫ਼ ਕਰੋ", "loading": "ਲੋਡ ਹੋ ਰਿਹਾ ਹੈ...", "viewDetails": "ਵੇਰਵੇ ਦੇਖੋ",
      "allStates": "ਸਾਰੇ ਰਾਜ", "allDistricts": "ਸਾਰੇ ਜ਼ਿਲ੍ਹੇ", "allAreas": "ਸਾਰੇ ਖੇਤਰ",
      "verified": "ਪ੍ਰਮਾਣਿਤ", "pending": "ਬਕਾਇਆ", "rejected": "ਰੱਦ ਕੀਤਾ ਗਿਆ",
      "available": "ਉਪਲਬਧ", "unavailable": "ਨਾ-ਉਪਲਬਧ", "yes": "ਹਾਂ", "no": "ਨਹੀਂ",
      "continue": "ਜਾਰੀ ਰੱਖੋ", "send": "ਭੇਜੋ", "back": "ਪਿੱਛੇ", "next": "ਅੱਗੇ",
      "previous": "ਪਿਛਲਾ", "edit": "ਸੋਧੋ", "delete": "ਮਿਟਾਓ", "status": "ਸਥਿਤੀ",
      "role": "ਭੂਮਿਕਾ", "user": "ਉਪਭੋਗਤਾ", "liveSync": "ਲਾਈਵ ਸਿੰਕ", "reconnecting": "ਮੁੜ ਜੁੜ ਰਿਹਾ ਹੈ...",
      "reset": "ਰੀਸੈੱਟ", "actions": "ਕਾਰਵਾਈਆਂ", "crop": "ਫ਼ਸਲ", "quantity": "ਮਾਤਰਾ",
      "location": "ਸਥਾਨ", "date": "ਮਿਤੀ", "notes": "ਨੋਟਸ"
    },
    "navigation": {
      "home": "ਮੁੱਖ ਪੰਨਾ", "viewProduce": "ਉਤਪਾਦ ਦੇਖੋ", "officerPortal": "ਅਫ਼ਸਰ ਪੋਰਟਲ",
      "farmerPortal": "ਕਿਸਾਨ ਪੋਰਟਲ", "dashboard": "ਡੈਸ਼ਬੋਰਡ", "profile": "ਪ੍ਰੋਫਾਈਲ",
      "requests": "ਬੇਨਤੀਆਂ", "addProduce": "ਉਤਪਾਦ ਸ਼ਾਮਲ ਕਰੋ", "addCrop": "ਫ਼ਸਲ ਸ਼ਾਮਲ ਕਰੋ",
      "myRequests": "ਮੇਰੀਆਂ ਬੇਨਤੀਆਂ", "farmerRequests": "ਕਿਸਾਨ ਬੇਨਤੀਆਂ",
      "liveSync": "ਲਾਈਵ ਸਿੰਕ", "publicBuyerView": "ਜਨਤਕ ਖਰੀਦਦਾਰ ਦ੍ਰਿਸ਼"
    },
    "auth": {
      "roleSelector": "ਆਪਣੀ ਭੂਮਿਕਾ ਚੁਣੋ", "agricultureOfficer": "ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ", "farmer": "ਕਿਸਾਨ",
      "mobileOrEmail": "ਮੋਬਾਈਲ ਨੰਬਰ ਜਾਂ ਈਮੇਲ", "password": "ਪਾਸਵਰਡ", "signIn": "ਸਾਈਨ ਇਨ",
      "fullName": "ਪੂਰਾ ਨਾਮ", "mobileNumber": "ਮੋਬਾਈਲ ਨੰਬਰ", "emailOptional": "ਈਮੇਲ (ਵਿਕਲਪਿਕ)",
      "createAccount": "ਖਾਤਾ ਬਣਾਓ", "designation": "ਅਹੁਦਾ", "department": "ਵਿਭਾਗ",
      "assignedArea": "ਨਿਰਧਾਰਤ ਖੇਤਰ", "district": "ਜ਼ਿਲ੍ਹਾ", "state": "ਰਾਜ",
      "village": "ਪਿੰਡ", "landArea": "ਜ਼ਮੀਨ ਦਾ ਰਕਬਾ (ਏਕੜ)", "farmingType": "ਖੇਤੀ ਦੀ ਕਿਸਮ",
      "welcomeBack": "ਜੀ ਆਇਆਂ ਨੂੰ, {{name}}!", "accountCreated": "ਖਾਤਾ ਬਣ ਗਿਆ! ਜੀ ਆਇਆਂ ਨੂੰ, {{name}}.",
      "invalidCredentials": "ਅਵੈਧ ਲਾਗਇਨ ਵੇਰਵੇ", "requiredFields": "ਕਿਰਪਾ ਕਰਕੇ ਸਾਰੇ ਜ਼ਰੂਰੀ ਖੇਤਰ ਭਰੋ (ਨਾਮ, ਮੋਬਾਈਲ, ਪਾਸਵਰਡ)।",
      "demoLoginFailed": "ਡੈਮੋ ਲਾਗਇਨ ਅਸਫਲ", "networkError": "ਨੈੱਟਵਰਕ ਗਲਤੀ",
      "logoutSuccess": "ਤੁਸੀਂ ਸਫਲਤਾਪੂਰਵਕ ਸਾਈਨ ਆਉਟ ਕਰ ਲਿਆ ਹੈ।",
      "officerLoginRequired": "ਅਫ਼ਸਰ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਲਈ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਵਜੋਂ ਲਾਗਇਨ ਕਰੋ।",
      "farmerLoginRequired": "ਕਿਸਾਨ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਲਈ ਕਿਸਾਨ ਵਜੋਂ ਲਾਗਇਨ ਕਰੋ।",
      "registrationFailed": "ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਅਸਫਲ ਰਹੀ। ਕਿਰਪਾ ਕਰਕੇ ਵੇਰਵਿਆਂ ਦੀ ਜਾਂਚ ਕਰੋ।", "switchedRole": "{{role}} ਵਿੱਚ ਬਦਲਿਆ ਗਿਆ"
    },
    "landing": {
      "verifiedPlatform": "ਪ੍ਰਮਾਣਿਤ ਸਥਾਨਕ ਖੇਤੀ ਉਤਪਾਦ ਪਲੇਟਫਾਰਮ", "title": "ਖੋਜੋ। ਪ੍ਰਮਾਣਿਤ ਕਰੋ। ਜੁੜੋ।",
      "subtitle": "ਐਗਰੀਫਲੋ ਕਿਸਾਨਾਂ ਅਤੇ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰਾਂ ਨੂੰ ਸਥਾਨਕ ਖੇਤੀ ਉਤਪਾਦਾਂ ਦੀ ਪ੍ਰਮਾਣਿਤ ਜਾਣਕਾਰੀ ਰੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ, ਤਾਂ ਜੋ ਖਰੀਦਦਾਰ ਸਥਾਨ, ਫ਼ਸਲ ਅਤੇ ਮਾਤਰਾ ਅਨੁਸਾਰ ਆਸਾਨੀ ਨਾਲ ਉਤਪਾਦ ਲੱਭ ਸਕਣ।",
      "searchVerifiedProduce": "ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦ ਖੋਜੋ", "findVerifiedProduce": "ਉਤਪਾਦ ਲੱਭੋ",
      "quickDiscovery": "ਖੇਤਰ ਅਨੁਸਾਰ ਤੇਜ਼ ਉਤਪਾਦ ਖੋਜ", "cropName": "ਫ਼ਸਲ ਦਾ ਨਾਮ",
      "cropPlaceholder": "ਜਿਵੇਂ: ਪਿਆਜ਼, ਟਮਾਟਰ...", "state": "ਰਾਜ", "district": "ਜ਼ਿਲ੍ਹਾ",
      "allStates": "ਸਾਰੇ ਰਾਜ", "allDistricts": "ਸਾਰੇ ਜ਼ਿਲ੍ਹੇ", "howItWorks": "ਐਗਰੀਫਲੋ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ",
      "workflowIntro": "ਸਥਾਨਕ ਖੇਤੀ ਨੂੰ ਖੁੱਲ੍ਹੀ ਮੰਡੀ ਨਾਲ ਜੋੜਨ ਵਾਲੀ ਇੱਕ ਪਾਰਦਰਸ਼ੀ ਅਤੇ ਸਥਾਨ-ਅਧਾਰਿਤ ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਕਿਰਿਆ।",
      "sihPlatform": "SIH ਪਲੇਟਫਾਰਮ", "tagLine": "ਖੋਜੋ। ਪ੍ਰਮਾਣਿਤ ਕਰੋ। ਜੁੜੋ।"
    },
    "howItWorks": {
      "farmerSubmission": "ਕਿਸਾਨ ਵੱਲੋਂ ਇੰਦਰਾਜ",
      "farmerSubmissionDesc": "ਕਿਸਾਨ ਆਪਣੀ ਸਰਗਰਮ ਖੇਤੀ, ਜ਼ਮੀਨ ਦਾ ਆਕਾਰ ਅਤੇ ਆਉਣ ਵਾਲੇ ਝਾੜ ਦੇ ਵੇਰਵੇ ਸਥਾਨਕ ਤਸਦੀਕ ਲਈ ਦਰਜ ਕਰਦੇ ਹਨ।",
      "officerVerification": "ਅਫ਼ਸਰ ਵੱਲੋਂ ਪੜਤਾਲ",
      "officerVerificationDesc": "ਸਥਾਨਕ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਕਿਸਾਨ ਅਰਜ਼ੀਆਂ ਦੀ ਸਮੀਖਿਆ ਕਰਦੇ ਹਨ, ਮੌਕੇ 'ਤੇ ਜਾਂਚ ਕਰਦੇ ਹਨ ਅਤੇ ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰਦੇ ਹਨ।",
      "publicDiscovery": "ਜਨਤਕ ਖੋਜ ਅਤੇ ਸੰਪਰਕ",
      "publicDiscoveryDesc": "ਖਰੀਦਦਾਰ ਬਿਨਾਂ ਕਿਸੇ ਲਾਗਇਨ ਰੁਕਾਵਟ ਦੇ ਫ਼ਸਲ, ਜ਼ਿਲ੍ਹੇ ਅਤੇ ਮਾਤਰਾ ਦੇ ਅਧਾਰ 'ਤੇ ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦ ਆਸਾਨੀ ਨਾਲ ਲੱਭਦੇ ਹਨ।"
    },
    "roles": {
      "farmers": "ਕਿਸਾਨਾਂ ਲਈ", "officers": "ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰਾਂ ਲਈ", "buyers": "ਖਰੀਦਦਾਰਾਂ ਅਤੇ ਵਪਾਰੀਆਂ ਲਈ",
      "farmerTitle": "ਫ਼ਸਲ ਦੀ ਸਿੱਧੀ ਦਿੱਖ", "officerTitle": "ਅਧਿਕਾਰ ਖੇਤਰ ਨਿਯੰਤਰਣ ਅਤੇ ਭਰੋਸਾ",
      "buyerTitle": "ਪ੍ਰਮਾਣਿਤ ਸਪਲਾਈ ਦੀ ਖੋਜ",
      "farmerItem1": "ਖੇਤੀ ਪ੍ਰੋਫਾਈਲ ਅਤੇ ਕਾਸ਼ਤਯੋਗ ਜ਼ਮੀਨ ਰਜਿਸਟਰ ਕਰੋ",
      "farmerItem2": "ਸਥਾਨਕ ਤਸਦੀਕ ਲਈ ਆਉਣ ਵਾਲੀ ਫ਼ਸਲ ਦਾ ਝਾੜ ਜਮ੍ਹਾ ਕਰੋ",
      "farmerItem3": "ਅਸਲ ਸਮੇਂ ਦੀ ਸਥਿਤੀ ਜਾਣੋ: ਬਕਾਇਆ → ਪ੍ਰਮਾਣਿਤ / ਰੱਦ",
      "officerItem1": "ਸਥਾਨਕ ਖੇਤਰ ਦੇ ਪ੍ਰਮਾਣਿਤ ਖੇਤੀ ਉਤਪਾਦ ਸਿੱਧੇ ਸ਼ਾਮਲ ਕਰੋ",
      "officerItem2": "ਆਪਣੇ ਬਲਾਕ ਦੇ ਕਿਸਾਨਾਂ ਦੀਆਂ ਬੇਨਤੀਆਂ ਦੀ ਫੀਲਡ ਪੜਤਾਲ ਕਰੋ",
      "officerItem3": "ਮਾਤਰਾ ਅਤੇ ਉਪਲਬਧਤਾ ਨੂੰ ਅਪਡੇਟ ਕਰੋ",
      "buyerItem1": "ਬਿਨਾਂ ਲਾਗਇਨ ਦੇ ਤੁਰੰਤ ਉਤਪਾਦ ਲੱਭੋ",
      "buyerItem2": "ਰਾਜ, ਜ਼ਿਲ੍ਹਾ, ਖੇਤਰ ਅਤੇ ਮਾਤਰਾ ਅਨੁਸਾਰ ਫਿਲਟਰ ਕਰੋ",
      "buyerItem3": "ਪ੍ਰਮਾਣਿਤ ਸਪਲਾਇਰਾਂ ਨੂੰ ਸਿੱਧੀ ਖਰੀਦ ਪੁੱਛਗਿੱਛ ਭੇਜੋ"
    },
    "produce": {
      "title": "ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦ ਖੋਜ",
      "subtitle": "ਸਥਾਨਕ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰਾਂ ਦੁਆਰਾ ਪ੍ਰਮਾਣਿਤ ਉਪਲਬਧ ਅਤੇ ਆਉਣ ਵਾਲੇ ਖੇਤੀ ਉਤਪਾਦ ਲੱਭੋ।",
      "searchCropName": "ਫ਼ਸਲ ਦਾ ਨਾਮ ਖੋਜੋ", "state": "ਰਾਜ", "district": "ਜ਼ਿਲ੍ਹਾ", "areaBlock": "ਖੇਤਰ / ਬਲਾਕ",
      "minQty": "ਘੱਟੋ-ਘੱਟ ਮਾਤਰਾ (ਟਨ)", "maxQty": "ਵੱਧ ਤੋਂ ਵੱਧ ਮਾਤਰਾ (ਟਨ)", "availBefore": "ਉਪਲਬਧਤਾ ਮਿਤੀ ਤੱਕ/ਨੂੰ",
      "verifiedOnly": "ਸਿਰਫ਼ ਪ੍ਰਮਾਣਿਤ (ਸਿਫ਼ਾਰਸ਼ੀ)", "clearFilters": "ਫਿਲਟਰ ਸਾਫ਼ ਕਰੋ",
      "count": "{{count}} ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦ ਰਿਕਾਰਡ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ",
      "countPlural": "{{count}} ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦ ਰਿਕਾਰਡ ਦਿਖਾਈ ਦੇ ਰਹੇ ਹਨ",
      "emptyTitle": "ਕੋਈ ਉਤਪਾਦ ਰਿਕਾਰਡ ਨਹੀਂ ਮਿਲਿਆ",
      "emptyDescription": "ਆਪਣੀ ਖੋਜ ਦਾ ਦਾਇਰਾ ਵਧਾਓ ਜਾਂ ਨੇੜਲੇ ਖੇਤਰਾਂ ਦੀਆਂ ਫ਼ਸਲਾਂ ਦੇਖਣ ਲਈ ਫਿਲਟਰ ਸਾਫ਼ ਕਰੋ।",
      "resetAllFilters": "ਸਾਰੇ ਫਿਲਟਰ ਰੀਸੈੱਟ ਕਰੋ", "autoSynced": "WebSocket ਰਾਹੀਂ ਲਾਈਵ ਸਿੰਕ",
      "availableQuantity": "ਉਪਲਬਧ ਮਾਤਰਾ", "quality": "ਗੁਣਵੱਤਾ", "availability": "ਉਪਲਬਧਤਾ",
      "sourceOfficer": "ਅਫ਼ਸਰ ਦੁਆਰਾ ਪ੍ਰਮਾਣਿਤ", "sourceFarmer": "ਕਿਸਾਨ ਦੁਆਰਾ ਪ੍ਰਮਾਣਿਤ",
      "verifiedBadge": "✓ ਪ੍ਰਮਾਣਿਤ", "qualityGrade": "ਗੁਣਵੱਤਾ ਗ੍ਰੇਡ", "verificationSource": "ਤਸਦੀਕ ਸਰੋਤ",
      "fieldNotes": "ਅਫ਼ਸਰ ਫੀਲਡ ਪੜਤਾਲ ਨੋਟਸ",
      "purchaseTitle": "ਖਰੀਦ ਪੁੱਛਗਿੱਛ / ਮੰਗ ਪੱਤਰ ਭੇਜੋ",
      "purchaseSubtitle": "ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦਕ / ਸਥਾਨਕ ਅਫ਼ਸਰ ਨਾਲ ਸਿੱਧਾ ਜੁੜਨ ਲਈ ਆਪਣੀ ਲੋੜ ਜਮ੍ਹਾ ਕਰੋ।",
      "yourName": "ਤੁਹਾਡਾ ਨਾਮ / ਕੰਪਨੀ", "contact": "ਸੰਪਰਕ ਨੰਬਰ / ਈਮੇਲ",
      "requestedQty": "ਲੋੜੀਂਦੀ ਮਾਤਰਾ", "message": "ਸੁਨੇਹਾ / ਲੋੜਾਂ", "sendRequest": "ਖਰੀਦ ਬੇਨਤੀ ਭੇਜੋ",
      "notFound": "ਉਤਪਾਦ ਰਿਕਾਰਡ ਨਹੀਂ ਮਿਲਿਆ", "noLogin": "ਲਾਗਇਨ ਦੀ ਲੋੜ ਨਹੀਂ", "unitLabel": "ਇਕਾਈ"
    },
    "officer": {
      "portal": "ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਪੋਰਟਲ", "subtitle": "ਸਥਾਨਕ ਅਧਿਕਾਰ ਖੇਤਰ ਦੇ ਉਤਪਾਦ ਸੰਭਾਲੋ, ਕਿਸਾਨ ਅਰਜ਼ੀਆਂ ਦੀ ਤਸਦੀਕ ਕਰੋ",
      "profile": "ਪ੍ਰੋਫਾਈਲ ਸੋਧੋ", "totalRecords": "ਕੁੱਲ ਰਿਕਾਰਡ", "totalRecordsHint": "ਤੁਹਾਡੇ ਖੇਤਰ ਵਿੱਚ",
      "availableQty": "ਉਪਲਬਧ ਮਾਤਰਾ", "availableQtyHint": "ਪ੍ਰਮਾਣਿਤ ਉਤਪਾਦ", "farmerRequests": "ਕਿਸਾਨ ਬੇਨਤੀਆਂ",
      "pending": "ਫੀਲਡ ਪੜਤਾਲ ਬਕਾਇਆ", "verifiedRecords": "ਪ੍ਰਮਾਣਿਤ ਰਿਕਾਰਡ", "verifiedRecordsHint": "ਖਰੀਦਦਾਰਾਂ ਲਈ ਉਪਲਬਧ",
      "queueTitle": "ਕਿਸਾਨ ਤਸਦੀਕ ਬੇਨਤੀਆਂ", "queueSubtitle": "ਤੁਹਾਡੇ ਖੇਤਰ ਵਿੱਚ ਫੀਲਡ ਪੜਤਾਲ ਦੀ ਉਡੀਕ ਕਰ ਰਹੇ ਕਿਸਾਨ",
      "queueEmpty": "ਸਾਰਾ ਕੰਮ ਮੁਕੰਮਲ! ਕੋਈ ਬਕਾਇਆ ਬੇਨਤੀ ਨਹੀਂ ਹੈ।",
      "localProduceTitle": "ਸਥਾਨਕ ਖੇਤਰ ਦੇ ਖੇਤੀ ਉਤਪਾਦ", "localProduceSubtitle": "ਤੁਹਾਡੇ ਅਧਿਕਾਰ ਖੇਤਰ ਵਿੱਚ ਦਰਜ ਉਤਪਾਦ",
      "addProduce": "+ ਉਤਪਾਦ ਸ਼ਾਮਲ ਕਰੋ", "editProduce": "ਉਤਪਾਦ ਸੋਧੋ", "addProduceModalTitle": "+ ਸਥਾਨਕ ਉਤਪਾਦ ਸ਼ਾਮਲ ਕਰੋ",
      "modalSubtitle": "ਅਫ਼ਸਰ ਦੁਆਰਾ ਸਿੱਧਾ ਦਰਜ ਕੀਤਾ ਉਤਪਾਦ ਪ੍ਰਮਾਣਿਤ ਮੰਨਿਆ ਜਾਵੇਗਾ",
      "savePublish": "ਸੰਭਾਲੋ ਅਤੇ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰੋ", "verify": "ਤਸਦੀਕ ਕਰੋ", "reject": "ਰੱਦ ਕਰੋ",
      "pendingBadge": "🟡 ਪੜਤਾਲ ਬਕਾਇਆ", "directOfficerEntry": "ਅਫ਼ਸਰ ਦਾ ਸਿੱਧਾ ਇੰਦਰਾਜ",
      "markUnavailable": "ਨਾ-ਉਪਲਬਧ ਚਿੰਨ੍ਹਿਤ ਕਰੋ", "markAvailable": "ਉਪਲਬਧ ਚਿੰਨ੍ਹਿਤ ਕਰੋ",
      "editProduceAction": "ਉਤਪਾਦ ਸੋਧੋ", "deleteProduce": "ਰਿਕਾਰਡ ਮਿਟਾਓ",
      "deleteConfirm": "ਕੀ ਤੁਸੀਂ ਯਕੀਨੀ ਤੌਰ 'ਤੇ ਇਹ ਰਿਕਾਰਡ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?", "rejectTitle": "ਕਿਸਾਨ ਬੇਨਤੀ ਰੱਦ ਕਰੋ",
      "rejectDescription": "ਕਿਰਪਾ ਕਰਕੇ ਰੱਦ ਕਰਨ ਦਾ ਢੁਕਵਾਂ ਕਾਰਨ ਦੱਸੋ",
      "rejectionReason": "ਰੱਦ ਕਰਨ ਦਾ ਕਾਰਨ / ਲੋੜੀਂਦੀ ਸੋਧ",
      "rejectionPlaceholder": "ਜਿਵੇਂ: ਅਨੁਮਾਨਿਤ ਝਾੜ ਜ਼ਮੀਨ ਦੇ ਰਕਬੇ ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦਾ; ਕਿਰਪਾ ਕਰਕੇ ਮੁੜ ਮਾਪੋ।",
      "confirmRejection": "ਰੱਦ ਕਰਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ", "fieldInspected": "ਅਫ਼ਸਰ ਦੁਆਰਾ ਮੌਕੇ 'ਤੇ ਜਾਂਚ ਕਰਕੇ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਗਿਆ",
      "verificationSuccess": "✓ ਕਿਸਾਨ ਇੰਦਰਾਜ ਪ੍ਰਮਾਣਿਤ ਹੋ ਗਿਆ ਅਤੇ ਜਨਤਕ ਤੌਰ 'ਤੇ ਪ੍ਰਕਾਸ਼ਿਤ ਹੋ ਗਿਆ!",
      "rejectionSuccess": "ਬੇਨਤੀ ਰੱਦ ਕਰ ਦਿੱਤੀ ਗਈ ਅਤੇ ਕਿਸਾਨ ਨੂੰ ਸੂਚਿਤ ਕਰ ਦਿੱਤਾ ਗਿਆ।",
      "provideReason": "ਕਿਰਪਾ ਕਰਕੇ ਰੱਦ ਕਰਨ ਦਾ ਕਾਰਨ ਦਿਓ", "noProduceYet": "ਤੁਹਾਡੇ ਖੇਤਰ ਵਿੱਚ ਅਜੇ ਕੋਈ ਉਤਪਾਦ ਦਰਜ ਨਹੀਂ ਕੀਤਾ ਗਿਆ।",
      "cropCol": "ਫ਼ਸਲ", "qtyCol": "ਮਾਤਰਾ", "locationCol": "ਸਥਾਨ", "availDateCol": "ਉਪਲਬਧਤਾ ਮਿਤੀ",
      "qualityCol": "ਗੁਣਵੱਤਾ", "sourceCol": "ਸਰੋਤ", "statusCol": "ਸਥਿਤੀ", "actionsCol": "ਕਾਰਵਾਈਆਂ",
      "officerRecordedSuccess": "✓ ਅਫ਼ਸਰ ਦੁਆਰਾ ਸਿੱਧਾ ਦਰਜ ਅਤੇ ਪ੍ਰਮਾਣਿਤ ਕੀਤਾ ਗਿਆ!",
      "updateProduceSuccess": "ਉਤਪਾਦ ਸਫਲਤਾਪੂਰਵਕ ਅਪਡੇਟ ਕੀਤਾ ਗਿਆ"
    },
    "farmer": {
      "portal": "ਕਿਸਾਨ ਪੋਰਟਲ", "myProfile": "ਮੇਰੀ ਖੇਤੀ ਪ੍ਰੋਫਾਈਲ",
      "assignedOfficer": "ਤੁਹਾਡੇ ਨਿਯੁਕਤ ਸਥਾਨਕ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ", "assignedOfficerHint": "ਅਰਜ਼ੀਆਂ ਇੱਥੇ ਭੇਜੀਆਂ ਜਾਂਦੀਆਂ ਹਨ",
      "totalSubmissions": "ਕੁੱਲ ਅਰਜ਼ੀਆਂ", "pending": "ਬਕਾਇਆ", "verified": "ਪ੍ਰਮਾਣਿਤ ਅਤੇ ਸਰਗਰਮ",
      "rejected": "ਰੱਦ ਕੀਤਾ ਗਿਆ", "requestsTitle": "ਮੇਰੀਆਂ ਫ਼ਸਲ ਤਸਦੀਕ ਬੇਨਤੀਆਂ",
      "requestsSubtitle": "ਆਪਣੇ ਸਥਾਨਕ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਤੋਂ ਸਥਿਤੀ ਜਾਣੋ",
      "addCrop": "+ ਫ਼ਸਲ ਦੇ ਵੇਰਵੇ ਸ਼ਾਮਲ ਕਰੋ", "addCropButton": "+ ਫ਼ਸਲ ਸ਼ਾਮਲ ਕਰੋ", "myCropDetails": "+ ਖੇਤੀ ਫ਼ਸਲ ਦੇ ਵੇਰਵੇ ਸ਼ਾਮਲ ਕਰੋ",
      "submittedToOfficer": "ਜਮ੍ਹਾ ਕੀਤੇ ਵੇਰਵੇ ਤਸਦੀਕ ਲਈ ਤੁਹਾਡੇ ਸਥਾਨਕ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਨੂੰ ਭੇਜੇ ਜਾਣਗੇ",
      "submitToOfficer": "ਸਥਾਨਕ ਅਫ਼ਸਰ ਨੂੰ ਜਮ੍ਹਾ ਕਰੋ", "noCrops": "ਅਜੇ ਤੱਕ ਕੋਈ ਫ਼ਸਲ ਜਮ੍ਹਾ ਨਹੀਂ ਕੀਤੀ ਗਈ",
      "noCropsDescription": "ਸਥਾਨਕ ਤਸਦੀਕ ਲਈ ਆਪਣੀ ਮੌਜੂਦਾ ਫ਼ਸਲ ਦੇ ਵੇਰਵੇ ਸ਼ਾਮਲ ਕਰੋ।", "addFirstCrop": "ਪਹਿਲੀ ਫ਼ਸਲ ਸ਼ਾਮਲ ਕਰੋ",
      "pendingStatus": "🟡 ਪੜਤਾਲ ਬਕਾਇਆ", "verifiedStatus": "🟢 ✓ ਪ੍ਰਮਾਣਿਤ", "rejectedStatus": "🔴 ਰੱਦ ਕੀਤਾ ਗਿਆ",
      "expectedHarvest": "ਅਨੁਮਾਨਿਤ ਵਾਢੀ ਮਿਤੀ", "cultivatedArea": "ਕਾਸ਼ਤਯੋਗ ਰਕਬਾ", "expectedYield": "ਅਨੁਮਾਨਿਤ ਝਾੜ",
      "cropStage": "ਫ਼ਸਲ ਦਾ ਪੜਾਅ", "officerFeedback": "ਅਫ਼ਸਰ ਦੀ ਫੀਡਬੈਕ:", "submissionSuccess": "✓ ਫ਼ਸਲ ਜਮ੍ਹਾ ਹੋ ਗਈ! ਤਸਦੀਕ ਲਈ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਨੂੰ ਭੇਜੀ ਗਈ।",
      "verificationStatus": "ਬਕਾਇਆ → ਪ੍ਰਮਾਣਿਤ / ਰੱਦ", "locationRouting": "ਸਥਾਨ ਰੂਟਿੰਗ (ਸਥਾਨਕ ਅਫ਼ਸਰ ਲਈ)",
      "additionalNotes": "ਵਾਧੂ ਖੇਤੀ ਨੋਟਸ", "farmingNotesPlaceholder": "ਖੇਤੀ ਦੇ ਢੰਗ, ਸਿੰਚਾਈ, ਖਾਦ ਦੇ ਵੇਰਵੇ..."
    },
    "profile": {
      "title": "ਮੇਰੀ ਪ੍ਰੋਫਾਈਲ", "subtitle": "ਆਪਣੀ ਖਾਤਾ ਜਾਣਕਾਰੀ ਅਤੇ ਖੇਤੀ ਵੇਰਵਿਆਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰੋ",
      "saveChanges": "ਤਬਦੀਲੀਆਂ ਸੰਭਾਲੋ", "fullName": "ਪੂਰਾ ਨਾਮ", "village": "ਪਿੰਡ",
      "area": "ਖੇਤਰ / ਬਲਾਕ", "district": "ਜ਼ਿਲ੍ਹਾ", "state": "ਰਾਜ", "landArea": "ਜ਼ਮੀਨ ਦਾ ਰਕਬਾ",
      "landUnit": "ਜ਼ਮੀਨ ਦੀ ਇਕਾਈ", "farmingType": "ਖੇਤੀ ਦੀ ਕਿਸਮ", "officialEmail": "ਸਰਕਾਰੀ ਈਮੇਲ",
      "designation": "ਅਫ਼ਸਰ ਅਹੁਦਾ", "department": "ਵਿਭਾਗ", "contactNumber": "ਸੰਪਰਕ ਨੰਬਰ",
      "assignedArea": "ਨਿਰਧਾਰਤ ਖੇਤਰ / ਬਲਾਕ", "profileUpdated": "ਪ੍ਰੋਫਾਈਲ ਸਫਲਤਾਪੂਰਵਕ ਅਪਡੇਟ ਕੀਤੀ ਗਈ"
    },
    "crops": {
      "onion": "ਪਿਆਜ਼", "tomato": "ਟਮਾਟਰ", "potato": "ਆਲੂ", "rice": "ਝੋਨਾ / ਚੌਲ",
      "wheat": "ਕਣਕ", "maize": "ਮੱਕੀ", "carrot": "ਗਾਜਰ", "cabbage": "ਬੰਦਗੋਭੀ",
      "cauliflower": "ਫੁੱਲਗੋਭੀ", "garlic": "ਲਸਣ", "ginger": "ਅਦਰਕ", "banana": "ਕੇਲਾ",
      "mango": "ਅੰਬ", "groundnut": "ਮੂੰਗਫਲੀ", "sugarcane": "ਗੰਨਾ", "cotton": "ਨਰਮਾ / ਕਪਾਹ"
    },
    "produce_types": {
      "tubers": "ਗੰਢਾਂ", "vegetable": "ਸਬਜ਼ੀ", "vegetable_bulbs": "ਸਬਜ਼ੀ / ਗੰਢਾਂ",
      "field_crop": "ਖੇਤ ਦੀ ਫ਼ਸਲ", "cereals": "ਅਨਾਜ", "fruits": "ਫਲ",
      "cash_crops": "ਨਕਦੀ ਫ਼ਸਲਾਂ", "spices": "ਮਸਾਲੇ"
    },
    "units": { "tons": "ਟਨ", "quintals": "ਕੁਇੰਟਲ", "kg": "ਕਿਲੋ", "acres": "ਏਕੜ", "hectares": "ਹੈਕਟੇਅਰ" },
    "qualities": {
      "gradeA": "ਗ੍ਰੇਡ A", "gradeB": "ਗ੍ਰੇਡ B", "gradeC": "ਗ੍ਰੇਡ C",
      "gradeAPremium": "ਗ੍ਰੇਡ A (ਵਧੀਆ)", "gradeBStandard": "ਗ੍ਰੇਡ B (ਮਿਆਰੀ)", "gradeCFair": "ਗ੍ਰੇਡ C (ਦਰਮਿਆਨਾ)"
    },
    "crop_stages": {
      "bulbDevelopment": "ਗੰਢ ਬਣਨਾ", "vegetative": "ਵਾਧੇ ਦਾ ਪੜਾਅ",
      "flowering": "ਫੁੱਲ ਪੈਣ ਦਾ ਪੜਾਅ", "readyForHarvest": "ਵਾਢੀ ਲਈ ਤਿਆਰ", "preHarvest": "ਵਾਢੀ ਤੋਂ ਪਹਿਲਾਂ ਦਾ ਪੜਾਅ"
    },
    "statuses": {
      "verified": "ਪ੍ਰਮਾਣਿਤ", "pending": "ਬਕਾਇਆ", "rejected": "ਰੱਦ ਕੀਤਾ ਗਿਆ",
      "available": "ਉਪਲਬਧ", "unavailable": "ਨਾ-ਉਪਲਬਧ"
    },
    "sources": {
      "officerVerified": "ਅਫ਼ਸਰ ਦੁਆਰਾ ਪ੍ਰਮਾਣਿਤ", "farmerVerified": "ਕਿਸਾਨ ਦੁਆਰਾ ਪ੍ਰਮਾਣਿਤ",
      "directOfficerEntry": "ਅਫ਼ਸਰ ਦਾ ਸਿੱਧਾ ਇੰਦਰਾਜ"
    },
    "notifications": {
      "newProduceAdded": "🌾 ਨਵਾਂ ਉਤਪਾਦ ਸ਼ਾਮਲ ਕੀਤਾ ਗਿਆ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 ਉਤਪਾਦ ਅਪਡੇਟ ਹੋਇਆ: {{crop}}",
      "newFarmerSubmission": "📋 ਨਵੀਂ ਕਿਸਾਨ ਫ਼ਸਲ ਅਰਜ਼ੀ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ ਫ਼ਸਲ ਪ੍ਰਮਾਣਿਤ ਹੋਈ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ ਕਿਸਾਨ ਬੇਨਤੀ ਰੱਦ ਕੀਤੀ ਗਈ: {{crop}}",
      "purchaseInquiry": "💼 ਖਰੀਦ ਪੁੱਛਗਿੱਛ: ਖਰੀਦਦਾਰ ਨੇ {{qty}} {{unit}} {{crop}} ਦੀ ਮੰਗ ਕੀਤੀ",
      "demoReset": "🔄 ਡੈਮੋ ਡਾਟਾ ਮੁੜ ਸੈੱਟ ਹੋ ਗਿਆ",
      "inquirySent": "✓ ਖਰੀਦ ਪੁੱਛਗਿੱਛ ਉਤਪਾਦਕ / ਅਫ਼ਸਰ ਨੂੰ ਭੇਜੀ ਗਈ!",
      "statusUpdated": "ਉਤਪਾਦ ਸਥਿਤੀ ਅਪਡੇਟ ਹੋਈ", "deleted": "ਉਤਪਾਦ ਰਿਕਾਰਡ ਮਿਟਾਇਆ ਗਿਆ"
    },
    "demo": {
      "controlsTitle": "SIH ਡੈਮੋ ਕੰਟਰੋਲ:", "officerBtn": "ਅਫ਼ਸਰ (ਰਵੀ ਕੁਮਾਰ)",
      "farmerBtn": "ਕਿਸਾਨ (ਕੁਮਾਰ)", "buyerBtn": "ਜਨਤਕ ਖਰੀਦਦਾਰ ਦ੍ਰਿਸ਼",
      "resetBtn": "ਡੈਮੋ ਰੀਸੈੱਟ", "resetConfirm": "ਕੀ ਤੁਸੀਂ ਡਾਟਾਬੇਸ ਨੂੰ ਸ਼ੁਰੂਆਤੀ ਡੈਮੋ ਸਥਿਤੀ ਵਿੱਚ ਰੀਸੈੱਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?"
    }
  },
  "or": {
    "lang": { "name": "Odia", "nativeName": "ଓଡ଼ିଆ", "code": "or", "dir": "ltr" },
    "common": {
      "language": "ଭାଷା", "login": "ଲଗଇନ", "register": "ପଞ୍ଜୀକରଣ", "logout": "ଲଗଆଉଟ",
      "dashboard": "ଡ୍ୟାସବୋର୍ଡ", "profile": "ପ୍ରୋଫାଇଲ", "save": "ସଂରକ୍ଷଣ", "cancel": "ବାତିଲ",
      "close": "ବନ୍ଦ କରନ୍ତୁ", "submit": "ଦାଖଲ କରନ୍ତୁ", "refresh": "ରିଫ୍ରେଶ", "search": "ଖୋଜନ୍ତୁ",
      "clearFilters": "ଫିଲ୍ଟର ହଟାନ୍ତୁ", "loading": "ଲୋଡ୍ ହେଉଛି...", "viewDetails": "ବିବରଣୀ ଦେଖନ୍ତୁ",
      "allStates": "ସମସ୍ତ ରାଜ୍ୟ", "allDistricts": "ସମସ୍ତ ଜିଲ୍ଲା", "allAreas": "ସମସ୍ତ ଅଞ୍ଚଳ",
      "verified": "ଯାଞ୍ଚ ହୋଇଛି", "pending": "ବକେୟା ଅଛି", "rejected": "ପ୍ରତ୍ୟାଖ୍ୟାନ ହୋଇଛି",
      "available": "ଉପଲବ୍ଧ", "unavailable": "ଅନୁପଲବ୍ଧ", "yes": "ହଁ", "no": "ନାହିଁ",
      "continue": "ଜାରି ରଖନ୍ତୁ", "send": "ପଠାନ୍ତୁ", "back": "ପଛକୁ", "next": "ପରବର୍ତ୍ତୀ",
      "previous": "ପୂର୍ବବର୍ତ୍ତୀ", "edit": "ସମ୍ପାଦନ", "delete": "ଡିଲିଟ କରନ୍ତୁ", "status": "ସ୍ଥିତି",
      "role": "ଭୂମିକା", "user": "ବ୍ୟବହାରକାରୀ", "liveSync": "ଲାଇଭ ସିଙ୍କ", "reconnecting": "ପୁନଃ ସଂଯୋଗ ହେଉଛି...",
      "reset": "ରିସେଟ", "actions": "କାର୍ଯ୍ୟ", "crop": "ଫସଲ", "quantity": "ପରିମାଣ",
      "location": "ସ୍ଥାନ", "date": "ତାରିଖ", "notes": "ଟିପ୍ପଣୀ"
    },
    "navigation": {
      "home": "ମୁଖ୍ୟ ପୃଷ୍ଠା", "viewProduce": "ଉତ୍ପାଦନ ଦେଖନ୍ତୁ", "officerPortal": "ଅଧିକାରୀ ପୋର୍ଟାଲ",
      "farmerPortal": "କୃଷକ ପୋର୍ଟାଲ", "dashboard": "ଡ୍ୟାସବୋର୍ଡ", "profile": "ପ୍ରୋଫାଇଲ",
      "requests": "ଅନୁରୋଧ", "addProduce": "ଉତ୍ପାଦନ ଯୋଡନ୍ତୁ", "addCrop": "ଫସଲ ଯୋଡନ୍ତୁ",
      "myRequests": "ମୋର ଅନୁରୋଧ", "farmerRequests": "କୃଷକ ଅନୁରୋଧ",
      "liveSync": "ଲାଇଭ ସିଙ୍କ", "publicBuyerView": "ସାଧାରଣ କ୍ରେତା ଦୃଶ୍ୟ"
    },
    "auth": {
      "roleSelector": "ଆପଣଙ୍କ ଭୂମିକା ବାଛନ୍ତୁ", "agricultureOfficer": "କୃଷି ଅଧିକାରୀ", "farmer": "କୃଷକ",
      "mobileOrEmail": "ମୋବାଇଲ ନମ୍ବର କିମ୍ବା ଇମେଲ", "password": "ପାସୱାର୍ଡ", "signIn": "ସାଇନ ଇନ",
      "fullName": "ପୂରା ନାମ", "mobileNumber": "ମୋବାଇଲ ନମ୍ବର", "emailOptional": "ଇମେଲ (ଇଚ୍ଛାଧୀନ)",
      "createAccount": "ଖାତା ଖୋଲନ୍ତୁ", "designation": "ପଦବୀ", "department": "ବିଭାଗ",
      "assignedArea": "ନିଯୁକ୍ତ ଅଞ୍ଚଳ", "district": "ଜିଲ୍ଲା", "state": "ରାଜ୍ୟ",
      "village": "ଗ୍ରାମ", "landArea": "ଜମି ପରିମାଣ (ଏକର)", "farmingType": "ଚାଷ ପ୍ରଣାଳୀ",
      "welcomeBack": "ସ୍ୱାଗତ, {{name}}!", "accountCreated": "ଖାତା ସୃଷ୍ଟି ହୋଇଛି! ସ୍ୱାଗତ, {{name}}.",
      "invalidCredentials": "ଭୁଲ ଲଗଇନ ବିବରଣୀ", "requiredFields": "ଦୟାକରି ସମସ୍ତ ଆବଶ୍ୟକ ତଥ୍ୟ ପୂରଣ କରନ୍ତୁ (ନାମ, ମୋବାଇଲ, ପାସୱାର୍ଡ)।",
      "demoLoginFailed": "ଡେମୋ ଲଗଇନ ବିଫଳ", "networkError": "ନେଟୱାର୍କ ତ୍ରୁଟି",
      "logoutSuccess": "ଆପଣ ସଫଳତାର ସହିତ ଲଗଆଉଟ ହୋଇଛନ୍ତି।",
      "officerLoginRequired": "ଅଧିକାରୀ ପୋର୍ଟାଲ ବ୍ୟବହାର କରିବାକୁ କୃଷି ଅଧିକାରୀ ଭାବେ ଲଗଇନ କରନ୍ତୁ।",
      "farmerLoginRequired": "କୃଷକ ପୋର୍ଟାଲ ବ୍ୟବହାର କରିବାକୁ କୃଷକ ଭାବେ ଲଗଇନ କରନ୍ତୁ।",
      "registrationFailed": "ପଞ୍ଜୀକରଣ ବିଫଳ ହୋଇଛି। ଦୟାକରି ଯାଞ୍ଚ କରନ୍ତୁ।", "switchedRole": "{{role}} କୁ ପରିବର୍ତ୍ତନ କରାଗଲା"
    },
    "landing": {
      "verifiedPlatform": "ପ୍ରମାଣିତ ସ୍ଥାନୀୟ କୃଷି ଉତ୍ପାଦନ ମଞ୍ଚ", "title": "ଆବିଷ୍କାର କରନ୍ତୁ। ଯାଞ୍ଚ କରନ୍ତୁ। ଯୋଡ଼ି ହୁଅନ୍ତୁ।",
      "subtitle": "କୃଷକ ଏବଂ କୃଷି ଅଧିକାରୀମାନଙ୍କୁ ସ୍ଥାନୀୟ ଉତ୍ପାଦନର ପ୍ରମାଣିତ ତଥ୍ୟ ରଖିବାରେ ଏଗ୍ରିଫ୍ଲୋ ସାହାଯ୍ୟ କରେ, ଯାହାଦ୍ୱାରା କ୍ରେତାମାନେ ସହଜରେ ଫସଲ ଖୋଜିପାରିବେ।",
      "searchVerifiedProduce": "ପ୍ରମାଣିତ ଉତ୍ପାଦନ ଖୋଜନ୍ତୁ", "findVerifiedProduce": "ଉତ୍ପାଦନ ଖୋଜନ୍ତୁ",
      "quickDiscovery": "ଅଞ୍ଚଳ ଅନୁସାରେ ଶୀଘ୍ର ଫସଲ ଖୋଜନ୍ତୁ", "cropName": "ଫସଲର ନାମ",
      "cropPlaceholder": "ଯଥା: ପିଆଜ, ଟମାଟୋ...", "state": "ରାଜ୍ୟ", "district": "ଜିଲ୍ଲା",
      "allStates": "ସମସ୍ତ ରାଜ୍ୟ", "allDistricts": "ସମସ୍ତ ଜିଲ୍ଲା", "howItWorks": "ଏଗ୍ରିଫ୍ଲୋ କିପରି କାମ କରେ",
      "workflowIntro": "ସ୍ଥାନୀୟ କୃଷିକୁ ଖୋଲା ବଜାର ସହିତ ଯୋଡୁଥିବା ଏକ ସ୍ୱଚ୍ଛ ଯାଞ୍ଚ ପ୍ରକ୍ରିୟା।",
      "sihPlatform": "SIH ମଞ୍ଚ", "tagLine": "ଆବିଷ୍କାର କରନ୍ତୁ। ଯାଞ୍ଚ କରନ୍ତୁ। ଯୋଡ଼ି ହୁଅନ୍ତୁ।"
    },
    "howItWorks": {
      "farmerSubmission": "କୃଷକଙ୍କ ଆବେଦନ",
      "farmerSubmissionDesc": "କୃଷକମାନେ ନିଜର ଚାଷ ଜମି, ଫସଲ ଅବସ୍ଥା ଏବଂ ଆଗାମୀ ଅମଳର ବିବରଣୀ ସ୍ଥାନୀୟ ଯାଞ୍ଚ ପାଇଁ ଦାଖଲ କରନ୍ତି।",
      "officerVerification": "ଅଧିକାରୀଙ୍କ ଯାଞ୍ଚ",
      "officerVerificationDesc": "ସ୍ଥାନୀୟ କୃଷି ଅଧିକାରୀ ଆବେଦନଗୁଡ଼ିକୁ କ୍ଷେତ୍ର ପରିଦର୍ଶନ କରି ଯାଞ୍ଚ କରନ୍ତି ଏବଂ ପ୍ରମାଣିତ ଉତ୍ପାଦ ପ୍ରକାଶ କରନ୍ତି।",
      "publicDiscovery": "ସାଧାରଣ ଖୋଜ ଏବଂ ଯୋଗାଯୋଗ",
      "publicDiscoveryDesc": "କ୍ରେତାମାନେ ବିନା କୌଣସି ଲଗଇନ ବାଧାରେ ଫସଲ, ଜିଲ୍ଲା ଏବଂ ପରିମାଣ ଅନୁଯାୟୀ ପ୍ରମାଣିତ ଉତ୍ପାଦ ଖୋଜିପାରିବେ।"
    },
    "roles": {
      "farmers": "କୃଷକମାନଙ୍କ ପାଇଁ", "officers": "କୃଷି ଅଧିକାରୀମାନଙ୍କ ପାଇଁ", "buyers": "କ୍ରେତା ଓ ବ୍ୟବସାୟୀଙ୍କ ପାଇଁ",
      "farmerTitle": "ଫସଲର ସିଧାସଳଖ ପ୍ରଦର୍ଶନ", "officerTitle": "ଅଧିକାର କ୍ଷେତ୍ର ନିୟନ୍ତ୍ରଣ ଓ ବିଶ୍ୱାସ",
      "buyerTitle": "ପ୍ରମାଣିତ ଯୋଗାଣର ସନ୍ଧାନ",
      "farmerItem1": "କୃଷି ପ୍ରୋଫାଇଲ ଏବଂ ଚାଷ ଜମି ପଞ୍ଜୀକରଣ କରନ୍ତୁ",
      "farmerItem2": "ସ୍ଥାନୀୟ ଯାଞ୍ଚ ପାଇଁ ଆଗାମୀ ଅମଳର ବିବରଣୀ ଦାଖଲ କରନ୍ତୁ",
      "farmerItem3": "ପ୍ରକୃତ ସ୍ଥିତି ଜାଣନ୍ତୁ: ବକେୟା → ଯାଞ୍ଚ ହୋଇଛି / ପ୍ରତ୍ୟାଖ୍ୟାତ",
      "officerItem1": "ସ୍ଥାନୀୟ ଅଞ୍ଚଳର ପ୍ରମାଣିତ ଉତ୍ପାଦ ସିଧାସଳଖ ଯୋଡନ୍ତୁ",
      "officerItem2": "ନିଜ ବ୍ଲକର କୃଷକ ଆବେଦନଗୁଡ଼ିକର କ୍ଷେତ୍ର ପରିଦର୍ଶନ କରି ଯାଞ୍ଚ କରନ୍ତୁ",
      "officerItem3": "ପରିମାଣ ଏବଂ ଉପଲବ୍ଧତା ଅଦ୍ୟତନ କରନ୍ତୁ",
      "buyerItem1": "ଲଗଇନ ବିନା ତୁରନ୍ତ ଉତ୍ପାଦ ଖୋଜନ୍ତୁ",
      "buyerItem2": "ରାଜ୍ୟ, ଜିଲ୍ଲା, ଅଞ୍ଚଳ ଏବଂ ପରିମାଣ ଅନୁସାରେ ଫିଲ୍ଟର କରନ୍ତୁ",
      "buyerItem3": "ପ୍ରମାଣିତ ଯୋଗାଣକାରୀଙ୍କୁ ସିଧାସଳଖ କ୍ରୟ ଅନୁରୋଧ ପଠାନ୍ତୁ"
    },
    "produce": {
      "title": "ପ୍ରମାଣିତ ଉତ୍ପାଦନ ଖୋଜନ୍ତୁ",
      "subtitle": "ସ୍ଥାନୀୟ କୃଷି ଅଧିକାରୀମାନଙ୍କ ଦ୍ୱାରା ପ୍ରମାଣିତ ଉପଲବ୍ଧ ଏବଂ ଆଗାମୀ କୃଷି ଉତ୍ପାଦନ ଖୋଜନ୍ତୁ।",
      "searchCropName": "ଫସଲର ନାମ ଖୋଜନ୍ତୁ", "state": "ରାଜ୍ୟ", "district": "ଜିଲ୍ଲା", "areaBlock": "ଅଞ୍ଚଳ / ବ୍ଲକ",
      "minQty": "ସର୍ବନିମ୍ନ ପରିମାଣ (ଟନ)", "maxQty": "ସର୍ବାଧିକ ପରିମାଣ (ଟନ)", "availBefore": "ଉପଲବ୍ଧତା ତାରିଖ ସୁଦ୍ଧା/ରେ",
      "verifiedOnly": "କେବଳ ଯାଞ୍ଚ ହୋଇଥିବା (ପରାମର୍ଶିତ)", "clearFilters": "ଫିଲ୍ଟର ହଟାନ୍ତୁ",
      "count": "{{count}}ଟି ପ୍ରମାଣିତ ଉତ୍ପାଦନ ରେକର୍ଡ ଦେଖାଯାଉଛି",
      "countPlural": "{{count}}ଟି ପ୍ରମାଣିତ ଉତ୍ପାଦନ ରେକର୍ଡ ଦେଖାଯାଉଛି",
      "emptyTitle": "କୌଣସି ଉତ୍ପାଦନ ରେକର୍ଡ ମିଳିଲା ନାହିଁ",
      "emptyDescription": "ଅନ୍ୟ ଫସଲ ଖୋଜିବା ପାଇଁ ଅନୁସନ୍ଧାନ ପରିସର ବଢ଼ାନ୍ତୁ କିମ୍ବା ଫିଲ୍ଟର ହଟାନ୍ତୁ।",
      "resetAllFilters": "ସମସ୍ତ ଫିଲ୍ଟର ରିସେଟ କରନ୍ତୁ", "autoSynced": "WebSocket ଦ୍ୱାରା ଲାଇଭ ସିଙ୍କ ହୋଇଛି",
      "availableQuantity": "ଉପଲବ୍ଧ ପରିମାଣ", "quality": "ଗୁଣବତ୍ତା", "availability": "ଉପଲବ୍ଧତା",
      "sourceOfficer": "ଅଧିକାରୀଙ୍କ ଦ୍ୱାରା ଯାଞ୍ଚିତ", "sourceFarmer": "କୃଷକଙ୍କ ଦ୍ୱାରା ଯାଞ୍ଚିତ",
      "verifiedBadge": "✓ ଯାଞ୍ଚ ହୋଇଛି", "qualityGrade": "ଗୁଣବତ୍ତା ଗ୍ରେଡ୍", "verificationSource": "ଯାଞ୍ଚ ଉତ୍ସ",
      "fieldNotes": "ଅଧିକାରୀ କ୍ଷେତ୍ର ପରିଦର୍ଶନ ନୋଟ୍ସ",
      "purchaseTitle": "କ୍ରୟ ଅନୁସନ୍ଧାନ / ଅନୁରୋଧ ପଠାନ୍ତୁ",
      "purchaseSubtitle": "ପ୍ରମାଣିତ ଉତ୍ପାଦକ / ସ୍ଥାନୀୟ ଅଧିକାରୀଙ୍କ ସହିତ ସିଧାସଳଖ ଯୋଡ଼ି ହେବାକୁ ଆପଣଙ୍କ ଆବଶ୍ୟକତା ଜଣାନ୍ତୁ।",
      "yourName": "ଆପଣଙ୍କ ନାମ / କମ୍ପାନୀ", "contact": "ଯୋଗାଯୋଗ ନମ୍ବର / ଇମେଲ",
      "requestedQty": "ଆବଶ୍ୟକ ପରିମାଣ", "message": "ବାର୍ତ୍ତା / ଆବଶ୍ୟକତା", "sendRequest": "କ୍ରୟ ଅନୁରୋଧ ପଠାନ୍ତୁ",
      "notFound": "ଉତ୍ପାଦନ ରେକର୍ଡ ମିଳିଲା ନାହିଁ", "noLogin": "ଲଗଇନ ଆବଶ୍ୟକ ନାହିଁ", "unitLabel": "ଏକକ"
    },
    "officer": {
      "portal": "କୃଷି ଅଧିକାରୀ ପୋର୍ଟାଲ", "subtitle": "ସ୍ଥାନୀୟ ଉତ୍ପାଦନ ପରିଚାଳନା କରନ୍ତୁ, କୃଷକ ଆବେଦନ ଯାଞ୍ଚ କରନ୍ତୁ",
      "profile": "ପ୍ରୋଫାଇଲ ସମ୍ପାଦନ", "totalRecords": "ମୋଟ ରେକର୍ଡ", "totalRecordsHint": "ଆପଣଙ୍କ ଅଞ୍ଚଳରେ",
      "availableQty": "ଉପଲବ୍ଧ ପରିମାଣ", "availableQtyHint": "ପ୍ରମାଣିତ ଉତ୍ପାଦନ", "farmerRequests": "କୃଷକ ଅନୁରୋଧ",
      "pending": "କ୍ଷେତ୍ର ଯାଞ୍ଚ ବକେୟା", "verifiedRecords": "ପ୍ରମାଣିତ ରେକର୍ଡ", "verifiedRecordsHint": "କ୍ରେତାଙ୍କ ପାଇଁ ଉପଲବ୍ଧ",
      "queueTitle": "କୃଷକ ଯାଞ୍ଚ ଅନୁରୋଧ", "queueSubtitle": "ଆପଣଙ୍କ ଅଞ୍ଚଳରେ କ୍ଷେତ୍ର ପରିଦର୍ଶନ ପାଇଁ ଅପେକ୍ଷା କରିଥିବା କୃଷକମାନେ",
      "queueEmpty": "ସମସ୍ତ କାର୍ଯ୍ୟ ସମାପ୍ତ! କୌଣସି ବକେୟା ଅନୁରୋଧ ନାହିଁ।",
      "localProduceTitle": "ସ୍ଥାନୀୟ କୃଷି ଉତ୍ପାଦନ", "localProduceSubtitle": "ଆପଣଙ୍କ ଅଧିକାର କ୍ଷେତ୍ରରେ ପଞ୍ଜୀକୃତ ଉତ୍ପାଦନ",
      "addProduce": "+ ଉତ୍ପାଦନ ଯୋଡନ୍ତୁ", "editProduce": "ଉତ୍ପାଦନ ସମ୍ପାଦନ", "addProduceModalTitle": "+ ସ୍ଥାନୀୟ ଉତ୍ପାଦନ ଯୋଡନ୍ତୁ",
      "modalSubtitle": "ଅଧିକାରୀଙ୍କ ଦ୍ୱାରା ପ୍ରବିଷ୍ଟ ଉତ୍ପାଦନ ସିଧାସଳଖ ଯାଞ୍ଚ ହୋଇଥିବା ଭାବେ ଚିହ୍ନିତ ହେବ",
      "savePublish": "ସଂରକ୍ଷଣ ଓ ପ୍ରକାଶ କରନ୍ତୁ", "verify": "ଯାଞ୍ଚ କରନ୍ତୁ", "reject": "ପ୍ରତ୍ୟାଖ୍ୟାନ କରନ୍ତୁ",
      "pendingBadge": "🟡 ଯାଞ୍ଚ ବକେୟା", "directOfficerEntry": "ଅଧିକାରୀଙ୍କ ସିଧାସଳଖ ଏଣ୍ଟ୍ରି",
      "markUnavailable": "ଅନୁପଲବ୍ଧ ଚିହ୍ନିତ କରନ୍ତୁ", "markAvailable": "ଉପଲବ୍ଧ ଚିହ୍ନିତ କରନ୍ତୁ",
      "editProduceAction": "ଉତ୍ପାଦନ ସମ୍ପାଦନ", "deleteProduce": "ରେକର୍ଡ ବିଲୋପ କରନ୍ତୁ",
      "deleteConfirm": "ଆପଣ ଏହି ଉତ୍ପାଦନ ରେକର୍ଡଟି ବିଲୋପ କରିବାକୁ ନିଶ୍ଚିତ କି?", "rejectTitle": "କୃଷକ ଅନୁରୋଧ ପ୍ରତ୍ୟାଖ୍ୟାନ କରନ୍ତୁ",
      "rejectDescription": "ଦୟାକରି ପ୍ରତ୍ୟାଖ୍ୟାନର ଉପଯୁକ୍ତ କାରଣ ଦର୍ଶାନ୍ତୁ",
      "rejectionReason": "ପ୍ରତ୍ୟାଖ୍ୟାନର କାରଣ / ଆବଶ୍ୟକ ସଂଶୋଧନ",
      "rejectionPlaceholder": "ଯଥା: ଆକଳନ କରାଯାଇଥିବା ଅମଳ ଜମି ଆକାର ସହିତ ମେଳ ଖାଉନାହିଁ; ପୁନର୍ବାର ମାପ କରନ୍ତୁ।",
      "confirmRejection": "ପ୍ରତ୍ୟାଖ୍ୟାନ ନିଶ୍ଚିତ କରନ୍ତୁ", "fieldInspected": "ଅଧିକାରୀଙ୍କ ଦ୍ୱାରା କ୍ଷେତ୍ର ପରିଦର୍ଶନ କରାଯାଇ ଯାଞ୍ଚିତ",
      "verificationSuccess": "✓ କୃଷକ ଆବେଦନ ଯାଞ୍ଚ ହୋଇ ସାଧାରଣ ଦୃଶ୍ୟରେ ପ୍ରକାଶିତ ହେଲା!",
      "rejectionSuccess": "ଅନୁରୋଧ ପ୍ରତ୍ୟାଖ୍ୟାନ କରାଗଲା ଏବଂ କୃଷକଙ୍କୁ ସୂଚନା ଦିଆଗଲା।",
      "provideReason": "ଦୟାକରି ପ୍ରତ୍ୟାଖ୍ୟାନର କାରଣ ଉଲ୍ଲେଖ କରନ୍ତୁ", "noProduceYet": "ଆପଣଙ୍କ ଅଞ୍ଚଳରେ ଏପର୍ଯ୍ୟନ୍ତ କୌଣସି ଉତ୍ପାଦନ ପଞ୍ଜୀକୃତ ହୋଇନାହିଁ।",
      "cropCol": "ଫସଲ", "qtyCol": "ପରିମାଣ", "locationCol": "ସ୍ଥାନ", "availDateCol": "ଉପଲବ୍ଧତା ତାରିଖ",
      "qualityCol": "ଗୁଣବତ୍ତା", "sourceCol": "ଉତ୍ସ", "statusCol": "ସ୍ଥିତି", "actionsCol": "କାର୍ଯ୍ୟ",
      "officerRecordedSuccess": "✓ ଅଧିକାରୀଙ୍କ ଦ୍ୱାରା ସିଧାସଳଖ ପଞ୍ଜୀକୃତ ଏବଂ ଯାଞ୍ଚିତ!",
      "updateProduceSuccess": "ଉତ୍ପାଦନ ସଫଳତାର ସହିତ ଅଦ୍ୟତନ ହେଲା"
    },
    "farmer": {
      "portal": "କୃଷକ ପୋର୍ଟାଲ", "myProfile": "ମୋର କୃଷି ପ୍ରୋଫାଇଲ",
      "assignedOfficer": "ଆପଣଙ୍କ ନିଯୁକ୍ତ ସ୍ଥାନୀୟ କୃଷି ଅଧିକାରୀ", "assignedOfficerHint": "ଆବେଦନଗୁଡ଼ିକ ଏଠାକୁ ପଠାଯାଏ",
      "totalSubmissions": "ମୋଟ ଆବେଦନ", "pending": "ବକେୟା", "verified": "ଯାଞ୍ଚ ହୋଇଛି & ସକ୍ରିୟ",
      "rejected": "ପ୍ରତ୍ୟାଖ୍ୟାତ", "requestsTitle": "ମୋର ଫସଲ ଯାଞ୍ଚ ଅନୁରୋଧ",
      "requestsSubtitle": "ନିଜ ସ୍ଥାନୀୟ କୃଷି ଅଧିକାରୀଙ୍କଠାରୁ ସ୍ଥିତି ଜାଣନ୍ତୁ",
      "addCrop": "+ ଫସଲ ବିବରଣୀ ଯୋଡନ୍ତୁ", "addCropButton": "+ ଫସଲ ଯୋଡନ୍ତୁ", "myCropDetails": "+ କୃଷି ଫସଲ ବିବରଣୀ ଯୋଡନ୍ତୁ",
      "submittedToOfficer": "ଦାଖଲ କରାଯାଇଥିବା ତଥ୍ୟ ଯାଞ୍ଚ ପାଇଁ ସ୍ଥାନୀୟ କୃଷି ଅଧିକାରୀଙ୍କ ନିକଟକୁ ପଠାଯିବ",
      "submitToOfficer": "ସ୍ଥାନୀୟ ଅଧିକାରୀଙ୍କୁ ଦାଖଲ କରନ୍ତୁ", "noCrops": "ଏପର୍ଯ୍ୟନ୍ତ କୌଣସି ଫସଲ ଦାଖଲ ହୋଇନାହିଁ",
      "noCropsDescription": "ସ୍ଥାନୀୟ ଯାଞ୍ଚ ପାଇଁ ଆପଣଙ୍କ ବର୍ତ୍ତମାନର ଚାଷ ବିବରଣୀ ଯୋଡନ୍ତୁ।", "addFirstCrop": "ପ୍ରଥମ ଫସଲ ଯୋଡନ୍ତୁ",
      "pendingStatus": "🟡 ଯାଞ୍ଚ ବକେୟା", "verifiedStatus": "🟢 ✓ ଯାଞ୍ଚ ହୋଇଛି", "rejectedStatus": "🔴 ପ୍ରତ୍ୟାଖ୍ୟାତ",
      "expectedHarvest": "ଅନୁମାନିତ ଅମଳ ତାରିଖ", "cultivatedArea": "ଚାଷ ଜମି ପରିମାଣ", "expectedYield": "ଅନୁମାନିତ ଅମଳ",
      "cropStage": "ଫସଲର ଅବସ୍ଥା", "officerFeedback": "ଅଧିକାରୀଙ୍କ ମତାମତ:", "submissionSuccess": "✓ ଫସଲ ଦାଖଲ ହେଲା! ଯାଞ୍ଚ ପାଇଁ କୃଷି ଅଧିକାରୀଙ୍କ ନିକଟକୁ ପଠାଗଲା।",
      "verificationStatus": "ବକେୟା → ଯାଞ୍ଚ ହୋଇଛି / ପ୍ରତ୍ୟାଖ୍ୟାତ", "locationRouting": "ସ୍ଥାନ ରୁଟିଂ (ସ୍ଥାନୀୟ ଅଧିକାରୀଙ୍କ ପାଇଁ)",
      "additionalNotes": "ଅତିରିକ୍ତ କୃଷି ଟିପ୍ପଣୀ", "farmingNotesPlaceholder": "ଚାଷ ପ୍ରଣାଳୀ, ଜଳସେଚନ, ସାର ପ୍ରୟୋଗ ବିବରଣୀ..."
    },
    "profile": {
      "title": "ମୋର ପ୍ରୋଫାଇଲ", "subtitle": "ଆପଣଙ୍କ ଖାତା ବିବରଣୀ ଏବଂ କୃଷି ତଥ୍ୟ ପରିଚାଳନା କରନ୍ତୁ",
      "saveChanges": "ପରିବର୍ତ୍ତନ ସଂରକ୍ଷଣ କରନ୍ତୁ", "fullName": "ପୂରା ନାମ", "village": "ଗ୍ରାମ",
      "area": "ଅଞ୍ଚଳ / ବ୍ଲକ", "district": "ଜିଲ୍ଲା", "state": "ରାଜ୍ୟ", "landArea": "ଜମି ପରିମାଣ",
      "landUnit": "ଜମି ଏକକ", "farmingType": "ଚାଷ ପ୍ରଣାଳୀ", "officialEmail": "ସରକାରୀ ଇମେଲ",
      "designation": "ଅଧିକାରୀ ପଦବୀ", "department": "ବିଭାଗ", "contactNumber": "ଯୋଗାଯୋଗ ନମ୍ବର",
      "assignedArea": "ନିଯୁକ୍ତ ଅଞ୍ଚଳ / ବ୍ଲକ", "profileUpdated": "ପ୍ରୋଫାଇଲ ସଫଳତାର ସହିତ ଅଦ୍ୟତନ ହେଲା"
    },
    "crops": {
      "onion": "ପିଆଜ", "tomato": "ଟମାଟୋ", "potato": "ଆଳୁ", "rice": "ଧାନ / ଚାଉଳ",
      "wheat": "ଗହମ", "maize": "ମକା", "carrot": "ଗାଜର", "cabbage": "ବନ୍ଧାକୋବି",
      "cauliflower": "ଫୁଲକୋବି", "garlic": "ରସୁଣ", "ginger": "ଅଦା", "banana": "କଦଳୀ",
      "mango": "ଆମ୍ବ", "groundnut": "ଚିନାବାଦାମ", "sugarcane": "ଆଖୁ", "cotton": "କପା"
    },
    "produce_types": {
      "tubers": "କନ୍ଦମୂଳ", "vegetable": "ପନିପରିବା", "vegetable_bulbs": "ପନିପରିବା / କନ୍ଦମୂଳ",
      "field_crop": "କ୍ଷେତ ଫସଲ", "cereals": "ଶସ୍ୟ", "fruits": "ଫଳମୂଳ",
      "cash_crops": "ଅର୍ଥକରୀ ଫସଲ", "spices": "ମସଲା"
    },
    "units": { "tons": "ଟନ", "quintals": "କ୍ୱିଣ୍ଟାଲ", "kg": "କିଲୋଗ୍ରାମ", "acres": "ଏକର", "hectares": "ହେକ୍ଟର" },
    "qualities": {
      "gradeA": "ଗ୍ରେଡ୍ A", "gradeB": "ଗ୍ରେଡ୍ B", "gradeC": "ଗ୍ରେଡ୍ C",
      "gradeAPremium": "ଗ୍ରେଡ୍ A (ଉନ୍ନତ)", "gradeBStandard": "ଗ୍ରେଡ୍ B (ମାନକ)", "gradeCFair": "ଗ୍ରେଡ୍ C (ସାଧାରଣ)"
    },
    "crop_stages": {
      "bulbDevelopment": "କନ୍ଦ ବୃଦ୍ଧି", "vegetative": "ବୃଦ୍ଧି ପର୍ଯ୍ୟାୟ",
      "flowering": "ଫୁଲ ଫୁଟିବା ଅବସ୍ଥା", "readyForHarvest": "ଅମଳ ପାଇଁ ପ୍ରସ୍ତୁତ", "preHarvest": "ଅମଳ ପୂର୍ବବର୍ତ୍ତୀ"
    },
    "statuses": {
      "verified": "ଯାଞ୍ଚ ହୋଇଛି", "pending": "ବକେୟା", "rejected": "ପ୍ରତ୍ୟାଖ୍ୟାତ",
      "available": "ଉପଲବ୍ଧ", "unavailable": "ଅନୁପଲବ୍ଧ"
    },
    "sources": {
      "officerVerified": "ଅଧିକାରୀଙ୍କ ଦ୍ୱାରା ଯାଞ୍ଚିତ", "farmerVerified": "କୃଷକଙ୍କ ଦ୍ୱାରା ଯାଞ୍ଚିତ",
      "directOfficerEntry": "ଅଧିକାରୀଙ୍କ ସିଧାସଳଖ ଏଣ୍ଟ୍ରି"
    },
    "notifications": {
      "newProduceAdded": "🌾 ନୂଆ ଉତ୍ପାଦନ ଯୋଡ଼ାଗଲା: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 ଉତ୍ପାଦନ ଅଦ୍ୟତନ ହେଲା: {{crop}}",
      "newFarmerSubmission": "📋 ନୂଆ କୃଷକ ଆବେଦନ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ ଫସଲ ଯାଞ୍ଚିତ ହେଲା: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ କୃଷକ ଅନୁରୋଧ ପ୍ରତ୍ୟାଖ୍ୟାତ ହେଲା: {{crop}}",
      "purchaseInquiry": "💼 କ୍ରୟ ଅନୁସନ୍ଧାନ: କ୍ରେତା {{qty}} {{unit}} {{crop}} ଚାହିଁଛନ୍ତି",
      "demoReset": "🔄 ଡେମୋ ଡାଟା ପୁନଃ ସେଟ୍ ହେଲା",
      "inquirySent": "✓ କ୍ରୟ ଅନୁରୋଧ ଉତ୍ପାଦକ / ଅଧିକାରୀଙ୍କୁ ପଠାଗଲା!",
      "statusUpdated": "ଉତ୍ପାଦନ ସ୍ଥିତି ଅଦ୍ୟତନ ହେଲା", "deleted": "ଉତ୍ପାଦନ ରେକର୍ଡ ବିଲୋପ କରାଗଲା"
    },
    "demo": {
      "controlsTitle": "SIH ଡେମୋ ନିୟନ୍ତ୍ରଣ:", "officerBtn": "ଅଧିକାରୀ (ରବି କୁମାର)",
      "farmerBtn": "କୃଷକ (କୁମାର)", "buyerBtn": "ସାଧାରଣ କ୍ରେତା ଦୃଶ୍ୟ",
      "resetBtn": "ଡେମୋ ରିସେଟ", "resetConfirm": "ଡାଟାବେସକୁ ପ୍ରାରମ୍ଭିକ ଡେମୋ ସ୍ଥିତିକୁ ରିସେଟ କରିବାକୁ ଚାହାଁନ୍ତି କି?"
    }
  },
  "as": {
    "lang": { "name": "Assamese", "nativeName": "অসমীয়া", "code": "as", "dir": "ltr" },
    "common": {
      "language": "ভাষা", "login": "লগইন", "register": "পঞ্জীয়ন", "logout": "লগআউট",
      "dashboard": "ড্যাশবোর্ড", "profile": "প্রফাইল", "save": "সংৰক্ষণ", "cancel": "বাতিল",
      "close": "বন্ধ কৰক", "submit": "দাখিল কৰক", "refresh": "সতেজ কৰক", "search": "সন্ধାନ",
      "clearFilters": "ফিল্টাৰ আঁতৰাওক", "loading": "লোড হৈ আছে...", "viewDetails": "বিৱৰণ চাওক",
      "allStates": "সকলো ৰাজ্য", "allDistricts": "সকলো জিলা", "allAreas": "সকলো অঞ্চল",
      "verified": "পৰীক্ষিত", "pending": "বাকী থকা", "rejected": "প্রত্যাখ্যাত",
      "available": "উপলব্ধ", "unavailable": "অনুপলব্ধ", "yes": "হয়", "no": "নহয়",
      "continue": "আগবাঢ়ক", "send": "প্ৰেৰণ কৰক", "back": "পিছলৈ", "next": "পৰৱৰ্তী",
      "previous": "পূৰ্বৱৰ্তী", "edit": "সম্পাদনা", "delete": "মচি পেলাওক", "status": "স্থিতি",
      "role": "ভূমিকা", "user": "ব্যৱহাৰকাৰী", "liveSync": "লাইভ ছিংক", "reconnecting": "পুনৰ সংযোগ হৈছে...",
      "reset": "ৰিছেট", "actions": "কাৰ্য্য", "crop": "শস্য", "quantity": "পৰিমাণ",
      "location": "স্থান", "date": "তাৰিখ", "notes": "টোকা"
    },
    "navigation": {
      "home": "গৃহ", "viewProduce": "উৎপাদিত সামগ্ৰী চাওক", "officerPortal": "বিষয়াৰ পৰ্টেল",
      "farmerPortal": "কৃষক পৰ্টেল", "dashboard": "ড্যাশবোর্ড", "profile": "প্রফাইল",
      "requests": "অনুৰোধ", "addProduce": "সামগ্ৰী যোগ কৰক", "addCrop": "শস্য যোগ কৰক",
      "myRequests": "মোৰ অনুৰোধ", "farmerRequests": "কৃষকৰ অনুৰোধ",
      "liveSync": "লাইভ ছিংক", "publicBuyerView": "ৰাজহুৱਾ ক্ৰেতাৰ দৃশ্য"
    },
    "auth": {
      "roleSelector": "আপোনাৰ ভূমিকা বাছক", "agricultureOfficer": "কৃষি বিষয়া", "farmer": "কৃষক",
      "mobileOrEmail": "ম'বাইল নম্বৰ বা ইমেইল", "password": "পাছৱৰ্ড", "signIn": "ছাইন ইন",
      "fullName": "সম্পূৰ্ণ নাম", "mobileNumber": "ম'বাইল নম্বৰ", "emailOptional": "ইমেইল (ঐচ্ছিক)",
      "createAccount": "একাউণ্ট খোলক", "designation": "পদবী", "department": "বিভাগ",
      "assignedArea": "নিযুক্ত অঞ্চল", "district": "জিলা", "state": "ৰাজ্য",
      "village": "গাঁও", "landArea": "মাটিৰ পৰিমাণ (একর)", "farmingType": "কৃষিৰ প্ৰকাৰ",
      "welcomeBack": "স্বাগতম, {{name}}!", "accountCreated": "একাউণ্ট সৃষ্টি হ'ল! স্বাগতম, {{name}}.",
      "invalidCredentials": "অবৈধ লগইন তথ্য", "requiredFields": "অনুগ্ৰহ কৰি সকলো প্ৰয়োজনীয় তথ্য পূৰণ কৰক (নাম, ম'বাইল, পাছৱৰ্ড)।",
      "demoLoginFailed": "ডেমো লগইন ব্যৰ্থ হ'ল", "networkError": "নেটৱৰ্ক ত্রুটি",
      "logoutSuccess": "আপুনি সফলভাৱে লগআউট হ'ল।",
      "officerLoginRequired": "বিষয়া পৰ্টেল ব্যৱহাৰ কৰিবলৈ কৃষি বিষয়া হিচাপে লগইন কৰক।",
      "farmerLoginRequired": "কৃষক পৰ্টেল ব্যৱহাৰ কৰিবলৈ কৃষক হিচাপে লগইন কৰক।",
      "registrationFailed": "পঞ্জীয়ন ব্যৰ্থ হ'ল। অনুগ্ৰহ কৰি বিৱৰণ পৰীক্ষা কৰক।", "switchedRole": "{{role}} লৈ সলনি কৰা হ'ল"
    },
    "landing": {
      "verifiedPlatform": "প্ৰমাণিত স্থানীয় কৃষি উৎপাদন মঞ্চ", "title": "আৱিষ্কাৰ কৰক। পৰীক্ষা কৰক। সংযোগ কৰক।",
      "subtitle": "কৃষক আৰু কৃষি বিষয়াসকলক স্থানীয় কৃষি সামগ্ৰীৰ প্ৰমাণিত তথ্য ৰখাত এগ্ৰিফ্ল'ই সহায় কৰে, যাৰ ফলত ক্ৰেতাসকলে সহজে স্থান আৰু শস্য অনুসৰি সামগ্ৰী বিচাৰি পায়।",
      "searchVerifiedProduce": "প্ৰমাণিত সামগ্ৰী সন্ধান কৰক", "findVerifiedProduce": "সামগ্ৰী বিচাৰক",
      "quickDiscovery": "অঞ্চল অনুসৰি দ্ৰুত সামগ্ৰী সন্ধান", "cropName": "শস্যৰ নাম",
      "cropPlaceholder": "যেনে: পিয়াঁজ, বিলাহী...", "state": "ৰাজ্য", "district": "জিলা",
      "allStates": "সকলো ৰাজ্য", "allDistricts": "সকলো জিলা", "howItWorks": "এগ্ৰিফ্ল' কেনেকৈ কাম কৰে",
      "workflowIntro": "স্থানীয় কৃষিক মুক্ত বজাৰৰ সৈতে সংযোগ কৰা এক স্বচ্ছ আৰু স্থান-ভিত্তিক পৰীক্ষণ প্ৰক্ৰিয়া।",
      "sihPlatform": "SIH মঞ্চ", "tagLine": "আৱিষ্কাৰ কৰক। পৰীক্ষা কৰক। সংযোগ কৰক।"
    },
    "howItWorks": {
      "farmerSubmission": "কৃষকৰ আবেদন",
      "farmerSubmissionDesc": "কৃষকসকলে তেওঁলোকৰ সক্ৰিয় খেতি, মাটিৰ পৰিমাণ আৰু প্ৰত্যাশিত উৎপাদনৰ বিৱৰণ স্থানীয় পৰীক্ষণৰ বাবে দাখিল কৰে।",
      "officerVerification": "বিষয়াৰ পৰীক্ষণ",
      "officerVerificationDesc": "স্থানীয় কৃষি বিষয়াসকলে আবেদনসমূহ পৰ্যালোচনা কৰে, ক্ষেত্ৰ পৰিদৰ্শন কৰে আৰু প্ৰমাণিত সামগ্ৰী প্ৰকাশ কৰে।",
      "publicDiscovery": "ৰাজহুৱা সন্ধান আৰু যোগাযোগ",
      "publicDiscoveryDesc": "ক্ৰেতাসকলে কোনো লগইন বাধা নোহোৱাকৈ শস্য, জিলা আৰু পৰিমাণ অনুসৰি প্ৰমাণিত সামগ্ৰী বিচাৰি পায়।"
    },
    "roles": {
      "farmers": "কৃষকসকলৰ বাবে", "officers": "কৃষি বিষয়াসকলৰ বাবে", "buyers": "ক্ৰেতা আৰু ব্যৱসায়ীৰ বাবে",
      "farmerTitle": "শস্যৰ প্ৰত্যক্ষ দৃশ্যমানতা", "officerTitle": "অধিকাৰক্ষেত্ৰ নিয়ন্ত্ৰণ আৰু বিশ্বাস",
      "buyerTitle": "প্ৰমাণিত যোগানৰ সন্ধান",
      "farmerItem1": "কৃষি প্ৰফাইল আৰু খেতিৰ মাটি পঞ্জীয়ন কৰক",
      "farmerItem2": "স্থানীয় পৰীক্ষণৰ বাবে প্ৰত্যাশিত উৎপাদন দাখিল কৰক",
      "farmerItem3": "প্ৰকৃত স্থিতি জানক: বাকী থকা → পৰীক্ষিত / প্রত্যাখ্যাত",
      "officerItem1": "স্থানীয় অঞ্চলৰ প্ৰমাণিত সামগ্ৰী পোনে পোনে যোগ কৰক",
      "officerItem2": "আপোনাৰ ব্লকৰ কৃষকৰ আবেদনসমূহ ক্ষেত্ৰ পৰিদৰ্শন কৰি পৰীক্ষা কৰক",
      "officerItem3": "পৰিমাণ আৰু উপলব্ধতা আপডেট কৰক",
      "buyerItem1": "লগইন নকৰাকৈয়ে সামগ্ৰী বিচাৰি পাওক",
      "buyerItem2": "ৰাজ্য, জিলা, অঞ্চল আৰু পৰিমাণ অনুসৰি ফিল্টাৰ কৰক",
      "buyerItem3": "প্ৰমাণিত যোগানকৰ্তাসকললৈ প্ৰত্যক্ষ ক্ৰয় অনুসন্ধান প্ৰেৰণ কৰক"
    },
    "produce": {
      "title": "প্ৰমাণিত সামগ্ৰী সন্ধান",
      "subtitle": "স্থানীয় কৃষি বিষয়াসকলে পৰীক্ষা কৰা উপলব্ধ আৰু আগন্তুক কৃষি সামগ্ৰী বিচাৰক।",
      "searchCropName": "শস্যৰ নাম সন্ধান কৰক", "state": "ৰাজ্য", "district": "জিলা", "areaBlock": "অঞ্চল / ব্লক",
      "minQty": "নূন্যতম পৰিমাণ (টন)", "maxQty": "সৰ্বোচ্চ পৰিমাণ (টন)", "availBefore": "উপলব্ধতা তাৰিখৰ ভিতৰত/দিনা",
      "verifiedOnly": "কেৱল প্ৰমাণিত (পৰামৰ্শিত)", "clearFilters": "ফিল্টাৰ আঁতৰাওক",
      "count": "{{count}}টা প্ৰমাণিত সামগ্ৰীৰ তথ্য দেখা গৈছে",
      "countPlural": "{{count}}টা প্ৰমাণিত সামগ্ৰীৰ তথ্য দেখা গৈছে",
      "emptyTitle": "কোনো সামগ্ৰীৰ তথ্য পোৱা নগ'ল",
      "emptyDescription": "সন্ধানৰ পৰিসৰ বৃদ্ধি কৰক বা ওচৰৰ সামগ্ৰী চাবলৈ ফিল্টাৰ আঁতৰাওক।",
      "resetAllFilters": "সকলো ফিল্টাৰ পুনৰায় ছেট কৰক", "autoSynced": "WebSocket যোগে লাইভ ছিংক কৰা হৈছে",
      "availableQuantity": "উপলব্ধ পৰিমাণ", "quality": "গুণমান", "availability": "উপলব্ধতা",
      "sourceOfficer": "বিষয়া পৰীক্ষিত", "sourceFarmer": "কৃষক পৰীক্ষিত",
      "verifiedBadge": "✓ পৰীক্ষিত", "qualityGrade": "গুণমান গ্ৰেড", "verificationSource": "পৰীক্ষণ উৎস",
      "fieldNotes": "বিষয়াৰ ক্ষেত্ৰ পৰিদৰ্শন টোকা",
      "purchaseTitle": "ক্ৰয় অনুসন্ধান / প্ৰয়োজনীয়তা প্ৰেৰণ",
      "purchaseSubtitle": "প্ৰমাণিত উৎপাদক / স্থানীয় বিষয়াৰ সৈতে পোনপটীয়া যোগাযোগৰ বাবে প্ৰয়োজনীয়তা দাখিল কৰক।",
      "yourName": "আপোনাৰ নাম / প্ৰতিষ্ঠান", "contact": "যোগাযোগ নম্বৰ / ইমেইল",
      "requestedQty": "প্ৰয়োজনীয় পৰিমাণ", "message": "বাৰ্তা / প্ৰয়োজনীয়তা", "sendRequest": "ক্ৰয় অনুৰোধ প্ৰেৰণ কৰক",
      "notFound": "সামগ্ৰীৰ তথ্য পোৱা নগ'ল", "noLogin": "লগইনৰ প্ৰয়োজন নাই", "unitLabel": "একক"
    },
    "officer": {
      "portal": "কৃষি বিষয়াৰ পৰ্টেল", "subtitle": "স্থানীয় এলেকাৰ সামগ্ৰী পৰিচালনা কৰক, কৃষকৰ আবেদন পৰীক্ষা কৰক",
      "profile": "প্রফাইল সম্পাদনা", "totalRecords": "মুঠ তথ্য", "totalRecordsHint": "আপোনাৰ নিযুক্ত অঞ্চলত",
      "availableQty": "উপলব্ধ পৰিমাণ", "availableQtyHint": "প্ৰমাণিত সামগ্ৰী", "farmerRequests": "কৃষকৰ আবেদন",
      "pending": "ক্ষেত্ৰ পৰিদৰ্শন বাকী", "verifiedRecords": "পৰীক্ষিত সামগ্ৰী", "verifiedRecordsHint": "ক্ৰেতাৰ বাবে উপলব্ধ",
      "queueTitle": "কৃষক পৰীক্ষণ অনুৰোধ", "queueSubtitle": "আপোনাৰ অঞ্চলত ক্ষেত্ৰ পৰিদৰ্শনৰ বাবে অপেক্ষাৰত কৃষকসকল",
      "queueEmpty": "সকলো কাম শেষ! কোনো বাকী আবেদন নাই।",
      "localProduceTitle": "স্থানীয় এলেকাৰ কৃষি সামগ্ৰী", "localProduceSubtitle": "আপোনাৰ এলেকাত প্ৰকাশিত সামগ্ৰীৰ তালিকা",
      "addProduce": "+ সামগ্ৰী যোগ কৰক", "editProduce": "সামগ্ৰী সম্পাদনা", "addProduceModalTitle": "+ স্থানীয় সামগ্ৰী যোগ কৰক",
      "modalSubtitle": "বিষয়াৰ দ্বাৰা পোনপটীয়াভাৱে অন্তৰ্ভুক্ত সামগ্ৰী পৰীক্ষিত বুলি গণ্য হ'ব",
      "savePublish": "সংৰক্ষণ আৰু প্ৰকাশ কৰক", "verify": "পৰীক্ষা কৰক", "reject": "প্রত্যাখ্যান কৰক",
      "pendingBadge": "🟡 পৰীক্ষা বাকী আছে", "directOfficerEntry": "বিষয়াৰ প্ৰত্যক্ষ প্রৱেশ",
      "markUnavailable": "অনুপলব্ধ বুলি চিহ্নিত কৰক", "markAvailable": "উপলব্ধ বুলি চিহ্নিত কৰক",
      "editProduceAction": "সামগ্ৰী সম্পাদনা", "deleteProduce": "তথ্য মচি পেলাওক",
      "deleteConfirm": "আপুনি নিশ্চিতভাৱে এই সামগ্ৰীৰ তথ্য মচিব বিচাৰেনে?", "rejectTitle": "কৃষকৰ আবেদন প্রত্যাখ্যান কৰক",
      "rejectDescription": "অনুগ্ৰহ কৰি প্রত্যাখ্যানৰ সঠিক কাৰণ উল্লেখ কৰক",
      "rejectionReason": "প্রত্যাখ্যানৰ কাৰণ / প্ৰয়োজনীয় সংশোধন",
      "rejectionPlaceholder": "যেনে: প্ৰত্যাশিত উৎপাদন মাটিৰ পৰিমাণৰ লগত মিলা নাই; অনুগ্ৰহ কৰি পুনৰ জুখক।",
      "confirmRejection": "প্রত্যাখ্যান নিশ্চিত কৰক", "fieldInspected": "বিষয়াৰ দ্বাৰা ক্ষেত্ৰ পৰিদৰ্শন কৰি পৰীক্ষা কৰা হৈছে",
      "verificationSuccess": "✓ কৃষকৰ আবেদন পৰীক্ষিত হ'ল আৰু ৰাজহুৱাভাৱে প্ৰকাশ পালে!",
      "rejectionSuccess": "আবেদন প্রত্যাখ্যান কৰা হ'ল আৰু কৃষকক অৱগত কৰা হ'ল।",
      "provideReason": "অনুগ্ৰহ কৰি প্রত্যাখ্যানৰ কাৰণ দিয়ক", "noProduceYet": "আপোনাৰ অঞ্চলত এতিয়ালৈকে কোনো সামগ্ৰী পঞ্জীয়ন হোৱা নাই।",
      "cropCol": "শস্য", "qtyCol": "পৰিমাণ", "locationCol": "স্থান", "availDateCol": "উপলব্ধতাৰ তাৰিখ",
      "qualityCol": "গুণমান", "sourceCol": "উৎস", "statusCol": "স্থিতি", "actionsCol": "কাৰ্য্য",
      "officerRecordedSuccess": "✓ বিষয়াৰ দ্বাৰা প্ৰত্যক্ষভাৱে পঞ্জীয়ন আৰু পৰীক্ষিত!",
      "updateProduceSuccess": "সামগ্ৰী সফলতাৰে আপডেট কৰা হ'ল"
    },
    "farmer": {
      "portal": "কৃষক পৰ্টেল", "myProfile": "মোৰ কৃষি প্রফাইল",
      "assignedOfficer": "আপোনাৰ নিযুক্ত স্থানীয় কৃষি বিষয়া", "assignedOfficerHint": "আবেদনসমূহ ইয়ালৈ প্ৰেৰণ কৰা হয়",
      "totalSubmissions": "মুঠ আবেদন", "pending": "বাকী থকা", "verified": "পৰীক্ষিত & সক্ৰিয়",
      "rejected": "প্রত্যাখ্যাত", "requestsTitle": "মোৰ শস্য পৰীক্ষণ অনুৰোধ",
      "requestsSubtitle": "স্থানীয় কৃষি বিষয়াৰ পৰা স্থিতি জানক",
      "addCrop": "+ শস্যৰ বিৱৰণ যোগ কৰক", "addCropButton": "+ শস্য যোগ কৰক", "myCropDetails": "+ কৃষি শস্যৰ বিৱৰণ যোগ কৰক",
      "submittedToOfficer": "দাখিল কৰা বিৱৰণ পৰীক্ষণৰ বাবে স্থানীয় কৃষি বিষয়ালৈ প্ৰেৰণ কৰা হ'ব",
      "submitToOfficer": "স্থানীয় বিষয়াক দাখিল কৰক", "noCrops": "এতিয়ালৈকে কোনো শস্য দাখিল কৰা নাই",
      "noCropsDescription": "স্থানীয় পৰীক্ষণৰ বাবে আপোনাৰ বৰ্তমানৰ খেতিৰ বিৱৰণ যোগ কৰক।", "addFirstCrop": "প্ৰথম শস্য যোগ কৰক",
      "pendingStatus": "🟡 পৰীক্ষা বাকী আছে", "verifiedStatus": "🟢 ✓ পৰীক্ষিত", "rejectedStatus": "🔴 প্রত্যাখ্যাত",
      "expectedHarvest": "প্ৰত্যাশিত চপোৱাৰ তাৰিখ", "cultivatedArea": "খেতি কৰা মাটি", "expectedYield": "প্ৰত্যাশিত উৎপাদন",
      "cropStage": "শস্যৰ পৰ্যায়", "officerFeedback": "বিষয়াৰ মন্তব্য:", "submissionSuccess": "✓ শস্য দাখিল হ'ল! পৰীক্ষণৰ বাবে কৃষি বিষয়ালৈ প্ৰেৰণ কৰা হ'ল।",
      "verificationStatus": "বাকী থকা → পৰীক্ষিত / প্রত্যাখ্যাত", "locationRouting": "স্থান পথনিৰ্দেশ (স্থানীয় বিষয়াৰ বাবে)",
      "additionalNotes": "অতিৰিক্ত খেতিৰ টোকা", "farmingNotesPlaceholder": "খেতি পদ্ধতি, জলসিঞ্চন, সাৰৰ বিৱৰণ..."
    },
    "profile": {
      "title": "মোৰ প্রফাইল", "subtitle": "আপোনাৰ একাউণ্টৰ তথ্য আৰু কৃষি বিৱৰণ পৰিচালনা কৰক",
      "saveChanges": "পৰিৱৰ্তনসমূহ সংৰক্ষণ কৰক", "fullName": "সম্পূৰ্ণ নাম", "village": "গাঁও",
      "area": "অঞ্চল / ব্লক", "district": "জিলা", "state": "ৰাজ্য", "landArea": "মাটিৰ পৰিমাণ",
      "landUnit": "মাটিৰ একক", "farmingType": "কৃষিৰ প্ৰকাৰ", "officialEmail": "চৰকাৰী ইমেইল",
      "designation": "বিষয়াৰ পদবী", "department": "বিভাগ", "contactNumber": "যোগাযোগ নম্বৰ",
      "assignedArea": "নিযুক্ত অঞ্চল / ব্লক", "profileUpdated": "প্রফাইল সফলতাৰে আপডেট হ'ল"
    },
    "crops": {
      "onion": "পিয়াঁজ", "tomato": "বিলাহী", "potato": "আলু", "rice": "ধান / চাউল",
      "wheat": "ঘেঁহু", "maize": "মাকৈ", "carrot": "গাজৰ", "cabbage": "বন্ধাকবি",
      "cauliflower": "ফুলকবি", "garlic": "নহৰু", "ginger": "আদা", "banana": "কল",
      "mango": "আম", "groundnut": "বাদাম", "sugarcane": "কুঁহিয়াৰ", "cotton": "কপাহ"
    },
    "produce_types": {
      "tubers": "কন্দমূল", "vegetable": "শাক-পাচলি", "vegetable_bulbs": "শাক-পাচলি / কন্দ",
      "field_crop": "পথাৰৰ শস্য", "cereals": "খাদ্যশস্য", "fruits": "ফল-মূল",
      "cash_crops": "অৰ্থকৰী শস্য", "spices": "মচলা"
    },
    "units": { "tons": "টন", "quintals": "কুইন্টল", "kg": "কিলোগ্ৰাম", "acres": "একর", "hectares": "হেক্টৰ" },
    "qualities": {
      "gradeA": "গ্ৰেড A", "gradeB": "গ্ৰেড B", "gradeC": "গ্ৰেড C",
      "gradeAPremium": "গ্ৰেড A (উন্নত)", "gradeBStandard": "গ্ৰেড B (মানক)", "gradeCFair": "গ্ৰেড C (সাধাৰণ)"
    },
    "crop_stages": {
      "bulbDevelopment": "কন্দ বৃদ্ধি", "vegetative": "শাৰীৰিক বৃদ্ধিৰ পৰ্যায়",
      "flowering": "ফুল ধৰা পৰ্যায়", "readyForHarvest": "চপোৱাৰ বাবে সাজু", "preHarvest": "চপোৱাৰ পূৰ্বৰ পৰ্যায়"
    },
    "statuses": {
      "verified": "পৰীক্ষিত", "pending": "বাকী থকা", "rejected": "প্রত্যাখ্যাত",
      "available": "উপলব্ধ", "unavailable": "অনুপলব্ধ"
    },
    "sources": {
      "officerVerified": "বিষয়া পৰীক্ষিত", "farmerVerified": "কৃষক পৰীক্ষিত",
      "directOfficerEntry": "বিষয়াৰ প্ৰত্যক্ষ প্রৱেশ"
    },
    "notifications": {
      "newProduceAdded": "🌾 নতুন সামগ্ৰী যোগ হ'ল: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 সামগ্ৰী আপডেট হ'ল: {{crop}}",
      "newFarmerSubmission": "📋 নতুন কৃষকৰ শস্য আবেদন: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ শস্য পৰীক্ষিত হ'ল: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ কৃষকৰ অনুৰোধ প্রত্যাখ্যান হ'ল: {{crop}}",
      "purchaseInquiry": "💼 ক্ৰয় অনুসন্ধান: ক্ৰেতাই {{qty}} {{unit}} {{crop}} বিচাৰিছে",
      "demoReset": "🔄 ডেমো তথ্য প্ৰাৰম্ভিক অৱস্থালৈ ঘূৰি আহিল",
      "inquirySent": "✓ ক্ৰয় অনুসন্ধান উৎপাদক / বিষয়ালৈ প্ৰেৰণ কৰা হ'ল!",
      "statusUpdated": "সামগ্ৰীৰ স্থিতি আপডেট হ'ল", "deleted": "সামগ্ৰীৰ তথ্য মচি পেলোৱা হ'ল"
    },
    "demo": {
      "controlsTitle": "SIH ডেমো নিয়ন্ত্ৰণ:", "officerBtn": "বিষয়া (ৰবি কুমাৰ)",
      "farmerBtn": "কৃষਕ (কুমাৰ)", "buyerBtn": "ৰাজহুৱা ক্ৰেতাৰ দৃশ্য",
      "resetBtn": "ডেমো ৰিছেট", "resetConfirm": "ডাটাবেছটো প্ৰাৰম্ভিক ডেমো অৱস্থালৈ ৰিছেট কৰিব বিচাৰেনে?"
    }
  },
  "ur": {
    "lang": { "name": "Urdu", "nativeName": "اردو", "code": "ur", "dir": "rtl" },
    "common": {
      "language": "زبان", "login": "لاگ ان", "register": "رجسٹر", "logout": "لاگ آؤٹ",
      "dashboard": "ڈیش بورڈ", "profile": "پروفائل", "save": "محفوظ کریں", "cancel": "منسوخ کریں",
      "close": "بند کریں", "submit": "جمع کرائیں", "refresh": "تازہ کریں", "search": "تلاش کریں",
      "clearFilters": "فلٹرز صاف کریں", "loading": "لوڈ ہو رہا ہے...", "viewDetails": "تفصیلات دیکھیں",
      "allStates": "تمام ریاستیں", "allDistricts": "تمام اضلاع", "allAreas": "تمام علاقے",
      "verified": "تصدیق شدہ", "pending": "زیر التواء", "rejected": "مسترد شدہ",
      "available": "دستیاب", "unavailable": "ناقابل دستياب", "yes": "ہاں", "no": "نہیں",
      "continue": "جاری رکھیں", "send": "بھیجیں", "back": "واپس", "next": "اگلا",
      "previous": "پچھلا", "edit": "ترمیم", "delete": "حذف کریں", "status": "حیثیت",
      "role": "کردار", "user": "صارف", "liveSync": "لائیو مطابقت پذیری", "reconnecting": "دوبارہ منسلک ہو رہا ہے...",
      "reset": "ری سیٹ", "actions": "اقدامات", "crop": "فصل", "quantity": "مقدار",
      "location": "مقام", "date": "تاریخ", "notes": "نوٹس"
    },
    "navigation": {
      "home": "ہوم", "viewProduce": "پیداوار دیکھیں", "officerPortal": "افسر پورٹل",
      "farmerPortal": "کسان پورٹل", "dashboard": "ڈیش بورڈ", "profile": "پروفائل",
      "requests": "درخواستیں", "addProduce": "پیداوار شامل کریں", "addCrop": "فصل شامل کریں",
      "myRequests": "میری درخواستیں", "farmerRequests": "کسان کی درخواستیں",
      "liveSync": "لائیو سنک", "publicBuyerView": "عوامی خریدار منظر"
    },
    "auth": {
      "roleSelector": "اپنا کردار منتخب کریں", "agricultureOfficer": "زراعت افسر", "farmer": "کسان",
      "mobileOrEmail": "موبائل نمبر یا ای میل", "password": "پاس ورڈ", "signIn": "سائن ان",
      "fullName": "پورا نام", "mobileNumber": "موبائل نمبر", "emailOptional": "ای میل (اختیاری)",
      "createAccount": "اکاؤنٹ بنائیں", "designation": "عہدہ", "department": "محکمہ",
      "assignedArea": "مقررہ علاقہ", "district": "ضلع", "state": "ریاست",
      "village": "گاؤں", "landArea": "رقبہ زمین (ایکڑ)", "farmingType": "کاشتکاری کی قسم",
      "welcomeBack": "خوش آمدید، {{name}}!", "accountCreated": "اکاؤنٹ بن گیا! خوش آمدید، {{name}}.",
      "invalidCredentials": "غلط لاگ ان تفصیلات", "requiredFields": "براہ کرم تمام مطلوبہ خانے پر کریں (نام، موبائل، پاس ورڈ)۔",
      "demoLoginFailed": "ڈیمو لاگ ان ناکام رہا", "networkError": "نیٹ ورک کی خرابی",
      "logoutSuccess": "آپ کامیابی سے لاگ آؤٹ ہو چکے ہیں۔",
      "officerLoginRequired": "افسر پورٹل استعمال کرنے کے لیے زراعت افسر کے طور پر لاگ ان کریں۔",
      "farmerLoginRequired": "کسان پورٹل استعمال کرنے کے لیے کسان کے طور پر لاگ ان کریں۔",
      "registrationFailed": "رجسٹریشن ناکام رہی۔ براہ کرم تفصیلات چیک کریں۔", "switchedRole": "{{role}} میں تبدیل کر دیا گیا"
    },
    "landing": {
      "verifiedPlatform": "تصدیق شدہ مقامی زرعی پیداوار پلیٹ فارم", "title": "دریافت کریں۔ تصدیق کریں۔ جڑیں۔",
      "subtitle": "ایگری فلو کسانوں اور زراعت افسران کو مقامی پیداوار کی تصدیق شدہ معلومات رکھنے میں مدد کرتا ہے تاکہ خریدار مقام، فصل اور مقدار کے مطابق آسانی سے تلاش کر سکیں۔",
      "searchVerifiedProduce": "تصدیق شدہ پیداوار تلاش کریں", "findVerifiedProduce": "پیداوار تلاش کریں",
      "quickDiscovery": "علاقے کے لحاظ سے فوری پیداوار تلاش", "cropName": "فصل کا نام",
      "cropPlaceholder": "مثلاً پیاز، ٹماٹر...", "state": "ریاست", "district": "ضلع",
      "allStates": "تمام ریاستیں", "allDistricts": "تمام اضلاع", "howItWorks": "ایگری فلو کیسے کام کرتا ہے",
      "workflowIntro": "مقامی زراعت کو کھلی منڈی سے جوڑنے والا ایک شفاف اور مقام پر مبنی تصدیقی عمل۔",
      "sihPlatform": "SIH پلیٹ فارم", "tagLine": "دریافت کریں۔ تصدیق کریں۔ جڑیں۔"
    },
    "howItWorks": {
      "farmerSubmission": "کسان کی اندراج",
      "farmerSubmissionDesc": "کسان اپنی کاشت کی تفصیلات، رقبہ اور متوقع پیداوار مقامی تصدیق کے لیے جمع کراتے ہیں۔",
      "officerVerification": "افسر کی تصدیق",
      "officerVerificationDesc": "مقامی زراعت افسران درخواستوں کا معائنہ کرتے ہیں، فیلڈ تصدیق کرتے ہیں اور تصدیق شدہ پیداوار شائع کرتے ہیں۔",
      "publicDiscovery": "عوامی تلاش اور رابطہ",
      "publicDiscoveryDesc": "خریدار بغیر کسی لاگ ان رکاوٹ کے فصل، ضلع اور مقدار کے مطابق تصدیق شدہ پیداوار تلاش کر سکتے ہیں۔"
    },
    "roles": {
      "farmers": "کسانوں کے لیے", "officers": "زراعت افسران کے لیے", "buyers": "خریداروں اور تاجروں کے لیے",
      "farmerTitle": "فصلوں کی براہ راست رسائی", "officerTitle": "اختیار اور اعتماد",
      "buyerTitle": "تصدیق شدہ رسد کی دریافت",
      "farmerItem1": "کاشتکاری پروفائل اور قابل کاشت زمین رجسٹر کریں",
      "farmerItem2": "مقامی تصدیق کے لیے متوقع پیداوار جمع کرائیں",
      "farmerItem3": "حقیقی وقت میں صورتحال جانیں: زیر التواء → تصدیق شدہ / مسترد",
      "officerItem1": "مقامی علاقے کی تصدیق شدہ زرعی پیداوار براہ راست درج کریں",
      "officerItem2": "اپنے بلاک کے کسانوں کی درخواستوں کی فیلڈ تصدیق کریں",
      "officerItem3": "مقدار اور دستیابی کی معلومات اپ ڈیٹ کریں",
      "buyerItem1": "بغیر لاگ ان کے فوری طور پر پیداوار تلاش کریں",
      "buyerItem2": "ریاست، ضلع، علاقہ اور مقدار کے لحاظ سے فلٹر کریں",
      "buyerItem3": "تصدیق شدہ سپلائرز کو براہ راست خریداری کی پوچھ گچھ بھیجیں"
    },
    "produce": {
      "title": "تصدیق شدہ پیداوار کی تلاش",
      "subtitle": "مقامی زراعت افسران کی تصدیق شدہ دستیاب اور آنے والی زرعی پیداوار تلاش کریں۔",
      "searchCropName": "فصل کا نام تلاش کریں", "state": "ریاست", "district": "ضلع", "areaBlock": "علاقہ / بلاک",
      "minQty": "کم از کم مقدار (ٹن)", "maxQty": "زیادہ سے زیادہ مقدار (ٹن)", "availBefore": "دستیابی تاریخ تک/کو",
      "verifiedOnly": "صرف تصدیق شدہ (تجویز کردہ)", "clearFilters": "فلٹرز صاف کریں",
      "count": "{{count}} تصدیق شدہ پیداوار ریکارڈ دکھایا جا رہا ہے",
      "countPlural": "{{count}} تصدیق شدہ پیداوار ریکارڈز دکھائے جا رہے ہیں",
      "emptyTitle": "کوئی پیداوار ریکارڈ نہیں ملا",
      "emptyDescription": "اپنی تلاش کو وسعت دیں یا قریبی علاقوں کی دیگر فصلیں دیکھنے کے لیے فلٹرز صاف کریں۔",
      "resetAllFilters": "تمام فلٹرز ری سیٹ کریں", "autoSynced": "WebSocket کے ذریعے لائیو مطابقت پذیر",
      "availableQuantity": "دستیاب مقدار", "quality": "معیار", "availability": "دستیابی",
      "sourceOfficer": "افسر سے تصدیق شدہ", "sourceFarmer": "کسان سے تصدیق شدہ",
      "verifiedBadge": "✓ تصدیق شدہ", "qualityGrade": "معیار کا گریڈ", "verificationSource": "تصدیق کا ذریعہ",
      "fieldNotes": "افسر کے فیلڈ نوٹس اور معائنہ",
      "purchaseTitle": "خریداری کی پوچھ گچھ / طلب بھیجیں",
      "purchaseSubtitle": "تصدیق شدہ کسان / مقامی افسر سے براہ راست جڑنے کے لیے اپنی ضرورت جمع کرائیں۔",
      "yourName": "آپ کا نام / کمپنی", "contact": "رابطہ نمبر / ای میل",
      "requestedQty": "مطلوبہ مقدار", "message": "پیغام / ضروریات", "sendRequest": "خریداری کی درخواست بھیجیں",
      "notFound": "پیداوار ریکارڈ نہیں ملا", "noLogin": "لاگ ان درکار نہیں", "unitLabel": "اکائی"
    },
    "officer": {
      "portal": "زراعت افسر پورٹل", "subtitle": "مقامی پیداوار کا انتظام کریں اور کسانوں کی درخواستوں کی تصدیق کریں",
      "profile": "پروفائل میں ترمیم کریں", "totalRecords": "کل ریکارڈز", "totalRecordsHint": "آپ کے علاقے میں",
      "availableQty": "دستیاب مقدار", "availableQtyHint": "تصدیق شدہ پیداوار", "farmerRequests": "کسان کی درخواستیں",
      "pending": "فیلڈ تصدیق باقی ہے", "verifiedRecords": "تصدیق شدہ ریکارڈز", "verifiedRecordsHint": "خریداروں کے لیے دستیاب",
      "queueTitle": "کسان تصدیق کی درخواستیں", "queueSubtitle": "آپ کے علاقے میں فیلڈ تصدیق کے منتظر کسان",
      "queueEmpty": "تمام کام مکمل! کوئی زیر التواء درخواست نہیں ہے۔",
      "localProduceTitle": "مقامی علاقے کی زرعی پیداوار", "localProduceSubtitle": "آپ کے دائرہ اختیار میں درج شدہ پیداوار",
      "addProduce": "+ پیداوار شامل کریں", "editProduce": "پیداوار میں ترمیم کریں", "addProduceModalTitle": "+ مقامی پیداوار شامل کریں",
      "modalSubtitle": "افسر کے ذریعے براہ راست درج کردہ پیداوار تصدیق شدہ شمار ہوگی",
      "savePublish": "محفوظ کریں اور شائع کریں", "verify": "تصدیق کریں", "reject": "مسترد کریں",
      "pendingBadge": "🟡 تصدیق باقی ہے", "directOfficerEntry": "افسر کا براہ راست اندراج",
      "markUnavailable": "ناقابل دستياب نشان زد کریں", "markAvailable": "دستیاب نشان زد کریں",
      "editProduceAction": "پیداوار میں ترمیم کریں", "deleteProduce": "ریکارڈ حذف کریں",
      "deleteConfirm": "کیا آپ واقعی یہ پیداوار ریکارڈ حذف کرنا چاہتے ہیں؟", "rejectTitle": "کسان کی درخواست مسترد کریں",
      "rejectDescription": "براہ کرم مسترد کرنے کی تعمیری وجہ فراہم کریں",
      "rejectionReason": "مسترد کرنے کی وجہ / درکار درستی",
      "rejectionPlaceholder": "مثلاً متوقع پیداوار رقبہ زمین سے میل نہیں کھاتی؛ براہ کرم دوبارہ ناپیں۔",
      "confirmRejection": "مسترد کی تصدیق کریں", "fieldInspected": "افسر کی جانب سے موقع پر تصدیق شدہ",
      "verificationSuccess": "✓ کسان کی درخواست تصدیق ہو کر عوام کے لیے شائع کر دی گئی!",
      "rejectionSuccess": "درخواست مسترد کر دی گئی اور کسان کو مطلع کر دیا گیا۔",
      "provideReason": "براہ کرم مسترد کرنے کی وجہ بتائیں", "noProduceYet": "آپ کے علاقے میں ابھی کوئی پیداوار درج نہیں کی گئی۔",
      "cropCol": "فصل", "qtyCol": "مقدار", "locationCol": "مقام", "availDateCol": "دستیابی تاریخ",
      "qualityCol": "معیار", "sourceCol": "ذریعہ", "statusCol": "حیثیت", "actionsCol": "اقدامات",
      "officerRecordedSuccess": "✓ افسر کی جانب سے براہ راست درج اور تصدیق شدہ!",
      "updateProduceSuccess": "پیداوار کامیابی سے اپ ڈیٹ ہو گئی"
    },
    "farmer": {
      "portal": "کسان پورٹل", "myProfile": "میری زراعتی پروفائل",
      "assignedOfficer": "آپ کے مقررہ مقامی زراعت افسر", "assignedOfficerHint": "درخواستیں یہاں بھیجی جاتی ہیں",
      "totalSubmissions": "کل درخواستیں", "pending": "زیر التواء", "verified": "تصدیق شدہ اور فعال",
      "rejected": "مسترد شدہ", "requestsTitle": "میری فصل تصدیق کی درخواستیں",
      "requestsSubtitle": "اپنے مقامی زراعت افسر سے پیش رفت معلوم کریں",
      "addCrop": "+ فصل کی تفصیل شامل کریں", "addCropButton": "+ فصل شامل کریں", "myCropDetails": "+ کاشتکاری فصل کی تفصیل درج کریں",
      "submittedToOfficer": "جمع کرائی گئی تفصیلات تصدیق کے لیے آپ کے مقامی زراعت افسر کو بھیجی جائیں گی",
      "submitToOfficer": "مقامی افسر کو جمع کرائیں", "noCrops": "ابھی تک کوئی فصل جمع نہیں کرائی گئی",
      "noCropsDescription": "مقامی تصدیق کے لیے اپنی موجودہ کاشت کی تفصیلات شامل کریں۔", "addFirstCrop": "پہلی فصل شامل کریں",
      "pendingStatus": "🟡 تصدیق باقی ہے", "verifiedStatus": "🟢 ✓ تصدیق شدہ", "rejectedStatus": "🔴 مسترد شدہ",
      "expectedHarvest": "متوقع کٹائی", "cultivatedArea": "کاشت شدہ رقبہ", "expectedYield": "متوقع پیداوار",
      "cropStage": "فصل کا مرحلہ", "officerFeedback": "افسر کی رائے:", "submissionSuccess": "✓ فصل جمع ہو گئی! تصدیق کے لیے زراعت افسر کو بھیج دی گئی۔",
      "verificationStatus": "زیر التواء → تصدیق شدہ / مسترد", "locationRouting": "مقام کی رہنمائی (مقامی افسر کے لیے)",
      "additionalNotes": "اضافی زراعتی نوٹس", "farmingNotesPlaceholder": "کاشتکاری کے طریقے، آبپاشی، کھاد کی تفصیلات..."
    },
    "profile": {
      "title": "میری پروفائل", "subtitle": "اپنے اکاؤنٹ کی معلومات اور کاشتکاری کی تفصیلات کا انتظام کریں",
      "saveChanges": "تبدیلیاں محفوظ کریں", "fullName": "پورا نام", "village": "گاؤں",
      "area": "علاقہ / بلاک", "district": "ضلع", "state": "ریاست", "landArea": "رقبہ زمین",
      "landUnit": "زمین کی اکائی", "farmingType": "کاشتکاری کی قسم", "officialEmail": "سرکاری ای میل",
      "designation": "افسر کا عہدہ", "department": "محکمہ", "contactNumber": "رابطہ نمبر",
      "assignedArea": "مقررہ علاقہ / بلاک", "profileUpdated": "پروفائل کامیابی سے اپ ڈیٹ ہو گئی"
    },
    "crops": {
      "onion": "پیاز", "tomato": "ٹماٹر", "potato": "آلو", "rice": "دھان / چاول",
      "wheat": "گندم", "maize": "مکئی", "carrot": "گاجر", "cabbage": "بند گوبھی",
      "cauliflower": "پھول گوبھی", "garlic": "لہسن", "ginger": "ادرک", "banana": "کیلا",
      "mango": "آم", "groundnut": "مونگ پھلی", "sugarcane": "گنا", "cotton": "کپاس"
    },
    "produce_types": {
      "tubers": "جڑ والی فصلیں", "vegetable": "سبزی", "vegetable_bulbs": "سبزی / جڑ",
      "field_crop": "کھیت کی فصل", "cereals": "اناج", "fruits": "پھل",
      "cash_crops": "نقد آور فصلیں", "spices": "مصالحہ جات"
    },
    "units": { "tons": "ٹن", "quintals": "کوئنٹل", "kg": "کلوگرام", "acres": "ایکڑ", "hectares": "ہیکٹر" },
    "qualities": {
      "gradeA": "گریڈ A", "gradeB": "گریڈ B", "gradeC": "گریڈ C",
      "gradeAPremium": "گریڈ A (اعلیٰ)", "gradeBStandard": "گریڈ B (معیاری)", "gradeCFair": "گریڈ C (درمیانہ)"
    },
    "crop_stages": {
      "bulbDevelopment": "جڑ کی نشوونما", "vegetative": "نشوونما کا مرحلہ",
      "flowering": "پھول آنے کا مرحلہ", "readyForHarvest": "کٹائی کے لیے تیار", "preHarvest": "کٹائی سے قبل"
    },
    "statuses": {
      "verified": "تصدیق شدہ", "pending": "زیر التواء", "rejected": "مسترد شدہ",
      "available": "دستیاب", "unavailable": "ناقابل دستياب"
    },
    "sources": {
      "officerVerified": "افسر سے تصدیق شدہ", "farmerVerified": "کسان سے تصدیق شدہ",
      "directOfficerEntry": "افسر کا براہ راست اندراج"
    },
    "notifications": {
      "newProduceAdded": "🌾 نئی پیداوار شامل کی گئی: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 پیداوار اپ ڈیٹ ہوئی: {{crop}}",
      "newFarmerSubmission": "📋 کسان کی نئی درخواست: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ فصل تصدیق شدہ: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ کسان کی درخواست مسترد: {{crop}}",
      "purchaseInquiry": "💼 خریداری کی پوچھ گچھ: خریدار نے {{qty}} {{unit}} {{crop}} طلب کیا ہے",
      "demoReset": "🔄 ڈیمو ڈیٹا دوبارہ ترتیب دیا گیا",
      "inquirySent": "✓ خریداری کی پوچھ گچھ کسان / افسر کو بھیج دی گئی!",
      "statusUpdated": "پیداوار کی حیثیت اپ ڈیٹ ہو گئی", "deleted": "پیداوار ریکارڈ حذف کر دیا گیا"
    },
    "demo": {
      "controlsTitle": "SIH ڈیمو کنٹرولز:", "officerBtn": "افسر (روی کمار)",
      "farmerBtn": "کسان (کمار)", "buyerBtn": "عوامی خریدار منظر",
      "resetBtn": "ڈیمو ری سیٹ", "resetConfirm": "کیا آپ ڈیٹا بیس کو ابتدائی ڈیمو حالت میں ری سیٹ کرنا چاہتے ہیں؟"
    }
  },
  "sd": {
    "lang": { "name": "Sindhi", "nativeName": "سنڌي", "code": "sd", "dir": "rtl" },
    "common": {
      "language": "ٻولي", "login": "لاگ ان", "register": "رجسٽر", "logout": "لاگ آئوٽ",
      "dashboard": "ڊيش بورڊ", "profile": "پروفائل", "save": "محفوظ ڪريو", "cancel": "رد ڪريو",
      "close": "بند ڪريو", "submit": "جمع ڪرايو", "refresh": "تازو ڪريو", "search": "ڳولھيو",
      "clearFilters": "فلٽر صاف ڪريو", "loading": "لوڊ ٿي رھيو آھي...", "viewDetails": "تفصيل ڏسو",
      "allStates": "سمورا صوبا/ریاستون", "allDistricts": "سمورا ضلعا", "allAreas": "سمورا علائقا",
      "verified": "تصديق ٿيل", "pending": "باقي", "rejected": "رد ٿيل",
      "available": "دستياب", "unavailable": "غير دستياب", "yes": "ها", "no": "نه",
      "continue": "جاري رکو", "send": "موڪليو", "back": "واپس", "next": "اڳيون",
      "previous": "پوئيون", "edit": "ترميم", "delete": "ختم ڪريو", "status": "حيثيت",
      "role": "ڪردار", "user": "صارف", "liveSync": "لائيو سنڪ", "reconnecting": "ٻيهر ڳنڍجي رهيو آهي...",
      "reset": "ري سيٽ", "actions": "عمل", "crop": "فصل", "quantity": "مقدار",
      "location": "جڳھ", "date": "تاريخ", "notes": "نوٽس"
    },
    "navigation": {
      "home": "مک صفحو", "viewProduce": "پيداوار ڏسو", "officerPortal": "آفيسر پورٽل",
      "farmerPortal": "ھاري پورٽل", "dashboard": "ڊيش بورڊ", "profile": "پروفائل",
      "requests": "درخواستون", "addProduce": "پيداوار شامل ڪريو", "addCrop": "فصل شامل ڪريو",
      "myRequests": "منھنجون درخواستون", "farmerRequests": "ھاري درخواستون",
      "liveSync": "لائيو سنڪ", "publicBuyerView": "عوامي خريدار ڏيک"
    },
    "auth": {
      "roleSelector": "پنهنجو ڪردار چونڊيو", "agricultureOfficer": "زراعت آفيسر", "farmer": "ھاري",
      "mobileOrEmail": "موبائل نمبر يا اي ميل", "password": "پاس ورڊ", "signIn": "سائن ان",
      "fullName": "پورو نالو", "mobileNumber": "موبائل نمبر", "emailOptional": "اي ميل (اختیاري)",
      "createAccount": "اکائونٽ ٺاهيو", "designation": "عھدو", "department": "شعبو",
      "assignedArea": "مقرر ڪيل علائقو", "district": "ضلعو", "state": "رياست",
      "village": "ڳوٺ", "landArea": "زمين جو علائقو (ايڪڙ)", "farmingType": "کاشتڪاري جو قسم",
      "welcomeBack": "ڀلي ڪري آيا، {{name}}!", "accountCreated": "اکائونٽ ٺهي ويو! ڀلي ڪري آيا، {{name}}.",
      "invalidCredentials": "غلط لاگ ان تفصيل", "requiredFields": "مهرباني ڪري سڀ ضروري خانا ڀريو (نالو، موبائل، پاس ورڊ).",
      "demoLoginFailed": "ڊيمو لاگ ان ناڪام ٿيو", "networkError": "نيٽ ورڪ خرابي",
      "logoutSuccess": "توهان ڪاميابيءَ سان سائن آئوٽ ٿي ويا آهيو.",
      "officerLoginRequired": "آفيسر پورٽل واપરڻ لاءِ زراعت آفيسر طور لاگ ان ٿيو.",
      "farmerLoginRequired": "ھاري پورٽل واپرڻ لاءِ ھاري طور لاگ ان ٿيو.",
      "registrationFailed": "رجسٽريشن ناڪام وئي. مهرباني ڪري تفصيل چڪاسيو.", "switchedRole": "{{role}} ۾ تبديل ٿي ويو"
    },
    "landing": {
      "verifiedPlatform": "تصديق ٿيل مقامي زرعي پيداوار پليٽ فارم", "title": "دریافت ڪريو. تصدیق ڪريو. ڳنڍجو.",
      "subtitle": "ايگري فلو هارين ۽ زرعي آفيسرن کي مقامي پيداوار جي تصديق ٿيل معلومات رکڻ ۾ مدد ڪري ٿو ته جيئن خريدار علائقي ۽ فصل مطابق سولائي سان ڳولي سگهن.",
      "searchVerifiedProduce": "تصدیق ٿيل پيداوار ڳولھيو", "findVerifiedProduce": "پيداوار ڳولھيو",
      "quickDiscovery": "علائقي موجب تڪڙي فصل ڳولا", "cropName": "فصل جو نالو",
      "cropPlaceholder": "مثال طور پصر، ٽماٽو...", "state": "رياست", "district": "ضلعو",
      "allStates": "سمورا صوبا/ریاستون", "allDistricts": "سمورا ضلعا", "howItWorks": "ايگري فلو ڪيئن ڪم ڪري ٿو",
      "workflowIntro": "مقامي زراعت کي کليل منڊي سان ڳنڍيندڙ هڪ شفاف تصديقي عمل.",
      "sihPlatform": "SIH پليٽ فارم", "tagLine": "دریافت ڪريو. تصدیق ڪريو. ڳنڍجو."
    },
    "howItWorks": {
      "farmerSubmission": "ھاري جي داخلا",
      "farmerSubmissionDesc": "ھاري پنهنجي فعال پوک، زمين جي ماپ ۽ متوقع پيداوار مقامي تصديق لاءِ جمع ڪرائين ٿا.",
      "officerVerification": "آفيسر جي تصديق",
      "officerVerificationDesc": "مقامي زراعت آفيسر درخواستن جو جائزو وٺن ٿا، زميني معائنو ڪن ٿا ۽ تصديق ٿيل فصل شايع ڪن ٿا.",
      "publicDiscovery": "عوامي ڳولا ۽ رابطو",
      "publicDiscoveryDesc": "خريدار بغير ڪنهن لاگ ان جي فصل، ضلعي ۽ مقدار مطابق پيداوار ڳولي سگهن ٿا."
    },
    "roles": {
      "farmers": "هارين لاءِ", "officers": "زراعت آفيسرن لاءِ", "buyers": "خريدارن ۽ واپارين لاءِ",
      "farmerTitle": "فصلن جي سڌي سڃاڻپ", "officerTitle": "اختيار ۽ اعتماد",
      "buyerTitle": "تصديق ٿيل سپلائي جي ڳولا",
      "farmerItem1": "کاشتڪاري پروفائل ۽ زمين رجسٽر ڪريو",
      "farmerItem2": "مقامي تصديق لاءِ ايندڙ فصل جي پيداوار جمع ڪريو",
      "farmerItem3": "حقيقي وقت واري حيثيت ڄاڻو: باقي → تصديق ٿيل / رد ٿيل",
      "officerItem1": "مقامي علائقي جي تصديق ٿيل پيداوار سڌي طرح داخل ڪريو",
      "officerItem2": "پنهنجي بلاڪ جي هارين جي درخواستن جو فيلڊ معائنو ڪريو",
      "officerItem3": "مقدار ۽ دستيابي جا تفصيل اپڊيٽ ڪريو",
      "buyerItem1": "بغير لاگ ان جي ترت پيداوار ڳولھيو",
      "buyerItem2": "رياست، ضلعي، علائقي ۽ مقدار مطابق فلٽر ڪريو",
      "buyerItem3": "تصديق ٿيل سپلائرز کي سڌي طرح خريداري پڇا ڳاڇا موڪليو"
    },
    "produce": {
      "title": "تصديق ٿيل پيداوار جي ڳولا",
      "subtitle": "مقامي زراعت آفيسرن پاران تصديق ٿيل دستياب ۽ ايندڙ زرعي پيداوار ڳولھيو.",
      "searchCropName": "فصل جو نالو ڳولھيو", "state": "رياست", "district": "ضلعو", "areaBlock": "علائقو / بلاڪ",
      "minQty": "گھٽ ۾ گھٽ مقدار (ٽن)", "maxQty": "وڌ ۾ وڌ مقدار (ٽن)", "availBefore": "دستيابي تاريخ تائين/تي",
      "verifiedOnly": "صرف تصديق ٿيل (تجويز ڪيل)", "clearFilters": "فلٽر صاف ڪريو",
      "count": "{{count}} تصديق ٿيل پيداوار رڪارڊ ڏيکاريو پيو وڃي",
      "countPlural": "{{count}} تصديق ٿيل پيداوار رڪارڊ ڏيکاريا پيا وڃن",
      "emptyTitle": "ڪو به پيداوار رڪارڊ نه مليو",
      "emptyDescription": "پنهنجي ڳولا کي وسيع ڪريو يا ٻيا فصل ڏسڻ لاءِ فلٽر صاف ڪريو.",
      "resetAllFilters": "سمورا فلٽر ري سيٽ ڪريو", "autoSynced": "WebSocket ذريعي لائيو هم وقت سازي",
      "availableQuantity": "دستياب مقدار", "quality": "معيار", "availability": "دستيابي",
      "sourceOfficer": "آفيسر تصديق ٿيل", "sourceFarmer": "ھاري تصديق ٿيل",
      "verifiedBadge": "✓ تصديق ٿيل", "qualityGrade": "معيار جو گريڊ", "verificationSource": "تصديق جو ذريعو",
      "fieldNotes": "آفيسر جا فيلڊ معائني نوٽس",
      "purchaseTitle": "خريداري پڇا ڳاڇا / گهرજ موڪليو",
      "purchaseSubtitle": "تصديق ٿيل پوکيندڙ / مقامي آفيسر سان رابطي لاءِ پنهنجي ضرورت جمع ڪريو.",
      "yourName": "توهان جو نالو / ڪمپني", "contact": "رابطي نمبر / اي ميل",
      "requestedQty": "گهربل مقدار", "message": "پيغام / گهرجون", "sendRequest": "خريداري درخواست موڪليو",
      "notFound": "پيداوار رڪارڊ نه مليو", "noLogin": "لاگ ان جي ضرورت ناهي", "unitLabel": "ايڪم"
    },
    "officer": {
      "portal": "زراعت آفيسر پورٽل", "subtitle": "مقامي پيداوار سنڀاليو ۽ هارين جي درخواستن جي تصديق ڪريو",
      "profile": "پروفائل ترميم ڪريو", "totalRecords": "ڪل رڪارڊ", "totalRecordsHint": "توهان جي علائقي ۾",
      "availableQty": "دستياب مقدار", "availableQtyHint": "تصديق ٿيل پيداوار", "farmerRequests": "ھاري جون درخواستون",
      "pending": "فيلڊ تصديق باقي آهي", "verifiedRecords": "تصديق ٿيل رڪارڊ", "verifiedRecordsHint": "خريدارن لاءِ دستياب",
      "queueTitle": "هارين جي تصديقي درخواستون", "queueSubtitle": "توهان جي علائقي ۾ تصديق جا منتظر هاري",
      "queueEmpty": "سڀ ڪم مڪمل! ڪا به باقي درخواست ناهي.",
      "localProduceTitle": "مقامي علائقي جي زرعي پيداوار", "localProduceSubtitle": "توهان جي دائرہ اختيار ۾ شايع ٿيل پيداوار",
      "addProduce": "+ پيداوار شامل ڪريو", "editProduce": "پيداوار ترميم ڪريو", "addProduceModalTitle": "+ مقامي پيداوار شامل ڪريو",
      "modalSubtitle": "آفيسر پاران سڌي طرح داخل ڪيل پيداوار تصديق ٿيل سمجهي ويندي",
      "savePublish": "محفوظ ڪريو ۽ شايع ڪريو", "verify": "تصديق ڪريو", "reject": "رد ڪريو",
      "pendingBadge": "🟡 تصديق باقي آهي", "directOfficerEntry": "آفيسر جو سڌو اندراج",
      "markUnavailable": "غير دستياب نشان لڳايو", "markAvailable": "دستياب نشان لڳايو",
      "editProduceAction": "پيداوار ترميم ڪريو", "deleteProduce": "رڪارڊ ختم ڪريو",
      "deleteConfirm": "ڇا توهان پڪ سان هي رڪارڊ ختم ڪرڻ چاهيو ٿا؟", "rejectTitle": "هارين جي درخواست رد ڪريو",
      "rejectDescription": "مهرباني ڪري رد ڪرڻ جو مناسب سبب ڏيو",
      "rejectionReason": "رد ڪرڻ جو سبب / سڌارو گهربل",
      "rejectionPlaceholder": "مثال طور متوقع پيداوار زمين جي ماپ مطابق ناهي؛ مهرباني ڪري ٻيهر ماپيو.",
      "confirmRejection": "رد جي تصديق ڪريو", "fieldInspected": "آفيسر پاران زميني معائنو ڪري تصديق ڪئي وئي",
      "verificationSuccess": "✓ هاري جي درخواست تصديق ٿي عام ڏيک لاءِ شايع ٿي وئي!",
      "rejectionSuccess": "درخواست رد ڪئي وئي ۽ هاري کي اطلاع ڏنو ويو.",
      "provideReason": "مهرباني ڪري رد ڪرڻ جو سبب ڏيو", "noProduceYet": "توهان جي علائقي ۾ اڃا ڪا پيداوار درج نه ٿي آهي.",
      "cropCol": "فصل", "qtyCol": "مقدار", "locationCol": "جڳھ", "availDateCol": "دستيابي تاريخ",
      "qualityCol": "معيار", "sourceCol": "ذريعو", "statusCol": "حيثيت", "actionsCol": "عمل",
      "officerRecordedSuccess": "✓ آفيسر پاران سڌي طرح داخل ۽ تصديق ٿيل!",
      "updateProduceSuccess": "پيداوار ڪاميابيءَ سان اپڊيٽ ٿي وئي"
    },
    "farmer": {
      "portal": "ھاري پورٽل", "myProfile": "منهنجي زرعي پروفائل",
      "assignedOfficer": "توهان جو مقرر ڪيل مقامي زراعت آفيسر", "assignedOfficerHint": "درخواستون هتي موڪليون وڃن ٿيون",
      "totalSubmissions": "ڪل درخواستون", "pending": "باقي", "verified": "تصديق ٿيل ۽ فعال",
      "rejected": "رد ٿيل", "requestsTitle": "منهنجون فصل تصديقي درخواستون",
      "requestsSubtitle": "پنهنجي مقامي زراعت آفيسر کان حيثيت ڄاڻو",
      "addCrop": "+ فصل تفصيل شامل ڪريو", "addCropButton": "+ فصل شامل ڪريو", "myCropDetails": "+ پوکيل فصل جا تفصيل شامل ڪريو",
      "submittedToOfficer": "جمع ڪيل تفصيل تصديق لاءِ توهان جي مقامي زراعت آفيسر ڏانهن موڪليا ويندا",
      "submitToOfficer": "مقامي آفيسر کي جمع ڪريو", "noCrops": "اڃا تائين ڪو فصل جمع نه ڪرايو ويو آهي",
      "noCropsDescription": "مقامي تصديق لاءِ پنهنجي موجوده پوک جا تفصيل شامل ڪريو.", "addFirstCrop": "پهريون فصل شامل ڪريو",
      "pendingStatus": "🟡 تصديق باقي آهي", "verifiedStatus": "🟢 ✓ تصديق ٿيل", "rejectedStatus": "🔴 رد ٿيل",
      "expectedHarvest": "متوقع لڻڻ جي تاريخ", "cultivatedArea": "پوکيل علائقو", "expectedYield": "متوقع پيداوار",
      "cropStage": "فصل جو مرحلو", "officerFeedback": "آفيسر جو رايو:", "submissionSuccess": "✓ فصل جمع ٿي ويو! تصديق لاءِ زراعت آفيسر ڏانهن موڪليو ويو.",
      "verificationStatus": "باقي → تصديق ٿيل / رد ٿيل", "locationRouting": "مقام جي هدايت (مقامي آفيسر لاءِ)",
      "additionalNotes": "اضافي زرعي نوٽس", "farmingNotesPlaceholder": "پوک جا طريقا، پاڻي، ڀاڻ جا تفصيل..."
    },
    "profile": {
      "title": "منهنجي پروفائل", "subtitle": "پنهنجي کاتي جي معلومات ۽ زراعت جا تفصيل سنڀاليو",
      "saveChanges": "تبديليون محفوظ ڪريو", "fullName": "پورو نالو", "village": "ڳوٺ",
      "area": "علائقو / بلاڪ", "district": "ضلعو", "state": "رياست", "landArea": "زمين جو علائقو",
      "landUnit": "زمين جو ايڪم", "farmingType": "کاشتڪاري جو قسم", "officialEmail": "سرڪاري اي ميل",
      "designation": "آفيسر جو عھدو", "department": "شعبو", "contactNumber": "رابطي نمبر",
      "assignedArea": "مقرر علائقو / بلاڪ", "profileUpdated": "پروفائل ڪاميابيءَ سان اپڊيٽ ٿي وئي"
    },
    "crops": {
      "onion": "بصر / پصل", "tomato": "ٽماٽو", "potato": "پٽاٽو", "rice": "چانور / ڊانگر",
      "wheat": "ڪڻڪ", "maize": "مکئي", "carrot": "گاجਰ", "cabbage": "بند گوبھی",
      "cauliflower": "ڦل گوبھی", "garlic": "ٿوم", "ginger": "ادرڪ", "banana": "ڪيلو",
      "mango": "انب", "groundnut": "مڱيرا", "sugarcane": "ڪمند", "cotton": "ڪپهه"
    },
    "produce_types": {
      "tubers": "پاڙ وارا فصل", "vegetable": "ڀاڄي", "vegetable_bulbs": "ڀاڄي / پاڙ",
      "field_crop": "کيت جو فصل", "cereals": "اناج", "fruits": "ميوا",
      "cash_crops": "نقد فصل", "spices": "مصالحا"
    },
    "units": { "tons": "ٽن", "quintals": "ڪوئينٽل", "kg": "ڪلو", "acres": "ايڪڙ", "hectares": "هيڪٽر" },
    "qualities": {
      "gradeA": "گريڊ A", "gradeB": "گريڊ B", "gradeC": "گريڊ C",
      "gradeAPremium": "گريڊ A (بهترين)", "gradeBStandard": "گريڊ B (معياري)", "gradeCFair": "گريڊ C (مناسب)"
    },
    "crop_stages": {
      "bulbDevelopment": "پاڙ جو واڌارو", "vegetative": "واڌ ويجهه جو مرحلو",
      "flowering": "گل اچڻ جو مرحلو", "readyForHarvest": "لڻڻ لاءِ تيار", "preHarvest": "لڻڻ کان اڳ وارو مرحلو"
    },
    "statuses": {
      "verified": "تصديق ٿيل", "pending": "باقي", "rejected": "رد ٿيل",
      "available": "دستياب", "unavailable": "غير دستياب"
    },
    "sources": {
      "officerVerified": "آفيسر تصديق ٿيل", "farmerVerified": "ھاري تصديق ٿيل",
      "directOfficerEntry": "آفيسر جو سڌو اندراج"
    },
    "notifications": {
      "newProduceAdded": "🌾 نئين پيداوار شامل ٿي: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "produceUpdated": "🔄 پيداوار اپڊيٽ ٿي: {{crop}}",
      "newFarmerSubmission": "📋 هاري پاران نئين درخواست: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "cropVerified": "✅ فصل تصديق ٿيل: {{crop}} ({{qty}} {{unit}}) - {{area}}",
      "farmerRequestRejected": "⚠️ هاري جي درخواست رد: {{crop}}",
      "purchaseInquiry": "💼 خريداري پڇا ڳاڇا: خريدار پاران {{qty}} {{unit}} {{crop}} جي گهر",
      "demoReset": "🔄 ڊيمو ڊيٽا اصل حالت ۾ بحال ٿي ويو",
      "inquirySent": "✓ خريداري پڇا ڳاڇا هاري / آفيسر ڏانهن موڪلي وئي!",
      "statusUpdated": "پيداوار جي حيثيت اپڊيٽ ٿي", "deleted": "پيداوار رڪارڊ ختم ٿي ويو"
    },
    "demo": {
      "controlsTitle": "SIH ڊيمو ڪنٽرولز:", "officerBtn": "آفيسر (روي ڪمار)",
      "farmerBtn": "ھاري (ڪمار)", "buyerBtn": "عوامي خريدار ڏيک",
      "resetBtn": "ڊيمو ري سيٽ", "resetConfirm": "ڇا توهان ڊيٽابيس کي اصل ڊيمو حالت ۾ ري سيٽ ڪرڻ چاهيو ٿا؟"
    }
  }
}
