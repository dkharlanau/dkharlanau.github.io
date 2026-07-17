---
layout: blog
title: "Why SAP Retail Is Not Just SAP MM and SD: The Complete Architecture from Product Onboarding to Omnichannel Fulfilment"
description: "products are materials; - stores are plants; - purchases are purchase orders; - sales are sales orders; - stock is inventory; - customers are."
slug: why-sap-retail-is-not-just-sap-mm-and-sd-the-complete-architecture-from
permalink: /blog/why-sap-retail-is-not-just-sap-mm-and-sd-the-complete-architecture-from/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP industry solutions"
tags:
  - sap-industry-solutions
  - ai-operations
  - sap-architecture
  - retail
canonical_url: https://dkharlanau.github.io/blog/why-sap-retail-is-not-just-sap-mm-and-sd-the-complete-architecture-from/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 41
migration_sequence: 44
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/why-sap-car-becomes-the-most-important-retail-system-nobody-can-clearly/
  - /blog/sap-for-automotive-explained-the-complete-architecture-from-engineering/
---

## On this page

- [What “SAP for Retail” means today](#what-sap-for-retail-means-today)
- [The retail operating model](#the-retail-operating-model)
- [The merchandise-management core](#the-merchandise-management-core)
- [Part I: The retail organizational model](#part-i-the-retail-organizational-model)
- [Company code](#company-code)
- [Purchasing organization](#purchasing-organization)
- [Sales organization and distribution channel](#sales-organization-and-distribution-channel)
- [Site](#site)
- [Store versus distribution centre](#store-versus-distribution-centre)
- [Storage location and warehouse number](#storage-location-and-warehouse-number)
- [Part II: Retail product and article master](#part-ii-retail-product-and-article-master)
- [Article versus material](#article-versus-material)
- [Single article](#single-article)
- [Generic article and variants](#generic-article-and-variants)
- [Structured and grouped product concepts](#structured-and-grouped-product-concepts)
- [Merchandise category](#merchandise-category)
- [Product hierarchy and category management](#product-hierarchy-and-category-management)
- [Units of measure and packaging hierarchy](#units-of-measure-and-packaging-hierarchy)
- [GTIN and barcode management](#gtin-and-barcode-management)
- [Product lifecycle states](#product-lifecycle-states)
- [Product onboarding integration](#product-onboarding-integration)
- [Part III: Supplier and sourcing model](#part-iii-supplier-and-sourcing-model)
- [Business partner and supplier](#business-partner-and-supplier)
- [Purchasing info and source relationships](#purchasing-info-and-source-relationships)
- [Contracts and scheduling agreements](#contracts-and-scheduling-agreements)
- [Supplier collaboration](#supplier-collaboration)
- [Direct store delivery](#direct-store-delivery)
- [Cross-docking and flow-through](#cross-docking-and-flow-through)
- [Part IV: Assortment and listing](#part-iv-assortment-and-listing)
- [Assortment](#assortment)
- [Listing](#listing)
- [Listing is not inventory](#listing-is-not-inventory)
- [Listing is not only a technical extension](#listing-is-not-only-a-technical-extension)
- [Store clustering](#store-clustering)
- [Assortment Planning and CAR](#assortment-planning-and-car)
- [Part V: Retail pricing](#part-v-retail-pricing)
- [Purchase price versus retail price](#purchase-price-versus-retail-price)
- [Price zones](#price-zones)
- [Price publication](#price-publication)
- [Promotional pricing](#promotional-pricing)
- [Omnichannel Promotion Pricing](#omnichannel-promotion-pricing)
- [Offline stores](#offline-stores)
- [Returns and promotion reconstruction](#returns-and-promotion-reconstruction)
- [Supplier-funded promotions](#supplier-funded-promotions)
- [Part VI: Planning, allocation and replenishment](#part-vi-planning-allocation-and-replenishment)
- [Merchandise financial planning](#merchandise-financial-planning)
- [Assortment planning](#assortment-planning)
- [Allocation](#allocation)
- [Replenishment](#replenishment)
- [Allocation Management](#allocation-management)
- [Replenishment](#replenishment)
- [Order and Delivery Scheduling](#order-and-delivery-scheduling)
- [Fresh products](#fresh-products)
- [Fashion and seasonal retail](#fashion-and-seasonal-retail)
- [Part VII: Distribution-centre execution](#part-vii-distribution-centre-execution)
- [SAP EWM](#sap-ewm)
- [Store order versus e-commerce order](#store-order-versus-e-commerce-order)
- [Allocation to warehouse execution](#allocation-to-warehouse-execution)
- [Distribution-centre replenishment](#distribution-centre-replenishment)
- [Transportation Management](#transportation-management)
- [Part VIII: Store operations](#part-viii-store-operations)
- [Store receiving](#store-receiving)
- [Shelf replenishment](#shelf-replenishment)
- [Inventory adjustment](#inventory-adjustment)
- [RFID](#rfid)
- [Store fulfilment](#store-fulfilment)
- [Part IX: POS, CAR and financial posting](#part-ix-pos-car-and-financial-posting)
- [POS outbound integration](#pos-outbound-integration)
- [POS inbound integration](#pos-inbound-integration)
- [Sales audit](#sales-audit)
- [Aggregation](#aggregation)
- [Tender reconciliation](#tender-reconciliation)
- [Part X: Omnichannel commerce and order management](#part-x-omnichannel-commerce-and-order-management)
- [Commerce Cloud](#commerce-cloud)
- [Order Management foundation](#order-management-foundation)
- [Sourcing and availability](#sourcing-and-availability)
- [Inventory visibility versus availability](#inventory-visibility-versus-availability)
- [aATP versus OMS availability](#aatp-versus-oms-availability)
- [Sourcing objectives](#sourcing-objectives)
- [Ship from store](#ship-from-store)
- [Click and collect](#click-and-collect)
- [Endless aisle](#endless-aisle)
- [Returns](#returns)
- [Part XI: The integration architecture](#part-xi-the-integration-architecture)
- [Master-data integration](#master-data-integration)
- [Transactional APIs](#transactional-apis)
- [Events](#events)
- [High-volume replication](#high-volume-replication)
- [Batch and file integration](#batch-and-file-integration)
- [Integration Suite](#integration-suite)
- [Product integration map](#product-integration-map)
- [Inventory integration map](#inventory-integration-map)
- [Order integration map](#order-integration-map)
- [Sales integration map](#sales-integration-map)
- [Supplier integration map](#supplier-integration-map)
- [Part XII: Finance and profitability](#part-xii-finance-and-profitability)
- [Inventory valuation](#inventory-valuation)
- [Cost of goods sold](#cost-of-goods-sold)
- [Markdown](#markdown)
- [Shrinkage](#shrinkage)
- [Gross margin return on inventory](#gross-margin-return-on-inventory)
- [Vendor rebates](#vendor-rebates)
- [Part XIII: Data and analytics](#part-xiii-data-and-analytics)
- [CAR as operational retail data foundation](#car-as-operational-retail-data-foundation)
- [Business Data Cloud and Datasphere](#business-data-cloud-and-datasphere)
- [Real-time versus historical truth](#real-time-versus-historical-truth)
- [AI in retail](#ai-in-retail)
- [Part XIV: Main limitations and traps](#part-xiv-main-limitations-and-traps)
- [Trap 1: Treating Retail as a standard ERP template](#trap-1-treating-retail-as-a-standard-erp-template)
- [Trap 2: Extending every product to every site](#trap-2-extending-every-product-to-every-site)
- [Trap 3: Using one product hierarchy for every purpose](#trap-3-using-one-product-hierarchy-for-every-purpose)
- [Trap 4: Making CAR the owner of everything](#trap-4-making-car-the-owner-of-everything)
- [Trap 5: Publishing stock without reservation](#trap-5-publishing-stock-without-reservation)
- [Trap 6: Calculating promotions in every channel](#trap-6-calculating-promotions-in-every-channel)
- [Trap 7: Running several forecast engines without authority](#trap-7-running-several-forecast-engines-without-authority)
- [Trap 8: Replenishing against sales rather than demand](#trap-8-replenishing-against-sales-rather-than-demand)
- [Trap 9: Ignoring supplier pack size and schedules](#trap-9-ignoring-supplier-pack-size-and-schedules)
- [Trap 10: Using store inventory as if it were perfectly accurate](#trap-10-using-store-inventory-as-if-it-were-perfectly-accurate)
- [Trap 11: Direct integration to tables](#trap-11-direct-integration-to-tables)
- [Trap 12: Confusing inventory, availability and fulfilment capacity](#trap-12-confusing-inventory-availability-and-fulfilment-capacity)
- [Trap 13: Aggregating POS data too early](#trap-13-aggregating-pos-data-too-early)
- [Trap 14: Sending every POS receipt to ERP individually](#trap-14-sending-every-pos-receipt-to-erp-individually)
- [Trap 15: Migrating ECC Retail configuration one to one](#trap-15-migrating-ecc-retail-configuration-one-to-one)
- [Trap 16: Assuming cloud products replace the merchandise core](#trap-16-assuming-cloud-products-replace-the-merchandise-core)
- [Trap 17: Creating one omnichannel order in several systems](#trap-17-creating-one-omnichannel-order-in-several-systems)
- [Trap 18: Ignoring degraded operations](#trap-18-ignoring-degraded-operations)
- [Part XV: Modern target architectures](#part-xv-modern-target-architectures)
- [Architecture A: Traditional store-centric retailer](#architecture-a-traditional-store-centric-retailer)
- [Architecture B: Omnichannel retailer](#architecture-b-omnichannel-retailer)
- [Architecture C: High-volume grocery](#architecture-c-high-volume-grocery)
- [Architecture D: Fashion and seasonal](#architecture-d-fashion-and-seasonal)
- [Architecture E: Multi-ERP global retailer](#architecture-e-multi-erp-global-retailer)
- [Part XVI: Migration to S/4HANA Retail](#part-xvi-migration-to-s-4hana-retail)
- [Product migration](#product-migration)
- [Site migration](#site-migration)
- [Supplier and Business Partner conversion](#supplier-and-business-partner-conversion)
- [Pricing and promotions](#pricing-and-promotions)
- [POS integration](#pos-integration)
- [CAR integration](#car-integration)
- [Inventory cutover](#inventory-cutover)
- [Open documents](#open-documents)
- [Parallel operations](#parallel-operations)
- [Part XVII: Implementation approach](#part-xvii-implementation-approach)
- [Phase 1: Define the retail business model](#phase-1-define-the-retail-business-model)
- [Phase 2: Assign system authority](#phase-2-assign-system-authority)
- [Phase 3: Build identity model](#phase-3-build-identity-model)
- [Phase 4: Design lifecycle before interfaces](#phase-4-design-lifecycle-before-interfaces)
- [Phase 5: Design integration contracts](#phase-5-design-integration-contracts)
- [Phase 6: Pilot one complete flow](#phase-6-pilot-one-complete-flow)
- [Phase 7: Measure operational results](#phase-7-measure-operational-results)
- [Questions managers and architects should ask](#questions-managers-and-architects-should-ask)
- [The management conclusion](#the-management-conclusion)

A retailer implements SAP S/4HANA.

The project team says that most processes already exist in standard ERP:

- products are materials;
- stores are plants;
- purchases are purchase orders;
- sales are sales orders;
- stock is inventory;
- customers are business partners.

Technically, these statements are partly correct.

Operationally, they miss the nature of retail.

A manufacturer may manage tens of thousands of materials and a limited number of customers.

A retailer may manage:

- millions of product-location combinations;
- thousands of stores and fulfilment nodes;
- hundreds of price and promotion changes every day;
- short product lifecycles;
- seasonal collections;
- supplier-funded promotions;
- point-of-sale transactions at receipt level;
- store inventory that changes every few seconds;
- online orders competing with physical shoppers for the same stock.

The problem is not simply processing more documents.

Retail has a different operating model.

A product is not usable merely because its master record exists.

It must also be:

- ranged for the relevant channel;
- listed for the location;
- purchasable from an approved source;
- priced;
- replenishable;
- delivered in the right pack;
- sellable at POS;
- visible online;
- eligible for promotions;
- available for fulfilment.

That is why SAP Retail should not be understood as “MM and SD with some additional fields.”

It is an industry-specific merchandise, supply, store, sales and financial model.

SAP currently positions its retail portfolio around connected merchandise management, demand and supply planning, omnichannel commerce, store fulfilment, customer activity and financial operations. Its current merchandise-management product is SAP S/4HANA Retail for merchandise management, while adjacent capabilities are supplied through CAR, Commerce Cloud, Order Management, Predictive Replenishment, EWM, TM and other applications.

The main architectural lesson is:

> SAP for Retail is not one product. It is a set of bounded systems that must share one product, location, price, inventory and order model.

## What “SAP for Retail” means today

The terminology is often used inconsistently.

### SAP for Retail

This is the broad retail solution landscape.

It may include:

- SAP S/4HANA Retail for merchandise management;
- SAP Customer Activity Repository;
- SAP Commerce Cloud;
- SAP Order Management;
- SAP Omnichannel Promotion Pricing;
- SAP Predictive Replenishment;
- SAP Order and Delivery Scheduling;
- SAP EWM;
- SAP TM;
- SAP Business Network;
- planning, finance, workforce and data applications.

SAP’s current retail portfolio explicitly spans merchandising, supply-chain orchestration, commerce, order sourcing, customer engagement, finance and workforce processes.

### SAP Retail or SAP S/4HANA Retail

This normally refers to the ERP-based retail merchandise-management core.

It contains retail-specific capabilities built into the S/4HANA business model.

SAP currently describes SAP S/4HANA Retail for merchandise management as connecting finance, supply chain, manufacturing, sales, store operations and merchandise processes, with deployment options including on-premises, cloud and hybrid models.

### SAP CAR

This is the customer-activity and retail-planning foundation used for detailed sales, demand, selected retail planning and omnichannel scenarios.

SAP currently positions CAR as a multichannel sales repository and planning foundation with inventory visibility, forecasting, assortment, allocation, replenishment and promotion capabilities.

### SAP Commerce Cloud

This is the customer-facing commerce platform.

It manages areas such as:

- storefront;
- product discovery;
- cart;
- checkout;
- commerce account;
- commerce pricing and promotions;
- order capture.

SAP currently positions Commerce Cloud for B2B, B2C and B2B2C commerce, product catalogues, pricing, promotions, search and composable storefronts.

### SAP Order Management

This provides a separate omnichannel orchestration layer when orders must be coordinated across several sales channels and fulfilment systems.

SAP Order Management foundation currently centralizes order, fulfilment and return processes and routes orders across distributed fulfilment systems through a cloud-native, API-first architecture.

These applications overlap around some data.

They should not have overlapping authority.

## The retail operating model

A complete retail lifecycle can be represented as:

```text
Product strategy
→ product onboarding
→ assortment and listing
→ sourcing and purchasing
→ allocation and replenishment
→ distribution-centre execution
→ store or channel availability
→ pricing and promotion
→ customer sale
→ POS and financial settlement
→ returns, markdown and lifecycle exit
```

A retailer must coordinate three connected flows.

### Merchandise flow

The physical movement of goods:

```text
Supplier
→ distribution centre
→ store or fulfilment node
→ customer
```

### Information flow

The movement of:

- product data;
- prices;
- promotions;
- orders;
- inventory;
- sales;
- forecasts;
- supplier confirmations.

### Financial flow

The movement of:

- purchase commitments;
- supplier invoices;
- inventory valuation;
- customer payments;
- tax;
- revenue;
- rebates;
- markdowns;
- shrinkage.

SAP Retail is valuable when these flows remain connected.

It becomes difficult when every flow has a different owner, key and timing model.

## The merchandise-management core

SAP S/4HANA Retail for merchandise management is normally the operational core.

Typical responsibilities include:

- product and article data;
- sites;
- merchandise categories;
- assortment and listing;
- purchasing;
- stock transfers;
- inventory valuation;
- sales posting;
- supplier settlement;
- retail pricing;
- finance.

SAP’s current product scope includes customer-centric merchandise management, supplier synchronization, omnichannel price and promotion information, stock segmentation, store operations and connected retail supply-chain processes.

This core should normally own financially and operationally binding merchandise transactions.

CAR, Commerce and planning applications may enrich or consume the information.

They should not silently become replacement ERPs.

## Part I: The retail organizational model

Retail organizational design is one of the first places where a standard ERP mindset creates problems.

## Company code

The company code represents the legal accounting entity.

It determines areas such as:

- financial statements;
- local currency;
- statutory accounting;
- tax and legal reporting.

Stores and distribution centres may belong to the same or different company codes.

This matters for:

- stock transfers;
- intercompany movements;
- inventory ownership;
- pricing;
- tax;
- transfer pricing.

## Purchasing organization

The purchasing organization represents procurement responsibility.

Possible models include:

- one central purchasing organization;
- purchasing by country;
- category-specific purchasing;
- local store purchasing;
- hybrid centralized and local procurement.

The design affects:

- supplier agreements;
- contract ownership;
- purchasing prices;
- source determination;
- responsibility.

## Sales organization and distribution channel

These represent the selling structure.

Retailers may distinguish:

- physical stores;
- online;
- marketplace;
- wholesale;
- franchise;
- outlet;
- mobile.

A distribution channel should not be created merely because a technical application exists.

It should represent a meaningful commercial distinction.

## Site

The site is one of the most important retail objects.

A site may represent:

- store;
- distribution centre;
- fulfilment centre;
- dark store;
- outlet;
- warehouse-linked location.

A site is usually connected to the plant concept but enriched with retail-specific meaning.

The site determines or influences:

- inventory;
- assortment;
- purchasing;
- receiving;
- selling;
- replenishment;
- valuation;
- delivery;
- tax;
- opening calendar.

The retail site is not merely a warehouse address.

It is an operational and commercial node.

## Store versus distribution centre

Both can be represented through site-related structures.

But their business roles differ.

### Store

Normally:

- receives goods;
- holds selling stock;
- sells to consumers;
- performs returns;
- may fulfil online orders;
- reports POS activity.

### Distribution centre

Normally:

- receives bulk supply;
- stores merchandise;
- allocates and replenishes stores;
- fulfils e-commerce;
- consolidates supplier deliveries.

A dark store or hybrid node can perform both store and fulfilment roles.

The architecture should describe capabilities rather than rely only on one site type.

## Storage location and warehouse number

A plant or site may contain several storage locations.

Examples:

- selling area;
- back room;
- returns;
- damaged goods;
- quality;
- e-commerce stock;
- blocked inventory.

Where EWM is used, the detailed warehouse model is managed through:

- warehouse number;
- storage type;
- storage section;
- bin;
- handling unit;
- stock type.

Do not use storage locations to reproduce every physical warehouse bin.

Do not hide commercially separate inventory inside one undifferentiated location either.

## Part II: Retail product and article master

The retail product model is more complex than a conventional material record.

A retail product may have:

- consumer description;
- supplier description;
- brand;
- merchandise category;
- variants;
- size;
- colour;
- season;
- barcode;
- packaging hierarchy;
- purchasing units;
- selling units;
- country-specific attributes;
- channel content;
- shelf-life rules.

## Article versus material

In SAP Retail terminology, the business often speaks about articles.

At database and S/4HANA platform level, the product remains connected with the broader material or product model.

The important difference is not only the name.

Retail-specific behaviour includes:

- article categories;
- variants;
- merchandise categories;
- assortments;
- listing;
- store distribution;
- retail pricing;
- sales-unit handling.

## Single article

A single article represents an independently managed sellable product.

Examples:

- one bottle of water;
- one television;
- one package of detergent.

It can have:

- its own GTIN;
- purchasing data;
- sales data;
- valuation;
- stock;
- listing.

## Generic article and variants

A generic article groups related sellable variants.

Example:

```text
Generic article: Running Shoe Model A

Variants:
Black / Size 40
Black / Size 41
Blue / Size 40
Blue / Size 41
```

The generic article can hold common data.

Variants hold differentiating values.

This is particularly important in fashion and apparel.

The risk is variant explosion.

A model with:

- 10 colours;
- 15 sizes;
- 4 fits;
- 3 seasons

can generate thousands of product combinations.

The company should create only valid, sellable variants.

## Structured and grouped product concepts

Traditional SAP Retail models may also use specialised article structures for:

- displays;
- sets;
- pre-packs;
- grouped merchandise;
- empties or returnable packaging.

Exact object support and terminology depend on the S/4HANA release and industry configuration.

The architecture should distinguish:

- what is sold;
- what is purchased;
- what is physically packed;
- what is inventoried.

A display bought as one supplier unit but sold as individual consumer units requires clear component and inventory logic.

## Merchandise category

The merchandise category is a central retail classification.

It may influence:

- purchasing responsibility;
- assortment;
- hierarchy;
- planning;
- reporting;
- valuation;
- pricing;
- product defaults.

Examples:

```text
Food
  └─ Dairy
      └─ Yogurt
```

or:

```text
Fashion
  └─ Women
      └─ Footwear
          └─ Running shoes
```

A merchandise category should represent stable business management.

It should not be redesigned every season only to satisfy one report.

## Product hierarchy and category management

Retailers may need several hierarchies:

- merchandise hierarchy;
- web navigation;
- financial reporting;
- supplier category;
- marketing category;
- planning hierarchy.

One hierarchy rarely satisfies every use case.

The architecture should define one authoritative hierarchy for each meaning.

Do not force Commerce navigation into the ERP merchandise hierarchy if the commercial purposes are different.

## Units of measure and packaging hierarchy

Retail products may be purchased, transported, stored and sold in different units.

Example:

```text
1 pallet
= 40 cases

1 case
= 12 consumer units
```

The system must understand:

- base unit;
- order unit;
- selling unit;
- issue unit;
- conversion;
- GTIN by level;
- dimensions and weight.

Incorrect conversions affect:

- procurement;
- inventory;
- replenishment;
- warehouse capacity;
- transportation;
- POS;
- margin.

A unit error can propagate through the entire retail network.

## GTIN and barcode management

The same product may have barcodes for:

- consumer unit;
- multipack;
- case;
- pallet;
- regional packaging;
- promotional pack.

Barcode governance must prevent:

- duplicate active GTINs;
- reused identifiers;
- wrong unit assignment;
- expired packaging remaining active;
- POS lookup failures.

GTIN is an external trade identifier.

It should not replace the internal product key.

## Product lifecycle states

A product should move through explicit states.

For example:

```text
Proposed
→ Enriched
→ Approved
→ Sourced
→ Listed
→ Active
→ Markdown
→ Delisted
→ Discontinued
→ Archived
```

Different capabilities may become allowed at different states.

A record that exists technically should not automatically be:

- orderable;
- replenishable;
- sellable;
- visible online.

## Product onboarding integration

Product information may originate from:

- supplier;
- product-information management;
- marketplace seller;
- internal category manager;
- global data-synchronization network.

The onboarding process should separate:

1. external supplier data;
2. governed internal product identity;
3. operational ERP extensions;
4. channel content;
5. listing and activation.

A direct supplier spreadsheet upload into the productive product master is not governance.

## Part III: Supplier and sourcing model

A retailer may buy:

- direct from manufacturer;
- from wholesaler;
- from local supplier;
- through import organisation;
- through distribution agreement;
- through consignment.

## Business partner and supplier

In S/4HANA, suppliers are represented through the Business Partner approach.

Supplier data may include:

- legal identity;
- purchasing organization;
- payment terms;
- partner functions;
- bank details;
- tax;
- ordering communication;
- delivery calendars.

Central legal identity and local purchasing data should be distinguished.

## Purchasing info and source relationships

The product-supplier relationship may contain:

- supplier product number;
- order unit;
- planned delivery time;
- price;
- minimum quantity;
- rounding;
- packaging;
- tolerance.

This relationship is essential for replenishment.

The cheapest supplier is not usable if:

- pack size is incompatible;
- lead time is too long;
- product is not approved for the country;
- delivery calendar does not serve the store.

## Contracts and scheduling agreements

Long-term retail sourcing may use:

- purchasing contracts;
- scheduling agreements;
- supplier catalogues;
- central agreements.

The agreement may control:

- price;
- validity;
- target quantity;
- source;
- delivery schedule;
- rebates;
- freight;
- promotion funding.

Operational orders should be traceable to the agreement.

Otherwise, negotiated savings are not realized.

## Supplier collaboration

SAP Business Network Supply Chain Collaboration currently supports forecast sharing, supplier commitments, digital purchase orders, confirmations, shipment visibility, inventory collaboration and supplier-managed inventory scenarios.

A practical flow is:

```text
Retail forecast or replenishment need
→ supplier forecast
→ supplier commitment
→ purchase order
→ order confirmation
→ advance shipment information
→ goods receipt
```

The retailer should distinguish:

- forecast;
- expected order;
- legally binding purchase order;
- supplier-confirmed quantity and date.

A forecast visible to the supplier is not automatically a confirmed supply commitment.

## Direct store delivery

Some suppliers deliver directly to stores.

This can reduce distribution-centre handling.

It increases complexity in:

- store receiving;
- supplier calendars;
- invoice matching;
- returns;
- delivery visibility;
- local inventory.

Direct-store delivery should be used where it creates economic value, not simply because it shortens the physical route.

## Cross-docking and flow-through

Products can sometimes move through a distribution centre without long-term storage.

The flow may be:

```text
Supplier
→ distribution centre receiving
→ store-specific allocation
→ outbound staging
→ store
```

This requires close alignment between:

- inbound quantity;
- allocation;
- store demand;
- transport schedule;
- labelling;
- handling units.

A late supplier delivery can disrupt multiple store shipments.

## Part IV: Assortment and listing

The product master answers:

> What is the product?

Assortment answers:

> Which product should be offered in which market, store or channel?

Listing answers:

> During which period is the product permitted or expected to be handled at the location?

These are foundational retail concepts.

## Assortment

An assortment represents a set of products relevant to a group of sites or channels.

Possible assortments include:

- all large urban stores;
- convenience format;
- premium stores;
- online channel;
- regional cluster;
- airport stores.

A site may belong to one or more assortment structures depending on the design.

## Listing

Listing creates the valid relationship between:

- product;
- site or assortment;
- validity period.

A product may exist centrally but not be listed in a specific store.

Without the appropriate listing or activation, the store may not be permitted to:

- order;
- receive;
- replenish;
- sell;
- forecast

the product according to the implemented process.

## Listing is not inventory

A listed product may have no stock.

A non-listed product may still physically exist because of:

- old inventory;
- return;
- transfer;
- incorrect delivery;
- delisting.

The system needs explicit handling for residual inventory after delisting.

## Listing is not only a technical extension

Listing reflects commercial decisions:

- store format;
- shelf capacity;
- customer demand;
- regional policy;
- season;
- product role;
- supplier agreement.

Generating every product for every store creates an enormous product-location volume.

It also weakens planning relevance.

## Store clustering

Retailers frequently group stores by:

- size;
- format;
- geography;
- customer profile;
- sales behaviour;
- climate;
- tourist demand.

Clusters support:

- assortment;
- allocation;
- pricing;
- promotion;
- forecasting.

A cluster should have one clear purpose.

The same segmentation may not be suitable for both assortment and replenishment.

## Assortment Planning and CAR

CAR-based Assortment Planning supports ranking and selecting products using retail KPIs and store or format context. SAP currently describes its assortment capabilities as supporting product ranking, merchandise-plan alignment and space-related optimization.

A planning recommendation should not immediately create operational listing.

A controlled flow is:

```text
Assortment recommendation
→ category-manager review
→ approval
→ operational listing
→ channel publication
→ replenishment activation
```

## Part V: Retail pricing

Retail pricing is not one price condition.

It may include:

- regular retail price;
- regional price;
- store price;
- channel price;
- markdown;
- promotion;
- coupon;
- loyalty price;
- mix-and-match;
- multibuy;
- employee price;
- tax.

## Purchase price versus retail price

The purchase price represents expected acquisition cost.

The retail price represents the customer-facing selling price.

Margin depends on more than the difference between the two.

It may also include:

- supplier rebate;
- logistics;
- markdown;
- waste;
- shrinkage;
- payment cost;
- promotion funding.

## Price zones

Retailers may group stores into price zones.

Examples:

- national;
- regional;
- urban premium;
- outlet;
- airport.

Price zones reduce the need to maintain every store-product price separately.

But they also create questions:

- Which zone owns online pricing?
- Can a store override the zone?
- What happens during store reassignment?
- Which price applies to click and collect?

## Price publication

A price may need to reach:

- POS;
- Commerce;
- mobile app;
- shelf labels;
- electronic shelf labels;
- customer service;
- marketplace;
- order system.

Every channel should receive:

- value;
- currency;
- unit;
- validity;
- tax treatment;
- source;
- version.

## Promotional pricing

Promotion rules may be basket-dependent.

Examples:

- buy two, get one free;
- spend EUR 100, save EUR 10;
- loyalty members receive 20%;
- mix products from one category;
- coupon with usage limit.

These rules cannot always be represented as one static product price.

## Omnichannel Promotion Pricing

SAP Omnichannel Promotion Pricing currently provides central upload, maintenance and calculation of price and promotion data across web, POS and sales-order channels, including coupon creation, reservation and redemption.

A strong architecture can use:

```text
Promotion authority
→ OPP repository
→ calculation service
→ POS, Commerce and assisted sales
```

The calculation engine should not also become the commercial approval process unless explicitly designed for that responsibility.

## Offline stores

A central cloud pricing service creates a dependency.

Stores may lose connectivity.

The architecture must decide:

- whether prices are cached locally;
- which promotions work offline;
- how coupon reservation works;
- how results are reconciled after reconnection;
- what happens when a promotion changes during the outage.

A retailer cannot promise consistent pricing without a degraded-mode design.

## Returns and promotion reconstruction

Returns are difficult when discounts were distributed across several products.

Example:

```text
Buy 3 items for EUR 20
```

The customer returns one item.

The system must know:

- original basket;
- discount allocation;
- returned quantity;
- retained products;
- coupon state.

Do not calculate the return using today’s price.

Preserve the original commercial result.

## Supplier-funded promotions

A supplier may fund:

- display;
- price discount;
- volume target;
- marketing campaign;
- new product launch.

The retailer needs to connect:

- promotion;
- eligible product;
- stores;
- sales volume;
- supplier agreement;
- receivable or settlement.

This may involve Settlement Management, condition contracts or specialist solutions such as Vistex depending on complexity.

## Part VI: Planning, allocation and replenishment

Retail planning should be separated into several decisions.

## Merchandise financial planning

Answers:

- What sales are expected?
- What margin should be delivered?
- How much inventory can be purchased?
- How much markdown is acceptable?

## Assortment planning

Answers:

- Which products should be offered?
- In which stores and channels?
- During which period?

## Allocation

Answers:

- How should a constrained or initial quantity be distributed?

## Replenishment

Answers:

- How much should be reordered for each product-location and when?

## Allocation Management

CAR allocation capabilities currently support initial allocation, in-season replenishment and promotional allocation based on demand forecast, inventory, targets and retail KPIs.

Allocation is especially important for:

- fashion;
- seasonal products;
- launches;
- promotions;
- short-lifecycle goods.

### Initial allocation

Occurs before sufficient actual sales history exists.

May use:

- store cluster;
- similar product;
- size profile;
- assortment plan;
- store capacity;
- product role.

### In-season allocation

Uses actual sales to rebalance remaining stock.

### Promotional allocation

Distributes finite promotional merchandise.

## Replenishment

SAP Predictive Replenishment currently calculates automated order proposals using demand estimates, service levels, supplier restrictions, minimum quantities and coverage constraints, with prebuilt integrations to S/4HANA Retail, Order and Delivery Scheduling and CAR UDF.

A target flow may be:

```text
POS and online demand
→ CAR/UDF or other forecast
→ Predictive Replenishment
→ order proposal
→ S/4HANA purchase order or stock transfer
→ supplier or DC execution
```

## Order and Delivery Scheduling

Retail replenishment depends on commercial and physical calendars.

SAP Order and Delivery Scheduling currently manages supply-network combinations and ordering and delivery patterns, including exceptions such as holidays, and generates schedules for downstream fulfilment systems such as S/4HANA.

Examples:

```text
Order every Monday
Supplier ships Tuesday
DC receives Wednesday
Store receives Thursday
```

Calendars may differ by:

- supplier;
- product group;
- DC;
- store;
- transport lane;
- holiday.

A technically correct replenishment quantity sent on the wrong ordering day is still a failed replenishment.

## Fresh products

Fresh and perishable products add constraints such as:

- shelf life;
- spoilage;
- minimum remaining life;
- daily or intraday demand;
- waste;
- supplier cut-off;
- temperature;
- display requirements.

The objective is not simply to prevent stockouts.

It is to balance:

- sales;
- availability;
- waste;
- markdown;
- freshness.

## Fashion and seasonal retail

Fashion adds:

- style-colour-size;
- season;
- collection;
- launch;
- initial allocation;
- size curve;
- markdown;
- short lifecycle.

SAP currently positions its fashion and vertical capabilities around integrated style-colour-size logic across manufacturing, wholesale and retail.

The ERP, CAR planning and Commerce models must agree on the variant structure.

## Part VII: Distribution-centre execution

Retail distribution centres may process:

- supplier receipts;
- putaway;
- cross-docking;
- flow-through;
- store replenishment;
- e-commerce orders;
- returns;
- value-added services.

## SAP EWM

SAP EWM is normally the detailed warehouse-execution system.

It owns:

- bins;
- stock types;
- handling units;
- warehouse tasks;
- waves;
- replenishment;
- picking;
- packing;
- staging;
- loading.

SAP’s current retail portfolio positions EWM for resilient, cost-controlled warehouse operations supporting retail fulfilment.

## Store order versus e-commerce order

The same DC may fulfil:

- full pallets to stores;
- cases to stores;
- individual pieces to online customers.

These processes have different:

- picking methods;
- packaging;
- cut-offs;
- cost;
- transport.

Do not manage them through one undifferentiated warehouse process merely because they share inventory.

## Allocation to warehouse execution

An allocation decision may produce store-specific quantities.

EWM must receive enough information to:

- identify store;
- preserve product quantity;
- pick correct pack;
- label;
- consolidate;
- stage by route.

Planning quantity does not automatically become a physically executable handling-unit plan.

## Distribution-centre replenishment

The DC itself must be replenished by:

- suppliers;
- factories;
- other DCs.

This network replenishment belongs in S/4HANA, Predictive Replenishment, IBP or another planning layer.

Internal EWM replenishment moves stock between reserve and picking areas.

These are different decisions.

## Transportation Management

SAP TM may support:

- inbound supplier transport;
- store delivery routes;
- e-commerce transport;
- carrier planning;
- consolidation;
- freight settlement.

Store deliveries often operate through fixed or semi-fixed routes.

Online orders may use parcel networks.

The transportation architecture should distinguish:

- store network;
- home delivery;
- click-and-collect transfer;
- supplier inbound;
- returns.

## Part VIII: Store operations

The store is no longer only a selling location.

It may be:

- sales floor;
- micro-warehouse;
- pickup point;
- return point;
- fulfilment node;
- customer-service location.

SAP currently describes S/4HANA Retail capabilities for store dashboards, real-time product lookup, RFID-enabled stock movements and click-and-collect fulfilment.

## Store receiving

The store may receive from:

- DC;
- direct supplier;
- another store;
- customer return.

Receiving should update inventory accurately and promptly.

Delayed receiving creates false out-of-stock information.

## Shelf replenishment

Inventory can exist in the back room while the shelf is empty.

This is an on-shelf availability problem.

Possible inputs include:

- POS sales;
- shelf capacity;
- back-room stock;
- planogram;
- RFID;
- task management.

ERP plant stock alone cannot prove shelf availability.

## Inventory adjustment

Store inventory changes through:

- sales;
- return;
- damage;
- waste;
- theft;
- counting;
- transfer;
- receiving.

Every unrecorded physical movement makes omnichannel availability weaker.

## RFID

RFID can improve:

- receiving;
- inventory counting;
- item location;
- fulfilment;
- loss prevention.

RFID data volume is much greater than ordinary inventory transactions.

The architecture should decide which events become:

- operational stock updates;
- analytical telemetry;
- exceptions.

Do not send every reader observation into ERP as a stock movement.

## Store fulfilment

A store may pick online orders.

The process requires:

- inventory reservation;
- pick task;
- substitution;
- short-pick handling;
- customer notification;
- pickup staging;
- expiry;
- cancellation.

The sales-floor inventory is still accessible to physical shoppers.

Without reservation and fast execution, the online promise may fail.

## Part IX: POS, CAR and financial posting

The POS system owns the original customer checkout transaction.

CAR or Omnichannel Sales Transfer and Audit can receive, validate and prepare sales-channel data.

SAP currently describes CAR as collecting and auditing multichannel sales and Omnichannel Sales Transfer and Audit as a dedicated sales capture and audit solution.

## POS outbound integration

Before sales occur, stores may need:

- products;
- barcodes;
- regular prices;
- promotions;
- tax rules;
- tender configuration;
- store data.

These data flows may be:

- scheduled;
- event-driven;
- API-based;
- file-based.

The POS must know the effective validity and version.

## POS inbound integration

After checkout, the POS sends:

- receipt;
- items;
- quantities;
- prices;
- discounts;
- tax;
- tenders;
- returns;
- loyalty reference.

The retailer should preserve a stable transaction identity such as:

```text
Store
+ business date
+ register
+ receipt number
```

A retry should not create another sale.

## Sales audit

The audit process checks:

- duplicate transactions;
- missing sequences;
- unknown products;
- total mismatch;
- invalid tax;
- invalid tender;
- incomplete business day.

A sales-audit error is not merely a technical message.

It may represent unposted:

- revenue;
- inventory;
- tax;
- payment.

## Aggregation

Detailed receipt lines may remain in CAR.

ERP may receive aggregated results.

The aggregation should still support reconciliation.

A complete chain is:

```text
POS totals
= CAR received totals
= CAR accepted totals
= ERP posted sales
= finance and inventory result
```

## Tender reconciliation

A receipt may include:

- cash;
- card;
- voucher;
- gift card;
- wallet;
- loyalty redemption.

Tender data must reconcile with:

- payment provider;
- bank settlement;
- store cash;
- receivables.

Sales revenue and received payment are connected but distinct facts.

## Part X: Omnichannel commerce and order management

The hardest retail architecture problem is deciding where the omnichannel order lives.

A customer order may start in:

- Commerce;
- marketplace;
- mobile app;
- customer service;
- store.

It may be fulfilled by:

- DC;
- store;
- supplier;
- third-party logistics provider.

## Commerce Cloud

Commerce should own the customer-facing buying journey:

```text
Search
→ product detail
→ basket
→ promotion
→ checkout
→ payment
→ order submission
```

SAP Commerce Cloud currently supports product catalogue, pricing, promotions, search and B2B/B2C commerce experiences.

## Order Management foundation

Order Management foundation should be considered where orders from several channels require one orchestration model.

It currently provides:

- centralized order view;
- routing;
- fulfilment coordination;
- returns;
- integration to several execution systems.

## Sourcing and availability

SAP Order Management for sourcing and availability currently provides centralized inventory visibility, reservation management and objective-based sourcing across multiple fulfilment nodes and backend systems.

It answers questions such as:

- Which node has stock?
- Which node can meet the promise?
- Which option minimizes fulfilment cost?
- Should the order be split?
- Which stock must be reserved?

## Inventory visibility versus availability

### Inventory visibility

```text
Store A reports 5 units
```

### Availability

```text
3 units can be offered after safety stock and reservations
```

### Reservation

```text
2 units are protected for order X
```

### Sourcing

```text
Store A is selected instead of DC B
```

### Orchestration

```text
Order X is routed, fulfilled, monitored and returned
```

CAR, S/4HANA aATP and Order Management may each contain part of this picture.

One system must own the binding reservation.

## aATP versus OMS availability

S/4HANA aATP is appropriate when:

- S/4HANA owns the sales order;
- relevant supply is inside one ERP scope;
- allocation and backorder rules are ERP-centred.

Order Management for sourcing and availability is stronger when:

- inventory exists in several systems;
- stores and warehouses are distributed;
- commerce needs fast API-based response;
- reservations and fulfilment-objective optimization are central.

CAR can provide valuable retail activity and inventory insight.

It should not be assumed to be the reservation system merely because it contains inventory data.

## Sourcing objectives

A sourcing engine may optimize for:

- fastest delivery;
- lowest cost;
- fewest splits;
- oldest stock;
- store capacity;
- inventory balancing;
- carbon;
- margin.

These objectives conflict.

Management must decide priority.

A sourcing engine cannot determine whether customer speed is worth the additional fulfilment cost without an explicit policy.

## Ship from store

Ship-from-store can:

- use local inventory;
- shorten delivery;
- reduce markdown.

It can also create:

- expensive piece picking;
- inventory inaccuracy;
- store labour disruption;
- packaging inconsistency;
- split shipments.

The sourcing objective should include real store fulfilment cost.

## Click and collect

Click and collect requires:

- reliable inventory;
- reservation;
- store task;
- ready notification;
- customer pickup;
- expiry and cancellation.

The order should not be marked ready because stock was visible.

It should be marked ready after physical picking and staging.

## Endless aisle

A store associate may sell a product that is unavailable locally but available elsewhere.

The process needs:

- customer context;
- product information;
- global availability;
- payment;
- order capture;
- selected fulfilment source.

This is an omnichannel order, not a conventional POS sale.

## Returns

An omnichannel customer may:

- buy online;
- return in store;
- receive refund through original payment;
- ship item back to another node.

The architecture must decide:

- who owns the return;
- where inventory becomes available;
- which price and tax apply;
- which system executes refund;
- how loyalty and promotion are reversed.

## Part XI: The integration architecture

A strong SAP Retail landscape uses different integration styles for different needs.

## Master-data integration

Suitable for:

- products;
- sites;
- suppliers;
- assortments;
- hierarchies;
- prices;
- calendars.

Possible mechanisms include:

- standard APIs;
- events;
- replication;
- managed integration flows;
- files for partner or legacy systems.

Master data should include:

- stable identity;
- validity;
- version;
- source;
- lifecycle state.

## Transactional APIs

Suitable for:

- availability;
- reservation;
- order creation;
- order status;
- returns;
- price calculation.

These require:

- low latency;
- idempotency;
- clear error semantics;
- status retrieval.

## Events

Suitable for facts such as:

- product activated;
- listing changed;
- inventory changed;
- order accepted;
- order fulfilled;
- sale audited.

Consumers should treat events as durable facts, not remote procedure calls.

## High-volume replication

CAR private-edition architectures currently require SAP Landscape Transformation Replication Server for exchange with ERP or S/4HANA as part of the documented prerequisite model.

SLT can be useful for:

- high-volume source-table replication;
- low-latency data foundation updates.

Its limitations include:

- structural coupling;
- replicated data without business acknowledgement;
- additional monitoring;
- complex cutover during S/4HANA migration.

## Batch and file integration

Still appropriate for:

- legacy POS;
- supplier feeds;
- large catalogue export;
- periodic financial posting;
- initial load.

A file process should include:

- file ID;
- checksum;
- expected count;
- control total;
- duplicate protection;
- archive;
- record-level error handling.

## Integration Suite

SAP Integration Suite may provide:

- API management;
- integration flows;
- protocol conversion;
- event connectivity;
- partner integration;
- monitoring.

It should not become the owner of:

- assortment decisions;
- promotion policy;
- inventory reservation;
- supplier approval.

Middleware moves and adapts business contracts.

It should not silently create retail truth.

## Product integration map

A practical master-data flow may be:

```text
Supplier/PIM
→ product governance
→ S/4HANA Retail product
→ CAR/DDF
→ Commerce catalogue
→ POS
→ OMS
→ analytics
```

Each target needs a different projection.

### POS projection

Needs:

- sellable product;
- barcode;
- description;
- tax;
- price;
- promotion eligibility.

### Commerce projection

Needs:

- rich content;
- images;
- attributes;
- navigation;
- search;
- customer-facing description.

### Replenishment projection

Needs:

- product-location;
- lead time;
- pack size;
- demand;
- service;
- source.

Do not expose one giant ERP product payload to every consumer.

## Inventory integration map

```text
S/4HANA and EWM
Operational inventory
        |
        v
Availability/OMS hub
Available and reserved quantity
        |
        v
Commerce, stores and service channels
```

CAR may also consume and expose inventory for planning and insight.

The architecture must prevent:

- double counting;
- stale copies;
- several reservation authorities;
- availability based on blocked stock.

## Order integration map

```text
Commerce / marketplace / store
            |
            v
Order Management
            |
      sourcing decision
            |
      +-----+------+------+
      |            |      |
      v            v      v
S/4HANA         store   supplier
DC fulfilment   fulfil. drop ship
      |
      v
EWM / TM / carrier
      |
      v
Fulfilment events back to OMS and channel
```

S/4HANA may remain the order authority in simpler models.

Do not add an OMS when one ERP already owns all channels and nodes adequately.

## Sales integration map

```text
POS
→ sales-transfer and audit
→ CAR
→ aggregated or detailed posting
→ S/4HANA inventory and finance
→ enterprise analytics
```

The authoritative receipt and authoritative accounting document are different objects.

Both must remain linked.

## Supplier integration map

```text
Forecast/replenishment
→ purchase order
→ Business Network
→ supplier confirmation
→ shipment notice
→ EWM/store receipt
→ S/4HANA invoice verification
```

A supplier confirmation should update the expected supply date used by planning.

Otherwise, the retailer continues promising stock against an obsolete purchase-order date.

## Part XII: Finance and profitability

Retail finance must connect high-volume sales with inventory and margin.

## Inventory valuation

Retailers may manage:

- moving average;
- standard cost;
- retail valuation approaches;
- valuation by site or company.

The exact model depends on accounting and industry configuration.

## Cost of goods sold

The sale should generate the appropriate inventory and financial impact.

When POS sales are aggregated, finance must still reconcile:

- product or merchandise category;
- store;
- tax;
- revenue;
- cost;
- payment.

## Markdown

Markdown is a commercial decision to reduce selling price.

It affects:

- revenue;
- margin;
- sell-through;
- remaining inventory;
- future write-off.

Markdown should not be confused with inventory revaluation unless accounting policy explicitly creates that effect.

## Shrinkage

Shrinkage can originate from:

- theft;
- damage;
- spoilage;
- process error;
- unrecorded transfer.

Inventory differences should be classified.

A generic write-off hides the operational cause.

## Gross margin return on inventory

Retail management often needs more than gross margin percentage.

A product with high margin but very slow inventory movement may underperform a lower-margin fast-moving product.

Useful measures include:

- gross margin;
- sell-through;
- inventory turns;
- markdown;
- waste;
- return;
- stockout;
- gross margin return on inventory investment.

## Vendor rebates

Supplier agreements may include:

- volume rebate;
- promotional funding;
- listing allowance;
- markdown support;
- logistics allowance.

These may be managed through:

- condition contracts;
- Settlement Management;
- specialist vendor-program applications.

The retailer should measure effective net cost, not only purchase-order price.

## Part XIII: Data and analytics

The retail landscape produces detailed information from:

- product;
- inventory;
- POS;
- orders;
- customers;
- suppliers;
- promotions;
- logistics.

## CAR as operational retail data foundation

CAR is well suited for:

- detailed retail activity;
- POS audit;
- UDF;
- selected planning applications;
- omnichannel context.

It is not automatically the final enterprise analytics platform.

## Business Data Cloud and Datasphere

The enterprise data layer may publish governed data products such as:

- store sales;
- product performance;
- inventory;
- customer profitability;
- supplier performance;
- promotion effectiveness.

The data platform should preserve:

- business semantics;
- lineage;
- freshness;
- source authority.

## Real-time versus historical truth

Operational systems answer:

> What should we act on now?

Analytical systems answer:

> What happened, why, and what pattern exists?

A corrected historical sales record may differ from the operational event originally used for replenishment.

Both can be valid for their purpose.

## AI in retail

AI can support:

- product enrichment;
- demand forecasting;
- pricing recommendations;
- assortment ranking;
- replenishment;
- order reliability;
- customer engagement.

SAP currently presents retail AI across merchandising, demand, supply, commerce and fulfilment, including agent-oriented capabilities in Commerce and Order Management.

The architecture should distinguish:

- recommendation;
- simulation;
- automated decision;
- binding transaction.

An AI agent may propose a markdown.

It should not automatically activate it across 2,000 stores without:

- margin guardrail;
- inventory analysis;
- approval;
- rollback;
- result measurement.

## Part XIV: Main limitations and traps

## Trap 1: Treating Retail as a standard ERP template

The project underestimates:

- listing;
- assortment;
- variants;
- store operations;
- POS;
- promotion;
- omnichannel stock.

## Trap 2: Extending every product to every site

Product-location volume explodes.

Planning and maintenance become slow and meaningless.

## Trap 3: Using one product hierarchy for every purpose

ERP, Commerce, finance and planning require different semantics.

## Trap 4: Making CAR the owner of everything

CAR becomes:

- sales repository;
- data warehouse;
- price engine;
- inventory service;
- customer database;
- integration hub.

## Trap 5: Publishing stock without reservation

Several channels sell the same physical unit.

## Trap 6: Calculating promotions in every channel

POS and Commerce produce different baskets and discounts.

## Trap 7: Running several forecast engines without authority

UDF, IBP and external AI produce competing forecasts.

## Trap 8: Replenishing against sales rather than demand

Stockout periods are interpreted as zero customer demand.

## Trap 9: Ignoring supplier pack size and schedules

The forecast is good, but the order proposal cannot be executed.

## Trap 10: Using store inventory as if it were perfectly accurate

Ship-from-store cancellations rise.

## Trap 11: Direct integration to tables

Commerce, POS and custom applications become tightly coupled to S/4HANA or CAR internals.

## Trap 12: Confusing inventory, availability and fulfilment capacity

A store has stock but cannot pick 500 online orders.

## Trap 13: Aggregating POS data too early

Receipt-level traceability disappears.

## Trap 14: Sending every POS receipt to ERP individually

ERP receives unnecessary transaction volume.

## Trap 15: Migrating ECC Retail configuration one to one

Historical complexity is reproduced in S/4HANA.

## Trap 16: Assuming cloud products replace the merchandise core

Modular cloud services still need authoritative product, site, inventory and finance data.

## Trap 17: Creating one omnichannel order in several systems

Commerce, OMS and S/4HANA each claim to own the order.

## Trap 18: Ignoring degraded operations

A store must continue selling when central services or network connectivity fail.

## Part XV: Modern target architectures

## Architecture A: Traditional store-centric retailer

Suitable when:

- stores dominate;
- one S/4HANA system;
- limited online channel;
- central DC network.

```text
S/4HANA Retail
    |
    +→ EWM/TM
    |
    +→ POS master data
    |
POS → CAR/sales audit → S/4HANA
    |
    +→ planning and analytics
```

## Architecture B: Omnichannel retailer

Suitable when:

- high online volume;
- stores as fulfilment nodes;
- multiple order sources.

```text
S/4HANA Retail
Merchandise, finance, procurement
        |
        +→ CAR / Predictive Replenishment
        |
        +→ EWM / TM
        |
        +→ Order Management inventory feed

Commerce / Marketplace / Store
        |
        v
Order Management foundation
        |
Sourcing and availability
        |
Reservations and node selection
        |
S/4HANA / EWM / Store / Supplier
```

## Architecture C: High-volume grocery

Focus:

- POS completeness;
- fresh demand;
- intraday replenishment;
- waste;
- direct store delivery.

```text
POS → Sales Audit/CAR → UDF
                         |
                         v
Predictive Replenishment
                         |
Order and Delivery Scheduling
                         |
S/4HANA orders
                         |
Supplier/DC/store execution
```

## Architecture D: Fashion and seasonal

Focus:

- style-colour-size;
- season;
- initial allocation;
- size profiles;
- markdown.

```text
Product lifecycle
→ S/4HANA Fashion/Retail
→ Assortment Planning
→ Allocation Management
→ EWM/store distribution
→ POS and Commerce sales
→ in-season reallocation
→ markdown and exit
```

## Architecture E: Multi-ERP global retailer

Focus:

- several country ERPs;
- common Commerce;
- global OMS;
- regional inventory.

```text
Country ERPs and warehouses
          |
          v
Global sourcing and availability hub
          |
          v
Order Management
          |
Commerce and marketplaces
```

A global product and location identity is mandatory.

## Part XVI: Migration to S/4HANA Retail

A retail migration is not only a technical conversion.

## Product migration

Review:

- article types;
- generic articles and variants;
- barcodes;
- units;
- merchandise categories;
- site extensions;
- listing;
- product status.

## Site migration

Review:

- stores;
- DCs;
- organisational assignments;
- calendars;
- valuation;
- warehouse connections;
- address and tax.

## Supplier and Business Partner conversion

Supplier and customer data must align with the S/4HANA Business Partner model.

Duplicate and local identities should be resolved before cutover where possible.

## Pricing and promotions

Separate:

- ERP price;
- POS price;
- Commerce price;
- promotion rules;
- coupons;
- markdown.

Do not migrate every historical condition record without analysing active usage.

## POS integration

Test:

- outbound master data;
- price and promotion validity;
- transaction identity;
- duplicates;
- business-date closure;
- financial posting;
- offline backlog.

## CAR integration

Where CAR remains:

- validate SLT compatibility;
- data model;
- custom code;
- replication latency;
- HANA sizing;
- interfaces;
- retention.

SAP’s current CAR private-edition model continues to identify ERP or S/4HANA as the source master-data system and SLT as an exchange prerequisite.

## Inventory cutover

Retail inventory may exist in:

- DC;
- store;
- consignment;
- transit;
- blocked stock;
- return;
- e-commerce reservation.

The cutover must preserve status, not only quantity.

## Open documents

Include:

- purchase orders;
- stock transfers;
- deliveries;
- store orders;
- customer orders;
- returns;
- supplier confirmations;
- promotions.

## Parallel operations

During transition, some countries or channels may remain on legacy systems.

The architecture must prevent:

- duplicate product publication;
- conflicting price authority;
- double inventory;
- two reservation systems;
- duplicate POS posting.

## Part XVII: Implementation approach

## Phase 1: Define the retail business model

Clarify:

- store formats;
- channels;
- fulfilment nodes;
- product types;
- supply network;
- price strategy.

## Phase 2: Assign system authority

For every object, define one owner.

| Object | Recommended authority |
|---|---|
| Governed product | S/4HANA/PIM/MDG according to design |
| Operational site | S/4HANA Retail |
| Assortment decision | Assortment planning/business process |
| Listing | S/4HANA Retail |
| Purchase order | S/4HANA |
| POS receipt | POS, audited in CAR/sales audit |
| Financial posting | S/4HANA Finance |
| Promotion definition | Named promotion authority |
| Promotion calculation | OPP where selected |
| Commerce cart | Commerce |
| Omnichannel orchestration | OMS where selected |
| Reservation | One OMS/aATP authority |
| Warehouse task | EWM |
| Enterprise data product | Governed data platform |

## Phase 3: Build identity model

Define:

- product ID;
- GTIN;
- variant;
- site;
- fulfilment node;
- supplier;
- customer;
- receipt;
- order;
- promotion.

## Phase 4: Design lifecycle before interfaces

For product:

```text
Create
→ enrich
→ approve
→ list
→ publish
→ replenish
→ sell
→ delist
```

For order:

```text
Capture
→ source
→ reserve
→ release
→ fulfil
→ settle
→ return
```

## Phase 5: Design integration contracts

Specify:

- business meaning;
- source authority;
- latency;
- idempotency;
- failure behaviour;
- reconciliation.

## Phase 6: Pilot one complete flow

A strong pilot:

> One product category, one DC, ten stores and one online channel.

Include:

- product onboarding;
- listing;
- purchasing;
- replenishment;
- DC execution;
- store receipt;
- POS sale;
- online order;
- return;
- financial reconciliation.

## Phase 7: Measure operational results

Do not measure only interface success.

Measure:

- time to list product;
- on-shelf availability;
- stockout;
- inventory;
- promotion accuracy;
- store fulfilment cancellation;
- POS reconciliation;
- margin.

## Questions managers and architects should ask

1. What does S/4HANA Retail own?
2. What does CAR own?
3. Which application owns the retail forecast?
4. Which application owns replenishment proposals?
5. Which application owns the final purchase order?
6. Which system owns product identity?
7. Which system owns rich commerce content?
8. How are products listed for stores and channels?
9. Are all product-location combinations actually required?
10. Which system owns regular price?
11. Which system owns promotion definition?
12. Which engine calculates basket promotions?
13. What happens when central promotion calculation is unavailable?
14. Which system owns the customer order?
15. Which system owns inventory reservation?
16. What prevents several channels from selling the same unit?
17. Can store stock support online fulfilment reliably?
18. How is store fulfilment capacity represented?
19. Can every POS receipt be reconciled to finance?
20. Which supplier confirmation updates planning?
21. Are supplier calendars reflected in replenishment?
22. Where is distribution-centre replenishment calculated?
23. Where is internal warehouse replenishment executed?
24. How are returns priced and financially settled?
25. Which CAR data remains in expensive hot storage?
26. Which applications read ERP or CAR tables directly?
27. Is the architecture prepared for offline stores?
28. Which data product is safe for AI consumption?
29. Can the company trace one product from supplier to consumer?
30. Can the company explain the architecture without saying “everything is in SAP”?

## The management conclusion

SAP for Retail is not a single monolithic application.

The operational core is SAP S/4HANA Retail for merchandise management.

It connects:

- products;
- sites;
- assortment;
- sourcing;
- purchasing;
- inventory;
- sales;
- finance.

SAP currently positions that core for connected merchandise management, store operations, supply-chain management, omnichannel price information and retail inventory processes.

Around it, specialised applications provide bounded capabilities:

- CAR for detailed customer activity and retail planning;
- Sales Transfer and Audit for POS transaction control;
- Predictive Replenishment for order proposals;
- Order and Delivery Scheduling for retail supply calendars;
- Commerce Cloud for customer-facing commerce;
- Order Management for orchestration;
- Sourcing and Availability for inventory reservations and fulfilment selection;
- OPP for consistent promotional calculations;
- EWM and TM for logistics execution;
- Business Network for supplier collaboration.

The strength of SAP Retail is not that one system does everything.

Its strength is that merchandise, supply, sales and financial processes can share one governed model.

Its main danger is allowing every product to become a second master system.

A strong architecture can answer:

- where a product is created;
- where it is listed;
- where it is priced;
- where demand is forecast;
- where replenishment is calculated;
- where the order is owned;
- where stock is reserved;
- where the sale is audited;
- where the money is posted.

The decisive question is not:

> Which SAP Retail modules do we have?

It is:

> Can one product move from supplier onboarding to customer sale and financial settlement without losing identity, authority, price, inventory or accountability between systems?

When the answer is yes, SAP for Retail becomes a connected operating model.

When the answer is no, the retailer has a collection of powerful SAP products connected by reconciliation spreadsheets.

---

### SAP for Retail architecture checklist

- [ ] SAP for Retail and S/4HANA Retail are distinguished.
- [ ] S/4HANA is the operational merchandise and financial core.
- [ ] Site design reflects stores, DCs and fulfilment nodes.
- [ ] Product, generic article and variant models are governed.
- [ ] Only valid variants are created.
- [ ] Merchandise categories have stable ownership.
- [ ] GTINs and packaging levels are controlled.
- [ ] Product lifecycle states are explicit.
- [ ] Product onboarding separates supplier, governed and channel data.
- [ ] Supplier agreements flow into operational purchasing.
- [ ] Assortment and listing are separate from product creation.
- [ ] Product-location volume is actively controlled.
- [ ] Price zones have clear commercial meaning.
- [ ] Regular and promotional price authorities are separated.
- [ ] OPP or another engine provides consistent basket calculation.
- [ ] Offline-store pricing behaviour is tested.
- [ ] Promotion returns reproduce the original transaction.
- [ ] Allocation and replenishment are distinguished.
- [ ] Forecast and replenishment have named system owners.
- [ ] Supplier, product and delivery calendars are integrated.
- [ ] EWM owns warehouse execution, not network planning.
- [ ] TM is connected to store and online fulfilment requirements.
- [ ] Store inventory movements are recorded promptly.
- [ ] Store fulfilment includes reservation and capacity.
- [ ] POS transactions have stable identities.
- [ ] Sales are reconciled from POS through S/4HANA Finance.
- [ ] Inventory visibility and reservation are separate capabilities.
- [ ] One system owns binding omnichannel reservation.
- [ ] Commerce owns customer experience, not merchandise accounting.
- [ ] OMS is introduced only where orchestration complexity justifies it.
- [ ] Sourcing objectives include fulfilment cost and capacity.
- [ ] Customer returns have one end-to-end process owner.
- [ ] CAR remains bounded to its retail data and planning role.
- [ ] SLT and high-volume replication are monitored.
- [ ] Consumers use governed APIs and events rather than direct tables.
- [ ] Enterprise analytics is separated from operational transaction control.
- [ ] AI recommendations cannot bypass pricing, inventory or assortment governance.
- [ ] Migration preserves retail state, not only master records and quantities.
- [ ] The company can trace one transaction across every retail layer.

### Sources and further reading

SAP’s current retail industry portfolio connects merchandise management, demand and supply planning, omnichannel commerce, store fulfilment, customer engagement, finance and workforce operations. It lists S/4HANA Retail, CAR, Predictive Replenishment, EWM, TM, Commerce, OPP and Order Management as distinct but connected capabilities.

SAP currently describes SAP S/4HANA Retail for merchandise management as the ERP-based retail core connecting finance, supply chain, manufacturing, sales, distribution, store operations and customer-centric merchandise management.

SAP CAR currently provides a multichannel sales repository, inventory and customer-activity insight, demand forecasting, assortment planning, allocation, replenishment and promotion-management capabilities. Its private-edition commercial model requires ERP or S/4HANA as the source master-data system and identifies SLT as the exchange mechanism.

SAP Commerce Cloud currently provides B2B, B2C and B2B2C commerce, product-catalogue management, pricing, promotions, search, discovery and storefront capabilities.

SAP Order Management foundation currently centralizes order, fulfilment and return orchestration across channels and distributed execution systems through a modular cloud architecture.

SAP Order Management for sourcing and availability currently provides multi-backend inventory visibility, reservations and objective-based fulfilment sourcing with integration to S/4HANA and customer-experience applications.

SAP Predictive Replenishment currently automates order-proposal calculation using demand, service, minimum-order and coverage constraints and provides prebuilt integrations with S/4HANA Retail, CAR UDF and Order and Delivery Scheduling.

SAP Order and Delivery Scheduling currently manages retail supply-network combinations, ordering patterns, delivery patterns and holiday exceptions and generates schedules for downstream fulfilment systems.

SAP Business Network Supply Chain Collaboration currently supports forecast collaboration, purchase-order and confirmation exchange, shipment visibility, supplier-managed inventory, replenishment and manufacturing collaboration.

SAP Omnichannel Promotion Pricing currently centralizes promotion data and calculation across web, POS and sales-order channels and includes coupon creation, reservation and redemption services.

*Reviewed: July 2026. SAP Retail scope, licensing, deployment models and integration mechanisms differ by S/4HANA, CAR and cloud-service release. Detailed architecture should be validated against the exact Product Availability Matrix, scope items, service descriptions and current SAP road maps.*

## Continue exploring

- [Why SAP CAR Becomes the Most Important Retail System Nobody Can Clearly Explain](/blog/why-sap-car-becomes-the-most-important-retail-system-nobody-can-clearly/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [Why SAP CAR Becomes the Most Important Retail System Nobody Can Clearly Explain](/blog/why-sap-car-becomes-the-most-important-retail-system-nobody-can-clearly/)
- Next in the migration: [SAP EWM Explained: Processes, Integrations, Deployment Choices, and the Limitations Nobody Should Ignore](/blog/sap-ewm-explained-processes-integrations-deployment-choices-and-the/)
