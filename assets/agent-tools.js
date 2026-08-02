(function () {
  const root = document.querySelector('[data-agent-tools]');
  if (!root) return;
  const form = root.querySelector('form');
  const list = root.querySelector('[data-tool-list]');
  const count = root.querySelector('[data-tool-count]');
  const esc = (v) => String(v).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  fetch('/ai/agent-tools.json').then(r => r.json()).then(data => {
    const render = () => {
      const values = Object.fromEntries(new FormData(form));
      const q = (values.q || '').toLowerCase().trim();
      const tools = data.tools.filter(t => {
        const haystack = [t.name, t.status, ...t.domains, ...t.capabilities, t.assessment].join(' ').toLowerCase();
        return (!q || haystack.includes(q)) && (!values.status || t.status === values.status) && (!values.domain || t.domains.includes(values.domain)) && (!values.access || t.access === values.access) && (!values.deployment || t.deployment === values.deployment) && (!values.maturity || t.maturity === values.maturity);
      });
      count.textContent = `${tools.length} of ${data.count} tools`;
      list.innerHTML = tools.map(t => `<article class="agent-tool-card"><header><p class="agent-tool-card__state">${esc(t.status)} · ${esc(t.maturity)} · ${esc(t.access)}</p><h3><a href="${esc(t.repository_url)}" target="_blank" rel="noopener noreferrer">${esc(t.name)} <span aria-hidden="true">↗</span></a></h3></header><p class="agent-tool-card__assessment">${esc(t.assessment)}</p><dl class="agent-tool-card__meta"><div><dt>Domains</dt><dd>${esc(t.domains.join(', '))}</dd></div><div><dt>Transport</dt><dd>${esc(t.transport)} · ${esc(t.deployment)}</dd></div><div><dt>Risk</dt><dd>Credentials ${esc(t.credential_risk)} · system modification ${esc(t.system_modification_risk)}</dd></div></dl></article>`).join('') || '<p class="agent-tool-empty">No tools match these filters.</p>';
    };
    form.addEventListener('input', render); form.addEventListener('change', render); render();
  }).catch(() => { list.innerHTML = '<p>The static tool index could not be loaded.</p>'; });
}());
