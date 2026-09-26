(() => {
  const article = document.querySelector('.page-context--skill-hub article.atlas-page');
  if (!article) return;

  const norm = (value) => (value || '').trim().toLowerCase();
  const sections = [...article.querySelectorAll(':scope > section')];

  const findSection = (title) =>
    sections.find((section) => norm(section.querySelector(':scope > h2')?.textContent) === norm(title));

  const countDirectItems = (section) =>
    section ? section.querySelectorAll(':scope > ul > li, :scope > ol > li').length : 0;

  const deliverables = countDirectItems(findSection('Deliverables'));
  const decisionRules = countDirectItems(findSection('Decision rules'));
  const templatesSection = findSection('Templates');
  const templates = templatesSection ? templatesSection.querySelectorAll('pre').length : 0;

  const lead = article.querySelector(':scope > .lead');
  if (lead && !article.querySelector(':scope > .skill-summary')) {
    const icons = {
      deliverables: '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 7.5h14v11H5zM8 4.5h8v3H8zM8 11h8M8 14.5h5" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      templates: '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="8" y="7" width="10" height="12" rx="2" stroke-width="1.7"/><path d="M6 16H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v1" stroke-width="1.7" stroke-linecap="round"/></svg>',
      rules: '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 5v5m0 0c0 4 3 4 6 4h6m-12-4c0-4 3-4 6-4h6M15 3l3 3-3 3M15 11l3 3-3 3" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      sections: '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M8 6h11M8 12h11M8 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01" stroke-width="1.9" stroke-linecap="round"/></svg>'
    };

    const metrics = [
      { value: deliverables, label: 'Deliverables', icon: icons.deliverables },
      { value: templates, label: 'Ready-to-copy templates', icon: icons.templates },
      { value: decisionRules, label: 'Decision rules', icon: icons.rules },
      { value: sections.length, label: 'Key sections', icon: icons.sections }
    ].filter((metric) => metric.value > 0);

    if (metrics.length) {
      const summary = document.createElement('div');
      summary.className = 'skill-summary';
      summary.setAttribute('aria-label', 'Skill page summary');
      summary.innerHTML = metrics.map((metric) => `
        <div class="skill-summary__item">
          <span class="skill-summary__icon">${metric.icon}</span>
          <span>
            <strong class="skill-summary__value">${metric.value}</strong>
            <span class="skill-summary__label">${metric.label}</span>
          </span>
        </div>
      `).join('');
      lead.insertAdjacentElement('afterend', summary);
    }
  }

  if (!templatesSection) return;

  const copyIcon = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="8" y="8" width="11" height="11" rx="2" stroke-width="1.7"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2" stroke-width="1.7" stroke-linecap="round"/></svg>';
  const checkIcon = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="m5 12 4 4L19 6" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  const writeClipboard = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    const ok = document.execCommand('copy');
    textarea.remove();
    if (!ok) throw new Error('Copy failed');
  };

  templatesSection.querySelectorAll('pre').forEach((pre, index) => {
    if (pre.closest('.template-snippet')) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'template-snippet';
    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'template-copy';
    button.setAttribute('aria-label', `Copy template ${index + 1}`);
    button.innerHTML = `${copyIcon}<span>Copy</span>`;

    button.addEventListener('click', async () => {
      const text = pre.querySelector('code')?.innerText || pre.innerText;
      try {
        await writeClipboard(text);
        button.dataset.state = 'copied';
        button.innerHTML = `${checkIcon}<span>Copied</span>`;
        window.setTimeout(() => {
          button.dataset.state = '';
          button.innerHTML = `${copyIcon}<span>Copy</span>`;
        }, 1600);
      } catch {
        button.querySelector('span').textContent = 'Copy failed';
        window.setTimeout(() => {
          button.querySelector('span').textContent = 'Copy';
        }, 1800);
      }
    });

    wrapper.appendChild(button);
  });
})();
