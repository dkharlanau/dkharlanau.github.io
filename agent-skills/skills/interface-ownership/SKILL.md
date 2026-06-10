---
name: interface-ownership
description: Use when interface failures sit unresolved because teams point at each other, when a schema change breaks a consumer and no one knows who approved it, or when an AMS team lacks business context for integration alerts. Produces an Interface Ownership Matrix with four ownership roles per interface. Do not use for API design or integration architecture decisions.
---

# Interface Ownership

## Purpose

Map every interface in your landscape to a named owner for business decisions, technical decisions, and operational response. Close ownership gaps before they become incidents.

## Use when

- Post-merger or platform consolidation requires an interface cleanup.
- A new project is handing over integrations to AMS or operations.
- Recurring interface failures sit unresolved for days because teams point at each other.
- An audit finding notes missing governance or unclear responsibilities for integrations.
- A schema change breaks a consumer and no one knows who approved it.
- The AMS team receives alerts but does not know which business unit to contact for data validation.

## Do not use when

- You are designing a new API or event schema (use API design or event-driven architecture skills).
- The problem is purely a middleware infrastructure capacity issue with no ownership dimension.
- You need a high-level integration strategy without a specific interface inventory.

## Required inputs

- Interface inventory: all known APIs, IDocs, RFCs, file transfers, events.
- System landscape diagram showing sources, targets, and middleware.
- Organizational chart or team directory.
- Existing SLAs or operational agreements.
- Incident history for the last 6–12 months (to find pain points).
- Middleware configuration: queues, topics, routing rules.
- Project documentation for recent or upcoming interfaces.

## Workflow

1. **List all interfaces.** Gather from middleware, SAP (WE02, SM58, BD87), API gateways, file transfer logs, and project docs. Include active, dormant, and planned interfaces.
2. **Classify by type and criticality.** Tag each interface as API, IDoc, RFC, file, or event. Rate criticality by business impact: critical, major, minor, dormant.
3. **Define four ownership roles per interface.**
   - **Business owner:** approves schema changes, validates semantics, decides deprecation.
   - **Technical owner:** designs and maintains the interface, approves implementation changes.
   - **Operational owner:** monitors, responds to alerts, performs first-line diagnosis.
   - **Consumer representative:** speaks for downstream consumers, validates compatibility.
4. **Document in ownership matrix.** Record interface ID, source, target, direction, type, criticality, and all four owners.
5. **Identify gaps.** Flag interfaces with missing owners, conflicting claims, or owners who have left the organization.
6. **Assign missing owners.** For each gap, propose an owner based on domain, system, or incident history. Get written confirmation.
7. **Define change process.** Document how ownership is updated when systems change, teams reorganize, or projects end.
8. **Validate with incident drill.** Simulate a failure for a critical interface. Verify that the operational owner knows who to contact and that the business owner can make decisions.

## Decision rules

- If an interface has no business owner, assign one from the source data domain.
- If the operational owner is missing, default to the AMS or integration operations team.
- If a consumer is external or from another business unit, designate a consumer representative.
- If ownership is disputed between two teams, escalate to the architecture or governance board.
- If an interface is critical and unowned, treat it as a P1 risk and assign an interim owner within 24 hours.
- If an owner changes, update the matrix within 48 hours and notify all stakeholders.
- If an interface has no consumer for 12 months, initiate deprecation review with the business owner.
- If an interface crosses legal entities or countries, assign a compliance owner in addition to the four standard roles.

## Output format

Produce an **Interface Ownership Matrix**:

```markdown
---
artifact: Interface Ownership Matrix
id: IOM-001
date: YYYY-MM-DD
scope: System landscape | Project | Domain
---

## Interfaces

| Interface ID | Source | Target | Direction | Type | Criticality | Business Owner | Technical Owner | Operational Owner | Consumer Rep | SLA | Status |
|--------------|--------|--------|-----------|------|-------------|----------------|-----------------|-------------------|--------------|-----|--------|
| IF-001 | SAP S/4 | Salesforce | Outbound | API | Critical | <name> | <name> | <name> | <name> | 4h | Active |

## Ownership gaps

| Interface ID | Missing Role | Risk | Action | Assignee | Due Date |
|--------------|--------------|------|--------|----------|----------|
| IF-004 | Business Owner | No one approves schema changes | Assign from Sales domain | <name> | <date> |

## Unowned interfaces
<!-- Interfaces discovered but not in any ownership model -->

## Change process
<!-- How ownership is updated when systems change -->

## Review frequency
<!-- Quarterly recommended -->
```

Also produce an **Ownership Gap Report** and a **RACI for Interface Changes**.

## Quality gates

- [ ] Every active interface has a named business owner.
- [ ] Every active interface has a named technical owner.
- [ ] Every active interface has a named operational owner.
- [ ] Critical interfaces have a consumer representative.
- [ ] Change process is documented and communicated.
- [ ] Matrix is reviewed at least quarterly.
- [ ] Ownership gaps have assigned resolution owners and due dates.
- [ ] Incident drill confirmed that operational owners know escalation paths.

## References

- `references/method.md` — Detailed interface discovery, ownership role definition, and gap resolution.
- `references/templates.md` — Copy-ready templates for Ownership Matrix, Gap Report, and RACI.
- `references/examples.md` — Good and bad examples from post-merger, SAP AMS handover, and multi-vendor contexts.

## Safety rules

- Separate facts from assumptions. Label proposed owners as "confirmed" or "proposed."
- Separate decisions from open questions. List open questions about disputed ownership or missing org chart data.
- Do not expose client names, vendor names, or proprietary interface contracts.
- Do not copy proprietary framework text. Use your own words.
