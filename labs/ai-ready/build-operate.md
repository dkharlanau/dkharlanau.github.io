---
layout: default
title: "AI Ready — Build and Operate"
description: "A practical production guide for AI services: versioning, environments, deployment gates, observability, retries, budgets, capacity, and rollback."
permalink: /labs/ai-ready/build-operate/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-29
hide_global_cta: true
tags: [ai, deployment, operations, observability, cicd, reliability, cost, token-economics]
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

<h2 id="token-economics">Token economics: spend where intelligence matters</h2>

AI cost rarely grows because of one expensive model call. It grows because the system repeats work: the same context is sent again, agents take too many steps, retries multiply, large tool schemas travel with every request, and long answers are produced only to be shortened later.

So do not optimize **price per token**. Optimize **cost per accepted task**.

```text
cost per accepted task
  = model + tool + retrieval + infrastructure cost
    / tasks that pass the quality gate
```

A cheaper call can still be the expensive option if it creates more retries, more review, or more failed outcomes.

<div class="callout callout--note">
  <p><strong>Lead rule:</strong> reduce cost only while quality, latency, security, and control stay inside the agreed boundary.</p>
</div>

### First: find the waste

Before changing the model, trace where money is actually going.

Look at:

- model calls per task;
- uncached input versus cached input;
- output and reasoning tokens;
- retries and agent steps;
- tool and search calls;
- repeated tool schemas or large JSON payloads;
- media size;
- human correction after the model is done.

The average is useful. The expensive tail is usually more useful. Ten normal requests and one runaway agent can have the same average as eleven healthy requests.

### Take the cheap wins first

These changes often reduce cost without changing the task itself.

<div class="table-scroll study-table" role="region" aria-label="Low-risk AI cost levers" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Lever</th><th scope="col">What to change</th><th scope="col">Watch for</th></tr>
</thead>
<tbody>
<tr><th scope="row">Prompt caching</th><td>Keep stable instructions, examples, and tool definitions in a stable prefix.</td><td>One changing timestamp, user field, or reordered tool near the top can kill reuse.</td></tr>
<tr><th scope="row">Batch / async work</th><td>Move evals, enrichment, reports, embeddings, and nightly jobs away from interactive execution when the provider supports it.</td><td>Check turnaround time, retries, and current service pricing.</td></tr>
<tr><th scope="row">Smaller context</th><td>Send the evidence needed for this task, not the whole manual, chat history, or export.</td><td>Measure retrieval coverage. Smaller context is not better if the answer loses the key evidence.</td></tr>
<tr><th scope="row">Fewer tool schemas</th><td>Show the model only the tools relevant to the current route or stage.</td><td>Do not hide tools required for valid exception paths.</td></tr>
<tr><th scope="row">Programmatic filtering</th><td>Filter, join, calculate, and validate in code before data enters model context.</td><td>Keep source IDs and evidence needed for traceability.</td></tr>
<tr><th scope="row">Prompt cleanup</th><td>Remove old instructions, duplicated examples, and unused schema fields.</td><td>Run the same eval before and after. Shorter is useful only if behavior holds.</td></tr>
<tr><th scope="row">Shorter output</th><td>Ask for the smallest output the next consumer really needs.</td><td>Do not remove explanation needed for audit, review, or a business decision.</td></tr>
<tr><th scope="row">Agent limits</th><td>Cap steps, retries, tool calls, wall time, parallel workers, and spend.</td><td>Define a useful stop state such as <code>budget_exhausted</code> instead of letting the loop drift.</td></tr>
</tbody>
</table>
</div>

A useful prompt shape is simple:

```text
stable instructions
stable tool definitions
stable reference rules
---------------------- reuse boundary
user-specific context
current request
```

The exact caching rules depend on the provider and model. The design rule does not: **put stable content before changing content and measure actual cache usage.**

### Remove calls before reducing intelligence

The first instinct is often: “use a cheaper model.” That is not always the best first move.

Start by removing calls that should not exist:

- exact calculation → code;
- sorting or filtering → code;
- policy check → code;
- validation → code;
- data that can be joined before the model → join it first;
- second model call that only reformats the first result → remove it;
- one more agent search after enough evidence is already available → stop.

Fewer calls usually improve cost, latency, and reliability at the same time.

### Then the trade-offs begin

After the low-risk savings, cheaper usually means giving something up: reasoning depth, latency, generality, or operating simplicity.

<div class="table-scroll study-table" role="region" aria-label="AI cost and quality trade-offs" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Lever</th><th scope="col">What you trade</th><th scope="col">Good fit</th><th scope="col">How to prove it</th></tr>
</thead>
<tbody>
<tr><th scope="row">Lower reasoning effort</th><td>Depth on harder cases.</td><td>Routine extraction, classification, or bounded reasoning.</td><td>Run the same eval at each effort level.</td></tr>
<tr><th scope="row">Cheap first, retry failures</th><td>Latency on failed first attempts.</td><td>Most requests are easy and failure is easy to detect.</td><td>Count retries in the final task cost.</td></tr>
<tr><th scope="row">Tighter task budgets</th><td>Some difficult tasks will stop or escalate.</td><td>Long-tail agent runs create much of the spend.</td><td>Compare pass rate and cost at each budget.</td></tr>
<tr><th scope="row">Step down model tier</th><td>Performance on ambiguous or difficult work.</td><td>High-volume, narrow, checkable tasks.</td><td>Compare easy and hard segments separately.</td></tr>
<tr><th scope="row">Routing / cascades</th><td>Router errors and more architecture.</td><td>Traffic contains clear easy and hard populations.</td><td>Measure wrong routes, retries, and total cascade cost.</td></tr>
<tr><th scope="row">Specialized smaller model</th><td>Generality plus training and serving work.</td><td>Stable, repetitive, high-volume tasks.</td><td>Include training, serving, monitoring, and drift in the economics.</td></tr>
<tr><th scope="row">Self-host open weights</th><td>Managed-service simplicity.</td><td>High sustained utilization or strong deployment constraints.</td><td>Use total cost of ownership, not GPU price.</td></tr>
</tbody>
</table>
</div>

The order is usually:

1. remove waste;
2. improve cache and batch use;
3. shrink unnecessary context and output;
4. tune effort and budgets;
5. route easy and hard work differently;
6. change the model;
7. consider specialization or self-hosting only when volume justifies the operating burden.

This is not a law. It is a way to avoid redesigning the platform before fixing obvious waste.

### The eval is the gate

If we cannot measure quality, we cannot safely reduce cost.

For a first baseline, freeze **20–30 representative requests**. Include normal work, difficult work, and failures that matter. Keep the set unchanged while comparing prompts, models, effort, routing, and budgets.

Use the cheapest reliable scoring method:

- deterministic test;
- schema or business-rule check;
- golden answer;
- short human rubric;
- model grader only when simpler checks are not enough.

The decision is then simple:

<div class="table-scroll study-table" role="region" aria-label="AI cost optimization decision gate" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Result</th><th scope="col">Meaning</th></tr>
</thead>
<tbody>
<tr><th scope="row">Cheaper, same quality</th><td>Keep it if latency and controls are still acceptable.</td></tr>
<tr><th scope="row">Cheaper, slightly worse</th><td>Business decision: is the quality loss inside the agreed tolerance?</td></tr>
<tr><th scope="row">Cheaper call, more retries</th><td>Recalculate the full task cost. The first call is not the unit of value.</td></tr>
<tr><th scope="row">More expensive, much better</th><td>It may still win if it removes review, retries, rework, or business failure.</td></tr>
</tbody>
</table>
</div>

Related: [Evals and Reliability](/labs/ai-ready/evals-reliability/).

### Five questions that expose the real cost problem

You can usually identify the project shape in one meeting.

<div class="table-scroll study-table" role="region" aria-label="Five AI cost discovery questions" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Ask</th><th scope="col">What the answer tells you</th></tr>
</thead>
<tbody>
<tr><th scope="row">1. What does one accepted task cost today?</th><td>If the answer is only a monthly invoice or token price, measurement is the first project.</td></tr>
<tr><th scope="row">2. How much repeated input is actually cached?</th><td>Low reuse points to unstable prefixes, changing tool schemas, request ordering, or provider eligibility.</td></tr>
<tr><th scope="row">3. Which AI traffic has nobody waiting for it?</th><td>That is your batch and asynchronous candidate set.</td></tr>
<tr><th scope="row">4. Do we have an eval, or only an opinion?</th><td>No eval means model, effort, routing, and budget changes are mostly guesswork.</td></tr>
<tr><th scope="row">5. What are we not allowed to change?</th><td>Residency, security, latency, approved-model lists, contracts, and committed cloud spend may remove options before cost work starts.</td></tr>
</tbody>
</table>
</div>

These answers usually point to one of five starting points: **measurement, request shape, batch execution, evaluation, or architecture constraints.**

### Operate it as a loop

1. **Measure** cost and quality per task.
2. **Find** the expensive pattern, not just the expensive model.
3. **Change one lever.**
4. **Run the same eval.**
5. **Keep the change only if the whole task improves.**

Useful production measures are cost per accepted task, calls per task, cached-input share, retry rate, agent steps, p50/p95 latency, eval pass rate, and human correction time.

### Know where not to optimize

Do not save tokens by weakening authorization, policy checks, transaction controls, evidence, or auditability. Do not cache dynamic business facts without a freshness rule. Do not hide sources just to make context smaller.

The right question is not “How do we use fewer tokens?”

It is: **“Which spend is not creating accepted business value?”**

### Current provider examples

Provider behavior and pricing move quickly. Use current documentation before putting any percentage into a business case:

- [OpenAI Prompt Caching](https://developers.openai.com/api/docs/guides/prompt-caching)
- [OpenAI Batch API](https://developers.openai.com/api/docs/guides/batch)
- [Google Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Google Gemini Batch API](https://ai.google.dev/gemini-api/docs/batch-api)

Reviewed for this section: 29 Sep 2026.

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
