---
layout: default
title: "AI Ready — Observability"
description: "A practical guide to tracing model calls, retrieval, tools, agent steps, latency, cost, versions, failures, and privacy-safe operational telemetry."
permalink: /labs/ai-ready/engineering/observability/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, observability, tracing, metrics, logs, cost, latency]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/engineering/">Engineering</a></li><li aria-current="page">Observability</li></ol>
</nav>

# Observability

AI systems fail across several layers. A final answer alone is not enough to explain what happened.

## Trace the whole request

Use one trace ID across the path:

```text
request
 -> retrieval
 -> model
 -> tool
 -> model
 -> approval
 -> write
 -> response
```

Not every request uses every step, but all active steps should be connected.

## Capture versions

A result can change without application code changing. Store versions for:

- application;
- model profile;
- system instructions;
- prompt template;
- context builder;
- retrieval index/configuration;
- embedding model;
- reranker;
- tool schema;
- MCP server;
- policy configuration;
- eval dataset.

Without version metadata, “why did the answer change?” becomes guesswork with timestamps.

## Model-call telemetry

Useful fields include:

```text
trace_id
model_profile
instruction_version
input_size / usage
output_size / usage
latency
status
retry_count
finish/stop reason when available
```

Do not log raw sensitive prompts by default. Keep enough data to debug without creating a second ungoverned data lake.

## Retrieval telemetry

Capture:

- query or safe query hash/reference;
- filters;
- candidate source IDs;
- ranking positions/scores;
- reranker version;
- selected context IDs;
- no-evidence state;
- latency per stage.

This lets you separate “retrieval failed” from “model ignored good evidence”.

## Tool telemetry

Capture:

- tool name and version;
- sanitized arguments;
- authorization result;
- status/error class;
- latency;
- stable result/evidence ID;
- retry count;
- idempotency/request ID for writes.

Never store secrets because a trace field looked convenient.

## Agent telemetry

For a bounded agent, record the trajectory:

```text
step 1 -> selected tool -> result -> decision
step 2 -> selected tool -> result -> decision
...
stop_reason
```

Useful metrics:

- steps/request;
- repeated-tool-call rate;
- budget-exhausted rate;
- tool-error rate;
- approval-required rate;
- escalation rate.

## Metrics that matter

Track system-level outcomes, not only tokens:

- critical eval pass rate;
- successful task rate;
- no-evidence rate;
- p50/p95 latency;
- dependency latency;
- error rate;
- cost/request;
- cost/successful outcome;
- retrieval recall on monitored cases;
- tool-call failure rate;
- agent step count.

A token graph is operationally interesting. It is not a product outcome.

## Logs, metrics, traces, evals

They solve different problems:

| Signal | Main job |
|---|---|
| logs | discrete events and errors |
| metrics | trends, rates, budgets, alerts |
| traces | one request across components |
| evals | expected behavior against known cases |

Use them together.

## Decision card

**Minimum for prototype:** request IDs, errors, latency, model profile.

**Minimum for tool/RAG system:** add source/tool IDs, versions, and retrieval/tool timings.

**Minimum for agent:** add step trajectory, budgets, stop reason, approval events.

**Production:** connect traces to dashboards, alerts, eval releases, and incident review.

## Practice

Run one eval case and write the trace you would need to explain a wrong answer two weeks later. If you cannot identify the model, prompt, evidence, tool result, and deployed versions, add the missing fields before production.

Next: [Security and Governance](/labs/ai-ready/security-governance/) · [Build and Operate](/labs/ai-ready/build-operate/)
