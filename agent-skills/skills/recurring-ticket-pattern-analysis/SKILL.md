---
name: recurring-ticket-pattern-analysis
description: Use when the same error message appears in at least three tickets in 30 days, when a specific user or team opens tickets for the same process step every week, or when an interface or job fails on a predictable schedule and is always fixed the same way. Produces a pattern analysis report with cost quantification and prevention proposals. Do not use for one-off incidents or already-resolved systemic issues.
---

# Recurring Ticket Pattern Analysis

## Purpose

Find the patterns behind repeated tickets, quantify the cost, and design a permanent fix instead of handling the same symptom forever.

## Use when

- The same error message appears in at least three tickets in the last 30 days.
- A specific business user or team opens tickets for the same process step every week.
- An interface or background job fails on a predictable schedule and is always fixed the same way.
- A data quality issue is corrected manually every month but never prevented.
- The AMS team spends more than 20% of its time on a small set of recurring symptoms.
- Management asks why ticket volume is not decreasing despite staffing increases.

## Do not use when

- The incident is a one-off with no recurrence pattern.
- The systemic issue has already been identified and a permanent fix is in progress.
- You need a general operational review without ticket data.

## Required inputs

- Ticket system export for the last 90–180 days: ticket ID, date, category, description, resolution, time spent, resolver.
- Classification of tickets by symptom, error message, module, and business process.
- Time tracking data or estimate of hours per ticket type.
- Business impact data: orders blocked, invoices delayed, users affected, revenue at risk.
- System logs for the time windows when recurring tickets occur.
- Change calendar: transports, maintenance windows, data loads, and scheduled jobs.
- Stakeholder access: functional leads, business users, data stewards, and management.

## Workflow

1. **Extract ticket data.** Export tickets for the last 90–180 days. Include: ID, date, category, short description, resolution text, time spent, and resolver name.
2. **Classify by symptom.** Group tickets by error message, process step, or object. Use keyword search and pattern matching. Do not rely on the ticket category alone.
3. **Count frequency.** For each symptom group, count tickets per week or per month. Identify the top 3–5 groups by volume.
4. **Build a timeline.** Plot the top groups against the change calendar. Look for correlation with transports, month-end, quarter-end, or scheduled jobs.
5. **Quantify cost.** For each top group, calculate: handling cost (tickets × hours × rate) + business cost (delayed orders, credit notes, complaints, revenue at risk).
6. **Analyze resolution patterns.** Read resolution texts for the top groups. Is the fix always the same? Is it a workaround? Does it require manual intervention?
7. **Trace to root cause.** For the top group, perform a Root Cause Analysis on a representative ticket. Identify the systemic failure that allows the symptom to recur.
8. **Design prevention.** Propose a permanent fix: validation, workflow, monitoring, schedule change, process change, or automation. The prevention must address the root cause, not the symptom.
9. **Build the business case.** Compare the annual cost of handling versus the one-time cost of prevention. Include risk reduction and user satisfaction benefits.
10. **Document the pattern.** Produce a Recurring Ticket Pattern Analysis report.
11. **Present and decide.** Share the report with functional leads and management. Request a decision on prevention investment.

## Decision rules

- If a symptom appears in more than 5% of monthly tickets, it qualifies for pattern analysis.
- If the resolution is always the same manual workaround, the symptom is a candidate for automation or prevention.
- If tickets cluster around a specific time or event, investigate the trigger first, not the symptom.
- If the annual handling cost exceeds the estimated prevention cost by 2× or more, the business case is strong.
- If the root cause is a missing validation, propose the validation before proposing a monitoring alert.
- If the root cause is a process gap, propose a process change with named owners and deadlines.
- If a permanent fix was proposed and rejected before, document the reason and address it in the new proposal.
- If the pattern involves multiple modules or systems, assign a cross-functional owner, not a single module lead.
- If the pattern is caused by a third-party system or supplier, involve procurement or vendor management in the solution.

## Output format

Produce a **Recurring Ticket Pattern Analysis Report**:

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

Also produce a **Business Case Summary** and a **Prevention Proposal**.

## Quality gates

- [ ] Ticket data covers at least 90 days and includes ID, date, description, and resolution.
- [ ] At least three distinct symptom groups were identified and counted.
- [ ] Frequency analysis shows tickets per week or month, not just total count.
- [ ] Timeline correlation was checked against the change calendar or scheduled events.
- [ ] Cost is quantified for at least the top pattern: handling cost + business cost.
- [ ] The root cause for the top pattern was traced using the Root Cause Analysis skill.
- [ ] The prevention proposal addresses the root cause, not the symptom.
- [ ] The business case compares annual handling cost to prevention cost.
- [ ] The report was reviewed by at least one functional lead and one business stakeholder.

## References

- `references/method.md` — Detailed ticket classification, cost quantification, and timeline correlation.
- `references/templates.md` — Copy-ready templates for Pattern Analysis Report, Business Case Summary, and Prevention Proposal.
- `references/examples.md` — Good and bad examples from SAP IDoc failures, pricing condition expirations, and post-transport authorization issues.

## Safety rules

- Separate facts from assumptions. Label assumptions about ticket handling time and business cost estimates.
- Separate decisions from open questions. List open questions about missing ticket data or unverified cost figures.
- Do not expose client names, ticket numbers, or internal incident IDs.
- Do not copy proprietary framework text. Use your own words.
- Do not invent ticket counts or costs. If data is missing, state the gap and propose how to collect it.
