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
      list.innerHTML = tools.map(t => `<article class="agent-tool-card"><p class="eyebrow">${esc(t.status)} · ${esc(t.maturity)} · ${esc(t.access)}</p><h2><a href="${esc(t.repository_url)}">${esc(t.name)}</a></h2><p>${esc(t.assessment)}</p><p class="agent-tool-meta"><strong>Domains:</strong> ${esc(t.domains.join(', '))}<br><strong>Transport:</strong> ${esc(t.transport)} · ${esc(t.deployment)}<br><strong>Risk:</strong> credentials ${esc(t.credential_risk)}, system modification ${esc(t.system_modification_risk)}<br><strong>Verified:</strong> ${esc(t.verification_date)}</p></article>`).join('') || '<p>No tools match these filters.</p>';
    };
    form.addEventListener('input', render); form.addEventListener('change', render); render();
  }).catch(() => { list.innerHTML = '<p>The static tool index could not be loaded.</p>'; });
}());
