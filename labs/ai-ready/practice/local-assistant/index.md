---
layout: default
title: "AI Ready Practice — Local Operations Assistant"
description: "Build a local read-first assistant with retrieval, typed tools, traces, prepared changes, approval, idempotency, and stale-state protection."
permalink: /labs/ai-ready/practice/local-assistant/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, practice, agents, tools, approval, observability, local]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/practice/">Practice</a></li><li aria-current="page">Local Assistant</li></ol>
</nav>

# Local Operations Assistant

This project joins the earlier pieces into one small application.

It deliberately uses a deterministic planner instead of an LLM. That keeps retrieval, tools, state, approval, idempotency, and traces visible. Later you can replace the planner with a model without redesigning the authority boundary.

## Architecture

```text
incident
  -> read incident
  -> read service state
  -> retrieve trusted runbooks
  -> deterministic planner
  -> prepared change
  -> approval bound to payload hash
  -> optimistic version check
  -> idempotent execution
  -> trace
```

The synthetic workspace contains services, incidents, trusted runbooks, and one hostile external note.

## Run it

Investigate only:

```bash
python3 labs/ai-ready/practice/local-assistant/app.py --incident inc-101
```

Approve and execute the prepared change:

```bash
python3 labs/ai-ready/practice/local-assistant/app.py --incident inc-101 --approve
```

Run failure-path tests:

```bash
python3 labs/ai-ready/practice/local-assistant/app.py --self-test
```

The self-test covers:

- trusted retrieval;
- indirect prompt-injection filtering;
- exact approval binding;
- stale-version rejection;
- duplicate execution;
- tool-budget exhaustion;
- a read-only incident where no change should be proposed.

## Where a model fits

Replace only the decision component:

```text
evidence + typed tool results
  -> model proposes next read or recommendation
  -> application validates action
  -> application owns approval and execution
```

Do not move identity, authorization, payload validation, durable state, or the write itself into the prompt.

## Extend it

1. add an explicit model adapter;
2. turn read tools into MCP tools;
3. persist traces to JSONL;
4. run the scenario set as evals;
5. add timeouts and degraded behavior;
6. expose a small HTTP API;
7. containerize it and perform a rollback drill.

This is the useful transition from “agent demo” to application architecture. The model may become smarter. The safety boundary should remain boring.

Related: [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Security](/labs/ai-ready/security-governance/) · [Build and Operate](/labs/ai-ready/build-operate/)
