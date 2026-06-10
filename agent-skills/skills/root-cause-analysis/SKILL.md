---
name: root-cause-analysis
description: Use when an incident has been triaged and the same symptom has occurred at least twice, when a high-impact incident blocked a critical business process for more than four hours, or when a change caused unexpected failures. Produces a Root Cause Analysis Note with correction and prevention. Do not use for initial incident classification or for one-off user errors without systemic pattern.
---

# Root Cause Analysis

## Purpose

Separate symptoms from causes, trace defects to their entry point, and produce a correction and prevention plan.

## Use when

- An incident has been triaged and the same symptom has occurred at least twice.
- A high-impact incident blocked a critical business process for more than four hours.
- A change went live and caused unexpected failures in a different module or system.
- A data quality report shows a spike in defects and the source is unknown.
- A background job or interface has been failing intermittently and the failure pattern is unclear.

## Do not use when

- The incident has just arrived and needs classification and containment (use `incident-triage`).
- The symptom is a one-off user error with no systemic pattern.
- You need a high-level operational improvement plan without a specific incident.

## Required inputs

- The triage record or incident ticket with full symptom description, timestamps, and affected scope.
- System logs: SM21, SLG1, ST22, SM37, SM58, SMQ1/SMQ2, WE02/WE05.
- Change history: transport logs, change documents (SCU3), configuration changes in the relevant time window.
- Master data samples: affected records with before/after comparison if available.
- Process documentation or runbooks for the affected area.
- Stakeholder access: functional consultant, data steward, Basis, integration team, business user who reported the issue.
- Ticket history for the last 30–90 days to check for recurrence.

## Workflow

1. **Confirm the symptom.** Reproduce or verify the reported defect with your own eyes. Document the exact error text, transaction, and record IDs.
2. **Define the defect boundary.** Determine: affected system, module, document type, time window, number of records, and whether the defect is ongoing or historical.
3. **Build a timeline.** List events in chronological order: first failure, last success, any changes, any maintenance windows, any data loads.
4. **Identify the immediate cause.** What directly produced the symptom? State it in one sentence.
5. **Trace to the root cause.** Ask "why" up to five times or until you reach a process, configuration, or governance gap that explains the immediate cause.
6. **Identify the entry point.** Where in the lifecycle did the defect first enter? User entry, interface, batch, replication, manual config, or code change?
7. **Classify the defect type.** Use one of: data, configuration, custom code, process, integration, infrastructure, user error, or unknown.
8. **Quantify business impact.** Count affected records, estimate cost, identify downstream processes that are blocked or delayed.
9. **Design the correction.** How will affected records or systems be fixed? Manual, mass update, reprocessing, reversal, or configuration rollback?
10. **Design the prevention control.** What validation, workflow, monitoring, or process change will stop this from recurring? The prevention must address the root cause, not the symptom.
11. **Assign owners and deadlines.** Name a person or team for correction and a person or team for prevention. Set realistic deadlines.
12. **Document in a Root Cause Analysis Note.** Use the structured format below.

## Decision rules

- If the symptom cannot be reproduced, stop the analysis and gather more data before building theories.
- If the timeline shows a change within 24 hours of first failure, treat the change as the primary suspect until disproven.
- If the defect affects fewer than 10 records and the rule is clear, correct through the governed manual process.
- If the defect affects more than 100 records, prepare a mass correction with validation, approval, and a rollback plan.
- If the root cause is a missing validation, fix the validation before correcting existing records.
- If the root cause is a process gap, produce a process change proposal, not just a one-time fix.
- If the defect has occurred before and was "fixed," the previous fix was not a root cause fix. Escalate to find the deeper cause.
- If the entry point is an interface, check the source system validation before blaming SAP configuration.
- If the root cause is unknown after 4 hours of analysis, document what is known, what was ruled out, and what data is missing.

## Output format

Produce a **Root Cause Analysis Note**:

```markdown
---
artifact: Root Cause Analysis Note
id: RCA-001
date: YYYY-MM-DD
author: Name
status: draft | reviewed | closed
---

## Symptom
<!-- Exact observation. Error text, transaction, record IDs. -->

## Defect classification
<!-- data | config | code | process | integration | infrastructure | user error | unknown -->

## Affected scope
<!-- Systems, records, users, business areas, time period -->

## Timeline
<!-- Chronological list of events: last success, first failure, changes, maintenance -->

## Immediate cause
<!-- What directly produced the symptom -->

## Root cause
<!-- The underlying reason. Ask "why" until you reach a process or governance gap. -->

## Entry point
<!-- Where the defect entered the lifecycle -->

## Business impact
<!-- Quantified: orders blocked, invoices delayed, revenue at risk, hours lost -->

## Correction approach
<!-- Manual, mass update, reprocessing, reversal, rollback -->

## Prevention control
<!-- What stops recurrence: validation, workflow, monitoring, process change -->

## Correction owner
<!-- Who fixes the affected records -->

## Prevention owner
<!-- Who implements the control -->

## Deadlines
<!-- Correction by: YYYY-MM-DD. Prevention by: YYYY-MM-DD. -->

## Verification
<!-- How we confirm the fix and the control work -->

## Related incidents
<!-- Ticket numbers, IDocs, change requests, previous RCAs -->
```

Also produce a **Remediation Backlog Item** and a **Prevention Control Proposal** if needed.

## Quality gates

- [ ] The symptom is described with exact error text, transaction code, and at least one example record ID.
- [ ] A timeline exists with at least three data points: last known success, first failure, and any relevant change or event.
- [ ] The root cause is distinct from the symptom and the immediate cause.
- [ ] The entry point is identified: where the defect first entered the lifecycle.
- [ ] Business impact is quantified or at least estimated with a clear method.
- [ ] The correction approach addresses affected records or systems, not just the root cause.
- [ ] The prevention control addresses the root cause, not the symptom.
- [ ] Both correction and prevention have named owners and deadlines.
- [ ] Ticket history for the last 30 days was checked for recurrence.

## References

- `references/method.md` — Detailed timeline building, 5 Whys technique, and defect classification.
- `references/templates.md` — Copy-ready templates for RCA Note, Remediation Backlog Item, and Prevention Control Proposal.
- `references/examples.md` — Good and bad examples from SAP master data, IDoc failures, and batch job cancellations.

## Safety rules

- Separate facts from assumptions. Label assumptions about log interpretation and timeline correlation.
- Separate decisions from open questions. List open questions about missing logs or unverified system states.
- Do not expose client names, ticket numbers, internal incident IDs, or proprietary system details.
- Do not copy proprietary framework text. Use your own words.
- Never accept the user's first description as the root cause. Ask "why" repeatedly.
