/* Present existing text sequences as reading diagrams without changing their words. */
(() => {
  'use strict';
  function sequenceSteps(text, language = '') {
    if (language && !['text', 'plaintext'].includes(language)) return null;
    const normalised = ['text', 'plaintext'].includes(language) ? text.replace(/\s+->\s+/g, ' → ') : text;
    const lines = normalised.trim().split(/\r?\n/).map(line => line.trim()).filter(Boolean);
    let steps;
    if (lines.length === 1) {
      if (!lines[0].includes('→')) return null;
      steps = lines[0].split(/\s*→\s*/);
    } else {
      if (!lines.slice(1).every(line => /^→\s+/.test(line))) return null;
      if (/^→/.test(lines[0])) return null;
      steps = [lines[0], ...lines.slice(1).map(line => line.replace(/^→\s+/, ''))];
    }
    if (steps.length < 3 || steps.length > 12) return null;
    // Leave branches, commands and multi-part notation in their original form.
    if (steps.some(step => !step || step.length > 100 || /[{}<>|=;`]|→|->|\t/.test(step))) return null;
    return steps;
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {sequenceSteps};
  if (typeof document === 'undefined') return;

  function enhance() {
    document.querySelectorAll('#content pre').forEach(pre => {
      if (pre.closest('.study-original') || pre.dataset.studyDiagram) return;
      const code = pre.querySelector('code');
      const languageClass = [code?.className || '', pre.closest('[class*="language-"]')?.className || ''].join(' ').match(/language-([\w-]+)/);
      const steps = sequenceSteps(code?.textContent || pre.textContent, languageClass?.[1] || '');
      if (!steps) return;
      pre.dataset.studyDiagram = 'true';
      const figure = document.createElement('figure');
      figure.className = 'study-sequence';
      const caption = document.createElement('figcaption');
      caption.textContent = 'Trace the sequence';
      const list = document.createElement('ol');
      steps.forEach(text => {
        const item = document.createElement('li');
        item.textContent = text;
        list.append(item);
      });
      const original = document.createElement('details');
      original.className = 'study-original';
      const summary = document.createElement('summary');
      summary.textContent = 'Original text sequence';
      original.append(summary);
      const originalBlock = pre.closest('.highlighter-rouge') || pre;
      originalBlock.before(figure);
      figure.append(caption, list, original);
      original.append(originalBlock);
    });
    document.querySelectorAll('#content table').forEach((table, index) => {
      if (table.closest('.study-table-scroll') || table.closest('[role="region"]')) return;
      if (getComputedStyle(table.parentElement).overflowX === 'auto') return;
      const wrapper = document.createElement('div');
      wrapper.className = 'study-table-scroll';
      wrapper.tabIndex = 0;
      wrapper.setAttribute('role', 'region');
      const caption = table.querySelector('caption')?.textContent.trim();
      wrapper.setAttribute('aria-label', caption || `Comparison table ${index + 1}; scroll horizontally if needed`);
      table.before(wrapper);
      wrapper.append(table);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', enhance, {once: true});
  else enhance();
})();
