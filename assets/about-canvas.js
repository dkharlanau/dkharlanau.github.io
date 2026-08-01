(() => {
  const canvas = document.querySelector('.profile-canvas');
  if (!canvas) return;

  const items = [...canvas.querySelectorAll(':scope > [data-reveal]')];
  canvas.classList.add('js-enabled');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (reduceMotion || !('IntersectionObserver' in window)) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });

  items.forEach((item) => observer.observe(item));
})();
