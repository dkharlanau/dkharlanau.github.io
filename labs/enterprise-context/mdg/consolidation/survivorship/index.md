---
layout: default
title: "SAP MDG Matching & Survivorship — Enterprise Context Lab"
description: "How to design matching thresholds, review bands, best-record rules, manual overrides and duplicate strategies in SAP MDG consolidation."
permalink: /labs/enterprise-context/mdg/consolidation/survivorship/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 matching, Match Review, best-record and active-record consolidation primary sources + policy review"
search_intent: "SAP MDG matching survivorship match review best record source priority recency completeness duplicate strategy"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg-matching-survivorship"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - logistics-master-data
tags: [sap, mdg, consolidation, matching, survivorship, golden-record]
source_links:
  - title: "Configure Matching — SAP S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/e0c1ce6bfa1e4f2aa23393217e94b4c6.html"
  - title: "Match Review"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5cb861909ee642388d828a9d1759901c.html"
  - title: "Best Record Calculation"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/866c1271ed9f49a382ce6ed93ddcb05c.html"
  - title: "Consolidation of Active Records"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/399dfaaa10204570a94f126c64f30718.html"
# ai-discovery-managed:start
primary_topic: "sap-mdg-matching-survivorship"
ai_sidecar: "/ai/pages/labs--enterprise-context--mdg--consolidation--survivorship.json"
entity_mentions:
  - "sap-mdg"
semantic_links:
  - type: "parent_context"
    title: "SAP MDG Consolidation & Golden Record — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/consolidation/"
  - type: "parent_context"
    title: "SAP Master Data Governance — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/"
  - type: "related_topic"
    title: "Data, Master Data and Governance — Enterprise Context Lab"
    url: "/labs/enterprise-context/data-governance/"
  - type: "related_topic"
    title: "Where Should Master-Data Validation Live? — SAP Decision Card"
    url: "/labs/enterprise-context/decisions/master-data-validation/"
  - type: "integrates_with"
    title: "SAP DRF — Data Replication Framework"
    url: "/labs/enterprise-context/integrations/drf/"
  - type: "related_topic"
    title: "SAP MDG Lead Assessment Drills — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/assessment/"
# ai-discovery-managed:end
---
# SAP MDG Matching & Survivorship

Two decisions are often mixed together:

```text
Matching     = Are these records probably the same real-world object?
Survivorship = Which source/table/field value should become the best record?
```

They need different rules and different evidence.

## Matching policy

SAP MDG matching can create match groups and use configured matching rules and scores. Match Review exists for groups that remain open and require user decision. That gives us the product mechanism. The architecture still needs a business policy for false positives, false negatives and authority. [Configure Matching](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/e0c1ce6bfa1e4f2aa23393217e94b4c6.html) and [Match Review](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5cb861909ee642388d828a9d1759901c.html).

I use three **policy bands** as a design frame, not as SAP-delivered fixed thresholds:

| Band | Meaning | Action |
|---|---|---|
| Automatic match | Strong evidence and an accepted false-positive risk | Continue automatically only if the configured process and policy permit it |
| Review band | Ambiguous score or high business impact | Human review |
| Non-match | Evidence below the accepted match policy | Keep identities separate |

A single global threshold is often weak design. Identity risk can differ by country, object type, available identifiers, data quality and downstream transaction history. The numeric thresholds themselves are configuration decisions.

## Evidence hierarchy

Strong identity evidence can include governed legal/registration identifiers, stable tax identifiers, or trusted source mappings where the domain and legal context support them. Name and address are useful but can be noisy. Free text and local aliases are usually supporting evidence rather than sufficient proof by themselves.

For an ambiguous BP, I want the reviewer to see, where available and permitted:

- normalized values;
- relevant identifiers;
- source system;
- previous match decisions;
- current key mapping;
- downstream usage and transaction history.

A score without business context is incomplete evidence.

## Survivorship rules

SAP best-record calculation supports rule-based selection. I treat source priority, recency, completeness and domain rules as building blocks, not universal truth. [Best Record Calculation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/866c1271ed9f49a382ce6ed93ddcb05c.html).

### Source priority

Use it when a source is authoritative for that table or field group. Do not make one source globally “golden” if authority differs by domain.

### Recency

Use it only when the timestamp represents business freshness. A technical reload timestamp can make stale data look new.

### Completeness

Non-empty is not the same as correct. Completeness can enrich a record when trust is comparable, but it should not override a higher-quality controlled source only because another row has more fields filled.

### Domain rule

For sensitive fields, a domain-specific precedence rule may be better than generic source/recency/completeness logic.

## Manual override

SAP's Best Record Calculation Review allows authorized users to inspect and, for supported data, manually adapt the calculated result. The operating policy should keep enough evidence to explain the override.

A useful audit record includes:

```text
Calculated winner
Selected override
Reason
Reviewer
Timestamp
Downstream impact
```

The exact audit implementation depends on the configured process and governance requirements.

## Duplicate strategy

For consolidation of active records, SAP supports strategies including Remove Duplicates, Improve Best Record and Improve All Records. The technical choice changes identity continuity and therefore must be discussed with downstream consumers. [Consolidation of Active Records](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/399dfaaa10204570a94f126c64f30718.html).

Before a destructive or redirecting duplicate strategy, I would prove:

- surviving identity;
- replacement/key mapping behavior;
- target-system behavior;
- transaction-history implications;
- archive/retention requirements;
- replay and reconciliation plan.

## Metrics

Useful quality signals can include automatic-match rate, human-review rate, reviewer override rate, sampled false-positive/false-negative rates, unresolved match age, manual survivorship overrides and key-mapping reconciliation errors. These are operating-model metrics, not SAP-mandated KPI names.

## Machine-readable model

The structured policy is in `_data/labs/enterprise_context/topics/mdg_survivorship_matching_policy.yml`.

Use it with [Consolidation & Golden Record](/labs/enterprise-context/mdg/consolidation/), the [Business Partner domain](/labs/enterprise-context/mdg/domains/business-partner/) and [DRF operations](/labs/enterprise-context/mdg/replication/operations/).
