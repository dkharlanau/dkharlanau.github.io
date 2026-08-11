---
layout: default
title: SAP CVI Synchronization Diagnostics
description: A source-backed SAP CVI guide for missing Business Partner, customer, or supplier links, roles, number assignment, and postprocessing errors.
permalink: /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
last_modified_at: 2026-08-11
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: CVI / BP / customer / vendor
business_process: Master data governance
status: reviewed
verified: true
last_reviewed: '2026-06-13'
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
- /atlas/diagnostics/sap-company-code-data-diagnostics/
- /atlas/diagnostics/sap-supplier-master-diagnostics/
robots: index,follow
sitemap: true
level: 2
---

**Sources:** [SAP Business Partner Approach for Customer/Supplier Integration](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/74b0b157c81944ffaac6ebc07245b9dc/25b46c8241fd4852bf7876d87bed8fd0.html?locale=en-US), [SAP synchronization processing scenarios](https://help.sap.com/docs/SAP_ERP/6db8ae6e26e64854bc6f369d2dfd395f/36f8c5536a51204be10000000a174cb4.html), and [SAP customer and supplier synchronization guidance](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/d1a0c753b1081d4be10000000a174cb4-824.html).
**Date checked:** 2026-08-11
**Confidence:** high for the object-pair and role diagnostic sequence; medium for cockpit, postprocessing, and table details that vary by release.
**Related page/topic:** /atlas/diagnostics/sap-business-partner-replication-diagnostics/
**Practical implication:** Establish the intended object pair, active synchronization direction, role scope, grouping/account-group mapping, and existing link before creating or resynchronizing anything.
**Tags:** master-data, sap-mdg, diagnostics, cvi, business-partner, customer, supplier

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
    <p class="note-subtitle">A link-first workflow for missing, incomplete, or duplicate Business Partner, customer, and supplier object pairs.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>CVI / BP / customer / vendor</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Customer/Vendor Integration (CVI), also described in current SAP documentation as Customer/Supplier Integration, synchronizes linked Business Partner and customer or supplier objects. In SAP S/4HANA the Business Partner is the leading object for creating customer and supplier master data. Diagnose the intended object pair, active synchronization direction, existing link, grouping-to-account-group mapping, number assignment, and required role-specific data before treating the symptom as damaged master data.</p>

    <h2>Role and object scope</h2>
    <table>
      <thead>
        <tr><th>Business requirement</th><th>Typical BP role category</th><th>Data scope to verify</th></tr>
      </thead>
      <tbody>
        <tr><td>Customer accounting</td><td>FLCU00</td><td>Customer and company-code data.</td></tr>
        <tr><td>Customer sales processing</td><td>FLCU01</td><td>Customer and sales-area data.</td></tr>
        <tr><td>Supplier accounting</td><td>FLVN00</td><td>Supplier and company-code data.</td></tr>
        <tr><td>Supplier purchasing</td><td>FLVN01</td><td>Supplier and purchasing-organization data.</td></tr>
      </tbody>
    </table>
    <p>A general customer or supplier link can exist while the organizational segment needed by the business process is absent. Select the expected role from the process requirement; do not add every role as a generic synchronization fix.</p>

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
      <li><strong>Synchronization option or mapping gap:</strong> the required BP-to-customer/supplier or customer/supplier-to-BP option, grouping-to-account-group assignment, or direction-specific number assignment is not configured as intended.</li>
      <li><strong>Existing-object mismatch:</strong> one side already exists but is not assigned to the intended counterpart, so create processing can conflict with an existing master record.</li>
      <li><strong>Number assignment conflict:</strong> internal/external number settings or same-number expectations do not match the assigned grouping and account group.</li>
      <li><strong>Role or organizational data missing:</strong> the BP lacks the accounting, sales, or purchasing role and segment required by the business process.</li>
      <li><strong>CVI mapping error:</strong> the field mapping between BP and customer/vendor is misconfigured or missing for a specific field.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>Transaction BP or the release-appropriate Business Partner app — check the object, customer/supplier roles, and organizational segments.</li>
      <li>Customer or supplier master display available in the release — verify the corresponding object and required company-code, sales-area, or purchasing-organization data.</li>
      <li>Synchronization cockpit and CVI postprocessing environment — check unsynchronized records and exact postprocessing messages. Transaction names and availability are release-dependent.</li>
      <li>CVI Customizing — check active synchronization options, grouping-to-account-group assignments, direction-specific number assignment, field mapping, and queue settings.</li>
    </ul>

    <h2>Key objects and configuration evidence</h2>
    <ul>
      <li><strong>Object pair:</strong> BP number plus customer or supplier number and the system-recognized assignment between them.</li>
      <li><strong>Role and segment:</strong> FLCU00/FLCU01 or FLVN00/FLVN01 plus the required company code, sales area, or purchasing organization.</li>
      <li><strong>Grouping and account group:</strong> the configured mapping for the relevant processing direction.</li>
      <li><strong>Number assignment:</strong> internal/external ranges and whether same-number processing is configured.</li>
      <li><strong>Postprocessing message:</strong> exact error, source object, target object, direction, timestamp, and processing status.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the known BP, customer, or supplier number; the expected counterpart; the business process; and the expected accounting, sales, or purchasing segment.</li>
      <li>Open the BP and check the roles and organizational data. A role name without the required segment is not a complete business result.</li>
      <li>Verify whether the system recognizes the intended BP-to-customer or BP-to-supplier object pair before creating anything manually.</li>
      <li>Review the synchronization cockpit or postprocessing evidence for the exact failing object, direction, field, and message.</li>
      <li>Check the active synchronization option, grouping/account-group mapping, and number assignment for that direction.</li>
      <li>Compare source values with target validation and field mapping. Resolve the first failing field or rule before reprocessing.</li>
      <li>After correction, use the approved synchronization or postprocessing action and confirm both the link and the required organizational data.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the relevant synchronization option and grouping-to-account-group mapping through controlled Customizing.</li>
      <li>Add only the customer or supplier role and organizational segment required by the approved business process.</li>
      <li>Correct direction-specific number assignment or same-number settings with the master-data design owner.</li>
      <li>Assign existing objects using the supported process when both sides already exist; do not create a second counterpart to bypass a broken link.</li>
      <li>Reprocess the failed synchronization only after the configuration or data error is corrected and duplicate risk is assessed.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the BP and customer or supplier numbers, object-creation sequence, BP grouping, account group, expected role and organizational segment, processing direction, number-assignment expectation, link result, exact postprocessing message, and last synchronization time. Keep personal, banking, tax, and client-specific values out of public notes.</p>

    <h2>Official references</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/74b0b157c81944ffaac6ebc07245b9dc/25b46c8241fd4852bf7876d87bed8fd0.html?locale=en-US">SAP: Business Partner Approach (Customer/Supplier Integration)</a></li>
      <li><a href="https://help.sap.com/docs/SAP_ERP/6db8ae6e26e64854bc6f369d2dfd395f/36f8c5536a51204be10000000a174cb4.html">SAP: synchronization directions with processing scenarios</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/d1a0c753b1081d4be10000000a174cb4-824.html">SAP: synchronization of customer and supplier master data</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/74b0b157c81944ffaac6ebc07245b9dc/a8a7da1dc0d0476a9476d4c03d66a1e5.html">SAP: customer and supplier Business Partner role categories</a></li>
    </ul>

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

    <h2>Customer-vendor integration boundary</h2>
    <p>CVI is a synchronization and assignment mechanism, not a generic cleanup tool. SAP documents supported scenarios for creating or assigning the counterpart when one or both objects already exist. Use the supported scenario for the actual object state; manual duplicate creation can make the link and number-assignment problem harder to recover.</p>

    <h2>Practical checklist</h2>
    <div markdown="1">
- [ ] Collect BP number, customer/vendor number, BP grouping, and expected roles. **Synthetic example:** BP 1234567890, customer 1000000001, grouping TEST_CUST_GRP.

- [ ] Check transaction BP or the applicable BP app for the required FLCU00/FLCU01 or FLVN00/FLVN01 role and organizational segment.

- [ ] Verify that the system recognizes the intended BP-to-customer or BP-to-supplier assignment.

- [ ] Display the customer or supplier using the release-appropriate app or transaction and confirm the required organizational data.

- [ ] Review CVI synchronization log for field-level or direction errors.

- [ ] Confirm active synchronization, grouping/account-group mapping, and number assignment for the intended direction.

- [ ] Safety limit: do not manually create a customer/vendor for a BP that should be synchronized; fix CVI config first.
</div>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">SAP Vendor Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-bp-relationship-diagnostics/">SAP BP Relationship Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-company-code-data-diagnostics/">SAP Company Code Data Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-supplier-master-diagnostics/">SAP Supplier Master Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
