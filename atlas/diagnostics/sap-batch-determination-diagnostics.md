---
layout: default
title: "SAP Batch Determination Diagnostics"
description: "Diagnose SAP batch determination by separating the business trigger, search strategy, selection criteria, availability, sort sequence, and quantity proposal."
permalink: /atlas/diagnostics/sap-batch-determination-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Inventory and batch management
concept_type: diagnostic guide
sap_area: "MM / SD / WM batch management"
business_process: Inventory management
status: needs_verification
verified: false
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
author: Dzmitryi Kharlanau
level: 1
robots: noindex,follow
sitemap: false
tags:
  - batch-management
  - sap-mm
  - sap-sd
  - sap-wm
  - diagnostics
  - inventory
related:
  - /atlas/diagnostics/sap-movement-types-diagnostics/
  - /atlas/diagnostics/sap-stock-transfer-diagnostics/
  - /atlas/diagnostics/sap-material-document-diagnostics/
  - /atlas/diagnostics/sap-physical-inventory-diagnostics/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Batch Determination Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP batch determination diagnostics</h1>
    <p class="note-subtitle">Treat batch determination as a pipeline: find the search strategy, prove which batches qualify, then inspect availability, sorting, and quantity proposal.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Inventory management</dd></div>
      <div><dt>SAP area</dt><dd>MM / SD / WM batch management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until reviewed against the target SAP landscape.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>“No batch found” sounds like a stock problem, but stock is only one stage of batch determination. SAP first has to find the relevant search strategy for the business transaction. That strategy defines how batches are selected, how the result is sorted, and, where batch split is allowed, how quantities are proposed.</p>

    <p>A useful diagnosis therefore follows the same order as the determination process. Start from the exact document and step that requested a batch. Then ask whether SAP found the intended strategy, whether the expected batch satisfied its selection criteria, whether usable quantity remained available, and whether the sort and quantity rules produced the expected result.</p>

    <aside class="callout">
      <strong>Working rule:</strong> do not start by changing classification or creating a broader strategy. First identify the strategy SAP actually used and the first stage where the expected batch dropped out.
    </aside>

    <h2>The process has five different decisions</h2>
    <ol>
      <li><strong>Trigger and search procedure.</strong> The business transaction must call batch determination with a search procedure that is relevant for that context.</li>
      <li><strong>Search strategy.</strong> SAP evaluates the strategy types in the procedure and adopts the first valid search strategy.</li>
      <li><strong>Batch selection.</strong> The selection class and characteristic values define which batches meet the required specification.</li>
      <li><strong>Availability and ordering.</strong> SAP checks whether the selected batches are available, then applies the configured sort sequence.</li>
      <li><strong>Quantity proposal.</strong> If the process allows several batches, quantity-proposal and batch-split rules determine how the required quantity is distributed.</li>
    </ol>

    <p>SAP documents this sequence explicitly for current S/4HANA batch determination. It is useful because each symptom points to a different layer. A missing strategy is not repaired by changing batch characteristics; a correct candidate list in the wrong order is not a stock problem.</p>

    <h2>Start from the application that requested the batch</h2>
    <p>Batch determination is used in several logistics processes, but the trigger is not universal. Inventory Management can determine batches for goods issues, stock transfers, and transfer postings. Production can determine component batches. Sales and Distribution can determine batches during sales processing or delivery processing. Classic Warehouse Management can also perform its own batch determination.</p>

    <p>This matters when someone says, “It works in the sales order but not in the delivery,” or “The same material works for one movement but not another.” Those are different business transactions and can therefore reach different search procedures or strategy keys. Compare the failing case with a working case from the same application and process step before comparing configuration across applications.</p>

    <p>SAP EWM is another boundary. In integrated scenarios, batch determination can be performed directly in EWM instead of in SAP S/4HANA; S/4HANA can then pass batch selection characteristics to the warehouse. If EWM owns the determination step, an S/4HANA search-strategy investigation alone is incomplete.</p>

    <h2>If no strategy is found, inspect the condition path</h2>
    <p>Batch search strategy uses the condition technique. The design includes condition tables, access sequences, strategy types, search procedures, and the assignment of a search procedure to the relevant business transaction. A strategy record is then maintained for a key combination supported by the strategy type.</p>

    <p>So when no strategy is selected, inspect the values SAP used for that call: for example, movement type and plant in an Inventory Management scenario, or customer/material/plant where the configured strategy type uses those fields. Do not assume the material itself owns one universal “batch search procedure.”</p>

    <p>Where an online determination screen is available, strategy information is especially valuable: it shows which strategy matched and the values behind that match. A working comparison case can quickly reveal whether the difference is a plant, customer, movement, document context, or another key field.</p>

    <h2>If the strategy is correct, follow candidate selection</h2>
    <p>The selection class tells SAP which batch characteristics matter for this search. The expected batch must have values compatible with those criteria. A characteristic can exist on the batch and still be irrelevant if it is not part of the selection logic used by the strategy.</p>

    <p>Shelf life is a good example. An expiration date does not automatically mean that every expired or near-expiry batch is always excluded by one global rule. Current SAP batch determination supports dynamic remaining-shelf-life criteria through standard characteristics, and expiration-related values can also participate in batch classification and sorting. The result therefore depends on the configured selection and check logic for the process.</p>

    <p>For a missing candidate, compare the expected batch with one batch that does appear. Check the actual classification values and the selection criteria side by side. This is more reliable than opening the batch master and asking whether its data “looks correct.”</p>

    <h2>Keep batch status separate from stock category</h2>
    <p>Two controls are often mixed together during support: <strong>batch status</strong> and <strong>stock type</strong>. When batch status management is active, a batch can carry an unrestricted or restricted status. SAP also manages stock in categories such as quality inspection or blocked stock. These are related operationally, but they are not the same field or the same decision.</p>

    <p>That distinction matters when stock visibly exists but is not usable for the current requirement. Confirm where the quantity sits, which stock category the process can consume, and whether batch status management is active. Avoid summarizing all of these cases as “the batch is blocked.”</p>

    <h2>If the right batches appear in the wrong order, inspect the sort sequence</h2>
    <p>A sort rule orders the batches that survived selection and availability checks. SAP allows the sequence to use batch characteristics and selected standard characteristics. The business rule should therefore be expressed through the actual sort sequence, not through an assumption such as “SAP always uses FIFO.”</p>

    <p>If the business expects the earliest-expiring batch first, prove which expiration-related characteristic is used and whether the direction is correct. If it expects the largest usable quantity first, prove that rule instead. The diagnosis is complete only when the observed order can be explained by the active sort definition.</p>

    <h2>Correct batches with wrong quantities point to another layer</h2>
    <p>Finding the correct batches does not guarantee the expected split. Search strategies can control the number of batch splits and the quantity proposal used to distribute the requirement across the ordered candidate list. A delivery can also use batch split to cover one item with several batches.</p>

    <p>When the selected batch numbers look right but quantities do not, stop changing selection criteria. Inspect the quantity proposal, allowed split behaviour, the available quantity of each candidate, and the application-specific document rules.</p>

    <h2>A practical incident path</h2>
    <ol>
      <li><strong>Capture the exact business step.</strong> Record the document, item, material, plant/storage context, required quantity, and expected batch behaviour.</li>
      <li><strong>Confirm where determination runs.</strong> Inventory Management, production, sales order, delivery, classic WM, or EWM can represent different control points.</li>
      <li><strong>Identify the active search strategy.</strong> Check the search procedure, strategy type, matched key combination, and strategy record used by the failing call.</li>
      <li><strong>Inspect selection criteria.</strong> Compare the expected batch’s classification and dynamic criteria with a batch that SAP accepted.</li>
      <li><strong>Check usable stock.</strong> Confirm quantity, plant/storage context, stock category, batch status, and reservations or other requirements that affect availability.</li>
      <li><strong>Inspect sort and split only after the candidate list is correct.</strong> These controls cannot restore a batch that selection or availability already removed.</li>
      <li><strong>Retest the original process.</strong> A manual batch entry can prove that a batch exists, but it does not prove that automatic determination is configured correctly.</li>
    </ol>

    <p>This sequence also makes support notes more useful. Instead of “batch determination is wrong,” the ticket can state something testable: the expected search strategy was not found, batch X failed selection characteristic Y, batch X was selected but unavailable, or the candidate list was correct and the sort sequence produced the disputed order.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/49d0972a760b4646918ce9fddb034d64/0dfeb753128eb44ce10000000a174cb4.html">Batch Determination</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/4eb099dbc8a6435c9b36a854a7e05522/16feb753128eb44ce10000000a174cb4.html">Definition of a Batch Search Strategy</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/4eb099dbc8a6435c9b36a854a7e05522/9d6c49f60a1840959a70a852f5db168f.html">Definition of a Batch Sort Sequence</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/fc62bd534f22b44ce10000000a174cb4.html">Stocks in the Material Master Record</a>.</li>
      <li>SAP S/4HANA 2025 FPS01 — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2d95c3180a974e0aad07556ee4d28e94/78f6ef525c1b287ee10000000a44176d.html">Batch Determination When Using SAP EWM</a>.</li>
    </ul>

    <h2>Boundaries</h2>
    <p>This page explains the diagnostic logic around batch determination. It does not attempt to reproduce application-specific Customizing, EWM stock-removal strategy, quality-management release logic, or the full batch-management data model. Those details should be checked in the documentation and configuration for the target release and process.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-movement-types-diagnostics/">SAP Movement Types Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-stock-transfer-diagnostics/">SAP Stock Transfer Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-material-document-diagnostics/">SAP Material Document Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-physical-inventory-diagnostics/">SAP Physical Inventory Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
