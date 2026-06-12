---
layout: default
title: "Test Evidence Review Working Skill"
description: "Review executed test evidence for completeness, accuracy, and traceability so the test record is audit-ready and credible."
permalink: /skill-hub/testing-quality-delivery/test-evidence-review-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">Test Evidence Review</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>Test Evidence Review Working Skill</h1>
  <p class="lead">Produce a Test Evidence Review Report that confirms executed test results are complete, accurate, traceable to requirements, and credible enough for audit and release decisions.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Test execution produces evidence: screenshots, logs, IDoc numbers, order numbers, and status records. This evidence is the proof that the system was tested and that it behaved as expected. However, evidence is often incomplete, inconsistent, or untraceable. Screenshots are missing. Test cases are marked "passed" without evidence. Expected results are not stated. Defects are linked to the wrong requirement. This skill reviews the test evidence systematically to ensure it is complete, accurate, traceable, and credible. The output is a Test Evidence Review Report that identifies gaps, requests corrections, and certifies the evidence package for QA sign-off and audit.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Test execution has finished and the evidence must be reviewed before QA sign-off.</li>
      <li>An audit or compliance review requires evidence that testing was performed and documented.</li>
      <li>Test cases are marked passed but the evidence is missing, vague, or inconsistent.</li>
      <li>A defect was found during testing and the evidence does not clearly show the failure and the retest.</li>
      <li>The project lead suspects that test results were padded or that failed cases were marked passed without proper resolution.</li>
      <li>Test evidence must be handed over to operations or support as part of the release documentation.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Missing screenshots in a regulatory audit</h3>
    <p>A pharmaceutical company requires documented evidence for every validated SAP change. The test team executed 50 cases and marked them all passed. The evidence review discovers that 12 cases have no screenshots, 5 screenshots show a different system client than the test environment, and 3 cases have no traceability to requirements. The review must request the missing evidence, verify the client consistency, and add the requirement links before the audit. Without the review, the audit fails and the release is blocked for two weeks.</p>

    <h3>Inconsistent IDoc status evidence</h3>
    <p>A test case verifies that customer IDocs process successfully within five minutes. The evidence shows the IDoc number and a status 53 screenshot, but the timestamp on the screenshot is from a different day than the test execution date. The review must flag the inconsistency, request the correct evidence, and verify the actual processing time. Without the review, the release proceeds with unverified performance claims, and the IDoc processing time degrades in production.</p>

    <h3>Defect retest without before-and-after evidence</h3>
    <p>A defect in the pricing procedure was fixed and retested. The test case is marked passed, but the evidence only shows the after-fix screenshot. The review requires the before-fix evidence (the failure) and the after-fix evidence (the success) to prove that the fix addressed the reported issue. Without the review, the defect could have been closed on a different scenario, and the original issue recurs in production.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Test Case Document with planned cases, expected results, and traceability links.</li>
      <li>Test execution log or report showing which cases were executed, by whom, and when.</li>
      <li>Test evidence attachments: screenshots, logs, documents, IDoc numbers, order numbers, and report outputs.</li>
      <li>Defect log showing defects found, their status, and retest evidence.</li>
      <li>Traceability matrix showing requirements mapped to test cases and defects.</li>
      <li>Environment configuration records showing which system and client were used for each test.</li>
      <li>Review criteria from the QA policy or regulatory standard defining what evidence is required.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Does every executed test case have evidence attached, and does the evidence match the case description?</li>
      <li>Does the evidence show the system identifier (client, URL, environment) used for the test?</li>
      <li>Does the evidence include the expected result, the actual result, and a clear indication of pass or fail?</li>
      <li>Are dates and timestamps in the evidence consistent with the test execution schedule?</li>
      <li>For failed cases, is there evidence of the failure, the defect report, and the retest after fix?</li>
      <li>Does every case trace to a requirement, and does every defect trace to a case and a requirement?</li>
      <li>Is the evidence readable, complete, and stored in a location that is accessible for audit?</li>
      <li>Are there cases that were marked passed but the evidence is missing, ambiguous, or from a different test?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Gather the evidence package.</strong> Collect all test execution reports, evidence attachments, defect logs, and traceability matrices. Ensure the package is complete and versioned.</li>
      <li><strong>Verify evidence completeness.</strong> For every test case marked as executed, check that evidence is present. If a case is missing evidence, flag it as "evidence gap" and request the tester to provide it.</li>
      <li><strong>Verify evidence accuracy.</strong> Check that the evidence matches the test case description. For example, if the case tests a credit block, the evidence must show the blocked order, not a successful order. If the case tests IDoc processing, the evidence must show the IDoc number and status. Mismatches are flagged as "evidence mismatch."</li>
      <li><strong>Verify environment consistency.</strong> Check that the system, client, URL, or environment name visible in the evidence matches the approved test environment. Evidence from production or a different client is invalid and must be rejected.</li>
      <li><strong>Verify traceability.</strong> Confirm that every test case links to a requirement and that every defect links to a test case and a requirement. Orphan evidence (cases with no requirement, defects with no case) is flagged as "traceability gap."</li>
      <li><strong>Verify defect closure evidence.</strong> For every defect marked closed, confirm that there is evidence of the original failure and evidence of the retest after fix. Defects closed without both pieces of evidence are flagged as "closure incomplete."</li>
      <li><strong>Verify timestamp consistency.</strong> Check that dates and timestamps in the evidence are consistent with the test execution schedule. Evidence dated before the test started or after it ended is suspicious and must be investigated.</li>
      <li><strong>Document findings in the review report.</strong> Use the template below. For each finding, state the case ID, the finding type (gap, mismatch, traceability, closure, timestamp), the severity, and the required correction.</li>
      <li><strong>Request corrections.</strong> Send the report to the test lead or tester with a deadline for corrections. Re-review the corrected evidence before finalizing the report.</li>
      <li><strong>Certify the evidence package.</strong> Once all findings are resolved, produce a final Test Evidence Review Report that certifies the evidence as complete, accurate, and traceable. Include the reviewer name, date, and scope of the certification.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a test case has no evidence, it is not considered executed. Mark it as "not executed" until evidence is provided.</li>
      <li>If evidence is from a different environment than the approved test system, reject it and request re-execution in the correct environment.</li>
      <li>If a defect is closed without retest evidence, reopen the defect and require retest evidence before closing it again.</li>
      <li>If evidence is ambiguous but the case is clearly correct, request clearer evidence rather than accepting ambiguity.</li>
      <li>If a timestamp inconsistency is minor (e.g., screenshot taken one minute after case completion due to file save delay), accept it with a note. If it is major (e.g., different day), investigate and reject.</li>
      <li>If the traceability matrix is missing or incomplete, require it to be updated before the evidence is certified.</li>
      <li>If all findings are resolved and the evidence package is complete, the package is certified for QA sign-off and audit.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Test Evidence Review Report</strong> — Per test cycle or per release. Contains findings, corrections requested, and certification status. See template below.</li>
      <li><strong>Corrected Evidence Package</strong> — Updated evidence attachments that address all findings.</li>
      <li><strong>Certification Statement</strong> — Formal statement that the evidence package is complete, accurate, and traceable, signed by the reviewer.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Test Evidence Review Report (compact)</h3>
    <pre><code>---
artifact: Test Evidence Review Report
cycle: &lt;Test cycle or release&gt;
reviewer: &lt;Name&gt;
date: &lt;YYYY-MM-DD&gt;
---

## Scope
- Test cases reviewed: &lt;count&gt;
- Evidence items reviewed: &lt;count&gt;
- Defects reviewed: &lt;count&gt;
- Requirements traced: &lt;count&gt;

## Findings
| Case ID | Finding Type | Severity | Description | Required Correction | Status |
|---------|--------------|----------|-------------|---------------------|--------|
| TC-001 | Evidence gap | High | No screenshot attached | Provide screenshot of saved order | Open |
| TC-002 | Mismatch | Medium | Screenshot shows different material than case specifies | Re-execute with correct material or update case | Open |
| TC-003 | Traceability | High | Case not linked to any requirement | Link to REQ-003 and update matrix | Open |
| TC-004 | Closure | High | Defect DEF-001 closed without retest evidence | Provide retest screenshot and re-close | Open |
| TC-005 | Timestamp | Low | Screenshot timestamp 2 minutes after execution | Accept with note | Closed |

## Summary
- Findings open: &lt;count&gt;
- Findings closed: &lt;count&gt;
- Evidence package status: Not certified / Certified pending corrections / Certified

## Certification
- **Status:** Not certified / Certified
- **Scope:** Evidence package for cycle &lt;name&gt;
- **Certified by:** ___________________ Date: _________
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every executed test case has evidence that is present, readable, and matches the case description.</li>
      <li>Evidence is from the approved test environment, not from production or an unapproved system.</li>
      <li>Every case traces to a requirement, and every defect traces to a case and a requirement.</li>
      <li>Every closed defect has both failure evidence and retest evidence.</li>
      <li>Timestamps in evidence are consistent with the test execution schedule.</li>
      <li>The review report documents every finding with a type, severity, and required correction.</li>
      <li>All findings are resolved before the evidence package is certified.</li>
      <li>The certification statement is signed, dated, and scoped to a specific test cycle or release.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Accepting test results without reviewing evidence.</strong> Consequence: cases are marked passed with no proof. The audit fails, the release is blocked, and the QA sign-off is questioned.</li>
      <li><strong>Ignoring environment mismatches in evidence.</strong> Consequence: evidence from production or a different client is accepted as valid. The test does not actually prove the change works in the target environment.</li>
      <li><strong>Allowing defect closure without retest evidence.</strong> Consequence: defects are assumed fixed but were never verified. They recur in production, causing rework and trust erosion.</li>
      <li><strong>Reviewing evidence only for failed cases.</strong> Consequence: passed cases with missing or incorrect evidence are overlooked, and the pass rate is inflated. The coverage claim is false.</li>
      <li><strong>Storing evidence in inaccessible locations.</strong> Consequence: when the audit or support team needs the evidence, it cannot be found. The certification is meaningless if the package is lost.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A simple confirmation: "All test cases have been executed and passed. Evidence is attached in the shared folder. No issues found." No review of individual evidence items, no traceability check, no environment verification, no defect closure verification, no findings, no certification.</p>
    <p><strong>Why it fails:</strong> It is not a review; it is a statement of trust. If evidence is missing, mismatched, or from the wrong environment, the confirmation is false. It cannot be used in an audit or a retrospective. It provides no basis for improvement.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Test Evidence Review Report
cycle: UAT Wave 2
reviewer: D. Kharlanau
date: 2026-06-12
---

## Scope
- Test cases reviewed: 45
- Evidence items reviewed: 45
- Defects reviewed: 5
- Requirements traced: 12

## Findings
| Case ID | Finding Type | Severity | Description | Required Correction | Status |
|---------|--------------|----------|-------------|---------------------|--------|
| TC-001 | Evidence gap | High | No screenshot of saved order | Provide screenshot | Open |
| TC-002 | Mismatch | Medium | Screenshot shows material M-002 instead of M-001 | Re-execute with M-001 | Open |
| TC-003 | Traceability | High | Not linked to requirement | Link to REQ-003 | Open |
| DEF-001 | Closure | High | Closed without retest evidence | Provide retest screenshot | Open |
| TC-005 | Timestamp | Low | 2 min after execution | Accept with note | Closed |

## Summary
- Findings open: 4
- Findings closed: 1
- Status: Certified pending corrections

## Certification
- **Status:** Certified pending corrections
- **Scope:** UAT Wave 2 evidence package
- **Certified by:** D. Kharlanau, 2026-06-12
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Test evidence reviewer for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have test execution reports, evidence attachments, defect logs, and a traceability matrix. You need to produce a Test Evidence Review Report that verifies completeness, accuracy, traceability, and environment consistency.</p>
    <p><strong>Task:</strong> Review every executed case for evidence presence and accuracy. Verify environment consistency. Verify traceability. Verify defect closure evidence. Document findings, request corrections, and certify the package when resolved.</p>
    <p><strong>Output format:</strong> Test Evidence Review Report in Markdown, using the compact template with a findings table and a certification section.</p>

    <ul>
      <li><strong>Never certify an evidence package without reviewing every executed case.</strong> A sampling approach is acceptable only if the sampling method is documented and approved; otherwise, review every case.</li>
      <li><strong>Always reject evidence from the wrong environment.</strong> Evidence from production or a different client does not prove the change works in the target environment.</li>
      <li><strong>Always require retest evidence for closed defects.</strong> A defect is not closed until the original failure and the post-fix success are both documented.</li>
      <li><strong>Always verify traceability.</strong> Orphan cases and orphan defects are gaps that must be fixed before certification.</li>
      <li><strong>Always document findings with severity and required corrections.</strong> Vague findings like "check evidence" are not actionable.</li>
      <li><strong>Do not invent evidence, timestamps, or traceability links.</strong> Use the inputs provided. If inputs are missing, flag the gap as a finding.</li>
      <li><strong>Link to Atlas diagnostics</strong> when findings touch SAP-specific evidence. For example, IDoc status evidence should be evaluated against <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> for correct status codes.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/testing-quality-delivery/test-case-design-working-skill/">Test Case Design</a> — Provides the cases and expected results that evidence must match.</li>
      <li><a href="/skill-hub/testing-quality-delivery/qa-review-sign-off-working-skill/">QA Review and Sign-Off</a> — Uses the certified evidence package for the quality gate.</li>
      <li><a href="/skill-hub/testing-quality-delivery/defect-triage-classification-working-skill/">Defect Triage and Classification</a> — Provides the defect log that the evidence review verifies.</li>
      <li><a href="/skill-hub/decision-validation/traceability-matrix-working-skill/">Traceability Matrix</a> — Provides the requirement-to-case mapping that the review verifies.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Reference for evaluating IDoc evidence and status codes.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Context for reviewing batch job execution evidence.</li>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Reference for credit block evidence verification.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of test evidence review practices. It is not official ISTQB, GxP, or SAP documentation. It focuses on enterprise contexts where test evidence must be credible for audit, compliance, and release decisions.</p>
    <p>Known limitations: the skill assumes that evidence is stored in a retrievable format (screenshots, logs, documents). It does not cover video recordings or automated test tool exports, which may require specialized review methods. It does not address regulatory validation standards (e.g., FDA 21 CFR Part 11) that require electronic signatures and audit trails on the evidence itself. The review process is manual; large-scale automated testing may require sampling strategies not covered here.</p>
  </section>
</article>
