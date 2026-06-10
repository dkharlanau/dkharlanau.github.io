---
name: change-impact-analysis
description: Use when assessing impact before applying a transport, configuration change, master data update, or interface schema modification. Produces a Change Impact Assessment that lists affected systems, data, interfaces, processes, and stakeholders with risk levels and a rollback plan. Do not use after a change has already caused an incident (use root-cause-analysis instead).
---

# Change Impact Analysis

## Purpose

Before applying a transport, configuration change, or master data update, know which processes, interfaces, and stakeholders are affected.

## Use when

- A transport is ready for production and the release note only says "config update."
- A master data change (new plant, new company code, new payment term) is planned and downstream systems may be affected.
- An interface schema or API contract is being modified and consumers need to adapt.
- A new validation rule or incompletion procedure is being introduced.
- A user role or authorization change is planned and sensitive transactions may be affected.
- A periodic process timing or scheduling change is proposed.

## Do not use when

- The change has already gone live and caused an incident (use `root-cause-analysis`).
- You are designing the change itself (this skill assesses impact, not designs the solution).
- The change is purely infrastructure (server restart, patch) with no application or data impact.

## Required inputs

- A precise description of the proposed change: what object, what value, what system, and what the intended outcome is.
- The transport or change request documentation with object list and developer notes.
- System landscape diagram or list: DEV, QAS, PRD, and connected systems (CRM, SRM, BW, Ariba, Salesforce, etc.).
- Interface ownership matrix or list of interfaces that touch the changed object.
- Process documentation for the business process that uses the changed object.
- Where-used lists: for config objects, tables, fields, and custom code.
- Stakeholder list: functional owners, integration team, data stewards, business users who will test.
- Test environment availability and data freshness.

## Workflow

1. **Define the change boundary.** Document exactly what is changing: object name, table, field, transaction, program, or configuration path. Include current and proposed values.
2. **Map direct consumers.** Use where-used search, cross-reference tools, or SE11/SE16 to find all programs, classes, reports, and transactions that reference the object.
3. **Map interface consumers.** Check all interfaces (IDoc, RFC, API, file) that send or receive the object. Review the segment structures, API schemas, and mapping tables.
4. **Map process consumers.** Identify business process steps that use the object. Check process documentation or interview the process owner.
5. **Map data consumers.** Check BW extractors, reporting tables, data warehouse loads, and analytics tools that reference the object.
6. **Identify authorization impacts.** If the change affects transactions or data access, check roles and profiles that grant access.
7. **Assess risk for each consumer.** For each affected component, rate the risk: Low, Medium, High, or Critical.
8. **Define testing scope.** List what must be tested: unit test, integration test, regression test, user acceptance test. Name the tester and the test data requirements.
9. **Define rollback plan.** How can the change be reversed? Transport reversal, config rollback, data restore, or emergency procedure?
10. **Document in a Change Impact Assessment.** Use the structured format below.
11. **Obtain approval.** The assessment must be reviewed by the functional owner, integration lead, and change manager before implementation.

## Decision rules

- If the change affects a table or field used by more than one interface, treat the risk as High until each interface is verified.
- If the change introduces a new mandatory field, check all creation channels (GUI, API, EDI, batch) before approving.
- If the change affects master data, check replication and synchronization settings in all target systems.
- If the change affects a background job schedule, check all dependent jobs and their schedules.
- If the change affects authorization objects, test with at least one user from each affected role.
- If no rollback plan exists, do not approve the change.
- If testing cannot be performed with representative data, delay the change until test data is available.
- If the change was developed in DEV but the object exists differently in PRD, verify the production state before impact analysis.

## Output format

Produce a **Change Impact Assessment**:

```markdown
---
artifact: Change Impact Assessment
id: CIA-001
date: YYYY-MM-DD
change: Description
status: draft | reviewed | approved
---

## Change description
<!-- Exact object, current value, proposed value, system -->

## Change driver
<!-- Why this change is needed -->

## Systems affected
<!-- Direct and indirect system impacts -->

| System | Component | Risk | Action Required | Owner |
|--------|-----------|------|-----------------|-------|
| SAP PRD | <object> | Medium | <action> | <name> |

## Data affected
<!-- Tables, fields, records that change -->

## Interfaces affected
<!-- APIs, IDocs, events that may break or need update -->

| Interface | Direction | Risk | Action Required | Owner |
|-----------|-----------|------|-----------------|-------|
| <ID> | <direction> | High | <action> | <name> |

## Processes affected
<!-- Business processes that change -->

## Stakeholders affected
<!-- Who needs to know or act -->

## Testing required
<!-- What must be tested before go-live -->

| Test | Tester | Data | Success Criteria |
|------|--------|------|------------------|
| <test> | <name> | <data> | <criteria> |

## Rollback plan
<!-- How to undo if the change fails -->

## Risk level
<!-- Low | Medium | High | Critical -->

## Approval required
<!-- Who must approve before implementation -->

## Owner
<!-- Who drives this assessment and the change -->

## Related changes
<!-- Links to other change impact assessments -->
```

Also produce an **Affected Component List** and a **Test Plan**.

## Quality gates

- [ ] The change is described with exact object names, table/field references, and current versus proposed values.
- [ ] At least one direct consumer (program, report, transaction) was identified through where-used search.
- [ ] All interfaces that touch the changed object were checked and documented.
- [ ] All business process steps that depend on the object were identified.
- [ ] Each affected component has a risk rating and a required action.
- [ ] A test plan exists with named testers, test data, and success criteria.
- [ ] A rollback plan exists and has been validated as technically feasible.
- [ ] The assessment was reviewed by the functional owner and change manager before approval.

## References

- `references/method.md` — Detailed where-used search, consumer mapping, and risk assessment.
- `references/templates.md` — Copy-ready templates for Change Impact Assessment, Affected Component List, and Test Plan.
- `references/examples.md` — Good and bad examples from SAP payment terms, sales document types, and background job schedule changes.

## Safety rules

- Separate facts from assumptions. Label assumptions about consumer behavior and test data representativeness.
- Separate decisions from open questions. List open questions about unverified interfaces or missing where-used data.
- Do not expose client names, internal system names, or proprietary configuration details.
- Do not copy proprietary framework text. Use your own words.
- Do not invent system names or interface IDs. Use only the systems, interfaces, and objects the user confirms exist.
