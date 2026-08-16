---
layout: default
title: "SAP MDG Consolidation & Golden Record — Enterprise Context Lab"
description: "Matching, match review, best-record calculation, validation, duplicate strategy, activation and provenance."
permalink: /labs/enterprise-context/mdg/consolidation/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, consolidation, matching, golden-record, data-quality]
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

SAP MDG consolidation supports matching and best-record calculation, and current documentation describes rules such as source priority, recency and completeness depending on configuration. [SAP Help: Best Record Calculation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/866c1271ed9f49a382ce6ed93ddcb05c.html).

## Matching design

For each domain define strong identity evidence, supporting evidence and noisy fields. Then define thresholds for automatic match, possible match and non-match. False positives are usually more dangerous than an extra review because they can merge two real-world objects.

## Best-record policy

A useful policy can decide at field or table level:

- trusted source wins;
- most recent trusted value wins;
- complete value wins when sources have similar trust;
- a domain-specific business rule wins.

Preserve provenance: source record, selected value, rule, rejected alternatives and manual override.

## Active duplicate strategy

Do not treat duplicate handling as cosmetic cleanup. It changes identity across interfaces and business processes. If a duplicate is retired or redirected, key mapping and consumers must follow the surviving identity.

## Assessment answer

I would explain the difference between **matching confidence** and **business authority to merge**. The algorithm proposes evidence. Governance decides what level of evidence is enough for an irreversible identity action.

## Policy deep dive

Continue with [Matching & Survivorship](/labs/enterprise-context/mdg/consolidation/survivorship/) for threshold bands, review evidence, source/recency/completeness rules, manual overrides, duplicate strategies and quality metrics.

The [Business Partner entity map](/labs/enterprise-context/mdg/domains/business-partner/entity-map/) shows where identity and organizational behavior diverge. The [MDG Lead Assessment Drills](/labs/enterprise-context/mdg/assessment/) include a duplicate-supplier consolidation challenge.
