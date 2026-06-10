# Data Governance Ownership — Detailed Method

## The Ownership Gap Method

Data governance fails when ownership is unclear. This method surfaces gaps systematically and closes them with named owners, decision rights, and enforcement mechanisms.

### Step 1: Domain Scoping

Do not try to govern all data at once. Pick one domain with visible pain:
- High incident count
- Audit finding
- Integration breakage
- Report reconciliation dispute

Scope criteria:
- 3–7 data elements maximum for the first pass
- At least one element with a known recent incident
- At least one element with cross-system consumption

### Step 2: System Landscape Mapping

For each data element, document:
- **Source system:** where the record is created or last modified authoritatively
- **System of record:** the system that holds the agreed master version
- **Consuming systems:** all systems that read or copy this data element
- **Transformation points:** where the value is changed, mapped, or derived

Common mistake: assuming the system of record is the same as the source system. In SAP landscapes, MDG may be the system of record while CRM is the source.

### Step 3: Stakeholder Identification

For each data element, identify four roles:
- **Business owner:** accountable for data quality and business semantics. Can approve changes.
- **Technical owner:** accountable for the systems that store and move the data.
- **Data steward:** day-to-day caretaker. Reviews, corrects, and monitors.
- **Consumer representative:** speaks for downstream systems. Validates compatibility.

If any role is missing, flag it as a gap. If a role is filled by a team rather than a named person, flag it as "ceremonial ownership."

### Step 4: Ownership Gap Analysis

For each gap, document:
- **Gap description:** what is missing
- **Business risk:** what happens because the gap exists
- **Proposed assignee:** who should fill the role
- **Confirmation status:** confirmed, proposed, or refused
- **Due date:** when the gap must be closed

Escalation rules:
- If two teams claim ownership, escalate to architecture or governance board
- If no one accepts ownership, assign to the business unit that loses most when the data is wrong
- If the steward lacks system access, treat as a high-priority access gap

### Step 5: Rule Cataloging

For each data element, collect:
- **Validation rules:** what must be true about the data
- **Access rules:** who can read, write, or approve changes
- **Retention rules:** how long the data must be kept
- **Synchronization rules:** how often and by what mechanism data is replicated

For each rule, document:
- **Enforcement point:** system, transaction, or API where the rule is checked
- **Failure action:** what happens when the rule is violated
- **Review frequency:** how often the rule is reviewed for correctness
- **Gap status:** none, process-only, or unenforced

### Step 6: Decision Rights Definition

For each data domain, document who can:
- **Create:** add new records
- **Update:** modify existing records
- **Delete:** remove records
- **Approve changes:** sign off on modifications
- **Approve access:** grant read or write permissions
- **Define rules:** change validation, retention, or synchronization policies

If the same person holds all rights, flag concentration risk. If no one holds a specific right, flag it as a decision gap.

### Step 7: Governance Action Plan Assembly

Combine all findings into a single prioritized plan:
- **P1:** ownership gaps on data elements with recent incidents
- **P2:** unenforced rules on high-consumption data elements
- **P3:** decision rights gaps on stable data elements
- **P4:** process improvements and review cycle establishment

Each action must have:
- Specific description
- Named owner
- Due date
- Success criteria
- Risk if not done

### Step 8: Validation and Review Cycle

Walk through the plan with each named owner. Confirm they:
- Understand the role
- Accept the authority
- Have the access and time to perform it

Set review cycle:
- Volatile domains: quarterly
- Stable domains: semi-annually
- Review owner: named person who schedules and runs the review

## Common Governance Pitfalls

1. **Proposing a tool before ownership is clear.** The tool enforces nothing if no one configures it.
2. **Naming a business unit instead of a person.** "Sales owns it" means no one owns it.
3. **Treating a policy document as governance.** Without enforcement, review, and consequence, a policy is paper.
4. **Defining governance for all data at once.** Scope collapse is the most common failure mode.
5. **Ignoring informal caretakers.** The person who already does the work may resist formalization if not consulted.
