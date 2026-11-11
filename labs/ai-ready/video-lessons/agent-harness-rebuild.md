---
layout: default
title: "We Built Ten Agents. Then We Went Back to One."
description: "Lessons from Arize's production AI agent: why plans, memory, completion gates and regression tests matter more than agent count."
permalink: /labs/ai-ready/video-lessons/agent-harness-rebuild/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, agents, harness, memory, evaluation, architecture, video-learning]
career_impact: mapped
career_skills: [ai-agents-mcp, ai-evaluation, ai-readiness]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# We Built Ten Agents. Then We Went Back to One.

*What two years of rebuilding an AI agent can teach an SAP architect.*

**Source:** [Fuad Ali (Arize AI), “We Kept Rebuilding Our AI Agent. Here's What Survived” — AI Engineer, 27 October 2026](https://www.youtube.com/watch?v=YIhvrvHtonk) (20 min). [Searchable transcript](https://ainotes.us/summary/we-kept-rebuilding-our-ai-agent-here-s-what-survived-fuad-ali-arize-ai).

Here is the twist: while many teams are exploring networks of small agents, Arize describes moving **from ten specialists back to one agent with tools and skills loaded on demand**. The question is not which approach sounds more advanced. It is which one solves the job with less confusion and better evidence.

## The useful story behind the demo

Arize's in-product assistant, Alex, evolved from a router and skills into a multi-step system with planning, state, memory and evaluations. Fuad Ali describes experiments that were removed as well as features that stayed.

| Question | What the team tried | What survived | Architectural lesson |
| --- | --- | --- | --- |
| Who keeps the plan? | Model-managed to-do tool | The **harness** controls progress | A model should not spend turns simply ticking boxes. |
| When is a task finished? | No tool call means finished | An explicit finish check | Completion is an application state, not a writing style. |
| Where do huge tool responses go? | Large results in context | Store output externally, read slices | More context is not always better context. |
| What is useful long-term memory? | Vector / graph / separate stores | Small, auditable memory file in this product | Start with the least complex storage that performs well. |
| One agent or many? | Around ten specialists | One agent with skills on demand | Coordination is a cost; measure whether it pays back. |
| How do we test changes? | Read failures case by case | Traces converted into regression cases | Production failures should improve the next release. |

The speaker's **8,000-character per-user memory file** is a reported design choice for Alex, not a recommended limit for every application. The same is true of its model selection: the practical insight is to choose the fastest sufficiently accurate configuration on task tests, not to copy a vendor's default model.

## Why this matters in SAP

Imagine a customer asks why a sales order did not reach the next process step. You could build eight specialists: SD, MM, EWM, TM, MDG, integration, security and FI. But each specialist needs its own context, permissions, errors, handoff rules and tests.

There may be a simpler version:

~~~text
One case owner (bounded agent)
  -> inspect sales-order evidence       [read tool]
  -> inspect customer/master-data state [read tool]
  -> inspect integration trace          [read tool]
  -> apply a domain-specific skill      [instructions]
  -> compare hypotheses
  -> return diagnosis or missing evidence
~~~

One agent is a strong default when the job has **one business owner, one case boundary and mostly sequential evidence reads**. Separate specialists become more attractive when they have independent authority, different data residency, explicit domain ownership, or genuinely parallel work. See [Standard Agents](/labs/ai-ready/standard-agents/) for the opposite architectural argument.

## Build a minimal harness, not a magic prompt

The application should own a typed case record. For example:

~~~json
{
  "case_id": "SYN-042",
  "plan": ["read_order", "check_master_data", "check_interface"],
  "completed": ["read_order"],
  "status": "in_progress",
  "evidence_refs": ["snapshot/order/042"],
  "next_action": "check_master_data",
  "write_allowed": false
}
~~~

This is an illustrative training contract, not a SAP API or an Arize product schema. The model chooses which **allowed read** is useful next; code checks completion and stores source references. Large API responses stay outside the conversation and are loaded by exact case scope.

The harness should refuse to call an unavailable tool, enforce a step limit and return an honest stop state. If the request demands an unapproved write, the answer is `approval_required`, not an improvised workaround.

## 40-minute exercise: delete an agent

Take a hypothetical SAP support design with three specialists: Sales, Master Data and Integration. Build a comparison on the same three synthetic incidents:

1. **Workflow:** fixed sequence of three reads and rule-based output.
2. **Single bounded agent:** may choose the next read from evidence.
3. **Three specialists:** separate contexts and a typed handoff.

Measure complete/correct cases, unsupported claims, tool calls, time, and intervention rate. Record one case where coordination actually added value. If it did not, reject the multi-agent design.

**Decision prompt:** The integration specialist and Sales specialist always return the same information from the same API. Would you keep both? What would justify a separate identity or deployment?

## What I would keep — and challenge

Keep the harness-owned completion gate, bounded context, and production-to-eval feedback loop. Challenge the assumption that one tiny memory file generalizes to every governed enterprise process. Some SAP evidence needs immutable source records, retention controls, segregation of duties and transaction-specific ownership; a user preference file cannot replace that.

**Practical takeaway:** give the model uncertainty to solve. Keep exact state, arithmetic, permissions and completion rules in code. Add a specialist only after its value survives a controlled comparison.

**Related:** [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [Memory and State](/labs/ai-ready/engineering/memory-state/).

*Evidence boundary: Arize's product history and selected implementation decisions are speaker-reported. All SAP cases and metrics proposed here are independent synthetic training designs. This page has not completed human editorial review.*
