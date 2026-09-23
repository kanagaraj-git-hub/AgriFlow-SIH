window.AgriFlowI18n = (() => {
  const FALLBACK_LOCALE = 'en';
  const STORAGE_KEY = 'agriflow_language';
  const RTL_LANGS = new Set(['ur', 'sd']);

  function getLocaleData() {
    return window.AgriFlowLocaleData || {};
  }

  function deepGet(obj, path) {
    if (!obj || !path) return undefined;
    return path.split('.').reduce((current, key) => (current && current[key] !== undefined ? current[key] : undefined), obj);
  }

  function resolveLocale(locale) {
    const locales = getLocaleData();
    return locales[locale] ? locale : FALLBACK_LOCALE;
  }

  function getActiveLocale() {
    const stored = localStorage.getItem(STORAGE_KEY);
    return stored && getLocaleData()[stored] ? stored : FALLBACK_LOCALE;
  }

  function getLocaleMeta(locale = getActiveLocale()) {
    const locales = getLocaleData();
    const selected = locales[locale] || locales[FALLBACK_LOCALE];
    return selected?.lang || locales[FALLBACK_LOCALE].lang;
  }

  function getLanguageOptions() {
    return Object.entries(getLocaleData()).map(([code, value]) => ({
      code,
      name: value.lang.nativeName,
      label: `${value.lang.nativeName}`
    }));
  }

  function formatString(template, params = {}) {
    if (!template) return '';
    return template.replace(/\{\{\s*(\w+)\s*\}\}/g, (_, key) => params[key] ?? '');
  }

  const KEY_ALIASES = {
    'badge_verified': 'produce.verifiedBadge',
    'avail_qty': 'produce.availableQuantity',
    'availability': 'produce.availability',
    'btn_contact_seller': 'produce.contactSeller',
    'contact_seller': 'produce.contactSeller',
    'view_details': 'common.viewDetails',
    'viewDetails': 'common.viewDetails',
    'view_product': 'produce.viewProduct',
    'viewProduct': 'produce.viewProduct',
    'verified_by_officer': 'produce.verifiedByOfficer',
    'verifiedByOfficer': 'produce.verifiedByOfficer',
    'assistant_agri_officer': 'produce.assistantAgriOfficer',
    'assistantAgriOfficer': 'produce.assistantAgriOfficer',
    'assigned_jurisdiction': 'produce.assignedJurisdiction',
    'assignedJurisdiction': 'produce.assignedJurisdiction',
    'grade': 'produce.grade',
    'category': 'produce.category',
    'crop': 'common.crop',
    'quantity': 'common.quantity',
    'unit': 'produce.unitLabel',
    'price': 'produce.price',
    'state': 'common.state',
    'district': 'common.district',
    'area': 'common.area'
  };

  function resolveKeyPath(key) {
    if (!key) return '';
    if (KEY_ALIASES[key]) return KEY_ALIASES[key];
    return key;
  }

  function t(key, params = {}, localeOverride, defaultFallback) {
    if (!key) return defaultFallback !== undefined ? defaultFallback : '';
    const locales = getLocaleData();
    const locale = localeOverride || getActiveLocale();
    const selected = locales[resolveLocale(locale)] || locales[FALLBACK_LOCALE];
    const fallback = locales[FALLBACK_LOCALE];

    const actualKey = resolveKeyPath(key);
    let value = deepGet(selected, actualKey);

    // If not found by full path, try in produce or common if single token
    if (value === undefined || value === null) {
      if (!actualKey.includes('.')) {
        value = deepGet(selected, `produce.${actualKey}`) ?? deepGet(selected, `common.${actualKey}`);
      }
    }

    // Try fallback locale (en)
    if (value === undefined || value === null) {
      value = deepGet(fallback, actualKey);
      if ((value === undefined || value === null) && !actualKey.includes('.')) {
        value = deepGet(fallback, `produce.${actualKey}`) ?? deepGet(fallback, `common.${actualKey}`);
      }
    }

    if (value === undefined || value === null) {
      if (defaultFallback !== undefined) {
        return defaultFallback;
      }
      return key;
    }

    if (typeof value === 'string') {
      return formatString(value, params);
    }

    return value;
  }

  function setDocumentDirection(locale = getActiveLocale()) {
    const isRtl = RTL_LANGS.has(locale);
    document.documentElement.lang = locale;
    document.documentElement.dir = isRtl ? 'rtl' : 'ltr';
  }

  function applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      const value = t(key);
      if (value && value !== key) {
        el.textContent = value;
      }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
      const key = el.getAttribute('data-i18n-placeholder');
      const value = t(key);
      if (value && value !== key) {
        el.setAttribute('placeholder', value);
      }
    });

    document.querySelectorAll('[data-i18n-aria]').forEach((el) => {
      const key = el.getAttribute('data-i18n-aria');
      const value = t(key);
      if (value && value !== key) {
        el.setAttribute('aria-label', value);
      }
    });

    document.querySelectorAll('[data-i18n-title]').forEach((el) => {
      const key = el.getAttribute('data-i18n-title');
      const value = t(key);
      if (value && value !== key) {
        el.setAttribute('title', value);
      }
    });

    const selector = document.getElementById('language-selector');
    if (selector) {
      selector.value = getActiveLocale();
    }
  }

  function setLocale(locale) {
    const locales = getLocaleData();
    if (!locales[locale]) return;
    localStorage.setItem(STORAGE_KEY, locale);
    setDocumentDirection(locale);
    applyTranslations();
    if (typeof window.refreshTranslatedUi === 'function') {
      window.refreshTranslatedUi();
    }
  }

  function initLanguageSelector() {
    const selector = document.getElementById('language-selector');
    if (!selector) return;

    selector.innerHTML = Object.entries(getLocaleData()).map(([code, lang]) =>
      `<option value="${code}">${lang.lang.nativeName}</option>`
    ).join('');
    selector.value = getActiveLocale();
    selector.setAttribute('aria-label', t('common.language'));
    selector.addEventListener('change', (event) => {
      setLocale(event.target.value);
    });
  }

  function validateLocaleStructure() {
    const locales = getLocaleData();
    const baseKeys = JSON.stringify(Object.keys(locales.en || {}));
    Object.entries(locales).forEach(([code, locale]) => {
      if (code === 'en') return;
      if (JSON.stringify(Object.keys(locale)) !== baseKeys) {
        console.warn(`Locale structure mismatch for ${code}`);
      }
    });
  }

  function init() {
    setDocumentDirection(getActiveLocale());
    initLanguageSelector();
    applyTranslations();
    validateLocaleStructure();
  }

  return {
    t,
    setLocale,
    init,
    getActiveLocale,
    applyTranslations,
    getLocaleMeta,
    getLanguageOptions
  };
})();

// Centralized global t(...) function
window.t = (key, params, localeOverride, defaultFallback) => window.AgriFlowI18n ? window.AgriFlowI18n.t(key, params, localeOverride, defaultFallback) : (defaultFallback || key);

