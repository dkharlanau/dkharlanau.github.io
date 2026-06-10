# Root Cause Analysis — Detailed Method

## The Three-Layer Trace Method

The core of this skill is separating symptom, immediate cause, and root cause. Most failures stop at the immediate cause and miss the systemic gap that allows recurrence.

### Step 1: Symptom Confirmation

Reproduce or verify the reported defect with your own eyes. Do not rely on second-hand descriptions.

Document:
- Exact error text
- Transaction code
- Record IDs or document numbers
- Screenshots (if available)
- Timestamp of observation

If the symptom cannot be reproduced, stop and gather more data before building theories.

### Step 2: Defect Boundary Definition

Determine the scope:
- Affected system(s)
- Affected module(s)
- Affected document type(s)
- Time window of first occurrence
- Number of records affected
- Whether the defect is ongoing or historical

### Step 3: Timeline Building

List events in chronological order:
- Last known success (when did this work correctly?)
- First failure (when was the defect first observed?)
- Changes in the window (transports, config, data loads, maintenance)
- Maintenance windows
- User actions
- System restarts

Use system logs and change documents. Do not guess at chronology.

### Step 4: Immediate Cause Identification

What directly produced the symptom? State it in one sentence.

Examples:
- "The incompletion procedure added a mandatory field that existing open orders do not have."
- "The RFC destination was unavailable during queue release after restart."
- "The condition record expired and was not extended."

### Step 5: Root Cause Tracing

Ask "why" up to five times or until you reach a process, configuration, or governance gap.

Example trace:
- Symptom: Batch job cancellation every night at 02:00
- Immediate cause: Missing required field in 3% of orders
- Why? Incompletion procedure change added a mandatory field
- Why? The transport changed the incompletion procedure without data migration
- Why? The change process does not require data impact assessment for incompletion procedure changes
- Root cause: Missing change process step — data impact assessment for incompletion procedure changes

The root cause is the thing that, if fixed, prevents recurrence.

### Step 6: Entry Point Identification

Where in the lifecycle did the defect first enter?
- User entry (manual transaction)
- Interface (IDoc, API, file)
- Batch job
- System replication
- Manual configuration change
- Code change (transport)

Name the exact system, transaction, interface, or user action.

### Step 7: Defect Classification

Use one of:
- **Data:** incorrect, missing, or inconsistent data
- **Configuration:** wrong or missing system setting
- **Custom code:** ABAP enhancement, user exit, or custom program defect
- **Process:** missing or incorrect business process step
- **Integration:** interface failure or mismatch
- **Infrastructure:** server, database, network issue
- **User error:** incorrect action without system guardrail
- **Unknown:** cannot determine with available data

### Step 8: Business Impact Quantification

Count:
- Affected records
- Blocked orders or invoices
- Delayed processes
- Revenue at risk
- Hours lost

If exact numbers are unavailable, state the estimation method.

### Step 9: Correction Design

Choose a method:
- **Manual correction:** for small numbers with clear rules
- **Mass update with validation:** for larger numbers; include sample check and approval
- **Reprocessing:** for batch or integration failures where source is now correct
- **Reversal:** for incorrect postings or billing documents
- **Configuration rollback:** for config changes that caused the defect

### Step 10: Prevention Control Design

The prevention must address the root cause, not the symptom:
- Missing validation → add validation at entry point
- Process gap → add process step with owner and deadline
- Monitoring gap → add monitoring (only if a fix is genuinely impossible)
- Training gap → add guided workflow or guardrail (not just "better training")

### Step 11: Owner and Deadline Assignment

Name specific people or teams:
- Correction owner
- Prevention owner
- Validation owner

Set realistic deadlines. Do not let the RCA sit in a document repository.

## Common RCA Pitfalls

1. **Treating the symptom as the root cause.** The defect recurs because the upstream validation was never fixed.
2. **Stopping at the immediate cause.** You fix the failed IDoc but the sender system keeps sending invalid data.
3. **Not checking for recurrence.** You treat a systemic issue as a one-off.
4. **Proposing prevention that is too expensive or complex.** The prevention is never approved, and no simpler control was proposed.
5. **Failing to name owners and deadlines.** The RCA sits in a document repository and nothing changes.
