(function () {
  const canvas = document.querySelector('[data-service-canvas]');
  if (!canvas) return;

  const services = {
    ams: { kicker: 'AMS reliability', title: 'Stabilise the system your business runs on.', description: 'Start where repeat incidents, slow recovery, and fragile handovers keep absorbing attention.', deliverables: ['Incident-recurrence map', 'Ownership and recovery route', 'Runbook and prevention backlog'], href: '/services/sap-ams-consulting/', link: 'Explore AMS consulting' },
    data: { kicker: 'Master data', title: 'Make data decisions dependable.', description: 'Start where customer, supplier, material, or business-partner defects create repair work downstream.', deliverables: ['Change and consumption map', 'Control and ownership model', 'Data-quality improvement backlog'], href: '/services/sap-master-data-stability-assessment/', link: 'Explore master data stability' },
    logistics: { kicker: 'Logistics & planning', title: 'Turn signals into safe commitments.', description: 'Start where shortages, expedites, and exception queues create urgency without a clear decision path.', deliverables: ['Exception decision map', 'Evidence and approval route', 'Planning-control backlog'], href: '/services/sap-planning-and-replenishment-assessment/', link: 'Explore logistics and planning' },
    integration: { kicker: 'Integration & automation', title: 'Connect what matters. Automate the rest.', description: 'Start where interfaces look healthy until a business flow blocks and manual recovery becomes the process.', deliverables: ['Failure-boundary map', 'Observability and recovery route', 'Automation decision list'], href: '/services/sap-integration-reliability-assessment/', link: 'Explore integration reliability' },
    ai: { kicker: 'Practical AI', title: 'Use AI where it helps. Keep people in control.', description: 'Start with one narrow use case that has usable context, safe checks, and accountable human review.', deliverables: ['Use-case and boundary brief', 'Review and evidence model', 'Controlled delivery plan'], href: '/services/sap-ai-ml-enablement/', link: 'Explore practical AI' }
  };

  const nodes = [...canvas.querySelectorAll('[data-service]')];
  const panel = canvas.querySelector('[data-service-detail]');
  const title = canvas.querySelector('[data-service-title]');
  const kicker = canvas.querySelector('[data-service-kicker]');
  const description = canvas.querySelector('[data-service-description]');
  const deliverables = canvas.querySelector('[data-service-deliverables]');
  const detailLink = canvas.querySelector('[data-service-link]');

  const showService = (key, focusPanel) => {
    const service = services[key];
    if (!service) return;
    nodes.forEach((node) => {
      const active = node.dataset.service === key;
      node.classList.toggle('is-active', active);
      node.setAttribute('aria-selected', String(active));
      node.tabIndex = active ? 0 : -1;
    });
    panel.setAttribute('aria-labelledby', `service-tab-${key}`);
    kicker.textContent = service.kicker;
    title.textContent = service.title;
    description.textContent = service.description;
    deliverables.replaceChildren(...service.deliverables.map((item) => { const li = document.createElement('li'); li.textContent = item; return li; }));
    detailLink.href = service.href;
    detailLink.childNodes[0].textContent = `${service.link} `;
    if (focusPanel) panel.focus({ preventScroll: true });
  };

  nodes.forEach((node, index) => {
    node.tabIndex = index === 0 ? 0 : -1;
    node.addEventListener('click', () => showService(node.dataset.service, false));
    node.addEventListener('keydown', (event) => {
      if (!['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const targetIndex = event.key === 'Home' ? 0 : event.key === 'End' ? nodes.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + nodes.length) % nodes.length;
      nodes[targetIndex].focus();
      showService(nodes[targetIndex].dataset.service, false);
    });
  });

  const inputList = [...canvas.querySelectorAll('[data-constraint-input]')];
  const resultTitle = canvas.querySelector('[data-constraint-title]');
  const resultCopy = canvas.querySelector('[data-constraint-copy]');
  const resultLink = canvas.querySelector('[data-constraint-link]');
  const chooseConstraint = () => {
    const state = Object.fromEntries(inputList.map((input) => [input.name, input.value]));
    const key = state.impact === 'data' ? 'data' : state.impact === 'delivery' ? 'logistics' : state.impact === 'connectivity' || state.manual === 'high' ? 'integration' : state.impact === 'decision' ? 'ai' : 'ams';
    const service = services[key];
    resultTitle.textContent = service.kicker;
    resultCopy.textContent = state.recurrence === 'constant' ? `${service.description} Begin with the repeated pattern that creates the most rework.` : service.description;
    resultLink.href = service.href;
    resultLink.childNodes[0].textContent = `${service.link} `;
    showService(key, false);
  };
  inputList.forEach((input) => input.addEventListener('change', chooseConstraint));

  const revealItems = [...canvas.querySelectorAll('[data-reveal]')];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => entries.forEach((entry) => { if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); } }), { threshold: .12 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }
}());
