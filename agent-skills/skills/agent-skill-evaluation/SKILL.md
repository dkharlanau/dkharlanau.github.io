---
name: agent-skill-evaluation
description: Use when creating, trimming, retiring, or retesting a SKILL.md package after a model, runtime, tool contract, or team procedure changes. Compare routing and task outcomes with controlled runs and record a keep, revise, retire, or retest decision.
---

# Agent Skill Evaluation

## Purpose

Measure which behavior a specific agent skill contributes on the model and runtime where it will be used.

## Use when

Evaluate a new skill's discovery and task performance, simplify an existing skill, or check whether a runtime upgrade made instructions redundant.

## Do not use when

The work is general agent release testing or evaluation of a person's professional capability.

## Required inputs

Identify the skill or proposed procedure, target model and runtime, intended user requests, observable outputs, and any exact rules the procedure must preserve. Use public, synthetic, or otherwise authorized test data.

## Workflow

1. Write outcome checks before running the agent. Include intended trigger cases, nearby requests that should avoid the skill, one expected failure, and a held-out case. Link checks to artifacts or tool receipts where possible.
2. For a skill-effect test, compare a normal run with the skill available against a run where it is absent. For an instruction edit, also compare the original and revised packages. Keep fixtures, permissions, settings, and tools equivalent across each pair. Start fresh sessions and repeat when behavior varies.
3. Score routing independently of task completion. Where the runtime cannot show whether it loaded the skill, record routing as unobservable. If discovery fails and you need to diagnose the body, run a separate explicitly loaded diagnostic.
4. Preserve the case-level results, exact versions, and costs when reported. Compare critical and held-out cases before aggregate pass rates.
5. Record a decision and its next review trigger. If the requested runtime cannot execute the comparison, deliver the case plan and report the run as pending.

## Decision rules

- **Keep** a skill when it protects a required workflow or shows a useful outcome improvement at acceptable cost.
- **Revise** a skill when routing, redundancy, or a regression has a specific fix. Rerun the original and revised packages before adopting the edit.
- **Retire** a skill from a tested environment when the baseline meets the agreed outcome and critical checks without it. Preserve the regression cases and retest after relevant changes.
- **Retest** when the sample is too noisy, the variants changed more than one factor, or observation is incomplete.

## Output format

Produce an **Agent Skill Evaluation Record** with the scope, versions, case results, critical failures, comparison limits, decision, and next review trigger. The template below accepts planned and observed runs.

## Quality gates

Review expected outcomes before runs, keep grading keys and held-out cases outside the agent's workspace, and verify external effects using trusted records. Follow normal authorization and environment controls for all test tools.

## References

- [Method](references/method.md) for designing a controlled comparison.
- [Record template](references/templates.md) for handing off results.
- [Synthetic examples](references/examples.md) for drafting cases and reading the outcome.
