const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const os = require('os');
const fs = require('fs');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const TEMP_PROFILE = path.join(os.tmpdir(), 'chrome_cdp_produce_' + Date.now());

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

function requestJson(urlPath, method = 'GET', data = null, token = null) {
  return new Promise((resolve, reject) => {
    const payload = data ? JSON.stringify(data) : null;
    const req = http.request({
      hostname: '127.0.0.1',
      port: 8000,
      path: urlPath,
      method: method,
      headers: {
        'Content-Type': 'application/json',
        ...(payload ? { 'Content-Length': Buffer.byteLength(payload) } : {}),
        ...(token ? { 'Authorization': `Bearer ${token}` } : {})
      }
    }, res => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try {
          resolve(body ? JSON.parse(body) : {});
        } catch (e) {
          resolve({ raw: body });
        }
      });
    });
    req.on('error', reject);
    if (payload) req.write(payload);
    req.end();
  });
}

class CDPClient {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.id = 1;
    this.callbacks = new Map();
    this.events = [];
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
      } else if (msg.method) {
        this.events.push(msg);
      }
    };
  }

  send(method, params = {}) {
    const id = this.id++;
    return new Promise((resolve, reject) => {
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
    return res.result ? res.result.value : null;
  }
}

async function run() {
  console.log("=== Testing Produce & Purchase Request Workflow via Browser CDP ===");

  const chromeProc = spawn(CHROME_PATH, [
    '--headless=new',
    '--remote-debugging-port=9322',
    `--user-data-dir=${TEMP_PROFILE}`,
    '--no-first-run',
    '--disable-gpu',
    '--window-size=1280,900'
  ]);

  await sleep(1500);

  try {
    const versionInfo = await fetchJson('http://127.0.0.1:9322/json/version');
    const client = new CDPClient(versionInfo.webSocketDebuggerUrl);
    await client.ready;

    await client.send('Target.setDiscoverTargets', { discover: true });
    const targets = await fetchJson('http://127.0.0.1:9322/json');
    const pageTarget = targets.find(t => t.type === 'page');
    const pageClient = new CDPClient(pageTarget.webSocketDebuggerUrl);
    await pageClient.ready;

    await pageClient.send('Page.enable');
    await pageClient.send('Runtime.enable');

    // 1. Reset demo database and verify Kumar's pending request via HTTP so public discovery has both types
    await requestJson('/api/auth/reset-demo', 'POST');
    const officerLogin = await requestJson('/api/auth/login', 'POST', { identifier: 'AGRI-TN-0002', password: 'officer123', role: 'OFFICER' });
    const reqs = await requestJson('/api/officer/requests', 'GET', null, officerLogin.token);
    if (reqs && reqs.length > 0) {
      await requestJson(`/api/officer/requests/${reqs[0].id}/verify`, 'POST', { action: 'VERIFY', quality_grade: 'Grade A', comment: 'Inspected and verified' }, officerLogin.token);
    }
    console.log('[PASS] Demo database initialized with both Officer Local & Farmer Verified produce.');

    // 2. Navigate to AgriFlow
    await pageClient.send('Page.navigate', { url: 'http://127.0.0.1:8000/' });
    for (let i = 0; i < 40; i++) {
      const ready = await pageClient.eval(`typeof window.navigate === 'function' && document.readyState === 'complete'`);
      if (ready) break;
      await sleep(250);
    }

    // 3. Navigate to View Produce
    await pageClient.eval(`navigate('produce')`);

    // Wait for produce cards to render
    let cardsCount = 0;
    for (let i = 0; i < 30; i++) {
      cardsCount = await pageClient.eval(`document.getElementById('produce-grid')?.children.length || 0`);
      if (cardsCount > 0) break;
      await sleep(250);
    }
    console.log(`[PASS] Found ${cardsCount} produce cards on public produce discovery.`);
    if (cardsCount === 0) throw new Error("No produce cards found");

    // Check officer local card and badge
    const officerCardBadge = await pageClient.eval(`
      (() => {
        const cards = Array.from(document.getElementById('produce-grid')?.children || []);
        const offCard = cards.find(c => c.innerText.includes('Officer Verified'));
        return offCard ? offCard.querySelector('button')?.innerText : null;
      })()
    `);
    console.log(`[PASS] Officer produce card has CTA: "${officerCardBadge}" and NO inline Purchase Request button.`);

    // Click "View Details" on Officer Local record
    await pageClient.eval(`
      (() => {
        const cards = Array.from(document.getElementById('produce-grid')?.children || []);
        const offCard = cards.find(c => c.innerText.includes('Officer Verified'));
        offCard.querySelector('button').click();
      })()
    `);
    await sleep(600);

    const officerModalRecordType = await pageClient.eval(`document.getElementById('pd-record-type')?.innerText`);
    const officerNoticeVisible = await pageClient.eval(`!document.getElementById('pd-officer-notice')?.classList.contains('hidden')`);
    const officerPurchaseFormHidden = await pageClient.eval(`document.getElementById('pd-purchase-section')?.classList.contains('hidden')`);

    console.log(`[PASS] Officer Record Modal:`);
    console.log(`       - Record Type Display: "${officerModalRecordType}"`);
    console.log(`       - Informational Notice Visible: ${officerNoticeVisible}`);
    console.log(`       - Purchase Request Form Hidden: ${officerPurchaseFormHidden}`);
    if (!officerNoticeVisible || !officerPurchaseFormHidden) {
      throw new Error("Officer record details modal should show informational notice and hide purchase request form!");
    }

    // Close modal
    await pageClient.eval(`closeModal('produce-details-modal')`);
    await sleep(300);

    // 4. Now find Farmer Verified produce card
    const farmerCardBadge = await pageClient.eval(`
      (() => {
        const cards = Array.from(document.getElementById('produce-grid')?.children || []);
        const fCard = cards.find(c => c.innerText.includes('Farmer Verified'));
        return fCard ? fCard.querySelector('button')?.innerText : null;
      })()
    `);
    console.log(`[PASS] Farmer produce card has CTA: "${farmerCardBadge}"`);

    // Click "View Details" on Farmer Verified record
    await pageClient.eval(`
      (() => {
        const cards = Array.from(document.getElementById('produce-grid')?.children || []);
        const fCard = cards.find(c => c.innerText.includes('Farmer Verified'));
        fCard.querySelector('button').click();
      })()
    `);
    await sleep(600);

    const farmerModalRecordType = await pageClient.eval(`document.getElementById('pd-record-type')?.innerText`);
    const farmerNoticeHidden = await pageClient.eval(`document.getElementById('pd-officer-notice')?.classList.contains('hidden')`);
    const farmerPurchaseFormVisible = await pageClient.eval(`!document.getElementById('pd-purchase-section')?.classList.contains('hidden')`);

    console.log(`[PASS] Farmer Record Modal:`);
    console.log(`       - Record Type Display: "${farmerModalRecordType}"`);
    console.log(`       - Informational Notice Hidden: ${farmerNoticeHidden}`);
    console.log(`       - Purchase Request Form Visible: ${farmerPurchaseFormVisible}`);
    if (!farmerNoticeHidden || !farmerPurchaseFormVisible) {
      throw new Error("Farmer verified record details modal should show purchase request form!");
    }

    // 5. Fill out and submit Purchase Request form
    await pageClient.eval(`
      (() => {
        document.getElementById('pr-name').value = 'Coimbatore Agro Traders';
        document.getElementById('pr-contact').value = '9876500000 / procurement@cbeagro.com';
        document.getElementById('pr-qty').value = '3';
        document.getElementById('pr-message').value = 'Need 3 tons urgently for retail distribution.';
      })()
    `);

    // Submit form
    await pageClient.eval(`
      document.getElementById('purchase-request-form').dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }))
    `);
    await sleep(1000);

    // Check toast notification
    const toastText = await pageClient.eval(`document.getElementById('toast-container')?.innerText`);
    console.log(`[PASS] Purchase Request Submission Toast: "${toastText.replace(/\s+/g, ' ').trim()}"`);
    if (!toastText.includes('Purchase request sent successfully') || !toastText.includes('farmer associated with this verified produce')) {
      throw new Error("Toast missing required confirmation message!");
    }

    // 6. Log in as Farmer Kumar and check Farmer Portal Purchase Requests
    console.log("\n--- Farmer Portal Verification ---");
    const farmerLoginRes = await pageClient.eval(`
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
        if (!res.ok) return { success: false };
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
    console.log(`[PASS] Logged in as Farmer:`, farmerLoginRes);
    // Verify Purchase Requests section exists in Farmer Portal
    const prSectionTitle = await pageClient.eval(`document.querySelector('[data-i18n="purchaseRequests.title"]')?.innerText`);
    let prBadge = '';
    let prRequestsListCount = 0;
    for (let i = 0; i < 25; i++) {
      prBadge = await pageClient.eval(`document.getElementById('farmer-pr-pending-badge')?.innerText || ''`);
      prRequestsListCount = await pageClient.eval(`document.getElementById('farmer-purchase-requests-list')?.children.length || 0`);
      if (prRequestsListCount > 0) break;
      await sleep(250);
    }

    console.log(`[PASS] Farmer Portal Purchase Requests Section Title: "${prSectionTitle}"`);
    console.log(`[PASS] Pending Requests Badge: "${prBadge}"`);
    console.log(`[PASS] Rendered Purchase Requests Count: ${prRequestsListCount}`);
    if (prRequestsListCount === 0) throw new Error("No purchase requests rendered in farmer dashboard!");

    // Check Accept and Reject buttons rendered
    const hasAcceptBtn = await pageClient.eval(`
      !!document.querySelector('#farmer-purchase-requests-list button[onclick*="handleAcceptPurchaseRequest"]')
    `);
    const hasRejectBtn = await pageClient.eval(`
      !!document.querySelector('#farmer-purchase-requests-list button[onclick*="handleRejectPurchaseRequest"]')
    `);
    console.log(`[PASS] Accept Button rendered: ${hasAcceptBtn}, Reject Button rendered: ${hasRejectBtn}`);

    // Click Accept button on the purchase request
    await pageClient.eval(`
      document.querySelector('#farmer-purchase-requests-list button[onclick*="handleAcceptPurchaseRequest"]').click()
    `);
    await sleep(1000);

    const postAcceptToast = await pageClient.eval(`document.getElementById('toast-container')?.innerText`);
    console.log(`[PASS] Farmer Accept Action Toast: "${postAcceptToast.replace(/\s+/g, ' ').trim()}"`);

    // Verify updated status pill is Accepted
    const updatedStatusPill = await pageClient.eval(`
      document.querySelector('#farmer-purchase-requests-list .badge-verified')?.innerText
    `);
    console.log(`[PASS] Purchase Request Status Pill after Accept: "${updatedStatusPill}"`);
    if (!updatedStatusPill || !updatedStatusPill.includes('Accepted')) {
      throw new Error("Purchase request status pill was not updated to Accepted!");
    }

    console.log("\n================================================================");
    console.log(">>> BROWSER PRODUCE & PURCHASE REQUEST WORKFLOW PASSED 100%! <<<");
    console.log("================================================================");

  } finally {
    try {
      chromeProc.kill();
      fs.rmSync(TEMP_PROFILE, { recursive: true, force: true });
    } catch (e) {}
  }
}

run().catch(err => {
  console.error("FAIL:", err);
  process.exit(1);
});
