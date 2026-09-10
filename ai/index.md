---
layout: default
title: "AI Routing Hub — SAP Learning & AMS Optimization"
permalink: /ai/
description: "Machine-readable routing for two primary site jobs: SAP learning and assessment practice, or SAP AMS optimization, with evidence and publication-state boundaries."
last_modified_at: 2026-09-10
hide_global_cta: true
tags:
  - sap-learning
  - sap-ams
  - ai-discovery
  - agent-ready-web-profile
---

Before reusing a profile, dataset or generated answer, check the [Trust Center](/trust/) for source attribution, review boundaries, crawler policy and corrections.

<div class="ai-canvas">
  <header class="ai-canvas__hero" data-reveal>
    <div>
      <p class="ai-canvas__eyebrow">Public context / AI systems</p>
      <h1>Two jobs first.<br />Evidence second.</h1>
      <p>Classify the request as SAP learning/practice or SAP AMS optimization before entering the deeper MDG, integration, logistics, architecture, data or AI knowledge layers.</p>
      <div class="ai-canvas__actions">
        <a class="ai-canvas__button" href="/ai/focus-map.json">Open the focus map <span class="material-symbols-outlined" aria-hidden="true">route</span></a>
        <a class="ai-canvas__text-link" href="/ai/site-profile.json">Open ARWP profile <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
      </div>
    </div>
    <dl class="ai-canvas__model" aria-label="Public context model">
      <div><dt>01 / Focus</dt><dd>Learning and assessment practice, or AMS optimization.</dd></div>
      <div><dt>02 / Routing</dt><dd>Domain and intent maps select the relevant public source.</dd></div>
      <div><dt>03 / Evidence</dt><dd>Review state, datasets, sources and trust boundaries control what can be cited.</dd></div>
    </dl>
  </header>

  <section class="ai-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">policy</span>
    <p><strong>Publication state is authoritative.</strong> A route appearing in ARWP, the focus map or navigation does not make a draft or noindex page verified.</p>
    <a href="/legal/responsible-ai/">Read responsible AI boundaries <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="ai-canvas__sources" data-reveal>
    <header><p class="ai-canvas__eyebrow">Primary retrieval sources</p><h2>Choose the source in the right order.</h2><p>Start with the audience job, then follow the specialist routing and evidence chain.</p></header>
    <div class="ai-route-list">
      <a href="/ai/focus-map.json"><span>01</span><strong>Two-focus routing map</strong><small>Classifies a request as SAP learning/practice or SAP AMS optimization and declares current indexable versus review-gated entry points.</small><em>Focus</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/site-profile.json"><span>02</span><strong>Agent-Ready Web Profile</strong><small>Canonical inventory of web, data, retrieval, Agent Skills, MCP, identity and trust surfaces, with the two-focus extension.</small><em>ARWP</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/discovery-map.json"><span>03</span><strong>Specialist discovery map</strong><small>Routes a narrower SAP problem after the primary learning-versus-AMS choice is known.</small><em>Routing</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/markdown-clusters.json"><span>04</span><strong>Markdown cluster index</strong><small>Structure and retrieval eligibility across AI, course, AMS, Atlas, Skill Hub, datasets, tools and research pages.</small><em>Coverage</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/llms.txt"><span>05</span><strong>LLMs manifest</strong><small>Two-focus routing, preferred retrieval sequence, trust links and publication-state guidance.</small><em>Context</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="ai-canvas__sources ai-canvas__sources--supporting" data-reveal>
    <header><p class="ai-canvas__eyebrow">Supporting sources</p><h2>Use the deeper layer after routing.</h2><p>These endpoints provide identity, reasoning, evidence and implementation context without becoming extra top-level site promises.</p></header>
    <div class="ai-route-list">
      <a href="/ai/resume.yml"><span>06</span><strong>Resume / YAML</strong><small>Role fit, delivery scope, problem domains and structured skills.</small><em>Identity</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/professional-intelligence.json"><span>07</span><strong>Professional intelligence contract</strong><small>Readiness dimensions, decision chain, evidence levels, pressure routes and privacy boundaries for SAP Lead preparation.</small><em>Reasoning</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/principles.json"><span>08</span><strong>Consulting principles</strong><small>Operating heuristics for SAP AMS improvement, support knowledge, architecture and change design.</small><em>Method</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/datasets/manifest.json"><span>09</span><strong>Dataset manifest</strong><small>Published data material for AMS, agentic tooling and governance work.</small><em>Evidence</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/ai/public-portfolio.json"><span>10</span><strong>Public project map</strong><small>Machine-readable project projection with explicit roles, verification boundaries and public entry points.</small><em>Projects</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/about/"><span>11</span><strong>Profile page</strong><small>Canonical human page for identity, expertise, credentials and reference checks.</small><em>Identity</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/publications/"><span>12</span><strong>Publication register</strong><small>Public articles, SAP technical notes, architecture writing and reusable knowledge surfaces.</small><em>Evidence</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/agent-tools/"><span>13</span><strong>Agent tools</strong><small>Public agent-facing tools and contracts where a task needs a more specific machine interface.</small><em>Tools</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="ai-canvas__intents" data-reveal>
    <header><p class="ai-canvas__eyebrow">Specialist intent routes</p><h2>Resolve the narrow SAP question after the primary route.</h2><p>Each specialist intent keeps a business or operating problem close to its public evidence. These are subroutes, not new site pillars.</p></header>
    <div class="ai-intent-list">
      {% for intent in site.data.discovery_map.intents %}
      <a href="{{ intent.permalink }}"><span>{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span><strong>{{ intent.title }}</strong><small>{{ intent.summary }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>
</div>