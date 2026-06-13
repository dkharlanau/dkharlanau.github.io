---
layout: default
title: "SAP Business Partner Replication Diagnostics"
description: "A conservative diagnostic frame for business partner replication issues in SAP S/4HANA."
permalink: /atlas/diagnostics/sap-business-partner-replication-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "BP / MDG / replication"
business_process: Master data governance
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - replication
related:
  - /atlas/diagnostics/sap-vendor-master-replication-diagnostics/
  - /atlas/diagnostics/sap-customer-master-replication-diagnostics/
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
  - /atlas/data-quality/master-data-governance-failure-modes/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Business Partner Replication Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP business partner replication diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a business partner was not replicated, arrived incomplete, or created duplicates in a target system.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>BP / MDG / replication</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Business partner replication moves BP master data from a source system to target systems. Most tickets resolve to one of three handoffs: the source did not select the BP, the target did not accept it, or the accepted BP was mapped to the wrong key. The diagnostic job is to find which handoff failed and why.</p>
    <p>The fastest way to narrow the issue is to prove the message left the source, then prove the target received it. Everything in between is noise until those two facts are established.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>BP created in source system but does not appear in target system after expected replication time.</li>
      <li>BP appears in target but with missing roles, addresses, or bank details.</li>
      <li>Target system creates a duplicate BP instead of updating the existing one.</li>
      <li>Replication shows success in the source but the target BP has different data.</li>
      <li>Specific BP role (customer, vendor, contact) is missing after replication.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Replication model filter:</strong> the BP type, role, or organizational unit is excluded from the replication model.</li>
      <li><strong>Key mapping missing:</strong> the source BP GUID or number is not mapped to the target system key, causing a new BP to be created.</li>
      <li><strong>Data quality block:</strong> the BP data fails validation in the target system (missing required field, invalid format, duplicate tax number).</li>
      <li><strong>Role-specific filter:</strong> the replication model sends the BP header but filters out specific roles or relationships.</li>
      <li><strong>Target system configuration:</strong> the target system has different BP grouping, number ranges, or role assignment rules that conflict with the replicated data.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MDG Data Replication log (if MDG is the source) — check replication status and error messages.</li>
      <li>BDCP / BDCPS — change pointers for the BP object.</li>
      <li>WE02 — IDoc status if ALE is used for replication.</li>
      <li>Key mapping tables (if custom mapping is used) — check source-to-target key mapping.</li>
      <li>Target system BP display (FLBP1 / FLBP2) — verify roles, addresses, and assignments.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>BUT000 / BUT001</strong> — BP header and general data.</li>
      <li><strong>BUT100 / BUT100</strong> — BP roles.</li>
      <li><strong>BUT020 / ADRC</strong> — BP addresses.</li>
      <li><strong>BKDF / BNKA</strong> — BP bank details.</li>
      <li><strong>BDCP / BDCPS</strong> — change pointers.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the BP number, source system, target system, and the expected versus actual result.</li>
      <li>Check the replication log or change pointer status to confirm the BP was selected for replication.</li>
      <li>Check WE02 or the replication middleware for IDoc or message status.</li>
      <li>Verify key mapping: does the target system recognize the source BP key or create a new one?</li>
      <li>Check the target BP in FLBP1/FLBP2 for missing roles, addresses, or data.</li>
      <li>Compare the source BP data with the target BP data to identify which fields were filtered or failed validation.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Update the replication model to include the missing BP type, role, or organizational unit.</li>
      <li>Create or correct key mapping between source and target systems.</li>
      <li>Fix data quality issues in the source BP before replicating.</li>
      <li>Adjust target system BP grouping or role assignment rules if they conflict with replicated data.</li>
      <li>If duplicates exist, evaluate merge or deactivation options with master data governance.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Before routing the issue, capture: BP number, source and target systems, expected versus actual result, replication model name, and any error from the replication log or IDoc status. A vague "BP missing" report wastes a round of basic questions; these six items let a support engineer start the real diagnosis.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Replication failures affect many business partners or all target systems.</li>
      <li>A duplicate BP was created in a target system and needs data steward or business approval to merge.</li>
      <li>The issue involves key mapping, number ranges, or BP grouping changes that require MDG/ BASIS involvement.</li>
      <li>Missing bank, tax, or address data has compliance, payment, or reporting impact.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a BP replication configuration guide. It does not cover MDG replication model design, key mapping setup, or BP grouping configuration. It does not replace SAP's master data governance documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">SAP Vendor Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
