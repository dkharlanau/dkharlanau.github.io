---
layout: default
title: "SAP TM Integration Overview"
description: "How SAP Transportation Management connects orders, deliveries, freight planning, EWM execution, and freight settlement in SAP S/4HANA."
permalink: /atlas/sap/sap-tm-integration-overview/
atlas_section: sap
domain: SAP operations
subdomain: Transportation integration
concept_type: SAP concept
sap_area: MM / TM / logistics
business_process: Logistics execution
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - integration
  - tm
  - transportation
  - logistics
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP TM Integration Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP TM integration overview</h1>
    <p class="note-subtitle">Trace transportation demand from the source document through freight planning, warehouse execution, and settlement.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Logistics execution</dd></div>
      <div><dt>SAP area</dt><dd>MM / TM / logistics</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP TM integration is not one fixed “delivery to freight order” interface. Transportation can start from an order or from a delivery, and the downstream execution pattern changes depending on whether TM works with EWM, Inventory Management, an external warehouse, carriers, or settlement processes.</p>

    <p>The most useful diagnostic model is to follow the document chain and ask which layer first stopped agreeing with the previous one.</p>

    <h2>Planning may begin before the delivery</h2>
    <p>Current SAP S/4HANA documentation supports both <strong>order-based</strong> and <strong>delivery-based</strong> transportation planning. Sales orders, purchase orders, stock transport orders, and other supported source documents can create transportation demand before a delivery exists. TM builds freight units from that demand and can plan them onto freight orders or bookings.</p>

    <p>For relevant order-based scenarios, TM can also create delivery proposals and trigger delivery creation in Logistics Execution. This reverses a common mental model: the delivery does not always initiate transportation. Sometimes the transportation plan helps determine when and how the delivery should be created.</p>

    <p>Later, when a delivery is created, a delivery-based transportation requirement can replace or consume the earlier order-based demand. A support analysis therefore has to know whether it is looking at the order stage, delivery stage, or the transition between them.</p>

    <h2>The freight unit is the bridge into planning</h2>
    <p>A freight unit represents transportation demand. If the source order or delivery is correct but the expected freight unit does not exist, the problem is at the TM relevance or demand-creation boundary. If the freight unit exists but is not assigned to a freight document, the problem has moved into planning.</p>

    <p>Once assigned to a freight order, the issue becomes more concrete: routes, dates, capacity, resources, carrier assignment, and execution status can be evaluated against that freight document. This is a different class of problem from source-document integration.</p>

    <h2>EWM integration has more than one pattern</h2>
    <p>SAP documents several TM–EWM integration options. In <strong>freight-order-based integration</strong>, including Advanced Shipping and Receiving scenarios, TM freight orders can directly coordinate shipping and receiving activities with EWM. SAP also supports integration based on deliveries and EWM transportation units, including cases where EWM is embedded or runs as an external decentralized system.</p>

    <p>These patterns have different document and status handoffs. In one process, TM planning may release warehouse work; in another, EWM can begin warehouse execution from the delivery and later update TM with packaging or execution information. That is why generic advice such as “check whether the shipment reached EWM” is often too vague.</p>

    <p>A useful incident description names the integration pattern and the objects involved: source order or delivery, freight unit, freight order, EWM delivery or transportation unit, and the last status that changed successfully.</p>

    <h2>Execution feedback closes the logistics loop</h2>
    <p>TM needs execution information because the transportation plan is not complete when a freight order is created. Warehouse loading, departure, arrival, carrier events, and other execution signals can update transportation status and dates. In integrated TM–EWM processes, warehouse events can therefore change the transport document after planning is finished.</p>

    <p>This also means that an apparently “stuck freight order” can be waiting on an EWM execution state rather than a TM planning error. The source of truth for the missing event must be identified before re-planning or changing master data.</p>

    <h2>Settlement is a separate integration boundary</h2>
    <p>After transportation execution, TM can calculate and settle freight charges. The <strong>freight settlement document</strong> is the TM settlement object for shipper-side freight cost processing. Current SAP S/4HANA documentation describes posting FSDs to Materials Management for further financial processing and invoice verification.</p>

    <p>An FSD is therefore not simply “the carrier invoice.” Carrier invoice submission, TM charge expectations, and MM/FI follow-on processing are related but distinct steps. A charge mismatch can arise before settlement; an FSD can also be correct in TM while the follow-on posting fails in another component.</p>

    <h2>How to isolate the failing boundary</h2>
    <ol>
      <li><strong>Source:</strong> identify the sales, purchasing, stock-transfer, or delivery document that created the transportation demand.</li>
      <li><strong>Demand:</strong> confirm that the expected transportation requirement and freight unit exist with the right quantity, locations, and dates.</li>
      <li><strong>Plan:</strong> confirm the freight unit is assigned to the expected freight order or booking and inspect planning constraints only after the demand itself is correct.</li>
      <li><strong>Execution:</strong> identify whether the next expected event belongs to TM, EWM, Inventory Management, or an external carrier.</li>
      <li><strong>Settlement:</strong> distinguish a TM charge-calculation issue from FSD creation and from the later MM/FI invoice-verification path.</li>
    </ol>

    <p>This sequence replaces the previous assumption that every TM problem can be reduced to a delivery transfer, a planning job, or one transaction code. It follows the actual business objects instead.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/04474a8485384e3fbfcb346d943b3217.html">Internal TM Component Integration</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/36f56df518d34f95b56582784dc6b056.html">Creation of Delivery Proposals</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/sap_s4hana_on-premise/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/bd1fbe54f20dc40ae10000000a441470.html">Integration with Extended Warehouse Management</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/15501287309340b0a189820da173943c.html">Collective Settlement</a>, SAP S/4HANA 2025 FPS01.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page explains the integration model, not every TM planning profile, charge configuration, carrier interface, or EWM execution variant. Exact object flow depends on the business scenario and release, so implementation-specific behavior must be verified in the target landscape.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-tm/">SAP TM</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
