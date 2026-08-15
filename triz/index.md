---
layout: default
title: "TRIZ for Digital Systems"
description: "A contradiction-driven framework for solving IT, business-process, integration, data, and AI problems without starting from a product or buzzword."
permalink: /triz/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, problem-solving, architecture, business-processes, ai, systems-thinking]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li aria-current="page">TRIZ for Digital Systems</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / digital systems</p>
      <h1>Do not start with a solution.<br />Start with the contradiction.</h1>
      <p>I use TRIZ here as a reasoning engine for IT systems, business processes, integrations, data, and AI. The classical ideas are useful, but digital systems need their own working language: state, authority, time, events, data representation, uncertainty, feedback, and system levels.</p>
      <a class="research-canvas__button" href="/triz/workbench/">Open the workbench <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Framework summary">
      <p>Working model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>3</strong><small>Reasoning passes</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>9</strong><small>Method steps</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>6 + 12</strong><small>Operators + patterns</small></div>
      <em>Draft framework. Durable method and dated technology signals are kept separate.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">balance</span>
    <p><strong>Core idea:</strong> many digital problems are unresolved contradictions: faster but safer, standard but flexible, automated but accountable, integrated but loosely coupled, autonomous but trusted.</p>
    <p><strong>Working rule:</strong> operator first, pattern second, technology third.</p>
    <a href="/triz/framework/">Read the full method <span class="material-symbols-outlined" aria-hidden="true">menu_book</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">The method</p><h2>Understand. Recompose. Engineer.</h2><p>The middle pass matters. It stops the framework from jumping directly from a contradiction to a favorite technology.</p></header>
    <div class="research-route-list">
      <a href="/triz/framework/#frame"><span>A1</span><strong>Frame the useful function</strong><small>Observed behavior, actors, business objects, evidence, impact, boundary.</small><i class="material-symbols-outlined" aria-hidden="true">crop_free</i></a>
      <a href="/triz/framework/#ideal"><span>A2</span><strong>Define the ideal result</strong><small>Improve outcome while keeping coordination, duplicated state, cost, exposure, and irreversible risk small.</small><i class="material-symbols-outlined" aria-hidden="true">flag</i></a>
      <a href="/triz/framework/#contradiction"><span>A3</span><strong>Name both useful sides</strong><small>If we improve A, B becomes worse. Explain why both still matter.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="/triz/framework/#separation"><span>B1</span><strong>Separate the conflict</strong><small>Try time, condition, context, system level, authority, and representation.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a>
      <a href="/triz/framework/#resources"><span>B2</span><strong>Scan existing resources</strong><small>Information, time, structure, history, negative signals, people, policy, compute, attention.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/triz/framework/#system-map"><span>B3</span><strong>Generate different system shapes</strong><small>Map objects, events, decisions, state, rules, evidence, delays, and side effects; then apply patterns.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/triz/framework/#technology"><span>C1</span><strong>Allocate mechanism and authority</strong><small>Rules, workflow, events, retrieval, models, agents, humans, and read/propose/validate/approve/execute boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="/triz/framework/#experiment"><span>C2</span><strong>Run a falsifiable experiment</strong><small>Primary metric, counter-metric, failure condition, reversible scope.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/triz/framework/#feedback"><span>C3</span><strong>Expose the next contradiction</strong><small>Observe outcome, failure modes, cost, rework, latency, and new constraints.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Toolbox</p><h2>Use a small set of moves deeply.</h2><p>I do not want another catalogue where the method is buried under its own terminology.</p></header>
    <div class="research-route-list">
      <a href="/triz/operators/"><span>OPS</span><strong>Separation operators + resources</strong><small>Six ways to untie a conflict and eight resource groups to inspect before adding machinery.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a>
      <a href="/triz/patterns/"><span>PAT</span><strong>Digital transformation patterns</strong><small>Twelve reusable moves around boundaries, state, events, exceptions, reversibility, authority, and observability.</small><i class="material-symbols-outlined" aria-hidden="true">transform</i></a>
      <a href="/triz/workbench/"><span>WB</span><strong>Practical workbench</strong><small>A workshop flow from evidence to options, complexity tax, authority chain, experiment, and structured output.</small><i class="material-symbols-outlined" aria-hidden="true">edit_note</i></a>
      <a href="/triz/failure-modes/"><span>FAIL</span><strong>False resolutions</strong><small>Ten ways a solution can move waiting, risk, state, responsibility, or complexity instead of removing it.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Domain lenses</p><h2>The mechanism changes. The reasoning spine stays.</h2></header>
    <div class="research-route-list">
      <a href="/triz/business-processes/"><span>BP</span><strong>Business processes</strong><small>Approvals, queues, handoffs, exceptions, process data, ownership, and end-to-end outcomes.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/triz/framework/#integration"><span>IT</span><strong>IT and integration</strong><small>Coupling, state, synchronous vs asynchronous flow, decision location, resilience, and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/triz/ai/"><span>AI</span><strong>AI and agents</strong><small>Autonomy, authority, privacy, cost, repeatability, MCP/A2A boundaries, and evaluation.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/triz/cases/"><span>EX</span><strong>Synthetic enterprise cases</strong><small>Sales, procurement, master data, integrations, global processes, and AI operations.</small><i class="material-symbols-outlined" aria-hidden="true">experiment</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Evolution</p><h2>Ask what recurring contradiction the system is trying to remove next.</h2></header>
    <div class="research-route-list">
      <a href="/triz/evolution/"><span>EVOL</span><strong>Digital evolution hypotheses</strong><small>Ten directional prompts: explicit state, condition-based flow, selective synchronization, contextual decisions, bounded autonomy, purpose-specific data, prevention, object graphs, adaptive edges, self-observation.</small><i class="material-symbols-outlined" aria-hidden="true">trending_up</i></a>
      <a href="/triz/signals/"><span>2026</span><strong>Current solution-space signals</strong><small>Dated notes on MCP, A2A, object-centric process data, simulation, AI-enabled process analysis, and GenAI observability.</small><i class="material-symbols-outlined" aria-hidden="true">radar</i></a>
    </div>
    <p>Evolution hypotheses are not maturity laws. A batch job, synchronous call, or human approval can still be the better design when it matches the contradiction.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Machine-readable layer</p><h2>The method is data too.</h2><p>An agent should not have to reconstruct the workflow from prose and vibes.</p></header>
    <div class="research-route-list">
      <a href="/datasets/triz-digital-framework/catalog.json"><span>CAT</span><strong>Framework catalog</strong><small>Passes, steps, operators, resources, contradiction types, allocation rules, authority model, risk tiers, metrics, and sources.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/datasets/triz-digital-framework/patterns.json"><span>PAT</span><strong>Pattern graph</strong><small>Patterns with triggers, risks, controls, relationships, and classical lineage.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/datasets/triz-digital-framework/reasoning-schema.json"><span>SCHEMA</span><strong>Reasoning contract</strong><small>JSON Schema for inspectable problem analysis and agent output.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/datasets/triz-digital-framework/cases.jsonl"><span>CASE</span><strong>Reasoning cases</strong><small>Problem → contradiction → operators → resources → options → authority → experiment examples.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Lineage</p><h2>Classic TRIZ remains a library, not a cage.</h2></header>
    <p>The existing <a href="/datasets/TRIZ-bytes/">TRIZ-bytes dataset</a> keeps the classical principles and techniques as a separate reference layer. This framework uses that lineage without forcing every digital problem through a one-to-one mapping with the traditional forty principles.</p>
    <p>Principles are reusable prompts. The digital framework is a decision process.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
