(() => {
  const header = document.querySelector("[data-site-header]");
  const toggle = header?.querySelector(".site-nav__toggle");
  const navigation = header?.querySelector(".nav-links");

  if (header) {
    const closeMenu = () => {
      header.classList.remove("site-header--menu-open");
      toggle?.setAttribute("aria-expanded", "false");
    };

    const updateHeader = () => header.classList.toggle("site-header--scrolled", window.scrollY > 12);
    window.addEventListener("scroll", updateHeader, { passive: true });
    updateHeader();

    toggle?.addEventListener("click", () => {
      const open = header.classList.toggle("site-header--menu-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    navigation?.addEventListener("click", (event) => {
      if (event.target.closest("a")) closeMenu();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeMenu();
        toggle?.focus();
      }
    });
    document.addEventListener("click", (event) => {
      if (header.classList.contains("site-header--menu-open") && !header.contains(event.target)) closeMenu();
    });
  }

  document.querySelectorAll(".home-language-switcher, .hc-langs").forEach((switcher) => {
    document.addEventListener("click", (event) => {
      if (switcher.open && !switcher.contains(event.target)) switcher.open = false;
    });
  });

  document.querySelectorAll("[data-atlas-pathfinder]").forEach((root) => {
    const steps = [...root.querySelectorAll("[data-path-title]")];
    const outputIcon = root.querySelector("[data-path-output-icon]");
    const outputTitle = root.querySelector("[data-path-output-title]");
    const outputDetail = root.querySelector("[data-path-output-detail]");
    const outputLink = root.querySelector("[data-path-output-link]");
    const outputPanel = root.querySelector("[role='tabpanel']");

    const activate = (step) => {
      steps.forEach((item) => {
        const active = item === step;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-selected", String(active));
        item.tabIndex = active ? 0 : -1;
      });
      if (outputIcon) outputIcon.textContent = step.dataset.pathIcon;
      if (outputTitle) outputTitle.textContent = step.dataset.pathTitle;
      if (outputDetail) outputDetail.textContent = step.dataset.pathDetail;
      if (outputPanel) outputPanel.setAttribute("aria-labelledby", step.id);
      if (outputLink) {
        outputLink.href = step.dataset.pathLink;
        outputLink.firstChild.textContent = `${step.dataset.pathLinkLabel} `;
      }
    };

    steps.forEach((step, index) => {
      step.tabIndex = index === 0 ? 0 : -1;
      step.addEventListener("click", () => activate(step));
      step.addEventListener("keydown", (event) => {
        if (!['ArrowDown', 'ArrowRight', 'ArrowUp', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
        event.preventDefault();
        let targetIndex = index;
        if (event.key === 'Home') targetIndex = 0;
        else if (event.key === 'End') targetIndex = steps.length - 1;
        else targetIndex = (index + (event.key === 'ArrowDown' || event.key === 'ArrowRight' ? 1 : -1) + steps.length) % steps.length;
        steps[targetIndex].focus();
        activate(steps[targetIndex]);
      });
    });
  });
})();
