---
layout: blog
title: "Your ATP Is Not a Stock Check: How SAP aATP, gATP, IBP, Allocation, and Backorder Processing Actually Work"
description: "Another customer has received the available stock. A production receipt was delayed. The warehouse cannot complete the delivery before the carrier cut-off."
slug: your-atp-is-not-a-stock-check-how-sap-aatp-gatp-ibp-allocation-and
permalink: /blog/your-atp-is-not-a-stock-check-how-sap-aatp-gatp-ibp-allocation-and/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP solution architecture"
tags:
  - sap-solution-architecture
  - sap-sd
canonical_url: https://dkharlanau.github.io/blog/your-atp-is-not-a-stock-check-how-sap-aatp-gatp-ibp-allocation-and/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 31
migration_sequence: 41
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/
  - /blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/
---

## On this page

- [What ATP actually does](#what-atp-actually-does)
- [ATP is not inventory](#atp-is-not-inventory)
- [ATP is not forecasting](#atp-is-not-forecasting)
- [ATP is not MRP](#atp-is-not-mrp)
- [ATP is not capacity planning](#atp-is-not-capacity-planning)
- [ATP is not transportation planning](#atp-is-not-transportation-planning)
- [ATP is not allocation policy](#atp-is-not-allocation-policy)
- [The evolution from classic ATP to gATP and aATP](#the-evolution-from-classic-atp-to-gatp-and-aatp)
- [Classic ATP in SAP ERP and S/4HANA](#classic-atp-in-sap-erp-and-s-4hana)
- [SAP APO Global Available-to-Promise](#sap-apo-global-available-to-promise)
- [SAP S/4HANA Advanced Available-to-Promise](#sap-s-4hana-advanced-available-to-promise)
- [Product Availability Check](#product-availability-check)
- [Checking horizon and replenishment lead time](#checking-horizon-and-replenishment-lead-time)
- [Full and partial confirmation](#full-and-partial-confirmation)
- [Product Allocation](#product-allocation)
- [Supply Protection](#supply-protection)
- [Alternative-Based Confirmation](#alternative-based-confirmation)
- [Backorder Processing](#backorder-processing)
- [BOP prioritization should be commercially governed](#bop-prioritization-should-be-commercially-governed)
- [Release for Delivery](#release-for-delivery)
- [Classic ATP versus aATP](#classic-atp-versus-aatp)
- [gATP versus aATP](#gatp-versus-aatp)
- [Why gATP migrations become difficult](#why-gatp-migrations-become-difficult)
- [SAP IBP Response & Supply](#sap-ibp-response-supply)
- [aATP and IBP are not competitors by default](#aatp-and-ibp-are-not-competitors-by-default)
- [When IBP adds value](#when-ibp-adds-value)
- [PP/DS and capable-to-promise](#pp-ds-and-capable-to-promise)
- [ATP, PP/DS and IBP answer different horizons](#atp-pp-ds-and-ibp-answer-different-horizons)
- [What “global ATP” should mean today](#what-global-atp-should-mean-today)
- [One S/4HANA system](#one-s-4hana-system)
- [Multiple S/4HANA or ERP systems](#multiple-s-4hana-or-erp-systems)
- [Global ATP requires global identity](#global-atp-requires-global-identity)
- [Global ATP requires freshness](#global-atp-requires-freshness)
- [ATP for e-commerce and omnichannel](#atp-for-e-commerce-and-omnichannel)
- [ATP and warehouse execution](#atp-and-warehouse-execution)
- [ATP and Transportation Management](#atp-and-transportation-management)
- [Confirmation should have levels of confidence](#confirmation-should-have-levels-of-confidence)
- [The hardest ATP problem is fairness under shortage](#the-hardest-atp-problem-is-fairness-under-shortage)
- [Do not hide scarcity policy inside technical filters](#do-not-hide-scarcity-policy-inside-technical-filters)
- [Manual confirmation changes need governance](#manual-confirmation-changes-need-governance)
- [Modern ATP architecture patterns](#modern-atp-architecture-patterns)
- [Pattern 1: Simple stocked-product business](#pattern-1-simple-stocked-product-business)
- [Pattern 2: Constrained B2B distribution](#pattern-2-constrained-b2b-distribution)
- [Pattern 3: Multi-plant fulfilment](#pattern-3-multi-plant-fulfilment)
- [Pattern 4: Complex manufacturing](#pattern-4-complex-manufacturing)
- [Pattern 5: Global multi-ERP landscape](#pattern-5-global-multi-erp-landscape)
- [Pattern 6: Omnichannel commerce](#pattern-6-omnichannel-commerce)
- [Pattern 7: APO gATP migration](#pattern-7-apo-gatp-migration)
- [How to migrate from APO gATP](#how-to-migrate-from-apo-gatp)
- [Step 1: Inventory real usage](#step-1-inventory-real-usage)
- [Step 2: Identify business outcomes](#step-2-identify-business-outcomes)
- [Step 3: Remove unused complexity](#step-3-remove-unused-complexity)
- [Step 4: Select the target owner](#step-4-select-the-target-owner)
- [Step 5: Compare promise results](#step-5-compare-promise-results)
- [Step 6: Test disruption](#step-6-test-disruption)
- [Step 7: Reconcile during transition](#step-7-reconcile-during-transition)
- [A practical implementation programme](#a-practical-implementation-programme)
- [Phase 1: Define the customer promise](#phase-1-define-the-customer-promise)
- [Phase 2: Segment the business](#phase-2-segment-the-business)
- [Phase 3: Clean the supply picture](#phase-3-clean-the-supply-picture)
- [Phase 4: Configure basic PAC correctly](#phase-4-configure-basic-pac-correctly)
- [Phase 5: Define scarcity policy](#phase-5-define-scarcity-policy)
- [Phase 6: Add alternatives](#phase-6-add-alternatives)
- [Phase 7: Connect planning](#phase-7-connect-planning)
- [Phase 8: Connect execution](#phase-8-connect-execution)
- [Phase 9: Build reconciliation](#phase-9-build-reconciliation)
- [Phase 10: Measure customer reliability](#phase-10-measure-customer-reliability)
- [KPIs that matter](#kpis-that-matter)
- [Common mistakes](#common-mistakes)
- [Questions managers should ask](#questions-managers-should-ask)
- [The management conclusion](#the-management-conclusion)

A customer requests 1,000 units for delivery next Friday.

SAP confirms the order.

Sales informs the customer.

Three days later, the confirmation changes.

Another customer has received the available stock. A production receipt was delayed. The warehouse cannot complete the delivery before the carrier cut-off. The sales team escalates the order and asks planning to “fix ATP.”

The availability check was technically correct at the moment it ran.

The customer promise was not reliable.

This is the central misunderstanding around Available-to-Promise:

> ATP does not create supply. It determines what the company is willing to promise based on the supply, demand, rules and priorities currently visible to it.

If the input data is weak, ATP produces a precise answer from unreliable assumptions.

If allocation rules are missing, the earliest order may consume supply intended for a strategic customer.

If backorder processing is poorly governed, confirmed quantities move repeatedly between orders.

If production and transportation constraints are absent, the system may promise stock that cannot be produced, packed or shipped on time.

Modern SAP landscapes offer several capabilities for order promising:

- classic ATP;
- SAP APO Global Available-to-Promise, usually called gATP;
- SAP S/4HANA Advanced Available-to-Promise, or aATP;
- SAP IBP for response and supply;
- embedded PP/DS for production planning and detailed scheduling;
- warehouse and transportation execution systems;
- external commerce or distributed order-management services.

These solutions are related.

They are not interchangeable.

A good architecture starts by deciding which question each one should answer.

## What ATP actually does

ATP answers a transactional question:

> Can this demand be confirmed, in which quantity and on which date?

The calculation normally considers some combination of:

- current stock;
- expected receipts;
- existing requirements;
- planned replenishment;
- allocation rules;
- protected supply;
- possible alternative products or locations;
- scheduling dates.

The result may be:

- full confirmation on the requested date;
- partial confirmation;
- later confirmation;
- several schedule lines;
- no confirmation;
- an alternative proposal.

ATP is therefore a commitment mechanism.

It stands between planning and execution.

```text id="a68wbr"
Supply plan
→ ATP decision
→ customer confirmation
→ warehouse and transportation execution
```

If the company treats ATP as a simple technical stock check, it misses the commercial importance of the decision.

## ATP is not inventory

Inventory answers:

> What stock is recorded?

ATP answers:

> What portion of supply remains available for this demand after other relevant requirements and policies are considered?

A warehouse may hold 10,000 units.

ATP may confirm zero because the stock is:

- already committed;
- blocked;
- in quality inspection;
- outside the relevant scope;
- located in another plant;
- protected for another demand segment;
- not available before the required date.

The reverse is also possible.

Physical stock may be zero, while ATP confirms a future quantity based on:

- purchase orders;
- production orders;
- planned orders;
- stock transfers;
- other expected receipts.

This is why the statement “we have stock” does not automatically mean “we can promise it.”

## ATP is not forecasting

A forecast estimates future demand.

ATP evaluates a concrete or simulated demand against available and expected supply.

Forecasting asks:

> What will customers probably request?

ATP asks:

> What can we promise to this request now?

Forecast consumption and planning influence future supply.

They do not replace transactional confirmation.

## ATP is not MRP

MRP identifies material shortages and creates or proposes replenishment elements.

Depending on the process, this may result in:

- planned orders;
- purchase requisitions;
- scheduling proposals;
- stock-transfer proposals.

ATP consumes the resulting supply picture.

MRP asks:

> What should we procure or produce?

ATP asks:

> What may we commit to a customer?

A sales order may receive no ATP confirmation today and later become confirmable after MRP creates new supply.

That does not mean ATP failed.

It means the supply did not yet exist in the relevant confirmation picture.

## ATP is not capacity planning

A product may have a planned production receipt.

That receipt may not be feasible because:

- machine capacity is overloaded;
- a component is missing;
- the planned order has not been scheduled realistically;
- labour capacity is unavailable.

A simple material availability check may still see the receipt.

Capacity-constrained planning belongs to capabilities such as PP/DS or SAP IBP Response & Supply.

ATP can consume a more feasible supply plan.

It should not be expected to repair an unrealistic one during every sales-order entry.

## ATP is not transportation planning

A product may be materially available at the plant on Friday.

That does not prove the customer can receive it on Friday.

The complete promise may depend on:

```text id="n4jsmk"
Material availability
→ picking and packing
→ loading
→ goods issue
→ transportation
→ customer receipt
```

If route durations, calendars, cut-offs or warehouse processing times are wrong, ATP may confirm a materially valid but commercially impossible date.

## ATP is not allocation policy

Without explicit rules, ATP often behaves close to:

> Demand that reaches the system first consumes the available quantity first.

That may be technically neutral.

It may be commercially wrong.

The company may need to protect supply for:

- strategic customers;
- regulated markets;
- service contracts;
- spare parts;
- production-critical demand;
- selected regions;
- new product launches.

Product allocation and supply protection introduce policy into the confirmation process.

ATP alone does not decide the business priority.

## The evolution from classic ATP to gATP and aATP

Understanding the history helps explain current solution choices.

## Classic ATP in SAP ERP and S/4HANA

Classic ATP is based on the availability picture within the ERP system.

The calculation is controlled through elements such as:

- checking group;
- checking rule;
- scope of check;
- requirements transfer;
- replenishment lead time;
- material and organizational configuration.

The scope of check determines which supply and demand elements are relevant.

Possible supply elements may include:

- unrestricted stock;
- purchase orders;
- production orders;
- planned orders;
- stock-transfer receipts.

Possible demand elements may include:

- sales orders;
- deliveries;
- reservations;
- dependent requirements.

The exact scope depends on the business process and configuration.

### Where classic ATP works well

Classic ATP can be sufficient when:

- one ERP system owns the supply and demand;
- the network is relatively simple;
- customer prioritization is limited;
- alternatives are not complex;
- order confirmation is mostly plant-specific;
- backorder redistribution is basic;
- high-speed advanced allocation is unnecessary.

Many companies do not need the most sophisticated ATP architecture for every product.

A simple process with good data is better than an advanced process nobody can explain.

## SAP APO Global Available-to-Promise

SAP APO gATP was introduced for more advanced and global confirmation processes outside the ERP execution system.

A typical historical architecture looked like:

```text id="5s60k8"
SAP ERP
↔ Core Interface
↔ SAP APO
↔ gATP planning data
```

The word “global” reflected the ability to evaluate a broader supply-chain model rather than only one local ERP plant.

Depending on the implemented scenario, APO gATP could support capabilities such as:

- product availability checks;
- product allocation;
- backorder processing;
- rules-based ATP;
- location and product substitution;
- multi-level checks;
- capable-to-promise integration with production planning.

The strength was the advanced planning model.

The cost was architectural complexity.

Companies had to manage:

- a separate APO system;
- planning master data;
- Core Interface integration;
- queues and reconciliation;
- duplicated or replicated planning objects;
- specialized skills.

A technically green CIF did not always mean that APO and ERP had the same business state.

## SAP S/4HANA Advanced Available-to-Promise

SAP S/4HANA aATP brings advanced confirmation capabilities into the S/4HANA environment.

The architectural advantage is important:

> The confirmation engine is closer to the transactional supply and demand that it is promising.

This reduces some of the separation historically associated with an external APO gATP landscape.

The aATP capability set has evolved by S/4HANA release and deployment model. Depending on the edition, release and licensed scope, it can include capabilities such as:

- Product Availability Check;
- Product Allocation;
- Supply Protection;
- Backorder Processing;
- Alternative-Based Confirmation;
- Release for Delivery.

These functions solve different business problems.

They should not all be activated simply because they exist.

## Product Availability Check

Product Availability Check, or PAC, is the foundation.

It evaluates whether a requested product and quantity can be confirmed based on relevant supply and demand.

A simplified picture is:

```text id="ux9jf8"
Relevant stock
+ relevant future receipts
– existing relevant requirements
= remaining confirmation capability
```

The real calculation is date-dependent.

Supply available next month cannot satisfy a request for tomorrow unless the customer accepts the later date.

### What PAC needs

PAC depends on reliable:

- product data;
- plant and storage-location design;
- checking configuration;
- receipt dates;
- requirement dates;
- units of measure;
- calendars;
- scheduling parameters.

The algorithm cannot know that a purchase order date is unrealistic.

It sees the date maintained in the system.

### Scope of check is a business decision

Including more receipt categories may increase confirmation.

It may also reduce reliability.

For example, should ATP consider:

- planned orders that have not been converted?
- purchase requisitions without a supplier?
- purchase orders from an unreliable supplier?
- quality-inspection stock?
- stock in transfer?
- supply beyond the replenishment horizon?

There is no universally correct answer.

The company must decide which supply is sufficiently reliable to support a customer commitment.

## Checking horizon and replenishment lead time

Some ATP processes use a replenishment horizon after which the system assumes the material can be replenished.

This can be useful for regularly replenished products.

It can also create false confidence when:

- the supplier has constrained capacity;
- the product is being phased out;
- the lead time is outdated;
- a component is scarce;
- the source is blocked.

A replenishment lead time is not a guarantee.

It is a planning assumption.

Managers should measure how often promises based on assumed future replenishment are later changed.

## Full and partial confirmation

Suppose a customer requests 100 units.

Available supply is:

- 40 units on the requested date;
- 60 units one week later.

Possible responses include:

- confirm 40 now and 60 later;
- wait and deliver all 100 later;
- reject the partial confirmation;
- propose another product or plant;
- escalate under service policy.

SAP can represent partial confirmations through schedule lines.

The commercial policy should decide whether partial delivery is acceptable.

Otherwise, the availability engine may create technically valid split fulfilment with unnecessary:

- warehouse work;
- freight;
- billing;
- customer receiving effort.

## Product Allocation

Product Allocation controls how much demand may be confirmed for defined market or demand segments.

It is useful when total supply is limited and management wants to distribute it deliberately.

Possible allocation characteristics might include:

- customer;
- customer group;
- country;
- region;
- sales organization;
- distribution channel;
- product group;
- time period.

A simplified allocation table might be:

| Market segment | Weekly allocation |
|---|---:|
| Strategic customers | 4,000 |
| Standard domestic | 3,000 |
| Export | 2,000 |
| Service parts | 1,000 |

The allocation does not necessarily mean that physical stock is stored separately.

It controls the confirmation entitlement.

### Why allocation is needed

Without allocation, one channel may consume the supply before another channel places its orders.

Examples:

- domestic customers consume stock planned for export;
- one distributor enters inflated orders early;
- a low-margin channel consumes supply needed for contractual service;
- one country takes stock intended for a regulated launch.

Product Allocation makes the scarcity decision explicit.

### Allocation is not a forecast

A forecast estimates demand.

An allocation defines how much confirmation is permitted for a segment.

The two may be connected.

They should not be confused.

A forecast says:

> We expect this region to request 5,000 units.

An allocation says:

> This region may consume up to 4,000 units from the constrained supply during the period.

### Poor allocation can lock supply unnecessarily

If one segment does not use its allocation while another has urgent demand, the company needs a release or redistribution policy.

Possible rules include:

- unused quantity released after a date;
- central planner approval;
- backorder redistribution;
- rolling time buckets;
- protected minimum plus shared remainder.

The allocation model should balance:

- protection;
- utilization;
- flexibility.

## Supply Protection

Supply Protection addresses a related but different problem.

Instead of only limiting how much a demand segment may consume, it protects a quantity of supply for selected demand groups.

Conceptually:

```text id="xsf00s"
Available supply
– protected quantity for priority demand
= supply available to non-protected demand
```

This can be useful when management wants to preserve a minimum quantity for:

- critical customers;
- important markets;
- service parts;
- production continuity;
- contractual obligations.

### Product Allocation versus Supply Protection

A simplified distinction is:

#### Product Allocation

Controls the maximum quantity that a demand group can consume.

#### Supply Protection

Preserves a minimum portion of supply for protected demand.

They may solve similar scarcity problems from opposite directions.

### Protection requires expiration rules

Protected supply can become obsolete if the intended demand never arrives.

The architecture should define:

- protection period;
- release date;
- hierarchy;
- remaining quantity;
- emergency override.

Otherwise, the company may deny real orders while protected stock remains unused.

## Alternative-Based Confirmation

Alternative-Based Confirmation is intended for situations where the originally requested product or source cannot satisfy demand, but an acceptable alternative may exist.

Alternatives may include, depending on the designed scenario and available functionality:

- another plant;
- another supplying location;
- another product;
- substitute product;
- alternative fulfilment source.

A modern promise should sometimes answer more than:

> No stock.

It may answer:

> The requested product is unavailable from plant A, but can be supplied from plant B two days later.

Or:

> Product X is unavailable, but approved substitute Y can be delivered on the requested date.

### Alternatives have economic consequences

An alternative plant may create:

- additional transport cost;
- intercompany processing;
- customs exposure;
- longer route;
- different inventory priority.

A substitute product may create:

- customer-approval requirements;
- price differences;
- technical incompatibility;
- different packaging;
- regulatory issues.

Alternative confirmation should therefore use:

- eligibility rules;
- ranking;
- cost or service guardrails;
- customer permissions;
- clear explanation.

Do not activate broad substitution merely to increase the confirmation rate.

## Backorder Processing

A confirmation is not permanent simply because it was created first.

Supply changes.

Examples include:

- supplier delay;
- production shortfall;
- stock difference;
- quality block;
- new urgent order;
- customer cancellation;
- improved supply.

Backorder Processing, or BOP, re-evaluates existing confirmations.

The management question is:

> When supply changes, which demands should keep, gain or lose confirmation?

This is not a technical batch job.

It is a scarcity policy.

### Typical BOP concepts

Orders can be segmented by business priority.

The process may attempt to:

- protect confirmations for high-priority demand;
- improve selected orders;
- redistribute supply;
- fill unconfirmed quantities;
- remove confirmations from low-priority demand.

SAP aATP BOP uses confirmation strategies commonly described around behaviours such as:

- Win;
- Gain;
- Redistribute;
- Fill;
- Lose.

The exact configuration depends on the release and business design.

The important point is that BOP makes reallocation intentional.

### BOP should not create daily chaos

A poorly designed BOP process may repeatedly move supply between orders.

The customer sees:

```text id="mhm60r"
Monday: confirmed
Tuesday: unconfirmed
Wednesday: confirmed later
Thursday: confirmed again
```

The system is reacting dynamically.

The customer experiences unreliability.

### Use confirmation stability as a KPI

Measure:

- percentage of orders whose first confirmation changes;
- number of changes per order;
- quantity moved by BOP;
- orders gaining confirmation;
- orders losing confirmation;
- customer impact;
- expedite created after change.

The objective is not to maximize BOP activity.

It is to improve the quality and fairness of commitments.

## BOP prioritization should be commercially governed

Possible priority attributes include:

- customer segment;
- service agreement;
- requested date;
- order age;
- delivery priority;
- product criticality;
- order margin;
- contractual penalty;
- production impact.

Avoid uncontrolled priority fields maintained manually by sales users.

If every urgent order receives the highest priority, BOP has no real policy.

## Release for Delivery

An order may have a confirmation but still compete with other orders when the company prepares deliveries.

Release-for-delivery capabilities can help prioritize and process orders approaching delivery execution, depending on the implemented S/4HANA aATP scope.

The important distinction is:

```text id="pa0k0z"
ATP confirmation
≠ physical delivery readiness
```

Before delivery release, the company may need to verify:

- current confirmation;
- delivery due date;
- service priority;
- warehouse capacity;
- transportation departure;
- blocks;
- complete-delivery requirement.

A confirmation should not remain protected indefinitely when the customer or process is not ready to consume it.

## Classic ATP versus aATP

| Requirement | Classic ATP | S/4HANA aATP |
|---|---:|---:|
| Basic stock and receipt check | Strong | Strong |
| Embedded S/4HANA execution | Yes | Yes |
| Advanced product allocation | Limited/basic scenarios | Stronger capability |
| Advanced backorder prioritization | Basic possibilities | Stronger segmentation and strategies |
| Supply protection | Not the main model | Dedicated capability |
| Alternative source or product logic | Limited/custom-dependent | Alternative-based scenarios |
| High-volume advanced confirmation | Depends on design | Designed for advanced S/4HANA scenarios |
| Separate planning system required | No | No |
| Complexity | Lower | Higher |

Not every S/4HANA customer needs aATP.

The investment is justified when the business has real problems in:

- constrained supply;
- prioritization;
- global or multi-location fulfilment;
- repeated backorder redistribution;
- customer segmentation;
- alternatives.

## gATP versus aATP

| Area | APO gATP | S/4HANA aATP |
|---|---|---|
| Runtime architecture | Separate APO system | Embedded closer to S/4HANA |
| Data integration | CIF and replicated planning model | Uses S/4HANA transactional context |
| Historic advanced capabilities | Broad mature gATP scenarios | Modern S/4HANA capability set evolving by release |
| Rules-based substitution | Strong historical use | Alternative-based approach, scope must be assessed |
| Product allocation | Yes | Yes |
| Backorder processing | Yes | Yes, redesigned user and segmentation model |
| CTP and multi-level scenarios | Used with APO planning | Must be reassessed with S/4HANA, PP/DS and IBP |
| Migration approach | Existing legacy solution | Target option for S/4HANA landscape |

The migration is not a technical one-to-one conversion.

A company should not ask:

> Which aATP switch replaces this gATP setting?

It should ask:

> Which current business promise does the old design provide, and which target capability should provide it now?

## Why gATP migrations become difficult

Long-running APO landscapes often contain business logic in:

- rule strategies;
- product substitution;
- location substitution;
- location-product hierarchies;
- allocation objects;
- BOP filters;
- multi-level checks;
- custom enhancements;
- CIF filters;
- fallback logic.

Some of this logic remains valuable.

Some exists because the old network and process required it 15 years ago.

A migration should classify each capability as:

- still required;
- replace with aATP;
- replace with IBP;
- replace with PP/DS;
- move to order management;
- simplify;
- retire.

## SAP IBP Response & Supply

SAP IBP operates at a different planning level.

SAP currently positions IBP as a cloud-based planning solution combining demand, inventory, response and supply, S&OP and related planning capabilities. Its response-management scope includes operational or order-based supply planning, allocations and order repromising based on prioritization rules.

This makes IBP relevant where the company needs to look across a wider horizon and network.

### aATP asks

> What can I confirm to this transaction now?

### IBP Response & Supply asks

> Given current demand, supply, capacity and priorities, how should the network respond and which orders should receive supply?

IBP can support:

- multilevel network planning;
- constrained supply planning;
- order-based planning;
- prioritization;
- allocation planning;
- scenario comparison;
- repromising.

SAP states that IBP Response & Supply can model across locations and multilevel bills of material, create constrained or unconstrained supply plans and manage order-based plans, allocations and repromising.

## aATP and IBP are not competitors by default

A practical architecture may use both.

```text id="bjg9pj"
SAP IBP
Network planning, allocation and response decisions
                     |
                     v
SAP S/4HANA aATP
Real-time transactional promise
                     |
                     v
Sales order and fulfilment execution
```

IBP can provide a broader supply-response plan.

aATP can execute immediate order confirmation inside S/4HANA.

The boundary must be clear.

Otherwise, the two systems may repeatedly repromise the same orders under different rules.

## When IBP adds value

IBP becomes more relevant when:

- several locations and supply levels matter;
- production and material constraints interact;
- planners need scenarios;
- customer orders must be prioritized globally;
- supply plans are frequently rebalanced;
- medium-term decisions influence short-term confirmations.

It may be unnecessary when:

- one plant serves one market;
- supply is rarely constrained;
- confirmation rules are simple;
- S/4HANA has the complete relevant picture.

## PP/DS and capable-to-promise

Product availability asks whether supply exists.

Capable-to-promise asks whether supply can be created feasibly.

This may require checking:

- material components;
- production capacity;
- sequence;
- lead time;
- resource constraints.

In modern S/4HANA landscapes, embedded PP/DS can support detailed production planning and scheduling.

A company may use PP/DS to improve the feasibility of future receipts consumed by ATP.

The architecture should avoid performing a full production optimization synchronously for every low-value order.

### Use CTP selectively

Capable-to-promise is more appropriate for:

- make-to-order;
- engineered products;
- constrained manufacturing;
- high-value orders;
- long lead-time products.

It may be excessive for:

- high-volume stocked products;
- simple replenishment;
- low-value orders where response time matters.

## ATP, PP/DS and IBP answer different horizons

| Capability | Main question | Typical horizon |
|---|---|---|
| aATP | Can this order be promised now? | Immediate to operational |
| BOP | Which existing orders should receive changed supply? | Short-term operational |
| PP/DS | Can production be scheduled feasibly? | Short-term detailed |
| IBP Response & Supply | How should supply and orders be balanced across the network? | Operational to tactical |
| IBP S&OP | Which business plan balances demand, supply and finance? | Tactical to strategic |

The exact horizons vary by company.

The distinction of responsibility is more important than the exact number of days.

## What “global ATP” should mean today

Many companies ask for global ATP because they have:

- several plants;
- several countries;
- multiple S/4HANA systems;
- legacy ERPs;
- external warehouses;
- e-commerce platforms.

The phrase should be defined carefully.

### Global inventory visibility

Can the company see stock across all relevant locations?

### Global confirmation

Can one service make a commitment using supply across the network?

### Global allocation

Can scarce supply be distributed across markets and customers?

### Global fulfilment selection

Can the system choose the economically appropriate source?

### Global reallocation

Can confirmations be reprioritized across systems?

These are different capabilities.

A dashboard showing global inventory is not global ATP.

## One S/4HANA system

When one S/4HANA instance owns the relevant:

- stock;
- receipts;
- requirements;
- sales orders;

embedded aATP can provide a strong central confirmation point.

This is the cleanest architecture.

## Multiple S/4HANA or ERP systems

When supply and demand are distributed across several execution systems, one local aATP engine does not automatically become globally authoritative.

The company must choose an architecture.

### Option 1: Centralize order capture in one ERP

One S/4HANA system owns the customer order and selected global supply picture.

Advantages:

- one transactional promise;
- simpler ownership.

Risks:

- replication dependency;
- complex intercompany execution;
- one central system becomes critical.

### Option 2: Use a central planning and allocation layer

IBP or another planning service creates global supply and allocation decisions.

Local ERPs execute within these limits.

Advantages:

- broad network view;
- local operational ownership.

Risks:

- global plan and local confirmation may diverge;
- synchronization and repromising are required.

### Option 3: Use a distributed order-management layer

A central order-management service receives channel demand, reads availability and chooses a fulfilment source.

Advantages:

- omnichannel orchestration;
- source selection across systems.

Risks:

- another order authority;
- reservation and consistency problems;
- complex cancellation and reallocation.

### Option 4: Keep local ATP with commercial allocation

Each ERP confirms local orders.

A central governance process defines market allocations.

Advantages:

- simpler local execution;
- lower real-time integration dependency.

Risks:

- limited dynamic global optimization;
- manual or batch redistribution.

There is no universally correct model.

The architecture should follow:

- order ownership;
- response-time requirement;
- number of systems;
- network complexity;
- tolerance for temporary inconsistency.

## Global ATP requires global identity

A central promise service must understand:

- the same product across systems;
- equivalent units of measure;
- plants and fulfilment locations;
- customer and segment identity;
- order priority;
- supply status.

Without governed identity, the system may:

- count the same stock twice;
- fail to recognize substitute products;
- assign the wrong allocation;
- misinterpret units;
- promise from a location that cannot serve the customer.

Global ATP is partly a master-data programme.

## Global ATP requires freshness

Availability changes rapidly.

A replicated inventory feed may be:

- seconds old;
- minutes old;
- hours old.

The acceptable delay depends on:

- order volume;
- scarcity;
- product value;
- concurrency;
- cancellation rate.

A portal showing yesterday’s stock is inventory reporting.

It is not transactional ATP.

### Prevent overselling

If several channels consume the same supply, the architecture needs a control such as:

- one central confirmation authority;
- reservation;
- allocation by channel;
- synchronized decrement;
- safety buffer;
- frequent reconciliation.

Reading stock from several systems without controlling commitment creates overselling.

## ATP for e-commerce and omnichannel

E-commerce customers expect immediate responses.

The process may need to answer:

- in stock;
- delivery date;
- pickup location;
- substitute;
- split shipment;
- delivery cost.

Calling a complex global production check for every product-page view may be impractical.

### Separate availability inquiry from binding reservation

#### Informational inquiry

Used for:

- product page;
- estimated availability;
- store display.

May tolerate:

- caching;
- simplified rules;
- safety buffer.

#### Transactional promise

Used for:

- cart checkout;
- order submission;
- final confirmation.

Requires:

- current supply;
- duplicate protection;
- authoritative reservation or confirmation.

Do not present an informational estimate as a guaranteed promise.

## ATP and warehouse execution

ATP may confirm a quantity from a plant.

EWM determines whether the warehouse can physically process it.

Potential constraints include:

- picking capacity;
- packaging;
- stock status;
- batch;
- handling unit;
- carrier cut-off.

The warehouse should feed realistic execution times into scheduling and planning.

But warehouse-task capacity should not necessarily be evaluated synchronously during every order confirmation.

Use service calendars and capacity policies where transaction-level detailed checks would be too expensive.

## ATP and Transportation Management

A product may be available.

Transportation may still be impossible on the confirmed date.

Relevant constraints include:

- departure schedule;
- transit time;
- delivery window;
- carrier capacity;
- route;
- customs.

For standard flows, ATP may rely on maintained scheduling rules and calendars.

For constrained or special transport, the promise may require an additional transport check or later confirmation stage.

The company should state what the confirmation actually guarantees:

- product availability;
- shipment date;
- delivery date;
- complete logistical feasibility.

## Confirmation should have levels of confidence

Not every confirmed date has the same evidence.

A useful management model may classify promises.

### Firm confirmation

Based on:

- current stock;
- firm receipt;
- reliable execution capacity.

### Planned confirmation

Based on:

- planned production;
- expected purchase;
- standard lead time.

### Conditional confirmation

Depends on:

- customer approval;
- substitute;
- alternative plant;
- transport capacity;
- manual decision.

The customer-facing message may remain simple.

Internally, the company should know the confidence behind the promise.

## The hardest ATP problem is fairness under shortage

When supply is sufficient, ATP appears simple.

When supply is constrained, ATP becomes a commercial policy engine.

Consider 1,000 available units and demand from:

- strategic customer: 600;
- standard customers: 800;
- spare-parts contract: 200;
- export market: 300.

Total demand is 1,900.

The system cannot avoid a business decision.

It can only apply the one management has encoded.

Possible objectives include:

- maximize revenue;
- maximize margin;
- protect contracts;
- protect customer relationships;
- minimize penalties;
- preserve market presence;
- protect production.

These objectives may conflict.

The ATP project must force management to decide.

## Do not hide scarcity policy inside technical filters

A BOP filter such as:

```text id="ohsn3q"
Delivery priority = 01
```

looks technical.

It may determine which customer loses supply.

Every priority attribute should have:

- business definition;
- owner;
- permitted values;
- audit;
- protection from manipulation.

## Manual confirmation changes need governance

Sales and planners may need to override confirmations.

Typical reasons include:

- strategic escalation;
- system data error;
- customer agreement;
- emergency service;
- confirmed new supply.

Manual changes should record:

- reason;
- user;
- quantity;
- displaced demand;
- approval;
- expected recovery.

Otherwise, ATP becomes a system calculation constantly bypassed by informal power.

## Modern ATP architecture patterns

## Pattern 1: Simple stocked-product business

Characteristics:

- one S/4HANA system;
- few plants;
- stable supply;
- limited scarcity.

Recommended approach:

- classic ATP or basic aATP;
- reliable scope of check;
- scheduling;
- exception reporting.

Do not overengineer.

## Pattern 2: Constrained B2B distribution

Characteristics:

- scarce products;
- strategic customers;
- several markets;
- frequent reprioritization.

Recommended approach:

- aATP Product Availability Check;
- Product Allocation or Supply Protection;
- governed BOP;
- confirmation-stability reporting.

## Pattern 3: Multi-plant fulfilment

Characteristics:

- several possible sources;
- different lead times and freight cost;
- customer substitution rules.

Recommended approach:

- aATP with carefully designed alternative confirmation;
- source-ranking policy;
- transport and intercompany guardrails;
- cost-to-serve visibility.

## Pattern 4: Complex manufacturing

Characteristics:

- constrained components;
- limited production capacity;
- make-to-order;
- long lead time.

Recommended approach:

- aATP for transactional promise;
- embedded PP/DS for feasible production planning;
- selective CTP-style logic where justified;
- IBP for broader response planning.

## Pattern 5: Global multi-ERP landscape

Characteristics:

- several execution systems;
- shared customers;
- global constrained supply.

Recommended approach:

- explicit global allocation authority;
- IBP or central order-management layer;
- local ATP inside controlled allocations;
- cross-system identity and reconciliation.

## Pattern 6: Omnichannel commerce

Characteristics:

- high inquiry volume;
- stores and warehouses;
- instant customer expectation.

Recommended approach:

- cached informational availability;
- authoritative checkout promise;
- reservation or confirmation control;
- distributed source selection where required;
- overselling reconciliation.

## Pattern 7: APO gATP migration

Characteristics:

- mature rules-based ATP;
- custom substitutions;
- allocations;
- BOP;
- CIF dependencies.

Recommended approach:

- business capability inventory;
- map each capability to aATP, IBP, PP/DS or order management;
- avoid one-to-one technical replication;
- parallel promise comparison before cutover.

## How to migrate from APO gATP

## Step 1: Inventory real usage

Do not rely only on configuration.

Identify:

- active check modes;
- rules strategies;
- location substitutions;
- product substitutions;
- allocation objects;
- BOP variants;
- CTP scenarios;
- multi-level ATP;
- custom enhancements;
- manual workarounds.

## Step 2: Identify business outcomes

For each capability, document:

- business problem;
- users;
- customer segments;
- response-time requirement;
- financial impact;
- current pain.

## Step 3: Remove unused complexity

Many mature APO systems contain objects no longer used in real order processing.

Do not migrate dead logic.

## Step 4: Select the target owner

Possible target:

- S/4HANA aATP;
- PP/DS;
- IBP Response & Supply;
- distributed order management;
- simplified business process.

## Step 5: Compare promise results

Run representative demands through old and target logic.

Compare:

- confirmed quantity;
- confirmed date;
- source;
- substitute;
- allocation consumption;
- order priority;
- later BOP result.

## Step 6: Test disruption

Include:

- late supply;
- cancelled production;
- new strategic order;
- stock difference;
- expired allocation;
- alternative plant unavailable.

## Step 7: Reconcile during transition

If APO and S/4HANA coexist, define which system owns each order and confirmation.

Do not allow both to reallocate the same supply independently.

## A practical implementation programme

## Phase 1: Define the customer promise

State clearly whether the confirmation guarantees:

- material availability;
- goods-issue date;
- delivery date;
- complete quantity;
- selected source.

## Phase 2: Segment the business

Separate:

- stocked products;
- make-to-order;
- constrained products;
- service parts;
- strategic customers;
- e-commerce.

## Phase 3: Clean the supply picture

Validate:

- stock categories;
- receipt reliability;
- requirements;
- lead times;
- units;
- calendars.

## Phase 4: Configure basic PAC correctly

Do not add advanced rules before the foundation works.

## Phase 5: Define scarcity policy

Choose:

- Product Allocation;
- Supply Protection;
- BOP prioritization;
- manual exception authority.

## Phase 6: Add alternatives

Define:

- permitted substitute;
- source ranking;
- freight impact;
- customer approval.

## Phase 7: Connect planning

Use PP/DS and IBP where capacity, materials and network decisions require them.

## Phase 8: Connect execution

Align:

- delivery creation;
- EWM cut-offs;
- TM departures;
- customer schedules.

## Phase 9: Build reconciliation

Compare:

- requested;
- first confirmed;
- current confirmed;
- delivered.

## Phase 10: Measure customer reliability

Do not declare success because confirmation performance is fast.

Measure whether it remains true.

## KPIs that matter

### Confirmation rate

Percentage of requested quantity confirmed.

Useful, but dangerous alone.

A high rate may rely on unrealistic future receipts.

### Requested-date confirmation rate

Percentage confirmed on the requested date.

### First-confirmation reliability

Percentage delivered according to the first confirmed commitment.

This is stronger than using the latest changed date.

### Confirmation stability

Percentage of orders whose confirmation does not change.

### BOP churn

Quantity or number of orders repeatedly gaining and losing confirmation.

### Allocation utilization

How much allocated quantity was actually consumed?

### Allocation denial

How much demand was rejected because of allocation despite unused total supply?

### Protected-supply utilization

Was protected stock actually used by the intended segment?

### Alternative-confirmation rate

How often was an alternative product or location proposed?

### Alternative acceptance

How often did the customer accept it?

### Expedite dependency

How much premium freight or manual intervention was required to fulfil the confirmed promise?

### Manual override rate

How frequently are system confirmations changed manually?

### Promise response time

How quickly can the company provide an authoritative answer?

### Lost-demand visibility

How much demand was unconfirmed, cancelled or moved elsewhere?

## Common mistakes

### Mistake 1: Treating ATP as a stock lookup

Existing commitments and future receipts are ignored.

### Mistake 2: Including unreliable supply

The confirmation rate improves while reliability falls.

### Mistake 3: Using first come, first served during scarcity

Strategic and contractual demand loses supply.

### Mistake 4: Creating allocations with no release policy

Supply remains unused while orders are rejected.

### Mistake 5: Protecting every important customer

Almost all supply becomes protected and the model stops working.

### Mistake 6: Running aggressive BOP too frequently

Customers receive unstable promises.

### Mistake 7: Letting users manipulate priority fields

Commercial allocation is bypassed.

### Mistake 8: Using aATP as a replacement for production planning

Material receipts remain infeasible.

### Mistake 9: Using IBP as the real-time checkout engine

A planning system is forced into transactional response.

### Mistake 10: Using local ATP as global ATP

Several systems promise the same limited supply.

### Mistake 11: Reading global stock without reservation control

Omnichannel overselling occurs.

### Mistake 12: Activating substitution without cost rules

Confirmation improves while freight and complexity grow.

### Mistake 13: Ignoring transportation and warehouse calendars

The product is available, but delivery is impossible.

### Mistake 14: Migrating APO configuration one to one

Historical complexity is recreated in S/4HANA.

### Mistake 15: Measuring the latest confirmed date

Repeated promise failures disappear from the KPI.

## Questions managers should ask

1. What exactly does our confirmation promise?
2. Which supply elements are trusted enough to support it?
3. How often does the first confirmation change?
4. Which customers should receive scarce supply?
5. Is the priority policy formally approved?
6. Are we using Product Allocation or Supply Protection for the right purpose?
7. When is unused protection released?
8. How often does BOP move supply between customers?
9. Can sales users override priorities?
10. Which alternatives may be offered?
11. Does alternative sourcing include freight and service cost?
12. Are production receipts capacity-feasible?
13. Does IBP or S/4HANA own order repromising?
14. Can several systems promise the same supply?
15. How fresh is global availability data?
16. What prevents omnichannel overselling?
17. Are warehouse and transport constraints reflected in the date?
18. Which APO gATP functions are genuinely still required?
19. Can every confirmation be explained?
20. Are we optimizing the confirmation rate or customer reliability?

## The management conclusion

Modern ATP is not mainly about checking stock faster.

It is about controlling the promise the company makes under uncertainty.

Classic ATP can remain sufficient for straightforward businesses.

SAP S/4HANA aATP adds stronger capabilities for availability checks, allocation, supply protection, backorder reprioritization and alternative confirmation.

Embedded PP/DS improves the feasibility of production supply.

SAP IBP extends the decision into multilevel, constrained and order-based response planning across a wider network. SAP currently describes IBP Response & Supply as supporting multilevel supply planning, constrained and unconstrained methods, rough-cut capacity planning and order-based response management with allocations and repromising rules.

The correct architecture should be layered:

```text id="nnmb4j"
IBP
Plans network response and supply priorities
                    |
PP/DS
Creates a feasible short-term production plan
                    |
S/4HANA aATP
Makes and revises the transactional promise
                    |
EWM and TM
Execute warehouse and transportation commitments
```

Not every company needs every layer.

But every company needs one clear promise owner.

The decisive question is not:

> Did SAP find an available quantity?

It is:

> Did the company make the right commitment to the right customer, based on supply it can realistically execute, and did that commitment remain stable?

When ATP is judged by that standard, it stops being a technical SD setting.

It becomes one of the central control mechanisms of the supply chain.

---

### SAP ATP architecture checklist

- [ ] The customer promise is defined precisely.
- [ ] Inventory, ATP, planning and execution are distinguished.
- [ ] The scope of check includes only sufficiently reliable supply.
- [ ] Receipt dates and replenishment lead times are measured against reality.
- [ ] Partial-delivery policy is commercially approved.
- [ ] Product Allocation has clear segments and release rules.
- [ ] Supply Protection has expiration and override governance.
- [ ] BOP priorities are based on approved business policy.
- [ ] Confirmation stability is measured.
- [ ] Manual overrides require reason and authority.
- [ ] Alternatives include customer, cost and logistics restrictions.
- [ ] Product and location substitutions are explainable.
- [ ] Production feasibility is handled through PP/DS or appropriate planning.
- [ ] IBP and aATP responsibilities are separated.
- [ ] One system owns each transactional confirmation.
- [ ] Multi-system supply is not promised twice.
- [ ] Global product, location and customer identity is governed.
- [ ] Informational availability is separated from binding confirmation.
- [ ] E-commerce checkout uses authoritative supply control.
- [ ] Warehouse and transportation scheduling support the confirmed date.
- [ ] APO gATP migration is based on capabilities, not settings.
- [ ] Parallel promise comparison is performed before cutover.
- [ ] Requested, first-confirmed, current-confirmed and delivered dates are retained.
- [ ] ATP success is measured through reliable customer fulfilment.

### Sources and further reading

SAP currently describes SAP Integrated Business Planning as a cloud planning solution combining S&OP, demand, inventory, response and supply, demand-driven replenishment and supply-chain visibility.

SAP’s current IBP feature description states that Response and Supply Planning supports multilevel network modelling, constrained and unconstrained supply planning, rough-cut capacity planning, and operational or order-based response management with allocations and repromising based on prioritization rules.

*Reviewed: July 2026. SAP aATP, PP/DS and IBP functionality, licensing and available scope differ by S/4HANA edition, deployment model and release. Detailed solution design should be validated against the exact SAP release, current product documentation and the company’s real order-promising policy.*

## Continue exploring

- [Do You Actually Need RISE with SAP? What It Is, What It Includes, and Where Companies Get Trapped](/blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [SAP Pricing Explained: Sales, Procurement, Rebates, CPQ, Contracts, and the Right Solution for Each Business Model](/blog/sap-pricing-explained-sales-procurement-rebates-cpq-contracts-and-the/)
- Next in the migration: [Why MRP Alone Cannot Run Your Supply Chain: The Complete SAP Landscape for Demand, Supply, and Replenishment Planning](/blog/why-mrp-alone-cannot-run-your-supply-chain-the-complete-sap-landscape/)
