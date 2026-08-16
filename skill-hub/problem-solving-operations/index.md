---
author: "Dzmitryi Kharlanau"
layout: default
title: "Problem Solving & Operations Skills"
description: "Cross-domain working skills for troubleshooting, evidence collection, process deviations, data reconciliation, procedures, incidents, root cause analysis, and operational improvement."
permalink: /skill-hub/problem-solving-operations/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li aria-current="page">Problem Solving &amp; Operations</li></ol></nav>

<section class="section atlas-hero">
  <p class="eyebrow">Skill Hub / Problem Solving &amp; Operations</p>
  <h1>Diagnose the system, not the brand name.</h1>
  <p class="lead">A failure can happen in SAP, a SaaS product, an API, a spreadsheet, a batch job, or a custom application. The basic reasoning is often the same: define the symptom, collect evidence, isolate the failing layer, act safely, and validate the result.</p>
</section>

<section class="section">
  <header class="section-heading"><h2>The operating model</h2></header>
  <p><strong>Situation → Skill → Evidence → Decision → Action → Validation → Reuse</strong></p>
  <p>The core Skill should be product-neutral. A domain adapter can add specific tools, logs, transactions, APIs, or checks. This keeps the reasoning reusable while still allowing deep technical work.</p>
  <pre><code>Evidence-Driven Troubleshooting
├─ Browser / UI adapter
├─ API / Integration adapter
├─ Database adapter
├─ SAP adapter
├─ Cloud / Platform adapter
└─ File / Data adapter
</code></pre>
</section>

<section class="section">
  <header class="section-heading"><h2>Core skills</h2></header>
  <div class="topic-grid">
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/">Evidence-Driven Troubleshooting</a></h3><p>Reproduce a problem, identify the first failing layer, test hypotheses, and avoid random changes.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/data-reconciliation-working-skill/">Data Reconciliation</a></h3><p>Compare two or more datasets, explain differences, classify exceptions, and produce a controlled reconciliation result.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/process-deviation-analysis-working-skill/">Process Deviation Analysis</a></h3><p>Find the first point where an actual process diverged from expected behavior and explain why.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/procedure-design-working-skill/">Procedure / Runbook Design</a></h3><p>Turn repeated operational work into an executable procedure with evidence, decision points, stop conditions, rollback, and ownership.</p></div>
  </div>
</section>

<section class="section">
  <header class="section-heading"><h2>How skills compose</h2></header>
  <p>Skills should call each other instead of copying the same reasoning.</p>
  <pre><code>Incident
  ↓
Evidence-Driven Troubleshooting
  ├─ Data problem → Data Reconciliation
  ├─ Wrong business route → Process Deviation Analysis
  ├─ Recurring cause → Root Cause Analysis
  └─ Repeated recovery → Procedure / Runbook Design
                         ↓
                 Operational Knowledge Capture
</code></pre>
</section>

<section class="section">
  <header class="section-heading"><h2>Domain adapters</h2></header>
  <table>
    <thead><tr><th>Domain</th><th>Typical evidence and tools</th><th>Core reasoning stays the same</th></tr></thead>
    <tbody>
      <tr><td>Web / SaaS</td><td>Browser console, network trace, application logs, identity, feature flags</td><td>Reproduce → isolate layer → test → validate</td></tr>
      <tr><td>API / Integration</td><td>Request, response, correlation ID, contract, mapping, queue, retry history</td><td>Trace the first failed boundary</td></tr>
      <tr><td>Data / Files</td><td>Schema, keys, row counts, nulls, duplicates, totals, transformations</td><td>Compare expected and actual data state</td></tr>
      <tr><td>Cloud / Platform</td><td>Deployment history, service health, metrics, logs, permissions, configuration</td><td>Separate change, platform, application, and dependency failures</td></tr>
      <tr><td>SAP</td><td>Business documents, application logs, traces, jobs, queues, configuration, master data</td><td>Same core method plus SAP-specific diagnostic branches</td></tr>
    </tbody>
  </table>
</section>

<section class="section">
  <header class="section-heading"><h2>Related skills</h2></header>
  <ul>
    <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a></li>
    <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a></li>
    <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a></li>
    <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a></li>
    <li><a href="/labs/templates/">Operational Templates</a></li>
    <li><a href="/skill-hub/skill-template-contract/">Skill → Template Contract</a></li>
  </ul>
</section>
