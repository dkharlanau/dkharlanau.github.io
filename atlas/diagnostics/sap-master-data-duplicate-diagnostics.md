---
layout: default
title: "SAP Master Data Duplicate Diagnostics"
description: "A conservative diagnostic frame for duplicate master data issues in SAP."
permalink: /atlas/diagnostics/sap-master-data-duplicate-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "Master data quality / duplicates"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - data-quality
related:
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/diagnostics/sap-number-range-diagnostics/
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
    <li aria-current="page">SAP Master Data Duplicate Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP master data duplicate diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why duplicate master data records exist, how to identify them, and how to prevent recurrence.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>Master data quality / duplicates</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until master data duplicate behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Duplicate master data records create confusion in transactions, reporting, and interfaces. They often arise from manual entry, replication without key mapping, number range overlaps, or missing validation. The support goal is to identify the duplicate records, understand how they were created, assess the business impact, and determine whether merge, deactivation, or re-keying is the right next step.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Multiple records exist for the same business entity (supplier, customer, material, business partner).</li>
      <li>Transactions reference different duplicates for the same real-world entity.</li>
      <li>Reporting shows inflated counts or split data for what should be one entity.</li>
      <li>Replication or interface creates a new record instead of updating the existing one.</li>
      <li>Users complain that master data search returns multiple similar results.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Manual creation without search:</strong> the user created a new record without checking if one already existed.</li>
      <li><strong>Replication without key mapping:</strong> the interface or replication did not find the existing target record and created a new one.</li>
      <li><strong>Number range overlap:</strong> different systems or number range intervals created records with colliding keys.</li>
      <li><strong>Missing duplicate check:</strong> the system does not enforce uniqueness on critical fields (tax number, email, bank account).</li>
      <li><strong>Data migration residue:</strong> legacy migration created duplicates that were never cleaned up.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>Standard master data search — use search by name, tax number, or other identifying fields to find duplicates.</li>
      <li>MDG duplicate check — if MDG is used, check the duplicate check log.</li>
      <li>Data quality reports — many organizations have custom reports for duplicate detection.</li>
      <li>Interface logs — check if replication or interface created the duplicate.</li>
      <li>Change documents — review creation history to identify who or what created the duplicate.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>BUT000</strong> — BP header (for duplicate BP detection).</li>
      <li><strong>KNA1 / LFA1</strong> — customer / vendor general data.</li>
      <li><strong>MARA</strong> — material master.</li>
      <li><strong>CDHDR / CDPOS</strong> — change documents.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the object type and the business entity that appears duplicated.</li>
      <li>Search for duplicates using name, tax number, email, bank account, or other identifying fields.</li>
      <li>Compare the duplicates: creation date, creator, source system, and data differences.</li>
      <li>Determine which record is the 'master' and which are duplicates based on usage and data quality.</li>
      <li>Check if transactions, documents, or interfaces reference the duplicate records.</li>
      <li>Assess the impact of merge, deactivation, or re-keying before taking action.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Merge duplicate records if a merge tool or process is available and safe.</li>
      <li>Deactivate or block the duplicate record if merge is not possible.</li>
      <li>Re-key existing transactions to reference the master record if the duplicate was used.</li>
      <li>Update key mapping to prevent future replication from creating the same duplicate.</li>
      <li>Implement or strengthen duplicate checks at creation time.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Duplicate master data is usually a process or integration gap, not a system bug. A useful ticket should include: object type, duplicate keys, identifying fields (name, tax number), creation history, which record is the master, and the business impact of the duplication.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a master data merge or de-duplication tool guide. It does not cover MDG duplicate check configuration, data migration cleanup, or merge program design. It does not replace SAP's master data governance documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-number-range-diagnostics/">SAP Number Range Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
