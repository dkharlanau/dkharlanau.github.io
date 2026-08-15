---
layout: default
title: "AI Ready — Agent Architecture"
description: "A practical guide to workflows, routers, tool loops, orchestrator-worker patterns, budgets, termination, approvals, and agent failure modes."
permalink: /labs/ai-ready/agent-architecture/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, agents, workflow, orchestration, tools, approval]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Agent Architecture</li></ol>
</nav>

# Agent Architecture

An agent is useful when the next step cannot be fully defined before the request starts. That is the reason to add autonomy. “Agents are modern” is not a reason.

## Start with the least autonomous shape

Use this order:

1. deterministic function;
2. deterministic workflow;
3. workflow with one model decision;
4. router to known paths;
5. bounded tool loop;
6. orchestrator with workers;
7. broader agent only when evidence proves the simpler shapes are not enough.

Every extra decision point creates another place to test, trace, secure, and pay for.

## Pattern 1: workflow

```text
input -> validate -> retrieve -> model -> schema check -> output
```

Use when the steps are stable. A model can still be used inside a workflow for classification, extraction, or explanation.

## Pattern 2: router

```text
request -> model/router
             |-- sales-order workflow
             |-- procurement workflow
             |-- master-data workflow
```

Use when the possible paths are known, but the correct path depends on messy input.

## Pattern 3: bounded tool loop

```text
question
  -> model selects read
  -> application validates
  -> tool returns evidence
  -> model decides: enough / another read / escalate
  -> stop on explicit condition
```

Use for investigations where each result changes the next useful read.

## Pattern 4: orchestrator and workers

Use when independent tasks can run in parallel and have a clear merge rule. Example: one worker checks order data, one checks ATP, one checks integration history, then an orchestrator compares results.

Do not use workers only to make the diagram look important. Parallel agents can repeat the same search, disagree, and multiply latency without improving the answer.

## Give the loop a budget

A production agent needs hard limits:

- maximum steps;
- maximum tool calls;
- maximum wall-clock time;
- cost/token budget;
- allowed tool set;
- allowed data scope;
- retry limit;
- maximum worker count;
- termination conditions.

Useful stop states include: `resolved`, `insufficient_evidence`, `permission_denied`, `approval_required`, `tool_failure`, and `budget_exhausted`.

## Separate investigation from action

A strong enterprise pattern is:

```text
read tools -> diagnosis -> proposed change -> validation -> approval -> write tool
```

The investigation can be adaptive. The write path should be much more deterministic.

For high-impact actions, the model should produce a prepared change with evidence and expected effect. A human or policy engine approves it. The application then executes through a narrow write tool.

## SAP logistics example

Question: “Why can sales order 4711 not confirm the requested quantity?”

A bounded agent may choose among:

- order schedule lines;
- ATP snapshot;
- material/plant status;
- plant determination inputs;
- credit status;
- delivery or rejection blocks;
- recent interface errors;
- product allocation or supply constraints.

It stops when evidence supports a cause, when no authorized read can reduce uncertainty, or when a change is required.

The agent should not remove a block just because it found one. Diagnosis and correction are different permissions.

## Failure modes

- No stop condition.
- Same tool is called repeatedly with equivalent arguments.
- Agent uses a write tool to “check” current state.
- Workers receive more data than they need.
- A tool error is interpreted as “object does not exist”.
- The model invents a root cause after weak retrieval.
- Approval exists in the prompt, not in the application.
- Agent state cannot be reconstructed from traces.

## What to trace

For every step capture:

- trace and request ID;
- model and prompt version;
- selected tool;
- sanitized arguments;
- authorization result;
- tool status and latency;
- evidence IDs;
- agent decision;
- budget remaining;
- approval event if present;
- final stop reason.

## Test the loop, not only the answer

Good eval cases include:

- first tool gives enough evidence;
- first tool gives conflicting evidence;
- relevant tool is forbidden;
- tool times out;
- data is stale;
- two causes are possible;
- a write is required;
- user rejects approval;
- budget is exhausted;
- hostile instructions arrive inside a tool result.

Related: [System Boundaries](/labs/ai-ready/system-boundaries/) · [Tools and MCP](/labs/ai-ready/tools-mcp/) · [Agent with Approval Lab](/labs/ai-ready/labs/agent-approval/)