---
layout: default
title: "SAP Incident Diagnostics — Evidence to Incident Brief and RCA"
description: "Browser-local SAP incident diagnostics for IDoc, integration, BP/MDG replication, evidence gaps, RCA drafts, and Jira-ready handoff."
permalink: /labs/incident-diagnostics/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
last_reviewed: 2026-09-22
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
      <h1>Turn scattered incident evidence into a useful handoff.</h1>
      <p>A SAP incident often arrives as fragments: an error message, a status, a timestamp, a ticket comment, and several assumptions about what went wrong. This lab helps us turn a small sanitized excerpt into a structured incident brief, an evidence checklist, an RCA draft, and Jira-ready Markdown. The analysis stays deterministic and browser-local; it organizes evidence but does not claim a production root cause.</p>
    </div>
    <aside class="incident-diagnostics__privacy" aria-label="Privacy and safety boundary">
      <strong>Browser-local by design</strong>
      <p>Selected files are read in the browser. The page does not upload the input or write it to localStorage.</p>
      <p>That does not make every input safe to use. Follow employer and client policy, and remove secrets, credentials, personal data, and proprietary details before working with an excerpt.</p>
      <span class="incident-diagnostics__status" data-source-status data-state="loading">Loading canonical public sources…</span>
    </aside>
  </header>

  <section class="incident-diagnostics__boundary" aria-label="Diagnostic boundary">
    <strong>This is an evidence organizer, not an automation authority.</strong> It cannot prove the root cause. It can show what is present, what is missing, and which reviewed references may help. A human still has to establish the cause and approve any retry, reprocessing, data correction, queue action, or production change.
  </section>

  <section class="incident-diagnostics__workspace" aria-label="Incident input and analysis">
    <div class="incident-diagnostics__panel">
      <p class="incident-diagnostics__label">01 / Scope</p>
      <h2>Start with the kind of incident.</h2>
      <p>The selected pack narrows the public cases, protocols, and Atlas references used by the draft. It does not add landscape-specific rules.</p>

      <div class="incident-diagnostics__field">
        <label for="incident-pack">Diagnostic pack</label>
        <select id="incident-pack" data-pack>
          <option value="idoc">IDoc / integration failure</option>
          <option value="bp">Business Partner / MDG replication</option>
          <option value="recurring">Recurring AMS incident</option>
        </select>
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
      <h2>Add a small, sanitized excerpt.</h2>
      <p>Useful evidence can be simple: status history, an error, a timestamp, message type, affected scope, or the recent change that preceded the issue. The tool looks for evidence signals; it does not send the text to an LLM or copy the raw excerpt into the generated artifacts.</p>

      <div class="incident-diagnostics__field">
        <label for="incident-evidence">Paste evidence</label>
        <textarea id="incident-evidence" data-evidence placeholder="Status history, error text, timestamp, message type, affected scope, recent change, or a sanitized ticket excerpt."></textarea>
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
      <h2>See what still needs to be proved.</h2>
      <div class="incident-diagnostics__summary" data-analysis-summary>
        <p>Choose a diagnostic pack and add evidence to start.</p>
      </div>
    </div>
    <div class="incident-diagnostics__panel">
      <p class="incident-diagnostics__label">04 / Sources</p>
      <h2>Keep the draft tied to reviewed material.</h2>
      <div class="incident-diagnostics__reference-list" data-references>
        <p>Reviewed Atlas references will appear here.</p>
      </div>
    </div>
  </section>

  <section class="incident-diagnostics__results" aria-labelledby="incident-output-title">
    <p class="incident-diagnostics__label">05 / Artifact</p>
    <h2 id="incident-output-title">Create the artifact the next person actually needs.</h2>
    <p>The four views use the same evidence but serve different moments in the incident: fast handoff, evidence collection, root-cause work, and ticket communication.</p>
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
    <h2 id="incident-source-model">Reuse one public evidence chain instead of inventing another one.</h2>
    <p>The lab combines three source types already maintained on the site: reviewed Atlas material, synthetic incident cases, and operational protocols. The MCP package exposes the same public diagnostic knowledge through a separate read-only interface.</p>
    <div class="research-route-list">
      <a href="/atlas/"><span>ATLAS</span><strong>Reviewed diagnostics</strong><small>Only records eligible for the public Atlas manifest are used as diagnostic references.</small><i class="material-symbols-outlined" aria-hidden="true">library_books</i></a>
      <a href="/datasets/incident-lab/"><span>CASE</span><strong>Synthetic incident cases</strong><small>Public-safe cases describe expected evidence, unsafe actions, ownership, and human-approval boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/templates/"><span>PROTO</span><strong>Operational protocols</strong><small>Incident triage, integration analysis, RCA, process deviation, and runbook structures shape the generated drafts.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="/mcp/sap-diagnostics-mcp/"><span>MCP</span><strong>SAP Diagnostics MCP</strong><small>The local read-only MCP package exposes the same public Atlas and Incident Lab sources for tool-based use.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
    </div>
  </section>
</div>

<script src="/assets/js/incident-diagnostics.js" defer></script>
