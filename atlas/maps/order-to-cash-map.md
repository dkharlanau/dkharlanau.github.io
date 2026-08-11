---

title: SAP Order-to-Cash Process Map
layout: default
description: A source-backed SAP order-to-cash process map for tracing sales order, delivery, goods issue, billing, accounting, and clearing failures.
permalink: /atlas/maps/order-to-cash-map/
last_modified_at: 2026-08-11
atlas_section: maps
domain: Business operations
subdomain: Sales fulfillment
concept_type: process map
sap_area: SD / FI / logistics integration
business_process: Order to cash
status: reviewed
verified: true
level: 2
last_reviewed: 2026-05-06

tags:
  - order-to-cash
  - sap-sd
  - sap-mm
related: 
  - "/atlas/concepts/order-to-cash/"
  - "/atlas/diagnostics/sap-invoice-split-analysis/"
  - "/atlas/concepts/sap-atp-is-not-inventory/"
  - "/atlas/concepts/sap-stock-exists-not-promisable/"
robots: index,follow
sitemap: true
short_title: Order to Cash Map
h1: Order to cash map
subtitle: A map for tracing where an O2C process stopped and which evidence should exist at each stage.
author: Dzmitryi Kharlanau
---

**Sources:** [SAP sales document flow](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6aa7c6535e601e4be10000000a174cb4.html), [SAP outbound delivery creation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c7894a248ca14f74aca67f97528e5ad7/c81fbf53f106b44ce10000000a174cb4.html), and [SAP sales billing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/4c74c957b7018809e10000000a4450e5.html).
**Date checked:** 2026-08-11
**Confidence:** high for the standard document-chain checkpoints; medium for landscape-specific controls, interfaces, and ownership.
**Related page/topic:** /atlas/concepts/order-to-cash/
**Practical implication:** Start with the last correct business document and its item-level status, then investigate the control responsible for the missing transition.
**Tags:** order-to-cash, sap-sd, document-flow, fulfillment, billing

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/maps/">Maps</a></li><li aria-current="page">Order to Cash Map</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP order-to-cash process map</h1>

<p class="note-subtitle">A map for tracing where an O2C process stopped and which evidence should exist at each stage.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>Business operations</dd></div><div><dt>Type</dt><dd>process map</dd></div><div><dt>Reviewed</dt><dd>2026-05-06</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>Use this map when a customer demand exists but the expected delivery, goods issue, invoice, accounting entry, or clearing result does not. The fastest starting point is the last correct business document—not the team that first received the ticket.</p>

<h2>Process and evidence flow</h2>

<figure class="atlas-process-map" aria-labelledby="o2c-flow-caption">
  <figcaption id="o2c-flow-caption">Standard order-to-cash checkpoints. Each step names the business outcome and the evidence that should exist before the process moves forward.</figcaption>
  <ol class="atlas-process-map__steps">
    <li><strong>Demand</strong><span>Sales order</span><small>Customer, material, quantity, requested date, partners, and commercial terms are valid.</small></li>
    <li><strong>Commit</strong><span>Confirmed schedule</span><small>Availability, credit, pricing, incompletion, and delivery controls permit execution.</small></li>
    <li><strong>Fulfil</strong><span>Delivery and goods issue</span><small>Picking and shipping evidence exists, and goods issue records the inventory event.</small></li>
    <li><strong>Bill</strong><span>Billing and accounting</span><small>The billable reference produces the intended invoice and financial posting.</small></li>
    <li><strong>Settle</strong><span>Receivable and clearing</span><small>Payment, deduction, dispute, or clearing evidence resolves the open customer item.</small></li>
  </ol>
</figure>

<h2>Checkpoint-to-evidence map</h2>

<table>
  <thead><tr><th>Transition</th><th>Evidence that should exist</th><th>Typical reason it stops</th><th>Next route</th></tr></thead>
  <tbody>
    <tr><td>Demand → commitment</td><td>Complete sales order item, confirmed quantity/date, pricing and credit status.</td><td>Incompletion, master data, pricing, credit, availability, or manual block.</td><td><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">Sales order block diagnosis</a></td></tr>
    <tr><td>Commitment → fulfilment</td><td>Delivery-due schedule line and outbound delivery with executable status.</td><td>Delivery block, shipping-point or route data, due-date selection, stock, warehouse, or interface issue.</td><td><a href="/atlas/diagnostics/sap-delivery-processing-diagnostics/">Delivery processing diagnostics</a></td></tr>
    <tr><td>Fulfilment → billing</td><td>Goods issue or another valid billable reference, billing status, and complete billing data.</td><td>Billing block, copy control, split criteria, incomplete reference, or posting error.</td><td><a href="/atlas/diagnostics/sap-billing-block-analysis/">Billing block analysis</a></td></tr>
    <tr><td>Billing → accounting</td><td>Billing document plus the expected accounting transfer and customer open item.</td><td>Account determination, tax, posting period, partner, or interface failure.</td><td><a href="/atlas/diagnostics/sap-invoice-split-analysis/">Invoice split analysis</a></td></tr>
    <tr><td>Receivable → settlement</td><td>Payment, clearing document, deduction, dispute, or dunning status.</td><td>Reference mismatch, underpayment, bank allocation, dispute, or payment-processing issue.</td><td><a href="/atlas/diagnostics/sap-payment-run-dunning-diagnostics/">Payment and dunning diagnostics</a></td></tr>
  </tbody>
</table>

<h2>How to trace a stopped O2C process</h2>

<ol>
  <li>Capture the customer, sales document and item, material, requested date, expected outcome, and business impact.</li>
  <li>Open the sales document flow and inspect item-level status. SAP document flow lists existing preceding and subsequent documents; absence of a document is different from an existing document in error.</li>
  <li>Name the failed transition: order-to-delivery, delivery-to-goods-issue, reference-to-billing, billing-to-accounting, or receivable-to-clearing.</li>
  <li>Check the control that owns that transition. Separate master data, configuration, application status, integration, timing, and approval before proposing a fix.</li>
  <li>Confirm the next business proof after correction. A green technical status is not enough if the delivery, invoice, accounting entry, or clearing result is still absent.</li>
</ol>

<h2>Evidence to capture before routing</h2>

<ul>
  <li>Sales document and item, document type, customer, material, plant, requested and confirmed dates.</li>
  <li>Current header and item statuses, active block or incompletion reason, and document-flow screenshot or export.</li>
  <li>Last successful document, missing next document, exact error text, and time of the last processing attempt.</li>
  <li>Expected business outcome and owning team for the failed control.</li>
</ul>

<h2>Boundaries and non-goals</h2>

<p>This is a standard diagnostic map, not a claim that every SAP sales process follows one document chain. Returns, third-party processing, intercompany sales, services, billing plans, EWM, transportation, tax engines, and external commerce platforms introduce additional documents and controls. Preserve the same method: identify the last correct evidence and the missing transition.</p>

<h2>Official references</h2>

<ul>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6aa7c6535e601e4be10000000a174cb4.html">SAP: displaying a sales document flow</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c7894a248ca14f74aca67f97528e5ad7/c81fbf53f106b44ce10000000a174cb4.html">SAP: outbound delivery creation</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/4c74c957b7018809e10000000a4450e5.html">SAP: sales billing</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/43e92f5581788a05e10000000a441470.html">SAP: order-to-cash performance checkpoints</a></li>
</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
<li><a href="/atlas/concepts/sap-atp-is-not-inventory/">SAP ATP Is Not Inventory</a></li>
<li><a href="/atlas/concepts/sap-stock-exists-not-promisable/">SAP Stock Exists but Is Not Promisable</a></li>
<li><a href="/atlas/diagnostics/sap-delivery-processing-diagnostics/">SAP Delivery Processing Diagnostics</a></li>
<li><a href="/atlas/diagnostics/sap-invoice-split-analysis/">SAP Invoice Split Analysis</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
