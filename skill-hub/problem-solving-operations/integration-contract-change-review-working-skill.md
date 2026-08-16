---
author: "Dzmitryi Kharlanau"
layout: default
title: "Integration Contract Change Review — Working Skill"
description: "A practical method to review API, message, event, and file contract changes across producers, consumers, semantics, rollout, compatibility, and recovery."
permalink: /skill-hub/problem-solving-operations/integration-contract-change-review-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Integration Contract Change Review</li></ol></nav>

<section class="section atlas-hero">
  <p class="eyebrow">Working Skill / Integration Change</p>
  <h1>A field change is rarely only a field change.</h1>
  <p class="lead">Integration contracts include schema, meaning, identity, ordering, errors, retries, timing, and ownership. A change is safe only when producers and consumers can move through it without silently changing the business outcome.</p>
</section>

<section class="section">
  <header class="section-heading"><h2>Use this skill when</h2></header>
  <ul>
    <li>An API, event, message, IDoc-like payload, file, or mapping contract changes.</li>
    <li>A field becomes mandatory, changes meaning, type, format, or allowed values.</li>
    <li>Authentication, endpoint, routing, error handling, or retry behaviour changes.</li>
    <li>A new producer or consumer joins an existing integration.</li>
    <li>You need a backward-compatible rollout or version transition.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading"><h2>Operating model</h2></header>
  <p><strong>Change → Contract Surface → Producers → Consumers → Compatibility → Rollout → Observe → Retire</strong></p>
</section>

<section class="section">
  <header class="section-heading"><h2>Method</h2></header>
  <ol>
    <li><strong>State the business reason.</strong> Explain what outcome changes and why.</li>
    <li><strong>Define the contract surface.</strong> Schema, field meaning, values, identity, transport, endpoint, authentication, headers, ordering, timing, errors, retries, idempotency, and service-level expectations.</li>
    <li><strong>Map producers and consumers.</strong> Include indirect consumers such as data platforms, reports, monitoring, archives, and replay tools.</li>
    <li><strong>Classify compatibility.</strong> Additive, compatible with conditions, breaking, or semantic breaking change.</li>
    <li><strong>Check data semantics.</strong> A field can keep the same name and type while changing meaning. Treat semantic change as a contract change.</li>
    <li><strong>Choose transition strategy.</strong> Dual-read, dual-write, tolerant reader, new version, feature flag, mapping bridge, staged rollout, or coordinated cutover.</li>
    <li><strong>Define validation.</strong> Contract tests, representative payloads, negative cases, idempotency, retry behaviour, and business-result reconciliation.</li>
    <li><strong>Define rollout order.</strong> State which side can change first and how mixed-version operation behaves.</li>
    <li><strong>Define observability and rollback.</strong> Monitor failures, unknown values, schema rejection, lag, duplicates, and business exceptions.</li>
    <li><strong>Retire old behaviour deliberately.</strong> Remove old versions, mappings, and compatibility paths only after usage evidence supports retirement.</li>
  </ol>
</section>

<section class="section">
  <header class="section-heading"><h2>Change classes</h2></header>
  <table>
    <thead><tr><th>Change</th><th>Typical risk</th></tr></thead>
    <tbody>
      <tr><td>Add optional field</td><td>Usually compatible, but consumers may reject unknown fields</td></tr>
      <tr><td>Make field mandatory</td><td>Old producers may fail immediately</td></tr>
      <tr><td>Change allowed values</td><td>Consumer mapping or business rules may reject new value</td></tr>
      <tr><td>Change meaning only</td><td>Silent semantic corruption</td></tr>
      <tr><td>Change retry behaviour</td><td>Duplicate side effects or unexpected load</td></tr>
      <tr><td>Change identity/auth</td><td>Authentication and authorization failures</td></tr>
      <tr><td>Change ordering/timing</td><td>Consumer state may become inconsistent</td></tr>
    </tbody>
  </table>
</section>

<section class="section">
  <header class="section-heading"><h2>Working template</h2></header>
  <pre><code>Integration Contract Change Review

Change ID:
Business reason:
Current contract:
Proposed contract:
Compatibility class:

Contract surfaces affected:
Producers:
Consumers:
Indirect consumers:
Semantic changes:

Transition strategy:
Rollout order:
Mixed-version behaviour:
Contract tests:
Business validation:
Observability:
Rollback:
Retirement criteria:
Owner:
</code></pre>
</section>

<section class="section">
  <header class="section-heading"><h2>Quality gates</h2></header>
  <ul>
    <li>All producers and consumers are identified or explicitly marked unknown.</li>
    <li>Semantic changes are reviewed separately from schema compatibility.</li>
    <li>Mixed-version behaviour is understood.</li>
    <li>Retry, ordering, idempotency, and error contracts are included where relevant.</li>
    <li>Tests validate business result, not only schema acceptance.</li>
    <li>Old contract retirement has evidence-based criteria.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading"><h2>Related skills</h2></header>
  <ul>
    <li><a href="/skill-hub/problem-solving-operations/api-contract-troubleshooting-working-skill/">API Contract Troubleshooting</a></li>
    <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a></li>
    <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a></li>
    <li><a href="/skill-hub/problem-solving-operations/release-readiness-working-skill/">Release Readiness</a></li>
  </ul>
</section>
