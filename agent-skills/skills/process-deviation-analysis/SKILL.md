---
name: process-deviation-analysis
description: Use when a business case, document, workflow, approval, calculation, or routing completed differently from the expected path. Compare a failing case with expected or known-good behavior, identify the first divergence, inspect the decision inputs, and classify the deviation. Produces a Process Deviation Record. Do not use when the main issue is a technical outage with no process path to compare.
---

# Process Deviation Analysis

## Purpose

Find the first point where actual process behavior diverged from expected behavior and explain the decision that caused it.

## Use when

- A workflow selected the wrong branch or owner.
- A case, document, or transaction reached the wrong status or outcome.
- A calculation, determination, routing, or approval differs from a comparable case.
- Data, rules, configuration, timing, integration, or manual action may explain the difference.

## Do not use when

- The system is unavailable or failing before a process path exists. Use `evidence-driven-troubleshooting`.
- The task is to design a new process rather than diagnose an existing deviation.

## Required inputs

- Failing case and a comparable successful or expected case.
- Expected process sequence or rule.
- Actual timestamps, statuses, decisions, and system events.
- Relevant business inputs, reference data, configuration, rules, identities, and external responses.
- Recent change history.

## Workflow

1. State the expected outcome.
2. Trace the actual path from trigger to current state.
3. Build or obtain the expected or known-good path.
4. Align the paths step by step.
5. Identify the first meaningful divergence.
6. Compare inputs at that decision point.
7. Identify the rule, component, or actor that selected the next state.
8. Test whether the explanation covers both failed and successful behavior.
9. Classify the deviation as input, data, rule/configuration, code, integration timing, authorization, manual action, process design, or unknown.
10. Define correction and regression scope.
11. Validate the corrected path.

## Decision rules

- Start with the first divergence, not the final error message.
- Test input differences before assuming a platform defect.
- If the rule behaved as designed but the business result is wrong, classify it as process or rule design.
- If timing changes the result, preserve the exact sequence and dependency state.
- Preserve original evidence before manual correction.
- Regression scope must include other objects that share the same rule or condition.

## Output format

Produce a **Process Deviation Record** with expected path, actual path, first divergence, input comparison, decision mechanism, deviation class, correction, regression scope, and validation evidence.

## Quality gates

- [ ] Expected behavior is explicit.
- [ ] Actual path is reconstructed from evidence.
- [ ] First divergence is identified.
- [ ] Decision inputs are compared.
- [ ] The explanation covers failed and known-good behavior.
- [ ] Regression scope is defined.
- [ ] Validation confirms the corrected business path.

## References

- `references/method.md` — Path comparison and first-divergence method.
- `references/templates.md` — Copy-ready Process Deviation Record.
- `references/examples.md` — Workflow, pricing, routing, and status examples.

## Safety rules

- Preserve original state and evidence before manual corrections.
- Label assumptions about undocumented rules or external decisions.
- Do not expose client-identifying process data in reusable examples.
