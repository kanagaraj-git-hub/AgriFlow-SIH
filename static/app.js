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

  // Initialization on DOM Ready
  document.addEventListener('DOMContentLoaded', async () => {
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
        if (statusEl) statusEl.innerText = 'Live Sync';
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
        const statusEl = document.getElementById('ws-status');
        if (statusEl) statusEl.innerText = 'Reconnecting...';
        setTimeout(setupWebSocket, 3000);
      };
    } catch (err) {
      console.error("WS connection error:", err);
    }
  }

  function handleRealTimeMessage(msg) {
    if (msg.type === 'PRODUCE_ADDED') {
      showToast(`🌾 New produce added: ${msg.record.crop_name} (${msg.record.quantity} ${msg.record.unit}) in ${msg.record.area}`, 'info');
      if (STATE.currentView === 'produce') loadProduceList();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'PRODUCE_UPDATED') {
      showToast(`🔄 Produce updated: ${msg.record.crop_name}`, 'info');
      if (STATE.currentView === 'produce') loadProduceList();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'PRODUCE_DELETED') {
      if (STATE.currentView === 'produce') loadProduceList();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'REQUEST_SUBMITTED') {
      showToast(`📋 New Farmer crop submission: ${msg.request.crop_name} (${msg.request.expected_quantity} ${msg.request.quantity_unit}) in ${msg.request.area}`, 'info');
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
      if (STATE.currentView === 'farmer-dashboard') loadFarmerDashboard();
    } else if (msg.type === 'REQUEST_VERIFIED') {
      showToast(`✅ Crop verified: ${msg.request.crop_name} (${msg.request.expected_quantity} ${msg.request.quantity_unit}) is now live!`, 'success');
      if (STATE.currentView === 'farmer-dashboard') loadFarmerDashboard();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
      if (STATE.currentView === 'produce') loadProduceList();
    } else if (msg.type === 'REQUEST_REJECTED') {
      showToast(`⚠️ Farmer request rejected: ${msg.request.crop_name}`, 'warning');
      if (STATE.currentView === 'farmer-dashboard') loadFarmerDashboard();
      if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
    } else if (msg.type === 'PURCHASE_REQUEST_RECEIVED') {
      showToast(`💼 Purchase Inquiry: Buyer requested ${msg.request.requested_quantity} ${msg.request.quantity_unit} of ${msg.crop_name}`, 'success');
    } else if (msg.type === 'DEMO_RESET') {
      showToast(`🔄 Demo data has been reset to initial state`, 'info');
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

  function updateNavAuth(isLoggedIn) {
    const guestControls = document.getElementById('guest-controls');
    const userControls = document.getElementById('user-controls');
    const officerNav = document.getElementById('officer-nav');
    const farmerNav = document.getElementById('farmer-nav');

    if (isLoggedIn && STATE.user) {
      guestControls.classList.add('hidden');
      userControls.classList.remove('hidden');

      document.getElementById('nav-user-name').innerText = STATE.user.name;
      document.getElementById('nav-user-role').innerText = STATE.user.role === 'OFFICER' ? 'Agriculture Officer' : 'Farmer';
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

  function populateLocationDropdowns() {
    const stateSelect = document.getElementById('filter-state');
    const landingStateSelect = document.getElementById('landing-state-select');
    if (!stateSelect) return;

    const states = Object.keys(STATE.locations);
    if (states.length === 0) return;

    let stateHtml = '<option value="All">All States</option>';
    states.forEach(st => {
      stateHtml += `<option value="${st}">${st}</option>`;
    });

    stateSelect.innerHTML = stateHtml;
    if (landingStateSelect) landingStateSelect.innerHTML = stateHtml;

    // Default to Tamil Nadu if available
    if (states.includes('Tamil Nadu')) {
      stateSelect.value = 'Tamil Nadu';
      if (landingStateSelect) landingStateSelect.value = 'Tamil Nadu';
      onStateFilterChange();
    }
  }

  function onStateFilterChange() {
    const stateVal = document.getElementById('filter-state').value;
    const districtSelect = document.getElementById('filter-district');
    const areaSelect = document.getElementById('filter-area');

    let districtHtml = '<option value="All">All Districts</option>';
    if (stateVal !== 'All' && STATE.locations[stateVal]) {
      const districts = Object.keys(STATE.locations[stateVal]);
      districts.forEach(dt => {
        districtHtml += `<option value="${dt}">${dt}</option>`;
      });
    }
    districtSelect.innerHTML = districtHtml;

    // Default to Salem if present
    if (stateVal === 'Tamil Nadu') {
      districtSelect.value = 'Salem';
    }

    onDistrictFilterChange();
  }

  function onDistrictFilterChange() {
    const stateVal = document.getElementById('filter-state').value;
    const districtVal = document.getElementById('filter-district').value;
    const areaSelect = document.getElementById('filter-area');

    let areaHtml = '<option value="All">All Areas</option>';
    if (stateVal !== 'All' && districtVal !== 'All' && STATE.locations[stateVal]?.[districtVal]) {
      const areas = STATE.locations[stateVal][districtVal];
      areas.forEach(ar => {
        areaHtml += `<option value="${ar}">${ar}</option>`;
      });
    }
    areaSelect.innerHTML = areaHtml;

    // Default to Sankari if present
    if (districtVal === 'Salem') {
      areaSelect.value = 'Sankari';
    }

    loadProduceList();
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

    countText.innerText = `Showing ${items.length} verified produce record${items.length === 1 ? '' : 's'}`;

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

      html += `
        <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:shadow-md hover:border-brand-300 transition flex flex-col justify-between space-y-4">
          <div>
            <!-- Card Header: Emoji, Crop Name, Status -->
            <div class="flex items-start justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-3xl p-2 rounded-xl bg-slate-50 border border-slate-100">${emoji}</span>
                <div>
                  <h3 class="text-lg font-bold text-slate-900 leading-tight">${escapeHtml(p.crop_name)}</h3>
                  <span class="text-[11px] text-slate-500 font-medium">${escapeHtml(p.produce_type || 'Field Crop')}</span>
                </div>
              </div>
              <span class="badge-verified text-[11px] font-bold px-2 py-0.5 rounded-full inline-flex items-center space-x-1">
                <span>✓ VERIFIED</span>
              </span>
            </div>

            <!-- Quantity Display -->
            <div class="mt-4 p-3 rounded-xl bg-emerald-50/70 border border-emerald-100">
              <span class="text-[11px] font-semibold text-emerald-800 uppercase tracking-wider block">Available Quantity</span>
              <div class="text-2xl font-black text-emerald-950 flex items-baseline space-x-1 mt-0.5">
                <span>${p.quantity}</span>
                <span class="text-xs font-bold text-emerald-700">${escapeHtml(p.unit)}</span>
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
                <span>Availability: <strong class="text-slate-700">${p.availability_date}</strong></span>
              </div>
              <div class="flex items-center space-x-1.5">
                <i data-lucide="award" class="w-3.5 h-3.5 text-slate-400 shrink-0"></i>
                <span>Quality: <strong class="text-slate-700">${escapeHtml(p.quality || 'Grade A')}</strong></span>
              </div>
            </div>
          </div>

          <!-- Footer: Source Badge & View Details CTA -->
          <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
            <div class="inline-flex items-center space-x-1 px-2 py-0.5 rounded-md ${sourceBadgeClass} text-[10px] font-bold">
              <i data-lucide="${sourceIcon}" class="w-3 h-3"></i>
              <span class="truncate max-w-[130px]">${p.source_type === 'OFFICER_ENTRY' ? 'Officer Verified' : 'Farmer Verified'}</span>
            </div>

            <button onclick="openProduceDetails(${p.id})" class="px-3.5 py-1.5 rounded-lg bg-brand-700 hover:bg-brand-800 text-white font-bold text-xs shadow-sm transition flex items-center space-x-1">
              <span>View Details</span>
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
        showToast("Produce record not found", "error");
        return;
      }
      const data = await res.json();

      document.getElementById('pd-crop-name').innerText = data.crop_name;
      document.getElementById('pd-emoji').innerText = getCropEmoji(data.crop_name);
      document.getElementById('pd-location').innerText = `${data.area}, ${data.district}, ${data.state}`;
      document.getElementById('pd-qty').innerText = `${data.quantity} ${data.unit}`;
      document.getElementById('pd-quality').innerText = data.quality || 'Grade A';
      document.getElementById('pd-avail-date').innerText = data.availability_date;
      document.getElementById('pd-source').innerText = data.source_display;
      document.getElementById('pd-notes').innerText = data.notes || "Official local agricultural entry inspected and verified.";

      // Set form fields for purchase request
      document.getElementById('pr-produce-id').value = data.id;
      document.getElementById('pr-unit').value = data.unit;
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
        showToast("✓ Purchase inquiry sent to producer / local officer!", "success");
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
        document.getElementById('officer-dash-details').innerText = `${STATE.profile?.designation || 'Agricultural Officer'} | Assigned Jurisdiction: ${dash.jurisdiction.area}, ${dash.jurisdiction.district}, ${dash.jurisdiction.state}`;

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
      html += `
        <div class="p-4 rounded-xl bg-amber-50/50 border border-amber-200/80 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="flex items-start space-x-3.5">
            <span class="text-3xl p-2 bg-white rounded-xl border border-amber-200">${emoji}</span>
            <div class="space-y-1">
              <div class="flex items-center space-x-2">
                <span class="text-base font-bold text-slate-900">${escapeHtml(req.farmer_name)}</span>
                <span class="text-xs text-slate-500 font-medium">(${escapeHtml(req.farmer_phone)})</span>
                <span class="badge-pending text-[10px] font-bold px-2 py-0.5 rounded-full">🟡 Pending Verification</span>
              </div>
              <div class="text-xs text-slate-700 font-semibold">
                Crop: <span class="text-brand-800 text-sm font-bold">${escapeHtml(req.crop_name)}</span> |
                Cultivated: <strong>${req.cultivated_area} ${escapeHtml(req.cultivated_area_unit || 'Acres')}</strong> |
                Expected Yield: <strong class="text-emerald-800 font-bold">${req.expected_quantity} ${escapeHtml(req.quantity_unit)}</strong>
              </div>
              <div class="text-[11px] text-slate-500 flex flex-wrap gap-x-3">
                <span>📍 Location: <strong>${escapeHtml(req.area)}, ${escapeHtml(req.district)}, ${escapeHtml(req.state)}</strong></span>
                <span>📅 Harvest: <strong>${req.expected_harvest_date}</strong></span>
                <span>🌱 Stage: <strong>${escapeHtml(req.crop_stage || 'Pre-Harvest')}</strong></span>
              </div>
              ${req.notes ? `<p class="text-[11px] text-slate-600 italic bg-white/70 p-1.5 rounded border border-amber-100">Farmer Note: "${escapeHtml(req.notes)}"</p>` : ''}
            </div>
          </div>

          <div class="flex items-center space-x-2 shrink-0 self-end md:self-center">
            <button onclick="confirmOfficerVerify(${req.id})" class="px-4 py-2 rounded-lg bg-emerald-700 hover:bg-emerald-800 text-white font-bold text-xs shadow-sm transition flex items-center space-x-1">
              <i data-lucide="check" class="w-4 h-4"></i>
              <span>VERIFY</span>
            </button>
            <button onclick="openRejectModal(${req.id})" class="px-3.5 py-2 rounded-lg bg-red-100 hover:bg-red-200 text-red-700 font-bold text-xs transition flex items-center space-x-1">
              <i data-lucide="x" class="w-4 h-4"></i>
              <span>REJECT</span>
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
      tbody.innerHTML = `<tr><td colspan="8" class="text-center py-8 text-slate-400">No produce records recorded yet in your area.</td></tr>`;
      return;
    }

    let html = '';
    items.forEach(p => {
      const isAvail = p.verification_status === 'VERIFIED';
      const statusPill = isAvail
        ? `<span class="badge-verified text-[11px] font-bold px-2 py-0.5 rounded-full">✓ Verified</span>`
        : `<span class="badge-unavailable text-[11px] font-bold px-2 py-0.5 rounded-full">⚪ Unavailable</span>`;

      html += `
        <tr class="hover:bg-slate-50 transition text-slate-700">
          <td class="py-3 px-4 font-bold text-slate-900 flex items-center space-x-2">
            <span>${getCropEmoji(p.crop_name)}</span>
            <span>${escapeHtml(p.crop_name)}</span>
          </td>
          <td class="py-3 px-4 font-bold text-emerald-800">${p.quantity} ${escapeHtml(p.unit)}</td>
          <td class="py-3 px-4">${escapeHtml(p.area)}, ${escapeHtml(p.district)}</td>
          <td class="py-3 px-4">${p.availability_date}</td>
          <td class="py-3 px-4 font-semibold text-slate-600">${escapeHtml(p.quality || 'Grade A')}</td>
          <td class="py-3 px-4 text-xs font-semibold text-slate-500">${p.source_type === 'OFFICER_ENTRY' ? 'Direct Officer Entry' : 'Farmer Verified'}</td>
          <td class="py-3 px-4">${statusPill}</td>
          <td class="py-3 px-4 text-right space-x-1 whitespace-nowrap">
            <button onclick="toggleProduceAvailability(${p.id})" title="${isAvail ? 'Mark Unavailable' : 'Mark Available'}" class="p-1.5 rounded hover:bg-slate-100 text-slate-500 hover:text-slate-800">
              <i data-lucide="${isAvail ? 'eye-off' : 'eye'}" class="w-4 h-4"></i>
            </button>
            <button onclick="openOfficerEditProduce(${JSON.stringify(p).replace(/"/g, '&quot;')})" title="Edit Produce" class="p-1.5 rounded hover:bg-slate-100 text-slate-500 hover:text-blue-600">
              <i data-lucide="edit-2" class="w-4 h-4"></i>
            </button>
            <button onclick="deleteOfficerProduce(${p.id})" title="Delete" class="p-1.5 rounded hover:bg-red-50 text-slate-400 hover:text-red-600">
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
          area: area,
          district: district,
          state: state,
          quality: quality,
          availability_date: availDate,
          notes: notes
        })
      });

      if (res.ok) {
        showToast(editId ? "Produce updated successfully" : "✓ Produce recorded and verified directly by Officer!", "success");
        closeModal('add-produce-modal');
        document.getElementById('officer-produce-form').reset();
        document.getElementById('officer-produce-edit-id').value = '';
        loadOfficerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || "Failed to save produce", "error");
      }
    } catch (err) {
      showToast("Error saving produce", "error");
    }
  }

  function openOfficerEditProduce(p) {
    document.getElementById('produce-modal-title').innerText = 'Edit Local Produce';
    document.getElementById('officer-produce-edit-id').value = p.id;
    document.getElementById('op-crop').value = p.crop_name;
    document.getElementById('op-type').value = p.produce_type || 'Field Crop';
    document.getElementById('op-qty').value = p.quantity;
    document.getElementById('op-unit').value = p.unit;
    document.getElementById('op-area').value = p.area;
    document.getElementById('op-district').value = p.district;
    document.getElementById('op-state').value = p.state;
    document.getElementById('op-quality').value = p.quality || 'Grade A';
    document.getElementById('op-avail-date').value = p.availability_date;
    document.getElementById('op-notes').value = p.notes || '';

    openModal('add-produce-modal');
  }

  async function toggleProduceAvailability(id) {
    try {
      const res = await fetch(`/api/officer/produce/${id}/toggle-status`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${STATE.token}` }
      });
      if (res.ok) {
        showToast("Produce status updated", "info");
        loadOfficerDashboard();
      }
    } catch (err) {
      showToast("Failed to toggle status", "error");
    }
  }

  async function deleteOfficerProduce(id) {
    if (!confirm("Are you sure you want to delete this produce record?")) return;

    try {
      const res = await fetch(`/api/officer/produce/${id}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${STATE.token}` }
      });
      if (res.ok) {
        showToast("Produce record deleted", "info");
        loadOfficerDashboard();
      }
    } catch (err) {
      showToast("Failed to delete produce", "error");
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
        showToast("✓ Farmer submission verified and published to public View Produce!", "success");
        loadOfficerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || "Verification failed", "error");
      }
    } catch (e) {
      showToast("Network error verifying request", "error");
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
      showToast("Please provide a reason for rejection", "warning");
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
        showToast("Request rejected and feedback sent to farmer.", "info");
        closeModal('reject-modal');
        loadOfficerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || "Rejection failed", "error");
      }
    } catch (e) {
      showToast("Network error rejecting request", "error");
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
        document.getElementById('farmer-dash-details').innerText = `${STATE.profile?.land_area || 2} ${STATE.profile?.land_unit || 'Acres'} | ${dash.location.village || 'Sankari West'}, ${dash.location.area}, ${dash.location.district}`;

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
          document.getElementById('assigned-officer-contact').innerText = `Jurisdiction: ${dash.assigned_officer.assigned_area}, ${dash.assigned_officer.district} | Contact: ${dash.assigned_officer.phone || dash.assigned_officer.email}`;
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
        statusPill = `<span class="badge-pending text-xs font-bold px-2.5 py-1 rounded-full">🟡 Pending Verification</span>`;
      } else if (r.status === 'VERIFIED') {
        statusPill = `<span class="badge-verified text-xs font-bold px-2.5 py-1 rounded-full">🟢 ✓ Verified</span>`;
      } else {
        statusPill = `<span class="badge-rejected text-xs font-bold px-2.5 py-1 rounded-full">🔴 Rejected</span>`;
      }

      html += `
        <div class="p-4 rounded-xl bg-white border border-slate-200 shadow-sm hover:border-brand-300 transition space-y-3">
          <div class="flex items-start justify-between">
            <div class="flex items-center space-x-3">
              <span class="text-3xl p-2 bg-slate-50 rounded-xl border border-slate-100">${getCropEmoji(r.crop_name)}</span>
              <div>
                <h4 class="text-base font-bold text-slate-900">${escapeHtml(r.crop_name)}</h4>
                <span class="text-xs text-slate-500 font-medium">Expected Harvest: <strong>${r.expected_harvest_date}</strong></span>
              </div>
            </div>
            ${statusPill}
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs bg-slate-50 p-2.5 rounded-lg border border-slate-100">
            <div>
              <span class="text-slate-400 block text-[10px]">Cultivated Area</span>
              <span class="font-bold text-slate-800">${r.cultivated_area} ${escapeHtml(r.cultivated_area_unit || 'Acres')}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">Expected Yield</span>
              <span class="font-bold text-emerald-800">${r.expected_quantity} ${escapeHtml(r.quantity_unit)}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">Location</span>
              <span class="font-bold text-slate-800">${escapeHtml(r.area)}, ${escapeHtml(r.district)}</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">Crop Stage</span>
              <span class="font-bold text-slate-800">${escapeHtml(r.crop_stage || 'Vegetative')}</span>
            </div>
          </div>

          ${r.officer_comment ? `
            <div class="text-xs p-2.5 rounded-lg ${r.status === 'VERIFIED' ? 'bg-emerald-50 text-emerald-900 border border-emerald-100' : 'bg-red-50 text-red-900 border border-red-100'}">
              <span class="font-bold block text-[11px] mb-0.5">Officer Feedback:</span>
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
        showToast("✓ Crop submitted! Sent to local Agriculture Officer for verification.", "success");
        closeModal('add-crop-modal');
        document.getElementById('farmer-crop-form').reset();
        loadFarmerDashboard();
      } else {
        const err = await res.json();
        showToast(err.detail || "Submission failed", "error");
      }
    } catch (err) {
      showToast("Network error submitting crop", "error");
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

    if (isOfficer) {
      container.innerHTML = `
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Full Name *</label>
            <input type="text" id="prof-name" required value="${escapeHtml(STATE.user.name)}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Officer Designation *</label>
            <input type="text" id="prof-designation" required value="${escapeHtml(prof.designation || 'Assistant Agricultural Officer')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Department *</label>
            <input type="text" id="prof-department" required value="${escapeHtml(prof.department || 'Department of Agriculture')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Contact Number *</label>
            <input type="text" id="prof-contact" required value="${escapeHtml(prof.contact || STATE.user.phone)}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-3 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Assigned Area / Block *</label>
            <input type="text" id="prof-area" required value="${escapeHtml(prof.assigned_area || 'Sankari')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">District *</label>
            <input type="text" id="prof-district" required value="${escapeHtml(prof.district || 'Salem')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">State *</label>
            <input type="text" id="prof-state" required value="${escapeHtml(prof.state || 'Tamil Nadu')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 mb-1">Official Email</label>
          <input type="email" id="prof-email" value="${escapeHtml(STATE.user.email || '')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
        </div>
      `;
    } else {
      container.innerHTML = `
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Full Name *</label>
            <input type="text" id="prof-name" required value="${escapeHtml(STATE.user.name)}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Village *</label>
            <input type="text" id="prof-f-village" required value="${escapeHtml(prof.village || 'Sankari West')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Area / Block *</label>
            <input type="text" id="prof-area" required value="${escapeHtml(prof.area || 'Sankari')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">District *</label>
            <input type="text" id="prof-district" required value="${escapeHtml(prof.district || 'Salem')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div class="grid grid-cols-3 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">State *</label>
            <input type="text" id="prof-state" required value="${escapeHtml(prof.state || 'Tamil Nadu')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Land Area *</label>
            <input type="number" id="prof-f-land" required step="0.5" value="${prof.land_area || 2}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Land Unit</label>
            <input type="text" id="prof-f-unit" value="${escapeHtml(prof.land_unit || 'Acres')}" class="w-full px-3 py-2 text-sm rounded-lg border border-slate-200">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-600 mb-1">Farming Type</label>
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
        showToast("Profile updated successfully", "success");
        await checkSession();
        navigate(isOfficer ? 'officer-dashboard' : 'farmer-dashboard');
      } else {
        const err = await res.json();
        showToast(err.detail || "Failed to update profile", "error");
      }
    } catch (err) {
      showToast("Network error updating profile", "error");
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
        showToast(`Welcome back, ${data.user.name}!`, 'success');
        await checkSession();
        navigate(data.user.role === 'OFFICER' ? 'officer-dashboard' : 'farmer-dashboard');
      } else {
        const err = await res.json();
        showToast(err.detail || "Invalid login credentials", "error");
      }
    } catch (err) {
      showToast("Network error logging in", "error");
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
      showToast("Please fill in all required fields (Name, Mobile, Password).", "warning");
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
        showToast(`Account created! Welcome, ${data.user.name}.`, 'success');
        await checkSession();
        navigate(data.user.role === 'OFFICER' ? 'officer-dashboard' : 'farmer-dashboard');
      } else {
        const err = await res.json().catch(() => ({}));
        showToast(err.detail || "Registration failed. Please check your details.", "error");
      }
    } catch (err) {
      console.error("Registration error:", err);
      showToast("Network error registering account", "error");
    }
  }

  // -------------------------------------------------------------
  // SIH DEMO BAR HELPERS (Section 22, 24)
  // -------------------------------------------------------------
  async function demoLogin(role) {
    try {
      const res = await fetch('/api/auth/demo-login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ role: role })
      });

      if (res.ok) {
        const data = await res.json();
        STATE.token = data.token;
        STATE.user = data.user;
        localStorage.setItem('agriflow_token', data.token);
        showToast(`Switched to ${role === 'OFFICER' ? 'Officer Ravi Kumar' : 'Farmer Kumar'}`, 'success');
        await checkSession();
        navigate(role === 'OFFICER' ? 'officer-dashboard' : 'farmer-dashboard');
      } else {
        showToast("Demo login failed", "error");
      }
    } catch (e) {
      showToast("Network error in demo login", "error");
    }
  }

  async function resetDemoData() {
    if (!confirm("Reset database to initial demo state (Ravi Kumar & Kumar with sample produce)?")) return;

    try {
      const res = await fetch('/api/auth/reset-demo', { method: 'POST' });
      if (res.ok) {
        showToast("Demo database reset successfully!", "success");
        await checkSession();
        if (STATE.currentView === 'produce') loadProduceList();
        else if (STATE.currentView === 'officer-dashboard') loadOfficerDashboard();
        else if (STATE.currentView === 'farmer-dashboard') loadFarmerDashboard();
      }
    } catch (e) {
      showToast("Failed to reset demo data", "error");
    }
  }

  let isFloaterMinimized = false;
  function toggleDemoFloater() {
    const floater = document.getElementById('demo-floater');
    const icon = document.getElementById('demo-floater-icon');
    isFloaterMinimized = !isFloaterMinimized;
    if (isFloaterMinimized) {
      floater.style.transform = 'translate(-50%, 80%)';
      icon.style.transform = 'rotate(180deg)';
    } else {
      floater.style.transform = 'translate(-50%, 0)';
      icon.style.transform = 'rotate(0deg)';
    }
  }

  // -------------------------------------------------------------
  // UI UTILITIES & TOASTS
  // -------------------------------------------------------------
  function openModal(modalId) {
    const m = document.getElementById(modalId);
    if (m) {
      m.classList.remove('hidden');
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
