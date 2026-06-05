---
layout: default
title: "SAP Clean Core Strategy"
description: "What clean core means for SAP S/4HANA operations, why it matters for upgrades and compliance, and where teams commonly drift away from it."
permalink: /atlas/concepts/sap-clean-core-strategy/
atlas_section: concepts
domain: Business operations
subdomain: Enterprise architecture
concept_type: business concept
sap_area: S/4HANA architecture
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau
tags:
  - concepts
  - sap-s4hana
  - architecture
  - clean-core
related:
  - /atlas/concepts/composable-erp-for-sap-operations/
  - /atlas/automation/sap-ams-operating-model/
  - /atlas/diagnostics/sap-process-audit/
  - /atlas/data-quality/sap-master-data-quality/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">SAP Clean Core Strategy</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Concepts</p>
    <h1>SAP clean core strategy</h1>
    <p class="note-subtitle">Keep the core standard. Extend at the edges. Know where the line is.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>S/4HANA architecture</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until clean core claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Clean core is the practice of keeping SAP S/4HANA as close to standard as possible, while placing extensions, customizations, and integrations outside the core through released APIs and events. The goal is not purity for its own sake. It is reducing upgrade friction, compliance risk, and the hidden cost of maintaining modifications that SAP never intended to support.</p>

    <h2>What clean core means in practice</h2>
    <ul>
      <li><strong>Standard processes first.</strong> Use SAP-delivered scope items and configuration before building custom alternatives.</li>
      <li><strong>Extensions outside the core.</strong> Custom code, new UIs, and integrations run in BTP, side-by-side apps, or external services — not inside the S/4 database and ABAP stack.</li>
      <li><strong>Released APIs only.</strong> Extensions communicate with S/4 through stable, versioned APIs and business events.</li>
      <li><strong>Upgrade-safe by design.</strong> A clean-core landscape should move to the next release without retrofitting custom code in the core.</li>
    </ul>

    <h2>Why it matters</h2>
    <ul>
      <li><strong>Upgrade speed.</strong> Every modification in the core adds test scope and risk to a release upgrade. Clean core reduces both.</li>
      <li><strong>Compliance clarity.</strong> Auditors and regulators prefer standard processes with documented exceptions over opaque custom code.</li>
      <li><strong>Vendor portability.</strong> When extensions live outside the core, switching an integration partner or a best-of-breed tool does not require core changes.</li>
      <li><strong>Support clarity.</strong> SAP support can diagnose standard processes more reliably than undocumented custom enhancements.</li>
    </ul>

    <h2>Common drift patterns</h2>
    <p>Teams rarely set out to violate clean core. Drift happens gradually:</p>
    <ul>
      <li><strong>Shadow modifications.</strong> A "small" user exit or BAdI implementation that grows over years into a critical dependency.</li>
      <li><strong>Custom tables in the core.</strong> Storing extension data in S/4 tables rather than in a side-by-side database.</li>
      <li><strong>Direct database updates.</strong> Programs that write to SAP tables bypassing the application layer, breaking audit trails and authorization checks.</li>
      <li><strong>Unreleased API use.</strong> Calling internal function modules or tables that SAP can change without notice.</li>
      <li><strong>Compatibility pack reliance.</strong> Using legacy scope items that SAP is retiring rather than migrating to standard alternatives.</li>
    </ul>

    <h2>Clean core assessment questions</h2>
    <ul>
      <li>Can we list every modification, enhancement, and custom code object in the core?</li>
      <li>Does each one have a business justification and an owner?</li>
      <li>Can we move any of them to a side-by-side app without changing the data model?</li>
      <li>Are we using released APIs for all external communication?</li>
      <li>Do we have a dashboard or report that shows deviation from the clean-core baseline?</li>
    </ul>

    <h2>Practical boundaries</h2>
    <p>Clean core is not a ban on all customization. Some capabilities genuinely require core extension — complex tax logic, industry-specific calculations, or tightly coupled document flow. The discipline is in making the choice explicit, documenting it, and reviewing it regularly.</p>

    <h2>Common failure modes</h2>
    <ul>
      <li>Treating clean core as a one-time project rather than an ongoing governance practice.</li>
      <li>Allowing "temporary" modifications that never get removed or documented.</li>
      <li>Measuring clean core by the number of modifications rather than their business impact and upgrade risk.</li>
      <li>Ignoring integration adapters that use unreleased interfaces because "they work today."</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page does not provide a clean core certification checklist or a specific tool recommendation. It does not claim that every SAP landscape can or should achieve 100% standard processes. It does not replace SAP's own clean core documentation or Cloud ALM guidance.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/composable-erp-for-sap-operations/">Composable ERP for SAP Operations</a></li>
      <li><a href="/atlas/automation/sap-ams-operating-model/">SAP AMS Operating Model</a></li>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
