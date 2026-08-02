(() => {
  const canvas = document.querySelector('.scenario-canvas');
  if (!canvas) return;

  canvas.classList.add('js-enabled');

  const scenarios = {
    data: { kicker: 'Master data', title: 'When a record stops a business process.', detail: 'Trace the record from change through activation, distribution, and business use before treating it as an isolated ticket.', href: '#scenario-data', link: 'See master data scenarios' },
    process: { kicker: 'Process execution', title: 'When the order-to-cash or procure-to-pay route stalls.', detail: 'Start with the blocked document and follow the process, data, configuration, and approval conditions behind it.', href: '#scenario-process', link: 'See process execution scenarios' },
    integration: { kicker: 'Integration', title: 'When the handoff fails between systems.', detail: 'Separate source, mapping, transport, target, monitoring, and recovery ownership before choosing the fix.', href: '#scenario-integration', link: 'See integration scenarios' },
    ams: { kicker: 'AMS cost', title: 'When support work repeats without reducing demand.', detail: 'Group repeat incidents, identify the shared failure condition, and decide what should prevent the next occurrence.', href: '#scenario-ams', link: 'See AMS cost scenarios' },
    ai: { kicker: 'AI use', title: 'When a useful AI use case needs an operating boundary.', detail: 'Begin with a narrow task, usable evidence, deterministic checks, and accountable human review.', href: '#scenario-ai', link: 'See AI use scenarios' },
    architecture: { kicker: 'Architecture', title: 'When the extension model makes change more expensive.', detail: 'Make the customisation, transition debt, and operating consequence visible before choosing the next architecture decision.', href: '#scenario-architecture', link: 'See architecture scenarios' }
  };

  const tabs = [...canvas.querySelectorAll('[data-scenario]')];
  const panel = canvas.querySelector('#scenario-panel');
  const kicker = canvas.querySelector('[data-scenario-kicker]');
  const title = canvas.querySelector('[data-scenario-title]');
  const detail = canvas.querySelector('[data-scenario-detail]');
  const link = canvas.querySelector('[data-scenario-link]');

  const activate = (key) => {
    const scenario = scenarios[key];
    if (!scenario) return;
    tabs.forEach((tab) => {
      const active = tab.dataset.scenario === key;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
    });
    panel?.setAttribute('aria-labelledby', `scenario-tab-${key}`);
    if (kicker) kicker.textContent = scenario.kicker;
    if (title) title.textContent = scenario.title;
    if (detail) detail.textContent = scenario.detail;
    if (link) {
      link.href = scenario.href;
      link.firstChild.textContent = `${scenario.link} `;
    }
  };

  tabs.forEach((tab, index) => {
    tab.tabIndex = index === 0 ? 0 : -1;
    tab.addEventListener('click', () => activate(tab.dataset.scenario));
    tab.addEventListener('keydown', (event) => {
      if (!['ArrowRight', 'ArrowLeft', 'ArrowDown', 'ArrowUp', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const next = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : (index + (event.key === 'ArrowRight' || event.key === 'ArrowDown' ? 1 : -1) + tabs.length) % tabs.length;
      tabs[next].focus();
      activate(tabs[next].dataset.scenario);
    });
  });

  const revealItems = [...canvas.querySelectorAll('[data-reveal]')];
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    revealItems.forEach((item) => item.classList.add('is-visible'));
    return;
  }
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('is-visible');
    observer.unobserve(entry.target);
  }), { threshold: 0.12 });
  revealItems.forEach((item) => observer.observe(item));
})();
