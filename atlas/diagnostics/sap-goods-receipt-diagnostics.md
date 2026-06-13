---

title: SAP Goods Receipt Diagnostics
layout: default
description: A practical support diagnostic guide for SAP goods receipt issues.
permalink: /atlas/diagnostics/sap-goods-receipt-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: MM inventory management
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - procurement
  - goods-receipt
related: 
  - "/atlas/maps/procure-to-pay-map/"
  - "/atlas/sap/gr-ir-clearing-explained/"
  - "/atlas/diagnostics/sap-invoice-verification-diagnostics/"
  - "/atlas/diagnostics/sap-three-way-match-diagnostics/"
  - "/atlas/diagnostics/sap-purchase-order-creation-diagnostics/"
  - "/atlas/diagnostics/sap-material-document-diagnostics/"
  - "/atlas/diagnostics/sap-movement-types-diagnostics/"
robots: noindex,follow
short_title: Goods Receipt Diagnostics
h1: SAP goods receipt diagnostics
subtitle: Goods receipt is where physical delivery becomes system evidence. Mistakes ripple into stock, invoice matching, and finance.
sitemap: false

---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/diagnostics/">Diagnostics</a></li><li aria-current="page">Goods Receipt Diagnostics</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP goods receipt diagnostics</h1>

<p class="note-subtitle">Goods receipt is where physical delivery becomes system evidence. Mistakes ripple into stock, invoice matching, and finance.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP AMS</dd></div><div><dt>Type</dt><dd>diagnostic guide</dd></div><div><dt>Reviewed</dt><dd>2026-06-13</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>Goods receipt sits at the boundary of inbound logistics, inventory management, invoice verification, and accounting. A posting failure here usually means the physical delivery, the purchase order, the material master, or the user input are not aligned.</p>

<h2>Common symptoms</h2>

<ul>

<li>The purchase order is closed, blocked, wrong, or no longer matches the physical delivery.</li>

<li>The material, batch, serial number, storage location, or quality status prevents normal posting.</li>

<li>A receipt was posted too early, too late, with the wrong quantity, or against the wrong reference.</li>

<li>The receipt quantity does not match the invoice quantity, causing a three-way match block.</li>

<li>Stock is visible physically but not in the system, or posted to the wrong plant or storage location.</li>

</ul>

<h2>Likely causes</h2>

<ul>

<li><strong>PO mismatch:</strong> the delivered material, quantity, or unit of measure differs from the purchase order item.</li>

<li><strong>Status block:</strong> the PO item is marked delivery completed, blocked, or deleted.</li>

<li><strong>Master data gap:</strong> the material is not extended to the plant or storage location, or the batch/serial profile is inconsistent.</li>

<li><strong>Quality inspection:</strong> the material requires inspection and cannot be posted directly to unrestricted stock.</li>

<li><strong>Movement type issue:</strong> the wrong movement type is used, or the movement type is not configured for the transaction.</li>

<li><strong>Timing issue:</strong> the invoice arrived before the goods receipt, or the receipt was posted against the wrong period.</li>

</ul>

<h2>Where to check in SAP</h2>

<ul>

<li>MIGO / MB01 — goods receipt entry and error messages.</li>

<li>ME23N — purchase order history showing ordered, delivered, and still-to-deliver quantities.</li>

<li>MB52 / MMBE — stock overview to confirm where stock was posted.</li>

<li>MKPF / MSEG — material document header and item details.</li>

<li>QA33 / QE51N — inspection lot status if quality management is involved.</li>

</ul>

<h2>Key tables / transactions / objects</h2>

<ul>

<li><strong>MKPF</strong> — material document header.</li>

<li><strong>MSEG</strong> — material document items.</li>

<li><strong>EKBE</strong> — purchase order history.</li>

<li><strong>MARD</strong> — storage location stock.</li>

<li><strong>QALS</strong> — inspection lot data.</li>

</ul>

<h2>Diagnostic workflow</h2>

<ol>

<li>Confirm the physical delivery: material, quantity, batch/serial, supplier, and delivery note.</li>

<li>Check the purchase order in ME23N for expected quantity, open quantity, delivery status, and blocks.</li>

<li>Attempt or review the goods receipt posting in MIGO and capture the exact error message.</li>

<li>Verify material master plant/storage location/batch settings and quality inspection requirements.</li>

<li>Check whether stock was already posted elsewhere or the PO was already delivery-completed.</li>

<li>Post the receipt correctly, or document the variance and route to procurement/quality/logistics.</li>

</ol>

<h2>Typical fixes or next actions</h2>

<ul>

<li>Reverse the incorrect receipt and repost against the correct PO item or quantity.</li>

<li>Update the PO quantity or remove the delivery-completed indicator if the delivery is legitimate.</li>

<li>Extend the material master to the required plant/storage location or resolve batch/serial issues.</li>

<li>Process the inspection lot usage decision if stock is held in quality inspection.</li>

<li>Coordinate with procurement if supplier deliveries repeatedly mismatch PO terms.</li>

</ul>

<h2>Support takeaway</h2>

<p>Goods receipt diagnostics should always reconcile physical evidence, purchase order history, and material document data. A useful ticket should include: material number, PO number, delivery note, quantity expected versus received, exact error message, plant/storage location, and whether the issue is recurring.</p>

<h2>Boundaries and non-goals</h2>

<p>This page is a diagnostic frame, not a warehouse management or quality management configuration guide. It does not cover advanced EWM putaway, QM inspection plans, or customs/inbound logistics scenarios.</p>

<h2>Escalation signals</h2>

<ul>

<li>Receipt failures affect multiple users, plants, or materials at the same time.</li>

<li>The issue involves a closed accounting period, inventory valuation, or intercompany transfer.</li>

<li>Quality inspection stock is blocked and operations cannot use the material.</li>

<li>Supplier deliveries repeatedly mismatch PO terms and procurement must review the relationship.</li>

</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>

<li><a href="/atlas/sap/gr-ir-clearing-explained/">GR/IR Clearing Explained</a></li>

<li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a></li>

<li><a href="/atlas/diagnostics/sap-three-way-match-diagnostics/">SAP Three-Way Match Diagnostics</a></li>

<li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>

<li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>

<li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
