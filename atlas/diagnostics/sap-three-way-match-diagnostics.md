---
layout: default
title: "SAP Three-Way Match Diagnostics"
description: "A conservative diagnostic frame for three-way match failures in SAP procurement."
permalink: /atlas/diagnostics/sap-three-way-match-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM / FI procurement control"
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - invoice-verification
related:
  - /atlas/diagnostics/sap-invoice-verification-diagnostics/
  - /atlas/sap/gr-ir-clearing-explained/
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
    <h1>SAP three-way match diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why purchase order, goods receipt, and invoice do not align.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM / FI procurement control</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until three-way match behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Three-way match is the control that compares purchase order, goods receipt, and invoice before payment is released. When the three documents do not align, the invoice is blocked. The support goal is not to force the match but to identify which document is the outlier and whether the discrepancy is valid or indicates a process failure.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Invoice blocked because PO price, quantity, or terms do not match GR or invoice.</li>
      <li>GR posted but invoice still shows missing receipt.</li>
      <li>Invoice quantity exceeds PO quantity even though GR was partial.</li>
      <li>Payment blocked for a supplier that usually invoices automatically.</li>
      <li>GR/IR clearing account shows persistent imbalance for a PO item.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>PO data is wrong:</strong> the original PO had incorrect price, quantity, or terms that GR and invoice now expose.</li>
      <li><strong>GR is missing or late:</strong> invoice arrived before goods were received, or GR was posted to a different PO item.</li>
      <li><strong>Invoice references wrong document:</strong> supplier consolidated multiple POs or used a different reference number.</li>
      <li><strong>Returns or corrections not processed:</strong> a return to vendor or credit memo was not posted, leaving GR/IR out of balance.</li>
      <li><strong>Tolerance exceeded:</strong> a small variance in price or quantity is outside the configured tolerance for automatic approval.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME23N — PO history showing ordered, delivered, and invoiced quantities.</li>
      <li>MIGO — material documents for GR and returns.</li>
      <li>MIRO / MIR4 — invoice document and blocking reasons.</li>
      <li>FBL1N — supplier line items to see blocked invoices.</li>
      <li>MB5S — GR/IR list showing open items per PO item.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKPO / EKBE</strong> — PO items and history.</li>
      <li><strong>RBKP / RSEG</strong> — invoice header and items.</li>
      <li><strong>MKPF / MSEG</strong> — material documents.</li>
      <li><strong>BSEG</strong> — accounting document items (GR/IR account).</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the three documents: PO, GR, and invoice. Capture document numbers and quantities.</li>
      <li>Compare ordered quantity (EKPO), delivered quantity (GR), and invoiced quantity (IR).</li>
      <li>Check if the variance is within tolerance. If yes, the block may be manual or from another cause.</li>
      <li>If GR is missing, verify physical receipt and post or investigate why GR was not created.</li>
      <li>If invoice is wrong, contact the supplier for a correction or process a credit memo.</li>
      <li>If PO is wrong, determine if the PO should be amended or if a subsequent debit/credit is appropriate.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Release the invoice with documented approval if the variance is valid and within policy.</li>
      <li>Post missing GR if the goods were received.</li>
      <li>Request a corrected invoice from the supplier if the invoice is wrong.</li>
      <li>Process a subsequent debit or credit memo to correct the PO price after the fact.</li>
      <li>Clear the GR/IR account manually only if the imbalance is confirmed and documented.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Three-way match failures are usually process evidence, not system errors. A useful ticket should include: PO number, GR document, invoice number, the three quantities, the variance, and the business decision on how to resolve it. Do not bypass the match without documenting why.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a three-way match configuration guide. It does not cover tolerance configuration, automatic approval workflows, or EDI invoicing. It does not replace the judgment of procurement or finance.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">Gr Ir Clearing Explained</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
