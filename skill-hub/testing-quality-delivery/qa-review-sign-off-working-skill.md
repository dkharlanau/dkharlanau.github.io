---
layout: default
title: "QA Review and Sign-Off Working Skill"
description: "Run a structured quality gate review before release: verify test coverage, defect status, documentation completeness, and risk acceptance."
permalink: /skill-hub/testing-quality-delivery/qa-review-sign-off-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">QA Review and Sign-Off</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>QA Review and Sign-Off Working Skill</h1>
  <p class="lead">Produce a QA Sign-Off Memo that confirms whether the release meets quality gate criteria, documents open risks, and gives a go, conditional go, or no-go recommendation.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>The QA Review and Sign-Off is the quality gate that determines whether a release is approved to proceed to deployment or UAT. It is not a generic checklist tick; it is a structured review of test coverage, defect status, documentation completeness, and accepted risk. This skill helps the QA lead or project manager assemble evidence, evaluate it against predefined criteria, and produce a QA Sign-Off Memo that is credible to the steering committee, auditors, and deployment team. The memo is the official record of the quality decision at a point in time.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Testing is complete and the release requires a formal quality gate before deployment.</li>
      <li>The steering committee or CAB needs a documented recommendation on whether to approve the release.</li>
      <li>Regulatory or contractual requirements mandate a QA sign-off before go-live.</li>
      <li>Defects remain open and the project lead wants to know whether the risk is acceptable.</li>
      <li>Test coverage is partial and the team needs a formal record of what was not tested and why.</li>
      <li>An audit or retrospective requires evidence that the release was reviewed and signed off by QA.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP transport release: QA gate before production move</h3>
    <p>A set of transports containing custom code and configuration changes is ready to move from the quality system to production. The QA lead must verify: all test cases in the regression plan were executed, defect triage is complete with no critical defects open, the transport documentation lists every object, the rollback plan is documented, and the business owner has accepted the known open minor defects. Without a structured QA review, the transport is approved verbally and a critical defect is found in production because the last test case was skipped.</p>

    <h3>UAT completion sign-off: business readiness for go-live</h3>
    <p>UAT has finished for a new sales order workflow. The business testers reported five defects, all of which are minor or have workarounds. The QA lead must verify: every UAT scenario was executed, the test evidence is complete and traceable, the defect log shows all items are closed or accepted, the business owner has signed the UAT completion form, and the training documentation is updated. Without a structured QA review, the business owner assumes UAT was thorough and discovers a missing scenario after go-live that blocks a critical customer segment.</p>

    <h3>Data migration release: quality gate for production load</h3>
    <p>A master data migration is scheduled for the weekend. The QA lead must verify: the migration was tested in the quality system with a full data set, the reconciliation report matches the source and target counts, the error log is empty or all errors are explained and accepted, the rollback script is tested and available, and the business owner has accepted the migration timing and data scope. Without a structured QA review, the migration runs with an untested rollback script and a partial data set, leading to a 12-hour recovery window.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Test execution report showing which test cases passed, failed, skipped, or blocked, with evidence links.</li>
      <li>Defect Triage Log with current status of all defects, including open items and accepted risks.</li>
      <li>Regression Test Plan or Test Case Document showing the scope of testing and any exclusions.</li>
      <li>Traceability matrix showing requirements mapped to test cases and defects.</li>
      <li>Release documentation: change description, transport list, deployment steps, and rollback plan.</li>
      <li>Quality gate criteria from the project plan or QA policy: thresholds for defect counts, coverage levels, and documentation completeness.</li>
      <li>UAT sign-off or business acceptance record (if applicable).</li>
      <li>Risk acceptance register showing which risks are accepted, by whom, and with what mitigation.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What percentage of planned test cases were executed, and what percentage passed?</li>
      <li>How many critical and major defects are open, and what is the business impact of each?</li>
      <li>Which requirements have no test coverage, and why?</li>
      <li>Is the rollback plan documented, tested, and accessible to the deployment team?</li>
      <li>Has the business owner or requirement owner accepted the open defects and untested areas?</li>
      <li>Are all transport objects, configuration changes, and data loads documented in the release notes?</li>
      <li>Does the test evidence match the test cases, or are there gaps in the execution record?</li>
      <li>What would happen if the release proceeds and the worst open defect occurs in production?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Assemble the evidence package.</strong> Collect all inputs: test execution reports, defect logs, traceability matrices, release documentation, and risk registers. Organize them in a single location or sharepoint.</li>
      <li><strong>Verify test coverage completeness.</strong> Compare the executed test cases to the planned test cases. Calculate coverage percentage. Identify skipped or blocked cases and determine whether they are required for the quality gate. Document gaps.</li>
      <li><strong>Verify defect status against gate criteria.</strong> Count open defects by severity. Compare to the quality gate thresholds (e.g., zero critical, no more than two major). If thresholds are exceeded, mark the gate as failed and list the defects.</li>
      <li><strong>Review traceability.</strong> Verify that every requirement has at least one executed test case or a documented exclusion with acceptance. Verify that every defect traces to a requirement and a test case. Orphan defects or untested requirements are red flags.</li>
      <li><strong>Review release documentation.</strong> Confirm that the change description, transport list, deployment steps, and rollback plan are complete and reviewed by the technical team. Confirm that the rollback plan has been tested or at least validated in a non-production environment.</li>
      <li><strong>Confirm risk acceptance.</strong> Verify that all open defects, untested areas, and known issues have been accepted by a named stakeholder with a dated record. Unaccepted risks block the gate.</li>
      <li><strong>Classify the gate outcome.</strong> Use three outcomes: Go (all criteria met, no significant open risks), Conditional Go (criteria mostly met, minor open risks accepted with mitigation), No-Go (criteria not met, significant risks remain). Do not use ambiguous language like "almost ready."</li>
      <li><strong>Write the QA Sign-Off Memo.</strong> Use the template below. Include the evidence summary, criteria evaluation, open risks, gate outcome, and conditions for a Conditional Go.</li>
      <li><strong>Review with stakeholders.</strong> Walk through the memo with the project lead, QA lead, and business owner. Confirm that the evidence is accurate and the conclusion is shared.</li>
      <li><strong>Obtain signatures or electronic approval.</strong> Store the signed memo in the project records. The memo is the official record of the quality decision.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If any critical defect is open, the gate outcome is No-Go unless the critical defect is accepted by the executive sponsor with a documented mitigation plan.</li>
      <li>If test coverage is below the threshold (e.g., less than 90% of planned cases executed), the outcome is No-Go or Conditional Go depending on whether the uncovered areas are high-risk.</li>
      <li>If the rollback plan is missing or untested, the outcome is No-Go regardless of test results.</li>
      <li>If a requirement has no test case and no documented acceptance, the outcome is No-Go until the gap is addressed or accepted.</li>
      <li>If all criteria are met and only trivial defects remain, the outcome is Go.</li>
      <li>If criteria are met but minor defects or untested areas are accepted, the outcome is Conditional Go with a dated follow-up condition.</li>
      <li>If the QA lead and project lead disagree on the outcome, escalate to the steering committee with both positions documented.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>QA Sign-Off Memo</strong> — Per release or per quality gate. Contains evidence summary, criteria evaluation, open risks, gate outcome, and conditions. See template below.</li>
      <li><strong>Evidence Package Index</strong> — List of all documents reviewed, with locations and versions.</li>
      <li><strong>Risk Acceptance Record</strong> — Documented confirmation of accepted risks by named stakeholders.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>QA Sign-Off Memo (compact)</h3>
    <pre><code>---
artifact: QA Sign-Off Memo
release: &lt;Release name or version&gt;
gate: &lt;Gate name, e.g., QA Gate before Production&gt;
date: &lt;YYYY-MM-DD&gt;
---

## Evidence summary
- Test cases planned: &lt;count&gt;
- Test cases executed: &lt;count&gt; (&lt;percentage&gt;%)
- Test cases passed: &lt;count&gt;
- Critical defects open: &lt;count&gt;
- Major defects open: &lt;count&gt;
- Minor defects open: &lt;count&gt;
- Untested requirements: &lt;count&gt; with documented acceptance

## Criteria evaluation
| Criterion | Threshold | Actual | Status |
|-----------|-----------|--------|--------|
| Test coverage | ≥ 90% | 94% | Met |
| Critical defects open | 0 | 0 | Met |
| Major defects open | ≤ 2 | 1 | Met |
| Rollback plan tested | Yes | Yes | Met |
| Business acceptance | Signed | Signed | Met |

## Open risks and conditions
| Risk | Impact | Mitigation | Accepted by | Date |
|------|--------|------------|-------------|------|
| DEF-004 label typo | Low | Fix in first patch | Business Owner | 2026-06-12 |
| TC-103 not executed | Medium | Run within 48h of go-live | QA Lead | 2026-06-12 |

## Gate outcome
- **Recommendation:** Go / Conditional Go / No-Go
- **Rationale:** &lt;One paragraph explaining the decision&gt;
- **Conditions for Conditional Go:** &lt;List if applicable&gt;

## Signatures
- QA Lead: ___________________ Date: _________
- Project Lead: ___________________ Date: _________
- Business Owner: ___________________ Date: _________
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>All evidence is assembled and versioned before the review begins.</li>
      <li>Test coverage is calculated and compared to the threshold.</li>
      <li>Defect counts by severity are compared to the gate criteria.</li>
      <li>Every untested requirement or open defect has a documented acceptance with a named stakeholder and date.</li>
      <li>The rollback plan is present and validated.</li>
      <li>The gate outcome is one of three clear categories: Go, Conditional Go, or No-Go.</li>
      <li>The memo includes a rationale that explains the decision in one paragraph.</li>
      <li>Conditional Go items have specific, dated conditions.</li>
      <li>The memo is signed or electronically approved by QA lead, project lead, and business owner.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Approving a release without reviewing evidence.</strong> Consequence: the sign-off is a formality. A critical defect or missing test case is discovered in production, and the QA memo is cited as evidence that the release was approved, which damages QA credibility.</li>
      <li><strong>Using ambiguous outcomes like "almost ready."</strong> Consequence: the deployment team does not know whether to proceed. The steering committee makes an uninformed decision. The memo does not serve as a clear record.</li>
      <li><strong>Missing documented risk acceptance.</strong> Consequence: when an open defect hits production, there is no record that the business owner accepted it. Blame shifts to QA, and the sign-off is questioned.</li>
      <li><strong>Ignoring the rollback plan.</strong> Consequence: the release fails and the team does not know how to revert. Downtime extends while the rollback steps are reconstructed from memory.</li>
      <li><strong>Reviewing only the test pass rate.</strong> Consequence: the review misses that the test cases themselves were weak, that defects were closed without retest, or that requirements were not traced. The pass rate is a necessary but not sufficient condition.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A generic email: "The QA team has reviewed the release and everything looks good. We found a few minor issues but they are not blockers. The team is ready to go live. Please approve." No evidence summary, no criteria, no defect counts, no coverage percentage, no open risks, no rollback check, no signatures.</p>
    <p><strong>Why it fails:</strong> It cannot be audited. It provides no record of what was reviewed. It cannot be used in a retrospective to understand what went wrong. It is not a quality gate; it is a request for trust.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: QA Sign-Off Memo
release: S/4 2026.06 Wave 2
gate: QA Gate before Production
date: 2026-06-12
---

## Evidence summary
- Test cases planned: 45
- Test cases executed: 45 (100%)
- Test cases passed: 43
- Critical defects open: 0
- Major defects open: 1
- Minor defects open: 2
- Untested requirements: 0

## Criteria evaluation
| Criterion | Threshold | Actual | Status |
|-----------|-----------|--------|--------|
| Test coverage | ≥ 90% | 100% | Met |
| Critical defects open | 0 | 0 | Met |
| Major defects open | ≤ 2 | 1 | Met |
| Rollback plan tested | Yes | Yes | Met |
| Business acceptance | Signed | Signed | Met |

## Open risks
| Risk | Impact | Mitigation | Accepted by | Date |
|------|--------|------------|-------------|------|
| DEF-004 label typo | Low | Fix in first patch | Business Owner | 2026-06-12 |

## Gate outcome
- **Recommendation:** Go
- **Rationale:** All criteria are met. One major defect is open but has a tested workaround accepted by the business owner. The rollback plan was executed successfully in the QA environment. Test coverage is complete.

## Signatures
- QA Lead: D. Kharlanau, 2026-06-12
- Project Lead: [Name], 2026-06-12
- Business Owner: [Name], 2026-06-12
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> QA lead performing a quality gate review for an enterprise SAP release.</p>
    <p><strong>Context:</strong> You have test execution reports, a defect log, a traceability matrix, release documentation, and quality gate criteria. You need to produce a QA Sign-Off Memo that evaluates the evidence and gives a clear recommendation.</p>
    <p><strong>Task:</strong> Calculate coverage, compare defect counts to thresholds, verify traceability, check the rollback plan, confirm risk acceptance, and produce a memo with a Go, Conditional Go, or No-Go outcome.</p>
    <p><strong>Output format:</strong> QA Sign-Off Memo in Markdown, using the compact template, including an evidence summary table and a criteria evaluation table.</p>

    <ul>
      <li><strong>Never produce a sign-off memo without reviewing the actual evidence.</strong> If inputs are missing, state the gaps and recommend No-Go until they are provided.</li>
      <li><strong>Always use a clear three-outcome classification.</strong> Do not use ambiguous language. Go means all criteria met. Conditional Go means criteria met with minor accepted risks and dated conditions. No-Go means criteria not met or significant risks remain.</li>
      <li><strong>Always require documented risk acceptance for any open defect or untested area.</strong> Name the stakeholder, the date, and the mitigation. Unaccepted risks block the gate.</li>
      <li><strong>Always verify the rollback plan.</strong> A missing or untested rollback plan is a No-Go criterion regardless of how good the test results are.</li>
      <li><strong>Do not invent test results, defect counts, or stakeholder signatures.</strong> Use the evidence provided. If evidence is inconsistent, flag the inconsistency.</li>
      <li><strong>Link to Atlas diagnostics</strong> when open defects touch SAP processes. Reference the relevant diagnostic page to add context to the risk assessment.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/testing-quality-delivery/test-evidence-review-working-skill/">Test Evidence Review</a> — Verifies that test execution evidence is complete before the QA review.</li>
      <li><a href="/skill-hub/testing-quality-delivery/defect-triage-classification-working-skill/">Defect Triage and Classification</a> — Produces the defect log that the QA review evaluates.</li>
      <li><a href="/skill-hub/testing-quality-delivery/deployment-readiness-checklist-working-skill/">Deployment Readiness Checklist</a> — Confirms deployment prerequisites after QA sign-off.</li>
      <li><a href="/skill-hub/testing-quality-delivery/release-risk-review-working-skill/">Release Risk Review</a> — Assesses final risk for the go/no-go decision.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Context for reviewing scheduled job test coverage.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Reference for integration test coverage in the QA review.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of QA gate review practices. It is not official ISTQB, BABOK, or SAP documentation. It focuses on enterprise release quality gates where documented evidence and stakeholder acceptance are required.</p>
    <p>Known limitations: the skill assumes that quality gate criteria are predefined. It does not cover continuous deployment pipelines where every commit is automatically released. It does not address formal safety or medical device certification (FDA, IEC 62304), which require specialized quality gate frameworks. The rollback plan validation assumes a separate environment; in some organizations, rollback is only testable in production-like systems that may not be available.</p>
  </section>
</article>
