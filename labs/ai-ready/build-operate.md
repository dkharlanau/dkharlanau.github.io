---
layout: default
title: "AI Ready — Build and Operate"
description: "A practical production guide for AI services: versioning, environments, deployment gates, observability, retries, budgets, capacity, and rollback."
permalink: /labs/ai-ready/build-operate/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
hide_global_cta: true
tags: [ai, deployment, operations, observability, cicd, reliability]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Build and Operate</li></ol>
</nav>

# Build and Operate

A local AI demo proves that one path worked once. Production asks a harder question: **can we understand, reproduce, limit, and recover the behavior when the system changes?**

AI services still need ordinary engineering discipline: controlled releases, separate environments, observability, retry rules, capacity limits, and rollback. The extra difficulty is that behavior can change even when application code does not.

## Version the behavior, not only the application

In a conventional service, a code version often explains most changes in behavior. An AI service can also change because someone switched the model, edited instructions, changed a tool schema, rebuilt the retrieval index, replaced the embedding model, changed chunking or reranking, or modified a policy.

Those parts belong in deployment metadata and traces. If yesterday's answer and today's answer differ, we should be able to tell what changed.

A useful release identity may therefore include:

- application version;
- model and model configuration;
- system instructions and prompt templates;
- tool or MCP contract versions;
- retrieval, embedding, chunking, and reranking configuration;
- policy configuration;
- evaluation dataset and grader versions.

This does not mean every setting needs a complex release process. It means important behavior should not change anonymously.

## Keep environments genuinely separate

Development, test, and production should differ by more than a label in the UI.

```text
DEV  -> synthetic or local data, fast iteration
TEST -> controlled integrations and regression evaluation
PROD -> real identity, real policy, strict budgets and tracing
```

Credentials, backend targets, and write permissions should follow the environment. A local experiment should not accidentally call a production write endpoint because the same token happened to be available.

The same rule applies to retrieval. Test results are difficult to trust when a test environment silently reads the production index while using a development prompt and a different model.

## Treat model and prompt changes as releases

A production gate does not need to be complicated, but it should be explicit.

```text
code + prompts + schemas + configuration
        |
unit and schema checks
        |
representative evals
        |
security / policy checks
        |
build and release artifact
        |
limited rollout
        |
production
```

Some evaluation failures should block release rather than reduce an average score. A system that still answers most questions correctly but starts crossing an authorization boundary is not “slightly worse”.

We should decide those hard gates before a release is under pressure.

## Trace one request across the whole system

An AI answer may depend on retrieval, several model calls, one or more tools, authorization, approvals, and retries. If each component logs separately without a shared trace, diagnosing a failure becomes guesswork.

One trace or request ID should connect the important steps. From that trace we want to understand which model and instructions ran, what evidence was retrieved, which tools were called, how authorization was evaluated, whether a retry occurred, and how the final result was produced.

Operational measures then become easier to interpret. We can separate model latency from tool latency, distinguish application errors from dependency errors, and watch cost, step count, approval rate, or budget exhaustion alongside ordinary success and latency measures.

## Retries need business meaning

Retries are useful for transient failures such as a network timeout or a rate-limit response. They are dangerous when the failure means “do not try again”.

A validation error, permission denial, failed business precondition, or unsafe request normally needs a different response. A write is especially sensitive: if the network fails after the backend commits, retrying the same request may repeat the business action.

That is why retry policy belongs in application logic. Writes should use idempotency keys, business keys, version checks, or another duplicate-protection mechanism where the backend supports it. The model should not decide whether an uncertain write is safe to repeat.

## Budgets protect both cost and dependencies

One user request can expand into many model and tool calls. A tool-using agent may also create parallel work. Production limits should therefore cover more than token count.

We normally care about request timeout, maximum context, agent steps, parallel workers, model cost, tool-call count, queue depth, user or tenant rate limits, and concurrency against external systems.

These limits are part of system behavior. When a budget is exhausted, the system should return a clear degraded result or escalation state rather than quietly continue until an upstream service becomes the bottleneck.

## Cache only with a freshness rule

Caching stable reference material, schemas, tool catalogs, or short-lived read results can reduce cost and latency. The important question is how stale the value is allowed to become.

A cached handbook page and a cached deployment status have different risk. Account state, ticket status, availability, prices, permissions, and operational health may change faster than the cache is useful. If we cannot state the freshness rule, we do not yet understand what we are caching.

## Rollback has several layers

AI releases are not only code releases. We may need to roll back the application, prompt bundle, model selection, retrieval index, tool or MCP server, or policy configuration.

This is one reason to version the behavior explicitly. If a model switch causes a regression, restoring the previous model configuration should not require pretending that the application binary changed.

A good runbook also describes degraded behavior. If vector retrieval fails, perhaps lexical retrieval is still useful. If one read API fails, the system may return a partial answer and name the missing evidence. If the write service is unavailable, it can preserve a prepared change without claiming that execution succeeded.

## Production readiness is the ability to explain failure

The production question is not whether the model is impressive. It is whether the service can be operated when something goes wrong.

We should know what changed, what the request touched, what limits applied, which dependency failed, what was retried, and how to return to a known state. Once those answers are available, AI becomes another production component rather than a special exception to engineering practice.

Related: [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [Security and Governance](/labs/ai-ready/security-governance/) · [Production Readiness Lab](/labs/ai-ready/labs/production-readiness/)
