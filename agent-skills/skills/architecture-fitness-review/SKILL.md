---
name: architecture-fitness-review
description: Use when an enterprise architecture must be checked against current outcomes, quality attributes, dependencies, ownership, controls, operations, and accumulated drift.
---

# Architecture Fitness Review

## Purpose
Evaluate whether an existing architecture remains fit for current business and operational conditions.

## Use when
- A solution has evolved through many changes.
- Incidents, exceptions, or delivery friction suggest structural drift.
- A periodic architecture review needs evidence rather than diagram inspection.

## Do not use when
- The architecture is still only a proposal and no current-state evidence exists.
- One local defect needs troubleshooting.

## Required inputs
- Intended outcomes, architecture decisions, and quality attributes.
- Current dependency, ownership, control, and deployment information.
- Incident, metric, change, and exception evidence where available.

## Workflow
1. Recover intended architecture properties and constraints.
2. Reassess current business criticality and quality attributes.
3. Compare intended and current dependencies, data flows, ownership, and controls.
4. Review incidents, metrics, exceptions, delivery friction, and workarounds.
5. Define observable fitness checks for important architecture principles.
6. Identify structural drift and unsupported assumptions.
7. Classify findings by severity and required decision.
8. Assign actions, owners, and review triggers.

## Decision rules
- Do not score architecture from diagrams alone.
- Fitness is relative to current business conditions and NFRs.
- Repeated operational workarounds are architecture evidence.
- A principle without an observable check is difficult to govern.

## Output format
Produce an **Architecture Fitness Review** with intended properties, current evidence, fitness checks, drift findings, risk, classification, action, owner, and review trigger.

## Quality gates
- [ ] Intended properties are explicit.
- [ ] Current evidence is used.
- [ ] Operations and delivery signals are included.
- [ ] Drift is separated from intentional decisions.
- [ ] Findings have owners and next actions.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
