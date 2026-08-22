(() => {
  const header = document.querySelector("[data-site-header]");
  const toggle = header?.querySelector(".site-nav__toggle");
  const toggleLabel = toggle?.querySelector(".site-nav__toggle-label");
  const navigation = header?.querySelector(".nav-links");

  if (header) {
    const focusableMenuItems = () => navigation
      ? [...navigation.querySelectorAll("a[href], button:not([disabled]), summary")]
      : [];
    const setMenu = (open) => {
      header.classList.toggle("site-header--menu-open", open);
      document.documentElement.classList.toggle("site-menu-open", open);
      toggle?.setAttribute("aria-expanded", String(open));
      if (toggleLabel) toggleLabel.textContent = open
        ? (toggle?.dataset.closeLabel || "Close")
        : (toggle?.dataset.menuLabel || "Menu");
    };
    const closeMenu = () => setMenu(false);

    const updateHeader = () => header.classList.toggle("site-header--scrolled", window.scrollY > 12);
    window.addEventListener("scroll", updateHeader, { passive: true });
    updateHeader();

    toggle?.addEventListener("click", () => {
      const open = !header.classList.contains("site-header--menu-open");
      setMenu(open);
      if (open) window.requestAnimationFrame(() => focusableMenuItems()[0]?.focus());
    });
    navigation?.addEventListener("click", (event) => {
      if (event.target.closest("a")) closeMenu();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeMenu();
        toggle?.focus();
        return;
      }
      if (event.key !== "Tab" || !header.classList.contains("site-header--menu-open")) return;
      const items = focusableMenuItems();
      if (!items.length) return;
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        toggle?.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        toggle?.focus();
      } else if (document.activeElement === toggle && event.shiftKey) {
        event.preventDefault();
        last.focus();
      } else if (document.activeElement === toggle) {
        event.preventDefault();
        first.focus();
      }
    });
    document.addEventListener("click", (event) => {
      if (header.classList.contains("site-header--menu-open") && !header.contains(event.target)) closeMenu();
    });
    const mobileMenu = window.matchMedia("(max-width: 1100px)");
    const closeOnDesktop = (event) => { if (!event.matches) closeMenu(); };
    if (mobileMenu.addEventListener) mobileMenu.addEventListener("change", closeOnDesktop);
    else mobileMenu.addListener(closeOnDesktop);
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

(() => {
  const root = document.querySelector("[data-intent-brief]");
  if (!root) return;

  const sections = [...root.querySelectorAll("[data-intent-reveal]")];
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) {
    sections.forEach((section) => section.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add("is-visible");
    observer.unobserve(entry.target);
  }), { threshold: 0.08 });

  sections.forEach((section) => observer.observe(section));
})();

(() => {
  const root = document.querySelector("[data-evidence-canvas]");
  if (!root) return;

  const buttons = [...root.querySelectorAll("[data-evidence-filter]")];
  const records = [...root.querySelectorAll("[data-evidence-record]")];
  const status = root.querySelector("[data-evidence-status]");
  const show = (category) => {
    let count = 0;
    records.forEach((record) => {
      const visible = category === "all" || record.dataset.evidenceCategory === category;
      record.hidden = !visible;
      if (visible) count += 1;
    });
    buttons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.evidenceFilter === category)));
    if (status) status.textContent = `${count} ${count === 1 ? "record" : "records"} shown`;
  };

  buttons.forEach((button) => button.addEventListener("click", () => show(button.dataset.evidenceFilter)));

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const reveal = [...root.querySelectorAll(".evidence-canvas__hero, .evidence-canvas__section")];
  if (!("IntersectionObserver" in window)) { reveal.forEach((item) => item.classList.add("is-visible")); return; }
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) { entry.target.classList.add("is-visible"); observer.unobserve(entry.target); }
  }), { threshold: .08 });
  reveal.forEach((item) => { item.dataset.reveal = ""; observer.observe(item); });
})();

(() => {
  const root = document.querySelector("[data-learning-timeline]");
  if (!root) return;
  const buttons = [...root.querySelectorAll("[data-learning-filter]")];
  const records = [...root.querySelectorAll("[data-learning-item]")];
  const status = root.querySelector("[data-learning-status]");
  const setFilter = (kind) => {
    let count = 0;
    records.forEach((record) => {
      const visible = kind === "all" || record.dataset.kind === kind;
      record.hidden = !visible;
      if (visible) count += 1;
    });
    buttons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.learningFilter === kind)));
    if (status) status.textContent = `${count} ${count === 1 ? "record" : "records"} shown`;
  };
  buttons.forEach((button) => button.addEventListener("click", () => setFilter(button.dataset.learningFilter)));
})();
