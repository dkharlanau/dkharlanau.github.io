(() => {
  const canvas = document.querySelector('.research-canvas');
  if (!canvas) return;

  const tabs = [...canvas.querySelectorAll('[data-research-target]')];
  const panels = [...canvas.querySelectorAll('.research-panel')];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  canvas.classList.add('js-enabled');

  const selectPanel = (id, focus = false) => {
    tabs.forEach((tab) => {
      const active = tab.dataset.researchTarget === id;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      if (active && focus) tab.focus();
    });
    panels.forEach((panel) => {
      const active = panel.id === id;
      panel.hidden = !active;
      panel.classList.toggle('is-active', active);
    });
  };

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectPanel(tab.dataset.researchTarget));
    tab.addEventListener('keydown', (event) => {
      if (!['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const next = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
      selectPanel(tabs[next].dataset.researchTarget, true);
    });
  });

  const reveals = [...canvas.querySelectorAll('[data-reveal]')];
  if (reduceMotion || !('IntersectionObserver' in window)) {
    reveals.forEach((item) => item.classList.add('is-visible'));
    return;
  }
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('is-visible');
    observer.unobserve(entry.target);
  }), { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  reveals.forEach((item) => observer.observe(item));
})();
