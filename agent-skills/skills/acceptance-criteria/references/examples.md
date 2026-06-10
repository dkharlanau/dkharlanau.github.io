# Acceptance Criteria — Examples

## Good Example: Credit Limit Check Rule

**Requirement:** "The system must enforce credit limits."

**Acceptance criteria set:**

```
Scenario: Normal case
Given a customer with a credit limit of 50,000 EUR and an open order value of 45,000 EUR
When a new order of 10,000 EUR is created
Then the system blocks the order with status "Credit block" and routes it to the credit team

Scenario: Boundary case
Given a customer with a credit limit of 50,000 EUR and an open order value of 49,999 EUR
When a new order of 2 EUR is created
Then the system blocks the order with status "Credit block"

Scenario: Error case
Given a customer with a missing credit limit
When a new order is created
Then the system blocks the order and alerts the credit team within 15 minutes

Non-functional criteria:
- Performance: credit check must complete within 2 seconds for 95% of orders
- Availability: credit check service must be available 99.5% during business hours

Edge cases:
- Emergency order under 1,000 EUR proceeds with warning and logs to audit
- Customer with multiple credit segments: check all segments, not just the first
```

**Why this is good:** Specific numbers, clear outcomes, boundary and error cases covered, non-functional criteria included.

---

## Bad Example: "The System Must Be Fast"

**Requirement:** "The system must be fast."

**Bad criteria:**
- "The system should respond quickly."
- "Users should not wait long."

**Why this is bad:**
- No measurable threshold
- "Quickly" and "not long" are subjective
- No test data identified
- No edge cases
- No non-functional criteria

**Good criteria:**
- "Given 100 concurrent users, when a sales order is created, then the system responds within 3 seconds for 95% of requests."
- "Given peak load (500 orders/hour), when orders are created, then no timeout occurs."

---

## Good Example: Data Migration — Customer Master

**Requirement:** "Migrate all active customers to the new system."

**Acceptance criteria:**
- "100% of customers with status 'Active' in the source system exist in the target system."
- "Matching fields: account group, tax number, payment terms."
- "Zero duplicate account groups are created."
- "All tax numbers pass country-specific validation."
- "Migration completes within the 48-hour maintenance window."
- "Given a customer with an invalid tax number, when migration runs, then the customer is rejected with error code TAX_INVALID and logged to the migration exception report."

**Why this is good:** Quantified coverage, specific fields, completeness rules, performance threshold, error handling specified.

---

## Bad Example: Implementation Detail in Criteria

**Requirement:** "The report must show open orders by credit status."

**Bad criteria:** "Use index Z_CREDIT_STATUS on table VBAK."

**Why this is bad:** The criterion constrains the solution. It tells the developer how to build it, not what the outcome should be.

**Good criteria:** "Given a user with report authorization, when the open orders report is run, then all orders with credit status 'Blocked' are displayed within 5 seconds, sortable by block reason and block age."
