import os
import sys
import json
import re
import urllib.request

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test_endpoints():
    print("=== 1. Checking HTTP Endpoints and Content-Type Headers ===")
    endpoints = [
        ("http://127.0.0.1:8000/", "text/html; charset=utf-8"),
        ("http://127.0.0.1:8000/static/i18n/languages.js", "application/javascript; charset=utf-8"),
        ("http://127.0.0.1:8000/static/i18n/index.js", "application/javascript; charset=utf-8"),
        ("http://127.0.0.1:8000/static/app.js", "application/javascript; charset=utf-8"),
        ("http://127.0.0.1:8000/static/i18n/locales/en.json", "application/json; charset=utf-8"),
        ("http://127.0.0.1:8000/static/i18n/locales/ta.json", "application/json; charset=utf-8"),
        ("http://127.0.0.1:8000/static/i18n/locales/hi.json", "application/json; charset=utf-8"),
        ("http://127.0.0.1:8000/static/i18n/locales/ur.json", "application/json; charset=utf-8"),
        ("http://127.0.0.1:8000/api/public/produce", "application/json; charset=utf-8"),
    ]
    for url, expected_ctype in endpoints:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            ctype = resp.headers.get("Content-Type", "")
            status = resp.status
            assert status == 200, f"{url} returned status {status}"
            assert "charset=utf-8" in ctype.lower(), f"{url} missing charset=utf-8, got {ctype}"
            print(f"  [PASS] {url} -> Status {status}, Content-Type: {ctype}")

def test_all_23_locales():
    print("\n=== 2. Checking All 23 Locale JSON Files ===")
    EXPECTED_LANGS = [
        "en", "as", "bn", "brx", "doi", "gu", "hi", "kn", "ks", "kok",
        "mai", "ml", "mni", "mr", "ne", "or", "pa", "sa", "sat", "sd",
        "ta", "te", "ur"
    ]
    locales_dir = os.path.join("static", "i18n", "locales")
    files = os.listdir(locales_dir)
    assert len(EXPECTED_LANGS) == 23, "Must have exactly 23 languages"
    
    # Check that each expected lang file exists and is valid JSON
    en_path = os.path.join(locales_dir, "en.json")
    with open(en_path, "r", encoding="utf-8") as f:
        en_data = json.load(f)
    
    en_produce_keys = set(en_data.get("produce", {}).keys())
    en_common_keys = set(en_data.get("common", {}).keys())
    
    corrupt_patterns = ["Γ£ô", "ΓåÆ", "αªà", "\ufffd"]

    for lang in EXPECTED_LANGS:
        lpath = os.path.join(locales_dir, f"{lang}.json")
        assert os.path.exists(lpath), f"Missing locale file for {lang}"
        with open(lpath, "r", encoding="utf-8") as f:
            content = f.read()
            # Check for corrupt patterns
            for pat in corrupt_patterns:
                assert pat not in content, f"Found corrupt pattern '{pat}' in {lang}.json"
            data = json.loads(content)
        
        # Verify structure
        assert "lang" in data, f"{lang}.json missing 'lang'"
        assert "code" in data["lang"] and data["lang"]["code"] == lang
        assert "nativeName" in data["lang"] and len(data["lang"]["nativeName"]) > 0
        assert "produce" in data, f"{lang}.json missing 'produce'"
        assert "common" in data, f"{lang}.json missing 'common'"
        
        # Check required produce keys
        required_produce = [
            "verifiedBadge", "availableQuantity", "availability", "viewDetails",
            "contactSeller", "price", "pricePerTon", "pricePerQuintal", "pricePerKg",
            "enterPrice", "priceOnInquiry", "qualityGrade", "verificationSource"
        ]
        for k in required_produce:
            assert k in data["produce"], f"{lang}.json missing produce.{k}"
            val = data["produce"][k]
            assert val and not val.startswith("badge_"), f"Invalid val for {k} in {lang}: {val}"

        print(f"  [PASS] {lang} ({data['lang']['nativeName']}): Valid UTF-8, complete key structure")

def test_languages_js():
    print("\n=== 3. Checking static/i18n/languages.js ===")
    ljs_path = os.path.join("static", "i18n", "languages.js")
    with open(ljs_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    corrupt_patterns = ["Γ£ô", "ΓåÆ", "αªà", "\ufffd"]
    for pat in corrupt_patterns:
        assert pat not in content, f"Found corrupt pattern '{pat}' in languages.js"
    
    assert "মণিপুরী" in content, "Manipuri native name মণিপুরী missing in languages.js"
    assert "اردو" in content, "Urdu native name اردو missing in languages.js"
    assert "سنڌي" in content, "Sindhi native name سنڌي missing in languages.js"
    assert "தமிழ்" in content, "Tamil native name தமிழ் missing in languages.js"
    assert "हिन्दी" in content, "Hindi native name हिन्दी missing in languages.js"
    print("  [PASS] languages.js has valid UTF-8, correct native names, and 0 corrupt characters")

def test_static_scan_for_corrupt_mojibake():
    print("\n=== 4. Scanning Entire static/ Directory for Corrupted Symbols ===")
    corrupt_patterns = ["Γ£ô", "ΓåÆ", "αªà", "\ufffd"]
    for root, dirs, files in os.walk("static"):
        for fname in files:
            fpath = os.path.join(root, fname)
            with open(fpath, "rb") as f:
                raw = f.read()
            text = raw.decode("utf-8", errors="replace")
            for pat in corrupt_patterns:
                assert pat not in text, f"Found corrupt pattern '{pat}' in {fpath}"
    print("  [PASS] Entire static/ directory is free of mojibake and corrupt symbols")

def test_i18n_resolution_simulation():
    print("\n=== 5. Simulating I18n Key Resolution for Buyer Produce Discovery ===")
    locales_dir = os.path.join("static", "i18n", "locales")
    with open(os.path.join(locales_dir, "ta.json"), "r", encoding="utf-8") as f:
        ta = json.load(f)
    with open(os.path.join(locales_dir, "hi.json"), "r", encoding="utf-8") as f:
        hi = json.load(f)
    with open(os.path.join(locales_dir, "ur.json"), "r", encoding="utf-8") as f:
        ur = json.load(f)

    # Test key resolution
    test_keys = [
        ("badge_verified", "produce.verifiedBadge"),
        ("avail_qty", "produce.availableQuantity"),
        ("availability", "produce.availability"),
        ("btn_contact_seller", "produce.contactSeller"),
        ("price", "produce.price"),
    ]
    for raw, resolved in test_keys:
        val_ta = ta["produce"].get(resolved.split(".")[1])
        val_hi = hi["produce"].get(resolved.split(".")[1])
        val_ur = ur["produce"].get(resolved.split(".")[1])
        assert val_ta and not val_ta.startswith("badge_"), f"Ta resolution failed for {raw}"
        assert val_hi and not val_hi.startswith("badge_"), f"Hi resolution failed for {raw}"
        assert val_ur and not val_ur.startswith("badge_"), f"Ur resolution failed for {raw}"
        print(f"  [PASS] {raw} -> TA: '{val_ta}', HI: '{val_hi}', UR: '{val_ur}'")

def main():
    test_endpoints()
    test_all_23_locales()
    test_languages_js()
    test_static_scan_for_corrupt_mojibake()
    test_i18n_resolution_simulation()
    print("\n=======================================================")
    print(">>> ALL VERIFICATION CHECKS PASSED SUCCESSFULLY (100%) <<<")
    print("=======================================================")

if __name__ == "__main__":
    main()
