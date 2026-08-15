---
layout: default
title: "TRIZ Digital Framework — Method"
description: "A three-pass, nine-step method for turning digital contradictions into simpler architecture, process, and AI experiments."
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
      <h1>Understand.<br />Recompose.<br />Engineer.</h1>
      <p>I now use the framework in three passes and nine steps. The first pass makes the useful function and contradiction explicit. The second tries to separate the conflict and reuse existing resources. Only the third pass allocates software, process controls, integration, AI, and authority.</p>
    </div>
    <div class="research-canvas__signal" aria-label="Framework structure">
      <p>Method structure</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>3</strong><small>Passes</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>9</strong><small>Steps</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>6</strong><small>Separation operators</small></div>
      <em>Technology selection starts only after the contradiction, separation test, and resource scan.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">compare_arrows</span>
    <p><strong>Main rule:</strong> do not optimize the requested solution. Identify the useful function, the property that becomes worse, and the boundary that forces both properties to fight.</p>
    <p><strong>Design rule:</strong> operator first, pattern second, technology third.</p>
    <a href="/triz/workbench/">Open the practical workbench <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Pass A / Understand</p><h2>Find the useful function before redesigning the mechanism.</h2></header>
    <div class="research-route-list">
      <a href="#frame"><span>01</span><strong>Frame the job and useful function</strong><small>Observed behavior, outcome, actors, business objects, evidence, boundary, and current workaround.</small><i class="material-symbols-outlined" aria-hidden="true">crop_free</i></a>
      <a href="#ideal"><span>02</span><strong>Define the ideal result</strong><small>Useful outcome with minimal new coordination, duplicated state, manual work, and irreversible risk.</small><i class="material-symbols-outlined" aria-hidden="true">flag</i></a>
      <a href="#contradiction"><span>03</span><strong>Name the contradiction</strong><small>Write the useful property we improve and the useful property that becomes worse.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="frame" data-reveal>
    <header><p class="research-canvas__eyebrow">01 / Frame</p><h2>Describe the job, not the requested feature.</h2></header>
    <p><strong>Capture:</strong> observed behavior, useful function, business impact, affected actors, business objects, evidence, system boundary, frequency, and current workaround.</p>
    <p><strong>Avoid:</strong> “We need a chatbot”, “we need Kafka”, “we need another approval”, or “we need a dashboard”. Those are solution statements wearing a problem-shaped hat.</p>
    <p><strong>Useful form:</strong> “When X happens, actor Y cannot achieve Z for business object O because condition C. The current workaround causes cost or risk R.”</p>
  </section>

  <section class="research-canvas__inventory" id="ideal" data-reveal>
    <header><p class="research-canvas__eyebrow">02 / Ideal result</p><h2>Make complexity defend itself.</h2></header>
    <p>The ideal result is a pressure test. Describe the useful outcome with the least new coordination, state, ownership, data duplication, manual work, runtime cost, and irreversible risk.</p>
    <p>I use a simple qualitative idea of <strong>digital ideality</strong>: useful outcome and reliability should grow faster than the complexity tax. It is not a mathematical score. It is a way to notice when a solution “works” only because we added a new queue, platform, state store, approval team, and operating model.</p>
    <p>Example: “A valid order exception is resolved before delivery risk appears, without a new central queue and without giving an AI model broad permission to change commercial data.”</p>
  </section>

  <section class="research-canvas__inventory" id="contradiction" data-reveal>
    <header><p class="research-canvas__eyebrow">03 / Contradiction</p><h2>Both sides must be useful.</h2></header>
    <p>Use the form: <strong>If we improve A, B becomes worse.</strong> Then explain why A matters and why B also matters. If one side is obviously useless, it is not a contradiction; it is probably waste.</p>
    <p>When possible, sharpen it into a physical-style statement: “The same step should exist for high-risk cases and should not exist for routine low-risk cases.” This usually points toward a separation operator.</p>
    <div class="research-route-list">
      <a href="#"><span>C1</span><strong>Speed vs control</strong><small>Faster flow conflicts with independent verification or approval.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#"><span>C2</span><strong>Standardization vs flexibility</strong><small>One common process conflicts with valid local variation.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="#"><span>C3</span><strong>Automation vs accountability</strong><small>Less manual work conflicts with clear ownership of important decisions.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#"><span>C4</span><strong>Integration vs coupling</strong><small>Shared information conflicts with independent change and failure boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#"><span>C5</span><strong>Freshness vs cost</strong><small>Current information conflicts with source load, inference cost, or synchronization overhead.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
      <a href="#"><span>C6</span><strong>Autonomy vs trust</strong><small>Adaptive action conflicts with operational safety and explainable authority.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Pass B / Recompose</p><h2>Try to untie the conflict before choosing machinery.</h2></header>
    <div class="research-route-list">
      <a href="#separation"><span>04</span><strong>Apply separation operators</strong><small>Try time, condition, context, system level, authority, and representation.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a>
      <a href="#resources"><span>05</span><strong>Scan system resources</strong><small>Use existing information, time, history, structure, exceptions, policy, people, compute, and attention.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="#system-map"><span>06</span><strong>Map and generate system shapes</strong><small>Model objects, events, decisions, rules, state, delays, side effects, then apply transformation patterns.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="separation" data-reveal>
    <header><p class="research-canvas__eyebrow">04 / Separation</p><h2>Ask whether the conflict has to exist in the same place.</h2></header>
    <p>I use six digital separation operators: <strong>time, condition, context, system level, authority, and representation</strong>. They are deliberately more fundamental than architecture patterns.</p>
    <p>Examples: approve only high-risk cases; prepare evidence before the decision moment; keep global policy separate from local context; let an agent read broadly but write narrowly; give a consumer a derived signal instead of the full sensitive record.</p>
    <p><a href="/triz/operators/">Open the operators and examples.</a></p>
  </section>

  <section class="research-canvas__inventory" id="resources" data-reveal>
    <header><p class="research-canvas__eyebrow">05 / Resource scan</p><h2>Look for unused value inside the current system.</h2></header>
    <p>I scan eight resource groups: <strong>information, time, structure, history, negative signals, human judgment, policy/permission, and compute/attention</strong>.</p>
    <p>This changes the discussion. A queue is not only delay; it is also a time window for pre-validation. An exception is not only failure; it is also evidence. Logs are not only operations data; they can support replay. A rejected proposal can become an eval case. A role or permission boundary can solve an autonomy contradiction without weakening the whole system.</p>
  </section>

  <section class="research-canvas__inventory" id="system-map" data-reveal>
    <header><p class="research-canvas__eyebrow">06 / System shapes</p><h2>Model what moves, then force different options.</h2></header>
    <p>For digital work I map <strong>actors, business objects, events, decisions, rules, state, data, constraints, time, side effects, and evidence</strong>. Applications are attached to the model; they are not the model.</p>
    <p>Then I apply the <a href="/triz/patterns/">digital transformation patterns</a> and force materially different options. My default is at least two. For a complex problem, I prefer three: <strong>remove/simplify</strong>, <strong>deterministic redesign</strong>, and <strong>uncertainty-assisted redesign</strong>.</p>
    <p>Three cloud vendors implementing the same architecture are one option with three invoices.</p>
  </section>

  <section class="research-canvas__inventory" id="integration" data-reveal>
    <header><p class="research-canvas__eyebrow">IT lens</p><h2>Many contradictions are boundary mistakes.</h2></header>
    <div class="research-route-list">
      <a href="/triz/patterns/#separate-read-write"><span>RW</span><strong>Read vs write</strong><small>Broad visibility does not require broad mutation authority.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="/triz/patterns/#replace-sync-events"><span>EV</span><strong>Synchronous vs asynchronous</strong><small>Immediate coordination is useful until availability and latency become coupled.</small><i class="material-symbols-outlined" aria-hidden="true">bolt</i></a>
      <a href="/triz/patterns/#make-state-explicit"><span>ST</span><strong>Implicit vs explicit state</strong><small>Hidden state saves design work early and creates diagnosis work later.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/triz/patterns/#move-decision"><span>DX</span><strong>Central vs local decision</strong><small>Move a decision to the layer that owns the needed context and risk.</small><i class="material-symbols-outlined" aria-hidden="true">alt_route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Pass C / Engineer</p><h2>Allocate mechanism, authority, and evidence deliberately.</h2></header>
    <div class="research-route-list">
      <a href="#technology"><span>07</span><strong>Allocate technology and authority</strong><small>Rules, workflow, events, retrieval, models, agents, human judgment, and permission boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="#experiment"><span>08</span><strong>Run a falsifiable experiment</strong><small>Primary metric, counter-metric, scope, failure condition, rollback or redesign trigger.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#feedback"><span>09</span><strong>Close the feedback loop</strong><small>Observe outcome, failure modes, cost, latency, rework, and the next contradiction.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="technology" data-reveal>
    <header><p class="research-canvas__eyebrow">07 / Technology and authority</p><h2>Put uncertainty and permission in different boxes.</h2><p>Deterministic problem, deterministic mechanism. Uncertain problem, probabilistic mechanism with bounded authority.</p></header>
    <div class="research-route-list">
      <a href="#"><span>RULE</span><strong>Exact rule</strong><small>Code, configuration, schema, constraint, or policy.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#"><span>WF</span><strong>Known sequence</strong><small>Workflow, orchestration, or state machine.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#"><span>EVT</span><strong>Loose coordination</strong><small>Business event, queue, or pub/sub when consumers should react independently.</small><i class="material-symbols-outlined" aria-hidden="true">notifications_active</i></a>
      <a href="#"><span>RET</span><strong>Fresh knowledge</strong><small>Retrieval or typed read tool instead of model memory.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="/triz/ai/"><span>AI</span><strong>Interpretation</strong><small>Messy language, classification, synthesis, candidate generation, uncertain routing.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/triz/ai/#agent"><span>AG</span><strong>Unknown next step</strong><small>Bounded agent when the next useful action depends on evidence found during the task.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#"><span>H</span><strong>Value conflict or high-impact approval</strong><small>Accountable human when the remaining choice cannot be reduced to a stable rule.</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
    </div>
    <p><strong>Authority chain:</strong> read → propose → validate → approve → execute. Do not assume one component should own all five.</p>
  </section>

  <section class="research-canvas__inventory" id="experiment" data-reveal>
    <header><p class="research-canvas__eyebrow">08 / Experiment</p><h2>Test the contradiction, not the demo.</h2></header>
    <p>Each option gets a hypothesis with <strong>change, expected effect, primary metric, counter-metric, failure condition, and test scope</strong>. If the goal is speed, also measure control failure. If the goal is automation, also measure wrong actions and rework. If the goal is autonomy, measure unsafe attempts and unnecessary tool steps.</p>
    <p>Prefer reversible scope: replay, shadow mode, one process variant, one country, one interface, one user group, or one low-risk action class.</p>
  </section>

  <section class="research-canvas__inventory" id="feedback" data-reveal>
    <header><p class="research-canvas__eyebrow">09 / Feedback</p><h2>The new system should reveal its next contradiction.</h2></header>
    <p>For software: traces, metrics, logs, error classes, latency, retries, and dependency behavior. For processes: cycle time, waiting time, rework, exception rate, manual touches, compliance, and outcome quality. For AI: task success, evidence quality, tool errors, unsafe attempts, cost, latency, escalation, and trajectory quality.</p>
    <p>The loop does not end because the project went live. It ends when we have enough evidence to keep the design, revise it, or state the next contradiction clearly. Systems are annoyingly committed to having a sequel.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
