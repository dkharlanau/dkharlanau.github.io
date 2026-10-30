---
layout: default
title: "SAP Financial Accounting Fundamentals: Accounts Payable and Receivable"
description: "A practical SAP S/4HANA FI introduction: assets, liabilities, debit and credit, AP, AR, GR/IR, payments, clearing, credit management, bank statements and the SD/MM connection."
permalink: /labs/enterprise-context/finance-logistics/financial-accounting-fundamentals/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-10-30
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-fi-co
  - sales-o2c
  - logistics-p2p
tags:
  - sap-s4hana
  - financial-accounting
  - accounts-payable
  - accounts-receivable
  - fi-ap
  - fi-ar
  - gr-ir
  - cash-management
  - clearing
  - credit-management
semantic_links:
  - type: parent_topic
    title: "FI/CO for Logistics"
    url: /labs/enterprise-context/finance-logistics/
  - type: related_topic
    title: "SAP Controlling Fundamentals"
    url: /labs/enterprise-context/finance-logistics/controlling-fundamentals/
  - type: deep_dive
    title: "Payments, Banks and Rejections"
    url: /labs/enterprise-context/finance-logistics/payments-banks-rejections/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/finance-logistics/">FI/CO for Logistics</a></li><li aria-current="page">Financial Accounting Fundamentals</li></ol></nav>

<header class="note-header">
  <p class="eyebrow">SAP S/4HANA / understand the money</p>
  <h1>Financial Accounting: who owes whom, and what changes when money moves?</h1>
  <p class="note-subtitle">A beginner-friendly bridge from Sales and Procurement to G/L, accounts receivable, accounts payable, payments and reconciliation.</p>
</header>

**Learning outcome.** You should be able to read a simple journal entry, explain why an invoice is not a payment, trace a supplier invoice through Accounts Payable (AP), trace a customer invoice through Accounts Receivable (AR), and find the first incorrect state when the reported balance does not match a business document.

**Scope and confidence.** The numerical examples are synthetic, use EUR, and first exclude VAT, withholding tax, exchange differences, discounts and special postings so the accounting logic stays visible. Actual tax rules, account determination, bank steps, payment programs and available Fiori apps depend on configuration, jurisdiction and S/4HANA edition/release. This is a source-backed learning draft awaiting human review.

## First, understand five everyday accounting words

| Word | Plain meaning | Example |
| --- | --- | --- |
| **Asset** | Something the company owns or has a right to collect | Stock, bank balance, customer receivable |
| **Liability** | Something the company must pay or deliver | Supplier payable, tax payable |
| **Revenue** | Income earned by selling goods or services | Revenue from a customer invoice |
| **Expense** | Cost recognized in the income statement | Cost of goods sold, rent |
| **Equity** | Residual interest after liabilities are subtracted from assets | Owners' capital and retained earnings |

**Accounting equation:** Assets = Liabilities + Equity. A transaction must keep this equation in balance.

**Income statement (P&L)** shows revenue and expense over a period. **Balance sheet** shows assets, liabilities and equity at a date. A supplier payable and a customer receivable are **balance-sheet positions**, not expenses or revenue by themselves.

### Debit and credit without memorizing complicated rules

A journal entry has a debit side (Dr) and a credit side (Cr). Total debit equals total credit. In a simple teaching model:

| Account group | Increases on | Decreases on |
| --- | --- | --- |
| Asset: bank, inventory, receivable | Debit | Credit |
| Expense: COGS, rent | Debit | Credit |
| Liability: supplier payable, tax payable | Credit | Debit |
| Revenue: sales | Credit | Debit |
| Equity | Credit | Debit |

**Example:** Receive an unpaid electricity invoice of €80 for a period expense: **Dr Electricity expense €80 / Cr Supplier payable €80**. Later pay it: **Dr Supplier payable €80 / Cr Bank €80**. The payment clears the debt; it does **not** recognize the expense a second time.

One more essential distinction: **profit is not cash**. A company can report revenue today but collect the money next month. It can buy inventory today but recognize COGS when that inventory is sold. This difference is the reason working capital matters.

## The two opposite sides: AP and AR

<figure aria-labelledby="fi-ap-ar-flow">
  <figcaption id="fi-ap-ar-flow"><strong>Figure 1.</strong> Supplier and customer transactions are mirror images, but purchase receipt and sales goods issue create different stock effects.</figcaption>
  <div class="table-scroll study-table" role="region" aria-label="Horizontal diagram comparing supplier Accounts Payable and customer Accounts Receivable" tabindex="0">
    <svg viewBox="0 0 930 212" role="img" aria-label="Top flow: Purchase order, goods receipt, supplier invoice, payable, outgoing payment, cleared liability. Bottom flow: Sales order, goods issue, customer invoice, receivable, incoming payment, cleared receivable." style="min-width:810px;width:100%;height:auto">
      <defs><marker id="fi-arw" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="#4c6778"/></marker></defs>
      <g stroke="#8093a2" stroke-width="1.5">
        <rect x="5" y="27" width="158" height="60" rx="9" fill="#eaf1f4"/><rect x="194" y="27" width="158" height="60" rx="9" fill="#eaf1f4"/><rect x="383" y="27" width="158" height="60" rx="9" fill="#eaf1f4"/><rect x="572" y="27" width="158" height="60" rx="9" fill="#eaf1f4"/><rect x="761" y="27" width="158" height="60" rx="9" fill="#eaf1f4"/>
        <rect x="5" y="123" width="158" height="60" rx="9" fill="#eef4e9"/><rect x="194" y="123" width="158" height="60" rx="9" fill="#eef4e9"/><rect x="383" y="123" width="158" height="60" rx="9" fill="#eef4e9"/><rect x="572" y="123" width="158" height="60" rx="9" fill="#eef4e9"/><rect x="761" y="123" width="158" height="60" rx="9" fill="#eef4e9"/>
      </g>
      <g fill="#173447" font-size="16" font-weight="650" text-anchor="middle">
        <text x="84" y="64">Purchase order</text><text x="273" y="64">Goods receipt</text><text x="462" y="64">Supplier invoice</text><text x="651" y="64">AP open item</text><text x="840" y="64">Payment / clear</text>
        <text x="84" y="160">Sales order</text><text x="273" y="160">Goods issue</text><text x="462" y="160">Customer billing</text><text x="651" y="160">AR open item</text><text x="840" y="160">Receipt / clear</text>
      </g>
      <g fill="none" stroke="#4c6778" stroke-width="2.5" marker-end="url(#fi-arw)">
        <path d="M165 57 H188"/><path d="M354 57 H377"/><path d="M543 57 H566"/><path d="M732 57 H755"/>
        <path d="M165 153 H188"/><path d="M354 153 H377"/><path d="M543 153 H566"/><path d="M732 153 H755"/>
      </g>
      <text x="8" y="18" font-size="14" fill="#315266">PROCURE TO PAY / LIABILITY</text>
      <text x="8" y="111" font-size="14" fill="#315266">ORDER TO CASH / RECEIVABLE</text>
    </svg>
  </div>
</figure>

**Accounts Payable (FI-AP)** answers: Which supplier do we owe, how much, when is it due, and what has been paid?

**Accounts Receivable (FI-AR)** answers: Which customer owes us, for which invoice, when is it due, and what have we collected?

Both are **subledgers**: detailed open items belong to a specific supplier or customer Business Partner. The related **reconciliation account** gives the G/L balance-sheet view. Normal supplier/customer postings update the relevant G/L reconciliation balances automatically; a user does not usually post directly to the reconciliation account to fix an invoice.

In S/4HANA, the Business Partner model combines the identity with role- and organization-specific data. A sold-to party, payer and billing recipient may differ. The customer that places an order is therefore not necessarily the **payer whose AR open item is affected**. Similarly, a purchasing supplier and an invoice/payee party may differ by process. Always inspect the actual accounting partner and company code, rather than guessing from the sales order header.

## AP explained: we buy first, pay later

Consider a stock purchase worth **€100**, without tax.

| Step | Business document and event | Simplified financial entry | Result |
| --- | --- | --- | --- |
| 1. Create purchase order | MM purchasing document | Usually no standard FI journal yet | A commercial commitment exists |
| 2. Post valuated goods receipt | Material document / PO history | Dr Inventory €100 / Cr GR/IR €100 | Stock increases; temporary GR/IR credit |
| 3. Post matched supplier invoice | Invoice verification + FI document | Dr GR/IR €100 / Cr Supplier payable €100 | Supplier debt exists; GR/IR is matched |
| 4. Pay the supplier | Payment / bank process | Dr Supplier payable €100 / Cr Bank or bank clearing €100 | AP open item is cleared under the applicable process |
| 5. Reconcile the bank | Bank statement and reconciliation | Clearing and bank accounts updated as designed | SAP posting matches actual bank activity |

The crucial middle account is **GR/IR (Goods Receipt / Invoice Receipt)**. At goods receipt, stock exists before a supplier invoice arrives. At invoice receipt, we match the invoice to received goods. Open GR/IR is not automatically wrong: it can represent a legitimate quantity or timing difference.

**Two AP differences that matter:**

- A **stock PO** often creates an inventory asset at valuated goods receipt. A **consumable or account-assigned PO** can produce an expense or cost-object effect instead. For a non-valuated receipt scenario, the accounting timing can move to invoice receipt.
- **Invoice verification blocked for payment**, a **parked invoice** and an **invoice not yet received** are different states. An invoice can already be posted as an AP liability while payment is blocked. Do not solve one by changing another.

### Why an approved purchase order is not a supplier payable

The PO says what we plan to buy. The goods receipt proves what arrived. The invoice says what the supplier claims we owe. The AP open item records the liability. The payment is a later settlement. A three-way check compares **PO, goods receipt and invoice** where that matching design applies.

If €100 was received but only €70 invoiced, investigate PO history, receipts, invoices, returns, quantity and currency before clearing the remaining GR/IR balance. Do not post a balancing entry merely to make the account look zero.

### How an outgoing payment actually reaches a bank

1. **Select** payable open items by due date, payment method, blocks and supplier/bank data.
2. **Propose and check** which items should be paid; correct exceptions and obtain approvals.
3. **Post the payment / create the payment instruction** according to the payment design. Some country-specific methods post at a different stage.
4. **Send and acknowledge** the payment file or instruction through the banking channel.
5. **Receive the bank statement** and reconcile cash or bank-clearing accounts. Handle rejected payments and reopen items when required.

A successful proposal is not a successful bank transfer. A posted SAP payment is not proof that the bank executed it. Follow [Payments, Banks and Rejections](/labs/enterprise-context/finance-logistics/payments-banks-rejections/) for the deeper operational model.

**Terms of payment** set baseline dates, due dates and possible cash-discount windows. **Payment method** decides how money is sent or collected. **Payment block** can prevent an item from entering the run. These controls may originate from BP master data, the purchasing document, the invoice or configuration. They do not mean the same thing.

## AR explained: we sell first, collect later

Now sell the finished product for **€180**, excluding tax. Assume the cost of the product in finished stock is **€100**.

| Step | Business event | Simplified financial entry | Result |
| --- | --- | --- | --- |
| 1. Create sales order | SD order | Usually no standard FI journal yet | Price, schedule and delivery requirements are set |
| 2. Post goods issue | Outbound delivery / material document | Dr COGS €100 / Cr Inventory €100 | Stock decreases; expense recognized in the baseline |
| 3. Transfer billing to FI | Customer billing + FI journal | Dr Customer receivable €180 / Cr Revenue €180 | Company earned revenue and is owed €180 |
| 4. Receive payment | Incoming payment / bank clearing | Dr Bank or bank clearing €180 / Cr Customer receivable €180 | Receivable clears when matched |
| 5. Reconcile | Customer open items and bank statement | No duplicate revenue entry | Check that bank and AR states agree |

**Gross margin here is €80 (180 − 100)** before other costs. **Cash collected after the invoice is €180**, but that does not mean profit is €180. The company may also have paid suppliers, salaries, taxes and freight at different times.

### Open items and clearing: the key AR concept

When billing posts €180, a **customer open item** is created. It remains open until the amount is cleared by payment, credit memo or another allowed clearing transaction. **Posting a bank receipt** and **matching it to the correct invoice** are related but not always identical steps.

Example: Customer invoice is **€500**. Customer sends **€200**.

| Treatment | Open-item result | Business consequence |
| --- | --- | --- |
| **Partial payment** | Original €500 invoice and €200 incoming payment remain as open items linked for tracking | Net outstanding amount is €300, but the old invoice remains open |
| **Residual item** | Original invoice and payment are cleared; a new €300 residual item remains | Aging and follow-up now operate on the new open item and its reference |
| **Payment on account** | Money is recorded for the customer without matching a specific invoice | Cash may be present while invoice clearing is unresolved |
| **Authorized discount / write-off** | Relevant difference posts to configured accounts | Financial result changes; requires policy, reason code and tolerances |

The choice is an **accounting and collections policy**, not a cosmetic document-status change. Do not post a difference to an expense account simply because the payment does not match.

### What if the customer does not pay?

- **Aging** groups receivables by due date and overdue period. It helps prioritize collections and identify overdue balances.
- **Dunning and Collections** coordinate reminders, contact and recovery according to configured policies.
- **Disputes** record why a customer withholds payment; do not assume every deduction is a genuine write-off.
- **Credit Management** considers credit exposure and risk. Depending on configuration and document stage, exposure can include open orders, deliveries, billing values and unpaid receivables. The **SD credit check** and **FI-AR open item** are different objects with a defined integration.
- **Credit memo** changes a customer claim by its own billing/accounting flow. A sales-order cancellation is not automatically equivalent to reversing an already posted customer receivable.

See [SAP Credit Management](/labs/enterprise-context/credit/) and [Sales Billing](/labs/enterprise-context/billing/) for the order-to-cash integration. For a delayed or absent billing accounting document, check SD accounting transfer status before changing customer credit data.

## Taxes: why the invoice amount is not always revenue or expense

Here is a **purely illustrative** sale with a 20% VAT rate (not a statement of the applicable rate or local tax rules):

- Goods or service net value: **€200**
- Illustrative output VAT: **€40**
- Total customer invoice: **€240**
- Simplified entry: **Dr Customer receivable €240 / Cr Revenue €200 / Cr Output VAT payable €40**

The customer owes €240, but **revenue is €200**, not €240. For a supplier invoice, deductible input tax, non-deductible tax, withholding and local accounting rules can produce different G/L lines. Do not infer tax behavior from this arithmetic; tax codes, jurisdiction and the actual document determine it.

## AP vs AR: the differences an architect must know

| Topic | AP: supplier side | AR: customer side |
| --- | --- | --- |
| Main business trigger | Supplier invoice, often tied to a PO/receipt | Customer billing transferred into FI |
| Open item | Amount we owe | Amount customer owes us |
| Balance-sheet type | Liability | Asset |
| Main settlement | Outgoing payment | Incoming payment, credit memo, offset |
| Operational exception | Invoice block, GR/IR mismatch, failed payment | Unmatched receipt, underpayment, overdue invoice, dispute |
| Master data focus | Supplier company-code/purchasing data, bank, payment terms | Customer company-code/sales-area data, payer, terms, credit data |
| Closest process | Procure-to-Pay (MM → FI-AP) | Order-to-Cash (SD → FI-AR) |
| Common management measure | Due payables, payment accuracy, DPO | Overdue AR, collection, DSO, bad debt |
| Risk of a careless shortcut | Paying duplicate or disputed invoices | Closing an open item that still needs collection |

**DSO (days sales outstanding)** is a rough measure of time to collect credit sales. **DPO (days payable outstanding)** estimates payment timing against credit purchases or a defined proxy. They are business indicators, not proof that individual invoices were cleared correctly. Define the denominator, time window, population and currency before comparing markets. Also watch **working capital**: inventory + receivables − payables (a simple operational approximation).

### A boundary that is easy to miss: FI-AR is not FI-CA

Standard customer open-item accounting (FI-AR) and **Contract Accounts Receivable and Payable (FI-CA)** are separate processing models. FI-CA is used in specific high-volume or contract-accounting scenarios and has its own document, clearing and integration patterns. Do not apply the same support steps or data assumptions without identifying the actual subledger.

## How Finance connects back to Controlling

A supplier invoice for electricity can create **Dr Expense / Cr Supplier payable**, with a cost center as its management assignment. Paying that invoice changes the **bank and payable**, not the original cost-center expense again.

A production order can receive **material consumption and internal activities** from MM/PP/CO. Finished-goods stock may later reach **COGS** through SD goods issue. Billing creates **revenue and AR**, while CO-PA/Margin Analysis can interpret revenue and COGS by business segment. This connection explains why an AP team, a plant controller and a sales manager can all look at one chain and ask different questions.

Continue with [Controlling Fundamentals](/labs/enterprise-context/finance-logistics/controlling-fundamentals/) and the [complete procurement-to-margin case](/atlas/concepts/sap-finance-controlling-from-procurement-to-margin/).

## Four failure scenarios worth practicing

| Symptom | Two plausible causes | Discriminating evidence | First owner |
| --- | --- | --- | --- |
| Supplier says invoice is unpaid | AP invoice has payment block; bank rejected a posted payment | AP open item, payment proposal/run, bank acknowledgement, statement | AP + Banking |
| Received stock is correct, but GR/IR remains | Invoice not posted; quantity or price mismatch | PO history, GR/IR account, invoice, reversals | MM Invoice Verification + FI |
| Customer paid, but invoice is overdue in SAP | Incoming cash not assigned; clearing failed / partial payment was used | Bank statement, incoming payment, customer line items, clearing document | AR + Cash Application |
| Customer credit check blocks a new order | Exposure is genuinely high; stale/unreconciled exposure or open items | Credit check log, exposure categories, FI-AR open items, update timing | Credit Management + SD + FI-AR |

**Diagnostic rule:** find the first state that differs between the business, subledger, G/L and bank. A bank balance, open-item status and customer credit exposure can be correct **at different moments**. Time and integration state matter.

## A simple period-end review

1. **AP:** Are all supplier invoices correctly posted, blocked or parked, and are payment cut-offs and open items understood?
2. **GR/IR:** Which unmatched receipts/invoices are legitimate timing differences? Which need investigation or approved correction?
3. **AR:** Do open items, due dates, disputes, credit memos and collections agree with the billing and receipt evidence?
4. **Bank:** Have statements arrived, are bank-clearing accounts reconciled, and are failed or rejected payments handled?
5. **Profitability:** Do revenue and COGS postings, inventory valuation, production settlement and the margin report use compatible period, currency and ledger logic?

Do not "zero" accounts just to make close easier. A controlled unreconciled item with a known cause and owner is better than an unsupported manual posting.

## Check your understanding

<details><summary>Case 1: We received €300 from a customer, but the revenue report did not increase. Is something broken?</summary><p>Not necessarily. If the invoice recognized revenue earlier, the receipt now clears the receivable. Check whether the payment was matched to the correct open item.</p></details>

<details><summary>Case 2: The PO is approved and the material arrived. Why is AP still zero?</summary><p>For the stock-PO baseline, goods receipt credits GR/IR; a supplier payable appears when the invoice is posted. Investigate the invoice status and account-assignment/valuation variant.</p></details>

<details><summary>Case 3: Supplier invoices are marked paid in SAP, but the bank rejected the file. Can we close the incident?</summary><p>No. The payment instruction, SAP accounting entry, bank outcome and reversal/reopen procedure must be reconciled. A successful SAP payment run alone is not proof of execution.</p></details>

<details><summary>Case 4: A customer owes €500, paid €200, and still has a €500 open invoice. Is this necessarily an error?</summary><p>No. That can be a partial-payment design: the €500 invoice and a €200 payment remain open while the net balance is €300. A residual-item design would clear the original and create a new €300 open item.</p></details>

### 45-second explanation (B2 English)

> “Accounts Payable tracks what we owe suppliers. Accounts Receivable tracks what customers owe us. A purchase order is not the same as a posted supplier invoice, and a customer invoice is not the same as collected cash. In Procurement, goods receipt can create inventory and a GR/IR balance. Supplier invoice creates a payable; payment clears it. In Sales, goods issue creates COGS, billing creates revenue and a receivable, and incoming payment clears that receivable. When a balance looks wrong, I would compare document flow, subledger items, bank evidence and G/L postings before changing master data or configuration.”

## SAP sources and further learning

Checked 30 October 2026 against SAP S/4HANA on-premise 2025 documentation and SAP S/4HANA Cloud Public Edition 2608 or current SAP Learning where noted. The process examples remain illustrative.

- [SAP Help — Accounts Receivable (FI-AR) and Accounts Payable (FI-AP)](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/4d3818c3010c2303e10000000a15822b.html).
- [SAP Help — Universal Journal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/523b8a55559ad007e10000000a44538d.html).
- [SAP Learning — Configuring Payment Terms and Cash Discounts](https://learning.sap.com/courses/customizing-core-settings-in-financial-accounting-in-sap-s4hana/configuring-payment-terms-and-cash-discounts).
- [SAP Learning — Running the Payment Program](https://learning.sap.com/courses/configuring-additional-settings-in-financial-accounting-in-sap-s-4hana/running-the-payment-program).
- [SAP Help — Clearing Process in AR](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/a21af993466648b994144cdd15ab1a39.html).
- [SAP Help — Partial Payments Versus Residual Items](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/279bad94d6414e05aab0cacf42eb3803.html).
- [SAP Help — Clear Incoming Payments](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a8aaa72cb39a48528b39b61623c15baa/340f87546ccd9c62e10000000a445394.html).
- [SAP Help — Credit Exposure Categories](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/4afbe04131d54863868d5afd7c6d6ba3.html).
- [SAP Help — Credit Check Process](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/4e63bf186cc943be821bc0b8be3557a6.html).

**Continue:** [FI/CO for Logistics](/labs/enterprise-context/finance-logistics/) · [Controlling Fundamentals](/labs/enterprise-context/finance-logistics/controlling-fundamentals/) · [Payments, Banks and Rejections](/labs/enterprise-context/finance-logistics/payments-banks-rejections/) · [Credit Management](/labs/enterprise-context/credit/).

This teaching guide does not replace tax advice, accounting policy or verification against the target system and company-code configuration.
