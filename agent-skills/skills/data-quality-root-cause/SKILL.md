---
name: data-quality-root-cause
description: Use when investigating recurring data defects, failed validations, bad master data, migration data errors, duplicate records, or SAP/business process failures caused by missing, invalid, inconsistent, or poorly owned data. Do not use for generic data governance summaries.
---

# Data Quality Root Cause

## Purpose

Trace a data defect from symptom to entry point. Classify the root cause type. Produce a correction plan and a prevention control.

## Use when

- A report shows incorrect values and someone says "the data is bad" without explaining why.
- Orders are blocked because customer master data is incomplete, and the fix is always manual.
- Duplicate records appear in a system and deduplication campaigns keep finding more.
- An integration sends data to a target system, but the target rejects it or stores it incorrectly.
- A data steward spends more than 20% of their time correcting the same type of defect.
- An audit or incident review requires a documented root cause and prevention plan.

## Do not use when

- The issue is purely a system performance or infrastructure problem with no data element involved.
- You need a high-level data governance strategy without a specific defect to investigate.
- The data is unstructured (images, free text) and requires NLP or ML analysis.

## Required inputs

- Exact symptom: field, value, record count, system, business process affected.
- Sample records showing the defect (anonymized).
- System landscape: where data is created, transformed, stored, consumed.
- Data entry points: user interfaces, integrations, batch loads, API calls.
- Validation rules that should have caught the defect.
- Ticket or incident history showing recurrence frequency (optional).
- Stakeholders who can explain the business process and data flow (optional but recommended).

## Workflow

1. **Document the symptom precisely.** Record: data element, wrong value, expected value, system where observed, business process affected, number of records, first occurrence date. Do not proceed with vague symptoms.
2. **Identify the business impact.** Quantify if possible: orders blocked, invoices delayed, reports wrong, compliance risk. If you cannot quantify, describe the business consequence in process terms.
3. **Trace backward to the entry point.** Follow the data from the symptom system to the system that created or last modified the record. Check integrations, batch jobs, user transactions, and API calls.
4. **Classify the root cause type.** Use one of: missing rule, unenforced rule, wrong rule, upstream data error, integration mapping error, reference data mismatch, user error without guardrail, system bug, unknown.
5. **Identify the entry point detail.** Name the exact system, transaction, interface, or user action where the defect entered. Include timestamp and user or process ID if available.
6. **Assess scope.** Determine how many records are affected now, how many could be affected in the future, and whether the defect is spreading to downstream systems.
7. **Design the correction.** Choose: manual correction, mass update with validation, reprocessing, mapping fix, or record merge. Define validation and approval steps.
8. **Design the prevention control.** Choose: add validation, strengthen workflow, fix mapping, synchronize reference data, add monitoring, or change the user interface. The prevention must address the root cause, not the symptom.
9. **Assign ownership.** Name who corrects, who validates, who implements the prevention, and who monitors.
10. **Produce the Root Cause Analysis Note.** Document symptom, classification, entry point, impact, correction, prevention, and owners.
11. **Validate with stakeholders.** Confirm the root cause, correction approach, and prevention control with business and technical owners before execution.

## Decision rules

- If the defect recurs, the root cause is not the symptom; trace further upstream.
- If only a few records are affected and the rule is clear, correct records through the governed process.
- If many records are affected, prepare mass correction with validation and approval; never mass-update without a sample check.
- If the root cause is "user error," look for the missing guardrail or validation that should have prevented it.
- If the root cause is an integration mapping error, fix the mapping before correcting records, or the correction will be overwritten.
- If the root cause is a reference data mismatch, synchronize reference data before reprocessing affected transactions.
- If no validation rule exists for this data element, the root cause is "missing rule" even if the data looks obviously wrong.
- If a rule exists but is bypassed by a specific path (API, batch, direct DB), the root cause is "unenforced rule."

## Output format

Produce a **Data Quality Root Cause Note** with these sections:

```markdown
## Symptom
- Field: <exact field>
- Wrong value: <observed>
- Expected value: <target>
- System: <where observed>
- Business process affected: <process>
- Records affected: <count>
- First occurrence: <date>

## Business impact
<quantified or described in process terms>

## Root cause classification
<Type from the classification table>

## Entry point
<System, transaction, interface, or user action>

## Scope assessment
- Currently affected: <count>
- Potentially affected: <count>
- Downstream spread: <yes/no + systems>

## Correction approach
- Method: <manual / mass update / reprocessing / mapping fix / merge>
- Validation steps: <what to check before and after>
- Approval required: <who>

## Prevention control
- Control type: <validation / workflow / mapping / sync / monitoring / UI>
- Implementation owner: <name>
- Monitoring: <how to detect recurrence>

## Owners
- Correction: <name>
- Validation: <name>
- Prevention implementation: <name>
- Monitoring: <name>

## Validation
- Confirmed by: <business owner> and <technical owner>
- Date: <YYYY-MM-DD>
```

Also produce a **Remediation Backlog Item** if mass correction or prevention implementation is needed.

## Quality gates

- [ ] The symptom is documented with exact field, value, system, and business process.
- [ ] The root cause is classified into one of the defined types, not described as a narrative.
- [ ] The entry point is named: specific system, transaction, interface, or user action.
- [ ] The correction approach includes validation and approval steps.
- [ ] The prevention control addresses the root cause, not the symptom.
- [ ] All owners are named, not just roles.
- [ ] The analysis has been validated with at least one business and one technical stakeholder.
- [ ] If the root cause is unknown, there is a plan to add monitoring or logging to discover it.

## References

- `references/method.md` — Detailed trace method, classification definitions, and scope assessment techniques.
- `references/templates.md` — Copy-ready templates for Root Cause Note, Remediation Backlog Item, and Data Quality Rule.
- `references/examples.md` — Good and bad examples from SAP, integration, and master data contexts.

## Safety rules

- Separate facts from assumptions. Label every assumption with a risk if it is wrong.
- Separate decisions from open questions. List open questions explicitly and assign discovery owners.
- Do not expose client names, ticket numbers, or internal incident IDs in the output.
- Do not copy proprietary framework text. Use your own words.
