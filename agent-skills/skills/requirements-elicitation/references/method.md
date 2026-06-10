# Requirements Elicitation — Detailed Method

## The Classification-First Method

Stakeholders rarely state requirements. They state complaints, solutions, wishes, and constraints. The core of this skill is classifying every raw statement before writing any requirement.

### Step 1: Raw Statement Collection

Gather everything stakeholders have said:
- Emails and meeting notes
- Tickets and incident descriptions
- Proposals and change requests
- Complaints and escalations

Do not filter or summarize yet. The filtering happens in Step 2.

### Step 2: Statement Classification

Label each statement as exactly one of:
- **Need:** the underlying problem or opportunity
- **Solution idea:** a proposed way to address the need
- **Assumption:** something the stakeholder believes is true
- **Constraint:** a hard limit that cannot be changed
- **Risk:** something that could go wrong
- **Complaint:** a statement of dissatisfaction without a clear need

Use a table for classification:

| Raw Statement | Classification | Source | Owner |
|---------------|----------------|--------|-------|
| "The system is too slow" | Complaint + Need (implied) | Interview | Warehouse Manager |
| "Add a new index" | Solution idea | Email | IT Lead |
| "We have 500 line items per shift" | Assumption | Meeting | Operations |

### Step 3: Need Extraction

For every solution idea, ask: "What problem does this solve?"

Example:
- Solution idea: "Add a new index"
- Problem it solves: "Goods receipt posting takes more than 30 minutes for 500 line items"
- Need: "Post 500 line items within 30 minutes during peak shift"

Discard the solution idea unless it is a constraint (e.g., "must use existing database").

### Step 4: Testable Requirement Writing

Format: "The system/process must [action] so that [outcome]."

Each requirement must be verifiable. Test for verifiability:
- Can a tester check whether this is met? If no, rewrite.
- Does it contain measurable thresholds? If no, add them.
- Does it reference specific fields, tables, or transactions? If no, add them or flag as open question.

Bad: "The system must be fast."
Good: "The system must post 500 goods receipt line items within 30 minutes during peak shift."

### Step 5: Missing Context Identification

For each requirement, list what you do not know:
- Field names or table names
- Transaction codes
- Volume estimates
- Owner names
- System versions

Flag these as open questions with assigned discovery owners.

### Step 6: Business Rule Mapping

Identify rules that constrain the requirement:
- Regulatory rules
- Company policies
- System limitations
- Integration contracts

Document rules separately so they can be validated independently of the requirement.

### Step 7: Owner Validation

Walk through each requirement with the named business owner. Confirm:
- The requirement matches their intent
- The acceptance criteria are acceptable
- The assumptions are valid
- The risks are acknowledged

Revise based on feedback. Do not finalize without owner confirmation.

### Step 8: Brief Packaging

One brief per distinct business need. Link related briefs. Include traceability to source statements.

If a brief contains more than one need, split it. If two briefs address the same need, merge them.

## Common Elicitation Pitfalls

1. **Recording solutions as requirements.** The team builds what was asked, not what was needed.
2. **Skipping acceptance criteria.** No way to verify delivery. Disputes continue indefinitely.
3. **Failing to document assumptions.** Requirements break when assumptions turn out false.
4. **Hiding stakeholder conflicts.** Late-stage scope disputes when conflicts surface during testing.
5. **Writing requirements without system verification.** Requirements reference non-existent fields or transactions.
