# Requirements Elicitation — Examples

## Good Example: SAP Rollout — "The System Is Too Slow"

**Raw statement:** "The system is too slow during goods receipt posting."

**Classification:** Complaint + implied Need

**Need extraction:** "Post 500 line items within 30 minutes during peak shift."

**Requirement:** "The goods receipt posting process must handle 500 line items within 30 minutes during the peak shift window (06:00–10:00), with concurrent users up to 20, without transaction timeouts."

**Acceptance criteria:**
- Given 500 line items and 20 concurrent users, when goods receipt is posted during 06:00–10:00, then all items post within 30 minutes and no timeout occurs.

**Why this is good:** The vague complaint became a testable requirement with specific numbers, time window, and concurrency.

---

## Bad Example: "Just Move Everything"

**Raw statement:** "Migrate all customer master data to the new SAP S/4 system."

**Bad requirement:** "Migrate all customer master data to SAP S/4."

**Why this is bad:**
- "All" is undefined. Does it include inactive customers?
- No deduplication rules specified
- No tax validation specified
- No cut-off date specified
- No acceptance criteria
- No test data identified

**Good requirement set:**
- "Migrate all customers with status 'Active' in the source system as of the cut-off date."
- "Zero duplicate account groups may be created in the target system."
- "All tax numbers must pass country-specific validation before migration."
- "Migration must complete within the 48-hour maintenance window."

---

## Good Example: Post-Incident — "This Should Never Happen Again"

**Raw statement:** "After a sales order bypassed credit check due to a missing credit segment, the sales manager says this should never happen again."

**Classification:** Need (implied from incident)

**Need:** "Prevent sales order creation when credit segment is missing."

**Requirement:** "The system must block sales order creation when the credit segment is missing, route the order to the credit team, and alert the credit team within 15 minutes."

**Acceptance criteria:**
- Given a customer without a credit segment, when a sales order is created, then the system blocks with status 'Credit block' and sends an alert to the credit team within 15 minutes.

**Why this is good:** The requirement addresses the root cause (missing credit segment), not just the symptom (bypassed check). It includes routing and alerting.

---

## Bad Example: Solution Disguised as Requirement

**Raw statement:** "We need a custom report to show open orders by credit status."

**Bad requirement:** "The system must provide a custom report showing open orders by credit status."

**Why this is bad:** This is a solution, not a need. The underlying need might be: "Credit team needs visibility of orders blocked for credit review so they can prioritize clearance."

**Better approach:**
- Need: "Credit team needs to prioritize order clearance by risk and age."
- Requirement: "The system must display a prioritized list of credit-blocked orders, sortable by credit risk category and block age, accessible to the credit team without custom development."
- This opens the door to using standard SAP transactions (VKM1/VKM4) instead of building a custom report.
