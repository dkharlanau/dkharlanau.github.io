# Data Governance Ownership — Templates

## Template 1: Data Ownership Matrix

```markdown
---
artifact: Data Ownership Matrix
id: DOM-001
date: YYYY-MM-DD
scope: <domain or system>
---

## Data elements

| Data Element | System of Record | Business Owner | Technical Owner | Data Steward | Consumers | Ownership Gap |
|--------------|------------------|----------------|-----------------|--------------|-----------|---------------|
| <element> | <system> | <name> | <name> | <name> | <list> | <gap or NONE> |

## Ownership gaps

| Data Element | Missing Role | Risk | Proposed Assignee | Confirmation | Due Date |
|--------------|--------------|------|-------------------|--------------|----------|
| <element> | <role> | <risk> | <name> | <confirmed/proposed/refused> | <date> |

## Review cycle
- Frequency: <quarterly / semi-annual / annual>
- Review owner: <name>
- Next review: <date>
```

## Template 2: Rule Catalog

```markdown
---
artifact: Rule Catalog
id: RC-001
date: YYYY-MM-DD
scope: <domain or system>
---

## Rules

| Rule | Applies To | Enforcement Point | Failure Action | Review Frequency | Gap |
|------|------------|-------------------|--------------|------------------|-----|
| <rule> | <element> | <system/transaction> | <action> | <frequency> | <gap or NONE> |

## Enforcement gaps

| Rule | Gap Description | Business Risk | Proposed Closure | Owner | Due Date |
|------|-----------------|---------------|------------------|-------|----------|
| <rule> | <description> | <risk> | <action> | <name> | <date> |
```

## Template 3: Governance Action Plan

```markdown
---
artifact: Governance Action Plan
id: GAP-001
date: YYYY-MM-DD
scope: <domain or system>
status: draft | reviewed | approved
---

## Priority actions

| Priority | Action | Owner | Due Date | Success Criteria | Risk if Not Done |
|----------|--------|-------|----------|------------------|------------------|
| P1 | <action> | <name> | <date> | <criteria> | <risk> |
| P2 | <action> | <name> | <date> | <criteria> | <risk> |

## Decision rights charter

| Data Domain | Create | Update | Delete | Approve Changes | Approve Access | Define Rules |
|-------------|--------|--------|--------|-----------------|----------------|--------------|
| <domain> | <who> | <who> | <who> | <who> | <who> | <who> |

## Review cycle
- Frequency: <quarterly / semi-annual / annual>
- Review owner: <name>
- Next review: <date>
```

## Template 4: Ownership Gap Report

```markdown
---
artifact: Ownership Gap Report
id: OGR-001
date: YYYY-MM-DD
---

## Summary
- Total data elements in scope: <count>
- Elements with ownership gaps: <count>
- Critical gaps (P1): <count>

## Gap details

| Data Element | Gap | Risk | Proposed Owner | Status | Due Date |
|--------------|-----|------|----------------|--------|----------|
| <element> | <description> | <risk> | <name> | <status> | <date> |

## Recommendations
1. <recommendation>
2. <recommendation>
```
