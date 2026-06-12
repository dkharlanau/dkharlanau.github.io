---
layout: default
title: "Test Scenario Derivation Working Skill"
description: "Derive concrete test scenarios from requirements and acceptance criteria so that testers know exactly what to verify before development begins."
permalink: /skill-hub/decision-validation/test-scenario-derivation-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/decision-validation/">Decision & Validation</a></li>
    <li aria-current="page">Test Scenario Derivation</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Decision & Validation</p>
  <h1>Test Scenario Derivation Working Skill</h1>
  <p class="lead">Convert approved requirements and acceptance criteria into concrete test scenarios so that testers, developers, and business owners know what must be verified before any code is written.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Test scenarios are the bridge between "what the system must do" and "how we will prove it does it." This skill converts requirements and acceptance criteria into structured test scenarios that cover positive paths, negative paths, boundary conditions, and exploratory conditions. A test scenario is higher-level than a test case: it describes the condition to verify, not the exact click-by-click steps. The output is a Test Scenario Set that maps each scenario back to its requirement, classifies the test type, and identifies the data needed. This gives test planners coverage visibility and gives developers clarity on edge cases before they build.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Acceptance criteria are approved and the test team needs to know what to verify.</li>
      <li>A test plan is being created and coverage must be estimated before effort is committed.</li>
      <li>Developers need to understand edge cases, error conditions, and boundary values before implementation.</li>
      <li>Regression testing must be scoped and you need to know which scenarios are already covered by existing tests.</li>
      <li>A new feature or change request needs verification, and no one has written down what to test.</li>
      <li>An AI agent is generating test cases and needs a structured scenario list as input.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP credit management: positive, negative, and boundary</h3>
    <p>A requirement states: "Block sales orders when the customer exceeds their credit limit." The acceptance criteria specify a 50,000 EUR limit. The test scenarios must cover: positive (customer at 40,000 EUR with a 5,000 EUR order proceeds), negative (customer at 48,000 EUR with a 5,000 EUR order is blocked), boundary (customer at 49,999 EUR with a 2 EUR order is blocked, customer at 50,000 EUR with a 0 EUR order proceeds). Without these scenarios, testers verify only the happy path and the credit block fails in production for edge cases.</p>

    <h3>IDoc processing: error and retry scenarios</h3>
    <p>A requirement states: "Sales order IDocs from the e-commerce platform must process within 5 minutes." The test scenarios must cover: positive (standard IDoc with valid data processes in 2 minutes), negative (IDoc with invalid material number fails and posts to error queue), boundary (IDoc with 1,000 line items processes within 5 minutes), error (IDoc arrives during system maintenance and queues for retry), exploratory (two IDocs for the same customer arrive simultaneously and both process without collision). Without these scenarios, the integration goes live with untested error handling and duplicate order risks.</p>

    <h3>Master data migration: validation and reconciliation</h3>
    <p>A requirement states: "Migrate all active customers with matching account group and tax number." The test scenarios must cover: positive (active customer with complete data migrates successfully), negative (inactive customer is excluded), boundary (customer with missing tax number is rejected and logged), error (duplicate account group in target system is detected and flagged), exploratory (customer with special characters in the name is handled correctly). Without these scenarios, the migration loads incomplete data that blocks invoicing and requires manual cleanup.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Approved requirements with unique IDs and clear requirement statements.</li>
      <li>Acceptance Criteria Set for each requirement, covering normal, boundary, and error cases.</li>
      <li>System documentation showing transactions, fields, tables, and business objects involved.</li>
      <li>Test data samples or production data extracts that represent normal and edge cases.</li>
      <li>Business rules catalog showing decision logic, validation rules, and exception handling.</li>
      <li>Existing test plan or regression test suite to avoid duplication (if available).</li>
      <li>Non-functional requirements: performance thresholds, availability windows, and data volume limits.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the positive path: given valid data and normal conditions, what must happen?</li>
      <li>What is the boundary condition: the largest value, the smallest value, the edge of a range?</li>
      <li>What happens when required data is missing, invalid, or formatted incorrectly?</li>
      <li>What happens when the system is unavailable, under load, or in maintenance mode?</li>
      <li>What happens when two users or two processes attempt the same action simultaneously?</li>
      <li>What existing behavior must remain unchanged, and how do we verify it is not broken?</li>
      <li>Which data combinations are dangerous or historically problematic?</li>
      <li>What would a malicious or mistaken user do that the system must handle gracefully?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the requirement and acceptance criteria.</strong> Ensure the requirement is approved and the acceptance criteria are testable. If criteria are missing, stop and request them.</li>
      <li><strong>Identify the positive scenario.</strong> Define the normal case: valid data, standard conditions, expected outcome. This is the baseline scenario.</li>
      <li><strong>Identify boundary scenarios.</strong> Find the edges of valid input: maximum credit limit, minimum order value, longest material description, largest IDoc payload. Define the expected behavior at each boundary.</li>
      <li><strong>Identify negative and error scenarios.</strong> Define what happens with invalid data, missing fields, unauthorized access, system downtime, and concurrent actions. Expected behavior must include error messages, logging, and rollback.</li>
      <li><strong>Identify exploratory scenarios.</strong> Define unusual but realistic conditions: high volume, slow network, corrupted data, unexpected sequence of events. These are not always automated but must be considered.</li>
      <li><strong>Map each scenario to a requirement.</strong> Every scenario must link to at least one requirement ID and acceptance criterion ID. If a scenario does not map, it is orphan.</li>
      <li><strong>Classify test type.</strong> Label each scenario: positive, negative, boundary, exploratory, regression, or performance. This helps with coverage estimation and test planning.</li>
      <li><strong>Estimate coverage.</strong> Count scenarios per requirement. A healthy requirement has at least one positive, one negative, and one boundary scenario. Flag under-covered requirements.</li>
      <li><strong>Document in a Test Scenario Set.</strong> Use the template below. Include scenario ID, description, linked requirement, test type, preconditions, expected outcome, and test data needs.</li>
      <li><strong>Validate with stakeholders.</strong> Walk through the scenario set with the requirement owner and a tester. Confirm that the scenarios match intent and are executable.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a requirement has no acceptance criteria, do not derive scenarios yet. Request criteria first.</li>
      <li>If a scenario cannot be executed in the test environment, flag it and request environment or data changes.</li>
      <li>If multiple scenarios test the same condition with the same data, consolidate them into one scenario.</li>
      <li>If a scenario requires production data, require anonymization or synthetic data creation before testing.</li>
      <li>If a scenario touches a critical business process, prioritize it for manual verification even if automation is planned.</li>
      <li>If a scenario changes existing data, require a rollback plan or a dedicated test environment refresh.</li>
      <li>If a scenario has no expected outcome defined, it is not a scenario. Define the outcome before adding it to the set.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Test Scenario Set</strong> — Per requirement or per feature. Contains scenario ID, description, linked requirement, test type, preconditions, expected outcome, and test data needs. See template below.</li>
      <li><strong>Coverage Matrix</strong> — Table showing requirements versus scenario types, with counts and gaps.</li>
      <li><strong>Test Data Requirements</strong> — List of data needed, source system, creation method, and anonymization requirements.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Test Scenario Set (compact)</h3>
    <pre><code>---
artifact: Test Scenario Set
id: TS-001
requirement: Link to requirement
status: draft | reviewed | approved
---

## Scenario: Positive — Normal case
- ID: TS-001-POS
- Description: &lt;What is being tested&gt;
- Requirement: REQ-001
- Acceptance Criterion: AC-001-A
- Preconditions: &lt;System state and data before test&gt;
- Steps: &lt;High-level actions, not click-by-click&gt;
- Expected outcome: &lt;What must be true after the test&gt;
- Test data: &lt;What data is needed and where to get it&gt;
- Environment: &lt;System and client&gt;

## Scenario: Boundary — Edge of valid range
- ID: TS-001-BND
- Description: &lt;What is being tested&gt;
- Requirement: REQ-001
- Acceptance Criterion: AC-001-B
- Preconditions: &lt;System state and data before test&gt;
- Steps: &lt;High-level actions&gt;
- Expected outcome: &lt;What must be true after the test&gt;
- Test data: &lt;What data is needed&gt;
- Environment: &lt;System and client&gt;

## Scenario: Negative — Error or invalid input
- ID: TS-001-NEG
- Description: &lt;What is being tested&gt;
- Requirement: REQ-001
- Acceptance Criterion: AC-001-C
- Preconditions: &lt;System state and data before test&gt;
- Steps: &lt;High-level actions&gt;
- Expected outcome: &lt;Error message, status, log entry, or block&gt;
- Test data: &lt;What data is needed&gt;
- Environment: &lt;System and client&gt;

## Scenario: Exploratory — Unusual condition
- ID: TS-001-EXP
- Description: &lt;What is being tested&gt;
- Requirement: REQ-001
- Preconditions: &lt;System state and data before test&gt;
- Steps: &lt;High-level actions&gt;
- Expected outcome: &lt;What must be true after the test&gt;
- Test data: &lt;What data is needed&gt;
- Environment: &lt;System and client&gt;

## Coverage summary
- Positive: &lt;count&gt;
- Boundary: &lt;count&gt;
- Negative: &lt;count&gt;
- Exploratory: &lt;count&gt;
- Total: &lt;count&gt;
- Gaps: &lt;list any missing scenario types&gt;
</code></pre>

    <h3>Coverage Matrix (compact)</h3>
    <pre><code>| Requirement | Positive | Boundary | Negative | Exploratory | Performance | Total | Gap |
|-------------|----------|----------|----------|-------------|-------------|-------|-----|
| REQ-001 | 1 | 1 | 1 | 1 | 0 | 4 | — |
| REQ-002 | 1 | 0 | 0 | 0 | 0 | 1 | missing boundary, negative |
| REQ-003 | 1 | 1 | 1 | 0 | 1 | 4 | — |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every approved requirement has at least one test scenario.</li>
      <li>Scenarios cover positive, negative, and boundary cases for every requirement.</li>
      <li>Each scenario links to a specific requirement ID and acceptance criterion ID.</li>
      <li>Each scenario has a clear expected outcome, not just a description of the action.</li>
      <li>Test data is identified with source, creation method, and anonymization requirements.</li>
      <li>Scenarios are higher-level than test cases: they describe what to verify, not how to click.</li>
      <li>The Coverage Matrix shows no under-covered requirements.</li>
      <li>All scenarios are validated with the requirement owner and a tester before execution.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing test cases instead of test scenarios.</strong> Consequence: the scenario set is too granular to give coverage overview. Test cases belong in the test tool; scenarios belong in the planning document.</li>
      <li><strong>Missing negative paths.</strong> Consequence: production failures on invalid data, missing permissions, or system errors that were never tested because only the happy path was considered.</li>
      <li><strong>Not linking scenarios to requirements.</strong> Consequence: orphan tests that cannot be traced to business value, and requirements that appear covered but are not.</li>
      <li><strong>Defining scenarios without expected outcomes.</strong> Consequence: testers do not know what constitutes pass or fail. The scenario is a task description, not a verification standard.</li>
      <li><strong>Deriving scenarios from vague requirements.</strong> Consequence: the scenarios test assumptions, not approved criteria. When the requirement is clarified, the scenarios are invalid.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A vague list of test ideas with no structure: "Test that the system works. Test with invalid data. Test with large orders. Test during downtime. Make sure everything is fast enough." No requirement links, no expected outcomes, no data specifications, no classification of test types.</p>
    <p><strong>Why it fails:</strong> Testers cannot plan effort. Developers cannot understand edge cases. Coverage is unmeasurable. The output is indistinguishable from a brainstorming session.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Test Scenario Set
id: TS-S4-CREDIT-2026-001
requirement: REQ-101 — Credit limit block at 50k EUR
status: reviewed
---

## Scenario: Positive — Normal case
- ID: TS-101-POS
- Description: Customer with open orders below credit limit can create a new standard order.
- Requirement: REQ-101
- Acceptance Criterion: AC-101-A
- Preconditions: Customer C-10001 has credit limit 50,000 EUR and open order value 40,000 EUR.
- Steps: Create sales order VA01 for customer C-10001 with value 5,000 EUR.
- Expected outcome: Order creates with status "Open" and no credit block. Credit exposure updates to 45,000 EUR.
- Test data: Customer C-10001 in test client 300. Use material M-001 with price 5,000 EUR.
- Environment: S/4 Test Client 300.

## Scenario: Boundary — At the limit
- ID: TS-101-BND
- Description: Customer at exactly the credit limit can create a zero-value order.
- Requirement: REQ-101
- Acceptance Criterion: AC-101-B
- Preconditions: Customer C-10002 has credit limit 50,000 EUR and open order value 50,000 EUR.
- Steps: Create sales order VA01 for customer C-10002 with value 0 EUR.
- Expected outcome: Order creates with status "Open" and no credit block. Credit exposure remains 50,000 EUR.
- Test data: Customer C-10002 in test client 300.
- Environment: S/4 Test Client 300.

## Scenario: Negative — Exceeds limit
- ID: TS-101-NEG
- Description: Customer exceeding credit limit is blocked with correct status and routing.
- Requirement: REQ-101
- Acceptance Criterion: AC-101-C
- Preconditions: Customer C-10003 has credit limit 50,000 EUR and open order value 48,000 EUR.
- Steps: Create sales order VA01 for customer C-10003 with value 5,000 EUR.
- Expected outcome: Order is blocked with status "Credit block." Alert is sent to credit team. Order is visible in VKM1.
- Test data: Customer C-10003 in test client 300.
- Environment: S/4 Test Client 300.

## Coverage summary
- Positive: 1 | Boundary: 1 | Negative: 1 | Exploratory: 0
- Total: 3
- Gaps: Add exploratory scenario for concurrent order creation by same customer. Create TS-101-EXP by 2026-06-14.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Test scenario designer for an SAP enterprise project.</p>
    <p><strong>Context:</strong> You have approved requirements with acceptance criteria. You need to create a Test Scenario Set that testers can use for planning and developers can use for understanding edge cases.</p>
    <p><strong>Task:</strong> Derive positive, negative, boundary, and exploratory scenarios from each requirement. Map each scenario to its requirement and acceptance criterion. Produce a Coverage Matrix.</p>
    <p><strong>Output format:</strong> Structured Test Scenario Set per requirement, followed by a Coverage Matrix table.</p>

    <ul>
      <li><strong>Never derive scenarios from a requirement without acceptance criteria.</strong> Request criteria first, then derive scenarios.</li>
      <li><strong>Always include at least one positive, one negative, and one boundary scenario per requirement.</strong> Exploratory scenarios are added where risk warrants.</li>
      <li><strong>Link every scenario to a requirement ID and an acceptance criterion ID.</strong> No orphan scenarios.</li>
      <li><strong>Write scenarios, not test cases.</strong> Describe what to verify and the expected outcome. Do not write click-by-click instructions.</li>
      <li><strong>Define expected outcomes precisely.</strong> Include system status, field values, error messages, or log entries.</li>
      <li><strong>Identify test data explicitly.</strong> State what data, in which system, and how to obtain or create it.</li>
      <li><strong>Do not invent requirements or acceptance criteria.</strong> Derive only from approved inputs. If gaps exist, flag them.</li>
      <li><strong>Link to Atlas diagnostics</strong> when scenarios touch SAP validation. For example, incompletion procedure scenarios should reference <a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria Working Skill</a> — Use to produce the acceptance criteria that feed scenario derivation.</li>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a> — Use to produce the requirements that scenarios must trace to.</li>
      <li><a href="/skill-hub/decision-validation/requirements-review-checklist-working-skill/">Requirements Review Checklist Working Skill</a> — Use to verify that requirements are ready before scenarios are derived.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Validation context for completeness scenarios in order-to-cash.</li>
      <li><a href="/atlas/diagnostics/sap-release-strategy-diagnostics/">SAP Release Strategy Diagnostics</a> — Approval workflow context for scenarios involving block and release.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of test scenario derivation practices. It is not official ISTQB, BABOK, or SAP documentation. It focuses on enterprise and SAP contexts where scenarios must be concrete enough for testers to plan and developers to understand edge cases.</p>
    <p>Known limitations: the skill assumes requirements and acceptance criteria are already approved. It does not cover test automation scripting, performance testing tooling, or security penetration testing. It treats scenarios as planning artifacts, not executable test scripts. Non-functional scenarios may require specialized tools or environments that are not always available.</p>
  </section>
</article>
