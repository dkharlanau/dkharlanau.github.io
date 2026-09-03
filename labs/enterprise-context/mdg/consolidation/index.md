---
layout: default
title: "SAP MDG Consolidation & Golden Record — Enterprise Context Lab"
description: "Matching, match review, best-record calculation, validation, duplicate strategy, activation and provenance."
permalink: /labs/enterprise-context/mdg/consolidation/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 consolidation, matching, best-record and active-record primary sources + policy review"
search_intent: "SAP MDG consolidation matching best record calculation golden record duplicate strategy active records"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg-consolidation"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - logistics-master-data
tags: [sap, mdg, consolidation, matching, golden-record, data-quality]
source_links:
  - title: "Consolidating Master Data — SAP S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5c1f0c571db4124ce10000000a4450e5.html"
  - title: "Best Record Calculation"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/866c1271ed9f49a382ce6ed93ddcb05c.html"
  - title: "Match Review"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5cb861909ee642388d828a9d1759901c.html"
  - title: "Consolidation of Active Records"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/399dfaaa10204570a94f126c64f30718.html"
---

# Consolidation and Golden Record

A golden record is not “the row with most fields”. It is a governed result of identity evidence and precedence rules.

```text
Source records
→ Standardize
→ Match
→ Review ambiguous groups
→ Best Record Calculation
→ Validate
→ Duplicate strategy
→ Activate
→ Key mapping
→ Distribute
```

SAP S/4HANA 2025 FPS01 documents MDG consolidation as a configurable sequence that can include matching, best-record calculation, validation and activation. Match Review supports user decisions for open match groups, and consolidation of active records provides explicit duplicate strategies. [Consolidating Master Data](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5c1f0c571db4124ce10000000a4450e5.html), [Best Record Calculation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/866c1271ed9f49a382ce6ed93ddcb05c.html), and [Match Review](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5cb861909ee642388d828a9d1759901c.html).

## Matching design

For each domain define strong identity evidence, supporting evidence and noisy fields. Then define thresholds and review behavior for the chosen matching configuration. False positives can be more damaging than extra human review when two productive identities carry different legal or transactional history.

The exact matching algorithm, score configuration and auto-approval behavior are configuration-dependent. Do not copy a numeric threshold from another domain or landscape as a universal SAP value.

## Best-record policy

SAP best-record calculation is rule-based. Current product documentation also supports review of the calculated result before later process steps where the process template and authorizations permit it.

A useful business policy can decide at field or table level:

- trusted source wins;
- most recent trusted value wins;
- complete value wins when sources have similar trust;
- a domain-specific business rule wins.

Source priority, recency and completeness are common rule ideas, but their business meaning must be defined. A technical timestamp is not automatically “freshest business truth”, and a non-empty value is not automatically the correct value.

Preserve provenance: source record, selected value, rule, rejected alternatives and manual override where the operating model requires it.

## Active duplicate strategy

Do not treat duplicate handling as cosmetic cleanup. It changes identity across interfaces and business processes. SAP's active-record consolidation supports strategies such as Remove Duplicates, Improve Best Record and Improve All Records. The selected strategy changes what happens to duplicates and key mapping, so downstream consumers must be part of the decision. [Consolidation of Active Records](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/399dfaaa10204570a94f126c64f30718.html).

## Assessment answer

I would explain the difference between **matching confidence** and **business authority to merge**. The algorithm proposes evidence. Governance decides what level of evidence is enough for an identity action and how the downstream process is protected.

## Policy deep dive

Continue with [Matching & Survivorship](/labs/enterprise-context/mdg/consolidation/survivorship/) for threshold bands, review evidence, source/recency/completeness rules, manual overrides, duplicate strategies and quality metrics.

The [Business Partner domain](/labs/enterprise-context/mdg/domains/business-partner/) shows where identity and organizational behavior diverge. The [MDG Lead Assessment Drills](/labs/enterprise-context/mdg/assessment/) include a duplicate-supplier consolidation challenge.
