# Acceptance Criteria — Detailed Method

## The Given/When/Then Method

Acceptance criteria turn requirements into testable statements. The core technique is breaking each requirement into scenarios with preconditions, actions, and expected outcomes.

### Step 1: Requirement Testability Check

Before writing criteria, verify the requirement is testable:
- Does it contain vague qualifiers (fast, secure, user-friendly)? If yes, rewrite the requirement first.
- Does it reference specific fields, transactions, or systems? If no, flag as open question.
- Can a tester verify it without asking the author what was meant?

If the requirement fails this check, return it to elicitation.

### Step 2: Scenario Decomposition

For each requirement, identify:
- **Precondition:** what must be true before the action
- **Action or event:** what happens
- **Expected outcome:** what must be true after

Write at least three scenarios:
1. **Normal case:** standard, expected input
2. **Boundary case:** edge of valid range, large volume, last item
3. **Error case:** invalid input, missing data, system failure

### Step 3: Given/When/Then Writing

Format:
```
Given <precondition>
When <action or event>
Then <expected outcome>
```

Rules:
- Given: state the data, user, or system state explicitly
- When: state the action or trigger explicitly
- Then: state the observable outcome explicitly

Bad:
```
Given a customer
When I create an order
Then it works
```

Good:
```
Given a customer with credit limit 50,000 EUR and open order value 45,000 EUR
When a new order of 10,000 EUR is created
Then the system blocks the order with status "Credit block" and routes it to the credit team
```

### Step 4: Non-Functional Criteria

For each requirement, add:
- **Performance:** response time, throughput, concurrency
- **Availability:** uptime percentage, recovery time
- **Security:** access control, audit trail, encryption
- **Compliance:** regulatory requirements, data retention

Each must have a specific metric or threshold.

Bad: "The system must be fast."
Good: "The system must respond within 2 seconds for 95% of requests under normal load."

### Step 5: Edge Case Identification

Identify at least three edge cases per requirement:
- **Normal case:** standard input, expected behavior
- **Boundary case:** maximum volume, minimum value, last record
- **Error case:** missing data, invalid input, downstream failure

If edge cases are missing, the criterion is incomplete.

### Step 6: Test Data Definition

State exactly:
- What data is needed
- In which system
- How to obtain or create it
- Whether anonymization is required

If test data does not exist in test systems, flag a test environment gap.

### Step 7: Sign-Off Owner Identification

Name the person who will approve that criteria are met. Verify:
- They have authority to approve
- They understand the criteria
- They are available during testing

If the sign-off owner is not the requirement owner, verify their authority.

### Step 8: Criteria Packaging

One Acceptance Criteria Set per requirement. Link to the Requirements Brief. Include:
- Scenarios (Given/When/Then)
- Non-functional criteria
- Edge cases
- Test data requirements
- Verification method
- Sign-off owner

## Common Criteria Pitfalls

1. **Repeating the requirement without adding verifiability.** Still no way to test.
2. **Including implementation instructions.** Constrains the solution unnecessarily.
3. **Forgetting edge cases.** Production failures on exceptions never tested.
4. **Omitting non-functional criteria.** Passes functional tests but fails under load.
5. **Not identifying test data.** Testing blocked because no one can create required data.
