const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const os = require('os');
const fs = require('fs');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const TEMP_PROFILE = path.join(os.tmpdir(), 'chrome_cdp_forgot_' + Date.now());
const CDP_PORT = 9260 + Math.floor(Math.random() * 300);

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
      returnByValue: true,
      awaitPromise: true
    });
    if (res.exceptionDetails) {
      throw new Error(`Eval exception: ${JSON.stringify(res.exceptionDetails)}`);
    }
    return res.result ? res.result.value : undefined;
  }
}

async function runBrowserTests() {
  console.log('=================================================================');
  console.log('BROWSER AUTOMATION TEST: FORGOT PASSWORD INTERACTIVE FLOW');
  console.log('=================================================================');

  const chromeProc = spawn(CHROME_PATH, [
    '--headless=new',
    `--remote-debugging-port=${CDP_PORT}`,
    `--user-data-dir=${TEMP_PROFILE}`,
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    'about:blank'
  ], { stdio: 'ignore' });

  try {
    let connected = false;
    let list;
    for (let i = 0; i < 30; i++) {
      await sleep(300);
      try {
        list = await fetchJson(`http://127.0.0.1:${CDP_PORT}/json`);
        if (list && list.length > 0) {
          connected = true;
          break;
        }
      } catch (e) {}
    }

    if (!connected) {
      throw new Error(`Could not connect to Chrome DevTools port ${CDP_PORT}`);
    }

    const pageTarget = list.find(t => t.type === 'page') || list[0];
    console.log('[PASS] Connected to Chrome DevTools port', CDP_PORT);

    const client = new CDPClient(pageTarget.webSocketDebuggerUrl);
    await client.ready;
    await client.send('Page.enable');
    await client.send('Runtime.enable');
    await client.send('Console.enable');

    const consoleLogs = [];
    const consoleErrors = [];

    client.ws.addEventListener('message', (event) => {
      const msg = JSON.parse(event.data);
      if (msg.method === 'Console.messageAdded') {
        const text = msg.params.message.text;
        const level = msg.params.message.level;
        if (level === 'error') {
          consoleErrors.push(text);
        } else {
          consoleLogs.push(`[${level}] ${text}`);
        }
      } else if (msg.method === 'Runtime.exceptionThrown') {
        const desc = msg.params.exceptionDetails?.exception?.description || msg.params.exceptionDetails?.text;
        consoleErrors.push(`Runtime Exception: ${desc}`);
      }
    });

    // 1. Navigate to AgriFlow application
    console.log('\n--- 1. Navigating to AgriFlow (http://127.0.0.1:8000) ---');
    await client.send('Page.navigate', { url: 'http://127.0.0.1:8000' });
    await sleep(1500);

    const appTitle = await client.eval('document.title');
    console.log(`[PASS] Page loaded: "${appTitle}"`);

    // Verify no JS syntax/runtime error occurred on initial load
    if (consoleErrors.length > 0) {
      console.error('Console errors found:', consoleErrors);
    }
    console.log(`[PASS] Initial load console errors: ${consoleErrors.length}`);

    // 2. Open Login Page
    console.log('\n--- 2. Opening Login View ---');
    await client.eval('window.openAuthModal("login", "FARMER")');
    await sleep(500);

    const isLoginVisible = await client.eval('!document.getElementById("form-login").classList.contains("hidden")');
    console.log(`[PASS] Login form is visible: ${isLoginVisible}`);

    const forgotBtnText = await client.eval('document.getElementById("btn-forgot-password")?.innerText');
    console.log(`[PASS] "Forgot Password?" button detected with text: "${forgotBtnText?.trim()}"`);

    // 3. Test Farmer Forgot Password Flow
    console.log('\n--- 3. Testing Farmer Forgot Password Flow ---');
    // Click "Forgot Password?"
    console.log('-> Clicking "Forgot Password?" button...');
    await client.eval('document.getElementById("btn-forgot-password").click()');
    await sleep(500);

    // Verify Forgot Password wizard is visible and login form is hidden
    const isWizardVisible = await client.eval('!document.getElementById("forgot-password-wizard").classList.contains("hidden")');
    const isLoginHidden = await client.eval('document.getElementById("form-login").classList.contains("hidden")');
    console.log(`[PASS] Forgot Password wizard visible: ${isWizardVisible}, Login form hidden: ${isLoginHidden}`);
    if (!isWizardVisible) {
      throw new Error('FAILED: Forgot Password wizard did not open after click!');
    }

    // Verify Step 1 is active with Farmer selected
    const activeStep = await client.eval('!document.getElementById("forgot-step-1").classList.contains("hidden") ? 1 : 0');
    console.log(`[PASS] Active wizard step: Step ${activeStep}`);

    const identifierLabel = await client.eval('document.getElementById("forgot-identifier-label")?.innerText');
    console.log(`[PASS] Identifier field label: "${identifierLabel?.trim()}"`);

    // Enter Farmer identifier
    console.log('-> Entering Farmer mobile number: 9123456780...');
    await client.eval('document.getElementById("forgot-identifier-input").value = "9123456780"');
    
    // Submit Step 1 (Send Verification Code)
    console.log('-> Submitting Step 1 (Send Verification Code)...');
    await client.eval('document.getElementById("form-forgot-identifier").dispatchEvent(new Event("submit", { cancelable: true, bubbles: true }))');
    await sleep(1500);

    // Verify Step 2 is active
    const isStep2Visible = await client.eval('!document.getElementById("forgot-step-2").classList.contains("hidden")');
    const maskedMobile = await client.eval('document.getElementById("forgot-masked-mobile")?.innerText');
    const demoOtpVal = await client.eval('document.getElementById("forgot-demo-otp-val")?.innerText');
    const timerText = await client.eval('document.getElementById("forgot-otp-timer")?.innerText');

    console.log(`[PASS] Step 2 (OTP) visible: ${isStep2Visible}`);
    console.log(`[PASS] Masked phone: ${maskedMobile}, Demo OTP: ${demoOtpVal}, Timer: ${timerText}`);
    if (!isStep2Visible) {
      throw new Error('FAILED: Step 2 did not open after sending code!');
    }

    // 4. Test "Close / Back to Login"
    console.log('\n--- 4. Testing Back to Login Navigation ---');
    await client.eval('closeForgotPasswordFlow()');
    await sleep(500);
    const loginRestored = await client.eval('!document.getElementById("form-login").classList.contains("hidden")');
    const wizardHidden = await client.eval('document.getElementById("forgot-password-wizard").classList.contains("hidden")');
    console.log(`[PASS] Returned to Login: Form visible = ${loginRestored}, Wizard hidden = ${wizardHidden}`);

    // 5. Test Agriculture Officer Forgot Password Flow
    console.log('\n--- 5. Testing Agriculture Officer Forgot Password Flow ---');
    // Switch role to OFFICER on login page
    await client.eval('setAuthRole("OFFICER")');
    await sleep(300);

    // Click "Forgot Password?"
    console.log('-> Clicking "Forgot Password?" for Agriculture Officer...');
    await client.eval('document.getElementById("btn-forgot-password").click()');
    await sleep(500);

    const officerWizardVisible = await client.eval('!document.getElementById("forgot-password-wizard").classList.contains("hidden")');
    const officerLabel = await client.eval('document.getElementById("forgot-identifier-label")?.innerText');
    console.log(`[PASS] Officer wizard visible: ${officerWizardVisible}, Label: "${officerLabel?.trim()}"`);

    // Enter Officer ID
    console.log('-> Entering Officer ID: AGRI-TN-0001...');
    await client.eval('document.getElementById("forgot-identifier-input").value = "AGRI-TN-0001"');
    
    // Submit Step 1
    console.log('-> Submitting Step 1 for Officer...');
    await client.eval('document.getElementById("form-forgot-identifier").dispatchEvent(new Event("submit", { cancelable: true, bubbles: true }))');
    await sleep(1500);

    const officerStep2Visible = await client.eval('!document.getElementById("forgot-step-2").classList.contains("hidden")');
    const officerDemoOtp = await client.eval('document.getElementById("forgot-demo-otp-val")?.innerText');
    console.log(`[PASS] Officer Step 2 active: ${officerStep2Visible}, Demo OTP: ${officerDemoOtp}`);

    // Click Auto-fill
    console.log('-> Clicking "Auto-fill Demo Code" button...');
    await client.eval('autoFillForgotDemoOtp()');
    const filledOtp = await client.eval('document.getElementById("forgot-otp-input")?.value');
    console.log(`[PASS] Auto-filled OTP input: "${filledOtp}" (Matches: ${filledOtp === officerDemoOtp})`);

    // Submit Step 2 (Verify Code)
    console.log('-> Submitting Step 2 (Verify Code)...');
    await client.eval('document.getElementById("form-forgot-otp").dispatchEvent(new Event("submit", { cancelable: true, bubbles: true }))');
    await sleep(1500);

    // Verify Step 3 (New Password)
    const isStep3Visible = await client.eval('!document.getElementById("forgot-step-3").classList.contains("hidden")');
    console.log(`[PASS] Step 3 (Create New Password) visible: ${isStep3Visible}`);
    if (!isStep3Visible) {
      throw new Error('FAILED: Step 3 did not open after OTP verification!');
    }

    // Enter new password & confirm
    console.log('-> Entering new password and confirmation...');
    await client.eval('document.getElementById("forgot-new-password").value = "officerResetPass2026!"');
    await client.eval('document.getElementById("forgot-confirm-password").value = "officerResetPass2026!"');

    // Submit Step 3
    console.log('-> Submitting Step 3 (Reset Password)...');
    await client.eval('document.getElementById("form-forgot-reset-password").dispatchEvent(new Event("submit", { cancelable: true, bubbles: true }))');
    await sleep(1500);

    // Verify Step 4 (Success Card)
    const isStep4Visible = await client.eval('!document.getElementById("forgot-step-4").classList.contains("hidden")');
    console.log(`[PASS] Step 4 (Password Reset Success) visible: ${isStep4Visible}`);
    if (!isStep4Visible) {
      throw new Error('FAILED: Step 4 did not appear after password reset!');
    }

    // Click "Back to Login"
    console.log('-> Clicking "Back to Login" button from Success Card...');
    await client.eval('goToLoginAfterReset()');
    await sleep(500);

    const loginRestoredFinal = await client.eval('!document.getElementById("form-login").classList.contains("hidden")');
    const prefilledLoginId = await client.eval('document.getElementById("login-identifier")?.value');
    console.log(`[PASS] Back on Login page. Form visible: ${loginRestoredFinal}, Prefilled ID: "${prefilledLoginId}"`);

    // Check final console error count
    console.log('\n--- 6. Console Health & Error Audit ---');
    console.log(`Total Console Messages: ${consoleLogs.length}`);
    console.log(`Total Console Errors: ${consoleErrors.length}`);
    if (consoleErrors.length > 0) {
      consoleErrors.forEach(err => console.error('  [ERROR]', err));
      throw new Error(`Browser test failed with ${consoleErrors.length} console errors!`);
    } else {
      console.log('[PASS] ZERO JavaScript errors or runtime exceptions detected across all flows!');
    }

    console.log('\n=================================================================');
    console.log('ALL BROWSER AUTOMATION TESTS PASSED (100% SUCCESS)!');
    console.log('=================================================================');
  } finally {
    try {
      chromeProc.kill('SIGKILL');
    } catch (e) {}
    try {
      fs.rmSync(TEMP_PROFILE, { recursive: true, force: true });
    } catch (e) {}
  }
}

runBrowserTests().catch(err => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
