---
layout: default
title: "AI Ready — Practical Use Cases"
description: "A practical map from real work to AI architecture: research, knowledge, coding, data analysis, automation, and agents."
permalink: /labs/ai-ready/use-cases/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
hide_global_cta: true
tags: [ai, use-cases, research, coding, rag, automation, agents]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li aria-current="page">Use Cases</li></ol>
</nav>

# Practical AI Use Cases

A useful AI design starts with the work, not with the technology label. “We need an agent” tells us almost nothing. We first need to understand what must be correct, what is uncertain, where the facts live, and whether the system is only explaining or may also act.

Once those questions are clear, the architecture often becomes much simpler.

## Research: find evidence before asking for synthesis {#research}

Research work combines two different jobs: finding relevant material and making sense of it. The model is usually more reliable when those jobs remain visible in the architecture.

```text
question -> search / retrieval -> selected evidence -> synthesis -> references
```

The retrieval layer should bring back material we can identify and inspect. The model can then compare sources, explain disagreements, and produce a readable answer. If several research threads are independent, they may run in parallel, but parallelism is useful only when the outputs can be merged under a clear question.

A common weak design is to send a large document pile to the model and call the result “research”. Volume is not coverage. We still need to know which sources were relevant, which claims are supported, and what evidence is missing.

## Knowledge assistants: distinguish documents from current facts {#knowledge}

A knowledge assistant often works with policies, product documentation, support notes, project records, or internal guidance. Retrieval helps when the answer depends on passages spread across changing documents.

We normally want stable source identifiers, document versions, permission-aware retrieval, and an explicit way to say that the evidence is insufficient. Retrieval quality should be tested separately from writing quality: a fluent answer cannot compensate for missing the correct source.

Not every “knowledge” question belongs in RAG. If the user asks for the current ticket status, inventory quantity, account balance, or deployment state, a direct read from the owning system is usually better. Structured facts should come from structured sources when possible.

## Coding: let the model explore, let engineering tools judge {#coding}

Coding work suits models because repositories are messy and the path from a task to the relevant files is often uncertain. A good coding loop may look like this:

```text
read repository
 -> find the relevant code
 -> form a change hypothesis
 -> prepare the patch
 -> run tests and static checks
 -> inspect failures
 -> revise or publish through controlled tools
```

The model helps navigate, explain, and propose. Compilers, tests, type checkers, linters, scanners, and CI remain stronger judges for conditions that software can verify exactly.

Write access should also match the task. A coding assistant that edits one repository does not need every repository, deployment credential, and secret in the organization. Wider access is not a sign of a more capable agent; it is a wider failure boundary.

For a more detailed workflow, see the [Coding Agents Playbook](/labs/ai-ready/coding-agents/).

## Data analysis: keep arithmetic executable {#data}

Natural language is useful at the start and end of analysis. The middle should be as deterministic as the problem allows.

```text
question
 -> define metric and dimensions
 -> inspect schema and data
 -> generate SQL / Python
 -> execute
 -> validate the result
 -> explain or visualize
```

The model can help translate an ambiguous business question into an analysis plan, but SQL, Python, a calculator, or a business-rules service should perform exact calculations. This also makes review easier: we can inspect the query, the data range, the joins, and the units instead of trusting arithmetic hidden inside prose.

Many analysis errors come from definitions rather than mathematics. “Revenue”, “active customer”, or “late delivery” can mean different things across systems. Clarifying the metric is part of the analysis, not a preliminary inconvenience.

## Automation: use the model inside a known process {#automation}

A large class of useful AI work is still ordinary workflow automation with one or two uncertain steps.

```text
trigger -> interpret -> retrieve -> draft -> validate -> send or prepare action
```

Examples include routing support tickets, extracting fields from documents, preparing CRM updates, drafting an issue from an incident report, or comparing an incoming request with a policy.

The trigger, authorization, validation, and business rules can remain deterministic. The model handles the parts that are difficult to express as exact rules, such as interpreting free text or producing a useful draft.

Typed tools make external reads and writes explicit. MCP can become relevant when several AI clients need the same governed capabilities, but a single workflow does not need a protocol layer just to call one backend.

## Agents: use them when discovery changes the path {#agents}

An agent becomes useful when the next sensible action depends on what the system finds.

Suppose the question is “Why did deployment X fail?”. The system may inspect deployment status first. A failed job may point to a dependency. Another case may point to a configuration change. We cannot always know the correct sequence before reading the first result.

That is a genuine agent problem:

```text
question
 -> choose an allowed read
 -> inspect evidence
 -> choose the next useful read
 -> stop with a supported conclusion
    or escalate when evidence is not enough
```

The flexibility belongs inside clear boundaries: allowed tools, data scope, time and cost budgets, explicit stop reasons, traceability, and approval before high-impact actions.

If one fixed workflow already expresses the process, an agent usually adds complexity without adding useful freedom.

## Content work is often simpler than it looks

Drafting, rewriting, translation, classification, extraction, and summarization usually do not require an agent. A model call, a clear instruction, and structured output may be enough.

Retrieval becomes useful when the content must reflect external or private facts. Tools become useful when the system must read or change another application. An agent becomes useful only when the path itself needs to adapt.

This progression matters because it keeps the design proportional to the problem.

## Choose the smallest useful shape

| Need | Good starting point |
|---|---|
| Rewrite, classify, extract | Prompt + structured output |
| Changing document knowledge | Retrieval |
| Current structured fact | Read tool / API |
| Repeatable sequence | Workflow |
| Several known routes | Router |
| Next step depends on evidence | Bounded agent |
| Shared capabilities across AI clients | MCP candidate |
| High-impact write | Prepared change + approval |

We can add complexity later when evaluation shows a real gap. It is much harder to understand a system that started with every mechanism at once.

A practical build sequence is therefore simple: collect representative cases, build the smallest path that can solve them, validate what can be checked deterministically, and study the failures. Retrieval, tools, orchestration, and agent loops should answer observed needs rather than architecture fashion.

## Further reading

- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

Related: [System Boundaries](/labs/ai-ready/system-boundaries/) · [Deep Dives](/labs/ai-ready/deep-dives/) · [Hands-on Labs](/labs/ai-ready/#labs)
