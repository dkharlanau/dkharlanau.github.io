---
name: cross-system-ownership
description: Use when a business outcome crosses systems or teams and ownership is unclear for data, interfaces, incidents, changes, controls, or end-to-end validation.
---

# Cross-System Ownership

## Purpose
Define accountable ownership across system and team boundaries.

## Use when
- A process or integration crosses several systems or suppliers.
- Incidents bounce between teams.
- Change, data, monitoring, or validation ownership is unclear.

## Do not use when
- One team owns the full outcome and all dependencies.
- The task is only to identify a current technical fault.

## Required inputs
- Business outcome and process boundary.
- Systems, teams, interfaces, data objects, and known support responsibilities.
- Incident, change, and operational expectations.

## Workflow
1. Map the end-to-end business outcome.
2. Identify systems, teams, data, interfaces, controls, and decision points.
3. Separate ownership types instead of using one generic owner field.
4. Identify handoff boundaries and ownerless completion points.
5. Define decision rights, escalation, and fallback ownership.
6. Test the model against incident, change, cutover, and supplier-failure scenarios.
7. Record gaps and unresolved shared responsibilities.

## Decision rules
- Component ownership is not end-to-end outcome ownership.
- Shared responsibility without a decision rule is an ownership gap.
- Producer and consumer responsibilities must both be explicit for integrations.
- Escalation ownership must work outside normal conditions.

## Output format
Produce a **Cross-System Ownership Map** with outcome, boundary, ownership types, named roles or teams, decision rights, escalation, fallback, and gaps.

## Quality gates
- [ ] End-to-end outcome owner is explicit.
- [ ] Data, interface, operations, change, and validation ownership are separated where relevant.
- [ ] Handoff boundaries are visible.
- [ ] Escalation and fallback are defined.
- [ ] Shared responsibilities have decision rules.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
