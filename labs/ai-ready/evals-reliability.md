---
layout: default
title: "AI Ready — Evals and Reliability"
description: "A practical guide to golden datasets, deterministic and model graders, retrieval evals, regression gates, traces, latency, and cost."
permalink: /labs/ai-ready/evals-reliability/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-19
hide_global_cta: true
tags: [ai, evals, testing, reliability, observability]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Evals and Reliability</li></ol>
</nav>

# Evals and Reliability

An AI change is not better because one answer looks better in chat. Prompts, models, retrieval, tool schemas, and agent logic need regression tests. Evals turn “I think this is better” into evidence.

## Problem

AI systems can regress silently when prompts, models, retrieval, tools, or policies change without repeatable tests.

## Build the dataset before tuning the system

Keep a small golden set early. It should contain real decision shapes, not only friendly examples.

Include:

- common easy cases;
- hard cases;
- ambiguous cases;
- no-answer cases;
- permission failures;
- stale or conflicting data;
- unsafe requests;
- tool failures;
- cases that broke in production or testing.

A dataset of 30 useful cases can teach more than 3,000 synthetic questions that all test the same happy path.

## Separate what you measure

| Layer | Example metric |
|---|---|
| Classification | correct route / intent |
| Retrieval | expected source in top K |
| Grounding | claims supported by evidence |
| Tool use | correct tool and arguments |
| Safety | forbidden action not executed |
| Agent loop | correct stop reason, no repeated calls |
| Output | schema validity, required fields |
| Operations | latency, cost, error rate |

A good final answer can hide bad retrieval, and weak prose can hide a correct tool result. Measure layers separately.

## Use deterministic graders first

If code can check the requirement, use code.

Good deterministic checks:

- JSON schema valid;
- expected ID matches;
- required source ID present;
- forbidden tool not called;
- maximum step count respected;
- expected error state returned;
- latency below budget.

Use a model grader for qualities that are hard to express as exact rules, such as explanation completeness or whether a summary preserves important evidence. Keep model-grader criteria narrow and test the grader itself.

## Retrieval evals

Test retrieval before generation:

```text
question -> expected source IDs -> retrieval -> ranking check
```

Useful measures include recall at K, ranking position, permission correctness, stale-version rejection, and no-result behavior.

Then test grounded generation:

```text
retrieved evidence -> answer -> claim/support check
```

## Tool and agent evals

For tools, check selection, arguments, authorization path, output validation, and retries.

For agents, also check the trajectory:

- Did it choose a useful first read?
- Did it repeat equivalent calls?
- Did it stop when evidence was enough?
- Did it escalate when evidence was weak?
- Did it request approval before a risky write?

The final sentence is only one part of agent quality.

## Regression gate

A practical release rule can be simple:

```text
critical safety regressions = 0
schema pass rate = 100%
retrieval recall >= agreed threshold
critical use cases = 100%
p95 latency <= budget
cost/request <= budget
```

Do not chase one global score. Some cases should be hard gates.

## Revalidate after remediation

A proposed fix is not the end of the finding lifecycle. After remediation, rerun the narrowest test or evidence path that originally demonstrated the problem.

Use this sequence:

```text
original finding
-> bounded fix
-> focused verification
-> revalidate original evidence path
-> regression check
-> close, revise, or reopen
```

Revalidation should answer two different questions:

1. Is the original finding actually addressed?
2. Did the fix introduce a regression, move the failure to another path, or weaken a nearby control?

Keep the original reproduction case, trace, failing test, scanner evidence, or approved runtime proof when possible. It becomes the strongest starting point for revalidation and should usually become a regression case after the issue is fixed.

Do not mark a finding resolved only because the patch merged or the implementation looks plausible. The evidence that justified the finding should also provide the basis for closing it.

## Trace every evaluated run

Store enough information to explain why the result changed:

- dataset and case version;
- application version;
- model version;
- prompt/instruction version;
- retrieval configuration;
- tool schema version;
- tool results or stable evidence IDs;
- grader version;
- latency and usage;
- final decision.

Without version context, an eval history becomes a spreadsheet of unexplained numbers, humanity’s favorite form of confidence.

## Practical golden set

For a deployment-investigation assistant, include cases such as:

- obvious build failure;
- dependency timeout;
- configuration mismatch;
- permission denied while reading logs;
- two simultaneous causes;
- stale runbook page;
- no evidence for a safe conclusion;
- a tool timeout during investigation;
- hostile instructions inside a log or retrieved page;
- proposed rollback without enough evidence.

Expected output is not only the root cause. It can include required evidence, allowed tools, forbidden actions, and the correct stop state.

## Failure modes

- Testing only one prompt by hand.
- Using only synthetic easy questions.
- A model grader judges exact facts that code could check.
- Retrieval changes without retrieval evals.
- Production failure never becomes a regression case.
- Dataset is edited without version history.
- Average score hides a critical failure.
- A finding is closed because a patch merged, without revalidating the original evidence path.

## Build checklist

1. Define the decisions that matter.
2. Create golden cases before optimization.
3. Add deterministic checks wherever possible.
4. Evaluate retrieval and generation separately.
5. Test tool trajectories and stop reasons.
6. Keep critical cases as release gates.
7. Revalidate the original finding after remediation.
8. Add fixed failures back into the regression dataset.
9. Track quality, latency, and cost together.

Related: [Sample Eval Dataset](/labs/ai-ready/data/eval-sample.jsonl) · [Data and RAG](/labs/ai-ready/data-rag/) · [Production Readiness Lab](/labs/ai-ready/labs/production-readiness/)
