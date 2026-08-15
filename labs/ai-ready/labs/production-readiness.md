---
layout: default
title: "AI Ready Lab — Production Readiness"
description: "A hands-on production-readiness lab for eval gates, traces, budgets, retries, secrets, deployment, degraded modes, and rollback."
permalink: /labs/ai-ready/labs/production-readiness/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, lab, production, deployment, observability, evals]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Production Readiness</li></ol>
</nav>

# Lab 04: Production Readiness

Take one of the previous labs and treat it like a service that another team must operate on Monday morning. The goal is to remove hidden assumptions from the demo.

## Starting point

Choose either:

- RAG with evals; or
- agent with approval.

The service must have a stable API, versioned configuration, synthetic test data, and no client secrets or production credentials in the repository.

## Step 1: define service budgets

Write explicit targets before tuning:

```text
p95 latency: <= 6 s
request timeout: 15 s
max agent steps: 8
max tool calls: 10
max parallel workers: 3
max retries/dependency: 2
cost budget/request: project-defined
critical eval failures: 0
```

The exact numbers are less important than making the trade-off visible.

## Step 2: version the behavior

Expose deployment metadata:

```json
{
  "app_version": "0.4.0",
  "model_profile": "reasoning-default-v2",
  "prompt_version": "orders-12",
  "tool_schema_version": "sap-read-5",
  "retrieval_version": "policy-index-2026-08-15",
  "eval_set": "architecture-golden-3"
}
```

Do not depend on an undocumented prompt pasted into a UI.

## Step 3: add a release gate

Pipeline:

```text
lint/schema tests
 -> unit tests
 -> eval dataset
 -> security cases
 -> build
 -> deploy to test
 -> smoke test
 -> limited production traffic
```

Block the release if a critical authorization, approval, grounding, or duplicate-write case fails.

## Step 4: add traces

One trace should connect:

- request;
- retrieval;
- model calls;
- tool/MCP calls;
- auth checks;
- approvals;
- retries;
- final result.

Do not log secrets or unnecessary personal data just because traces are convenient.

## Step 5: failure policy

Define behavior for:

| Failure | Expected behavior |
|---|---|
| model timeout | retry if safe, then return controlled failure/degraded response |
| retrieval unavailable | use allowed trusted tools or return evidence gap |
| SAP read unavailable | partial diagnosis with missing dependency named |
| permission denied | stop that path, do not reinterpret it as missing data |
| rate limit | backoff, respect total request budget |
| write timeout | check idempotency/business key before retry |
| approval expired | require new approval |

## Step 6: secrets and identity

Use environment-specific secret storage or workload identity. Development credentials must not reach production. A model should receive business data required for the task, not backend credentials.

## Step 7: degraded mode

Decide what still works when one component is down.

Example:

```text
vector search down -> lexical retrieval remains
reranker down -> use baseline ranking
agent disabled -> deterministic status lookup remains
write service down -> diagnosis remains read-only
```

A degraded service that tells the truth is more useful than a “smart” service that invents completion.

## Step 8: rollback drill

Practice rolling back:

- code version;
- prompt bundle;
- model profile;
- retrieval index;
- tool/MCP server;
- policy configuration.

Create one deliberate regression, catch it with evals, deploy it to test, and prove the rollback path.

## Step 9: operational dashboard

Track at least:

- success and error rate;
- p95 latency;
- dependency latency;
- model usage/cost;
- tool failures;
- agent steps per request;
- retrieval no-evidence rate;
- approval and rejection rate;
- budget-exhausted rate.

## Done when

Another engineer can answer these questions without asking the original author:

1. Which versions produced this result?
2. Why did the request fail?
3. Which dependency was slow?
4. Which eval protects this business behavior?
5. Can a retry duplicate a write?
6. What works in degraded mode?
7. How do we roll back the last behavior change?

Read first: [Build and Operate](/labs/ai-ready/build-operate/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [Security and Governance](/labs/ai-ready/security-governance/)