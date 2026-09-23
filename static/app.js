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
    if (sourceType === 'OFFICER_ENTRY') {
      return t('produce.sourceOfficer', {}, undefined, 'Officer Verified');
    } else if (sourceType === 'FARMER_VERIFIED') {
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
        const statusEl = document.getElementById('ws-status');
        if (statusEl && window.AgriFlowI18n) {
          statusEl.innerText = window.AgriFlowI18n.t('common.liveSync');
        } else if (statusEl) {
          statusEl.innerText = 'Live Sync';
        }
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
    showToast("You have been signed out.", "info");
    navigate('landing');
  }

  // Navigation Controller
  function navigate(view, subaction = null) {
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
      const isOfficer = p.source_type === 'OFFICER_ENTRY';
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

      const sourceLabel = translateSource(data.source_type);
      const actorName = data.source_type === 'OFFICER_ENTRY' ? (data.officer_name || '') : (data.farmer_name || '');
      document.getElementById('pd-source').innerText = actorName ? `${sourceLabel} (${actorName})` : sourceLabel;

      const badgeEl = document.getElementById('pd-status-badge');
      if (badgeEl) {
        badgeEl.innerText = t('produce.verifiedBadge', {}, undefined, '✓ VERIFIED');
      }

      document.getElementById('pd-notes').innerText = data.notes || "Official local agricultural entry inspected and verified.";

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
        showToast(t('notifications.inquirySent', {}, undefined, "✓ Purchase inquiry sent to producer / local officer!"), "success");
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
        document.getElementById('officer-dash-details').innerText = `${STATE.profile?.designation || 'Agricultural Officer'} | ${assignedJurisdictionLabel}: ${dash.jurisdiction.area}, ${dash.jurisdiction.district}, ${dash.jurisdiction.state}`;

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
          comment: 'Field inspected and verified by AAO Ravi Kumar.'
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

        // Render assigned officer card
        const offCard = document.getElementById('farmer-officer-card');
        if (dash.assigned_officer) {
          offCard.classList.remove('hidden');
          document.getElementById('assigned-officer-name').innerText = `${dash.assigned_officer.name} (${dash.assigned_officer.designation})`;
          const jurisdictionLabel = t('officer.assignedJurisdiction', {}, undefined, 'Jurisdiction');
          const contactLabel = t('produce.contact', {}, undefined, 'Contact');
          document.getElementById('assigned-officer-contact').innerText = `${jurisdictionLabel}: ${dash.assigned_officer.assigned_area}, ${dash.assigned_officer.district} | ${contactLabel}: ${dash.assigned_officer.phone || dash.assigned_officer.email}`;
        } else {
          offCard.classList.add('hidden');
        }
      }

      if (reqRes.ok) {
        STATE.farmerRequests = await reqRes.json();
        renderFarmerRequests(STATE.farmerRequests);
      }
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
      container.innerHTML = `
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(fullNameLabel)} *</label>
            <input type="text" id="prof-name" required value="${escapeHtml(STATE.user.name)}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(designationLabel)} *</label>
            <input type="text" id="prof-designation" required value="${escapeHtml(prof.designation || 'Assistant Agricultural Officer')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(departmentLabel)} *</label>
            <input type="text" id="prof-department" required value="${escapeHtml(prof.department || 'Department of Agriculture')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(contactLabel)} *</label>
            <input type="text" id="prof-contact" required value="${escapeHtml(prof.contact || STATE.user.phone)}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-3 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(assignedAreaLabel)} *</label>
            <input type="text" id="prof-area" required value="${escapeHtml(prof.assigned_area || 'Sankari')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(districtLabel)} *</label>
            <input type="text" id="prof-district" required value="${escapeHtml(prof.district || 'Salem')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(stateLabel)} *</label>
            <input type="text" id="prof-state" required value="${escapeHtml(prof.state || 'Tamil Nadu')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 mb-1">${escapeHtml(officialEmailLabel)}</label>
          <input type="email" id="prof-email" value="${escapeHtml(STATE.user.email || '')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
        </div>
      `;
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
    const name = document.getElementById('prof-name').value;

    let body = {};
    let url = '';

    if (isOfficer) {
      url = '/api/officer/profile';
      body = {
        name: name,
        designation: document.getElementById('prof-designation').value,
        department: document.getElementById('prof-department').value,
        assigned_area: document.getElementById('prof-area').value,
        district: document.getElementById('prof-district').value,
        state: document.getElementById('prof-state').value,
        contact: document.getElementById('prof-contact').value,
        email: document.getElementById('prof-email').value
      };
    } else {
      url = '/api/farmer/profile';
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

  function openAuthModal(tab = 'login', preferredRole = null) {
    navigate('auth');
    switchAuthTab(tab);
    if (preferredRole) {
      setAuthRole(preferredRole);
    }
  }

  function switchAuthTab(tab) {
    const formLogin = document.getElementById('form-login');
    const formRegister = document.getElementById('form-register');
    const tabLogin = document.getElementById('tab-login');
    const tabRegister = document.getElementById('tab-register');

    if (tab === 'login') {
      formLogin.classList.remove('hidden');
      formRegister.classList.add('hidden');
      tabLogin.classList.add('border-brand-700', 'text-brand-700');
      tabLogin.classList.remove('border-transparent', 'text-slate-500');
      tabRegister.classList.remove('border-brand-700', 'text-brand-700');
      tabRegister.classList.add('border-transparent', 'text-slate-500');
    } else {
      formLogin.classList.add('hidden');
      formRegister.classList.remove('hidden');
      tabRegister.classList.add('border-brand-700', 'text-brand-700');
      tabRegister.classList.remove('border-transparent', 'text-slate-500');
      tabLogin.classList.remove('border-brand-700', 'text-brand-700');
      tabLogin.classList.add('border-transparent', 'text-slate-500');
    }
  }

  function setAuthRole(role) {
    currentAuthRole = role;
    const btnOff = document.getElementById('role-btn-officer');
    const btnFarm = document.getElementById('role-btn-farmer');
    const regOffFields = document.getElementById('reg-officer-fields');
    const regFarmFields = document.getElementById('reg-farmer-fields');

    if (role === 'OFFICER') {
      btnOff.classList.add('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnOff.classList.remove('border-slate-200', 'bg-white', 'text-slate-600');
      btnFarm.classList.remove('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnFarm.classList.add('border-slate-200', 'bg-white', 'text-slate-600');

      regOffFields.classList.remove('hidden');
      regFarmFields.classList.add('hidden');
    } else {
      btnFarm.classList.add('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnFarm.classList.remove('border-slate-200', 'bg-white', 'text-slate-600');
      btnOff.classList.remove('border-brand-700', 'bg-brand-50/50', 'text-brand-800');
      btnOff.classList.add('border-slate-200', 'bg-white', 'text-slate-600');

      regOffFields.classList.add('hidden');
      regFarmFields.classList.remove('hidden');
    }
  }

  async function handleLoginSubmit(e) {
    e.preventDefault();
    const id = document.getElementById('login-identifier').value;
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
        const err = await res.json();
        showToast(err.detail || t('auth.invalidCredentials', {}, undefined, "Invalid login credentials"), "error");
      }
    } catch (err) {
      showToast(t('auth.networkError', {}, undefined, "Network error logging in"), "error");
    }
  }

  async function handleRegisterSubmit(e) {
    e.preventDefault();
    const name = document.getElementById('reg-name')?.value?.trim() || '';
    const phone = document.getElementById('reg-phone')?.value?.trim() || '';
    const emailRaw = document.getElementById('reg-email')?.value?.trim();
    const email = emailRaw ? emailRaw : null;
    const pw = document.getElementById('reg-password')?.value || '';

    if (!name || !phone || !pw) {
      showToast(t('auth.requiredFields', {}, undefined, "Please fill in all required fields (Name, Mobile, Password)."), "warning");
      return;
    }

    const payload = {
      name: name,
      phone: phone,
      email: email,
      password: pw,
      role: currentAuthRole
    };

    if (currentAuthRole === 'OFFICER') {
      payload.designation = document.getElementById('reg-designation')?.value?.trim() || 'Assistant Agricultural Officer';
      payload.department = document.getElementById('reg-department')?.value?.trim() || 'Department of Agriculture';
      payload.assigned_area = document.getElementById('reg-assigned-area')?.value?.trim() || 'Sankari';
      payload.district = document.getElementById('reg-district')?.value?.trim() || 'Salem';
      payload.state = document.getElementById('reg-state')?.value?.trim() || 'Tamil Nadu';
    } else {
      payload.village = document.getElementById('reg-f-village')?.value?.trim() || 'Sankari West';
      payload.area = document.getElementById('reg-f-area')?.value?.trim() || 'Sankari';
      payload.district = document.getElementById('reg-f-district')?.value?.trim() || 'Salem';
      payload.state = document.getElementById('reg-f-state')?.value?.trim() || 'Tamil Nadu';
      const landVal = parseFloat(document.getElementById('reg-f-land')?.value || '1.0');
      payload.land_area = isNaN(landVal) || landVal <= 0 ? 1.0 : landVal;
      payload.land_unit = 'Acres';
      payload.farming_type = document.getElementById('reg-f-farming-type')?.value?.trim() || 'Conventional';
    }

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
        navigate(data.user.role === 'OFFICER' ? 'officer-dashboard' : 'farmer-dashboard');
      } else {
        const err = await res.json().catch(() => ({}));
        showToast(err.detail || t('auth.registrationFailed', {}, undefined, "Registration failed. Please check your details."), "error");
      }
    } catch (err) {
      console.error("Registration error:", err);
      showToast(t('auth.networkError', {}, undefined, "Network error registering account"), "error");
    }
  }

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
