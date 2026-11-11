---
layout: default
title: "Three Graphs Behind a Dependable Agent"
description: "Practical AI Engineer video lesson on graph engineering, processes, state, provenance; includes decisions, a synthetic SAP case, evaluation and implementation steps."
permalink: /labs/ai-ready/video-lessons/graph-engineering-execution-context/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [ai-agents-mcp, integration-ownership, ai-retrieval]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# Three Graphs Behind a Dependable Agent

A graph of SAP systems looks impressive. But does it help an agent **choose and verify the next action**? If the answer is no, it may be only a diagram.

Zach Blumenfeld's [Make Your AI Agents Predictable With Graph Engineering](https://aietalks.com/talks/make-your-ai-agents-predictable-with-graph-engineering) separates three uses of graphs: execution, context and procedure. The components are familiar from state machines, workflow engines and knowledge graphs. The useful advance is connecting them to AI tasks without losing deterministic behavior.

## Do not mix these three graphs

| Graph | What an edge means | Typical owner | Example |
| --- | --- | --- | --- |
| **Execution graph** | Which task may run next | Workflow/harness | Read order → check evidence → return diagnosis |
| **Context graph** | How facts and decisions are related | Evidence/knowledge layer | BP → sales order → delivery → message trace |
| **Procedural graph** | How a repeatable skill is performed | Process/rules owner | Validate fields → compare snapshots → request review |

A graph node should not be created just because a label sounds technical. A useful model defines **node identity, ownership, edge semantics, observation time, and evidence**.

## One SAP diagnostic seen through three lenses

**Synthetic case:** A route is missing from an order. We want to distinguish source data, copied order fields, target master data, and route-determination configuration.

**Execution:** Validate the order ID. Read the actual order values. Choose the next read based on what is missing. Stop if you lack authorization.

**Context:** Sold-To and Ship-To relationships, plant, relevant transportation attributes, replicated BP record, order and source message, plus timestamps. A relationship does **not** itself prove a causal error.

**Procedure:** Compare source/target snapshots, evaluate the required route inputs, apply configuration-specific checks, and produce an evidence-backed owner recommendation.

~~~text
Observed order
   | has ship-to
   v
Target BP --replicated-from--> Source BP
   | transport data                 | source version
   v                                v
Route-determination inputs <--- Message evidence
   |
   v
Candidate route / no match
~~~

The diagram is a conceptual map. Actual determination behavior depends on SAP configuration and deployment. Never let graph edges silently replace SAP's system-owned logic.

## A small portable graph contract

~~~yaml
nodes:
  - id: order:synthetic-51
    kind: sales_order
    owner: target_system
  - id: bp:synthetic-77
    kind: business_partner
    owner: master_data
edges:
  - from: order:synthetic-51
    to: bp:synthetic-77
    relation: ship_to
    source_ref: snapshot-51
    as_of: "2026-11-11"
~~~

This is **not** a Neo4j schema or SAP interface payload. It illustrates the missing contract many quick graph demos ignore: explicit provenance and type. A deterministic validator should reject broken references and duplicate IDs.

## Graph as code: when to compile a procedure

The talk describes turning procedural graph logic into execution steps. This is particularly useful when the sequence is stable and compliance-sensitive. If the procedure says **every write needs approval**, the generated workflow should enforce it in code, not only repeat it to the model.

A graph database is one way to store relationships. A small YAML/JSON model and a graph renderer may be simpler for a bounded pilot. Do not adopt a graph database because the diagram has arrows.

## 60-minute practical task

Use a **synthetic** Order-to-Cash exception and draw six nodes and eight edges. Mark each edge as observed, configured, inferred or proposed. Then answer one question: *"Where did the first incorrect value enter the process?"*

Try solving it with plain retrieval versus traversing explicit relations. Evaluate: number of source reads, wrong links, missing provenance and time to a defensible conclusion. A model that produces a beautiful graph with unproven edges has failed.

If using the DK Harlanau ecosystem, compare [Visual Workbench](https://github.com/dkharlanau/visual-workbench) for semantic diagrams, [Data Relationship Map](https://github.com/dkharlanau/data-relationship-map) for lineage, and [Transformation Graph](https://github.com/dkharlanau/transformation-graph) for dependencies before building another renderer.

**Architect challenge:** When should a graph be the source of truth, and when should it remain a projection of SAP and integration evidence?

Related: [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Source transcript](https://ainotes.us/summary/make-your-ai-agents-predictable-with-graph-engineering-zachary-blumenfeld-neo4j).

**Source boundary:** Graph distinctions and demonstration are drawn from the speaker. The SAP structures and contracts are independent synthetic examples.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
