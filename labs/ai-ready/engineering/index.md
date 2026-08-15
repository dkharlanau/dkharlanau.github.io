---
layout: default
title: "AI Ready — Engineering Handbook"
description: "A practical learning path from model selection to prompting, structured output, embeddings, RAG, tools, MCP, agents, memory, evals, observability, and deployment."
permalink: /labs/ai-ready/engineering/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, engineering, models, prompting, embeddings, rag, mcp, agents, evals, deployment]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li aria-current="page">Engineering Handbook</li></ol>
</nav>

# AI Engineering Handbook

This is the build path. Read it from top to bottom once, then jump directly to the layer you need for a real problem.

The rule is simple: **do not add a layer because it is fashionable. Add it because a measured problem needs it.**

## The 13-step map

| Step | Topic | Use it to answer |
|---|---|---|
| 01 | [Models](/labs/ai-ready/engineering/models/) | Which model profile fits quality, latency, cost, privacy, and modality? |
| 02 | [Prompt and Context](/labs/ai-ready/engineering/prompt-context/) | What instructions and evidence should the model receive? |
| 03 | [Structured Output](/labs/ai-ready/engineering/structured-output/) | How does model output become a reliable software contract? |
| 04 | [Embeddings and Vector Search](/labs/ai-ready/engineering/embeddings-vector-search/) | How do we search by meaning, and when is lexical search better? |
| 05 | [RAG](/labs/ai-ready/data-rag/) | How do we answer from current or private evidence? |
| 06 | [Tool Calling](/labs/ai-ready/tools-mcp/#tool-first-protocol-second) | How does a model read current facts or call deterministic actions? |
| 07 | [MCP](/labs/ai-ready/tools-mcp/) | When should several AI clients share one capability contract? |
| 08 | [Agents](/labs/ai-ready/agent-architecture/) | When should the system choose the next step from changing evidence? |
| 09 | [Memory and State](/labs/ai-ready/engineering/memory-state/) | What must survive one request, one session, or many sessions? |
| 10 | [Evals](/labs/ai-ready/evals-reliability/) | How do we know a change is better and did not break something critical? |
| 11 | [Observability](/labs/ai-ready/engineering/observability/) | How do we explain latency, cost, tool choices, and failures? |
| 12 | [Security and Governance](/labs/ai-ready/security-governance/) | What can untrusted content, broad permissions, or sensitive data break? |
| 13 | [Deployment](/labs/ai-ready/build-operate/) | How do we release, operate, degrade, and roll back the system? |

## Architecture ladder

Start low and move up only when needed:

```text
single model call
  -> prompt + schema
  -> retrieval
  -> typed tools
  -> workflow
  -> bounded agent
  -> workers / multi-agent only with measured value
```

A large part of AI engineering is deciding what **not** to build.

## Decision cards

### Need better wording or extraction

Start with prompt, examples, structured output, and evals.

Do not add RAG unless external knowledge is missing. Do not add an agent unless the next step must change during the task.

### Need current or private knowledge

Use retrieval. Keep source IDs, dates, permissions, and a no-evidence state.

### Need one exact fact from another system

Use a read tool or API. Do not make the model guess from memory.

### Need an external action

Use a typed tool. Keep authorization, validation, retries, and side effects outside the model.

### Need several AI clients to share capabilities

Consider MCP. A direct tool remains simpler when one application owns the integration.

### Need adaptive investigation

Use a bounded agent with read-first tools, hard budgets, explicit stop states, and traces.

### Need durable personalization

Store explicit user preferences or application state. Do not dump the whole conversation forever and call it memory.

### Need production confidence

Create evals, traces, budgets, failure policy, and rollback before adding more autonomy.

## Build path

A useful learning sequence is:

1. call a model and compare two model profiles;
2. force one response into a schema and validate it;
3. build a lexical retrieval baseline;
4. add semantic similarity only for cases the baseline misses;
5. answer from retrieved evidence with citations;
6. expose two read-only tools;
7. wrap the same capability in MCP and compare the extra value;
8. build a bounded tool loop;
9. persist explicit state outside the model;
10. create a small golden eval set;
11. add end-to-end traces;
12. inject hostile content and test the security boundary;
13. deploy with budgets, degraded mode, and rollback.

## Runnable examples

These examples use Python standard library only. They teach the mechanics without hiding them behind an SDK:

- [`structured_output_validation.py`](/labs/ai-ready/examples/structured_output_validation.py) — validate a model-like JSON response before software uses it.
- [`lexical_retrieval.py`](/labs/ai-ready/examples/lexical_retrieval.py) — build a tiny lexical retrieval baseline.
- [`tool_loop.py`](/labs/ai-ready/examples/tool_loop.py) — simulate a bounded read-only tool loop.
- [`eval_runner.py`](/labs/ai-ready/examples/eval_runner.py) — run deterministic regression cases.
- [`approval_state.py`](/labs/ai-ready/examples/approval_state.py) — bind approval to an exact prepared action and precondition.

Run an example with:

```bash
python3 labs/ai-ready/examples/lexical_retrieval.py
```

## What good looks like

You should be able to explain a design without starting from a vendor product name:

```text
problem
-> required facts and actions
-> model role
-> deterministic boundaries
-> retrieval/tools
-> state
-> evals
-> security controls
-> operational budgets
-> deployment and rollback
```

If the explanation begins with “we will use an agent framework” before the problem is clear, the architecture has started at the wrong end.

Related: [Practical Use Cases](/labs/ai-ready/use-cases/) · [Architecture Deep Dives](/labs/ai-ready/deep-dives/) · [Hands-on Labs](/labs/ai-ready/#labs)
