---
layout: default
title: "SAP TM"
description: "SAP Transportation Management explained through transportation requirements, freight units, freight orders, execution, charges, and settlement."
permalink: /atlas/sap/sap-tm/
atlas_section: sap
domain: SAP operations
subdomain: Transportation management
concept_type: product
sap_area: "TM"
business_process: "Transportation planning and execution"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-tm
  - transportation
  - logistics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/supply-chain-domain/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-ewm/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP TM</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP TM</h1>
    <p class="note-subtitle">Transportation Management turns demand for movement into planned, executable, and settleable freight.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Transportation planning and execution</dd></div>
      <div><dt>SAP area</dt><dd>TM</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Transportation Management (TM) manages the transportation layer between a business demand and the physical movement of goods. It can take transportation-relevant orders or deliveries, derive transportation demand, consolidate that demand, plan capacity, execute with carriers or internal resources, calculate charges, and support freight settlement.</p>

    <p>The simplest way to understand TM is to separate <strong>what needs to be moved</strong> from <strong>how it will be moved</strong>. The first side is transportation demand. The second side is transportation capacity and execution.</p>

    <h2>Transportation demand becomes freight units</h2>
    <p>Sales, purchasing, stock-transfer, delivery, and other supported logistics processes can create transportation requirements in TM. Depending on the scenario, planning can be <strong>order-based</strong> or <strong>delivery-based</strong>. That distinction matters because transportation planning does not always start after a delivery exists.</p>

    <p>TM uses <strong>freight units</strong> to represent transportable demand for planning. A freight unit carries the quantity to move together with relevant locations, dates, and other planning attributes. Freight-unit building determines how source demand is split or grouped into those planning units.</p>

    <p>This gives us an important boundary: a sales order, purchase order, stock transport order, or delivery expresses the business requirement; the freight unit expresses the transportation demand that TM can plan.</p>

    <h2>Freight orders describe execution capacity</h2>
    <p>Planning assigns freight units to capacity documents such as <strong>freight orders</strong> or, for relevant modes and scenarios, freight bookings. A freight order describes the planned transportation execution: stops, stages, dates, resources, carrier, and the cargo assigned to the movement.</p>

    <p>TM can plan manually or with optimization and can include carrier selection, tendering, routing, scheduling, and charge calculation where the scenario uses those capabilities. The resulting freight document is not merely a copied delivery. It is the transportation plan that can combine demand from several source documents.</p>

    <h2>Order-based and delivery-based planning solve different timing problems</h2>
    <p>With order-based planning, TM can plan transportation before the logistics delivery is created. SAP even supports delivery proposals from TM for relevant SD and MM orders. This is useful when transportation capacity or routing decisions need to influence delivery creation.</p>

    <p>With delivery-based planning, the delivery already exists and becomes the basis for the transportation requirement. Current SAP documentation also describes processes where a delivery-based transportation requirement consumes freight units that were previously created from an order-based requirement. In other words, the transport plan can evolve as the logistics document chain becomes more concrete.</p>

    <h2>Warehouse execution is connected, not absorbed</h2>
    <p>TM and EWM solve different parts of logistics. TM plans the movement between locations; EWM executes the work inside a warehouse. SAP S/4HANA supports several integration patterns between them, including freight-order-based Advanced Shipping and Receiving and delivery/EWM-transportation-unit-based integration.</p>

    <p>That separation explains why “the freight order is planned” does not mean “the truck can leave.” Picking, packing, staging, loading, warehouse readiness, and transport execution may still have to synchronize across TM and EWM.</p>

    <h2>Charges and settlement come after the transport plan</h2>
    <p>Charge calculation determines expected transportation charges from the freight context and the relevant agreements, rates, and calculation rules. After execution, TM can create <strong>freight settlement documents</strong> for the shipper-side settlement process.</p>

    <p>A freight settlement document should not be described as the carrier invoice itself. In current SAP S/4HANA documentation, an FSD can be posted to Materials Management for further financial processing and invoice verification. Carrier-submitted invoice data and the TM settlement expectation can then be compared in the relevant process.</p>

    <h2>Three different failures can look like “transportation is broken”</h2>
    <p>A missing freight unit is a demand-integration problem. An unplanned freight unit is a planning or capacity problem. A freight order with wrong charges is a calculation or commercial-master-data problem. A completed freight order whose settlement cannot continue is a settlement integration problem.</p>

    <p>Keeping those states separate is more useful than memorizing one long list of TM transactions. Start with the source document, locate the transportation requirement and freight unit, then follow the assigned freight document through execution and settlement.</p>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/sap-tm-integration-overview/">SAP TM Integration Overview</a></li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/04474a8485384e3fbfcb346d943b3217.html">Internal TM Component Integration</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/36f56df518d34f95b56582784dc6b056.html">Creation of Delivery Proposals</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/sap_s4hana_on-premise/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/bd1fbe54f20dc40ae10000000a441470.html">Integration with Extended Warehouse Management</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/15501287309340b0a189820da173943c.html">Collective Settlement</a>, SAP S/4HANA 2025 FPS01.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>TM document flow and available functions depend on the shipper or logistics-service-provider scenario, transportation mode, integration pattern, release, and activated scope. This page describes the durable conceptual model and current documented S/4HANA patterns, not a universal configuration recipe.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-tm-integration-overview/">SAP TM Integration Overview</a></li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
