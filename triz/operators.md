---
layout: default
title: "TRIZ Digital Operators"
description: "Six separation operators and a practical resource scan for resolving contradictions in IT, business processes, data, integration, and AI systems."
permalink: /triz/operators/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, contradictions, systems-thinking, architecture, business-processes, ai]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Operators</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / contradiction operators</p>
      <h1>Do not compromise too early.<br />First try to separate the conflict.</h1>
      <p>When two useful properties fight each other, the first reaction is often a compromise: a little slower, a little safer; a little more standard, a little more flexible. I prefer a different question first: do both properties really need to exist in the same place, time, condition, system level, authority boundary, or data representation?</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Separation test</p><h2>Six ways to untie a digital contradiction.</h2><p>These operators sit between the contradiction and the solution pattern. They help generate a new system shape before we start choosing products.</p></header>
    <div class="research-route-list">
      <a href="#time"><span>O1</span><strong>Separate by time</strong><small>Different behavior before, during, or after the critical moment.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#condition"><span>O2</span><strong>Separate by condition</strong><small>Use different behavior for normal flow, exception, risk class, confidence, or threshold.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#context"><span>O3</span><strong>Separate by context</strong><small>Keep local context local while common policy stays common.</small><i class="material-symbols-outlined" aria-hidden="true">location_on</i></a>
      <a href="#level"><span>O4</span><strong>Separate by system level</strong><small>Move the conflict from component to process, platform, or enterprise level.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#authority"><span>O5</span><strong>Separate by authority</strong><small>Read, propose, validate, approve, and execute do not need the same owner.</small><i class="material-symbols-outlined" aria-hidden="true">admin_panel_settings</i></a>
      <a href="#representation"><span>O6</span><strong>Separate by representation</strong><small>Use a derived signal, summary, score, or typed object instead of exposing the full raw input everywhere.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    </div>
  </section>

  <section id="time"><h2>O1 — Separate by time</h2><p><strong>Question:</strong> must both conflicting properties be active at the same moment?</p><p><strong>Moves:</strong> prepare before execution, approve only when the risk appears, cache stable knowledge, batch non-urgent work, validate asynchronously, or compensate after a reversible action.</p><p><strong>Example:</strong> collect and validate order evidence before an approver opens the case. Control remains; waiting moves out of the decision moment.</p></section>

  <section id="condition"><h2>O2 — Separate by condition</h2><p><strong>Question:</strong> does every case need the expensive or restrictive behavior?</p><p><strong>Moves:</strong> straight-through processing for low-risk cases, exception flow for ambiguous cases, stronger controls above a threshold, different model or retrieval depth for hard cases, human review only when confidence or impact requires it.</p><p><strong>Example:</strong> exact purchase rules handle normal requests; only unusual category, value, supplier, or policy combinations enter deeper review.</p></section>

  <section id="context"><h2>O3 — Separate by context</h2><p><strong>Question:</strong> which part is truly global and which part depends on local context?</p><p><strong>Moves:</strong> common core plus local rule, central policy plus local execution, shared schema plus local extension, global process state plus country-specific decision table.</p><p><strong>Watch:</strong> “local” is not a polite word for uncontrolled customization. Local behavior still needs an owner and a clear boundary.</p></section>

  <section id="level"><h2>O4 — Separate by system level</h2><p><strong>Question:</strong> are we trying to solve a process contradiction inside one application or one team?</p><p><strong>Moves:</strong> move a decision to a service or policy layer, move coordination from one transaction to an event layer, move duplicated logic into a shared capability, or move a local KPI discussion to the end-to-end process outcome.</p><p><strong>Example:</strong> source-system load is not always solved by a faster API. The better level may be a business event consumed by several systems.</p></section>

  <section id="authority"><h2>O5 — Separate by authority</h2><p><strong>Question:</strong> does the component that understands the situation also need permission to change it?</p><p><strong>Moves:</strong> broad read and narrow write, AI proposes while software validates, one actor approves while another executes, prepared-change objects, approval bound to exact parameters and expiry.</p><p><strong>AI fit:</strong> this is one of the most important operators for agents. Capability and authority are different design dimensions.</p></section>

  <section id="representation"><h2>O6 — Separate by representation</h2><p><strong>Question:</strong> does every consumer need the full raw data, or only the information needed for its decision?</p><p><strong>Moves:</strong> typed extraction, derived score, redacted view, event projection, summary with evidence links, tokenized identifier, or aggregated telemetry.</p><p><strong>Example:</strong> an AI assistant may need a structured risk summary and evidence references, not every sensitive field from every connected system.</p></section>

  <section class="research-canvas__inventory" id="resources" data-reveal>
    <header><p class="research-canvas__eyebrow">Resource scan</p><h2>Before adding a component, inspect what the system already has.</h2><p>Classic TRIZ pays attention to available resources. Digital systems have plenty of them; teams simply get used to ignoring them.</p></header>
    <div class="research-route-list">
      <a href="#"><span>R1</span><strong>Information</strong><small>Existing master data, transaction data, metadata, schemas, business keys, documents, and relationships.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#"><span>R2</span><strong>Time</strong><small>Idle periods, batch windows, approval waiting, lead time before the critical event, and deadlines.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>
      <a href="#"><span>R3</span><strong>Structure</strong><small>Existing APIs, events, queues, workflow states, extension points, caches, indexes, and boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#"><span>R4</span><strong>History</strong><small>Logs, traces, resolved incidents, past decisions, process events, corrections, and replayable data.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      <a href="#"><span>R5</span><strong>Negative signals</strong><small>Errors, rejects, retries, delays, overrides, and exceptions that can become structured feedback.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="#"><span>R6</span><strong>Human judgment</strong><small>Expert knowledge, accountable roles, review capacity, and decisions that still contain real value conflicts.</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
      <a href="#"><span>R7</span><strong>Policy and permission</strong><small>Existing rules, authorization scopes, segregation of duties, thresholds, ownership, and contracts.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#"><span>R8</span><strong>Compute and attention</strong><small>Cheap deterministic checks, caches, small models, large models, human attention, and expensive reasoning budgets.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Digital ideality</p><h2>Useful outcome should grow faster than complexity tax.</h2></header>
    <p>I use “ideality” as a design heuristic, not a fake-precise formula. A design is more attractive when useful outcome and reliability improve while coordination, duplicated state, cognitive load, runtime cost, and irreversible risk stay small.</p>
    <p><strong>Practical test:</strong> if the option solves the contradiction only by adding a new queue, a new copy of data, a new approval team, a new agent, and a new platform, the contradiction probably moved rather than disappeared.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Order of work</p><h2>Operator first, pattern second, technology third.</h2></header>
    <p>My preferred sequence is: name the contradiction → try the six separation operators → scan available resources → select transformation patterns → generate system-shape options → allocate technology and authority.</p>
    <p>This order matters. Otherwise “use AI”, “use events”, or “add workflow” arrives too early and quietly becomes the problem definition.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
