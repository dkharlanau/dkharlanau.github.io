---
layout: default
title: "SAP Movement Types and Inventory"
description: "How SAP movement types express the business purpose of a goods movement and control quantity, valuation, account updates, and follow-on behavior."
permalink: /atlas/sap/sap-movement-types-inventory/
atlas_section: sap
domain: SAP operations
subdomain: Inventory management
concept_type: SAP concept
sap_area: MM inventory management / WM
business_process: Procure to pay / Inventory management
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - inventory
  - movement-types
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
  - /atlas/maps/procure-to-pay-map/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Movement Types and Inventory</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP movement types and inventory</h1>
    <p class="note-subtitle">A movement type does more than label a receipt or issue. It tells Inventory Management what kind of business event is being posted.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay / Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM inventory management</dd></div>
      <div><dt>Reviewed</dt><dd>2026-09-22</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>The movement type gives a goods movement its meaning</h2>
    <p>In SAP Inventory Management, a movement type is a three-digit key that describes the business purpose of a goods movement. A quantity of 10 pieces is not enough information by itself. SAP also needs to know whether those 10 pieces are being received from a supplier, issued to a cost object, transferred between locations, released from another stock type, or used to reverse an earlier posting.</p>

    <p>That business meaning drives system behavior. SAP documentation describes movement types as control keys for quantity updates, stock and material valuation, consumption accounts, field selection, and in some cases the creation of follow-on business objects or accounting documents. This is why changing a movement type can change much more than the sign of a stock quantity.</p>

    <h2>A few examples are more useful than memorizing a long list</h2>
    <p><strong>101</strong> is the familiar goods receipt for a purchase order. Its reversal is normally <strong>102</strong>. Together they illustrate an important pattern: reversals are separate business postings that undo the effect of an earlier movement rather than deleting history.</p>

    <p><strong>103</strong> and <strong>105</strong> show a different idea. The first step records a receipt into GR blocked stock; the second releases that quantity into the next stock state. The accounting and valuation effect depends on the process and configuration, so it is safer to understand the two-step business purpose than to treat every movement number as a fixed journal-entry recipe.</p>

    <p><strong>261</strong> is used for a goods issue to an order, with <strong>262</strong> as the corresponding reversal. The posting reduces inventory and charges the relevant order or consumption context according to account determination. It should not be described simply as “posting to work in process,” because the financial result depends on the order and valuation setup.</p>

    <p>Transfer movements provide another family of examples. A one-step transfer can remove stock from one organizational unit and place it into another in the same posting. A two-step transfer separates those events and makes the quantity visible in an intermediate transfer stock until the receiving step is posted.</p>

    <h2>Movement type and account determination are related, but not identical</h2>
    <p>The movement type helps SAP determine how the goods movement should affect accounting, but it is not the only input. Valuation class, valuation area, transaction/event logic, account modifiers, special stock, and other configuration can influence the final G/L account. When a goods movement fails with an account-determination error, we therefore trace the complete combination instead of assuming that the movement type alone points to one account.</p>

    <p>The same principle applies to stock quantity. A movement type can move quantity between unrestricted-use, blocked, quality inspection, transfer, or other stock categories depending on the scenario. Reading only the total stock before and after posting can hide what actually changed.</p>

    <h2>Use the document context, not just the number</h2>
    <p>A movement type is easiest to understand together with its reference document. A 101 with a purchase order tells a procurement story. A 261 with an order tells a consumption story. A transfer movement tells us which organizational units are giving and receiving stock. In many business process chains, SAP copies or proposes the movement type from the preceding document, so the surrounding process matters as much as the code itself.</p>

    <p>For analysis, we normally reconstruct three things: the business event that should have happened, the movement that SAP actually posted, and the stock or accounting state that resulted. If those three agree, the movement is probably correct. If they do not, changing stock directly only hides the original problem.</p>

    <h2>Sources</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/1663bd534f22b44ce10000000a174cb4.html">SAP Help: The Movement Type Concept</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/9e64bd534f22b44ce10000000a174cb4.html">SAP Help: Transfer Postings and Stock Transfers — Overview</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
