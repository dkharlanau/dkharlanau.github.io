# SAP for Automotive Explained: The Complete Architecture from Engineering and JIT Supply to Vehicle Sales, Warranty, and Aftermarket

An automotive company says it is implementing SAP S/4HANA.

The programme scope includes:

- procurement;
- production;
- sales;
- logistics;
- finance.

This sounds similar to any manufacturing transformation.

Then the real requirements appear.

The customer does not send ordinary purchase orders. It sends:

- long-term forecasts;
- delivery schedules;
- just-in-time calls;
- sequence calls;
- engineering changes;
- cumulative quantities;
- self-billing documents.

The product is not one stable material.

It may have:

- thousands of configuration combinations;
- engineering and manufacturing BOMs;
- country-specific homologation;
- software versions;
- customer-specific components;
- serialised traceability.

The finished vehicle is not only inventory.

It has:

- a VIN;
- configuration;
- production status;
- physical location;
- ownership;
- dealer assignment;
- registration and sales history;
- warranty and service lifecycle.

This is why SAP for Automotive cannot be reduced to standard MM, SD and PP.

Those capabilities remain the foundation.

The automotive operating model adds several tightly connected requirements:

- highly configurable products;
- repetitive and sequenced manufacturing;
- long-term scheduling agreements;
- JIT and JIS supply;
- multi-tier supplier collaboration;
- returnable container loops;
- customer self-billing;
- component and vehicle traceability;
- warranty and complaint recovery;
- dealer and aftermarket operations.

SAP’s current automotive portfolio spans product development, sourcing, supply-chain collaboration, manufacturing, warehouse and transportation management, vehicle sales, service parts, customer service, trade compliance, self-billing and industry-network scenarios. It is therefore better understood as a portfolio around the ERP core rather than one automotive application.

## There is no single SAP Automotive architecture

The correct landscape depends on the company’s role.

## Automotive OEM

An OEM normally needs to manage:

- vehicle programme and product development;
- configurable vehicle structure;
- production allocation;
- body and final-assembly sequencing;
- inbound JIT/JIS;
- supplier quality;
- vehicle production;
- vehicle distribution;
- dealer allocation;
- warranty;
- service parts;
- regulatory compliance.

## Tier-1 supplier

A Tier-1 supplier may receive demand from several OEMs.

It commonly needs:

- customer scheduling agreements;
- forecast and JIT releases;
- sequence calls;
- customer-specific packaging;
- cumulative quantities;
- repetitive or make-to-sequence production;
- outbound ASN and EDI;
- self-billing reconciliation;
- returnable-container tracking;
- supplier call-offs to lower tiers.

## Tier-2 or component supplier

The company may have less JIS complexity but still require:

- long-term forecast collaboration;
- scheduling agreements;
- serial or batch traceability;
- quality complaints;
- contract pricing;
- customer self-billing;
- constrained material planning.

## National sales company or importer

Its core processes are different:

- vehicle procurement from OEM;
- country allocation;
- homologation;
- inbound vehicle logistics;
- dealer distribution;
- pricing;
- incentives;
- registration;
- warranty and service.

## Dealer group

A dealer requires:

- vehicle inventory;
- quotation and sales;
- trade-in;
- workshop scheduling;
- repair orders;
- parts;
- warranty;
- customer communication;
- finance integration.

A dealer management system is not automatically included just because the manufacturer uses S/4HANA. SAP’s current automotive portfolio lists Vehicle Sales and Service as a partner application, demonstrating that full dealer operations may require an industry partner solution rather than only core S/4HANA.

## Aftermarket and service organisation

The business focuses on:

- installed base;
- technical objects;
- service contracts;
- dealer and workshop operations;
- spare-parts forecasting;
- service-level planning;
- returns and remanufacturing;
- warranty claims;
- supplier recovery.

A useful SAP Automotive design must therefore begin with the business archetype.

Installing every automotive capability everywhere creates unnecessary complexity.

## The complete SAP Automotive architecture

A modern target architecture can be represented as:

```text
Product strategy and engineering
SAP Integrated Product Development / PLM / engineering systems
                         |
                         v
Product and manufacturing definition
S/4HANA product master, variant configuration, BOM, routing
                         |
                         v
Demand and supply planning
SAP IBP + S/4HANA MRP + embedded PP/DS
                         |
           +-------------+-------------+
           |                           |
           v                           v
Supplier collaboration           Customer demand
Business Network                 Scheduling agreements
Forecast / PO / quality          JIT and sequence calls
           |                           |
           +-------------+-------------+
                         |
                         v
Manufacturing execution
S/4HANA Manufacturing + SAP Digital Manufacturing
                         |
                         v
Inbound, line supply, warehouse and transport
EWM + TM + Yard + returnable packaging
                         |
                         v
Finished vehicle or component delivery
Sales, delivery, ASN, self-billing, trade compliance
                         |
                         v
Vehicle sales, warranty and aftermarket
Service, service parts, dealer applications, claims
                         |
                         v
Cross-company data ecosystem
SAP Industry Network for Automotive / Catena-X
```

The architecture is broad because the automotive value chain is broad.

The main design discipline is to assign one authoritative owner to each object and decision.

## Part I: Product development and the automotive digital thread

Automotive companies do not begin with an ERP material.

They begin with:

- customer and regulatory requirements;
- platform architecture;
- engineering design;
- hardware and software components;
- product variants;
- manufacturing feasibility;
- cost targets.

SAP currently positions SAP Integrated Product Development as a cloud PLM capability that links requirements, engineering data, specifications, product models, change management and SAP S/4HANA, while supporting bidirectional product-data synchronisation and digital-thread scenarios.

## Engineering BOM versus manufacturing BOM

The engineering BOM answers:

> What constitutes the engineered product?

The manufacturing BOM answers:

> How will this product be built at a specific plant?

They may differ because manufacturing needs:

- plant-specific components;
- assembly sequence;
- phantom assemblies;
- packaging;
- substitutes;
- production-relevant grouping.

A common flow is:

```text
Engineering structure
→ engineering release
→ manufacturing review
→ manufacturing BOM
→ routing and production version
→ production planning
```

The handover should preserve:

- component identity;
- revision;
- effectivity;
- change number;
- configuration dependency;
- traceability to the original requirement.

## Engineering change management

An automotive engineering change can affect:

- open purchase orders;
- supplier tooling;
- stock;
- production orders;
- service parts;
- warranty;
- homologation;
- vehicles already in the field.

A valid change process must define:

1. which products or vehicles are affected;
2. from which date, serial number or production position it applies;
3. what happens to old stock;
4. whether the old and new components are interchangeable;
5. which suppliers must be notified;
6. how service parts are handled.

The change is not complete when the BOM is updated.

It is complete when the downstream supply and service processes understand the effectivity.

## Software-defined vehicle problem

The vehicle increasingly combines:

- physical hardware;
- embedded software;
- cloud services;
- digital features;
- licenses.

A traditional material BOM is not sufficient to represent every software relationship.

The architecture may need to connect:

- engineering configuration;
- hardware serials;
- software versions;
- vehicle identity;
- entitlement;
- service update history.

S/4HANA should remain the commercial and operational core.

It should not be forced to replace specialist software-development lifecycle systems.

## Product Lifecycle Costing

Automotive programmes require cost visibility before production begins.

Cost may include:

- purchased components;
- manufacturing operations;
- tooling;
- logistics;
- warranty provision;
- engineering effort;
- programme investment.

SAP’s current automotive portfolio includes Product Lifecycle Costing as a product-development and margin-management capability.

The estimated lifecycle cost should later be reconciled with:

- standard cost;
- purchase prices;
- production variance;
- warranty;
- actual logistics cost.

Otherwise, the early business case and operational economics become unrelated models.

## Part II: Configurable products and vehicle structures

Automotive products often have a high number of valid variants.

A vehicle may differ by:

- engine or electric drivetrain;
- battery;
- body style;
- colour;
- market;
- steering side;
- interior;
- assistance package;
- emissions class;
- software package.

Creating one independent material for every possible vehicle configuration is normally impractical.

## Variant configuration

SAP variant configuration can represent:

- configurable material;
- characteristics;
- characteristic values;
- configuration profiles;
- dependencies;
- constraints;
- variant conditions;
- configuration-relevant BOM selection;
- operation selection.

Example:

```text
Characteristic: MARKET
Values: EU, US, CN

Characteristic: DRIVE
Values: FWD, AWD

Constraint:
US market + selected engine
requires emissions package US-3
```

## Configuration is not only sales logic

The same configuration may influence:

- customer quotation;
- material selection;
- production operations;
- purchasing;
- costing;
- compliance;
- vehicle documentation;
- service parts.

A configuration accepted by Sales must also be:

- manufacturable;
- procurable;
- homologated;
- serviceable.

## Super BOM and super routing

A configurable product may use broad structures containing alternative components and operations.

Dependencies select the relevant elements for the specific configuration.

The advantage is reuse.

The risk is complexity.

A super BOM can become difficult to:

- test;
- explain;
- change;
- cost;
- integrate with external engineering systems.

## Configuration lifecycle

The organisation should preserve:

```text
Quoted configuration
→ ordered configuration
→ planned configuration
→ built configuration
→ delivered configuration
→ current field configuration
```

These versions may differ legitimately.

For example:

- the customer changes an option before the freeze date;
- a component is substituted during production;
- software is updated after delivery.

Do not overwrite historical configurations with the latest state.

## Part III: Demand in automotive is usually schedule-driven

Many automotive suppliers do not receive isolated sales orders for every delivery.

Instead, the commercial relationship is based on a scheduling agreement.

## Scheduling agreement

A sales scheduling agreement can represent a long-running customer relationship containing:

- customer;
- material;
- plant;
- validity;
- pricing;
- delivery rules;
- schedule lines;
- cumulative quantities.

The customer then sends demand releases against the agreement.

## Forecast delivery schedule

The forecast schedule provides medium- or longer-term demand.

It supports:

- capacity planning;
- procurement;
- production planning;
- labour planning.

Its quantities may change frequently.

It should not automatically be interpreted as a firm shipping instruction.

## JIT delivery schedule or call

A JIT call gives more operational demand.

It may specify:

- quantity;
- required date and time;
- unloading point;
- call number;
- customer reference;
- packaging;
- delivery sequence.

## Sequenced JIT call

A sequenced call adds sequence information.

It may identify:

- vehicle;
- production position;
- component variant;
- sequence number;
- exact consumption order.

## Release horizons

A customer may communicate demand across several zones.

For example:

```text
Forecast zone:
planning information, still volatile

Material release zone:
buyer authorises material procurement

Production release zone:
supplier may produce

Shipping release zone:
supplier should ship
```

The legal interpretation depends on the customer agreement.

SAP configuration should not invent the commercial meaning.

## EDI in automotive

Common integration standards include variants of:

- VDA messages;
- EDIFACT DELFOR;
- EDIFACT DELJIT;
- ANSI X12;
- Odette;
- customer-specific XML or API formats.

The difficulty is not only message conversion.

The system must understand:

- message purpose;
- customer agreement;
- schedule version;
- cumulative quantities;
- replacement logic;
- cancellation;
- time zone;
- unloading point;
- packaging.

Integration middleware can transform syntax.

It cannot determine whether the new schedule legally replaces the old one unless the business rules are explicit.

## Cumulative quantities

Automotive scheduling agreements often use cumulative quantities to reconcile what:

- the customer believes was received;
- the supplier believes was delivered;
- the agreement has called off.

A discrepancy can cause:

- too much supply;
- too little supply;
- incorrect open quantity;
- invoice mismatch.

Cumulative quantity control should include:

- start date;
- reset point;
- customer cumulative received quantity;
- supplier cumulative delivered quantity;
- correction process;
- audit.

## The most dangerous EDI mistake

A common weak design is:

```text
Message received successfully
= business demand accepted
```

These are not equivalent.

A technically valid message may contain:

- wrong customer material;
- unexpected quantity;
- past date;
- impossible sequence;
- cumulative mismatch;
- unknown unloading point.

The integration should produce a business validation result, not only a green interface status.

## Part IV: JIT and JIS

## Just in time

JIT supply aims to deliver material near the time of consumption.

It reduces line-side inventory.

It increases dependence on:

- accurate demand;
- reliable transport;
- stable production;
- supplier responsiveness;
- real-time integration.

## Just in sequence

JIS adds sequence.

The supplier does not only deliver the correct quantity.

It delivers components in the order in which they will be consumed.

Typical JIS products include:

- seats;
- dashboards;
- door modules;
- bumpers;
- interior modules.

## A simplified JIS flow

```text
OEM freezes production sequence
→ sequence call sent to supplier
→ supplier selects or produces correct variants
→ components packed into sequence racks
→ transport dispatched
→ racks arrive at line
→ components consumed in vehicle sequence
```

## Sequence reference

The process may identify demand by:

- production position;
- planned order;
- body number;
- vehicle identification;
- sequence number.

Every participant must understand the same sequence identity.

## JIS is fragile by design

JIS reduces buffer.

The reduced buffer removes recovery time.

Disruption may originate from:

- vehicle removed from sequence;
- rework;
- paint-shop delay;
- component quality issue;
- supplier-machine failure;
- traffic;
- incorrect rack;
- missing EDI message.

A good JIS implementation therefore requires explicit exception processes.

## Sequence changes

The company must decide how to handle:

- vehicle removed;
- vehicle reinserted;
- sequence swapped;
- duplicate call;
- late call;
- missing position;
- wrong component already produced.

Possible actions include:

- skip;
- resequence;
- buffer;
- emergency replacement;
- manual line-side intervention.

## JIT/JIS systems boundary

S/4HANA can own:

- customer agreement;
- JIT call;
- delivery demand;
- inventory posting;
- billing.

PP/DS or another sequencing solution may own:

- production feasibility;
- resource sequence;
- supplier production sequence.

Digital Manufacturing may own:

- shop-floor execution;
- actual assembly status.

EWM may own:

- picking;
- sequencing;
- rack handling;
- line staging.

TM may own:

- transport;
- departure;
- arrival.

No single application should claim the entire process without integration.

## Do not use JIS where the process is not stable enough

JIS is not automatically more advanced than JIT.

It is appropriate only when:

- final sequence is sufficiently stable;
- supplier response time is achievable;
- product variability justifies sequencing;
- quality is predictable;
- transport is reliable;
- emergency recovery exists.

Otherwise, the company removes inventory but replaces it with disruption cost.

## Part V: Supply planning and procurement

The automotive supply network contains multiple tiers.

An OEM demand change can propagate through:

```text
OEM
→ Tier-1 module supplier
→ Tier-2 component supplier
→ raw-material producer
```

Traditional MRP sees only the data inside one enterprise unless external commitments are integrated.

## SAP IBP

SAP IBP currently combines S&OP, demand planning, response and supply, demand-driven replenishment and inventory planning. It supports multilevel network planning, scenario comparison and constrained response planning.

For automotive, IBP can support:

- programme forecast;
- market demand;
- capacity scenario;
- supplier constraint;
- battery and semiconductor allocation;
- inventory targets;
- disruption response.

## IBP is not JIT execution

IBP answers:

> How should demand and supply be balanced across the network?

JIT processing answers:

> What must be delivered against this specific operational call?

Do not send every sequence call into tactical planning as though it were a new independent forecast.

## S/4HANA MRP

MRP creates operational supply proposals based on:

- customer schedules;
- planned requirements;
- dependent requirements;
- stock;
- receipts.

Outputs can include:

- planned orders;
- purchase requisitions;
- scheduling lines;
- stock transfers.

## PP/DS

SAP S/4HANA Manufacturing for planning and scheduling provides embedded advanced planning with material and capacity constraints, exception-based planning and detailed scheduling.

It is relevant for automotive when the business needs:

- finite bottleneck capacity;
- setup optimisation;
- sequence-dependent production;
- alternative resources;
- short-term detailed scheduling.

## Supplier collaboration

SAP Business Network Supply Chain Collaboration currently supports:

- forecast collaboration;
- supplier commitments;
- purchase orders;
- order confirmations;
- shipment visibility;
- scheduling agreements;
- supplier-managed inventory;
- quality and manufacturing collaboration.

This can provide earlier evidence of supply feasibility.

But a network portal does not ensure supplier adoption.

The supplier may still operate through:

- EDI;
- local portal;
- email;
- spreadsheet;
- another customer network.

The integration strategy must support the real supplier ecosystem.

## Supplier commitment hierarchy

A mature model distinguishes:

```text
Forecast
→ supplier forecast response
→ purchase requirement
→ purchase order or schedule
→ supplier confirmation
→ shipment notice
→ goods receipt
```

Each step has a different confidence level.

## Quota and alternative sourcing

Automotive sourcing may need to divide volume across suppliers.

Possible reasons include:

- capacity;
- risk;
- localisation;
- quality;
- price;
- regulatory requirement.

The system should distinguish:

- strategic allocation;
- operational source determination;
- emergency substitution.

## Part VI: Manufacturing and sequence execution

Automotive final assembly combines:

- high volume;
- high variety;
- strict takt;
- complex component synchronisation.

## S/4HANA Manufacturing

The ERP layer normally owns:

- planned order;
- production order;
- component requirements;
- goods issue;
- confirmation;
- goods receipt;
- cost.

## Digital Manufacturing

SAP Digital Manufacturing is SAP’s current cloud manufacturing-operations platform. It connects shop-floor execution with planning and logistics, supports worklists, labour, production controls, rework and resource orchestration.

It may own:

- operator execution;
- work instructions;
- production status;
- nonconformance capture;
- labour confirmation;
- machine integration;
- actual production sequence.

## MES integration

The plant may already have:

- SAP Digital Manufacturing;
- SAP ME/MII;
- a plant-specific MES;
- OEM proprietary sequencing system.

The architecture must define one owner for:

- order dispatch;
- sequence;
- operation completion;
- serial genealogy;
- scrap;
- rework.

## Takt and production sequence

A final-assembly sequence is not only a list of vehicles.

It must respect constraints such as:

- option density;
- labour;
- colour;
- battery type;
- component availability;
- station capacity;
- ergonomic limits.

A planning system can generate a feasible sequence.

The shop floor may still change it because of disruption.

The actual sequence must feed:

- JIS calls;
- component staging;
- vehicle status;
- supplier reconciliation.

## Production backflush

High-volume automotive production may use automatic component consumption based on production confirmation.

This reduces transactional effort.

It assumes:

- BOM accuracy;
- quantity accuracy;
- controlled scrap;
- correct production version;
- reliable confirmations.

Backflush does not mean the physical component inventory is automatically correct.

## Serialised genealogy

For safety- or warranty-relevant components, the company may need to know:

- which serialised component;
- was installed in which vehicle;
- at which station;
- on which date;
- from which supplier batch.

The genealogy should connect:

```text
Supplier batch or serial
→ goods receipt
→ warehouse handling
→ production consumption
→ vehicle VIN
→ customer and warranty lifecycle
```

## Rework

A vehicle may leave the normal production sequence for rework.

This affects:

- JIS demand;
- component consumption;
- vehicle status;
- planned completion;
- outbound logistics.

Rework cannot be managed only as free text.

It requires:

- reason;
- location;
- required operations;
- new status;
- completion evidence.

## Part VII: Warehouse, line supply, and returnable packaging

Automotive logistics includes:

- inbound supplier receipt;
- supermarkets;
- line-side supply;
- Kanban;
- sequenced racks;
- finished vehicle yards;
- spare-parts warehouses.

## SAP EWM

SAP EWM supports high-volume warehouse operations, integration with production and quality, automation, stock transparency, waves, batches, serial numbers and warehouse robotics.

## Production supply

EWM can support:

- order-specific staging;
- release-order staging;
- crate-part staging;
- Kanban;
- production supply areas;
- component returns;
- finished-product receipt.

## Warehouse supply versus JIT supply

These are related but different.

### Warehouse replenishment

Moves stock from reserve to the production supply area.

### Supplier JIT

Triggers supply from an external or internal supplier against a call.

### JIS staging

Preserves the required production sequence.

A company can have all three in one material flow.

## Handling units

Automotive materials frequently move in:

- racks;
- pallets;
- boxes;
- totes;
- special load carriers.

The handling unit may carry:

- packaging ID;
- product;
- quantity;
- batch;
- sequence;
- destination;
- supplier.

## Returnable packaging

Returnable racks and containers are operationally critical.

A missing container can stop supply even when the component itself is available.

SAP Returnable Packaging Management currently supports packaging-account visibility, receipts and returns, planning, rental processes, packaging agreements and partner collaboration.

## Returnable-container loop

```text
Empty container at OEM
→ returned to supplier
→ filled by supplier
→ delivered to OEM
→ unloaded and consumed
→ empty container available again
```

The company needs visibility into:

- full containers;
- empty containers;
- containers in transit;
- damaged containers;
- containers at partners;
- cleaning or repair;
- ownership.

## Container management limitations

The system cannot detect every lost container without physical discipline.

Container balances become unreliable when:

- scans are skipped;
- packaging IDs are reused;
- partner movements are delayed;
- damaged containers are not reported;
- one party counts quantity and another counts individual assets.

## Finished vehicle yard

A completed vehicle may move through:

- production completion;
- quality hold;
- rework;
- storage;
- accessory installation;
- transport staging;
- carrier loading.

A vehicle yard differs from a conventional pallet warehouse.

The asset is:

- individually identified;
- high value;
- movable under its own power;
- configuration-specific;
- sensitive to damage;
- often subject to status and document controls.

## Part VIII: Transportation and inbound control

Automotive transport includes:

- inbound milk runs;
- JIT shuttles;
- sequence deliveries;
- finished vehicle logistics;
- service-parts transport;
- export transport.

## SAP Transportation Management

SAP TM currently supports transportation planning, tendering, carrier management, shipment execution and freight settlement.

## Inbound milk run

A milk run consolidates collections from several suppliers.

It may reduce:

- transport cost;
- empty mileage;
- receiving variability.

It requires:

- stable pickup windows;
- packaging readiness;
- capacity planning;
- supplier execution;
- route monitoring.

## JIT transport

JIT transport should align:

- call-off time;
- supplier preparation;
- loading;
- travel;
- gate;
- unloading;
- line-side staging.

A transport ETA is not enough.

The system should identify whether the delay threatens production consumption.

## TM and EWM integration

TM may own:

- freight order;
- carrier;
- route;
- departure;
- cost.

EWM may own:

- receiving;
- unloading;
- staging;
- loading;
- warehouse tasks.

The two systems must agree on:

- transportation unit;
- cargo readiness;
- door;
- actual quantity;
- departure.

## Global Trade Services

Automotive supply networks operate across borders.

SAP GTS currently supports:

- sanctions screening;
- import and export compliance;
- customs;
- tariff classification;
- preference and free-trade processes;
- communication with customs systems.

Trade compliance can block:

- customer order;
- delivery;
- export;
- procurement.

A warehouse or transport agent should never bypass a GTS block to “protect delivery.”

## Finished vehicle logistics

Vehicle distribution may involve:

- factory yard;
- rail;
- truck;
- port;
- compound;
- dealer.

The transport unit is not always a pallet or container.

The architecture should retain vehicle-level:

- VIN;
- location;
- status;
- carrier;
- damage;
- estimated arrival;
- handover.

## Part IX: Vehicle Management

A finished vehicle requires a different management model from an anonymous finished-goods material.

## Vehicle identity

A vehicle can have:

- internal vehicle number;
- VIN;
- model;
- configuration;
- production order;
- sales order;
- plant;
- current location;
- status;
- dealer;
- owner.

## Vehicle Management System

Vehicle Management System is a long-established SAP automotive capability used in some on-premises and private-cloud automotive landscapes to manage individual vehicles through logistics and sales status chains.

Conceptually, VMS provides a vehicle object connecting:

- configuration;
- procurement or production;
- inventory;
- vehicle location;
- sales;
- actions and statuses.

## Vehicle action and status model

A vehicle lifecycle may contain actions such as:

```text
Vehicle created
→ production planned
→ produced
→ quality released
→ assigned to importer
→ transported
→ assigned to dealer
→ sold
→ delivered
```

Each action may:

- change status;
- create an ERP document;
- update location;
- trigger follow-up.

## Why VMS implementations become complex

The vehicle status model often accumulates:

- country-specific steps;
- dealer steps;
- logistics steps;
- finance approvals;
- custom actions;
- external-system states.

If every local exception becomes a new status, the lifecycle becomes impossible to govern.

## VMS is not automatically a modern dealer platform

VMS can manage the individual vehicle and related logistics.

A dealer management system may additionally need:

- lead management;
- trade-in;
- workshop;
- technician planning;
- parts;
- customer communication;
- dealer accounting.

SAP’s current portfolio positions Vehicle Sales and Service as a partner application, not a universally included S/4HANA core capability.

This is an important procurement question:

> Does the company require vehicle logistics, dealer management, or both?

## Vehicle object versus equipment

After sale, the vehicle may also be represented as a technical object for:

- service;
- warranty;
- installed base;
- maintenance history.

The architecture should link vehicle identity without creating uncontrolled duplicate records.

## Part X: Sales, outbound logistics, and customer collaboration

An automotive Tier-1 supplier may deliver against scheduling agreements rather than ordinary discrete orders.

A vehicle OEM or importer may sell configured vehicles through:

- dealers;
- direct sales;
- fleet customers;
- leasing companies.

## Sales scheduling agreement fulfilment

The process can be:

```text
Customer forecast
→ scheduling agreement update
→ JIT call
→ delivery creation
→ picking or production
→ ASN
→ goods issue
→ customer receipt
→ self-billing
```

## Delivery creation

Deliveries may be grouped or split by:

- unloading point;
- route;
- time window;
- JIT call;
- packaging;
- customer plant.

The document design must preserve customer references required for EDI reconciliation.

## Advance shipping notification

The ASN may communicate:

- delivery;
- material;
- quantity;
- handling unit;
- batch or serial;
- carrier;
- departure;
- expected arrival;
- customer call reference.

The customer may use the ASN to:

- plan receiving;
- update expected supply;
- prepare line-side demand;
- create self-billing.

## Customer material number

Automotive customers often reference their own part numbers.

The supplier must map:

- internal material;
- customer material;
- revision;
- plant;
- packaging;
- validity.

One customer part number may not always map permanently to one supplier material.

Engineering changes make validity essential.

## Pricing

Automotive pricing may include:

- base part price;
- raw-material surcharge;
- indexation;
- tooling amortisation;
- freight;
- packaging;
- retrospective adjustment.

Pricing changes can be retroactive.

The architecture must decide whether the change affects:

- future deliveries only;
- open deliveries;
- already billed quantities;
- self-billing corrections.

## Part XI: Self-billing

In automotive, the customer may create the billing document based on its received quantities and agreed price.

The supplier then receives a self-billing message.

This reverses the conventional assumption that the supplier always issues the invoice first.

## Self-billing process

```text
Supplier ships
→ customer receives
→ customer calculates payable amount
→ customer sends self-billing document
→ supplier compares with internal billing
→ difference handled
→ receivable cleared
```

## Common differences

- quantity;
- receipt date;
- price;
- cumulative quantity;
- customer material;
- tax;
- freight;
- credit;
- rejected delivery.

SAP Self-Billing Cockpit currently receives and verifies customer self-billing transmissions, compares them with internal invoices, supports tolerance controls and can create credit or debit adjustments for differences.

## Self-billing is not simple EDI posting

A self-billing document may be technically valid but commercially wrong.

The process needs:

- matching;
- simulation;
- tolerance;
- exception ownership;
- accounting reconciliation;
- payment reference.

## Dangerous automation

Do not automatically accept every customer self-billing amount merely because the customer is a strategic OEM.

Repeated differences may indicate:

- incorrect customer receipt;
- outdated price;
- failed ASN;
- wrong cumulative quantities;
- internal delivery error.

## Part XII: Quality, traceability, and complaints

Automotive quality management extends beyond internal inspection.

It includes:

- supplier quality;
- incoming inspection;
- production quality;
- customer complaint;
- containment;
- root cause;
- corrective action;
- warranty;
- supplier recovery.

## Supplier quality collaboration

SAP Business Network currently supports quality collaboration and visibility into supplier quality issues and complaints.

## Complaint process

A robust process may include:

```text
Defect reported
→ affected vehicle or component identified
→ containment
→ supplier and batch traced
→ root-cause analysis
→ corrective action
→ cost recovery
→ design or process feedback
```

## 8D and corrective action

Many automotive companies use structured problem-solving methods such as 8D.

The system should control:

- issue;
- owner;
- affected products;
- containment;
- root cause;
- action;
- verification;
- closure.

An attached PDF is not a controlled corrective-action process.

## Part traceability

SAP Industry Network for Automotive currently includes parts traceability packages intended to track serials, batches and components across organisations.

Cross-company traceability requires common:

- identity;
- event semantics;
- business partner identity;
- data-sharing agreement.

## Recall scope

A precise genealogy can reduce recall scope.

Instead of recalling every vehicle produced during one month, the company may identify:

- vehicles containing a specific supplier batch;
- production window;
- line;
- serial range.

The value depends on data completeness.

One missing consumption scan can invalidate the apparent precision.

## Warranty

A warranty process connects:

- vehicle;
- customer;
- coverage;
- repair;
- labour;
- parts;
- dealer claim;
- approval;
- supplier recovery;
- accounting.

## Warranty is both service and quality data

Warranty claims should feed:

- engineering;
- supplier quality;
- manufacturing quality;
- reliability analysis;
- financial provision.

If warranty remains isolated in the dealer system, the company loses product feedback.

## Part XIII: Service and aftermarket

The aftermarket has a different supply-chain structure.

Demand is:

- intermittent;
- long-tailed;
- geographically distributed;
- service-level-sensitive.

A part may be required many years after vehicle production ends.

## Extended service parts planning

SAP S/4HANA Supply Chain for extended service parts planning currently provides demand management, stocking decisions, multi-echelon inventory optimisation, economic order quantities, network supply planning and distribution for high-volume service-parts networks.

## Service-parts supersession

An old part may be replaced by:

- direct substitute;
- one-way substitute;
- kit;
- remanufactured part;
- upgraded part.

The system must know:

- compatibility;
- validity;
- customer or vehicle applicability;
- stock disposition.

## Intermittent demand

A part may have:

- zero demand for months;
- one urgent request;
- very high service impact.

Conventional forecast accuracy becomes misleading.

Planning should consider:

- installed base;
- failure rate;
- vehicle age;
- service target;
- criticality;
- supersession;
- repairability.

## Service management

SAP’s current service-management portfolio connects service contracts, field service, spare parts, returns, repairs, warranties and billing.

## Repair process

```text
Customer complaint
→ service diagnosis
→ warranty check
→ parts reservation
→ workshop or field service
→ labour and parts confirmation
→ claim or invoice
→ vehicle history updated
```

## Remanufacturing

Returned automotive parts may be:

- inspected;
- repaired;
- remanufactured;
- reused;
- scrapped.

The process should preserve:

- core return;
- condition;
- serial;
- ownership;
- credit;
- refurbishment cost;
- new warranty.

## Part XIV: Catena-X and SAP Industry Network for Automotive

SAP currently positions SAP Industry Network for Automotive as a set of Catena-X-ready packages supporting cross-company parts traceability, carbon-footprint management, demand and capacity management, quality and circular-economy use cases.

## Catena-X is not one central database

The principle is controlled, sovereign data exchange between participants.

A company does not simply upload all supply-chain data to one shared platform.

It shares defined data for a defined use case under defined policies.

## Potential use cases

- parts traceability;
- demand and capacity visibility;
- quality;
- product carbon footprint;
- battery passport;
- circular economy;
- business-partner data.

## Business Partner Number

Cross-company data exchange requires common partner identity.

The business partner number supports identification across the ecosystem.

## Eclipse Dataspace Connector

SAP describes data-space connectivity through the Eclipse Dataspace Connector and SAP Integration Suite capabilities.

## Catena-X limitations

### Participation dependency

A use case creates value only when relevant partners participate.

### Data readiness

Companies must have governed:

- products;
- partners;
- serials;
- batches;
- events;
- carbon data.

### Semantic agreement

Sharing the same field name does not guarantee the same meaning.

### Commercial sensitivity

Capacity, cost and supply data may be strategically sensitive.

### Integration cost

A data connector does not automatically extract and validate the correct source information.

### Uncertain ROI

Catena-X should begin with a defined use case.

“Join the automotive data ecosystem” is not a complete business case.

## Part XV: Finance and controlling

Automotive finance must connect:

- programme cost;
- product cost;
- tooling;
- purchasing;
- production variance;
- logistics;
- warranty;
- customer settlement.

## Product costing

Standard cost may include:

- BOM components;
- routing activities;
- overhead;
- subcontracting;
- external processing.

## Actual cost and variance

Variance may originate from:

- purchase price;
- scrap;
- usage;
- labour;
- production volume;
- setup;
- rework.

## Tooling

Customer- or supplier-funded tooling may require:

- asset;
- project;
- amortisation;
- milestone billing;
- ownership;
- maintenance.

Tooling should not be hidden as one part-price condition if it is economically a separate investment.

## Customer profitability

A high-volume customer may still be unprofitable after:

- premium freight;
- packaging;
- quality claims;
- engineering changes;
- price corrections;
- self-billing effort.

Profitability analysis should connect operational causes to commercial accounts.

## Part XVI: System ownership

A mature architecture can assign ownership as follows.

| Business object or decision | Primary authority |
|---|---|
| Engineering requirement | PLM / requirements system |
| Engineering BOM | Engineering system / IPD |
| Manufacturing BOM | S/4HANA manufacturing definition |
| Product and material master | S/4HANA or governed MDG process |
| Product configuration | Governed configuration model |
| Tactical demand and supply plan | SAP IBP |
| Material replenishment proposal | S/4HANA MRP |
| Detailed production schedule | Embedded PP/DS or approved sequencing system |
| Customer scheduling agreement | S/4HANA Sales |
| JIT/JIS call | S/4HANA automotive process or dedicated execution layer |
| Supplier commitment | Business Network / supplier confirmation |
| Shop-floor execution | SAP Digital Manufacturing or plant MES |
| Warehouse task | SAP EWM |
| Freight order | SAP TM |
| Vehicle object | VMS or approved vehicle platform |
| Dealer process | Dealer management solution |
| Self-billing reconciliation | Self-Billing Cockpit / S/4HANA Finance |
| Service-parts network plan | Extended service parts planning |
| Warranty and repair transaction | Service and warranty process |
| Cross-company traceability | Industry Network / Catena-X use case |

The exact product can vary.

The ownership cannot remain ambiguous.

## Part XVII: Integration architecture

Automotive integration is not only SAP-to-SAP.

It includes:

- OEMs;
- suppliers;
- logistics providers;
- dealers;
- customs;
- shop-floor systems;
- engineering platforms.

## EDI gateway

The gateway may process:

- DELFOR;
- DELJIT;
- ASN;
- invoice;
- self-billing;
- quality;
- packaging.

It should provide:

- sender authentication;
- syntax validation;
- duplicate protection;
- message sequencing;
- control totals;
- business acknowledgement;
- monitoring.

## Integration Suite

SAP Integration Suite can mediate:

- APIs;
- EDI;
- events;
- partner connections;
- Catena-X data exchange.

But the middleware should not become the owner of:

- cumulative quantity;
- scheduling-agreement status;
- vehicle status;
- quality decision.

## Event-driven integration

Useful events include:

- engineering change released;
- supplier commitment changed;
- vehicle completed;
- sequence changed;
- shipment departed;
- quality defect confirmed;
- warranty claim approved.

The consumer should reread authoritative state before performing a critical action.

## Exactly-once processing

Automotive EDI messages may be resent.

The architecture needs business idempotency.

Possible keys include:

```text
Partner
+ message type
+ message number
+ call number
+ schedule version
```

Technical message ID alone may not be enough.

## Timing and clocks

JIT and JIS require consistent handling of:

- time zone;
- plant calendar;
- shift;
- daylight saving;
- timestamp precision.

A one-hour error may become a production stoppage.

## Part XVIII: Main limitations and traps

## Limitation 1: SAP for Automotive is not one licensed package

The required capabilities may involve:

- S/4HANA;
- IBP;
- EWM;
- TM;
- Digital Manufacturing;
- Business Network;
- GTS;
- service applications;
- partner products.

Commercial scope must be checked product by product.

## Limitation 2: Private and public cloud scope differs

Long-established automotive functions may not have identical scope in:

- on-premises S/4HANA;
- Cloud ERP Private;
- Cloud ERP Public.

A process available in a legacy ECC or private S/4HANA system should not be assumed to exist unchanged in Public Edition.

## Limitation 3: Legacy automotive customisation is deep

Many OEMs and suppliers have decades of custom code around:

- scheduling agreements;
- JIT;
- EDI;
- cumulative quantities;
- self-billing;
- vehicle management.

A technical conversion can preserve this complexity without improving the process.

## Limitation 4: Customer-specific EDI never disappears completely

Industry standards reduce variation.

Large OEMs still apply:

- customer-specific fields;
- interpretation;
- release policies;
- exception processes.

## Limitation 5: JIS has little tolerance for system failure

The operating model requires:

- high availability;
- message monitoring;
- degraded operation;
- emergency sequence;
- manual recovery.

## Limitation 6: Several systems may own production sequence

Possible owners include:

- PP/DS;
- MES;
- OEM sequencing system;
- JIT engine;
- custom plant application.

One must be authoritative.

## Limitation 7: Product configuration can become untestable

Thousands of dependencies create combinations nobody has validated.

Use automated configuration regression tests.

## Limitation 8: Engineering and manufacturing structures diverge

The ERP may build a structure different from the latest released engineering model.

Reconciliation must be continuous.

## Limitation 9: Supplier collaboration depends on supplier maturity

A network does not create data quality or capacity commitment by itself.

## Limitation 10: Cumulative quantity errors are financially material

A small reconciliation difference can propagate into:

- delivery quantities;
- open calls;
- self-billing;
- receivables.

## Limitation 11: Returnable packaging is often poorly scanned

The digital balance becomes more precise than the physical process.

## Limitation 12: Traceability creates large data volume

Vehicle and component genealogy may contain millions of relationships.

Retention and retrieval requirements must be designed.

## Limitation 13: Dealer operations may need partner solutions

Core ERP and VMS do not automatically equal a complete dealer-management platform.

## Limitation 14: Warranty remains disconnected from engineering

Claims are processed financially but do not improve product design.

## Limitation 15: Catena-X can become a technology programme without a use case

Begin with measurable traceability, capacity or carbon outcomes.

## Limitation 16: Automation reduces buffers but increases dependency

JIT, JIS, EDI and automation create efficiency under normal conditions.

They can amplify disruption when data or systems fail.

## Part XIX: Architecture by company type

## OEM target architecture

```text
IPD / engineering tools
→ S/4HANA product and manufacturing definition
→ IBP and PP/DS
→ supplier collaboration and JIT/JIS
→ Digital Manufacturing
→ EWM and TM
→ vehicle management
→ dealer distribution
→ service, warranty and service-parts planning
→ Catena-X traceability and sustainability
```

## Tier-1 supplier target architecture

```text
Customer EDI schedules and JIT calls
→ S/4HANA sales scheduling agreements
→ MRP and PP/DS
→ lower-tier supplier collaboration
→ Digital Manufacturing / MES
→ EWM sequence and packaging execution
→ TM and ASN
→ customer self-billing
→ quality complaint and recovery
```

## Dealer or importer target architecture

```text
OEM vehicle supply
→ vehicle inventory and logistics
→ dealer management / VSS
→ customer quotation and sale
→ registration and delivery
→ workshop and parts
→ warranty and claims
→ finance and profitability
```

## Aftermarket target architecture

```text
Installed base and vehicle population
→ service-parts demand
→ extended service parts planning
→ procurement and distribution
→ EWM and transport
→ dealer or service order
→ warranty and repair
→ remanufacturing and core return
```

## Part XX: Implementation approach

## Phase 1: Identify the business archetype

Do not use one global automotive template for:

- OEM;
- Tier-1;
- importer;
- dealer;
- aftermarket.

## Phase 2: Map external commitments

Document:

- customer schedules;
- release zones;
- JIT calls;
- sequence calls;
- supplier commitments;
- self-billing.

## Phase 3: Establish product identity

Connect:

- engineering part;
- SAP material;
- customer part;
- supplier part;
- serial;
- vehicle VIN;
- service part.

## Phase 4: Design configuration governance

Define:

- authoring authority;
- release;
- effectivity;
- validation;
- manufacturing handover.

## Phase 5: Choose planning authority

Separate:

- IBP tactical plan;
- MRP material plan;
- PP/DS finite schedule;
- MES execution sequence.

## Phase 6: Build EDI canonical models

Do not build separate ungoverned mapping logic for every customer message.

Create reusable business representations for:

- forecast release;
- JIT call;
- sequence call;
- ASN;
- self-billing.

## Phase 7: Design the exception model

Test:

- missing schedule;
- duplicate JIT call;
- cumulative mismatch;
- sequence change;
- supplier shortage;
- delayed transport;
- quality block;
- incorrect self-billing.

## Phase 8: Connect physical execution

Include:

- handling units;
- containers;
- line-side supply;
- sequence racks;
- yard;
- transport.

## Phase 9: Close the financial loop

Reconcile:

- delivery;
- receipt;
- billing;
- self-billing;
- payment;
- quality recovery;
- rebate.

## Phase 10: Close the product feedback loop

Connect:

- complaint;
- warranty;
- component genealogy;
- supplier;
- engineering change.

## KPIs that matter

## Customer schedules

- schedule-change frequency;
- forecast volatility;
- release-horizon stability;
- cumulative-quantity difference;
- JIT-call processing latency.

## Supply

- supplier commitment;
- confirmed capacity gap;
- shortage lead time;
- premium-freight dependency;
- Tier-2 visibility.

## JIT/JIS

- sequence-call completeness;
- sequence adherence;
- emergency resequencing;
- line-stop minutes;
- missed call;
- wrong variant delivered.

## Production

- schedule adherence;
- takt loss;
- rework;
- configuration error;
- sequence stability;
- component shortage.

## Logistics

- ASN accuracy;
- container balance;
- inbound punctuality;
- line-side availability;
- vehicle-yard dwell time;
- premium freight.

## Quality

- defects per vehicle or component;
- containment time;
- 8D cycle time;
- affected serial population;
- supplier recovery.

## Commercial and finance

- self-billing discrepancy;
- retroactive price correction;
- customer profitability;
- warranty cost;
- tooling recovery.

## Aftermarket

- service-parts fill rate;
- emergency order;
- backorder;
- obsolete stock;
- supersession success;
- first-time repair rate.

## Questions managers should ask

1. Are we an OEM, supplier, importer, dealer or service organisation for this process?
2. Which system owns the engineering product?
3. Which system owns the manufacturing product?
4. How are changes and effectivity transferred?
5. Which system owns product configuration?
6. Can every accepted configuration be produced and serviced?
7. Which customer schedule is informational?
8. Which release authorises procurement, production and shipment?
9. How are cumulative quantities reconciled?
10. Which system owns the production sequence?
11. Which system sends the JIS sequence to suppliers?
12. What happens when the sequence changes?
13. Can production continue during an EDI outage?
14. Which supplier confirmation is binding?
15. Does supplier capacity enter the planning process?
16. Who owns returnable-container balances?
17. Can every critical component be traced to a VIN?
18. Which system owns the finished vehicle object?
19. Do we require VMS, a dealer system, or both?
20. How are self-billing differences handled?
21. Does warranty information reach engineering and supplier quality?
22. Which system plans long-tail service parts?
23. Which Catena-X use case has measurable value?
24. Which automotive functions require private-cloud or on-prem scope?
25. How much custom code exists only because the original business rule was never standardised?

## The management conclusion

SAP for Automotive is not an ERP template with an automotive logo.

It is a connected operating architecture across:

- product development;
- configuration;
- demand planning;
- scheduling agreements;
- JIT and JIS;
- supplier collaboration;
- constrained manufacturing;
- warehouse and transport execution;
- vehicle lifecycle;
- self-billing;
- service parts;
- warranty;
- cross-company traceability.

SAP’s current automotive portfolio reflects this breadth, combining S/4HANA with Integrated Product Development, IBP, Business Network, Manufacturing for planning and scheduling, Digital Manufacturing, EWM, TM, GTS, service applications and Industry Network for Automotive.

The deepest automotive problems are not created by missing screens.

They are created at the boundaries:

- engineering part versus manufacturing material;
- forecast versus firm release;
- customer call versus feasible supply;
- planned sequence versus actual sequence;
- ERP quantity versus customer cumulative quantity;
- delivery versus self-billing;
- component serial versus vehicle VIN;
- warranty claim versus root cause.

A strong SAP Automotive architecture makes those boundaries explicit and controlled.

A weak one connects every system technically while leaving the meaning of the data unresolved.

The decisive test is:

> Can the company trace one customer requirement from forecast and configuration through supplier commitment, production sequence, component genealogy, delivery, self-billing, warranty and financial result?

When the answer is yes, SAP supports a real automotive operating model.

When the answer is no, the landscape may process millions of messages while the business still manages the critical sequence in spreadsheets and emergency calls.

---

### SAP Automotive architecture checklist

- [ ] The company’s automotive business archetype is explicit.
- [ ] SAP Automotive is understood as a portfolio, not one module.
- [ ] Engineering and manufacturing product structures have clear owners.
- [ ] Engineering changes include effectivity and downstream impact.
- [ ] Product configuration is governed and regression tested.
- [ ] Quoted, ordered, built and delivered configurations are retained.
- [ ] Customer and supplier part-number mappings include validity.
- [ ] Forecast, material release, production release and shipping release are distinguished.
- [ ] Scheduling agreements have explicit commercial meaning.
- [ ] JIT and JIS calls use stable business identities.
- [ ] Duplicate and replacement message logic is controlled.
- [ ] Cumulative quantities are regularly reconciled.
- [ ] IBP, MRP, PP/DS and MES responsibilities are separated.
- [ ] One system owns the production sequence.
- [ ] Sequence changes have controlled recovery processes.
- [ ] Supplier forecast responses are not confused with order confirmations.
- [ ] Business Network adoption matches supplier reality.
- [ ] EWM, production and JIT staging responsibilities are explicit.
- [ ] Returnable packaging is physically scanned and reconciled.
- [ ] TM planning reflects JIT consumption risk.
- [ ] Trade blocks cannot be bypassed by logistics.
- [ ] Component genealogy links supplier material to vehicle VIN.
- [ ] Quality complaints lead to corrective action and supplier recovery.
- [ ] VMS and dealer-management scope are distinguished.
- [ ] One system owns each vehicle status.
- [ ] Self-billing documents are matched and simulated before adjustment.
- [ ] Warranty data returns to engineering and supplier quality.
- [ ] Service-parts planning accounts for intermittent demand and supersession.
- [ ] Catena-X participation begins with a defined business use case.
- [ ] Public, private and on-premises feature scope is verified.
- [ ] Automotive custom code has a clean-core disposition.
- [ ] Integration monitoring includes business impact, not only message status.
- [ ] System outage and degraded-operation procedures are tested.
- [ ] The company can trace one requirement through the complete automotive lifecycle.

### Sources and further reading

SAP’s current automotive industry portfolio covers product development, procurement, supplier collaboration, supply-chain planning, manufacturing, warehousing, transportation, vehicle sales, service parts, self-billing and industry-network use cases.

SAP Integrated Product Development currently supports requirements traceability, product and specification data, change control, engineering collaboration, digital twins and integration with S/4HANA.

SAP IBP currently combines S&OP, demand, inventory, response and supply planning and supports multilevel network planning and scenario simulation.

SAP Business Network Supply Chain Collaboration currently supports supplier forecasts and commitments, purchase orders, scheduling agreements, inventory collaboration, quality and contract-manufacturing processes.

SAP S/4HANA Manufacturing for planning and scheduling currently provides embedded constrained planning, detailed scheduling and feedback integration across ERP, manufacturing and logistics.

SAP Digital Manufacturing currently provides cloud manufacturing-operations management, execution worklists, resource orchestration, labour and shop-floor controls.

SAP EWM currently supports high-volume warehousing, production integration, automation, serial and batch control, yard coordination and advanced warehouse execution.

SAP TM currently supports transport planning, tendering, execution visibility and freight settlement.

SAP Returnable Packaging Management currently supports packaging-account balances, planning, rental management, agreements and partner collaboration.

SAP Self-Billing Cockpit currently supports receipt, matching, simulation and reconciliation of customer self-billing documents.

SAP S/4HANA Supply Chain for extended service parts planning currently supports demand history, stocking decisions, multi-echelon inventory optimisation and service-parts distribution planning.

SAP Industry Network for Automotive currently provides Catena-X-ready packages for parts traceability, demand and capacity management, carbon footprint, quality and circular-economy processes.

*Reviewed: July 2026. Automotive scope differs significantly across SAP S/4HANA on-premises, SAP Cloud ERP Private, SAP Cloud ERP Public, add-ons and partner products. JIT/JIS, Vehicle Management, warranty, dealer and industry-network designs must be validated against the exact release, Product Availability Matrix, licensing documents and current SAP road maps.*
