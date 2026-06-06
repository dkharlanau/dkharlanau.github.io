---
layout: default
title: "SAP Customer Master Replication Diagnostics"
description: "A conservative diagnostic frame for customer master replication issues in SAP."
permalink: /atlas/diagnostics/sap-customer-master-replication-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "Customer master / CVI / replication"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - replication
related:
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
  - /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Customer Master Replication Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP customer master replication diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a customer was not replicated, arrived with wrong data, or created a duplicate in the target system.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>Customer master / CVI / replication</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until customer master replication behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Customer master replication moves customer data from a source system to target systems, often through ALE, CVI, or MDG. When a customer is missing, has wrong sales area assignments, or creates duplicates, the support goal is to identify whether the issue is in the replication model, the CVI synchronization, key mapping, or the target system's customer configuration.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Customer created in source system but missing in target system.</li>
      <li>Customer exists in target but sales area or company code data is missing.</li>
      <li>Target system creates duplicate customer instead of updating existing one.</li>
      <li>CVI synchronization creates a business partner but the customer link is broken.</li>
      <li>Customer partner functions or tax classification differ between source and target.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Replication model filter:</strong> the customer account group or sales area is excluded from replication.</li>
      <li><strong>CVI synchronization failure:</strong> the customer-vendor integration did not create or link the BP correctly.</li>
      <li><strong>Key mapping missing:</strong> the source customer number is not mapped to the target system, causing a new customer to be created.</li>
      <li><strong>Sales area filter:</strong> the replication sends general data but filters out specific sales organizations or distribution channels.</li>
      <li><strong>Target number range issue:</strong> the target system number range is exhausted or configured for external numbering while the source uses internal.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>XD01 / XD02 / XD03 — customer master display in target system.</li>
      <li>WE02 — IDoc status if ALE replication is used.</li>
      <li>FLBP1 / FLBP2 — business partner display if CVI is involved.</li>
      <li>MDG replication log — if MDG is the source.</li>
      <li>Key mapping tables — source-to-target customer number mapping.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>KNA1</strong> — customer general data.</li>
      <li><strong>KNB1</strong> — customer company code data.</li>
      <li><strong>KNVV</strong> — customer sales area data.</li>
      <li><strong>BUT000 / BUT001</strong> — BP header (if CVI is used).</li>
      <li><strong>CVI_LINK</strong> — CVI link table between BP and customer.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the customer number, source system, target system, and the expected versus actual result.</li>
      <li>Check the replication log or IDoc status to confirm the customer was selected and sent.</li>
      <li>Verify the customer exists in the target system (XD03) and check which views are present.</li>
      <li>If CVI is used, check FLBP1 for the linked BP and verify the CVI_LINK table.</li>
      <li>Check key mapping to confirm the source customer maps to the correct target customer.</li>
      <li>Compare sales area and company code data between source and target.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Update the replication model to include the missing account group or sales area.</li>
      <li>Create or correct key mapping between source and target customer numbers.</li>
      <li>Fix CVI synchronization issues by re-running CVI synchronization or correcting the BP link.</li>
      <li>Extend the customer to the missing sales area or company code in the target system.</li>
      <li>Adjust target number ranges if they conflict with the source numbering.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Customer replication issues are usually model, mapping, or CVI problems. A useful ticket should include: customer number, source system, target system, expected views/data, actual result, replication model, and any IDoc or CVI error messages.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a customer replication configuration guide. It does not cover CVI setup, replication model design, or customer account group configuration. It does not replace SAP's customer master documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP Cvi Synchronization Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
