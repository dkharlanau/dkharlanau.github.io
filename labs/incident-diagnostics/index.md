---
layout: default
title: "SAP Incident Diagnostics — Evidence to Incident Brief and RCA"
description: "Browser-local SAP incident diagnostics that turns pasted evidence into an incident brief, evidence checklist, RCA draft, and Jira-ready Markdown using reviewed Atlas references and operational protocols."
permalink: /labs/incident-diagnostics/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-05
hide_global_cta: true
hide_site_share: true
career_impact: mapped
career_skills:
  - integration-recovery
  - integration-observability
  - logistics-mdg
tags:
  - sap
  - incident-management
  - diagnostics
  - integration
  - mdg
  - root-cause-analysis
---

<link rel="stylesheet" href="/assets/css/incident-diagnostics.css" />

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">SAP Incident Diagnostics</li></ol>
</nav>

<div class="incident-diagnostics" data-incident-diagnostics data-has-result="false">
  <header class="incident-diagnostics__hero">
    <div>
      <p class="incident-diagnostics__eyebrow">Lab / SAP operations</p>
      <h1>Turn incident evidence into a usable next step.</h1>
      <p>Paste a small incident excerpt or load a text, XML, JSON, or CSV file. The browser checks which evidence signals are present, finds reviewed Atlas references, applies existing operational protocols, and builds four working artifacts. It does not diagnose a production root cause automatically.</p>
    </div>
    <aside class="incident-diagnostics__privacy" aria-label="Privacy and safety boundary">
      <strong>Browser-local by design</strong>
      <p>This page reads the selected file in your browser. It does not upload the input or store it in localStorage.</p>
      <p>Still follow employer and client policy. Do not paste secrets, credentials, personal data, or proprietary material into an unapproved browser session.</p>
      <span class="incident-diagnostics__status" data-source-status data-state="loading">Loading canonical public sources…</span>
    </aside>
  </header>

  <section class="incident-diagnostics__boundary" aria-label="Diagnostic boundary">
    <strong>Evidence, not automation authority.</strong> The tool can structure a case, expose missing evidence, and suggest reviewed diagnostic references. It cannot prove the root cause, approve a retry, change SAP, reprocess an IDoc, clear a queue, or correct master data.
  </section>

  <section class="incident-diagnostics__workspace" aria-label="Incident input and analysis">
    <div class="incident-diagnostics__panel">
      <p class="incident-diagnostics__label">01 / Scope</p>
      <h2>Choose the problem shape.</h2>

      <div class="incident-diagnostics__field">
        <label for="incident-pack">Diagnostic pack</label>
        <select id="incident-pack" data-pack>
          <option value="idoc">IDoc / integration failure</option>
          <option value="bp">Business Partner / MDG replication</option>
          <option value="recurring">Recurring AMS incident</option>
        </select>
        <span class="incident-diagnostics__hint">Packs only select existing synthetic cases, Atlas topics, and operational protocols. They do not contain landscape-specific rules.</span>
      </div>

      <div class="incident-diagnostics__field">
        <label for="incident-title">Working title</label>
        <input id="incident-title" data-case-title type="text" maxlength="160" placeholder="Example: inbound IDoc fails during vendor update" autocomplete="off" />
      </div>

      <div class="incident-diagnostics__field">
        <label for="incident-impact">Business impact</label>
        <input id="incident-impact" data-impact type="text" maxlength="240" placeholder="Example: vendor updates are delayed for one interface" autocomplete="off" />
      </div>
    </div>

    <div class="incident-diagnostics__panel">
      <p class="incident-diagnostics__label">02 / Evidence</p>
      <h2>Add a small, safe excerpt.</h2>

      <div class="incident-diagnostics__field">
        <label for="incident-evidence">Paste evidence</label>
        <textarea id="incident-evidence" data-evidence placeholder="Status history, error text, timestamp, message type, affected scope, recent change, or a sanitized ticket excerpt."></textarea>
        <span class="incident-diagnostics__hint">The deterministic check looks for evidence signals. It does not send the text to an LLM and does not copy the raw text into generated artifacts.</span>
      </div>

      <div class="incident-diagnostics__field incident-diagnostics__file">
        <label for="incident-file">Or load a local file</label>
        <input id="incident-file" data-file type="file" accept=".txt,.log,.xml,.json,.csv,text/plain,text/csv,application/json,application/xml,text/xml" />
        <small data-file-meta>No file selected. Maximum 256 KB.</small>
      </div>

      <div class="incident-diagnostics__actions">
        <button class="incident-diagnostics__button" type="button" data-analyze>Build diagnostic draft</button>
        <button class="incident-diagnostics__button incident-diagnostics__button--quiet" type="button" data-reset>Clear</button>
      </div>
    </div>
  </section>

  <section class="incident-diagnostics__workspace" aria-label="Diagnostic summary">
    <div class="incident-diagnostics__panel">
      <p class="incident-diagnostics__label">03 / Gaps</p>
      <h2>What evidence is still missing?</h2>
      <div class="incident-diagnostics__summary" data-analysis-summary>
        <p>Choose a diagnostic pack and add evidence to start.</p>
      </div>
    </div>
    <div class="incident-diagnostics__panel">
      <p class="incident-diagnostics__label">04 / Sources</p>
      <h2>Reviewed references only.</h2>
      <div class="incident-diagnostics__reference-list" data-references>
        <p>Reviewed Atlas references will appear here.</p>
      </div>
    </div>
  </section>

  <section class="incident-diagnostics__results" aria-labelledby="incident-output-title">
    <p class="incident-diagnostics__label">05 / Artifact</p>
    <h2 id="incident-output-title">Generate something the team can use.</h2>
    <div class="incident-diagnostics__tabs" role="tablist" aria-label="Generated artifact">
      <button class="incident-diagnostics__tab" type="button" role="tab" aria-selected="true" data-output-tab="incident">Incident brief</button>
      <button class="incident-diagnostics__tab" type="button" role="tab" aria-selected="false" tabindex="-1" data-output-tab="evidence">Evidence checklist</button>
      <button class="incident-diagnostics__tab" type="button" role="tab" aria-selected="false" tabindex="-1" data-output-tab="rca">RCA draft</button>
      <button class="incident-diagnostics__tab" type="button" role="tab" aria-selected="false" tabindex="-1" data-output-tab="jira">Jira-ready Markdown</button>
    </div>
    <textarea class="incident-diagnostics__output" data-output readonly aria-label="Generated Markdown">Run the diagnostic to generate a draft.</textarea>
    <div class="incident-diagnostics__actions">
      <button class="incident-diagnostics__button" type="button" data-copy>Copy Markdown</button>
      <button class="incident-diagnostics__button incident-diagnostics__button--quiet" type="button" data-download>Download .md</button>
    </div>
  </section>

  <section class="incident-diagnostics__sources" aria-labelledby="incident-source-model">
    <p class="incident-diagnostics__label">Source model</p>
    <h2 id="incident-source-model">One public evidence chain, three inputs.</h2>
    <p>The page deliberately reuses the existing sources instead of keeping a second incident knowledge base:</p>
    <div class="research-route-list">
      <a href="/atlas/"><span>ATLAS</span><strong>Reviewed diagnostics</strong><small>Only records eligible for the public Atlas manifest are used as diagnostic references.</small><i class="material-symbols-outlined" aria-hidden="true">library_books</i></a>
      <a href="/datasets/incident-lab/"><span>CASE</span><strong>Synthetic incident cases</strong><small>Public-safe cases provide evidence expectations, unsafe actions, ownership, and human-approval boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/templates/"><span>PROTO</span><strong>Operational protocols</strong><small>Incident triage, integration failure analysis, RCA, process deviation, and runbook structures shape the outputs.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="/mcp/sap-diagnostics-mcp/"><span>MCP</span><strong>SAP Diagnostics MCP</strong><small>The same public Atlas and Incident Lab sources are already available through the local read-only MCP package.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
    </div>
  </section>
</div>

<script src="/assets/js/incident-diagnostics.js" defer></script>
