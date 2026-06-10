# Incident Triage — Detailed Method

## The Classify-Contain-Route Method

The core of this skill is deciding what an incident is, who should handle it, and what to do in the first 15 minutes. It stops premature debugging and ensures business impact is contained before diagnosis begins.

### Step 1: Ticket Reading (No Debugging)

Read the ticket once. Extract:
- Reporter name and team
- Timestamp of first report
- System where the symptom was observed
- Transaction or process affected
- Error text (if any)
- Number of affected items (users, records, orders, IDocs)
- Business process affected

Do not start debugging. Do not open SM37 or WE02 yet. The goal is context, not diagnosis.

### Step 2: Business Impact Classification

Classify into one of four levels:

| Level | Definition | Examples | Response Time |
|-------|------------|----------|---------------|
| Critical | Revenue-impacting process stopped for multiple users | All orders blocked, all invoices failing | Immediate |
| High | Single user or small group blocked on time-sensitive process | Month-end closing blocked, one plant down | < 30 min |
| Medium | Workaround exists, no immediate business deadline | Report delay, non-urgent data correction | < 4 hours |
| Low | Cosmetic, reporting lag, or single non-urgent request | UI layout issue, one-off question | Next business day |

Quantify if possible: orders blocked, invoices delayed, cost per hour.

### Step 3: Technical Domain Classification

Map the symptom to one domain:
- **Master data:** incorrect or missing master data record
- **Configuration:** wrong or missing system configuration
- **Custom code:** ABAP enhancement, user exit, or custom program failure
- **Integration:** IDoc, RFC, API, or file transfer failure
- **Infrastructure:** server, database, network, or storage issue
- **Security:** authorization, authentication, or encryption issue
- **User error:** incorrect user action without system guardrail
- **Unknown:** cannot classify with available information

### Step 4: Recent Change Check

Look at the last 48 hours:
- Transport logs (STMS)
- Change documents (SCU3)
- Configuration changes
- Master data loads
- Password policy updates
- Scheduled job changes

Correlation is not causation, but it is the fastest filter. If a transport went live 6 hours before the first failure, treat it as the primary suspect until disproven.

### Step 5: Impact Containment

Take action to stop the damage from spreading:

| Symptom Type | Containment Action |
|--------------|-------------------|
| Data being created incorrectly | Stop the creation process or add validation |
| Interface failing | Pause or queue messages; do not let them accumulate |
| Job failing | Disable the schedule until cause is known |
| Users locked out | Apply emergency workaround and document it |
| Multiple incorrect records | Stop the batch or process creating them |

Document every containment action with timestamp and expected reversal condition.

### Step 6: Owner Routing

Assign to a named functional area with a specific question. Do not assign to "AMS team" as a whole.

Routing rules:
- Master data issue → Data steward or MDM team
- Configuration issue → Functional consultant for the module
- Custom code issue → ABAP developer or solution architect
- Integration issue → Integration team (after checking IDoc/message status)
- Infrastructure issue → Basis or infrastructure team
- Security issue → Security administration
- User error → Functional team + training assessment

Include a specific question: "Why are IDocs in status 51 for partner profile X?" not "Please investigate."

### Step 7: Triage Documentation

Record:
- Classification (impact level and technical domain)
- Containment action taken
- Owner assigned and specific question
- What was checked (recent changes, logs, scope)
- What is still unknown

This becomes the input for root cause analysis if needed.

### Step 8: Reporter Communication

Tell the reporter:
- What you found
- What you did
- Who is working on it
- When they will hear next

Set a specific next update time. Do not say "we are looking into it" without a time commitment.

## Common Triage Pitfalls

1. **Starting to debug before classifying.** You spend two hours tracing ABAP code when the issue is a missing address in a replicated business partner.
2. **Assigning to the wrong team because the symptom looks technical.** The ticket bounces between teams for days.
3. **Failing to contain impact while investigating.** More incorrect data is created, more IDocs fail, and cleanup multiplies.
4. **Not documenting the triage decision.** The next shift or the root cause analyst starts from scratch.
5. **Treating every incident as unique.** You miss patterns that would reveal a systemic failure.
