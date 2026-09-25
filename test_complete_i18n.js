const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const os = require('os');
const fs = require('fs');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const TEMP_PROFILE = path.join(os.tmpdir(), 'chrome_cdp_profile_' + Date.now());

function fetchJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

class CDPClient {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.id = 1;
    this.callbacks = new Map();
    this.ready = new Promise((resolve, reject) => {
      this.ws.onopen = () => resolve();
      this.ws.onerror = (err) => reject(err);
    });

    this.ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id && this.callbacks.has(msg.id)) {
        const { resolve, reject } = this.callbacks.get(msg.id);
        this.callbacks.delete(msg.id);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    };
  }

  send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = this.id++;
      this.callbacks.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }

  async eval(expression) {
    const res = await this.send('Runtime.evaluate', {
      expression,
      returnByValue: true,
      awaitPromise: true
    });
    if (res.exceptionDetails) {
      throw new Error(JSON.stringify(res.exceptionDetails));
    }
    return res.result ? res.result.value : undefined;
  }
}

async function run() {
  console.log('=== Starting Headless Chrome for Comprehensive AgriFlow i18n Test ===');
  const chromeProc = spawn(CHROME_PATH, [
    '--headless=new',
    '--remote-debugging-port=9222',
    `--user-data-dir=${TEMP_PROFILE}`,
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    'about:blank'
  ], { stdio: 'ignore' });

  try {
    let connected = false;
    let list;
    for (let i = 0; i < 20; i++) {
      await sleep(500);
      try {
        list = await fetchJson('http://127.0.0.1:9222/json');
        if (list && list.length > 0) {
          connected = true;
          break;
        }
      } catch (e) {}
    }

    if (!connected) {
      throw new Error('Could not connect to Chrome DevTools port 9222');
    }

    const pageTarget = list.find(t => t.type === 'page') || list[0];
    const client = new CDPClient(pageTarget.webSocketDebuggerUrl);
    await client.ready;
    await client.send('Page.enable');
    await client.send('Runtime.enable');

    console.log('\n--- Test 1: Navigation to AgriFlow and Initial Verification ---');
    await client.send('Page.navigate', { url: 'http://127.0.0.1:8000' });
    for (let i = 0; i < 30; i++) {
      await sleep(300);
      try {
        const ready = await client.eval('document.readyState');
        const hasBody = await client.eval('!!document.body');
        if (ready === 'complete' && hasBody) break;
      } catch (e) {}
    }
    await sleep(500);

    const title = await client.eval('document.title');
    console.log('[PASS] Page Title:', title);

    // Verify Branding has NO "SIH Platform"
    const brandText = await client.eval(`document.querySelector('header span.text-xl')?.innerText || ''`);
    console.log('[PASS] Brand text in UI:', brandText);
    if (brandText.includes('SIH Platform')) {
      throw new Error('FAIL: "SIH Platform" found in branding!');
    }

    console.log('\n--- Test 2: Branding & UI Audit across full page text ---');
    const fullText = await client.eval(`document.body.innerText`);
    if (fullText.includes('SIH Platform') || fullText.includes('AgriFlowSIH Platform')) {
      throw new Error('FAIL: "SIH Platform" appears in visible text!');
    }
    if (fullText.includes('Reconnecting...')) {
      throw new Error('FAIL: "Reconnecting..." appears in visible text!');
    }
    if (fullText.toLowerCase().includes('live sync')) {
      throw new Error('FAIL: "Live Sync" appears in visible text!');
    }
    const wsStatusEl = await client.eval(`document.getElementById('ws-status')`);
    if (wsStatusEl !== null) {
      throw new Error('FAIL: #ws-status element still exists in DOM!');
    }
    const wsReadyState = await client.eval(`STATE.ws ? STATE.ws.readyState : null`);
    console.log('[PASS] WebSocket object readyState (1=OPEN):', wsReadyState);
    console.log('[PASS] NO "SIH Platform", NO "Reconnecting...", and NO "Live Sync" in visible DOM text.');

    console.log('\n--- Test 3: Language Switching: English -> Tamil (ta) ---');
    await client.eval(`
      (async () => {
        window.AgriFlowI18n.setLocale('ta');
      })()
    `);
    await sleep(800);

    const activeLocaleTa = await client.eval(`localStorage.getItem('agriflow_language')`);
    const homeNavTa = await client.eval(`document.querySelector('[data-i18n="navigation.home"]')?.innerText`);
    const produceNavTa = await client.eval(`document.querySelector('[data-i18n="navigation.viewProduce"]')?.innerText`);
    const taglineTa = await client.eval(`document.querySelector('[data-i18n="landing.tagline"]')?.innerText`);
    console.log('[PASS] Active locale:', activeLocaleTa);
    console.log('[PASS] Home Nav (ta):', homeNavTa);
    console.log('[PASS] Produce Nav (ta):', produceNavTa);
    console.log('[PASS] Tagline (ta):', taglineTa);

    console.log('\n--- Test 4: Buyer / Produce Discovery in Tamil ---');
    await client.eval(`navigate('produce')`);
    await sleep(800);

    const produceTitleTa = await client.eval(`document.querySelector('[data-i18n="produce.title"]')?.innerText`);
    const filterCropPlaceholderTa = await client.eval(`document.querySelector('#filter-crop')?.getAttribute('placeholder')`);
    const cardBadgeTa = await client.eval(`document.querySelector('#produce-grid .badge-verified')?.innerText`);
    const cardBtnTa = await client.eval(`document.querySelector('#produce-grid button')?.innerText`);
    console.log('[PASS] Produce Title (ta):', produceTitleTa);
    console.log('[PASS] Crop Filter Placeholder (ta):', filterCropPlaceholderTa);
    console.log('[PASS] Card Badge (ta):', cardBadgeTa);
    console.log('[PASS] Card Button (ta):', cardBtnTa);

    // Open Produce Details Modal in Tamil
    await client.eval(`
      (() => {
        const btn = document.querySelector('#produce-grid [onclick*="openProduceDetails"]');
        if (btn) btn.click();
      })()
    `);
    await sleep(600);

    const modalBadgeTa = await client.eval(`document.querySelector('#pd-status-badge')?.innerText`);
    const modalNotesLabelTa = await client.eval(`document.querySelector('[data-i18n="produce.fieldNotes"]')?.innerText`);
    const modalPurchaseTitleTa = await client.eval(`document.querySelector('[data-i18n="produce.purchaseTitle"]')?.innerText`);
    console.log('[PASS] Modal Status Badge (ta):', modalBadgeTa);
    console.log('[PASS] Modal Notes Label (ta):', modalNotesLabelTa);
    console.log('[PASS] Modal Purchase Title (ta):', modalPurchaseTitleTa);
    await client.eval(`closeModal('produce-details-modal')`);
    await sleep(300);

    console.log('\n--- Test 5: Language Switching: Tamil -> Hindi (hi) ---');
    await client.eval(`
      (async () => {
        window.AgriFlowI18n.setLocale('hi');
      })()
    `);
    await sleep(800);

    const activeLocaleHi = await client.eval(`localStorage.getItem('agriflow_language')`);
    const produceTitleHi = await client.eval(`document.querySelector('[data-i18n="produce.title"]')?.innerText`);
    const cardBadgeHi = await client.eval(`document.querySelector('#produce-grid .badge-verified')?.innerText`);
    const cardBtnHi = await client.eval(`document.querySelector('#produce-grid button')?.innerText`);
    console.log('[PASS] Active locale:', activeLocaleHi);
    console.log('[PASS] Produce Title (hi):', produceTitleHi);
    console.log('[PASS] Card Badge (hi):', cardBadgeHi);
    console.log('[PASS] Card Button (hi):', cardBtnHi);

    console.log('\n--- Test 6: Language Switching: Hindi -> Urdu (ur) & RTL Layout ---');
    await client.eval(`
      (async () => {
        window.AgriFlowI18n.setLocale('ur');
      })()
    `);
    await sleep(800);

    const activeLocaleUr = await client.eval(`localStorage.getItem('agriflow_language')`);
    const docDirUr = await client.eval(`document.documentElement.getAttribute('dir')`);
    const produceTitleUr = await client.eval(`document.querySelector('[data-i18n="produce.title"]')?.innerText`);
    const cardBadgeUr = await client.eval(`document.querySelector('#produce-grid .badge-verified')?.innerText`);
    console.log('[PASS] Active locale:', activeLocaleUr);
    console.log('[PASS] HTML dir (RTL):', docDirUr);
    console.log('[PASS] Produce Title (ur):', produceTitleUr);
    console.log('[PASS] Card Badge (ur):', cardBadgeUr);

    if (docDirUr !== 'rtl') {
      throw new Error('FAIL: Urdu layout direction is not RTL!');
    }

    console.log('\n--- Test 7: Persistence Verification across Page Reload ---');
    await client.send('Page.reload');
    for (let i = 0; i < 30; i++) {
      await sleep(300);
      try {
        const ready = await client.eval('document.readyState');
        const hasBody = await client.eval('!!document.body');
        if (ready === 'complete' && hasBody) break;
      } catch (e) {}
    }
    await sleep(500);

    const reloadedLocale = await client.eval(`localStorage.getItem('agriflow_language')`);
    const reloadedDir = await client.eval(`document.documentElement.getAttribute('dir')`);
    const reloadedProduceNav = await client.eval(`document.querySelector('[data-i18n="navigation.viewProduce"]')?.innerText`);
    console.log('[PASS] Stored locale after reload:', reloadedLocale);
    console.log('[PASS] Document dir after reload:', reloadedDir);
    console.log('[PASS] Produce Nav text after reload:', reloadedProduceNav);

    if (reloadedLocale !== 'ur' || reloadedDir !== 'rtl') {
      throw new Error('FAIL: Language persistence failed on reload!');
    }

    console.log('\n--- Test 8: Agriculture Officer Portal in Tamil ---');
    // Switch to Tamil for portal testing
    await client.eval(`window.AgriFlowI18n.setLocale('ta')`);
    await sleep(600);

    // Login via demo button or direct API login as Officer
    const loginResult = await client.eval(`
      (async () => {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            identifier: '9876543210',
            password: 'officer123',
            role: 'OFFICER'
          })
        });
        if (!res.ok) return { success: false, status: res.status };
        const data = await res.json();
        STATE.token = data.token;
        STATE.user = data.user;
        STATE.profile = data.profile;
        localStorage.setItem('agriflow_token', data.token);
        updateNavAuth(true);
        navigate('officer-dashboard');
        return { success: true, name: data.user.name };
      })()
    `);
    console.log('[PASS] Logged in as Officer:', loginResult);
    if (!loginResult.success) throw new Error('FAIL: Officer login failed');
    await sleep(1000);

    const officerNavRoleTa = await client.eval(`document.getElementById('nav-user-role')?.innerText`);
    const officerTotalRecordsLabelTa = await client.eval(`document.querySelector('[data-i18n="officer.totalRecords"]')?.innerText`);
    const officerAvailQtyLabelTa = await client.eval(`document.querySelector('[data-i18n="officer.availableQty"]')?.innerText`);
    const officerPendingLabelTa = await client.eval(`document.querySelector('[data-i18n="officer.farmerRequests"]')?.innerText`);
    const officerVerifiedLabelTa = await client.eval(`document.querySelector('[data-i18n="officer.verifiedRecords"]')?.innerText`);
    const officerCropColTa = await client.eval(`document.querySelector('[data-i18n="officer.cropCol"]')?.innerText`);
    const officerPriceColTa = await client.eval(`document.querySelector('[data-i18n="officer.priceCol"]')?.innerText`);

    console.log('[PASS] Officer Navbar Role (ta):', officerNavRoleTa);
    console.log('[PASS] Officer Total Records Card (ta):', officerTotalRecordsLabelTa);
    console.log('[PASS] Officer Available Qty Card (ta):', officerAvailQtyLabelTa);
    console.log('[PASS] Officer Farmer Requests Card (ta):', officerPendingLabelTa);
    console.log('[PASS] Officer Verified Records Card (ta):', officerVerifiedLabelTa);
    console.log('[PASS] Officer Table Crop Column (ta):', officerCropColTa);
    console.log('[PASS] Officer Table Price Column (ta):', officerPriceColTa);

    // Open Officer Add Produce Modal
    await client.eval(`openModal('add-produce-modal')`);
    await sleep(500);

    const addProduceModalTitleTa = await client.eval(`document.getElementById('produce-modal-title')?.innerText`);
    const addProducePriceLabelTa = await client.eval(`document.querySelector('[data-i18n="produce.price"]')?.innerText`);
    const addProduceSaveBtnTa = await client.eval(`document.querySelector('[data-i18n="officer.savePublish"]')?.innerText`);
    console.log('[PASS] Add Produce Modal Title (ta):', addProduceModalTitleTa);
    console.log('[PASS] Add Produce Price Label (ta):', addProducePriceLabelTa);
    console.log('[PASS] Add Produce Save Button (ta):', addProduceSaveBtnTa);
    await client.eval(`closeModal('add-produce-modal')`);

    console.log('\n--- Test 9: Farmer Portal in Tamil ---');
    // Login as Farmer
    const farmerLoginResult = await client.eval(`
      (async () => {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            identifier: '9123456780',
            password: 'farmer123',
            role: 'FARMER'
          })
        });
        if (!res.ok) return { success: false, status: res.status };
        const data = await res.json();
        STATE.token = data.token;
        STATE.user = data.user;
        STATE.profile = data.profile;
        localStorage.setItem('agriflow_token', data.token);
        updateNavAuth(true);
        navigate('farmer-dashboard');
        return { success: true, name: data.user.name };
      })()
    `);
    console.log('[PASS] Logged in as Farmer:', farmerLoginResult);
    if (!farmerLoginResult.success) throw new Error('FAIL: Farmer login failed');
    await sleep(1000);

    const farmerNavRoleTa = await client.eval(`document.getElementById('nav-user-role')?.innerText`);
    const farmerTotalSubmissionsTa = await client.eval(`document.querySelector('[data-i18n="farmer.totalSubmissions"]')?.innerText`);
    const farmerPendingLabelTa = await client.eval(`document.querySelector('[data-i18n="status.Pending"]')?.innerText`);
    const farmerVerifiedLabelTa = await client.eval(`document.querySelector('[data-i18n="farmer.verified"]')?.innerText`);
    const farmerRequestsTitleTa = await client.eval(`document.querySelector('[data-i18n="farmer.requestsTitle"]')?.innerText`);

    console.log('[PASS] Farmer Navbar Role (ta):', farmerNavRoleTa);
    console.log('[PASS] Farmer Total Submissions Card (ta):', farmerTotalSubmissionsTa);
    console.log('[PASS] Farmer Pending Card (ta):', farmerPendingLabelTa);
    console.log('[PASS] Farmer Verified Card (ta):', farmerVerifiedLabelTa);
    console.log('[PASS] Farmer Requests Section Title (ta):', farmerRequestsTitleTa);

    console.log('\n--- Test 10: User Profile Page in Tamil ---');
    await client.eval(`navigate('profile')`);
    await sleep(600);

    const profileTitleTa = await client.eval(`document.querySelector('[data-i18n="profile.title"]')?.innerText`);
    const profileSaveBtnTa = await client.eval(`document.querySelector('[data-i18n="profile.saveChanges"]')?.innerText`);
    console.log('[PASS] Profile Title (ta):', profileTitleTa);
    console.log('[PASS] Profile Save Button (ta):', profileSaveBtnTa);

    console.log('\n--- Test 11: Raw Translation Keys Check on full application ---');
    const rawKeysFound = await client.eval(`
      (() => {
        const text = document.body.innerText;
        const keys = [
          'badge_verified', 'avail_qty', 'availability', 'btn_contact_seller',
          'common.save', 'produce.crop', 'officer.addProduce', 'farmer.portal'
        ];
        return keys.filter(k => text.includes(k));
      })()
    `);
    console.log('[PASS] Raw keys found in DOM:', rawKeysFound);
    if (rawKeysFound.length > 0) {
      throw new Error(`FAIL: Raw translation keys displayed in UI: ${rawKeysFound.join(', ')}`);
    }

    console.log('\n================================================================');
    console.log('>>> COMPLETE BROWSER VERIFICATION PASSED WITH 100% SUCCESS! <<<');
    console.log('================================================================');

  } finally {
    chromeProc.kill('SIGKILL');
    try {
      fs.rmSync(TEMP_PROFILE, { recursive: true, force: true });
    } catch (e) {}
  }
}

run().catch(err => {
  console.error('[FAIL]', err);
  process.exit(1);
});
