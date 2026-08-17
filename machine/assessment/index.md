---
layout: default
title: "SAP Lead Assessment — Machine Access"
description: "Machine-readable access to SAP Lead assessment cases, schemas, practice contracts, and the local read-only MCP server."
permalink: /machine/assessment/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-17
hide_global_cta: true
tags: [sap, assessment, machine-readable, mcp, datasets]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/machine/">Machine Layer</a></li><li aria-current="page">Assessment Access</li></ol></nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Machine layer / assessment</p>
      <h1>One assessment source.<br />Three access modes.</h1>
      <p>Humans use the site pages. Scripts use the static JSON and JSONL files. MCP clients use a local read-only server that exposes the same committed assessment data as resources and tools.</p>
      <a class="research-canvas__button" href="#access">Choose access <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Assessment machine access">
      <p>Access modes</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>HTML</strong><small>Human study</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>JSON</strong><small>Static automation</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>MCP</strong><small>Client context</small></div>
      <em>GitHub Pages publishes files. It does not execute the MCP server.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">schema</span>
    <p><strong>Source rule:</strong> the case manifest points to every active JSONL case set. A client should load the manifest first instead of hard-coding case filenames.</p>
    <p><strong>Boundary:</strong> assessment attempts, local scoring history, private notes, credentials, and SAP landscape data are not MCP resources in this public package.</p>
  </section>

  <section class="research-canvas__inventory" id="access" data-reveal>
    <header><p class="research-canvas__eyebrow">Access decision</p><h2>Use the simplest interface that fits the job.</h2><p>MCP is useful when the client needs discoverable context and tools. It is unnecessary when a normal file read is enough. Humanity survives another avoided abstraction.</p></header>
    <div class="research-route-list">
      <a href="/labs/assessment/start-here/"><span>HUMAN</span><strong>Site pages</strong><small>Use for study, explanation, diagrams, domain navigation, mocks, review, and Board Mode.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/labs/assessment/data/case-sets.json"><span>DATA</span><strong>Static assessment data</strong><small>Use in scripts, tests, notebooks, indexers, or custom applications that can read JSON and JSONL directly.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/mcp/sap-assessment-mcp/"><span>MCP</span><strong>SAP Assessment MCP</strong><small>Use when an MCP client should discover case resources, search cases, build practice sets, or fetch study routes.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Canonical data</p><h2>Start from contracts, not from assumptions.</h2><p>The current manifest contains 63 structured cases across core and specialist sets.</p></header>
    <div class="research-route-list">
      <a href="/labs/assessment/data/case-sets.json"><span>MANIFEST</span><strong>Case Set Manifest</strong><small>Active files, counts, coverage, schema route, and loading rule.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="/labs/assessment/data/case-schema.json"><span>SCHEMA</span><strong>Case Schema</strong><small>Required fields for case ID, track, level, prompt, expected points, follow-ups, red flags, graph refs, and human refs.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/assessment/data/scoring.json"><span>SCORE</span><strong>Scoring Contract</strong><small>Shared scoring dimensions and Lead-level signals used by the practice layer.</small><i class="material-symbols-outlined" aria-hidden="true">score</i></a>
      <a href="/labs/assessment/data/adaptive-selection.json"><span>SELECT</span><strong>Adaptive Selection</strong><small>Selection rules for weak dimensions, track gaps, reasoning levels, recency, and diversity.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="/labs/assessment/data/mock-session.json"><span>MOCK</span><strong>Mock Contract</strong><small>Rules for balanced multi-case assessment sessions.</small><i class="material-symbols-outlined" aria-hidden="true">assignment</i></a>
      <a href="/labs/assessment/data/review-map.json"><span>REVIEW</span><strong>Review Map</strong><small>Maps weak signals to focused human study routes.</small><i class="material-symbols-outlined" aria-hidden="true">target</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">MCP resources</p><h2>Stable context without copying the corpus.</h2><p>The local server exposes a small catalog plus one resource per assessment case.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Catalog</h3><ul><li><code>sap-assessment://catalog/case-sets</code></li><li><code>sap-assessment://catalog/case-schema</code></li><li><code>sap-assessment://catalog/tracks</code></li></ul></div>
      <div><h3>Case resource</h3><p><code>sap-assessment://case/ASSESS-SALES-001</code></p><p>Returns the prompt, expected points, follow-ups, red flags, graph refs, and human study routes.</p></div>
      <div><h3>Track resource</h3><p><code>sap-assessment://track/sales</code></p><p>Returns all cases for one assessment track.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">MCP tools</p><h2>Use tools for selection, resources for context.</h2><p>The server stays read-only and deterministic. It does not call an LLM and does not change assessment history.</p></header>
    <div class="research-route-list">
      <a href="/mcp/sap-assessment-mcp/#tools"><span>SEARCH</span><strong>search_assessment_cases</strong><small>Filter by query, track, reasoning level, and result limit.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="/mcp/sap-assessment-mcp/#tools"><span>GET</span><strong>get_assessment_case</strong><small>Retrieve one complete case by stable case ID.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/mcp/sap-assessment-mcp/#tools"><span>TRACK</span><strong>list_assessment_tracks</strong><small>Return case counts, reasoning-level coverage, and source routes.</small><i class="material-symbols-outlined" aria-hidden="true">view_list</i></a>
      <a href="/mcp/sap-assessment-mcp/#tools"><span>SET</span><strong>build_practice_set</strong><small>Build a deterministic filtered practice set.</small><i class="material-symbols-outlined" aria-hidden="true">playlist_add</i></a>
      <a href="/mcp/sap-assessment-mcp/#tools"><span>MOCK</span><strong>build_mock_set</strong><small>Build a balanced deterministic set across tracks.</small><i class="material-symbols-outlined" aria-hidden="true">assignment</i></a>
      <a href="/mcp/sap-assessment-mcp/#tools"><span>READ</span><strong>get_study_sources</strong><small>Return the human-readable site routes linked to a case.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Client workflow</p><h2>A practical MCP loop.</h2></div>
    <ol>
      <li><span>01</span><strong>Discover</strong><p>List resources or call <code>list_assessment_tracks</code>.</p></li>
      <li><span>02</span><strong>Select</strong><p>Search for a topic or build a practice set.</p></li>
      <li><span>03</span><strong>Read</strong><p>Load the chosen case resource before answering.</p></li>
      <li><span>04</span><strong>Answer</strong><p>Give the answer without exposing expected points first when running a realistic practice session.</p></li>
      <li><span>05</span><strong>Review</strong><p>Use the case rubric and human refs to identify the exact gap.</p></li>
      <li><span>06</span><strong>Repeat</strong><p>Select a related case and test the same weak reasoning dimension again.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
