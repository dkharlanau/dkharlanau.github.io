---
layout: default
title: "Material Valuation and Automatic Account Determination — SAP S/4HANA MM"
description: "A practical SAP S/4HANA MM guide to material valuation, automatic account determination, valuation classes, transaction keys, G/L postings, split valuation, GR/IR, and delivery-cost accounting."
permalink: /labs/enterprise-context/procurement/material-valuation/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-10-04
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
  - automatic-account-determination
  - valuation-class
  - split-valuation
source_links:
  - title: "Analyzing Material Valuation"
    url: "https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-procurement/analyzing-material-valuation"
  - title: "Invoices for Purchase Orders"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/be5eb6531de6b64ce10000000a174cb4.html"
  - title: "Example: Material with MAP"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/8860b6531de6b64ce10000000a174cb4.html"
  - title: "Example: Material with MAP Without Stock Coverage"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/6370b6531de6b64ce10000000a174cb4.html"
  - title: "Product Valuation"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/18fe3fab96864826bfa0be0de4f65b85/772bf4b02b4245d9912a2b04cd042643.html"
  - title: "WRX — GR/IR Clearing Account"
    url: "https://help.sap.com/docs/s4hana-best-practices/ycoa-1f2ae10b96f740759d66e695f953aa8f/wrx-gr-ir-clearing-account"
  - title: "Describing Automatic Account Determination"
    url: "https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/describing-automatic-account-determination"
  - title: "Determining the Relevance of Company Codes and Valuation Areas"
    url: "https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/determining-the-relevance-of-company-codes-and-valuation-areas"
  - title: "Creating Valuation Classes and Account Category References"
    url: "https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/creating-valuation-classes-and-account-category-references"
  - title: "Setting Up Account Determination for Specific Transactions"
    url: "https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/setting-up-account-determination-for-specific-transactions"
  - title: "Subdividing a Transaction with the Account Grouping Code"
    url: "https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/subdividing-a-transaction-with-the-account-grouping-code"
  - title: "Adjusting Account Determination for Special Cases"
    url: "https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/adjusting-account-determination-for-special-cases"
  - title: "Adjusting Settings for Split Valuation"
    url: "https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/adjusting-settings-for-split-valuation"
last_reviewed: 2026-10-02
publication_wave: "logistics-search-wave-01"
review_method: "Current SAP Learning S4500 material-valuation lesson + SAP S/4HANA 2025 FPS01 Help cross-check + editorial rewrite"
search_intent: "SAP MM material valuation automatic account determination valuation class transaction key GBB BSX WRX PRD split valuation GR IR FI postings"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-procurement"
ai_sidecar: "/ai/pages/labs--enterprise-context--procurement--material-valuation.json"
entity_mentions:
  - "sap-s4hana"
  - "sap-inventory-management"
semantic_links:
  - type: "same_domain"
    title: "Tax Code Determination in Purchasing & Invoice Receipt — SAP S/4HANA MM"
    url: "/labs/enterprise-context/procurement/tax-code-determination/"
  - type: "parent_context"
    title: "Procurement Process & Decision Map — Enterprise Context Lab"
    url: "/labs/enterprise-context/procurement/"
  - type: "related_topic"
    title: "Inventory Management — Enterprise Context Lab"
    url: "/labs/enterprise-context/inventory-management/"
  - type: "related_topic"
    title: "SAP Business Partner — Roles, CVI and Organizational Data"
    url: "/labs/enterprise-context/business-partner/"
  - type: "related_topic"
    title: "Who Owns an Open GR/IR Balance? — SAP Procurement Decision Card"
    url: "/labs/enterprise-context/decisions/grir-ownership/"
  - type: "parent_context"
    title: "Labs — SAP Enterprise, Assurance, AI, Interview and Assessment"
    url: "/labs/"
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
      <h2>The G/L account is the end of a determination chain.</h2>
      <p>Do not start with an account number. SAP first decides which accounting operation is required, then combines organizational and material context to find the G/L account.</p>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
      <p><strong>Fast chain:</strong> business event → value string → transaction/event key → optional general modification → chart of accounts and valuation grouping → valuation class → G/L account.</p>
    </div>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Factors that influence MM automatic account determination">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Factor</th><th scope="col">Question it answers</th><th scope="col">Why it matters</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">Business event / movement type</th><td>What happened?</td><td>Controls the goods-movement logic and helps determine which posting operations can be required.</td></tr>
          <tr><th scope="row">Chart of accounts</th><td>Which G/L account framework applies?</td><td>The company code is assigned to a chart of accounts. Automatic account determination is maintained separately for each chart of accounts.</td></tr>
          <tr><th scope="row">Valuation area and valuation grouping code</th><td>Which organizational valuation context applies?</td><td>The grouping code can let several valuation areas share the same account assignment or keep them different.</td></tr>
          <tr><th scope="row">Valuation class</th><td>Which material account family applies?</td><td>Materials that need different stock or consumption accounts can use different valuation classes.</td></tr>
          <tr><th scope="row">Transaction/event key</th><td>What is the accounting purpose?</td><td>Examples are stock, GR/IR, price difference, or an offsetting entry to inventory.</td></tr>
          <tr><th scope="row">General modification</th><td>Does one transaction key need a finer split?</td><td>For selected keys such as GBB, it separates business reasons such as production consumption, scrapping, or inventory differences.</td></tr>
        </tbody>
      </table>
    </div>

    <p><strong>Lead rule:</strong> an account-determination problem is not proven because a G/L account looks wrong. First prove the business event, expected amount, transaction/event key, organizational context, and material valuation class. Then compare the configured account.</p>
  </section>

  <section class="research-canvas__inventory" id="transaction-keys" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Transaction/event keys</p>
      <h2>Remember the posting purpose, not customer-specific account numbers.</h2>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Important MM transaction event keys">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Key</th><th scope="col">Purpose</th><th scope="col">Typical use</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">BSX</th><td>Stock posting</td><td>Inventory account for valuated stock movements.</td></tr>
          <tr><th scope="row">WRX</th><td>GR/IR clearing</td><td>Temporary bridge between valuated goods receipt and supplier invoice.</td></tr>
          <tr><th scope="row">PRD</th><td>Price differences</td><td>Variance outside inventory when price control or stock coverage requires it.</td></tr>
          <tr><th scope="row">GBB</th><td>Offsetting entry for inventory posting</td><td>Goods issues, scrapping, inventory differences, and other movements where the business reason matters.</td></tr>
          <tr><th scope="row">UMB</th><td>Gain/loss from revaluation</td><td>Value changes caused by revaluation scenarios.</td></tr>
          <tr><th scope="row">KDM</th><td>Exchange-rate differences</td><td>Foreign-currency PO cases when an exchange-rate difference cannot be posted to the material account.</td></tr>
        </tbody>
      </table>
    </div>

    <p>Other transaction keys exist for specific processes, for example purchase-account management or subcontracting. For assessment preparation, the important skill is to explain why a key is needed and which business event produced it.</p>
    <p><strong>Boundary:</strong> the supplier line does not come from the same MM account-determination rule. The supplier posts through the reconciliation account assigned in Business Partner / Financial Accounting. Tax accounts follow tax determination. This prevents a common error: treating every line in the accounting document as an MM automatic-posting problem.</p>
  </section>

  <section class="research-canvas__inventory" id="value-strings" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Value strings</p>
      <h2>A value string says what may post. It does not contain the final G/L accounts.</h2>
    </header>

    <p>SAP provides value strings for accounting-relevant Inventory Management and Invoice Verification processes. A value string contains transaction/event keys for the posting operations that can occur. The G/L account is determined later from the key plus the active organizational and material factors.</p>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Account determination layers">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Layer</th><th scope="col">Meaning</th><th scope="col">Assessment question</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">Movement / business process</th><td>The logistics event that is being posted.</td><td>What happened and which movement type or IV process was used?</td></tr>
          <tr><th scope="row">Value string</th><td>The possible accounting operations for that process.</td><td>Which transaction/event keys can be triggered?</td></tr>
          <tr><th scope="row">Transaction/event key</th><td>The accounting purpose, such as stock or GR/IR.</td><td>What kind of posting should this line represent?</td></tr>
          <tr><th scope="row">General modification</th><td>An optional finer split of selected transaction keys.</td><td>Why did this stock movement occur?</td></tr>
          <tr><th scope="row">Automatic account determination</th><td>The mapping from the active factors to the G/L account.</td><td>Which account should receive this posting in this valuation context?</td></tr>
        </tbody>
      </table>
    </div>

    <p>For example, a standard valuated goods receipt for a PO can require BSX for inventory and WRX for GR/IR. If a standard-price material has a variance between PO price and valuation price, PRD can also become relevant. The value string defines the possible posting operations; it does not replace the account-determination table.</p>
  </section>

  <section class="research-canvas__inventory" id="organization-and-material" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Organization and material</p>
      <h2>Chart of accounts, valuation area, and valuation class answer different questions.</h2>
    </header>

    <div class="ecg-decision-columns">
      <div><h3>Chart of accounts</h3><p>The plant leads to a company code, and the company code uses a chart of accounts. Account determination is maintained for that chart because the meaning and number of a G/L account belong to it.</p></div>
      <div><h3>Valuation area</h3><p>The valuation area defines where material stock is valuated. In the customizing model covered by SAP Learning, the valuation level is defined as company code or plant. This is a foundational organizational decision.</p></div>
      <div><h3>Valuation grouping code</h3><p>It groups valuation areas for account determination. The same code can reuse the same G/L mapping; different codes can separate accounts even when the chart of accounts is the same.</p></div>
    </div>

    <h3>Valuation class is the material-side account key</h3>
    <p>The valuation class groups materials that should use the same account logic. Material type and account category reference control which valuation classes are allowed. The material then carries the relevant valuation class in its accounting data.</p>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">compare_arrows</span>
      <p><strong>Do not mix two fields:</strong> price control answers <em>how much</em> inventory is worth (for example S or V). Valuation class helps answer <em>which G/L account family</em> receives the posting. Both can influence the same accounting document, but they solve different problems.</p>
    </div>

    <p>The exact configuration UI and available organizational choices depend on the deployment model. In an assessment, explain the determination logic first; then state which S/4HANA edition and configuration scope you are talking about.</p>
  </section>

  <section class="research-canvas__inventory" id="account-grouping" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">General modification</p>
      <h2>GBB needs a second question: why did inventory change?</h2>
    </header>

    <p>GBB is intentionally broad. A goods issue to production, scrapping, and an inventory difference can all need an offsetting entry to inventory, but Finance normally wants different expense or difference accounts. The account grouping code, also called the general modification, provides that extra split.</p>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Common GBB general modification examples">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Business reason</th><th scope="col">Common movement example</th><th scope="col">Transaction logic</th><th scope="col">Expected account family</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">Production consumption</th><td>261</td><td>GBB + VBR in the standard example</td><td>Consumption / production issue</td></tr>
          <tr><th scope="row">Scrapping</th><td>551</td><td>GBB + VNG in the standard example</td><td>Scrapping expense</td></tr>
          <tr><th scope="row">Inventory difference</th><td>Physical-inventory difference movement</td><td>GBB + INV in the standard example</td><td>Inventory difference expense or income</td></tr>
        </tbody>
      </table>
    </div>

    <p>These are standard examples, not a promise that every customer uses identical settings. The movement type and related indicators drive the relevant modification. The important design point is the extra business-reason dimension.</p>
    <p><strong>Assessment boundary:</strong> the account grouping code described here is for Inventory Management transactions. It is not used to subdivide Invoice Verification transactions.</p>
  </section>

  <section class="research-canvas__inventory" id="special-cases" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Special cases</p>
      <h2>Some postings use extra account-determination inputs outside the simple stock example.</h2>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Special MM account determination cases">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Case</th><th scope="col">Determination consequence</th><th scope="col">Lead-level point</th></tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Account-assigned purchasing item</th>
            <td>GBB plus the account modification of the account assignment category can default the G/L account. With a material, the material valuation class is relevant. Without a material, a material-group valuation class or a blank valuation class can be used, depending on setup.</td>
            <td>The G/L default and the CO object are different decisions. Cost center, order, WBS element, or another receiver still comes from account assignment.</td>
          </tr>
          <tr>
            <th scope="row">Planned delivery costs</th>
            <td>They are planned in the PO with condition types. Their account keys come from the purchasing calculation schema and can post through a clearing or provision account at goods receipt.</td>
            <td>Do not look for these account keys in the MM value string. The purchasing pricing schema owns this part of the design.</td>
          </tr>
          <tr>
            <th scope="row">Unplanned delivery costs</th>
            <td>Invoice Verification can distribute them across invoice items or post them to a separate G/L account. The separate-account option uses transaction key UPF.</td>
            <td>The choice changes whether the cost behaves like a price variance on the items or is isolated on its own account.</td>
          </tr>
          <tr>
            <th scope="row">Supplier and tax lines</th>
            <td>The supplier uses its reconciliation-account logic; tax uses tax determination.</td>
            <td>Not every line in an MM-triggered accounting document is determined by the same MM transaction key.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="split-valuation" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Split valuation</p>
      <h2>One material number can have sub-stocks with different values and different account logic.</h2>
    </header>

    <p>Split valuation is useful when the same material must be valued differently inside one valuation area, for example by procurement type or origin. It avoids separate material numbers, but it adds another operational decision to purchasing and goods movements.</p>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Split valuation concepts">
      <table class="study-table__table">
        <thead>
          <tr><th scope="col">Object</th><th scope="col">Meaning</th><th scope="col">Example</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">Valuation category</th><td>The criterion used to split the stock.</td><td>Procurement type or origin.</td></tr>
          <tr><th scope="row">Valuation type</th><td>One concrete partial stock inside that category.</td><td>External / in-house, or Germany / China.</td></tr>
          <tr><th scope="row">Valuation area assignment</th><td>Where the category and types are allowed for use.</td><td>A specific plant when plant-level valuation is active.</td></tr>
          <tr><th scope="row">Valuation class by type</th><td>Allows partial stocks to reach different stock or consumption accounts.</td><td>External stock and in-house stock can use different account mappings.</td></tr>
        </tbody>
      </table>
    </div>

    <p>Valuation categories and valuation types are defined globally and then assigned for use in valuation areas. If a valuation type is entered in the purchase order, the later goods receipt is tied to that type. If it is not entered in the PO, the valuation type must be provided when the receipt requires it.</p>
    <p><strong>Design trade-off:</strong> split valuation reduces master-data duplication, but every value-relevant movement must identify the correct partial stock. It increases configuration, master-data, and operational discipline. SAP Learning also notes that split valuation can only be activated for a material when existing stock or open documents do not block the change.</p>
  </section>

  <section class="research-canvas__inventory" id="diagnostics" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Diagnostics</p>
      <h2>If the FI document looks wrong, replay the determination chain.</h2>
      <p>The fastest path is to find the first wrong decision. Changing a G/L account before that point is understood can hide the real defect.</p>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>01</span><small>event</small></div><h3>Prove the business event and sequence</h3><p class="ecg-question">What was posted, with which movement or IV process, and in what order?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Evidence</h4><p>PO history, material document, invoice document, accounting document, reversal status.</p></div>
          <div><h4>Why it matters</h4><p>A correct account for the wrong movement is still a process defect.</p></div>
          <div><h4>First split</h4><p>Wrong amount points toward quantity, price, valuation, currency, or condition logic before account mapping.</p></div>
        </div>
      </article>

      <article class="ecg-determination-detail">
        <header><div><span>02</span><small>posting</small></div><h3>Identify the expected posting purpose</h3><p class="ecg-question">Which value string and transaction/event keys should this process produce?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Stock receipt</h4><p>Expect BSX and WRX in the normal valuated PO receipt, with PRD only when the valuation logic requires a difference posting.</p></div>
          <div><h4>Goods issue</h4><p>For an offsetting inventory entry, determine whether GBB is expected and why the stock left.</p></div>
          <div><h4>Boundary</h4><p>Do not treat supplier or tax lines as if they came from the same MM transaction key.</p></div>
        </div>
      </article>

      <article class="ecg-determination-detail">
        <header><div><span>03</span><small>context</small></div><h3>Rebuild organization and material inputs</h3><p class="ecg-question">Which chart of accounts, valuation grouping code, valuation class, and price-control context were active?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Organization</h4><p>Plant → company code → chart of accounts, plus valuation area and grouping code.</p></div>
          <div><h4>Material</h4><p>Material type, valuation class, price control, and valuation type when split valuation is active.</p></div>
          <div><h4>Evidence</h4><p>Use the values that were valid for the posting, not only today's master data after later changes.</p></div>
        </div>
      </article>

      <article class="ecg-determination-detail">
        <header><div><span>04</span><small>modifier</small></div><h3>Check the extra business-reason split</h3><p class="ecg-question">Does the transaction key use a general modification or another special account key?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>GBB</h4><p>Check the movement type and the resulting general modification such as the production, scrapping, or inventory-difference branch.</p></div>
          <div><h4>Delivery costs</h4><p>For planned costs, inspect purchasing condition and account keys; for unplanned costs, inspect the Invoice Verification setting.</p></div>
          <div><h4>Account assignment</h4><p>Separate the G/L default from the cost object or other management-accounting receiver.</p></div>
        </div>
      </article>

      <article class="ecg-determination-detail">
        <header><div><span>05</span><small>proof</small></div><h3>Compare the configured account and simulate before changing it</h3><p class="ecg-question">Does the active combination map to the expected G/L account?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Simulation</h4><p>The simulation in Configure Automatic Postings can test material or valuation class, plant, and the relevant Inventory Management or Invoice Verification transaction.</p></div>
          <div><h4>Posting readiness</h4><p>Check that the G/L account exists and that field-status requirements are compatible with the movement and account assignment.</p></div>
          <div><h4>Proof</h4><p>After correction, repeat the supported business process or test scenario and compare the new accounting document with the expected posting purpose.</p></div>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">60–90 second assessment answer</p>
      <h2>Explain automatic account determination as a chain, not as a transaction code.</h2>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>Answer:</strong> “In MM, I do not normally enter the G/L account for a valuated goods movement. SAP first identifies the business event and the posting operations required for it. A value string contains transaction/event keys such as BSX for stock, WRX for GR/IR, PRD for price differences, or GBB for an offsetting inventory entry. The final account is then determined from the chart of accounts, valuation grouping context, transaction key, valuation class, and, where the key supports it, a general modification. For GBB, that modification lets us separate production consumption, scrapping, and inventory differences. I also separate this from price control: S or V decides valuation behavior, while valuation class helps decide the account. If a posting is wrong, I trace the event, key, organizational and material inputs, modifier, and configured account before changing Customizing.”</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="common-mistakes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Common mistakes</p>
      <h2>Seven statements to avoid in an assessment.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>“The movement type directly stores the G/L account.”</h3><p>No. It helps drive posting logic. The final G/L comes from automatic account determination.</p></div>
      <div><h3>“Valuation class alone determines the account.”</h3><p>No. It is one input together with chart of accounts, transaction key, valuation grouping, and any active modifier.</p></div>
      <div><h3>“Price control and valuation class do the same thing.”</h3><p>No. Price control drives valuation behavior; valuation class groups materials for account determination.</p></div>
      <div><h3>“GBB means one consumption account.”</h3><p>No. General modification can separate production consumption, scrapping, inventory differences, and other reasons.</p></div>
      <div><h3>“General modification also subdivides Invoice Verification.”</h3><p>Not in this MM account-grouping logic. It is used for Inventory Management transactions.</p></div>
      <div><h3>“The supplier line is determined by BSX, WRX, or GBB.”</h3><p>No. The supplier uses its reconciliation-account logic; tax has its own determination.</p></div>
      <div><h3>“Split valuation means creating another material number.”</h3><p>No. It keeps one material number and separates partial stocks with valuation types.</p></div>
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
      <p>This page explains the determination model and the standard examples used in current SAP Learning material. Customer configuration, localization, Material Ledger settings, special stock, account assignment, planned delivery costs, exchange rates, and deployment model can change the detailed posting lines or configuration path.</p>
    </header>
    <div class="research-route-list">
      <a href="https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-procurement/analyzing-material-valuation" target="_blank" rel="noopener"><span>SAP</span><strong>Analyzing Material Valuation</strong><small>Standard price, moving average price, and procurement valuation.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/describing-automatic-account-determination" target="_blank" rel="noopener"><span>SAP</span><strong>Describing Automatic Account Determination</strong><small>Organizational, material, and business-transaction factors.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/determining-the-relevance-of-company-codes-and-valuation-areas" target="_blank" rel="noopener"><span>SAP</span><strong>Company Codes and Valuation Areas</strong><small>Chart of accounts, valuation area, and valuation grouping code.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/creating-valuation-classes-and-account-category-references" target="_blank" rel="noopener"><span>SAP</span><strong>Valuation Classes and Account Category References</strong><small>Material-side grouping for account determination.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/setting-up-account-determination-for-specific-transactions" target="_blank" rel="noopener"><span>SAP</span><strong>Account Determination for Specific Transactions</strong><small>Value strings and transaction/event keys such as BSX, WRX, PRD, and GBB.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/subdividing-a-transaction-with-the-account-grouping-code" target="_blank" rel="noopener"><span>SAP</span><strong>Account Grouping Code</strong><small>General modification for finer Inventory Management account splits.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/adjusting-account-determination-for-special-cases" target="_blank" rel="noopener"><span>SAP</span><strong>Account Determination for Special Cases</strong><small>Default accounts and account-assigned purchasing scenarios.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/cross-functional-customizing-in-sap-s-4hana-materials-management/adjusting-settings-for-split-valuation" target="_blank" rel="noopener"><span>SAP</span><strong>Split Valuation</strong><small>Valuation categories, valuation types, and account consequences.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/be5eb6531de6b64ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Invoices for Purchase Orders</strong><small>Price variance behavior for standard price and moving average price.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/8860b6531de6b64ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Example: Material with MAP</strong><small>GR, invoice, GR/IR, stock correction, and stock-coverage logic.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/s4hana-best-practices/ycoa-1f2ae10b96f740759d66e695f953aa8f/wrx-gr-ir-clearing-account" target="_blank" rel="noopener"><span>SAP</span><strong>WRX — GR/IR Clearing Account</strong><small>Account-determination example for inventory, GR/IR, and price variance.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
