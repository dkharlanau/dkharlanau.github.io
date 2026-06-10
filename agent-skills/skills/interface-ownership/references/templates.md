# Interface Ownership — Templates

## Template 1: Interface Ownership Matrix

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
| IF-002 | SAP S/4 | Warehouse | Outbound | IDoc | Major | <name> | <name> | <name> | <name> | 8h | Active |
| IF-003 | Bank | SAP S/4 | Inbound | File | Critical | <name> | <name> | <name> | <name> | 2h | Active |

## Ownership gaps

| Interface ID | Missing Role | Risk | Action | Assignee | Due Date |
|--------------|--------------|------|--------|----------|----------|
| IF-004 | Business Owner | No one approves schema changes | Assign from Sales domain | <name> | <date> |
| IF-005 | Operational Owner | Alerts go to unmonitored mailbox | Route to AMS Team | <name> | <date> |

## Unowned interfaces
<!-- Interfaces discovered but not in any ownership model -->

## Change process
<!-- How ownership is updated when systems change -->

## Review frequency
<!-- Quarterly recommended -->
```

## Template 2: Ownership Gap Report

```markdown
---
artifact: Ownership Gap Report
id: OGR-001
date: YYYY-MM-DD
---

## Summary
- Total interfaces: <count>
- Interfaces with gaps: <count>
- Critical interfaces with gaps: <count>

## Gap details

| Interface ID | Gap | Risk | Proposed Owner | Status | Due Date |
|--------------|-----|------|----------------|--------|----------|
| <ID> | <description> | <risk> | <name> | <status> | <date> |

## Recommendations
1. <recommendation>
2. <recommendation>
```

## Template 3: RACI for Interface Changes

```markdown
---
artifact: RACI for Interface Changes
id: RACI-001
date: YYYY-MM-DD
---

## Change types

| Change Type | Business Owner | Technical Owner | Operational Owner | Consumer Rep | Compliance |
|-------------|----------------|-----------------|-------------------|--------------|------------|
| Schema change | A | R | C | C | I |
| Infrastructure change | I | A/R | C | I | C |
| Deprecation | A | R | C | C | I |
| SLA change | A | C | R | C | I |

## Legend
- R = Responsible (does the work)
- A = Accountable (approves)
- C = Consulted (provides input)
- I = Informed (notified after)
```

## Template 4: Runbook for Ownership Updates

```markdown
---
artifact: Runbook for Ownership Updates
id: ROU-001
date: YYYY-MM-DD
---

## Trigger events
- Team reorganization
- System decommission
- Project handover to AMS
- Owner departure
- Interface criticality change

## Update process
1. Identify the affected interface(s)
2. Propose new owner based on domain or system
3. Get written confirmation from proposed owner
4. Update the ownership matrix
5. Notify all stakeholders
6. Update SLA if needed
7. Schedule incident drill for critical interfaces

## Review cycle
- Frequency: quarterly
- Review owner: <name>
```
