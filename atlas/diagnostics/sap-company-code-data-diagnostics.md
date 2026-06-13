---
layout: default
title: "SAP Company Code Data Diagnostics"
description: "A diagnostic frame for company code assignment failures affecting vendors, customers, and business partners in SAP."
permalink: /atlas/diagnostics/sap-company-code-data-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Organizational data
concept_type: diagnostic guide
sap_area: "FI organizational data"
business_process: Cross-process master data
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-fi
  - organizational-data
  - master-data
  - diagnostics
related:
  - /atlas/diagnostics/sap-organizational-data-diagnostics/
  - /atlas/diagnostics/sap-supplier-master-diagnostics/
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
  - /atlas/diagnostics/sap-number-range-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Company Code Data Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP company code data diagnostics</h1>
    <p class="note-subtitle">Resolve company-code view gaps that block posting, payment, or replication for business partners, vendors, and customers.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process master data</dd></div>
      <div><dt>SAP area</dt><dd>FI organizational data</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Company code data controls how vendors, customers, and business partners are used in financial posting. A missing company-code view means invoices cannot be posted, payments cannot be run, and downstream reporting is incomplete. The diagnostic goal is to identify the missing company-code assignment or financial data element.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Invoice cannot be posted because the vendor is not extended to the company code.</li>
      <li>Payment run excludes a vendor due to missing payment method or bank details.</li>
      <li>Customer invoice fails because the customer is not extended to the company code.</li>
      <li>Business Partner replication succeeds but the vendor or customer role is missing a company-code view.</li>
      <li>Intercompany postings fail because the trading partner company code is not assigned.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Company-code view missing:</strong> vendor or customer was created without extending to the relevant company code.</li>
      <li><strong>Payment terms missing:</strong> company-code view exists but payment terms are blank.</li>
      <li><strong>Reconciliation account missing:</strong> vendor/customer company-code view lacks the general ledger reconciliation account.</li>
      <li><strong>Tax jurisdiction incomplete:</strong> tax data required for posting is not maintained.</li>
      <li><strong>BP role synchronization gap:</strong> Business Partner role exists but the FI customer/vendor view was not generated.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>FK03 / FD03 — vendor/customer company-code view.</li>
      <li>BP — Business Partner roles and company-code assignments.</li>
      <li>FBL1N / FBL5N — vendor/customer line items by company code.</li>
      <li>FB50 / FB70 — posting transactions that reveal missing company-code data.</li>
      <li>SE16 / LFB1, KNB1 — vendor and customer company-code tables.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>LFB1</strong> — vendor company-code data.</li>
      <li><strong>KNB1</strong> — customer company-code data.</li>
      <li><strong>BUT000 / BUT100</strong> — Business Partner general and role data.</li>
      <li><strong>T001</strong> — company codes.</li>
      <li><strong>SKA1 / SKB1</strong> — G/L accounts.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the business partner, vendor, or customer number and the failing company code.</li>
      <li>Check whether the company-code view exists in LFB1, KNB1, or the BP role.</li>
      <li>Verify required fields: reconciliation account, payment terms, tax data, payment method.</li>
      <li>If the BP role exists but the FI view is missing, check CVI synchronization.</li>
      <li>Extend the company-code view or correct missing financial data.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Extend the vendor or customer to the missing company code.</li>
      <li>Maintain the reconciliation account and payment terms.</li>
      <li>Update tax jurisdiction or tax number if posting requires it.</li>
      <li>Trigger BP-to-vendor/customer synchronization if the role is out of sync.</li>
      <li>Reprocess the failed document after master data correction.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Company-code data failures are almost always missing views or missing financial fields. The first check is whether LFB1 or KNB1 has a row for the company code; the second check is whether the reconciliation account and payment terms are populated.</p>

    <h2>Related diagnostics</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-organizational-data-diagnostics/">SAP Organizational Data Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-supplier-master-diagnostics/">SAP Supplier Master Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP CVI Synchronization Diagnostics</a></li>
    </ul>
  </div>
</article>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
