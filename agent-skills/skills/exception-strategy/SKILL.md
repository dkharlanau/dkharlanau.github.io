---
name: exception-strategy
description: Use when an enterprise process, integration, migration, or automation needs explicit handling for expected failures, partial outcomes, retries, holds, corrections, and escalation.
---

# Exception Strategy

## Purpose
Design controlled behavior for expected exceptions instead of leaving them as ad hoc support work.

## Use when
- A process has retries, holds, corrections, rejections, or partial completion.
- An integration needs error, retry, or compensation rules.
- A migration or cutover needs controlled exception handling.

## Do not use when
- The task is to diagnose one unknown incident.
- The exception is already fully defined by a mandatory policy and only implementation is needed.

## Required inputs
- Normal path and completion state.
- Known failure and exception classes.
- Business criticality, ownership, retry safety, and evidence sources.

## Workflow
1. Define the happy path and completion state.
2. Enumerate expected exception classes.
3. Separate expected exceptions from unknown failures.
4. Define detection evidence and classification rules.
5. Select response: reject, hold, retry, compensate, reroute, correct, approve, or escalate.
6. Define owner and authority for each response.
7. Define idempotency before automatic retry.
8. Define retry, wait, and escalation limits.
9. Define reconciliation for uncertain or partial outcomes.
10. Route recurring exceptions into improvement work.

## Decision rules
- Do not automatically retry non-idempotent actions without duplicate protection.
- A retry limit without escalation only creates delayed failure.
- Partial completion requires reconciliation or compensation.
- Expected business rejection is not the same as technical failure.

## Output format
Produce an **Exception Strategy Record** with class, trigger, evidence, response, owner, authority, retry/compensation rules, escalation, and closure criteria.

## Quality gates
- [ ] Happy path completion is defined.
- [ ] Important exception classes are explicit.
- [ ] Retry safety is addressed.
- [ ] Partial outcomes have reconciliation or compensation.
- [ ] Every class has ownership and closure criteria.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
