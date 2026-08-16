---
name: cutover-hypercare-control
description: Use when a production go-live needs coordinated technical and business cutover steps, checkpoints, stop decisions, recovery, validation, incident routing, and measurable stabilization after go-live. Produces a Cutover & Hypercare Control Record. Do not use when release readiness has not yet been decided or for routine low-risk deployment without coordinated transition work.
---

# Cutover & Hypercare Control

## Purpose

Control a production transition using explicit states, dependencies, evidence, checkpoints, stop conditions, recovery decisions, business validation, and measurable hypercare exit criteria.

## Use when

- A go-live has coordinated technical and business activities.
- Data, interfaces, jobs, configuration, deployments, users, or external partners must switch in sequence.
- A high-impact release needs command-and-control checkpoints.
- Hypercare needs structured stabilization and exit criteria.

## Do not use when

- Release readiness has not been established. Use `release-readiness` first.
- The deployment is low-risk and does not need coordinated cutover control.
- A post-go-live incident already needs detailed diagnosis. Route it to the relevant diagnostic skill.

## Required inputs

- Approved release scope and readiness decision.
- Cutover activities, dependencies, owners, planned windows, and access needs.
- Rollback or forward-recovery strategy.
- Critical technical and business validation scenarios.
- Monitoring signals, incident routing, escalation contacts, and decision authority.

## Workflow

1. Define transition states: pre-cutover, freeze, execution, technical validation, business validation, open-for-business, stabilization, and closure.
2. Build dependencies, parallel work, external dependencies, and critical path.
3. Define completion evidence for each critical activity.
4. Define checkpoints and the authority to continue, hold, rollback, or forward-recover.
5. Define measurable stop conditions.
6. During execution, record actual start/end, evidence, deviations, owner, and decisions.
7. Run technical validation for deployments, interfaces, jobs, queues, data controls, errors, and platform signals as relevant.
8. Run the minimum critical business scenarios that prove operations can continue.
9. Enter hypercare with structured incident routing, impact, workaround, owner, and permanent-action tracking.
10. Monitor stabilization using error, backlog, throughput, data-quality, business-flow, and unresolved-defect signals.
11. Exit hypercare only when agreed stability criteria and knowledge handover are met.
12. Convert recurring recovery into runbooks and material recurring issues into RCA or backlog actions.

## Decision rules

- Do not mark a critical step complete without evidence.
- A delay matters when it affects the critical path or decision window, not simply because a timestamp moved.
- If a stop condition is met, record an explicit continue, hold, rollback, or forward-recovery decision.
- Hypercare should reduce as stability improves; it is not a permanent support model.
- Do not exit hypercare while recurring high-impact incidents lack owner and permanent action.

## Output format

Produce a **Cutover & Hypercare Control Record**:

```markdown
## Transition
Release:
Window:
Command owner:
Current state:

## Critical path
| Step | Dependency | Owner | Planned | Actual | Evidence | Status |
|---|---|---|---|---|---|---|

## Checkpoints
| Checkpoint | Continue criteria | Stop criteria | Decision owner | Decision |
|---|---|---|---|---|

## Recovery
Rollback / forward recovery:
Trigger:
Owner:

## Technical validation

## Business validation

## Hypercare incidents
| Pattern / issue | Impact | Workaround | Owner | Permanent action |
|---|---|---|---|---|

## Stabilization signals
| Signal | Exit threshold | Actual | Trend |
|---|---|---|---|

## Hypercare exit
Decision:
Open risks:
Handover owner:
```

## Quality gates

- [ ] Critical steps have dependencies, owners, evidence, and status.
- [ ] Checkpoints have measurable continue and stop criteria.
- [ ] Recovery decision authority is explicit.
- [ ] Technical and business validation both exist.
- [ ] Actual execution state is recorded.
- [ ] Hypercare has measurable exit criteria.
- [ ] Recurring issues have permanent follow-up.

## References

- `references/method.md` — Transition-state, checkpoint, and stabilization model.
- `references/templates.md` — Cutover control and hypercare templates.
- `references/examples.md` — Synthetic data, integration, checkpoint, and stabilization cases.
