---
layout: default
title: "TRIZ Practice Templates"
description: "Reusable TRIZ-inspired templates for consultants, architects and developers working on process, SAP, integration, data and AI problems."
permalink: /triz/templates/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, templates, consulting, architecture, sap, integration, data, ai, development]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Practice Templates</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / practice templates</p>
      <h1>Use the framework.<br />Do not admire it.</h1>
      <p>These templates are made for real delivery work: workshops, change requests, incidents, architecture decisions, SAP extensions, integrations, data governance, and AI use cases. Open the smallest template that matches the problem, fill it with evidence, and stop when the decision is clear.</p>
      <a class="research-canvas__button" href="/datasets/triz-digital-framework/practice-template-pack/">Open the copy-ready pack <span class="material-symbols-outlined" aria-hidden="true">content_copy</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Template library summary">
      <p>Working pack</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>10</strong><small>Reusable templates</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>10–45</strong><small>Typical minutes per template</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>2</strong><small>Human + machine formats</small></div>
      <em>Draft library. Use synthetic or approved project information only on the public site.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">build</span>
    <p><strong>Working rule:</strong> choose the template by the decision you need to make, not by the technology currently being discussed.</p>
    <p><strong>Order:</strong> evidence → useful function → contradiction → separation → options → authority → experiment.</p>
    <a href="/triz/workbench/">Use the interactive workbench <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Start here</p>
      <h2>Pick the situation you have today.</h2>
      <p>The templates overlap on purpose. Real problems are rude enough to ignore our category boundaries.</p>
    </header>
    <div class="research-route-list">
      <a href="#problem-frame"><span>T01</span><strong>Problem Framing Card</strong><small>Use when the requirement is vague, the symptom is louder than the cause, or teams disagree on what the problem is.</small><i class="material-symbols-outlined" aria-hidden="true">crop_free</i></a>
      <a href="#contradiction"><span>T02</span><strong>Contradiction Canvas</strong><small>Use when two useful requirements conflict and the team is drifting toward compromise too early.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#process"><span>T03</span><strong>Business Process Redesign</strong><small>Use for approvals, queues, handoffs, rework, exception-heavy flows, and process automation.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#integration"><span>T04</span><strong>Integration Decision</strong><small>Use for API, event, queue, file, batch, sync/async, replay, idempotency, and ownership decisions.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#sap-change"><span>T05</span><strong>SAP Change and Extension</strong><small>Use before turning a requirement into configuration, custom code, developer extension, or side-by-side service.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="#ai"><span>T06</span><strong>AI Use-Case Boundary</strong><small>Use to separate interpretation from policy, authorization, durable state, approval, and execution.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="#incident"><span>T07</span><strong>Incident to Systemic Problem</strong><small>Use when the same incident returns and the workaround is quietly becoming architecture.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      <a href="#adr"><span>T08</span><strong>Contradiction-Driven ADR</strong><small>Use when several system shapes are plausible and the decision will survive longer than the meeting.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="#data"><span>T09</span><strong>Data and Master Data Governance</strong><small>Use for ownership, duplicate prevention, global/local data, quality rules, distribution, and stewardship.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#experiment"><span>T10</span><strong>Reversible Experiment</strong><small>Use when the design looks promising but evidence is too weak for a broad production decision.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="problem-frame" data-reveal>
    <header><p class="research-canvas__eyebrow">T01 / 10 minutes</p><h2>Problem Framing Card</h2><p>Before a workshop becomes a catalogue of requested features, make the useful function and boundary explicit.</p></header>
    <p><strong>Fill:</strong> observed behavior, useful function, actors, business object, impact, evidence, boundary, constraints, facts, assumptions, unknowns.</p>
    <p><strong>Leave with:</strong> one problem statement that both business and technical people can challenge.</p>
  </section>

  <section class="research-canvas__inventory" id="contradiction" data-reveal>
    <header><p class="research-canvas__eyebrow">T02 / 15 minutes</p><h2>Contradiction Canvas</h2><p>Useful when a team says “we need a balance”. Sometimes balance is right. Sometimes it is just a polite name for not redesigning the conflict.</p></header>
    <p><strong>Fill:</strong> property A, property B, why both matter, physical contradiction if possible, six separation tests.</p>
    <p><strong>Leave with:</strong> selected separation operators and a changed solution space.</p>
  </section>

  <section class="research-canvas__inventory" id="process" data-reveal>
    <header><p class="research-canvas__eyebrow">T03 / 45 minutes</p><h2>Business Process Redesign Canvas</h2><p>For process consultants and developers working on approval chains, queues, exceptions, handoffs, manual checks, or automation.</p></header>
    <p><strong>Fill:</strong> step purpose, state change, owner, waiting, exception, independent control, normal path, high-risk path, validation that can move earlier, machinery that can disappear.</p>
    <p><strong>Leave with:</strong> current friction map plus three target shapes: simplify, deterministic redesign, uncertainty-assisted redesign.</p>
  </section>

  <section class="research-canvas__inventory" id="integration" data-reveal>
    <header><p class="research-canvas__eyebrow">T04 / 30 minutes</p><h2>Integration Decision Template</h2><p>Use it before somebody writes “Kafka” or “REST” in the architecture box and the room collectively decides the hard part is finished.</p></header>
    <p><strong>Fill:</strong> command/query/event/bulk intent, immediate confirmation need, durable state owner, freshness, consistency, outage behavior, ordering, replay, duplicates, idempotency, retry, recovery, projection, security, observability.</p>
    <p><strong>Leave with:</strong> an integration shape and explicit failure semantics, not just middleware selection.</p>
  </section>

  <section class="research-canvas__inventory" id="sap-change" data-reveal>
    <header><p class="research-canvas__eyebrow">T05 / 30 minutes</p><h2>SAP Change and Extension Template</h2><p>For functional consultants and developers deciding whether a requirement belongs in standard configuration, an extension, or a side-by-side service.</p></header>
    <p><strong>Fill:</strong> missing outcome, current standard behavior, business objects, lifecycle events, stable vs contextual variation, configuration option, extension options, data/authorization boundary, upgrade impact, owner, reversibility.</p>
    <p><strong>Leave with:</strong> a standard-vs-extension decision that can survive design review.</p>
  </section>

  <section class="research-canvas__inventory" id="ai" data-reveal>
    <header><p class="research-canvas__eyebrow">T06 / 30 minutes</p><h2>AI Use-Case Boundary Template</h2><p>Use it when the phrase “AI can do this” appears before anyone has defined what “this” includes.</p></header>
    <p><strong>Fill:</strong> uncertain task, deterministic constraints, read/propose/validate/approve/execute chain, risk tier, tool allowlist, budgets, evidence, fallback, evaluation.</p>
    <p><strong>Leave with:</strong> a narrow AI responsibility and a clear non-AI control plane.</p>
  </section>

  <section class="research-canvas__inventory" id="incident" data-reveal>
    <header><p class="research-canvas__eyebrow">T07 / 30 minutes</p><h2>Incident to Systemic Problem Template</h2><p>For recurring incidents where the technical fix works, until the next Tuesday when the same system remembers it has hobbies.</p></header>
    <p><strong>Fill:</strong> useful function, timeline, expected/observed state, first deviation, evidence, negative signals, recovery action, state/ownership gaps, observability gap.</p>
    <p><strong>Leave with:</strong> failure chain, systemic options, and a preventive experiment.</p>
  </section>

  <section class="research-canvas__inventory" id="adr" data-reveal>
    <header><p class="research-canvas__eyebrow">T08 / 30 minutes</p><h2>Contradiction-Driven ADR</h2><p>A normal ADR records a decision. This version also records the contradiction that made the decision necessary.</p></header>
    <p><strong>Fill:</strong> context, contradiction, separation, simplify option, deterministic option, uncertainty-assisted option if relevant, consequences, assumptions, review triggers, evidence after implementation.</p>
    <p><strong>Leave with:</strong> an ADR that explains why the boundary exists and when it should be reconsidered.</p>
  </section>

  <section class="research-canvas__inventory" id="data" data-reveal>
    <header><p class="research-canvas__eyebrow">T09 / 45 minutes</p><h2>Data and Master Data Governance Template</h2><p>Use when quality, ownership, duplicates, distribution, or global/local variation are causing process friction.</p></header>
    <p><strong>Fill:</strong> decisions depending on data, semantic owner, steward, authority chain, global/local attributes, exact vs judgment rules, duplicate point, authoritative state, consumer views, distribution, reconciliation, quality metric and lead-time counter-metric.</p>
    <p><strong>Leave with:</strong> a governance design instead of “add another approval”.</p>
  </section>

  <section class="research-canvas__inventory" id="experiment" data-reveal>
    <header><p class="research-canvas__eyebrow">T10 / 20 minutes</p><h2>Reversible Experiment Template</h2><p>Useful after the design discussion, when everybody is suddenly certain their preferred option will work.</p></header>
    <p><strong>Fill:</strong> hypothesis, baseline, smallest reversible scope, primary metric, counter-metric, success threshold, stop condition, rollback, evidence, decision rule.</p>
    <p><strong>Leave with:</strong> a way to learn without converting a hypothesis directly into production architecture.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Formats</p><h2>Take the templates with you.</h2><p>The framework is more useful when it leaves this website.</p></header>
    <div class="research-route-list">
      <a href="/datasets/triz-digital-framework/practice-template-pack/"><span>MD</span><strong>Copy-ready Markdown pack</strong><small>Blank templates that can be copied into a ticket, Confluence page, Notion page, repository, ADR folder, or workshop notes.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/datasets/triz-digital-framework/practice-templates.json"><span>JSON</span><strong>Machine-readable template catalog</strong><small>Use cases, participants, questions, outputs, operators, patterns, and red flags for tools and agents.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/datasets/triz-digital-framework/reasoning-schema.json"><span>SCHEMA</span><strong>Reasoning output schema</strong><small>A stricter structured result when a tool or agent turns a filled template into analysis.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
