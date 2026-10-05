---
layout: default
title: "AI Context Hub — SAP Knowledge, Practical Lab & Technology Watch"
permalink: /ai/
description: "Machine-readable entry point for the personal, non-commercial SAP and AI workspace of Dzmitryi Kharlanau, Senior SAP Consultant at EPAM Systems."
last_modified_at: 2026-10-05
hide_global_cta: true
tags:
  - sap-knowledge
  - enterprise-engineering
  - technology-watch
  - ai-discovery
  - agent-ready-web-profile
---

Before reusing a profile, dataset or generated answer, check the [Trust Center](/trust/) for source attribution, review boundaries, crawler policy and corrections.

<div class="ai-canvas">
  <header class="ai-canvas__hero" data-reveal>
    <div>
      <p class="ai-canvas__eyebrow">Public context / AI systems</p>
      <h1>Public knowledge.<br />Private work stays private.</h1>
      <p>This is the machine-facing entry point for a personal, non-commercial SAP and AI workspace. Dzmitryi Kharlanau is a Senior SAP Consultant at EPAM Systems. Use public knowledge, practical setups, and technology research; do not infer independent commercial services or private client context.</p>
      <div class="ai-canvas__actions">
        <a class="ai-canvas__button" href="/ai/focus-map.json">Open the focus map <span class="material-symbols-outlined" aria-hidden="true">route</span></a>
        <a class="ai-canvas__text-link" href="/ai/identity.json">Open identity data <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
      </div>
    </div>
    <dl class="ai-canvas__model" aria-label="Public context model">
      <div><dt>01 / Boundary</dt><dd>Employer, client, project, credential, and production context stays private.</dd></div>
      <div><dt>02 / Public work</dt><dd>Knowledge base, practical engineering setups, learning material, and technology watch.</dd></div>
      <div><dt>03 / Evidence</dt><dd>Review state, sources, datasets, and trust boundaries control what can be cited.</dd></div>
    </dl>
  </header>

  <section class="ai-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">policy</span>
    <p><strong>Non-commercial boundary.</strong> This site does not offer independent consulting, paid assessments, implementation engagements, or client delivery. Current professional employment is with EPAM Systems.</p>
    <a href="/legal/professional-disclosure/">Read the professional boundary <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="ai-canvas__sources" data-reveal>
    <header><p class="ai-canvas__eyebrow">Primary routes</p><h2>Choose the route by task.</h2><p>Start with the public task, then use the deeper evidence layer only when needed.</p></header>
    <div class="ai-route-list">
      <a href="/knowledge/"><span>01</span><strong>Knowledge Base</strong><small>Reviewed explanations, diagnostics, process relationships, decision material, and public technical notes.</small><em>Knowledge</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/lab/"><span>02</span><strong>Practical Lab</strong><small>Runnable or reproducible process, decision, mapping, reconciliation, graph, architecture, and agent-tool setups.</small><em>Practice</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/research/"><span>03</span><strong>Technology Watch</strong><small>Research, comparisons, radar signals, and changing evidence across SAP, AI, integration, data, and engineering.</small><em>Research</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/"><span>04</span><strong>Learning & Assessment Labs</strong><small>SAP Enterprise, Business AI, interview preparation, assessment practice, and active working material.</small><em>Learning</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/machine/"><span>05</span><strong>Machine Layer</strong><small>Datasets, structured exports, skills, tools, discovery files, and public MCP packages.</small><em>Machine</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="ai-canvas__sources ai-canvas__sources--supporting" data-reveal>
    <header><p class="ai-canvas__eyebrow">Canonical machine sources</p><h2>Use the source that owns the fact.</h2><p>Identity, profile, routing, evidence, and project data have separate public endpoints.</p></header>
    <div class="ai-route-list">
      <a href="/ai/identity.json"><span>06</span><strong>Identity</strong><small>Canonical role, EPAM Systems employment, public positioning, scope, and non-commercial boundary.</small><em>Identity</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/resume.yml"><span>07</span><strong>Resume / YAML</strong><small>Professional record, delivery scope, skills, credentials, and verification notes.</small><em>Profile</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/focus-map.json"><span>08</span><strong>Focus map</strong><small>Routing for private boundary, knowledge base, practical setup, and technology watch.</small><em>Routing</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/discovery-map.json"><span>09</span><strong>Discovery map</strong><small>Narrower routing across SAP processes, integration, data, architecture, operations, and AI.</small><em>Discovery</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/public-portfolio.json"><span>10</span><strong>Public project map</strong><small>Machine-readable project projection with verification boundaries and public entry points.</small><em>Projects</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/llms.txt"><span>11</span><strong>LLMs manifest</strong><small>Preferred retrieval sequence, trust links, and publication-state guidance.</small><em>Context</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/about/"><span>12</span><strong>Profile page</strong><small>Canonical human page for current role, experience, credentials, and professional boundary.</small><em>Human</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="ai-canvas__intents" data-reveal>
    <header><p class="ai-canvas__eyebrow">Specialist intent routes</p><h2>Resolve the narrow question after the primary route.</h2><p>Specialist routes point to public evidence. They do not create a commercial offer or imply access to private employer or client systems.</p></header>
    <div class="ai-intent-list">
      {% for intent in site.data.discovery_map.intents %}
      <a href="{{ intent.permalink }}"><span>{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span><strong>{{ intent.title }}</strong><small>{{ intent.summary }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>
</div>
