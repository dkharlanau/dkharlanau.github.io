# Operational Knowledge Capture — Examples

## Good Example: The "Magic" Transaction Sequence for Stuck IDocs

**Situation:** IDocs in status 64 that should have processed but did not.

**Symptom:** IDoc status 64, no error, not processing.

**What was done:**
1. Run BD87 for the IDoc number
2. Check partner profile in WE20 — found mismatch in partner type
3. Open WE19, copy the IDoc
4. Modify segment E1EDKA1 field PARVW to correct partner type
5. Post the modified IDoc
6. Verify in WE02 that status changes to 53

**Why it worked:** The partner profile mismatch caused the IDoc to be queued in status 64 instead of being processed. WE19 allows manual correction of the segment before posting. The corrected partner type matches the profile, so the IDoc processes normally.

**What was tried and failed:**
- Running RBDAPP01 (batch IDoc processing) — did not help because the partner profile mismatch prevents processing
- Manually changing status in WE02 — not possible for status 64
- Reprocessing via BD87 — failed because the partner type was still wrong

**Preconditions:**
- Applies to IDocs in status 64 only
- Applies when the error is a partner profile mismatch
- Does NOT apply to status 51 (syntax errors) or status 56 (IDoc ready for dispatch)

**Limitations:**
- Does not fix the partner profile itself; only corrects the individual IDoc
- Does not prevent future mismatches
- Requires authorization for WE19

**Verification:**
- Check WE02 for status 53
- Verify the business document was created correctly

**Why this is good:** Exact steps, causal explanation, failed attempts documented, clear preconditions and limitations.

---

## Bad Example: "Run Program X and It Works"

**Situation:** Customer master data issue.

**Capture:** "Run program Z_CUSTOMER_FIX and it works."

**Why this is bad:**
- No transaction codes
- No causal explanation
- No preconditions
- No limitations
- No failed attempts
- No verification method
- No system or client specified

**Good capture:**
- "Run program Z_CUSTOMER_FIX in client 100 with parameter P_DATE = today."
- "This program updates the customer credit segment table KNKK when the credit management area is missing."
- "Precondition: customer must have a credit control area assigned in FD32."
- "Limitation: does not fix customers without any credit control area at all."
- "Verification: run report RFDKLX10 and verify credit limit is displayed."

---

## Good Example: Weekend Restart Procedure Missing Step

**Situation:** After every planned restart, qRFC queues fail to process.

**Symptom:** SMQ1 shows thousands of queued messages after restart.

**What was done:**
1. Check SMQ1 for queued messages
2. Check SM58 for tRFC errors
3. Found: one RFC destination is not available
4. Verify destination in SM59
5. Restart the destination service
6. Release queues in SMQ1

**Why it worked:** The restart procedure did not include a step to verify RFC destination availability before releasing queues. One destination handles CRM replication and was not ready when queues were released. By verifying the destination first, queues process successfully.

**Prevention:** Update the restart runbook with the verification step.

**Why this is good:** The capture identified a process gap, not just a technical fix. The runbook update prevents recurrence.

---

## Bad Example: Private Notes on Local Drive

**Situation:** A consultant resolves a complex pricing issue.

**Capture:** Notes saved in a local text file on the consultant's laptop.

**Result:** Consultant leaves the project. The next consultant encounters the same issue and spends 4 hours re-discovering the solution.

**Why this is bad:**
- Knowledge is not discoverable
- No one else can access it
- No review or update process
- No linking to related knowledge

**Good practice:**
- Store in the team wiki or knowledge base
- Tag with "pricing," "condition type," "VK11"
- Link to related Atlas pages
- Set a review date
- Notify the business owner that operational knowledge has been captured
