---

title: SAP Procure-to-Pay Process Map
layout: default
description: A source-backed SAP procure-to-pay map for tracing requisition, purchase order, receipt, invoice verification, GR/IR, and payment failures.
permalink: /atlas/maps/procure-to-pay-map/
last_modified_at: 2026-08-11
atlas_section: maps
domain: Business operations
subdomain: Procurement
concept_type: process map
sap_area: MM / FI integration
business_process: Procure to pay
status: reviewed
verified: true
level: 2
last_reviewed: 2026-05-06

tags:
  - procure-to-pay
  - sap-mm
  - procurement
related: 
  - "/atlas/sap/gr-ir-clearing-explained/"
  - "/atlas/diagnostics/sap-goods-receipt-diagnostics/"
  - "/atlas/data-quality/sap-master-data-quality/"
  - "/atlas/data-quality/master-data-governance-failure-modes/"
  - "/atlas/automation/operational-memory-for-sap-ams/"
robots: index,follow
sitemap: true
short_title: Procure to Pay Map
h1: Procure to pay map
subtitle: A practical map for connecting procurement demand, purchasing documents, goods receipt, invoice verification, and financial clearing.
author: Dzmitryi Kharlanau
---

**Sources:** [SAP goods receipts for purchase orders](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/240fcdcc71c640ea9aa9691500b34889/a363bd534f22b44ce10000000a174cb4.html), [SAP invoice processing](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ed84b70c199d4470ae2e5ccb93b2e45b/ab6fb6531de6b64ce10000000a174cb4.html), and [SAP invoices for purchase orders](https://help.sap.com/docs/SAP_S4HANA_ON-PREMI-SE/af9ef57f504840d2b81be8667206d485/be5eb6531de6b64ce10000000a174cb4.html).
**Date checked:** 2026-08-11
**Confidence:** high for the standard purchasing, receipt, and invoice checkpoints; medium for landscape-specific approvals and payment controls.
**Related page/topic:** /atlas/sap/gr-ir-clearing-explained/
**Practical implication:** Reconcile the purchasing document, receipt evidence, invoice evidence, and accounting result before treating a blocked payment as a finance-only issue.
**Tags:** procure-to-pay, sap-mm, procurement, invoice-verification, gr-ir

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/maps/">Maps</a></li><li aria-current="page">Procure to Pay Map</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>SAP procure-to-pay process map</h1>

<p class="note-subtitle">A practical map for connecting procurement demand, purchasing documents, goods receipt, invoice verification, and financial clearing.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>Business operations</dd></div><div><dt>Type</dt><dd>process map</dd></div><div><dt>Reviewed</dt><dd>2026-05-06</dd></div></dl></aside>

<div class="note-body">

<h2>Where this fits</h2>

<p>Use this map when a procurement need exists but the expected purchase order, receipt, invoice, liability, or payment result does not. Procure-to-pay incidents are easiest to resolve when the physical, commercial, and accounting evidence is compared at the same purchase-order item.</p>

<h2>Process and evidence flow</h2>

<figure class="atlas-process-map" aria-labelledby="p2p-flow-caption">
  <figcaption id="p2p-flow-caption">Standard procure-to-pay checkpoints. Each step identifies the business outcome and the evidence needed by the next control.</figcaption>
  <ol class="atlas-process-map__steps">
    <li><strong>Need</strong><span>Requisition or demand</span><small>Quantity, date, account assignment, specification, and approval need are explicit.</small></li>
    <li><strong>Order</strong><span>Purchase order</span><small>Supplier, price, quantity, delivery terms, account assignment, and release status are valid.</small></li>
    <li><strong>Receive</strong><span>Goods receipt or service acceptance</span><small>Physical or service evidence is posted against the intended PO item.</small></li>
    <li><strong>Verify</strong><span>Supplier invoice</span><small>Price, quantity, tax, reference, and receipt evidence pass the required checks.</small></li>
    <li><strong>Settle</strong><span>Liability and payment</span><small>The invoice is released, due, paid, and cleared with the expected accounting result.</small></li>
  </ol>
</figure>

<h2>Checkpoint-to-evidence map</h2>

<table>
  <thead><tr><th>Transition</th><th>Evidence that should exist</th><th>Typical reason it stops</th><th>Next route</th></tr></thead>
  <tbody>
    <tr><td>Need → purchase order</td><td>Approved requisition or other valid demand, source decision, and complete account assignment.</td><td>Missing source, release, budget, master data, contract, or purchasing responsibility.</td><td><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">PO creation diagnostics</a></td></tr>
    <tr><td>Purchase order → receipt</td><td>Released PO item with open quantity and delivery or service evidence.</td><td>Closed/deleted item, wrong reference, quantity/UoM mismatch, material, batch, quality, or service-entry issue.</td><td><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">Goods receipt diagnostics</a></td></tr>
    <tr><td>Receipt → invoice</td><td>PO history showing the applicable goods receipt or accepted service and its quantity/value.</td><td>Missing receipt, wrong PO item, partial delivery, return, or GR-based invoice-verification mismatch.</td><td><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">Invoice verification diagnostics</a></td></tr>
    <tr><td>Invoice → liability</td><td>Posted invoice document, variance status, tax result, and supplier open item.</td><td>Price, quantity, tax, duplicate, tolerance, account, period, or approval issue.</td><td><a href="/atlas/diagnostics/sap-three-way-match-diagnostics/">Three-way match diagnostics</a></td></tr>
    <tr><td>Liability → settlement</td><td>Due and released supplier item, payment proposal/run, bank result, and clearing document.</td><td>Payment block, terms, bank data, payment method, approval, exception, or clearing mismatch.</td><td><a href="/atlas/diagnostics/sap-payment-run-dunning-diagnostics/">Payment-run diagnostics</a></td></tr>
  </tbody>
</table>

<h2>How to trace a stopped P2P process</h2>

<ol>
  <li>Capture the purchase order and item, supplier, material or service, expected quantity/value, company code, plant, and expected business result.</li>
  <li>Use purchase-order history to align the order, goods or service receipt, invoice, returns, reversals, and credit memos at item level.</li>
  <li>Name the failed transition: demand-to-order, order-to-receipt, receipt-to-invoice, invoice-to-liability, or liability-to-payment.</li>
  <li>Separate a real commercial variance from missing or late evidence. Do not raise tolerance, release an invoice, or clear GR/IR merely to remove a technical symptom.</li>
  <li>After correction, confirm the downstream result: usable stock or accepted service, correctly posted invoice, expected GR/IR position, and cleared supplier liability.</li>
</ol>

<h2>Evidence to capture before routing</h2>

<ul>
  <li>PO and item, supplier, material/service, quantity and value, account assignment, plant, company code, and document currency.</li>
  <li>Release status, open quantity, delivery-completed/final-invoice indicators, PO history, and exact variance or block.</li>
  <li>Receipt, reversal, return, invoice, credit memo, payment, and clearing document references where they exist.</li>
  <li>Expected business outcome, last correct evidence, and the owner authorized to approve any commercial exception.</li>
</ul>

<h2>Boundaries and non-goals</h2>

<p>This map does not assume every procurement path requires a material goods receipt. Services, limits, evaluated receipt settlement, consignment, subcontracting, intercompany, central procurement, and external networks use different evidence. The diagnostic rule remains the same: identify what the next control expects and prove whether that evidence exists.</p>

<h2>Official references</h2>

<ul>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/240fcdcc71c640ea9aa9691500b34889/a363bd534f22b44ce10000000a174cb4.html">SAP: goods receipts for purchase orders</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ed84b70c199d4470ae2e5ccb93b2e45b/ab6fb6531de6b64ce10000000a174cb4.html">SAP: invoice processing</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMI-SE/af9ef57f504840d2b81be8667206d485/be5eb6531de6b64ce10000000a174cb4.html">SAP: invoices for purchase orders and GR/IR</a></li>
  <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/a97eb65334e6b54ce10000000a174cb4.html">SAP: goods-receipt-based invoice verification</a></li>
</ul>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
<li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a></li>
<li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a></li>
<li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
<li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
<li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
