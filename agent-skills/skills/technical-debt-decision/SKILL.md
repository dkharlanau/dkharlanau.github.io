---
name: technical-debt-decision
description: Use when a legacy design, workaround, unsupported dependency, duplication, or structural limitation needs a business-backed decision to accept, contain, refactor, replace, or retire it.
---

# Technical Debt Decision

## Purpose
Turn vague technical-debt complaints into an evidence-based investment decision.

## Use when
- Legacy structure repeatedly slows change or operations.
- A rewrite or refactor is proposed.
- Debt competes with feature or delivery investment.

## Do not use when
- A current defect has a clear mandatory fix.
- The item is only stylistic preference with no material consequence.

## Required inputs
- Concrete debt statement and affected boundary.
- Change frequency, incident history, manual effort, and dependency evidence.
- Risk, roadmap, and available containment options.

## Workflow
1. Define the structural debt precisely.
2. Capture current cost of carry and business impact.
3. Measure change frequency and incident exposure.
4. Estimate risk of keeping versus changing it.
5. Generate options: accept, monitor, contain, refactor, replace, retire.
6. Estimate payoff horizon and dependencies.
7. Select an option using evidence and reversibility.
8. Define trigger conditions for revisiting the decision.
9. Assign owner and review date.

## Decision rules
- Age alone is not technical debt.
- A rewrite is an option, not a default remedy.
- High-change, high-risk debt deserves more attention than stable ugly code.
- Containment can be rational when replacement risk is higher than carry cost.

## Output format
Produce a **Technical Debt Decision Record** with debt statement, evidence, cost of carry, change frequency, risk, options, decision, rationale, triggers, owner, and review date.

## Quality gates
- [ ] Debt is concrete and bounded.
- [ ] Cost of carry is evidenced.
- [ ] Change frequency is considered.
- [ ] At least one containment option is considered before rewrite.
- [ ] Decision has revisit triggers.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
