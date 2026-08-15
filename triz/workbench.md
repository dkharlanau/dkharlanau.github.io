---
layout: default
title: "TRIZ Digital Workbench"
description: "A practical worksheet for turning an IT, business-process, integration, data, or AI problem into contradiction-driven options and a falsifiable experiment."
permalink: /triz/workbench/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, workshop, problem-solving, architecture, business-processes, ai]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Workbench</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / workbench</p>
      <h1>One problem in.<br />Several system shapes out.</h1>
      <p>This is the practical version of the framework. It is meant for architecture workshops, process redesign, incident patterns, requirement discussions, and AI use-case reviews. The output is not “the answer”. It is a small set of better-framed options that can be tested.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Input card</p><h2>Start with evidence that already exists.</h2></header>
    <p><strong>Observed behavior:</strong> what happens now, in plain language.</p>
    <p><strong>Useful function:</strong> what outcome the process or system must provide.</p>
    <p><strong>Actor and business object:</strong> who needs the result and what object changes state.</p>
    <p><strong>Business impact:</strong> delay, cost, quality, risk, lost revenue, compliance, manual effort, or poor decision quality.</p>
    <p><strong>Evidence:</strong> process data, transaction examples, logs, traces, queue age, errors, user reports, or measurements.</p>
    <p><strong>Constraints:</strong> policy, authorization, legal, financial, timing, integration, data residency, or operational limits.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Contradiction card</p><h2>Write the conflict so both sides sound useful.</h2></header>
    <p><strong>Template:</strong> “We need more A because …, but more A makes B worse because … . We still need B because … .”</p>
    <p>A weak contradiction is “speed vs bad process”. Nobody wants the bad process. A stronger one is “speed vs independent risk review”. Now both sides have a reason to exist, so the design problem becomes interesting.</p>
    <p><strong>Physical version:</strong> when possible, make it sharper: “The same step should exist for high-risk cases and should not exist for routine low-risk cases.” That often points directly to separation by condition.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Operator card</p><h2>Try separation before compromise.</h2></header>
    <div class="research-route-list">
      <a href="/triz/operators/#time"><span>O1</span><strong>Time</strong><small>Can preparation, validation, approval, execution, or correction happen at different moments?</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="/triz/operators/#condition"><span>O2</span><strong>Condition</strong><small>Can normal, exception, low-risk, high-risk, high-confidence, and low-confidence cases behave differently?</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="/triz/operators/#context"><span>O3</span><strong>Context</strong><small>Can common policy and local context be separated instead of mixed into one giant branch tree?</small><i class="material-symbols-outlined" aria-hidden="true">location_on</i></a>
      <a href="/triz/operators/#level"><span>O4</span><strong>System level</strong><small>Does the contradiction belong to the component, process, integration layer, platform, or enterprise policy?</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/triz/operators/#authority"><span>O5</span><strong>Authority</strong><small>Can read, propose, validate, approve, and execute be separated?</small><i class="material-symbols-outlined" aria-hidden="true">admin_panel_settings</i></a>
      <a href="/triz/operators/#representation"><span>O6</span><strong>Representation</strong><small>Can the consumer use a safe derived signal instead of full raw data?</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Resource card</p><h2>Use what is already inside the system.</h2></header>
    <p>Scan the eight resource groups from the <a href="/triz/operators/#resources">resource model</a>: information, time, structure, history, negative signals, human judgment, policy/permission, and compute/attention.</p>
    <p>Useful prompt: <strong>“What do we already have that is currently waste, waiting, noise, history, or an unused boundary?”</strong> An exception queue can become training/eval evidence. Waiting time can become a pre-validation window. A rejected action can become a control signal. An existing correlation ID can remove hours of incident archaeology.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Option generation</p><h2>Force different system shapes.</h2><p>Do not generate five versions of the same preferred solution. That is not exploration; it is a meeting ritual.</p></header>
    <div class="research-route-list">
      <a href="#"><span>A</span><strong>Remove or simplify</strong><small>What if a step, copy, handoff, sync call, or approval disappears because its useful function moves elsewhere?</small><i class="material-symbols-outlined" aria-hidden="true">remove_circle_outline</i></a>
      <a href="#"><span>B</span><strong>Deterministic redesign</strong><small>Can rules, workflow, eventing, state, policy, or data structure resolve the conflict without AI?</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#"><span>C</span><strong>Uncertainty-assisted redesign</strong><small>Where interpretation, search, prediction, or adaptive investigation remains after the deterministic shape is clean?</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
    </div>
    <p><strong>Default rule:</strong> produce at least two materially different options. For a complex problem, I prefer three: simpler boundary, deterministic redesign, and AI-assisted redesign. “Same architecture with a different vendor” does not count as a new option.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Option score</p><h2>Compare useful effect and complexity tax.</h2></header>
    <p>Score qualitatively, not with fake precision. I compare: <strong>useful outcome, reliability, reversibility, new coordination, duplicated state, operational load, cognitive load, data exposure, authority risk, and evidence quality</strong>.</p>
    <p>An option that performs slightly better but creates a new platform, new state store, new approval queue, and new operational team may have poor ideality. Sometimes the boring option is the inventive one because it removes machinery.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Experiment card</p><h2>Make the preferred option easy to disprove.</h2></header>
    <p><strong>Hypothesis:</strong> if we make change X, useful property A improves without unacceptable damage to property B.</p>
    <p><strong>Primary metric:</strong> the result we want to improve.</p>
    <p><strong>Counter-metric:</strong> the useful property that could become worse.</p>
    <p><strong>Failure condition:</strong> the threshold or observation that tells us to stop, roll back, or redesign.</p>
    <p><strong>Scope:</strong> shadow, replay, one process variant, one country, one interface, one user group, or a low-risk action class.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">AI / agent output</p><h2>Make the reasoning inspectable.</h2></header>
    <p>The agent should return structured output, not a polished essay that hides how it got there. The machine contract requires the useful function, contradiction, operator choices, resource scan, system map, options, technology allocation, authority boundary, experiment, risks, assumptions, and unknowns.</p>
    <div class="research-route-list">
      <a href="/datasets/triz-digital-framework/reasoning-schema.json"><span>SCHEMA</span><strong>Reasoning schema</strong><small>JSON Schema for a reusable problem-analysis result.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/datasets/triz-digital-framework/cases.jsonl"><span>CASES</span><strong>Reasoning examples</strong><small>Synthetic examples for retrieval, regression checks, and agent evaluation.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
