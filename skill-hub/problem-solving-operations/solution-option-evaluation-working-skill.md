---
author: "Dzmitryi Kharlanau"
layout: default
title: "Solution Option Evaluation — Working Skill"
description: "Compare materially different solution options against outcomes, constraints, quality attributes, risk, reversibility, and operating cost before selecting a direction."
permalink: /skill-hub/problem-solving-operations/solution-option-evaluation-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

# Solution Option Evaluation

A Lead should not turn the first plausible idea into the architecture. The job is to make the choice visible.

## When to use it
Use this skill when a team has several technical or process directions, when a vendor is being selected too early, or when a proposal sounds attractive but its trade-offs are still hidden.

## Working method
1. State the business outcome and the decision to make.
2. Separate hard constraints from preferences and assumptions.
3. Define evaluation criteria before scoring options: capability fit, data fit, integration fit, security, operability, resilience, cost, delivery effort, reversibility, and organizational fit.
4. Create materially different options. Two products implementing the same system shape are not two architectures.
5. Record benefits, disadvantages, dependencies, failure modes, migration impact, and operational tax for every option.
6. Use evidence where possible. Mark estimates and assumptions explicitly.
7. Identify irreversible or expensive commitments.
8. Compare options with weighted criteria only when the weights are justified.
9. Record the preferred option, rejected options, decision owner, evidence gaps, and conditions that could reverse the decision.

## Decision rules
Do not hide a veto condition inside a weighted score. A legal, security, or mandatory business constraint can disqualify an option regardless of its average score. Avoid false precision: a score of 4.2 is not knowledge if the evidence is weak.

## Output
The result is a **Solution Option Evaluation Record** with decision context, criteria, options, evidence, trade-offs, recommendation, confidence, and reversal triggers.

## Lead signal
A strong answer explains why an option wins, what it costs, what risk remains, and what would make the team reconsider. A weak answer names a technology and then invents reasons after the fact.

## Related skills
- [Non-Functional Requirements](/skill-hub/problem-solving-operations/non-functional-requirements-working-skill/)
- [Decision Facilitation](/skill-hub/problem-solving-operations/decision-facilitation-working-skill/)
- [Architecture Decision Record](/skill-hub/architecture/architecture-decision-record-working-skill/)
- [Failure Mode / Resilience Review](/skill-hub/problem-solving-operations/failure-mode-resilience-review-working-skill/)
