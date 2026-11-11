---
layout: default
title: "Context Is Not Memory: Five Lifecycles an AI Agent Must Respect"
description: "An applied lesson on context lifecycle engineering, evidence freshness and SAP process ownership, grounded in the AI Native DevCon November 2026 agenda."
permalink: /labs/ai-ready/video-lessons/context-lifecycle-engineering/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, context-engineering, memory, rag, sap, architecture]
career_impact: mapped
career_skills: [ai-retrieval, ai-data-governance, ai-agents-mcp]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# Context Is Not Memory: Five Lifecycles an AI Agent Must Respect

*Context engineering is more than filling a prompt window.*

**Source boundary:** This is an original technical lesson inspired by the **confirmed agenda topics** “Context != Context: One Window, Different Lifecycles” (Birgitta Boeckeler), “Models Alone Aren't Enough: Engineering Context as a Graph for Human + Agent Teams” (Alan Braun), and “Memory Without Deterministic Coordinates Is Just Hearsay” (Veljko Kovac) at [AI Native DevCon, 2–4 November 2026](https://tessl.io/devcon). **It is not a transcript or verified summary of these presentations.** The specific design and SAP examples below are independent.

## Why this problem is harder than it looks

Imagine an SAP diagnostic assistant receiving three statements:

- “For the current project, all delivery errors come from master data.”
- “Last week the interface was unavailable.”
- “This order has no route.”

All three sentences fit in the same context window. But they have **different owners, lifetimes, trust levels and consequences**. If you mix them into one memory blob, the agent can treat an old assumption as current evidence.

The correct question is not “How many tokens can we store?” It is “Which facts may influence this decision, and until when?”

## Five kinds of context

| Kind | Owner | Typical lifetime | Example | Failure when confused |
| --- | --- | --- | --- | --- |
| **Policy** | Security / architecture | Versioned until replaced | Production writes require approval | A chat message overrides authorization |
| **Task** | Requester / workflow | One case or run | Diagnose order SYN-100 | Another case's facts leak into this one |
| **Source evidence** | SAP / middleware / monitoring | Timestamped snapshot | Route field read at 10:15 | Old state presented as current |
| **Domain knowledge** | Document owner | Until review or supersession | Route determination dependencies | A legacy rule is treated as universal SAP standard |
| **Preference / working memory** | User or team | Longer-lived, revisable | Preferred answer format | Preference becomes an operational instruction |

The **same text** can appear in several layers, but its authority changes. A retrieved PDF can contain instructions; that does not make it an instruction source for the agent. A previous diagnosis can be useful background; that does not make it proof of the current incident.

## A minimal evidence contract

~~~json
{
  "claim": "The target shipping zone is missing",
  "kind": "source_evidence",
  "source_system": "synthetic-s4",
  "object_ref": "BP-SYN-100",
  "observed_at": "2026-11-11T10:15:00Z",
  "owner": "master-data",
  "trust": "authenticated_tool_result",
  "scope": "case-SYN-100",
  "expires_at": "2026-11-11T10:30:00Z"
}
~~~

This is a proposed internal schema, **not** an SAP API. A useful system also keeps the raw source reference, authorization boundary and a reason for each expiry policy. Some facts do not expire after 15 minutes; others are already stale after seconds. Choose freshness based on the business action.

## Context graph without a graph database

The smallest useful graph can be a few linked records:

~~~text
Case SYN-100
  -> business object: sales order
  -> observed input: shipping condition
  -> observed input: transportation zone
  -> relevant rule: route determination
  -> competing cause: configuration mismatch
  -> competing cause: stale downstream master data
  -> verification: target-system determination result
~~~

A JSON object with stable IDs can implement this before any graph engine. A graph database earns its cost when traversals, lineage, many-to-many dependencies and change impact become difficult to manage with simpler storage.

## SAP exercise: find the stale claim

Create three synthetic snapshots for the same Ship-To: source at 09:00, target at 09:05, source after a correction at 10:00. An agent reads the old target snapshot and confidently says “replication succeeded.” Ask it to return a claim with source, observation time and freshness status.

**Pass criteria:** it must say the target's latest business state is **not proven** and request a fresh target read. It must not resend or modify the BP.

Then change one condition: the target snapshot is fresh, but route determination still fails. Which evidence now distinguishes master-data failure from configuration failure?

## A practical architecture decision

Use a layered context builder, not one unlimited conversation:

1. Read policies from a trusted, versioned source.
2. Load only the task's authorized identifiers and objectives.
3. Fetch fresh evidence through narrow tools.
4. Retrieve domain documentation with source/version metadata.
5. Return a structured answer that distinguishes observation, hypothesis and recommendation.
6. Store only reviewed, durable learnings; do not automatically memorize raw incident claims.

**Architect challenge:** Would you store a successful incident diagnosis as a global memory rule? Under what conditions could that become dangerous?

**Related:** [Memory and State](/labs/ai-ready/engineering/memory-state/) · [Data and RAG](/labs/ai-ready/data-rag/) · [Agent Architecture](/labs/ai-ready/agent-architecture/).

*Editorial status: draft/noindex, pending source-level and human review.*
