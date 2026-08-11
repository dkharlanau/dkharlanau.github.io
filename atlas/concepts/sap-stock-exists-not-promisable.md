---

title: SAP Stock Exists but Is Not Promisable
layout: default
description: A source-backed SAP guide to why visible stock can remain unpromisable because of ATP scope, demand, location, dates, allocation, or protection.
permalink: /atlas/concepts/sap-stock-exists-not-promisable/
last_modified_at: 2026-08-11
atlas_section: concepts
domain: SAP operations
subdomain: Availability and fulfillment
concept_type: business concept
sap_area: ATP / availability / stock status
business_process: Order to cash
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-13

tags:
  - order-to-cash
  - sap-sd
  - diagnostics
  - retail
related: 
  - "/atlas/concepts/sap-atp-is-not-inventory/"
  - "/atlas/concepts/order-to-cash/"
  - "/atlas/diagnostics/sap-sales-order-block-diagnosis/"
  - "/atlas/concepts/store-receiving-sap-retail/"
robots: index,follow
sitemap: true
short_title: Stock Exists but Is Not Promisable
h1: SAP Stock Exists but Is Not Promisable
subtitle: A practical explanation of why visible stock can still fail availability, ATP, allocation, or channel commitment checks.
author: Dzmitryi Kharlanau
---

**Sources:** [SAP scope of availability check](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/d0960a564b52fb37e10000000a44147b.html), [SAP availability-check levels](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/199d86d0f85e4ea982a529c6e0409660.html?locale=en-us), and [SAP stock protection with product allocation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9905622a5c1f49ba84e9076fc83a9c2c/e7582f68181d476ab37550c6ebe6d25e.html).
**Date checked:** 2026-08-11
**Confidence:** high for the availability-scope distinction; medium for the exact result in a configured customer landscape.
**Related page/topic:** /atlas/concepts/sap-atp-is-not-inventory/
**Practical implication:** Reproduce the promise check in the same material, location, date, and document context before comparing its result with an inventory report.
**Tags:** order-to-cash, sap-sd, atp, inventory, allocation, diagnostics

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/concepts/">Concepts</a></li><li aria-current="page">Stock Exists but Is Not Promisable</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP Stock Exists but Is Not Promisable</h1>

<p class="note-subtitle">A practical explanation of why visible stock can still fail availability, ATP, allocation, or channel commitment checks.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>SAP operations</dd></div><div><dt>Type</dt><dd>business concept</dd></div><div><dt>Reviewed</dt><dd>2026-06-13</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>This page sits between inventory reporting and customer commitment. Use it when stock appears in a report or physical location but a sales order, store, or digital channel cannot confirm the expected quantity or date.</p>

<h2>Why the two figures differ</h2>

<table>
  <thead><tr><th>Question</th><th>Inventory view</th><th>Promise view</th></tr></thead>
  <tbody>
    <tr><td>What is measured?</td><td>Quantity recorded in one or more stock categories and locations.</td><td>Quantity and date available after the configured check considers eligible stocks, receipts, issues, and requirements.</td></tr>
    <tr><td>Which location matters?</td><td>The plant, storage location, batch, or stock segment selected in the report.</td><td>The location and level used by the document's availability check.</td></tr>
    <tr><td>Which time matters?</td><td>Usually the report's current stock position.</td><td>The requested date, receipt dates, existing demand, and applicable horizon or time-bucket rules.</td></tr>
    <tr><td>Which business controls matter?</td><td>Stock type and inventory status.</td><td>Checking group/rule, scope of check, document context, product allocation, supply protection, and other configured confirmation rules.</td></tr>
  </tbody>
</table>

<h2>Common issues</h2>

<ul>

<li>The inventory figure and the promise check use different plants, storage locations, batches, stock segments, or stock categories.</li>

<li>Stock is physically present but existing requirements, stock status, or the configured scope prevents it from supporting the new demand.</li>

<li>Product allocation or supply protection reserves capacity for customers, regions, channels, or prioritized demand, so a lower-priority request cannot consume all visible stock.</li>

<li>A receipt exists but falls after the requested date, is excluded by the scope, or is not treated as reliable supply for that check.</li>

</ul>

<h2>Diagnostic sequence</h2>

<ol>

<li>Capture the material, plant, storage location if relevant, batch or stock segment, document/item, requested date, requested quantity, confirmed date, and confirmed quantity.</li>

<li>Identify the inventory report and exact stock category behind the user's number. Do not compare an aggregate plant figure with a storage-location or segment-specific check.</li>

<li>Confirm the material's checking group, the process checking rule, and the resulting scope of check. SAP documentation defines the scope as the stocks, receipts, issue elements, and requirements included in the availability check.</li>

<li>Review relevant supply and demand by date. Determine whether another requirement consumes the quantity or whether a future receipt falls outside the requested date or configured horizon.</li>

<li>Check product allocation, supply protection, and other aATP controls only when they are active for the scenario. Record the protection or allocation object that changes the result.</li>

<li>Repeat the check in the same document context and confirm the resulting schedule-line quantity and date. A different simulation context may legitimately produce a different answer.</li>

</ol>

<h2>Evidence to retain</h2>

<ul>
  <li>Inventory report name, selection criteria, timestamp, and stock category—not only a screenshot of the total.</li>
  <li>Sales document/item, requested and confirmed quantities/dates, plant and storage location, checking group/rule, and check result.</li>
  <li>Relevant requirements and receipts with dates, plus any allocation or protection restriction.</li>
  <li>Whether the mismatch is isolated to one document context or affects a wider material/location population.</li>
</ul>

<h2>Limitations and boundaries</h2>

<p>This guide does not prescribe one ATP configuration or assume every landscape uses advanced ATP. Classic availability checking, aATP, external order management, allocation services, EWM, retail stock segments, and custom fulfilment sourcing can produce different evidence paths. Confirm the active architecture before changing scope or protection rules.</p>

<h2>Official references</h2>

<ul>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/d0960a564b52fb37e10000000a44147b.html">SAP: scope of availability check</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/199d86d0f85e4ea982a529c6e0409660.html?locale=en-us">SAP: availability-check scope and levels</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9905622a5c1f49ba84e9076fc83a9c2c/e7582f68181d476ab37550c6ebe6d25e.html">SAP: stock protection using product allocation</a></li>
</ul>

<p>Stock visibility and promisable stock answer different questions. The gap is diagnostic evidence: locate the scope, date, demand, location, or prioritization rule that explains it before changing inventory or ATP settings.</p>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/concepts/sap-atp-is-not-inventory/">SAP ATP Is Not Inventory</a></li>
<li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
<li><a href="/atlas/concepts/store-receiving-sap-retail/">Store Receiving in SAP Retail</a></li>
<li><a href="/atlas/maps/order-to-cash-map/">SAP Order-to-Cash Process Map</a></li>
<li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
