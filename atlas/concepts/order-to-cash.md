---

layout: default
title: "Order to Cash"
description: "A concise operational explanation of order to cash as the chain from customer demand to fulfillment, billing, and payment."
permalink: /atlas/concepts/order-to-cash/
atlas_section: concepts
domain: Business operations
subdomain: Sales fulfillment
concept_type: business process
sap_area: "SD / FI integration"
business_process: Order to cash
status: reviewed
verified: true
level: 2
last_reviewed: 2026-05-06
author: Dzmitryi Kharlanau

tags:
  - order-to-cash
  - sap-sd
related:
  - /atlas/concepts/sap-atp-is-not-inventory/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /services/sap-o2c-process-audit/
  - /atlas/maps/order-to-cash-map/
  - /atlas/concepts/sap-stock-exists-not-promisable/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">Order to Cash</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Concept</p>
    <h1>Order to cash</h1>
    <p class="note-subtitle">The operating chain that turns customer demand into delivery, billing, accounting, and cash collection.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>SD with finance and logistics touchpoints</dd></div>
      <div><dt>Reviewed</dt><dd>06 May 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Order to cash is the end-to-end flow from customer demand to financial settlement. In a SAP-heavy environment it usually spans sales order capture, availability, delivery, goods issue, billing, accounting, receivables, and dispute handling.</p>

    <h2>Why it matters</h2>
    <p>O2C is where customer promise, inventory reality, logistics execution, pricing, tax, credit, and revenue recognition meet. Weakness in one area often appears as a support ticket somewhere else: an order block, a failed delivery, a billing split, a pricing dispute, or a delayed cash collection.</p>

    <h2>Useful operating view</h2>
    <ul>
      <li><strong>Demand:</strong> customer, product, quantity, requested date, and commercial terms.</li>
      <li><strong>Commitment:</strong> availability, credit/risk controls, pricing, and order validation.</li>
      <li><strong>Execution:</strong> delivery creation, picking, packing, goods issue, and shipment handoff.</li>
      <li><strong>Billing:</strong> invoice creation, account determination, tax, and customer communication.</li>
      <li><strong>Cash:</strong> receivables, payment, clearing, disputes, and credit feedback.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>O2C diagnostics should follow the document flow and the business event sequence. Ask where the process stopped, which document exists, which document is missing, and which team owns the failed control. This prevents “SAP issue” from becoming a vague label for a cross-functional operating problem.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-atp-is-not-inventory/">SAP ATP Is Not Inventory</a></li>
      <li><a href="/atlas/maps/order-to-cash-map/">Order to Cash Map</a></li>
      <li><a href="/atlas/concepts/sap-stock-exists-not-promisable/">SAP Stock Exists but Is Not Promisable</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
