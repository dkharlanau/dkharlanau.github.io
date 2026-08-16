---
author: "Dzmitryi Kharlanau"
layout: default
title: "Problem Solving & Operations Skills"
description: "Cross-domain working skills for dependency mapping, tracing, troubleshooting, integrations, identity, data, business rules, resilience, AI evaluation, releases, cutover, monitoring, and operational improvement."
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
  <p class="lead">A failure can happen in SAP, a SaaS product, an API, a spreadsheet, a batch job, or a custom application. The basic reasoning is often the same: understand dependencies and rules, trace the flow, isolate the failing boundary, act safely, validate the result, and improve the operating model.</p>
</section>

<section class="section">
  <header class="section-heading"><h2>The operating model</h2></header>
  <p><strong>Situation → Map → Trace → Diagnose → Decide → Change → Validate → Operate → Reuse</strong></p>
  <p>The core Skill should be product-neutral. A domain adapter can add specific tools, logs, transactions, APIs, or checks. This keeps the reasoning reusable while still allowing deep technical work.</p>
  <pre><code>Service Dependency Mapping
├─ Business Rule Ownership Analysis
└─ End-to-End Flow Trace
   └─ Evidence-Driven Troubleshooting
      ├─ API Contract Troubleshooting
      │  ├─ Authorization & Identity Diagnosis
      │  └─ Batch & Queue Troubleshooting
      ├─ Data Discovery & Mapping
      │  ├─ Data Reconciliation
      │  ├─ Data Migration Validation
      │  └─ Delta / Cutoff Control
      ├─ Configuration Drift Analysis
      └─ Process Deviation Analysis

Planned change
├─ Integration Contract Change Review
├─ Failure Mode / Resilience Review
├─ AI Evaluation & Guardrail Testing
└─ Release Readiness → Cutover & Hypercare Control
                         ↓
                 Operational Metrics & Alert Triage
</code></pre>
</section>

<section class="section">
  <header class="section-heading"><h2>Core skills</h2></header>
  <div class="topic-grid">
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/service-dependency-mapping-working-skill/">Service Dependency Mapping</a></h3><p>Map runtime dependencies, owners, failure impact, and health evidence behind one business outcome.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/business-rule-ownership-analysis-working-skill/">Business Rule Ownership Analysis</a></h3><p>Make business rules traceable across source, owner, data, enforcement points, exceptions, and change paths.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/end-to-end-flow-trace-working-skill/">End-to-End Flow Trace</a></h3><p>Follow one business object across systems and find the first boundary where evidence breaks.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/">Evidence-Driven Troubleshooting</a></h3><p>Reproduce a problem, identify the first failing layer, test hypotheses, and avoid random changes.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/api-contract-troubleshooting-working-skill/">API Contract Troubleshooting</a></h3><p>Trace caller, identity, route, schema, provider logic, dependencies, and consumer handling to find the first broken contract.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/authorization-identity-diagnosis-working-skill/">Authorization &amp; Identity Diagnosis</a></h3><p>Separate authentication, effective identity, propagation, resource scope, and action authorization before changing access.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/batch-queue-troubleshooting-working-skill/">Batch &amp; Queue Troubleshooting</a></h3><p>Trace scheduled and asynchronous work through states, retries, locks, acknowledgement, backlog, and throughput.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/data-discovery-mapping-working-skill/">Data Discovery &amp; Mapping</a></h3><p>Profile unfamiliar datasets, find keys and relationships, propose mappings, and validate them on real rows.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/data-reconciliation-working-skill/">Data Reconciliation</a></h3><p>Compare datasets, explain differences, classify exceptions, and produce a controlled reconciliation result.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/data-migration-validation-working-skill/">Data Migration Validation</a></h3><p>Prove migrated population, identity, relationships, transformations, values, and business usability.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/delta-cutoff-control-working-skill/">Delta / Cutoff Control</a></h3><p>Control incremental windows, watermarks, late arrivals, duplicates, replay, and business cutoffs.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/configuration-drift-analysis-working-skill/">Configuration Drift Analysis</a></h3><p>Compare effective environment state and prove which difference actually explains changed behavior.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/process-deviation-analysis-working-skill/">Process Deviation Analysis</a></h3><p>Find the first point where an actual process diverged from expected behavior and explain why.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/procedure-design-working-skill/">Procedure / Runbook Design</a></h3><p>Turn repeated operational work into an executable procedure with evidence, decisions, stop conditions, rollback, and ownership.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/decision-facilitation-working-skill/">Decision Facilitation</a></h3><p>Turn an unclear discussion into a decision or explicit deferment with evidence, trade-offs, owner, and next action.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/integration-contract-change-review-working-skill/">Integration Contract Change Review</a></h3><p>Review schema, semantics, producers, consumers, compatibility, rollout, mixed versions, tests, and retirement.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/failure-mode-resilience-review-working-skill/">Failure Mode / Resilience Review</a></h3><p>Identify realistic failure modes, detection gaps, containment, recovery, stop conditions, and resilience tests.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/ai-evaluation-guardrail-testing-working-skill/">AI Evaluation &amp; Guardrail Testing</a></h3><p>Test AI task quality, authority boundaries, tool use, failure handling, guardrails, and regression before release.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/release-readiness-working-skill/">Release Readiness</a></h3><p>Make a go/no-go decision from risk, evidence, dependencies, recovery, monitoring, ownership, and business readiness.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/cutover-hypercare-control-working-skill/">Cutover &amp; Hypercare Control</a></h3><p>Control production transition, checkpoints, stop decisions, validation, stabilization, and handover.</p></div>
    <div class="topic-card"><h3><a href="/skill-hub/problem-solving-operations/operational-metrics-alert-triage-working-skill/">Operational Metrics &amp; Alert Triage</a></h3><p>Translate alerts into business impact, correlate evidence, route ownership, recover safely, and tune monitoring.</p></div>
  </div>
</section>

<section class="section">
  <header class="section-heading"><h2>How skills compose</h2></header>
  <pre><code>Business outcome unclear or fragile
  ↓
Service Dependency Mapping + Business Rule Ownership Analysis
  ↓
End-to-End Flow Trace
  ↓
First failed boundary
  ├─ API → API Contract Troubleshooting
  │        ├─ identity → Authorization & Identity Diagnosis
  │        └─ async → Batch & Queue Troubleshooting
  ├─ data semantics → Data Discovery & Mapping → Data Reconciliation
  ├─ environment difference → Configuration Drift Analysis
  └─ business route → Process Deviation Analysis

Migration / Cutover
  ↓
Data Discovery & Mapping
  ↓
Data Migration Validation
  ↓
Delta / Cutoff Control
  ↓
Release Readiness
  ↓
Cutover & Hypercare Control
  ↓
Operational Metrics & Alert Triage

Planned integration change
  ↓
Integration Contract Change Review
  ↓
Failure Mode / Resilience Review
  ↓
Release Readiness

AI workflow
  ↓
AI Agent Authority Design
  ↓
AI Evaluation & Guardrail Testing
  ↓
Release Readiness
  ↓
Operational Metrics & Alert Triage

Recurring issue
  ↓
Root Cause Analysis
  ↓
Procedure / Runbook Design
  ↓
Operational Knowledge Capture
</code></pre>
</section>

<section class="section">
  <header class="section-heading"><h2>Domain adapters</h2></header>
  <table>
    <thead><tr><th>Domain</th><th>Typical evidence and tools</th><th>Core reasoning stays the same</th></tr></thead>
    <tbody>
      <tr><td>Web / SaaS</td><td>Browser console, network trace, application logs, identity, feature flags</td><td>Map → trace → isolate → validate</td></tr>
      <tr><td>API / Integration</td><td>Request, response, correlation ID, contract, mapping, queue, retry history</td><td>Trace boundaries and manage contract evolution</td></tr>
      <tr><td>Data / Files</td><td>Schema, keys, row counts, watermarks, nulls, duplicates, totals, transformations</td><td>Discover → map → reconcile → control delta → validate</td></tr>
      <tr><td>Cloud / Platform</td><td>Deployment history, service health, metrics, logs, permissions, configuration</td><td>Map dependencies → review failure modes → monitor outcomes</td></tr>
      <tr><td>AI / Agents</td><td>Evaluation cases, tool calls, authority gates, deterministic validation, regression results</td><td>Define authority → test guardrails → release with monitoring</td></tr>
      <tr><td>SAP</td><td>Business documents, application logs, traces, jobs, queues, configuration, master data</td><td>Same core method plus SAP-specific diagnostic branches</td></tr>
    </tbody>
  </table>
</section>

<section class="section">
  <header class="section-heading"><h2>Related skills</h2></header>
  <ul>
    <li><a href="/skill-hub/ai-assisted-analysis/ai-agent-authority-design-working-skill/">AI Agent Authority Design</a></li>
    <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a></li>
    <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a></li>
    <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a></li>
    <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a></li>
    <li><a href="/triz/">TRIZ for Digital Systems</a></li>
    <li><a href="/labs/reusable-data-procedures/">Reusable Data Procedures</a></li>
    <li><a href="/labs/templates/">Operational Templates</a></li>
    <li><a href="/skill-hub/skill-template-contract/">Skill → Template Contract</a></li>
  </ul>
</section>
