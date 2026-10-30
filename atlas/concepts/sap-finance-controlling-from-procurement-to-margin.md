---
layout: default
title: "Where Does the Money Go? SAP S/4HANA FI/CO, Procurement, Production, Costing and Margin Analysis"
description: "A worked, source-backed introduction to how values move through SAP MM, PP, SD, FI, CO, Product Costing, Material Ledger and CO-PA, with journal examples, diagrams, diagnostics and practice."
permalink: /atlas/concepts/sap-finance-controlling-from-procurement-to-margin/
last_modified_at: 2026-10-30
last_reviewed:
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
author: "Dzmitryi Kharlanau"
atlas_section: concepts
domain: SAP Enterprise
subdomain: Cross-process financial integration
concept_type: learning guide
sap_area: "FI / CO / MM / SD / PP"
business_process: "Procure to pay, plan to produce, order to cash"
tags:
  - sap-s4hana
  - sap-fi
  - sap-co
  - product-costing
  - margin-analysis
  - material-ledger
  - controlling
  - procurement
  - manufacturing
  - order-to-cash
related:
  - /labs/enterprise-context/finance-logistics/
  - /labs/enterprise-context/production/
  - /labs/enterprise-context/procurement/
  - /labs/enterprise-context/billing/
  - /atlas/concepts/order-to-cash/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/labs/enterprise-context/finance-logistics/">FI/CO for Logistics</a></li><li aria-current="page">From Cost to Margin</li></ol></nav>

<header class="note-header">
<p class="eyebrow">SAP finance / guided learning</p>
<h1>Where does the money go?</h1>
<p class="note-subtitle">A practical guide to FI, CO, Product Costing, Material Ledger and CO-PA through one product, from supplier purchase to customer profit.</p>
</header>

<p><strong>Reading time:</strong> approximately 30–40 minutes. <strong>Best for:</strong> SAP SD/MM consultants moving into cross-functional solution design. <strong>Source review:</strong> 30 October 2026; SAP S/4HANA on-premise / Private Edition 2025 FPS02 where available, and Cloud Public Edition 2608 where explicitly indicated. <strong>Editorial status:</strong> learning draft awaiting human review.</p>

**Start with one rule:** SAP does not move “a cost” through a single module. Each business event has a quantity, a financial value, a G/L account, and sometimes a controlling object. The next event can change where that value appears. A customer order, purchase order, production order, invoice and accounting document are not interchangeable evidence.

## Learning route

1. [Six questions that make FI/CO easier](#six-questions-that-make-fico-easier)
2. [A complete story with numbers](#one-product-one-story)
3. [Read the journal entries](#the-journal-entry-walkthrough)
4. [Understand Product Costing and actual costs](#product-costing-and-actual-costing)
5. [Understand Margin Analysis / CO-PA](#margin-analysis-and-co-pa)
6. [See the surrounding business processes](#when-the-process-is-not-the-simple-example)
7. [Diagnose an integration problem](#a-cross-module-diagnostic-method)
8. [Test yourself and explain the design](#practice-and-interview-answer)

## Six questions that make FI/CO easier

Read every SAP posting using the same six questions. Do this before opening a transaction or asking which team owns the issue.

| Question | What it means | Example |
| --- | --- | --- |
| **1. What happened?** | The physical or commercial event. | A supplier delivered one raw material. |
| **2. How much value moved?** | Valuation rule, price, quantity and currency. | Raw stock is valued at €100. |
| **3. Where was it recorded?** | Financial account and debit/credit effect. | Inventory increases; GR/IR increases. |
| **4. Who or what owns the cost?** | Cost center, manufacturing order, project, profit center or market segment. | Material consumption is assigned to a production order. |
| **5. Is the value final or temporary?** | Stock, expense, receivable, clearing, WIP or variance. | GR/IR must be matched to the supplier invoice. |
| **6. What proves completion?** | The next document, reconciliation or settlement evidence. | A posted invoice, settled order, or cleared customer item. |

**FI and CO are not two independent sets of money.** FI answers which financial accounts and legal entity are affected. CO explains responsibility, purpose, production costs and profitability. In SAP S/4HANA, primary and secondary cost elements are represented as G/L accounts. The Universal Journal (table <code>ACDOCA</code>) brings financial and controlling line-item dimensions together. Not every posting has every profitability dimension. [SAP: Controlling overview](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/dfb64c53d5ec7d77e10000000a441470-2408.html) · [SAP: Universal Journal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c0c54048d35849128be8e872df5bea6d/76c59195039142338af63e8a1a7c016f.html).

### The objects are not the same

| Object | Core question | A useful mental model |
| --- | --- | --- |
| Company code | Which legal entity reports the posting? | Legal accounting boundary. |
| G/L account / cost element | What kind of value is this? | Inventory, liability, revenue, COGS, salary, allocation. |
| Cost center | Where is the cost managed? | Production department, maintenance, administration. |
| Activity type | Which service did a cost center provide? | Machine hour or labor hour, valued at a cost rate. |
| Production order / product cost collector | What did manufacturing consume and deliver? | Cost object for production execution. |
| Internal order / WBS element | What temporary purpose or project is being funded? | Marketing campaign, investment, customer project. |
| Profit center | Which business unit is responsible for its result? | Management P&amp;L responsibility, often spanning many customers. |
| Profitability segment | Which market slice generated the margin? | Customer × product × market × sales organization, as configured. |
| Operating concern | What is the organizational scope of CO-PA analysis? | Profitability reporting structure. |

A **profit center** and a **profitability segment** are not synonyms. The first often represents internal responsibility. The second combines market characteristics, such as customer and product. The same sales posting may carry both.

## One product, one story

We will manufacture **one finished product** and sell it for **€250 net**. All amounts are in EUR, with no VAT, discounts, freight, returns or foreign currency. We assume standard-price valuation for both the raw material and finished product, a simple make-to-stock process, one production order, and no Material Ledger actual-costing revaluation in the base case.

These are deliberately synthetic amounts, not entries taken from a customer system.

| Input or event | Amount | Why it matters |
| --- | ---: | --- |
| Raw material standard price | €100 | Value used for raw-stock and component-consumption postings. |
| Supplier invoice price | €108 | There is a €8 purchase price difference. |
| Planned production activity | €40 | Standard cost estimate. |
| Planned production overhead | €10 | Standard cost estimate. |
| **Released finished-product standard cost** | **€150** | €100 + €40 + €10. |
| Actual activity allocated to production order | €45 | €5 above the plan. |
| Actual overhead allocated to production order | €12 | €2 above the plan. |
| **Manufacturing-order actual debits** | **€157** | €100 + €45 + €12. |
| Customer net selling price | €250 | Revenue on billing in the baseline. |

<figure aria-labelledby="finance-value-caption">
  <figcaption id="finance-value-caption"><strong>Diagram 1 — one product, six business events.</strong> Follow the amount and the object. The numbers describe a synthetic standard-price example; they are not a universal posting template.</figcaption>
  <div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable diagram tracing value from procurement through finance">
    <svg width="1265" height="250" viewBox="0 0 1265 250" role="img" aria-label="Procurement purchase order, goods receipt to raw stock, production order costing, finished goods receipt, goods issue and customer billing">
      <defs><marker id="fin-arrow" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="#365c79"/></marker></defs>
      <rect x="14" y="42" width="184" height="169" rx="12" fill="#f1f5f9" stroke="#9aabba"/><text x="27" y="70" font-size="15" font-weight="700" fill="#17344a">1 · PROCUREMENT</text><text x="27" y="106" font-size="16" font-weight="600" fill="#122b3a">PO: 1 raw material</text><text x="27" y="137" font-size="15" fill="#294b63">PO price €100</text><text x="27" y="170" font-size="14" fill="#37536a">No journal at PO</text><path d="M 201 126 H 215" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow)"/>
<rect x="223" y="42" width="184" height="169" rx="12" fill="#f1f5f9" stroke="#9aabba"/><text x="236" y="70" font-size="15" font-weight="700" fill="#17344a">2 · GOODS RECEIPT</text><text x="236" y="106" font-size="16" font-weight="600" fill="#122b3a">Raw stock +€100</text><text x="236" y="137" font-size="15" fill="#294b63">GR/IR +€100</text><text x="236" y="170" font-size="14" fill="#37536a">Inventory asset</text><path d="M 410 126 H 424" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow)"/>
<rect x="432" y="42" width="184" height="169" rx="12" fill="#f1f5f9" stroke="#9aabba"/><text x="445" y="70" font-size="15" font-weight="700" fill="#17344a">3 · PRODUCTION</text><text x="445" y="106" font-size="16" font-weight="600" fill="#122b3a">Order actual €157</text><text x="445" y="137" font-size="15" fill="#294b63">Components + activities</text><text x="445" y="170" font-size="14" fill="#37536a">CO cost object</text><path d="M 619 126 H 633" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow)"/>
<rect x="641" y="42" width="184" height="169" rx="12" fill="#f1f5f9" stroke="#9aabba"/><text x="654" y="70" font-size="15" font-weight="700" fill="#17344a">4 · FINISHED GOODS</text><text x="654" y="106" font-size="16" font-weight="600" fill="#122b3a">Finished stock +€150</text><text x="654" y="137" font-size="15" fill="#294b63">Order credited €150</text><text x="654" y="170" font-size="14" fill="#37536a">€7 variance remains</text><path d="M 828 126 H 842" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow)"/>
<rect x="850" y="42" width="184" height="169" rx="12" fill="#f1f5f9" stroke="#9aabba"/><text x="863" y="70" font-size="15" font-weight="700" fill="#17344a">5 · GOODS ISSUE</text><text x="863" y="106" font-size="16" font-weight="600" fill="#122b3a">COGS expense €150</text><text x="863" y="137" font-size="15" fill="#294b63">FG stock −€150</text><text x="863" y="170" font-size="14" fill="#37536a">Expense at PGI</text><path d="M 1037 126 H 1051" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow)"/>
<rect x="1059" y="42" width="184" height="169" rx="12" fill="#ecf8f0" stroke="#408c68"/><text x="1072" y="70" font-size="15" font-weight="700" fill="#17344a">6 · BILLING</text><text x="1072" y="106" font-size="16" font-weight="600" fill="#122b3a">Revenue €250</text><text x="1072" y="137" font-size="15" fill="#294b63">Customer receivable</text><text x="1072" y="170" font-size="14" fill="#37536a">Margin can be analysed</text>
      <text x="15" y="232" font-size="14" fill="#345267">Separate questions: What moved? What was it worth? Which G/L? Which CO object? What must be cleared or settled?</text>
    </svg>
  </div>
</figure>

The path has **three different meanings of cost**. The raw material is first an **asset**. After component issue, it contributes to **production-order cost**. The finished product becomes a **finished-goods asset** again when received. Only when the product is sold does its standard valuation become **cost of goods sold (COGS)** in our baseline. A production variance and purchase price difference remain separate until the configured settlement / actual-costing process deals with them.

### What exists after each event?

| Event | Logistics / SD evidence | FI / CO interpretation | Common misunderstanding |
| --- | --- | --- | --- |
| Purchase order | Purchase order item | Commercial commitment; normally no standard FI journal yet. | “A purchase order is an expense.” |
| Goods receipt for stock | Material document, PO history | Stock asset and GR/IR liability bridge. | “The goods are already paid for.” |
| Supplier invoice | Invoice document, FI journal | Vendor payable, GR/IR match, and possible price difference. | “The invoice always changes stock value.” |
| Component issue | Material document, order actual cost | Raw stock decreases; production cost object gets the consumption. | “The material was lost as an expense.” |
| Activity allocation | Confirmation / CO posting | Manufacturing order receives cost; providing cost center is credited. | “Every internal allocation is another supplier bill.” |
| Finished-goods receipt | Material document, manufacturing order | Finished stock increases at relevant valuation; order receives credit. | “Order actual costs must equal the stock receipt.” |
| Production close | WIP / variance / settlement evidence | Open balances and differences are handled under the configured method. | “Physical completion closes accounting.” |
| Post goods issue | Outbound delivery, goods movement | Inventory decreases; COGS generally increases. | “The customer has already been invoiced.” |
| Customer billing | SD billing document, accounting transfer | Receivable and revenue / taxes / deductions as configured. | “Billing is the COGS posting.” |
| Customer payment | Bank / clearing document | Cash increases, customer receivable is cleared. | “Cash receipt creates sales revenue a second time.” |

## The journal-entry walkthrough

The table is a **teaching-level posting model**. It shows the usual accounting meaning, not every intermediate technical line, document split or account derived in every SAP system. Account names are generic rather than account numbers. Actual account determination depends on the chart of accounts, movement scenario, account assignment, material price control and configuration.

<div class="table-scroll study-table" role="region" aria-label="Simplified journal postings for one purchase-production-sale process" tabindex="0">
<table class="study-table__table">
<thead><tr><th>Step</th><th>Debit (Dr)</th><th>Credit (Cr)</th><th>What you should conclude</th></tr></thead>
<tbody>
<tr><th scope="row">1. Create PO</th><td>—</td><td>—</td><td>A normal stock PO does not by itself create this FI journal.</td></tr>
<tr><th scope="row">2. Receive raw material</th><td>Raw inventory €100</td><td>GR/IR €100</td><td>We own stock but have not yet matched the supplier invoice.</td></tr>
<tr><th scope="row">3. Post supplier invoice</th><td>GR/IR €100; purchase price difference €8</td><td>Supplier payable €108</td><td>GR/IR is matched at the PO value; the €8 remains a separate variance under this standard-price assumption.</td></tr>
<tr><th scope="row">4. Issue raw material to production</th><td>Consumption / production input €100</td><td>Raw inventory €100</td><td>FI recognizes the material consumption effect; the manufacturing order is debited in CO.</td></tr>
<tr><th scope="row">5. Allocate manufacturing activity</th><td>Production order €45 (CO)</td><td>Production cost center €45 (CO)</td><td>Internal allocation shifts managerial cost; it is not a second external payment. The relevant secondary G/L cost element appears in the Universal Journal.</td></tr>
<tr><th scope="row">6. Apply overhead</th><td>Production order €12 (CO)</td><td>Configured overhead sender / credit €12</td><td>Overhead calculation or allocation depends on the costing method and sender rules. This is not a universal external FI posting pair.</td></tr>
<tr><th scope="row">7. Receive finished product</th><td>Finished-goods inventory €150</td><td>Production output / inventory-change account €150</td><td>At the same time, the manufacturing cost object is credited by €150. Its €7 cost balance still needs analysis.</td></tr>
<tr><th scope="row">8. Settle completed production</th><td colspan="2">Configured variance / price-difference / settlement postings for €7</td><td>The cost object is settled according to its receiver and valuation settings. Do not assume the €7 automatically increases this customer's COGS.</td></tr>
<tr><th scope="row">9. Post goods issue for sale</th><td>COGS €150</td><td>Finished-goods inventory €150</td><td>Standard cost moves from stock to expense for this simple sell-from-stock case.</td></tr>
<tr><th scope="row">10. Post customer invoice</th><td>Customer receivable €250</td><td>Sales revenue €250</td><td>Revenue and receivable are created on accounting transfer from billing, excluding tax here.</td></tr>
<tr><th scope="row">11. Receive customer payment</th><td>Bank €250</td><td>Customer receivable €250</td><td>Cash changes; revenue is not created a second time.</td></tr>
</tbody></table>
</div>

For the **supplier payment**, the separate journal is generally Dr supplier payable / Cr bank for €108. It clears the liability, not the purchasing expense again.

**Three traps:** (1) Dr and Cr describe an accounting line, while a production order or cost center is a *cost object*, not simply another G/L account. (2) The €8 purchasing difference is not automatically part of the €157 production-order actual debit when the component was issued at standard €100. (3) A production order with an unsettled balance and a material with a price difference can create a difference between the operational view of margin and the period's financial result. [SAP: goods/invoice receipt](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/825eb6531de6b64ce10000000a174cb4.html) · [SAP: production settlement](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/5c35d85275c8d142e10000000a4450e5-2273.html).

### Why GR/IR is not an error account

The purchasing team orders and receives 100 pieces, but the supplier invoices only 80. The receipt value for 20 pieces may remain open on GR/IR while the remaining invoice is still expected. A GR/IR balance must be interpreted against **purchase-order history, received quantity, invoiced quantity, posting dates and clearing status**. When the process is truly finished, unresolved differences need a controlled reconciliation decision, not a random manual journal. [SAP: GR/IR clearing](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/72256b54f94c8f4ce10000000a4450e5.html).

### Why an expense can later become inventory

During production, materials, activities and overhead are collected on a cost object. Finished-goods receipt creates inventory at the relevant valuation. A partly completed order may require **work in process (WIP)** treatment at period-end. Thus “cost is booked” does not always mean “the product has been sold.” Accounting must distinguish stock, work in process, period expenses and cost of sales, according to the valuation method and recognition rules. [SAP: WIP, variances and settlement](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4032610758dc437089f0c28320eec93f/a5787e40787a4b4eb7c8c69d1faeba38.html).

## Product Costing and actual costing

### 1. Standard cost estimate: what should one unit cost?

Product Cost Planning reads the **BOM** for materials and the **routing / work centers / activities** for manufacturing effort. Material prices, activity rates, costing variants, overhead rules and the cost component structure influence the result.

Our example:

| Cost component | Planned cost per unit |
| --- | ---: |
| Raw material from BOM | €100 |
| Planned production activities | €40 |
| Applied overhead | €10 |
| **Standard cost estimate** | **€150** |

A valid cost estimate can support the released standard price of the finished material. The **cost component split** explains *why* it costs €150, rather than treating €150 as a black box. This is a planning / valuation calculation, not proof that exactly €150 was spent in production. [SAP: cost components](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/82a6d7531a4d414de10000000a174cb4-2589.html) · [SAP: PP master data for costing](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/61c8d8530439414de10000000a174cb4.html).

### 2. Manufacturing-order actuals: what did this order consume?

| Production cost | Plan | Actual assigned to order | Difference |
| --- | ---: | ---: | ---: |
| Raw material consumption at standard valuation | €100 | €100 | €0 |
| Activity | €40 | €45 | +€5 |
| Overhead | €10 | €12 | +€2 |
| **Total** | **€150** | **€157** | **+€7** |

The €157 is an **order-cost figure**. On finished-goods receipt the order can be credited by €150 at standard valuation. The remaining €7 is subject to applicable variance determination and settlement. A period-end process may distinguish WIP from production variances, and settlement receivers and ledger effects depend on the scenario.

**Do not call the €7 the same thing as the €8 supplier price difference.** One arose inside manufacturing execution; the other arose in procurement valuation. They can ultimately affect profitability through different channels. [SAP: variance calculation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/c2de385313e57d77e10000000a441470.html) · [SAP: settlement](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/5c35d85275c8d142e10000000a4450e5-2273.html).

### 3. Standard price S versus moving average V

With **S (standard price)**, inventory movements are valuated using a fixed standard price for the period, and differences are recorded separately according to the posting scenario. With **V (moving average price)**, eligible receipts and invoice differences can change the carrying value and average price while stock coverage and other conditions allow it.

This matters enormously for SD/MM: two materials with the same supplier invoice can produce **different stock and price-difference postings**. Never explain an invoice difference before checking price control, stock coverage, goods-receipt/invoice sequence and any Material Ledger configuration. [SAP: price control and price determination](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/5af1d353ca9f4408e10000000a174cb4.html).

### 4. Material Ledger is not the same as Actual Costing

- **Material Ledger** provides the inventory valuation and currency framework in SAP S/4HANA.
- **Actual Costing**, when activated and configured, uses material price determination and period-end processing to calculate actual costs and distribute eligible differences across inventory and consumption, including multilevel production in supported scenarios.
- Activating Material Ledger does **not** by itself mean that each customer margin is continuously updated with a fully settled actual cost. Actual costing, revaluation, timing and profitability reporting must be designed and verified.

If actual costing is active, our €8 raw-material price difference may be rolled into eligible consumption / higher-level material valuation during period-end processing. This can change the reported cost of goods sold or inventory compared with the standard-price view. Do not assume exactly which part goes to the sold product without testing stock quantities, price determination, transaction sequence and the actual costing run. [SAP: collecting actual costing data](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/6ff1d353ca9f4408e10000000a174cb4.html) · [SAP: price determination](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/5af1d353ca9f4408e10000000a174cb4.html).

### 5. What does “settlement” really mean?

A production order can collect costs without being the final reporting destination. **Settlement** moves relevant balances or results under defined rules to their receivers; it is not a manual way to make an error disappear. An unfinished order may need WIP. A completed order may generate production variances. A project or overhead order has different possible receivers and closing logic. **Allocation** is different: it distributes or charges costs between CO objects, often before settlement.

The design question is: *What is the cost object, what is its final receiver, at what time does the transfer happen, and what reconciles it?*

## Margin Analysis and CO-PA

### Margin Analysis asks a different question from FI-GL

FI can show **total revenue and total COGS**. A sales director asks **which product, customer, market, sales organization or distribution channel generated that margin**. CO-PA adds this market-segment perspective, using the characteristics available and derived for the postings.

- **Account-based CO-PA / Margin Analysis** uses G/L accounts and cost elements in the Universal Journal. It is SAP's preferred integrated profitability approach for S/4HANA.
- **Costing-based CO-PA** uses value fields and its own valuation approach. It can coexist in supported on-premise scenarios but requires additional reconciliation and should not be described as the same data model.
- **COGS split** can separate total COGS into material, production and other cost-component accounts where configured. A cost component split in the cost estimate does not automatically mean you see all those components in every COGS journal. [SAP: costing-based vs margin analysis](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/9e33b3533ebb823de10000000a4450e5.html) · [SAP: COGS split](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/2dd0c7548342b109e10000000a423f68.html).

<figure aria-labelledby="finance-margin-caption">
  <figcaption id="finance-margin-caption"><strong>Diagram 2 — why standard margin and the cost of the example differ.</strong> The final €85 is an economic teaching calculation, not a guaranteed CO-PA report value. Allocation to customers and periods depends on configuration and timing.</figcaption>
  <div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable diagram of standard gross margin versus illustrative actual economic margin">
    <svg width="1148" height="218" viewBox="0 0 1148 218" role="img" aria-label="Net revenue 250, standard cost of goods sold 150, standard gross margin 100, price difference 8 plus production variance 7, economic result 85">
      <defs><marker id="fin-arrow2" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="#365c79"/></marker></defs>
      <rect x="16" y="39" width="206" height="145" rx="11" fill="#ecf2f9" stroke="#8da4b7"/><text x="29" y="75" font-size="25" font-weight="700" fill="#163b4b">€250</text><text x="29" y="106" font-size="14" font-weight="700" fill="#25465b">NET REVENUE</text><text x="29" y="143" font-size="15" fill="#29485a">Billing</text><path d="M 225 111 H 235" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow2)"/><rect x="242" y="39" width="206" height="145" rx="11" fill="#fff1e6" stroke="#8da4b7"/><text x="255" y="75" font-size="25" font-weight="700" fill="#163b4b">− €150</text><text x="255" y="106" font-size="14" font-weight="700" fill="#25465b">STANDARD COGS</text><text x="255" y="143" font-size="15" fill="#29485a">Goods issue</text><path d="M 451 111 H 461" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow2)"/><rect x="468" y="39" width="206" height="145" rx="11" fill="#e9f6ed" stroke="#518b62"/><text x="481" y="75" font-size="25" font-weight="700" fill="#163b4b">= €100</text><text x="481" y="106" font-size="14" font-weight="700" fill="#25465b">STANDARD MARGIN</text><text x="481" y="143" font-size="15" fill="#29485a">Revenue − COGS</text><path d="M 677 111 H 687" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow2)"/><rect x="694" y="39" width="206" height="145" rx="11" fill="#fff1e6" stroke="#8da4b7"/><text x="707" y="75" font-size="25" font-weight="700" fill="#163b4b">− €8 − €7</text><text x="707" y="106" font-size="14" font-weight="700" fill="#25465b">PRICE + PRODUCTION</text><text x="707" y="143" font-size="15" fill="#29485a">Differences / variance</text><path d="M 903 111 H 913" stroke="#365c79" stroke-width="2.5" fill="none" marker-end="url(#fin-arrow2)"/><rect x="920" y="39" width="206" height="145" rx="11" fill="#e9f6ed" stroke="#518b62"/><text x="933" y="75" font-size="25" font-weight="700" fill="#163b4b">= €85</text><text x="933" y="106" font-size="14" font-weight="700" fill="#25465b">ECONOMIC MARGIN</text><text x="933" y="143" font-size="15" fill="#29485a">Illustrative allocation</text>
    </svg>
  </div>
</figure>

In our **one-unit teaching case**, the operational standard gross margin is €250 − €150 = **€100**. If the entire €8 purchasing difference and €7 production variance economically belong to this single sold unit, the economic gross result would be **€85** before selling and administrative costs. This does **not** imply that standard CO-PA automatically reports €85 against this customer. Variances may remain on separate accounts or be allocated to different segments or periods, and actual costing may change valuation.

A careful Solution Architect asks whether the business wants **standard gross margin**, **actual-cost margin**, **contribution margin after selling expenses**, or **legal P&amp;L**. These are different definitions. Agree on account scope, cost allocations, reporting currency, segment derivation and timing before promising a dashboard.

### What is a profitability segment?

Think of market characteristics, not a new “bank account”. A segment can be made of customer, material, product group, region, sales organization, distribution channel and other characteristics supported by the design. Different journal lines can carry different characteristic completeness. A report filtered by customer may omit costs that were posted without that customer characteristic.

**Example:** COGS of €150 is assigned to the sold product and market segment, but a €7 production variance is booked without the final customer dimension. A product-level margin may reflect the variance while a customer-level view does not. The answer is not “CO-PA is broken”: trace the cost assignment, receiver and segment derivation.

### Revenue, COGS and cash happen at different times

For a typical sell-from-stock flow:

1. **Sales order:** a commercial promise; normally not yet revenue or an FI receivable.
2. **Post goods issue:** inventory reduces and COGS is posted in the standard baseline.
3. **Billing → accounting:** customer receivable and revenue are posted.
4. **Payment and clearing:** receivable becomes cash (or is otherwise cleared).

Special scenarios such as stock in transit, project-based revenue recognition, long-term service obligations, RAR and **event-based revenue recognition** change the timing or add adjustment entries. Do not project the above simple sequence onto every sales process. [SAP: forwarding billing to FI](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9da51938e0a54f708ebda0b1f44aff05/9c70b6535fe6b74ce10000000a174cb4.html) · [SAP: event-based revenue recognition](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f63dd39a28bb4b90adbf9e608aff58ea/7fd9ad1108b94403a2871cf348d4b891.html).

### SD price is not inventory cost

The sales pricing procedure produces commercial values: base price, discounts, surcharges, taxes and sometimes statistical cost data. A statistical cost condition may help a sales user see an estimated margin, but it is not a substitute for the **actual COGS journal** produced by valuation and goods issue. Discount condition determination and revenue account determination are also different decisions. For source and context, see the site's [SAP Pricing guide](/blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/) and [Sales Billing](/labs/enterprise-context/billing/).

## When the process is not the simple example

<div class="table-scroll study-table" role="region" aria-label="Cross-process finance integration variants" tabindex="0">
<table class="study-table__table"><thead><tr><th>Scenario</th><th>Where finance becomes important</th><th>Architectural question</th></tr></thead>
<tbody>
<tr><th scope="row">Stock procurement</th><td>Inventory valuation, GR/IR, price differences and supplier payable.</td><td>Is the purchase for inventory or direct consumption?</td></tr>
<tr><th scope="row">Account-assigned procurement</th><td>Cost center, order, WBS or asset may be the receiver instead of ordinary stock.</td><td>Which object will bear the cost, and at which receipt / invoice event?</td></tr>
<tr><th scope="row">Make-to-stock manufacturing</th><td>Standard cost, production-order actuals, finished-goods valuation, WIP and variance.</td><td>Should variances remain separate or affect actual inventory/COGS?</td></tr>
<tr><th scope="row">Make-to-order</th><td>Sales-order-related cost objects, special stock, settlement and revenue-recognition design.</td><td>Is sales-order stock valuated, and where is the margin recognized?</td></tr>
<tr><th scope="row">Outbound delivery / EWM</th><td>Physical warehouse tasks are not the same as inventory valuation postings.</td><td>Which exact movement posts goods issue, and is COGS created then?</td></tr>
<tr><th scope="row">Transportation / freight</th><td>Freight charge, accruals, service procurement, invoice verification and cost assignment.</td><td>Is freight part of inventory, COGS, selling expense or customer charge?</td></tr>
<tr><th scope="row">STO within one company code</th><td>Stock transfer valuation and stock-in-transit mechanics may apply; no ordinary external-customer sale is implied.</td><td>When and where does stock ownership / value change?</td></tr>
<tr><th scope="row">Cross-company STO / intercompany</th><td>Legal entities, intercompany billing, revenue, COGS, clearing and transfer pricing.</td><td>Which company owns which inventory, revenue and margin?</td></tr>
<tr><th scope="row">Third-party sales</th><td>Supplier fulfillment, purchasing / invoice process and customer billing may replace ordinary own-stock PGI.</td><td>What event creates COGS or expense, and how is customer profitability matched?</td></tr>
<tr><th scope="row">Customer returns</th><td>Credit memo, reversal or adjustment of sales, stock return and COGS valuation.</td><td>What original value and price should a return reverse?</td></tr>
<tr><th scope="row">Project / service delivery</th><td>WBS / service object costs, revenue recognition and settlement.</td><td>Is revenue recognized from billing, fulfillment, progress or another rule?</td></tr>
</tbody></table></div>

The correct architecture starts with **legal ownership, valuation, timing, cost object and reporting requirement**. Only then choose standard SAP processes, their account assignment and any justified extensions. A change to the logistics document flow can change accounting outcomes even when no FI configuration is touched.

## The configuration map: why the same document can post differently

A strong functional consultant does not need to memorize every FI customizing screen. But they do need to explain **which configuration decision changes the financial result** and who must validate it.

<div class="table-scroll study-table" role="region" aria-label="SAP master data and account determination dependency map" tabindex="0"><table class="study-table__table">
<thead><tr><th>Layer</th><th>Inputs to check</th><th>Financial consequence</th><th>Typical owner</th></tr></thead>
<tbody>
<tr><th scope="row">Legal and CO structure</th><td>Company code, controlling area, chart of accounts, ledger, accounting principle, currency, profit center.</td><td>Which entity and financial view own the value.</td><td>FI/CO.</td></tr>
<tr><th scope="row">MM valuation</th><td>Plant / valuation area, material valuation class, price control S/V, quantity, movement type, account assignment category.</td><td>Inventory vs consumption; value, stock account, GR/IR, price difference.</td><td>MM with FI/CO.</td></tr>
<tr><th scope="row">Purchasing document</th><td>PO price, delivery costs, supplier invoice, invoice-before-GR or GR-before-invoice sequence.</td><td>What is cleared and whether a price difference remains or changes inventory.</td><td>Purchasing with AP/FI.</td></tr>
<tr><th scope="row">Production costing</th><td>BOM, routing, work center, activity type / rate, costing variant, cost component structure, overhead and released estimate.</td><td>Planned cost, actual order debit and finished-goods valuation.</td><td>PP with CO-PC.</td></tr>
<tr><th scope="row">Period-end processing</th><td>WIP method, order status, variance logic, settlement rule and receiver, actual-costing activation.</td><td>Capitalized WIP, production differences, revaluation and profitability effects.</td><td>CO-PC with FI.</td></tr>
<tr><th scope="row">SD billing</th><td>Billing relevance, pricing conditions, account assignment groups, account determination, tax, payer / reconciliation account.</td><td>Revenue, deductions, customer receivable and tax posting.</td><td>SD with FI-AR.</td></tr>
<tr><th scope="row">Profitability analytics</th><td>Margin characteristics, cost account / COGS split, settlement assignment and reporting filters.</td><td>What customer, product or market appears to be profitable.</td><td>CO-PA / FP&amp;A with SD.</td></tr>
</tbody></table></div>

For classic SAP S/4HANA private / on-premise implementations, MM automatic account determination and SD revenue account determination are separate configuration domains. First reproduce the **value**. Then use the system's account determination analysis to see why the selected **G/L account** was derived. For an SD billing issue, SAP documents an account determination analysis that displays the relevant conditions, access sequence and keys. An MM goods movement uses inventory valuation and account determination rather than the SD sales-price procedure. Public Cloud configuration options and app navigation differ; do not blindly reuse classic GUI steps. [SAP: material valuation structure](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/585eb6531de6b64ce10000000a174cb4.html) · [SAP: billing account determination analysis](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/ee9cc353fad0b44ce10000000a174cb4.html) · [SAP: purchasing account assignment](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/cd7eb65334e6b54ce10000000a174cb4.html).

### Period-end close: why “real-time” has a limit

The journal can be current while the final **actual cost** is not yet known. In a representative production environment, the close may require the following controls. This is a dependency guide, not a fixed job sequence for every release or company:

1. Confirm that operational documents are posted in the correct period: goods receipts, component issues, activities, billing, supplier invoices and corrections.
2. Reconcile key open states such as GR/IR, stock differences, unprocessed confirmations and failed accounting transfers.
3. Post or allocate missing production activities and applicable overhead.
4. Determine and post WIP for unfinished cost objects under the chosen method.
5. Calculate variances and settle eligible completed production orders / product cost collectors.
6. If **Actual Costing** is active, calculate material actual prices, distribute eligible single- and multilevel differences and perform configured stock / consumption revaluation.
7. Run any required cost allocations, accruals or profitability adjustments in their approved order.
8. Reconcile FI accounts, production cost objects, Material Ledger and Margin Analysis using the same ledger, period, currency and reporting basis.
9. Close the period only after exceptions have named owners and documented treatment.

An architect should challenge the requirement **“final actual margin every minute”** if some cost inputs only arrive at month end. A better design may show **provisional operational margin now** and **closed actual margin after settlement**, with visible status and traceable adjustment postings. “Real-time” describes when information is available; it does not make an unknown supplier or manufacturing cost known in advance.

## A cross-module diagnostic method

Imagine Sales says: “Revenue is €250, but Finance says margin is too high.” Do not start by changing the sales price or forcing a CO-PA allocation.

**Trace the value in this order:**

1. **Agree the metric.** Is the complaint about SD estimated margin, a G/L gross margin report, Margin Analysis by customer, or an actual-cost P&amp;L report?
2. **Identify the exact object and period.** Company code, ledger, plant, product, customer, sales-order item, posting dates and reporting currency.
3. **Prove the logistics events.** PO history → goods receipt → invoice; manufacturing-order consumption and goods receipt; outbound PGI → billing.
4. **Prove the valuation.** Price control S/V, released cost estimate, quantity, cost component split, material ledger price determination, costing run status.
5. **Prove the journals.** Relevant G/L accounts, amounts, cost centers, orders, profit centers and market-segment characteristics.
6. **Find the temporary balances.** GR/IR, open production-order amount, WIP, variance, price difference, accrual and open receivable.
7. **Check period-end results.** Allocation, overhead, variance calculation, settlement, actual costing (if active), revaluation, reconciliation.
8. **Name the first wrong decision.** Quantity, value, account, account assignment, missing follow-on document, or a reporting definition mismatch.
9. **Repair in the owning process.** Reverse / repost / correct via supported business procedures. Do not hide a logistics error behind an arbitrary manual FI adjustment.
10. **Prove the recovery.** Reconcile the expected document chain, journal and margin report for one representative item before scaling.

### Where to inspect in S/4HANA

The exact SAP GUI transaction and Fiori app availability varies by deployment and role. Use the **business object** rather than relying only on a transaction name:

| Evidence | First object to inspect |
| --- | --- |
| Procurement mismatch | PO history, goods receipt, supplier invoice, GR/IR reconciliation. |
| Wrong stock value | Material valuation data, price control, material documents, accounting journals. |
| Wrong manufacturing cost | BOM / routing, cost estimate, manufacturing order costs and confirmations. |
| Open manufacturing amount | WIP, production variance, settlement rule / receiver, close status. |
| Wrong SD margin | Sales pricing versus actual billing, PGI / COGS journal, account assignment and margin characteristics. |
| Actual margin changed after period close | Actual-costing run and revaluation effects, if used; journal reconciliation. |
| Correct amounts in wrong reporting market | Profitability characteristic derivation, posting account assignment and report filters. |

### A decision record for an architect

Before approving a design, write down these seven choices:

1. Inventory and finished-goods valuation method.
2. Standard costing inputs, ownership and recalculation / release timing.
3. Production cost-object design and the sender/receiver of activities and overhead.
4. WIP, variance and settlement method; relevant period-end controls.
5. Revenue and COGS recognition points for every process variant.
6. Margin Analysis characteristics and what “actual margin” must include.
7. Reconciliation, authorization and operational evidence across FI, CO, MM, SD and PP.

Business should explicitly sign off on the **margin definition**. Without this, technically correct postings can still produce a dashboard that answers the wrong question.

## Practice and interview answer

### Exercise 1 — when is a PO an expense?

A buyer creates a purchase order for stock worth €5,000. No goods and no invoice have arrived. Does SAP post a normal stock expense immediately?

<details><summary>Check your answer</summary><p>Generally no in the standard stock procurement baseline. The PO is a commitment. The valuated goods receipt and invoice receipt are the accounting events, with the exact postings depending on price control and account assignment. Budget / commitment accounting is a separate design topic.</p></details>

### Exercise 2 — why is the production order not zero?

The order collected €157 and the completed finished-product receipt credited it by €150. What remains?

<details><summary>Check your answer</summary><p>€7 remains before the relevant variance / settlement processing. Investigate actual input costs, output, order status and settlement method. Do not assume all €7 automatically becomes the sold customer's COGS.</p></details>

### Exercise 3 — can two margin reports both be correct?

Billing shows €250, goods issue posted €150 COGS, purchasing recorded €8 price difference and manufacturing has €7 variance. One margin report shows €100. Another finance analysis suggests €85. Which is right?

<details><summary>Check your answer</summary><p>Both can describe different measures. €100 is standard gross margin. €85 is a teaching example of economic margin after attributing all €15 of differences to the single unit. Verify where differences were posted, which accounts and dimensions each report includes, whether revaluation occurred, and whether there is other inventory. Neither number should be called the final customer margin without a defined reporting basis.</p></details>

### Exercise 4 — a stronger architecture question

A customer demands: “We need real-time actual margin by sales order, including production, freight and purchase price differences.” What five questions must you ask before agreeing?

<details><summary>Suggested response</summary><p>Ask how the customer defines actual margin; which process variants and cost objects are involved; when purchasing, production and freight costs become known; which actual-costing / revaluation and revenue-recognition capabilities are in scope; and which line-item characteristics must be available for a sales-order report. Explain the difference between real-time provisional margin and final period-end actual margin. Recommend a clear accounting baseline, an agreed provisional measure, reconciled closing processes, and explicit exception handling before considering custom calculation.</p></details>

### A 90-second SAP Lead answer (B2 English)

> “I would start with the business event and follow its financial impact. In procurement, goods receipt normally updates inventory and the GR/IR account. The supplier invoice creates the payable and can also create price differences. In production, materials, activities and overhead are assigned to a manufacturing cost object. Finished-goods receipt values the output, while WIP and variances may require period-end processing.
>
> In sales, goods issue normally creates COGS and reduces inventory. Billing creates revenue and the customer receivable. Margin Analysis helps us understand the result by customer, product or market. However, standard margin and actual-cost margin are not always the same, because price differences, production variances and other allocations can be processed later.
>
> Before designing a solution, I would agree on valuation rules, the cost-object structure, posting timing, the margin definition and the reconciliation controls. Then I would test one end-to-end case with real accounting evidence.”

## Further reading and product boundaries

This guide deliberately starts with **one standard-price, make-to-stock process**. It is not a substitute for a signed FI/CO accounting design. Exact journal lines, available Fiori apps, costing methods, posting timing, ledger behavior and extensibility can differ by SAP S/4HANA release, activated scope, Public Edition versus Private Edition/on-premise, and local accounting rules. Corporate ledger, parallel currencies, transfer pricing, tax and revenue-recognition scenarios need their own validation.

**Primary SAP references (checked 30 October 2026):**

- [SAP — Controlling integration and the FI/CO account model](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/dfb64c53d5ec7d77e10000000a441470-2408.html).
- [SAP — Universal Journal and Margin Analysis (Cloud Public Edition 2608)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c0c54048d35849128be8e872df5bea6d/76c59195039142338af63e8a1a7c016f.html).
- [SAP — Postings at Goods Receipt and Invoice Receipt](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/825eb6531de6b64ce10000000a174cb4.html).
- [SAP — Material Price Control and Price Determination](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/5af1d353ca9f4408e10000000a174cb4.html).
- [SAP — Product Cost Components](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/82a6d7531a4d414de10000000a174cb4-2589.html).
- [SAP — WIP, Variances and Settlement (Cloud Public Edition)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4032610758dc437089f0c28320eec93f/a5787e40787a4b4eb7c8c69d1faeba38.html).
- [SAP — Production Settlement](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/5c35d85275c8d142e10000000a4450e5-2273.html).
- [SAP — Costing-Based CO-PA and Margin Analysis](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/9e33b3533ebb823de10000000a4450e5.html).
- [SAP — Splitting Cost of Goods Sold](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/2dd0c7548342b109e10000000a423f68.html).
- [SAP — Event-Based Revenue Recognition](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f63dd39a28bb4b90adbf9e608aff58ea/7fd9ad1108b94403a2871cf348d4b891.html).

**Continue in the Lab:** [FI/CO for Logistics](/labs/enterprise-context/finance-logistics/), [Procurement](/labs/enterprise-context/procurement/), [Production](/labs/enterprise-context/production/), [Sales Billing](/labs/enterprise-context/billing/) and [Order-to-Cash concept](/atlas/concepts/order-to-cash/).

{% include atlas/disclaimer.html %}
