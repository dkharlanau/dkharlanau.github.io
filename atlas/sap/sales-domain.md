---
layout: default
title: "Sales — SAP S/4HANA Domain"
description: "A clear overview of SAP S/4HANA Sales: the document flow, the master data and configuration behind it, and the links to delivery, billing, and finance."
permalink: /atlas/sap/sales-domain/
atlas_section: sap
domain: SAP operations
subdomain: Sales
concept_type: domain
sap_area: "SD"
business_process: "Order to cash"
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau

tags:
  - sap-sd
  - sales
  - order-to-cash
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/concepts/order-to-cash/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /atlas/diagnostics/sap-invoice-split-analysis/
  - /atlas/sap/sap-s4hana/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Sales Domain</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Domain</p>
    <h1>Sales — SAP S/4HANA domain</h1>
    <p class="note-subtitle">From customer demand to delivery and billing, with the document flow that keeps the process connected.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>SD / Sales</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until domain claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Sales is a document flow, not one module screen</h2>
    <p>In SAP S/4HANA, Sales represents the commercial side of the customer process. We may start with an inquiry or quotation, but the central object is usually the sales order. From there, SAP can create follow-on documents for delivery and billing, while Finance receives the accounting impact of the billing document.</p>

    <p>The useful way to understand the domain is to follow this chain rather than memorize transactions. A sales order describes what the customer wants and under which commercial terms. Schedule lines hold quantities and dates. An outbound delivery turns the confirmed demand into a logistics document. The billing document turns the fulfilled or billable quantity into a customer invoice. The exact flow varies by scenario: some processes are delivery-related, while others can be billed directly from the order.</p>

    <h2>What controls a sales order</h2>
    <p>A sales order looks simple on the surface, but its behavior is assembled from several layers. The sales document type controls the overall document. Item categories define how individual items behave. Schedule line categories control important logistics behavior below the item. Pricing builds the commercial value from conditions. Partner determination supplies roles such as sold-to, ship-to, bill-to, and payer.</p>

    <p>Master data provides the business context. The customer is represented through the Business Partner model with customer roles and sales-area data. Product or material data contributes sales units, delivering data, item-category information, tax-relevant attributes, and other controls. When one of these layers is incomplete or inconsistent, the symptom often appears later in delivery or billing even though the cause started in the order.</p>

    <h2>How Sales connects to the rest of S/4HANA</h2>
    <p>Sales is tightly connected to logistics. Availability checks can influence confirmed quantities and dates. Delivery processing connects the order with shipping and warehouse execution. Depending on the landscape, warehouse work may be handled in embedded or decentralized EWM. Transportation planning can involve SAP Transportation Management. Make-to-order, third-party, and other scenarios also connect Sales with production or procurement.</p>

    <p>Billing is the bridge to Finance. A billing document can create the accounting data for customer receivables and revenue posting. This is why a problem that users describe as “an SD issue” may actually depend on account determination, credit management, tax, logistics status, or master data outside the immediate sales document.</p>

    <h2>Pricing, partners, and document control</h2>
    <p>Three mechanisms explain a large part of day-to-day Sales behavior. <strong>Pricing</strong> determines the price elements that apply to the transaction. <strong>Partner determination</strong> provides the business partners needed by the process. <strong>Document control</strong> — especially document types, item categories, schedule line categories, and copying control — determines how data and status move through the chain.</p>

    <p>We usually understand a sales process faster when we ask which layer owns a behavior. If the problem is a missing ship-to party, pricing configuration is unlikely to be the answer. If an item cannot create a delivery, the item and schedule-line behavior matters more than the invoice. SAP Sales becomes much easier to reason about once these responsibilities are separated.</p>

    <h2>A simple end-to-end example</h2>
    <p>Consider a standard stock sale. The customer places an order for ten units. SAP creates the sales order, determines partners and pricing, and confirms quantity and date according to the available process. The order then becomes relevant for outbound delivery. Warehouse execution prepares the goods and posts goods issue. Billing uses the relevant preceding document to create the invoice, and the billing data is transferred to Financial Accounting.</p>

    <p>The important point is not that every scenario follows exactly these steps. The point is that each document has a job and passes controlled data to the next one. When we read the process this way, document flow becomes a map of what has happened rather than a list of unrelated SAP objects.</p>

    <h2>Where to go deeper</h2>
    <p>This page is the domain map. Detailed topics belong on narrower pages: item category determination, pricing condition technique, sales-order blocks, invoice splits, partner determination, availability, credit, delivery, and billing. Keeping those subjects separate avoids turning one overview into a catalogue of every SD setting.</p>

    <h2>Sources</h2>
    <ul>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/fundamental-customizing-in-sap-s-4hana-sales/executing-the-sales-and-distribution-process">Executing the Sales and Distribution Process</a>.</li>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/exploring-sap-s-4hana-sales-essentials/executing-the-billing-process-and-the-integration-to-sap-s-4hana-finance_e2dd5db3-73c3-4cda-8ad5-1e7f39f04fba">Executing the Billing Process and the Integration to SAP S/4HANA Finance</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/0e70b6535fe6b74ce10000000a174cb4.html">Invoice</a>.</li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
      <li><a href="/atlas/diagnostics/sap-invoice-split-analysis/">SAP Invoice Split Analysis</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
