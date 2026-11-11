---
layout: default
title: "Your Old Prompts May Be Slowing Down New Models"
description: "Practical AI Engineer lesson: prompt hygiene, cache-friendly context, train-test evals. Includes source limitations, SAP decisions and measurable exercises."
permalink: /labs/ai-ready/video-lessons/modern-prompts-and-eval-hillclimbing/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [ai-evaluation, ai-agents-mcp, ai-business-value]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# Your Old Prompts May Be Slowing Down New Models

Some prompt libraries carry instructions written for models from several generations ago: "think step by step", "double-check everything", "be maximally thorough", sometimes all in the same template. They sound responsible, but they can cause unnecessary work or conflict with newer models' built-in behavior.

Lance Martin (Anthropic) explores this in [Your Old Prompts Are Making Claude Worse](https://aietalks.com/talks/your-old-prompts-are-making-claude-worse), a November 2026 workshop. These are **model- and workload-dependent observations**, not a rule that reasoning instructions are always harmful.

## Treat prompts as versioned software

A production prompt has a release version, dependencies, known test cases and rollback. It is not a magical paragraph that should grow forever.

| Prompt debt | Typical symptom | Safer revision |
| --- | --- | --- |
| Old "thinking booster" language | Extra output, wasted tokens | Define the actual output contract; test whether the booster helps |
| Conflicting instructions | Inconsistent classification | Resolve ownership and priority |
| Long repeated background | Increasing cost and latency | Move reusable knowledge into retrievable sources; cache stable context |
| Undefined terms | Agent invents definitions | Supply a short glossary and examples |
| Huge exception list | Agent follows wrong exception | Prefer deterministic rule tables for exact logic |
| No abstain state | Confident guesses | Add insufficient-evidence and tool-failure states |

Don't optimize merely by shortening the text. Remove only instructions proven redundant or harmful on an evaluation set.

## A precise SAP exercise: classify a data issue

Old prompt:

> You are a perfect SAP expert. Think very carefully, check everything many times, do not make mistakes, always fix the issue.

This invites overclaiming and suggests writes are acceptable. A better *task contract* says:

> Given an order snapshot, a master-data snapshot and an interface trace, return the most likely failure category with evidence references. Choose from DATA, CONFIGURATION, INTEGRATION or UNKNOWN. Never change the system. If evidence is missing, return UNKNOWN and name the next read.

The second prompt defines inputs, output and a hard boundary. **Real access control must still be enforced by the application**, not by this text.

## Split your evaluation before optimizing

The talk describes iterative "hill climbing": the model inspects failing examples, proposes revisions and tries again. Without an independent test set, a prompt can memorize the training cases and look better without improving production.

Use three sets:

- **Train (development):** 30 synthetic incidents used to decide what to change.
- **Holdout (unseen):** 15 independent cases shown only to the evaluator after each revision.
- **Safety:** 10 adversarial cases (injected instructions, stale timestamps, missing authority, unknown tool status).

Track category accuracy, evidence quality, unsupported writes, token usage, and latency. After each revision show the *difference on the holdout*, not just the new training score. If train increases while holdout stalls, stop optimizing for that benchmark.

## Make cache-aware context observable

Keep reusable instructions and tool definitions stable. Put case-specific observations late. Then inspect real provider cache-hit telemetry and task economics. A claimed reduction is meaningless if no actual cache was used.

**Practical 50-minute lab:** Compare three prompt versions with the same model and cases. Change only one hypothesis at a time: remove a verbose instruction, reorganize the stable prefix, and shorten retrieved evidence. Record exact prompt hash, model configuration, dataset version, run time and result.

**Architect challenge:** A prompt version wins 45/45 visible training cases but loses four important production examples. Would you release it? Explain train/holdout split, risk weighting and rollback.

Related: [Prompt and Context](/labs/ai-ready/engineering/prompt-context/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [Source transcript](https://ainotes.us/summary/your-old-prompts-are-making-claude-worse-lance-martin-anthropic).

**Source boundary:** Model-specific findings and reported optimization effects are attributed to the speaker. The training sets and prompts are illustrative, not a measured SAP benchmark.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
