---
layout: default
title: "AI Can Translate Code. Can It Preserve the Whole Business Process?"
description: "Practical AI Engineer lesson about legacy modernization, graph lineage, parity testing, applied to synthetic SAP decisions and reproducible evaluation."
permalink: /labs/ai-ready/video-lessons/graph-first-legacy-modernization/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [integration-ownership, integration-recovery, ai-data-governance]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# AI Can Translate Code. Can It Preserve the Whole Business Process?

A legacy billing formula is translated to modern Java. Every unit test passes. After deployment, some invoices differ by one cent and an overnight reconciliation job silently fails. The error may not be the formula. It may be the **record layout, rounding mode, batch order, or one of the downstream consumers**.

In [How We Mapped a 35-Million-Line Mainframe in 4 Days](https://aietalks.com/talks/how-we-mapped-a-35-million-line-mainframe-in-4-days), Stephen Chin (Neo4j) and Neeraj Deshmukh (Blitzy) describe mapping a legacy estate as a graph before replacing code. The reported project speed and scale are **presenter claims**; the reusable method is dependency discovery plus continuous parity testing.

## Translation is not modernization

A function can return the same value for one input while the new system breaks the business process.

| Layer | What must remain equivalent | Typical missed dependency |
| --- | --- | --- |
| Calculation | Formula, decimals, rounding, currency | Changed precision or rounding behavior |
| Data | Layout, types, field meaning, identity | Numeric string treated as a number |
| Flow | Batch sequence, triggers, idempotency | Different processing order |
| Side effects | Database updates, events, status flags | Missing update to a second table |
| Interfaces | Output structure and error contracts | Downstream system rejects a changed payload |
| Operations | Scheduling, restart, recovery | A retry doubles a posting |

The speakers advocate extracting semantic relations from source code and metadata and using a knowledge graph to give agents **small, relevant slices** of the complete estate. The graph is not proof that all relationships were discovered. It is a tool for making missing dependencies inspectable.

## Apply the method to an SAP migration

**Synthetic scenario:** A legacy ERP feeds a new S/4HANA order-to-cash process. A migration team wants to move only customer and sales order data.

A dependency walk may discover other business objects that change the result: sales-area data, partner functions, route inputs, open deliveries, pricing records, billing references, credit dependencies and FI handoffs. The relevant objects are **landscape and scenario dependent**; do not assume each exists in every deployment.

Instead of asking an agent to "map everything", start from one concrete question:

> What must be true before a migrated sales order can be processed and billed correctly?

Model relationships with four required properties: source reference, relation type, owning system, and observation/effective date. Every inferred edge stays marked **unverified** until supported by configuration, data or a test.

## Parity testing: compare the business effects

For each synthetic case, run both implementations or an approved reference model and compare:

1. Input normalization, customer/material identity and effective dates.
2. Output values and field-level differences.
3. Generated document relationships or events.
4. Persisted status changes.
5. Error behavior and recovery path.
6. Numeric precision, currency and rounding.

"Compiled successfully" is weaker than "same business result." Even value equality in one test is weaker than equivalence across process variants.

## A useful graph contract

~~~yaml
change: legacy-billing-rule-modernization
nodes:
  - {id: input, kind: source_record}
  - {id: calculate, kind: business_rule}
  - {id: post, kind: accounting_effect}
edges:
  - {from: input, to: calculate, type: consumes, status: observed}
  - {from: calculate, to: post, type: produces, status: unverified}
checks:
  - output_value_parity
  - rounding_parity
  - side_effect_parity
~~~

This is a teaching sketch, not SAP configuration or a Neo4j import format.

## 60-minute practical exercise

Take a **synthetic** legacy rule with three upstream inputs and two downstream outputs. Draw the smallest graph that proves its impact. Then deliberately change precision or the execution order and add a regression test that catches the difference.

If you need a visual, [Visual Workbench](https://github.com/dkharlanau/visual-workbench) can be the projection layer. For relationship semantics and transformation dependencies, inspect the existing [Data Relationship Map](https://github.com/dkharlanau/data-relationship-map) and [Transformation Graph](https://github.com/dkharlanau/transformation-graph) first.

**Architect question:** What would convince you that an AI-generated modernization plan covers a business process rather than just code symbols?

Related: [SAP Enterprise](/labs/enterprise-context/) · [Graph Engineering](/labs/ai-ready/video-lessons/graph-engineering-execution-context/) · [Source transcript](https://ainotes.us/summary/how-we-mapped-a-35-million-line-mainframe-in-4-days-stephen-chin-neo4j-neeraj).

**Source boundary:** Mapping scale, duration and vendor workflow are reported by the presenters. The SAP migration example is synthetic and not a certification of process parity.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
