---
name: release-readiness
description: Use before a production release, deployment, configuration change, data load, model update, or integration change when a go/no-go decision must be based on scope, risk, evidence, dependencies, execution, rollback or recovery, monitoring, ownership, and business readiness. Produces a Release Readiness Record. Do not use for detailed solution design or post-incident root cause analysis.
---

# Release Readiness

## Purpose

Decide whether a production change is ready using evidence for the important risks, clear dependencies and owners, an executable recovery path, and planned production validation.

## Use when

- A release, deployment, transport, configuration change, data load, integration change, or model update approaches production.
- Several teams own parts of one release and the final readiness view is fragmented.
- Tests passed but production dependencies, monitoring, rollback, or business readiness remain unclear.
- A high-risk change needs an explicit go/no-go record.

## Do not use when

- You are still designing the solution.
- The change has already failed and needs root cause analysis.
- You need only detailed test case design. Use testing skills.

## Required inputs

- Release scope and change list.
- Risk and impact assessment.
- Test evidence and unresolved defects.
- Dependencies and owners.
- Deployment sequence, window, and access needs.
- Rollback or forward-recovery approach.
- Monitoring, support, and business communication plan.

## Workflow

1. Freeze the decision scope: included, excluded, and still changing.
2. Classify risk using business criticality, data mutation, integration reach, security, reversibility, user volume, timing, and novelty.
3. Map each important risk to test evidence, review evidence, preventive control, monitoring, or explicit acceptance.
4. Review unresolved defects and classify each as blocker, accepted risk, known limitation, or cosmetic issue.
5. Validate dependencies: versions, configuration, credentials, data, endpoints, jobs, feature flags, infrastructure, and external teams.
6. Validate production execution: sequence, owner per step, timing, access, automation, checkpoints, and stop conditions.
7. Validate rollback or forward recovery, including decision owner and technical feasibility.
8. Define production signals that prove technical and business success.
9. Confirm business readiness, support coverage, communications, and accountable acceptance where needed.
10. Run go/no-go review and record decision, conditions, exceptions, owners, and evidence gaps.
11. After release, execute the planned validation and keep the release open until required signals are stable.

## Decision rules

- No rollback does not automatically mean no-go, but it requires an explicit recovery strategy and stronger evidence.
- A passed test is weak evidence when environment, data, or dependencies do not represent the relevant production risk.
- An unresolved defect is acceptable only when impact, workaround, owner, and acceptance are explicit.
- If a critical dependency has no confirmed owner or state, readiness is not proven.
- If monitoring cannot detect a major failure mode, add a control before release or define a manual validation.
- A conditional go must list the condition and accountable owner; do not hide it behind a green status.

## Output format

Produce a **Release Readiness Record**:

```markdown
## Release identity
Release / change:
Environment:
Window:
Decision owner:

## Scope
Included:
Excluded:
Still changing:

## Risk and evidence
| Risk | Level | Evidence / control | Status | Owner |
|---|---|---|---|---|

## Unresolved defects
| Defect | Impact | Classification | Workaround | Owner |
|---|---|---|---|---|

## Dependencies
| Dependency | Required state | Confirmed state | Owner |
|---|---|---|---|

## Execution
Sequence:
Checkpoints:
Stop conditions:

## Rollback / recovery
Trigger:
Method:
Decision owner:
Feasibility evidence:

## Production validation
| Signal | Expected | Owner | Time window |
|---|---|---|---|

## Business readiness

## Decision
GO | CONDITIONAL GO | NO-GO
Conditions / reasons:

## Post-release result
```

## Quality gates

- [ ] Scope is stable enough for a meaningful decision.
- [ ] Critical risks have evidence, control, or explicit acceptance.
- [ ] Unresolved defects are classified with impact and owner.
- [ ] Critical dependencies have confirmed state and owner.
- [ ] Rollback or recovery is technically executable.
- [ ] Production validation signals exist before release.
- [ ] Decision conditions and owners are explicit.

## References

- `references/method.md` — Risk-to-evidence and go/no-go model.
- `references/templates.md` — Readiness record and compact decision table.
- `references/examples.md` — Synthetic integration, data-load, UI, and high-risk release cases.
