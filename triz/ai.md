---
layout: default
title: "TRIZ for AI Systems"
description: "How to use contradiction-driven design for AI, agents, retrieval, tools, autonomy, controls, and evaluation."
permalink: /triz/ai/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, ai, agents, rag, evals, governance]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">AI</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / AI systems</p>
      <h1>Use AI for uncertainty.<br />Do not outsource the system boundary.</h1>
      <p>AI creates new solution space, but also new contradictions. More autonomy can reduce manual work and increase operational risk. More context can improve answers and increase privacy exposure. More reasoning can improve difficult cases and increase latency and cost.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">AI contradiction map</p><h2>The useful questions are architectural.</h2></header>
    <div class="research-route-list">
      <a href="#"><span>A1</span><strong>Autonomy vs control</strong><small>The agent needs freedom to adapt, but write access and broad tools increase impact.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#"><span>A2</span><strong>Context vs privacy</strong><small>More context can improve quality, but increases data exposure and permission complexity.</small><i class="material-symbols-outlined" aria-hidden="true">privacy_tip</i></a>
      <a href="#"><span>A3</span><strong>Accuracy vs latency and cost</strong><small>More retrieval, reasoning, tools, or model calls can improve hard cases and slow the service.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#"><span>A4</span><strong>Flexibility vs repeatability</strong><small>Open-ended reasoning handles variation, but makes regression testing and explanation harder.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#"><span>A5</span><strong>Personalization vs governance</strong><small>Local memory and adaptation can help users while weakening common policy and auditability.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#"><span>A6</span><strong>Tool power vs blast radius</strong><small>The more useful a tool is, the more carefully its scope, preconditions, and side effects must be controlled.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Allocation rule</p><h2>Give the model a job it can actually improve.</h2></header>
    <p><strong>Good AI territory:</strong> messy language, document understanding, semantic classification, evidence synthesis, candidate generation, uncertain routing, anomaly explanation, and deciding the next read action during an investigation.</p>
    <p><strong>Bad AI territory:</strong> identity, permission checks, exact calculations, legal or financial thresholds, durable state, sequence guarantees, idempotency, mandatory policy, and irreversible side effects. Those belong in software or accountable process controls.</p>
  </section>

  <section class="research-canvas__inventory" id="agent" data-reveal>
    <header><p class="research-canvas__eyebrow">Agent pattern</p><h2>Unknown next step → bounded agent.</h2><p>An agent is useful when the next useful read or analysis step depends on evidence discovered during the task. If the sequence is already known, a workflow is usually easier to test and operate.</p></header>
    <div class="research-route-list">
      <a href="#"><span>01</span><strong>Read-first</strong><small>Start with tools that inspect state. Do not give write access just because the SDK makes it easy.</small><i class="material-symbols-outlined" aria-hidden="true">visibility</i></a>
      <a href="#"><span>02</span><strong>Budgets</strong><small>Bound model calls, tool calls, time, cost, and depth.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>
      <a href="#"><span>03</span><strong>Stop states</strong><small>Define success, insufficient evidence, permission denied, unsafe action, budget exhaustion, and human escalation.</small><i class="material-symbols-outlined" aria-hidden="true">stop_circle</i></a>
      <a href="#"><span>04</span><strong>Prepared change</strong><small>Separate investigation from mutation. The agent prepares an exact action object first.</small><i class="material-symbols-outlined" aria-hidden="true">draft</i></a>
      <a href="#"><span>05</span><strong>Approval binding</strong><small>Bind approval to the exact target, parameters, preconditions, approver, and expiry.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#"><span>06</span><strong>Trajectory trace</strong><small>Record evidence, selected tools, important decisions, failures, and stop reason without leaking secrets.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">TRIZ moves for AI</p><h2>Resolve the contradiction before scaling the model.</h2></header>
    <div class="research-route-list">
      <a href="/triz/patterns/#separate-read-write"><span>P03</span><strong>Broad read, narrow write</strong><small>Resolve autonomy vs control by separating investigation capability from mutation authority.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="/triz/patterns/#move-uncertainty"><span>P02</span><strong>Model at the uncertain edge</strong><small>Resolve flexibility vs repeatability by returning typed output into deterministic flow.</small><i class="material-symbols-outlined" aria-hidden="true">filter_alt</i></a>
      <a href="/triz/patterns/#simulate-first"><span>P10</span><strong>Shadow before execute</strong><small>Resolve learning vs operational risk by running the agent in observe-only or replay mode first.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/triz/patterns/#self-observation"><span>P12</span><strong>Trace the trajectory</strong><small>Resolve flexibility vs diagnosis by making tool and decision behavior observable.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Evaluation</p><h2>Measure both sides of the contradiction.</h2></header>
    <p>If AI reduces manual work, also measure wrong actions and escalation quality. If retrieval improves freshness, also measure latency and cost. If an agent solves more edge cases, also measure tool errors, unsafe attempts, loop length, and cases where it should have stopped.</p>
    <p>I keep three eval layers: <strong>outcome</strong> (did the task succeed?), <strong>evidence</strong> (was the answer supported?), and <strong>trajectory</strong> (did the system use allowed tools and stop correctly?).</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Current architecture signals</p><h2>Useful trends, without worshipping them.</h2></header>
    <p><strong>Typed tools and MCP:</strong> useful when models need governed access to external data and actions. A standard protocol can improve reuse, but it does not remove authorization or tool-design work.</p>
    <p><strong>Event-driven AI:</strong> useful when models or agents react to business events without blocking the source transaction. Events need stable semantics, correlation, replay, idempotency, and failure handling.</p>
    <p><strong>Object-centric process data:</strong> useful for reasoning across orders, deliveries, invoices, approvals, cases, and other connected business objects instead of forcing every analysis into one case ID.</p>
    <p><strong>Observability and evals:</strong> AI systems need both software telemetry and task-quality evidence. Production debugging without either becomes expensive archaeology.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
