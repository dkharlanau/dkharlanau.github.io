---
layout: default
title: "AI-Assisted Test Case Generation Working Skill"
description: "Generate structured test cases with AI assistance, then validate coverage, edge cases, and traceability before adding them to a test plan."
permalink: /skill-hub/ai-assisted-analysis/ai-assisted-test-case-generation-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">AI-Assisted Test Case Generation</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>AI-Assisted Test Case Generation</h1>
  <p class="lead">Generate structured test cases with AI assistance, then validate coverage, edge cases, and traceability before adding them to a test plan.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Writing test cases from requirements is repetitive and time-consuming, but it is critical for delivery quality. AI can draft test cases quickly, but it often misses negative paths, duplicates existing cases, and uses incorrect test data assumptions. This skill provides a workflow where AI generates the first draft and a human validates coverage, correctness, and completeness before the test cases enter the test plan. The output is an AI-Generated Test Case Draft with human validation marks that show what was kept, what was corrected, and what was added.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A new feature or fix has clear requirements and the team needs test cases before development or testing begins.</li>
      <li>A regression test suite needs to be expanded for a changed area, and the team wants to generate candidate cases fast.</li>
      <li>An integration scenario has complex preconditions and multiple systems, making manual test case design slow.</li>
      <li>A data migration or conversion requires validation rules that can be expressed as pass-or-fail test cases.</li>
      <li>The team has existing test cases for a similar feature and wants AI to adapt them for a new context.</li>
      <li>Time pressure makes fully manual test case design impractical, but quality standards do not allow unchecked AI output.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>SAP SD pricing change needs forty test cases fast</h3>
    <p>A new pricing condition type is being introduced in SAP SD. The requirements document is twelve pages and includes scale-based pricing, customer-specific discounts, and tax calculations. The QA team has two days to produce test cases. AI generates a first draft of thirty cases in ten minutes. The human reviewer finds that the AI missed the negative case where the scale breaks at the boundary value, duplicated the standard customer discount case three times, and assumed a tax code that is not valid in the target country. The reviewer adds the missing cases, merges the duplicates, and corrects the tax code, producing a valid draft in one hour instead of two days.</p>
    <h3>EDI interface needs negative test cases for error handling</h3>
    <p>A new EDI interface for outbound invoices is ready for testing. The requirements describe the happy path clearly but say little about error handling. AI generates ten happy-path test cases. The human reviewer recognizes that the interface must handle invalid partner numbers, missing material master data, and duplicate invoice numbers. The reviewer adds six negative test cases, defines the expected error messages and IDoc status codes, and flags the requirements gap for the business analyst to fill.</p>
    <h3>Data migration needs validation rules expressed as test cases</h3>
    <p>A master data migration from the legacy system to SAP S/4HANA must be validated. The migration team has mapping rules but no formal test cases. AI drafts test cases from the mapping rules and produces cases for field presence, length validation, and reference data integrity. The human reviewer adds a case for duplicate customer numbers, a case for invalid email formats, and a case for missing organizational data. The reviewer also flags that the AI assumed all legacy fields map one-to-one, which is false for the customer classification field that requires a lookup table.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Requirements or user stories</strong> — the functional description that the test cases must verify.</li>
      <li><strong>Acceptance criteria</strong> — the pass-or-fail conditions that define test success.</li>
      <li><strong>Existing test cases</strong> — for the same or similar features, to avoid duplication and maintain consistency (optional).</li>
      <li><strong>System configuration details</strong> — valid transaction codes, field names, organizational units, and test data constraints.</li>
      <li><strong>Test environment constraints</strong> — what data exists, what can be created, and what systems are available.</li>
      <li><strong>Negative path requirements</strong> — explicit error conditions, boundary values, and exception scenarios (optional, but highly recommended).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What are the boundary values, and does the AI test at, just above, and just below each boundary?</li>
      <li>What are the error paths, and does the AI cover them with expected error messages and system behavior?</li>
      <li>Which requirements are traced to which test cases, and is the traceability complete?</li>
      <li>Does the AI use the correct transaction codes, field names, and test data for this system?</li>
      <li>Are there duplicate or near-duplicate test cases that should be merged?</li>
      <li>Does the AI assume test data that does not exist in the test environment?</li>
      <li>What is the priority of each test case, and does the AI assign reasonable priorities?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Prepare the input package.</strong> Gather requirements, acceptance criteria, existing test cases, and system configuration details. Organize them so the AI can read them in one context window.</li>
      <li><strong>Define the generation scope.</strong> Decide how many test cases are needed, which areas to cover, and which negative paths are mandatory.</li>
      <li><strong>Run the AI generation.</strong> Prompt the AI to produce test cases in the required format, with explicit instructions to include negative paths and boundary values.</li>
      <li><strong>Capture the raw draft.</strong> Save the AI output exactly as generated. Do not edit it during this step.</li>
      <li><strong>Validate coverage.</strong> Check that every requirement and acceptance criterion is covered by at least one test case. Flag gaps.</li>
      <li><strong>Validate correctness.</strong> Check transaction codes, field names, test data, and expected results against the system configuration. Flag errors.</li>
      <li><strong>Validate completeness.</strong> Check for boundary values, negative paths, error messages, and data dependencies. Add missing cases.</li>
      <li><strong>Validate traceability.</strong> Ensure each test case can be traced to a requirement or user story. Add traceability links.</li>
      <li><strong>Merge duplicates and resolve conflicts.</strong> Combine near-duplicate cases and correct conflicting expected results.</li>
      <li><strong>Produce the validated draft.</strong> Output the final test case set with human validation marks showing what was added, corrected, or removed.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the AI misses a negative path or boundary case, add it manually and flag the gap in the requirements.</li>
      <li>If the AI duplicates an existing test case, merge the duplicates and keep the most complete version.</li>
      <li>If the AI uses a wrong transaction code, field name, or data value, correct it and log the error pattern.</li>
      <li>If the AI assigns a high priority to a happy-path case and a low priority to a critical error path, override the priority.</li>
      <li>If the AI assumes test data that is not available, either change the test data or mark the case as blocked pending data setup.</li>
      <li>If the AI generates more cases than needed, select the most valuable cases based on risk and coverage, not quantity.</li>
      <li>If a requirement has no test case after generation, do not proceed with testing until the gap is filled.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>AI-Generated Test Case Draft</strong> — the raw AI output, preserved for traceability.</li>
      <li><strong>Validated Test Case Set</strong> — the corrected and expanded test cases with human validation marks.</li>
      <li><strong>Coverage Matrix</strong> — a mapping of requirements to test cases showing traceability.</li>
      <li><strong>AI Error Log</strong> — a list of AI-generated errors and missing cases to improve future prompts.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>AI-Assisted Test Case Draft</h3>
    <pre><code>---
feature: [feature name]
source_requirements: [requirement IDs]
ai_tool: [tool name]
date: [YYYY-MM-DD]
reviewer: [name]
---

## Test Case TC-001
- **ID**: TC-001
- **Title**: [short title]
- **Requirement**: [requirement ID]
- **Priority**: [High / Medium / Low]
- **AI generated**: [Yes / No]
- **Human validation**: [Accepted / Corrected / Added]
- **Preconditions**: [system state, data, access]
- **Steps**:
  1. [step]
  2. [step]
- **Expected result**: [specific, observable outcome]
- **AI original result**: [if corrected, what the AI wrote]
- **Boundary / Negative**: [Yes / No] — if yes, describe the boundary or error condition

## Coverage Matrix
| Requirement ID | Test Cases | Coverage Status |
|----------------|------------|-----------------|
| REQ-001 | TC-001, TC-002 | Complete |
| REQ-002 | TC-003 | Partial — missing negative path |

## AI Error Log
| # | Issue | AI Claim | Correction | Pattern to Avoid |
|---|-------|----------|------------|------------------|
| 1 | Wrong transaction | VA01 | VA02 (change) | Verify transaction against requirement type |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] Every requirement and acceptance criterion is covered by at least one test case.</li>
      <li>[ ] Every test case has a specific, observable expected result.</li>
      <li>[ ] Boundary values and negative paths are included and were not only generated by the AI but also validated by a human.</li>
      <li>[ ] No duplicate test cases exist unless they are intentionally testing different data sets.</li>
      <li>[ ] Transaction codes, field names, and test data values are correct for the target system.</li>
      <li>[ ] The coverage matrix shows complete traceability from requirements to test cases.</li>
      <li>[ ] The AI error log contains at least one entry or a note that no errors were found.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Using AI-generated happy-path cases without adding negative paths. <strong>Consequence:</strong> The test suite passes in ideal conditions but fails to catch defects that appear in real-world error scenarios.</li>
      <li><strong>Mistake:</strong> Accepting AI test cases without checking system-specific details. <strong>Consequence:</strong> Test cases reference nonexistent transactions or invalid test data, making them impossible to execute.</li>
      <li><strong>Mistake:</strong> Generating as many test cases as possible instead of the right test cases. <strong>Consequence:</strong> The test plan is bloated with low-value cases while high-risk areas remain under-tested.</li>
      <li><strong>Mistake:</strong> Not logging AI errors, so the same wrong patterns are repeated in the next generation cycle. <strong>Consequence:</strong> Every AI-assisted test generation requires the same corrections, wasting the time saving the tool was supposed to provide.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A team uses AI to generate test cases for a new SAP pricing condition. The AI produces twenty happy-path cases that all test the same standard discount scenario with slightly different customer numbers. There are no boundary tests, no scale-break tests, no tax-exclusion tests, and no tests for the error message when the condition is missing. The team adds all twenty cases to the test plan. During testing, a scale-break bug causes incorrect pricing for orders at the boundary value. The defect is found in production because the test suite never covered it. The AI output was accepted without coverage validation or human review.</p>
    <h3>Strong output — good AI usage</h3>
    <pre><code>## Validated Test Case Set — Pricing Condition ZPR0

### TC-005: Boundary — Scale Break at 100 Units
- **Requirement**: REQ-004 (Scale-based pricing)
- **Priority**: High
- **AI generated**: Yes
- **Human validation**: Corrected — AI used 99 units; changed to 100 to test the boundary.
- **Steps**:
  1. Create sales order for customer 1000, material M-001, quantity 100.
  2. Verify condition ZPR0 is applied with rate 5.00 per unit.
- **Expected result**: Net price = 500.00. No error. Condition record found.
- **AI original result**: "Price calculated correctly" — corrected to specific value.

### TC-012: Negative — Missing Condition Record
- **Requirement**: REQ-004
- **Priority**: High
- **AI generated**: No
- **Human validation**: Added manually — AI missed this negative path entirely.
- **Steps**:
  1. Create sales order for customer 9999, material M-001.
  2. Verify no condition record exists for ZPR0 for this customer-material combo.
- **Expected result**: System shows incompletion message: "Pricing error: missing condition ZPR0." Order is blocked.

### Coverage Matrix
| Requirement | Test Cases | Status |
|-------------|------------|--------|
| REQ-004 | TC-005, TC-012, TC-013 | Complete |
| REQ-005 | TC-008 | Complete |</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are a test case generation assistant for SAP and enterprise systems.
Context: I need test cases for [feature / process / integration] based on the requirements and acceptance criteria below. The system is [SAP module / version / landscape].
Tasks:
1. Generate test cases in the format: ID, Title, Preconditions, Steps, Expected Result, Priority.
2. For each requirement, generate at least one happy-path test case and one negative-path test case.
3. Include boundary values where numeric ranges or scale breaks exist.
4. Use the correct SAP transaction codes and field names from the system configuration provided.
5. Do not assume test data exists unless I confirm it.
6. Output a coverage matrix showing which requirement each test case covers.
Constraints: Do not invent transactions, tables, or fields. Do not duplicate test cases unless they test different data sets. Do not assign high priority to every case. If a negative path is not described in the requirements, flag it as a requirements gap rather than guessing the expected error.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for system configuration details and valid test data before generating test cases.</li>
      <li>Validate every test case against the requirements and the system before adding it to the test plan.</li>
      <li>Log AI errors and missing cases so the prompt can be improved for the next generation.</li>
      <li>Prioritize negative paths and boundary cases as highly as happy paths.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not accept AI-generated test cases without a coverage check.</li>
      <li>Do not let the AI assign priorities without human review.</li>
      <li>Do not add test cases that reference nonexistent transactions or invalid data.</li>
      <li>Do not skip the negative-path validation because the happy-path cases look complete.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-output-review-working-skill/">AI Output Review</a> — general review workflow for any AI-generated output.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/validate-ai-generated-requirements-working-skill/">Validate AI-Generated Requirements</a> — ensuring requirements are solid before test case generation begins.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-prompt-briefing-work-artifacts-working-skill/">AI Prompt Briefing for Work Artifacts</a> — writing stronger prompts to improve test case generation quality.</li>
      <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a> — the broader skill group for test design, regression, and release readiness.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — understanding error paths that test cases must cover.</li>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — structured process frame that informs test scope.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI-assisted test case generation. It is not official ISTQB, SAP, or test management framework documentation. The effectiveness of AI-generated test cases depends on the quality of the requirements, the system configuration provided, and the AI model's familiarity with SAP and enterprise systems. AI tools may generate plausible-looking but incorrect test data or transaction codes. The human validation step is mandatory and cannot be reduced. Use this skill as a structured starting point, not as a substitute for test design expertise.</p>
  </section>
</article>
