---
layout: default
title: "SAP Stock Transfer and In-Transit Inventory"
description: "How one-step transfers, two-step transfers, and stock transport orders represent stock moving between SAP organizational units."
permalink: /atlas/sap/sap-stock-transfer-in-transit/
atlas_section: sap
domain: SAP operations
subdomain: Logistics and inventory
concept_type: SAP concept
sap_area: MM / logistics execution
business_process: Inventory management
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - inventory
  - logistics
  - stock-transfer
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/maps/procure-to-pay-map/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Stock Transfer and In-Transit Inventory</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP stock transfer and in-transit inventory</h1>
    <p class="note-subtitle">The key question is not only where stock moved, but which transfer process SAP used to represent the journey.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM / logistics execution</dd></div>
      <div><dt>Reviewed</dt><dd>2026-09-22</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>There is more than one way to move stock</h2>
    <p>When material moves between storage locations or plants, SAP can represent the movement in different ways. The three broad procedures are a one-step transfer posting, a two-step transfer posting, and a transfer using a stock transport order. They can describe similar physical movement, but they leave different document trails and give the business different visibility while the goods are travelling.</p>

    <p>This distinction matters because “stock is missing after transfer” is often not an inventory-loss problem. The quantity may simply be sitting in an intermediate stock category created by the chosen process.</p>

    <h2>One step means one posting event</h2>
    <p>In a one-step transfer posting, SAP records the removal from the issuing unit and the receipt into the receiving unit together. For a plant-to-plant transfer, the system creates the issuing and receiving material-document items as part of one posting. There is no separate period in which the receiving team still needs to confirm the arrival.</p>

    <p>This is efficient when the physical and system movements can be treated as one event. It is less suitable when the journey itself matters—for example, when plants are far apart or different people control goods issue and goods receipt.</p>

    <h2>Two steps make the journey visible</h2>
    <p>A two-step transfer separates removal and placement into storage. After the first posting, SAP manages the quantity as <strong>stock in transfer</strong> at the receiving plant. It is not yet unrestricted-use stock there. The second posting moves that quantity out of stock in transfer and into the receiving stock.</p>

    <p>That intermediate state is useful operationally because it answers a real question: how much material has left one plant but has not yet been received by the other? It also explains why storage-location stock alone can give an incomplete picture during reconciliation.</p>

    <h2>A stock transport order adds a purchasing document to the flow</h2>
    <p>A stock transport order, or STO, gives the transfer a purchasing-document backbone. It can support planning, delivery processing, goods issue, goods receipt, and—depending on the scenario—additional logistics or intercompany processing. After goods issue, SAP can manage the quantity as stock in transit until the receiving side posts the receipt.</p>

    <p>It is useful to keep the terms separate. SAP documentation uses <strong>stock in transfer</strong> for the intermediate quantity in a two-step transfer posting, while STO processes commonly use <strong>stock in transit</strong>. The business meaning is similar—goods have left the source but are not yet available at the destination—but the document flow is different.</p>

    <h2>Valuation follows the process as well</h2>
    <p>A plant-to-plant transfer can have accounting effects, especially when valuation prices differ between plants or company codes. SAP documentation for transfer postings describes the transfer value as being based on the issuing plant and explains that price differences may arise at the receiving plant depending on price control. This is one reason not to reduce stock transfers to “subtract here, add there.” Quantity and value move under the rules of the chosen scenario.</p>

    <h2>How we read a transfer that looks incomplete</h2>
    <p>We first identify the process: direct one-step, direct two-step, or STO. Then we follow the related goods movements in sequence. In a two-step transfer, the open question is whether the receiving step was posted. In an STO flow, we look at the order and its goods-issue and goods-receipt history. That approach is more reliable than starting from one stock report and assuming anything absent from unrestricted stock has disappeared.</p>

    <p>The useful end state is a simple explanation: the material is still in transfer, still in transit against an STO, already received, or reversed. Once that state is known, the correction usually follows the document flow naturally.</p>

    <h2>Sources</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/9e64bd534f22b44ce10000000a174cb4.html">SAP Help: Transfer Postings and Stock Transfers — Overview</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/bf64bd534f22b44ce10000000a174cb4.html">SAP Help: Two-Step Procedure — Plant</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/af9ef57f504840d2b81be8667206d485/a35eb6531de6b64ce10000000a174cb4.html">SAP Help: Transfer Posting — From Plant to Plant</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure to Pay Map</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
