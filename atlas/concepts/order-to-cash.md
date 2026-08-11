---

layout: default
title: "SAP Order-to-Cash Process"
description: "A source-backed explanation of the SAP order-to-cash process from sales order and ATP through delivery, billing, accounting, and clearing."
permalink: /atlas/concepts/order-to-cash/
last_modified_at: 2026-08-11
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

**Sources:** [SAP sales document flow](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6aa7c6535e601e4be10000000a174cb4.html), [SAP outbound delivery creation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c7894a248ca14f74aca67f97528e5ad7/c81fbf53f106b44ce10000000a174cb4.html), and [SAP sales billing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/4c74c957b7018809e10000000a4450e5.html).
**Date checked:** 2026-08-11
**Confidence:** high for the standard document chain; medium for variations introduced by industry processes, extensions, and external systems.
**Related page/topic:** /atlas/maps/order-to-cash-map/
**Practical implication:** Diagnose an O2C delay as a failed transition between business documents and controls, not as a generic module or team problem.
**Tags:** order-to-cash, sap-sd, fulfillment, billing, receivables

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">SAP Order-to-Cash Process</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Concept</p>
    <h1>SAP order-to-cash process</h1>
    <p class="note-subtitle">The document and control chain that turns customer demand into a fulfilment promise, delivery, billing, accounting, and settlement.</p>
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
    <p>Order to cash is the end-to-end operating chain from customer demand to financial settlement. In a standard sell-from-stock path, the evidence normally progresses through a sales order, availability confirmation, outbound delivery, goods issue, billing document, accounting entry, receivable, and clearing result.</p>
    <p>The document chain is not merely technical history. Each transition represents a business control: what can be promised, what can be shipped, what can be invoiced, what can be posted, and what can be considered settled.</p>

    <h2>Why it matters</h2>
    <p>O2C is where customer promise, inventory reality, logistics execution, pricing, tax, credit, accounting, and receivables meet. A failure in one control often appears in another team's queue: an availability problem looks like an order issue, a warehouse status looks like a billing delay, or a payment reference problem looks like an open-credit problem.</p>

    <h2>Operating decisions and evidence</h2>
    <table>
      <thead><tr><th>Stage</th><th>Decision</th><th>Evidence</th><th>Frequent blind spot</th></tr></thead>
      <tbody>
        <tr><td>Demand</td><td>Is the requested transaction commercially and operationally complete?</td><td>Sales order header/item data, partners, material, quantity, dates, price, tax, and incompletion status.</td><td>The order exists, but an item-level control prevents the next document.</td></tr>
        <tr><td>Commitment</td><td>What quantity and date can be promised under the applicable rules?</td><td>Confirmed schedule lines, availability result, credit/risk status, and active blocks.</td><td>Visible stock is treated as automatically promisable.</td></tr>
        <tr><td>Execution</td><td>Can the confirmed demand be physically fulfilled?</td><td>Delivery, picking/packing or warehouse status, goods issue, and logistics handoff.</td><td>A delivery exists, but its status does not permit goods issue or billing.</td></tr>
        <tr><td>Billing</td><td>Which reference is billable, and can it post correctly?</td><td>Billing due status, invoice, split analysis, tax/account determination, and accounting transfer.</td><td>Invoice creation is checked without confirming the billable reference and its status.</td></tr>
        <tr><td>Settlement</td><td>Has the receivable been resolved according to the business outcome?</td><td>Customer open item, payment, clearing, deduction, dispute, or dunning status.</td><td>Technical payment receipt is confused with correct allocation and clearing.</td></tr>
      </tbody>
    </table>

    <h2>How to diagnose across teams</h2>
    <ol>
      <li>Start with the customer's expected outcome and the exact sales-document item.</li>
      <li>Use document flow and item statuses to find the last correct evidence and the first missing or blocked transition.</li>
      <li>Separate the cause into master data, configuration, application status, integration, timing, or approval ownership.</li>
      <li>Route the incident with the evidence needed by the owning team, not only the symptom reported by the user.</li>
      <li>Close the incident only after the expected downstream document or settlement evidence exists.</li>
    </ol>

    <h2>Useful measures</h2>
    <p>Process health is clearer when teams measure transitions rather than raw ticket counts. Useful signals include order-to-confirmation time, order-to-delivery time, goods-issue-to-billing time, billing-to-accounting failures, aged open deliveries, billing blocks, disputed receivables, and cash-application delay. SAP's order-to-cash performance guidance similarly treats blocks and lead times between process events as operational evidence.</p>

    <h2>Support takeaway</h2>
    <p>Follow the document flow and business-event sequence. Ask which document exists, which result should follow, which control owns that transition, and what proof will show recovery. This prevents “SAP issue” from becoming a vague label for a cross-functional operating problem.</p>

    <h2>Boundaries and process variants</h2>
    <p>Third-party, intercompany, make-to-order, returns, services, billing plans, subscriptions, external commerce, EWM, and transportation scenarios add or replace documents. Do not force them into a sell-from-stock sequence. Use the <a href="/atlas/maps/order-to-cash-map/">SAP order-to-cash process map</a> as a tracing method, then adapt the checkpoints to the approved process design.</p>

    <h2>Official references</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6aa7c6535e601e4be10000000a174cb4.html">SAP: displaying a sales document flow</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c7894a248ca14f74aca67f97528e5ad7/c81fbf53f106b44ce10000000a174cb4.html">SAP: outbound delivery creation</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/4c74c957b7018809e10000000a4450e5.html">SAP: sales billing</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/43e92f5581788a05e10000000a441470.html">SAP: order-to-cash performance</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-atp-is-not-inventory/">SAP ATP Is Not Inventory</a></li>
      <li><a href="/atlas/maps/order-to-cash-map/">Order to Cash Map</a></li>
      <li><a href="/atlas/concepts/sap-stock-exists-not-promisable/">SAP Stock Exists but Is Not Promisable</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
      <li><a href="/atlas/diagnostics/sap-delivery-processing-diagnostics/">SAP Delivery Processing Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
