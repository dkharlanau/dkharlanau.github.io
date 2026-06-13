---
layout: default
title: "SAP MDG to S/4 Replication Diagnostics"
description: "A conservative diagnostic frame for SAP Master Data Governance to S/4HANA replication issues."
permalink: /atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "MDG / S/4HANA replication"
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
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/data-quality/master-data-governance-failure-modes/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP MDG to S/4 Replication Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP MDG to S/4 replication diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why master data approved in MDG does not appear correctly in S/4HANA target systems.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>MDG / S/4HANA replication</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until MDG to S/4 replication behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP MDG is the governance layer where master data is created, validated, and approved before replication to operational S/4HANA systems. When approved data does not appear in S/4, appears incomplete, or creates conflicts, the support goal is to identify whether the issue is in the replication model, the data replication hub, the key mapping, the S/4 target configuration, or the MDG activation process.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>MDG change request is approved but the data does not appear in S/4 after expected time.</li>
      <li>S/4 shows the object but with missing or different data compared to MDG.</li>
      <li>Replication log shows success but S/4 object has wrong organizational assignments.</li>
      <li>MDG creates the object in S/4 but with a different number than expected.</li>
      <li>Replication fails for specific object types or target systems while others work.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Replication model not active:</strong> the replication model for the object type or target system is not activated or has errors.</li>
      <li><strong>Data replication hub failure:</strong> the DRF (Data Replication Framework) or SOA message failed during transmission.</li>
      <li><strong>Key mapping missing:</strong> MDG and S/4 use different numbering and the key mapping is not maintained.</li>
      <li><strong>S/4 target validation failure:</strong> the data passed MDG validation but fails S/4-specific validation (e.g., tax jurisdiction, industry code).</li>
      <li><strong>MDG activation issue:</strong> the change request was approved but the final activation step did not trigger replication.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MDG Data Replication log — check replication status per object and target system.</li>
      <li>DRFOUT — DRF output monitoring for message status.</li>
      <li>SOAMANAGER — SOA message monitoring if web services are used.</li>
      <li>WE02 — IDoc status if ALE is used for replication.</li>
      <li>S/4 target system — verify object existence and data using standard display transactions.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>DRFOUT</strong> — DRF output log.</li>
      <li><strong>USMD120C / USMD160C</strong> — MDG change request status and replication status.</li>
      <li><strong>USMD1100</strong> — MDG staging area data.</li>
      <li><strong>Key mapping tables</strong> — MDG-to-S/4 key mapping (landscape-specific).</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the MDG change request, object type, target system, and expected versus actual result.</li>
      <li>Check the MDG change request status to confirm it reached 'final' or 'approved' status.</li>
      <li>Check the MDG Data Replication log or DRFOUT for replication status and error messages.</li>
      <li>If ALE is used, check WE02 for IDoc generation and status.</li>
      <li>If web services are used, check SOAMANAGER for message status.</li>
      <li>Verify key mapping between MDG and S/4 for the object type.</li>
      <li>Check the S/4 target system for the object and compare data with MDG.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Activate or correct the replication model for the object type and target system.</li>
      <li>Re-process failed DRF or SOA messages after fixing the underlying data or configuration issue.</li>
      <li>Create or update key mapping between MDG and S/4.</li>
      <li>Fix S/4-specific validation issues (e.g., extend organizational units, update code lists).</li>
      <li>If activation did not trigger replication, manually trigger or investigate the activation workflow.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>MDG to S/4 replication issues are usually model, DRF, or key mapping problems. A useful ticket should include: change request number, object type, target system, MDG replication log status, DRF/SOA message status, and the S/4 result.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an MDG replication configuration guide. It does not cover DRF setup, SOA configuration, or MDG workflow design. It does not replace SAP's MDG documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — use this for broader data quality signals and governance context.</li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — go here when the replicated object is a business partner.</li>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a> — check this if MDG and S/4 object numbers differ.</li>
      <li><a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP CVI Synchronization Diagnostics</a> — use this when the replicated object is a BP/customer/vendor with CVI issues.</li>
    </ul>

    <h2>Practical checklist</h2>
    <div markdown="1">
- [ ] Collect MDG change request number, object type, target system, and expected object key. **Synthetic example:** CR 1234567890, object type business partner, target S/4 TEST_01.

- [ ] Check MDG change request status reaches approved/final and review the Data Replication log.

- [ ] Check DRFOUT or SOAMANAGER for message status; if ALE is used, check WE02 for IDoc status.

- [ ] Verify key mapping between MDG and S/4 for the object type.

- [ ] Compare the object in S/4 with MDG staging data for missing fields or organizational assignments.

- [ ] Document the replication model used and any target-system validation errors.

- [ ] Safety limit: do not re-trigger mass replication until the root cause (model, mapping, or target validation) is fixed.
</div>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
