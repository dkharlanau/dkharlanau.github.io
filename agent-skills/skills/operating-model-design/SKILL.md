---
name: operating-model-design
description: Use when an enterprise solution needs explicit ownership, support, monitoring, incident, change, data, resilience, governance, supplier, and continuous-improvement responsibilities after delivery.
---

# Operating Model Design

## Purpose
Design how a solution is owned and operated throughout its lifecycle.

## Use when
- A new service or platform is moving toward production.
- Ownership and support are fragmented across teams or suppliers.
- Architecture decisions create new operational responsibilities.

## Do not use when
- The task is only to prepare a short-term hypercare plan.
- One incident needs immediate triage.

## Required inputs
- Business service or outcome and criticality.
- Systems, teams, suppliers, service hours, and dependencies.
- Monitoring, incident, change, data, resilience, and governance expectations.

## Workflow
1. Define service scope and business outcome.
2. Map ownership by responsibility type.
3. Define support hours, severity, escalation, and fallback.
4. Define monitoring, alert, incident, problem, and knowledge flows.
5. Define change, release, emergency-change, and dependency coordination.
6. Define data-quality and reconciliation ownership.
7. Define capacity, resilience, recovery, and continuity ownership.
8. Define supplier and platform boundaries.
9. Define service, business, and operational-load metrics.
10. Define governance cadence and improvement loop.

## Decision rules
- Do not use one generic support owner for distinct decision rights.
- Monitoring ownership must include response ownership.
- Supplier responsibility does not remove internal business accountability.
- Operational load and recurring work should feed improvement decisions.

## Output format
Produce an **Operating Model Record** with service scope, ownership map, support model, escalation, monitoring, incident/problem, change/release, data, resilience, supplier boundaries, metrics, governance, and improvement loop.

## Quality gates
- [ ] Business outcome and criticality are explicit.
- [ ] Ownership is separated by responsibility type.
- [ ] Monitoring has response ownership.
- [ ] Change and data responsibilities are defined.
- [ ] Supplier boundaries and escalation are explicit.
- [ ] Improvement loop uses operational evidence.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
