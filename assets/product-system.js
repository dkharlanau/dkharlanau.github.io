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
    const disclosure = switcher.matches("details") ? switcher : switcher.querySelector("details");
    document.addEventListener("click", (event) => {
      if (disclosure?.open && !switcher.contains(event.target)) disclosure.open = false;
    });
  });

  document.querySelectorAll("[data-atlas-pathfinder]").forEach((root) => {
    const steps = [...root.querySelectorAll("[data-path-target]")];
    const panels = [...root.querySelectorAll("[data-path-panel]")];
    const tabList = root.querySelector("[data-path-tabs]");
    if (!steps.length || !tabList || steps.some((step) => !panels.some((panel) => panel.id === step.dataset.pathTarget))) return;

    // The source is a complete set of anchor links and visible routes. Tabs are
    // an enhancement; a missing script never hides the method or its template.
    tabList.setAttribute("role", "tablist");
    steps.forEach((step) => {
      step.setAttribute("role", "tab");
      step.setAttribute("aria-controls", step.dataset.pathTarget);
    });
    panels.forEach((panel) => {
      panel.setAttribute("role", "tabpanel");
      panel.setAttribute("aria-labelledby", steps.find((step) => step.dataset.pathTarget === panel.id).id);
      panel.tabIndex = 0;
    });

    const activate = (step) => {
      steps.forEach((item) => {
        const active = item === step;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-selected", String(active));
        item.tabIndex = active ? 0 : -1;
      });
      panels.forEach((panel) => { panel.hidden = panel.id !== step.dataset.pathTarget; });
    };

    steps.forEach((step, index) => {
      step.addEventListener("click", (event) => {
        event.preventDefault();
        activate(step);
      });
      step.addEventListener("keydown", (event) => {
        if (event.key === ' ') {
          event.preventDefault();
          activate(step);
          return;
        }
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
    const showLinkedRoute = () => {
      const linkedStep = steps.find((step) => step.getAttribute("href") === window.location.hash);
      if (linkedStep) activate(linkedStep);
      return linkedStep;
    };
    if (!showLinkedRoute()) activate(steps[0]);
    window.addEventListener("hashchange", showLinkedRoute);
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
