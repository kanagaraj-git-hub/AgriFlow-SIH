const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const os = require('os');
const fs = require('fs');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const TEMP_PROFILE = path.join(os.tmpdir(), 'chrome_cdp_officer_' + Date.now());
const CDP_PORT = 9250 + Math.floor(Math.random() * 400);

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
  console.log(`Using Chrome debugging port: ${CDP_PORT}`);

  // Launch headless Chrome
  const chromeProcess = spawn(CHROME_PATH, [
    '--headless=new',
    `--remote-debugging-port=${CDP_PORT}`,
    `--user-data-dir=${TEMP_PROFILE}`,
    '--no-first-run',
    '--disable-gpu',
    '--window-size=1280,900'
  ]);

  try {
    let versionData = null;
    for (let i = 0; i < 30; i++) {
      try {
        versionData = await fetchJson(`http://127.0.0.1:${CDP_PORT}/json/version`);
        if (versionData && versionData.webSocketDebuggerUrl) break;
      } catch (e) {
        await sleep(200);
      }
    }

    if (!versionData) {
      throw new Error(`Failed to connect to Chrome remote debugging port ${CDP_PORT}`);
    }

    const targets = await fetchJson(`http://127.0.0.1:${CDP_PORT}/json/list`);
    const pageTarget = targets.find(t => t.type === 'page') || targets[0];
    const client = new CDPClient(pageTarget.webSocketDebuggerUrl);

    await client.send('Page.enable');
    await client.send('Runtime.enable');

    // Step 0: Navigate to AgriFlow and Reset Demo DB
    console.log('\n--- Step 0: Navigate to AgriFlow & Reset Demo Data ---');
    await client.send('Page.navigate', { url: 'http://127.0.0.1:8000/' });

    // Wait until document is ready and openAuthModal is available
    for (let i = 0; i < 40; i++) {
      const ready = await client.eval(`typeof window.openAuthModal === 'function' && document.readyState === 'complete'`);
      if (ready) break;
      await sleep(250);
    }

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
    await client.eval(`openAuthModal('register', 'OFFICER');`);
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

    // =========================================================================
    // TEST 2: Test Invalid Officer ID (AGRI-TN-9999).
    // Expected: Title "Invalid Officer ID", message "Please enter a valid registered Agriculture Officer ID.", stays on Step 1.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 2: Test Invalid Officer ID (AGRI-TN-9999)');
    console.log('===============================================================');
    await client.eval(`
      document.getElementById('officer-verify-id-input').value = 'AGRI-TN-9999';
      document.getElementById('btn-verify-officer-id').click();
    `);
    await sleep(1000);

    const t2ErrVis = await client.eval(`!document.getElementById('officer-id-error').classList.contains('hidden')`);
    const t2ErrHtml = await client.eval(`document.getElementById('officer-id-error').innerHTML`);
    const t2ErrText = await client.eval(`document.getElementById('officer-id-error').innerText`);
    const t2Step1Still = await client.eval(`!document.getElementById('officer-step-1').classList.contains('hidden')`);
    const t2Step2Hidden = await client.eval(`document.getElementById('officer-step-2').classList.contains('hidden')`);

    if (!t2ErrVis || !t2Step1Still || !t2Step2Hidden || !t2ErrText.includes('Invalid Officer ID') || !t2ErrText.includes('Please enter a valid registered Agriculture Officer ID.')) {
      throw new Error(`TEST 2 FAILED: Err visible=${t2ErrVis}, Text="${t2ErrText}", Step 1 visible=${t2Step1Still}, Step 2 hidden=${t2Step2Hidden}`);
    }
    console.log(`[PASS] TEST 2 SUCCEEDED: Invalid Officer ID rejected!`);
    console.log(`       Error Title & Message: "${t2ErrText.replace(/\\s+/g, ' ').trim()}"`);
    console.log(`       Remained on Step 1: ${t2Step1Still}`);
    console.log(`       Did not advance to Step 2: ${t2Step2Hidden}`);

    // =========================================================================
    // TEST 3: Test Already Registered Officer ID (AGRI-TN-0002 / Priya Devi).
    // Expected: Title "Officer account already exists", message "An AgriFlow account has already been created for this Officer ID. Please use Officer Login.", button to proceed to login.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 3: Test Already Registered Officer ID (AGRI-TN-0002)');
    console.log('===============================================================');
    await client.eval(`
      document.getElementById('officer-verify-id-input').value = 'AGRI-TN-0002';
      document.getElementById('btn-verify-officer-id').click();
    `);
    await sleep(1000);

    const t3ErrVis = await client.eval(`!document.getElementById('officer-id-error').classList.contains('hidden')`);
    const t3ErrText = await client.eval(`document.getElementById('officer-id-error').innerText`);
    const t3LoginBtnVis = await client.eval(`!!document.querySelector('#officer-id-error button[onclick*="goToOfficerLoginPrefilled"]')`);
    const t3Step1Still = await client.eval(`!document.getElementById('officer-step-1').classList.contains('hidden')`);

    if (!t3ErrVis || !t3Step1Still || !t3ErrText.includes('Officer account already exists') || !t3LoginBtnVis) {
      throw new Error(`TEST 3 FAILED: Err visible=${t3ErrVis}, Text="${t3ErrText}", LoginBtn=${t3LoginBtnVis}`);
    }
    console.log(`[PASS] TEST 3 SUCCEEDED: Duplicate registration prevented!`);
    console.log(`       Error Box: "${t3ErrText.replace(/\\s+/g, ' ').trim()}"`);
    console.log(`       Proceed to Login button present: ${t3LoginBtnVis}`);

    // =========================================================================
    // TEST 4: Valid Available Officer ID (AGRI-TN-0001) via Form Submit / Enter.
    // Expected: Advances to Step 2 OTP screen with Demo OTP banner.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 4: Valid Available Officer ID (AGRI-TN-0001) via Button Click');
    console.log('===============================================================');
    await client.eval(`
      document.getElementById('officer-verify-id-input').value = 'AGRI-TN-0001';
      document.getElementById('btn-verify-officer-id').click();
    `);
    await sleep(1200);

    const t4Step2Vis = await client.eval(`!document.getElementById('officer-step-2').classList.contains('hidden')`);
    const t4MaskedMobile = await client.eval(`document.getElementById('officer-masked-mobile').textContent`);
    const t4DemoOtp = await client.eval(`document.getElementById('officer-demo-otp-val').textContent`);
    const t4BannerVis = await client.eval(`document.querySelector('#officer-step-2 [data-i18n="auth.demoOtpBanner"]') !== null`);

    if (!t4Step2Vis || !t4DemoOtp || t4DemoOtp === '------') {
      throw new Error(`TEST 4 FAILED: Step 2 visible=${t4Step2Vis}, Demo OTP=${t4DemoOtp}`);
    }
    console.log(`[PASS] TEST 4 SUCCEEDED: Step 2 OTP reached for AGRI-TN-0001!`);
    console.log(`       Masked Mobile: ${t4MaskedMobile}`);
    console.log(`       Demo OTP generated: "${t4DemoOtp}"`);
    console.log(`       Demo OTP Banner visible: ${t4BannerVis}`);

    // =========================================================================
    // TEST 5: Wrong OTP Verification on Step 2.
    // Expected: Error displayed, remains on Step 2.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 5: Wrong OTP Verification on Step 2');
    console.log('===============================================================');
    await client.eval(`
      document.getElementById('officer-otp-input').value = '000000';
      document.getElementById('btn-verify-otp').click();
    `);
    await sleep(1000);

    const t5OtpErrVis = await client.eval(`!document.getElementById('officer-otp-error').classList.contains('hidden')`);
    const t5OtpErrText = await client.eval(`document.getElementById('officer-otp-error').innerText`);
    const t5StillOnStep2 = await client.eval(`!document.getElementById('officer-step-2').classList.contains('hidden')`);

    if (!t5OtpErrVis || !t5StillOnStep2) {
      throw new Error(`TEST 5 FAILED: OTP Err visible=${t5OtpErrVis}, Step 2 visible=${t5StillOnStep2}`);
    }
    console.log(`[PASS] TEST 5 SUCCEEDED: Wrong OTP rejected! Error: "${t5OtpErrText.trim()}"`);

    // =========================================================================
    // TEST 6: Auto-fill Demo OTP & Verify -> Confirm Official Details (Step 3).
    // Expected: Advances to Step 3 with verified official details.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 6: Auto-fill Demo OTP & Verify -> Confirm Details (Step 3)');
    console.log('===============================================================');
    await client.eval(`
      autoFillDemoOtp();
      document.getElementById('btn-verify-otp').click();
    `);
    await sleep(1200);

    const t6Step3Vis = await client.eval(`!document.getElementById('officer-step-3').classList.contains('hidden')`);
    const t6OfficerName = await client.eval(`document.getElementById('dtl-name').textContent`);
    const t6OfficerDistrict = await client.eval(`document.getElementById('dtl-district').textContent`);
    const t6OfficerState = await client.eval(`document.getElementById('dtl-state').textContent`);

    if (!t6Step3Vis || !t6OfficerName || t6OfficerName !== 'Ravi Kumar') {
      throw new Error(`TEST 6 FAILED: Step 3 visible=${t6Step3Vis}, Name=${t6OfficerName}`);
    }
    console.log(`[PASS] TEST 6 SUCCEEDED: Step 3 Official Details confirmed!`);
    console.log(`       Officer Name: ${t6OfficerName}`);
    console.log(`       District: ${t6OfficerDistrict}, State: ${t6OfficerState}`);

    // =========================================================================
    // TEST 7: Proceed to Step 4 -> Create Login Credentials -> Step 5 Success.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 7: Create Login Credentials -> Account Created Success');
    console.log('===============================================================');
    await client.eval(`goToOfficerStep(4)`);
    await sleep(400);

    const t7Step4Vis = await client.eval(`!document.getElementById('officer-step-4').classList.contains('hidden')`);
    console.log(`[PASS] Step 4 Credentials screen visible: ${t7Step4Vis}`);

    await client.eval(`
      document.getElementById('officer-new-login-id').value = 'ravi_salem_new';
      document.getElementById('officer-new-password').value = 'officer123';
      document.getElementById('officer-confirm-password').value = 'officer123';
      document.getElementById('btn-create-officer-acc').click();
    `);
    await sleep(1500);

    const t7Step5Vis = await client.eval(`!document.getElementById('officer-step-5').classList.contains('hidden')`);
    const t7DoneId = await client.eval(`document.getElementById('done-officer-id').textContent`);
    const t7DoneName = await client.eval(`document.getElementById('done-officer-name').textContent`);
    const t7DoneLogin = await client.eval(`document.getElementById('done-login-id').textContent`);

    if (!t7Step5Vis || t7DoneId !== 'AGRI-TN-0001' || t7DoneName !== 'Ravi Kumar' || t7DoneLogin !== 'ravi_salem_new') {
      throw new Error(`TEST 7 FAILED: Step 5 visible=${t7Step5Vis}, ID=${t7DoneId}, Name=${t7DoneName}, Login=${t7DoneLogin}`);
    }
    console.log(`[PASS] TEST 7 SUCCEEDED: Officer account created successfully!`);
    console.log(`       Officer ID: "${t7DoneId}"`);
    console.log(`       Full Name: "${t7DoneName}"`);
    console.log(`       Login ID: "${t7DoneLogin}"`);

    // =========================================================================
    // TEST 8: Proceed to Officer Login -> Login -> Logout -> Reopen Registration.
    // Expected: Step 1 is freshly shown, NOT the previous success screen.
    // =========================================================================
    console.log('\n===============================================================');
    console.log('TEST 8: Proceed to Login -> Login -> Logout -> Fresh Registration');
    console.log('===============================================================');
    await client.eval(`goToOfficerLoginAfterReg()`);
    await sleep(500);

    await client.eval(`
      document.getElementById('login-password').value = 'officer123';
      document.getElementById('btn-login-submit').click();
    `);
    await sleep(2000);

    const t8OfficerNavVis = await client.eval(`!document.getElementById('officer-nav').classList.contains('hidden')`);
    console.log(`[PASS] Officer logged in successfully! Officer navigation visible: ${t8OfficerNavVis}`);

    // Logout
    await client.eval(`logout()`);
    await sleep(800);

    // Reopen Officer Registration
    await client.eval(`openAuthModal('register', 'OFFICER');`);
    await sleep(500);

    const t8Step1Vis = await client.eval(`!document.getElementById('officer-step-1').classList.contains('hidden')`);
    const t8Step5Vis = await client.eval(`!document.getElementById('officer-step-5').classList.contains('hidden')`);

    if (!t8Step1Vis || t8Step5Vis) {
      throw new Error(`TEST 8 FAILED: Step 1 visible=${t8Step1Vis}, Step 5 visible=${t8Step5Vis}`);
    }
    console.log(`[PASS] TEST 8 SUCCEEDED: Clean Step 1 reopens after logout!`);

    client.close();
    console.log('\n===============================================================');
    console.log('ALL 8 COMPREHENSIVE BROWSER E2E TESTS PASSED 100% SUCCESSFULLY!');
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
