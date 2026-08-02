(() => {
  const canvas = document.querySelector('.diagnostics-canvas');
  if (!canvas) return;
  canvas.classList.add('js-enabled');
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
