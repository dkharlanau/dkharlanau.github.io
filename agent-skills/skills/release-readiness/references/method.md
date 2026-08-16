# Release Readiness Method

## Risk-to-evidence model

A readiness decision should connect each material risk to one or more controls:

- test evidence
- review evidence
- preventive control
- production monitoring
- rollback or recovery
- explicit risk acceptance

A green status without this link is decoration.

## Risk dimensions

Assess at least:

- business criticality
- data mutation and reversibility
- integration reach
- security and authorization impact
- number of users or transactions
- timing sensitivity
- operational novelty
- dependency count
- rollback complexity

The goal is not a perfect numeric score. The goal is to decide where stronger evidence is required.

## Evidence strength

Stronger evidence is closer to production reality:

1. claim or assumption
2. design review
3. unit or local test
4. integrated test
5. representative end-to-end test
6. rehearsal or production-like validation
7. controlled production signal after release

Use the level appropriate to the risk. Do not demand expensive rehearsal for a low-risk reversible text change, and do not accept a screenshot as proof for a high-risk data conversion.

## Decision states

### GO

Critical evidence exists, dependencies are confirmed, recovery is usable, and no blocker remains.

### CONDITIONAL GO

A limited gap remains but the condition, owner, deadline or checkpoint, and risk are explicit.

### NO-GO

A blocker exists, critical evidence is missing, recovery is not credible for the risk, or a critical dependency is unknown.

## Post-release closure

Do not close the release at technical deployment completion. Validate planned technical and business signals for the defined observation window.
