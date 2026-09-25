---
layout: default
title: "SAP EWM Integration Overview"
description: "How SAP Extended Warehouse Management exchanges delivery and execution data with SAP S/4HANA, and how to reason about broken handoffs."
permalink: /atlas/sap/sap-ewm-integration-overview/
atlas_section: sap
domain: SAP operations
subdomain: Warehouse integration
concept_type: SAP concept
sap_area: MM / EWM / logistics
business_process: Inventory management
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - integration
  - ewm
  - logistics
  - warehouse
related:
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/concepts/sap-stock-exists-not-promisable/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP EWM Integration Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP EWM integration overview</h1>
    <p class="note-subtitle">Follow the delivery handoff into EWM, the warehouse execution inside it, and the confirmation back.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM / EWM / logistics</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>An SAP EWM integration problem is easier to diagnose when we separate three states: the <strong>enterprise document</strong>, the <strong>EWM warehouse document</strong>, and the <strong>physical execution result</strong>. A delivery can be correct in SAP S/4HANA and still fail before EWM creates executable warehouse work. Conversely, warehouse work can finish while a follow-on confirmation has not yet updated the enterprise document.</p>

    <h2>The delivery is the main business handoff</h2>
    <p>For inbound and outbound delivery processes, current SAP documentation describes the S/4HANA–EWM interface around deliveries. On the EWM side, inbound processing uses inbound deliveries; outbound processing uses outbound delivery orders and outbound deliveries. EWM reports relevant changes and confirmations back so that SAP S/4HANA can continue with goods receipt, goods issue, billing, or other follow-on steps.</p>

    <p>This is more precise than saying that EWM simply receives purchase orders or sales orders. Those documents can initiate the business process, but the warehouse execution boundary is normally expressed through the appropriate delivery or warehouse request.</p>

    <h2>One outbound example</h2>
    <p>Suppose a sales process produces an outbound delivery for an EWM-managed location. The delivery-relevant data reaches EWM, where an <strong>outbound delivery order</strong> is generated as a warehouse request. EWM enriches that request with warehouse-processing data, such as warehouse process type and, where configured, wave assignment.</p>

    <p>Warehouse tasks then describe the concrete work. Warehouse orders group suitable tasks into work packages for execution. After picking, packing, staging, loading, and goods issue steps occur as required by the process, EWM sends the relevant delivery confirmations back to SAP S/4HANA.</p>

    <p>The important diagnostic question is therefore not just “Did the delivery reach EWM?” It is “How far did this document chain progress?” A delivery visible in EWM proves the handoff happened; it does not prove that task creation or warehouse execution succeeded.</p>

    <h2>Embedded and decentralized integration are not the same boundary</h2>
    <p>With <strong>embedded EWM</strong>, EWM and the enterprise processes run in the same SAP S/4HANA system. With <strong>decentralized EWM based on SAP S/4HANA</strong>, the warehouse system is separate and integrates with a remote enterprise-management system.</p>

    <p>For the decentralized system boundary, SAP documents asynchronous delivery communication using queued Remote Function Call (qRFC). Serialization matters because later messages can depend on earlier document state. This is why a queue problem can leave a perfectly valid business document waiting outside the warehouse process.</p>

    <p>That technical point should not be copied mechanically into an embedded scenario. Embedded EWM removes the remote-system handoff, although the logical separation between delivery processing and warehouse execution remains.</p>

    <h2>Stock differences need a document history, not a slogan</h2>
    <p>It is tempting to say that one system “owns” stock and the other does not. That is too crude, especially when embedded and decentralized deployments are considered together. EWM represents stock with warehouse-level detail such as bins, handling units, stock attributes, and process status, while enterprise inventory processes maintain their own relevant inventory and accounting state.</p>

    <p>When quantities appear inconsistent, first identify the business event that should have aligned the states. Was goods receipt confirmed? Was goods issue posted? Was a reversal sent? Is the discrepancy in total quantity, warehouse location, stock type, or document status? The answer determines whether the problem is warehouse execution, goods-movement follow-up, or communication.</p>

    <h2>A practical fault-isolation sequence</h2>
    <p>Start with the business document and move forward, rather than opening every technical monitor at once.</p>
    <ol>
      <li>Confirm the relevant inbound or outbound delivery and the EWM-managed warehouse context.</li>
      <li>Check whether the corresponding EWM delivery or warehouse request exists.</li>
      <li>Check whether warehouse tasks were created. If not, inspect warehouse-process and stock-determination evidence around that request.</li>
      <li>If tasks exist, determine whether execution stopped before confirmation, at a handling-unit or resource step, or at the goods-movement boundary.</li>
      <li>For decentralized EWM, inspect the relevant outbound and inbound qRFC state when the document or confirmation is missing across systems.</li>
      <li>Compare document status and quantities after the final successful step; do not infer the failing layer from the final stock number alone.</li>
    </ol>

    <p>This sequence also prevents a common support mistake: repeatedly reprocessing an integration message before understanding whether the target document already exists or whether a later step is the real blocker.</p>

    <h2>Where TM changes the picture</h2>
    <p>Transportation Management can integrate with EWM through several patterns. Current SAP documentation includes freight-order-based integration and delivery/EWM-transportation-unit-based integration. In these scenarios, warehouse readiness, loading, and transport execution can influence each other. The exact document chain must therefore be identified before assuming that a warehouse delivery alone controls the process.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9832125c23154a179bfa1784cdc9577a/65cecb53ad377114e10000000a174cb4.html">Communication from EWM to SAP S/4HANA</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9832125c23154a179bfa1784cdc9577a/4faf5b22635e42f5e10000000a421937.html">Generation of Warehouse Request of Outbound Delivery Order Type</a>, SAP S/4HANA 2025 FPS01.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/s4hana-best-practices/administration-guide-to-implementation-of-sap-s-4hana-cloud-private-edition-2023-with-sap-best-practices/defining-scope-of-business-scenario-for-integrating-sap-s-4hana-with-decentralized-extended-warehouse-management-ewm-based-on-sap-s-4hana">Decentralized EWM deployment scope</a>, SAP Best Practices administration guidance.</li>
      <li>SAP Help Portal, <a href="https://help.sap.com/docs/sap_s4hana_on-premise/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/bd1fbe54f20dc40ae10000000a441470.html">Integration with Extended Warehouse Management</a>, Transportation Management, SAP S/4HANA 2025 FPS01.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page explains the integration boundary and a durable diagnostic model. It does not prescribe warehouse configuration, queue repair steps, or transaction codes for every deployment. Those details must be verified for the actual SAP S/4HANA and EWM release and architecture.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/concepts/sap-stock-exists-not-promisable/">SAP Stock Exists but Is Not Promisable</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
