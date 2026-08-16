---
name: solution-option-evaluation
description: Use when several enterprise solution directions must be compared before a decision. Evaluates materially different options against outcomes, constraints, quality attributes, evidence, risk, reversibility, and operating cost.
---

# Solution Option Evaluation

## Purpose
Compare real solution alternatives before a technology or design direction becomes fixed.

## Use when
- Several architectures, products, process shapes, or delivery approaches are possible.
- A team is converging on a preferred solution without explicit trade-offs.
- A Lead decision needs evidence and reversal conditions.

## Do not use when
- One option is already mandated by a non-negotiable policy or contract.
- The problem is an incident with a known cause and correction.

## Required inputs
- Business outcome and decision statement.
- Constraints, assumptions, evidence, and stakeholders.
- Candidate options or enough context to generate them.
- Relevant quality attributes and operating constraints.

## Workflow
1. Frame the decision and useful outcome.
2. Separate hard constraints, preferences, and assumptions.
3. Define evaluation criteria before comparing options.
4. Produce materially different options when evidence allows choice.
5. Record benefits, complexity tax, dependencies, failure modes, migration impact, and operating cost.
6. Mark evidence, estimate, assumption, and unknown separately.
7. Identify irreversible commitments and reversal cost.
8. Compare options without hiding veto conditions in averages.
9. Recommend only when evidence supports a preference.
10. Record rejected options and reversal triggers.

## Decision rules
- Different vendors with the same system shape are not different options.
- Hard constraints can disqualify an option regardless of weighted score.
- Do not use numeric precision beyond the evidence quality.
- Prefer reversible choices when value is similar and uncertainty is high.

## Output format
Produce a **Solution Option Evaluation Record** with: decision, outcome, constraints, criteria, option matrix, evidence confidence, trade-offs, recommendation, rejected options, risks, owner, and reversal triggers.

## Quality gates
- [ ] At least two materially different options exist when choice is real.
- [ ] Criteria were defined before final scoring.
- [ ] Hard constraints are explicit.
- [ ] Evidence and assumptions are separated.
- [ ] Operating cost and reversibility are considered.
- [ ] Recommendation has reversal conditions.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
