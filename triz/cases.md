---
layout: default
title: "TRIZ Digital Cases"
description: "Synthetic examples of contradiction-driven problem solving across sales, procurement, master data, integration, process design, and AI-assisted operations."
permalink: /triz/cases/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [triz, cases, sap, sales, procurement, architecture, business-processes, ai]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/triz/">TRIZ</a></li><li aria-current="page">Cases</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">TRIZ / synthetic cases</p>
      <h1>The method becomes useful<br />when it changes a design decision.</h1>
      <p>These are synthetic cases. Some are SAP-flavored because enterprise logistics is a good place to test the method, but none describes a real client. Each case makes the contradiction, separation operator, resource, system shape, authority boundary, and experiment visible.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 01 / Sales</p><h2>Order exceptions: speed vs control.</h2></header>
    <p><strong>Problem:</strong> blocked or unusual orders wait in a shared queue. Teams want faster resolution but do not want automatic changes to commercial data.</p>
    <p><strong>Contradiction:</strong> more automation reduces waiting, but broader write authority increases financial and operational risk.</p>
    <p><strong>Operators:</strong> condition separates routine and high-impact exceptions; authority separates read, propose, approve, and execute.</p>
    <p><strong>Resources:</strong> order context, existing rules, previous resolved exceptions, queue age, rejection reasons.</p>
    <p><strong>Design:</strong> AI reads context and similar resolved exceptions, classifies the issue, and prepares a proposed action. Deterministic rules validate mandatory constraints. High-impact changes remain approval-bound.</p>
    <p><strong>Experiment:</strong> measure median exception age and manual investigation time; counter-metrics are wrong classification, rejected proposals, and post-change correction.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 02 / Integration</p><h2>Integration load: freshness vs coupling.</h2></header>
    <p><strong>Problem:</strong> several consumers repeatedly call a transactional system for status updates. Fresh data is useful, but traffic and availability coupling grow with every consumer.</p>
    <p><strong>Contradiction:</strong> more frequent reads improve freshness and worsen load and dependency.</p>
    <p><strong>Operators:</strong> time separates immediate confirmation from later reaction; system level moves fan-out coordination away from the source transaction.</p>
    <p><strong>Resources:</strong> existing business state changes, correlation IDs, consumer tolerance for delay, replayable history.</p>
    <p><strong>Design:</strong> keep synchronous reads for cases that need immediate confirmation. Publish stable business events for state changes that many consumers can process independently.</p>
    <p><strong>Experiment:</strong> compare source request volume and consumer freshness; counter-metrics are missed events, duplicate handling, replay failures, and stale consumer state.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 03 / Master Data</p><h2>Master data approval: quality vs lead time.</h2></header>
    <p><strong>Problem:</strong> every request follows the same review chain although most issues are predictable missing fields or duplicate candidates.</p>
    <p><strong>Contradiction:</strong> more review improves quality and increases lead time.</p>
    <p><strong>Operators:</strong> condition separates exact validation, ambiguous duplicate decisions, and policy exceptions; time moves deterministic checks before the human review moment.</p>
    <p><strong>Resources:</strong> validation rules, existing master data, duplicate history, rejected requests, steward decisions.</p>
    <p><strong>Design:</strong> deterministic validation handles exact checks; similarity search or AI highlights likely duplicates and explains evidence; the approval chain is reserved for policy or value decisions that cannot be reduced to a stable rule.</p>
    <p><strong>Experiment:</strong> measure approval cycle time and first-pass completeness; counter-metrics are missed duplicates and downstream correction rate.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 04 / Process Architecture</p><h2>Global process: standardization vs local reality.</h2></header>
    <p><strong>Problem:</strong> a global template keeps growing country and business-unit branches. The process is technically standard and practically unreadable.</p>
    <p><strong>Contradiction:</strong> central standardization improves governance while valid local rules require variation.</p>
    <p><strong>Operators:</strong> context separates common policy from local decision logic; system level separates enterprise constraints from local execution.</p>
    <p><strong>Resources:</strong> common business states, country rule ownership, existing local extensions, process-variant data.</p>
    <p><strong>Design:</strong> keep stable global states, evidence requirements, and policy common. Move contextual rules into governed local decision tables or extension points.</p>
    <p><strong>Experiment:</strong> measure global branch count, local change lead time, and policy violations; counter-metric is divergence that should have remained global.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 05 / AI Operations</p><h2>Operations agent: autonomy vs trust.</h2></header>
    <p><strong>Problem:</strong> an operations assistant can diagnose incidents using many systems, but giving it direct corrective actions creates a large blast radius.</p>
    <p><strong>Contradiction:</strong> broader autonomy can improve resolution time and makes mistakes more expensive.</p>
    <p><strong>Operators:</strong> authority separates investigation, proposal, validation, approval, and execution; time separates learning in shadow mode from later mutation.</p>
    <p><strong>Resources:</strong> telemetry, incident history, runbooks, read-only APIs, existing approval roles, rollback paths.</p>
    <p><strong>Design:</strong> start read-only. The agent gathers evidence, forms hypotheses, and selects the next diagnostic tool. It may prepare a bounded remediation object, but write execution requires deterministic preconditions and approval according to risk tier.</p>
    <p><strong>Experiment:</strong> run in shadow mode on historical and selected live incidents. Measure correct diagnosis and time saved; counter-metrics are unsafe proposals, excessive tool loops, missing evidence, and unnecessary escalation.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 06 / SAP Sales</p><h2>Credit-blocked sales order: release speed vs commercial risk.</h2></header>
    <p><strong>Problem:</strong> a sales order is blocked for credit-related review. Business wants the order released quickly, but the control exists to prevent unacceptable exposure.</p>
    <p><strong>Contradiction:</strong> faster release improves customer and delivery flow; weaker review can increase financial risk.</p>
    <p><strong>Operators:</strong> condition separates routine low-risk blocks from material exceptions; authority separates evidence preparation from release authority; representation can expose a concise credit-risk view rather than every finance detail.</p>
    <p><strong>Resources:</strong> order value, current credit status, overdue exposure, customer risk data, previous decisions, block age, existing release policy.</p>
    <p><strong>Design:</strong> deterministic rules calculate exact policy conditions. AI may summarize the order context, explain why the case is unusual, and retrieve similar approved or rejected cases. The final release follows explicit policy and accountable authority; the model does not invent a credit rule.</p>
    <p><strong>Experiment:</strong> measure block age and analyst preparation time; counter-metrics are incorrect releases, avoidable rejected proposals, and later credit correction.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Case 07 / SAP Procurement</p><h2>Purchase request approval: control vs queueing.</h2></header>
    <p><strong>Problem:</strong> routine purchase requests pass through the same approval effort as unusual or high-risk requests. The control is valid, but the queue becomes the process.</p>
    <p><strong>Contradiction:</strong> independent control reduces purchasing risk; applying the strongest control to every request increases lead time and manual effort.</p>
    <p><strong>Operators:</strong> condition separates low-risk straight-through cases from exceptions; time moves completeness and policy checks before approval; authority keeps segregation of duties where it actually matters.</p>
    <p><strong>Resources:</strong> value thresholds, category rules, supplier status, contract coverage, request history, rejected reasons, existing authorization roles.</p>
    <p><strong>Design:</strong> exact rules handle thresholds, mandatory fields, approved suppliers, and contract conditions. AI can interpret free-text justification or classify unusual requests, but it does not replace segregation-of-duties controls. Human review concentrates on real exceptions.</p>
    <p><strong>Experiment:</strong> measure request lead time and manual touches; counter-metrics are policy violations, wrong routing, rework, and post-approval correction.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">What these cases teach</p><h2>The recurring move is not “add AI”.</h2></header>
    <p>Across the seven cases, the recurring moves are more basic: separate normal from exception, move work before the critical moment, expose useful state, reuse history, move decisions to the right level, separate understanding from authority, and make the result observable.</p>
    <p>AI appears where interpretation or adaptive investigation remains after that redesign. Sometimes it is valuable. Sometimes the cleaner system shape makes it unnecessary, which is inconvenient for presentations and quite healthy for architecture.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
