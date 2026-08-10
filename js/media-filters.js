(() => {
  const filterBox = document.getElementById('media-filters');
  const items = Array.from(document.querySelectorAll('.media-item'));
  const sections = Array.from(document.querySelectorAll('.media-section'));

  if (!filterBox || !items.length || !sections.length) return;

  const lang = document.documentElement.lang === 'en' ? 'en' : 'es';
  const searchInput = document.getElementById('media-search');
  const yearSelect = document.getElementById('media-year');
  const typeSelect = document.getElementById('media-type');
  const territorySelect = document.getElementById('media-territory');
  const mediumSelect = document.getElementById('media-medium');
  const clearButton = document.getElementById('media-clear');
  const resultCount = document.getElementById('media-result-count');
  const noResults = document.getElementById('media-no-results');

  const normalize = (value = '') => value
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim();

  const labels = {
    es: {
      type: {
        entrevista: 'Entrevista',
        juridico: 'Jurídico',
        television: 'Televisión',
        radio: 'Radio',
        revista: 'Revista',
        agencia: 'Agencia',
        prensa: 'Prensa escrita'
      },
      territory: {
        nacional: 'Nacional',
        'castilla-y-leon': 'Castilla y León',
        euskadi: 'Euskadi',
        navarra: 'Navarra',
        asturias: 'Asturias'
      }
    },
    en: {
      type: {
        entrevista: 'Interview',
        juridico: 'Legal media',
        television: 'Television',
        radio: 'Radio',
        revista: 'Magazine',
        agencia: 'News agency',
        prensa: 'Print press'
      },
      territory: {
        nacional: 'National',
        'castilla-y-leon': 'Castile and León',
        euskadi: 'Basque Country',
        navarra: 'Navarre',
        asturias: 'Asturias'
      }
    }
  };

  items.forEach((item) => {
    item.dataset.searchText = normalize([
      item.textContent,
      item.dataset.medium,
      item.dataset.type,
      item.dataset.territory,
      item.dataset.year
    ].join(' '));
  });

  const uniqueValues = (key) => [...new Set(items.map((item) => item.dataset[key]).filter(Boolean))];

  const populateSelect = (select, values, labelMap = null, sorter = null) => {
    const sorted = sorter ? [...values].sort(sorter) : [...values].sort((a, b) => a.localeCompare(b, lang));
    sorted.forEach((value) => {
      const option = document.createElement('option');
      option.value = value;
      option.textContent = labelMap?.[value] || value;
      select.appendChild(option);
    });
  };

  populateSelect(yearSelect, uniqueValues('year'), null, (a, b) => Number(b) - Number(a));
  populateSelect(typeSelect, uniqueValues('type'), labels[lang].type);
  populateSelect(territorySelect, uniqueValues('territory'), labels[lang].territory);
  populateSelect(mediumSelect, uniqueValues('medium'));

  const params = new URLSearchParams(window.location.search);
  searchInput.value = params.get('q') || '';

  const restoreSelect = (select, key) => {
    const value = params.get(key) || '';
    if ([...select.options].some((option) => option.value === value)) select.value = value;
  };

  restoreSelect(yearSelect, 'year');
  restoreSelect(typeSelect, 'type');
  restoreSelect(territorySelect, 'territory');
  restoreSelect(mediumSelect, 'medium');

  const updateUrl = () => {
    const next = new URLSearchParams();
    const q = searchInput.value.trim();
    if (q) next.set('q', q);
    if (yearSelect.value) next.set('year', yearSelect.value);
    if (typeSelect.value) next.set('type', typeSelect.value);
    if (territorySelect.value) next.set('territory', territorySelect.value);
    if (mediumSelect.value) next.set('medium', mediumSelect.value);

    const query = next.toString();
    const nextUrl = `${window.location.pathname}${query ? `?${query}` : ''}${window.location.hash}`;
    window.history.replaceState(null, '', nextUrl);
  };

  const applyFilters = () => {
    const q = normalize(searchInput.value);
    const year = yearSelect.value;
    const type = typeSelect.value;
    const territory = territorySelect.value;
    const medium = mediumSelect.value;

    let visibleCount = 0;

    items.forEach((item) => {
      const matches = (!q || item.dataset.searchText.includes(q))
        && (!year || item.dataset.year === year)
        && (!type || item.dataset.type === type)
        && (!territory || item.dataset.territory === territory)
        && (!medium || item.dataset.medium === medium);

      item.hidden = !matches;
      if (matches) visibleCount += 1;
    });

    sections.forEach((section) => {
      const hasVisibleItems = Array.from(section.querySelectorAll('.media-item')).some((item) => !item.hidden);
      section.hidden = !hasVisibleItems;
    });

    resultCount.textContent = lang === 'es'
      ? `${visibleCount} ${visibleCount === 1 ? 'resultado' : 'resultados'}`
      : `${visibleCount} ${visibleCount === 1 ? 'result' : 'results'}`;

    noResults.hidden = visibleCount !== 0;
    clearButton.disabled = !q && !year && !type && !territory && !medium;
    updateUrl();
  };

  const clearFilters = () => {
    searchInput.value = '';
    yearSelect.value = '';
    typeSelect.value = '';
    territorySelect.value = '';
    mediumSelect.value = '';
    applyFilters();
    searchInput.focus();
  };

  searchInput.addEventListener('input', applyFilters);
  [yearSelect, typeSelect, territorySelect, mediumSelect].forEach((select) => {
    select.addEventListener('change', applyFilters);
  });
  clearButton.addEventListener('click', clearFilters);

  applyFilters();
})();
