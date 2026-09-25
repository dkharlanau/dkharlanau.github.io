---
layout: default
title: "SAP Procurement KPIs"
description: "How to define procurement KPIs in SAP without confusing document counts with process performance, including cycle time, delivery performance, supplier variance, and GR/IR aging."
permalink: /atlas/sap/sap-procurement-kpis/
atlas_section: sap
domain: SAP operations
subdomain: Procurement analytics
concept_type: SAP concept
sap_area: MM / analytics
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - analytics
  - kpis
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Procurement KPIs</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP procurement KPIs</h1>
    <p class="note-subtitle">A useful procurement KPI starts with a business definition. SAP data comes second.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM / analytics</dd></div>
      <div><dt>Reviewed</dt><dd>2026-09-22</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>A KPI is a definition before it is a query</h2>
    <p>SAP contains detailed purchasing history, but that does not make every calculation meaningful. A procurement KPI needs a clear event, population, denominator, and time rule. If we cannot explain those four things in plain language, the resulting chart is usually harder to trust than it looks.</p>

    <p>Consider “purchase-order cycle time.” Does it start when a purchase requisition is created, approved, released, or first sent to a buyer? Does it end when the purchase order is created or sent to the supplier? SAP itself publishes a <strong>Purchase Requisition-to-Order Cycle Time</strong> KPI with a specific definition. A custom dashboard can use a different definition, but it should say so explicitly.</p>

    <h2>Cycle time measures flow, not buyer speed alone</h2>
    <p>Requisition-to-order time is useful because it shows how long demand spends inside the sourcing and approval process before an order reaches the supplier. Long time can come from buyer workload, approvals, incomplete requisitions, sourcing events, missing master data, or deliberate waiting. The number needs segmentation before it becomes a diagnosis.</p>

    <p>We therefore compare like with like: purchasing organization, purchasing group, material group, source type, or another business dimension that explains the process. Mixing automatically generated routine demand with complex manually sourced purchases can make the average almost meaningless.</p>

    <h2>Delivery performance needs a reference date and a completion rule</h2>
    <p>“On-time delivery” sounds simple until partial deliveries appear. One purchase-order item can have several schedule lines and several goods receipts. A late first receipt followed by an on-time final receipt tells a different story from a complete shipment that arrived one day late.</p>

    <p>Current SAP S/4HANA analytics reflects this nuance through supplier-evaluation KPIs. The operational supplier score can combine time, quantity, price, and quality variance, while dedicated time and quantity views expose the underlying dimensions. That is a better model than reducing supplier performance to one home-made percentage without explaining how early, late, partial, or over-deliveries are treated.</p>

    <h2>Quantity and price variance are supplier signals, but also process signals</h2>
    <p>A quantity variance compares what was expected with what was actually delivered. SAP's standard supplier-evaluation logic considers both under-delivery and over-delivery. Price variance can reveal supplier behavior, but it can also expose stale purchase-order prices, unprocessed contract changes, or incorrect master data. Before assigning the problem to the supplier, we need to know whether SAP's purchasing documents represented the agreement correctly.</p>

    <h2>GR/IR aging shows unfinished procurement</h2>
    <p>GR/IR aging is different from a classic supplier score. It measures how long goods receipts and invoice receipts remain unmatched. An old balance can mean a missing invoice, a missing receipt, a quantity difference, a correction that was never completed, or a purchase-order item that should be reconciled because no further documents are expected.</p>

    <p>For this KPI, the useful unit is usually the purchase-order item and its open GR/IR state rather than a raw G/L line count. This keeps the metric connected to the procurement process that created the accounting balance.</p>

    <h2>Contract coverage and maverick buying require a policy definition</h2>
    <p>“Spend under contract” normally asks how much purchasing value is linked to an approved agreement. “Maverick buying” usually asks how much spend bypasses an expected procurement channel. Neither has one universal SAP formula. Some organizations require a requisition for almost everything; others allow direct purchase orders for defined categories or values.</p>

    <p>We should therefore encode the procurement policy first and only then map SAP documents to it. A purchase order without a requisition is not automatically non-compliant. A purchase order without a contract reference is not automatically uncontrolled spend. The KPI becomes useful only when the exception rule matches the company's real process.</p>

    <h2>Five questions before publishing a procurement dashboard</h2>
    <p>Before we trust a number, we check its grain, scope, dates, reversals, and currency. Is the metric calculated per document, item, schedule line, receipt, or supplier? Which company codes, plants, and purchasing organizations are included? Which date defines the period? How are cancellations and reversals handled? If values are aggregated, in which currency are they comparable?</p>

    <p>Those questions sound basic, but they prevent most procurement dashboards from becoming polished summaries of inconsistent data.</p>

    <h2>Sources</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/2ee7f056cfe4174ce10000000a4450e5.html">SAP Help: Purchase Requisition-to-Order Cycle Time</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/d628857f20b146dc818ffdcc11e3dea0.html">SAP Help: Operational Supplier Evaluation</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/3a57c255962a3105e10000000a44538d.html">SAP Help: Supplier Evaluation by Quantity</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">SAP GR/IR Clearing Explained</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
