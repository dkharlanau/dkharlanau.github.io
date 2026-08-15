---
layout: default
title: "TRIZ Digital Cases"
description: "Synthetic examples of contradiction-driven problem solving across business processes, integration, master data, and AI-assisted operations."
permalink: /triz/cases/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, cases, architecture, business-processes, ai]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Cases</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / synthetic cases</p>
      <h1>The method becomes useful<br />when it changes a design decision.</h1>
      <p>These are synthetic cases. They are intentionally generic, so the reasoning can be reused without dragging client details into a public site. Each case starts from a contradiction and ends with an experiment.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 01</p><h2>Order exceptions: speed vs control.</h2></header>
    <p><strong>Problem:</strong> blocked or unusual orders wait in a shared queue. Teams want faster resolution but do not want automatic changes to commercial data.</p>
    <p><strong>Contradiction:</strong> more automation reduces waiting, but broader write authority increases financial and operational risk.</p>
    <p><strong>Patterns:</strong> P03 separate read/write, P06 exception as signal, P08 reversible path, P09 interpretation vs accountability.</p>
    <p><strong>Design:</strong> AI reads order context, related policy, and similar resolved exceptions. It classifies the issue and prepares a proposed action. Deterministic rules validate mandatory constraints. High-impact changes remain approval-bound.</p>
    <p><strong>Experiment:</strong> measure median exception age and manual investigation time; counter-metrics are wrong classification, rejected proposals, and post-change correction.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 02</p><h2>Integration load: freshness vs coupling.</h2></header>
    <p><strong>Problem:</strong> several consumers repeatedly call a transactional system for status updates. Fresh data is useful, but traffic and availability coupling grow with every consumer.</p>
    <p><strong>Contradiction:</strong> more frequent reads improve freshness and worsen load and dependency.</p>
    <p><strong>Patterns:</strong> P01 split responsibility, P05 replace blocking coordination with events, P12 self-observation.</p>
    <p><strong>Design:</strong> keep synchronous reads for cases that need immediate confirmation. Publish stable business events for state changes that many consumers can process independently.</p>
    <p><strong>Experiment:</strong> compare source-system request volume and consumer freshness; counter-metrics are missed events, duplicate handling, replay failures, and stale consumer state.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 03</p><h2>Master data approval: quality vs lead time.</h2></header>
    <p><strong>Problem:</strong> every request follows the same review chain although most issues are predictable missing fields or duplicate candidates.</p>
    <p><strong>Contradiction:</strong> more review improves quality and increases lead time.</p>
    <p><strong>Patterns:</strong> P02 move uncertainty to the edge, P11 collapse handoffs, P06 exception as signal.</p>
    <p><strong>Design:</strong> deterministic validation handles exact checks; similarity search or AI highlights likely duplicates and explains evidence; the approval chain is reserved for policy or value decisions that cannot be reduced to a stable rule.</p>
    <p><strong>Experiment:</strong> measure approval cycle time and first-pass completeness; counter-metrics are missed duplicates and downstream correction rate.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 04</p><h2>Global process: standardization vs local reality.</h2></header>
    <p><strong>Problem:</strong> a global template keeps growing country and business-unit branches. The process is technically standard and practically unreadable.</p>
    <p><strong>Contradiction:</strong> central standardization improves governance while valid local rules require variation.</p>
    <p><strong>Patterns:</strong> P01 split responsibility, P07 move the decision, P04 explicit state.</p>
    <p><strong>Design:</strong> separate stable global policy from local decision tables or extension points. Keep common states and evidence requirements, but allow local rules where the business consequence is genuinely local.</p>
    <p><strong>Experiment:</strong> measure number of global branches, local change lead time, and policy violations; counter-metric is divergence that should have remained global.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 05</p><h2>Operations agent: autonomy vs trust.</h2></header>
    <p><strong>Problem:</strong> an operations assistant can diagnose incidents using many systems, but giving it direct corrective actions creates a large blast radius.</p>
    <p><strong>Contradiction:</strong> broader autonomy can improve resolution time and makes mistakes more expensive.</p>
    <p><strong>Patterns:</strong> P03 separate read/write, P08 reversible path, P10 simulate first, P12 self-observation.</p>
    <p><strong>Design:</strong> start read-only. The agent gathers evidence, forms hypotheses, and selects the next diagnostic tool. It may prepare a bounded remediation object, but write execution requires deterministic preconditions and approval according to risk tier.</p>
    <p><strong>Experiment:</strong> run in shadow mode on historical and live incidents. Measure correct diagnosis and time saved; counter-metrics are unsafe proposals, excessive tool loops, missing evidence, and unnecessary escalation.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
