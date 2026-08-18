---
layout: default
title: "Business AI Graph — Machine Layer"
description: "Machine-readable Business AI graph, manifest, evidence views, and SAP Enterprise context links for analysis and agent workflows."
permalink: /machine/business-ai/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-18
hide_global_cta: true
tags:
  - business-ai
  - knowledge-graph
  - machine-readable
  - sap
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/machine/">Machine Layer</a></li><li aria-current="page">Business AI Graph</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Machine layer / Business AI graph</p>
      <h1>Load relationships.<br />Keep evidence limits visible.</h1>
      <p>The graph connects business domains, end-to-end processes, stages, AI patterns, cases, metrics, evidence, controls, technology, and SAP Enterprise context. It is a generated view of canonical site data, not a second knowledge base.</p>
      <a class="research-canvas__button" href="/machine/business-ai/manifest.json">Open manifest <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Business AI graph rules">
      <p>Graph rules</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Typed</strong><small>Nodes and edges</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Linked</strong><small>Human source pages</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Bounded</strong><small>Evidence and authority</small></div>
      <em>Missing review state stays visible. A generated view never upgrades evidence by itself.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Graph boundary">
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Source rule:</strong> canonical YAML under <code>_data/labs/business_ai/</code> owns the business meaning. These endpoints are generated projections for tools and analysis.</p>
    <p><strong>ERP rule:</strong> Business AI processes stay vendor neutral. SAP-specific pages are linked as enterprise context, so SAP implementation details do not leak into the common process model.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Endpoints</p>
      <h2>Start with the manifest, then load only what the task needs.</h2>
      <p>The full graph supports cross-entity analysis. Smaller views reduce context size for focused agent tasks.</p>
    </header>
    <div class="research-route-list">
      <a href="/machine/business-ai/manifest.json"><span>META</span><strong>Graph manifest</strong><small>Version, source revisions, counts, views, and quality command.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/machine/business-ai/graph.json"><span>GRAPH</span><strong>Full Business AI graph</strong><small>Typed nodes and edges with canonical links, evidence, limitations, controls, and SAP context.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/machine/business-ai/views/process-context.json"><span>PROC</span><strong>Process context view</strong><small>Business AI processes linked to SAP pages, decisions, data, integrations, authority, and controls.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/machine/business-ai/views/case-evidence.json"><span>CASE</span><strong>Case evidence view</strong><small>Evidence grades, metrics, sources, limitations, review state, and proof gaps.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Quality contract</p>
      <h2>Broken structure blocks. Missing evidence remains a gap.</h2>
      <p>CI rejects invalid IDs, broken edge direction, missing graph targets, broken SAP source routes, and missing priority process mappings. Evidence review gaps, weak case coverage, and incomplete platform links are reported without pretending they are solved.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/model/"><span>MODEL</span><strong>Human graph model</strong><small>Entity and relationship design for Business AI analysis.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/business-ai/cases/"><span>EVID</span><strong>Public case records</strong><small>Human-readable implementation evidence and limitations behind the case nodes.</small><i class="material-symbols-outlined" aria-hidden="true">library_books</i></a>
      <a href="/labs/enterprise-context/"><span>SAP</span><strong>SAP Enterprise context</strong><small>Operational SAP process, data, integration, and diagnostic source pages.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
    </div>
  </section>
</div>
