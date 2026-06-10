---
layout: default
title: "Acceptance Criteria Working Skill"
description: "Define how to verify that a requirement is met, before work starts, so that delivery has an unambiguous pass/fail standard."
permalink: /skill-hub/business-analysis/acceptance-criteria-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Acceptance Criteria</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Acceptance Criteria Working Skill</h1>
  <p class="lead">Define pass/fail standards before work starts, so that delivery disputes are replaced by verifiable evidence.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Requirements without acceptance criteria are opinions. This skill turns requirements into testable statements that a developer can build against, a tester can verify, and a business owner can sign off on. The output is an Acceptance Criteria Set that removes ambiguity about what "done" means, prevents scope creep during testing, and gives AI agents a clear target for generating test cases or validation scripts.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A requirement is approved and ready for implementation, but no one has defined how to verify it.</li>
      <li>A user story is written and the development team asks "how will we know this is working?"</li>
      <li>A change request is scoped and the approver wants to know what success looks like.</li>
      <li>A test plan is being prepared and the testers need specific inputs and expected outputs.</li>
      <li>A contract milestone is defined and the vendor and client disagree on whether it was met.</li>
      <li>An incident fix is deployed and the business asks how to confirm the fix is permanent.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>New credit limit check rule</h3>
    <p>A requirement states: "The system must enforce credit limits." The acceptance criteria must specify: given a customer with a credit limit of 50,000 EUR and an open order value of 45,000 EUR, when a new order of 10,000 EUR is created, then the system blocks the order with status "Credit block" and routes it to the credit team. Exception: if the order is marked "Emergency" and under 1,000 EUR, it proceeds with a warning and logs to audit. Without these criteria, developers build a generic block that either over-blocks or under-blocks.</p>

    <h3>Data migration: customer master</h3>
    <p>A requirement states: "Migrate all active customers to the new system." The acceptance criteria must specify: 100 percent of customers with status "Active" in the source system exist in the target system with matching account group, tax number, and payment terms. Zero duplicate account groups are created. All tax numbers pass country-specific validation. Migration completes within the 48-hour maintenance window. Without these criteria, the migration loads incomplete data that blocks invoicing.</p>

    <h3>Integration fix: IDoc processing</h3>
    <p>A requirement states: "Fix the IDoc failure rate." The acceptance criteria must specify: given a standard sales order IDoc from the e-commerce platform, when it is received by SAP, then it processes within 5 minutes, creates an order with the correct pricing, and posts a success status. Error rate must be below 0.1 percent over a 7-day period. Monitoring alert fires within 1 minute of any IDoc error. Without these criteria, "fixed" means different things to operations and development.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Approved <a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Brief</a> with a clear requirement statement.</li>
      <li>System documentation showing current behavior, fields, and transactions involved.</li>
      <li>Test data samples or production data extracts that represent normal and edge cases.</li>
      <li>Stakeholder availability to validate that the criteria match their intent.</li>
      <li>Non-functional requirements: performance, availability, security, compliance constraints.</li>
      <li>Regulatory or audit constraints that affect what must be demonstrable.</li>
      <li>Previous test plans or criteria from similar requirements (if available).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>How will you know this is working correctly? What would you look at, click, or measure?</li>
      <li>What is the minimum acceptable result, not the best case or ideal scenario?</li>
      <li>Which data will you use to test this, and where does that data come from?</li>
      <li>Who will confirm this is correct, and do they have the authority to sign off?</li>
      <li>What happens if it is 90 percent correct? Is that acceptable or a failure?</li>
      <li>Which edge cases must be handled: new customers, large orders, missing data, system downtime?</li>
      <li>What must remain unchanged? What existing behavior must not break?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the requirement statement.</strong> Ensure it is testable. If it contains words like "easy," "fast," or "user-friendly," rewrite the requirement first.</li>
      <li><strong>Identify the scenario, precondition, action, and expected outcome.</strong> For each requirement, break it into: what must be true before, what happens, and what must be true after.</li>
      <li><strong>Write Given/When/Then criteria for each scenario.</strong> Use the format: Given [precondition], When [action or event], Then [expected outcome].</li>
      <li><strong>Add non-functional criteria.</strong> For each requirement, specify performance, availability, security, and compliance thresholds.</li>
      <li><strong>List edge cases.</strong> Identify at least three: normal case, boundary case, and error case.</li>
      <li><strong>Define test data needs.</strong> State exactly what data is needed, in which system, and how to obtain or create it.</li>
      <li><strong>Identify who signs off.</strong> Name the person who will approve that criteria are met. Verify they have authority.</li>
      <li><strong>Document in an Acceptance Criteria Set.</strong> One set per requirement. Link to the Requirements Brief.</li>
      <li><strong>Validate with the requirement owner.</strong> Walk through each criterion and confirm it matches their intent.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a requirement has no measurable outcome, rewrite the requirement before writing acceptance criteria.</li>
      <li>If criteria require data that does not exist in test systems, flag a test environment gap.</li>
      <li>If edge case handling is not specified, the criterion is incomplete.</li>
      <li>If the sign-off owner is not the requirement owner, verify their authority to approve.</li>
      <li>If non-functional criteria are missing, the deliverable may pass functionally and fail operationally.</li>
      <li>If criteria can be automated, note the automation approach and tool.</li>
      <li>If criteria conflict with existing system behavior, flag the conflict before implementation.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Acceptance Criteria Set</strong> — Per requirement. Contains scenarios, non-functional criteria, edge cases, test data needs, verification method, and sign-off owner. See template below.</li>
      <li><strong>Test Data Requirements</strong> — List of data needed, source system, creation method, and anonymization requirements.</li>
      <li><strong>Verification Plan</strong> — How each criterion will be checked: manual test, automated test, review, or demonstration.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Acceptance Criteria Set (compact)</h3>
    <pre><code>---
artifact: Acceptance Criteria Set
id: AC-001
requirement: Link to requirement brief
status: draft | reviewed | approved
---

## Scenario: Normal case
Given &lt;precondition&gt;
When &lt;action or event&gt;
Then &lt;expected outcome&gt;

## Scenario: Boundary case
Given &lt;precondition&gt;
When &lt;action or event&gt;
Then &lt;expected outcome&gt;

## Scenario: Error case
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
    <h2>Quality checklist</h2>
    <ul>
      <li>Every requirement has at least one acceptance criterion.</li>
      <li>Criteria are testable pass/fail statements, not open to interpretation.</li>
      <li>Edge cases are covered: normal, boundary, and error.</li>
      <li>Non-functional requirements have specific metrics or thresholds.</li>
      <li>Test data is identified with source and creation method.</li>
      <li>Sign-off owner is named and has authority.</li>
      <li>No criterion contains implementation detail or solution design.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing criteria that repeat the requirement without adding verifiability.</strong> Consequence: still no way to test. The criterion says "the system must be fast" instead of "the system must respond within 2 seconds."</li>
      <li><strong>Including implementation instructions in criteria.</strong> Consequence: constrains the solution unnecessarily. The criterion says "use index X" instead of "query returns in 2 seconds."</li>
      <li><strong>Forgetting edge cases.</strong> Consequence: production failures on exceptions that were never tested: missing data, large volumes, concurrent users.</li>
      <li><strong>Omitting non-functional criteria.</strong> Consequence: the deliverable passes functional tests but fails under load, lacks audit trails, or breaks compliance.</li>
      <li><strong>Not identifying test data.</strong> Consequence: testing is blocked because no one can create or access the required data.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>AI agents should use this skill to produce testable acceptance criteria before generating test cases, validation scripts, or implementation plans.</p>
    <ul>
      <li><strong>Never write acceptance criteria for a vague requirement.</strong> First clarify the requirement, then write criteria.</li>
      <li><strong>Use Given/When/Then format for functional criteria.</strong> Be specific about preconditions, actions, and outcomes.</li>
      <li><strong>Add specific metrics for non-functional criteria.</strong> Performance, availability, security, and compliance must have numbers or clear standards.</li>
      <li><strong>List at least three scenarios per requirement:</strong> normal case, boundary case, and error case.</li>
      <li><strong>Identify test data needs explicitly.</strong> State what data, in which system, and how to obtain it.</li>
      <li><strong>Name the sign-off owner.</strong> Do not leave approval ambiguous.</li>
      <li><strong>Produce an Acceptance Criteria Set per requirement.</strong> Link to the Requirements Brief.</li>
      <li><strong>Do not include implementation details in criteria.</strong> Criteria state what must be true, not how to build it.</li>
      <li><strong>Link to Atlas diagnostics</strong> when criteria relate to SAP validation. For example, incompletion procedure criteria should reference <a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Validation context for completeness criteria.</li>
      <li><a href="/atlas/diagnostics/sap-release-strategy-diagnostics/">SAP Release Strategy Diagnostics</a> — Approval workflow criteria context.</li>
      <li><a href="/scenarios/delivery-billing-block-order-to-cash-delays/">Delivery Billing Block Order-to-Cash Delays</a> — Scenario with block/release criteria.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of acceptance criteria practices. It is not official ISTQB, BABOK, or SAP documentation. It focuses on enterprise software and SAP contexts where criteria must be verifiable by business owners, not just technical testers.</p>
    <p>Known limitations: the skill assumes requirements are already elicited and approved. It does not cover exploratory testing, usability testing, or security penetration testing methodologies. Non-functional criteria may require specialized tools or environments that are not always available.</p>
  </section>
</article>
