---
layout: default
title: "SAP MDG Matching & Survivorship — Enterprise Context Lab"
description: "How to design matching thresholds, review bands, best-record rules, manual overrides and duplicate strategies in SAP MDG consolidation."
permalink: /labs/enterprise-context/mdg/consolidation/survivorship/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, consolidation, matching, survivorship, golden-record]
---

# SAP MDG Matching & Survivorship

Two decisions are often mixed together:

```text
Matching     = Are these records probably the same real-world object?
Survivorship = Which source/table/field value should become the best record?
```

They need different rules and different evidence.

## Matching policy

SAP MDG matching can create match groups and use configured thresholds. Match Review exists for groups that need user decision. That gives us the product mechanism. The architecture still needs a business policy for false positives, false negatives and authority.

I use three bands:

| Band | Meaning | Action |
|---|---|---|
| Automatic match | Strong evidence, acceptable false-positive risk | Continue if policy permits |
| Review band | Ambiguous score or high business impact | Human review |
| Non-match | Evidence below threshold | Keep identities separate |

A single global threshold is usually lazy design. Identity risk can differ by country, object type, data quality and downstream transaction history.

## Evidence hierarchy

Strong identity evidence can include trusted legal/registration identifiers, stable tax IDs or governed source mappings. Name and address are useful but can be noisy. Free text and local aliases are supporting evidence at best.

For an ambiguous BP, I want the reviewer to see:

- normalized values;
- identifiers;
- source system;
- previous match decisions;
- current key mapping;
- downstream usage and transaction history.

A score without context is just a confident number.

## Survivorship rules

SAP best-record calculation supports rule-based selection. Common rule ideas are source-system priority, recency and completeness. I treat them as building blocks, not universal truth.

### Source priority

Use it when a source is authoritative for that table or field group. Do not make one source globally “golden” if authority differs by domain.

### Recency

Use it only when the timestamp represents business freshness. A technical reload timestamp can make stale data look new.

### Completeness

Non-empty is not the same as correct. Completeness can enrich a record when trust is comparable, but it should not override a high-quality controlled source just because another row has more fields filled.

### Domain rule

For sensitive fields, a domain-specific precedence rule may be better than generic source/recency/completeness logic.

## Manual override

A manual best-record change should keep:

```text
Calculated winner
Selected override
Reason
Reviewer
Timestamp
Downstream impact
```

Otherwise the golden record becomes a golden mystery.

## Duplicate strategy

For consolidation of active records, SAP supports strategies including Remove Duplicates, Improve Best Record and Improve All Records. The technical choice changes identity continuity and therefore must be discussed with downstream consumers.

Before Remove Duplicates, I would prove:

- surviving identity;
- replacement/key mapping;
- target-system behavior;
- transaction-history implications;
- archive/retention path;
- replay and reconciliation plan.

## Metrics

Useful quality signals include automatic-match rate, human-review rate, reviewer override rate, sampled false-positive/false-negative rates, unresolved match age, manual survivorship overrides and key-mapping reconciliation errors.

## Machine-readable model

The structured policy is in `_data/labs/enterprise_context/topics/mdg_survivorship_matching_policy.yml`.

Use it with [Consolidation & Golden Record](/labs/enterprise-context/mdg/consolidation/), the [BP entity map](/labs/enterprise-context/mdg/domains/business-partner/entity-map/) and [DRF operations](/labs/enterprise-context/mdg/replication/operations/).
