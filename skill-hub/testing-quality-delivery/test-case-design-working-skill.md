---
layout: default
title: "Test Case Design Working Skill"
description: "Write step-by-step executable test cases that verify requirements, cover edge cases, and can be executed by testers who do not know the system internals."
permalink: /skill-hub/testing-quality-delivery/test-case-design-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">Test Case Design</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>Test Case Design Working Skill</h1>
  <p class="lead">Produce a step-by-step Test Case Document that testers can execute without system-internal knowledge, with each case tracing to a requirement and covering positive, negative, and boundary paths.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Test case design converts test scenarios and requirements into executable instructions. A test case is more granular than a scenario: it specifies the exact steps, input data, expected results, and preconditions needed for a tester to perform the verification. This skill ensures that every requirement has at least one executable test case, that edge cases are documented, and that the resulting Test Case Document is clear enough for a business tester or QA analyst to run without asking the developer for clarification. The output is a Test Case Document that serves as the primary input for test execution, automation scripting, and audit evidence.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Test scenarios are approved and the test team needs executable instructions before execution begins.</li>
      <li>A new feature or change request has acceptance criteria, but no one has written the click-by-click steps to verify them.</li>
      <li>Automation engineers need structured cases to convert into automated scripts.</li>
      <li>Business testers need clear instructions for UAT that do not assume SAP transaction knowledge.</li>
      <li>Regression testing requires updated cases for existing functionality affected by a change.</li>
      <li>An audit or compliance review requires documented test evidence with traceability to requirements.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP credit block: executable steps for a business tester</h3>
    <p>A change request modifies the credit limit check in S/4HANA. The test scenario covers blocking a sales order when the credit limit is exceeded. The test case must specify: the exact transaction (VA01), the customer master data values, the order material and quantity, the expected credit block status, the error message number, and where to verify the result (VKM1). Without this detail, a business tester creates an order with the wrong customer and concludes the feature works when it has not actually been tested.</p>

    <h3>Integration IDoc retry: verifying error handling in WE02</h3>
    <p>A requirement states that failed IDocs must queue for retry and alert the monitoring team after three failures. The test case must specify: the partner profile, the message type, the invalid data to trigger failure, the WE02 status sequence, the expected retry intervals, and the alert recipient. Without this detail, the tester only checks that the IDoc fails and misses the retry logic and alert routing entirely.</p>

    <h3>Master data migration: validation of converted records in target</h3>
    <p>A data migration loads customer master records from a legacy system to SAP. The test case must specify: the source extract criteria, the expected count of migrated records, the transaction to verify (XD03), the fields to check (name, tax number, account group), and the reconciliation report to run. Without this detail, the tester does a spot check and misses records with truncated names or incorrect account groups.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Approved Test Scenario Set with scenario IDs, descriptions, and linked requirement IDs.</li>
      <li>System documentation showing transactions, fields, tables, and messages relevant to the scenario.</li>
      <li>Test data specifications: customer accounts, material numbers, vendor codes, organizational units, and dates.</li>
      <li>Environment details: system, client, URL, user roles, and prerequisites (e.g., credit limit set to a specific value).</li>
      <li>Business rules and error message catalog so expected error messages can be stated precisely.</li>
      <li>Existing test cases for the same area (if available) to avoid duplication and ensure regression coverage.</li>
      <li>Traceability matrix or requirements list showing which requirements still lack test cases.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What transaction or screen does the tester open to start the test?</li>
      <li>What exact data values must be entered, and where does the tester find them?</li>
      <li>What is the system state before the test begins, and how is it verified?</li>
      <li>What is the exact expected result: field value, message number, status code, or log entry?</li>
      <li>Where does the tester verify the result: table, report, log, email, or downstream system?</li>
      <li>What happens if the precondition is not met, and how should the tester reset the environment?</li>
      <li>Which business rules could cause a different outcome, and how does the case account for them?</li>
      <li>Can a tester without developer knowledge execute this case, or does it require internal system access?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Select the scenario to case.</strong> Pick an approved test scenario. Verify that the scenario has a clear requirement link, test type, and expected outcome. If the scenario is vague, clarify it before writing cases.</li>
      <li><strong>Identify the entry point.</strong> Determine the transaction, screen, API endpoint, or URL where the tester begins. Record the exact navigation path.</li>
      <li><strong>Define preconditions.</strong> Document the required system state and data before the test starts. Include how to verify the precondition and how to reset if it is not met.</li>
      <li><strong>Write step-by-step actions.</strong> Number each action. Use imperative language: "Enter," "Select," "Click," "Navigate." Each step must be observable and unambiguous.</li>
      <li><strong>Specify input data.</strong> State exact values for every field: customer number, material code, quantity, date, amount. Reference test data sheets or creation instructions if data is dynamic.</li>
      <li><strong>Define expected results for each step.</strong> For every action, state what the system must show: field value, message text, status color, table entry, or report line. Include message numbers where possible.</li>
      <li><strong>Define postconditions and cleanup.</strong> State how the tester leaves the system: delete the test order, reset the credit limit, or log out. Cleanup prevents data pollution for subsequent tests.</li>
      <li><strong>Map the case to requirement and scenario.</strong> Every case must trace to at least one requirement ID and one scenario ID. If a case cannot be traced, it is an orphan and must be linked or removed.</li>
      <li><strong>Estimate execution effort.</strong> Assign a rough time estimate (e.g., 5 minutes, 30 minutes). This helps test planning and scheduling.</li>
      <li><strong>Review with a peer tester.</strong> Ask a tester who did not write the case to execute it from the document alone. Fix gaps, ambiguities, and missing data.</li>
      <li><strong>Store in the test management tool.</strong> Import or transcribe the case into the organization's test tool (ALM, Azure Test Plans, Jira Xray, or equivalent). Maintain the traceability links.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a scenario covers multiple paths, split it into one case per path. Do not combine positive and negative steps in one case.</li>
      <li>If a test case requires a system role or access the tester does not have, either change the case or request access before execution.</li>
      <li>If expected results depend on dynamic data (current date, exchange rate), state the rule for calculating the expected value rather than a fixed number.</li>
      <li>If a test case cannot be executed without another case having run first, document the dependency clearly and schedule them in order.</li>
      <li>If a case duplicates an existing case, reference the existing one and note the difference rather than rewriting it.</li>
      <li>If a requirement has no scenario, do not write a case. Derive the scenario first.</li>
      <li>If a test case takes longer than 60 minutes, split it into smaller cases or add a setup/cleanup sub-case.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Test Case Document</strong> — Per feature or per release. Contains case ID, linked requirement and scenario, preconditions, steps, input data, expected results, postconditions, and effort estimate. See template below.</li>
      <li><strong>Test Data Sheet</strong> — List of data values, source system, creation instructions, and anonymization status.</li>
      <li><strong>Traceability Update</strong> — Updated matrix showing requirements mapped to test cases, with coverage counts and gaps.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Test Case Document (compact)</h3>
    <pre><code>---
artifact: Test Case Document
id: TC-&lt;feature&gt;-&lt;number&gt;
scenario: TS-&lt;id&gt;
requirement: REQ-&lt;id&gt;
type: positive | negative | boundary | regression
status: draft | reviewed | ready
---

## TC-001 — Positive: Create standard sales order
- **Objective:** Verify that a standard sales order can be created for a valid customer with available credit.
- **Preconditions:**
  - Customer C-10001 exists in test client 300 with credit limit 50,000 EUR and open exposure 0 EUR.
  - Material M-001 exists with stock and price 5,000 EUR.
- **Steps:**
  1. Open transaction VA01. Select order type OR and sales organization 1000.
  2. Enter customer C-10001 in the Sold-to party field. Press Enter.
  3. Enter material M-001, quantity 1, and confirm the price is 5,000 EUR.
  4. Save the order.
- **Expected results:**
  - Step 2: Customer data copies into the order header without incompletion log.
  - Step 3: Price is 5,000 EUR. Availability check confirms stock is available.
  - Step 4: Order is saved with status "Open." Order number is displayed. Credit exposure updates to 5,000 EUR.
- **Postconditions / Cleanup:**
  - Delete the test order in VA02 or note the order number for batch cleanup.
  - Reset credit exposure if needed.
- **Test data:** Customer C-10001, Material M-001, Sales org 1000.
- **Environment:** S/4 Test Client 300.
- **Effort estimate:** 10 minutes.
- **Tester role:** Business tester with VA01 access.

## TC-002 — Negative: Credit block on exceeded limit
- **Objective:** Verify that a sales order is blocked when the customer exceeds the credit limit.
- **Preconditions:**
  - Customer C-10002 exists with credit limit 50,000 EUR and open exposure 48,000 EUR.
- **Steps:**
  1. Open VA01. Select order type OR and sales organization 1000.
  2. Enter customer C-10002.
  3. Enter material M-001, quantity 1, price 5,000 EUR.
  4. Save the order.
- **Expected results:**
  - Step 4: Order is blocked with status "Credit block." Message "Credit limit exceeded" appears. Order is listed in VKM1 with block reason.
- **Postconditions / Cleanup:** Release the block in VKM3 or delete the order.
- **Test data:** Customer C-10002, Material M-001.
- **Environment:** S/4 Test Client 300.
- **Effort estimate:** 10 minutes.
- **Tester role:** Business tester with VA01 and VKM1 access.
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every test case traces to a specific requirement ID and scenario ID.</li>
      <li>Every case has a clear, testable objective stated in one sentence.</li>
      <li>Preconditions are documented with verification steps and cleanup instructions.</li>
      <li>Steps are numbered, imperative, and unambiguous.</li>
      <li>Input data is exact or includes a rule for deriving the value.</li>
      <li>Expected results are specific: field values, message numbers, status codes, or report lines.</li>
      <li>A peer tester can execute the case from the document alone without asking the author.</li>
      <li>No case mixes positive and negative paths; each path is its own case.</li>
      <li>Postconditions and cleanup are defined so data does not pollute subsequent tests.</li>
      <li>Effort estimates are realistic and the total effort is calculable for planning.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing scenarios instead of cases.</strong> Consequence: testers lack the exact steps and data needed to execute. The document is a planning artifact, not an executable script.</li>
      <li><strong>Missing expected results for every step.</strong> Consequence: testers do not know whether an intermediate screen is correct, and defects are discovered late or missed.</li>
      <li><strong>Using placeholder data without instructions.</strong> Consequence: testers invent data that does not match the business rule, leading to false positives and false negatives.</li>
      <li><strong>Combining multiple paths in one case.</strong> Consequence: when the case fails, the tester cannot tell which path failed, and root cause analysis takes longer.</li>
      <li><strong>Skipping cleanup steps.</strong> Consequence: test data accumulates, credit limits are left altered, and subsequent tests fail due to polluted state.</li>
      <li><strong>Assuming system knowledge.</strong> Consequence: a business tester or new QA analyst cannot execute the case, and execution is delayed while questions are answered.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A generic test instruction with no steps, no data, and no traceability: "Test the sales order creation. Make sure it works. Also test that the credit block happens. Check the IDoc retry logic. Verify the master data is correct." No requirement links, no transaction names, no input values, no expected results, no cleanup.</p>
    <p><strong>Why it fails:</strong> Testers cannot execute it. Coverage is unmeasurable. Automation engineers cannot script it. Auditors cannot verify it. It is a brainstorming note, not a test case document.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Test Case Document
id: TC-S4-CREDIT-2026-001
scenario: TS-101
requirement: REQ-101
status: reviewed
---

## TC-001 — Positive: Standard order within credit limit
- **Objective:** Verify that a sales order for a customer within credit limit creates without block.
- **Preconditions:**
  - Customer C-10001 in client 300 has credit limit 50,000 EUR and exposure 0.
- **Steps:**
  1. Open VA01, select order type OR, sales org 1000.
  2. Enter customer C-10001. Press Enter.
  3. Enter material M-001, quantity 1. Confirm price 5,000 EUR.
  4. Save.
- **Expected results:**
  - Step 2: Header data copies, no incompletion log.
  - Step 3: Availability check confirms stock.
  - Step 4: Order saved with status "Open." Order number displayed. Exposure updates to 5,000 EUR.
- **Cleanup:** Delete order in VA02 or record number for cleanup job.
- **Test data:** C-10001, M-001, sales org 1000.
- **Environment:** S/4 Test Client 300.
- **Effort:** 10 min.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Test case designer for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have approved test scenarios with requirement links and acceptance criteria. You need to produce a Test Case Document that testers can execute without asking the developer for help.</p>
    <p><strong>Task:</strong> For each scenario, write numbered steps, exact input data, specific expected results, preconditions, cleanup, and effort estimates. Map every case to a requirement and scenario.</p>
    <p><strong>Output format:</strong> Test Case Document in Markdown, one section per case, using the compact template.</p>

    <ul>
      <li><strong>Never write a test case without a linked requirement and scenario.</strong> If the link is missing, flag it and stop.</li>
      <li><strong>Always specify exact transactions, fields, and values.</strong> Use placeholder text only when the value is genuinely dynamic, and state the derivation rule.</li>
      <li><strong>Define expected results for every step, not only the final outcome.</strong> Include message numbers, status codes, and field values.</li>
      <li><strong>Include cleanup steps.</strong> Do not leave the test environment in an altered state.</li>
      <li><strong>Write cases a business tester can execute.</strong> Avoid steps that require debugging, custom code, or developer access.</li>
      <li><strong>Do not invent requirements, scenarios, or system behavior.</strong> Derive only from approved inputs. If a scenario is unclear, request clarification rather than guessing.</li>
      <li><strong>Link to Atlas diagnostics</strong> when cases touch SAP validation logic. For example, credit block cases should reference <a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> for message numbers and status paths.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/decision-validation/test-scenario-derivation-working-skill/">Test Scenario Derivation</a> — Scenarios are the input; this skill converts them into executable cases.</li>
      <li><a href="/skill-hub/testing-quality-delivery/regression-test-planning-working-skill/">Regression Test Planning</a> — Uses test cases to decide what to retest and in what order.</li>
      <li><a href="/skill-hub/testing-quality-delivery/test-evidence-review-working-skill/">Test Evidence Review</a> — Reviews the results after cases are executed.</li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a> — Provides the criteria that test cases must verify.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Context for credit block test cases and status verification.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Validation context for completeness checks in order-to-cash cases.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Reference for IDoc retry and error handling test cases.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of test case design practices. It is not official ISTQB, BABOK, or SAP documentation. It focuses on enterprise contexts where test cases must be executable by testers who are not developers and where traceability to requirements is required for audit and compliance.</p>
    <p>Known limitations: the skill does not cover test automation scripting languages, performance test tool configuration, or security penetration testing. It assumes test scenarios already exist. It does not address exploratory testing without predefined scenarios. Some organizations use ALM tools with custom fields that may require additional metadata beyond the template provided.</p>
  </section>
</article>
