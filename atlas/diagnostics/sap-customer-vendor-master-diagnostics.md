---
layout: default
title: "SAP Customer and Vendor Master Diagnostics"
description: "A diagnostic frame for customer and vendor master data issues in SAP, with symptoms, checks, tables, and typical fixes."
permalink: /atlas/diagnostics/sap-customer-vendor-master-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data support
concept_type: diagnostic guide
sap_area: SD / MM / FI / BP / CVI
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - master-data
  - diagnostics
  - sap-sd
  - sap-mm
  - business-partner
related:
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/sap/sap-partner-determination-failures/
  - /atlas/data-quality/sap-mdg-governance-patterns/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Customer and Vendor Master Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostics Note</p>
    <h1>SAP customer and vendor master diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for tracing blocked transactions back to customer, vendor, or Business Partner master data gaps.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>SD / MM / FI / BP / CVI</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Many SAP support tickets that look like process failures — blocked sales order, failed invoice, excluded payment — are actually master data failures. Customer and vendor master data spans sales, procurement, finance, and logistics. A diagnostic that jumps to transaction-level fixes without checking the master data object will produce repeat incidents.</p>

    <h2>Key sections</h2>

    <h3>Common symptoms and where to look</h3>

    <h4>Sales order blocked due to incomplete customer master</h4>
    <p>The order cannot be created or released because a required field or organizational extension is missing. Check:</p>
    <ul>
      <li><strong>XD03</strong> — customer display: general data, company code, sales area, and partner roles.</li>
      <li>Incompletion log in the sales order (VA02) to see which field is flagged.</li>
      <li>Whether the customer is extended to the sales area and distribution channel of the order.</li>
    </ul>

    <h4>Invoice fails due to missing tax code in vendor master</h4>
    <p>MIRO or a logistics invoice verification document cannot post because tax data is incomplete. Check:</p>
    <ul>
      <li><strong>XK03</strong> — vendor display: general data, company code, and purchasing organization.</li>
      <li>Tax indicator fields in the vendor master for the relevant country and company code.</li>
      <li>Whether the vendor is subject to withholding tax and the corresponding data is maintained.</li>
    </ul>

    <h4>Payment run excludes vendor due to missing bank details</h4>
    <p>The automatic payment program (F110) skips a vendor because payment method data is incomplete. Check:</p>
    <ul>
      <li><strong>XK03</strong> — vendor display: general data and company code payment transactions.</li>
      <li>Bank details in the vendor master (or Business Partner bank data if CVI is active).</li>
      <li>Payment method and house bank assignment for the company code and payment method.</li>
    </ul>

    <h4>Business Partner not synchronized to customer or vendor (CVI issue)</h4>
    <p>A Business Partner exists in BP transaction but the linked customer or vendor does not appear, or vice versa. Check:</p>
    <ul>
      <li><strong>BP</strong> — Business Partner display: identification, roles, and relationships.</li>
      <li><strong>FLBPC1 / FLBPC2</strong> — CVI synchronization reports and error logs.</li>
      <li>CVI mapping tables for number ranges and groupings.</li>
      <li>Whether the BP role (FLCU01, FLCU00, FLVN01, FLVN00) is assigned.</li>
    </ul>

    <h3>Key tables</h3>
    <ul>
      <li><strong>KNA1</strong> — customer master general data.</li>
      <li><strong>LFA1</strong> — vendor master general data.</li>
      <li><strong>BUT000</strong> — Business Partner general data.</li>
      <li><strong>CVI_CUST_LINK</strong> — link between Business Partner and customer.</li>
      <li><strong>CVI_VEND_LINK</strong> — link between Business Partner and vendor.</li>
    </ul>

    <h3>Account balance and open item checks</h3>
    <p>Some symptoms are financial rather than master-data, but the boundary is blurry:</p>
    <ul>
      <li><strong>FD10N</strong> — customer account balance and open items.</li>
      <li><strong>FK10N</strong> — vendor account balance and open items.</li>
      <li>Check whether a credit limit block or payment block flag is set in the customer or vendor master.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the failing transaction and the error message or symptom.</li>
      <li>Determine whether the issue is missing data, inconsistent data, duplicate data, or a synchronization gap.</li>
      <li>Display the customer (XD03), vendor (XK03), or Business Partner (BP) and compare with the organizational context of the failing transaction.</li>
      <li>If CVI is active, check FLBPC1/FLBPC2 for synchronization errors and verify the link tables.</li>
      <li>Check account balance and open items if the symptom involves payment, credit, or collection.</li>
      <li>Confirm whether the record was created directly in the operational system or distributed from MDG or another source system.</li>
    </ol>

    <h2>Typical fixes</h2>
    <ul>
      <li>Extend the customer or vendor to the missing sales area, company code, or purchasing organization.</li>
      <li>Maintain missing tax, bank, or payment method data in the relevant organizational view.</li>
      <li>Assign the correct Business Partner role for CVI synchronization.</li>
      <li>Run CVI synchronization or reconciliation if the link between BP and customer/vendor is broken.</li>
      <li>Remove a payment block or credit block flag if it was set in error.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A customer or vendor master ticket should include: the object number, the organizational context (company code, sales area, purchasing org), the failing transaction, the exact error message, and whether the record was created locally or replicated. Avoid fixing the symptom in the transaction without checking whether the master data gap will affect the next transaction too.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page does not provide step-by-step master data creation instructions. It does not cover every country-specific field or industry-specific extension. It does not replace SAP's official documentation for customer, vendor, or Business Partner management.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/sap/sap-partner-determination-failures/">SAP Partner Determination Failures</a></li>
      <li><a href="/atlas/data-quality/sap-mdg-governance-patterns/">SAP MDG Governance Patterns</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
