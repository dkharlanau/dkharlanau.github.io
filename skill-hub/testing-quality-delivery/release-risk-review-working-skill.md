---
layout: default
title: "Release Risk Review Working Skill"
description: "Assess release risk by weighing open defects, untested areas, dependency changes, and business impact so the go/no-go decision is evidence-based."
permalink: /skill-hub/testing-quality-delivery/release-risk-review-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">Release Risk Review</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>Release Risk Review Working Skill</h1>
  <p class="lead">Produce a Release Risk Assessment that weighs open defects, untested areas, dependency changes, and business impact to produce an evidence-based go/no-go recommendation.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>The release risk review is the final decision point before a change is introduced to production. It is not a test status report; it is a risk assessment that combines technical, procedural, and business factors into a single judgment. This skill helps the project lead, QA lead, and business owner assemble the relevant risk factors, score them, and produce a Release Risk Assessment that supports a go, no-go, or conditional go decision. The assessment is the document that the steering committee or CAB reviews when deciding whether to approve the release. A structured risk review prevents releases that are likely to fail and provides defensible rationale for delaying or proceeding.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A release is scheduled and the steering committee or CAB must make a go/no-go decision.</li>
      <li>Defects remain open, untested areas exist, and the project lead needs a structured way to assess whether the risk is acceptable.</li>
      <li>Multiple changes are bundled into one release, and the cumulative risk must be evaluated.</li>
      <li>A previous release failed, and the team wants to ensure that the same risk factors are not repeated.</li>
      <li>The business owner is pressuring for an early go-live, and the QA lead needs an objective risk framework to support a delay.</li>
      <li>An audit or governance review requires evidence that release decisions were risk-based and documented.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP transport bundle: cumulative risk from multiple changes</h3>
    <p>A release contains three transports: a pricing procedure change, a new custom report, and a security patch. Individually, each is low risk. Together, the pricing change affects the report's input data, and the security patch changes authorizations that the report relies on. The risk review must assess the interaction risk, not only the individual risks. Without the review, the release is approved because each item is low risk, but the combination causes the report to fail on the first Monday run because the new security patch removes an authorization the report needs.</p>

    <h3>Data migration weekend: untested rollback scenario</h3>
    <p>A master data migration is scheduled for the weekend. The test evidence shows that the migration loads correctly in the quality system. However, the risk review discovers that the rollback script has never been tested with the full data volume, and the business owner is unavailable during the migration window. The risk review scores the rollback risk as high and the business impact as critical. Without the review, the migration proceeds, fails at 2 AM, and the untested rollback takes 8 hours to execute with business downtime.</p>

    <h3>Integration go-live: dependency on external system availability</h3>
    <p>A new IDoc interface is ready for production. The SAP side is tested and stable. The risk review assesses the external dependency: the e-commerce platform's availability window, the network path, and the fallback if the platform is down. The review discovers that the external platform has a planned maintenance window on the same weekend as the go-live. Without the review, the interface is activated, the platform is down, and IDocs queue until the platform returns, causing a backlog that requires manual cleanup.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>QA Sign-Off Memo showing the quality gate outcome and any conditional items.</li>
      <li>Deployment Readiness Checklist showing the technical and procedural prerequisites.</li>
      <li>Defect Triage Log with current open defects, their severity, priority, and business impact.</li>
      <li>Regression Test Plan showing what was tested and what was excluded, with rationale.</li>
      <li>Test Evidence Review Report certifying the completeness and accuracy of test evidence.</li>
      <li>Change description or release notes listing every change, dependency, and known issue.</li>
      <li>Business impact assessment: which processes, users, and revenue streams are affected by the release.</li>
      <li>External dependency status: third-party systems, network paths, and scheduled maintenance windows.</li>
      <li>Rollback plan with estimated time, resources, and prerequisites.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the worst defect that could occur in production, and what is the business impact?</li>
      <li>Which areas were not tested, and what is the probability and impact of failure in those areas?</li>
      <li>Which external dependencies could fail, and what is the fallback if they do?</li>
      <li>Is the rollback plan tested, and can it be executed within the maintenance window?</li>
      <li>What is the cumulative risk of multiple changes bundled together, including interaction risks?</li>
      <li>Is the business owner available during the deployment window and the first business day after?</li>
      <li>What is the cost of delaying the release versus the cost of a production failure?</li>
      <li>Has a similar release failed before, and what were the contributing risk factors?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Gather all risk inputs.</strong> Collect the QA sign-off, deployment readiness checklist, defect log, test evidence review, change description, and business impact assessment. Ensure they are current and consistent.</li>
      <li><strong>Identify risk categories.</strong> Group risks into four categories: Technical (defects, untested areas, code quality), Procedural (rollback, monitoring, support readiness), Dependency (external systems, networks, third parties), and Business (revenue impact, user readiness, regulatory deadline).</li>
      <li><strong>Identify specific risk items.</strong> Within each category, list concrete risks: open critical defect, untested credit block scenario, untested rollback plan, external maintenance window conflict, business owner unavailable. Be specific, not generic.</li>
      <li><strong>Score each risk item.</strong> Use a simple scale: Impact (1–3, where 3 is critical business impact) and Probability (1–3, where 3 is high probability). Multiply to get a Risk Score (1–9). This is not a precise actuarial calculation; it is a structured way to compare risks.</li>
      <li><strong>Assess interaction risks.</strong> For releases with multiple changes, identify risks that only exist because of the combination. For example, a pricing change and a report change may interact. Score these interaction risks separately.</li>
      <li><strong>Identify mitigations.</strong> For each risk with score 4 or higher, define a mitigation: fix the defect before release, test the rollback plan, reschedule to avoid the external maintenance window, or assign a standby business owner. If no mitigation exists, the risk is unmitigated.</li>
      <li><strong>Calculate overall risk posture.</strong> Count the number of high-score risks (7–9), medium-score risks (4–6), and low-score risks (1–3). Summarize the posture: predominantly low risk, mixed risk, or predominantly high risk. Note the number of unmitigated high risks.</li>
      <li><strong>Produce the Release Risk Assessment.</strong> Use the template below. Include risk categories, risk items with scores, mitigations, overall posture, and the go/no-go/conditional recommendation.</li>
      <li><strong>Review with stakeholders.</strong> Walk through the assessment with the project lead, QA lead, business owner, and operations lead. Confirm that the risks are understood and the mitigations are accepted.</li>
      <li><strong>Record the decision.</strong> Attach the assessment to the project records. If the decision is go, schedule the deployment. If the decision is no-go, document the conditions that must be met before the next review. If conditional, list the conditions and the monitoring plan.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If any unmitigated risk has a score of 9, the recommendation is No-Go unless the executive sponsor formally accepts the risk with a documented business justification.</li>
      <li>If there are two or more unmitigated medium risks (score 4–6), the recommendation is Conditional Go with a mitigation plan.</li>
      <li>If all high risks are mitigated and only low risks remain, the recommendation is Go.</li>
      <li>If the rollback plan is untested or the external dependency is unstable, the recommendation is No-Go regardless of test pass rate.</li>
      <li>If the business owner is unavailable during the deployment and the first business day after, the recommendation is Conditional Go with a standby contact requirement.</li>
      <li>If a similar release failed recently and the same risk factors are present, the recommendation is No-Go until the factors are addressed.</li>
      <li>If the cost of a production failure exceeds the cost of a one-week delay, the recommendation is No-Go when any high risk remains unmitigated.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Release Risk Assessment</strong> — Per release or per CAB review. Contains risk categories, risk items with scores, mitigations, overall posture, and recommendation. See template below.</li>
      <li><strong>Risk Mitigation Plan</strong> — For conditional go or no-go scenarios, the specific actions required to reduce risk before the next review.</li>
      <li><strong>Decision Record</strong> — Documented go/no-go/conditional decision with named decision-makers, dates, and rationale.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Release Risk Assessment (compact)</h3>
    <pre><code>---
artifact: Release Risk Assessment
release: &lt;Release name&gt;
review date: &lt;YYYY-MM-DD&gt;
reviewers: &lt;Names&gt;
---

## Risk categories and items

### Technical risks
| ID | Risk | Impact | Probability | Score | Mitigation | Status |
|----|------|--------|-------------|-------|------------|--------|
| T1 | Open critical defect in pricing | 3 | 2 | 6 | Fix before release | Mitigated |
| T2 | Untested credit block boundary | 3 | 1 | 3 | Add test case and execute | Mitigated |
| T3 | Untested rollback script | 3 | 3 | 9 | Test rollback in QA | Unmitigated |

### Procedural risks
| ID | Risk | Impact | Probability | Score | Mitigation | Status |
|----|------|--------|-------------|-------|------------|--------|
| P1 | Support team not briefed | 2 | 2 | 4 | Briefing scheduled | Mitigated |
| P2 | Monitoring not configured | 2 | 2 | 4 | Configure alerts | Mitigated |

### Dependency risks
| ID | Risk | Impact | Probability | Score | Mitigation | Status |
|----|------|--------|-------------|-------|------------|--------|
| D1 | External platform maintenance | 3 | 3 | 9 | Reschedule release | Unmitigated |

### Business risks
| ID | Risk | Impact | Probability | Score | Mitigation | Status |
|----|------|--------|-------------|-------|------------|--------|
| B1 | Business owner unavailable | 2 | 2 | 4 | Assign standby contact | Mitigated |

## Interaction risks
| ID | Risk | Score | Mitigation | Status |
|----|------|-------|------------|--------|
| I1 | Pricing change + report auth conflict | 6 | Test report with new auth | Mitigated |

## Overall posture
- High risks (7–9): 2 (T3, D1)
- Medium risks (4–6): 2 (T1, I1)
- Low risks (1–3): 1 (T2)
- Unmitigated high risks: 2

## Recommendation
- **Go / Conditional Go / No-Go:** No-Go
- **Rationale:** Two unmitigated high risks exist: the rollback script is untested, and the external platform has a maintenance window. Both must be resolved before release.
- **Conditions for next review:** Rollback tested in QA by 2026-06-14. External platform confirms no conflict by 2026-06-14.

## Decision record
- **Decision:** No-Go
- **Decision makers:** Project Lead, QA Lead, Business Owner
- **Date:** 2026-06-12
- **Next review:** 2026-06-15
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every risk item is specific, not generic (e.g., "untested rollback script" not "technical risk").</li>
      <li>Every risk item has an impact score, a probability score, and a calculated risk score.</li>
      <li>High risks (score 7–9) are identified and have mitigations or are explicitly accepted.</li>
      <li>Interaction risks between multiple changes are assessed separately.</li>
      <li>The overall risk posture is summarized with counts of high, medium, and low risks.</li>
      <li>The recommendation is one of three clear categories: Go, Conditional Go, or No-Go.</li>
      <li>The rationale explains the recommendation in terms of the highest risks and their mitigations.</li>
      <li>Conditional Go and No-Go decisions have specific, dated conditions for the next review.</li>
      <li>The decision is recorded with named decision-makers, dates, and next review date.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Assessing only test pass rate as the risk metric.</strong> Consequence: untested rollback plans, external dependencies, and procedural gaps are ignored. The release fails for reasons that were never tested.</li>
      <li><strong>Ignoring interaction risks between multiple changes.</strong> Consequence: each change is low risk individually, but the combination creates a high-risk scenario that is never assessed. The release fails on an interaction that no one considered.</li>
      <li><strong>Using generic risk categories without specific items.</strong> Consequence: the assessment is a template exercise. "Technical risk: medium" is not actionable. Specific items like "untested rollback script: score 9" are actionable.</li>
      <li><strong>Approving a release with unmitigated high risks because of schedule pressure.</strong> Consequence: the production failure validates the risk. The decision is not defensible, and accountability is unclear.</li>
      <li><strong>Not recording the decision and rationale.</strong> Consequence: when the release fails, there is no record of what was known and why the decision was made. Lessons learned are impossible.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A generic risk statement: "The release has some risks but the team is confident. Testing went well. There are a few open defects but they are minor. We recommend go-live." No risk categories, no specific items, no scores, no mitigations, no interaction risks, no decision record, no conditions.</p>
    <p><strong>Why it fails:</strong> It is not an assessment; it is an opinion. It cannot be reviewed, challenged, or audited. It provides no basis for a conditional go or no-go. If the release fails, the assessment offers no insight into what went wrong.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Release Risk Assessment
release: S/4 2026.06 Wave 2
review date: 2026-06-12
reviewers: Project Lead, QA Lead, Business Owner
---

## Technical risks
| ID | Risk | Impact | Probability | Score | Mitigation | Status |
|----|------|--------|-------------|-------|------------|--------|
| T1 | Untested rollback script | 3 | 3 | 9 | Test in QA by 2026-06-14 | Unmitigated |
| T2 | Open critical defect | 3 | 2 | 6 | Fix before release | Mitigated |

## Dependency risks
| ID | Risk | Impact | Probability | Score | Mitigation | Status |
|----|------|--------|-------------|-------|------------|--------|
| D1 | External platform maintenance | 3 | 3 | 9 | Reschedule | Unmitigated |

## Overall posture
- High risks: 2
- Medium risks: 1
- Low risks: 0
- Unmitigated high: 2

## Recommendation
- **No-Go**
- **Rationale:** Two unmitigated high risks exist. Rollback is untested and the external platform has a maintenance window. Both must be resolved before release.
- **Conditions:** Rollback tested by 2026-06-14. Platform confirms no conflict by 2026-06-14.

## Decision record
- **Decision:** No-Go
- **Date:** 2026-06-12
- **Next review:** 2026-06-15
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Release risk assessor for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have QA sign-off, deployment readiness, defect logs, test evidence, change descriptions, and business impact data. You need to produce a Release Risk Assessment that supports a go/no-go decision.</p>
    <p><strong>Task:</strong> Identify specific risks in four categories (technical, procedural, dependency, business), score each by impact and probability, assess interaction risks, define mitigations, summarize the overall posture, and give a clear recommendation.</p>
    <p><strong>Output format:</strong> Release Risk Assessment in Markdown, using the compact template with risk tables, interaction risk section, overall posture, recommendation, and decision record.</p>

    <ul>
      <li><strong>Never recommend go-live if an unmitigated high risk exists.</strong> Flag the risk and recommend No-Go or Conditional Go with a mitigation plan.</li>
      <li><strong>Always assess interaction risks.</strong> Multiple low-risk changes can combine into a high-risk scenario. Assess the bundle, not only the items.</li>
      <li><strong>Always use specific risk items, not generic categories.</strong> "Technical risk: medium" is not acceptable. "Untested rollback script: score 9" is acceptable.</li>
      <li><strong>Always define mitigations for high and medium risks.</strong> If no mitigation exists, the risk is unmitigated and must be addressed before release.</li>
      <li><strong>Always record the decision with named decision-makers and a next review date.</strong> undocumented decisions are not defensible.</li>
      <li><strong>Do not invent risk scores, mitigations, or stakeholder decisions.</strong> Use the inputs provided. If a risk factor is unknown, flag it as "unknown — assess before release."</li>
      <li><strong>Link to Atlas diagnostics</strong> when technical risks touch SAP processes. Reference relevant diagnostics to add context to the risk item.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/testing-quality-delivery/qa-review-sign-off-working-skill/">QA Review and Sign-Off</a> — Provides the quality gate evidence that feeds into the risk assessment.</li>
      <li><a href="/skill-hub/testing-quality-delivery/deployment-readiness-checklist-working-skill/">Deployment Readiness Checklist</a> — Provides procedural readiness data for the risk review.</li>
      <li><a href="/skill-hub/testing-quality-delivery/defect-triage-classification-working-skill/">Defect Triage and Classification</a> — Provides the defect log that the risk review evaluates.</li>
      <li><a href="/skill-hub/decision-validation/risk-dependency-mapping-working-skill/">Risk and Dependency Mapping</a> — Provides the dependency and risk analysis methods used in the assessment.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — Context for dependency and interaction risk assessment.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Reference for procedural risks involving scheduled jobs.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Reference for interface-related technical risks.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of release risk assessment practices. It is not official ITIL, BABOK, or SAP documentation. It focuses on enterprise release governance where go/no-go decisions require documented evidence and stakeholder accountability.</p>
    <p>Known limitations: the risk scoring is intentionally simple (impact × probability) and may not satisfy organizations with formal enterprise risk management frameworks. The skill does not cover quantitative risk modeling, Monte Carlo simulations, or financial risk analysis. It assumes that the necessary inputs (QA sign-off, defect logs, deployment readiness) are available. If inputs are missing, the assessment must flag gaps rather than proceed with incomplete data.</p>
  </section>
</article>
