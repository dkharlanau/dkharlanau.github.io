---
title: SAP Goods Receipt Diagnostics
layout: default
description: "Diagnose SAP goods receipt failures by reconciling physical delivery, PO history, material controls, posting context, and resulting stock."
permalink: /atlas/diagnostics/sap-goods-receipt-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: MM inventory management
business_process: Procure to pay
status: reviewed
verified: true
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- procure-to-pay
- sap-mm
- diagnostics
- procurement
- goods-receipt
related:
- /atlas/maps/procure-to-pay-map/
- /atlas/sap/gr-ir-clearing-explained/
- /atlas/diagnostics/sap-invoice-verification-diagnostics/
- /atlas/diagnostics/sap-three-way-match-diagnostics/
- /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
- /atlas/diagnostics/sap-material-document-diagnostics/
- /atlas/diagnostics/sap-movement-types-diagnostics/
robots: index,follow
short_title: Goods Receipt Diagnostics
h1: SAP goods receipt diagnostics
subtitle: A goods receipt connects a physical event to purchasing, stock, accounting, quality, and later invoice matching.
sitemap: true
level: 2
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/diagnostics/">Diagnostics</a></li><li aria-current="page">Goods Receipt Diagnostics</li></ol></nav>

<article class="section note-detail atlas-page">
<header class="note-header">
  <p class="eyebrow">Knowledge Atlas</p>
  <h1>SAP goods receipt diagnostics</h1>
  <p class="note-subtitle">A goods receipt connects a physical event to purchasing, stock, accounting, quality, and later invoice matching.</p>
  <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP AMS</dd></div><div><dt>Type</dt><dd>Diagnostic guide</dd></div><div><dt>Reviewed</dt><dd>2026-06-13</dd></div></dl></aside>

<div class="note-body">
  <h2>Begin with three versions of reality</h2>
  <p>For a goods-receipt incident, compare three things: what physically arrived, what the purchase order expects, and what SAP already posted. Most confusion starts when one of these is treated as the truth without checking the other two.</p>
  <p>A truck at the gate does not prove that the PO item is open. A PO with open quantity does not prove that the material can be posted to the requested plant or stock type. A material document does not prove that stock is available for the business use the user expects.</p>

  <h2>First identify the exact failure</h2>
  <div class="decision-table"><table><thead><tr><th>Symptom</th><th>First question</th><th>Likely next evidence</th></tr></thead><tbody>
    <tr><td>The receipt cannot be posted</td><td>What exact validation stops the posting?</td><td>PO item/status, material/plant data, movement/reference context, batch/serial/QM requirements, posting date.</td></tr>
    <tr><td>The receipt posted against the wrong reference or quantity</td><td>What was posted and what should have been posted?</td><td>Material document, PO history, delivery note, user input, reversal/follow-on documents.</td></tr>
    <tr><td>PO history does not look as expected</td><td>Is the receipt missing, reversed, or posted to another item/reference?</td><td>PO history sequence and material-document references.</td></tr>
    <tr><td>Stock exists but is not usable</td><td>Which plant, storage location, batch, special-stock or quality status received it?</td><td>Stock overview and stock type/status after posting.</td></tr>
    <tr><td>Invoice matching is now blocked</td><td>Do PO, receipt and invoice quantities/values describe the same business event?</td><td>PO history, GR quantity/value, invoice variance and reversal history.</td></tr>
  </tbody></table></div>

  <h2>A diagnostic sequence</h2>
  <ol>
    <li><strong>Capture the physical evidence.</strong> Supplier, delivery note, material, delivered quantity, unit, batch/serial information where relevant, and receiving location.</li>
    <li><strong>Read the PO item.</strong> Check ordered and open quantity, delivery-completed/deletion or other relevant status, plant, delivery tolerances, units, and any expected receiving controls.</li>
    <li><strong>Read PO history before reposting.</strong> A receipt may already exist, may have been reversed, or may have been posted against a different item.</li>
    <li><strong>Capture the exact posting error.</strong> The message and posting context tell you whether the issue belongs to purchasing data, material controls, inventory configuration, accounting period, quality, batch/serial handling, or another layer.</li>
    <li><strong>Check the material and organizational context.</strong> Confirm that the material is valid for the plant and that required stock, batch, serial, valuation, or quality controls are satisfied.</li>
    <li><strong>Confirm the result after posting.</strong> Check the material document, PO history, stock location/status, and any accounting or quality follow-on result expected from the movement.</li>
  </ol>

  <h2>Movement type is important, but it is not the whole diagnosis</h2>
  <p>The movement type controls important posting behaviour, but changing it to make an error disappear can create the wrong stock or accounting result. First confirm the business event and reference: purchase-order receipt, reversal, return, transfer, subcontracting, consignment, or another scenario. Then check whether the movement used by the process matches that event.</p>
  <p>For deeper movement-type questions, use the <a href="/atlas/diagnostics/sap-movement-types-diagnostics/">movement type diagnostic</a> rather than turning every receiving issue into configuration work.</p>

  <h2>Quality, batch, serial, and warehouse controls change the path</h2>
  <p>A valid receipt may not land in unrestricted-use stock. Quality inspection, batch management, serial-number requirements, EWM or warehouse execution, and special-stock scenarios add their own evidence and status. Do not “correct” the inventory because the stock category differs from a simple PO receipt example.</p>

  <h2>Be careful with reversal and reposting</h2>
  <p>Reversing an incorrect receipt can be the right correction, but it is not a harmless reset button. Check whether the receipt already affected invoice verification, stock consumption, quality, warehouse tasks, valuation, or later material movements. The later the process has moved, the more important the document flow becomes.</p>

  <h2>Tools depend on the release and process</h2>
  <p>In classic GUI-based processes, consultants commonly use MIGO or the relevant Fiori app for the receipt, ME23N for PO and history context, and stock/material-document views for the posted result. S/4HANA data structures and apps differ from older ECC habits, so avoid building the diagnosis around one legacy transaction or table name.</p>

  <h2>What belongs in the ticket</h2>
  <ul>
    <li>PO and item, supplier, material, plant and receiving location.</li>
    <li>Physical quantity/unit versus ordered, already received, and remaining quantity.</li>
    <li>Exact posting error or the material document if posting already occurred.</li>
    <li>Batch, serial, quality, warehouse, or special-stock context when relevant.</li>
    <li>Delivery note and business date/posting date.</li>
    <li>Downstream impact: stock unavailable, invoice blocked, production waiting, accounting period issue, or another concrete result.</li>
  </ul>

  <h2>The useful end state</h2>
  <p>A goods-receipt incident is solved when physical delivery, PO history, material document, and resulting stock tell the same story. If support only makes the posting screen accept the entry, the interesting problems have merely been moved downstream to invoice verification or inventory reconciliation, where humans traditionally rediscover them at a worse time.</p>
</div>

<section class="atlas-related"><h2>Related pages</h2><ul>
  <li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
  <li><a href="/atlas/sap/gr-ir-clearing-explained/">GR/IR Clearing Explained</a></li>
  <li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a></li>
  <li><a href="/atlas/diagnostics/sap-three-way-match-diagnostics/">SAP Three-Way Match Diagnostics</a></li>
  <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
  <li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>
</ul></section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
</article>
