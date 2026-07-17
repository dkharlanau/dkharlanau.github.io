---
layout: blog
title: "How to Design a Sales Solution for Subscription and Usage-Based Offers with SAP BRIM"
description: "a monthly platform fee; - a fixed amount of included usage; - an additional fee above the limit; - a discount for a two-year commitment."
slug: how-to-design-a-sales-solution-for-subscription-and-usage-based-offers
permalink: /blog/how-to-design-a-sales-solution-for-subscription-and-usage-based-offers/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP commercial processes"
tags:
  - sap-commercial-processes
  - sap-sd
canonical_url: https://dkharlanau.github.io/blog/how-to-design-a-sales-solution-for-subscription-and-usage-based-offers/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 21
migration_sequence: 21
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/when-standard-sap-billing-is-no-longer-enough-what-sap-brim-actually/
  - /blog/where-automation-actually-makes-sense-in-sap-sd-sales-order-processing/
---

## On this page

- [The most important object is the commercial offer](#the-most-important-object-is-the-commercial-offer)

A company introduces a new digital service.

The commercial model looks simple:

- a monthly platform fee;
- a fixed amount of included usage;
- an additional fee above the limit;
- a discount for a two-year commitment.

The sales team creates a quotation in CRM.

The contract is signed.

Then the operational questions begin:

- Which system creates the subscription?
- Where is the agreed price stored?
- What happens when the customer adds users?
- How is the included usage tracked?
- Which system applies the overage rate?
- How is a mid-month upgrade calculated?
- What must appear on the invoice?
- Which team owns a backdated contract correction?

The problem is no longer only billing.

It is the complete sales and monetization process.

This is where a BRIM sales solution should begin.

Not with the invoice.

Not with the activation of a billing component.

It should begin with the commercial promise made to the customer and follow that promise through:

1. opportunity;
2. offer configuration;
3. quotation;
4. approval;
5. contract or subscription;
6. fulfilment;
7. usage;
8. rating;
9. invoicing;
10. receivables and payment.

If these stages are designed separately, the company creates a technically integrated landscape with no stable commercial truth.

### Standard sales processes assume a relatively stable product

A traditional SAP sales process usually works well when the company sells:

- a known material;
- a known quantity;
- at an agreed price;
- with a clear delivery;
- followed by an invoice.

The commercial structure is often:

> Customer orders something once, the company delivers it, and the amount can be calculated from the order and delivery.

Subscription and consumption models behave differently.

The customer may buy:

- access rather than ownership;
- a right to consume;
- a recurring service;
- a package of physical and digital products;
- a commitment with variable monthly charges;
- a service that changes throughout the contract.

The sales process must therefore define more than product and quantity.

It must define:

- contract term;
- recurring charge;
- one-time fees;
- usage unit;
- included allowance;
- pricing tiers;
- renewal;
- cancellation;
- upgrade and downgrade rules;
- entitlement;
- billing cycle;
- payment terms.

This is why the sales solution cannot end with a quotation PDF.

The quotation must become an executable commercial model.

### The core design principle: sell what the billing system can execute

Sales teams want flexibility.

Billing and finance need precision.

If sales can promise conditions that downstream systems cannot represent, every complex deal becomes a manual project.

Typical examples include:

- customer-specific usage tiers stored only in the contract attachment;
- free months not connected to the subscription schedule;
- discount conditions maintained in spreadsheets;
- special cancellation terms known only to the account manager;
- bundles quoted as one item but billed through several unrelated systems;
- minimum commitments calculated manually at period end.

The quotation may be commercially approved.

It is not operationally executable.

A strong BRIM sales solution should create one controlled path from:

> what was sold

to:

> what will be provisioned, measured, rated and invoiced.

### What the sales-side architecture may include

A complete SAP solution can include several product and process layers.

The exact combination depends on the company. Not every implementation requires every product.

### SAP Sales Cloud

SAP currently positions SAP Sales Cloud as a CRM solution for sales automation, customer acquisition, guided selling, pipeline and forecast management, analytics and AI-assisted sales processes.

In a BRIM-oriented architecture, Sales Cloud can manage:

- accounts and contacts;
- opportunities;
- sales activities;
- pipeline;
- expected contract value;
- sales collaboration;
- commercial context.

It should answer:

- Who is the customer?
- What business problem are we selling against?
- Which opportunity is active?
- What is the expected commercial scope?
- Who owns the sales process?

It should not necessarily become the final source for every billing rule.

### SAP CPQ

SAP CPQ is designed for configuring, pricing and quoting complex offerings. SAP describes support for complex product dependencies, customer- and channel-specific pricing, margin controls, approval workflows and connection to CRM, commerce and ERP solutions.

In a BRIM sales solution, CPQ can manage:

- package configuration;
- product and service combinations;
- pricing;
- discounts;
- contract term options;
- approval thresholds;
- commercial proposal generation;
- partner or channel sales.

It should answer:

- What exactly is being offered?
- Is the configuration valid?
- Which price applies?
- Is the discount permitted?
- Which approval is required?
- What did the customer accept?

SAP states that CPQ can support different product types, including subscriptions, services and hardware, within the same quote.

That is useful when a sales package combines, for example:

- equipment;
- installation;
- recurring software access;
- usage-based service;
- maintenance.

### SAP Subscription Billing

SAP Subscription Billing currently supports one-time, recurring and usage-based fees, subscription lifecycle changes, renewals, flexible pricing, customer-specific offerings, data collection and integrated order-to-cash scenarios.

It can represent the ongoing commercial relationship after the quote is accepted.

It should answer:

- Which subscription is active?
- Which products and services does it contain?
- When does each charge begin?
- Which usage model applies?
- What happens after an upgrade or cancellation?
- Which price version is valid?

### SAP S/4HANA Cloud for contract accounting and invoicing

SAP positions contract accounting and invoicing for high-volume subscription and consumption invoicing, convergence of billing streams and management of receivables and payments through a dedicated subledger integrated with S/4HANA Finance.

It should answer:

- Which charges are ready to invoice?
- How are multiple billing streams combined?
- Which receivable is created?
- How is payment allocated?
- How are dunning, credits and corrections managed?
- How is detailed subledger activity reflected in finance?

### Fulfilment and entitlement systems

A sale may also trigger:

- hardware delivery;
- service activation;
- software access;
- user provisioning;
- partner notification;
- entitlement creation.

These responsibilities may sit in S/4HANA, entitlement management, BTP applications or external platforms.

The architecture should identify them explicitly.

### A practical end-to-end process

A useful BRIM sales solution can be understood as one continuous commercial flow.

### Stage 1: Qualify the opportunity

The sales team identifies:

- customer need;
- expected volume;
- required service;
- contract period;
- target start date;
- commercial value;
- expected usage pattern.

This information matters later.

For example, expected usage can affect:

- tier design;
- minimum commitment;
- capacity;
- margin;
- invoicing model.

The opportunity should capture enough commercial context to guide the offer.

It should not contain detailed billing configuration.

### Stage 2: Configure the offer

The seller selects a valid combination of:

- base subscription;
- service level;
- hardware;
- included usage;
- optional features;
- implementation services;
- partner products.

Configuration rules should prevent invalid combinations.

For example:

- premium support requires the enterprise plan;
- one device package requires one connectivity subscription;
- a regional service is available only in selected countries;
- an annual discount requires a minimum contract term.

The purpose is to stop invalid promises before they become contracts.

### Stage 3: Calculate the commercial price

The quote may contain different charge types.

#### One-time

Examples:

- setup;
- installation;
- migration;
- activation;
- equipment.

#### Recurring

Examples:

- monthly platform fee;
- user subscription;
- maintenance;
- support package.

#### Usage-based

Examples:

- transaction;
- API call;
- gigabyte;
- device hour;
- kilometre;
- energy unit.

#### Conditional

Examples:

- minimum monthly fee;
- volume discount;
- overage;
- early termination;
- service credit;
- partner commission.

Each charge should have a defined downstream representation.

A sales user should not need to understand the technical configuration.

The solution still needs to know how the quoted term will be executed.

### Stage 4: Apply commercial guardrails

A sales solution should make negotiation easier without allowing uncontrolled commitments.

Possible controls include:

- minimum margin;
- maximum discount;
- permitted contract duration;
- eligible customer segment;
- required legal terms;
- approved payment conditions;
- limit on free usage;
- approval for non-standard cancellation terms.

SAP CPQ currently describes rules-based price controls, margin guardrails and automated approval workflows as product capabilities.

The important design question is not only whether the workflow exists.

It is who owns each rule.

Possible owners include:

- sales operations;
- pricing;
- finance;
- legal;
- product management;
- risk.

The IT team implements the rule.

It should not invent the commercial policy.

### Stage 5: Generate the quotation

The customer-facing proposal should clearly explain:

- products and services;
- contract period;
- recurring fees;
- one-time fees;
- included usage;
- usage rates;
- minimum commitments;
- discounts;
- payment conditions;
- renewal;
- cancellation.

The legal text and the configured price must describe the same commercial model.

A common failure is that:

- CPQ contains one price structure;
- the contract attachment contains additional conditions;
- the billing system receives only part of them.

This creates contract leakage.

The company should not depend on consultants reading signed PDFs and manually translating terms into billing configuration.

### Stage 6: Create the commercial agreement

After acceptance, the quote must become a structured agreement.

The agreement should preserve:

- customer;
- sold package;
- effective dates;
- charge structure;
- price version;
- usage model;
- approved exceptions;
- payment terms;
- renewal rules;
- fulfilment requirements.

The transition from quote to contract should not lose information.

It should also not carry irrelevant sales data into the billing process.

The architecture needs a defined commercial handover object.

### Stage 7: Create and activate the subscription

The subscription represents the running commercial relationship.

Activation may depend on:

- contract signature;
- credit approval;
- payment confirmation;
- implementation completion;
- device installation;
- service provisioning;
- customer acceptance.

The company should define whether charges begin on:

- order date;
- contract date;
- activation date;
- first use;
- service acceptance;
- calendar date.

This rule can materially affect revenue and customer disputes.

It should not be left implicit.

### Stage 8: Trigger fulfilment and entitlement

Selling a subscription does not automatically mean the customer can use it.

The solution may need to trigger:

- account provisioning;
- licence assignment;
- device activation;
- service setup;
- partner order;
- physical delivery;
- entitlement creation.

The fulfilment result should return to the commercial process.

Otherwise, the company may bill for a service that was never activated.

Or it may provide a service that never became billable.

### Stage 9: Collect and rate usage

For a usage-based component, the solution receives consumption data.

The process should identify:

- customer;
- subscription;
- service;
- period;
- unit;
- quantity;
- unique event;
- source system.

SAP Subscription Billing currently describes collection of high-volume data from multiple systems, enrichment, aggregation, correlation, splitting and quality validation as supported capabilities.

The sales design affects this process.

If the quote contains a usage unit that operational systems cannot produce reliably, billing will fail.

For example:

> Price per successful business transaction

requires a clear definition of “successful.”

Is it:

- API accepted;
- order created;
- delivery completed;
- payment received?

The commercial metric must be technically measurable.

### Stage 10: Create the invoice

The invoice may combine:

- recurring fee;
- one-time fee;
- usage;
- discounts;
- credits;
- taxes;
- adjustments;
- partner charges.

SAP states that Subscription Billing can combine and aggregate data from multiple sources into a billing stream and support unified customer invoices.

Contract accounting and invoicing can also converge rated events and bills from multiple billing sources into a single invoice.

The invoice should remain understandable.

The customer should see a clear relationship between:

- contracted offer;
- consumed service;
- applied price;
- billed amount.

### Stage 11: Manage receivables and payment

The commercial process does not end when the invoice is generated.

The solution must manage:

- receivable;
- payment;
- allocation;
- dunning;
- dispute;
- credit;
- write-off;
- refund.

SAP’s current contract accounting and invoicing offering includes a high-volume subledger, payment processing, reconciliation and integration with S/4HANA Finance.

Sales teams need visibility into important payment and dispute status.

They should not receive full accounting authority.

The solution should expose the customer relationship without mixing responsibilities.

## The most important object is the commercial offer

Many implementations begin with applications and interfaces.

A stronger design begins with the commercial object.

Consider this example:

### Connected Equipment Premium Plan

The customer buys:

- one connected industrial device;
- installation;
- monthly monitoring;
- 1,000 included operating hours;
- usage charge above the allowance;
- premium support;
- two-year commitment.

The offer contains different operational elements:

| Commercial element | Downstream responsibility |
|---|---|
| Device | Sales and fulfilment |
| Installation | Service order |
| Monitoring subscription | Subscription lifecycle |
| Included hours | Rating allowance |
| Overage | Usage rating |
| Premium support | Entitlement |
| Two-year discount | Pricing and contract |
| Invoice | Billing and invoicing |
| Payment | Contract accounting |

If the solution models only the monthly charge, most of the commercial promise remains outside the controlled process.

### Create one offer model, not several conflicting catalogues

Complex sales landscapes often develop several catalogues:

- CRM product catalogue;
- CPQ catalogue;
- ERP material catalogue;
- subscription catalogue;
- billing charge catalogue;
- entitlement catalogue;
- external platform catalogue.

These catalogues serve different purposes.

They still need governance.

The organization should define:

- which catalogue creates the commercial offer;
- which system owns technical fulfilment products;
- how identifiers are mapped;
- how versions are synchronized;
- which change triggers downstream updates;
- how old contract versions remain reproducible.

The goal does not need to be one physical catalogue.

The goal is one governed commercial meaning.

### The signed quote must remain reproducible

Months after contract activation, the company may need to explain:

- why the customer received a specific price;
- which discount was approved;
- which catalogue version applied;
- what usage allowance was included;
- when a contract change became effective.

The system should preserve the commercial state used at the time of sale.

It is not enough to look at the current catalogue.

The current product may have:

- a new price;
- different included usage;
- new eligibility;
- changed terms.

Historical reproducibility is essential for:

- disputes;
- corrections;
- audit;
- renewals;
- contract migration.

### Separate list price, negotiated price and rated price

These values may differ.

#### List price

The standard commercial price.

#### Negotiated price

The value agreed with the customer.

#### Rated price

The price actually applied to a usage event under the valid contract rules.

The architecture should preserve the connection between them.

A discount approved in CPQ must reach the subscription and rating process correctly.

A later catalogue update must not overwrite the agreed contract price unless the contract explicitly permits it.

### Deal approval should examine future operational cost

A commercially attractive deal can be operationally expensive.

For example:

- non-standard billing calendar;
- manual usage source;
- customer-specific invoice layout;
- unique price calculation;
- special payment allocation;
- custom partner settlement.

The sales margin may look acceptable.

The cost of operating the exception may remove that margin.

Deal approval should therefore consider:

- billing complexity;
- implementation effort;
- ongoing exception handling;
- invoice dispute risk;
- integration cost;
- support dependency.

CPQ margin controls are useful.

The full margin model may need operational cost, not only product cost.

### Avoid unlimited commercial flexibility

Sales teams often request the ability to create any possible deal.

This sounds customer-centric.

It can produce an unmanageable platform.

Every unique combination may create:

- new billing rules;
- new tests;
- new invoice explanations;
- new support procedures;
- additional reconciliation.

A scalable model usually has:

- standard offers;
- controlled options;
- approved exception paths;
- explicit non-standard deal review.

The objective is configurable flexibility, not unrestricted creativity.

### Contract changes need their own sales process

After activation, the customer may request:

- more users;
- lower service level;
- additional device;
- temporary pause;
- early renewal;
- cancellation;
- contract extension;
- new pricing.

This is not always a new sale.

It is a change to a running commercial relationship.

The process should determine:

- effective date;
- proration;
- impact on usage allowance;
- impact on entitlement;
- whether fulfilment changes;
- whether a credit or new charge is required;
- whether the change needs approval.

SAP Subscription Billing currently states support for subscription lifecycle changes and automatic renewals.

The business still needs to define which changes are allowed and how they should be sold.

### Backdated changes should be restricted

A sales user may request:

> Apply the new discount from the beginning of last month.

This can affect:

- already rated usage;
- issued invoices;
- receivables;
- tax;
- payments;
- financial reporting.

The sales solution should not treat a backdated update as a simple contract-field change.

It should trigger a controlled correction process.

That process may include:

1. identify affected charges;
2. simulate rerating;
3. calculate credits or debits;
4. review accounting impact;
5. obtain approval;
6. execute correction;
7. communicate with the customer.

### Quote-to-cash needs end-to-end ownership

Each system may have an owner.

The complete process also needs an owner.

Possible system owners include:

- Sales Cloud owner;
- CPQ owner;
- subscription platform owner;
- billing owner;
- contract accounting owner;
- integration owner.

Without an end-to-end owner, failures move between teams.

For example:

- CPQ says the quote was correct.
- Subscription Billing says the contract was received.
- Billing says usage was missing.
- Integration says the source did not provide the correct customer key.
- Sales says the customer should already be invoiced.

Every system may be technically correct.

The business process still failed.

A quote-to-cash owner should be accountable for the complete commercial result.

### Define the source of truth for every object

A practical ownership table may look like this:

| Business object | Possible authoritative system |
|---|---|
| Account and opportunity | Sales Cloud |
| Offer configuration | CPQ |
| Approved quote | CPQ |
| Subscription | Subscription Billing or contract system |
| Entitlement | Entitlement or fulfilment platform |
| Usage event | Operational source |
| Rated charge | Rating platform |
| Invoice | Billing and invoicing |
| Receivable | Contract accounting |
| General ledger | S/4HANA Finance |

The exact systems can differ.

Ambiguity should not.

### Sales analytics should include revenue quality

A normal sales dashboard focuses on:

- pipeline;
- conversion;
- forecast;
- deal size;
- sales cycle.

A subscription model also needs:

- active recurring revenue;
- contracted usage;
- activation delay;
- unbilled usage;
- failed subscription creation;
- billing disputes;
- payment status;
- churn;
- contract changes.

The sales organization should understand whether signed business became operational revenue.

A signed quote that cannot be activated or billed is not a successful sale.

### Automation opportunities in the BRIM sales process

Several stages are suitable for automation.

### Offer eligibility

Automation can check whether:

- product is available in the region;
- customer meets eligibility;
- required base product exists;
- service combination is valid.

### Price and margin control

Rules can check:

- minimum margin;
- discount authority;
- commitment period;
- customer segment;
- special conditions.

### Approval routing

Workflow can route:

- discount approval;
- legal exception;
- payment-term exception;
- unusual contract term;
- non-standard operational requirement.

### Quote-to-subscription validation

Before activation, automation can verify:

- required identifiers;
- complete pricing;
- effective dates;
- usage definitions;
- approved terms;
- fulfilment dependencies.

### Activation monitoring

Automation can identify:

- accepted quote not converted;
- subscription not activated;
- fulfilment incomplete;
- entitlement missing;
- billing start delayed.

### Billing-readiness checks

Before the first billing cycle, verify:

- subscription active;
- price available;
- usage source connected;
- customer account ready;
- payment conditions valid;
- invoice recipient available.

### AI-assisted sales work

AI may help:

- summarize customer requirements;
- recommend standard packages;
- identify missing commercial information;
- draft proposal text;
- explain contract options;
- detect unusual terms.

AI should not invent prices or approve non-standard financial commitments.

### A practical implementation sequence

### Phase 1: Choose one sellable offer

Select one real subscription or usage-based product.

Avoid starting with the complete portfolio.

### Phase 2: Define the commercial model

Document:

- customer promise;
- charge types;
- contract term;
- usage;
- renewal;
- cancellation;
- fulfilment;
- invoice;
- payment.

### Phase 3: Define product and price ownership

Assign responsibility for:

- catalogue;
- price;
- discount;
- entitlement;
- usage definition;
- billing rule.

### Phase 4: Design the quote

Make sure the customer-facing offer can be represented downstream.

### Phase 5: Define the quote-to-subscription handover

Specify every required field, identifier and approval.

### Phase 6: Connect fulfilment

Ensure that sold services become usable and that activation is confirmed.

### Phase 7: Connect rating and billing

Verify that negotiated terms produce the expected charges.

### Phase 8: Connect receivables

Confirm invoice, payment and reconciliation.

### Phase 9: Test the complete lifecycle

Include:

- new sale;
- activation;
- usage;
- invoice;
- payment;
- upgrade;
- downgrade;
- cancellation;
- correction.

### Phase 10: Scale through standard patterns

Add more products only when the first pattern operates reliably.

### A strong pilot scenario

A practical pilot could be:

> Business software subscription with a base monthly fee, 100 included users and a per-user charge above the allowance.

#### Sales process

- opportunity created;
- seller configures plan;
- seller selects contract term;
- approved discount applied;
- quote generated and accepted.

#### Subscription process

- subscription created;
- billing start date confirmed;
- included user allowance stored;
- renewal rule activated.

#### Usage process

- active-user count received monthly;
- duplicate usage record rejected;
- usage linked to the correct subscription.

#### Billing process

- base fee calculated;
- included users excluded;
- excess users charged;
- discount applied;
- invoice generated.

#### Finance process

- receivable created;
- payment received and allocated;
- posting reconciled.

#### Contract-change test

- customer adds users mid-period;
- effective date applied;
- proration calculated;
- next invoice explains the change.

#### Success measures

- quote-to-activation time;
- manual handover effort;
- first-invoice accuracy;
- billing exception rate;
- contract-change processing time;
- customer dispute rate.

### Common mistakes

### Mistake 1: Starting the design with billing

The commercial promise is created earlier in the sales process.

### Mistake 2: Letting sales quote conditions that cannot be executed

Every term must have a downstream representation.

### Mistake 3: Maintaining several unrelated product models

Different catalogues need shared governance and identifiers.

### Mistake 4: Losing negotiated terms after quote acceptance

The subscription must preserve the approved commercial state.

### Mistake 5: Activating billing before fulfilment

The customer may be charged before the service is usable.

### Mistake 6: Using technical usage that does not match the commercial definition

The billed metric must be measurable and explainable.

### Mistake 7: Allowing unlimited non-standard deals

Every exception creates operational cost.

### Mistake 8: Treating upgrades and cancellations as simple field updates

They can affect charges, usage, entitlement and invoicing.

### Mistake 9: Separating sales success from billing success

Signed contracts should be tracked through activation and revenue.

### Mistake 10: Giving each application ownership but nobody process ownership

Quote-to-cash needs one end-to-end accountable owner.

### Questions managers should ask

1. What exactly is the customer buying?
2. Can every quoted term be represented in the subscription and billing systems?
3. Which system owns the offer?
4. Which system owns the negotiated price?
5. How are non-standard discounts approved?
6. What triggers the billing start date?
7. How is fulfilment confirmed?
8. Which operational event represents billable usage?
9. Can the customer understand the invoice?
10. How are upgrades and cancellations handled?
11. What happens after a backdated change?
12. How much operational cost does a non-standard deal create?
13. Can sales see whether the contract became billable revenue?
14. Who owns the complete quote-to-cash process?
15. Can every invoice be traced back to the accepted quotation?

### The goal is an executable commercial promise

A BRIM sales solution should not be evaluated only by how quickly a salesperson can create a quote.

The quote is only the beginning.

The stronger measure is whether the accepted offer can move through the complete lifecycle without manual reinterpretation:

- configured correctly;
- approved correctly;
- converted to a subscription;
- fulfilled;
- measured;
- rated;
- invoiced;
- collected;
- reconciled.

SAP’s current portfolio provides separate capabilities for sales automation, complex quoting, subscription lifecycle and flexible charging, unified invoices, and high-volume contract accounting.

The architecture still needs one coherent commercial model.

Without it, the company may implement several capable products and continue managing the most important contract conditions manually.

The sales solution should therefore be designed around one principle:

> Every promise made during the sale must become structured, executable and traceable through billing and payment.

That is the real role of BRIM in sales.

---

### BRIM sales-solution design checklist

- [ ] Opportunity data captures expected commercial and usage context.
- [ ] Product configuration prevents invalid offer combinations.
- [ ] One-time, recurring and usage charges are clearly separated.
- [ ] Discount and margin guardrails have business owners.
- [ ] Non-standard terms follow controlled approval.
- [ ] The customer proposal and system price describe the same deal.
- [ ] Accepted quotation data remains structured.
- [ ] Negotiated conditions are preserved historically.
- [ ] Quote-to-subscription handover is complete and validated.
- [ ] Billing start is connected to the correct activation event.
- [ ] Fulfilment and entitlement status return to the commercial process.
- [ ] Usage definitions are commercially and technically measurable.
- [ ] Duplicate and late usage rules are defined.
- [ ] Multiple billing streams can be explained on the invoice.
- [ ] Contract changes include effective-date and proration rules.
- [ ] Backdated changes use controlled correction.
- [ ] Each commercial object has an authoritative system.
- [ ] Quote-to-cash has an end-to-end owner.
- [ ] Sales performance includes activation and billing outcomes.
- [ ] The first implementation uses one complete commercial scenario.
- [ ] Expansion follows reusable product and process patterns.

### Sources and further reading

SAP currently describes SAP Sales Cloud as supporting sales automation, customer acquisition, guided selling, pipeline and forecast management, analytics and AI-assisted sales processes.

SAP CPQ currently supports configuration and quotation of complex products and services, customer- and channel-specific pricing, margin guardrails, approval workflows, proposal generation and connection with CRM, commerce and ERP platforms. SAP also states that quotes can combine subscriptions, services and hardware.

SAP Subscription Billing currently supports one-time, recurring and usage-based fees, flexible subscription changes, real-time and offline rating, customer-specific offerings, data enrichment, unified billing streams and integration with order-to-cash processes.

SAP S/4HANA Cloud for contract accounting and invoicing currently supports convergence of billing streams, subscription- and consumption-based invoicing, high-volume receivables and payments through a unified subledger, and integration with S/4HANA Finance.

*Reviewed: July 2026. SAP product naming, packaging, licensing and supported integration scenarios can change. The final sales architecture should be verified against the current SAP documentation and the organization’s real commercial model.*

## Continue exploring

- [When Standard SAP Billing Is No Longer Enough: What SAP BRIM Actually Solves](/blog/when-standard-sap-billing-is-no-longer-enough-what-sap-brim-actually/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [When Standard SAP Billing Is No Longer Enough: What SAP BRIM Actually Solves](/blog/when-standard-sap-billing-is-no-longer-enough-what-sap-brim-actually/)
- Next in the migration: [Where Automation Actually Makes Sense in SAP SD Sales Order Processing](/blog/where-automation-actually-makes-sense-in-sap-sd-sales-order-processing/)
