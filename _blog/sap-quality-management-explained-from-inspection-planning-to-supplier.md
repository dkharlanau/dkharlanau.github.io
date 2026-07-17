---
layout: blog
title: "SAP Quality Management Explained: From Inspection Planning to Supplier Quality, Production Control, Complaints, CAPA, and Certificates"
description: "recurring supplier defects; - production scrap; - delayed release of materials; - expired inspection lots; - customer complaints managed in email; -."
slug: sap-quality-management-explained-from-inspection-planning-to-supplier
permalink: /blog/sap-quality-management-explained-from-inspection-planning-to-supplier/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP industry solutions"
tags:
  - sap-industry-solutions
  - ai-operations
  - quality-management
canonical_url: https://dkharlanau.github.io/blog/sap-quality-management-explained-from-inspection-planning-to-supplier/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 37
migration_sequence: 48
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/why-sap-car-becomes-the-most-important-retail-system-nobody-can-clearly/
  - /blog/why-sap-retail-is-not-just-sap-mm-and-sd-the-complete-architecture-from/
---

## On this page

- [What SAP QM actually is](#what-sap-qm-actually-is)
- [Quality planning, control, assurance, and improvement](#quality-planning-control-assurance-and-improvement)
- [The core SAP QM objects](#the-core-sap-qm-objects)
- [Material or product quality settings](#material-or-product-quality-settings)
- [Inspection type](#inspection-type)
- [Inspection lot](#inspection-lot)
- [Inspection plan](#inspection-plan)
- [Master inspection characteristic](#master-inspection-characteristic)
- [Inspection method](#inspection-method)
- [Sampling procedure](#sampling-procedure)
- [Dynamic modification](#dynamic-modification)
- [Catalogue and code group](#catalogue-and-code-group)
- [Selected set](#selected-set)
- [Inspection point](#inspection-point)
- [Defect record](#defect-record)
- [Usage decision](#usage-decision)
- [Quality notification](#quality-notification)
- [Quality information record](#quality-information-record)
- [Certificate profile](#certificate-profile)
- [Quality level](#quality-level)
- [The end-to-end inspection lifecycle](#the-end-to-end-inspection-lifecycle)
- [Part I: Quality in procurement](#part-i-quality-in-procurement)
- [Supplier qualification is broader than an inspection lot](#supplier-qualification-is-broader-than-an-inspection-lot)
- [Quality in the purchasing process](#quality-in-the-purchasing-process)
- [Quality information record in procurement](#quality-information-record-in-procurement)
- [Source inspection](#source-inspection)
- [Goods-receipt inspection](#goods-receipt-inspection)
- [Stock posting after usage decision](#stock-posting-after-usage-decision)
- [Automatic usage decision](#automatic-usage-decision)
- [Supplier certificate at receipt](#supplier-certificate-at-receipt)
- [Supplier complaint](#supplier-complaint)
- [Chargeback and cost recovery](#chargeback-and-cost-recovery)
- [Supplier quality collaboration](#supplier-quality-collaboration)
- [Procurement-quality limitations](#procurement-quality-limitations)
- [Part II: Quality in manufacturing](#part-ii-quality-in-manufacturing)
- [In-process inspection](#in-process-inspection)
- [Inspection characteristics in routing or recipe](#inspection-characteristics-in-routing-or-recipe)
- [Process control versus laboratory control](#process-control-versus-laboratory-control)
- [Inspection points](#inspection-points)
- [Statistical process control](#statistical-process-control)
- [Goods receipt from production](#goods-receipt-from-production)
- [Rework](#rework)
- [Scrap](#scrap)
- [Production notification and nonconformance](#production-notification-and-nonconformance)
- [Integration with SAP Digital Manufacturing](#integration-with-sap-digital-manufacturing)
- [MES and machine integration](#mes-and-machine-integration)
- [Manufacturing-quality limitations](#manufacturing-quality-limitations)
- [Part III: Quality and EWM](#part-iii-quality-and-ewm)
- [S/4HANA QM owns the quality disposition](#s-4hana-qm-owns-the-quality-disposition)
- [EWM owns the physical warehouse execution](#ewm-owns-the-physical-warehouse-execution)
- [Typical EWM quality flow](#typical-ewm-quality-flow)
- [Inspection document and inspection lot](#inspection-document-and-inspection-lot)
- [Handling-unit level inspection](#handling-unit-level-inspection)
- [Partial acceptance](#partial-acceptance)
- [Quality work centre in warehouse](#quality-work-centre-in-warehouse)
- [Decentralised EWM](#decentralised-ewm)
- [Quality-stock bottleneck](#quality-stock-bottleneck)
- [Part IV: Quality in sales, delivery, and customer service](#part-iv-quality-in-sales-delivery-and-customer-service)
- [Outbound inspection](#outbound-inspection)
- [Customer-specific specifications](#customer-specific-specifications)
- [Quality certificate](#quality-certificate)
- [Certificate of analysis versus certificate of conformity](#certificate-of-analysis-versus-certificate-of-conformity)
- [Certificate limitations](#certificate-limitations)
- [Customer complaint](#customer-complaint)
- [Returns](#returns)
- [Warranty and service feedback](#warranty-and-service-feedback)
- [Part V: Batch management, serial numbers, and traceability](#part-v-batch-management-serial-numbers-and-traceability)
- [Batch management](#batch-management)
- [Batch traceability](#batch-traceability)
- [Batch status](#batch-status)
- [Serial numbers](#serial-numbers)
- [Traceability limitation](#traceability-limitation)
- [Part VI: Test equipment and calibration](#part-vi-test-equipment-and-calibration)
- [Test-equipment management](#test-equipment-management)
- [Calibration process](#calibration-process)
- [Out-of-tolerance equipment](#out-of-tolerance-equipment)
- [Integration with Asset Management](#integration-with-asset-management)
- [Part VII: Quality notifications, CAPA, and 8D](#part-vii-quality-notifications-capa-and-8d)
- [Notification structure](#notification-structure)
- [Containment versus corrective action](#containment-versus-corrective-action)
- [CAPA lifecycle](#capa-lifecycle)
- [8D](#8d)
- [Root-cause quality](#root-cause-quality)
- [Effectiveness check](#effectiveness-check)
- [Part VIII: Audit management, specifications, and product development](#part-viii-audit-management-specifications-and-product-development)
- [Product specifications](#product-specifications)
- [Inspection specification versus product specification](#inspection-specification-versus-product-specification)
- [Audit management](#audit-management)
- [FMEA](#fmea)
- [Control plan](#control-plan)
- [Part IX: LIMS integration](#part-ix-lims-integration)
- [Typical architecture](#typical-architecture)
- [Integration questions](#integration-questions)
- [Instruments](#instruments)
- [LIMS limitation](#lims-limitation)
- [Part X: Quality costs and financial integration](#part-x-quality-costs-and-financial-integration)
- [Cost of quality](#cost-of-quality)
- [SAP transactions behind quality cost](#sap-transactions-behind-quality-cost)
- [Cost of blocked stock](#cost-of-blocked-stock)
- [Cost recovery](#cost-recovery)
- [Part XI: Quality analytics](#part-xi-quality-analytics)
- [Incoming quality](#incoming-quality)
- [Production quality](#production-quality)
- [Customer quality](#customer-quality)
- [Process metrics](#process-metrics)
- [Inspection efficiency](#inspection-efficiency)
- [Leading versus lagging indicators](#leading-versus-lagging-indicators)
- [Part XII: AI in quality management](#part-xii-ai-in-quality-management)
- [Useful AI scenarios](#useful-ai-scenarios)
- [Weak AI scenarios](#weak-ai-scenarios)
- [Computer vision](#computer-vision)
- [AI limitation](#ai-limitation)
- [Part XIII: Where SAP QM is strong](#part-xiii-where-sap-qm-is-strong)
- [Where SAP QM is weaker](#where-sap-qm-is-weaker)
- [Full document control](#full-document-control)
- [Advanced laboratory execution](#advanced-laboratory-execution)
- [Sophisticated CAPA](#sophisticated-capa)
- [Advanced SPC and engineering quality](#advanced-spc-and-engineering-quality)
- [Supplier quality portal](#supplier-quality-portal)
- [Public-cloud scope](#public-cloud-scope)
- [Part XIV: Main limitations and traps](#part-xiv-main-limitations-and-traps)
- [Limitation 1: Master-data intensity](#limitation-1-master-data-intensity)
- [Limitation 2: Inspection-plan explosion](#limitation-2-inspection-plan-explosion)
- [Limitation 3: Result entry does not prove measurement](#limitation-3-result-entry-does-not-prove-measurement)
- [Limitation 4: Usage decisions become bottlenecks](#limitation-4-usage-decisions-become-bottlenecks)
- [Limitation 5: Quality stock can stop supply](#limitation-5-quality-stock-can-stop-supply)
- [Limitation 6: Defect codes remain weak](#limitation-6-defect-codes-remain-weak)
- [Limitation 7: Notifications become administrative archives](#limitation-7-notifications-become-administrative-archives)
- [Limitation 8: Attachments contain the real process](#limitation-8-attachments-contain-the-real-process)
- [Limitation 9: Supplier quality does not affect sourcing](#limitation-9-supplier-quality-does-not-affect-sourcing)
- [Limitation 10: Quality and engineering are disconnected](#limitation-10-quality-and-engineering-are-disconnected)
- [Limitation 11: QM and EWM statuses diverge](#limitation-11-qm-and-ewm-statuses-diverge)
- [Limitation 12: LIMS duplicates specifications](#limitation-12-lims-duplicates-specifications)
- [Limitation 13: Excessive inspection](#limitation-13-excessive-inspection)
- [Limitation 14: Excessive skipping](#limitation-14-excessive-skipping)
- [Limitation 15: Custom certificates create upgrade debt](#limitation-15-custom-certificates-create-upgrade-debt)
- [Limitation 16: Quality cost is invisible](#limitation-16-quality-cost-is-invisible)
- [Limitation 17: Quality ownership is unclear](#limitation-17-quality-ownership-is-unclear)
- [Limitation 18: Regulatory expectations exceed standard configuration](#limitation-18-regulatory-expectations-exceed-standard-configuration)
- [Part XV: Modern target architecture](#part-xv-modern-target-architecture)
- [Architecture for discrete manufacturing](#architecture-for-discrete-manufacturing)
- [Architecture for process industry](#architecture-for-process-industry)
- [Architecture for pharmaceuticals or medical devices](#architecture-for-pharmaceuticals-or-medical-devices)
- [Architecture for automotive](#architecture-for-automotive)
- [Part XVI: Migration from ECC QM to S/4HANA](#part-xvi-migration-from-ecc-qm-to-s-4hana)
- [Inspect the active scope](#inspect-the-active-scope)
- [Separate active from historical data](#separate-active-from-historical-data)
- [Open inspection lots](#open-inspection-lots)
- [Quality stock](#quality-stock)
- [Notifications](#notifications)
- [Custom enhancements](#custom-enhancements)
- [LIMS and equipment interfaces](#lims-and-equipment-interfaces)
- [EWM integration](#ewm-integration)
- [Part XVII: Implementation approach](#part-xvii-implementation-approach)
- [Phase 1: Define quality risk](#phase-1-define-quality-risk)
- [Phase 2: Map quality triggers](#phase-2-map-quality-triggers)
- [Phase 3: Define specification authority](#phase-3-define-specification-authority)
- [Phase 4: Design inspection plans](#phase-4-design-inspection-plans)
- [Phase 5: Design sampling and modification](#phase-5-design-sampling-and-modification)
- [Phase 6: Design stock consequences](#phase-6-design-stock-consequences)
- [Phase 7: Design notification workflows](#phase-7-design-notification-workflows)
- [Phase 8: Connect external systems](#phase-8-connect-external-systems)
- [Phase 9: Build exception handling](#phase-9-build-exception-handling)
- [Phase 10: Measure outcome](#phase-10-measure-outcome)
- [Questions managers and architects should ask](#questions-managers-and-architects-should-ask)
- [The management conclusion](#the-management-conclusion)

A company has implemented SAP Quality Management.

Incoming materials are placed into quality-inspection stock.

Inspectors record results.

Usage decisions are made.

Rejected materials are blocked.

The system appears to work.

Yet the business still experiences:

- recurring supplier defects;
- production scrap;
- delayed release of materials;
- expired inspection lots;
- customer complaints managed in email;
- corrective actions tracked in spreadsheets;
- certificates prepared manually;
- repeated quality holds with no root-cause closure.

SAP QM is recording quality events.

It is not necessarily managing quality.

This distinction matters.

> SAP QM can control whether a specific quantity, batch, delivery or production result is accepted. It does not automatically create an effective quality-management system.

A complete quality operating model must connect:

- product and process specifications;
- inspection planning;
- sampling;
- results recording;
- defects;
- stock disposition;
- supplier and customer communication;
- corrective action;
- engineering change;
- cost of poor quality;
- regulatory evidence.

SAP QM is strongest when quality must be embedded directly into procurement, inventory, manufacturing, sales and warehouse execution.

It is weaker when the company expects it to replace every capability of:

- a laboratory information management system;
- a document-management platform;
- a regulated electronic QMS;
- statistical engineering software;
- product lifecycle management;
- supplier relationship management.

The correct architecture uses SAP QM for transactional quality control while assigning adjacent quality responsibilities deliberately.

## What SAP QM actually is

SAP Quality Management is the quality-control and quality-assurance capability integrated into SAP’s transactional logistics processes.

It can support processes such as:

- inspection during procurement;
- source inspection at a supplier;
- goods-receipt inspection;
- in-process inspection;
- inspection at production completion;
- recurring inspection;
- stock inspection;
- delivery inspection;
- customer and supplier complaints;
- quality certificates;
- test-equipment calibration;
- quality-related stock decisions.

At its centre is a controlled relationship:

```text
Business event
→ inspection requirement
→ inspection lot
→ sample and characteristics
→ results and defects
→ usage decision
→ stock or process consequence
```

The most important word is **consequence**.

A quality result matters only when it changes what the business is allowed to do.

Examples:

- release stock;
- block stock;
- return material;
- rework production;
- create a supplier complaint;
- prevent delivery;
- require another inspection;
- change supplier status.

## Quality planning, control, assurance, and improvement

These terms are often mixed together.

### Quality planning

Defines what quality means before execution.

It includes:

- specification;
- inspection characteristics;
- methods;
- tolerances;
- sample size;
- inspection frequency;
- acceptance rules;
- responsible laboratory or work centre.

### Quality control

Measures actual output against the plan.

It includes:

- sample creation;
- result recording;
- defect recording;
- inspection completion;
- acceptance or rejection.

### Quality assurance

Provides evidence that controlled processes are operating consistently.

It may include:

- audit trail;
- approved inspection plans;
- certificates;
- supplier qualification;
- calibration;
- procedural controls.

### Quality improvement

Attempts to remove the cause of recurring failure.

It includes:

- root-cause analysis;
- corrective action;
- preventive action;
- engineering change;
- supplier development;
- process improvement.

SAP QM is strong in planning and transactional control.

It can support assurance and improvement.

It does not automatically ensure that corrective actions are effective.

## The core SAP QM objects

Understanding the object model is more important than memorising transactions.

## Material or product quality settings

Quality behaviour begins with the product master.

Quality-related settings can determine:

- whether an inspection is required;
- which inspection types are active;
- whether stock is posted to quality inspection;
- whether automatic usage decisions are permitted;
- whether certificate processing applies;
- whether procurement controls apply.

A material is not “QM active” in one universal way.

Different business events can trigger different inspection processes.

## Inspection type

An inspection type represents the business trigger and behaviour of an inspection.

Examples conceptually include:

- goods receipt from purchase order;
- goods receipt from production;
- in-process inspection;
- inspection from delivery;
- recurring inspection;
- manual inspection.

The inspection type can influence:

- inspection-lot creation;
- stock posting;
- task-list selection;
- results recording;
- automatic decisions;
- sample calculation.

The exact standard inspection types and available controls depend on the SAP edition and release.

## Inspection lot

The inspection lot is the central transactional quality object.

It represents a defined quantity or process instance to inspect.

It may reference:

- material;
- plant;
- batch;
- supplier;
- purchase order;
- production order;
- delivery;
- inspection plan;
- sample;
- stock quantity.

An inspection lot is not the physical sample.

It is the controlled inspection case.

## Inspection plan

The inspection plan defines how a product or process should be inspected.

It may contain:

- operations;
- work centres;
- master inspection characteristics;
- sampling procedures;
- methods;
- specifications;
- documentation requirements.

A plan may be selected according to factors such as:

- product;
- plant;
- usage;
- validity;
- lot size;
- material assignment.

## Master inspection characteristic

A master inspection characteristic, often abbreviated MIC, defines a reusable quality characteristic.

Examples:

- diameter;
- colour;
- tensile strength;
- weight;
- surface defect;
- packaging condition;
- microbiological result.

Characteristics may be:

### Quantitative

The result is numeric.

Example:

```text
Required diameter: 20.00 mm
Lower limit: 19.95 mm
Upper limit: 20.05 mm
```

### Qualitative

The result is selected from a controlled catalogue.

Example:

```text
Packaging condition:
- Acceptable
- Torn
- Wet
- Incorrect label
```

A reusable characteristic supports standardisation.

Too much reuse can create one generic characteristic whose meaning varies across products.

## Inspection method

The inspection method can describe how the characteristic is measured.

Examples:

- laboratory method;
- visual check;
- torque measurement;
- dimensional method;
- chemical analysis.

The method should connect the result to an approved procedure.

A text description in SAP is not automatically a controlled standard operating procedure.

In regulated environments, the approved method document may remain in a dedicated document or eQMS platform.

## Sampling procedure

The sampling procedure determines how much should be inspected.

Possible approaches include:

- fixed sample;
- percentage sample;
- 100% inspection;
- statistical sampling;
- sampling scheme;
- sample based on inspection severity.

Sampling is a risk decision.

A small sample reduces effort.

It increases the probability that defects remain undetected.

SAP can calculate the sample.

Management must approve the acceptance risk.

## Dynamic modification

Dynamic modification changes inspection intensity according to quality history.

For example:

```text
Repeated accepted lots
→ reduced inspection or skip

Rejected lot
→ normal or tightened inspection
```

This can reduce unnecessary inspection effort.

It can also create false confidence when:

- product design changes;
- supplier process changes;
- production location changes;
- quality history is pooled too broadly;
- skipped lots are not monitored.

## Catalogue and code group

Quality catalogues provide controlled classifications.

They may represent:

- defect type;
- defect location;
- cause;
- task;
- activity;
- usage decision;
- damage type.

A strong catalogue supports analysis.

A weak catalogue produces thousands of records classified as:

- Other;
- General defect;
- Supplier issue;
- Unknown cause.

## Selected set

A selected set restricts which catalogue codes are relevant for a specific decision or process.

This helps prevent users from choosing unrelated codes.

## Inspection point

Inspection points allow results to be recorded for subdivisions of a process.

Examples:

- time interval;
- production quantity;
- work centre;
- equipment;
- serial number;
- physical location.

They are useful for in-process control.

They can also generate very large result volumes.

## Defect record

A defect records a nonconformity found during inspection.

A defect should describe what was observed.

It is not automatically the root cause.

Example:

```text
Defect:
Surface scratch

Potential cause:
Incorrect handling

Root cause after investigation:
Damaged conveyor guide
```

These are different facts.

## Usage decision

The usage decision closes the inspection from a quality perspective and determines what should happen next.

Possible outcomes include:

- accepted;
- rejected;
- accepted under deviation;
- rework;
- return to supplier;
- scrap;
- block;
- transfer to another stock status.

The code should represent the quality decision.

The follow-up action should execute the required business consequence.

## Quality notification

A quality notification manages a quality problem or complaint.

It may contain:

- reference object;
- defect;
- cause;
- tasks;
- activities;
- partner;
- responsible person;
- deadlines;
- attachments;
- status.

Typical scenarios include:

- supplier complaint;
- internal defect;
- customer complaint.

An inspection lot answers:

> Does this inspected quantity meet the requirement?

A quality notification answers:

> What problem occurred, who must respond, and how should it be resolved?

## Quality information record

A quality information record for procurement can govern quality-related supplier-material relationships.

It may control:

- supplier release;
- required inspection;
- certification;
- source-inspection requirements;
- quality agreement;
- block status.

This is one of the strongest mechanisms for connecting supplier quality with purchasing execution.

## Certificate profile

A certificate profile defines which quality information should appear in a quality certificate.

It may include:

- inspection characteristics;
- specifications;
- actual results;
- batch attributes;
- statements;
- texts.

## Quality level

The quality level stores information used for dynamic modification and inspection severity.

It may be specific to combinations such as:

- material;
- plant;
- supplier;
- customer;
- inspection type.

The design of the quality level determines whether quality history is appropriately segmented.

## The end-to-end inspection lifecycle

A well-controlled inspection process looks like this:

```text
Trigger
→ inspection lot created
→ inspection plan selected
→ sample calculated
→ results recorded
→ defects recorded
→ characteristics valuated
→ usage decision
→ stock or process disposition
→ notification where required
→ corrective action
→ effectiveness review
```

Many implementations stop after the usage decision.

That controls the lot.

It does not necessarily improve the process.

## Part I: Quality in procurement

Procurement quality is one of SAP QM’s strongest integration areas.

## Supplier qualification is broader than an inspection lot

A supplier may be approved based on:

- commercial assessment;
- capability audit;
- certification;
- sample approval;
- quality history;
- delivery performance;
- regulatory status.

SAP QM can contribute quality controls.

A broader supplier-management process may be required for:

- onboarding;
- risk;
- ESG;
- financial assessment;
- supplier development.

## Quality in the purchasing process

A typical flow is:

```text
Supplier approved
→ purchase order created
→ supplier ships
→ goods receipt
→ inspection lot
→ results
→ usage decision
→ stock released or rejected
→ supplier complaint if needed
```

## Quality information record in procurement

The quality information record can prevent or control procurement from a supplier.

Possible uses include:

- supplier-material release;
- block purchasing;
- require source inspection;
- require certificate;
- define quality agreement information.

The quality decision therefore affects procurement before goods arrive.

## Source inspection

A source inspection occurs before shipment, often at the supplier site.

Possible objectives:

- approve the lot before dispatch;
- avoid transporting defective material;
- protect a critical production schedule;
- verify first production.

The process may include:

- inspection request;
- supplier or inspector result;
- acceptance;
- shipping release.

A passed source inspection should not automatically prove that transport and receiving caused no later damage.

The company must decide whether another receipt inspection is needed.

## Goods-receipt inspection

At goods receipt, SAP can create an inspection lot and post the quantity into quality-inspection stock.

Conceptually:

```text
Purchase order quantity received
→ quality-inspection stock
→ inspection
→ unrestricted, blocked, return, scrap, or another status
```

This provides strong stock control.

The main operational risk is inspection delay.

A material may physically exist but remain unusable for:

- production;
- customer delivery;
- replenishment.

## Stock posting after usage decision

The usage decision may trigger a stock posting.

Examples:

- quality to unrestricted;
- quality to blocked;
- return to supplier;
- scrap;
- sample consumption;
- other defined stock.

The quality user is therefore making an inventory decision.

Authorization and responsibility should reflect this impact.

## Automatic usage decision

Automatic usage decisions can reduce manual effort when:

- all required results are complete;
- all characteristics are accepted;
- no defects require review;
- the risk is low.

Automation should not be applied merely because the process is repetitive.

It should consider:

- product criticality;
- supplier risk;
- regulatory requirement;
- inspection completeness;
- result source.

## Supplier certificate at receipt

A supplier may provide a certificate of analysis or conformity.

The company may:

- record its receipt;
- validate it;
- extract values;
- reduce physical testing;
- block the lot if missing.

The certificate is supplier evidence.

It does not automatically replace independent verification.

## Supplier complaint

When material is rejected, a supplier quality notification can be created.

The notification may contain:

- defective quantity;
- batch;
- delivery;
- defect code;
- evidence;
- required response;
- corrective-action tasks.

A good process links:

```text
Rejected inspection lot
→ supplier complaint
→ containment
→ replacement or return
→ root cause
→ corrective action
→ effectiveness check
→ supplier score
```

## Chargeback and cost recovery

Supplier defects create costs such as:

- sorting;
- rework;
- line stoppage;
- premium freight;
- scrap;
- administration.

SAP QM can provide the defect and complaint evidence.

Financial recovery may require:

- debit memo;
- service charge;
- settlement;
- supplier claim process.

Do not measure supplier quality only by defect count.

Measure the cost and operational effect.

## Supplier quality collaboration

SAP Business Network Supply Chain Collaboration currently supports quality collaboration, including shared visibility into quality issues and complaints, exchange of quality documentation and coordinated resolution with trading partners. It also connects quality with procurement, inventory and manufacturing collaboration.

This can reduce email and document fragmentation.

Its practical value depends on:

- supplier participation;
- supplier identity;
- process ownership;
- agreed response times;
- integration back to S/4HANA.

A portal does not automatically produce an effective 8D response.

## Procurement-quality limitations

Common failures include:

- inspection stock blocks production;
- supplier certificate arrives late;
- purchasing bypasses the quality block;
- inspection plans differ by plant without reason;
- rejection does not affect supplier selection;
- quality notification is created but never closed;
- supplier corrective action is accepted without effectiveness review.

## Part II: Quality in manufacturing

Manufacturing quality should not be reduced to final inspection.

A defect discovered after production is more expensive than one prevented during the process.

## In-process inspection

An in-process inspection can be triggered during production.

It may be linked to:

- production order;
- process order;
- routing operation;
- phase;
- inspection point;
- batch.

Examples:

- temperature during mixing;
- torque during assembly;
- dimensions after machining;
- visual check after painting;
- weight at packaging.

## Inspection characteristics in routing or recipe

Inspection characteristics can be assigned to production operations.

This links the quality check to the process step where it matters.

The production operator or inspector may record results during execution.

## Process control versus laboratory control

A process characteristic may come from:

- manual measurement;
- machine;
- sensor;
- laboratory;
- MES.

The architecture must define the source of truth.

Do not require an operator to retype a value already produced reliably by equipment.

Do not accept an uncontrolled machine value when calibration and context are unclear.

## Inspection points

Inspection points can create multiple result sets within one lot.

Examples:

```text
Every 30 minutes
Every 100 pieces
Every container
Every serial number
Every shift
```

This provides detailed process visibility.

It also creates:

- more records;
- more user effort;
- more incomplete inspections;
- higher integration volume.

## Statistical process control

Quality results can support analysis of:

- average;
- variation;
- trend;
- upper and lower control limits;
- process capability.

A specification limit answers:

> Is the product acceptable?

A process-control limit answers:

> Is the process behaving consistently?

These should not be confused.

A result may remain inside the specification while the process is drifting toward failure.

## Goods receipt from production

When a production order is completed, the finished material may require inspection before release.

The flow can be:

```text
Production confirmation
→ goods receipt
→ inspection lot
→ quality stock
→ final inspection
→ usage decision
→ unrestricted stock
```

This is useful for:

- final product release;
- batch approval;
- regulated manufacturing;
- customer certificate preparation.

It may create unnecessary waiting when in-process controls already provide sufficient evidence.

## Rework

A rejected result may require:

- additional operation;
- rework order;
- production-order change;
- new inspection;
- restricted release.

Rework should have:

- reason;
- quantity;
- work instruction;
- cost;
- result;
- disposition.

A text note saying “reworked” is not enough.

## Scrap

Quality scrap should identify:

- material;
- quantity;
- operation;
- defect;
- cause;
- order;
- cost.

Without cause coding, scrap becomes a financial posting without learning.

## Production notification and nonconformance

A quality notification can manage an internal nonconformance.

It may contain:

- defect;
- affected order;
- batch;
- immediate containment;
- root cause;
- corrective task;
- responsible department.

## Integration with SAP Digital Manufacturing

SAP Digital Manufacturing is currently SAP’s cloud manufacturing-operations platform. SAP positions it as connecting shop-floor execution with planning and logistics, standardising work instructions and supporting process controls, scrap and rework management, labour tracking and production-quality execution.

A practical architecture may be:

```text
S/4HANA QM
Inspection requirements, lots, disposition, enterprise quality record
               |
               v
SAP Digital Manufacturing
Operator checks, process controls, shop-floor nonconformance
               |
               v
Equipment and measurement systems
Actual execution evidence
```

The boundary must be explicit.

Digital Manufacturing should not create a second independent usage decision for the same lot unless reconciliation is designed.

## MES and machine integration

A plant may use:

- SAP Digital Manufacturing;
- SAP ME or MII in legacy landscapes;
- non-SAP MES;
- laboratory systems;
- direct equipment integration.

SAP states that SAP ME and SAP MII are being retired, with version 15.5 as the final release, and directs customers toward SAP Digital Manufacturing. This is material for long-term quality-integration architecture.

A migration should not simply copy every legacy machine interface.

It should classify each data point as:

- process control;
- quality result;
- traceability event;
- equipment telemetry;
- analytical data.

## Manufacturing-quality limitations

Typical problems include:

- quality checks occur after the operation has completed;
- operators record expected rather than actual values;
- machine data lacks product or order context;
- rejected results do not stop the process;
- rework is hidden as normal production;
- defect causes remain unclassified;
- final inspection compensates for weak process control.

## Part III: Quality and EWM

Warehouse execution creates a difficult boundary between physical stock and the quality decision.

## S/4HANA QM owns the quality disposition

QM determines whether stock is:

- accepted;
- rejected;
- blocked;
- reworked;
- returned.

## EWM owns the physical warehouse execution

EWM determines:

- where the stock is;
- in which handling unit;
- which task moves it;
- where inspection occurs;
- where accepted or rejected stock should be moved.

SAP currently positions EWM as fully integrated with quality, production and track-and-trace processes.

## Typical EWM quality flow

```text
Inbound delivery
→ EWM receiving
→ inspection-relevant stock
→ quality inspection location or work centre
→ result and usage decision
→ follow-up warehouse task
→ final storage, blocked area, return, or scrap
```

## Inspection document and inspection lot

Depending on deployment and scenario, EWM may work with warehouse-specific inspection documents integrated with the S/4HANA QM inspection lot.

The design must preserve one authoritative decision.

A warehouse user should not release a handling unit physically while the QM process remains rejected.

## Handling-unit level inspection

One delivery may contain several HUs.

Quality may need to distinguish:

- accepted HUs;
- rejected HUs;
- sampled HUs;
- mixed batches.

The granularity of inspection and stock disposition should match the physical object.

## Partial acceptance

A lot may be partly acceptable.

This creates complexity in:

- quantity split;
- HU split;
- batch;
- stock posting;
- supplier claim;
- warehouse movement.

Partial acceptance should not be used merely to avoid creating multiple lots.

## Quality work centre in warehouse

Inspection may take place:

- at receiving;
- in a quality area;
- after putaway;
- at a laboratory;
- at an external facility.

The location affects:

- handling;
- space;
- cycle time;
- stock risk.

## Decentralised EWM

In a decentralised EWM landscape, quality integration crosses system boundaries.

Additional concerns include:

- document replication;
- inspection status;
- stock posting sequence;
- queue failure;
- recovery after partial processing.

The warehouse must not rely only on a technical queue status.

It needs business reconciliation between:

- EWM stock;
- inspection status;
- S/4HANA stock;
- usage decision.

## Quality-stock bottleneck

A large quality area may indicate:

- slow laboratory results;
- excessive inspection;
- missing certificates;
- unclear usage-decision ownership;
- disconnected EWM follow-up.

This is not always a warehouse-capacity problem.

## Part IV: Quality in sales, delivery, and customer service

Quality continues after stock is released.

## Outbound inspection

Some products require inspection before delivery.

Examples:

- customer-specific specification;
- export compliance;
- final visual check;
- batch verification;
- packaging quality.

A delivery inspection can provide evidence before goods issue.

It also creates another possible delay.

## Customer-specific specifications

The same product may have different quality requirements by customer.

Examples:

- tighter tolerance;
- certificate required;
- minimum remaining shelf life;
- approved batch;
- special packaging;
- specific test method.

The architecture must determine where the customer specification is governed.

A custom text in a sales order is not reliable quality planning.

## Quality certificate

A quality certificate communicates quality evidence to the customer.

It may contain:

- product;
- batch;
- specification;
- result;
- inspection method;
- statement of conformity;
- manufacturer;
- date.

Certificates may be generated:

- by batch;
- by delivery;
- by customer;
- according to a certificate profile.

## Certificate of analysis versus certificate of conformity

### Certificate of analysis

Contains actual measured results.

### Certificate of conformity

States that the product conforms to an agreed requirement.

The legal meaning should be defined by quality and legal teams.

SAP output configuration does not define the contractual obligation.

## Certificate limitations

Certificate projects often become heavily customised because of:

- customer-specific formats;
- multilingual text;
- logos;
- legal declarations;
- electronic signatures;
- country-specific requirements.

Before building hundreds of forms, standardise the information model.

## Customer complaint

A customer quality notification may reference:

- customer;
- material;
- batch;
- delivery;
- serial number;
- defect;
- returned quantity;
- claim evidence.

A complete customer-complaint process is:

```text
Complaint received
→ affected product identified
→ containment
→ return or field evidence
→ root cause
→ corrective action
→ customer response
→ financial settlement
→ effectiveness review
```

## Returns

The physical return may be handled through:

- sales return;
- inbound delivery;
- EWM;
- inspection lot;
- service process.

The quality notification should not become the only logistics document.

## Warranty and service feedback

Customer quality may also appear through:

- warranty claim;
- repair order;
- field-service report;
- equipment failure.

SAP’s current service portfolio connects customer returns and repair services with contracts, warranty information, logistics, repair work and billing, and describes closing the loop from service feedback to product improvement.

SAP QM should receive or reference relevant defect evidence.

It should not duplicate the entire service process.

## Part V: Batch management, serial numbers, and traceability

Quality decisions often apply to a specific batch or serialised unit.

## Batch management

A batch can carry characteristics such as:

- production date;
- expiry;
- supplier batch;
- potency;
- grade;
- country of origin;
- inspection status.

A usage decision may update or influence batch status and classification.

## Batch traceability

A strong traceability model can answer:

- Which supplier batch entered the plant?
- Which production batches consumed it?
- Which customer deliveries received the output?
- Which inspection and certificate applied?

## Batch status

A batch may be:

- unrestricted;
- restricted;
- blocked;
- otherwise controlled according to the design.

Batch status and stock type should not conflict.

## Serial numbers

Serialised products require unit-level quality evidence.

Examples:

- medical device;
- vehicle component;
- industrial equipment;
- electronics.

The process may need to link:

```text
Serial number
→ inspection result
→ production order
→ delivery
→ customer
→ service history
```

## Traceability limitation

The system can only trace events that were recorded correctly.

A sophisticated genealogy with missing scans creates false precision.

## Part VI: Test equipment and calibration

Measurement is reliable only when the equipment is reliable.

## Test-equipment management

Test equipment may include:

- gauge;
- scale;
- thermometer;
- laboratory instrument;
- torque wrench;
- measurement device.

The system may manage the equipment as a technical object and schedule calibration inspections.

## Calibration process

A typical process is:

```text
Calibration due
→ maintenance or calibration order
→ inspection lot
→ measurement results
→ accepted, adjusted, or rejected equipment
→ next calibration date
```

## Out-of-tolerance equipment

If a measurement device fails calibration, the quality problem is larger than the device.

The company may need to identify:

- products measured by the device;
- time period;
- inspection results;
- released batches;
- customer deliveries.

This retrospective impact analysis is often weak.

## Integration with Asset Management

Equipment maintenance and scheduling may belong to SAP Asset Management.

QM manages the inspection evidence.

One system should own the equipment status.

## Part VII: Quality notifications, CAPA, and 8D

Quality notifications can support problem resolution.

But a notification is not automatically a full CAPA system.

## Notification structure

A notification may contain:

### Defect

What failed?

### Cause

Why did it fail?

### Task

What must be done?

### Activity

What was done?

These distinctions are valuable.

They are often ignored in practice.

## Containment versus corrective action

### Containment

Limits immediate damage.

Examples:

- block stock;
- inspect all remaining units;
- stop shipment;
- inform customer;
- replace material.

### Corrective action

Removes the root cause.

Examples:

- change process parameter;
- modify fixture;
- retrain supplier process;
- update specification;
- redesign component.

### Preventive action

Reduces risk before another failure occurs elsewhere.

## CAPA lifecycle

A robust CAPA process should contain:

```text
Issue
→ risk assessment
→ containment
→ root-cause analysis
→ corrective-action plan
→ approval
→ implementation
→ effectiveness check
→ closure
```

SAP notification tasks can support parts of this.

Highly regulated companies may need a dedicated eQMS for:

- electronic signatures;
- formal CAPA stages;
- training linkage;
- document control;
- validation evidence;
- regulatory audit trail;
- controlled effectiveness review.

## 8D

An 8D process may involve:

1. team formation;
2. problem description;
3. containment;
4. root cause;
5. corrective-action selection;
6. implementation;
7. prevention;
8. closure.

SAP QM can record structured tasks and evidence.

Many companies still use attached spreadsheets or PDFs because the standard notification UI does not match their corporate 8D template.

The danger is that the attachment becomes the actual process while SAP stores only the status.

## Root-cause quality

A cause code should not be selected before investigation merely to close the notification.

Measure the percentage of cases using:

- unknown;
- other;
- operator error.

High use of these codes indicates weak problem solving.

## Effectiveness check

Closing a task proves that an action was performed.

It does not prove that the action worked.

Effectiveness should be checked through:

- recurrence;
- defect rate;
- process result;
- audit;
- supplier performance;
- subsequent lots.

## Part VIII: Audit management, specifications, and product development

Not every quality process belongs inside the transactional QM core.

## Product specifications

Product and raw-material specifications may include:

- composition;
- regulatory attributes;
- packaging;
- allergens;
- performance requirements;
- approved claims.

SAP Integrated Product Development currently supports product, raw-material and packaging specifications, requirements traceability, verification against requirements, change control and integration with S/4HANA.

This can be the upstream source for quality requirements.

The inspection plan should not become the only place where product specifications exist.

## Inspection specification versus product specification

### Product specification

Defines what the product must be.

### Inspection specification

Defines how the product will be tested.

They are related but not identical.

## Audit management

Some SAP private or on-premises landscapes use SAP quality-audit capabilities for:

- audit planning;
- questionnaires;
- findings;
- corrective actions.

Exact scope differs by product edition and release.

Organisations with complex regulated audit programmes may use a specialist eQMS instead.

## FMEA

Failure Mode and Effects Analysis supports preventive risk analysis.

FMEA asks:

- what can fail;
- why;
- how severe;
- how likely;
- how detectable;
- what control is needed.

It should influence:

- control plan;
- inspection frequency;
- process design;
- supplier requirement.

FMEA is often managed in specialised engineering or quality software.

It should not be recreated as unstructured notification text.

## Control plan

A control plan connects:

- process step;
- product characteristic;
- process characteristic;
- method;
- frequency;
- reaction plan.

SAP inspection plans can represent part of this logic.

Automotive and regulated manufacturers may still need stronger control-plan and PPAP integration.

## Part IX: LIMS integration

A laboratory information management system manages scientific laboratory execution.

Typical capabilities include:

- sample receipt;
- laboratory workflow;
- instrument integration;
- reagent and standard management;
- chromatographic data;
- calculations;
- analyst workload;
- scientific review;
- electronic signatures.

SAP QM can create and control the business inspection.

A LIMS can execute the detailed laboratory work.

## Typical architecture

```text
S/4HANA QM
Inspection lot and required characteristics
               |
               v
LIMS
Sample lifecycle, instrument work, calculations
               |
               v
S/4HANA QM
Approved results and disposition support
```

## Integration questions

- Who creates the sample ID?
- Who owns specification limits?
- Which system performs calculations?
- Which result is approved?
- Can a corrected result overwrite history?
- Who makes the usage decision?
- How are cancelled tests handled?

## Instruments

Direct instrument integration should preserve:

- instrument ID;
- calibration status;
- operator;
- method;
- timestamp;
- raw result;
- transformed result;
- approval.

## LIMS limitation

Adding a LIMS can create two specification masters.

The organisation must decide whether limits originate in:

- PLM;
- S/4HANA QM;
- LIMS;
- regulated document.

## Part X: Quality costs and financial integration

Quality creates direct and indirect cost.

## Cost of quality

A useful model separates:

### Prevention cost

- supplier development;
- training;
- process design;
- preventive maintenance;
- FMEA.

### Appraisal cost

- inspection;
- testing;
- laboratory;
- audit.

### Internal failure cost

- scrap;
- rework;
- sorting;
- production interruption.

### External failure cost

- return;
- warranty;
- complaint;
- recall;
- penalty;
- lost customer.

## SAP transactions behind quality cost

Quality events may create:

- scrap posting;
- rework order;
- supplier debit;
- customer credit;
- blocked inventory;
- inspection labour;
- premium freight.

The quality notification should link to these effects where possible.

## Cost of blocked stock

Stock waiting for quality creates:

- working capital;
- production risk;
- warehouse occupancy;
- expiry risk.

Measure:

```text
Quantity in quality stock
× inventory value
× waiting duration
```

This is not the full economic cost, but it reveals trapped capital.

## Cost recovery

Supplier-caused quality cost may be recovered through:

- return;
- debit memo;
- chargeback;
- settlement.

The recovery process should reference the quality case.

## Part XI: Quality analytics

The most common quality KPI is rejection rate.

It is not sufficient.

## Incoming quality

- supplier defect rate;
- accepted, rejected and conditional lots;
- inspection lead time;
- certificate completeness;
- skipped-lot failure;
- supplier complaint recurrence;
- cost recovery.

## Production quality

- first-pass yield;
- scrap;
- rework;
- defects per unit;
- process-capability measures;
- defect by operation;
- recurrence after corrective action.

## Customer quality

- complaints;
- returns;
- warranty rate;
- response time;
- escape rate;
- customer claims;
- cost of external failure.

## Process metrics

- inspection lots overdue;
- results incomplete;
- usage-decision lead time;
- quality-stock age;
- notification cycle time;
- task overdue;
- CAPA effectiveness.

## Inspection efficiency

- characteristics per lot;
- samples per lot;
- skip rate;
- manual result-entry effort;
- automated-result percentage;
- inspection cost per accepted unit.

## Leading versus lagging indicators

### Lagging

- defect;
- complaint;
- scrap;
- warranty.

### Leading

- process drift;
- supplier process change;
- calibration overdue;
- inspection-plan expiry;
- CAPA overdue;
- certificate missing.

A mature system should use both.

## Part XII: AI in quality management

AI can support quality processes.

It should not make uncontrolled release decisions.

## Useful AI scenarios

- classify free-text defect descriptions;
- suggest duplicate complaints;
- summarise supplier 8D reports;
- extract certificate values;
- identify recurring defect patterns;
- assist root-cause investigation;
- detect anomalous measurement trends;
- prepare quality-notification drafts;
- link service feedback to product issues.

## Weak AI scenarios

- invent specification limits;
- release a regulated batch based only on model judgement;
- override failed inspection;
- approve supplier corrective action without evidence;
- replace deterministic tolerance checks.

## Computer vision

Computer vision can inspect:

- surface defect;
- packaging;
- label;
- assembly;
- presence or absence of components.

The model output should include:

- model version;
- confidence;
- image reference;
- threshold;
- fallback;
- human-review policy.

## AI limitation

A model can classify an image incorrectly.

The business must decide:

- false acceptance risk;
- false rejection risk;
- validation frequency;
- drift monitoring;
- regulated-use restrictions.

## Part XIII: Where SAP QM is strong

SAP QM is particularly strong when:

- quality directly controls SAP inventory;
- inspections are triggered by logistics transactions;
- supplier and customer documents must remain linked;
- batches and orders require traceability;
- results affect production or delivery;
- one ERP already owns procurement, manufacturing and sales.

Its major advantage is integration.

A rejected lot can affect:

- stock;
- purchasing;
- production;
- supplier complaint;
- delivery;
- finance.

A standalone QMS may manage the investigation elegantly but lack transactional control.

## Where SAP QM is weaker

## Full document control

SAP can attach and manage documents.

A regulated eQMS may provide stronger:

- SOP lifecycle;
- training assignment;
- controlled copies;
- electronic signatures;
- periodic review.

## Advanced laboratory execution

A LIMS is usually stronger for:

- instrument integration;
- reagent;
- worksheet;
- scientific calculation;
- chain of custody.

## Sophisticated CAPA

Quality notifications can support CAPA.

Specialist eQMS products may provide more purpose-built workflows, risk controls and regulatory evidence.

## Advanced SPC and engineering quality

Specialised tools may be stronger for:

- control charts;
- capability studies;
- FMEA;
- control plans;
- PPAP;
- MSA.

## Supplier quality portal

Business Network can support external collaboration.

Supplier adoption and process depth should be assessed.

## Public-cloud scope

SAP QM scope is not identical across:

- SAP S/4HANA on-premises;
- SAP Cloud ERP Private;
- SAP Cloud ERP Public.

A legacy ECC QM process should not be assumed to exist unchanged in Public Edition.

## Part XIV: Main limitations and traps

## Limitation 1: Master-data intensity

QM requires disciplined maintenance of:

- inspection plans;
- characteristics;
- methods;
- catalogues;
- sampling;
- dynamic-modification rules;
- certificates.

Poor master data creates unreliable quality control.

## Limitation 2: Inspection-plan explosion

Separate plans may be created for:

- every plant;
- supplier;
- customer;
- product variant.

Reusability falls.

Maintenance becomes impossible.

## Limitation 3: Result entry does not prove measurement

A user can enter a value manually.

The system does not know whether the measurement was actually performed.

## Limitation 4: Usage decisions become bottlenecks

One quality manager may need to close thousands of routine lots.

Automate low-risk cases carefully.

## Limitation 5: Quality stock can stop supply

Inspection design may protect quality while creating production shortages.

The solution is not to bypass inspection.

It is to reduce inspection lead time and improve supplier capability.

## Limitation 6: Defect codes remain weak

Poor catalogues destroy analytics.

## Limitation 7: Notifications become administrative archives

Cases are closed without root cause or effectiveness review.

## Limitation 8: Attachments contain the real process

The 8D, certificate or investigation lives in Excel or PDF.

SAP stores only a link and status.

## Limitation 9: Supplier quality does not affect sourcing

The supplier continues receiving orders despite repeated defects.

## Limitation 10: Quality and engineering are disconnected

Recurring defects do not trigger design or specification change.

## Limitation 11: QM and EWM statuses diverge

Physically released stock remains logically blocked, or the reverse.

## Limitation 12: LIMS duplicates specifications

Limits differ between laboratory and ERP.

## Limitation 13: Excessive inspection

The company inspects every lot forever instead of improving the process.

## Limitation 14: Excessive skipping

Good historical results are used despite a changed supplier process.

## Limitation 15: Custom certificates create upgrade debt

Every customer format becomes custom logic.

## Limitation 16: Quality cost is invisible

Management sees rejection percentages but not:

- rework;
- line stop;
- premium freight;
- lost capacity.

## Limitation 17: Quality ownership is unclear

Procurement, production and quality each expect another team to close the issue.

## Limitation 18: Regulatory expectations exceed standard configuration

Electronic records, signatures and validation may require additional controls and products.

## Part XV: Modern target architecture

A balanced quality architecture may look like:

```text
SAP Integrated Product Development / PLM
Requirements, specifications, change
                    |
                    v
SAP S/4HANA QM
Inspection planning, lots, results, disposition,
notifications, certificates, transactional traceability
                    |
       +------------+-------------+
       |                          |
       v                          v
SAP Digital Manufacturing       LIMS
Shop-floor controls             Laboratory execution
       |                          |
       +------------+-------------+
                    |
                    v
SAP EWM
Physical quality stock and movement
                    |
                    v
SAP Business Network
Supplier quality collaboration
                    |
                    v
eQMS where required
CAPA, documents, training, regulatory workflow
                    |
                    v
Enterprise data and analytics
Quality cost, trends, product and supplier performance
```

Not every company needs every layer.

## Architecture for discrete manufacturing

Recommended core:

- S/4HANA QM;
- production integration;
- supplier complaints;
- EWM where applicable;
- Digital Manufacturing for shop-floor checks.

## Architecture for process industry

Additional emphasis:

- batches;
- certificates of analysis;
- laboratory integration;
- sample management;
- shelf life;
- recipe and specification integration.

## Architecture for pharmaceuticals or medical devices

Likely additional requirements:

- validated systems;
- electronic signatures;
- controlled documents;
- LIMS;
- eQMS;
- formal batch release;
- regulatory audit trail.

SAP QM can remain the transactional logistics-quality core.

It should not be presented as the complete regulatory platform without qualification.

## Architecture for automotive

Additional emphasis:

- supplier quality;
- serial and batch genealogy;
- defects per component;
- 8D;
- PPAP and control plans;
- customer complaints;
- warranty feedback;
- Business Network collaboration.

## Part XVI: Migration from ECC QM to S/4HANA

A QM migration should not be treated as a technical table conversion.

## Inspect the active scope

Inventory:

- inspection types;
- plans;
- MICs;
- methods;
- sampling procedures;
- catalogues;
- selected sets;
- dynamic-modification rules;
- quality info records;
- certificates;
- notifications;
- custom code;
- interfaces.

## Separate active from historical data

Not every historical plan needs to remain operational.

Classify:

- active and required;
- duplicate;
- obsolete;
- historical archive.

## Open inspection lots

Open lots require careful cutover.

Questions include:

- finish in legacy system?
- migrate?
- recreate?
- how will stock remain consistent?
- which system issues the usage decision?

## Quality stock

Cutover must preserve:

- quantity;
- batch;
- stock type;
- inspection reference;
- warehouse location.

## Notifications

Open complaints and CAPAs may remain active for months.

They require:

- status mapping;
- task ownership;
- attachments;
- deadlines;
- external references.

## Custom enhancements

Common custom areas include:

- automatic lot creation;
- customer certificates;
- supplier scoring;
- result interfaces;
- quality notification workflow;
- custom forms.

Each should be classified:

- standard replacement;
- API or BAdI extension;
- side-by-side application;
- retire.

## LIMS and equipment interfaces

Revalidate:

- object IDs;
- result schema;
- characteristic mapping;
- units;
- correction handling;
- error recovery.

## EWM integration

Test:

- inbound inspection;
- HU split;
- partial decision;
- accepted and rejected quantities;
- stock transfer;
- queue recovery.

## Part XVII: Implementation approach

## Phase 1: Define quality risk

Segment products and processes by:

- safety;
- regulatory risk;
- customer impact;
- process capability;
- supplier capability;
- cost of failure.

Do not apply one inspection policy to every material.

## Phase 2: Map quality triggers

Identify:

- procurement;
- production;
- delivery;
- recurring inspection;
- manual inspection;
- customer return.

## Phase 3: Define specification authority

For each characteristic, record:

- business owner;
- source;
- validity;
- method;
- unit;
- tolerance;
- approval.

## Phase 4: Design inspection plans

Use reusable characteristics and methods without destroying product-specific meaning.

## Phase 5: Design sampling and modification

Define:

- normal;
- reduced;
- tightened;
- skipped;
- requalification.

## Phase 6: Design stock consequences

For every usage decision, define:

- stock posting;
- warehouse movement;
- supplier action;
- production action;
- financial action.

## Phase 7: Design notification workflows

Separate:

- supplier complaint;
- internal defect;
- customer complaint;
- CAPA.

## Phase 8: Connect external systems

Integrate only where justified:

- Digital Manufacturing;
- EWM;
- LIMS;
- Business Network;
- eQMS;
- PLM.

## Phase 9: Build exception handling

Test:

- missing plan;
- missing certificate;
- failed result interface;
- partial result;
- rejected lot;
- changed specification;
- EWM queue failure;
- late usage decision.

## Phase 10: Measure outcome

Do not measure only inspection completion.

Measure:

- escaped defects;
- recurrence;
- release time;
- quality cost;
- supplier improvement.

## Questions managers and architects should ask

1. What business risk is each inspection controlling?
2. Which system owns the product specification?
3. Which system owns the inspection method?
4. Which event creates the inspection lot?
5. When does stock become usable?
6. Who is authorised to make the usage decision?
7. Which decisions can be automated?
8. What happens after rejection?
9. Does rejection affect supplier sourcing?
10. How is partial acceptance handled physically?
11. Which quality status is authoritative in EWM?
12. Which results come from machines or LIMS?
13. Can results be corrected without losing history?
14. Are measurement devices calibrated?
15. Which customer certificates are legally required?
16. Can the original certificate be reproduced?
17. Does every complaint have containment and root cause?
18. Is effectiveness checked after corrective action?
19. Which quality process remains in spreadsheets?
20. Is SAP QM being asked to replace a LIMS or eQMS?
21. How much inventory waits for inspection?
22. Which inspections can be reduced safely?
23. How are skipped lots requalified after a change?
24. Can a supplier access and respond to complaints digitally?
25. Is quality cost connected to defects and notifications?
26. Do warranty and service data reach product quality?
27. Which QM functions differ by SAP deployment model?
28. Can one batch be traced from supplier to customer?
29. Can management identify the causes of poor quality?
30. Is the process improving, or only documenting defects?

## The management conclusion

SAP QM is not merely an inspection module.

It is the transactional quality-control layer connecting:

- procurement;
- inventory;
- manufacturing;
- warehouse execution;
- sales;
- customer service;
- suppliers;
- finance.

Its strongest capability is not result recording.

It is the ability to turn a quality decision into a controlled business consequence.

A rejected supplier lot can:

- remain unavailable;
- move to blocked stock;
- trigger a return;
- create a supplier complaint;
- create a financial recovery process;
- affect supplier performance.

A rejected production result can:

- stop release;
- create rework;
- record scrap;
- block the batch;
- trigger corrective action.

Modern SAP landscapes can extend this transactional core through:

- SAP Digital Manufacturing for shop-floor execution and process controls;
- SAP EWM for physical handling of quality-relevant stock;
- SAP Business Network for supplier quality collaboration;
- SAP Integrated Product Development for requirements, specifications and change;
- Service Management for field, return and warranty feedback.

The system still cannot answer the most important quality question by itself:

> Why does this failure continue to happen?

That requires:

- process knowledge;
- engineering;
- supplier development;
- accountability;
- evidence;
- follow-through.

The decisive measure is not:

> How many inspection lots did we close?

It is:

> Did the quality system prevent defective product from moving forward, identify the cause of failure, remove recurrence, and reduce the total cost and risk of poor quality?

When SAP QM is designed around that outcome, it becomes an effective enterprise control system.

When it is designed only around inspection transactions, the organisation becomes very efficient at documenting defects it continues to create.

---

### SAP QM architecture checklist

- [ ] Quality planning and quality control are distinguished.
- [ ] Product specifications have an authoritative source.
- [ ] Inspection methods are governed.
- [ ] Inspection types have documented business triggers.
- [ ] Inspection plans are reusable but product-specific where necessary.
- [ ] Sampling reflects approved risk.
- [ ] Dynamic modification includes requalification rules.
- [ ] Quality levels are segmented correctly.
- [ ] Defect, cause, task and activity codes are distinct.
- [ ] Usage-decision codes have defined follow-up actions.
- [ ] Stock posting and warehouse movement remain synchronized.
- [ ] Automatic usage decisions are limited to suitable cases.
- [ ] Supplier quality records influence procurement.
- [ ] Source inspection and receipt inspection responsibilities are clear.
- [ ] Supplier certificates have controlled review rules.
- [ ] Supplier complaints include containment and effectiveness checks.
- [ ] Production characteristics are linked to the correct operations.
- [ ] Machine and MES results retain context and provenance.
- [ ] Rework and scrap have causes and costs.
- [ ] EWM and QM have one authoritative disposition.
- [ ] Partial acceptance is tested at HU and quantity level.
- [ ] Customer-specific specifications are governed.
- [ ] Certificates preserve the original approved result.
- [ ] Customer complaints link to delivery, batch and serial data.
- [ ] Warranty and service feedback reaches product quality.
- [ ] Calibration failures trigger impact analysis.
- [ ] Quality notifications support real problem solving.
- [ ] CAPA does not end when a task is marked complete.
- [ ] LIMS and SAP do not maintain conflicting specifications.
- [ ] Regulated document and signature requirements are addressed.
- [ ] Quality costs are linked to quality events.
- [ ] Inspection stock age is monitored.
- [ ] Quality analytics include recurrence and escaped defects.
- [ ] AI cannot override deterministic specifications or release policy.
- [ ] ECC-to-S/4HANA migration removes obsolete quality master data.
- [ ] Open inspection lots and notifications have a cutover strategy.
- [ ] Deployment-specific QM scope is verified.
- [ ] The organisation can trace a quality decision to its evidence and consequence.

### Sources and further reading

SAP Business Network Supply Chain Collaboration currently supports supplier quality collaboration, shared visibility into quality issues and complaints, exchange of quality documentation and coordinated resolution across buyers and trading partners.

SAP Digital Manufacturing currently provides cloud manufacturing-operations capabilities for production execution, process controls, scrap and rework, standardised work instructions, labour tracking and coordination with quality, inventory and logistics. SAP also states that SAP ME and SAP MII are being retired, with version 15.5 as the final release.

SAP Extended Warehouse Management currently provides integrated quality, production and track-and-trace processes alongside detailed warehouse-stock and physical-execution control.

SAP Integrated Product Development currently supports product, raw-material and packaging specifications, requirements traceability, validation against requirements, product change control and integration with SAP S/4HANA.

SAP’s current service-management portfolio connects customer returns and repairs with warranty information, logistics, service execution, billing and feedback to product improvement.

*Reviewed: July 2026. SAP QM scope, Fiori applications, inspection scenarios, quality-audit functionality and integration options differ by SAP S/4HANA release, private or public cloud edition, and licensed products. Detailed design should be validated against the exact Product Availability Matrix, scope items and current SAP Help documentation.*

## Continue exploring

- [Why SAP CAR Becomes the Most Important Retail System Nobody Can Clearly Explain](/blog/why-sap-car-becomes-the-most-important-retail-system-nobody-can-clearly/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [SAP for Automotive Explained: The Complete Architecture from Engineering and JIT Supply to Vehicle Sales, Warranty, and Aftermarket](/blog/sap-for-automotive-explained-the-complete-architecture-from-engineering/)
- Next in the migration: [SAP Business Data Cloud Explained: Architecture, Data Products, BW Modernization, Databricks, AI, and the Limits Behind the Marketing](/blog/sap-business-data-cloud-explained-architecture-data-products-bw/)
