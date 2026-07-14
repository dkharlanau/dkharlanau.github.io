(function () {
  const root = document.querySelector('[data-incident-lab]');
  if (!root) return;
  const select = root.querySelector('[data-case-select]');
  const form = root.querySelector('[data-response-form]');
  const result = root.querySelector('[data-evaluation-result]');
  let cases = [];
  const by = (selector) => root.querySelector(selector);
  const lines = (value) => String(value || '').split('\n').map((item) => item.trim()).filter(Boolean);
  const has = (values, expected) => values.some((value) => value.toLowerCase().includes(expected.toLowerCase()));
  const list = (selector, values, render) => {
    const element = by(selector); element.replaceChildren();
    values.forEach((value) => { const item = document.createElement('li'); render(item, value); element.appendChild(item); });
  };
  const current = () => cases.find((item) => item.id === select.value);
  const showCase = () => {
    const item = current(); if (!item) return;
    by('[data-case-meta]').textContent = `${item.domain} · ${item.difficulty}`;
    by('[data-case-title]').textContent = item.title;
    by('[data-case-scenario]').textContent = item.scenario;
    list('[data-case-facts]', item.known_facts, (node, value) => { node.textContent = value; });
    list('[data-case-missing]', item.missing_evidence, (node, value) => { node.textContent = value; });
    list('[data-case-sources]', item.expected_atlas_urls, (node, value) => { const link = document.createElement('a'); link.href = value; link.textContent = value; node.appendChild(link); });
    result.hidden = true;
  };
  const renderResult = (checks) => {
    result.replaceChildren(); result.hidden = false;
    const score = checks.filter((check) => check.passed).length;
    const heading = document.createElement('h2'); heading.textContent = `Loop score: ${score} / ${checks.length}`; result.appendChild(heading);
    const listElement = document.createElement('ul');
    checks.forEach((check) => { const item = document.createElement('li'); item.className = check.passed ? 'incident-lab__pass' : 'incident-lab__fail'; item.textContent = `${check.passed ? 'Pass' : 'Revise'} — ${check.label}`; listElement.appendChild(item); });
    result.appendChild(listElement);
    const next = document.createElement('p');
    next.textContent = score === checks.length ? 'Ready for human review. This result does not authorize any SAP action.' : 'Revise the failed checks, then evaluate again.';
    result.appendChild(next);
  };
  const evaluate = () => {
    const item = current(); const values = Object.fromEntries(new FormData(form));
    const evidence = lines(values.evidence); const refs = lines(values.evidence_refs); const hypotheses = lines(values.hypotheses); const actions = lines(values.proposed_actions);
    const text = [...evidence, ...refs, ...hypotheses, ...actions, values.approval_boundary].join('\n');
    const checks = [
      { label: 'Required evidence', passed: item.required_evidence.every((expected) => has(evidence, expected)) },
      { label: 'Acceptable hypothesis', passed: item.acceptable_hypotheses.some((expected) => has(hypotheses, expected)) },
      { label: 'Expected Atlas sources', passed: item.expected_atlas_urls.every((expected) => refs.some((value) => value === expected || value.endsWith(expected))) },
      { label: 'Forbidden action absent', passed: !item.forbidden_actions.some((expected) => text.toLowerCase().includes(expected.toLowerCase())) },
      { label: 'Human approval boundary', passed: Boolean(values.approval_boundary.trim()) }
    ];
    renderResult(checks);
  };
  fetch('/ai/incident-lab.json').then((response) => response.json()).then((data) => {
    cases = data.cases;
    cases.forEach((item) => { const option = document.createElement('option'); option.value = item.id; option.textContent = `${item.title} (${item.difficulty})`; select.appendChild(option); });
    showCase(); select.addEventListener('change', showCase);
    form.addEventListener('submit', (event) => { event.preventDefault(); evaluate(); });
  }).catch(() => { by('[data-case-title]').textContent = 'Incident Lab data could not be loaded.'; });
}());
