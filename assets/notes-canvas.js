(() => {
  const canvas = document.querySelector('.notes-canvas');
  if (!canvas) return;
  const sections = [...canvas.querySelectorAll('[data-reveal]')];
  canvas.classList.add('js-enabled');
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    sections.forEach((section) => section.classList.add('is-visible'));
    return;
  }
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('is-visible');
    observer.unobserve(entry.target);
  }), { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  sections.forEach((section) => observer.observe(section));
})();
