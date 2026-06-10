# Interface Ownership — Examples

## Good Example: IDoc Failures Sit Unresolved

**Situation:** Customer master IDocs from SAP to a CRM are failing with status 51. The SAP basis team says the IDoc is correct. The CRM team says the data is wrong. The middleware team says the routing is fine. After three days, a sales manager complains that new customers cannot be created.

**Ownership analysis:**
- Business owner: missing (no one approves schema changes)
- Technical owner: Integration team (maintains the IDoc segment)
- Operational owner: AMS team (monitors WE02)
- Consumer representative: missing (no one speaks for CRM)

**Gap resolution:**
- Assign MDM Lead as business owner (owns customer master semantics)
- Assign CRM Lead as consumer representative
- Update matrix within 48 hours
- Schedule incident drill

**Why this is good:** The gap was not just "no owner" but "wrong type of owner." The technical owner was present but could not resolve a semantic disagreement. The business owner and consumer representative were the missing pieces.

---

## Bad Example: Schema Change Without Approval

**Situation:** A developer adds a mandatory field to a customer API to support a new project. Two downstream systems start failing because they do not send the new field.

**Ownership analysis:**
- No business owner was documented for the API
- No change approval process existed
- The developer assumed it was safe because "it's just one field"

**Result:** Production incident, two downstream systems down for 6 hours, emergency rollback.

**Why this is bad:**
- No business owner to approve schema changes
- No consumer representative to validate compatibility
- No change process for interface modifications
- The ownership matrix did not exist or was not consulted

---

## Good Example: AMS Team Lacks Business Context

**Situation:** The AMS monitoring tool alerts on a failed file transfer. The AMS operator can see the technical error but does not know which business process is affected, who validates the file content, or whether the failure is urgent.

**Ownership analysis:**
- Operational owner: AMS team (receives alert)
- Business owner: Finance Manager (owns the file content)
- Consumer representative: Treasury team (uses the data)
- Gap: AMS operator does not know who to contact

**Resolution:**
- Add business owner and consumer representative contact info to the alert
- Create a runbook: "File transfer failure → contact Finance Manager for content validation, Treasury for urgency assessment"
- Update the ownership matrix with escalation paths

**Why this is good:** The gap was not missing ownership but missing operational context. The runbook connects the operational owner to the business owner.

---

## Bad Example: Vendor Owns Everything

**Situation:** An external vendor manages all integrations. The internal team assumes the vendor owns everything.

**Ownership analysis:**
- Business owner: missing (internal accountability)
- Technical owner: vendor (but internal team does not know who)
- Operational owner: vendor (but internal AMS cannot contact them directly)
- Consumer representative: missing

**Result:** When the vendor is slow to respond, the internal team has no escalation path. Business users blame IT. IT blames the vendor. Incidents sit unresolved.

**Why this is bad:**
- Internal business owner is essential even with a vendor
- Internal operational owner must know how to escalate to the vendor
- Consumer representative must be internal (the vendor does not know internal consumers)
- Vendor ownership does not replace internal ownership
