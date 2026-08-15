---
layout: default
title: "TRIZ Digital Framework — Method"
description: "An eight-step method for turning digital contradictions into architecture, process, and AI experiments."
permalink: /triz/framework/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, systems-thinking, architecture, problem-solving]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Framework</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / method</p>
      <h1>Make the conflict explicit.<br />Then redesign the system.</h1>
      <p>Digital projects often jump from a complaint directly to a tool. I prefer one extra piece of work first: describe what must improve and what becomes worse when we improve it. That contradiction is usually more useful than the initial feature request.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" id="frame" data-reveal>
    <header><p class="research-canvas__eyebrow">01 / Frame</p><h2>Describe the job, not the requested feature.</h2></header>
    <p><strong>Capture:</strong> observed behavior, business impact, affected actors, evidence, system boundary, frequency, and current workaround.</p>
    <p><strong>Avoid:</strong> “We need a chatbot”, “we need Kafka”, “we need another approval”, or “we need a dashboard”. Those are solution statements wearing a problem-shaped hat.</p>
    <p><strong>Useful form:</strong> “When X happens, actor Y cannot achieve Z because condition C. The current workaround causes cost or risk R.”</p>
  </section>

  <section class="research-canvas__inventory" id="ideal" data-reveal>
    <header><p class="research-canvas__eyebrow">02 / Ideal result</p><h2>Ask what would remain if complexity had to justify itself.</h2></header>
    <p>The ideal result is not fantasy. It is a pressure test. Describe the outcome with the least new coordination, state, ownership, data duplication, manual work, and runtime dependency.</p>
    <p>Example: “A valid order exception is resolved before delivery risk appears, without a new central queue and without giving an AI model permission to change the order.”</p>
  </section>

  <section class="research-canvas__inventory" id="contradiction" data-reveal>
    <header><p class="research-canvas__eyebrow">03 / Contradiction</p><h2>Write both sides of the conflict.</h2></header>
    <p>Use the form: <strong>If we improve A, B becomes worse.</strong> Then ask whether A and B really have to be controlled by the same component, actor, time window, data set, or rule.</p>
    <div class="research-route-list">
      <a href="#"><span>C1</span><strong>Speed vs control</strong><small>We want faster flow, but more control creates delay.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#"><span>C2</span><strong>Standardization vs flexibility</strong><small>We want one process, but local cases need different behavior.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="#"><span>C3</span><strong>Automation vs accountability</strong><small>We want less manual effort, but high-impact decisions need ownership and explanation.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#"><span>C4</span><strong>Integration vs coupling</strong><small>We want shared information, but direct dependencies make change and failure spread.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#"><span>C5</span><strong>Freshness vs cost</strong><small>We want current information, but constant synchronization, inference, or retrieval is expensive.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
      <a href="#"><span>C6</span><strong>Autonomy vs trust</strong><small>We want an agent to adapt, but broader freedom increases operational risk.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="system-map" data-reveal>
    <header><p class="research-canvas__eyebrow">04 / System map</p><h2>Model the things that actually move.</h2></header>
    <p>For digital work I map eight element types: <strong>actors, business objects, events, decisions, rules, data, constraints, and side effects</strong>. I add time because many contradictions disappear when actions do not have to happen at the same moment.</p>
    <p>Do not map only applications. A system diagram with twenty boxes and no business object, event, decision, or ownership is architecture theatre with good alignment.</p>
  </section>

  <section class="research-canvas__inventory" id="integration" data-reveal>
    <header><p class="research-canvas__eyebrow">IT lens</p><h2>Contradictions often sit at boundaries.</h2></header>
    <div class="research-route-list">
      <a href="/triz/patterns/#separate-read-write"><span>RW</span><strong>Read vs write</strong><small>One component may need broad visibility but narrow mutation rights.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="/triz/patterns/#replace-sync-events"><span>EV</span><strong>Synchronous vs asynchronous</strong><small>Immediate coordination is useful until availability and latency become coupled.</small><i class="material-symbols-outlined" aria-hidden="true">bolt</i></a>
      <a href="/triz/patterns/#make-state-explicit"><span>ST</span><strong>Implicit vs explicit state</strong><small>Hidden state saves design work early and creates diagnosis work later.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/triz/patterns/#move-decision"><span>DX</span><strong>Central vs local decision</strong><small>Move a decision to the layer that owns the needed context and risk.</small><i class="material-symbols-outlined" aria-hidden="true">alt_route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="technology" data-reveal>
    <header><p class="research-canvas__eyebrow">06 / Technology allocation</p><h2>Put uncertainty in the right place.</h2><p>I use a simple allocation rule: deterministic problem, deterministic mechanism. Uncertain problem, probabilistic mechanism with bounded authority.</p></header>
    <div class="research-route-list">
      <a href="#"><span>RULE</span><strong>Exact rule</strong><small>Use code, configuration, schema, constraint, or policy.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#"><span>WF</span><strong>Known sequence</strong><small>Use workflow or orchestration.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#"><span>EVT</span><strong>Loose coordination</strong><small>Use events when consumers should react without blocking the producer.</small><i class="material-symbols-outlined" aria-hidden="true">notifications_active</i></a>
      <a href="#"><span>RET</span><strong>Fresh knowledge</strong><small>Use retrieval or a typed read tool instead of model memory.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="/triz/ai/"><span>AI</span><strong>Interpretation</strong><small>Use AI for messy language, classification, synthesis, candidate generation, or uncertain routing.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/triz/ai/#agent"><span>AG</span><strong>Unknown next step</strong><small>Use a bounded agent only when the next useful action depends on evidence found during the task.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#"><span>H</span><strong>Value conflict or high-impact approval</strong><small>Keep a human decision where accountability cannot be reduced to a stable rule.</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="experiment" data-reveal>
    <header><p class="research-canvas__eyebrow">07 / Experiment</p><h2>Test the contradiction, not the demo.</h2></header>
    <p>Each option gets a small hypothesis: <strong>change, expected effect, counter-metric, and failure condition</strong>. The counter-metric is important. If the goal is speed, also measure control failure. If the goal is automation, also measure wrong actions and escalation quality.</p>
    <p>A useful experiment can fail quickly. A beautiful prototype that cannot disprove its own idea is just a sales meeting with better CSS.</p>
  </section>

  <section class="research-canvas__inventory" id="feedback" data-reveal>
    <header><p class="research-canvas__eyebrow">08 / Feedback</p><h2>Observe the new system as part of the design.</h2></header>
    <p>For software: traces, metrics, logs, error classes, latency, retries, and dependency behavior. For processes: cycle time, waiting time, rework, exception rate, manual touches, compliance, and outcome quality. For AI: task success, groundedness, tool errors, unsafe attempts, cost, latency, escalation, and trajectory quality.</p>
    <p>The loop ends only when the new design exposes its own new contradictions. Then we start again, because systems are rude like that.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
