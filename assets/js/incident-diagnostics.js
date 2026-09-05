(() => {
  'use strict';

  const root = document.querySelector('[data-incident-diagnostics]');
  if (!root) return;

  const endpoints = {
    cases: '/datasets/incident-lab/cases.json',
    templates: '/labs/templates/data/catalog.json',
    atlas: '/atlas/manifest.json'
  };

  const packs = {
    idoc: {
      label: 'IDoc / integration failure',
      caseIds: ['idoc-status-51-vendor-master', 'qrfc-queue-blocked'],
      templateIds: ['incident-triage', 'integration-failure-analysis', 'root-cause-analysis'],
      searchTerms: ['idoc', 'interface', 'integration', 'qrfc', 'trfc', 'message'],
      defaultChecks: [
        'Capture the complete status or queue history before retrying.',
        'Confirm the business object and affected scope, not only the technical message status.',
        'Separate source, transport, target processing, and recovery ownership.',
        'Check duplicate, ordering, and idempotency risk before reprocessing.'
      ]
    },
    bp: {
      label: 'Business Partner / MDG replication',
      caseIds: ['business-partner-replication-gap'],
      templateIds: ['incident-triage', 'process-deviation-analysis', 'root-cause-analysis'],
      searchTerms: ['business partner', 'mdg', 'replication', 'cvi', 'customer', 'vendor', 'supplier'],
      defaultChecks: [
        'Trace approval, activation, outbound replication, transport, and target validation as separate states.',
        'Confirm the affected role, view, and organizational extension before changing data.',
        'Separate data-governance ownership from integration transport ownership.',
        'Do not mass-correct or reprocess until the failing boundary is known.'
      ]
    },
    recurring: {
      label: 'Recurring AMS incident',
      caseIds: [],
      templateIds: ['incident-triage', 'root-cause-analysis', 'procedure-runbook'],
      searchTerms: ['incident', 'root cause', 'support', 'ams', 'recurring', 'operational memory'],
      defaultChecks: [
        'Compare one failing object with one known-good object.',
        'Separate containment from root cause, correction, and prevention.',
        'Record recurrence frequency, affected scope, and recent changes.',
        'Close only after a business outcome is validated and a recurrence signal is defined.'
      ]
    }
  };

  const state = {
    data: { cases: [], templates: [], atlas: [] },
    outputs: {},
    fileText: ''
  };

  const els = {
    status: root.querySelector('[data-source-status]'),
    pack: root.querySelector('[data-pack]'),
    title: root.querySelector('[data-case-title]'),
    impact: root.querySelector('[data-impact]'),
    evidence: root.querySelector('[data-evidence]'),
    file: root.querySelector('[data-file]'),
    fileMeta: root.querySelector('[data-file-meta]'),
    analyze: root.querySelector('[data-analyze]'),
    reset: root.querySelector('[data-reset]'),
    summary: root.querySelector('[data-analysis-summary]'),
    references: root.querySelector('[data-references]'),
    output: root.querySelector('[data-output]'),
    outputTabs: Array.from(root.querySelectorAll('[data-output-tab]')),
    copy: root.querySelector('[data-copy]'),
    download: root.querySelector('[data-download]')
  };

  const escapeHtml = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');

  const normalize = (value) => String(value ?? '').replace(/\s+/g, ' ').trim();
  const bulletList = (items, empty = '- Not provided') => items.length ? items.map((item) => `- ${item}`).join('\n') : empty;

  async function loadJson(url) {
    const response = await fetch(url, { credentials: 'same-origin' });
    if (!response.ok) throw new Error(`${url}: ${response.status}`);
    return response.json();
  }

  async function loadSources() {
    const results = await Promise.allSettled([
      loadJson(endpoints.cases),
      loadJson(endpoints.templates),
      loadJson(endpoints.atlas)
    ]);

    if (results[0].status === 'fulfilled') state.data.cases = results[0].value.cases || [];
    if (results[1].status === 'fulfilled') state.data.templates = results[1].value.templates || [];
    if (results[2].status === 'fulfilled') state.data.atlas = results[2].value.entries || [];

    const loaded = results.filter((result) => result.status === 'fulfilled').length;
    if (els.status) {
      els.status.textContent = loaded === 3
        ? `Ready · ${state.data.cases.length} synthetic cases · ${state.data.templates.length} protocols · ${state.data.atlas.length} reviewed Atlas records`
        : `Partial source load · ${loaded}/3 canonical sources available`;
      els.status.dataset.state = loaded === 3 ? 'ready' : 'partial';
    }
  }

  function selectedPack() {
    return packs[els.pack?.value] || packs.idoc;
  }

  function selectedCases(pack) {
    return state.data.cases.filter((item) => pack.caseIds.includes(item.id));
  }

  function selectedTemplates(pack) {
    return state.data.templates.filter((item) => pack.templateIds.includes(item.id));
  }

  function unique(items) {
    return [...new Set(items.filter(Boolean))];
  }

  function evidenceRequirements(pack, cases) {
    const fromCases = cases.flatMap((item) => item.required_evidence || []);
    if (fromCases.length) return unique(fromCases);
    if (pack === packs.recurring) {
      return ['business impact', 'failing example', 'known-good comparison', 'timestamp', 'error or symptom', 'affected scope', 'recent change'];
    }
    return [];
  }

  const requirementSignals = [
    { match: /idoc/i, test: (text) => /\bidoc\b|\b\d{10,16}\b/i.test(text) },
    { match: /status/i, test: (text) => /\bstatus\b|\b(?:51|53|64|68|03)\b/i.test(text) },
    { match: /error|symptom/i, test: (text) => /\berror\b|\bfailed?\b|\bexception\b|\bnot\s+(?:created|updated|replicated|processed)\b/i.test(text) },
    { match: /message type/i, test: (text) => /\b(?:debm[a-z0-9_]*|cremas|matmas|message\s*type)\b/i.test(text) },
    { match: /partner|recipient/i, test: (text) => /\bpartner\b|\brecipient\b|\bsender\b|\breceiver\b/i.test(text) },
    { match: /timestamp|time/i, test: (text) => /\b\d{1,2}:\d{2}\b|\b20\d{2}[-/.]\d{1,2}[-/.]\d{1,2}\b|\btimestamp\b/i.test(text) },
    { match: /queue|failed unit/i, test: (text) => /\bq?rfc\b|\bqueue\b|\bunit\b/i.test(text) },
    { match: /business partner|role/i, test: (text) => /\bbusiness\s*partner\b|\bBP\b|\brole\b/i.test(text) },
    { match: /approval|activation/i, test: (text) => /\bapproved?\b|\bapproval\b|\bactivated?\b|\bactivation\b/i.test(text) },
    { match: /replication/i, test: (text) => /\breplication\b|\bdrf\b|\boutbound\b|\binbound\b/i.test(text) },
    { match: /target validation/i, test: (text) => /\btarget\b|\bvalidation\b|\bposted\b|\bcommit\b/i.test(text) },
    { match: /business impact/i, test: (text) => /\bimpact\b|\bblocked\b|\bdelay\b|\bunable\b|\bstop(?:ped)?\b/i.test(text) },
    { match: /failing example/i, test: (text) => /\bfail(?:ing|ed)?\b|\bexample\b|\bobject\b|\bdocument\b/i.test(text) },
    { match: /known-good/i, test: (text) => /\bknown[- ]good\b|\bworking\b|\bsuccess(?:ful)?\b|\bcomparison\b/i.test(text) },
    { match: /affected scope|volume/i, test: (text) => /\bscope\b|\bvolume\b|\busers?\b|\bobjects?\b|\bdocuments?\b|\bcustomers?\b|\bvendors?\b/i.test(text) },
    { match: /recent change/i, test: (text) => /\btransport\b|\bdeploy(?:ment|ed)?\b|\bchange\b|\brelease\b|\bload\b/i.test(text) }
  ];

  function detectRequirement(requirement, text) {
    const rule = requirementSignals.find((item) => item.match.test(requirement));
    if (rule) return rule.test(text);
    const terms = requirement.toLowerCase().split(/[^a-z0-9]+/).filter((term) => term.length >= 4);
    return terms.some((term) => text.toLowerCase().includes(term));
  }

  function rankAtlas(pack, cases, evidenceText) {
    const requiredUrls = unique(cases.flatMap((item) => item.expected_atlas_urls || []));
    const direct = requiredUrls.map((url) => state.data.atlas.find((entry) => entry.url?.endsWith(url) || entry.url === url)).filter(Boolean);

    const queryTerms = unique([
      ...pack.searchTerms,
      ...evidenceText.toLowerCase().split(/[^a-z0-9]+/).filter((term) => term.length > 5).slice(0, 30)
    ]);

    const scored = state.data.atlas
      .filter((entry) => !direct.some((item) => item.url === entry.url))
      .map((entry) => {
        const haystack = [entry.title, entry.description, entry.domain, entry.subdomain, ...(entry.tags || [])].join(' ').toLowerCase();
        const score = queryTerms.reduce((sum, term) => sum + (haystack.includes(term) ? 1 : 0), 0);
        return { entry, score };
      })
      .filter((item) => item.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, Math.max(0, 4 - direct.length))
      .map((item) => item.entry);

    return [...direct, ...scored].slice(0, 4);
  }

  function buildAnalysis() {
    const pack = selectedPack();
    const cases = selectedCases(pack);
    const templates = selectedTemplates(pack);
    const rawEvidence = [els.evidence?.value || '', state.fileText].filter(Boolean).join('\n');
    const requirements = evidenceRequirements(pack, cases);
    const captured = requirements.filter((item) => detectRequirement(item, rawEvidence));
    const missing = requirements.filter((item) => !captured.includes(item));
    const atlas = rankAtlas(pack, cases, rawEvidence);
    const hypotheses = unique(cases.flatMap((item) => item.acceptable_hypotheses || []));
    const forbidden = unique(cases.flatMap((item) => item.forbidden_actions || []));
    const owners = unique(cases.map((item) => item.correct_owner));
    const approval = unique(cases.map((item) => item.human_approval_boundary));

    return {
      pack,
      cases,
      templates,
      title: normalize(els.title?.value) || 'Untitled SAP incident',
      impact: normalize(els.impact?.value) || 'Not yet stated',
      captured,
      missing,
      atlas,
      hypotheses,
      forbidden,
      owners,
      approval,
      checks: pack.defaultChecks,
      rawEvidenceLength: rawEvidence.length
    };
  }

  function referencesMarkdown(analysis) {
    return analysis.atlas.length
      ? analysis.atlas.map((entry) => `- [${entry.title}](${entry.url}) — reviewed Atlas reference`).join('\n')
      : '- No reviewed Atlas reference was resolved from the current public manifest.';
  }

  function buildOutputs(analysis) {
    const captured = analysis.captured.length ? analysis.captured : ['No required evidence signal confidently detected'];
    const missing = analysis.missing.length ? analysis.missing : ['No obvious required-evidence gap detected by the deterministic signal check'];
    const boundaries = analysis.approval.length ? analysis.approval : ['A human owner must approve production changes, retries, reprocessing, or data correction.'];
    const owners = analysis.owners.length ? analysis.owners : ['Assign a business-process owner and the technical owner of the failing boundary.'];
    const hypotheses = analysis.hypotheses.length ? analysis.hypotheses : ['Process/data/configuration/integration boundary still to be isolated'];
    const forbidden = analysis.forbidden.length ? analysis.forbidden : ['Do not change production state before preserving evidence and confirming the failing boundary.'];
    const protocolNames = analysis.templates.map((item) => item.title);
    const commonHeader = `> Browser-local draft. No root cause is asserted from pasted text. Validate in the actual landscape before action.\n`;

    const incidentBrief = `# Incident Brief\n\n${commonHeader}\n## Context\n- **Diagnostic pack:** ${analysis.pack.label}\n- **Working title:** ${analysis.title}\n- **Business impact:** ${analysis.impact}\n- **Input size:** ${analysis.rawEvidenceLength} characters processed locally; raw input is not copied into this artifact.\n\n## Evidence signals captured\n${bulletList(captured)}\n\n## Evidence still needed\n${bulletList(missing)}\n\n## Diagnostic checks\n${bulletList(analysis.checks)}\n\n## Ownership\n${bulletList(owners)}\n\n## Safety / approval boundary\n${bulletList(boundaries)}\n\n## Reviewed references\n${referencesMarkdown(analysis)}\n\n## Protocols used\n${bulletList(protocolNames)}\n`;

    const evidenceChecklist = `# Evidence Checklist\n\n${commonHeader}\n## Incident\n- **Title:** ${analysis.title}\n- **Impact:** ${analysis.impact}\n\n## Captured\n${bulletList(captured)}\n\n## Missing / confirm\n${bulletList(missing)}\n\n## Preserve before intervention\n- Failing object or message identifier\n- Timestamp and sequence of events\n- Error/status/log evidence\n- Known-good comparison where available\n- Affected business scope\n- Recent change context\n\n## Do not do yet\n${bulletList(forbidden)}\n\n## Reviewed references\n${referencesMarkdown(analysis)}\n`;

    const rcaDraft = `# RCA Draft\n\n${commonHeader}\n## Problem statement\n- **Observed:** ${analysis.title}\n- **Business impact:** ${analysis.impact}\n- **Expected:** _Define expected business outcome._\n- **Difference:** _State the smallest clear gap between expected and observed._\n\n## Evidence\n### Present\n${bulletList(captured)}\n\n### Missing\n${bulletList(missing)}\n\n## Hypotheses to test\n${bulletList(hypotheses)}\n\n## Causal chain\n1. Why did the business outcome fail? _Not established._\n2. Where is the first verified divergence? _Not established._\n3. Which condition allowed that divergence? _Not established._\n4. Which control, data rule, configuration, code path, or ownership model allowed it? _Not established._\n5. Why did prevention or detection not catch it? _Not established._\n\n## Actions\n- **Containment:** _Pending evidence._\n- **Corrective action:** _Pending verified cause._\n- **Preventive action:** _Pending verified cause._\n- **Validation:** _Define a business-result check and recurrence signal._\n\n## Safety boundary\n${bulletList(boundaries)}\n\n## Reviewed references\n${referencesMarkdown(analysis)}\n`;

    const jiraDraft = `# ${analysis.title}\n\n## Business impact\n${analysis.impact}\n\n## Observed\nA SAP production/support incident requires structured diagnosis. Raw evidence is intentionally not reproduced in this draft.\n\n## Evidence captured\n${bulletList(captured)}\n\n## Evidence missing\n${bulletList(missing)}\n\n## Next diagnostic checks\n${bulletList(analysis.checks)}\n\n## Candidate hypotheses — not confirmed\n${bulletList(hypotheses)}\n\n## Ownership\n${bulletList(owners)}\n\n## Change / recovery boundary\n${bulletList(boundaries)}\n\n## Reviewed references\n${referencesMarkdown(analysis)}\n\n## Done when\n- Failing boundary is supported by evidence.\n- Recovery is approved and executed safely.\n- Business outcome is validated.\n- Recurrence signal or preventive action is recorded where relevant.\n`;

    return { incident: incidentBrief, evidence: evidenceChecklist, rca: rcaDraft, jira: jiraDraft };
  }

  function renderSummary(analysis) {
    if (!els.summary) return;
    const capturedCount = analysis.captured.length;
    const total = analysis.captured.length + analysis.missing.length;
    const gaps = analysis.missing.slice(0, 5).map((item) => `<li>${escapeHtml(item)}</li>`).join('');
    const safety = analysis.forbidden.slice(0, 3).map((item) => `<li>${escapeHtml(item)}</li>`).join('');

    els.summary.innerHTML = `
      <div><span>Evidence coverage</span><strong>${capturedCount}/${total || 0}</strong><small>signal-based, not proof</small></div>
      <div><span>Reviewed references</span><strong>${analysis.atlas.length}</strong><small>from Atlas manifest</small></div>
      <div><span>Protocols</span><strong>${analysis.templates.length}</strong><small>canonical templates</small></div>
      <section><h3>Missing evidence</h3><ul>${gaps || '<li>No obvious gap detected. Confirm manually.</li>'}</ul></section>
      <section><h3>Unsafe early actions</h3><ul>${safety || '<li>Do not change production state before the cause is supported.</li>'}</ul></section>`;
  }

  function renderReferences(analysis) {
    if (!els.references) return;
    els.references.innerHTML = analysis.atlas.length
      ? analysis.atlas.map((entry) => `<a href="${escapeHtml(entry.url)}"><strong>${escapeHtml(entry.title)}</strong><small>${escapeHtml(entry.description || '')}</small></a>`).join('')
      : '<p>No reviewed Atlas match resolved. Continue with the evidence checklist and manual Atlas search.</p>';
  }

  function activeOutputKey() {
    return els.outputTabs.find((tab) => tab.getAttribute('aria-selected') === 'true')?.dataset.outputTab || 'incident';
  }

  function renderOutput(key = activeOutputKey()) {
    const value = state.outputs[key] || 'Run the diagnostic to generate a draft.';
    if (els.output) els.output.value = value;
    els.outputTabs.forEach((tab) => {
      const active = tab.dataset.outputTab === key;
      tab.setAttribute('aria-selected', active ? 'true' : 'false');
      tab.tabIndex = active ? 0 : -1;
    });
  }

  async function analyze() {
    const analysis = buildAnalysis();
    state.outputs = buildOutputs(analysis);
    renderSummary(analysis);
    renderReferences(analysis);
    renderOutput('incident');
    root.dataset.hasResult = 'true';
  }

  async function readFile(file) {
    if (!file) {
      state.fileText = '';
      if (els.fileMeta) els.fileMeta.textContent = 'No file selected.';
      return;
    }
    if (file.size > 256 * 1024) {
      state.fileText = '';
      if (els.fileMeta) els.fileMeta.textContent = 'File is larger than 256 KB. Use a smaller excerpt.';
      return;
    }
    state.fileText = await file.text();
    if (els.fileMeta) els.fileMeta.textContent = `${file.name} · ${Math.max(1, Math.round(file.size / 1024))} KB · processed locally`;
  }

  async function copyOutput() {
    if (!els.output?.value) return;
    await navigator.clipboard.writeText(els.output.value);
    const original = els.copy.textContent;
    els.copy.textContent = 'Copied';
    window.setTimeout(() => { els.copy.textContent = original; }, 1200);
  }

  function downloadOutput() {
    const key = activeOutputKey();
    const text = state.outputs[key];
    if (!text) return;
    const blob = new Blob([text], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `sap-incident-${key}.md`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  }

  function reset() {
    if (els.title) els.title.value = '';
    if (els.impact) els.impact.value = '';
    if (els.evidence) els.evidence.value = '';
    if (els.file) els.file.value = '';
    if (els.fileMeta) els.fileMeta.textContent = 'No file selected.';
    if (els.summary) els.summary.innerHTML = '<p>Choose a diagnostic pack and add evidence to start.</p>';
    if (els.references) els.references.innerHTML = '<p>Reviewed Atlas references will appear here.</p>';
    state.fileText = '';
    state.outputs = {};
    root.dataset.hasResult = 'false';
    renderOutput('incident');
  }

  els.analyze?.addEventListener('click', analyze);
  els.reset?.addEventListener('click', reset);
  els.file?.addEventListener('change', (event) => readFile(event.target.files?.[0]));
  els.copy?.addEventListener('click', () => copyOutput().catch(() => {}));
  els.download?.addEventListener('click', downloadOutput);
  els.outputTabs.forEach((tab) => tab.addEventListener('click', () => renderOutput(tab.dataset.outputTab)));

  loadSources().catch(() => {
    if (els.status) {
      els.status.textContent = 'Canonical sources could not be loaded. The page remains read-only and no production action is authorized.';
      els.status.dataset.state = 'error';
    }
  });
})();
