---
layout: default
title: "SAP MDG Replication & Distribution — Enterprise Context Lab"
description: "DRF, replication models, outbound implementations, filters, targets, key mapping, monitoring and reconciliation."
permalink: /labs/enterprise-context/mdg/replication/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 primary sources + DRF/key-mapping review + page-level factual review"
search_intent: "SAP MDG DRF replication model outbound implementation business system key mapping active data troubleshooting"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - integration-patterns
  - integration-recovery
tags: [sap, mdg, drf, replication, integration, key-mapping]
source_links:
  - title: "SAP MDG Data Replication — S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/ef0a1e74ff9044df9e43d28021900335.html"
  - title: "SAP MDG Key Mapping — S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/8f3d0f8274e642b5aed793f4f4f8e5a4.html"
  - title: "Configuring Data Replication"
    url: "https://help.sap.com/docs/SAP_ERP/d6bbe43b03894e4f817c8b939d532744/22d76454004f2357e10000000a44176d.html"
# ai-discovery-managed:start
primary_topic: "sap-mdg"
ai_sidecar: "/ai/pages/labs--enterprise-context--mdg--replication.json"
entity_mentions:
  - "sap-integration"
semantic_links:
  - type: "deep_dive"
    title: "SAP MDG DRF Operations & Replay — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/replication/operations/"
  - type: "same_domain"
    title: "SAP MDG Interface Contracts — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/interfaces/"
  - type: "parent_context"
    title: "SAP Master Data Governance — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/"
  - type: "same_domain"
    title: "SAP Business Partner — CVI, Configuration, Guardrails and Extensions"
    url: "/labs/enterprise-context/business-partner/"
  - type: "same_domain"
    title: "Data, Master Data and Governance — Enterprise Context Lab"
    url: "/labs/enterprise-context/data-governance/"
  - type: "integrates_with"
    title: "SAP DRF — Data Replication Framework"
    url: "/labs/enterprise-context/integrations/drf/"
# ai-discovery-managed:end
---
# Replication and Distribution

Activation and replication are two different proofs.

```text
Approved change
→ Active master data
→ Replication model
→ Outbound implementation
→ Filter
→ Business system
→ Message / service
→ Key mapping
→ Target persistence
→ Business consumer
```

SAP documents DRF around replication models, outbound implementations and assigned business systems. In standard MDG replication, the distribution source is active master data: unapproved changes remain in the staging process until activation. Key mapping becomes important when connected systems identify the same business object with different keys.

Current references: [SAP Help: Data Replication](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/ef0a1e74ff9044df9e43d28021900335.html), [Key Mapping](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/8f3d0f8274e642b5aed793f4f4f8e5a4.html), and [Configuring Data Replication](https://help.sap.com/docs/SAP_ERP/d6bbe43b03894e4f817c8b939d532744/22d76454004f2357e10000000a44176d.html).

## Design contract

For every consumer define:

1. Business object and population.
2. Replication model and outbound implementation.
3. Filters and organizational scope.
4. Target business system.
5. Payload/service/message contract.
6. Identity and key mapping.
7. Target validation and persistence.
8. Monitoring, replay and reconciliation.

The concrete business object controls which filters, outbound parameters, interfaces and output modes are available. Do not copy DRF values from another domain without checking the delivered implementation for the target release.

## Troubleshooting order

Do not begin with middleware logs. First ask whether the expected value is active and selected for distribution.

```text
Active source?
→ selected by DRF?
→ payload correct?
→ transport delivered?
→ identity resolved?
→ target accepted?
→ target committed?
→ business process used it?
```

This isolates the first failing boundary. A successful HTTP call or outbound message is only transport evidence.

## Initialization and delta

An initial distribution creates a baseline. Ongoing changes create the delta stream when the delivered outbound implementation supports the required change/output mechanism. The cut-off between baseline and ongoing processing needs an explicit reconciliation point. Otherwise two technically successful jobs can still leave a population gap.

A useful handover proves:

```text
source baseline population
→ selected count
→ sent count
→ accepted/persisted count
→ key-mapping coverage where relevant
→ agreed cut-off
→ first ongoing change cycle
→ source/target no-gap check
```

## Key mapping is identity control

Key mapping is not only a technical lookup table. It answers a business-identity question: which target object represents this source object? SAP S/4HANA 2025 FPS01 documents key mapping for connected systems where object identifiers differ.

Before repairing a mapping, check:

- source business system and object ID;
- target business system and object ID;
- whether a target object already exists;
- whether a confirmation or inbound process was expected to create/update the mapping;
- whether changing the mapping could point future changes to the wrong local object.

## Lead-level risk list

- filter excludes a required organization;
- target requires a field not governed centrally;
- key mapping points to the wrong local object;
- retry creates duplicate side effects;
- local repair hides a central mapping defect;
- baseline and ongoing changes use different population assumptions;
- monitoring checks transport but not target acceptance or business use.

## Operations deep dive

For failures and recovery, continue with [DRF Operations & Replay](/labs/enterprise-context/mdg/replication/operations/). It adds error classes, replay-versus-rebuild decisions, initial-load/delta controls, operational metrics and a runbook that ends with business-consumer proof.

Use the [MDG Lead Assessment Drills](/labs/enterprise-context/mdg/assessment/) to practice the target-outage recovery case.

## Lead answer

> “In MDG I separate governance activation from distribution. DRF distributes active master data through a replication model, an object-specific outbound implementation and a target business system. I control the population with the supported filters, handle identity through key mapping when systems use different IDs, and troubleshoot from active source and DRF selection through transport, target persistence and business consumption. A green outbound message is not the final proof.”
