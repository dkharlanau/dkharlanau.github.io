---
layout: default
title: "Regression Test Planning Working Skill"
description: "Select what to retest based on change risk, impact area, and historical defect density so regression effort is focused and defensible."
permalink: /skill-hub/testing-quality-delivery/regression-test-planning-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">Regression Test Planning</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>Regression Test Planning Working Skill</h1>
  <p class="lead">Produce a Regression Test Plan with risk scores that selects which existing functionality must be retested after a change, so the team does not retest everything and does not miss the parts that break.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Regression testing verifies that a change has not broken existing functionality. Full regression is often impossible because time and environments are limited. This skill helps you decide what to retest, in what order, and with what depth, based on the risk of the change, the areas it touches, and historical defect patterns. The output is a Regression Test Plan that includes a risk-scoped test set, effort estimate, and rationale for what is included and what is excluded. This plan is defensible to stakeholders and ensures that high-risk areas are covered even when full coverage is not feasible.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A new feature, enhancement, or fix is ready for test and the team must decide what existing functionality to retest.</li>
      <li>A change touches a shared component (credit check, pricing procedure, IDoc processing) and the impact radius is unclear.</li>
      <li>Time or environment constraints prevent full regression, and the team needs a risk-based selection.</li>
      <li>A release contains multiple changes and the cumulative regression risk must be assessed.</li>
      <li>Historical defects cluster in specific areas, and the team wants to prioritize retesting where breakage has occurred before.</li>
      <li>An auditor or steering committee asks for evidence that regression testing was planned and scoped.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP pricing procedure change: scoping regression for order-to-cash</h3>
    <p>A consultant modifies a pricing procedure to add a new discount condition type. The change affects sales order creation, billing, and returns. The regression plan must identify: which existing condition types could be affected by the sequence change, which order types use this procedure, which customer pricing scenarios must be retested, and which billing documents must be verified. Without a scoped plan, the team either retests every order type in the system (too expensive) or tests only the new discount (misses the break in existing surcharges).</p>

    <h3>Interface mapping change: regression across IDoc and API paths</h3>
    <p>A developer changes the mapping logic for customer master IDocs from the e-commerce platform. The change affects the IDoc segment mapping, the validation rules, and the downstream business partner creation. The regression plan must identify: which existing IDoc types and message types use the same mapping class, which test cases cover customer creation, update, and block scenarios, and which API consumers must be notified. Without a scoped plan, the team tests only the new field and misses the breakage in existing partner relationships.</p>

    <h3>Custom code transport: regression for background jobs and reports</h3>
    <p>A custom ABAP report is modified to add a new filter. The report is scheduled in multiple background jobs and called by another custom transaction. The regression plan must identify: which jobs use the report, which variants exist, which calling transactions depend on the output format, and which users run the report interactively. Without a scoped plan, the transport is released without testing the scheduled jobs, and the job fails the first night in production.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Change description or transport request listing the objects modified, added, or deleted.</li>
      <li>Impact analysis showing which transactions, tables, functions, and interfaces are affected by the change.</li>
      <li>Existing test case inventory for the affected areas, with last execution status and defect history.</li>
      <li>Historical defect data for the affected areas, showing where defects have clustered in the last 6–12 months.</li>
      <li>Business process map showing which processes depend on the changed objects.</li>
      <li>Time and environment constraints: available test days, environment windows, and tester capacity.</li>
      <li>Risk acceptance criteria from the project or QA lead: what risk level can be accepted without retesting.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What objects were changed, and what other objects call or reference them?</li>
      <li>Which business processes touch the changed objects, and how critical are they?</li>
      <li>Where have defects historically occurred in the affected areas?</li>
      <li>Which existing test cases cover the affected areas, and when were they last executed?</li>
      <li>What is the time and environment budget, and what can realistically be retested?</li>
      <li>What is the consequence if an untested area breaks in production?</li>
      <li>Are there automated tests that already cover some of the affected areas?</li>
      <li>Which stakeholders must accept the risk of excluding a test from the regression set?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the change footprint.</strong> List every object, table, function, interface, and configuration changed. Use the transport request, change document, or technical design as the source.</li>
      <li><strong>Map the footprint to business processes.</strong> For each changed object, identify the business processes that use it: order-to-cash, procure-to-pay, inventory management, master data governance. Record the process criticality.</li>
      <li><strong>Identify existing test coverage.</strong> List all existing test cases that cover the affected processes. Record their last execution date, last result, and any known defects.</li>
      <li><strong>Assess historical defect density.</strong> For each affected area, count defects found in the last 6–12 months. Higher density means higher regression priority.</li>
      <li><strong>Score risk for each area.</strong> Use a simple risk matrix: impact (critical, major, minor) multiplied by probability (high, medium, low) based on change complexity and historical defect density. Assign a numeric risk score (1–9).</li>
      <li><strong>Select test cases by risk score.</strong> Include all cases for areas with risk score 7–9. Include sample cases for areas with score 4–6. Exclude areas with score 1–3 unless they are required by policy or regulation. Document the rationale for exclusions.</li>
      <li><strong>Sequence the tests.</strong> Order tests by dependency: setup cases first, core process cases next, edge cases last. Place high-risk cases early so defects are found quickly.</li>
      <li><strong>Estimate effort and compare to budget.</strong> Sum the effort estimates of selected cases. If the total exceeds the budget, re-evaluate exclusions with the project lead or QA manager. Do not silently cut tests.</li>
      <li><strong>Identify automation candidates.</strong> Mark cases that are already automated or could be automated to reduce manual effort in future releases.</li>
      <li><strong>Document the Regression Test Plan.</strong> Use the template below. Include the change footprint, risk scores, selected cases, excluded cases with rationale, effort estimate, and dependencies.</li>
      <li><strong>Obtain stakeholder sign-off.</strong> Review the plan with the project lead, QA lead, and business owner. Confirm that the included set is acceptable and the excluded set is acknowledged.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If an area has a risk score of 7–9, include it in regression. Do not exclude high-risk areas due to time pressure without documented stakeholder acceptance.</li>
      <li>If an area has no existing test cases, either create a new case or document the untested risk and obtain acceptance.</li>
      <li>If an area is already covered by automated tests that passed in the last run, reduce manual regression depth but do not eliminate it entirely.</li>
      <li>If two changes affect the same area, consolidate the regression tests for that area rather than duplicating effort.</li>
      <li>If a test case has failed in the last three executions, include it regardless of risk score; it indicates instability.</li>
      <li>If a business process is regulatory or financial, include it regardless of risk score unless the compliance officer accepts exclusion.</li>
      <li>If a change is a configuration change with no code modification, regression can be lighter than for custom code changes, but still verify the affected process end-to-end.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Regression Test Plan</strong> — Per release or per change. Contains change footprint, risk scores, selected cases, excluded cases with rationale, effort estimate, and dependencies. See template below.</li>
      <li><strong>Risk Score Matrix</strong> — Table showing affected areas, impact, probability, risk score, and test coverage decision.</li>
      <li><strong>Stakeholder Acceptance Record</strong> — Documented confirmation that excluded areas are accepted by the project lead or QA lead.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Regression Test Plan (compact)</h3>
    <pre><code>---
artifact: Regression Test Plan
id: RTP-&lt;release&gt;-&lt;number&gt;
change: &lt;Change description or transport request&gt;
status: draft | reviewed | approved
---

## Change footprint
- Objects changed: &lt;list&gt;
- Transactions affected: &lt;list&gt;
- Interfaces affected: &lt;list&gt;
- Business processes affected: &lt;list&gt;

## Risk score matrix
| Area | Impact | Probability | Risk Score | Decision | Rationale |
|------|--------|-------------|------------|----------|-----------|
| Order-to-cash | Critical | High | 9 | Include | Core revenue process; pricing changed |
| Credit check | Major | High | 8 | Include | Shared component; history of defects |
| Returns | Major | Low | 4 | Sample | Indirect impact; sample 2 cases |
| Reporting | Minor | Low | 2 | Exclude | No code change; config only; accepted by QA lead |

## Selected test cases
| Case ID | Description | Risk Score | Effort | Sequence | Status |
|---------|-------------|------------|--------|----------|--------|
| TC-001 | Standard order creation | 9 | 10 min | 1 | Include |
| TC-002 | Credit block at limit | 8 | 10 min | 2 | Include |
| TC-003 | Returns processing | 4 | 15 min | 5 | Sample |

## Excluded test cases with rationale
| Case ID | Description | Exclusion Rationale | Risk Acceptance |
|---------|-------------|---------------------|-----------------|
| TC-004 | Batch report | Config only; no code change | Accepted by QA lead on 2026-06-12 |

## Effort estimate
- Total selected effort: &lt;sum&gt;
- Available budget: &lt;hours or days&gt;
- Gap: &lt;none or deficit&gt;

## Dependencies and sequence
1. Setup: Reset test data and credit limits.
2. Core: Order-to-cash positive path.
3. Edge: Credit block and returns.
4. Cleanup: Archive test orders.

## Sign-off
- QA Lead: ___________________ Date: _________
- Project Lead: ___________________ Date: _________
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every changed object is mapped to at least one business process.</li>
      <li>Every affected area has a risk score based on impact and probability.</li>
      <li>High-risk areas (score 7–9) are included in the regression set.</li>
      <li>Every selected test case has a clear rationale linking it to the change footprint.</li>
      <li>Every excluded case has a documented rationale and a named risk acceptor.</li>
      <li>Effort estimate is realistic and compared to the available budget.</li>
      <li>The test sequence respects dependencies and places high-risk cases early.</li>
      <li>Automation candidates are identified and noted for future efficiency.</li>
      <li>The plan is reviewed and signed off by QA lead and project lead.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Retesting everything regardless of risk.</strong> Consequence: regression effort is unsustainable, deadlines slip, and testers rush through cases without real attention. High-risk areas are not distinguished from low-risk areas.</li>
      <li><strong>Excluding areas without documented acceptance.</strong> Consequence: when a excluded area breaks in production, there is no record that the risk was accepted. Blame shifts to the QA team.</li>
      <li><strong>Ignoring historical defect data.</strong> Consequence: areas with known instability are deprioritized, and the same defects recur because the root cause was never fully verified.</li>
      <li><strong>Using the same regression set for every release.</strong> Consequence: the set becomes bloated with irrelevant cases and misses new risks introduced by recent changes.</li>
      <li><strong>Not mapping technical changes to business processes.</strong> Consequence: the regression plan is a list of technical objects with no business context, and stakeholders cannot assess whether the coverage is adequate.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A vague instruction: "Run the existing regression pack. Focus on the areas that might be affected. Make sure we test the important stuff. If we run out of time, cut the low-priority tests." No change footprint, no risk scores, no explicit list of what is included, no rationale for exclusions, no stakeholder sign-off.</p>
    <p><strong>Why it fails:</strong> Testers do not know what "important" means. The regression pack may be outdated. When time runs short, cuts are arbitrary. There is no defensible record of why something was not tested.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Regression Test Plan
id: RTP-S4-2026-06-001
change: TR-123456 — Pricing procedure ZPR01 updated with new discount condition
status: reviewed
---

## Change footprint
- Objects changed: Pricing procedure ZPR01, condition type ZDIS
- Transactions affected: VA01, VA02, VF01, VF02
- Business processes affected: Order-to-cash, billing

## Risk score matrix
| Area | Impact | Probability | Score | Decision |
|------|--------|-------------|-------|----------|
| Standard order pricing | Critical | High | 9 | Include |
| Discount application | Critical | High | 9 | Include |
| Surcharge sequence | Major | Medium | 6 | Include |
| Billing copy control | Major | Low | 4 | Sample |
| Returns pricing | Minor | Low | 2 | Exclude |

## Selected test cases
| Case ID | Description | Score | Effort | Sequence |
|---------|-------------|-------|--------|----------|
| TC-101 | Standard order with ZDIS | 9 | 10 min | 1 |
| TC-102 | Surcharge after ZDIS | 6 | 10 min | 2 |
| TC-103 | Billing copy to VF01 | 4 | 15 min | 3 |

## Excluded
| Case ID | Description | Rationale | Accepted by |
|---------|-------------|-----------|-------------|
| TC-104 | Returns with ZDIS | Minor process; low risk | QA Lead, 2026-06-12 |

## Effort
- Total: 35 minutes
- Budget: 4 hours
- Gap: none

## Sign-off
- QA Lead: D. Kharlanau, 2026-06-12
- Project Lead: [Name], 2026-06-12
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Regression test planner for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have a change transport or feature description, an impact analysis, an existing test case inventory, and historical defect data. You need to produce a Regression Test Plan that selects what to retest with risk scores and defensible rationale.</p>
    <p><strong>Task:</strong> Map the change footprint to business processes, score risk by impact and probability, select cases, document exclusions with acceptance, and produce a signed-off plan.</p>
    <p><strong>Output format:</strong> Regression Test Plan in Markdown, including a Risk Score Matrix table, selected case list, excluded case list with rationale, and effort summary.</p>

    <ul>
      <li><strong>Never produce a regression plan without a change footprint.</strong> If the changed objects are unknown, request the transport request or technical design first.</li>
      <li><strong>Always use a risk score matrix.</strong> Do not select cases by gut feeling. Quantify impact and probability, multiply them, and use the score to drive inclusion.</li>
      <li><strong>Always document excluded cases with rationale and a named acceptor.</strong> If exclusion is not accepted, mark the area as "include pending decision."</li>
      <li><strong>Map technical objects to business processes.</strong> A list of function modules is not enough; state which business process they support.</li>
      <li><strong>Do not invent historical defect data or test case inventories.</strong> Use the data provided. If data is missing, flag the gap rather than assuming low risk.</li>
      <li><strong>Link to Atlas diagnostics</strong> when regression areas touch SAP processes. For example, pricing procedure regression should reference <a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> for completeness validation context.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/testing-quality-delivery/test-case-design-working-skill/">Test Case Design</a> — Produces the cases that the regression plan selects from.</li>
      <li><a href="/skill-hub/decision-validation/test-scenario-derivation-working-skill/">Test Scenario Derivation</a> — Provides scenarios that feed into case design and regression selection.</li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a> — Provides the change footprint that drives regression scope.</li>
      <li><a href="/skill-hub/testing-quality-delivery/test-evidence-review-working-skill/">Test Evidence Review</a> — Reviews the results after regression tests are executed.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a> — Context for procure-to-pay regression testing.</li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a> — Context for order-to-cash regression testing.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Reference for regression of scheduled jobs and reports.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of regression test planning practices. It is not official ISTQB, BABOK, or SAP documentation. It focuses on risk-based regression scoping in enterprise environments where full regression is impractical and where stakeholder acceptance of risk is required.</p>
    <p>Known limitations: the skill assumes that change footprint and impact analysis are available. It does not cover automated regression suite maintenance, continuous integration pipelines, or A/B testing. It assumes a manual or hybrid test environment. Risk scoring is intentionally simple (impact × probability) and may need calibration for organizations with mature risk frameworks.</p>
  </section>
</article>
