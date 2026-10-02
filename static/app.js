  // AgriFlow Frontend Application Logic

  const STATE = {
    token: localStorage.getItem('agriflow_token') || null,
    user: null,
    profile: null,
    currentView: 'landing',
    locations: {},
    produce: [],
    officerRequests: [],
    farmerRequests: [],
    ws: null,
    searchDebounceTimer: null
  };

  // Crop Emoji Mapping
  const CROP_EMOJIS = {
    'onion': '🧅',
    'tomato': '🍅',
    'potato': '🥔',
    'carrot': '🥕',
    'corn': '🌽',
    'maize': '🌽',
    'rice': '🌾',
    'paddy': '🌾',
    'wheat': '🌾',
    'cotton': '🌱',
    'sugarcane': '🎋',
    'banana': '🍌',
    'mango': '🥭',
    'chilli': '🌶️',
    'garlic': '🧄',
    'cabbage': '🥬',
    'cauliflower': '🥦',
    'turmeric': '🌿',
    'groundnut': '🥜'
  };

  function getCropEmoji(cropName) {
    if (!cropName) return '🌱';
    const clean = cropName.toLowerCase().trim();
    for (const [key, emoji] of Object.entries(CROP_EMOJIS)) {
      if (clean.includes(key)) return emoji;
    }
    return '🌱';
  }

  // Centralized Translation Helpers
  function t(key, params, localeOverride, defaultFallback) {
    if (window.AgriFlowI18n && typeof window.AgriFlowI18n.t === 'function') {
      return window.AgriFlowI18n.t(key, params, localeOverride, defaultFallback);
    }
    return defaultFallback !== undefined ? defaultFallback : key;
  }
  window.t = t;

  const CROP_KEY_MAP = {
    'onion': 'onion',
    'tomato': 'tomato',
    'potato': 'potato',
    'rice': 'rice',
    'paddy': 'rice',
    'wheat': 'wheat',
    'maize': 'maize',
    'corn': 'maize',
    'carrot': 'carrot',
    'cabbage': 'cabbage',
    'cauliflower': 'cauliflower',
    'garlic': 'garlic',
    'ginger': 'ginger',
    'banana': 'banana',
    'mango': 'mango',
    'groundnut': 'groundnut',
    'sugarcane': 'sugarcane',
    'cotton': 'cotton'
  };

  function translateCrop(cropName) {
    if (!cropName) return '';
    const clean = cropName.toLowerCase().trim();
    for (const [key, cropKey] of Object.entries(CROP_KEY_MAP)) {
      if (clean.includes(key)) {
        return t(`crops.${cropKey}`, {}, undefined, cropName);
      }
    }
    return cropName;
  }
  window.translateCrop = translateCrop;

  const PRODUCE_TYPE_MAP = {
    'vegetable / bulbs': 'vegetable_bulbs',
    'vegetables / bulbs': 'vegetable_bulbs',
    'vegetable': 'vegetable',
    'vegetables': 'vegetable',
    'tubers': 'tubers',
    'field crop': 'field_crop',
    'cereals / grains': 'cereals',
    'cereals': 'cereals',
    'grains': 'cereals',
    'fruits': 'fruits',
    'cash crops': 'cash_crops',
    'spices': 'spices'
  };

  function translateProduceType(produceType) {
    if (!produceType) return t('produce_types.field_crop', {}, undefined, 'Field Crop');
    const clean = produceType.toLowerCase().trim();
    const typeKey = PRODUCE_TYPE_MAP[clean];
    if (typeKey) {
      return t(`produce_types.${typeKey}`, {}, undefined, produceType);
    }
    return produceType;
  }
  window.translateProduceType = translateProduceType;

  const QUALITY_MAP = {
    'grade a (premium)': 'gradeAPremium',
    'grade b (standard)': 'gradeBStandard',
    'grade c (fair)': 'gradeCFair',
    'grade a': 'gradeA',
    'grade b': 'gradeB',
    'grade c': 'gradeC'
  };

  function translateQuality(quality) {
    if (!quality) return t('qualities.gradeA', {}, undefined, 'Grade A');
    const clean = quality.toLowerCase().trim();
    const qKey = QUALITY_MAP[clean];
    if (qKey) {
      return t(`qualities.${qKey}`, {}, undefined, quality);
    }
    return quality;
  }
  window.translateQuality = translateQuality;

  const UNIT_MAP = {
    'tons': 'tons',
    'ton': 'tons',
    'quintals': 'quintals',
    'quintal': 'quintals',
    'kg': 'kg',
    'acres': 'acres',
    'acre': 'acres',
    'hectares': 'hectares',
    'hectare': 'hectares'
  };

  function translateUnit(unit) {
    if (!unit) return '';
    const clean = unit.toLowerCase().trim();
    const uKey = UNIT_MAP[clean];
    if (uKey) {
      return t(`units.${uKey}`, {}, undefined, unit);
    }
    return unit;
  }
  window.translateUnit = translateUnit;

  const STATUS_MAP = {
    'verified': 'verified',
    'pending': 'pending',
    'rejected': 'rejected',
    'available': 'available',
    'unavailable': 'unavailable'
  };

  function translateStatus(status) {
    if (!status) return '';
    const clean = status.toLowerCase().trim();
    const sKey = STATUS_MAP[clean];
    if (sKey) {
      return t(`statuses.${sKey}`, {}, undefined, status);
    }
    return status;
  }
  window.translateStatus = translateStatus;

  function translateSource(sourceType) {
    if (sourceType === 'officer_local' || sourceType === 'OFFICER_ENTRY') {
      return t('produce.sourceOfficer', {}, undefined, 'Officer Verified');
    } else if (sourceType === 'farmer_verified' || sourceType === 'FARMER_VERIFIED') {
      return t('produce.sourceFarmer', {}, undefined, 'Farmer Verified');
    }
    return sourceType;
  }
  window.translateSource = translateSource;

  const STAGE_MAP = {
    'bulb development / pre-harvest': 'bulbDevelopment',
    'bulb development': 'bulbDevelopment',
    'vegetative stage': 'vegetative',
    'vegetative': 'vegetative',
    'flowering': 'flowering',
    'maturity / ready for harvest': 'readyForHarvest',
    'ready for harvest': 'readyForHarvest',
    'pre-harvest': 'preHarvest'
  };

  function translateCropStage(stage) {
    if (!stage) return '';
    const clean = stage.toLowerCase().trim();
    const stKey = STAGE_MAP[clean];
    if (stKey) {
      return t(`crop_stages.${stKey}`, {}, undefined, stage);
    }
    return stage;
  }
  window.translateCropStage = translateCropStage;

  // Price formatting and dynamic unit helper
  function formatProducePrice(price, unit) {
    if (price === null || price === undefined || price === '' || isNaN(price)) {
      return null;
    }
    const num = parseFloat(price);
    let unitSingular = unit || 'unit';
    if (unitSingular.toLowerCase() === 'tons') unitSingular = 'Ton';
    else if (unitSingular.toLowerCase() === 'quintals') unitSingular = 'Quintal';

    const translatedUnit = translateUnit(unitSingular);
    const formattedNum = num.toLocaleString('en-IN', { maximumFractionDigits: 2 });
    return {
      num: num,
      formatted: `₹ ${formattedNum}`,
      unitSuffix: `/ ${translatedUnit}`,
      full: `₹ ${formattedNum} / ${translatedUnit}`
    };
  }

  function updatePriceUnitLabel() {
    const unitSelect = document.getElementById('op-unit');
    if (!unitSelect) return;
    const unit = unitSelect.value || 'Tons';
    let unitSingular = unit;
    if (unit.toLowerCase() === 'tons') unitSingular = 'Ton';
    else if (unit.toLowerCase() === 'quintals') unitSingular = 'Quintal';

    const translatedUnit = translateUnit(unitSingular);
    const hintEl = document.getElementById('op-price-unit-hint');
    if (hintEl) hintEl.innerText = `(₹ / ${translatedUnit})`;

    const tagEl = document.getElementById('op-price-unit-tag');
    if (tagEl) tagEl.innerText = `/ ${translatedUnit}`;

    const descEl = document.getElementById('op-price-dynamic-desc');
    if (descEl) {
      const exampleVal = unitSingular === 'Ton' ? '25,000' : (unitSingular === 'Quintal' ? '2,500' : '25');
      const pricePerSelectedUnitText = t('produce.pricePerUnit', {}, undefined, `Price per ${translatedUnit}`);
      descEl.innerText = `${pricePerSelectedUnitText} (e.g. ₹ ${exampleVal} / ${translatedUnit})`;
    }
  }
  window.updatePriceUnitLabel = updatePriceUnitLabel;
  window.formatProducePrice = formatProducePrice;

  // Initialization on DOM Ready
  document.addEventListener('DOMContentLoaded', async () => {
    if (window.AgriFlowI18n) {
      window.AgriFlowI18n.init();
    }
    setupWebSocket();
    await loadLocations();
    await checkSession();
    resetOfficerRegistrationState(true);

    // Initialize lucide icons
    lucide.createIcons();

    // Handle URL hash routing if present
    const hash = window.location.hash.replace('#', '');
    if (hash) {
      navigate(hash);
    } else {
      navigate('landing');
    }
  });

  // Real-Time WebSocket Connection
  function setupWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const wsUrl = `${protocol}//${window.location.host}/ws`;

    try {
      STATE.ws = new WebSocket(wsUrl);

      STATE.ws.onopen = () => {
        // WebSocket connection established successfully
      };

      STATE.ws.onmessage = (event) => {
        try {
          const msg = JSON.parse(event.data);
          handleRealTimeMessage(msg);
        } catch (e) {
          console.error("WS parse error:", e);
        }
      };

      STATE.ws.onclose = () => {
        // WebSocket reconnect logic runs silently in the background without UI interruption
        setTimeout(setupWebSocket, 3000);
      };
    } catch (err) {
      console.error("WS connection error:", err);
    }
  }

  function handleRealTimeMessage(msg) {
    if (msg.type === 'PRODUCE_ADDED') {
      const msgText = t('notifications.newProduceAdded', {
        crop: translateCrop(msg.record.crop_name),
        qty: msg.record.quantity,
        unit: translateUnit(msg.record.unit),
        area: msg.record.area
      }, undefined, `🌾 New produce added: ${msg.record.crop_name} (${msg.record.quantity} ${msg.record.unit}) in ${msg.record.area}`);
      showToast(msgText, 'info');
      if (STATE.currentView === 'produce') loadProduceList();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'PRODUCE_UPDATED') {
      const msgText = t('notifications.produceUpdated', {
        crop: translateCrop(msg.record.crop_name)
      }, undefined, `🔄 Produce updated: ${msg.record.crop_name}`);
      showToast(msgText, 'info');
      if (STATE.currentView === 'produce') loadProduceList();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'PRODUCE_DELETED') {
      if (STATE.currentView === 'produce') loadProduceList();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'REQUEST_SUBMITTED') {
      const msgText = t('notifications.newFarmerSubmission', {
        crop: translateCrop(msg.request.crop_name),
        qty: msg.request.expected_quantity,
        unit: translateUnit(msg.request.quantity_unit),
        area: msg.request.area
      }, undefined, `📋 New Farmer crop submission: ${msg.request.crop_name} (${msg.request.expected_quantity} ${msg.request.quantity_unit}) in ${msg.request.area}`);
      showToast(msgText, 'info');
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
      if (STATE.currentView === 'farmer-dashboard') loadFarmerDashboard();
    } else if (msg.type === 'REQUEST_VERIFIED') {
      const msgText = t('notifications.cropVerified', {
        crop: translateCrop(msg.request.crop_name),
        qty: msg.request.expected_quantity,
        unit: translateUnit(msg.request.quantity_unit),
        area: msg.request.area || ''
      }, undefined, `✅ Crop verified: ${msg.request.crop_name} (${msg.request.expected_quantity} ${msg.request.quantity_unit}) is now live!`);
      showToast(msgText, 'success');
      if (STATE.currentView === 'farmer-dashboard') loadFarmerDashboard();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
      if (STATE.currentView === 'produce') loadProduceList();
    } else if (msg.type === 'REQUEST_REJECTED') {
      const msgText = t('notifications.farmerRequestRejected', {
        crop: translateCrop(msg.request.crop_name)
      }, undefined, `⚠️ Farmer request rejected: ${msg.request.crop_name}`);
      showToast(msgText, 'warning');
      if (STATE.currentView === 'farmer-dashboard') loadFarmerDashboard();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'PURCHASE_REQUEST_RECEIVED') {
      const msgText = t('notifications.purchaseInquiry', {
        crop: translateCrop(msg.crop_name),
        qty: msg.request.requested_quantity,
        unit: translateUnit(msg.request.quantity_unit)
      }, undefined, `💼 Purchase Inquiry: Buyer requested ${msg.request.requested_quantity} ${msg.request.quantity_unit} of ${msg.crop_name}`);
      showToast(msgText, 'success');
      if (STATE.currentView === 'farmer-dashboard') {
        loadFarmerDashboard();
        loadFarmerPurchaseRequests();
      }
    } else if (msg.type === 'PURCHASE_REQUEST_UPDATED') {
      if (STATE.currentView === 'farmer-dashboard') {
        loadFarmerDashboard();
        loadFarmerPurchaseRequests();
      }
    } else if (msg.type === 'DEMO_RESET') {
      const msgText = t('notifications.demoReset', {}, undefined, `🔄 Demo data has been reset to initial state`);
      showToast(msgText, 'info');
      checkSession();
      if (STATE.currentView === 'produce') loadProduceList();
    }
  }

  // Session & Authentication
  async function checkSession() {
    if (!STATE.token) {
      updateNavAuth(false);
      return;
    }

    try {
      const res = await fetch('/api/auth/me', {
        headers: { 'Authorization': `Bearer ${STATE.token}` }
      });
      if (res.ok) {
        const data = await res.json();
        STATE.user = data.user;
        STATE.profile = data.profile;
        updateNavAuth(true);
      } else {
        logout();
      }
    } catch (err) {
      console.error("Session verification error:", err);
      logout();
    }
  }

  function refreshTranslatedUi() {
    if (window.AgriFlowI18n) {
      window.AgriFlowI18n.applyTranslations();
    }

    // Refresh location dropdowns with translated "All States/Districts/Areas" while preserving current selections
    populateLocationDropdowns(true);

    if (STATE.token && STATE.user) {
      updateNavAuth(true);
    }

    if (STATE.currentView === 'produce') {
      loadProduceList();
    } else if (STATE.currentView === 'officer-dashboard') {
      loadOfficerDashboard();
    } else if (STATE.currentView === 'farmer-dashboard') {
      loadFarmerDashboard();
    } else if (STATE.currentView === 'profile') {
      renderProfileForm();
    }

    // If produce details modal is currently open, refresh its content in current language
    const modal = document.getElementById('produce-details-modal');
    if (modal && !modal.classList.contains('hidden') && STATE.currentDetailsProduceId) {
      openProduceDetails(STATE.currentDetailsProduceId);
    }
  }

  window.refreshTranslatedUi = refreshTranslatedUi;

  function updateNavAuth(isLoggedIn) {
    const guestControls = document.getElementById('guest-controls');
    const userControls = document.getElementById('user-controls');
    const officerNav = document.getElementById('officer-nav');
    const farmerNav = document.getElementById('farmer-nav');

    if (isLoggedIn && STATE.user) {
      guestControls.classList.add('hidden');
      userControls.classList.remove('hidden');

      document.getElementById('nav-user-name').innerText = STATE.user.name;
      const roleText = STATE.user.role === 'OFFICER' ? t('roles.officer', {}, undefined, 'Agriculture Officer') : t('roles.farmer', {}, undefined, 'Farmer');
      document.getElementById('nav-user-role').innerText = roleText;
      document.getElementById('user-avatar-badge').innerText = STATE.user.name.charAt(0).toUpperCase();

      if (STATE.user.role === 'OFFICER') {
        officerNav.classList.remove('hidden');
        farmerNav.classList.add('hidden');
      } else {
        officerNav.classList.add('hidden');
        farmerNav.classList.remove('hidden');
      }
    } else {
      guestControls.classList.remove('hidden');
      userControls.classList.add('hidden');
      officerNav.classList.add('hidden');
      farmerNav.classList.add('hidden');
    }
    lucide.createIcons();
  }

  function logout() {
    if (STATE.token) {
      fetch('/api/auth/logout', {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${STATE.token}` }
      }).catch(() => {});
    }
    STATE.token = null;
    STATE.user = null;
    STATE.profile = null;
    localStorage.removeItem('agriflow_token');
    updateNavAuth(false);
    resetOfficerRegistrationState(true);
    showToast(t('auth.logoutSuccess', {}, undefined, "You have been signed out."), "info");
    navigate('landing');
  }

  // Navigation Controller
  function navigate(view, subaction = null) {
    // If leaving auth view after completing registration, reset the registration state cleanly
    if (view !== 'auth' && typeof officerRegState !== 'undefined' && officerRegState && officerRegState.step === 5) {
      resetOfficerRegistrationState(true);
    }
    // Authorization guards
    if (view === 'officer-dashboard' && (!STATE.user || STATE.user.role !== 'OFFICER')) {
      showToast("Please log in as an Agriculture Officer to access the Officer Portal.", "warning");
      openAuthModal('login', 'OFFICER');
      return;
    }

    if (view === 'farmer-dashboard' && (!STATE.user || STATE.user.role !== 'FARMER')) {
      showToast("Please log in as a Farmer to access the Farmer Portal.", "warning");
      openAuthModal('login', 'FARMER');
      return;
    }

    if (view === 'dashboard') {
      if (STATE.user?.role === 'OFFICER') view = 'officer-dashboard';
      else if (STATE.user?.role === 'FARMER') view = 'farmer-dashboard';
      else view = 'produce';
    }

    STATE.currentView = view;
    window.location.hash = view;

    // Hide all views
    document.querySelectorAll('.spa-view').forEach(el => el.classList.add('hidden'));

    // Highlight active nav links
    document.querySelectorAll('.nav-item').forEach(el => {
      if (el.getAttribute('data-view') === view) {
        el.classList.add('bg-brand-50', 'text-brand-800');
        el.classList.remove('text-slate-600');
      } else {
        el.classList.remove('bg-brand-50', 'text-brand-800');
        el.classList.add('text-slate-600');
      }
    });

    const targetView = document.getElementById(`view-${view}`);
    if (targetView) {
      targetView.classList.remove('hidden');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // View specific data load
    if (view === 'produce') {
      loadProduceList();
    } else if (view === 'officer-dashboard') {
      loadOfficerDashboard();
    } else if (view === 'farmer-dashboard') {
      loadFarmerDashboard();
    } else if (view === 'profile') {
      renderProfileForm();
    }

    lucide.createIcons();
  }

  // Locations Hierarchy
  async function loadLocations() {
    try {
      const res = await fetch('/api/public/locations');
      if (res.ok) {
        STATE.locations = await res.json();
        populateLocationDropdowns();
      }
    } catch (e) {
      console.error("Failed to load locations:", e);
    }
  }

  function populateLocationDropdowns(preserveSelections = false) {
    const stateSelect = document.getElementById('filter-state');
    const landingStateSelect = document.getElementById('landing-state-select');
    if (!stateSelect) return;

    const currentStateVal = stateSelect.value;
    const states = Object.keys(STATE.locations);
    if (states.length === 0) return;

    const allStatesLabel = t('common.allStates', {}, undefined, 'All States');
    let stateHtml = `<option value="All">${escapeHtml(allStatesLabel)}</option>`;
    states.forEach(st => {
      stateHtml += `<option value="${escapeHtml(st)}">${escapeHtml(st)}</option>`;
    });

    stateSelect.innerHTML = stateHtml;
    if (landingStateSelect) landingStateSelect.innerHTML = stateHtml;

    if (preserveSelections && currentStateVal && (currentStateVal === 'All' || states.includes(currentStateVal))) {
      stateSelect.value = currentStateVal;
      if (landingStateSelect) landingStateSelect.value = currentStateVal;
      onStateFilterChange(true);
    } else if (states.includes('Tamil Nadu')) {
      stateSelect.value = 'Tamil Nadu';
      if (landingStateSelect) landingStateSelect.value = 'Tamil Nadu';
      onStateFilterChange(false);
    } else {
      stateSelect.value = 'All';
      if (landingStateSelect) landingStateSelect.value = 'All';
      onStateFilterChange(false);
    }
  }

  function onStateFilterChange(preserveSelections = false) {
    const stateVal = document.getElementById('filter-state').value;
    const districtSelect = document.getElementById('filter-district');
    const areaSelect = document.getElementById('filter-area');

    const currentDistrictVal = districtSelect ? districtSelect.value : null;
    const allDistrictsLabel = t('common.allDistricts', {}, undefined, 'All Districts');
    let districtHtml = `<option value="All">${escapeHtml(allDistrictsLabel)}</option>`;
    if (stateVal !== 'All' && STATE.locations[stateVal]) {
      const districts = Object.keys(STATE.locations[stateVal]);
      districts.forEach(dt => {
        districtHtml += `<option value="${escapeHtml(dt)}">${escapeHtml(dt)}</option>`;
      });
    }
    districtSelect.innerHTML = districtHtml;

    if (preserveSelections && currentDistrictVal && (currentDistrictVal === 'All' || (stateVal !== 'All' && STATE.locations[stateVal]?.[currentDistrictVal]))) {
      districtSelect.value = currentDistrictVal;
    } else if (stateVal === 'Tamil Nadu') {
      districtSelect.value = 'Salem';
    } else {
      districtSelect.value = 'All';
    }

    onDistrictFilterChange(preserveSelections);
  }

  function onDistrictFilterChange(preserveSelections = false) {
    const stateVal = document.getElementById('filter-state').value;
    const districtVal = document.getElementById('filter-district').value;
    const areaSelect = document.getElementById('filter-area');

    const currentAreaVal = areaSelect ? areaSelect.value : null;
    const allAreasLabel = t('common.allAreas', {}, undefined, 'All Areas');
    let areaHtml = `<option value="All">${escapeHtml(allAreasLabel)}</option>`;
    if (stateVal !== 'All' && districtVal !== 'All' && STATE.locations[stateVal]?.[districtVal]) {
      const areas = STATE.locations[stateVal][districtVal];
      areas.forEach(ar => {
        areaHtml += `<option value="${escapeHtml(ar)}">${escapeHtml(ar)}</option>`;
      });
    }
    areaSelect.innerHTML = areaHtml;

    if (preserveSelections && currentAreaVal && (currentAreaVal === 'All' || (stateVal !== 'All' && districtVal !== 'All' && STATE.locations[stateVal]?.[districtVal]?.includes(currentAreaVal)))) {
      areaSelect.value = currentAreaVal;
    } else if (districtVal === 'Salem') {
      areaSelect.value = 'Sankari';
    } else {
      areaSelect.value = 'All';
    }

    if (!preserveSelections) {
      loadProduceList();
    }
  }

  // -------------------------------------------------------------
  // PUBLIC PRODUCE SEARCH & DISCOVERY (Section 11, 12, 13)
  // -------------------------------------------------------------
  function debounceProduceSearch() {
    clearTimeout(STATE.searchDebounceTimer);
    STATE.searchDebounceTimer = setTimeout(loadProduceList, 250);
  }

  function triggerLandingSearch() {
    const crop = document.getElementById('landing-crop-input').value;
    const state = document.getElementById('landing-state-select').value;
    const district = document.getElementById('landing-district-select').value;

    navigate('produce');

    document.getElementById('filter-crop').value = crop;
    if (state) document.getElementById('filter-state').value = state;
    onStateFilterChange();
    if (district) document.getElementById('filter-district').value = district;
    onDistrictFilterChange();
  }

  function resetProduceFilters() {
    document.getElementById('filter-crop').value = '';
    document.getElementById('filter-min-qty').value = '';
    document.getElementById('filter-max-qty').value = '';
    document.getElementById('filter-date').value = '';
    document.getElementById('filter-verified-only').checked = true;
    document.getElementById('filter-state').value = 'All';
    onStateFilterChange();
  }

  async function loadProduceList() {
    const crop = document.getElementById('filter-crop').value;
    const state = document.getElementById('filter-state').value;
    const district = document.getElementById('filter-district').value;
    const area = document.getElementById('filter-area').value;
    const minQty = document.getElementById('filter-min-qty').value;
    const maxQty = document.getElementById('filter-max-qty').value;
    const availDate = document.getElementById('filter-date').value;
    const verifiedOnly = document.getElementById('filter-verified-only').checked;

    const params = new URLSearchParams();
    if (crop && crop.trim()) params.append('crop', crop.trim());
    if (state && state !== 'All') params.append('state', state);
    if (district && district !== 'All') params.append('district', district);
    if (area && area !== 'All') params.append('area', area);
    if (minQty) params.append('min_qty', minQty);
    if (maxQty) params.append('max_qty', maxQty);
    if (availDate) params.append('availability_date', availDate);
    params.append('verified_only', verifiedOnly ? 'true' : 'false');

    try {
      const res = await fetch(`/api/public/produce?${params.toString()}`);
      if (res.ok) {
        STATE.produce = await res.json();
        renderProduceGrid(STATE.produce);
      }
    } catch (err) {
      console.error("Failed to load produce records:", err);
    }
  }

  function renderProduceGrid(items) {
    const grid = document.getElementById('produce-grid');
    const emptyState = document.getElementById('produce-empty-state');
    const countText = document.getElementById('produce-count-text');

    const countTemplate = items.length === 1 ? 'produce.count' : 'produce.countPlural';
    const fallbackCountText = `Showing ${items.length} verified produce record${items.length === 1 ? '' : 's'}`;
    countText.innerText = t(countTemplate, { count: items.length }, undefined, fallbackCountText);

    if (items.length === 0) {
      grid.innerHTML = '';
      emptyState.classList.remove('hidden');
      return;
    }

    emptyState.classList.add('hidden');

    let html = '';
    items.forEach(p => {
      const emoji = getCropEmoji(p.crop_name);
      const isOfficer = p.source_type === 'officer_local' || p.source_type === 'OFFICER_ENTRY';
      const sourceBadgeClass = isOfficer ? 'bg-emerald-100 text-emerald-800' : 'bg-blue-100 text-blue-800';
      const sourceIcon = isOfficer ? 'shield-check' : 'tractor';
      const priceInfo = formatProducePrice(p.price, p.unit);
      const priceDisplayHtml = priceInfo
        ? `<div class="text-xl font-black text-amber-950 flex items-baseline space-x-1 mt-0.5">
             <span>${priceInfo.formatted}</span>
             <span class="text-xs font-bold text-amber-700">${escapeHtml(priceInfo.unitSuffix)}</span>
           </div>`
        : `<div class="text-sm font-semibold text-slate-400 mt-1">
             <span>${escapeHtml(t('produce.priceOnInquiry', {}, undefined, 'On Inquiry'))}</span>
           </div>`;

      html += `
        <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:shadow-md hover:border-brand-300 transition flex flex-col justify-between space-y-4">
          <div>
            <!-- Card Header: Emoji, Crop Name, Status -->
            <div class="flex items-start justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-3xl p-2 rounded-xl bg-slate-50 border border-slate-100">${emoji}</span>
                <div>
                  <h3 class="text-lg font-bold text-slate-900 leading-tight">${escapeHtml(translateCrop(p.crop_name))}</h3>
                  <span class="text-[11px] text-slate-500 font-medium">${escapeHtml(translateProduceType(p.produce_type || 'Field Crop'))}</span>
                </div>
              </div>
              <span class="badge-verified text-[11px] font-bold px-2 py-0.5 rounded-full inline-flex items-center space-x-1">
                <span>${escapeHtml(t('produce.verifiedBadge', {}, undefined, '✓ VERIFIED'))}</span>
              </span>
            </div>

            <!-- Quantity & Price Display -->
            <div class="mt-4 grid grid-cols-2 gap-2">
              <div class="p-3 rounded-xl bg-emerald-50/70 border border-emerald-100">
                <span class="text-[11px] font-semibold text-emerald-800 uppercase tracking-wider block">${escapeHtml(t('produce.availableQuantity', {}, undefined, 'Available Quantity'))}</span>
                <div class="text-xl font-black text-emerald-950 flex items-baseline space-x-1 mt-0.5">
                  <span>${p.quantity}</span>
                  <span class="text-xs font-bold text-emerald-700">${escapeHtml(translateUnit(p.unit))}</span>
                </div>
              </div>
              <div class="p-3 rounded-xl ${priceInfo ? 'bg-amber-50/70 border border-amber-100' : 'bg-slate-50 border border-slate-100'}">
                <span class="text-[11px] font-semibold ${priceInfo ? 'text-amber-800' : 'text-slate-500'} uppercase tracking-wider block">${escapeHtml(t('produce.price', {}, undefined, 'Price'))}</span>
                ${priceDisplayHtml}
              </div>
            </div>

            <!-- Location & Details List -->
            <div class="mt-3 space-y-1.5 text-xs text-slate-600">
              <div class="flex items-center space-x-1.5">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400 shrink-0"></i>
                <span class="font-medium text-slate-800">${escapeHtml(p.area)}, ${escapeHtml(p.district)}, ${escapeHtml(p.state)}</span>
              </div>
              <div class="flex items-center space-x-1.5">
                <i data-lucide="calendar" class="w-3.5 h-3.5 text-slate-400 shrink-0"></i>
                <span>${escapeHtml(t('produce.availability', {}, undefined, 'Availability'))}: <strong class="text-slate-700">${escapeHtml(p.availability_date)}</strong></span>
              </div>
              <div class="flex items-center space-x-1.5">
                <i data-lucide="award" class="w-3.5 h-3.5 text-slate-400 shrink-0"></i>
                <span>${escapeHtml(t('produce.quality', {}, undefined, 'Quality'))}: <strong class="text-slate-700">${escapeHtml(translateQuality(p.quality || 'Grade A'))}</strong></span>
              </div>
            </div>
          </div>

          <!-- Footer: Source Badge & View Details CTA -->
          <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
            <div class="inline-flex items-center space-x-1 px-2 py-0.5 rounded-md ${sourceBadgeClass} text-[10px] font-bold">
              <i data-lucide="${sourceIcon}" class="w-3 h-3"></i>
              <span class="truncate max-w-[130px]">${escapeHtml(translateSource(p.source_type))}</span>
            </div>

            <button onclick="openProduceDetails(${p.id})" class="px-3.5 py-1.5 rounded-lg bg-brand-700 hover:bg-brand-800 text-white font-bold text-xs shadow-sm transition flex items-center space-x-1">
              <span>${escapeHtml(t('common.viewDetails', {}, undefined, 'View Details'))}</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>
      `;
    });

    grid.innerHTML = html;
    lucide.createIcons();
  }

  async function openProduceDetails(produceId) {
    try {
      const res = await fetch(`/api/public/produce/${produceId}`);
      if (!res.ok) {
        showToast(t('produce.notFound', {}, undefined, "Produce record not found"), "error");
        return;
      }
      const data = await res.json();
      STATE.currentDetailsProduceId = produceId;

      document.getElementById('pd-crop-name').innerText = translateCrop(data.crop_name);
      document.getElementById('pd-emoji').innerText = getCropEmoji(data.crop_name);
      document.getElementById('pd-location').innerText = `${data.area}, ${data.district}, ${data.state}`;
      document.getElementById('pd-qty').innerText = `${data.quantity} ${translateUnit(data.unit)}`;

      const priceInfo = formatProducePrice(data.price, data.unit);
      const priceEl = document.getElementById('pd-price');
      if (priceEl) {
        priceEl.innerText = priceInfo ? priceInfo.full : t('produce.priceOnInquiry', {}, undefined, 'On Inquiry');
      }
      document.getElementById('pd-quality').innerText = translateQuality(data.quality || 'Grade A');
      document.getElementById('pd-avail-date').innerText = data.availability_date;

      const isOfficer = data.source_type === 'officer_local' || data.source_type === 'OFFICER_ENTRY';
      const sourceLabel = isOfficer
        ? t('produce.sourceOfficer', {}, undefined, 'Officer Verified')
        : t('produce.sourceFarmer', {}, undefined, 'Farmer Verified');
      const actorName = isOfficer ? (data.officer_name || '') : (data.farmer_name || '');
      document.getElementById('pd-source').innerText = actorName ? `${sourceLabel} (${actorName})` : sourceLabel;

      const recordTypeEl = document.getElementById('pd-record-type');
      if (recordTypeEl) {
        recordTypeEl.innerText = isOfficer
          ? t('produce.localOfficerRecord', {}, undefined, 'Local Officer Availability')
          : t('produce.farmerVerifiedRecord', {}, undefined, 'Verified Farmer Produce');
      }

      // Handle Purchase Request form vs officer notice (Requirements 3, 4, 8)
      const officerNoticeEl = document.getElementById('pd-officer-notice');
      const purchaseSectionEl = document.getElementById('pd-purchase-section');
      if (isOfficer) {
        if (officerNoticeEl) officerNoticeEl.classList.remove('hidden');
        if (purchaseSectionEl) purchaseSectionEl.classList.add('hidden');
      } else {
        if (officerNoticeEl) officerNoticeEl.classList.add('hidden');
        if (purchaseSectionEl) purchaseSectionEl.classList.remove('hidden');
      }

      const badgeEl = document.getElementById('pd-status-badge');
      if (badgeEl) {
        badgeEl.innerText = t('produce.verifiedBadge', {}, undefined, '✓ VERIFIED');
      }

      document.getElementById('pd-notes').innerText = data.notes || (isOfficer ? "Official local agricultural entry inspected and verified." : "Verified farmer crop harvest submission.");

      // Set form fields for purchase request
      document.getElementById('pr-produce-id').value = data.id;
      document.getElementById('pr-unit').value = translateUnit(data.unit);
      document.getElementById('pr-qty').value = Math.min(data.quantity, 5);

      openModal('produce-details-modal');
    } catch (e) {
      console.error("Failed to load details:", e);
    }
  }

  async function handlePurchaseSubmit(e) {
    e.preventDefault();
    const produceId = document.getElementById('pr-produce-id').value;
    const name = document.getElementById('pr-name').value;
    const contact = document.getElementById('pr-contact').value;
    const qty = parseFloat(document.getElementById('pr-qty').value);
    const unit = document.getElementById('pr-unit').value;
    const message = document.getElementById('pr-message').value;

    try {
      const res = await fetch('/api/public/purchase-requests', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          produce_id: parseInt(produceId),
          buyer_name: name,
          buyer_contact: contact,
          requested_quantity: qty,
          quantity_unit: unit,
          message: message
        })
      });

      if (res.ok) {
        const successMsg = `${t('purchaseRequests.sentSuccess', {}, undefined, "Purchase request sent successfully.")} ${t('purchaseRequests.sentToFarmerDesc', {}, undefined, "Your request has been sent to the farmer associated with this verified produce.")}`;
        showToast(successMsg, "success");
        closeModal('produce-details-modal');
        document.getElementById('purchase-request-form').reset();
      } else {
        const err = await res.json();
        showToast(err.detail || "Failed to submit request", "error");
      }
    } catch (err) {
      showToast("Error connecting to server", "error");
    }
  }

  // -------------------------------------------------------------
  // OFFICER DASHBOARD & WORKFLOWS (Section 4, 5, 6, 10)
  // -------------------------------------------------------------
  async function loadOfficerDashboard() {
    if (!STATE.token) return;

    try {
      const [dashRes, reqRes, prodRes] = await Promise.all([
        fetch('/api/officer/dashboard', { headers: { 'Authorization': `Bearer ${STATE.token}` } }),
        fetch('/api/officer/requests', { headers: { 'Authorization': `Bearer ${STATE.token}` } }),
        fetch('/api/officer/produce', { headers: { 'Authorization': `Bearer ${STATE.token}` } })
      ]);

      if (dashRes.ok) {
        const dash = await dashRes.json();
        document.getElementById('officer-dash-name').innerText = STATE.user?.name || 'Agriculture Officer';
        const assignedJurisdictionLabel = t('officer.assignedJurisdiction', {}, undefined, 'Assigned Jurisdiction');
        document.getElementById('officer-dash-details').innerText = `${STATE.profile?.designation || 'Agriculture Officer'} | ${assignedJurisdictionLabel}: ${dash.jurisdiction.area}, ${dash.jurisdiction.district}, ${dash.jurisdiction.state}`;

        document.getElementById('stat-officer-records').innerText = dash.stats.total_records;
        document.getElementById('stat-officer-quantity').innerText = dash.stats.total_quantity;
        document.getElementById('stat-officer-pending').innerText = dash.stats.pending_requests;
        document.getElementById('stat-officer-verified').innerText = dash.stats.verified_records;

        // Update navbar badge
        const badge = document.getElementById('nav-pending-badge');
        if (dash.stats.pending_requests > 0) {
          badge.innerText = dash.stats.pending_requests;
          badge.classList.remove('hidden');
        } else {
          badge.classList.add('hidden');
        }
      }

      if (reqRes.ok) {
        STATE.officerRequests = await reqRes.json();
        renderOfficerRequests(STATE.officerRequests);
      }

      if (prodRes.ok) {
        const produces = await prodRes.json();
        renderOfficerProduceTable(produces);
      }

    } catch (err) {
      console.error("Failed to load officer dashboard:", err);
    }
  }

  function renderOfficerRequests(requests) {
    const container = document.getElementById('officer-requests-list');
    const empty = document.getElementById('officer-requests-empty');

    const pendingRequests = requests.filter(r => r.status === 'PENDING');

    if (pendingRequests.length === 0) {
      container.innerHTML = '';
      empty.classList.remove('hidden');
      return;
    }

    empty.classList.add('hidden');

    let html = '';
    pendingRequests.forEach(req => {
      const emoji = getCropEmoji(req.crop_name);
      const pendingText = t('officer.pendingBadge', {}, undefined, '🟡 Pending Verification');
      const cropLabel = t('produce.crop', {}, undefined, 'Crop');
      const cultivatedLabel = t('farmer.cultivatedArea', {}, undefined, 'Cultivated');
      const expectedYieldLabel = t('farmer.expectedYield', {}, undefined, 'Expected Yield');
      const locationLabel = t('common.location', {}, undefined, 'Location');
      const harvestLabel = t('farmer.expectedHarvest', {}, undefined, 'Harvest');
      const stageLabel = t('farmer.cropStage', {}, undefined, 'Stage');
      const farmerNoteLabel = t('farmer.officerFeedback', {}, undefined, 'Farmer Note:');
      const verifyText = t('officer.verify', {}, undefined, 'VERIFY');
      const rejectText = t('officer.reject', {}, undefined, 'REJECT');

      html += `
        <div class="p-4 rounded-xl bg-amber-50/50 border border-amber-200/80 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="flex items-start space-x-3.5">
            <span class="text-3xl p-2 bg-white rounded-xl border border-amber-200">${emoji}</span>
            <div class="space-y-1">
              <div class="flex items-center space-x-2">
                <span class="text-base font-bold text-slate-900">${escapeHtml(req.farmer_name)}</span>
                <span class="text-xs text-slate-500 font-medium">(${escapeHtml(req.farmer_phone)})</span>
                <span class="badge-pending text-[10px] font-bold px-2 py-0.5 rounded-full">${escapeHtml(pendingText)}</span>
              </div>
              <div class="text-xs text-slate-700 font-semibold">
                ${escapeHtml(cropLabel)}: <span class="text-brand-800 text-sm font-bold">${escapeHtml(translateCrop(req.crop_name))}</span> |
                ${escapeHtml(cultivatedLabel)}: <strong>${req.cultivated_area} ${escapeHtml(translateUnit(req.cultivated_area_unit || 'Acres'))}</strong> |
                ${escapeHtml(expectedYieldLabel)}: <strong class="text-emerald-800 font-bold">${req.expected_quantity} ${escapeHtml(translateUnit(req.quantity_unit))}</strong>
              </div>
              <div class="text-[11px] text-slate-500 flex flex-wrap gap-x-3">
                <span>📍 ${escapeHtml(locationLabel)}: <strong>${escapeHtml(req.area)}, ${escapeHtml(req.district)}, ${escapeHtml(req.state)}</strong></span>
                <span>📅 ${escapeHtml(harvestLabel)}: <strong>${req.expected_harvest_date}</strong></span>
                <span>🌱 ${escapeHtml(stageLabel)}: <strong>${escapeHtml(translateCropStage(req.crop_stage || 'Pre-Harvest'))}</strong></span>
              </div>
              ${req.notes ? `<p class="text-[11px] text-slate-600 italic bg-white/70 p-1.5 rounded border border-amber-100">${escapeHtml(farmerNoteLabel)} "${escapeHtml(req.notes)}"</p>` : ''}
            </div>
          </div>

          <div class="flex items-center space-x-2 shrink-0 self-end md:self-center">
            <button onclick="confirmOfficerVerify(${req.id})" class="px-4 py-2 rounded-lg bg-emerald-700 hover:bg-emerald-800 text-white font-bold text-xs shadow-sm transition flex items-center space-x-1">
              <i data-lucide="check" class="w-4 h-4"></i>
              <span>${escapeHtml(verifyText)}</span>
            </button>
            <button onclick="openRejectModal(${req.id})" class="px-3.5 py-2 rounded-lg bg-red-100 hover:bg-red-200 text-red-700 font-bold text-xs transition flex items-center space-x-1">
              <i data-lucide="x" class="w-4 h-4"></i>
              <span>${escapeHtml(rejectText)}</span>
            </button>
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
    lucide.createIcons();
  }

  function renderOfficerProduceTable(items) {
    const tbody = document.getElementById('officer-produce-table-body');
    if (items.length === 0) {
      const noProduceMsg = t('officer.noProduceYet', {}, undefined, "No produce records recorded yet in your area.");
      tbody.innerHTML = `<tr><td colspan="9" class="text-center py-8 text-slate-400">${escapeHtml(noProduceMsg)}</td></tr>`;
      return;
    }

    let html = '';
    items.forEach(p => {
      const isAvail = p.verification_status === 'VERIFIED';
      const statusPill = isAvail
        ? `<span class="badge-verified text-[11px] font-bold px-2 py-0.5 rounded-full">${escapeHtml(t('produce.verifiedBadge', {}, undefined, '✓ Verified'))}</span>`
        : `<span class="badge-unavailable text-[11px] font-bold px-2 py-0.5 rounded-full">⚪ ${escapeHtml(t('common.unavailable', {}, undefined, 'Unavailable'))}</span>`;
      const priceInfo = formatProducePrice(p.price, p.unit);
      const priceCell = priceInfo ? `<span class="font-bold text-amber-800">${priceInfo.full}</span>` : `<span class="text-slate-400 text-xs italic">-</span>`;

      html += `
        <tr class="hover:bg-slate-50 transition text-slate-700">
          <td class="py-3 px-4 font-bold text-slate-900 flex items-center space-x-2">
            <span>${getCropEmoji(p.crop_name)}</span>
            <span>${escapeHtml(translateCrop(p.crop_name))}</span>
          </td>
          <td class="py-3 px-4 font-bold text-emerald-800">${p.quantity} ${escapeHtml(translateUnit(p.unit))}</td>
          <td class="py-3 px-4">${priceCell}</td>
          <td class="py-3 px-4">${escapeHtml(p.area)}, ${escapeHtml(p.district)}</td>
          <td class="py-3 px-4">${escapeHtml(p.availability_date)}</td>
          <td class="py-3 px-4 font-semibold text-slate-600">${escapeHtml(translateQuality(p.quality || 'Grade A'))}</td>
          <td class="py-3 px-4 text-xs font-semibold text-slate-500">${escapeHtml(translateSource(p.source_type))}</td>
          <td class="py-3 px-4">${statusPill}</td>
          <td class="py-3 px-4 text-right space-x-1 whitespace-nowrap">
            <button onclick="toggleProduceAvailability(${p.id})" title="${isAvail ? escapeHtml(t('officer.markUnavailable', {}, undefined, 'Mark Unavailable')) : escapeHtml(t('officer.markAvailable', {}, undefined, 'Mark Available'))}" class="p-1.5 rounded hover:bg-slate-100 text-slate-500 hover:text-slate-800">
              <i data-lucide="${isAvail ? 'eye-off' : 'eye'}" class="w-4 h-4"></i>
            </button>
            <button onclick="openOfficerEditProduce(${JSON.stringify(p).replace(/"/g, '&quot;')})" title="${escapeHtml(t('officer.editProduceAction', {}, undefined, 'Edit Produce'))}" class="p-1.5 rounded hover:bg-slate-100 text-slate-500 hover:text-blue-600">
              <i data-lucide="edit-2" class="w-4 h-4"></i>
            </button>
            <button onclick="deleteOfficerProduce(${p.id})" title="${escapeHtml(t('common.delete', {}, undefined, 'Delete'))}" class="p-1.5 rounded hover:bg-red-50 text-slate-400 hover:text-red-600">
              <i data-lucide="trash-2" class="w-4 h-4"></i>
            </button>
          </td>
        </tr>
      `;
    });

    tbody.innerHTML = html;
    lucide.createIcons();
  }

  async function handleOfficerProduceSubmit(e) {
    e.preventDefault();
    const editId = document.getElementById('officer-produce-edit-id').value;
    const crop = document.getElementById('op-crop').value;
    const type = document.getElementById('op-type').value;
    const qty = parseFloat(document.getElementById('op-qty').value);
    const unit = document.getElementById('op-unit').value;
    const area = document.getElementById('op-area').value;
    const district = document.getElementById('op-district').value;
    const state = document.getElementById('op-state').value;
    const quality = document.getElementById('op-quality').value;
    const availDate = document.getElementById('op-avail-date').value;
    const notes = document.getElementById('op-notes').value;

    const priceInput = document.getElementById('op-price') ? document.getElementById('op-price').value.trim() : '';
    let priceVal = null;
    if (priceInput !== '') {
      priceVal = parseFloat(priceInput);
      if (isNaN(priceVal) || priceVal < 0) {
        showToast(window.AgriFlowI18n ? window.AgriFlowI18n.t('produce.invalidPrice') : "Please enter a valid positive price", "error");
        return;
      }
    }

    const url = editId ? `/api/officer/produce/${editId}` : '/api/officer/produce';
    const method = editId ? 'PUT' : 'POST';

    try {
      const res = await fetch(url, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${STATE.token}`
        },
        body: JSON.stringify({
          crop_name: crop,
          produce_type: type,
          quantity: qty,
          unit: unit,
          price: priceVal,
          area: area,
          district: district,
          state: state,
          quality: quality,
          availability_date: availDate,
          notes: notes
        })
      });

      if (res.ok) {
        showToast(editId ? t('officer.updateProduceSuccess', {}, undefined, "Produce updated successfully") : t('officer.officerRecordedSuccess', {}, undefined, "✓ Produce recorded and verified directly by Officer!"), "success");
        closeModal('add-produce-modal');
        document.getElementById('officer-produce-form').reset();
        document.getElementById('officer-produce-edit-id').value = '';
        if (document.getElementById('op-price')) document.getElementById('op-price').value = '';
        updatePriceUnitLabel();
        loadOfficerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || t('common.error', {}, undefined, "Failed to save produce"), "error");
      }
    } catch (err) {
      showToast(t('produce.submitError', {}, undefined, "Error saving produce"), "error");
    }
  }

  function openOfficerEditProduce(p) {
    document.getElementById('produce-modal-title').innerText = t('officer.editProduce', {}, undefined, 'Edit Local Produce');
    document.getElementById('officer-produce-edit-id').value = p.id;
    document.getElementById('op-crop').value = p.crop_name;
    document.getElementById('op-type').value = p.produce_type || 'Field Crop';
    document.getElementById('op-qty').value = p.quantity;
    document.getElementById('op-unit').value = p.unit;
    if (document.getElementById('op-price')) {
      document.getElementById('op-price').value = (p.price !== undefined && p.price !== null) ? p.price : '';
    }
    document.getElementById('op-area').value = p.area;
    document.getElementById('op-district').value = p.district;
    document.getElementById('op-state').value = p.state;
    document.getElementById('op-quality').value = p.quality || 'Grade A';
    document.getElementById('op-avail-date').value = p.availability_date;
    document.getElementById('op-notes').value = p.notes || '';
    updatePriceUnitLabel();

    openModal('add-produce-modal');
  }

  async function toggleProduceAvailability(id) {
    try {
      const res = await fetch(`/api/officer/produce/${id}/toggle-status`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${STATE.token}` }
      });
      if (res.ok) {
        showToast(t('notifications.statusUpdated', {}, undefined, "Produce status updated"), "info");
        loadOfficerDashboard();
      }
    } catch (err) {
      showToast(t('common.error', {}, undefined, "Failed to toggle status"), "error");
    }
  }

  async function deleteOfficerProduce(id) {
    if (!confirm(t('officer.deleteConfirm', {}, undefined, "Are you sure you want to delete this produce record?"))) return;

    try {
      const res = await fetch(`/api/officer/produce/${id}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${STATE.token}` }
      });
      if (res.ok) {
        showToast(t('notifications.deleted', {}, undefined, "Produce record deleted"), "info");
        loadOfficerDashboard();
      }
    } catch (err) {
      showToast(t('common.error', {}, undefined, "Failed to delete produce"), "error");
    }
  }

  async function confirmOfficerVerify(requestId) {
    try {
      const res = await fetch(`/api/officer/requests/${requestId}/verify`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${STATE.token}`
        },
        body: JSON.stringify({
          action: 'VERIFY',
          comment: 'Field inspected and verified by Agriculture Officer Ravi Kumar.'
        })
      });

      if (res.ok) {
        showToast(t('officer.verificationSuccess', {}, undefined, "✓ Farmer submission verified and published to public View Produce!"), "success");
        loadOfficerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || t('common.error', {}, undefined, "Verification failed"), "error");
      }
    } catch (e) {
      showToast(t('common.error', {}, undefined, "Network error verifying request"), "error");
    }
  }

  function openRejectModal(requestId) {
    document.getElementById('reject-request-id').value = requestId;
    document.getElementById('reject-comment').value = '';
    openModal('reject-modal');
  }

  async function submitOfficerReject() {
    const requestId = document.getElementById('reject-request-id').value;
    const comment = document.getElementById('reject-comment').value;

    if (!comment.trim()) {
      showToast(t('officer.provideReason', {}, undefined, "Please provide a reason for rejection"), "warning");
      return;
    }

    try {
      const res = await fetch(`/api/officer/requests/${requestId}/reject`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${STATE.token}`
        },
        body: JSON.stringify({
          action: 'REJECT',
          comment: comment.trim()
        })
      });

      if (res.ok) {
        showToast(t('officer.rejectionSuccess', {}, undefined, "Request rejected and feedback sent to farmer."), "info");
        closeModal('reject-modal');
        loadOfficerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || t('common.error', {}, undefined, "Rejection failed"), "error");
      }
    } catch (e) {
      showToast(t('common.error', {}, undefined, "Network error rejecting request"), "error");
    }
  }

  // -------------------------------------------------------------
  // FARMER DASHBOARD & WORKFLOWS (Section 7, 8, 9)
  // -------------------------------------------------------------
  async function loadFarmerDashboard() {
    if (!STATE.token) return;

    try {
      const [dashRes, reqRes] = await Promise.all([
        fetch('/api/farmer/dashboard', { headers: { 'Authorization': `Bearer ${STATE.token}` } }),
        fetch('/api/farmer/requests', { headers: { 'Authorization': `Bearer ${STATE.token}` } })
      ]);

      if (dashRes.ok) {
        const dash = await dashRes.json();
        document.getElementById('farmer-dash-name').innerText = STATE.user?.name || 'Farmer';
        document.getElementById('farmer-dash-details').innerText = `${STATE.profile?.land_area || 2} ${translateUnit(STATE.profile?.land_unit || 'Acres')} | ${dash.location.village || 'Sankari West'}, ${dash.location.area}, ${dash.location.district}`;

        document.getElementById('stat-farmer-total').innerText = dash.stats.total_crops;
        document.getElementById('stat-farmer-pending').innerText = dash.stats.pending_count;
        document.getElementById('stat-farmer-verified').innerText = dash.stats.verified_count;
        document.getElementById('stat-farmer-rejected').innerText = dash.stats.rejected_count;

        // Update badge
        const badge = document.getElementById('nav-farmer-pending-badge');
        if (dash.stats.pending_count > 0) {
          badge.innerText = dash.stats.pending_count;
          badge.classList.remove('hidden');
        } else {
          badge.classList.add('hidden');
        }

        // Update pending purchase inquiries badge
        if (dash.stats.pending_purchase_requests !== undefined) {
          const prBadge = document.getElementById('farmer-pr-pending-badge');
          if (prBadge) {
            if (dash.stats.pending_purchase_requests > 0) {
              prBadge.innerText = dash.stats.pending_purchase_requests;
              prBadge.classList.remove('hidden');
            } else {
              prBadge.classList.add('hidden');
            }
          }
        }

        // Render assigned officer card
        const offCard = document.getElementById('farmer-officer-card');
        if (dash.assigned_officer) {
          offCard.classList.remove('hidden');
          document.getElementById('assigned-officer-name').innerText = `${dash.assigned_officer.name} (${dash.assigned_officer.designation})`;
          const jurisdictionLabel = t('officer.assignedJurisdiction', {}, undefined, 'Jurisdiction');
          const contactLabel = t('produce.contact', {}, undefined, 'Contact');
          const stateStr = dash.assigned_officer.state ? `, ${dash.assigned_officer.state}` : '';
          document.getElementById('assigned-officer-contact').innerText = `${jurisdictionLabel}: ${dash.assigned_officer.assigned_area}, ${dash.assigned_officer.district}${stateStr} | ${contactLabel}: ${dash.assigned_officer.phone || dash.assigned_officer.email}`;
        } else {
          offCard.classList.add('hidden');
        }
      }

      if (reqRes.ok) {
        STATE.farmerRequests = await reqRes.json();
        renderFarmerRequests(STATE.farmerRequests);
      }

      // Also load farmer purchase requests
      await loadFarmerPurchaseRequests();
    } catch (err) {
      console.error("Failed to load farmer dashboard:", err);
    }
  }

  function renderFarmerRequests(requests) {
    const container = document.getElementById('farmer-requests-list');
    const empty = document.getElementById('farmer-requests-empty');

    if (requests.length === 0) {
      container.innerHTML = '';
      empty.classList.remove('hidden');
      return;
    }

    empty.classList.add('hidden');

    let html = '';
    requests.forEach(r => {
      let statusPill = '';
      if (r.status === 'PENDING') {
        statusPill = `<span class="badge-pending text-xs font-bold px-2.5 py-1 rounded-full">${escapeHtml(t('farmer.pendingStatus', {}, undefined, '🟡 Pending Verification'))}</span>`;
      } else if (r.status === 'VERIFIED') {
        statusPill = `<span class="badge-verified text-xs font-bold px-2.5 py-1 rounded-full">${escapeHtml(t('farmer.verifiedStatus', {}, undefined, '🟢 ✓ Verified'))}</span>`;
      } else {
        statusPill = `<span class="badge-rejected text-xs font-bold px-2.5 py-1 rounded-full">${escapeHtml(t('farmer.rejectedStatus', {}, undefined, '🔴 Rejected'))}</span>`;
      }

      html += `
        <div class="p-4 rounded-xl bg-white border border-slate-200 shadow-sm hover:border-brand-300 transition space-y-3">
          <div class="flex items-start justify-between">
            <div class="flex items-center space-x-3">
              <span class="text-3xl p-2 bg-slate-50 rounded-xl border border-slate-100">${getCropEmoji(r.crop_name)}</span>
              <div>
                <h4 class="text-base font-bold text-slate-900">${escapeHtml(translateCrop(r.crop_name))}</h4>
                <span class="text-xs text-slate-500 font-medium">${escapeHtml(t('farmer.expectedHarvest', {}, undefined, 'Expected Harvest'))}: <strong>${escapeHtml(r.expected_harvest_date)}</strong></span>
              </div>
            </div>
            ${statusPill}
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs bg-slate-50 p-2.5 rounded-lg border border-slate-100">
            <div>
              <span class="text-slate-400 block text-[10px]">${escapeHtml(t('farmer.cultivatedArea', {}, undefined, 'Cultivated Area'))}</span>
              <span class="font-bold text-slate-800">${r.cultivated_area} ${escapeHtml(translateUnit(r.cultivated_area_unit || 'Acres'))}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">${escapeHtml(t('farmer.expectedYield', {}, undefined, 'Expected Yield'))}</span>
              <span class="font-bold text-emerald-800">${r.expected_quantity} ${escapeHtml(translateUnit(r.quantity_unit))}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">${escapeHtml(t('common.location', {}, undefined, 'Location'))}</span>
              <span class="font-bold text-slate-800">${escapeHtml(r.area)}, ${escapeHtml(r.district)}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">${escapeHtml(t('farmer.cropStage', {}, undefined, 'Crop Stage'))}</span>
              <span class="font-bold text-slate-800">${escapeHtml(translateCropStage(r.crop_stage || 'Vegetative'))}</span>
            </div>
          </div>

          ${r.officer_comment ? `
            <div class="text-xs p-2.5 rounded-lg ${r.status === 'VERIFIED' ? 'bg-emerald-50 text-emerald-900 border border-emerald-100' : 'bg-red-50 text-red-900 border border-red-100'}">
              <span class="font-bold block text-[11px] mb-0.5">${escapeHtml(t('farmer.officerFeedback', {}, undefined, 'Officer Feedback:'))}</span>
              <span>${escapeHtml(r.officer_comment)}</span>
            </div>
          ` : ''}
        </div>
      `;
    });

    container.innerHTML = html;
    lucide.createIcons();
  }

  async function loadFarmerPurchaseRequests() {
    if (!STATE.token || (STATE.user?.role || '').toLowerCase() !== 'farmer') return;
    try {
      const res = await fetch('/api/farmer/purchase-requests', {
        headers: { 'Authorization': `Bearer ${STATE.token}` }
      });
      if (res.ok) {
        const data = await res.json();
        STATE.farmerPurchaseRequests = data;
        renderFarmerPurchaseRequests(data);
        const pendingCount = data.filter(r => (r.status || '').toLowerCase() === 'pending').length;
        const badge = document.getElementById('farmer-pr-pending-badge');
        if (badge) {
          if (pendingCount > 0) {
            badge.innerText = `${pendingCount} ${t('purchaseRequests.pending', {}, undefined, 'Pending')}`;
            badge.classList.remove('hidden');
          } else {
            badge.classList.add('hidden');
          }
        }
      }
    } catch (err) {
      console.error("Failed to load farmer purchase requests:", err);
    }
  }

  function renderFarmerPurchaseRequests(requests) {
    const container = document.getElementById('farmer-purchase-requests-list');
    const empty = document.getElementById('farmer-purchase-requests-empty');
    if (!container) return;

    if (!requests || requests.length === 0) {
      container.innerHTML = '';
      if (empty) empty.classList.remove('hidden');
      return;
    }

    if (empty) empty.classList.add('hidden');

    let html = '';
    requests.forEach(r => {
      const statusLower = (r.status || 'pending').toLowerCase();
      let statusBadge = '';
      let actionButtons = '';

      if (statusLower === 'pending') {
        statusBadge = `<span class="badge-pending text-xs font-bold px-2.5 py-1 rounded-full bg-amber-100 text-amber-800 border border-amber-200">🟡 ${escapeHtml(t('purchaseRequests.pending', {}, undefined, 'Pending'))}</span>`;
        actionButtons = `
          <div class="flex items-center space-x-2 pt-2 border-t border-slate-100">
            <button onclick="handleAcceptPurchaseRequest(${r.id})" class="px-3 py-1.5 rounded-lg bg-emerald-600 text-white text-xs font-bold hover:bg-emerald-700 transition flex items-center space-x-1 shadow-sm">
              <i data-lucide="check" class="w-3.5 h-3.5"></i>
              <span>${escapeHtml(t('purchaseRequests.accept', {}, undefined, 'Accept'))}</span>
            </button>
            <button onclick="handleRejectPurchaseRequest(${r.id})" class="px-3 py-1.5 rounded-lg border border-red-200 text-red-700 bg-red-50 text-xs font-bold hover:bg-red-100 transition flex items-center space-x-1">
              <i data-lucide="x" class="w-3.5 h-3.5"></i>
              <span>${escapeHtml(t('purchaseRequests.reject', {}, undefined, 'Reject'))}</span>
            </button>
          </div>
        `;
      } else if (statusLower === 'accepted') {
        statusBadge = `<span class="badge-verified text-xs font-bold px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200">🟢 ✓ ${escapeHtml(t('purchaseRequests.accepted', {}, undefined, 'Accepted'))}</span>`;
      } else {
        statusBadge = `<span class="badge-rejected text-xs font-bold px-2.5 py-1 rounded-full bg-red-100 text-red-800 border border-red-200">🔴 ${escapeHtml(t('purchaseRequests.rejected', {}, undefined, 'Rejected'))}</span>`;
      }

      const dateStr = r.created_at ? new Date(r.created_at).toLocaleDateString() : '';

      html += `
        <div class="p-4 rounded-xl bg-white border border-slate-200 shadow-sm hover:border-brand-300 transition space-y-3">
          <div class="flex items-start justify-between">
            <div class="flex items-center space-x-3">
              <span class="text-3xl p-2 bg-slate-50 rounded-xl border border-slate-100">${getCropEmoji(r.crop_name)}</span>
              <div>
                <div class="flex items-center space-x-2">
                  <h4 class="text-base font-bold text-slate-900">${escapeHtml(translateCrop(r.crop_name))}</h4>
                  ${r.quality_grade ? `<span class="text-[10px] font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-700">${escapeHtml(r.quality_grade)}</span>` : ''}
                </div>
                <p class="text-xs text-slate-500 font-medium">${escapeHtml(t('purchaseRequests.buyer', {}, undefined, 'Buyer'))}: <strong class="text-slate-800">${escapeHtml(r.buyer_name)}</strong> &bull; <span class="text-slate-600">${escapeHtml(r.buyer_contact)}</span></p>
              </div>
            </div>
            ${statusBadge}
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs bg-slate-50 p-2.5 rounded-lg border border-slate-100">
            <div>
              <span class="text-slate-400 block text-[10px]">${escapeHtml(t('purchaseRequests.requestedQuantity', {}, undefined, 'Requested Quantity'))}</span>
              <span class="font-bold text-emerald-800">${r.requested_quantity} ${escapeHtml(translateUnit(r.requested_unit))}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">${escapeHtml(t('common.location', {}, undefined, 'Location'))}</span>
              <span class="font-bold text-slate-800">${escapeHtml(r.area || '')}${r.district ? ', ' + escapeHtml(r.district) : ''}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">${escapeHtml(t('purchaseRequests.date', {}, undefined, 'Date'))}</span>
              <span class="font-medium text-slate-700">${escapeHtml(dateStr)}</span>
            </div>
          </div>

          ${r.message ? `
            <div class="text-xs p-2.5 rounded-lg bg-slate-50 text-slate-800 border border-slate-100">
              <span class="font-bold block text-[11px] text-slate-500 mb-0.5">${escapeHtml(t('purchaseRequests.message', {}, undefined, 'Message / Requirements'))}:</span>
              <p class="italic text-slate-700">"${escapeHtml(r.message)}"</p>
            </div>
          ` : ''}

          ${actionButtons}
        </div>
      `;
    });

    container.innerHTML = html;
    if (window.lucide) lucide.createIcons();
  }

  async function handleAcceptPurchaseRequest(id) {
    try {
      const res = await fetch(`/api/farmer/purchase-requests/${id}/accept`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${STATE.token}`
        }
      });
      if (res.ok) {
        showToast(t('purchaseRequests.acceptedSuccess', {}, undefined, 'Purchase request accepted successfully.'), 'success');
        await loadFarmerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || 'Failed to accept purchase request', 'error');
      }
    } catch (e) {
      showToast('Error accepting purchase request', 'error');
    }
  }

  async function handleRejectPurchaseRequest(id) {
    try {
      const res = await fetch(`/api/farmer/purchase-requests/${id}/reject`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${STATE.token}`
        }
      });
      if (res.ok) {
        showToast(t('purchaseRequests.rejectedSuccess', {}, undefined, 'Purchase request rejected.'), 'info');
        await loadFarmerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || 'Failed to reject purchase request', 'error');
      }
    } catch (e) {
      showToast('Error rejecting purchase request', 'error');
    }
  }

  window.loadFarmerPurchaseRequests = loadFarmerPurchaseRequests;
  window.handleAcceptPurchaseRequest = handleAcceptPurchaseRequest;
  window.handleRejectPurchaseRequest = handleRejectPurchaseRequest;

  async function handleFarmerCropSubmit(e) {
    e.preventDefault();
    const crop = document.getElementById('fc-crop').value;
    const areaSize = parseFloat(document.getElementById('fc-area-size').value);
    const areaUnit = document.getElementById('fc-area-unit').value;
    const expQty = parseFloat(document.getElementById('fc-expected-qty').value);
    const qtyUnit = document.getElementById('fc-qty-unit').value;
    const harvestDate = document.getElementById('fc-harvest-date').value;
    const stage = document.getElementById('fc-stage').value;
    const area = document.getElementById('fc-area').value;
    const district = document.getElementById('fc-district').value;
    const state = document.getElementById('fc-state').value;
    const notes = document.getElementById('fc-notes').value;

    try {
      const res = await fetch('/api/farmer/crops', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${STATE.token}`
        },
        body: JSON.stringify({
          crop_name: crop,
          cultivated_area: areaSize,
          cultivated_area_unit: areaUnit,
          expected_quantity: expQty,
          quantity_unit: qtyUnit,
          expected_harvest_date: harvestDate,
          crop_stage: stage,
          area: area,
          district: district,
          state: state,
          notes: notes
        })
      });

      if (res.ok) {
        showToast(t('farmer.submissionSuccess', {}, undefined, "✓ Crop submitted! Sent to local Agriculture Officer for verification."), "success");
        closeModal('add-crop-modal');
        document.getElementById('farmer-crop-form').reset();
        loadFarmerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || t('common.error', {}, undefined, "Submission failed"), "error");
      }
    } catch (err) {
      showToast(t('common.error', {}, undefined, "Network error submitting crop"), "error");
    }
  }

  // -------------------------------------------------------------
  // PROFILE EDITING & SAVING (Section 4, 7)
  // -------------------------------------------------------------
  function renderProfileForm() {
    const container = document.getElementById('profile-fields-container');
    if (!STATE.user) return;

    const isOfficer = STATE.user.role === 'OFFICER';
    const prof = STATE.profile || {};

    const fullNameLabel = t('profile.fullName', {}, undefined, 'Full Name');
    const designationLabel = t('profile.designation', {}, undefined, 'Officer Designation');
    const departmentLabel = t('profile.department', {}, undefined, 'Department');
    const contactLabel = t('profile.contactNumber', {}, undefined, 'Contact Number');
    const assignedAreaLabel = t('profile.assignedArea', {}, undefined, 'Assigned Area / Block');
    const districtLabel = t('profile.district', {}, undefined, 'District');
    const stateLabel = t('profile.state', {}, undefined, 'State');
    const officialEmailLabel = t('profile.officialEmail', {}, undefined, 'Official Email');
    const villageLabel = t('profile.village', {}, undefined, 'Village');
    const areaLabel = t('profile.area', {}, undefined, 'Area / Block');
    const landAreaLabel = t('profile.landArea', {}, undefined, 'Land Area');
    const landUnitLabel = t('profile.landUnit', {}, undefined, 'Land Unit');
    const farmingTypeLabel = t('profile.farmingType', {}, undefined, 'Farming Type');

    if (isOfficer) {
      const officerId = prof.officer_id || STATE.user.officer_id || 'AGRI-OFFICER';
      const isVerified = prof.is_verified_officer !== false;

      container.innerHTML = `
        <!-- Verified Official Information Card (Read-Only) -->
        <div class="rounded-xl border border-emerald-200 bg-emerald-50/40 p-4 space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <i data-lucide="shield-check" class="w-5 h-5 text-emerald-600"></i>
              <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-900" data-i18n="profile.verifiedOfficerInformation">Verified Officer Information</h4>
            </div>
            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800 flex items-center gap-1">
              <i data-lucide="lock" class="w-3 h-3"></i>
              <span data-i18n="profile.registryVerified">Registry Verified</span>
            </span>
          </div>
          <p class="text-[11px] text-emerald-800/80">
            ${escapeHtml(t('profile.verifiedNotice', {}, undefined, 'Official identity details are retrieved from the AgriFlow Demo Registry and locked from modification.'))}
          </p>

          <div class="grid grid-cols-2 gap-3 text-xs pt-1">
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="auth.officerId">Officer ID</span>
              <span class="font-mono font-bold text-brand-900 text-xs">${escapeHtml(officerId)}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="profile.fullName">Full Name</span>
              <span class="font-bold text-slate-900 text-xs">${escapeHtml(prof.name || STATE.user.name)}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="profile.designation">Designation</span>
              <span class="font-semibold text-slate-800 text-xs">${escapeHtml(prof.designation || 'Agriculture Officer')}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="profile.department">Department</span>
              <span class="font-semibold text-slate-800 text-xs">${escapeHtml(prof.department || 'Department of Agriculture')}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="common.state">State</span>
              <span class="font-semibold text-slate-800 text-xs">${escapeHtml(prof.state || 'Tamil Nadu')}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="common.district">District</span>
              <span class="font-semibold text-slate-800 text-xs">${escapeHtml(prof.district || 'Salem')}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="profile.assignedArea">Working Place / Area</span>
              <span class="font-semibold text-slate-800 text-xs">${escapeHtml(prof.assigned_area || 'Sankari')}</span>
            </div>
            <div class="bg-white/80 p-2.5 rounded-lg border border-emerald-100">
              <span class="text-slate-500 block text-[10px] uppercase font-bold" data-i18n="profile.contactNumber">Registered Mobile</span>
              <span class="font-mono font-semibold text-slate-800 text-xs">${escapeHtml(prof.contact || STATE.user.phone || '9876543210')}</span>
            </div>
          </div>
        </div>

        <!-- Editable Preferences Section -->
        <div class="space-y-3 pt-2">
          <h4 class="text-xs font-bold uppercase tracking-wider text-slate-700" data-i18n="profile.applicationPreferences">Application Preferences</h4>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1" data-i18n="profile.officialEmail">${escapeHtml(officialEmailLabel)}</label>
            <input type="email" id="prof-email" value="${escapeHtml(STATE.user.email || prof.email || '')}" placeholder="officer@example.com" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-brand-500">
            <p class="text-[11px] text-slate-400 mt-1" data-i18n="profile.emailNotice">Used for AgriFlow notification and produce verification alerts.</p>
          </div>
        </div>
      `;
      if (window.lucide) lucide.createIcons();
    } else {
      container.innerHTML = `
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(fullNameLabel)} *</label>
            <input type="text" id="prof-name" required value="${escapeHtml(STATE.user.name)}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(villageLabel)} *</label>
            <input type="text" id="prof-f-village" required value="${escapeHtml(prof.village || 'Sankari West')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(areaLabel)} *</label>
            <input type="text" id="prof-area" required value="${escapeHtml(prof.area || 'Sankari')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(districtLabel)} *</label>
            <input type="text" id="prof-district" required value="${escapeHtml(prof.district || 'Salem')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-3 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(stateLabel)} *</label>
            <input type="text" id="prof-state" required value="${escapeHtml(prof.state || 'Tamil Nadu')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(landAreaLabel)} *</label>
            <input type="number" id="prof-f-land" required step="0.5" value="${prof.land_area || 2}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(landUnitLabel)}</label>
            <input type="text" id="prof-f-unit" value="${escapeHtml(prof.land_unit || 'Acres')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(farmingTypeLabel)}</label>
          <input type="text" id="prof-f-type" value="${escapeHtml(prof.farming_type || 'Natural Farming')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
        </div>
      `;
    }
  }

  async function saveUserProfile(e) {
    e.preventDefault();
    const isOfficer = STATE.user.role === 'OFFICER';

    let body = {};
    let url = '';

    if (isOfficer) {
      url = '/api/officer/profile';
      const profEmailInput = document.getElementById('prof-email');
      body = {
        email: profEmailInput ? profEmailInput.value.trim() : STATE.user.email
      };
    } else {
      url = '/api/farmer/profile';
      const name = document.getElementById('prof-name').value;
      body = {
        name: name,
        village: document.getElementById('prof-f-village').value,
        area: document.getElementById('prof-area').value,
        district: document.getElementById('prof-district').value,
        state: document.getElementById('prof-state').value,
        land_area: parseFloat(document.getElementById('prof-f-land').value),
        land_unit: document.getElementById('prof-f-unit').value,
        farming_type: document.getElementById('prof-f-type').value
      };
    }

    try {
      const res = await fetch(url, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${STATE.token}`
        },
        body: JSON.stringify(body)
      });

      if (res.ok) {
        showToast(t('profile.profileUpdated', {}, undefined, "Profile updated successfully"), "success");
        await checkSession();
        navigate(isOfficer ? 'officer-dashboard' : 'farmer-dashboard');
      } else {
        const err = await res.json();
        showToast(err.detail || t('common.error', {}, undefined, "Failed to update profile"), "error");
      }
    } catch (err) {
      showToast(t('common.error', {}, undefined, "Network error updating profile"), "error");
    }
  }

  // -------------------------------------------------------------
  // AUTHENTICATION MODAL & LOGIC
  // -------------------------------------------------------------
  let currentAuthRole = 'OFFICER';

  // Officer Registration Wizard State
  let officerRegState = {
    step: 1,
    officerId: '',
    maskedMobile: '',
    demoOtp: '',
    verificationToken: '',
    officerDetails: null,
    otpTimerInterval: null,
    otpSecondsRemaining: 300
  };

  function openAuthModal(tab = 'login', preferredRole = null) {
    if (preferredRole) {
      setAuthRole(preferredRole);
    }
    if (tab === 'register' && (preferredRole === 'OFFICER' || currentAuthRole === 'OFFICER')) {
      if (typeof officerRegState !== 'undefined' && officerRegState && officerRegState.step === 5) {
        resetOfficerRegistrationState(true);
      }
    }
    navigate('auth');
    switchAuthTab(tab);
  }

  function switchAuthTab(tab) {
    const formLogin = document.getElementById('form-login');
    const formRegisterFarmer = document.getElementById('form-register-farmer');
    const officerWizard = document.getElementById('officer-reg-wizard');
    const tabLogin = document.getElementById('tab-login');
    const tabRegister = document.getElementById('tab-register');
    const idLabel = document.getElementById('login-identifier-label');
    const idInput = document.getElementById('login-identifier');
    const officerHint = document.getElementById('login-officer-hint');

    if (tab === 'login') {
      if (typeof officerRegState !== 'undefined' && officerRegState && officerRegState.step === 5) {
        resetOfficerRegistrationState(true);
      }
      if (formLogin) formLogin.classList.remove('hidden');
      if (formRegisterFarmer) formRegisterFarmer.classList.add('hidden');
      if (officerWizard) officerWizard.classList.add('hidden');

      tabLogin?.classList.add('border-brand-700', 'text-brand-700');
      tabLogin?.classList.remove('border-transparent', 'text-slate-500');
      tabRegister?.classList.remove('border-brand-700', 'text-brand-700');
      tabRegister?.classList.add('border-transparent', 'text-slate-500');

      if (currentAuthRole === 'OFFICER') {
        if (idLabel) idLabel.textContent = t('auth.officerLoginIdLabel', {}, undefined, 'Officer ID / Login ID');
        if (idInput) idInput.placeholder = 'e.g. AGRI-TN-0001 or ravi_salem';
        if (officerHint) officerHint.classList.remove('hidden');
      } else {
        if (idLabel) idLabel.textContent = t('auth.identifier', {}, undefined, 'Mobile Number or Email');
        if (idInput) idInput.placeholder = 'e.g. 9876543210 or email';
        if (officerHint) officerHint.classList.add('hidden');
      }
    } else {
      if (formLogin) formLogin.classList.add('hidden');

      tabRegister?.classList.add('border-brand-700', 'text-brand-700');
      tabRegister?.classList.remove('border-transparent', 'text-slate-500');
      tabLogin?.classList.remove('border-brand-700', 'text-brand-700');
      tabLogin?.classList.add('border-transparent', 'text-slate-500');

      if (currentAuthRole === 'OFFICER') {
        if (typeof officerRegState !== 'undefined' && officerRegState && officerRegState.step === 5) {
          resetOfficerRegistrationState(true);
        }
        if (formRegisterFarmer) formRegisterFarmer.classList.add('hidden');
        if (officerWizard) officerWizard.classList.remove('hidden');
      } else {
        if (officerWizard) officerWizard.classList.add('hidden');
        if (formRegisterFarmer) formRegisterFarmer.classList.remove('hidden');
      }
    }
    if (window.lucide) lucide.createIcons();
  }

  function setAuthRole(role) {
    currentAuthRole = role;
    const btnOff = document.getElementById('role-btn-officer');
    const btnFarm = document.getElementById('role-btn-farmer');
    const formLogin = document.getElementById('form-login');
    const formRegisterFarmer = document.getElementById('form-register-farmer');
    const officerWizard = document.getElementById('officer-reg-wizard');
    const idLabel = document.getElementById('login-identifier-label');
    const idInput = document.getElementById('login-identifier');
    const officerHint = document.getElementById('login-officer-hint');

    if (role === 'OFFICER') {
      if (typeof officerRegState !== 'undefined' && officerRegState && officerRegState.step === 5) {
        resetOfficerRegistrationState(true);
      }
      btnOff?.classList.add('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnOff?.classList.remove('border-slate-200', 'bg-white', 'text-slate-600');
      btnFarm?.classList.remove('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnFarm?.classList.add('border-slate-200', 'bg-white', 'text-slate-600');

      if (idLabel) idLabel.textContent = t('auth.officerLoginIdLabel', {}, undefined, 'Officer ID / Login ID');
      if (idInput) idInput.placeholder = 'e.g. AGRI-TN-0001 or ravi_salem';
      if (officerHint) officerHint.classList.remove('hidden');

      // If in register view, toggle to officer wizard
      if (formLogin && formLogin.classList.contains('hidden')) {
        formRegisterFarmer?.classList.add('hidden');
        officerWizard?.classList.remove('hidden');
      }
    } else {
      btnFarm?.classList.add('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnFarm?.classList.remove('border-slate-200', 'bg-white', 'text-slate-600');
      btnOff?.classList.remove('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnOff?.classList.add('border-slate-200', 'bg-white', 'text-slate-600');

      if (idLabel) idLabel.textContent = t('auth.identifier', {}, undefined, 'Mobile Number or Email');
      if (idInput) idInput.placeholder = 'e.g. 9876543210 or email';
      if (officerHint) officerHint.classList.add('hidden');

      // If in register view, toggle to farmer register
      if (formLogin && formLogin.classList.contains('hidden')) {
        officerWizard?.classList.add('hidden');
        formRegisterFarmer?.classList.remove('hidden');
      }
    }
    if (window.lucide) lucide.createIcons();
  }

  // -------------------------------------------------------------
  // AGRICULTURE OFFICER VERIFICATION & REGISTRATION FLOW
  // -------------------------------------------------------------
  function goToOfficerStep(step) {
    if (officerRegState) officerRegState.step = step;
    for (let s = 1; s <= 5; s++) {
      const stepEl = document.getElementById(`officer-step-${s}`);
      if (stepEl) {
        if (s === step) stepEl.classList.remove('hidden');
        else stepEl.classList.add('hidden');
      }
      const ind = document.getElementById(`step-ind-${s}`);
      if (ind) {
        const badge = ind.querySelector('span:first-child');
        if (s === step) {
          ind.className = 'text-brand-700 font-bold flex items-center gap-1';
          if (badge) badge.className = 'w-4 h-4 rounded-full bg-brand-700 text-white text-[10px] inline-flex items-center justify-center font-mono';
        } else if (s < step) {
          ind.className = 'text-emerald-700 font-semibold flex items-center gap-1';
          if (badge) badge.className = 'w-4 h-4 rounded-full bg-emerald-600 text-white text-[10px] inline-flex items-center justify-center font-mono';
        } else {
          ind.className = 'text-slate-400 flex items-center gap-1';
          if (badge) badge.className = 'w-4 h-4 rounded-full bg-slate-200 text-slate-600 text-[10px] inline-flex items-center justify-center font-mono';
        }
      }
    }
    if (window.lucide) lucide.createIcons();
  }

  function resetOfficerRegistrationState(clearInputs = true) {
    if (officerRegState && officerRegState.otpTimerInterval) {
      clearInterval(officerRegState.otpTimerInterval);
      officerRegState.otpTimerInterval = null;
    }

    officerRegState = {
      step: 1,
      officerId: '',
      maskedMobile: '',
      demoOtp: '',
      verificationToken: '',
      officerDetails: null,
      otpTimerInterval: null,
      otpSecondsRemaining: 300,
      createdLoginId: '',
      createdOfficerId: ''
    };

    try {
      sessionStorage.removeItem('agriflow_officer_reg_state');
      sessionStorage.removeItem('agriflow_officer_reg_temp');
      localStorage.removeItem('agriflow_officer_reg_state');
    } catch (e) {}

    goToOfficerStep(1);

    const errIds = ['officer-id-error', 'officer-otp-error', 'officer-cred-error'];
    errIds.forEach(id => {
      const el = document.getElementById(id);
      if (el) {
        el.classList.add('hidden');
        el.innerHTML = '';
      }
    });

    if (clearInputs) {
      const inputIds = [
        'officer-verify-id-input',
        'officer-otp-input',
        'officer-new-login-id',
        'officer-new-password',
        'officer-confirm-password'
      ];
      inputIds.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.value = '';
      });
    }

    const textResetMap = {
      'officer-masked-mobile': '******3210',
      'officer-demo-otp-val': '------',
      'officer-otp-timer': '05:00',
      'dtl-officer-id': '',
      'dtl-name': '',
      'dtl-post': '',
      'dtl-dept': '',
      'dtl-state': '',
      'dtl-district': '',
      'dtl-area': '',
      'dtl-mobile': '',
      'done-officer-id': '',
      'done-officer-name': '',
      'done-login-id': ''
    };
    Object.entries(textResetMap).forEach(([id, val]) => {
      const el = document.getElementById(id);
      if (el) el.textContent = val;
    });

    if (window.lucide) lucide.createIcons();
  }

  function resetOfficerWizardToStep1() {
    resetOfficerRegistrationState(false);
  }

  function fillOfficerId(id) {
    const input = document.getElementById('officer-verify-id-input');
    if (input) {
      input.value = id;
      input.focus();
    }
  }

  function startOtpCountdown(seconds = 300) {
    if (officerRegState.otpTimerInterval) {
      clearInterval(officerRegState.otpTimerInterval);
    }
    officerRegState.otpSecondsRemaining = seconds;
    const timerEl = document.getElementById('officer-otp-timer');

    const updateDisplay = () => {
      const mins = Math.floor(officerRegState.otpSecondsRemaining / 60);
      const secs = officerRegState.otpSecondsRemaining % 60;
      if (timerEl) {
        timerEl.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
      }
      if (officerRegState.otpSecondsRemaining <= 0) {
        clearInterval(officerRegState.otpTimerInterval);
        officerRegState.otpTimerInterval = null;
        if (timerEl) timerEl.textContent = 'Expired';
        const errBox = document.getElementById('officer-otp-error');
        if (errBox) {
          errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-800 text-xs';
          errBox.innerHTML = `<strong>${escapeHtml(t('auth.otpExpired', {}, undefined, 'OTP expired'))}:</strong> ${escapeHtml(t('auth.otpExpiredNotice', {}, undefined, 'This OTP has expired. Please click Resend OTP to generate a new one.'))}`;
          errBox.classList.remove('hidden');
        }
      } else {
        officerRegState.otpSecondsRemaining--;
      }
    };

    updateDisplay();
    officerRegState.otpTimerInterval = setInterval(updateDisplay, 1000);
  }

  async function handleVerifyOfficerId(e) {
    if (e && typeof e.preventDefault === 'function') {
      e.preventDefault();
    }

    if (officerRegState && officerRegState.isVerifying) {
      return;
    }

    const input = document.getElementById('officer-verify-id-input');
    const errBox = document.getElementById('officer-id-error');
    const btn = document.getElementById('btn-verify-officer-id');
    const btnText = document.getElementById('btn-verify-text');
    const officerId = input ? input.value.trim().toUpperCase() : '';

    if (errBox) {
      errBox.classList.add('hidden');
      errBox.innerHTML = '';
    }

    if (!officerId) {
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-amber-200 bg-amber-50 text-amber-900 text-xs';
        errBox.innerHTML = `<strong>${escapeHtml(t('common.warning', {}, undefined, 'Warning'))}:</strong> ${escapeHtml(t('auth.enterOfficerIdPrompt', {}, undefined, 'Please enter your Officer ID (e.g. AGRI-TN-0001).'))}`;
        errBox.classList.remove('hidden');
      }
      input?.focus();
      return;
    }

    try {
      if (officerRegState) officerRegState.isVerifying = true;
      if (btn) {
        btn.disabled = true;
        btn.classList.add('opacity-75', 'cursor-not-allowed');
      }
      if (btnText) {
        btnText.innerHTML = `<span class="inline-flex items-center gap-2"><i data-lucide="loader-2" class="w-4 h-4 animate-spin"></i><span>${escapeHtml(t('auth.verifying', {}, undefined, 'Verifying...'))}</span></span>`;
        if (window.lucide) lucide.createIcons();
      }

      const res = await fetch('/api/auth/officer/verify-id', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ officer_id: officerId })
      });

      const data = await res.json().catch(() => ({}));

      if (res.ok) {
        officerRegState.officerId = data.officer_id;
        officerRegState.maskedMobile = data.masked_mobile;
        officerRegState.demoOtp = data.demo_otp;

        // Populate Step 2 UI
        const mobileEl = document.getElementById('officer-masked-mobile');
        if (mobileEl) mobileEl.textContent = data.masked_mobile;

        const otpValEl = document.getElementById('officer-demo-otp-val');
        if (otpValEl) otpValEl.textContent = data.demo_otp;

        const otpInput = document.getElementById('officer-otp-input');
        if (otpInput) otpInput.value = '';

        startOtpCountdown(data.expires_in_seconds || 300);
        goToOfficerStep(2);
        showToast(t('auth.officerIdVerified', {}, undefined, "Officer ID verified!"), 'success');
      } else {
        if (errBox) {
          errBox.classList.remove('hidden');
          if (res.status === 409) {
            // Already registered
            errBox.className = 'p-3.5 rounded-xl border border-amber-300 bg-amber-50 text-amber-900 text-xs space-y-2';
            errBox.innerHTML = `
              <div class="font-bold text-amber-900 text-sm flex items-center gap-1.5">
                <i data-lucide="alert-circle" class="w-4 h-4 text-amber-600 shrink-0"></i>
                <span data-i18n="auth.accountAlreadyExists">${escapeHtml(t('auth.accountAlreadyExists', {}, undefined, 'Officer account already exists'))}</span>
              </div>
              <p class="text-amber-800 text-xs leading-relaxed" data-i18n="auth.accountAlreadyExistsMsg">${escapeHtml(data.detail || t('auth.accountAlreadyExistsMsg', {}, undefined, 'An AgriFlow account has already been created for this Officer ID. Please use Officer Login.'))}</p>
              <button type="button" onclick="goToOfficerLoginPrefilled('${escapeHtml(officerId)}')" class="w-full py-2 px-3 text-xs font-bold rounded-lg bg-brand-700 text-white hover:bg-brand-800 transition shadow-sm flex items-center justify-center gap-1.5">
                <span data-i18n="auth.proceedToLogin">${escapeHtml(t('auth.proceedToLogin', {}, undefined, 'Proceed to Officer Login'))}</span> →
              </button>
            `;
            if (window.lucide) lucide.createIcons();
          } else {
            // 400 or 404 Not Found or other error
            errBox.className = 'p-3.5 rounded-xl border border-red-200 bg-red-50 text-red-900 text-xs space-y-1';
            errBox.innerHTML = `
              <div class="font-bold text-red-900 text-sm flex items-center gap-1.5">
                <i data-lucide="alert-triangle" class="w-4 h-4 text-red-600 shrink-0"></i>
                <span data-i18n="auth.invalidOfficerId">${escapeHtml(t('auth.invalidOfficerId', {}, undefined, 'Invalid Officer ID'))}</span>
              </div>
              <p class="text-red-800 text-xs leading-relaxed" data-i18n="auth.invalidOfficerIdMsg">${escapeHtml(t('auth.invalidOfficerIdMsg', {}, undefined, 'Please enter a valid registered Agriculture Officer ID.'))}</p>
            `;
            if (window.lucide) lucide.createIcons();
          }
        }
      }
    } catch (err) {
      console.error("Error verifying officer ID:", err);
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 text-xs';
        errBox.innerHTML = `${escapeHtml(t('auth.networkError', {}, undefined, 'Network error verifying Officer ID.'))}`;
        errBox.classList.remove('hidden');
      }
    } finally {
      if (officerRegState) officerRegState.isVerifying = false;
      if (btn) {
        btn.disabled = false;
        btn.classList.remove('opacity-75', 'cursor-not-allowed');
      }
      if (btnText) {
        btnText.textContent = t('auth.verifyOfficerId', {}, undefined, 'Verify Officer ID');
      }
    }
  }

  function autoFillDemoOtp() {
    const input = document.getElementById('officer-otp-input');
    if (input && officerRegState.demoOtp) {
      input.value = officerRegState.demoOtp;
      input.focus();
    }
  }

  async function handleVerifyOtp(e) {
    if (e && typeof e.preventDefault === 'function') {
      e.preventDefault();
    }
    const input = document.getElementById('officer-otp-input');
    const errBox = document.getElementById('officer-otp-error');
    const btn = document.getElementById('btn-verify-otp');
    const otp = input ? input.value.trim() : '';

    if (errBox) {
      errBox.classList.add('hidden');
      errBox.innerHTML = '';
    }

    if (!otp || otp.length !== 6) {
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-amber-200 bg-amber-50 text-amber-900 text-xs';
        errBox.innerHTML = `<strong>${escapeHtml(t('common.warning', {}, undefined, 'Warning'))}:</strong> ${escapeHtml(t('auth.enterSixDigitOtp', {}, undefined, 'Please enter the 6-digit OTP code.'))}`;
        errBox.classList.remove('hidden');
      }
      input?.focus();
      return;
    }

    try {
      if (btn) {
        btn.disabled = true;
        btn.classList.add('opacity-75', 'cursor-not-allowed');
      }
      const res = await fetch('/api/auth/officer/verify-otp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          officer_id: officerRegState.officerId,
          otp: otp
        })
      });

      const data = await res.json();

      if (res.ok) {
        if (officerRegState.otpTimerInterval) {
          clearInterval(officerRegState.otpTimerInterval);
          officerRegState.otpTimerInterval = null;
        }

        officerRegState.verificationToken = data.verification_token;
        officerRegState.officerDetails = data.officer;

        // Populate Step 3 details card
        const dtlId = document.getElementById('dtl-officer-id');
        const dtlName = document.getElementById('dtl-name');
        const dtlPost = document.getElementById('dtl-post');
        const dtlDept = document.getElementById('dtl-dept');
        const dtlState = document.getElementById('dtl-state');
        const dtlDistrict = document.getElementById('dtl-district');
        const dtlArea = document.getElementById('dtl-area');
        const dtlMobile = document.getElementById('dtl-mobile');

        if (dtlId) dtlId.textContent = data.officer.officer_id;
        if (dtlName) dtlName.textContent = data.officer.name;
        if (dtlPost) dtlPost.textContent = data.officer.designation;
        if (dtlDept) dtlDept.textContent = data.officer.department;
        if (dtlState) dtlState.textContent = data.officer.state;
        if (dtlDistrict) dtlDistrict.textContent = data.officer.district;
        if (dtlArea) dtlArea.textContent = data.officer.assigned_area;
        if (dtlMobile) dtlMobile.textContent = data.officer.masked_mobile;

        // Default Login ID to the verified Officer ID in Step 4
        const loginIdInput = document.getElementById('officer-new-login-id');
        if (loginIdInput) {
          loginIdInput.value = data.officer.officer_id;
        }

        goToOfficerStep(3);
        showToast(t('auth.officerDetailsVerified', {}, undefined, "Officer identity verified! Official details retrieved."), 'success');
      } else {
        if (errBox) {
          errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 text-xs';
          errBox.innerHTML = `<strong>${escapeHtml(t('auth.verificationFailed', {}, undefined, 'Verification Failed'))}:</strong> ${escapeHtml(data.detail || t('auth.invalidOtp', {}, undefined, 'Invalid OTP code.'))}`;
          errBox.classList.remove('hidden');
        }
      }
    } catch (err) {
      console.error("Error verifying OTP:", err);
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 text-xs';
        errBox.innerHTML = `${escapeHtml(t('auth.networkError', {}, undefined, 'Network error during OTP verification.'))}`;
        errBox.classList.remove('hidden');
      }
    } finally {
      if (btn) {
        btn.disabled = false;
        btn.classList.remove('opacity-75', 'cursor-not-allowed');
      }
    }
  }

  async function handleResendOtp() {
    const errBox = document.getElementById('officer-otp-error');
    if (errBox) {
      errBox.classList.add('hidden');
      errBox.innerHTML = '';
    }

    try {
      const res = await fetch('/api/auth/officer/resend-otp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ officer_id: officerRegState.officerId })
      });

      const data = await res.json();

      if (res.ok) {
        officerRegState.demoOtp = data.demo_otp;
        const otpValEl = document.getElementById('officer-demo-otp-val');
        if (otpValEl) otpValEl.textContent = data.demo_otp;

        const otpInput = document.getElementById('officer-otp-input');
        if (otpInput) otpInput.value = '';

        startOtpCountdown(data.expires_in_seconds || 300);
        showToast(`${t('auth.newDemoOtpGenerated', {}, undefined, 'New Demo OTP generated')}: ${data.demo_otp}`, 'info');
      } else {
        if (errBox) {
          errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 text-xs';
          errBox.innerHTML = `${escapeHtml(data.detail || t('auth.resendOtpFailed', {}, undefined, 'Failed to resend OTP.'))}`;
          errBox.classList.remove('hidden');
        }
      }
    } catch (err) {
      console.error("Error resending OTP:", err);
      showToast(t('auth.networkError', {}, undefined, "Network error resending OTP"), "error");
    }
  }

  async function handleCreateOfficerAccount(e) {
    e.preventDefault();
    const loginIdInput = document.getElementById('officer-new-login-id');
    const pwInput = document.getElementById('officer-new-password');
    const confirmInput = document.getElementById('officer-confirm-password');
    const errBox = document.getElementById('officer-cred-error');
    const btn = document.getElementById('btn-create-officer-acc');

    if (errBox) {
      errBox.classList.add('hidden');
      errBox.innerHTML = '';
    }

    const loginId = loginIdInput ? loginIdInput.value.trim() : '';
    const password = pwInput ? pwInput.value : '';
    const confirmPassword = confirmInput ? confirmInput.value : '';

    if (!loginId || !password || !confirmPassword) {
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-amber-200 bg-amber-50 text-amber-900 text-xs';
        errBox.innerHTML = `${escapeHtml(t('auth.requiredFields', {}, undefined, 'Please fill in all fields.'))}`;
        errBox.classList.remove('hidden');
      }
      return;
    }

    if (password.length < 6) {
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-amber-200 bg-amber-50 text-amber-900 text-xs';
        errBox.innerHTML = `${escapeHtml(t('auth.passwordLengthError', {}, undefined, 'Password must be at least 6 characters long.'))}`;
        errBox.classList.remove('hidden');
      }
      pwInput?.focus();
      return;
    }

    if (password !== confirmPassword) {
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 text-xs';
        errBox.innerHTML = `${escapeHtml(t('auth.passwordMismatch', {}, undefined, 'Passwords do not match.'))}`;
        errBox.classList.remove('hidden');
      }
      confirmInput?.focus();
      return;
    }

    try {
      if (btn) btn.disabled = true;
      const res = await fetch('/api/auth/officer/create-account', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          officer_id: officerRegState.officerId,
          verification_token: officerRegState.verificationToken,
          login_id: loginId,
          password: password,
          confirm_password: confirmPassword
        })
      });

      const data = await res.json();

      if (res.ok) {
        // Populate Step 5 Complete Card
        const doneId = document.getElementById('done-officer-id');
        const doneName = document.getElementById('done-officer-name');
        const doneLogin = document.getElementById('done-login-id');

        if (doneId) doneId.textContent = data.user.officer_id || officerRegState.officerId;
        if (doneName) doneName.textContent = data.user.name;
        if (doneLogin) doneLogin.textContent = data.user.login_id || loginId;

        officerRegState.createdLoginId = data.user.login_id || loginId;
        officerRegState.createdOfficerId = data.user.officer_id || officerRegState.officerId;

        goToOfficerStep(5);
        showToast(t('auth.officerAccountCreatedSuccess', {}, undefined, "Officer account created successfully!"), 'success');
      } else {
        if (errBox) {
          errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 text-xs';
          errBox.innerHTML = `<strong>${escapeHtml(t('auth.registrationFailed', {}, undefined, 'Registration failed'))}:</strong> ${escapeHtml(data.detail || 'Could not create account.')}`;
          errBox.classList.remove('hidden');
        }
      }
    } catch (err) {
      console.error("Error creating officer account:", err);
      if (errBox) {
        errBox.className = 'p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 text-xs';
        errBox.innerHTML = `${escapeHtml(t('auth.networkError', {}, undefined, 'Network error creating officer account.'))}`;
        errBox.classList.remove('hidden');
      }
    } finally {
      if (btn) btn.disabled = false;
    }
  }

  function goToOfficerLoginAfterReg() {
    const prefillId = (officerRegState && (officerRegState.createdLoginId || officerRegState.createdOfficerId)) || '';
    resetOfficerRegistrationState(true);
    switchAuthTab('login');
    setAuthRole('OFFICER');
    const idInput = document.getElementById('login-identifier');
    if (idInput && prefillId) {
      idInput.value = prefillId;
      const pwInput = document.getElementById('login-password');
      if (pwInput) pwInput.focus();
    }
  }

  function goToOfficerLoginPrefilled(officerId) {
    resetOfficerRegistrationState(true);
    closeModal('demo-registry-modal');
    switchAuthTab('login');
    setAuthRole('OFFICER');
    const idInput = document.getElementById('login-identifier');
    if (idInput && officerId) {
      idInput.value = officerId;
      const pwInput = document.getElementById('login-password');
      if (pwInput) pwInput.focus();
    }
  }

  // -------------------------------------------------------------
  // LOGIN SUBMIT
  // -------------------------------------------------------------
  async function handleLoginSubmit(e) {
    e.preventDefault();
    const id = document.getElementById('login-identifier').value.trim();
    const pw = document.getElementById('login-password').value;

    try {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          identifier: id,
          password: pw,
          role: currentAuthRole
        })
      });

      if (res.ok) {
        const data = await res.json();
        STATE.token = data.token;
        STATE.user = data.user;
        localStorage.setItem('agriflow_token', data.token);
        showToast(t('auth.welcomeBack', { name: data.user.name }, undefined, `Welcome back, ${data.user.name}!`), 'success');
        await checkSession();
        navigate(data.user.role === 'OFFICER' ? 'officer-dashboard' : 'farmer-dashboard');
      } else {
        const err = await res.json().catch(() => ({}));
        showToast(err.detail || t('auth.invalidCredentials', {}, undefined, "Invalid login credentials"), "error");
      }
    } catch (err) {
      showToast(t('auth.networkError', {}, undefined, "Network error logging in"), "error");
    }
  }

  // -------------------------------------------------------------
  // FARMER REGISTRATION SUBMIT
  // -------------------------------------------------------------
  async function handleFarmerRegisterSubmit(e) {
    e.preventDefault();
    const name = document.getElementById('reg-farmer-name')?.value?.trim() || '';
    const phone = document.getElementById('reg-farmer-phone')?.value?.trim() || '';
    const emailRaw = document.getElementById('reg-farmer-email')?.value?.trim();
    const email = emailRaw ? emailRaw : null;
    const pw = document.getElementById('reg-farmer-password')?.value || '';

    if (!name || !phone || !pw) {
      showToast(t('auth.requiredFields', {}, undefined, "Please fill in all required fields (Name, Mobile, Password)."), "warning");
      return;
    }

    const payload = {
      name: name,
      phone: phone,
      email: email,
      password: pw,
      role: 'FARMER',
      village: document.getElementById('reg-f-village')?.value?.trim() || 'Sankari West',
      area: document.getElementById('reg-f-area')?.value?.trim() || 'Sankari',
      district: document.getElementById('reg-f-district')?.value?.trim() || 'Salem',
      state: document.getElementById('reg-f-state')?.value?.trim() || 'Tamil Nadu',
      land_unit: 'Acres',
      farming_type: document.getElementById('reg-f-farming-type')?.value?.trim() || 'Natural / Organic'
    };

    const landVal = parseFloat(document.getElementById('reg-f-land')?.value || '1.0');
    payload.land_area = isNaN(landVal) || landVal <= 0 ? 1.0 : landVal;

    try {
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const data = await res.json();
        STATE.token = data.token;
        STATE.user = data.user;
        localStorage.setItem('agriflow_token', data.token);
        showToast(t('auth.accountCreated', { name: data.user.name }, undefined, `Account created! Welcome, ${data.user.name}.`), 'success');
        await checkSession();
        navigate('farmer-dashboard');
      } else {
        const err = await res.json().catch(() => ({}));
        showToast(err.detail || t('auth.registrationFailed', {}, undefined, "Registration failed. Please check your details."), "error");
      }
    } catch (err) {
      console.error("Registration error:", err);
      showToast(t('auth.networkError', {}, undefined, "Network error registering account"), "error");
    }
  }

  // Preserve backwards compatibility and global access
  window.openAuthModal = openAuthModal;
  window.switchAuthTab = switchAuthTab;
  window.setAuthRole = setAuthRole;
  window.navigate = navigate;
  window.logout = logout;
  window.handleRegisterSubmit = handleFarmerRegisterSubmit;
  window.handleFarmerRegisterSubmit = handleFarmerRegisterSubmit;
  window.handleVerifyOfficerId = handleVerifyOfficerId;
  window.handleVerifyOtp = handleVerifyOtp;
  window.handleResendOtp = handleResendOtp;
  window.handleCreateOfficerAccount = handleCreateOfficerAccount;
  window.goToOfficerStep = goToOfficerStep;
  window.resetOfficerRegistrationState = resetOfficerRegistrationState;
  window.resetOfficerWizardToStep1 = resetOfficerWizardToStep1;
  window.autoFillDemoOtp = autoFillDemoOtp;
  window.fillOfficerId = fillOfficerId;
  window.goToOfficerLoginAfterReg = goToOfficerLoginAfterReg;
  window.goToOfficerLoginPrefilled = goToOfficerLoginPrefilled;

  // -------------------------------------------------------------
  // UI UTILITIES & TOASTS
  // -------------------------------------------------------------
  function openModal(modalId) {
    const m = document.getElementById(modalId);
    if (m) {
      m.classList.remove('hidden');
      if (modalId === 'add-produce-modal') {
        updatePriceUnitLabel();
      }
      lucide.createIcons();
    }
  }

  function closeModal(modalId) {
    const m = document.getElementById(modalId);
    if (m) m.classList.add('hidden');
  }

  function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    let bg = 'bg-slate-900 text-white border-slate-700';
    let icon = 'info';

    if (type === 'success') {
      bg = 'bg-emerald-800 text-white border-emerald-600';
      icon = 'check-circle-2';
    } else if (type === 'error') {
      bg = 'bg-red-800 text-white border-red-600';
      icon = 'alert-triangle';
    } else if (type === 'warning') {
      bg = 'bg-amber-800 text-white border-amber-600';
      icon = 'alert-circle';
    }

    toast.className = `${bg} px-4 py-3 rounded-xl border shadow-xl flex items-center space-x-2.5 text-xs font-semibold transition-all duration-300 transform translate-y-2 opacity-0 pointer-events-auto`;
    toast.innerHTML = `
      <i data-lucide="${icon}" class="w-4 h-4 shrink-0"></i>
      <span>${escapeHtml(message)}</span>
    `;

    container.appendChild(toast);
    lucide.createIcons();

    requestAnimationFrame(() => {
      toast.classList.remove('translate-y-2', 'opacity-0');
    });

    setTimeout(() => {
      toast.classList.add('opacity-0', '-translate-y-2');
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
