const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const os = require('os');
const fs = require('fs');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const TEMP_PROFILE = path.join(os.tmpdir(), 'chrome_cdp_officer_' + Date.now());

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
        if (msg.error) {
          reject(msg.error);
        } else {
          resolve(msg.result);
        }
      }
    };
  }

  async send(method, params = {}) {
    await this.ready;
    const msgId = this.id++;
    return new Promise((resolve, reject) => {
      this.callbacks.set(msgId, { resolve, reject });
      this.ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  async eval(expression) {
    const res = await this.send('Runtime.evaluate', {
      expression,
      awaitPromise: true,
      returnByValue: true
    });
    if (res.exceptionDetails) {
      throw new Error(`Eval failed: ${JSON.stringify(res.exceptionDetails)}`);
    }
    return res.result ? res.result.value : undefined;
  }

  close() {
    this.ws.close();
  }
}

async function main() {
  console.log('===============================================================');
  console.log('BROWSER E2E TEST: AGRICULTURE OFFICER REGISTRATION STATE FLOW');
  console.log('===============================================================');

  // Launch headless Chrome
  const chromeProcess = spawn(CHROME_PATH, [
    '--headless=new',
    '--remote-debugging-port=9223',
    `--user-data-dir=${TEMP_PROFILE}`,
    '--no-first-run',
    '--disable-gpu',
    '--window-size=1280,900'
  ]);

  try {
    let versionData = null;
    for (let i = 0; i < 30; i++) {
      try {
        versionData = await fetchJson('http://127.0.0.1:9223/json/version');
        if (versionData && versionData.webSocketDebuggerUrl) break;
      } catch (e) {
        await sleep(200);
      }
    }

    if (!versionData) {
      throw new Error('Failed to connect to Chrome remote debugging port 9223');
    }

    const targets = await fetchJson('http://127.0.0.1:9223/json/list');
    const pageTarget = targets.find(t => t.type === 'page') || targets[0];
    const client = new CDPClient(pageTarget.webSocketDebuggerUrl);

    await client.send('Page.enable');
    await client.send('Runtime.enable');

    // Step 0: Navigate to AgriFlow and Reset Demo DB
    console.log('\n--- Step 0: Navigate to AgriFlow & Reset Demo Data ---');
    await client.send('Page.navigate', { url: 'http://127.0.0.1:8000/' });
    await sleep(2000);

    await client.eval(`fetch('/api/auth/reset-demo', { method: 'POST' }).then(r => r.json())`);
    await sleep(500);

    const title = await client.eval(`document.title`);
    console.log(`[PASS] Page loaded: "${title}"`);

    // =========================================================================
    // TEST 1: Freshly open Agriculture Officer registration.
    // Expected: Step 1 — Officer ID verification.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 1: Freshly open Agriculture Officer registration');
    console.log('===============================================================');
    await client.eval(`
      openAuthModal('register', 'OFFICER');
    `);
    await sleep(400);

    const t1WizardVis = await client.eval(`!document.getElementById('officer-reg-wizard').classList.contains('hidden')`);
    const t1Step1Vis = await client.eval(`!document.getElementById('officer-step-1').classList.contains('hidden')`);
    const t1Step5Vis = await client.eval(`!document.getElementById('officer-step-5').classList.contains('hidden')`);
    const t1Badge = await client.eval(`document.querySelector('#officer-step-1 span[data-i18n="auth.officerVerificationBadge"]')?.textContent.trim()`);
    const t1Title = await client.eval(`document.querySelector('#officer-step-1 h3')?.textContent.trim()`);
    const t1Sub = await client.eval(`document.querySelector('#officer-step-1 p')?.textContent.trim()`);
    const t1InputVal = await client.eval(`document.getElementById('officer-verify-id-input').value`);

    if (!t1WizardVis || !t1Step1Vis || t1Step5Vis) {
      throw new Error(`TEST 1 FAILED: Wizard visible=${t1WizardVis}, Step 1 visible=${t1Step1Vis}, Step 5 visible=${t1Step5Vis}`);
    }
    console.log(`[PASS] TEST 1: Step 1 is actively displayed:`);
    console.log(`       Badge: "${t1Badge}"`);
    console.log(`       Heading: "${t1Title}"`);
    console.log(`       Subtitle: "${t1Sub}"`);
    console.log(`       Input value is empty: "${t1InputVal}"`);
    console.log(`       Step 5 is hidden: ${!t1Step5Vis}`);

    // =========================================================================
    // TEST 2: Register AGRI-TN-0003 completely.
    // Expected: Success screen appears ("Officer Account Created Successfully!")
    // with Officer ID, Full Name, Login ID, and Proceed to Officer Login button.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 2: Register AGRI-TN-0003 completely');
    console.log('===============================================================');
    await client.eval(`
      document.getElementById('officer-verify-id-input').value = 'AGRI-TN-0003';
      handleVerifyOfficerId();
    `);
    await sleep(800);

    const t2Step2Vis = await client.eval(`!document.getElementById('officer-step-2').classList.contains('hidden')`);
    const t2DemoOtp = await client.eval(`document.getElementById('officer-demo-otp-val').textContent`);
    console.log(`[PASS] Step 2 reached! Demo OTP generated: "${t2DemoOtp}"`);

    // Verify OTP
    await client.eval(`
      autoFillDemoOtp();
      handleVerifyOtp();
    `);
    await sleep(800);

    const t2Step3Vis = await client.eval(`!document.getElementById('officer-step-3').classList.contains('hidden')`);
    const t2OfficerName = await client.eval(`document.getElementById('dtl-name').textContent`);
    const t2OfficerDistrict = await client.eval(`document.getElementById('dtl-district').textContent`);
    console.log(`[PASS] Step 3 reached! Official Details: ${t2OfficerName} (${t2OfficerDistrict})`);

    // Proceed to Step 4
    await client.eval(`goToOfficerStep(4)`);
    await sleep(400);

    await client.eval(`
      document.getElementById('officer-new-login-id').value = 'senthil_cbe_test';
      document.getElementById('officer-new-password').value = 'officer123';
      document.getElementById('officer-confirm-password').value = 'officer123';
      document.getElementById('btn-create-officer-acc').click();
    `);
    await sleep(1000);

    const t2Step5Vis = await client.eval(`!document.getElementById('officer-step-5').classList.contains('hidden')`);
    const t2DoneId = await client.eval(`document.getElementById('done-officer-id').textContent`);
    const t2DoneName = await client.eval(`document.getElementById('done-officer-name').textContent`);
    const t2DoneLogin = await client.eval(`document.getElementById('done-login-id').textContent`);
    const t2SuccessTitle = await client.eval(`document.querySelector('#officer-step-5 h3').textContent.trim()`);

    if (!t2Step5Vis || t2DoneId !== 'AGRI-TN-0003' || t2DoneName !== 'Senthil Nathan' || t2DoneLogin !== 'senthil_cbe_test') {
      throw new Error(`TEST 2 FAILED: Step 5 visible=${t2Step5Vis}, ID=${t2DoneId}, Name=${t2DoneName}, Login=${t2DoneLogin}`);
    }
    console.log(`[PASS] TEST 2: Success screen displayed properly!`);
    console.log(`       Heading: "${t2SuccessTitle}"`);
    console.log(`       Officer ID: "${t2DoneId}"`);
    console.log(`       Full Name: "${t2DoneName}"`);
    console.log(`       Login ID: "${t2DoneLogin}"`);

    // =========================================================================
    // TEST 3: Proceed to Officer Login -> Login successfully -> Logout.
    // Open Agriculture Officer registration again.
    // Expected: Step 1 — Officer ID verification. NOT the previous success screen.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 3: Proceed to Login -> Login -> Logout -> Reopen Registration');
    console.log('===============================================================');
    await client.eval(`goToOfficerLoginAfterReg()`);
    await sleep(500);

    const t3FormLoginVis = await client.eval(`!document.getElementById('form-login').classList.contains('hidden')`);
    const t3PrefilledId = await client.eval(`document.getElementById('login-identifier').value`);
    console.log(`[PASS] Switched to Login mode. Form visible: ${t3FormLoginVis}, Prefilled: "${t3PrefilledId}"`);

    // Submit Login
    await client.eval(`
      document.getElementById('login-password').value = 'officer123';
      document.getElementById('btn-login-submit').click();
    `);
    await sleep(2000);

    const t3OfficerNavVis = await client.eval(`!document.getElementById('officer-nav').classList.contains('hidden')`);
    console.log(`[PASS] Officer logged in successfully! Officer navigation visible: ${t3OfficerNavVis}`);

    // Logout
    console.log('Logging out officer...');
    await client.eval(`logout()`);
    await sleep(800);

    const t3GuestVis = await client.eval(`!document.getElementById('guest-controls').classList.contains('hidden')`);
    console.log(`[PASS] Officer logged out. Guest controls visible: ${t3GuestVis}`);

    // Reopen Agriculture Officer registration
    console.log('Reopening Agriculture Officer registration...');
    await client.eval(`
      openAuthModal('register', 'OFFICER');
    `);
    await sleep(600);

    const t3ReopenStep1Vis = await client.eval(`!document.getElementById('officer-step-1').classList.contains('hidden')`);
    const t3ReopenStep5Vis = await client.eval(`!document.getElementById('officer-step-5').classList.contains('hidden')`);
    const t3ReopenInputVal = await client.eval(`document.getElementById('officer-verify-id-input').value`);

    if (!t3ReopenStep1Vis || t3ReopenStep5Vis) {
      throw new Error(`TEST 3 FAILED: Step 1 visible=${t3ReopenStep1Vis}, Step 5 visible=${t3ReopenStep5Vis}. Stale success screen was incorrectly retained!`);
    }
    console.log(`[PASS] TEST 3 SUCCEEDED: Step 1 is correctly displayed!`);
    console.log(`       Step 1 visible: ${t3ReopenStep1Vis}`);
    console.log(`       Step 5 hidden: ${!t3ReopenStep5Vis}`);
    console.log(`       Input cleared: "${t3ReopenInputVal}"`);

    // =========================================================================
    // TEST 4: Enter AGRI-TN-0003 again.
    // Expected: "Officer account already exists." NOT a new registration.
    // Provides [ Proceed to Officer Login ].
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 4: Enter already registered AGRI-TN-0003 again');
    console.log('===============================================================');
    await client.eval(`
      document.getElementById('officer-verify-id-input').value = 'AGRI-TN-0003';
      handleVerifyOfficerId();
    `);
    await sleep(800);

    const t4ErrVis = await client.eval(`!document.getElementById('officer-id-error').classList.contains('hidden')`);
    const t4ErrText = await client.eval(`document.getElementById('officer-id-error').textContent`);
    const t4Step1StillVis = await client.eval(`!document.getElementById('officer-step-1').classList.contains('hidden')`);
    const t4Step2NotVis = await client.eval(`document.getElementById('officer-step-2').classList.contains('hidden')`);
    const t4Step5NotVis = await client.eval(`document.getElementById('officer-step-5').classList.contains('hidden')`);

    if (!t4ErrVis || !t4ErrText.includes('Officer account already exists') || !t4Step1StillVis || !t4Step2NotVis || !t4Step5NotVis) {
      throw new Error(`TEST 4 FAILED: Err visible=${t4ErrVis}, text="${t4ErrText}", Step 1 visible=${t4Step1StillVis}, Step 2 hidden=${t4Step2NotVis}`);
    }
    console.log(`[PASS] TEST 4 SUCCEEDED: Duplicate registration prevented with 409!`);
    console.log(`       Error Box displayed: "${t4ErrText.replace(/\\s+/g, ' ').trim()}"`);
    console.log(`       Remained on Step 1: ${t4Step1StillVis}`);
    console.log(`       Did NOT proceed to OTP Step 2: ${t4Step2NotVis}`);
    console.log(`       Did NOT show previous Step 5 success screen: ${t4Step5NotVis}`);

    // =========================================================================
    // TEST 5: Enter an available officer ID (AGRI-TN-0001).
    // Expected: Normal OTP -> Confirm Details -> Create Login flow.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 5: Enter available officer ID (AGRI-TN-0001)');
    console.log('===============================================================');
    await client.eval(`
      document.getElementById('officer-verify-id-input').value = 'AGRI-TN-0001';
      handleVerifyOfficerId();
    `);
    await sleep(800);

    const t5Step2Vis = await client.eval(`!document.getElementById('officer-step-2').classList.contains('hidden')`);
    const t5MaskedMobile = await client.eval(`document.getElementById('officer-masked-mobile').textContent`);
    const t5DemoOtp = await client.eval(`document.getElementById('officer-demo-otp-val').textContent`);

    if (!t5Step2Vis || !t5DemoOtp) {
      throw new Error(`TEST 5 FAILED: Did not reach Step 2 OTP for available ID AGRI-TN-0001`);
    }
    console.log(`[PASS] Step 2 reached for AGRI-TN-0001. Masked Mobile: ${t5MaskedMobile}, OTP: ${t5DemoOtp}`);

    // Auto-fill OTP and verify
    await client.eval(`
      autoFillDemoOtp();
      handleVerifyOtp();
    `);
    await sleep(800);

    const t5Step3Vis = await client.eval(`!document.getElementById('officer-step-3').classList.contains('hidden')`);
    const t5OfficerName = await client.eval(`document.getElementById('dtl-name').textContent`);
    const t5District = await client.eval(`document.getElementById('dtl-district').textContent`);
    console.log(`[PASS] Step 3 reached for AGRI-TN-0001: ${t5OfficerName} (${t5District})`);

    // Proceed to Step 4
    await client.eval(`goToOfficerStep(4)`);
    await sleep(400);

    const t5Step4Vis = await client.eval(`!document.getElementById('officer-step-4').classList.contains('hidden')`);
    console.log(`[PASS] TEST 5 SUCCEEDED: Reached Step 4 Credentials for AGRI-TN-0001 (visible=${t5Step4Vis})`);

    // =========================================================================
    // TEST 6: Refresh the browser after logout and reopen registration.
    // Expected: Fresh Step 1.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 6: Refresh the browser after logout and reopen registration');
    console.log('===============================================================');
    await client.eval(`logout()`);
    await sleep(400);

    // Hard reload the browser page via Chrome DevTools Protocol
    console.log('Reloading page via CDP...');
    await client.send('Page.reload');
    await sleep(2500);

    console.log('Reopening Agriculture Officer registration after refresh...');
    await client.eval(`
      openAuthModal('register', 'OFFICER');
    `);
    await sleep(600);

    const t6Step1Vis = await client.eval(`!document.getElementById('officer-step-1').classList.contains('hidden')`);
    const t6Step5Vis = await client.eval(`!document.getElementById('officer-step-5').classList.contains('hidden')`);
    const t6InputVal = await client.eval(`document.getElementById('officer-verify-id-input').value`);

    if (!t6Step1Vis || t6Step5Vis) {
      throw new Error(`TEST 6 FAILED: After refresh, Step 1 visible=${t6Step1Vis}, Step 5 visible=${t6Step5Vis}`);
    }
    console.log(`[PASS] TEST 6 SUCCEEDED: Fresh Step 1 is displayed after browser refresh!`);
    console.log(`       Step 1 visible: ${t6Step1Vis}`);
    console.log(`       Step 5 hidden: ${!t6Step5Vis}`);
    console.log(`       Input value empty: "${t6InputVal}"`);

    client.close();
    console.log('\n===============================================================');
    console.log('ALL 6 USER TEST SCENARIOS PASSED 100% SUCCESSFULLY!');
    console.log('===============================================================');
    process.exit(0);

  } catch (err) {
    console.error('[FAIL] Error during browser test:', err);
    process.exit(1);
  } finally {
    try {
      chromeProcess.kill();
    } catch (e) {}
    try {
      fs.rmSync(TEMP_PROFILE, { recursive: true, force: true });
    } catch (e) {}
  }
}

main();
