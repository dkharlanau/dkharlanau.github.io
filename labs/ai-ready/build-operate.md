---
layout: default
title: "AI Ready — Build and Operate"
description: "A practical production guide for AI services: environments, versioning, deployment gates, observability, retries, budgets, capacity, and rollback."
permalink: /labs/ai-ready/build-operate/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, deployment, operations, observability, cicd, reliability]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Build and Operate</li></ol>
</nav>

# Build and Operate

A local AI demo proves that one path worked once. Production needs repeatable builds, controlled configuration, traces, limits, failure handling, and rollback. AI adds more moving versions, but the basic engineering discipline is pleasantly boring.

## Problem

A demo can appear useful while lacking versioning, observability, budgets, rollback, and operational ownership.

## Version the whole behavior

The application version is not enough. A result may change because of:

- model version;
- system instructions;
- prompt templates;
- tool schema;
- MCP server version;
- retrieval index;
- embedding model;
- chunking rules;
- reranker;
- policy configuration;
- eval dataset.

Keep these versions in deployment metadata and traces. Otherwise a changed answer becomes a séance.

## Environment model

Use separate environments for at least development, test, and production. Keep credentials and external-system targets separate.

```text
DEV  -> synthetic / local data, fast iteration
TEST -> controlled integrations, regression evals
PROD -> real identity, real policy, strict logging and budgets
```

Do not let a local experiment accidentally use a production write credential.

## Deployment gate

A useful release pipeline can be:

```text
code + prompts + schemas
        |
unit/schema tests
        |
eval suite
        |
security checks
        |
build artifact
        |
canary / limited traffic
        |
production
```

Critical eval failures should block release. Define the rule before a release is under pressure.

## Observe the request end to end

Use one trace ID across:

- incoming request;
- retrieval calls;
- model calls;
- tool or MCP calls;
- authorization checks;
- approval events;
- retries;
- final response.

Useful operational measures include:

- success/error rate;
- p50/p95/p99 latency;
- model and tool latency separately;
- model usage and cost;
- retrieval hit quality;
- tool failure rate;
- approval rate;
- agent step count;
- budget-exhausted rate.

## Retry at the right layer

Retry examples:

- transient network timeout;
- rate-limit response with backoff;
- temporary dependency error.

Do not blindly retry:

- validation error;
- permission denied;
- failed business precondition;
- unsafe request;
- non-idempotent write without duplicate protection.

A retry policy belongs to the application, not to the model’s mood.

## Capacity and budgets

Set explicit limits before production:

- request timeout;
- maximum context size;
- maximum agent steps;
- maximum parallel workers;
- model cost/request;
- tool-call budget;
- queue depth;
- rate limits by user or tenant;
- external-system concurrency.

A tool-using agent can fan out many backend calls from one user request. The model may still be cheerful while the dependency is becoming an accidental load test.

## Caching

Cache only when the freshness rule is clear. Good candidates can include stable reference content, tool catalogs, schemas, or repeated read results with a short TTL.

Do not cache changing facts without knowing how stale they may become. Account state, ticket status, deployment health, prices, availability, and permissions can change quickly.

## Rollback

Plan rollback for several layers:

- application code;
- prompt/instruction bundle;
- model selection;
- retrieval index/configuration;
- MCP/tool server;
- policy configuration.

A model change can be rolled back even when no application code changed. Treat model and prompt changes as releases.

## Practical service example

A research-and-operations assistant may depend on a model API, lexical/vector search, an MCP server, repository or ticket APIs, identity, and tracing. A production runbook should say what happens when each dependency is slow or unavailable.

Example degraded behavior:

- vector retrieval unavailable -> use lexical retrieval;
- one read API unavailable -> return a partial answer with the missing evidence named;
- model unavailable -> keep deterministic status lookup available;
- write service unavailable -> keep prepared change, do not pretend execution succeeded.

## Production checklist

- immutable deployment artifact;
- separate environments and credentials;
- versioned prompts/tools/retrieval/evals;
- CI eval gate;
- secret store;
- least-privilege runtime identity;
- trace correlation;
- latency and cost budgets;
- retry/backoff policy;
- idempotent writes;
- rate and concurrency limits;
- dashboards and alerts;
- incident runbook;
- rollback path;
- post-incident eval case.

Related: [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [Security and Governance](/labs/ai-ready/security-governance/) · [Production Readiness Lab](/labs/ai-ready/labs/production-readiness/)
