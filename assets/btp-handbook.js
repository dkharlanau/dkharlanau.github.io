/* Progressive enhancement: catalogue, terms and native disclosures work without JS. */
(() => {
  'use strict';
  const root = document.querySelector('.btp-handbook');
  if (!root) return;
  const normalise = value => value.toLocaleLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g, '');
  const resetters = [];

  function registerFilter({ inputId, clearId, countId, selector, noun, kindId, groupSelector }) {
    const input = root.querySelector(`#${inputId}`);
    const clear = root.querySelector(`#${clearId}`);
    const count = root.querySelector(`#${countId}`);
    const tools = input?.closest('.btp-glossary-tools');
    if (!input || !clear || !count || !tools) return;
    const kind = kindId ? root.querySelector(`#${kindId}`) : null;
    const entries = [...root.querySelectorAll(selector)].map(element => ({
      element, text: normalise(element.textContent), kind: element.dataset.kind || ''
    }));
    const groups = groupSelector ? [...root.querySelectorAll(groupSelector)] : [];
    const filter = () => {
      const words = normalise(input.value.trim()).split(/\s+/).filter(Boolean);
      let visible = 0;
      for (const entry of entries) {
        const match = (!kind?.value || entry.kind === kind.value) && words.every(word => entry.text.includes(word));
        entry.element.hidden = !match;
        if (match) visible++;
      }
      for (const group of groups) {
        group.hidden = !entries.some(entry => !entry.element.hidden && group.contains(entry.element));
        if (!group.hidden && (words.length || kind?.value)) group.open = true;
      }
      count.textContent = `${visible} of ${entries.length} ${noun} shown.${visible ? '' : ' Clear the filters or try another term.'}`;
    };
    const reset = () => { input.value = ''; if (kind) kind.value = ''; filter(); };
    tools.hidden = false;
    input.addEventListener('input', filter);
    kind?.addEventListener('change', filter);
    clear.addEventListener('click', () => { reset(); input.focus(); });
    resetters.push({ selector, reset });
    filter();
  }

  registerFilter({ inputId: 'btp-term-search', clearId: 'btp-term-clear', countId: 'btp-term-count', selector: '.btp-term', noun: 'terms' });
  registerFilter({ inputId: 'btp-service-search', clearId: 'btp-service-clear', countId: 'btp-service-count', selector: '.btp-service-row', noun: 'entries', kindId: 'btp-service-kind', groupSelector: '.btp-catalogue-group' });

  function reveal(hash, scroll = true) {
    let id;
    try { id = decodeURIComponent(hash.replace(/^#/, '')); } catch { return; }
    const target = document.getElementById(id);
    if (!target || !root.contains(target)) return;
    for (const filter of resetters) {
      const entry = target.closest(filter.selector);
      if (entry && (entry.hidden || entry.closest('.btp-catalogue-group')?.hidden)) filter.reset();
    }
    for (let node = target; node && node !== root; node = node.parentElement) {
      if (node.tagName === 'DETAILS') node.open = true;
    }
    if (scroll) requestAnimationFrame(() => target.scrollIntoView());
  }
  root.addEventListener('click', event => {
    const anchor = event.target.closest?.('a[href^="#"]');
    if (anchor) reveal(anchor.getAttribute('href'), false);
  });
  window.addEventListener('hashchange', () => reveal(location.hash));
  if (location.hash) reveal(location.hash);

  let printState = null;
  window.addEventListener('beforeprint', () => {
    if (printState) return;
    printState = {
      details: [...root.querySelectorAll('details')].map(element => [element, element.open]),
      hidden: [...root.querySelectorAll('.btp-term[hidden], .btp-service-row[hidden], .btp-catalogue-group[hidden]')]
    };
    printState.details.forEach(([element]) => { element.open = true; });
    printState.hidden.forEach(element => { element.hidden = false; });
  });
  window.addEventListener('afterprint', () => {
    if (!printState) return;
    printState.details.forEach(([element, open]) => { element.open = open; });
    printState.hidden.forEach(element => { element.hidden = true; });
    printState = null;
  });
})();
