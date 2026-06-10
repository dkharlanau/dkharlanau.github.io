# Incident Triage — Examples

## Good Example: Sales Orders Stuck in Delivery Block

**Ticket:** "40 sales orders created this morning are blocked for delivery."

**Triage process:**
1. Read ticket: 40 orders, all from this morning, all blocked for delivery
2. Business impact: High (single process blocked, but 40 orders and time-sensitive)
3. Technical domain: Master data (delivery block reason)
4. Recent changes: None in last 48h
5. Containment: None needed (orders are already blocked, not creating more)
6. Owner routing: Check if all 40 share a common data object
   - Found: all share the same newly created ship-to party
   - Ship-to party was replicated from MDG with incomplete address
   - Owner: BP/MDG data steward (not SD functional team)
   - Question: "Why was this ship-to party replicated with an incomplete address, and how do we validate future replications?"

**Triage record:**
- Impact: High
- Domain: Master data
- Containment: None (already contained by block)
- Owner: MDG Data Steward
- Question: Specific, about replication validation

**Why this is good:** The triage did not start debugging delivery block reasons in VBAK/VBAP. It found the common data object and routed to the correct owner.

---

## Bad Example: "System Not Working"

**Ticket:** "System not working."

**Bad triage:**
- Open SM37, check all jobs
- Open ST22, look for dumps
- Open SM21, scan system log
- Assign to "AMS Team" with "please investigate"

**Result:** 3 hours of random checking. No classification. No containment. No specific question. Ticket bounces between Basis, functional, and integration teams.

**Why this is bad:**
- No error message or screenshot requested
- No business impact classification
- No technical domain classification
- No recent change check
- No containment action
- Generic owner assignment
- No reporter update

**Good triage:**
- Ask for error message, screenshot, system, transaction, number of affected users
- If no response, classify as Low and ask for more info before technical assignment
- If multiple users affected, classify as High and ask for common symptom

---

## Good Example: IDoc Status 51 After Weekend Transport

**Ticket:** "Interface broken. 200 IDocs in status 51."

**Triage process:**
1. Read ticket: 200 IDocs, status 51, Monday morning
2. Business impact: Critical (integration down, downstream system not receiving data)
3. Technical domain: Integration
4. Recent changes: Transport on Saturday included segment version change
5. Containment: Queue new IDocs, do not let them accumulate
6. Owner routing: Integration team
   - Question: "The segment version changed in Saturday's transport but the sender system was not updated. Should we roll back the segment change or coordinate a sender update?"

**Why this is good:** The triage connected the symptom to the recent transport. Containment prevented more IDocs from failing. The question is specific and includes two options.

---

## Bad Example: Background Job Cancellation

**Ticket:** "Billing did not run."

**Bad triage:**
- Assign to ABAP team: "Please check the billing program."
- ABAP team reviews code for 2 hours
- No issue found in code

**Good triage:**
- Check SM37 for job log
- Found: job cancelled due to table space issue
- Check with Basis: database maintenance window ran longer than expected
- Domain: Infrastructure
- Owner: Basis team
- Question: "Why did the maintenance window overlap with the billing job schedule, and how do we prevent this?"

**Why this is good:** The triage checked the job log before assigning to functional or ABAP teams. The root cause was infrastructure, not code.
