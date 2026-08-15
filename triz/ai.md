---
layout: default
title: "TRIZ for AI Systems"
description: "How to use contradiction-driven design for AI, agents, retrieval, tools, autonomy, controls, protocols, and evaluation."
permalink: /triz/ai/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, ai, agents, rag, evals, governance, mcp, a2a]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">AI</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / AI systems</p>
      <h1>Use AI for uncertainty.<br />Do not outsource the system boundary.</h1>
      <p>AI creates new solution space and new contradictions. More autonomy can reduce manual work and increase operational risk. More context can improve answers and increase privacy exposure. More reasoning can improve difficult cases and increase latency, cost, and diagnosis effort.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">AI contradiction map</p><h2>The useful questions are architectural.</h2></header>
    <div class="research-route-list">
      <a href="#"><span>A1</span><strong>Autonomy vs control</strong><small>The agent needs freedom to adapt, but broad tools and write access increase impact.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#"><span>A2</span><strong>Context vs privacy</strong><small>More context can improve quality, but increases data exposure and permission complexity.</small><i class="material-symbols-outlined" aria-hidden="true">privacy_tip</i></a>
      <a href="#"><span>A3</span><strong>Accuracy vs latency and cost</strong><small>More retrieval, reasoning, tools, or model calls can improve hard cases and slow the service.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#"><span>A4</span><strong>Flexibility vs repeatability</strong><small>Open-ended reasoning handles variation and makes regression testing harder.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#"><span>A5</span><strong>Personalization vs governance</strong><small>Local memory and adaptation can help users while weakening common policy and auditability.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#"><span>A6</span><strong>Tool power vs blast radius</strong><small>The more useful a tool is, the more carefully scope, preconditions, and side effects must be controlled.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="#"><span>A7</span><strong>Agent specialization vs coordination</strong><small>Narrow agents can improve ownership and quality while creating delegation, context, and observability overhead.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Allocation rule</p><h2>Give the model a job it can actually improve.</h2></header>
    <p><strong>Good AI territory:</strong> messy language, document understanding, semantic classification, evidence synthesis, candidate generation, uncertain routing, anomaly explanation, and deciding the next read action during an investigation.</p>
    <p><strong>Keep deterministic:</strong> identity, permission checks, exact calculations, mandatory thresholds, durable state, sequence guarantees, idempotency, policy enforcement, and execution preconditions.</p>
    <p><strong>Keep accountable:</strong> value conflicts, risk acceptance, high-impact commercial decisions, policy exceptions, and actions where responsibility cannot be reduced to a stable rule.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Authority operator</p><h2>Read, propose, validate, approve, execute.</h2><p>These are five different capabilities. One agent does not automatically need all five.</p></header>
    <div class="research-route-list">
      <a href="#"><span>R</span><strong>Read</strong><small>Inspect data, documents, process state, telemetry, and related evidence.</small><i class="material-symbols-outlined" aria-hidden="true">visibility</i></a>
      <a href="#"><span>P</span><strong>Propose</strong><small>Return classification, plan, candidate action, explanation, or prepared change.</small><i class="material-symbols-outlined" aria-hidden="true">lightbulb</i></a>
      <a href="#"><span>V</span><strong>Validate</strong><small>Check exact policy, authorization, preconditions, schema, limits, and business invariants in software.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#"><span>A</span><strong>Approve</strong><small>Use an accountable human or explicit policy decision when the remaining conflict is not deterministic.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#"><span>X</span><strong>Execute</strong><small>Use a narrow, auditable, preferably idempotent tool with the exact approved parameters.</small><i class="material-symbols-outlined" aria-hidden="true">play_arrow</i></a>
    </div>
    <p>This chain is a direct application of <a href="/triz/operators/#authority">separation by authority</a>. It is also a useful antidote to “the agent can call the API, therefore the agent should own the decision”.</p>
  </section>

  <section class="research-canvas__inventory" id="agent" data-reveal>
    <header><p class="research-canvas__eyebrow">Agent pattern</p><h2>Unknown next step → bounded agent.</h2><p>An agent is useful when the next useful read or analysis step depends on evidence discovered during the task. If the sequence is already known, a workflow is usually easier to test and operate.</p></header>
    <div class="research-route-list">
      <a href="#"><span>01</span><strong>Read-first</strong><small>Start with inspection tools. Do not give write access just because the framework makes it easy.</small><i class="material-symbols-outlined" aria-hidden="true">visibility</i></a>
      <a href="#"><span>02</span><strong>Budgets</strong><small>Bound model calls, tool calls, time, cost, and depth.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>
      <a href="#"><span>03</span><strong>Stop states</strong><small>Success, insufficient evidence, permission denied, unsafe action, budget exhaustion, and human escalation.</small><i class="material-symbols-outlined" aria-hidden="true">stop_circle</i></a>
      <a href="#"><span>04</span><strong>Prepared change</strong><small>Separate investigation from mutation. The agent prepares an exact action object first.</small><i class="material-symbols-outlined" aria-hidden="true">draft</i></a>
      <a href="#"><span>05</span><strong>Approval binding</strong><small>Bind approval to the exact target, parameters, preconditions, approver, and expiry.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#"><span>06</span><strong>Trajectory trace</strong><small>Record evidence, tool use, important decisions, failures, and stop reason without leaking secrets.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Protocols as boundaries</p><h2>MCP and A2A solve different integration problems.</h2></header>
    <p><strong>MCP:</strong> useful when an AI client or agent needs a shared, governed surface for tools, resources, and related capabilities. The 2026-07-28 revision moved the protocol core to stateless request/response, strengthened authorization, made discovery more cacheable, and moved long-running Tasks into the extension model.</p>
    <p><strong>A2A:</strong> useful when one agent delegates work to another agent that may be remote, specialized, implemented in another language, or owned by another team. It separates agent capability from one application or framework.</p>
    <p><strong>TRIZ rule:</strong> protocol interoperability does not solve accountability. MCP can standardize access to a powerful tool and A2A can standardize delegation to a powerful agent; neither tells the business who is allowed to approve the side effect.</p>
    <p>See the dated <a href="/triz/signals/">Signals 2026</a> page for current source links and revision notes.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">TRIZ moves for AI</p><h2>Resolve the contradiction before scaling the model.</h2></header>
    <div class="research-route-list">
      <a href="/triz/operators/#condition"><span>O2</span><strong>Route hard cases differently</strong><small>Use cheap deterministic or small-model flow for normal cases and deeper reasoning only when the condition requires it.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="/triz/operators/#authority"><span>O5</span><strong>Separate capability from authority</strong><small>Broad investigation can coexist with narrow mutation rights.</small><i class="material-symbols-outlined" aria-hidden="true">admin_panel_settings</i></a>
      <a href="/triz/operators/#representation"><span>O6</span><strong>Minimize exposed context</strong><small>Give the model the useful representation, not every raw field by default.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/triz/patterns/#simulate-first"><span>P10</span><strong>Shadow before execute</strong><small>Run the agent in replay, simulation, or observe-only mode before mutation.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/triz/patterns/#self-observation"><span>P12</span><strong>Trace the trajectory</strong><small>Make model, retrieval, tool, and workflow behavior observable.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Evaluation</p><h2>Measure both sides of the contradiction.</h2></header>
    <p>If AI reduces manual work, also measure wrong actions and escalation quality. If retrieval improves freshness, also measure latency and cost. If an agent solves more edge cases, also measure tool errors, unsafe attempts, loop length, and cases where it should have stopped.</p>
    <p>I keep three eval layers: <strong>outcome</strong> (did the task succeed?), <strong>evidence</strong> (was the answer supported?), and <strong>trajectory</strong> (did the system use allowed tools, permissions, and stop states correctly?).</p>
    <p>For production telemetry, shared GenAI semantic conventions are becoming more useful, but prompts, retrieval content, and tool arguments can contain sensitive data. Observability has its own context-vs-privacy contradiction, because apparently no useful feature is allowed to arrive without paperwork.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Current architecture signals</p><h2>Useful trends, without worshipping them.</h2></header>
    <p><strong>Stateless AI integration protocols:</strong> useful when shared tool capability needs normal infrastructure properties such as routing, caching, authorization, and scaling.</p>
    <p><strong>Agent interoperability:</strong> useful when expertise belongs to different services or teams and one monolithic agent would create ownership or implementation coupling.</p>
    <p><strong>Object-centric process data:</strong> useful for reasoning across orders, deliveries, invoices, approvals, cases, and other connected business objects instead of forcing every analysis into one case ID.</p>
    <p><strong>Simulation and shadow operation:</strong> useful when learning from the system before mutation is cheaper than recovering after mutation.</p>
    <p><strong>Observability and evals:</strong> AI systems need both software telemetry and task-quality evidence. Production debugging without either becomes expensive archaeology.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
