---
name: incident-triage
description: Use when a ticket arrives with a vague subject like "system not working," when multiple users report the same symptom through different channels, when an interface failure is blocking downstream processes, or when a background job failed and you need to decide if this is one-off or systemic. Produces a Triage Record with classification, containment, and routing. Do not use for root cause analysis or permanent fix design.
---

# Incident Triage

## Purpose

Classify incidents fast, contain business impact, and route to the right owner without wasting time on premature diagnosis.

## Use when

- A ticket arrives with a vague subject like "system not working" and no error message.
- Multiple users report the same symptom through different channels (ticket, chat, email).
- An interface failure is blocking downstream processes and business users are escalating.
- A background job failed and you need to decide if this is a one-off or a systemic issue.
- A production change went live and unexpected errors are appearing in multiple areas.

## Do not use when

- The incident has been classified and contained and you need to find the permanent fix (use `root-cause-analysis`).
- You are designing a monitoring or alerting system (use `integration-observability`).
- The issue is a known recurring pattern that needs systemic analysis (use `recurring-ticket-pattern-analysis`).

## Required inputs

- The original ticket or alert with timestamp, reporter, and initial description.
- System landscape map or at least a list of systems in the scope (DEV, QAS, PRD, MDG, PI/PO/CPI).
- Interface ownership matrix or a list of known interfaces and their owners.
- Monitoring tool access: SM37, SM58, SMQ1/SMQ2, WE02/WE05, SLG1, ST22, DBACOCKPIT.
- Contact list for functional teams, Basis, security, data stewards, and integration.
- Recent change log: transports, configuration changes, master data loads, password policy updates.

## Workflow

1. **Read the ticket once.** Do not start debugging. Extract: reporter, timestamp, system, transaction, error text, number of affected items, business process.
2. **Classify by business impact.**
   - Critical: revenue-impacting process stopped for multiple users.
   - High: single user or small group blocked on a time-sensitive process.
   - Medium: workaround exists, no immediate business deadline.
   - Low: cosmetic, reporting lag, or single non-urgent request.
3. **Classify by technical domain.** Map the symptom to one of: master data, configuration, custom code, integration, infrastructure, security, user error, or unknown.
4. **Check for recent changes.** Look at transport logs, change documents, transport of copies, and scheduled jobs in the last 48 hours.
5. **Contain the impact.**
   - If data is being created incorrectly, stop the creation process.
   - If an interface is failing, pause or queue the messages.
   - If a job is failing, disable the schedule until the cause is known.
   - If users are locked out, apply an emergency workaround and document it.
6. **Route to the right owner.** Use the interface ownership matrix and team contact list. Do not assign to "AMS team" as a whole. Assign to a named functional area with a specific question.
7. **Document the triage decision.** Record classification, containment action, owner assignment, and what you checked.
8. **Set expectations.** Tell the reporter: what you found, what you did, who is working on it, and when they will hear next.

## Decision rules

- If the ticket has no error message and no screenshot, ask for both before assigning to a technical team.
- If the symptom matches a recent transport or config change, assign to the team that performed the change first.
- If multiple users are affected and the symptom is identical, treat as systemic and escalate to the relevant functional lead.
- If the symptom is scattered across modules with no common data object, check infrastructure and integration first.
- If an interface is involved, check the IDoc or message status before checking application logic.
- If a background job failed, check SM37 for the job log and ST22 for dumps before asking the functional team.
- If master data is involved, verify the data object in the source system before assuming SAP is misconfigured.
- If containment requires a system change, get approval from the change manager or document it as an emergency change.

## Output format

Produce an **Incident Triage Record**:

```markdown
---
artifact: Incident Triage Record
id: TRI-001
date: YYYY-MM-DD
reporter: Name / Team
---

## Symptom
<!-- What was reported. Exact error text if available. -->

## System / Transaction
<!-- Where it happened -->

## Business impact
<!-- Critical / High / Medium / Low. Quantify if possible. -->

## Number affected
<!-- Users, records, orders, IDocs -->

## Recent changes (last 48h)
<!-- Transports, config, data loads, patches -->

## Technical domain
<!-- master data | config | code | integration | infrastructure | security | user error | unknown -->

## Containment action
<!-- What was stopped, paused, or worked around -->

## Owner assigned
<!-- Name and team. Specific question they must answer. -->

## Next update
<!-- When the reporter will hear back -->

## Related tickets
<!-- Links to similar or duplicate tickets -->
```

Also produce an **Owner Assignment Note** and a **Containment Log**.

## Quality gates

- [ ] The triage record names the exact system and transaction where the symptom was observed.
- [ ] Business impact is classified and quantified (users affected, orders blocked, cost per hour).
- [ ] At least one containment action was taken or a clear reason is given why none was needed.
- [ ] The owner assignment includes a named team or person, not a generic queue.
- [ ] Recent changes in the last 48 hours were checked and documented.
- [ ] The reporter received an update with expected next communication time.
- [ ] No premature technical diagnosis was made before classification and containment.

## References

- `references/method.md` — Detailed classification method, containment techniques, and routing logic.
- `references/templates.md` — Copy-ready templates for Triage Record, Owner Assignment Note, and Containment Log.
- `references/examples.md` — Good and bad examples from SAP SD blocks, IDoc failures, and background job cancellations.

## Safety rules

- Separate facts from assumptions. State clearly what is known from the ticket and what is inferred. Label every inference as an assumption.
- Separate decisions from open questions. List open questions about missing logs or unverified system states.
- Do not expose client names, ticket numbers, or internal incident IDs.
- Do not copy proprietary framework text. Use your own words.
- Do not debug prematurely. The agent's job is classification, containment, and routing — not root cause analysis.
