---
layout: default
title: "SAP MDG Lead Assessment Drills — Enterprise Context Lab"
description: "Architecture and diagnostic MDG cases for Material, Business Partner, DRF, matching, survivorship and automotive multi-plant rollout."
permalink: /labs/enterprise-context/mdg/assessment/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, assessment, lead, architecture, logistics]
---

# SAP MDG Lead Assessment Drills

These cases are designed for Lead-level answers. The goal is not to remember transaction codes. The goal is to show how you frame scope, ownership, architecture, controls and proof.

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
MATERIAL root
→ plant entities
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

Then choose a duplicate strategy only after checking key mapping and downstream transaction behavior.

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

- [Material entity map](/labs/enterprise-context/mdg/domains/material/entity-map/)
- [Business Partner entity map](/labs/enterprise-context/mdg/domains/business-partner/entity-map/)
- [Change Request Type Matrix](/labs/enterprise-context/mdg/governance-engine/change-request-matrix/)
- [BRFplus Rule Catalog](/labs/enterprise-context/mdg/governance-engine/brfplus-rules/)
- [DRF Operations & Replay](/labs/enterprise-context/mdg/replication/operations/)
- [Matching & Survivorship](/labs/enterprise-context/mdg/consolidation/survivorship/)
