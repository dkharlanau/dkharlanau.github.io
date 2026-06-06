---
layout: default
title: "SAP Invoice Verification Diagnostics"
description: "A conservative diagnostic frame for invoice verification blocks and mismatches in SAP MM."
permalink: /atlas/diagnostics/sap-invoice-verification-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM invoice verification"
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
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/diagnostics/sap-three-way-match-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Invoice Verification Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP invoice verification diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for separating invoice blocks caused by price, quantity, tax, or reference mismatches.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM invoice verification</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until invoice verification behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Invoice verification is the control point where the supplier's bill is matched against purchase order and goods receipt evidence. A blocked invoice is usually process evidence, not a system error. The support goal is to identify which mismatch element triggered the block and whether it reflects a real discrepancy or a data timing issue.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Invoice posts with a blocking reason that prevents automatic payment.</li>
      <li>MIRO shows price, quantity, or tax differences beyond tolerance.</li>
      <li>Invoice references a purchase order item that has no goods receipt or partial receipt.</li>
      <li>Multiple invoices for the same PO item create duplicate payment risk.</li>
      <li>Tax code or tax jurisdiction mismatch prevents posting.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Price variance:</strong> invoice price differs from PO price beyond the configured tolerance. May be a valid supplier price change or a wrong PO price.</li>
      <li><strong>Quantity variance:</strong> invoice quantity exceeds GR quantity. May indicate partial delivery, returns not processed, or duplicate invoicing.</li>
      <li><strong>Reference mismatch:</strong> invoice references wrong PO number, item, or delivery note. Common with consolidated invoices or supplier numbering changes.</li>
      <li><strong>Tax mismatch:</strong> tax code on invoice differs from PO or supplier master. Often caused by jurisdiction changes or supplier tax registration updates.</li>
      <li><strong>Timing issue:</strong> GR was posted after invoice was entered, or invoice arrived before PO was released.</li>
      <li><strong>Master data issue:</strong> supplier not extended to company code, payment terms mismatch, or tax number invalid.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>MIRO / MIR7 — invoice entry and blocking reason display.</li>
      <li>ME23N — purchase order history showing GR and IR quantities.</li>
      <li>MIR4 — invoice document display with variance details.</li>
      <li>FBL1N — supplier line items to see if invoice was posted but blocked.</li>
      <li>PO history tab — compare ordered, delivered, and invoiced quantities.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>RBKP</strong> — invoice document header.</li>
      <li><strong>RSEG</strong> — invoice document items.</li>
      <li><strong>EKBE</strong> — PO history (GR and IR records).</li>
      <li><strong>LFA1 / LFB1</strong> — supplier master (general and company code).</li>
      <li><strong>T169</strong> — tolerance groups for invoice verification.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the PO number, item, and supplier on the invoice match the system record.</li>
      <li>Check PO history (EKBE) for GR quantity and IR quantity. Identify the gap.</li>
      <li>Review the blocking reason in RBKP or MIR4. Determine if it is price, quantity, tax, or reference.</li>
      <li>Check tolerance settings to see if the variance is within acceptable limits.</li>
      <li>If the variance is valid, document the business reason and release. If not, return to supplier or correct master data.</li>
      <li>Verify that releasing the invoice will not create a duplicate payment.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Release the invoice with documented approval if the variance is within business tolerance.</li>
      <li>Correct the PO price or quantity if the original document was wrong.</li>
      <li>Post a subsequent debit or credit memo if the supplier issued a corrected invoice.</li>
      <li>Update supplier master data (tax code, payment terms) if the mismatch stems from master data.</li>
      <li>Escalate to procurement if the supplier repeatedly invoices outside agreed terms.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Do not release blocked invoices without documenting the variance reason and the business approval. A useful invoice verification ticket should include: PO number, invoice number, supplier, variance type (price/quantity/tax/reference), expected versus actual values, and whether the issue is recurring.</p>

    <h2>Invoice blocking and release workflow</h2>
    <p>Blocked invoices are a standard control in invoice verification. The support goal is to identify the block reason, verify the business justification for release, and ensure that releasing the invoice does not create duplicate payment or bypass procurement controls.</p>
    <ul>
      <li><strong>Check MRBR:</strong> the blocked invoice report lists all invoices blocked for price, quantity, tax, or reference reasons. Review the block reason code.</li>
      <li><strong>Check PO history (EKBE):</strong> compare the invoice quantity and price against the goods receipt and purchase order to confirm the variance.</li>
      <li><strong>Check tolerance settings:</strong> the block may be automatic because the variance exceeds the configured tolerance for the company code or supplier.</li>
      <li><strong>Check approval workflow:</strong> some organizations require a separate approval step before a blocked invoice can be released. Verify that the approver has the correct authorization.</li>
      <li><strong>Check for duplicates:</strong> before releasing, confirm that the same invoice has not already been posted or paid under a different document number.</li>
    </ul>
    <p>A useful invoice blocking ticket should include: invoice number, PO number, supplier, block reason, expected versus actual quantity and price, and whether the variance is approved by procurement or finance.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an invoice verification configuration guide. It does not cover automatic invoice verification setup, EDI invoicing, or complex tax scenarios. It does not replace the judgment of a finance controller or procurement manager.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">Gr Ir Clearing Explained</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-three-way-match-diagnostics/">SAP Three Way Match Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
