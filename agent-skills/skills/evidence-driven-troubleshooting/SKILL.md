---
name: evidence-driven-troubleshooting
description: Use when a technical or operational failure is reproducible but the responsible layer is unclear. Follow evidence from trigger to result, compare failing and known-good cases, test rejectable hypotheses, and isolate the first failing layer before changing the system. Produces an Evidence-Driven Troubleshooting Record. Do not use when the root cause is already known or when only a routine procedure must be executed.
---

# Evidence-Driven Troubleshooting

## Purpose

Isolate the first failing layer with evidence before proposing a fix.

## Use when

- A user, service, batch, API, file flow, or application behaves unexpectedly.
- The failure crosses several components and ownership is unclear.
- A recent change may be related but has not been proven causal.
- Teams are trying fixes without a stable evidence set.

## Do not use when

- The cause is already known and only correction is required.
- The task is a stable repeated procedure. Use `procedure-design` or the approved runbook.
- The main question is whether two datasets reconcile. Use `data-reconciliation`.

## Required inputs

- Observed and expected behavior.
- Timestamp, environment, identity, and affected object or request.
- Failing example and known-good comparison when available.
- Recent change history.
- Access to relevant evidence sources such as logs, traces, monitoring, data, queues, configuration, or platform telemetry.

## Workflow

1. Write a testable symptom statement.
2. Reproduce or independently verify the failure.
3. Capture evidence before material changes.
4. Map the path from trigger to business result.
5. Compare failing and known-good paths.
6. Identify the first meaningful divergence.
7. Create small hypotheses with tests that can reject them.
8. Test one meaningful variable at a time and record results.
9. Isolate the failing layer and responsible boundary.
10. Choose the smallest safe and reversible action.
11. Validate the result end to end.
12. Route to RCA, change analysis, reconciliation, monitoring improvement, or procedure design when needed.

## Decision rules

- If the symptom cannot be reproduced, gather more evidence before assigning a cause.
- Treat a recent change as a hypothesis, not proof.
- Prefer the earliest divergence between failing and known-good cases.
- Do not retry when duplicate creation, financial impact, or inconsistent state is possible and recovery behavior is unknown.
- Preserve correlation IDs and evidence on both sides of a system boundary.
- If analysis is handed off, include rejected hypotheses and missing evidence.

## Output format

Produce an **Evidence-Driven Troubleshooting Record** with:

- Symptom and expected result.
- Scope and timeline.
- System or process path.
- Evidence captured before changes.
- Known-good comparison.
- Hypotheses, tests, and results.
- First failing layer.
- Containment or fix.
- Risk and rollback.
- End-to-end validation.
- Next skill or owner.

## Quality gates

- [ ] The symptom is testable.
- [ ] Evidence was captured before material changes.
- [ ] A known-good comparison was used when available.
- [ ] Hypotheses can be rejected by evidence.
- [ ] At least one hypothesis was explicitly rejected or ruled out.
- [ ] The isolated layer explains the evidence.
- [ ] Validation checks the business result, not only technical status.

## References

- `references/method.md` — Layer isolation and hypothesis method.
- `references/templates.md` — Copy-ready troubleshooting record.
- `references/examples.md` — Cross-domain examples.

## Safety rules

- Separate facts from assumptions.
- Do not perform destructive, irreversible, or high-impact actions without an explicit approval boundary.
- Redact credentials, secrets, personal data, and client-identifying details from evidence.
