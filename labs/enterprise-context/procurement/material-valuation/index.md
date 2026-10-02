---
layout: default
title: "Material Valuation in Procurement — Standard Price, Moving Average Price and FI Postings"
description: "A practical SAP S/4HANA MM guide to material and accounting documents, GR/IR, standard price, moving average price, price differences, stock coverage, and FI postings for goods receipt and invoice receipt."
permalink: /labs/enterprise-context/procurement/material-valuation/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-10-02
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-p2p
  - logistics-inventory
tags:
  - sap-s4hana
  - sap-mm
  - procurement
  - inventory-management
  - material-valuation
  - standard-price
  - moving-average-price
  - gr-ir
  - invoice-verification
  - fi-integration
source_links:
  - title: "Analyzing Material Valuation"
    url: "https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-procurement/analyzing-material-valuation"
  - title: "Invoices for Purchase Orders"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/be5eb6531de6b64ce10000000a174cb4.html"
  - title: "Example: Material with MAP"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/8860b6531de6b64ce10000000a174cb4.html"
  - title: "Example: Material with MAP Without Stock Coverage"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMI-SE/af9ef57f504840d2b81be8667206d485/6370b6531de6b64ce10000000a174cb4.html"
  - title: "Product Valuation"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/18fe3fab96864826bfa0be0de4f65b85/772bf4b02b4245d9912a2b04cd042643.html"
  - title: "WRX — GR/IR Clearing Account"
    url: "https://help.sap.com/docs/s4hana-best-practices/ycoa-1f2ae10b96f740759d66e695f953aa8f/wrx-gr-ir-clearing-account"
last_reviewed: 2026-10-02
publication_wave: "logistics-search-wave-01"
review_method: "Current SAP Learning S4500 material-valuation lesson + SAP S/4HANA 2025 FPS01 Help cross-check + editorial rewrite"
search_intent: "SAP MM material valuation standard price moving average price goods receipt invoice receipt GR IR FI postings"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-procurement"
ai_sidecar: "/ai/pages/labs--enterprise-context--procurement--material-valuation.json"
entity_mentions:
  - "sap-s4hana"
semantic_links:
  - type: "parent_context"
    title: "Procurement Process & Decision Map — Enterprise Context Lab"
    url: "/labs/enterprise-context/procurement/"
  - type: "integrates_with"
    title: "Inventory Management — Enterprise Context Lab"
    url: "/labs/enterprise-context/inventory-management/"
  - type: "integrates_with"
    title: "FI/CO for Logistics — Enterprise Context Lab"
    url: "/labs/enterprise-context/finance-logistics/"
  - type: "related_topic"
    title: "Tax Code Determination in Purchasing & Invoice Receipt — SAP S/4HANA MM"
    url: "/labs/enterprise-context/procurement/tax-code-determination/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/labs/">Labs</a></li>
    <li><a href="/labs/enterprise-context/">Enterprise Context</a></li>
    <li><a href="/labs/enterprise-context/procurement/">Procurement</a></li>
    <li aria-current="page">Material Valuation</li>
  </ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP MM / Goods Receipt → Invoice Verification → FI</p>
      <h1>The quantity changes in logistics.<br />The value change depends on price control.</h1>
      <p>Material valuation connects a physical event with an accounting result. The same purchase order can produce different FI postings depending on whether the material uses standard price or moving average price, whether the invoice differs from the PO, and whether enough stock still exists when the invoice is posted.</p>
      <a class="research-canvas__button" href="#mental-model">Build the model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <div>
      <p><strong>Assessment rule:</strong> separate the document event from the valuation rule.</p>
      <p><strong>Fast chain:</strong> PO sets the commercial reference → GR changes stock and may create FI → IR creates the supplier liability and resolves price differences → price control decides whether the difference stays in inventory or goes to a price-difference account.</p>
    </div>
    <a href="/labs/enterprise-context/procurement/">Back to Procurement <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="mental-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>Ask four questions in this order.</h2>
      <p>This prevents a common mistake: jumping directly to G/L account configuration before proving what business event and valuation method SAP is processing.</p>
    </header>

    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>01</span><strong>EVENT</strong><h3>What was posted?</h3><p>Goods receipt, invoice receipt, reversal, transfer posting, or another goods movement?</p></article>
      <article class="ecg-memory-card"><span>02</span><strong>DOCUMENT</strong><h3>Which document proves it?</h3><p>Material document for the movement, MM invoice document for invoice verification, and accounting document when FI is affected.</p></article>
      <article class="ecg-memory-card"><span>03</span><strong>PRICE</strong><h3>How is the material valuated?</h3><p>Standard price keeps inventory at a fixed planned value. Moving average price lets procurement differences change inventory value when the rules allow it.</p></article>
      <article class="ecg-memory-card"><span>04</span><strong>VARIANCE</strong><h3>Where does the difference go?</h3><p>Price-difference account for standard price; normally stock for moving average price when sufficient stock coverage exists.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="documents" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Document principle</p>
      <h2>Material document and accounting document answer different questions.</h2>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Material valuation document model">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Business event</th><th scope="col">Logistics document</th><th scope="col">Accounting document</th><th scope="col">What it proves</th></tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Goods movement</th>
            <td>Material document</td>
            <td>Created when the movement is valuation-relevant</td>
            <td>Quantity, material, movement type, plant, storage location, and the FI value effect when relevant.</td>
          </tr>
          <tr>
            <th scope="row">Supplier invoice</th>
            <td>MM invoice document</td>
            <td>Accounting document</td>
            <td>The supplier claim, GR/IR clearing, liability, tax, and possible price-difference or stock-value correction.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>A material document records the stock movement. An accounting document records the financial effect. They are linked, but they are not the same document. A movement can therefore exist without an FI posting when it is not valuation-relevant, for example a pure internal transfer that does not change value.</p>
    <p>After a material document is posted, you do not edit its core values. If quantity, movement type, plant, or storage location is wrong, the normal correction pattern is reversal and reposting with the correct data.</p>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">corporate_fare</span>
      <p><strong>Organizational consequence:</strong> for a valuated goods movement, the company-code context of the FI document follows from the plant and its organizational assignment. This is why a plant choice can have accounting consequences.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="price-control" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Price control</p>
      <h2>S and V answer one design question: should procurement differences change stock value?</h2>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Standard price and moving average price comparison">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Price control</th><th scope="col">Inventory valuation</th><th scope="col">Price variance</th><th scope="col">Useful mental model</th></tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">S — Standard price</th>
            <td>Stock is valuated at the standard price stored for the material.</td>
            <td>Differences between standard, PO, and invoice values are separated from inventory and posted to price-difference accounts.</td>
            <td>Keep inventory stable; make variances visible.</td>
          </tr>
          <tr>
            <th scope="row">V — Moving average price</th>
            <td>Stock value follows delivered cost and the moving average is recalculated from total stock value / total stock quantity.</td>
            <td>Differences normally correct inventory value when sufficient stock coverage exists.</td>
            <td>Let current procurement cost flow into inventory.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p><strong>Do not mix MAP with periodic unit price.</strong> In Material Ledger scenarios, periodic unit price can become relevant as a period-end actual valuation concept. For this procurement topic, the core runtime contrast is still standard price versus moving average price.</p>
  </section>

  <section class="research-canvas__inventory" id="worked-example" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">One worked example</p>
      <h2>The same PO produces different valuation logic under S and V.</h2>
      <p>We ignore tax and planned delivery costs here so the valuation mechanics stay visible.</p>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">calculate</span>
      <p><strong>Starting point:</strong> stock = 100 PC, total stock value = 200, unit value = 2.00. Purchase order = 100 PC at 2.40. Supplier invoice later arrives for 100 PC at 2.20.</p>
    </div>

    <h3>Case A — Standard price = 2.00</h3>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Standard price worked example">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Step</th><th scope="col">Posting logic</th><th scope="col">Stock after posting</th><th scope="col">Meaning</th></tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Goods receipt</th>
            <td>Dr Inventory 200<br />Dr Price difference 40<br />Cr GR/IR 240</td>
            <td>200 PC / value 400 / standard price 2.00</td>
            <td>Inventory receives quantity at standard price. The PO is higher than standard, so the 40 difference is kept outside inventory.</td>
          </tr>
          <tr>
            <th scope="row">Invoice receipt</th>
            <td>Dr GR/IR 240<br />Cr Supplier 220<br />Cr Price difference 20</td>
            <td>200 PC / value 400 / standard price 2.00</td>
            <td>The invoice is lower than the PO, so part of the earlier variance is reversed through the price-difference account. Inventory does not change.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>The net procurement cost is 220 for the new 100 PC, but inventory still increases by only 200 because the material is held at standard price. The remaining net difference of 20 stays outside stock value.</p>

    <h3>Case B — Moving average price starts at 2.00</h3>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Moving average price worked example">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Step</th><th scope="col">Posting logic</th><th scope="col">Stock after posting</th><th scope="col">Meaning</th></tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Goods receipt</th>
            <td>Dr Inventory 240<br />Cr GR/IR 240</td>
            <td>200 PC / value 440 / MAP 2.20</td>
            <td>The GR is valuated at the PO price. New MAP = 440 / 200 = 2.20.</td>
          </tr>
          <tr>
            <th scope="row">Invoice receipt</th>
            <td>Dr GR/IR 240<br />Cr Supplier 220<br />Cr Inventory 20</td>
            <td>200 PC / value 420 / MAP 2.10</td>
            <td>The actual invoice is lower than the PO. With sufficient stock coverage, SAP corrects stock value by 20. New MAP = 420 / 200 = 2.10.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p><strong>Why 2.10?</strong> We now own 100 old pieces valued at 2.00 and 100 newly procured pieces whose final supplier cost is 2.20. Total value is 420 for 200 pieces, so the moving average is 2.10.</p>
  </section>

  <section class="research-canvas__inventory" id="stock-coverage" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Critical exception</p>
      <h2>Moving average price does not mean every invoice variance always goes to inventory.</h2>
    </header>

    <p>Suppose goods were received, but part of them was consumed before the supplier invoice arrived. The full original quantity is no longer in stock. SAP cannot push the whole invoice price difference into the remaining inventory without distorting the value of stock that no longer exists.</p>
    <p>With moving average price, the invoice variance is posted to inventory only for the quantity still covered by stock. The uncovered part is posted to a price-difference expense or revenue account. This is the stock-coverage rule.</p>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">warning</span>
      <p><strong>Assessment trap:</strong> “V means all price differences go to stock” is incomplete. The correct answer is “normally to stock when sufficient stock coverage exists; otherwise the uncovered portion goes to a price-difference account.”</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="gr-ir" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">GR/IR clearing</p>
      <h2>GR/IR separates receipt timing from invoice timing.</h2>
    </header>

    <p>At goods receipt, SAP normally knows the purchase-order value but does not yet post a supplier liability. It therefore credits the GR/IR clearing account. At invoice receipt, the system debits GR/IR and credits the supplier account. When quantities and values match, the temporary balance clears.</p>
    <p>An open GR/IR balance is not automatically an error. It can mean the invoice has not arrived, the goods have not arrived, quantities differ, or a business decision is still needed about whether a remaining receipt or invoice is expected.</p>

    <div class="ecg-decision-columns">
      <div><h3>More GR than IR</h3><p>The system still expects an invoice for received goods.</p></div>
      <div><h3>More IR than GR</h3><p>The system still expects a goods receipt for invoiced quantity.</p></div>
      <div><h3>Business is complete</h3><p>Only after proving that no further receipt or invoice will occur should reconciliation or clearing be considered.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="account-determination" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Automatic account determination</p>
      <h2>Do not memorize account numbers. Understand the posting purpose.</h2>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="MM automatic account determination transaction keys">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Transaction key</th><th scope="col">Purpose</th><th scope="col">Typical role in this topic</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">BSX</th><td>Inventory posting</td><td>Stock account for valuated material movements.</td></tr>
          <tr><th scope="row">WRX</th><td>GR/IR clearing</td><td>Temporary bridge between goods receipt and invoice receipt.</td></tr>
          <tr><th scope="row">PRD</th><td>Price differences</td><td>Variance posting when price control or stock coverage sends the difference outside inventory.</td></tr>
        </tbody>
      </table>
    </div>

    <p>The final G/L account depends on the system's automatic account-determination setup and material valuation context. The material master contributes key information such as valuation class and price control. The document history contributes PO price, receipt status, and invoice status.</p>
    <p><strong>Lead diagnostic rule:</strong> first prove the amount and transaction purpose. Only then investigate why account determination selected a specific G/L account.</p>
  </section>

  <section class="research-canvas__inventory" id="diagnostics" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Diagnostics</p>
      <h2>If the FI document looks wrong, trace the decision instead of changing the account first.</h2>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>01</span><small>event</small></div><h3>Confirm the posting sequence</h3><p class="ecg-question">Did GR happen before IR, or did the invoice arrive first?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Evidence</h4><p>PO history, material document, invoice document, accounting documents.</p></div>
          <div><h4>Why it matters</h4><p>Valuation can use PO or invoice values differently depending on the sequence.</p></div>
          <div><h4>Do not do</h4><p>Do not compare only the final FI document with the PO and assume the difference is an account-determination defect.</p></div>
        </div>
      </article>

      <article class="ecg-determination-detail">
        <header><div><span>02</span><small>valuation</small></div><h3>Check S or V and current stock</h3><p class="ecg-question">Should the variance stay outside stock or correct stock value?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Standard price</h4><p>Expect inventory at standard price and variances outside stock.</p></div>
          <div><h4>Moving average</h4><p>Expect delivered cost to affect stock value when sufficient coverage exists.</p></div>
          <div><h4>Evidence</h4><p>Material valuation data, stock quantity at invoice time, PO and invoice prices.</p></div>
        </div>
      </article>

      <article class="ecg-determination-detail">
        <header><div><span>03</span><small>account</small></div><h3>Then inspect automatic account determination</h3><p class="ecg-question">Was the posting purpose correct but the G/L account wrong?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Inventory</h4><p>Check the account used for the inventory posting purpose.</p></div>
          <div><h4>GR/IR</h4><p>Check the clearing account determination and organizational context.</p></div>
          <div><h4>Price difference</h4><p>Check the price-difference account only after proving that a price-difference posting is actually expected.</p></div>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">60-second assessment answer</p>
      <h2>Explain the event, the price control, and the destination of the variance.</h2>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>Answer:</strong> “When I post a goods receipt for a PO, SAP creates a material document, and if the movement is valuated it also creates an accounting document. GR/IR is the temporary offset because the supplier liability is normally created only at invoice receipt. With standard price, stock is posted at the material's standard price and differences to the PO or invoice are posted to price-difference accounts. With moving average price, the GR is normally posted at the PO value and the moving average is recalculated. If the invoice later differs from the PO, the variance normally adjusts stock when there is enough stock coverage; otherwise the uncovered part goes to a price-difference account. I would diagnose a wrong posting by checking document sequence, price control, stock coverage, and only then automatic account determination.”</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="common-mistakes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Common mistakes</p>
      <h2>Five statements to avoid in an assessment.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>“Every goods movement creates FI.”</h3><p>No. The movement must be valuation-relevant.</p></div>
      <div><h3>“GR creates the supplier liability.”</h3><p>Not in the normal PO flow. GR normally posts against GR/IR; the supplier liability is created at invoice receipt.</p></div>
      <div><h3>“Standard price follows the PO.”</h3><p>No. Stock remains at standard price; procurement differences are separated.</p></div>
      <div><h3>“MAP means all differences go to stock.”</h3><p>Only when the stock-coverage rule allows it.</p></div>
      <div><h3>“A wrong G/L means OBYC is wrong.”</h3><p>First prove that the business event, valuation method, amount, and transaction key are correct.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="related" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Continue the chain</p>
      <h2>Material valuation sits between Procurement, Inventory, and Finance.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/procurement/"><span>MM</span><strong>Procurement Process & Decision Map</strong><small>Requirement, source, PO, receipt, invoice, and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/inventory-management/"><span>IM</span><strong>Inventory Management</strong><small>Movement types, stock categories, quantity updates, and inventory evidence.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/finance-logistics/"><span>FI</span><strong>FI/CO for Logistics</strong><small>Accounting consequences, G/L logic, clearing, and reconciliation across logistics.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/procurement/tax-code-determination/"><span>TAX</span><strong>Tax Code Determination</strong><small>PO tax code, invoice tax, deductible and non-deductible treatment.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Use SAP product documentation for release-sensitive behavior.</h2>
      <p>This page explains the standard logic used in the current SAP Learning procurement course and SAP S/4HANA Help examples. Customer configuration, localization, Material Ledger settings, special stock, account assignment, planned delivery costs, exchange rates, and invoice sequence can add more posting lines.</p>
    </header>
    <div class="research-route-list">
      <a href="https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-procurement/analyzing-material-valuation" target="_blank" rel="noopener"><span>SAP</span><strong>Analyzing Material Valuation</strong><small>Current SAP Learning lesson for S4500 procurement valuation.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/be5eb6531de6b64ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Invoices for Purchase Orders</strong><small>Price variance behavior for standard price and moving average price.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/8860b6531de6b64ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Example: Material with MAP</strong><small>GR, invoice, GR/IR, stock correction, and stock-coverage logic.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/s4hana-best-practices/ycoa-1f2ae10b96f740759d66e695f953aa8f/wrx-gr-ir-clearing-account" target="_blank" rel="noopener"><span>SAP</span><strong>WRX — GR/IR Clearing Account</strong><small>Account-determination example for inventory, GR/IR, and price variance.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
