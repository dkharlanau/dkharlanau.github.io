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

<h2 id="token-economics">Token economics: optimize cost per successful task</h2>

Token cost is only one part of AI cost. A workflow becomes expensive when it makes too many model calls, carries the same context again and again, produces more output than the task needs, uses a premium model for simple work, or lets retries and agent loops multiply silently.

The useful unit is therefore **cost per successful task**, not price per million tokens.

```text
cost per successful task
  = total model + tool + retrieval + infrastructure spend
    / number of outcomes that pass the quality gate
```

This changes the optimization question. A cheaper model that creates more retries or more rejected answers can make the final task more expensive. A larger model can sometimes be cheaper if it solves the task in one call instead of five. Measure the full path.

<div class="callout callout--note">
  <p><strong>Lead rule:</strong> optimize for the lowest cost that still passes the required quality, latency, security, and control gates.</p>
</div>

### First find where the cost is created

For each request or business task, separate these drivers:

- number of model calls;
- uncached input tokens;
- cached reads and cache writes, when the provider exposes them;
- output and reasoning tokens;
- retrieval, search, and paid tool calls;
- agent steps, retries, and parallel workers;
- media input such as large images, audio, or video;
- vector storage, cache storage, or other supporting infrastructure.

Then rank traces by total cost. The expensive tail often teaches more than the average.

<div class="table-scroll study-table" role="region" aria-label="AI cost optimization levers" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Lever</th><th scope="col">What changes</th><th scope="col">Use it when</th><th scope="col">Main check</th></tr>
</thead>
<tbody>
<tr><th scope="row">Model routing</th><td>Use a smaller or cheaper model for simple classification, extraction, formatting, or low-risk steps. Escalate only harder cases.</td><td>One expensive model handles every request today.</td><td>Keep one eval set across routes. A cheaper call is not a saving if failure and retry rates rise.</td></tr>
<tr><th scope="row">Prompt caching</th><td>Keep reusable instructions, examples, and tool definitions in a stable prefix so the provider can reuse processed context.</td><td>Many requests share a large common prefix.</td><td>Measure actual cache-hit tokens. Dynamic timestamps, user data, reordered tools, or other early changes can destroy prefix reuse.</td></tr>
<tr><th scope="row">Batch or flex execution</th><td>Move non-interactive work to a discounted asynchronous service tier when the provider offers one.</td><td>Evals, enrichment, classification, embeddings, document processing, or overnight jobs do not need an immediate answer.</td><td>Confirm turnaround time, rate limits, retry behavior, and the current provider price before building the business case.</td></tr>
<tr><th scope="row">Context reduction</th><td>Retrieve only the evidence needed for this question instead of sending the full manual, chat history, or data export.</td><td>Input grows faster than answer quality.</td><td>Evaluate retrieval coverage. Cutting context is useful only if the required evidence still reaches the model.</td></tr>
<tr><th scope="row">Progressive tool disclosure</th><td>Expose only the tool families relevant to the current route or task instead of placing every schema in every call.</td><td>A large tool catalog consumes context although most tools are never used.</td><td>Routing must be testable. Do not hide a tool that is required for a legitimate exception path.</td></tr>
<tr><th scope="row">Programmatic tool chaining</th><td>Filter, aggregate, validate, or join tool results in normal code and pass the model the useful result rather than raw payloads.</td><td>Large JSON responses repeatedly enter model context.</td><td>Keep source IDs and evidence needed for traceability. Compression must not erase the reason behind a decision.</td></tr>
<tr><th scope="row">Prompt and schema audit</th><td>Remove obsolete instructions, duplicated examples, unused schema fields, and prompting written for an older model.</td><td>Prompts have grown through many incremental fixes.</td><td>Run the same evals before and after. Shorter is useful only when behavior stays good.</td></tr>
<tr><th scope="row">Output discipline</th><td>Ask for the smallest output the next consumer needs: structured fields, short explanations, or bounded sections.</td><td>The model writes long prose that is later parsed, summarized, or discarded.</td><td>Do not remove explanations that are required for audit, user trust, or decision quality.</td></tr>
<tr><th scope="row">Agent budgets</th><td>Cap steps, retries, tool calls, wall time, parallel workers, and spend per task.</td><td>Agent loops occasionally run much longer than normal.</td><td>Define a useful stop state such as <code>budget_exhausted</code> or <code>insufficient_evidence</code> instead of silently continuing.</td></tr>
<tr><th scope="row">Semantic or result caching</th><td>Reuse a previous answer or deterministic result when the new request is equivalent enough.</td><td>Questions repeat and the underlying fact is stable.</td><td>Key the cache by permission scope, data version, and freshness. Do not reuse a result across users or states that should be isolated.</td></tr>
<tr><th scope="row">Media reduction</th><td>Crop, resize, sample, or extract the relevant part of image, video, or audio before model ingestion.</td><td>Large media enters the model although only a small region or time window matters.</td><td>Keep enough resolution and context for the decision. Validate the reduced input on representative cases.</td></tr>
</tbody>
</table>
</div>

### Preserve the stable prefix

Prompt caching deserves special attention because it can fail silently. A long shared prompt may look reusable to a developer while one changing field near the beginning makes most of the prefix different.

A safer request shape is:

```text
stable provider / system instructions
stable tool definitions
stable reference rules
------------------------- cache-friendly boundary
user-specific context
current timestamp or request metadata
new user input
```

The exact cache rules are provider- and model-specific. The design principle is stable: put shared content before changing content, preserve ordering where possible, and monitor reported cache usage instead of assuming reuse happened.

### Reduce calls before reducing intelligence

A common mistake is to start by switching every call to the cheapest model. First remove calls that should not exist.

Examples:

- use code for exact calculations, filtering, sorting, validation, and policy checks;
- stop asking a model to summarize data that the next function can read directly;
- avoid a second model call when structured output from the first call already contains the required fields;
- stop an agent after sufficient evidence instead of asking for one more search “just in case”;
- merge independent prompt steps when one well-defined call can perform them safely;
- do not run several workers on work that is not genuinely parallel.

Call reduction often improves latency and reliability at the same time as cost.

### Use a simple optimization loop

1. **Measure.** Record tokens, calls, cache usage, retries, tools, latency, quality result, and cost for each task.
2. **Find the expensive shape.** Separate normal requests from the costly tail: long contexts, loops, retries, media, or premium-model routes.
3. **Change one lever.** For example, stabilize the prefix, reduce retrieval size, cap output, route easy cases, or move offline work to batch.
4. **Run the same eval set.** Compare quality, latency, and cost on the same population.
5. **Keep the change only if the full task improves.** A token reduction that causes more human correction is not an optimization.

Useful production measures include:

- cost per request;
- **cost per successful task**;
- input, cached-input, output, and reasoning tokens when available;
- model calls and tool calls per task;
- cache-hit token ratio;
- retry rate;
- agent steps and parallel workers;
- p50 and p95 latency;
- eval pass rate or accepted-output rate;
- human correction time for tasks where review is part of the process.


### After the free wins, every saving buys a trade-off

Some savings are close to free: remove useless calls, stabilize the cache prefix, shorten irrelevant context, move background work to batch, and stop producing text nobody uses.

After that, the discussion changes. We start trading **quality, latency, generality, or operating effort** for lower cost. That can still be the right decision, but now the eval becomes the gate.

<div class="table-scroll study-table" role="region" aria-label="AI cost and quality trade-offs" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Lever</th><th scope="col">What we trade</th><th scope="col">When it can make sense</th><th scope="col">What must prove it</th></tr>
</thead>
<tbody>
<tr><th scope="row">Lower reasoning effort</th><td>Depth of analysis on harder tasks.</td><td>The task is mostly extraction, classification, routine explanation, or well-bounded reasoning and the provider exposes an effort control.</td><td>Run the same cases at each setting. Check both pass rate and cost per successful task.</td></tr>
<tr><th scope="row">Cheap first, retry the failures</th><td>More latency on the cases that fail first pass, plus a reliable way to detect failure.</td><td>Most requests are easy and failure can be detected by tests, schema checks, confidence rules, or a reviewer.</td><td>Measure the full cascade, including retries. A cheap first call is useful only if detection is strong.</td></tr>
<tr><th scope="row">Task budgets</th><td>Some hard cases will stop earlier or escalate.</td><td>Long-tail agent runs create much of the spend and the business accepts explicit stop states.</td><td>Track pass rate by budget level and define what happens at <code>budget_exhausted</code>.</td></tr>
<tr><th scope="row">Stronger model, lower effort</th><td>Sometimes very little; sometimes a surprising quality drop.</td><td>A stronger model can solve the task with a lower effort setting or fewer retries than a mid-tier model.</td><td>Benchmark the combination. Model price alone does not tell us task economics.</td></tr>
<tr><th scope="row">Step down a model tier</th><td>Generality and performance on ambiguous or difficult cases.</td><td>Work is high-volume, narrow, easy to check, and mistakes are recoverable.</td><td>Compare by task segment, not only one average score. Keep the hard cases visible.</td></tr>
<tr><th scope="row">Routing and cascades</th><td>Router errors and extra architecture.</td><td>Traffic has clear easy and hard populations, so not every request needs the same model.</td><td>Measure wrong-route rate, retry rate, quality by route, and the cost of the router itself.</td></tr>
<tr><th scope="row">Cheap workers under an orchestrator</th><td>Coordination, duplicated context, and more failure paths.</td><td>The work can be split into genuinely independent parts and merged cleanly.</td><td>Compare against one capable model. More workers are not automatically cheaper.</td></tr>
<tr><th scope="row">Distill or specialize a smaller model</th><td>Generality, plus a training and serving pipeline to maintain.</td><td>The task is narrow, repetitive, stable, high-volume, and there is enough labeled behavior to teach and test it.</td><td>Count training, serving, monitoring, retraining, and drift costs. Evaluate outside the training examples.</td></tr>
<tr><th scope="row">Self-host open weights</th><td>Managed-service simplicity for infrastructure, capacity planning, patching, safety work, and idle hardware risk.</td><td>Volume is high, utilization can stay high, deployment constraints justify it, and the selected model passes the same quality gate.</td><td>Use total cost of ownership, not GPU price. Include people, redundancy, storage, observability, upgrades, and spare capacity.</td></tr>
</tbody>
</table>
</div>

A useful order is:

1. remove waste;
2. use provider discounts and caching;
3. reduce unnecessary context and output;
4. tune effort and budgets;
5. route easy and hard work differently;
6. change the model only after the earlier levers are measured;
7. consider specialization or self-hosting only when volume and operating maturity justify it.

The sequence is not a law. It is a way to avoid rebuilding the architecture before checking the cheaper changes.

### The eval is the gate

Cost work without an eval is guesswork. If we cannot tell whether the cheaper version is still good enough, we cannot safely optimize it.

For a first practical baseline, freeze **20–30 representative requests**. This is not a magic number; it is a small working set that a team can review quickly. Include normal cases, difficult cases, and at least a few failures that matter.

Use the cheapest scoring method that gives a trustworthy answer:

- exact checks or unit tests for deterministic outputs;
- schema and business-rule checks for structured results;
- golden answers where the expected result is stable;
- a short human rubric for quality that cannot be checked exactly;
- a model grader only where simpler checks are not enough.

Keep the request set fixed while comparing model, effort, routing, prompt, and budget changes. If the test population changes every time, the cost comparison is weak.

A simple decision table is enough:

<div class="table-scroll study-table" role="region" aria-label="AI cost optimization decision gate" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Change</th><th scope="col">Cost</th><th scope="col">Quality</th><th scope="col">Decision</th></tr>
</thead>
<tbody>
<tr><th scope="row">Cheaper and same quality</th><td>Down</td><td>Stable</td><td>Good candidate. Check latency and control boundaries, then keep it.</td></tr>
<tr><th scope="row">Cheaper and slightly worse</th><td>Down</td><td>Down</td><td>Business decision. Is the quality loss inside the agreed tolerance?</td></tr>
<tr><th scope="row">Cheaper but more retries</th><td>Maybe down</td><td>Unclear</td><td>Calculate the full task cost. The first call is not the unit of value.</td></tr>
<tr><th scope="row">More expensive but much better</th><td>Up</td><td>Up</td><td>May still win if it removes retries, review, rework, or business failure.</td></tr>
</tbody>
</table>
</div>

Related: [Evals and Reliability](/labs/ai-ready/evals-reliability/).

### Five questions for one cost meeting

We can usually tell in one meeting whether the opportunity is mainly **measurement, architecture, model choice, or platform economics**. We do not need source-code access to start.

<div class="table-scroll study-table" role="region" aria-label="Five AI cost discovery questions" tabindex="0">
<table class="study-table__table">
<thead>
<tr><th scope="col">Question</th><th scope="col">Why it matters</th><th scope="col">What the answer tells us</th></tr>
</thead>
<tbody>
<tr><th scope="row">1. What does one successful task cost today?</th><td>A monthly invoice or price per million tokens is too far from the business outcome. We need cost per completed, accepted task.</td><td>If nobody can answer, the first project is measurement. That is often a small project and it unlocks every later decision.</td></tr>
<tr><th scope="row">2. How much reusable input actually becomes cached input?</th><td>Agent loops and repeated workflows often resend a large stable prefix. If reuse is expected but cache reads stay low, part of the architecture is wasting work.</td><td>Low reuse points us toward prefix instability, changing tool schemas, request ordering, or provider eligibility before we touch model quality.</td></tr>
<tr><th scope="row">3. Which AI traffic has nobody waiting for it?</th><td>Evals, enrichment, report generation, bulk classification, embeddings, and nightly jobs usually do not need interactive latency.</td><td>This is the candidate set for batch, queues, lower-priority service tiers, and more aggressive scheduling.</td></tr>
<tr><th scope="row">4. Do we have an eval, or only an opinion?</th><td>Without a repeatable outcome check, we cannot safely lower effort, change models, add routing, or tighten budgets.</td><td>If there is no eval, that becomes the first deliverable. Freeze representative requests and create the smallest scoring method that works.</td></tr>
<tr><th scope="row">5. What are we not allowed to do?</th><td>Residency, retention, approved-model lists, security rules, latency commitments, contracts, and committed cloud spend can remove options before cost analysis starts.</td><td>Strong constraints usually make the low-risk levers more valuable: measurement, caching, context reduction, batching, and call reduction.</td></tr>
</tbody>
</table>
</div>

These five answers also tell us what kind of work this is. A missing task-cost metric means observability first. Poor cache reuse means request-shape work. A large offline share means scheduling and batch. No eval means quality measurement. Tight constraints mean architecture optimization inside the current boundary.

### Know where not to optimize

Do not trade away the control boundary to save tokens. Authorization, policy, transaction checks, and required evidence still belong in normal software. Do not cache dynamic business facts without a freshness rule. Do not hide source evidence just to make context smaller. Do not use a weaker model for a high-risk decision only because its token price is lower.

The right question is not “How do we use fewer tokens?” It is “Which part of this task is creating spend without creating accepted business value?”

### Current provider examples

Provider details move quickly, so use these as implementation references rather than permanent price assumptions:

- [OpenAI Prompt Caching](https://developers.openai.com/api/docs/guides/prompt-caching) — current cache behavior, prefix rules, usage fields, and model-specific pricing notes.
- [OpenAI Batch API](https://developers.openai.com/api/docs/guides/batch) — asynchronous batch processing for work that does not need an immediate response.
- [Google Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) — examples of standard, cached-context, batch, and other service tiers.
- [Google Gemini Batch API](https://ai.google.dev/gemini-api/docs/batch-api) — asynchronous batch behavior and service-level details.

Reviewed for this section: 29 Sep 2026. Recheck current model pricing before using a percentage or unit rate in a financial estimate.

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
