---
layout: default
title: "SAP Invoice Verification Patterns"
description: "Practical patterns and diagnostic questions for SAP invoice verification, including MIRO, MR8M, tolerance checks, and common variance scenarios."
permalink: /atlas/sap/sap-invoice-verification-patterns/
atlas_section: sap
domain: SAP operations
subdomain: Procurement finance
concept_type: SAP concept
sap_area: MM / FI / invoice verification
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - invoice-verification
related:
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Invoice Verification Patterns</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP invoice verification patterns</h1>
    <p class="note-subtitle">How MIRO and MR8M handle invoices, what variances look like in practice, and where to check first.</p>
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
    <p>Invoice verification in SAP is the step where a supplier invoice is matched against the purchase order and goods receipt. The system checks price, quantity, tax, and delivery date against configured tolerances. When a mismatch exceeds tolerance, the invoice is blocked for manual review. Understanding the common patterns of variance helps an AMS operator decide whether the issue is master data, process timing, or a real business dispute.</p>

    <h2>Key sections</h2>

    <h3>The MIRO entry and matching logic</h3>
    <p>Transaction <strong>MIRO</strong> is the standard entry point for invoice receipt. The system proposes quantities and amounts from the PO and GR. The user can accept, adjust, or enter a completely different invoice. The match happens at the PO item level, and the result is an invoice document and an accounting document. If the invoice is blocked, the block reason is stored in the document and visible in <strong>MIR4</strong> or <strong>MRBR</strong>.</p>

    <h3>Common variance patterns</h3>
    <ul>
      <li><strong>Price variance</strong> — invoice price differs from PO price. If the difference exceeds the price tolerance (configured in tolerance keys VP, PP, PS), the invoice is blocked. Check the PO price history in <strong>ME23N</strong> and whether a new info record or contract price was intended.</li>
      <li><strong>Quantity variance</strong> — invoice quantity exceeds the GR quantity plus delivery tolerance. Common with partial deliveries or returns not yet processed. Check the PO history in <strong>ME23N</strong> and the GR documents in <strong>MIGO</strong> or <strong>MB51</strong>.</li>
      <li><strong>Blocked invoice</strong> — triggered by price, quantity, or manual block. Use <strong>MRBR</strong> to review blocked invoices and see the block reason code. Release is either automatic (if the variance drops below tolerance) or manual (via <strong>MRBR</strong> or workflow).</li>
      <li><strong>Tax mismatch</strong> — tax code or tax amount does not match the PO or supplier master. Often caused by jurisdiction changes, tax code updates, or supplier master data errors. Check the tax code in the PO and the supplier master tax classification.</li>
      <li><strong>Delivery date variance</strong> — invoice date or delivery date falls outside the allowed window. Relevant for cash discount and late delivery penalties.</li>
    </ul>

    <h3>Tolerance checks and configuration</h3>
    <p>Tolerances are defined per company code and control how much variance is acceptable before blocking. Key tolerance keys include:</p>
    <ul>
      <li><strong>VP</strong> — price variance percentage</li>
      <li><strong>PP</strong> — price variance absolute amount</li>
      <li><strong>PS</strong> — price variance for small differences</li>
      <li><strong>DQ</strong> — excess quantity without price variance</li>
      <li><strong>DW</strong> — quantity variance when no GR exists</li>
    </ul>
    <p>If an invoice is blocked, the block reason in <strong>MRBR</strong> maps to the tolerance key that was exceeded.</p>

    <h3>Reversals and corrections</h3>
    <p><strong>MR8M</strong> cancels an invoice document and reverses the accounting entries. It does not delete the document; it creates a reversal document. After MR8M, the PO history is updated and the GR/IR balance is adjusted. If the original invoice was already paid, the reversal may create a credit memo situation or require a manual refund process.</p>

    <h3>Where to check</h3>
    <ul>
      <li><strong>PO history</strong> — <strong>ME23N</strong> shows GR and IR documents linked to the PO item.</li>
      <li><strong>GR documents</strong> — <strong>MB51</strong> or <strong>MIGO</strong> display the material document, movement type, and quantity.</li>
      <li><strong>Invoice documents</strong> — <strong>MIR4</strong> or <strong>MRBR</strong> show the invoice, block status, and variance details.</li>
      <li><strong>GR/IR account</strong> — <strong>FBL3N</strong> on the GR/IR reconciliation account shows open items and clearing status.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>When an invoice is blocked, the first question is which tolerance was exceeded and whether the variance is justified by a business change (new price agreement, partial delivery, return). Do not release blocked invoices without checking the PO history and GR status. A useful ticket includes: invoice number, PO number, GR document, block reason code, and the expected versus actual price or quantity.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page covers standard invoice verification in MIRO. It does not cover evaluated receipt settlement (ERS), consignment settlement, pipeline material invoicing, or IDoc-based invoice entry. It does not replace SAP configuration documentation for tolerance keys or release strategies.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">SAP GR/IR Clearing Explained</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
