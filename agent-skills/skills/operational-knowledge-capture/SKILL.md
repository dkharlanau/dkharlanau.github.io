---
name: operational-knowledge-capture
description: Use when capturing knowledge after resolving a non-trivial incident, discovering a workaround for a known system limitation, or decoding complex configuration behavior. Produces an Operational Knowledge Capture Note that reduces repeat incidents and onboarding time. Do not use for generic documentation or training material creation.
---

# Operational Knowledge Capture

## Purpose

Turn firefighting into reusable knowledge: capture what was done, why it worked, and when it applies.

## Use when

- An incident was resolved after significant troubleshooting and the method should be reusable.
- A workaround was discovered for a known system limitation and other teams need to know it.
- A complex configuration or custom code behavior was decoded and the explanation should survive the person who found it.
- A new team member is joining and needs to understand how the landscape actually works, not just how it was designed.
- An AI agent or automation tool needs structured operational knowledge to handle routine incidents.
- A runbook or procedure was updated during an emergency and the update needs to be formalized.

## Do not use when

- The incident is still open and needs triage or root cause analysis.
- You are creating generic training material or user guides.
- The knowledge is already well-documented and discoverable.

## Required inputs

- The incident ticket or triage record with full symptom, resolution, and timeline.
- The exact transactions, programs, commands, or configuration paths used to resolve the issue.
- The system landscape where the resolution was applied: client, system, module.
- The business context: which process, which user group, which time window.
- What was tried that did not work — the failed attempts are as valuable as the success.
- The stakeholder who owns the process or data and can verify the knowledge is correct.
- Any related documentation, runbooks, or wiki pages that should be updated or linked.

## Workflow

1. **Capture immediately after resolution.** Do not wait. Schedule 15 minutes after every non-trivial incident to document.
2. **Record the situation.** What was happening? Which system, which process, which users, which time window? Include urgency and business impact.
3. **Record what was done.** Step by step. Include transaction codes, program names, table names, configuration paths, and exact values. Assume the reader has moderate SAP knowledge but no context about this specific landscape.
4. **Record why it worked.** Explain the system behavior, data flow, or configuration logic that made the fix effective.
5. **Record what almost went wrong.** Document failed attempts, wrong paths, assumptions that were false, and near misses.
6. **Define preconditions.** When does this knowledge apply? Which system version, which client, which module, which data state? Be explicit about exclusions.
7. **Define limitations.** What does this procedure not cover? What are the edge cases where it fails or needs escalation?
8. **Define verification.** How does the next person confirm the procedure is still valid? Which transaction, which report, which check?
9. **Name an owner.** Who maintains this knowledge? Who can answer questions if the note is unclear?
10. **Set a review date.** Operational knowledge rots. Systems change. Set a review date based on system stability: 3 months for volatile areas, 6 months for stable ones.
11. **Make it discoverable.** Store the note where people look for help. Tag it with symptom keywords, error messages, and transaction codes.
12. **Link related knowledge.** Connect to other capture notes, runbooks, or ticket histories that cover adjacent topics.

## Decision rules

- If the resolution took more than 30 minutes to find, it must be captured.
- If the same symptom has occurred twice, capture it and link both tickets to the note.
- If the fix involves a workaround for a known system limitation, capture it and flag it as temporary.
- If the fix requires access to a restricted system or elevated authorization, document the approval process.
- If the knowledge applies to only one client or system, state that explicitly. Do not generalize without verification.
- If a runbook already exists for this topic, update the runbook rather than creating a separate note.
- If the root cause is a bug or defect that will be fixed in a patch, set the review date to the patch release date and plan to retire the note.
- If the knowledge involves a custom program or enhancement, include the program name and version.

## Output format

Produce an **Operational Knowledge Capture Note**:

```markdown
---
artifact: Operational Knowledge Capture Note
id: OKC-001
date: YYYY-MM-DD
author: Name
topic: Incident | Procedure | Workaround | Decision
---

## Situation
<!-- What was happening. Context, urgency, systems involved. -->

## Symptom
<!-- Exact error, behavior, or observation -->

## What was done
<!-- Step by step. Commands, transactions, settings. -->

## Why it worked
<!-- Causal explanation, not just description -->

## What was tried and failed
<!-- Dead ends, wrong paths, false assumptions -->

## What almost went wrong
<!-- Near misses or risks that were avoided -->

## Preconditions
<!-- When this knowledge applies and when it does not -->

## Limitations
<!-- What this procedure does not cover -->

## Verification
<!-- How to confirm the procedure is still valid -->

## Owner
<!-- Who maintains this knowledge -->

## Review date
<!-- When this note should be revalidated -->

## Related knowledge
<!-- Links to other capture notes, runbooks, tickets -->
```

Also produce an **Updated Runbook or Wiki Page** if the knowledge fits an existing procedure, and a **Stakeholder Notification**.

## Quality gates

- [ ] The note was written within 24 hours of incident resolution.
- [ ] The symptom is described with exact error text, transaction, and at least one example record ID.
- [ ] The resolution steps are numbered and include exact transaction codes or program names.
- [ ] The causal explanation (why it worked) is present and distinct from the step description.
- [ ] At least one failed attempt or wrong path is documented.
- [ ] Preconditions and limitations are stated explicitly.
- [ ] A verification method is defined so the next person can confirm the note is still valid.
- [ ] An owner is named and a review date is set.
- [ ] The note is stored in a discoverable location with relevant tags or keywords.
- [ ] Related knowledge is linked: other notes, runbooks, tickets, or Atlas pages.

## References

- `references/method.md` — Detailed capture timing, causal explanation writing, and discoverability techniques.
- `references/templates.md` — Copy-ready templates for Knowledge Capture Note, Runbook Update, and Stakeholder Notification.
- `references/examples.md` — Good and bad examples from SAP IDoc clearing, restart procedures, and pricing condition maintenance.

## Safety rules

- Separate facts from assumptions. Label assumptions about system behavior and landscape specifics.
- Separate decisions from open questions. List open questions about verification methods or review dates.
- Do not expose client names, ticket numbers, internal incident IDs, or proprietary system details.
- Do not copy proprietary framework text. Use your own words.
- Do not generalize from one incident without verification. State exact scope.
