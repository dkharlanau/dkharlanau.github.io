# Recurring Ticket Pattern Analysis — Examples

## Good Example: Monthly "Customer Not Found" IDoc Failures

**Pattern:** Every month, 10–15 tickets report IDoc failures with status 51 and error "customer not found."

**Frequency analysis:**
- 12 tickets in January, 14 in February, 11 in March
- All occur in the first week of the month
- All involve customers created in downstream CRM

**Timeline correlation:**
- CRM-to-SAP replication batch job runs on the 1st of each month
- Customer approval workflow completes by the 3rd
- Batch job runs before approval workflow completes

**Cost quantification:**
- Handling cost: 13 tickets/month × 2 hours × $100/hour = $2,600/month
- Business cost: delayed orders, customer complaints
- Annual handling cost: ~$31,200

**Root cause:** CRM batch schedule runs before customer approval workflow completes. Unapproved customers are replicated to SAP and fail because they are incomplete.

**Prevention proposal:** Change CRM batch schedule to run after approval workflow completion.

**Prevention cost:** 4 hours of scheduling change = $400

**ROI:** $31,200 / $400 = 78×

**Why this is good:** Specific numbers, clear timeline correlation, quantified cost, simple prevention with high ROI.

---

## Bad Example: "We Have a Lot of IDoc Tickets"

**Analysis:**
- "We get a lot of IDoc tickets."
- "Maybe 10 per month?"
- "They take a while to fix."
- "We should monitor IDocs better."

**Prevention proposal:** "Add IDoc monitoring dashboard."

**Why this is bad:**
- No exact ticket count
- No classification by symptom
- No timeline correlation
- No cost quantification
- No root cause analysis
- Prevention is monitoring (detection), not a fix
- No business case

---

## Good Example: Quarterly Pricing Condition Expiration

**Pattern:** Every quarter, pricing team opens tickets because a specific customer group sees incorrect prices.

**Frequency analysis:**
- 8 tickets per quarter
- All in the first week of the new quarter
- All involve the same condition type

**Timeline correlation:**
- Condition type expires on the last day of the quarter
- Validity period is not extended until after expiration
- Manual extension is the standard resolution

**Cost quantification:**
- Handling cost: 8 tickets × 3 hours × $100/hour = $2,400/quarter
- Business cost: customer complaints, manual credit notes
- Annual handling cost: ~$9,600

**Root cause:** Pricing condition maintenance process does not include proactive expiration monitoring.

**Prevention proposal:** Scheduled report that alerts the pricing team 14 days before expiration.

**Prevention cost:** 8 hours to create report = $800

**ROI:** $9,600 / $800 = 12×

**Why this is good:** The pattern is predictable and preventable. The prevention is a simple report, not a complex system change.

---

## Bad Example: Ignoring Business Cost

**Pattern:** Weekly delivery blocks on the same material.

**Analysis:**
- 50 tickets per year
- 1.5 hours per ticket
- Hourly rate: $80
- Handling cost: $6,000/year

**Prevention proposal:** "Update supplier data requirements and add inbound validation rule."

**Prevention cost:** $5,000

**Business case:** "Handling cost is $6,000/year. Prevention costs $5,000. ROI is 1.2×."

**Why this is bad:**
- Business cost (warehouse delays, expedited shipping, customer complaints) is ignored
- If business cost is $20,000/year, the real ROI is 5×
- Management rejects the proposal because the business case looks weak

**Good business case:**
- Handling cost: $6,000/year
- Business cost: warehouse delays ($15,000), expedited shipping ($8,000), customer complaints (unquantified but noted)
- Total cost: ~$29,000/year
- Prevention cost: $5,000
- ROI: 5.8×
