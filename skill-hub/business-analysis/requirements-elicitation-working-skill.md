---
layout: default
title: "Requirements Elicitation Working Skill"
description: "Turn vague stakeholder complaints into structured requirements with assumptions, constraints, risks, and acceptance criteria."
permalink: /skill-hub/business-analysis/requirements-elicitation-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Requirements Elicitation</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Requirements Elicitation Working Skill</h1>
  <p class="lead">Turn vague stakeholder complaints into requirements, assumptions, risks, and acceptance criteria that a developer, tester, or AI agent can act on.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Stakeholders rarely state requirements. They state complaints, solutions, wishes, and constraints. This skill separates the signal from the noise and produces a Requirements Brief that contains: the underlying need, testable requirement statements, explicit assumptions, business rules, constraints, risks, and acceptance criteria. The output is usable by developers, testers, project managers, and AI agents without further translation.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A new project or phase starts and the scope is described in a single sentence.</li>
      <li>Scope creep is detected: new requests appear that do not map to any documented requirement.</li>
      <li>A change request arrives with a solution but no description of the problem it solves.</li>
      <li>An incident recurs and the post-mortem concludes that "the system should have caught this."</li>
      <li>An integration failure requires a new validation rule, but no one has defined what valid means.</li>
      <li>A data migration is planned and the business says "just move everything" without field-level clarity.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP rollout: "The system is too slow"</h3>
    <p>A warehouse manager says the system is too slow during goods receipt posting. The real need is not "faster system" — it is "post 500 line items within 30 minutes during peak shift." The requirement must specify throughput, concurrency, and peak time windows. Without this, infrastructure teams guess at hardware instead of measuring actual load.</p>

    <h3>Data migration: "Just move everything"</h3>
    <p>A finance director asks to migrate all customer master data to the new SAP S/4 system. Elicitation reveals that "everything" includes inactive customers, duplicate account groups, and unvalidated tax numbers. The requirement must specify: active-only, deduplication rules, tax validation, and cut-off date. Without this, the migration loads garbage that blocks invoicing.</p>

    <h3>Post-incident: "This should never happen again"</h3>
    <p>After a sales order bypassed credit check due to a missing credit segment, the sales manager says this should never happen again. The requirement is not "fix credit check" — it is "block order creation when credit segment is missing, route to credit team, and alert within 15 minutes." Without this, developers patch the symptom and leave the monitoring gap.</p>

    <h3>Integration failure: "The API should handle it"</h3>
    <p>An e-commerce integration drops orders when the customer record has an unsupported country code. The requirement is not "handle it" — it is "reject unsupported country codes at the API boundary with error code 422, log to monitoring, and queue for manual review." Without this, the integration silently drops orders or creates invalid data.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Stakeholder Interview Briefs from relevant business and technical owners.</li>
      <li>Existing system documentation, configuration guides, or transaction codes involved.</li>
      <li>Incident tickets or error logs that triggered the need.</li>
      <li>Process maps or <a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Notes</a> for the affected workflow.</li>
      <li>Regulatory documents or compliance constraints (if applicable).</li>
      <li>Current-state data samples showing the problem (if data-related).</li>
      <li>List of known constraints: budget, timeline, system versions, integration contracts.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What business process stops or slows down if this requirement is not met?</li>
      <li>Which fields, tables, or transactions must be present for this rule to execute correctly?</li>
      <li>Who loses time, money, or compliance standing when this fails?</li>
      <li>What is the minimum acceptable outcome, not the ideal outcome?</li>
      <li>What are you assuming to be true about the current data, configuration, or user behavior?</li>
      <li>Has this worked differently in the past? When did it change and why?</li>
      <li>Who can confirm that this requirement is correct and complete?</li>
      <li>What would prove that this requirement is met? What would prove it is not met?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Collect raw statements.</strong> Gather everything stakeholders have said: emails, meeting notes, tickets, complaints, proposals. Do not filter yet.</li>
      <li><strong>Classify each statement.</strong> Label each item as: need, solution idea, assumption, constraint, risk, or complaint. Use a table or color code.</li>
      <li><strong>Separate solution from requirement.</strong> For every solution idea, ask: "What problem does this solve?" Write the problem as the need. Discard the solution unless it is a constraint.</li>
      <li><strong>Write testable requirement statements.</strong> Format: "The system/process must [action] so that [outcome]." Each statement must be verifiable.</li>
      <li><strong>Identify missing context.</strong> For each requirement, list what you do not know: field names, transaction codes, volume estimates, owner names. Flag these as open questions.</li>
      <li><strong>Map to business rules.</strong> Identify rules that constrain the requirement. Document them separately so they can be validated.</li>
      <li><strong>Validate with the requirement owner.</strong> Walk through each requirement, assumption, and acceptance criterion with the named business owner. Revise based on feedback.</li>
      <li><strong>Package into Requirements Briefs.</strong> One brief per distinct business need. Link related briefs. Include traceability to source statements.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a stakeholder describes a solution, ask what problem it solves before writing a requirement.</li>
      <li>If a requirement has no acceptance criterion, it is not a requirement yet — it is a need statement.</li>
      <li>If two stakeholders give conflicting requirements, document both, flag the conflict, and ask who has decision authority.</li>
      <li>If a requirement references a system field, table, or transaction, verify that it exists and behaves as assumed before finalizing.</li>
      <li>If no owner can confirm a requirement, mark it as an assumption and add a risk that the requirement may be wrong.</li>
      <li>If a requirement came from an incident ticket, verify that the ticket root cause is addressed, not just the symptom.</li>
      <li>If a requirement is stated as "must be fast," "must be secure," or "must be user-friendly," rewrite it with a measurable threshold.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Requirements Brief</strong> — One per distinct business need. Contains need, requirement statement, assumptions, rules, constraints, risks, acceptance criteria, priority, owner, dependencies. See template below.</li>
      <li><strong>Stakeholder Interview Brief</strong> — Record of what each stakeholder said, classified. Reference <a href="/skill-hub/artifact-templates/">Artifact Templates</a> for the full format.</li>
      <li><strong>Assumptions Log</strong> — List of all assumptions with validation status and risk if false.</li>
      <li><strong>Requirements Traceability Matrix</strong> — Maps each requirement to source statement, stakeholder, business rule, and acceptance criterion.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Requirements Brief (compact)</h3>
    <pre><code>---
artifact: Requirements Brief
id: REQ-001
source: Stakeholder interview | Ticket | Audit | Regulation
status: draft | reviewed | approved
---

## Business need
<!-- The underlying need, not the solution. Example: "Orders must not ship to customers with expired credit limits." -->

## Requirement statement
<!-- Clear, testable statement. Example: "The system must block outbound delivery creation when the customer credit limit is exceeded." -->

## Assumptions
<!-- What we assume to be true. Example: "Credit limit is maintained in FD32 and updated daily." -->

## Business rules
<!-- Rules that constrain the solution. Example: "Emergency orders under 1,000 EUR may bypass credit block with director approval." -->

## Constraints
<!-- Technical, budget, time, policy limits. Example: "Must use existing credit management framework; no custom development." -->

## Acceptance criteria
<!-- How we will know this is met. Example: "Given a customer with exceeded credit limit, when delivery is created, then the system blocks with status 'Credit block' and routes to credit team." -->

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
    <h2>Quality checklist</h2>
    <ul>
      <li>Every requirement has at least one acceptance criterion.</li>
      <li>Every requirement has a named business owner who can confirm it.</li>
      <li>No requirement contains a solution disguised as a need.</li>
      <li>Assumptions are separated from facts and have a validation plan.</li>
      <li>Conflicts between stakeholders are flagged, not hidden.</li>
      <li>Each requirement traces back to a source statement or ticket.</li>
      <li>All vague qualifiers (fast, secure, user-friendly) have measurable thresholds.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Recording solutions as requirements.</strong> Consequence: the team builds what was asked, not what was needed. The real problem recurs in a different form.</li>
      <li><strong>Skipping acceptance criteria.</strong> Consequence: no way to verify delivery. Disputes about whether the requirement is met continue indefinitely.</li>
      <li><strong>Failing to document assumptions.</strong> Consequence: requirements break when assumptions turn out to be false. Rework is required late in the project.</li>
      <li><strong>Hiding conflicts between stakeholders.</strong> Consequence: late-stage scope disputes, change requests, and project delays when the conflict surfaces during testing.</li>
      <li><strong>Writing requirements without system verification.</strong> Consequence: requirements reference non-existent fields or transactions, making them impossible to implement.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Gather all raw stakeholder statements first.</strong> Do not summarize or filter before classification. Ask: what is the complaint, what is the proposed solution, what is the constraint, what is the risk?</li>
      <li><strong>Classify each statement</strong> as need, solution, assumption, constraint, risk, or complaint before writing any requirement.</li>
      <li><strong>Never write a requirement without an acceptance criterion.</strong> If the criterion is missing, flag the item as an unclassified need.</li>
      <li><strong>Separate facts from assumptions explicitly.</strong> Label assumptions and state the risk if each assumption is false.</li>
      <li><strong>If a field, table, transaction, or system is referenced,</strong> verify it exists in the current landscape before including it in a requirement.</li>
      <li><strong>Produce one Requirements Brief per distinct business need.</strong> Link related briefs. Do not bundle unrelated needs into a single brief.</li>
      <li><strong>Flag conflicts instead of resolving them silently.</strong> Document both conflicting requirements and ask who has decision authority.</li>
      <li><strong>Avoid generic framework language.</strong> Do not write "the system shall be user-friendly." Write specific, testable statements.</li>
      <li><strong>Link to Atlas diagnostics</strong> when requirements relate to SAP processes. For example, credit management requirements should reference <a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order-to-Cash</a> — Process context for O2C requirements.</li>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for process-related requirements.</li>
      <li><a href="/scenarios/master-data-issues-blocking-sales-orders/">Master Data Issues Blocking Sales Orders</a> — Scenario linking master data gaps to requirements.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of requirements elicitation practices. It is not official BABOK or IIBA documentation. It focuses on practical enterprise and SAP contexts and may not cover specialized domains such as safety-critical systems or financial trading platforms.</p>
    <p>Known limitations: the skill assumes access to stakeholders and system documentation. In environments with high turnover or poor documentation, additional discovery work is needed before elicitation can be effective. The skill does not cover formal requirements engineering tools or model-driven specification methods.</p>
  </section>
</article>
