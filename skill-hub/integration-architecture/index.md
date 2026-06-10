---
layout: default
title: "Integration Architecture — Skill Group Index"
description: "Practical working skills for designing, owning, monitoring, and troubleshooting enterprise integrations in SAP and mixed landscapes."
permalink: /skill-hub/integration-architecture/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Integration Architecture</li>
  </ol>
</nav>

<section class="section atlas-hero">
  <p class="eyebrow">Skill Hub — Integration Architecture</p>
  <h1>Design, own, monitor, and fix integrations.</h1>
  <p class="lead">Practical working skills for integration architects and operators who need to make integration decisions, assign ownership, define contracts, handle failures, and build observability in SAP and mixed enterprise landscapes.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>What this group covers</h2>
  </header>
  <p>Integration Architecture skills bridge the gap between integration theory and operational reality. They help you decide between APIs and events, define who owns an interface, design error handling that actually works, and build monitoring that catches failures before business users do.</p>
  <p>These skills are applicable to SAP-centric landscapes (IDoc, RFC, OData, AIF) and to mixed landscapes with cloud middleware, SaaS APIs, and event brokers.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>When to use this group</h2>
  </header>
  <ul>
    <li>You are designing a new integration and need to choose a pattern, protocol, and contract.</li>
    <li>An existing integration fails repeatedly and no one knows who is responsible.</li>
    <li>You need to replace point-to-point connections with a more maintainable architecture.</li>
    <li>Business users report missing data before any technical alert fires.</li>
    <li>You are introducing events or APIs and need to define ownership, schema, and failure handling.</li>
    <li>A post-merger or platform consolidation requires an interface inventory and ownership cleanup.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Skills in this group</h2>
  </header>
  <div class="topic-grid">
    <div class="topic-card">
      <h3><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a></h3>
      <p>Assign clear ownership to every interface. Document who decides what. Prevent failures from sitting unresolved because no one is responsible.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a></h3>
      <p>Choose the right protocol, define contracts, handle versioning, auth, and rate limits for REST, OData, SOAP, and SAP OData services.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a></h3>
      <p>Decide whether an event should exist, who owns it, what its contract is, and how failures are monitored and handled.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a></h3>
      <p>Design monitoring and alerting so failures are detected before business impact, and diagnostics are fast and repeatable.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a></h3>
      <p>Design retry, dead letter, and escalation logic so transient failures recover safely and permanent failures escalate correctly.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/integration-architecture/data-mesh-working-skill/">Data Mesh</a></h3>
      <p>Apply data mesh principles to SAP and enterprise landscapes: identify domains, define data products, assign ownership, choose integration patterns.</p>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Recommended path through this group</h2>
  </header>
  <ol>
    <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — Start here if your landscape has unclear responsibilities.</li>
    <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Use when designing or reviewing synchronous integrations.</li>
    <li><a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a> — Use when decoupling systems or replacing polling.</li>
    <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — Use to build or improve monitoring.</li>
    <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — Use to make integrations resilient.</li>
    <li><a href="/skill-hub/integration-architecture/data-mesh-working-skill/">Data Mesh</a> — Use for strategic data architecture and domain-driven data ownership.</li>
  </ol>
</section>

<section class="section">
  <header class="section-heading">
    <h2>How this group relates to other Skill Hub areas</h2>
  </header>
  <ul>
    <li><strong><a href="/skill-hub/architecture/">Architecture</a></strong> — System context mapping and architecture decision records provide the broader design context for integration choices.</li>
    <li><strong><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></strong> — Data lineage, data contracts, and data quality skills feed into integration contract design.</li>
    <li><strong><a href="/skill-hub/sap-ams/">SAP AMS</a></strong> — Incident triage and root cause analysis skills are used when integration monitoring fires.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Status and limitations</h2>
  </header>
  <p>This skill group is a public working interpretation of integration architecture practice. It is not official SAP, TOGAF, or vendor documentation. It focuses on operational applicability rather than comprehensive framework coverage. SAP-specific content is aligned with S/4HANA and common middleware patterns but may need adaptation for specific releases or custom landscapes.</p>
</section>
