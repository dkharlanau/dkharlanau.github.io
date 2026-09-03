---
layout: default
title: "SAP MDG Material Domain — Enterprise Context Lab"
description: "Deep Material data-model engineering across global, plant, sales, purchasing, storage, valuation, warehouse and quality grains."
permalink: /labs/enterprise-context/mdg/domains/material/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 MDG Material primary sources + organizational-grain review"
search_intent: "SAP MDG Material data model plant sales purchasing valuation storage warehouse governance design"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg-material"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - logistics-master-data
tags: [sap, mdg, material, product, logistics, data-model]
source_links:
  - title: "SAP MDG Material Data Model — S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/2a500de376504b4386a04d1085a52f22.html"
---

# SAP MDG Material Domain

The useful mental model is not “Material has many views”. It is **one business identity with several organizational grains**.

```text
Material
├─ Global / Basic
├─ Plant
│  ├─ MRP / planning
│  ├─ purchasing
│  ├─ quality
│  ├─ work scheduling
│  └─ storage / execution context
├─ Sales Organization + Distribution Channel
├─ Storage Location
├─ Valuation Area
├─ Warehouse / Storage Type where relevant
├─ Units of Measure
└─ Classification
```

SAP documents the MDG-M model as based on the ERP material master and includes basic material data plus dependent entity types for plant, sales, purchasing, valuation, units, classification and other material attributes. The exact supported entities and features depend on the S/4HANA/MDG release and selected scope. [SAP Help: MDG Material data model](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/2a500de376504b4386a04d1085a52f22.html).

## How I would build it

**1. Identity first.** Decide number strategy, duplicate policy and what a Material represents in the enterprise. Do not let plant extension create a second identity.

**2. Map fields to grain.** A field that changes by plant belongs to a plant-qualified slice. A field that changes by sales area belongs to the sales-area slice. Putting local meaning on the global root creates future conflicts.

**3. Assign owners.** Product governance can own identity and global attributes. Planning owns planning meaning. Sales owns sales meaning. Procurement, quality, warehouse and finance own their business semantics. Central governance coordinates them; it does not automatically become the expert for every field.

**4. Design CR patterns around business change.** “Create material”, “extend to plant”, “extend to sales area”, “change regulated attribute” and “mass correction” can require different scope and authority.

**5. Put deterministic quality early.** Validate allowed combinations before an approver spends time reviewing a technically impossible state. Use derivation only when inputs and precedence are clear.

**6. Design distribution with the consumer.** Activation is not the end. Define target, filter, identity mapping, mandatory target fields, monitoring and reconciliation.

**7. Prove business usability.** For a sales material, create the sales order and delivery. For planning, run the relevant planning scenario. For EWM, prove warehouse execution where EWM is in scope. “The record exists” is weak evidence.

## Model smell checklist

- Plant-specific requirement added to a global field.
- One custom entity becomes a dumping ground for unrelated organizational data.
- Pricing, source list or routing is pulled into Material only because it references Material.
- Replication mapping is designed after UI completion.
- Migration counts Material IDs but ignores missing plant or sales-area slices.
- A local target fix becomes the normal way to compensate for incomplete central data.

## Assessment answer shape

For “How would you design Material in MDG?” I would answer:

```text
Identity → Grain → Ownership → Rules → CR → Activation → DRF → Reconciliation → Logistics proof
```

Then I would give one plant-extension example and show exactly where MRP, purchasing, sales or warehouse behavior consumes the governed value.

## Go deeper

- [Technical entity map](/labs/enterprise-context/mdg/domains/material/entity-map/) — connect `MATERIAL`, plant, sales, valuation, storage and warehouse entities to business grains.
- [Change Request Type Matrix](/labs/enterprise-context/mdg/governance-engine/change-request-matrix/) — decide when create, extension, sensitive change and mass change need different governance contracts.
- [DRF Operations & Replay](/labs/enterprise-context/mdg/replication/operations/) — operate target distribution and recovery safely.
- [MDG Lead Assessment Drills](/labs/enterprise-context/mdg/assessment/) — practice the multi-plant design and broken-plant diagnostic cases.
