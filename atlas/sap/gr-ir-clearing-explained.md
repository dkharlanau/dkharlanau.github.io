---

title: SAP GR/IR Clearing Explained
layout: default
description: A conservative explanation of GR/IR clearing in procurement and invoice verification.
permalink: /atlas/sap/gr-ir-clearing-explained/
atlas_section: sap
domain: SAP operations
subdomain: Procurement finance
concept_type: SAP concept
sap_area: MM / FI / invoice verification
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-09

tags:
  - procure-to-pay
  - sap-mm
  - procurement
related: 
  - "/atlas/maps/procure-to-pay-map/"
  - "/atlas/diagnostics/sap-goods-receipt-diagnostics/"
  - "/atlas/diagnostics/sap-three-way-match-diagnostics/"
  - "/atlas/sap/sap-mm-procurement-overview/"
robots: noindex,follow
short_title: GR/IR Clearing Explained
h1: SAP GR/IR clearing explained
subtitle: GR/IR is the accounting bridge between received goods and supplier invoices. Mismatches are process evidence, not just finance noise.
sitemap: false
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/sap/">Sap</a></li><li aria-current="page">GR/IR Clearing Explained</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP GR/IR clearing explained</h1>

<p class="note-subtitle">GR/IR is the accounting bridge between received goods and supplier invoices. Mismatches are process evidence, not just finance noise.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP operations</dd></div><div><dt>Type</dt><dd>SAP concept</dd></div><div><dt>Reviewed</dt><dd>2026-06-09</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>GR/IR sits between goods receipt and invoice verification. It helps separate the physical receipt event from the supplier invoice event.</p>

<h2>How GR/IR works</h2>

<p>When a goods receipt (GR) is posted in MIGO, SAP creates an accounting entry that debits the stock or consumption account and credits the GR/IR clearing account. When the invoice is posted in MIRO, SAP debits the GR/IR clearing account and credits the vendor account. If quantities and prices match perfectly, the GR/IR line items net to zero and can be cleared. If they do not match, a balance remains on the GR/IR account until the difference is resolved or written off. The GR/IR account is therefore a temporary suspense account, not a permanent liability.</p>

<h2>Common issues</h2>

<ul>

<li>Goods are received but the invoice has not arrived or cannot be matched.</li>

<li>Invoice quantity, price, tax, or purchase order reference differs from the receipt evidence.</li>

<li>Old balances remain because reversals, returns, cancellations, or invoice corrections were not handled consistently.</li>

</ul>

<h2>Common mismatch patterns</h2>

<ul>
  <li><strong>Quantity differences</strong> — invoice quantity is higher or lower than the total GR quantity for the PO line. Common with partial deliveries, over-shipments, or returns not updated in SAP.</li>
  <li><strong>Price differences</strong> — invoice price differs from the PO net price due to price changes, scales, or unplanned delivery costs added in MIRO.</li>
  <li><strong>Tax differences</strong> — tax code or tax amount on the invoice does not match the PO or GR. Often caused by vendor invoice formatting or jurisdiction changes.</li>
  <li><strong>Currency differences</strong> — foreign-currency POs create exchange rate variances between GR date and invoice date. The GR/IR account may show a residual in local currency even when foreign currency matches.</li>
  <li><strong>Timing differences</strong> — GR posted in one period, invoice posted in another, or month-end closing prevents clearing until the next period.</li>
  <li><strong>Returns and credit memos</strong> — a return delivery or credit memo was posted but did not correctly reference the original GR or invoice, leaving unmatched items.</li>
</ul>

<h2>Diagnostic questions</h2>

<ul>

<li>Which purchase order, goods receipt, and invoice documents are involved?</li>

<li>Is the mismatch quantity-based, price-based, tax-related, timing-related, or reversal-related?</li>

<li>Does the open item represent a real business mismatch or a cleanup item?</li>

</ul>

<h2>Where to check</h2>

<ul>
  <li><strong>FBL3N</strong> — line items on the GR/IR clearing account. Look for open debits and credits that do not net to zero.</li>
  <li><strong>ME23N</strong> — PO history tab shows the full document flow: GRs, invoices, returns, and credit memos per PO line.</li>
  <li><strong>MIGO</strong> — review GR documents, movement types, and whether returns were posted correctly.</li>
  <li><strong>MIRO / MIR4</strong> — invoice documents, blocked reasons, and variance details. Check for unplanned delivery costs.</li>
  <li><strong>MR11</strong> — GR/IR maintenance: lists open items and allows write-off of small, approved differences.</li>
  <li><strong>F.13</strong> — automatic clearing program for GR/IR and other clearing accounts. Useful for mass clearing when document assignments match.</li>
</ul>

<h2>Tables and fields</h2>

<ul>
  <li><strong>BSEG</strong> — accounting document segment; contains GR/IR account postings with PO reference (EBELN, EBELP).</li>
  <li><strong>BSIS</strong> — open items for the GR/IR account; key for FBL3N and reconciliation.</li>
  <li><strong>EKBE</strong> — PO history; aggregates GR and invoice references per PO item.</li>
  <li><strong>MKPF</strong> — GR document header.</li>
  <li><strong>MSEG</strong> — GR document items; links to PO and accounting.</li>
  <li><strong>RBKP</strong> — invoice document header.</li>
  <li><strong>RSEG</strong> — invoice document items; links to PO and GR.</li>
</ul>

<h2>When to escalate</h2>

<p>Escalate when the mismatch indicates a process problem rather than a data cleanup task. Examples: repeated quantity differences from the same vendor suggest a receiving or vendor communication issue; persistent price differences suggest procurement is not updating outline agreements or info records; large old open items with no supporting documents may indicate fraud, theft, or system bypass. Data cleanup (MR11, F.13, manual clearing) should only be done after the root cause is understood and approved by finance.</p>

<h2>Retail-specific: month-end close issues</h2>
<p>Retail month-end closing faces unique challenges due to high transaction volume, POS reconciliation, markdown accruals, and inventory adjustments.</p>
<ul>
  <li><strong>GR/IR open items:</strong> high-volume retail procurement creates large numbers of unmatched GR/IR lines. Check FBL3N for old items and MR11 for cleanup.</li>
  <li><strong>POS posting status:</strong> missing or delayed POS data (WPUUMS IDocs) causes revenue and inventory postings to be incomplete at period end. Check WE02 for failed IDocs.</li>
  <li><strong>Markdown accruals:</strong> end-of-season markdowns may require accrual postings that are not yet reflected in the general ledger.</li>
  <li><strong>Inventory adjustment accounts:</strong> cycle counts, shrinkage postings, and damage write-offs accumulate in adjustment accounts that must be reviewed before close.</li>
  <li><strong>Timing:</strong> retail often operates with tight close windows. GR/IR, POS, and inventory postings that span period boundaries can delay close.</li>
</ul>
<p>A useful month-end close ticket should include: the period being closed, the specific account or process that is blocked, the volume of open items, and whether the issue is recurring every month-end.</p>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>

<li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">Goods Receipt Diagnostics</a></li>

<li><a href="/atlas/diagnostics/sap-three-way-match-diagnostics/">Three-Way Match Diagnostics</a></li>

<li><a href="/atlas/sap/sap-mm-procurement-overview/">MM Procurement Overview</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
