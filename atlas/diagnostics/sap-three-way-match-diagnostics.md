---
layout: default
title: "SAP Three-Way Match Diagnostics"
description: "Diagnostic guide for three-way match failures between purchase order, goods receipt, and invoice verification in SAP."
permalink: /atlas/diagnostics/sap-three-way-match-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement finance control
concept_type: diagnostic guide
sap_area: "MM / FI / invoice verification"
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - invoice-verification
related:
  - /atlas/diagnostics/sap-invoice-verification-diagnostics/
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/diagnostics/sap-invoice-split-analysis/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Three-Way Match Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP Three-Way Match Diagnostics</h1>
    <p class="note-subtitle">Practical steps to diagnose why PO, GR, and Invoice do not align in SAP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM / FI / invoice verification</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Three-way match in SAP compares purchase order (PO) quantities and prices against goods receipt (GR) and supplier invoice. When any leg differs, the invoice blocks or posts with a variance. The goal is to find which leg is wrong, not just clear the block.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Invoice blocked in MIRO with quantity or price variance.</li>
      <li>GR/IR clearing account shows open items that do not net to zero.</li>
      <li>Missing goods receipt for a PO line even though the invoice arrived.</li>
      <li>Duplicate invoice warning (message type F5, F6, or custom check).</li>
      <li>Partial delivery creates confusion: one PO line has multiple GRs and invoices that do not sum cleanly.</li>
      <li>Invoice posted but PO history does not show the expected reference.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li>GR quantity differs from invoice quantity due to over-delivery, under-delivery, or unit-of-measure conversion.</li>
      <li>Invoice price differs from PO net price because of price changes, scales, or conditions not copied correctly.</li>
      <li>Tax code or tax amount mismatch between PO, GR, and invoice.</li>
      <li>Currency exchange rate differences for foreign-currency POs.</li>
      <li>GR was reversed or cancelled after invoice posting, leaving an unmatched invoice.</li>
      <li>Invoice was posted against wrong PO or wrong PO line.</li>
      <li>Delivery costs or unplanned delivery costs were added in MIRO but not reflected in PO conditions.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>ME23N</strong> — PO history tab shows GR and invoice references per line item. Check quantities, dates, and document flow.</li>
      <li><strong>MIGO</strong> — review GR document, movement type, and whether it references the correct PO and line.</li>
      <li><strong>MIRO / MIR4</strong> — invoice document, blocked reason, and variance details. Check the Messages tab for block reasons.</li>
      <li><strong>MR11</strong> — GR/IR maintenance: lists open GR/IR items and allows write-off of small differences.</li>
      <li><strong>FBL3N</strong> — line items on the GR/IR clearing account to see open debits and credits.</li>
      <li><strong>ME2N / ME2L</strong> — PO list to confirm delivery status and invoice status per PO.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKPO</strong> — PO item data (quantity, price, delivery status, invoice status).</li>
      <li><strong>EKET</strong> — PO delivery schedule lines; useful for partial delivery scenarios.</li>
      <li><strong>MKPF</strong> — GR document header.</li>
      <li><strong>MSEG</strong> — GR document items; links to PO via LFBNR, LFPOS, LFBJA.</li>
      <li><strong>RBKP</strong> — invoice document header.</li>
      <li><strong>RSEG</strong> — invoice document items; links to PO and GR.</li>
      <li><strong>EKBE</strong> — PO history (aggregated view of GR and invoice per PO item).</li>
      <li><strong>BSEG / BSIS</strong> — accounting line items for GR/IR account.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <p>Start with the blocked invoice in MIRO or the open GR/IR item in FBL3N. Identify the PO number and line item. In ME23N, compare PO quantity, GR quantity, and invoice quantity. If GR is missing, check MIGO for unprocessed inbound deliveries or warehouse delays. If quantities differ, check whether the tolerance limits in the vendor master or company code allow the difference. If price differs, compare PO conditions (ME23N Conditions tab) with invoice conditions in MIRO. For duplicates, check RBKP for existing invoices with the same reference, amount, and vendor. Use MR11 only after confirming the mismatch is not a real business issue.</p>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Release the invoice block if the variance is within tolerance and approved.</li>
      <li>Post a missing GR in MIGO if goods were physically received but not recorded.</li>
      <li>Request a credit memo from the vendor if the invoice overstates quantity or price.</li>
      <li>Reverse and repost the invoice against the correct PO line if it was posted incorrectly.</li>
      <li>Use MR11 to write off small, approved GR/IR differences that will not be cleared by future documents.</li>
      <li>Update PO price or conditions if the vendor price changed and the business agrees.</li>
      <li>Escalate to procurement or warehouse if the mismatch indicates a process failure (wrong goods received, theft, or system bypass).</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Three-way match failures are rarely a single-document problem. The operator should trace PO → GR → Invoice in that order, confirm which document is the outlier, and decide whether the fix is data correction or process change. Never clear GR/IR blindly without understanding why the mismatch occurred.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This guide does not cover vendor master data issues, tax jurisdiction configuration, or custom invoice validation enhancements. It also does not replace SAP standard help or company-specific approval workflows.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">GR/IR Clearing Explained</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-invoice-split-analysis/">Invoice Split Analysis</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">MM Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
