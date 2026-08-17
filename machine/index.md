---
layout: default
title: "Machine Layer — Data, Agent Tools, and AI-Readable Sources"
description: "A technical entry point to datasets, machine-readable exports, agent skills, agent tools, and the SAP diagnostics MCP package."
permalink: /machine/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-17
hide_global_cta: true
tags:
  - datasets
  - ai-agents
  - machine-readable
  - mcp
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li aria-current="page">Machine Layer</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Machine layer / structured access</p>
      <h1>Human pages explain.<br />Machine endpoints expose structure.</h1>
      <p>This layer groups datasets, JSON and YAML exports, portable agent skills, tool descriptions, and local MCP packages. It supports retrieval and automation without turning the public site into a runtime platform.</p>
      <a class="research-canvas__button" href="#machine-routes">Open technical routes <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Machine layer">
      <p>Access types</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Data</strong><small>Canonical datasets</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>AI</strong><small>Readable exports</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Tools</strong><small>Skills and MCP</small></div>
      <em>Public files only. Runtime credentials and private corpora stay outside the repository.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Machine layer boundary">
    <span class="material-symbols-outlined" aria-hidden="true">schema</span>
    <p><strong>Problem:</strong> useful knowledge becomes hard for tools to retrieve when every source has a different format, route, or level of structure.</p>
    <p><strong>Context:</strong> this static layer exposes public datasets, indexes, schemas, skills, and tool descriptions for retrieval, evaluation, and local automation. It does not run agents or private services.</p>
  </section>

  <section class="research-canvas__inventory" id="machine-routes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Technical routes</p>
      <h2>One map for machine-facing assets.</h2>
      <p>The source collections keep their existing URLs and schemas.</p>
    </header>
    <div class="research-route-list">
      <a href="/datasets/"><span>DATA</span><strong>Datasets</strong><small>Canonical structured collections, manifests, schemas, and domain-specific data packages.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="/ai/"><span>AI</span><strong>AI-readable sources</strong><small>Generated and curated JSON, YAML, discovery maps, indexes, and expert evidence surfaces.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/skill-hub/"><span>SKILL</span><strong>Skill Hub</strong><small>Human-readable map of reusable analysis, architecture, development, and decision skills.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="/agent-tools/"><span>TOOL</span><strong>Agent Tools</strong><small>Static tool descriptions for SAP diagnostics, ABAP, integration, data analysis, evaluation, and related work.</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      <a href="/mcp/sap-diagnostics-mcp/"><span>MCP</span><strong>SAP Diagnostics MCP</strong><small>A local, read-only package that consumes committed public artifacts. GitHub Pages publishes it but does not execute it.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
    </div>
  </section>
</div>
