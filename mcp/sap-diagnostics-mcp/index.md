---
layout: default
title: "SAP Diagnostics MCP — AI Ready Lab"
description: "A local-first, read-only MCP learning project for deterministic SAP Atlas diagnostics."
permalink: /mcp/sap-diagnostics-mcp/
status: experimental
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/ai-ready/">AI Ready</a></li><li aria-current="page">SAP Diagnostics MCP</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">AI Ready / Hands-on Lab 01</p>
      <h1>Build a narrow MCP server first.</h1>
      <p>SAP Diagnostics MCP is a local-first, credential-free, read-only learning project. It exposes deterministic retrieval over public SAP Atlas artifacts through small diagnostic tools.</p>
      <a class="research-canvas__button" href="https://github.com/dkharlanau/dkharlanau.github.io/tree/main/mcp/sap-diagnostics-mcp" target="_blank" rel="noopener">Open the source <span class="material-symbols-outlined" aria-hidden="true">open_in_new</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Lab characteristics">
      <p>Lab boundary</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Read</strong><small>No write tools</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>stdio</strong><small>Local transport</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>0</strong><small>Runtime dependencies</small></div>
      <em>Learning artifact. Not a SAP connector or production authorization layer.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">lock</span>
    <p><strong>Why this shape:</strong> start with public data and read-only behavior. Learn tool contracts, context boundaries, protocol messages, testing, and evidence before adding credentials or writes.</p>
    <p><strong>Current-protocol note:</strong> MCP changes quickly. The AI Ready lab tracks the current protocol baseline separately from this small implementation.</p>
    <a href="/labs/ai-ready/#mcp">Open MCP architecture notes <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Tool surface</p><h2>Small tools with clear jobs.</h2><p>The current prototype keeps retrieval deterministic and preserves evidence and review state.</p></header>
    <div class="research-route-list">
      <a href="https://github.com/dkharlanau/dkharlanau.github.io/blob/main/mcp/sap-diagnostics-mcp/README.md" target="_blank" rel="noopener"><span>FIND</span><strong>Diagnostic retrieval</strong><small>Search diagnostics, open a diagnostic, follow related topics, and collect evidence checklists.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://github.com/dkharlanau/dkharlanau.github.io/blob/main/mcp/sap-diagnostics-mcp/README.md" target="_blank" rel="noopener"><span>RISK</span><strong>Tool risk profile</strong><small>Find agent tools and inspect their risk metadata before a wider agent architecture uses them.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="https://github.com/dkharlanau/dkharlanau.github.io/blob/main/mcp/sap-diagnostics-mcp/README.md" target="_blank" rel="noopener"><span>CASE</span><strong>Synthetic incident loop</strong><small>Evaluate a proposed response against public fixtures for evidence coverage, unsafe actions, and human approval boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Exercise</p><h2>What to learn from it.</h2><p>The server is useful because the boundaries are visible, not because it has many tools.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/#mcp"><span>01</span><strong>Contract design</strong><small>Make names, arguments, outputs, errors, and descriptions predictable enough for both models and software.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/ai-ready/#security"><span>02</span><strong>Permission design</strong><small>See why read-only and credential-free is a useful first trust boundary before remote access or writes.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="/labs/ai-ready/#evals"><span>03</span><strong>Protocol and behavior tests</strong><small>Test deterministic results and the protocol surface. Add evals later when a model becomes part of the loop.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/ai-ready/#deploy"><span>04</span><strong>Production gap</strong><small>Identify what a real remote service still needs: identity, authorization, current protocol support, tracing, deployment, rate limits, and operations.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
