---
layout: default
title: "SAP MM Procurement Overview"
description: "A practical explanation of SAP MM procurement from purchase requisition to purchase order, receipt, supplier invoice, and the handoff to Finance."
permalink: /atlas/sap/sap-mm-procurement-overview/
atlas_section: sap
domain: SAP operations
subdomain: Procurement and logistics
concept_type: SAP concept
sap_area: MM procurement
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - diagnostics
related:
  - /atlas/maps/procure-to-pay-map/
  - /atlas/sap/sap-mm-sourcing-overview/
  - /atlas/sap/gr-ir-clearing-explained/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP MM Procurement Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP MM procurement overview</h1>
    <p class="note-subtitle">How a requirement becomes a supplier order, a receipt, and an invoice in SAP S/4HANA.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM procurement</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until procurement claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>The procurement chain</h2>
    <p>The easiest way to understand SAP MM procurement is as a chain of documents with different responsibilities. A <strong>purchase requisition</strong> expresses an internal need. A <strong>purchase order</strong> turns that need into a purchasing document for a supplier. A <strong>goods receipt</strong> or <strong>service entry sheet</strong> records what the business actually received. A <strong>supplier invoice</strong> records what the supplier wants to be paid for.</p>

    <p>These documents are connected, but they are not mandatory in exactly the same combination for every scenario. A purchase order can be created without a preceding requisition. Services use a different receipt model from stock materials. Some processes require a goods receipt before invoice verification; others do not. The process design depends on what is being procured and how the organization wants to control it.</p>

    <h2>Purchase requisition: describe the need</h2>
    <p>A purchase requisition is an internal request for a material or service. It can be created manually, by planning, or by another business process. It may already contain a source of supply, or sourcing may happen later. The requisition can represent stock procurement or direct consumption, and it can use a material master or a descriptive item depending on the scenario.</p>

    <p>What matters is that the requisition provides enough context for purchasing: quantity, required date, plant or receiving context, purchasing responsibility, and account assignment when the cost should go directly to a cost object. Approval can also be part of the process when workflow is configured.</p>

    <h2>Purchase order: turn the requirement into a supplier commitment</h2>
    <p>The purchase order contains the commercial and logistical agreement with the supplier: what is ordered, how much, for which price, when it should arrive, and how the item will be processed. A requisition can be converted into a purchase order manually or, in suitable scenarios, automatically after the necessary source information is available.</p>

    <p>This is where sourcing data becomes visible. Supplier, purchasing organization, plant, purchasing info record, source list, contract, scheduling agreement, and other master data can all influence the result. The purchase order also carries item-category and account-assignment information that shapes the follow-on process.</p>

    <h2>Receipt: record what actually happened</h2>
    <p>For materials, the goods receipt records the delivered quantity with reference to the purchase order. Depending on the item and configuration, it can update stock, consumption, accounting, batch or valuation data, and the purchasing history. Warehouse and quality processes can add further steps without changing the basic idea: the receipt is evidence that fulfillment has moved from promise to execution.</p>

    <p>For services, we usually think in terms of a service entry and acceptance rather than a physical stock receipt. Keeping that distinction clear prevents the common mistake of describing every procurement process as “PO → MIGO → invoice.”</p>

    <h2>Invoice verification: compare the supplier claim with the purchasing history</h2>
    <p>When the supplier invoice arrives, SAP can reference the purchase order and the relevant receipt history. The system checks values such as quantity, price, and configured tolerances. Differences may be accepted, rejected by validation, or lead to a payment block depending on the scenario and configuration.</p>

    <p>The invoice is also where MM and Finance meet most visibly. In a standard goods-receipt process, the GR/IR account bridges the timing difference between receipt and invoice. When the invoice is posted, the supplier liability belongs to Financial Accounting. The later payment is an Accounts Payable process rather than another MM document.</p>

    <h2>Why the same symptom can have different causes</h2>
    <p>A procurement problem often appears one step later than its cause. A purchase order may fail because the source data is incomplete. A goods receipt may be impossible because the PO item is not intended for that receipt behavior. An invoice may be blocked because the purchase order price, receipt quantity, or tolerance logic does not support what the supplier billed.</p>

    <p>We therefore read the purchasing history in sequence. Which document exists? Which follow-on document is expected? What quantity and value moved at each step? This usually gives a clearer explanation than starting from a long list of transactions or configuration tables.</p>

    <h2>One example</h2>
    <p>A plant needs 100 units of a stock material. MRP creates a purchase requisition. Purchasing assigns a valid source and converts the requisition into a purchase order. The supplier delivers 60 units first, so SAP records a partial goods receipt. The invoice arrives for those 60 units and is posted against the purchase order and receipt history. The remaining 40 units stay open for later delivery. The same PO therefore carries both the commercial commitment and the history of how that commitment was fulfilled.</p>

    <h2>Where to go deeper</h2>
    <p>This overview deliberately stops before detailed configuration. Source determination, quota arrangements, movement types, invoice tolerances, GR/IR, stock transport, subcontracting, consignment, and service procurement each deserve their own explanation.</p>

    <h2>Sources</h2>
    <ul>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-and-procurement/outlining-a-general-procurement-process_dfbc33f8-72f1-4d30-a4cd-bd63d48d7a70">Outlining a General Procurement Process</a>.</li>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/exploring-operational-procurement-in-sap-s-4hana/outlining-purchase-order-processing-in-sap-s-4hana">Outlining Purchase Order Processing in SAP S/4HANA</a>.</li>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-and-procurement/creating-a-purchase-requisition-via-self-service-process_f60912b7-a44b-4344-85d1-ccb9a8e73365">Creating a Purchase Requisition via Self-Service Process</a>.</li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
      <li><a href="/atlas/sap/sap-mm-sourcing-overview/">SAP MM Sourcing Overview</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">SAP GR/IR Clearing Explained</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
