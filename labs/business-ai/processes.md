---
layout: default
title: "Enterprise Processes for Business AI — Business AI Lab"
description: "A process map for Business AI showing end-to-end stages, AI jobs, reusable patterns, technology families, and control points."
permalink: /labs/business-ai/processes/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - enterprise-processes
  - process-architecture
  - ai-patterns
---

{% assign process_map = site.data.labs.business_ai.process_map %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Processes</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / enterprise process map</p>
      <h1>Put AI inside a process.<br />Not beside it.</h1>
      <p>A domain tells us who owns a capability. A process tells us where work moves, where decisions happen, where systems exchange state, and where AI can actually change an outcome.</p>
      <a class="research-canvas__button" href="#process-list">Open process chains <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Process map</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ process_map.processes | size }}</strong><small>End-to-end processes</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>6+</strong><small>Cross-domain chains</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>1</strong><small>Rule: map the control point</small></div>
      <em>This is a working enterprise taxonomy, not a claim that one vendor owns these process names.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">route</span>
    <p><strong>Problem:</strong> AI use-case lists become shallow when they say “AI for Sales” or “AI for Finance” without naming the process step, input, decision, action, and control.</p>
    <p><strong>Process rule:</strong> attach AI to a stage or exception. Then connect it to the pattern, technology family, system of record, human role, and KPI.</p>
    <p><strong>Boundary rule:</strong> AI may interpret uncertainty. Exact rules, identities, approvals, hard constraints, and postings should remain explicit unless there is a very strong reason to do otherwise.</p>
    <a href="/labs/business-ai/patterns/">Open reusable patterns <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="process-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Process index</p>
      <h2>{{ process_map.processes | size }} working process chains.</h2>
      <p>Commercial, supply chain, manufacturing, finance, people, service, IT, legal, data, and knowledge work are all part of the same Business AI map.</p>
    </header>
    <div class="research-route-list">
      {% for process in process_map.processes %}
      <a href="#{{ process.id }}"><span>{{ process.stages | size }}</span><strong>{{ process.title }}</strong><small>{{ process.ai_jobs | first }} · Domains: {{ process.domains | join: ", " }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  {% for process in process_map.processes %}
  <section class="research-canvas__inventory" id="{{ process.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Process / {{ process.id }}</p>
      <h2>{{ process.title }}</h2>
      <p>{{ process.stages | join: " → " }}</p>
    </header>
    <div class="research-route-list">
      <a href="#{{ process.id }}"><span>AI</span><strong>AI jobs</strong><small>{{ process.ai_jobs | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/labs/business-ai/patterns/"><span>PAT</span><strong>Reusable patterns</strong><small>{{ process.pattern_ids | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/business-ai/technologies/"><span>TECH</span><strong>Technology families</strong><small>{{ process.technology_families | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#{{ process.id }}"><span>CTRL</span><strong>Control points</strong><small>{{ process.control_points | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      <a href="/labs/business-ai/domains/"><span>DOM</span><strong>Owning domains</strong><small>{{ process.domains | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Design sequence</p><h2>Turn a use case into architecture.</h2></div>
    <ol>
      <li><span>01</span><strong>Locate the step</strong><p>Name the exact stage, exception, handoff, or decision in the process chain.</p></li>
      <li><span>02</span><strong>Choose the pattern</strong><p>Separate extraction, retrieval, prediction, optimization, recommendation, workflow, and adaptive agent behavior.</p></li>
      <li><span>03</span><strong>Keep controls visible</strong><p>State which system owns identity, rules, approval, side effects, and audit evidence.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
