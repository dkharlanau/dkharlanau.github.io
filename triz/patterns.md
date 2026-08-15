---
layout: default
title: "TRIZ Digital Patterns"
description: "Twelve reusable transformation patterns for IT architecture, business processes, integrations, data, and AI systems."
permalink: /triz/patterns/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, patterns, architecture, business-processes, ai]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Patterns</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / transformation patterns</p>
      <h1>Patterns are prompts for redesign.<br />Not answers.</h1>
      <p>These patterns borrow the spirit of classic TRIZ: separate conflicting properties, change time or space, use feedback, prepare before failure, and reuse what already exists. I translate that logic into digital systems instead of copying the classical list.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Pattern set</p><h2>Twelve moves I try before adding more machinery.</h2></header>
    <div class="research-route-list">
      <a href="#split-system"><span>P01</span><strong>Split the system by responsibility</strong><small>Separate parts that need different change speed, risk, ownership, or scale.</small><i class="material-symbols-outlined" aria-hidden="true">splitscreen</i></a>
      <a href="#move-uncertainty"><span>P02</span><strong>Move uncertainty to the edge</strong><small>Keep the core deterministic; interpret messy input before it reaches critical logic.</small><i class="material-symbols-outlined" aria-hidden="true">filter_alt</i></a>
      <a href="#separate-read-write"><span>P03</span><strong>Separate read from write</strong><small>Give broad context without giving broad mutation rights.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="#make-state-explicit"><span>P04</span><strong>Make state explicit</strong><small>Expose status, owner, timestamp, evidence, and transition instead of hiding them in code or memory.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#replace-sync-events"><span>P05</span><strong>Replace blocking coordination with events</strong><small>Publish a fact and let independent consumers react when synchronous coupling is the contradiction.</small><i class="material-symbols-outlined" aria-hidden="true">notifications_active</i></a>
      <a href="#exception-signal"><span>P06</span><strong>Turn exceptions into signals</strong><small>Do not only repair failure. Capture it as structured evidence for routing, learning, and prevention.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="#move-decision"><span>P07</span><strong>Move the decision to the right layer</strong><small>Put a decision where the required context, authority, and consequence are visible.</small><i class="material-symbols-outlined" aria-hidden="true">alt_route</i></a>
      <a href="#reversible-path"><span>P08</span><strong>Create a reversible path</strong><small>Prefer prepared changes, preview, dry-run, compensation, and rollback before irreversible execution.</small><i class="material-symbols-outlined" aria-hidden="true">undo</i></a>
      <a href="#separate-judgment"><span>P09</span><strong>Separate interpretation from accountability</strong><small>AI can propose; deterministic controls and accountable actors decide what is allowed to happen.</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
      <a href="#simulate-first"><span>P10</span><strong>Simulate before mutation</strong><small>Use replay, digital twin, test data, shadow mode, or what-if analysis before touching production state.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#collapse-handoffs"><span>P11</span><strong>Collapse handoffs, preserve controls</strong><small>Remove coordination steps that add no independent decision or risk reduction.</small><i class="material-symbols-outlined" aria-hidden="true">merge</i></a>
      <a href="#self-observation"><span>P12</span><strong>Design for self-observation</strong><small>Make the system emit the evidence needed to understand what happened and why.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
    </div>
  </section>

  <section id="split-system"><h2>P01 — Split the system by responsibility</h2><p><strong>Use when:</strong> one component is forced to serve incompatible ownership, release speed, scale, or risk profiles.</p><p><strong>Typical move:</strong> separate command/query, core/extension, transactional/analytical, common/local, or synchronous/asynchronous responsibility.</p><p><strong>Watch:</strong> segmentation can remove one contradiction and create ten interfaces. Split around stable responsibility, not around fashionable service sizes.</p></section>

  <section id="move-uncertainty"><h2>P02 — Move uncertainty to the edge</h2><p><strong>Use when:</strong> messy language, documents, incomplete input, or human intent is mixed into deterministic processing.</p><p><strong>Typical move:</strong> classify, extract, normalize, or ask for missing context first. Pass a typed result into the core process.</p><p><strong>AI fit:</strong> strong. This is one of the cleanest places for a model because interpretation is the actual job.</p></section>

  <section id="separate-read-write"><h2>P03 — Separate read from write</h2><p><strong>Use when:</strong> a user, service, or agent needs wide visibility but should have narrow authority.</p><p><strong>Typical move:</strong> broad read tools, narrow write tools, prepared change objects, approval, idempotent execution.</p><p><strong>AI fit:</strong> especially useful for agents. Investigation can be flexible while mutation stays bounded.</p></section>

  <section id="make-state-explicit"><h2>P04 — Make state explicit</h2><p><strong>Use when:</strong> work gets lost in mail, chat, memory, hidden flags, or implicit code paths.</p><p><strong>Typical move:</strong> create an explicit state model with owner, timestamp, transition reason, evidence, and allowed next states.</p><p><strong>Process effect:</strong> waiting and rework become measurable instead of anecdotal.</p></section>

  <section id="replace-sync-events"><h2>P05 — Replace blocking coordination with events</h2><p><strong>Use when:</strong> one system must know that something happened, but it does not need to block the producer.</p><p><strong>Typical move:</strong> publish a business event with stable semantics; consumers react independently.</p><p><strong>Watch:</strong> events do not remove consistency problems. They move them. Add idempotency, correlation, replay policy, monitoring, and ownership.</p></section>

  <section id="exception-signal"><h2>P06 — Turn exceptions into signals</h2><p><strong>Use when:</strong> teams repeatedly solve the same class of incident without the system becoming smarter.</p><p><strong>Typical move:</strong> structure exception type, context, decision, resolution, and outcome. Feed it into analytics, rules, knowledge, or eval datasets.</p><p><strong>AI fit:</strong> models can help classify messy exceptions, but the taxonomy and outcome measure should stay explicit.</p></section>

  <section id="move-decision"><h2>P07 — Move the decision to the right layer</h2><p><strong>Use when:</strong> a central component lacks local context, or a local component lacks enterprise policy.</p><p><strong>Typical move:</strong> separate policy from execution. Centralize stable constraints; localize contextual decisions.</p><p><strong>Question:</strong> who has the information, who carries the consequence, and who can explain the decision later?</p></section>

  <section id="reversible-path"><h2>P08 — Create a reversible path</h2><p><strong>Use when:</strong> the desired automation has high-impact side effects.</p><p><strong>Typical move:</strong> preview, dry-run, staged rollout, prepared change, compensation transaction, rollback, or expiry.</p><p><strong>AI fit:</strong> a model may prepare the action. Execution should require stronger deterministic checks as impact rises.</p></section>

  <section id="separate-judgment"><h2>P09 — Separate interpretation from accountability</h2><p><strong>Use when:</strong> an AI system is useful for reasoning but the business still needs ownership, policy, and traceability.</p><p><strong>Typical move:</strong> model proposes classification, evidence, option, or plan; software validates permissions and constraints; a human approves when the remaining conflict is a value judgment.</p></section>

  <section id="simulate-first"><h2>P10 — Simulate before mutation</h2><p><strong>Use when:</strong> the effect of a change is hard to predict and production feedback is expensive.</p><p><strong>Typical move:</strong> replay historical events, shadow mode, synthetic cases, process simulation, digital twin, what-if model, or sandbox execution.</p><p><strong>Watch:</strong> a simulation is only useful when assumptions and missing variables are visible.</p></section>

  <section id="collapse-handoffs"><h2>P11 — Collapse handoffs, preserve controls</h2><p><strong>Use when:</strong> several people touch work but only one real decision is made.</p><p><strong>Typical move:</strong> automate data gathering, pre-validation, routing, and evidence packaging. Keep only the independent approvals that reduce a real risk.</p><p><strong>Business-process warning:</strong> removing a visible approval while leaving informal approval in chat changes the diagram, not the process.</p></section>

  <section id="self-observation"><h2>P12 — Design for self-observation</h2><p><strong>Use when:</strong> diagnosis depends on adding logs after the failure or asking five teams what they saw.</p><p><strong>Typical move:</strong> traces, metrics, structured logs, business correlation IDs, process events, decision reason, tool trajectory, and outcome telemetry.</p><p><strong>Result:</strong> observability stops being an operations afterthought and becomes part of the solution design.</p></section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
