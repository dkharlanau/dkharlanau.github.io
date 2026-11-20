---
layout: default
title: "Data Architecture Selection — Working Skill"
description: "A repeatable discovery, comparison, decision and validation method for warehouses, lakehouses, data fabric, data mesh, and SAP data landscapes."
permalink: /skill-hub/architecture/data-architecture-selection-working-skill/
author: Dzmitryi Kharlanau
last_modified_at: 2026-11-20
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
tags:
  - solution-architecture
  - data-architecture
  - decision-making
  - data-governance
  - sap
related:
  - /atlas/concepts/data-architecture-field-guide/
  - /skill-hub/architecture/
  - /skill-hub/dama-dmbok/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/architecture/">Architecture</a></li><li aria-current="page">Data Architecture Selection</li></ol></nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Skill Hub / Solution architecture</p>
    <h1>Choose a data architecture that survives the review.</h1>
    <p class="note-subtitle">A 45-minute discovery method, a comparison sheet, and an evidence-based decision. Not a vendor slide deck.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>1. What this skill is for</h2>
    <p>Turn an ambiguous request for a “data platform” into a defensible architecture choice. Produce a one-page decision record that states the business job, viable options, trade-offs, ownership and proof needed before implementation.</p>

    <h2>2. When to use this skill</h2>
    <ul><li>A team wants to replace its enterprise warehouse with a lakehouse.</li><li>Several domains propose Data Mesh but lack clear data-product ownership.</li><li>Real-time reporting is requested without a measured freshness requirement.</li><li>An SAP transformation needs reliable master data, analytics and non-SAP integration.</li></ul>

    <h2>3. Real work situations</h2>
    <p><strong>Customer reporting:</strong> finance disputes a customer revenue report because “customer” means different things in SAP, CRM and billing. The business impact is unreliable revenue classification.</p>
    <p><strong>Distribution visibility:</strong> logistics wants near-real-time delivery status, while finance needs accurate year-end history. One retention and latency strategy will not serve both.</p>
    <p><strong>AI retrieval:</strong> an operations team wants AI to search documents and combine findings with ERP facts. The architect must separate untrusted document content from governed transactional facts.</p>
    <p><em>All three are synthetic teaching scenarios.</em></p>

    <h2>4. Inputs required</h2>
    <ul><li>Business decision and consumer personas; one example report, API response, or AI question.</li><li>Source inventory: systems, object types, keys, volumes, daily change rate and deletion signals.</li><li>Freshness, availability, security, historical retention and geographic constraints.</li><li>Named data owners, platform operators, budget, skills and delivery deadline.</li><li>Current data quality samples and failure/recovery evidence, if available.</li></ul>

    <h2>5. Questions to ask in discovery</h2>
    <ol><li>What action will somebody take with these data, and what is the cost of a wrong answer?</li><li>Does “five-minute data” mean event visibility or reconciled financial truth?</li><li>Where does each business identifier originate? Which system can change it?</li><li>Must historical reports reproduce the state as of a past date?</li><li>Which sources can be copied, and which can only be queried in place?</li><li>Who resolves mismatches and signs off a data product's SLA?</li><li>What would a minimally useful result look like within the first iteration?</li></ol>

    <h2>6. Working method</h2>
    <ol>
      <li><strong>Define the decision.</strong> Write the use case as consumer + question + action + consequence. Separate known facts from assumptions.</li>
      <li><strong>Inventory constraints.</strong> Capture latency, history, volume, quality, classification, access, residency, skills and costs. Mark unknowns.</li>
      <li><strong>Trace one datum.</strong> Follow one business identifier from source through replication, transformation, semantic model and consumer.</li>
      <li><strong>Shortlist two or three architectures.</strong> Include a minimal/status-quo alternative. Explain which components are storage, governance, ownership and serving; they are not mutually exclusive.</li>
      <li><strong>Compare using evidence.</strong> Evaluate correctness, freshness, usability, security, recovery, portability, operating effort and cost. Do not award a score without rationale.</li>
      <li><strong>Design a thin slice.</strong> One source, one meaningful model, one consumer, one quality rule, one failure test. Measure response and recovery.</li>
      <li><strong>Record the choice.</strong> Document why the winner fits, why alternatives lose, what can change the choice and who accepts the risks.</li>
      <li><strong>Plan verification.</strong> Set row/amount reconciliation, freshness, authorization, lineage, performance and replay acceptance checks.</li>
    </ol>

    <h2>7. Decision rules</h2>
    <ul>
      <li><strong>If</strong> end users need stable cross-source reporting, <strong>then</strong> prioritize a governed analytical model and accessible semantic layer, regardless of storage choice.</li>
      <li><strong>If</strong> files, events and ML experimentation dominate, <strong>then</strong> evaluate a lake or lakehouse — but test actual consumer ergonomics.</li>
      <li><strong>If</strong> discovery, lineage or access policy fails across existing systems, <strong>then</strong> assess fabric capabilities before migrating storage.</li>
      <li><strong>If</strong> domains cannot fund and operate their own products, <strong>then</strong> do not label decentralized storage a Data Mesh program.</li>
      <li><strong>If</strong> copying is prohibited or unnecessarily expensive, <strong>then</strong> test federation for latency, source load and authorization.</li>
      <li><strong>If</strong> nightly data is sufficient, <strong>then</strong> avoid streaming operational complexity until its value is proven.</li>
      <li><strong>If</strong> you cannot demonstrate deletion, replay and reconciliation, <strong>then</strong> do not sign off an incremental pipeline.</li>
    </ul>

    <h2>8. Deliverables</h2>
    <p><strong>Decision canvas:</strong> one-page business job, constraints, options, recommendation and open questions. <strong>System/data-flow sketch:</strong> sources, ownership, ingestion, transform, storage, model, access and consumers. <strong>Validation sheet:</strong> measurable acceptance tests and named owners. <strong>ADR:</strong> a durable explanation of trade-offs and reversibility.</p>

    <h2>9. Copy-ready template</h2>
    <pre><code>DATA ARCHITECTURE DECISION
Business decision / consumer:
One representative data question:
Known facts / assumptions:
Source systems and system of record:
Identifiers / history / deletion semantics:
Freshness SLA / volume / security / retention:
Options: (1) baseline, (2) alternative, (3) alternative
Evaluation: correctness | latency | access | operations | cost
Recommended pattern and why:
Rejected options and why:
Data owner / platform owner:
Thin-slice test and pass criteria:
Failure, replay and reconciliation test:
Open risks / next review trigger:
</code></pre>

    <h2>10. Quality checklist</h2>
    <ul>
      <li>[ ] The business decision and a real consumer are named.</li>
      <li>[ ] At least two viable options are compared at the same level of detail.</li>
      <li>[ ] Source of record and business identifier semantics are clear.</li>
      <li>[ ] Latency is measurable; historical requirements are explicit.</li>
      <li>[ ] Security, residency, data-product ownership and operations have owners.</li>
      <li>[ ] Replay, deletes, reconciliation and one failure mode are covered.</li>
      <li>[ ] The trade-off, reversibility and trigger for revisiting the decision are recorded.</li>
    </ul>

    <h2>11. AI-agent use and boundaries</h2>
    <p>Give an agent this template and the non-sensitive source inventory. Ask it to identify missing evidence, compare alternatives, challenge the preferred option and draft an ADR. The agent must label assumptions, cite evidence, avoid vendor claims not verified against current docs, and request human approval for platform or data-governance changes. No autonomous production writes or copying confidential records to public tools.</p>
    <p><strong>Practice variation:</strong> redo your decision when the requirement changes from five-minute freshness to next-day data. State precisely which infrastructure and operating controls you would remove, retain or simplify.</p>

    <h2>Learn the concepts</h2>
    <p>Start with the <a href="/atlas/concepts/data-architecture-field-guide/">Data Architecture Field Guide</a>. The workflow was independently synthesized from James Serra's <a href="https://www.oreilly.com/library/view/deciphering-data-architectures/9781098150754/">Deciphering Data Architectures</a>, especially the architecture design session, modeling, ingestion and operating-model chapters. Reuse the site's <a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a> for a formal decision artifact.</p>
    <p><small>Review candidate: noindex pending human review. Examples are synthetic.</small></p>
  </div>
</article>
