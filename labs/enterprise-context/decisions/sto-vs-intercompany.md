---
layout: default
title: "STO or Intercompany Sales? — SAP Logistics Decision Card"
description: "A compact SAP logistics decision model for choosing stock transport order or intercompany sales flow."
permalink: /labs/enterprise-context/decisions/sto-vs-intercompany/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-17
last_reviewed: 2026-08-17
hide_global_cta: true
review_method: "authored decision model over reviewed procurement, sales, inventory, and finance-logistics material"
structured_data:
  type: TechArticle
primary_topic: "sap-sto-vs-intercompany"
semantic_links:
  - type: "part_of"
    title: "SAP Decision Cards"
    url: "/labs/enterprise-context/decisions/"
  - type: "depends_on"
    title: "Procurement Process & Decision Map"
    url: "/labs/enterprise-context/procurement/"
  - type: "related_topic"
    title: "Sales Processes"
    url: "/labs/enterprise-context/sales-processes/"
  - type: "related_topic"
    title: "FI/CO for Logistics"
    url: "/labs/enterprise-context/finance-logistics/"
tags: [sap, logistics, procurement, sales, sto, intercompany]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/decisions/">Decision Cards</a></li><li aria-current="page">STO or Intercompany?</li></ol></nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal><div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">Decision Card / Cross-functional Logistics</p><h1>STO or<br />intercompany sales?</h1><p>Both can move material between parts of a group. They do not represent the same business relationship, and choosing by transaction familiarity usually creates accounting or ownership problems later.</p></div><div class="research-canvas__signal"><p>My default question</p><div class="research-canvas__signal-line"><span>01</span><strong>Who owns?</strong><small>Stock and legal responsibility</small></div><div class="research-canvas__signal-line"><span>02</span><strong>Who sells?</strong><small>Commercial relationship</small></div><div class="research-canvas__signal-line"><span>03</span><strong>Who settles?</strong><small>Financial consequence</small></div><em>Model the business relation before the document flow.</em></div></header>

  <section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">rule</span><p><strong>Decision in one sentence:</strong> prefer STO when the primary problem is controlled stock transfer and internal replenishment; prefer an intercompany sales model when the process is fundamentally a commercial sale across company boundaries and billing is part of the business contract.</p></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Decision drivers</p><h2>Do not decide from the shipping step alone.</h2></header><div class="ecg-decision-columns">
    <div><h3>1. Legal and company-code boundary</h3><p>Ask whether the movement stays inside one legal accounting boundary or crosses entities that need a commercial relationship and settlement.</p></div>
    <div><h3>2. Business intent</h3><p>Replenishment, plant-to-plant balancing, and supply redistribution point toward STO. Customer-like selling between group entities points toward intercompany sales.</p></div>
    <div><h3>3. Billing requirement</h3><p>If the supplying entity must issue an intercompany billing document as part of the designed process, that is a strong signal for the sales model.</p></div>
    <div><h3>4. Receiving process</h3><p>Decide whether the receiver behaves mainly as a purchasing location receiving stock or as a buying company participating in a commercial order-to-cash / procure-to-pay relationship.</p></div>
    <div><h3>5. Ownership of exceptions</h3><p>Short shipment, price difference, goods in transit, returns, and invoice mismatch must have clear owners on both sides.</p></div>
  </div></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Default choice</p><h2>Use the lightest process that represents reality.</h2></header><div class="decision-table"><table><thead><tr><th>Model</th><th>Good fit</th><th>Warning sign</th></tr></thead><tbody>
    <tr><td><strong>STO</strong></td><td>Internal replenishment, planned stock movement, plant or storage-location supply, controlled goods issue and receipt.</td><td>The business expects a true commercial sale, legal-entity billing, or pricing logic that is central to the relationship.</td></tr>
    <tr><td><strong>Intercompany sales</strong></td><td>Separate selling and supplying entities, commercial ownership, customer-facing order flow, and intercompany settlement.</td><td>The process is really only inventory redistribution and the sales model adds documents without adding a real business responsibility.</td></tr>
  </tbody></table></div></section>

  <section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">warning</span><p><strong>I change the default when:</strong> tax, transfer pricing, customs, export control, valuation, goods-in-transit design, third-party ownership, or regional legal requirements create a stronger boundary than the logistics flow alone.</p><p><strong>Failure ownership:</strong> reconcile the physical movement and the financial movement separately. A delivered quantity can be correct while valuation, billing, GR/IR, or intercompany settlement is still wrong.</p></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Evidence path</p><h2>Trace both sides of the flow.</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/procurement/"><span>P2P</span><strong>Procurement</strong><small>Requirement, source, purchasing document, receipt, invoice, and settlement logic.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a><a href="/labs/enterprise-context/sales-processes/"><span>O2C</span><strong>Sales</strong><small>Order, delivery, billing, pricing, and cross-company sales responsibilities.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a><a href="/labs/enterprise-context/finance-logistics/"><span>FI</span><strong>Finance-logistics boundary</strong><small>Valuation, postings, reconciliation, and financial completion.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a></div></section>
</div>
