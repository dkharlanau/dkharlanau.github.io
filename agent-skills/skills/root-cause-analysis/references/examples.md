# Root Cause Analysis — Examples

## Good Example: Duplicate Customer Master Records

**Symptom:** Duplicate customers in the system blocking invoicing.

**Immediate cause:** Failed merge or missing uniqueness check.

**Root cause trace:**
- Why are there duplicate customers? Because the customer creation process allows manual entry in both SAP and CRM.
- Why does it allow manual entry in both? Because there is no uniqueness check against the central MDG system.
- Why is there no uniqueness check? Because MDG was implemented as a downstream system, not as the single point of entry.
- Root cause: Customer creation process bypasses MDG validation; MDG is not enforced as the single point of entry.

**Entry point:** CRM create API that bypasses MDG validation.

**Correction:** Data merge and deduplication run with survivorship rules.

**Prevention:** Enforce MDG as the single point of entry for customer creation; add uniqueness check at CRM entry.

**Why this is good:** The trace goes five levels deep. The root cause is a process and governance gap, not just a data error. Prevention addresses the entry point.

---

## Bad Example: "The IDoc Failed"

**Symptom:** IDoc status 51.

**Immediate cause:** "The IDoc failed."

**Root cause stated:** "Integration error."

**Correction:** "Reprocess the IDoc."

**Prevention:** "Monitor IDoc status more closely."

**Why this is bad:**
- No distinction between symptom, immediate cause, and root cause
- "Integration error" is a category, not a cause
- No trace to entry point
- Reprocessing is a symptom fix, not a root cause fix
- Monitoring is detection, not prevention

---

## Good Example: Sales Order Incompletion Procedure

**Symptom:** Batch job cancellation every night at 02:00.

**Immediate cause:** Missing required field in 3% of orders.

**Root cause trace:**
- Why is the field missing? Because a recent incompletion procedure change added a mandatory field.
- Why did existing orders not have the field? Because the transport changed the incompletion procedure without a data migration.
- Why was there no data migration? Because the change process does not require data impact assessment for incompletion procedure changes.
- Root cause: Missing change process step — data impact assessment for incompletion procedure changes.

**Entry point:** Transport that changed the incompletion procedure without data migration.

**Correction:** Mass update of the affected field with validation.

**Prevention:** Update change process to require data impact assessment for incompletion procedure changes.

**Why this is good:** The root cause is a process gap, not a data error. The prevention is a process change with clear ownership.

---

## Bad Example: qRFC Queue Buildup

**Symptom:** SMQ1 showing thousands of queued messages.

**Bad analysis:** "The system restart caused a backlog. We released the queues."

**Why this is bad:**
- The immediate cause (backlog after restart) is treated as the root cause
- No investigation of why the backlog happened
- No prevention beyond "be careful during restarts"

**Good analysis:**
- Why did queues build up after restart? Because the restart procedure does not verify RFC destination availability before releasing queues.
- Why does that matter? Because one destination was down for maintenance.
- Root cause: Restart runbook missing destination health check step.
- Prevention: Update runbook and add automated destination health check before queue release.
