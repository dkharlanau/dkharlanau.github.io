---
layout: default
title: "TRIZ for Business Processes"
description: "A contradiction-driven way to redesign approvals, handoffs, queues, exceptions, ownership, and process controls."
permalink: /triz/business-processes/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, business-processes, process-design, process-mining, automation]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Business Processes</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / business processes</p>
      <h1>A process problem is often<br />a coordination contradiction.</h1>
      <p>Business processes become slow for understandable reasons: controls were added, ownership was split, exceptions grew, systems stayed separate, and people learned local workarounds. I use TRIZ to ask which useful property each complication protects before removing it.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Process system map</p><h2>Model more than boxes and arrows.</h2></header>
    <p>For each process I capture <strong>business objects, events, decisions, actors, rules, states, handoffs, evidence, waiting time, exceptions, and outcome</strong>. Applications are attached to that model, not used as the model itself.</p>
    <p>Object-centric data is useful here because one real process can involve an order, delivery, invoice, customer, approval, task, and message at the same time. A single case ID can hide those relationships.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Common contradictions</p><h2>Why the process became complicated.</h2></header>
    <div class="research-route-list">
      <a href="#"><span>B1</span><strong>Control vs flow</strong><small>Approvals reduce risk and increase queue time.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#"><span>B2</span><strong>Common process vs local reality</strong><small>One standard improves consistency while local products, markets, and regulations create valid variation.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#"><span>B3</span><strong>Specialization vs handoffs</strong><small>Expert teams improve decision quality and increase coordination overhead.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
      <a href="#"><span>B4</span><strong>Automation vs exception handling</strong><small>Straight-through flow saves effort until exceptions become invisible or expensive.</small><i class="material-symbols-outlined" aria-hidden="true">automation</i></a>
      <a href="#"><span>B5</span><strong>Local KPI vs end-to-end outcome</strong><small>A team can improve its own metric while making the total process worse.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#"><span>B6</span><strong>Early decision vs incomplete evidence</strong><small>Fast decisions happen before all information exists; complete evidence arrives after the useful moment.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Redesign moves</p><h2>Remove coordination before automating coordination.</h2></header>
    <div class="research-route-list">
      <a href="/triz/patterns/#collapse-handoffs"><span>P11</span><strong>Collapse handoffs</strong><small>Automate evidence gathering and pre-validation; keep only independent decisions.</small><i class="material-symbols-outlined" aria-hidden="true">merge</i></a>
      <a href="/triz/patterns/#make-state-explicit"><span>P04</span><strong>Make work state visible</strong><small>Turn hidden waiting into explicit state, owner, age, and reason.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/triz/patterns/#exception-signal"><span>P06</span><strong>Structure exceptions</strong><small>Capture exception class, context, resolution, and outcome so repeated work becomes evidence.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="/triz/patterns/#move-decision"><span>P07</span><strong>Move the decision</strong><small>Centralize stable policy and place contextual decisions closer to the actor who has the necessary information.</small><i class="material-symbols-outlined" aria-hidden="true">alt_route</i></a>
      <a href="/triz/patterns/#simulate-first"><span>P10</span><strong>Replay before redesign</strong><small>Use historical event data, process mining, or simulation to test where a proposed change would matter.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">AI in the process</p><h2>Automate uncertainty, not accountability.</h2></header>
    <p>AI is useful for reading unstructured documents, classifying requests, finding similar exceptions, summarizing evidence, proposing routes, and preparing decisions. It can reduce the information-gathering part of an approval without pretending the approval itself never mattered.</p>
    <p>For high-impact changes I prefer a prepared-change pattern: AI gathers evidence and proposes an exact action; deterministic rules validate it; the accountable actor approves when required; execution is logged and preferably reversible.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Process experiment</p><h2>Measure outcome and counter-metric together.</h2></header>
    <p>Typical pairs: cycle time + control failure; automation rate + exception quality; touchless rate + rework; local productivity + end-to-end lead time; AI assistance + wrong-route rate; fewer approvals + post-fact correction cost.</p>
    <p>The purpose is not to prove that the new design is modern. It is to show that one side of the contradiction improved without silently breaking the other.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
