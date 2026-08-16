---
author: "Dzmitryi Kharlanau"
layout: default
title: "Failure Mode / Resilience Review — Working Skill"
description: "A cross-domain method to identify failure modes, detection gaps, containment, recovery, and resilience tests before production incidents expose them."
permalink: /skill-hub/problem-solving-operations/failure-mode-resilience-review-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Failure Mode / Resilience Review</li></ol></nav>

<section class="section atlas-hero">
  <p class="eyebrow">Working Skill / Resilience</p>
  <h1>Ask how it fails before production answers for you.</h1>
  <p class="lead">A resilient design is not a design that never fails. It is a design where important failures are understood, detected, contained, recoverable, and tested. The useful question is not only “can it work?” but also “what happens when one part does not?”</p>
</section>

<section class="section">
  <header class="section-heading"><h2>Use this skill when</h2></header>
  <ul>
    <li>Reviewing a new service, interface, workflow, data pipeline, batch process, or AI agent.</li>
    <li>Preparing a major release, migration, cutover, or architecture decision.</li>
    <li>A recurring incident shows that recovery or detection is weak.</li>
    <li>A dependency is external, asynchronous, rate-limited, or unreliable.</li>
    <li>You need to decide where monitoring, retries, fallback, or manual recovery are required.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading"><h2>Operating model</h2></header>
  <p><strong>Capability → Dependency → Failure Mode → Effect → Detection → Containment → Recovery → Test → Improvement</strong></p>
</section>

<section class="section">
  <header class="section-heading"><h2>Method</h2></header>
  <ol>
    <li><strong>Define the business capability.</strong> Describe the outcome that must survive failure, not only the technical component.</li>
    <li><strong>Map dependencies.</strong> Include systems, APIs, queues, data, identity, scheduling, people, configuration, and third-party services.</li>
    <li><strong>List realistic failure modes.</strong> Examples: timeout, wrong data, duplicate message, unavailable dependency, partial update, stale configuration, lost event, authorization failure, capacity saturation, or human handover gap.</li>
    <li><strong>Describe the effect.</strong> State what the user, process, data, or downstream system experiences.</li>
    <li><strong>Check detectability.</strong> Can the team distinguish the failure from normal delay? What signal, metric, log, reconciliation, or business exception exposes it?</li>
    <li><strong>Check containment.</strong> Determine whether the failure can create duplicates, inconsistent data, uncontrolled retries, incorrect documents, or cascading load.</li>
    <li><strong>Define recovery.</strong> Retry, resume, compensate, replay, reconcile, switch to fallback, or use a controlled manual procedure.</li>
    <li><strong>Define stop conditions.</strong> Some failures should stop automation instead of attempting recovery.</li>
    <li><strong>Test the failure.</strong> Use controlled simulation, dependency isolation, invalid data, timeout injection, queue backlog, or synthetic cases where safe.</li>
    <li><strong>Record improvements.</strong> Add monitoring, design changes, runbooks, ownership, or release gates based on evidence.</li>
  </ol>
</section>

<section class="section">
  <header class="section-heading"><h2>Review lenses</h2></header>
  <table>
    <thead><tr><th>Lens</th><th>Question</th></tr></thead>
    <tbody>
      <tr><td>Availability</td><td>What if a required component is unavailable?</td></tr>
      <tr><td>Latency</td><td>What if it answers too late rather than not at all?</td></tr>
      <tr><td>Integrity</td><td>Can failure leave partial, duplicate, or contradictory state?</td></tr>
      <tr><td>Ordering</td><td>What if messages or steps arrive in the wrong order?</td></tr>
      <tr><td>Capacity</td><td>What happens under backlog, burst, or sustained load?</td></tr>
      <tr><td>Identity</td><td>What happens when authentication or authorization changes?</td></tr>
      <tr><td>Configuration</td><td>Can environment drift produce silent behaviour change?</td></tr>
      <tr><td>Human recovery</td><td>Can an operator understand and safely recover the case?</td></tr>
    </tbody>
  </table>
</section>

<section class="section">
  <header class="section-heading"><h2>Working template</h2></header>
  <pre><code>Failure Mode / Resilience Review

Capability:
Business criticality:
Scope:
Dependencies:

Failure mode:
Trigger / condition:
Business effect:
Technical effect:
Detection signal:
Current containment:
Recovery path:
Stop condition:
Owner:

Test method:
Observed result:
Gap:
Improvement:
Validation:
Residual risk:
</code></pre>
</section>

<section class="section">
  <header class="section-heading"><h2>Quality gates</h2></header>
  <ul>
    <li>Failure modes cover data and business effects, not only infrastructure outages.</li>
    <li>Detection is specific enough to distinguish failure from normal waiting.</li>
    <li>Retries are checked for duplicate and side-effect risk.</li>
    <li>Recovery has an owner and a validated procedure.</li>
    <li>Critical failure modes are tested before release where feasible.</li>
    <li>Residual risk is explicit rather than hidden behind “monitor closely”.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading"><h2>Related skills</h2></header>
  <ul>
    <li><a href="/skill-hub/problem-solving-operations/service-dependency-mapping-working-skill/">Service Dependency Mapping</a></li>
    <li><a href="/skill-hub/problem-solving-operations/end-to-end-flow-trace-working-skill/">End-to-End Flow Trace</a></li>
    <li><a href="/skill-hub/problem-solving-operations/release-readiness-working-skill/">Release Readiness</a></li>
    <li><a href="/skill-hub/problem-solving-operations/cutover-hypercare-control-working-skill/">Cutover &amp; Hypercare Control</a></li>
  </ul>
</section>
