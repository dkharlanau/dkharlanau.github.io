---
layout: default
title: "SAP MDG Domain Engineering — Enterprise Context Lab"
description: "Deep SAP MDG domain engineering for Material, Business Partner, Customer and Supplier, with governance, replication, consolidation and migration links."
permalink: /labs/enterprise-context/mdg/domains/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "reviewed MDG Material, Business Partner, governance and replication modules + navigation-layer review"
search_intent: "SAP MDG domain engineering Material Business Partner customer supplier data model governance replication"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg-domain-engineering"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - logistics-master-data
tags: [sap, mdg, material, business-partner, customer, supplier, data-model]
---

# SAP MDG Domain Engineering

MDG becomes useful when the data model matches the real business grain. A screen is not a grain. A table is not automatically a business object. The design starts with identity, organizational meaning, ownership and lifecycle.

```text
Business identity
→ Organizational grain
→ Entity / relationship
→ Ownership
→ Validation / derivation
→ Change request
→ Activation
→ Distribution
→ Business proof
```

## Reviewed domain maps

- [Material Domain](/labs/enterprise-context/mdg/domains/material/) — global product identity, plant, sales, purchasing, storage, valuation, warehouse and quality contexts.
- [Business Partner / Customer / Supplier](/labs/enterprise-context/mdg/domains/business-partner/) — shared party identity, roles and application-specific organizational slices.

These pages use current SAP S/4HANA 2025 FPS01 MDG sources for the product model and keep ownership/grain guidance as explicit architecture reasoning.

## Governance mechanics

- [Change Request, Workflow & Rules](/labs/enterprise-context/mdg/governance-engine/) — reviewed against current change-request, workflow, validation and derivation documentation.
- [Replication & Distribution](/labs/enterprise-context/mdg/replication/) — reviewed against current DRF and key-mapping documentation.
- [DRF Operations & Replay](/labs/enterprise-context/mdg/replication/operations/) — operational recovery with SAP BP replication KBA evidence and explicit safety boundaries.
- [Consolidation & Golden Record](/labs/enterprise-context/mdg/consolidation/) — working material; keep its own verification status until separately reviewed.
- [Migration & Load Strategy](/labs/enterprise-context/mdg/migration/) — working material; keep its own verification status until separately reviewed.
- [Logistics End-to-End Cases](/labs/enterprise-context/mdg/logistics/cases/) — working cases; keep their own verification status until separately reviewed.

## Lead view

For every requirement, I want five answers before implementation starts:

1. What is the business identity and grain?
2. Who owns the value and who can approve a change?
3. Which deterministic rule validates or derives it?
4. Where does active truth live and how is it distributed?
5. Which business document proves the design works?

This keeps MDG out of the common trap where governance is designed around UI fields and the real process impact is discovered during integration testing.
