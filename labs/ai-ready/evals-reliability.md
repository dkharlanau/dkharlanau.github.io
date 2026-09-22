---
layout: default
title: "AI Ready — Evals and Reliability"
description: "A practical guide to evaluation datasets, deterministic and model graders, retrieval evals, regression gates, revalidation, traces, latency, and cost."
permalink: /labs/ai-ready/evals-reliability/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
career_impact: mapped
career_skills: [ai-evaluation, ai-readiness]
hide_global_cta: true
tags: [ai, evals, testing, reliability, observability]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Evals and Reliability</li></ol>
</nav>

# Evals and Reliability

An AI change is not better because one answer looks better in chat. A new prompt, model, retrieval strategy, tool schema, or agent loop can improve one example and quietly damage another. Evals give us a repeatable way to decide whether behavior actually improved.

The useful idea is simple: define what good looks like, run representative cases, measure the parts that matter, and keep important failures as regression tests.

## Start with cases, not with a score

A small evaluation set is useful long before it becomes a benchmark. The first version should represent the work the system is expected to handle: ordinary cases, difficult cases, ambiguity, missing evidence, permission failures, stale data, unsafe requests, and tool failures.

Real incidents are particularly valuable. When a system fails in testing or production, that case tells us something the original dataset missed. Once fixed, it can become part of the regression set.

The goal is coverage of **decisions and failure conditions**, not a large number of nearly identical prompts. Twenty well-chosen cases can teach us more than hundreds of easy variations.

## Measure the layer that can fail

A final answer combines several components. If we reduce everything to one score, we lose the reason for the result.

| Layer | What we may evaluate |
|---|---|
| Classification | correct route or intent |
| Retrieval | expected evidence appears in the results |
| Grounding | important claims are supported by retrieved evidence |
| Tool use | correct tool, arguments, and authorization path |
| Safety | forbidden action is not executed |
| Agent loop | useful trajectory and correct stop reason |
| Output | schema validity and required fields |
| Operations | latency, cost, error rate, step count |

A fluent answer can hide weak retrieval. A correct tool result can be wrapped in poor prose. An agent can reach a correct conclusion after ten unnecessary calls. These are different problems and should be visible as different measurements.

## Use deterministic checks whenever the rule is exact

If software can check a requirement directly, let software check it.

Schema validity, expected identifiers, required source IDs, forbidden tool calls, maximum step count, exact error states, and latency budgets are good examples. These checks are cheap, repeatable, and easy to explain when they fail.

Model graders are useful for qualities that resist exact rules: whether an explanation covers the important evidence, whether a summary preserves the main limitation, or whether two pieces of prose express the same conclusion. Their criteria should still be narrow. A grader is another model-based component, so it needs its own validation and spot checks.

## Retrieval should be evaluated before generation

When the system uses RAG, first ask whether it retrieved the right evidence.

```text
question -> expected source IDs -> retrieval -> ranking / coverage check
```

Only then evaluate what the model did with the evidence:

```text
retrieved evidence -> answer -> claim / support check
```

This separation makes diagnosis faster. If the correct document never entered the context, rewriting the generation prompt may not solve the real problem.

Retrieval evaluation can also cover permission correctness, stale-version rejection, ranking quality, and the behavior when no adequate source exists.

## Agent evaluation includes the path

For an agent, the final answer is only one part of the behavior. We also care about the trajectory.

Did it choose a useful first read? Did it repeat equivalent calls? Did it stop after the evidence became sufficient? Did it escalate when uncertainty remained? Did it respect the tool boundary and request approval before a risky write?

This is where traces become part of the evaluation dataset. They show not only what the agent concluded, but how it reached that conclusion.

## Read the denominator before the percentage

Evaluation results are easy to make impressive by changing the denominator.

Suppose 100 tasks are offered, 60 are completed, 35 are accepted by a reviewer, and 32 are usable without further correction. We can describe completion as `60/100` and usable output as `32/100`. The ratio `32/60` answers a different question: usable output among completed tasks.

Both numbers can be valid. They are not interchangeable.

The same principle applies when comparing two runs. Keep the evaluation population, success criteria, observation window, and review effort comparable. If the same number of outputs becomes usable but human correction time doubles, the operating result changed even if a headline pass rate did not.

## Release gates should reflect risk

Not every metric needs a hard threshold, but some failures should block a release.

A team might decide that safety-critical cases and required schemas must have zero regressions, while retrieval, latency, and cost have agreed operating ranges. The exact thresholds depend on the application. The important point is that they are decided before the release result is known.

One global score is rarely enough. A high average can hide a single permission failure or destructive tool call.

## Revalidate the original evidence after a fix

A merged patch is not proof that a finding is resolved. The strongest verification is usually the path that originally demonstrated the problem.

```text
original failing case
 -> bounded fix
 -> rerun the failing evidence path
 -> run nearby regression cases
 -> close, revise, or reopen
```

This answers two questions separately: did we fix the original problem, and did the change break something nearby?

Keeping the original trace, test, reproduction case, or evidence record makes this process much stronger. After the fix, that artifact can become a permanent regression case.

## Keep enough version context to explain change

An evaluation result is meaningful only if we can tell what produced it. Record the dataset and case version, application version, model, instructions, retrieval configuration, tool contracts, grader version, and relevant usage or latency data.

Otherwise an eval history becomes a sequence of numbers without an explanation for why they moved.

## The practical loop

We use evals as a feedback system rather than a one-time launch gate:

```text
define expected behavior
 -> collect representative cases
 -> run the system
 -> inspect failures
 -> change one part
 -> rerun focused and regression cases
 -> add newly discovered failures
```

That loop keeps improvement tied to evidence. It also makes architecture discussions more concrete: instead of arguing that one prompt, model, or agent pattern “feels better”, we can point to the behaviors that changed and the cases that still fail.

## Further reading

- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [OpenAI Academy — Builder Bootcamp: Evals](https://academy.openai.com/public/clubs/builders-etkn1/events/builder-bootcamp-evals-rzpwt996jy)

Related: [Sample Eval Dataset](/labs/ai-ready/data/eval-sample.jsonl) · [Data and RAG](/labs/ai-ready/data-rag/) · [Production Readiness Lab](/labs/ai-ready/labs/production-readiness/)
