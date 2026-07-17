---
layout: blog
title: "SAP Pricing Explained: Sales, Procurement, Rebates, CPQ, Contracts, and the Right Solution for Each Business Model"
description: "Suppliers send invoices with additional freight and commodity surcharges that were not visible when the purchase order was created."
slug: sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the
permalink: /blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP solution architecture"
tags:
  - sap-solution-architecture
  - ai-operations
  - sap-sd
canonical_url: https://dkharlanau.github.io/blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 39
migration_sequence: 40
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/
  - /blog/your-atp-is-not-a-stock-check-how-sap-aatp-gatp-ibp-allocation-and/
---

## On this page

- [Pricing is a management system, not only a calculation](#pricing-is-a-management-system-not-only-a-calculation)
- [The vocabulary must be clear](#the-vocabulary-must-be-clear)
- [Sales-side values](#sales-side-values)
- [Procurement-side values](#procurement-side-values)
- [The SAP pricing landscape](#the-sap-pricing-landscape)
- [Part I: Sales pricing in SAP S/4HANA](#part-i-sales-pricing-in-sap-s-4hana)
- [The main components of the condition technique](#the-main-components-of-the-condition-technique)
- [Pricing-procedure determination](#pricing-procedure-determination)
- [Pricing date and validity](#pricing-date-and-validity)
- [Scales](#scales)
- [Header and item conditions](#header-and-item-conditions)
- [Group conditions](#group-conditions)
- [Statistical conditions](#statistical-conditions)
- [Requirements and formulas](#requirements-and-formulas)
- [Condition exclusion](#condition-exclusion)
- [Manual pricing](#manual-pricing)
- [Price copying and redetermination across documents](#price-copying-and-redetermination-across-documents)
- [Mass maintenance and pricing governance](#mass-maintenance-and-pricing-governance)
- [Where S/4HANA sales pricing is the right solution](#where-s-4hana-sales-pricing-is-the-right-solution)
- [Where core sales pricing becomes difficult](#where-core-sales-pricing-becomes-difficult)
- [Part II: Procurement pricing in SAP S/4HANA](#part-ii-procurement-pricing-in-sap-s-4hana)
- [Purchasing conditions](#purchasing-conditions)
- [Purchasing info record](#purchasing-info-record)
- [Purchasing contract](#purchasing-contract)
- [Scheduling agreement](#scheduling-agreement)
- [Supplier quotation and RFQ](#supplier-quotation-and-rfq)
- [Planned delivery costs](#planned-delivery-costs)
- [Price-unit and order-unit risks](#price-unit-and-order-unit-risks)
- [Indexed procurement prices](#indexed-procurement-prices)
- [Purchase-order price versus invoice price](#purchase-order-price-versus-invoice-price)
- [Purchase price variance](#purchase-price-variance)
- [Procurement pricing is connected to material valuation but is not the same](#procurement-pricing-is-connected-to-material-valuation-but-is-not-the-same)
- [Part III: Strategic procurement and SAP Ariba capabilities](#part-iii-strategic-procurement-and-sap-ariba-capabilities)
- [When strategic sourcing is needed](#when-strategic-sourcing-is-needed)
- [Source-to-contract versus procure-to-pay](#source-to-contract-versus-procure-to-pay)
- [Contract leakage](#contract-leakage)
- [Negotiated savings versus realized savings](#negotiated-savings-versus-realized-savings)
- [Contract lifecycle management](#contract-lifecycle-management)
- [Part IV: Customer and supplier rebates with Settlement Management](#part-iv-customer-and-supplier-rebates-with-settlement-management)
- [Immediate discount versus retrospective rebate](#immediate-discount-versus-retrospective-rebate)
- [Condition contract](#condition-contract)
- [Business volume](#business-volume)
- [Accrual](#accrual)
- [Partial and final settlement](#partial-and-final-settlement)
- [Sales and procurement rebates should not be managed only in spreadsheets](#sales-and-procurement-rebates-should-not-be-managed-only-in-spreadsheets)
- [Part V: SAP CPQ for complex quotations](#part-v-sap-cpq-for-complex-quotations)
- [When CPQ is appropriate](#when-cpq-is-appropriate)
- [CPQ responsibilities](#cpq-responsibilities)
- [CPQ should not become an isolated pricing island](#cpq-should-not-become-an-isolated-pricing-island)
- [ERP pricing versus CPQ pricing](#erp-pricing-versus-cpq-pricing)
- [Margin guardrails](#margin-guardrails)
- [Variant configuration](#variant-configuration)
- [Part VI: Subscription and usage-based pricing](#part-vi-subscription-and-usage-based-pricing)
- [When subscription pricing is appropriate](#when-subscription-pricing-is-appropriate)
- [Rating versus billing](#rating-versus-billing)
- [When not to introduce subscription billing](#when-not-to-introduce-subscription-billing)
- [Part VII: Which system should own the price?](#part-vii-which-system-should-own-the-price)
- [Recommended ownership model](#recommended-ownership-model)
- [The binding-price principle](#the-binding-price-principle)
- [Do not place core pricing logic in middleware](#do-not-place-core-pricing-logic-in-middleware)
- [Part VIII: Pricing governance](#part-viii-pricing-governance)
- [Price ownership](#price-ownership)
- [Validity governance](#validity-governance)
- [Price-change approval](#price-change-approval)
- [Four-eye principle](#four-eye-principle)
- [Simulation before activation](#simulation-before-activation)
- [Regression testing](#regression-testing)
- [Explainability](#explainability)
- [Part IX: Common pricing failures](#part-ix-common-pricing-failures)
- [Failure 1: Too many condition tables](#failure-1-too-many-condition-tables)
- [Failure 2: Customer-material prices everywhere](#failure-2-customer-material-prices-everywhere)
- [Failure 3: One pricing procedure per country or business request](#failure-3-one-pricing-procedure-per-country-or-business-request)
- [Failure 4: Unrestricted manual discounting](#failure-4-unrestricted-manual-discounting)
- [Failure 5: Cost-plus pricing using unreliable cost](#failure-5-cost-plus-pricing-using-unreliable-cost)
- [Failure 6: Quotation and order recalculate differently](#failure-6-quotation-and-order-recalculate-differently)
- [Failure 7: Sourcing award does not reach the purchase order](#failure-7-sourcing-award-does-not-reach-the-purchase-order)
- [Failure 8: Supplier invoice differences become normal](#failure-8-supplier-invoice-differences-become-normal)
- [Failure 9: Rebates are calculated outside the transaction landscape](#failure-9-rebates-are-calculated-outside-the-transaction-landscape)
- [Failure 10: Pricing logic duplicated in CPQ and ERP](#failure-10-pricing-logic-duplicated-in-cpq-and-erp)
- [Failure 11: AI recommendation becomes automatic authority](#failure-11-ai-recommendation-becomes-automatic-authority)
- [Failure 12: Procurement optimizes unit price only](#failure-12-procurement-optimizes-unit-price-only)
- [Part X: How to choose the right solution](#part-x-how-to-choose-the-right-solution)
- [Scenario 1: Standard B2B sales](#scenario-1-standard-b2b-sales)
- [Scenario 2: Complex engineered equipment](#scenario-2-complex-engineered-equipment)
- [Scenario 3: Strategic direct-material procurement](#scenario-3-strategic-direct-material-procurement)
- [Scenario 4: Annual customer rebate](#scenario-4-annual-customer-rebate)
- [Scenario 5: Supplier bonus](#scenario-5-supplier-bonus)
- [Scenario 6: SaaS or equipment subscription](#scenario-6-saas-or-equipment-subscription)
- [Scenario 7: Simple recurring service invoice](#scenario-7-simple-recurring-service-invoice)
- [Scenario 8: Price recommendation](#scenario-8-price-recommendation)
- [Solution-selection matrix](#solution-selection-matrix)
- [Part XI: Pricing analytics managers actually need](#part-xi-pricing-analytics-managers-actually-need)
- [Sales pricing metrics](#sales-pricing-metrics)
- [Procurement pricing metrics](#procurement-pricing-metrics)
- [Pricing-operation metrics](#pricing-operation-metrics)
- [Price waterfall](#price-waterfall)
- [Part XII: A practical pricing-transformation programme](#part-xii-a-practical-pricing-transformation-programme)
- [Phase 1: Define pricing domains](#phase-1-define-pricing-domains)
- [Phase 2: Identify price authorities](#phase-2-identify-price-authorities)
- [Phase 3: Map the price lifecycle](#phase-3-map-the-price-lifecycle)
- [Phase 4: Inventory existing logic](#phase-4-inventory-existing-logic)
- [Phase 5: Remove dead complexity](#phase-5-remove-dead-complexity)
- [Phase 6: Define target architecture](#phase-6-define-target-architecture)
- [Phase 7: Establish governance](#phase-7-establish-governance)
- [Phase 8: Build regression evidence](#phase-8-build-regression-evidence)
- [Phase 9: Pilot one pricing archetype](#phase-9-pilot-one-pricing-archetype)
- [Phase 10: Measure realized value](#phase-10-measure-realized-value)
- [Questions managers should ask](#questions-managers-should-ask)
- [The management conclusion](#the-management-conclusion)

A company has a pricing problem.

Sales says that SAP calculates the wrong price.

Procurement says that purchase prices do not match negotiated contracts.

Finance says that rebates are accrued incorrectly.

Commercial managers maintain discounts in spreadsheets.

Customer-specific prices are copied manually between systems.

Suppliers send invoices with additional freight and commodity surcharges that were not visible when the purchase order was created.

The company decides to implement a new pricing tool.

This may solve part of the problem.

It may also create another pricing engine that disagrees with SAP.

The main difficulty is that “pricing” is not one process.

It can mean:

- calculating the price of a sales order;
- negotiating a customer quote;
- determining a purchase-order price;
- selecting the best supplier bid;
- calculating retrospective rebates;
- pricing configurable equipment;
- charging recurring subscription fees;
- rating millions of usage events;
- calculating taxes, freight and surcharges;
- protecting margins during approval;
- forecasting the effect of future price changes.

SAP provides different solutions for these responsibilities.

The problem begins when a company expects one of them to perform all the others.

For example:

- SAP S/4HANA sales pricing is a strong transactional calculation engine, but it is not automatically a complete pricing-strategy platform.
- SAP CPQ can support complex quotations and discount guardrails, but it should not create a second uncontrolled price truth outside the ERP.
- SAP Strategic Procurement can support sourcing, negotiation and contracts, but the awarded price must still reach operational purchasing correctly.
- Condition Contract Management can calculate and settle later rebates, but it should not replace the immediate price of an invoice.
- SAP Subscription Billing supports one-time, recurring and usage-based charging, but it is unnecessary for a conventional sale of physical products.

The correct starting question is therefore not:

> Which SAP pricing solution should we implement?

It is:

> Which pricing decision are we trying to control, when is that decision made, who owns it, and where must it become financially binding?

## Pricing is a management system, not only a calculation

A price is the result of several different decisions.

### Commercial strategy

Management decides:

- market position;
- target margin;
- customer segmentation;
- discount philosophy;
- channel policy;
- product strategy;
- risk appetite.

### Price design

The organization translates the strategy into:

- list prices;
- customer prices;
- volume scales;
- discounts;
- surcharges;
- bundles;
- rebates;
- approval limits.

### Price execution

A system determines the price for a specific:

- customer;
- product;
- quantity;
- date;
- sales organization;
- purchasing organization;
- supplier;
- contract;
- channel.

### Price approval

Exceptions may require authorization based on:

- discount;
- gross margin;
- transaction value;
- customer segment;
- risk;
- strategic importance.

### Price settlement

Some financial effects are calculated later.

Examples include:

- annual customer rebate;
- supplier bonus;
- growth incentive;
- marketing contribution;
- freight reimbursement.

### Price analysis

Management reviews:

- price realization;
- margin;
- purchase-price variance;
- contract compliance;
- discount leakage;
- rebate exposure.

One solution rarely owns every layer.

A strong architecture connects them without duplicating responsibility.

## The vocabulary must be clear

Many pricing projects fail because people use the word “price” for different values.

## Sales-side values

### List price

The published or standard starting price.

It may not be the price most customers actually pay.

### Gross price

The initial product price before discounts and selected adjustments.

The exact meaning should be defined internally because organizations may use the term differently.

### Discount

A reduction based on factors such as:

- customer;
- product;
- quantity;
- promotion;
- agreement;
- sales channel.

### Surcharge

An increase for factors such as:

- small order;
- urgent delivery;
- fuel;
- packaging;
- raw-material movement;
- special handling.

### Net price

The transactional product price after relevant price conditions.

The company should define whether freight, taxes and later rebates are included when it reports “net price.”

### Net-net price

A management view that may subtract additional expected effects such as:

- retrospective rebates;
- promotional support;
- commissions;
- customer incentives.

This is often more useful for margin analysis than the invoice price alone.

### Invoice amount

The financial amount billed to the customer, potentially including:

- product price;
- freight;
- surcharges;
- tax;
- rounding.

### Pocket price

The amount the company effectively retains after all discounts, rebates, incentives and commercial leakage.

It is not normally one standard SAP field.

It is a management calculation that must be designed.

## Procurement-side values

### Quoted supplier price

The price offered during an RFQ or sourcing event.

### Contracted price

The price negotiated and recorded in a purchasing contract or equivalent agreement.

### Purchase-order price

The price used for the specific procurement transaction.

### Planned delivery cost

Expected freight, customs or other acquisition-related cost included or represented during purchasing.

### Invoice price

The amount invoiced by the supplier.

It may differ from the purchase order because of:

- quantity;
- price changes;
- freight;
- taxes;
- surcharges;
- currency;
- unit-of-measure differences.

### Effective purchase price

The amount after later supplier rebates, credits or retrospective conditions.

### Landed cost

The complete cost of making the goods available at the required location.

It may include:

- material price;
- inbound freight;
- customs;
- handling;
- insurance;
- duties;
- non-recoverable tax;
- quality and acquisition cost where included by company policy.

The purchase-order unit price is not automatically the landed cost.

### Cost of ownership

A wider management view that may include:

- quality failures;
- inventory;
- supplier variability;
- administration;
- disruption;
- obsolescence.

SAP purchasing conditions cannot by themselves calculate every strategic total-cost-of-ownership effect.

## The SAP pricing landscape

A practical way to understand SAP pricing is to divide it into six solution areas.

| Pricing responsibility | Primary SAP capability |
|---|---|
| Sales-order and billing price calculation | SAP S/4HANA Sales pricing |
| Operational purchase-order price calculation | SAP S/4HANA Sourcing and Procurement |
| Complex configuration and quotation | SAP CPQ |
| Strategic sourcing and negotiated procurement agreements | SAP Strategic Procurement / SAP Ariba capabilities |
| Retrospective customer and supplier settlement | SAP S/4HANA Settlement Management and Condition Contract Management |
| Subscription, recurring and usage-based monetization | SAP Subscription Billing and related quote-to-cash capabilities |

Additional industry and partner products may extend these areas.

The first architecture decision should be assigning ownership among these layers.

## Part I: Sales pricing in SAP S/4HANA

SAP S/4HANA Sales pricing uses the condition technique.

The term sounds technical.

The business idea is simple:

> Search for all price elements that apply to this transaction, calculate them in a controlled sequence, and produce the final price.

SAP’s official learning material describes sales pricing through condition types, condition records, condition tables, access sequences and pricing procedures. Condition types can use different calculation and scale bases, including percentage, fixed amount, quantity, weight, volume and time-based calculation.

## The main components of the condition technique

### Condition record

A condition record contains the actual business value.

Examples:

- product price: EUR 100;
- customer discount: 5%;
- freight: EUR 20;
- quantity discount: 3% from 100 units;
- fuel surcharge: EUR 0.10 per kilogram.

A condition record normally includes:

- key;
- validity period;
- rate;
- currency or unit;
- scale where applicable;
- additional control data.

Example:

```text
Sales organization: 1000
Customer: C10045
Material: M20010
Valid from: 2026-01-01
Valid to: 2026-12-31
Price: EUR 87.50 per piece
```

### Condition table

A condition table defines the fields making up the search key.

SAP’s training material explains that condition tables define the structure of condition-record keys.

Possible sales keys include:

- sales organization;
- distribution channel;
- customer;
- customer price group;
- material;
- material price group;
- country;
- destination;
- currency.

Examples:

```text
Customer + Material
```

```text
Price List + Currency + Material
```

```text
Customer Group + Material Group
```

The more specific the key, the more precise the price.

The more combinations created, the more difficult the pricing model becomes to maintain.

### Access sequence

An access sequence defines where and in which order SAP searches for a condition record.

SAP explains that an access sequence contains an ordered sequence of condition tables, allowing prices, discounts and surcharges to be defined at different levels.

A simplified price search might be:

1. customer and material;
2. customer price group and material;
3. price list and material;
4. general material price.

The system normally uses the first valid record found according to the configured logic.

This allows a pricing hierarchy:

> Use a specific agreement when it exists. Otherwise use a broader default.

### Condition type

The condition type defines what a price element means and how it behaves.

Examples include:

- base price;
- percentage discount;
- fixed discount;
- freight;
- surcharge;
- tax;
- statistical cost;
- rebate accrual.

The condition type can control items such as:

- calculation type;
- whether manual entry is permitted;
- whether the value is positive or negative;
- scale behaviour;
- access sequence;
- rounding;
- whether the condition is statistical;
- whether it affects the net value.

SAP’s official course states that the condition type determines the category and use of a condition and controls its calculation and scale bases.

### Pricing procedure

The pricing procedure defines the complete sequence of price elements.

A simplified procedure could be:

```text
Base price
– customer discount
– volume discount
+ packaging surcharge
+ freight
= net value before tax
+ tax
= invoice value
```

The procedure can also contain:

- subtotals;
- requirements;
- statistical values;
- account-relevant values;
- accrual conditions;
- formulas;
- minimum-price controls.

The pricing procedure is not just a visual list.

It is the transactional commercial policy executed by SAP.

## Pricing-procedure determination

SAP must determine which pricing procedure applies.

The determination can depend on organizational and document context.

Typical factors include:

- sales area;
- customer pricing classification;
- sales document pricing classification.

This allows different procedures for:

- domestic sales;
- export;
- intercompany;
- returns;
- free-of-charge processes;
- specific business models.

The design should keep the number of procedures controlled.

Creating a new pricing procedure for every commercial exception creates long-term complexity.

## Pricing date and validity

A transaction must determine which date is used to find valid pricing conditions.

Possible business dates may include:

- quotation date;
- order date;
- requested delivery date;
- contract date;
- billing date.

The correct choice depends on the commercial agreement.

For example:

- catalogue price valid at order entry;
- commodity price valid on delivery date;
- transport surcharge valid on shipment date;
- service price valid during the service period.

The pricing date should be treated as a business rule.

It should not be selected only because it is the easiest SAP default.

## Scales

A condition can change according to a scale.

Examples include:

### Quantity scale

```text
1–99 units: EUR 100
100–499 units: EUR 95
500+ units: EUR 90
```

### Value scale

```text
Order value below EUR 10,000: no discount
EUR 10,000–49,999: 2%
EUR 50,000+: 4%
```

### Weight scale

Useful for:

- freight;
- bulk products;
- raw materials.

### Time or period scale

Useful for selected service or rental scenarios.

SAP’s pricing model supports several scale-base and calculation types.

A scale should represent real commercial economics.

Do not create quantity discounts when larger quantities actually increase:

- packaging complexity;
- delivery splitting;
- inventory risk;
- special transport cost.

## Header and item conditions

An item condition applies to a specific item.

Examples:

- product price;
- material discount;
- item surcharge.

A header condition applies to the complete document and may be distributed across items.

Examples:

- overall order discount;
- document freight;
- manual commercial adjustment.

The distribution basis matters.

A EUR 1,000 document discount might be distributed by:

- item value;
- quantity;
- weight;
- another rule.

The choice affects:

- item margin;
- returns;
- partial billing;
- accounting;
- rebate calculations.

## Group conditions

A scale may need to consider several items together.

For example, a customer buys 600 units across three items in the same product group.

The organization may want the quantity scale to use the total 600 units rather than evaluate each item independently.

This requires deliberate group logic.

Poor design can create unexpected results when:

- items are split;
- units differ;
- returns occur;
- documents are partially billed.

## Statistical conditions

A statistical condition is calculated and displayed but does not necessarily alter the payable net value.

Typical uses may include:

- product cost;
- internal freight estimate;
- expected rebate;
- margin basis;
- reference price.

Statistical conditions are useful for decision support.

They can become dangerous when users assume a displayed statistical amount is financially posted or contractually binding.

The meaning must be documented.

## Requirements and formulas

A requirement controls when a price element applies.

Examples:

- export surcharge only for export documents;
- small-order surcharge only below a value threshold;
- special price only for a selected channel;
- manual discount only for selected document types.

Formulas can calculate:

- alternative base value;
- alternative condition amount;
- special rounding;
- margin;
- indexed price.

Custom formulas are powerful.

They are also one of the easiest ways to hide business logic inside technical pricing code.

A custom formula should have:

- business owner;
- written specification;
- test cases;
- change history;
- performance review;
- retirement decision.

## Condition exclusion

Several discounts may be technically valid at the same time.

The company may want to apply:

- only the best discount;
- only the first discount found;
- the best price among alternatives;
- one promotional discount but not another.

Condition-exclusion logic can prevent unintended stacking.

Without it, customers may receive:

- contract price;
- channel discount;
- campaign discount;
- manual discount;
- volume discount,

even when the commercial policy intended only one or two of them.

## Manual pricing

Sales users may need to enter or change conditions manually.

This can support:

- negotiated exception;
- one-time compensation;
- urgent competitive response;
- correction.

Manual pricing is also a major source of leakage.

Controls should include:

- permitted condition types;
- maximum discount;
- minimum margin;
- reason code;
- approval;
- user role;
- change log.

Do not solve every unusual sale by allowing unrestricted manual net-price changes.

## Price copying and redetermination across documents

A price can move through:

```text
Quotation
→ sales order
→ delivery
→ billing
```

The company must decide when prices are:

- copied unchanged;
- fully recalculated;
- partially recalculated;
- updated only for selected conditions.

Examples:

- contract price fixed at quotation acceptance;
- tax redetermined at billing;
- freight calculated after shipment;
- commodity surcharge updated on delivery.

This is one of the most important pricing design decisions.

A customer may believe that the quotation fixed the price.

SAP may be configured to redetermine parts of it later.

The commercial documents and SAP behaviour must agree.

## Mass maintenance and pricing governance

SAP supports maintenance and mass changes of condition records. SAP’s official course also describes creating new validity intervals by reference, mass changes, copying condition records and reviewing changes through change documents.

The technical ability to change thousands of prices quickly increases the need for governance.

A price change should include:

- owner;
- scope;
- effective date;
- approval;
- overlap check;
- simulation;
- sample transactions;
- rollback plan;
- customer-communication decision.

## Where S/4HANA sales pricing is the right solution

Use core transactional pricing when:

- products and price rules are reasonably structured;
- the final executable price must be calculated in the ERP;
- customer and product agreements fit condition-based logic;
- pricing must flow through order, billing and accounting;
- auditability and deterministic reproduction matter.

Examples:

- standard B2B product sales;
- customer-specific product prices;
- volume discounts;
- freight and surcharges;
- standard export pricing;
- structured channel pricing.

## Where core sales pricing becomes difficult

The condition technique becomes harder to manage when the business has:

- millions of highly individualized price agreements;
- complex interactive configuration;
- multi-year commercial proposals;
- subscription and usage pricing;
- frequent market-based price optimization;
- sophisticated promotional retail pricing;
- extensive external price dependencies;
- complex bundles crossing products, services and subscriptions.

This does not make condition technique obsolete.

It means the architecture may need another layer for a different pricing decision.

## Part II: Procurement pricing in SAP S/4HANA

Sales pricing asks:

> What should we charge the customer?

Procurement pricing asks:

> What do we expect to pay the supplier for this specific purchase?

The transactional concepts look similar, but the business process is different.

The procurement price may originate from:

- supplier quotation;
- purchasing info record;
- contract;
- scheduling agreement;
- catalogue;
- source list or selected source;
- manually negotiated purchase order;
- external sourcing solution.

The exact source and priority depend on the configured procurement process.

## Purchasing conditions

A purchase order may contain conditions for:

- gross material price;
- discount;
- surcharge;
- freight;
- customs;
- insurance;
- handling;
- other planned delivery costs.

The result may be a net purchase value and additional cost components.

The organization must decide whether each condition is:

- paid to the supplier;
- paid to another party;
- included in material value;
- posted separately;
- statistical;
- expected to change at invoice.

## Purchasing info record

A purchasing info record can store information related to the relationship between:

- supplier;
- material;
- purchasing organization;
- plant where relevant.

It may include:

- price;
- planned delivery time;
- order unit;
- supplier material reference;
- tolerance or control information.

An info record is useful for recurring supplier-material relationships.

It should not automatically override a strategic contract simply because its price was maintained more recently.

The source-of-price policy must be understood end to end.

## Purchasing contract

A purchasing contract defines a longer-term agreement with a supplier.

It may include:

- target quantity or value;
- validity;
- negotiated price;
- scales;
- terms;
- product or service scope.

Operational purchase orders can reference the contract.

This provides a link between:

- negotiation;
- agreement;
- consumption;
- purchase-order execution.

A contract creates value only when buyers and systems actually use it.

## Scheduling agreement

A scheduling agreement is useful when supply is recurring and delivery schedules are communicated against a longer-term agreement.

It may fit:

- automotive;
- repetitive manufacturing;
- direct-material supply;
- frequent replenishment.

Pricing can be maintained as part of the agreement structure.

The key management issue is ensuring that price validity aligns with:

- delivery schedule;
- goods receipt;
- invoice;
- commodity periods;
- retroactive changes.

## Supplier quotation and RFQ

For individual or periodic sourcing, buyers may request and compare supplier quotations.

The selected quotation can influence the purchase order.

This is appropriate for relatively bounded sourcing.

Large or strategic events may need a dedicated sourcing platform.

## Planned delivery costs

The lowest product price may not produce the lowest acquired cost.

A supplier may offer:

- lower material price;
- higher freight;
- longer lead time;
- customs exposure;
- more expensive packaging.

Planned delivery costs can improve the transactional view.

They still do not automatically provide a complete total-cost-of-ownership calculation.

## Price-unit and order-unit risks

A supplier may quote:

- EUR 1,000 per 100 pieces;
- USD 5 per kilogram;
- EUR 50 per case;
- price per litre.

SAP must correctly handle:

- price unit;
- order unit;
- base unit;
- conversion;
- currency.

Errors here can be severe.

For example:

```text
Supplier price: EUR 100 per 100 pieces
Incorrect interpretation: EUR 100 per piece
```

The purchase order may remain technically valid while its value is wrong by a factor of 100.

Controls should validate:

- unusual unit price;
- changed conversion;
- large variance from history;
- price-unit mismatch;
- unexpected currency.

## Indexed procurement prices

Direct-material agreements may use formulas based on:

- commodity index;
- energy;
- exchange rate;
- labour index;
- freight index.

A simplified model may be:

```text
Base conversion cost
+ commodity index component
+ energy surcharge
+ freight adjustment
```

The formula must define:

- index source;
- publication date;
- averaging period;
- currency;
- effective date;
- floor and ceiling;
- correction process.

This logic can sometimes be represented through purchasing conditions and formulas.

For highly complex agreements, specialized contract or price-management tooling may be required.

Do not hide a commercial index formula inside an undocumented spreadsheet and manually copy the result to SAP.

## Purchase-order price versus invoice price

The purchase order represents the expected commercial basis.

The supplier invoice represents the requested payment.

They may differ.

Possible causes include:

- price variance;
- quantity variance;
- unplanned delivery costs;
- changed tax;
- exchange rate;
- incorrect unit;
- supplier error;
- legitimate contract adjustment.

Invoice verification should not become a routine process of accepting every difference.

The organization should classify:

- valid variation;
- buyer error;
- master-data error;
- supplier non-compliance;
- contract gap;
- timing difference.

## Purchase price variance

Purchase-price variance can mean different things depending on the organization.

Possible comparisons include:

- standard cost versus purchase-order price;
- purchase-order price versus invoice price;
- old price versus new price;
- budget versus actual;
- contracted price versus purchase-order price.

The KPI must state its reference.

A favourable purchase-order variance may still be economically negative if the supplier creates:

- poor quality;
- excess inventory;
- delivery delays;
- premium transport.

## Procurement pricing is connected to material valuation but is not the same

A purchase price affects inventory and accounting.

Material valuation may use methods such as:

- standard price;
- moving average price;

depending on the product and accounting design.

But procurement pricing answers:

> What should this purchase transaction cost?

Material valuation answers:

> At what value should the material be represented for inventory and accounting purposes?

Confusing these two leads to poor analysis.

## Part III: Strategic procurement and SAP Ariba capabilities

Operational purchasing determines the price for a purchase order.

Strategic sourcing determines:

- which suppliers should compete;
- how bids should be evaluated;
- what should be awarded;
- which agreement should govern future buying.

SAP currently positions its Strategic Procurement solution as an integrated source-to-contract capability covering sourcing, contracting and supplier management. It includes RFI/RFP events, constraint-based optimization scenarios, event scoring, contract workflows and supplier qualification.

## When strategic sourcing is needed

Use a strategic sourcing solution when pricing depends on more than one simple supplier quotation.

Examples include:

- several suppliers and regions;
- multiple lots;
- volume allocation;
- capacity constraints;
- minimum award percentages;
- risk diversification;
- sustainability criteria;
- complex bid structures;
- multi-round negotiation.

The objective may not be:

> Award everything to the lowest bidder.

It may be:

> Minimize total cost while preserving capacity, quality, resilience and regional requirements.

## Source-to-contract versus procure-to-pay

These should be separated conceptually.

### Source-to-contract

Includes:

- spend and category analysis;
- sourcing strategy;
- RFI/RFP;
- bid evaluation;
- negotiation;
- contract authoring;
- approval.

### Procure-to-pay

Includes:

- requisition;
- source selection;
- purchase order;
- receipt;
- invoice;
- payment.

The awarded commercial result must move from source-to-contract into operational purchasing.

That handover is where value is often lost.

## Contract leakage

Contract leakage occurs when negotiated value is not realized.

Examples include:

- buyer uses a non-contracted supplier;
- wrong price reaches the purchase order;
- purchase occurs outside the contract;
- contract expires without replacement;
- quantity scale is not applied;
- supplier invoices additional unapproved charges;
- local buyer negotiates independently.

SAP’s strategic procurement offering explicitly emphasizes contract compliance and reducing contract leakage through integrated sourcing and contract management.

## Negotiated savings versus realized savings

A sourcing event may report:

```text
Old price: EUR 100
New awarded price: EUR 92
Expected saving: 8%
```

But actual value depends on:

- purchased volume;
- contract usage;
- mix;
- supplier capacity;
- freight;
- currency;
- invoice compliance;
- later rebates.

A complete savings model should track:

```text
Identified saving
→ negotiated saving
→ contracted saving
→ purchase-order saving
→ invoiced saving
→ realized financial impact
```

Do not declare success after the sourcing award.

## Contract lifecycle management

A procurement contract is more than a price.

It may govern:

- validity;
- liabilities;
- service levels;
- indexation;
- renewal;
- termination;
- volume commitment;
- confidentiality;
- compliance;
- payment terms.

SAP’s current Strategic Procurement offering includes contract authoring, clause libraries, workflows, approvals and collaboration with internal stakeholders and trading partners.

The commercial price should remain connected to the legal agreement.

Otherwise, SAP may calculate a technically valid price that no longer matches the current contract.

## Part IV: Customer and supplier rebates with Settlement Management

Some price effects are not known or settled during each individual invoice.

Examples include:

- annual-volume rebate;
- quarterly growth bonus;
- customer loyalty rebate;
- distributor incentive;
- supplier bonus;
- retrospective purchase discount;
- marketing contribution.

These are subsequent-settlement scenarios.

SAP’s Condition Contract Management provides a standardized solution for customer and supplier conditions that are settled later rather than directly with the source invoice. Condition contracts can define validity, settlement dates, eligible business volume, conditions, accruals and settlement.

## Immediate discount versus retrospective rebate

### Immediate discount

Applied directly to the sales or purchasing transaction.

Example:

```text
Base price: EUR 100
Immediate discount: 5%
Invoice price: EUR 95
```

### Retrospective rebate

Calculated based on accumulated business volume.

Example:

```text
Annual sales below EUR 1 million: 0%
EUR 1–2 million: 2%
Above EUR 2 million: 4%
```

The final rate may not be known until later.

The company may accrue the expected amount during the year and settle it later.

## Condition contract

A condition contract can represent:

- contract partner;
- validity period;
- eligible products or transactions;
- business-volume selection;
- rebate or settlement conditions;
- accrual conditions;
- settlement calendar;
- settlement method.

SAP states that Condition Contract Management supports customer and supplier contracts, accruals, partial and final settlement, corrections and contracts created retrospectively where required.

## Business volume

The rebate base may be calculated from eligible transactions.

Examples include:

- billing value;
- purchase value;
- quantity;
- selected products;
- selected customers;
- selected suppliers;
- organizational units;
- time period.

This is one of the most sensitive design areas.

A rebate may exclude:

- returns;
- taxes;
- freight;
- free goods;
- selected product groups;
- cancelled documents;
- intercompany transactions.

The business-volume rule must match the signed agreement.

## Accrual

An accrual represents the expected future obligation or receivable.

For a customer rebate:

- sales occur during the year;
- expected rebate cost is accrued;
- final settlement occurs later.

Without accruals, the company may overstate margin during the year and record a large adjustment at settlement.

SAP supports accrual posting from source documents or through delta-accrual settlement runs.

## Partial and final settlement

A contract may support:

- monthly settlement;
- quarterly settlement;
- partial settlement;
- final settlement;
- delta correction.

The design should define:

- which period is closed;
- whether later changes affect earlier periods;
- how returns are handled;
- how tax is calculated;
- how corrections are communicated.

## Sales and procurement rebates should not be managed only in spreadsheets

Spreadsheet rebate management creates risks:

- incomplete transaction population;
- outdated agreement version;
- incorrect scale;
- no accrual;
- duplicate settlement;
- missed obligation;
- weak audit.

A spreadsheet can support analysis.

The binding contract and settlement logic should be governed in a controlled system where the volume justifies it.

## Part V: SAP CPQ for complex quotations

SAP CPQ addresses a different problem from core order pricing.

It is designed for configuring, pricing and quoting complex offerings across sales channels.

SAP states that CPQ supports complex product configuration, customer- and channel-specific pricing, proposal generation, approval workflows, margin guardrails, discount controls and integration with CRM, commerce and ERP.

## When CPQ is appropriate

CPQ is valuable when the seller must combine:

- configurable hardware;
- services;
- software;
- subscriptions;
- optional components;
- complex dependencies;
- multi-year terms;
- one-time and recurring components.

Examples include:

- industrial machinery;
- vehicles;
- telecom solutions;
- technical services;
- software and hardware bundles;
- engineered products.

## CPQ responsibilities

A CPQ solution may support:

### Configure

Determine which product combinations are valid.

### Price

Apply commercial logic, customer context and discount guardrails.

### Quote

Generate a customer proposal and manage approval.

## CPQ should not become an isolated pricing island

The architecture must define where the following live:

- product definition;
- configuration rules;
- list price;
- customer agreement;
- cost;
- discount authority;
- final order price.

Possible model:

```text
Product and configuration model
→ CPQ quotation
→ approved commercial terms
→ ERP sales order
→ billing and accounting
```

The approved quote should transfer to ERP with enough context to reproduce and explain the price.

## ERP pricing versus CPQ pricing

### ERP pricing is strongest when

- the transaction is already structured;
- price rules are deterministic;
- billing and accounting integration are central;
- the order is the commercial execution point.

### CPQ pricing is strongest when

- the offer is still being assembled;
- configuration is complex;
- many alternatives are compared;
- approval is interactive;
- a proposal document is required;
- margin guardrails guide the seller.

The company may use both.

The rule should be:

> CPQ creates the approved offer. ERP executes the accepted commercial commitment.

Do not independently recalculate the final price in both systems without defined reconciliation.

## Margin guardrails

SAP CPQ describes capabilities for product, customer and channel price controls, rules-driven discount eligibility, minimum-margin protection and approval workflows.

A good margin-control process may include:

- target margin;
- minimum margin;
- discount threshold;
- approval level;
- deal reason;
- strategic exception.

The cost used in the margin calculation must be governed.

An outdated or incomplete cost creates false protection.

## Variant configuration

SAP CPQ can leverage existing variant-configuration models and ERP data for complex quote processes.

This can reduce duplication.

But sales configuration, engineering configuration and manufacturing configuration may not be identical.

The organization should define:

- one product-model authority;
- permitted channel simplification;
- release synchronization;
- pricing-feature ownership.

## Part VI: Subscription and usage-based pricing

Conventional sales pricing assumes a relatively direct transaction:

```text
Product × Quantity × Price
```

Subscription and usage models may require:

- recurring monthly fee;
- one-time activation fee;
- usage charge;
- tiered usage;
- minimum commitment;
- bundle;
- contract change;
- renewal;
- proration;
- entitlement.

SAP Subscription Billing is positioned for one-time, recurring and usage-based fees, flexible contract changes, real-time or offline rating, bundles and integrated quote-to-cash processes.

## When subscription pricing is appropriate

Examples include:

- software subscriptions;
- equipment-as-a-service;
- connected products;
- digital services;
- membership;
- recurring maintenance;
- usage-based industrial service.

## Rating versus billing

These terms should be separated.

### Rating

Calculates a monetary charge from usage.

Example:

```text
First 1,000 units: included
Next 9,000 units: EUR 0.05 each
Above 10,000 units: EUR 0.03 each
```

### Billing

Aggregates charges and creates the bill.

### Invoicing

Produces the legal or customer-facing invoice.

### Receivables

Tracks the amount due and payment.

Simple SD pricing can support some recurring arrangements.

High-volume or complex usage models may need Subscription Billing or BRIM-related capabilities.

## When not to introduce subscription billing

Do not introduce a specialized subscription platform for:

- annual customer price lists;
- simple recurring invoices;
- ordinary product sales;
- one small service charge,

unless the lifecycle and scale justify it.

The additional platform creates:

- integration;
- product-model governance;
- rating reconciliation;
- billing reconciliation;
- support cost.

## Part VII: Which system should own the price?

A strong pricing architecture assigns each decision explicitly.

## Recommended ownership model

### SAP S/4HANA Sales

Owns:

- executable sales-order price;
- billing-relevant pricing elements;
- taxes and transactional charges where configured;
- deterministic customer-product agreements;
- accounting-relevant result.

### SAP S/4HANA Procurement

Owns:

- executable purchase-order conditions;
- expected supplier transaction price;
- planned delivery costs;
- operational contract reference;
- invoice-verification basis.

### SAP CPQ

Owns:

- interactive quote configuration;
- seller guidance;
- quote-level commercial proposal;
- discount and margin approval;
- proposal documentation.

### SAP Strategic Procurement

Owns:

- sourcing event;
- supplier bid;
- negotiation;
- award scenario;
- commercial contract lifecycle;
- supplier selection.

### Settlement Management

Owns:

- subsequent settlement;
- rebate business volume;
- accrual;
- partial and final settlement.

### Subscription Billing or BRIM-related architecture

Owns:

- subscription lifecycle;
- recurring and usage price model;
- rating;
- high-volume monetization.

### Analytical and AI platform

May own:

- recommendation;
- simulation;
- elasticity analysis;
- anomaly detection;
- margin analysis.

It should not silently become the binding transaction-price authority.

## The binding-price principle

Every business process should define one binding price at each stage.

For example:

```text
Recommended price
→ quoted price
→ approved price
→ ordered price
→ invoiced price
→ settled effective price
```

Differences may be legitimate.

They should be visible and explainable.

## Do not place core pricing logic in middleware

An integration flow may technically:

- read price from one system;
- add customer logic;
- convert currency;
- override discount;
- send a new price to SAP.

This is usually weak architecture.

Middleware may perform technical translation.

It should not become the only place where commercial pricing policy exists.

Pricing needs:

- owner;
- validity;
- approval;
- audit;
- simulation;
- reproducibility.

Integration scripts are poor pricing-governance systems.

## Part VIII: Pricing governance

The condition technique is flexible.

Flexibility without governance becomes commercial debt.

## Price ownership

Every price element should have an accountable owner.

Examples:

| Price element | Owner |
|---|---|
| Product list price | Product or commercial management |
| Customer contract price | Account management with pricing authority |
| Freight surcharge | Logistics or commercial policy |
| Commodity index | Procurement or product pricing |
| Manual deal discount | Sales authority |
| Tax | Tax function |
| Supplier price | Procurement category owner |
| Customer rebate | Commercial finance |
| Supplier rebate | Procurement finance |

The SAP team should implement the policy.

It should not become the owner of commercial meaning.

## Validity governance

Condition records normally have validity periods.

Common problems include:

- overlapping records;
- gaps;
- expired prices;
- future prices entered incorrectly;
- wrong currency;
- wrong unit;
- copied records with old dates.

Controls should detect:

- overlap;
- missing future price;
- unusual change;
- invalid unit;
- large percentage movement;
- unapproved backdating.

## Price-change approval

Not every price change needs executive approval.

Use risk-based thresholds.

Possible factors include:

- number of customers affected;
- revenue or spend;
- margin impact;
- percentage change;
- retrospective effect;
- regulated product;
- strategic customer;
- high-risk supplier.

## Four-eye principle

High-impact price changes may require:

- preparer;
- approver;
- effective-date confirmation;
- post-activation verification.

The same person should not be able to:

- create;
- approve;
- activate;
- verify

a major pricing change without control.

## Simulation before activation

A price-change simulation should estimate:

- affected customers or suppliers;
- affected products;
- expected revenue or spend;
- margin impact;
- open quotations or orders;
- existing contracts;
- rebate interaction.

Do not discover the commercial effect from the first production order.

## Regression testing

A pricing test pack should include:

- standard customer;
- contract customer;
- export;
- different currencies;
- quantity scales;
- free goods where used;
- returns;
- credit and debit adjustments;
- tax;
- freight;
- manual discounts;
- billing redetermination;
- procurement contract;
- supplier invoice variance;
- rebate settlement.

For each case, preserve:

- input;
- expected conditions;
- expected net result;
- accounting result where relevant.

## Explainability

A user should be able to answer:

- which price was found;
- which key found it;
- which discounts applied;
- which records were rejected;
- why another price was not used;
- which manual changes occurred;
- which approval applies.

Pricing that cannot be explained cannot be governed.

## Part IX: Common pricing failures

## Failure 1: Too many condition tables

Every new exception creates a new table.

The access sequence becomes long and difficult to analyse.

Better approach:

- define a deliberate pricing hierarchy;
- use groups and classifications where appropriate;
- avoid unique keys for every local request.

## Failure 2: Customer-material prices everywhere

Customer-specific prices are easy to understand.

At scale they produce:

- millions of records;
- duplicated maintenance;
- slow change;
- inconsistent validity;
- poor segmentation.

Use customer-specific pricing where the contract genuinely requires it.

Use broader price groups where the commercial meaning is shared.

## Failure 3: One pricing procedure per country or business request

The procedures diverge.

Improvements and corrections must be repeated.

Prefer shared procedures with controlled conditions and requirements where practical.

## Failure 4: Unrestricted manual discounting

Sales users bypass:

- price policy;
- margin control;
- agreement;
- approval.

Manual conditions should be explicit exceptions.

## Failure 5: Cost-plus pricing using unreliable cost

The system protects a margin calculated from:

- old standard cost;
- incomplete freight;
- missing service effort;
- wrong currency.

A technically correct margin can still be economically false.

## Failure 6: Quotation and order recalculate differently

The customer accepts one price.

The ERP creates another.

The organization must define:

- binding document;
- copied conditions;
- permitted redetermination.

## Failure 7: Sourcing award does not reach the purchase order

Procurement reports savings.

Buyers continue using old prices or suppliers.

The organization needs contract and price handover controls.

## Failure 8: Supplier invoice differences become normal

Invoice processors repeatedly accept:

- freight;
- surcharge;
- price changes.

The purchase-order price loses meaning.

Recurring variance should update:

- contract;
- master data;
- sourcing;
- supplier performance.

## Failure 9: Rebates are calculated outside the transaction landscape

Finance cannot prove:

- eligible volume;
- scale;
- accrual;
- payment.

## Failure 10: Pricing logic duplicated in CPQ and ERP

Both systems calculate independently.

Small differences create:

- order blocks;
- manual corrections;
- customer disputes.

## Failure 11: AI recommendation becomes automatic authority

A model recommends a price based on historical behaviour.

The price is activated without:

- floor;
- margin;
- fairness review;
- approval;
- experiment design.

AI should support pricing decisions.

It should not bypass pricing governance.

## Failure 12: Procurement optimizes unit price only

The selected supplier creates:

- more inventory;
- more freight;
- worse quality;
- disruption.

## Part X: How to choose the right solution

## Scenario 1: Standard B2B sales

Requirements:

- customer and product prices;
- discounts;
- scales;
- freight;
- tax;
- billing.

Recommended core:

> SAP S/4HANA Sales pricing.

Add CPQ only when quotation complexity justifies it.

## Scenario 2: Complex engineered equipment

Requirements:

- configurable product;
- dependencies;
- optional services;
- proposal;
- margin approval.

Recommended architecture:

```text
Product and configuration authority
→ SAP CPQ
→ approved quote
→ SAP S/4HANA order and billing
```

## Scenario 3: Strategic direct-material procurement

Requirements:

- supplier competition;
- several lots;
- capacity allocation;
- negotiated contract;
- operational purchase orders.

Recommended architecture:

```text
SAP Strategic Procurement
→ sourcing award and contract
→ S/4HANA purchasing agreement
→ purchase order
→ invoice verification
```

## Scenario 4: Annual customer rebate

Requirements:

- eligible sales volume;
- scale;
- accrual;
- quarterly and final settlement.

Recommended core:

> SAP S/4HANA Condition Contract Management and Settlement Management.

## Scenario 5: Supplier bonus

Requirements:

- purchasing volume;
- later credit or settlement;
- accrual;
- supplier agreement.

Recommended core:

> Condition Contract Management, configured for the applicable purchasing scenario.

## Scenario 6: SaaS or equipment subscription

Requirements:

- recurring fee;
- usage;
- contract change;
- renewal;
- rating.

Recommended architecture:

> SAP Subscription Billing or a broader BRIM-style quote-to-cash architecture, depending on scale and complexity.

## Scenario 7: Simple recurring service invoice

Requirements:

- fixed recurring amount;
- limited lifecycle complexity.

Possible solution:

> Standard ERP contracts and billing may be sufficient.

Do not introduce a high-complexity monetization platform unnecessarily.

## Scenario 8: Price recommendation

Requirements:

- elasticity;
- market signals;
- recommended discount;
- simulation.

Recommended architecture:

```text
Analytical or optimization capability
→ recommendation
→ approval
→ governed condition or quote
→ S/4HANA execution
```

The recommendation engine should not become an invisible transactional price source.

## Solution-selection matrix

| Business need | S/4 Sales Pricing | S/4 Procurement | SAP CPQ | Strategic Procurement | Settlement Management | Subscription Billing |
|---|---:|---:|---:|---:|---:|---:|
| Standard customer price | Strong | No | Possible | No | No | Limited |
| Purchase-order price | No | Strong | No | Source | No | No |
| Complex configurable quote | Limited | No | Strong | No | No | Possible component |
| Supplier sourcing event | No | Limited | No | Strong | No | No |
| Immediate discount | Strong | Strong | Strong at quote | Negotiated source | No | Strong for subscriptions |
| Annual rebate | Limited immediate use | Limited immediate use | No | Contract source | Strong | Possible for subscription adjustments |
| Accrual and later settlement | No as main solution | No as main solution | No | No | Strong | Different use |
| Usage rating | Weak | No | Possible quote input | No | No | Strong |
| Proposal document | Limited | No | Strong | Sourcing documents | No | No |
| Invoice and accounting integration | Strong | Strong | Through ERP | Through ERP | Strong | Integrated quote-to-cash architecture |

## Part XI: Pricing analytics managers actually need

A price engine calculates transactions.

Management needs to understand performance.

## Sales pricing metrics

- list-to-net discount;
- price realization;
- manual-condition rate;
- average discount by customer;
- margin by product and channel;
- override rate;
- price-expiry exposure;
- quote-to-order price variance;
- order-to-invoice price variance;
- rebate-adjusted margin.

## Procurement pricing metrics

- contracted versus ordered price;
- ordered versus invoiced price;
- purchase-price variance;
- contract-compliance rate;
- spot-buy rate;
- unplanned-delivery-cost rate;
- price-unit error rate;
- sourcing-award realization;
- supplier-rebate recovery.

## Pricing-operation metrics

- condition records without owner;
- overlapping validity records;
- emergency price changes;
- approval cycle time;
- failed price loads;
- unexplained manual changes;
- pricing incidents;
- time to explain a disputed price.

## Price waterfall

A sales price waterfall can show:

```text
List price
– standard discount
– customer discount
– promotional discount
– manual discount
+ surcharge
= invoice product price
– expected rebate
– commission
= pocket price
```

A procurement waterfall can show:

```text
Quoted material price
– negotiated discount
+ freight
+ customs
+ surcharge
– supplier rebate
= effective landed purchase price
```

These views reveal where value is lost.

## Part XII: A practical pricing-transformation programme

## Phase 1: Define pricing domains

Separate:

- sales transaction pricing;
- procurement transaction pricing;
- sourcing;
- quotation;
- rebates;
- subscription;
- tax;
- freight.

## Phase 2: Identify price authorities

For every price element, record:

- business owner;
- system;
- approval;
- effective date;
- downstream consumers.

## Phase 3: Map the price lifecycle

For sales:

```text
Strategy
→ list price
→ quote
→ order
→ billing
→ rebate settlement
→ margin
```

For procurement:

```text
Sourcing
→ contract
→ purchase order
→ goods receipt
→ invoice
→ supplier settlement
→ effective cost
```

## Phase 4: Inventory existing logic

Include:

- condition types;
- condition tables;
- access sequences;
- pricing procedures;
- formulas;
- manual conditions;
- custom code;
- spreadsheets;
- CPQ rules;
- procurement contracts;
- rebate agreements.

## Phase 5: Remove dead complexity

Identify:

- unused condition types;
- obsolete tables;
- duplicate records;
- expired agreements;
- unused formulas;
- redundant procedures.

## Phase 6: Define target architecture

Decide which responsibility belongs to:

- S/4HANA;
- CPQ;
- Ariba or Strategic Procurement;
- Settlement Management;
- Subscription Billing;
- analytics or AI.

## Phase 7: Establish governance

Implement:

- owners;
- validity checks;
- approvals;
- simulation;
- audit;
- emergency-change process.

## Phase 8: Build regression evidence

Create a golden pricing dataset.

## Phase 9: Pilot one pricing archetype

Examples:

- one sales organization and product family;
- one procurement category;
- one rebate type;
- one CPQ product family.

## Phase 10: Measure realized value

Do not stop at technical correctness.

Measure:

- sales margin;
- contract compliance;
- invoice variance;
- rebate accuracy;
- manual effort;
- price-explanation time.

## Questions managers should ask

1. What do we mean by price in each process?
2. Which price is binding?
3. Who owns the list price?
4. Who may change a customer-specific price?
5. Which discounts can be combined?
6. Which date determines the valid price?
7. When may quotation pricing be recalculated?
8. How are freight and surcharges represented?
9. Are later rebates included in margin analysis?
10. Which purchase price was negotiated?
11. Does the purchase order use that price?
12. Why does the supplier invoice differ?
13. Do we measure landed cost or only unit price?
14. Which rebate agreements exist outside SAP?
15. Are rebate accruals complete?
16. Is CPQ reproducing ERP pricing or creating another version?
17. Which system owns product-configuration rules?
18. Do subscription scenarios really require a specialized platform?
19. Which prices are recommendations and which are authoritative?
20. Can every disputed price be reproduced and explained?
21. How many manual price changes occur?
22. Which price records overlap or expire soon?
23. Do sourcing savings become actual invoice savings?
24. Is AI operating inside margin and approval guardrails?
25. Are we solving pricing strategy, calculation or settlement?

## The management conclusion

SAP pricing is not one engine.

It is a portfolio of capabilities designed for different moments in the commercial lifecycle.

SAP S/4HANA condition technique is the foundation for deterministic transactional pricing in sales. SAP’s model uses condition tables, access sequences, condition types, condition records and pricing procedures to determine prices, discounts, surcharges and other values.

SAP S/4HANA procurement provides the operational price for purchasing transactions through supplier agreements, purchasing master data and document conditions.

SAP CPQ supports configuration, pricing, proposal generation, discount guardrails and approvals for complex quotations.

SAP Strategic Procurement supports sourcing events, bid evaluation, contract lifecycle management and supplier management before operational purchasing.

Condition Contract Management supports customer and supplier conditions that require later accrual and settlement.

SAP Subscription Billing supports recurring, one-time and usage-based monetization where ordinary order pricing is no longer sufficient.

The company does not need every solution.

It needs a pricing architecture where each solution has a bounded role.

The decisive test is:

> Can the organization explain who decided the price, which agreement and data produced it, why it changed, how it became financially binding, and whether the expected margin or saving was actually realized?

When the answer is clear, pricing is controlled.

When several systems calculate plausible but different answers, the company does not have advanced pricing.

It has several competing versions of commercial truth.

---

### SAP pricing architecture checklist

- [ ] Pricing strategy and transactional calculation are separated.
- [ ] Sales, procurement, sourcing, rebates and subscriptions are treated as different domains.
- [ ] Every price element has a business owner.
- [ ] Binding and recommended prices are distinguished.
- [ ] List, net, net-net, invoice and pocket prices are defined.
- [ ] Purchase-order price, invoice price, landed cost and total cost are distinguished.
- [ ] Condition tables reflect a controlled pricing hierarchy.
- [ ] Access sequences do not contain unnecessary searches.
- [ ] Condition types have documented commercial meaning.
- [ ] Pricing procedures are consolidated where practical.
- [ ] Validity overlaps and gaps are detected.
- [ ] Scales reflect real commercial economics.
- [ ] Manual pricing has limits, reason and approval.
- [ ] Condition exclusion prevents unintended discount stacking.
- [ ] Custom formulas have owners and tests.
- [ ] Quotation-to-order and order-to-billing repricing rules are explicit.
- [ ] Purchasing prices reference approved sources and contracts.
- [ ] Units, price units and currencies are controlled.
- [ ] Planned delivery costs are visible.
- [ ] Supplier invoice differences are classified and corrected at source.
- [ ] Strategic sourcing awards flow into operational procurement.
- [ ] Negotiated and realized savings are measured separately.
- [ ] Customer and supplier rebates use governed business volume.
- [ ] Accruals are reconciled before final settlement.
- [ ] CPQ and ERP have a defined price handover.
- [ ] Configuration rules have one lifecycle authority.
- [ ] Subscription pricing is used only where lifecycle complexity justifies it.
- [ ] Middleware does not own core commercial pricing logic.
- [ ] AI provides recommendations inside explicit guardrails.
- [ ] Golden test cases prove the pricing result.
- [ ] Managers can trace price from strategy through financial outcome.

### Sources and further reading

SAP’s official pricing course for SAP S/4HANA Sales covers condition technique, pricing configuration, condition records, special pricing functions, tax determination and Condition Contract Management.

SAP explains that condition tables define condition-record keys and that access sequences specify the ordered condition tables searched for valid prices, discounts and surcharges.

SAP’s learning content describes condition-record maintenance, validity changes, mass updates, copying rules, release processing and change-document monitoring.

SAP describes Condition Contract Management as a standardized solution for customer and supplier conditions settled after the original logistics transaction, supporting business-volume determination, accruals, partial and final settlement and retrospective agreements.

SAP currently positions SAP CPQ for complex configuration, customer- and channel-specific pricing, proposal generation, margin protection, discount guardrails and integration with CRM, commerce and ERP.

SAP currently positions Strategic Procurement as an integrated source-to-contract solution covering sourcing events, constraint-based optimization, contract lifecycle management and supplier qualification and performance.

SAP Subscription Billing currently supports one-time, recurring and usage-based fees, contract lifecycle changes, real-time and offline rating, bundles, invoice discounting and integrated quote-to-cash scenarios.

*Reviewed: July 2026. SAP product names, cloud packaging, available integrations and supported scenarios may change. Detailed pricing configuration should be validated against the deployed SAP edition, current SAP documentation, accounting policy and signed commercial agreements.*

## Continue exploring

- [Do You Actually Need RISE with SAP? What It Is, What It Includes, and Where Companies Get Trapped](/blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [Do You Actually Need RISE with SAP? What It Is, What It Includes, and Where Companies Get Trapped](/blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/)
- Next in the migration: [Your ATP Is Not a Stock Check: How SAP aATP, gATP, IBP, Allocation, and Backorder Processing Actually Work](/blog/your-atp-is-not-a-stock-check-how-sap-aatp-gatp-ibp-allocation-and/)
