---
author: "Dzmitryi Kharlanau"
layout: default
title: "Technical Debt Decision — Working Skill"
description: "Decide when technical debt should be accepted, contained, paid down, or removed based on business impact, change frequency, risk, and future cost."
permalink: /skill-hub/problem-solving-operations/technical-debt-decision-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

# Technical Debt Decision

Calling everything old "technical debt" is easy. Deciding what deserves money is the actual work.

## Working method
1. Describe the debt as a concrete structural limitation, workaround, unsupported dependency, duplication, or complexity source.
2. Explain the business or delivery impact it creates now.
3. Measure frequency: how often does this area change, fail, slow delivery, create manual work, or block architecture choices?
4. Estimate risk of keeping it and risk of changing it.
5. Identify containment options, not only full rewrite.
6. Estimate payoff horizon and dependencies.
7. Decide: accept, monitor, contain, refactor, replace, or retire.
8. Define trigger conditions that change the decision.
9. Record owner and evidence for future review.

## Output
A **Technical Debt Decision Record** contains debt statement, evidence, cost of carry, change frequency, risk, options, decision, trigger conditions, owner, and review date.

## Lead signal
A Lead can defend why some debt stays. Architecture maturity is not measured by the number of rewrites approved.
