---
layout: default
title: "Artifact Templates — Reusable Templates for Skill Hub Skills"
description: "Reusable Markdown templates for enterprise consulting and operations work. Data quality rules, root cause analysis notes, stakeholder briefs, architecture decision records, and more."
permalink: /skill-hub/artifact-templates/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Artifact Templates</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Foundation</p>
  <h1>Artifact Templates</h1>
  <p class="lead">Reusable templates that Skill Hub skills reference. Copy, fill, and use directly in tickets, documents, wikis, or agent outputs.</p>

  <section>
    <h2>Data Quality Rule</h2>
    <pre><code>---
artifact: Data Quality Rule
id: DQ-RULE-001
status: draft | approved | deprecated
---

## Field / Object
<!-- Example: Customer.TaxNumber1 -->

## Condition
<!-- Example: must be present when Customer.Country = DE -->

## Rule type
<!-- validation | completeness | consistency | timeliness | uniqueness -->

## Business process affected
<!-- Example: invoice creation, VAT reporting -->

## System of record
<!-- Example: SAP BP, MDG -->

## Owner
<!-- Business owner + technical owner -->

## Enforcement mechanism
<!-- Example: MDG workflow validation, batch check report, API schema constraint -->

## Failure action
<!-- Example: block creation, route to data steward, log for review -->

## Detection method
<!-- Example: daily DQ report, real-time API validation, IDoc status monitor -->

## Remediation owner
<!-- Who fixes records that fail this rule -->

## Related rules
<!-- Links to related DQ rules -->
</code></pre>
  </section>

  <section>
    <h2>Root Cause Analysis Note</h2>
    <pre><code>---
artifact: Root Cause Analysis Note
id: RCA-001
date: YYYY-MM-DD
author: Name
status: draft | reviewed | closed
---

## Symptom
<!-- What was observed. Be specific. -->

## Defect classification
<!-- data | config | code | process | integration | user error | unknown -->

## Affected scope
<!-- Systems, records, users, business areas, time period -->

## Root cause
<!-- The underlying reason the defect occurred. Not the symptom. -->

## Entry point
<!-- Where the defect entered the lifecycle. -->

## Business impact
<!-- Quantified if possible: orders blocked, invoices delayed, reports wrong -->

## Correction approach
<!-- How affected records or systems will be fixed -->

## Prevention control
<!-- What will stop this from recurring -->

## Owner
<!-- Who owns the fix and the prevention control -->

## Deadline
<!-- When correction and prevention must be complete -->

## Verification
<!-- How we will confirm the fix worked -->

## Related incidents
<!-- Links to tickets, IDocs, change requests -->
</code></pre>
  </section>

  <section>
    <h2>Remediation Backlog Item</h2>
    <pre><code>---
artifact: Remediation Backlog Item
id: REM-001
priority: P0 | P1 | P2 | P3
status: open | in-progress | blocked | done
---

## Problem statement
<!-- One sentence. What is wrong and why it matters. -->

## Root cause reference
<!-- Link to RCA note or analysis -->

## Affected records / scope
<!-- Count, sample IDs, date range -->

## Correction method
<!-- Manual | mass update | reprocessing | mapping fix | config change -->

## Validation approach
<!-- How we confirm the correction is correct before applying -->

## Approval required
<!-- Yes / No. If yes, from whom. -->

## Prevention follow-up
<!-- What control prevents recurrence -->

## Owner
<!-- Who drives this item to completion -->

## Effort estimate
<!-- Hours or days -->

## Target date
<!-- When this must be complete -->

## Dependencies
<!-- What must happen first -->

## Risks
<!-- What could go wrong during remediation -->
</code></pre>
  </section>

  <section>
    <h2>Stakeholder Interview Brief</h2>
    <pre><code>---
artifact: Stakeholder Interview Brief
id: SIB-001
date: YYYY-MM-DD
interviewer: Name
stakeholder: Name | Role | Area
---

## Context
<!-- Why this interview happened. What project or problem. -->

## Questions asked
<!-- Numbered list of questions from the skill page -->

## Answers given
<!-- What the stakeholder said. Use quotes where precise. -->

## Facts confirmed
<!-- Verifiable statements -->

## Assumptions surfaced
<!-- Things the stakeholder believes but has not verified -->

## Needs identified
<!-- What the stakeholder actually needs, not what they asked for -->

## Pain points
<!-- Specific complaints with context -->

## Constraints
<!-- Budget, time, policy, system limits -->

## Risks mentioned
<!-- What the stakeholder is worried about -->

## Decisions required
<!-- What the stakeholder cannot decide alone -->

## Follow-up actions
<!-- Who does what by when -->

## Related interviews
<!-- Links to other stakeholder briefs -->
</code></pre>
  </section>

  <section>
    <h2>Requirements Brief</h2>
    <pre><code>---
artifact: Requirements Brief
id: REQ-001
source: Stakeholder interview | Ticket | Audit | Regulation
status: draft | reviewed | approved
---

## Business need
<!-- The underlying need, not the solution -->

## Requirement statement
<!-- Clear, testable statement of what must be true -->

## Assumptions
<!-- What we are assuming to be true for this requirement to hold -->

## Business rules
<!-- Rules that constrain the solution -->

## Constraints
<!-- Technical, budget, time, policy limits -->

## Acceptance criteria
<!-- How we will know this requirement is met -->

## Priority
<!-- Must have | Should have | Could have | Won't have -->

## Owner
<!-- Business owner who can confirm this is correct -->

## Dependencies
<!-- Other requirements, systems, decisions -->

## Risks
<!-- What could make this requirement wrong or impossible -->

## Related requirements
<!-- Links to other requirement briefs -->
</code></pre>
  </section>

  <section>
    <h2>Acceptance Criteria Set</h2>
    <pre><code>---
artifact: Acceptance Criteria Set
id: AC-001
requirement: Link to requirement brief
status: draft | reviewed | approved
---

## Scenario: &lt;Name&gt;
Given &lt;precondition&gt;
When &lt;action or event&gt;
Then &lt;expected outcome&gt;

## Scenario: &lt;Name&gt;
Given &lt;precondition&gt;
When &lt;action or event&gt;
Then &lt;expected outcome&gt;

## Non-functional criteria
- Performance: &lt;metric&gt;
- Availability: &lt;metric&gt;
- Security: &lt;requirement&gt;
- Compliance: &lt;requirement&gt;

## Edge cases
- &lt;Edge case 1&gt;
- &lt;Edge case 2&gt;

## Test data requirements
<!-- What data is needed to verify these criteria -->

## Verification method
<!-- Manual test | Automated test | Review | Demonstration -->

## Sign-off owner
<!-- Who approves that criteria are met -->
</code></pre>
  </section>

  <section>
    <h2>Gap Analysis Note</h2>
    <pre><code>---
artifact: Gap Analysis Note
id: GAP-001
date: YYYY-MM-DD
scope: Process | System | Data | Organization
---

## Current state
<!-- What exists today. Be specific. -->

## Target state
<!-- What is required. Source: regulation, project scope, best practice. -->

## Gap description
<!-- The difference between current and target -->

## Gap type
<!-- missing | incomplete | inconsistent | outdated | ungoverned -->

## Business impact
<!-- What happens because of this gap -->

## Affected stakeholders
<!-- Who is impacted -->

## Closure approach
<!-- Build | Buy | Configure | Process change | Training -->

## Effort estimate
<!-- Rough sizing: small | medium | large | unknown -->

## Owner
<!-- Who is responsible for closing the gap -->

## Dependencies
<!-- What must happen first -->

## Risks
<!-- What could prevent closure -->

## Related gaps
<!-- Links to other gap notes -->
</code></pre>
  </section>

  <section>
    <h2>Architecture Decision Record</h2>
    <pre><code>---
artifact: Architecture Decision Record
id: ADR-001
date: YYYY-MM-DD
status: proposed | accepted | deprecated | superseded
---

## Context
<!-- What is the situation that forces a decision? -->

## Decision required
<!-- What exactly must be decided? -->

## Options considered

### Option 1: &lt;Name&gt;
- Description:
- Pros:
- Cons:
- Risks:

### Option 2: &lt;Name&gt;
- Description:
- Pros:
- Cons:
- Risks:

### Option 3: &lt;Name&gt; (if applicable)
- Description:
- Pros:
- Cons:
- Risks:

## Decision
<!-- Which option was chosen and why -->

## Consequences
<!-- What happens because of this decision — positive and negative -->

## Compliance / NFR implications
<!-- Security, performance, maintainability, cost -->

## Reversibility
<!-- How hard is it to reverse this decision later? -->

## Owner
<!-- Who owns this decision -->

## Review date
<!-- When should this decision be revisited? -->

## Related decisions
<!-- Links to other ADRs -->
</code></pre>
  </section>

  <section>
    <h2>Interface Ownership Matrix</h2>
    <pre><code>---
artifact: Interface Ownership Matrix
id: IOM-001
date: YYYY-MM-DD
scope: System landscape | Project | Domain
---

## Interfaces

| Interface ID | Source System | Target System | Direction | Data / Event | Business Owner | Technical Owner | Operational Owner | SLA | Status |
|--------------|---------------|---------------|-----------|--------------|----------------|-----------------|-------------------|-----|--------|
| IF-001 | SAP S/4 | Salesforce | Outbound | Customer BP | MDM Team | Integration Team | AMS Team | 4h | Active |

## Ownership gaps
<!-- Interfaces with missing or unclear owners -->

| Interface ID | Missing Role | Risk | Action | Owner | Due Date |
|--------------|--------------|------|--------|-------|----------|
| IF-002 | Business Owner | No one approves schema changes | Assign owner from Sales domain | Integration Lead | YYYY-MM-DD |

## Unowned interfaces
<!-- Interfaces discovered but not in any ownership model -->

## Change process
<!-- How ownership is updated when systems change -->

## Review frequency
<!-- How often this matrix is validated -->
</code></pre>
  </section>

  <section>
    <h2>Integration Failure Review</h2>
    <pre><code>---
artifact: Integration Failure Review
id: IFR-001
date: YYYY-MM-DD
status: open | closed | recurring
---

## Failure symptom
<!-- What was observed: error message, timeout, missing data, duplicate data -->

## Interface
<!-- Link to Interface Ownership Matrix entry -->

## Failure type
<!-- timeout | schema mismatch | auth failure | data validation | rate limit | downstream unavailable | unknown -->

## Time of failure
<!-- When it started, when it was detected, when it was resolved -->

## Affected scope
<!-- Systems, records, users, business processes -->

## Business impact
<!-- Quantified if possible -->

## Immediate response
<!-- What was done to stop the bleeding -->

## Root cause
<!-- Why the failure happened -->

## Permanent fix
<!-- What prevents recurrence -->

## Monitoring improvement
<!-- What was added to detect this faster next time -->

## Owner
<!-- Who owns the fix and monitoring -->

## Related failures
<!-- Links to previous failure reviews for this interface -->
</code></pre>
  </section>

  <section>
    <h2>Data Lineage Gap Note</h2>
    <pre><code>---
artifact: Data Lineage Gap Note
id: DLG-001
date: YYYY-MM-DD
scope: System | Domain | Report
---

## Data element
<!-- Field, table, report column -->

## Known lineage
<!-- Where this data comes from, step by step -->

## Gap description
<!-- What part of the lineage is unknown or unverified -->

## Gap type
<!-- missing source | missing transformation | missing owner | missing documentation | untrusted hop -->

## Business risk
<!-- What decisions are affected by this gap -->

## Verification approach
<!-- How to confirm the actual lineage -->

## Documentation action
<!-- What must be documented once verified -->

## Owner
<!-- Who verifies and documents -->

## Target date
<!-- When this gap must be closed -->

## Related gaps
<!-- Links to other lineage gap notes -->
</code></pre>
  </section>

  <section>
    <h2>Process Analysis Note</h2>
    <pre><code>---
artifact: Process Analysis Note
id: PAN-001
date: YYYY-MM-DD
process: Name
scope: As-is | To-be | Gap
---

## Process name and trigger
<!-- What starts this process? -->

## Steps
<!-- Numbered list of steps with actor and system -->

| Step | Actor | System | Action | Input | Output | Duration | Issues |
|------|-------|--------|--------|-------|--------|----------|--------|
| 1 | User | SAP | Create sales order | Customer request | Order | 5 min | Manual entry |

## Variations
<!-- Exceptions, escalations, alternative paths -->

## Pain points
<!-- Where the process fails, slows, or frustrates -->

## System touchpoints
<!-- Which systems are involved -->

## Data flows
<!-- What data moves where -->

## Ownership
<!-- Who owns the process end-to-end -->

## Improvement opportunities
<!-- Specific, actionable improvements with effort estimate -->

## Related processes
<!-- Links to other process analysis notes -->
</code></pre>
  </section>

  <section>
    <h2>Change Impact Assessment</h2>
    <pre><code>---
artifact: Change Impact Assessment
id: CIA-001
date: YYYY-MM-DD
change: Description
status: draft | reviewed | approved
---

## Change description
<!-- What is being changed -->

## Change driver
<!-- Why this change is needed -->

## Systems affected
<!-- Direct and indirect system impacts -->

## Data affected
<!-- Tables, fields, records that change -->

## Interfaces affected
<!-- APIs, IDocs, events that may break or need update -->

## Processes affected
<!-- Business processes that change -->

## Stakeholders affected
<!-- Who needs to know or act -->

## Testing required
<!-- What must be tested before go-live -->

## Rollback plan
<!-- How to undo if the change fails -->

## Risk level
<!-- Low | Medium | High | Critical -->

## Approval required
<!-- Who must approve before implementation -->

## Owner
<!-- Who drives this assessment and the change -->

## Related changes
<!-- Links to other change impact assessments -->
</code></pre>
  </section>

  <section>
    <h2>Operational Knowledge Capture Note</h2>
    <pre><code>---
artifact: Operational Knowledge Capture Note
id: OKC-001
date: YYYY-MM-DD
author: Name
topic: Incident | Procedure | Workaround | Decision
---

## Situation
<!-- What was happening. Context, urgency, systems involved. -->

## What was done
<!-- Step by step. Commands, transactions, settings. -->

## Why it worked
<!-- Causal explanation, not just description -->

## What almost went wrong
<!-- Near misses, wrong paths, assumptions that were false -->

## Preconditions
<!-- When this knowledge applies and when it does not -->

## Limitations
<!-- What this procedure does not cover -->

## Verification
<!-- How to confirm the procedure is still valid -->

## Owner
<!-- Who maintains this knowledge -->

## Review date
<!-- When this note should be revalidated -->

## Related knowledge
<!-- Links to other capture notes, runbooks, tickets -->
</code></pre>
  </section>
</article>
