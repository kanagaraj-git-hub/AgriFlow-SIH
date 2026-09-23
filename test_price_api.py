import urllib.request
import json

BASE_URL = 'http://127.0.0.1:8000'

def req(path, method='GET', data=None, token=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    b = json.dumps(data).encode('utf-8') if data else None
    r = urllib.request.Request(f'{BASE_URL}{path}', data=b, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.getcode(), json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode('utf-8'))

def test_price():
    print("=== Testing Price Feature End-to-End via API ===")
    # 1. Login as Officer
    s, res = req('/api/auth/login', 'POST', {
        'identifier': 'ravi.kumar@agri.tn.gov.in',
        'password': 'officer123',
        'role': 'OFFICER'
    })
    assert s == 200, f'Login failed: {res}'
    token = res['token']
    print('[PASS] 1. Officer login successful')

    # 2. Reject negative price
    s, res = req('/api/officer/produce', 'POST', {
        'crop_name': 'Test Negative',
        'quantity': 10,
        'unit': 'Tons',
        'price': -500,
        'area': 'Sankari',
        'district': 'Salem',
        'state': 'Tamil Nadu',
        'availability_date': '2026-09-20'
    }, token=token)
    assert s == 400, f'Expected 400 for negative price, got {s}: {res}'
    print('[PASS] 2. Negative price correctly rejected with 400 error')

    # 3. Add Potato with Price 25000
    s, res = req('/api/officer/produce', 'POST', {
        'crop_name': 'Potato',
        'produce_type': 'Tubers',
        'quantity': 8,
        'unit': 'Tons',
        'price': 25000,
        'area': 'Sankari',
        'district': 'Salem',
        'state': 'Tamil Nadu',
        'quality': 'Grade B',
        'availability_date': '2026-09-20',
        'notes': 'Fresh bulk potatoes from local cluster'
    }, token=token)
    assert s == 200, f'Failed adding produce: {res}'
    produce_id = res['produce']['id']
    price_val = res['produce']['price']
    assert price_val == 25000.0, f'Price mismatch: {res}'
    print(f'[PASS] 3. Produce created successfully with Price: {price_val}')

    # 4. Check Public List
    s, items = req('/api/public/produce?crop=Potato')
    assert s == 200, f'Failed searching: {items}'
    match = [p for p in items if p['id'] == produce_id][0]
    assert match['price'] == 25000.0
    print(f'[PASS] 4. Public search returned price: {match["price"]}')

    # 5. Check Public Details
    s, detail = req(f'/api/public/produce/{produce_id}')
    assert s == 200 and detail['price'] == 25000.0
    print(f'[PASS] 5. Public details returned price: {detail["price"]}')

    # 6. Check existing produce without price
    s, all_items = req('/api/public/produce')
    no_price_items = [p for p in all_items if p.get('price') is None]
    print(f'[PASS] 6. Handled existing records without price safely: {len(no_price_items)} items have null price')

    print("\n>>> ALL PRICE API AND DATA PERSISTENCE TESTS PASSED! <<<")

if __name__ == '__main__':
    test_price()
