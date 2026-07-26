(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll("[data-op-flow]").forEach((root) => {
    const steps = [...root.querySelectorAll("[data-flow-step]")];
    const title = root.querySelector("[data-flow-title]");
    const detail = root.querySelector("[data-flow-detail]");
    let activeIndex = 0;
    let timer;

    const activate = (index) => {
      activeIndex = index;
      steps.forEach((step, stepIndex) => {
        const active = stepIndex === index;
        step.classList.toggle("is-active", active);
        step.setAttribute("aria-pressed", String(active));
      });
      if (title) title.textContent = steps[index].dataset.title;
      if (detail) detail.textContent = steps[index].dataset.detail;
    };

    const stop = () => window.clearInterval(timer);
    const start = () => {
      stop();
      if (!reduceMotion && steps.length > 1) timer = window.setInterval(() => activate((activeIndex + 1) % steps.length), 4600);
    };

    steps.forEach((step, index) => step.addEventListener("click", () => {
      activate(index);
      start();
    }));
    root.addEventListener("mouseenter", stop);
    root.addEventListener("mouseleave", start);
    root.addEventListener("focusin", stop);
    root.addEventListener("focusout", start);
    start();
  });

  document.querySelectorAll("[data-incident-calculator]").forEach((root) => {
    const controls = [...root.querySelectorAll("[data-calc]")];
    const output = (name) => root.querySelector(`[data-result="${name}"]`);
    const numberValue = (name) => {
      const control = root.querySelector(`[data-calc="${name}"]`);
      return Math.max(0, Number(control?.value) || 0);
    };

    const update = () => {
      const incidents = numberValue("incidents");
      const people = numberValue("people");
      const minutes = numberValue("minutes");
      const businessRate = numberValue("businessRate");
      const supportHours = numberValue("supportHours");
      const supportRate = numberValue("supportRate");
      const repeatShare = Math.min(100, numberValue("repeatShare")) / 100;
      const improvement = Math.min(100, numberValue("improvement")) / 100;
      const currency = root.querySelector('[data-calc="currency"]')?.value || "EUR";
      const locale = document.documentElement.lang || "en";
      const annualIncidents = incidents * 12;
      const businessHours = people * (minutes / 60);
      const costPerIncident = (businessHours * businessRate) + (supportHours * supportRate);
      const repeatExposure = annualIncidents * costPerIncident * repeatShare;
      const addressableValue = repeatExposure * improvement;
      const hoursRecovered = annualIncidents * (businessHours + supportHours) * repeatShare * improvement;
      const money = new Intl.NumberFormat(locale, { style: "currency", currency, maximumFractionDigits: 0 });
      const number = new Intl.NumberFormat(locale, { maximumFractionDigits: 0 });

      output("annualIncidents").textContent = number.format(annualIncidents);
      output("repeatExposure").textContent = money.format(repeatExposure);
      output("addressableValue").textContent = money.format(addressableValue);
      output("hoursRecovered").textContent = number.format(hoursRecovered);
    };

    controls.forEach((control) => control.addEventListener("input", update));
    controls.forEach((control) => control.addEventListener("change", update));
    update();
  });

  const revealItems = [...document.querySelectorAll("[data-reveal]")];
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  } else {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8%", threshold: 0.08 });
    revealItems.forEach((item) => revealObserver.observe(item));
  }
})();
