---
layout: default
title: "SAP Assessment MCP — Read-Only Practice Resources"
description: "A local read-only MCP server that exposes SAP Lead assessment cases as resources and deterministic selection tools."
permalink: /mcp/sap-assessment-mcp/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-17
hide_global_cta: true
tags: [sap, assessment, mcp, ai-agents, machine-readable]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/machine/">Machine Layer</a></li><li><a href="/machine/assessment/">Assessment Access</a></li><li aria-current="page">SAP Assessment MCP</li></ol></nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MCP / assessment practice</p>
      <h1>Use the case corpus<br />without copying it.</h1>
      <p>This local read-only server exposes committed SAP Lead assessment cases as MCP resources and deterministic tools. It uses stdio, has no runtime dependencies, and keeps private progress outside the server.</p>
      <a class="research-canvas__button" href="#setup">Set up the server <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="SAP Assessment MCP boundary">
      <p>Server boundary</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Read</strong><small>Committed public data</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Local</strong><small>stdio process</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>0</strong><small>SAP credentials</small></div>
      <em>The server selects and exposes practice material. It does not own the assessment result.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">security</span>
    <p><strong>Read-only by design:</strong> no SAP connection, no remote fetch, no telemetry, no private corpus, no attempt storage, and no write-capable tool.</p>
    <p><strong>Source:</strong> <a href="/labs/assessment/data/case-sets.json">case-sets.json</a> is the manifest. The server loads each active JSONL set from the local checkout.</p>
  </section>

  <section class="research-canvas__inventory" id="setup" data-reveal>
    <header><p class="research-canvas__eyebrow">Setup</p><h2>Run it from a local checkout.</h2><p>GitHub Pages publishes the package but cannot execute an MCP process.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>1. Requirements</h3><p>Node.js 20 or newer and a local checkout of this repository.</p></div>
      <div><h3>2. Test</h3><p><code>cd mcp/sap-assessment-mcp</code><br /><code>npm install .</code><br /><code>npm test</code><br /><code>npm run smoke</code></p></div>
      <div><h3>3. Client config</h3><p>Copy <code>examples/mcp.json</code>. Replace both absolute paths and point <code>SAP_ASSESSMENT_DATA_DIR</code> to the repository root.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Resources</p><h2>Resources hold stable assessment context.</h2><p>Clients can discover the catalog, read one case, or load a complete track.</p></header>
    <div class="research-route-list">
      <a href="/labs/assessment/data/case-sets.json"><span>SET</span><strong>sap-assessment://catalog/case-sets</strong><small>Manifest of active case files, counts, coverage, and the shared schema route.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="/labs/assessment/data/case-schema.json"><span>SCHEMA</span><strong>sap-assessment://catalog/case-schema</strong><small>The JSON Schema used by assessment case records.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/assessment/"><span>TRACK</span><strong>sap-assessment://catalog/tracks</strong><small>Derived track counts, reasoning-level coverage, and human study routes.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/assessment/data/cases.jsonl"><span>CASE</span><strong>sap-assessment://case/{case_id}</strong><small>One case with prompt, rubric points, follow-ups, red flags, graph refs, and human refs.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/labs/assessment/"><span>GROUP</span><strong>sap-assessment://track/{track}</strong><small>All cases for one assessment track.</small><i class="material-symbols-outlined" aria-hidden="true">view_list</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="tools" data-reveal>
    <header><p class="research-canvas__eyebrow">Tools</p><h2>Tools select. Resources explain.</h2><p>Selection is deterministic so the same input produces the same set.</p></header>
    <div class="research-route-list">
      <a href="/machine/assessment/"><span>SEARCH</span><strong>search_assessment_cases</strong><small>Search text and filter by track or reasoning level.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="/machine/assessment/"><span>GET</span><strong>get_assessment_case</strong><small>Return one full case by stable ID.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/machine/assessment/"><span>TRACK</span><strong>list_assessment_tracks</strong><small>Return track counts, reasoning-level coverage, and linked study routes.</small><i class="material-symbols-outlined" aria-hidden="true">view_list</i></a>
      <a href="/machine/assessment/"><span>SET</span><strong>build_practice_set</strong><small>Create a filtered practice set for one track or reasoning level.</small><i class="material-symbols-outlined" aria-hidden="true">playlist_add</i></a>
      <a href="/machine/assessment/"><span>MOCK</span><strong>build_mock_set</strong><small>Create a balanced set across the four assessment tracks.</small><i class="material-symbols-outlined" aria-hidden="true">assignment</i></a>
      <a href="/machine/assessment/"><span>READ</span><strong>get_study_sources</strong><small>Return the human-readable SAP Enterprise routes linked to one case.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Protocol</p><h2>Modern and legacy stdio clients are supported.</h2><p>The package supports MCP 2026-07-28 discovery and per-request metadata, plus the 2025-era initialize flow for clients that have not migrated yet.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>2026-07-28</h3><p><code>server/discover</code>, per-request protocol metadata, resource and tool list cache hints.</p></div>
      <div><h3>2025 clients</h3><p><code>initialize</code> remains available for common legacy stdio clients.</p></div>
      <div><h3>Transport</h3><p>stdio only in this package. A remote deployment needs a real runtime; static GitHub Pages is not one, despite its heroic ability to serve files.</p></div>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Practice loop</p><h2>Keep the rubric hidden until the answer exists.</h2></div>
    <ol>
      <li><span>01</span><strong>Select</strong><p>Search or build a practice set.</p></li>
      <li><span>02</span><strong>Ask</strong><p>Present only the title and prompt for realistic practice.</p></li>
      <li><span>03</span><strong>Answer</strong><p>Explain the business goal, ownership, flow, logic, boundary, proof, and trade-off.</p></li>
      <li><span>04</span><strong>Reveal</strong><p>Compare the answer with expected points, follow-ups, and red flags.</p></li>
      <li><span>05</span><strong>Study</strong><p>Open only the linked human routes that cover the weak area.</p></li>
      <li><span>06</span><strong>Repeat</strong><p>Use another case to test whether the reasoning improved.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
