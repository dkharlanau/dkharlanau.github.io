---
layout: default
title: "SAP CVI Synchronization Diagnostics"
description: "A conservative diagnostic frame for Customer-Vendor Integration synchronization issues in SAP S/4HANA."
permalink: /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "CVI / BP / customer / vendor"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - cvi
related:
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
  - /atlas/diagnostics/sap-vendor-master-replication-diagnostics/
  - /atlas/diagnostics/sap-customer-master-replication-diagnostics/
  - /atlas/diagnostics/sap-bp-relationship-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP CVI Synchronization Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP CVI synchronization diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a business partner, customer, or vendor is not synchronized correctly through CVI.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>CVI / BP / customer / vendor</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until CVI synchronization behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Customer-Vendor Integration (CVI) in S/4HANA synchronizes business partners with customer and vendor master data. When a BP is created but the corresponding customer or vendor is missing, has wrong data, or creates duplicates, the support goal is to identify whether the issue is in the CVI configuration, the BP grouping, the direction of synchronization, or the target master data setup.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Business partner created but no corresponding customer or vendor was generated.</li>
      <li>Customer or vendor exists but the linked BP has different data or is missing.</li>
      <li>CVI creates duplicate business partners for the same customer or vendor.</li>
      <li>BP role assignment is missing or wrong after CVI synchronization.</li>
      <li>CVI synchronization log shows errors that are not immediately actionable.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>CVI not active for the BP grouping:</strong> the BP grouping used for the new BP is not configured for CVI synchronization.</li>
      <li><strong>Direction mismatch:</strong> the synchronization direction is set to BP-to-customer but the customer was created first, or vice versa.</li>
      <li><strong>Number range conflict:</strong> the BP number range overlaps with customer or vendor number ranges, causing collisions.</li>
      <li><strong>Missing BP role:</strong> the BP was created without the FLCU00 (customer) or FLVN00 (vendor) role required for CVI.</li>
      <li><strong>CVI mapping error:</strong> the field mapping between BP and customer/vendor is misconfigured or missing for a specific field.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>FLBP1 / FLBP2 — business partner display to check roles and CVI link.</li>
      <li>XD03 / XK03 — customer/vendor display to check BP assignment.</li>
      <li>CVI_LINK — link table between BP and customer/vendor.</li>
      <li>CVI synchronization log — check for errors during synchronization.</li>
      <li>BP grouping configuration — check if CVI is active for the grouping.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>BUT000 / BUT001</strong> — BP header and general data.</li>
      <li><strong>CVI_LINK</strong> — CVI link table.</li>
      <li><strong>KNA1 / KNB1</strong> — customer master data.</li>
      <li><strong>LFA1 / LFB1</strong> — vendor master data.</li>
      <li><strong>TBZ9A</strong> — BP role definitions.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the BP number, customer number, or vendor number and the expected synchronization result.</li>
      <li>Check FLBP1 for the BP roles (FLCU00 for customer, FLVN00 for vendor).</li>
      <li>Check CVI_LINK for the relationship between BP and customer/vendor.</li>
      <li>Check XD03/XK03 for the customer/vendor and verify the BP assignment.</li>
      <li>Check the CVI synchronization log for errors during the last synchronization run.</li>
      <li>Verify the BP grouping is configured for CVI and the synchronization direction is correct.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Activate CVI for the BP grouping if it was not configured.</li>
      <li>Add the missing BP role (FLCU00 or FLVN00) to enable synchronization.</li>
      <li>Correct the synchronization direction if BP and customer/vendor were created in the wrong order.</li>
      <li>Fix number range conflicts to prevent duplicate creation.</li>
      <li>Re-run CVI synchronization after correcting configuration or data issues.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>CVI synchronization issues are usually configuration or role assignment problems. A useful ticket should include: BP number, customer/vendor number, BP grouping, expected roles, actual result, CVI_LINK status, and any synchronization log errors.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a CVI configuration guide. It does not cover CVI setup, BP grouping design, or field mapping configuration. It does not replace SAP's CVI documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — use this for broader data quality signals and governance context.</li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — go here when BP data is replicated between systems.</li>
      <li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a> — check this when the customer side is missing or wrong.</li>
      <li><a href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">SAP Vendor Master Replication Diagnostics</a> — use this when the vendor side is missing or wrong.</li>
      <li><a href="/atlas/diagnostics/sap-bp-relationship-diagnostics/">SAP BP Relationship Diagnostics</a> — go here if the issue involves related BP roles or relationships.</li>
    </ul>

    <h2>Practical checklist</h2>
    <div markdown="1">
- [ ] Collect BP number, customer/vendor number, BP grouping, and expected roles. **Synthetic example:** BP 1234567890, customer 1000000001, grouping TEST_CUST_GRP.

- [ ] Check FLBP1/FLBP2 for BP roles FLCU00/FLVN00 and the CVI link.

- [ ] Verify CVI_LINK relationship between BP and customer/vendor.

- [ ] Check XD03/XK03 for customer/vendor and confirm BP assignment.

- [ ] Review CVI synchronization log for field-level or direction errors.

- [ ] Confirm the BP grouping is configured for CVI and the synchronization direction matches the creation order.

- [ ] Safety limit: do not manually create a customer/vendor for a BP that should be synchronized; fix CVI config first.
</div>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">SAP Vendor Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-bp-relationship-diagnostics/">SAP Bp Relationship Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
