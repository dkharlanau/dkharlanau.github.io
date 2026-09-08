---
layout: default
title: "SAP MDG Lead Assessment Drills — Enterprise Context Lab"
description: "Architecture and diagnostic MDG cases for Material, Business Partner, DRF, matching, survivorship and automotive multi-plant rollout."
permalink: /labs/enterprise-context/mdg/assessment/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "synthetic case review against reviewed MDG Material, Business Partner, governance and replication modules"
search_intent: "SAP MDG Lead interview assessment questions Material Business Partner DRF duplicate supplier architecture"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - integration-recovery
  - lead-decision
tags: [sap, mdg, assessment, lead, architecture, logistics]
# ai-discovery-managed:start
primary_topic: "sap-mdg"
ai_sidecar: "/ai/pages/labs--enterprise-context--mdg--assessment.json"
semantic_links:
  - type: "parent_context"
    title: "SAP Master Data Governance — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/"
  - type: "same_domain"
    title: "Data, Master Data and Governance — Enterprise Context Lab"
    url: "/labs/enterprise-context/data-governance/"
  - type: "same_domain"
    title: "SAP MDG Material Domain — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/domains/material/"
  - type: "same_domain"
    title: "SAP MDG Change Request Type Matrix — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/governance-engine/change-request-matrix/"
  - type: "same_domain"
    title: "SAP Business Partner — CVI, Configuration, Guardrails and Extensions"
    url: "/labs/enterprise-context/business-partner/"
  - type: "same_domain"
    title: "SAP MDG Consolidation & Golden Record — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/consolidation/"
# ai-discovery-managed:end
---
# SAP MDG Lead Assessment Drills

These are **synthetic assessment cases**, not customer cases. The goal is not to remember transaction codes. The goal is to show how you frame scope, ownership, architecture, controls and proof using the reviewed MDG domain, governance and replication models on this site.

The machine-readable case set is `/labs/assessment/data/mdg-cases.jsonl`.

## Case 1 — Automotive multi-plant rollout

A group wants one MDG hub for Material and Supplier data across 12 plants and 7 consuming systems.

Your answer should separate:

```text
Global identity
→ organizational grains
→ owners
→ CR patterns
→ rules
→ activation
→ DRF
→ migration/delta
→ process proof
→ operating model
```

Do not answer “centralize everything”. Plant planning, local warehouse execution and shared legal identity do not have the same business owner.

A strong answer also explains what stays central, what can be proposed locally, what needs local approval and what can be derived automatically.

## Case 2 — Active Material, broken plant

The Material is active and usable in Sales, but MRP is wrong in one plant and EWM later rejects the product context.

Start by freezing one identity and plant. Then trace:

```text
Material identity
→ plant-level governed data
→ active state
→ DRF selection
→ target acceptance
→ process consumer
```

The trap is to treat “Material exists” as proof that the plant extension is correct.

## Case 3 — Duplicate suppliers

Two active supplier BPs have a high matching score, different external IDs and transaction history.

The answer needs two separate decisions:

```text
Are they the same identity?
          ↓
Which values should survive?
```

Then choose a duplicate strategy only after checking key mapping and downstream transaction behavior. A similarity score is evidence for review, not automatic authority to merge two productive identities.

## Case 4 — Target outage and replay

A target ERP was offline for two hours. Some updates failed, some timed out, later updates may have succeeded.

A Lead answer should not begin with “replay all”. It should establish current source truth, target state, ordering, duplicate behavior and whether the historical payload is still valid.

Useful decision:

```text
Safe replay
vs
Rebuild from current active truth
vs
Manual resolution
vs
Stop and reconcile population
```

## How I would answer on the board

For design questions:

```text
Outcome → Identity → Grain → Ownership → Rule → CR → Activation → Distribution → Business Proof
```

For incident questions:

```text
Expected state → Evidence → First wrong boundary → Scope → Recovery → Reconciliation → Business proof
```

For consolidation questions:

```text
Identity evidence → Match decision → Survivorship → Duplicate strategy → Key mapping → Consumer proof
```

## Study links

- [Material domain](/labs/enterprise-context/mdg/domains/material/)
- [Business Partner domain](/labs/enterprise-context/mdg/domains/business-partner/)
- [Governance Engine](/labs/enterprise-context/mdg/governance-engine/)
- [Replication & Distribution](/labs/enterprise-context/mdg/replication/)
- [DRF Operations & Replay](/labs/enterprise-context/mdg/replication/operations/)
- [Matching & Survivorship](/labs/enterprise-context/mdg/consolidation/survivorship/)
