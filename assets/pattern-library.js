/* Progressive enhancement for the SAP Development Pattern Library.
   All rows remain visible when JavaScript is disabled. */
(() => {
  'use strict';
  const search = document.getElementById('pattern-search');
  const family = document.getElementById('pattern-group');
  const status = document.getElementById('pattern-count');
  if (!search || !family || !status) return;

  const rows = Array.from(document.querySelectorAll('[data-pattern-row]'));
  const groups = Array.from(document.querySelectorAll('[data-pattern-group]'));
  const normalize = (text) => String(text || '').toLocaleLowerCase().trim();

  function applyFilters() {
    const words = normalize(search.value).split(/\s+/).filter(Boolean);
    const selectedFamily = family.value;
    let visible = 0;

    rows.forEach((row) => {
      const text = normalize(row.getAttribute('data-pattern-search'));
      const sameFamily = !selectedFamily || row.dataset.patternCategory === selectedFamily;
      const matches = words.every((word) => text.includes(word));
      row.hidden = !(sameFamily && matches);
      if (!row.hidden) visible += 1;
    });

    groups.forEach((section) => {
      const visibleInSection = section.querySelector('[data-pattern-row]:not([hidden])');
      section.hidden = !visibleInSection;
    });

    status.textContent = `${visible} of ${rows.length} patterns shown.`;
  }

  search.addEventListener('input', applyFilters);
  family.addEventListener('change', applyFilters);
  applyFilters();
})();
