# Recurring Ticket Pattern Analysis — Templates

## Template 1: Recurring Ticket Pattern Analysis Report

```markdown
---
artifact: Recurring Ticket Pattern Analysis Report
id: RTP-001
date: YYYY-MM-DD
analyst: Name
period: Last 90 days
---

## Executive summary
<!-- Top 3 patterns, total cost, and recommended action -->

## Method
<!-- How tickets were extracted, classified, and counted -->

## Pattern 1: [Symptom name]

### Symptom description
<!-- Error message, process step, or observation -->

### Frequency
<!-- Tickets per week/month, trend -->

### Affected scope
<!-- Systems, modules, users, data objects -->

### Timeline correlation
<!-- Correlation with transports, month-end, jobs -->

### Resolution pattern
<!-- How tickets are resolved. Workaround or permanent fix? -->

### Handling cost
<!-- Tickets × hours × rate -->

### Business cost
<!-- Delayed orders, credit notes, complaints, revenue at risk -->

### Root cause
<!-- Underlying reason the symptom recurs -->

### Prevention proposal
<!-- Specific action, owner, deadline, expected outcome -->

### Prevention cost estimate
<!-- One-time and ongoing cost -->

## Pattern 2: [Symptom name]
<!-- Same structure as Pattern 1 -->

## Pattern 3: [Symptom name]
<!-- Same structure as Pattern 1 -->

## Recommendations
<!-- Prioritized list of prevention actions with ROI -->

## Appendix
<!-- Ticket IDs, queries, data sources -->
```

## Template 2: Business Case Summary

```markdown
---
artifact: Business Case Summary
id: BCS-001
date: YYYY-MM-DD
source: RTP-001
---

## Problem
<!-- What recurring pattern was found -->

## Annual handling cost
<!-- Tickets per year × hours × rate + business cost -->

## Prevention cost
<!-- One-time implementation + ongoing maintenance -->

## ROI
<!-- Annual handling cost / prevention cost -->

## Risk reduction
<!-- What risks are reduced by the prevention -->

## Intangible benefits
<!-- User satisfaction, operational efficiency, etc. -->

## Recommendation
<!-- Approve / Reject / Defer -->

## Decision
<!-- Who decided and when -->
```

## Template 3: Prevention Proposal

```markdown
---
artifact: Prevention Proposal
id: PP-001
date: YYYY-MM-DD
source: RTP-001
---

## Prevention description
<!-- What will be implemented -->

## Type
<!-- validation | workflow | monitoring | schedule change | process change | automation -->

## Implementation steps
1. <step>
2. <step>

## Owner
<!-- Who implements the prevention -->

## Deadline
<!-- When the prevention must be in place -->

## Expected outcome
<!-- What will change after implementation -->

## Cost estimate
<!-- One-time and ongoing cost -->

## Verification
<!-- How to confirm the prevention works -->
```

## Template 4: Ticket Classification Table

```markdown
| Ticket ID | Date | Symptom | Error Message | Module | Resolution | Time Spent | Classification |
|-----------|------|---------|---------------|--------|------------|------------|----------------|
| <ID> | <date> | <symptom> | <message> | <module> | <resolution> | <hours> | <group> |
```
