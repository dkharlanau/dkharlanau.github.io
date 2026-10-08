/* Progressive enhancement only: all terms and native disclosures work without JS. */
(() => {
  'use strict';
  const root = document.querySelector('.btp-handbook');
  if (!root) return;
  const input = root.querySelector('#btp-term-search');
  const tools = root.querySelector('.btp-glossary-tools');
  const terms = [...root.querySelectorAll('.btp-term')];
  const count = root.querySelector('#btp-term-count');
  const clear = root.querySelector('#btp-term-clear');
  if (input && tools && count && clear) {
    const normalize = value => value.toLocaleLowerCase().normalize('NFKD');
    const index = terms.map(element => ({ element, text: normalize(element.textContent) }));
    const filter = () => {
      const words = normalize(input.value.trim()).split(/\s+/).filter(Boolean);
      let visible = 0;
      for (const entry of index) {
        const match = words.every(word => entry.text.includes(word));
        entry.element.hidden = !match;
        if (match) visible++;
      }
      count.textContent = `${visible} of ${terms.length} terms shown.`;
    };
    tools.hidden = false;
    input.addEventListener('input', filter);
    clear.addEventListener('click', () => { input.value = ''; filter(); input.focus(); });
    filter();
    const revealLinkedTerm = () => {
      let id = '';
      try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
      if (id.startsWith('term-')) {
        const term = document.getElementById(id);
        if (term && term.hidden) { input.value = ''; filter(); term.scrollIntoView(); }
      }
    };
    window.addEventListener('hashchange', revealLinkedTerm);
    revealLinkedTerm();
  }
  let priorOpen = [];
  window.addEventListener('beforeprint', () => {
    priorOpen = [...root.querySelectorAll('details')].map(el => [el, el.open]);
    priorOpen.forEach(([el]) => { el.open = true; });
  });
  window.addEventListener('afterprint', () => {
    priorOpen.forEach(([el, open]) => { el.open = open; });
  });
})();
