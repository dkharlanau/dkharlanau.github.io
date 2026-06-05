---
layout: default
title: "AI and ML Sidecars for SAP"
description: "A conservative frame for deciding when AI and ML add value around SAP, and how to keep the deterministic core separate from probabilistic edge services."
permalink: /atlas/ai-operations/ai-ml-sidecars-for-sap/
atlas_section: ai-operations
domain: AI-assisted operations
subdomain: AI/ML integration
concept_type: operating pattern
sap_area: SAP support / BTP-adjacent architecture
business_process: Support operations
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau
tags:
  - ai-operations
  - sap-ams
  - automation
  - machine-learning
related:
  - /atlas/ai-operations/practical-ai-ml-for-sap-support/
  - /atlas/automation/rule-based-automation-vs-ai/
  - /atlas/concepts/composable-erp-for-sap-operations/
  - /atlas/ai-operations/ai-agent-for-sap-support/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/ai-operations/">AI Operations</a></li>
    <li aria-current="page">AI and ML Sidecars for SAP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas AI Operations</p>
    <h1>AI and ML sidecars for SAP</h1>
    <p class="note-subtitle">Deterministic core. Probabilistic edge. Clear boundaries between them.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Support operations</dd></div>
      <div><dt>SAP area</dt><dd>SAP support / BTP-adjacent architecture</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until AI/ML integration claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Enterprise systems like SAP were designed as deterministic machines. Every transaction posts the same way, every document follows strict rules. AI and ML, by nature, deal in probabilities — forecasts, risk scores, pattern detection. The two can coexist only when the boundary between them is explicit and respected.</p>
    <p>The guiding principle: <strong>deterministic stays inside; probabilistic lives outside.</strong> SAP remains the system of record. AI/ML services run as sidecars, returning results with confidence scores and reason codes, never bypassing authorization or posting directly.</p>

    <h2>When AI/ML makes sense (and when it does not)</h2>
    <ul>
      <li><strong>Rule-driven and stable processes</strong> — keep them in SAP with validations or BRF+. Do not add model complexity where rules suffice.</li>
      <li><strong>Probability or pattern-dependent outcomes</strong> — demand forecasts, delivery risk scores, duplicate detection. These are natural ML tasks.</li>
      <li><strong>Measurable financial or defect impact</strong> — if the gain is clear, a pilot is usually justified. If not, think twice.</li>
      <li><strong>Poor or rare training data</strong> — start with clustering, anomaly detection, or rules. ML can wait until data quality improves.</li>
      <li><strong>Speed-critical on-screen decisions</strong> — keep them simple. Heavy inference should run asynchronously and feed back later.</li>
    </ul>

    <h2>Typical sidecar tasks</h2>
    <ul>
      <li>Forecasting demand, ETA, or workload — time-series models.</li>
      <li>Predicting risk (late payment, churn, stockout) — classification models.</li>
      <li>Grouping customers or detecting duplicates — clustering, embeddings.</li>
      <li>Reading invoices or contracts — OCR, NLP, retrieval-augmented generation.</li>
      <li>Summarizing incidents or tickets — large language models with human review.</li>
      <li>Optimizing transport or shifts — constraint solvers.</li>
    </ul>

    <h2>Three-tier extensibility model</h2>
    <p>SAP proposes three tiers for extensions. AI/ML fits this model cleanly:</p>
    <ul>
      <li><strong>Tier A — In-App / Key-User inside S/4:</strong> fields, validations, BRF+, lightweight enhancements. Deterministic logic only.</li>
      <li><strong>Tier B — ABAP Cloud inside S/4:</strong> clean extensions next to the core, upgrade-safe. Still deterministic and transactional.</li>
      <li><strong>Tier C — Side-by-Side app:</strong> separate service talking to S/4 via released APIs and events. This is where AI/ML belongs.</li>
    </ul>

    <h2>Data architecture for sidecars</h2>
    <ul>
      <li><strong>Facts stay in SAP.</strong> Master data and transactions remain the system of record.</li>
      <li><strong>History and patterns live outside.</strong> A lakehouse holds raw history and curated views for training and analysis.</li>
      <li><strong>Signals flow through events.</strong> Real-time changes should travel through event streams rather than point-to-point calls.</li>
      <li><strong>Features need consistency.</strong> What the model sees in training must match production. A feature store helps maintain that contract.</li>
      <li><strong>Knowledge for GenAI has its own shape.</strong> Documents, contracts, and SOPs need embeddings and vector indexes for retrieval.</li>
    </ul>

    <h2>Common failure modes</h2>
    <ul>
      <li>Embedding AI inside the core where rules should govern — creates upgrade risk and audit gaps.</li>
      <li>Training on dirty data and expecting clean predictions — garbage in, garbage out, even with advanced models.</li>
      <li>Missing authorization boundaries — an AI service that reads across all plants or company codes without respecting user limits.</li>
      <li>No observability or drift detection — models degrade silently when business conditions change.</li>
      <li>Treating every problem as an ML problem — sometimes a lookup table or a simple threshold is cheaper and more explainable.</li>
    </ul>

    <h2>Practical questions</h2>
    <ul>
      <li>Can this decision be expressed as a rule? If yes, use a rule.</li>
      <li>Do we have labeled historical data that matches the current landscape?</li>
      <li>Can we explain the model's recommendation to an auditor or a regulator?</li>
      <li>What happens when the model is wrong — is there a human review gate?</li>
      <li>Can we move this sidecar to another runtime without touching SAP?</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page does not prescribe specific models, vendors, or implementation steps. It does not claim that AI/ML will reduce costs in every scenario. It does not replace SAP's own documentation on BTP AI services or Joule.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/ai-operations/practical-ai-ml-for-sap-support/">Practical AI and ML for SAP Support</a></li>
      <li><a href="/atlas/automation/rule-based-automation-vs-ai/">Rule-Based Automation vs AI</a></li>
      <li><a href="/atlas/concepts/composable-erp-for-sap-operations/">Composable ERP for SAP Operations</a></li>
      <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
