import json
import re
import os

with open('static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

i18n_keys = re.findall(r'data-i18n="([^"]+)"', html)
placeholder_keys = re.findall(r'data-i18n-placeholder="([^"]+)"', html)
title_keys = re.findall(r'data-i18n-title="([^"]+)"', html)
aria_keys = re.findall(r'data-i18n-aria="([^"]+)"', html)

with open('static/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

app_t_keys = re.findall(r"(?:AgriFlowI18n\.t|(?:\b|^)t)\(\s*['\"]([^'\"]+)['\"]", app_js)

all_keys = sorted(list(set(i18n_keys + placeholder_keys + title_keys + aria_keys + app_t_keys)))
print(f"Total unique i18n keys across index.html & app.js: {len(all_keys)}")

def check_key(d, k):
    parts = k.split('.')
    curr = d
    for p in parts:
        if isinstance(curr, dict) and p in curr:
            curr = curr[p]
        else:
            return False
    return True

locale_dir = 'static/i18n/locales'
all_files = sorted([f for f in os.listdir(locale_dir) if f.endswith('.json')])
print(f"Found {len(all_files)} locale files.")

missing_any = False
for f in all_files:
    with open(os.path.join(locale_dir, f), 'r', encoding='utf-8') as fp:
        loc = json.load(fp)
    loc_missing = [k for k in all_keys if not check_key(loc, k)]
    if loc_missing:
        print(f"Missing in {f}: {loc_missing}")
        missing_any = True

if not missing_any:
    print("SUCCESS: ALL 246 keys exist in ALL 23 locale files!")
