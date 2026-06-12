---
layout: default
title: "Deployment Readiness Checklist Working Skill"
description: "Confirm that every prerequisite for safe deployment is complete: tests passed, rollback plan ready, stakeholders informed, monitoring active."
permalink: /skill-hub/testing-quality-delivery/deployment-readiness-checklist-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">Deployment Readiness Checklist</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>Deployment Readiness Checklist Working Skill</h1>
  <p class="lead">Produce a Deployment Readiness Checklist that verifies every technical, procedural, and stakeholder prerequisite for safe deployment is complete before the release moves to production.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Deployment readiness is the last checkpoint before a change is introduced into the production environment. It is not only about whether the code works; it is about whether the organization is ready to receive it. This skill covers the full set of prerequisites: technical (transports, scripts, data loads), procedural (rollback plan, communication plan, maintenance window), and human (stakeholders informed, support team briefed, monitoring active). The output is a Deployment Readiness Checklist that is reviewed and signed off by the deployment lead, the QA lead, and the business owner before the deployment window opens.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A release has passed QA sign-off and is scheduled for deployment to production.</li>
      <li>A transport or set of transports is ready to be imported into the production system.</li>
      <li>A data migration, patch, or emergency fix requires a documented readiness check before execution.</li>
      <li>The operations team requires evidence that all prerequisites are met before granting the deployment window.</li>
      <li>A post-mortem revealed that a previous deployment failed due to a missing prerequisite, and the team wants to prevent recurrence.</li>
      <li>An audit requires a checklist showing that deployments follow a controlled process.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP transport import: missing prerequisite costs a weekend</h3>
    <p>A transport containing a new pricing condition type is scheduled for Friday evening. The deployment team checks the transport list but misses that a prerequisite transport containing the new condition table was not yet imported. The deployment checklist catches this: the transport list is compared to the dependency matrix, and the missing transport is identified. Without the checklist, the import fails on Friday night, the rollback plan is invoked, and the go-live is delayed by two days.</p>

    <h3>Data migration load: monitoring not configured</h3>
    <p>A customer master data migration is scheduled for the weekend. The checklist verifies that the migration job is defined, the source extract is validated, the target system has space, and the business owner is on standby. However, the checklist also checks that monitoring alerts are configured for the batch job. The alert is missing. Without the checklist, the job fails silently on Saturday morning, and the business discovers the issue on Monday when customer orders cannot be created.</p>

    <h3>Custom code deployment: support team not briefed</h3>
    <p>A new custom report is deployed to production. The checklist verifies that the report is tested, the variant is created, and the job is scheduled. It also checks that the support team has been briefed on the new report, its purpose, and how to troubleshoot it. The briefing is missing. Without the checklist, the first failed job on Monday is escalated to the development team because the support team does not know how to check the variant or rerun the program.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>QA Sign-Off Memo confirming that the release passed the quality gate.</li>
      <li>Release documentation: change description, transport list, object list, and version numbers.</li>
      <li>Dependency matrix showing which transports, patches, or data loads must be in place before this release.</li>
      <li>Rollback plan with steps, estimated duration, and responsible contacts.</li>
      <li>Deployment schedule: maintenance window, start time, estimated duration, and contingency window.</li>
      <li>Communication plan showing who is notified, when, and by what channel.</li>
      <li>Monitoring and alert configuration: which jobs, interfaces, or metrics are watched, and who receives alerts.</li>
      <li>Support team briefing status: who was briefed, on what date, and on which topics.</li>
      <li>Environment readiness: system availability, disk space, backup status, and user access.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Is every transport, patch, or script in the release documented and available in the target system?</li>
      <li>Are all prerequisites and dependencies already deployed and verified?</li>
      <li>Is the rollback plan documented, tested, and executable within the maintenance window?</li>
      <li>Do the operations and support teams know what is changing, when, and how to detect failure?</li>
      <li>Are monitoring and alerting configured for the new or changed components?</li>
      <li>Is the business owner or key user available during the deployment window for validation?</li>
      <li>Has the environment been checked for space, performance, and availability?</li>
      <li>What is the contingency plan if the deployment exceeds the maintenance window?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Gather the release package.</strong> Collect the QA sign-off, transport list, object list, scripts, data loads, and documentation. Verify that the package is complete and versioned.</li>
      <li><strong>Verify the transport or change list.</strong> Compare the list of changes to the release documentation. Ensure every transport number, patch ID, or script name is documented and matches the QA-approved package.</li>
      <li><strong>Verify dependencies.</strong> Check the dependency matrix. Confirm that every prerequisite transport, table, or configuration is already in place in the target environment. If a dependency is missing, halt the checklist until it is resolved.</li>
      <li><strong>Verify the rollback plan.</strong> Confirm that the rollback plan is documented with exact steps, estimated time, and responsible contacts. Confirm that it has been tested or at least validated in a non-production environment. If the rollback plan is untested, mark it as a blocker.</li>
      <li><strong>Verify the deployment schedule.</strong> Confirm the maintenance window, start time, estimated duration, and contingency window. Confirm that the window is approved by the operations team and does not conflict with other scheduled work.</li>
      <li><strong>Verify communication readiness.</strong> Confirm that the communication plan is active: stakeholders are informed, the support team is on standby, and the business owner is available for validation. Confirm that the notification channels are tested.</li>
      <li><strong>Verify monitoring and alerting.</strong> Confirm that monitoring dashboards, job alerts, and interface health checks are configured for the new or changed components. Confirm that the alert recipients are correct and reachable.</li>
      <li><strong>Verify environment readiness.</strong> Confirm that the target system is available, has sufficient disk space, has a recent backup, and that the deployment user has the necessary authorizations.</li>
      <li><strong>Complete the checklist.</strong> Use the template below. Mark each item as Pass, Fail, or Not Applicable. Document any failures and the remediation plan.</li>
      <li><strong>Obtain sign-off.</strong> Review the completed checklist with the deployment lead, QA lead, and operations lead. If any item is Fail, do not proceed until it is remediated and re-verified. Obtain signatures or electronic approval before the deployment window opens.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If any item on the checklist is Fail, the deployment is blocked until the item is remediated and re-verified.</li>
      <li>If the rollback plan is missing or untested, the deployment is blocked regardless of other checklist status.</li>
      <li>If a dependency is missing, the deployment is blocked until the dependency is in place.</li>
      <li>If the maintenance window is not approved or conflicts with other work, reschedule rather than compress.</li>
      <li>If monitoring or alerting is not configured, the deployment is blocked unless the operations team formally accepts the risk.</li>
      <li>If the support team has not been briefed, the deployment is conditional on briefing completion before the window opens.</li>
      <li>If all items are Pass, the deployment is approved to proceed at the scheduled window.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Deployment Readiness Checklist</strong> — Per release or per deployment. Contains checklist items, status, evidence, and sign-off. See template below.</li>
      <li><strong>Remediation Log</strong> — Record of any failed items, the fix applied, and the re-verification result.</li>
      <li><strong>Deployment Execution Log</strong> — Record of actual deployment steps, times, and outcomes (produced after deployment).</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Deployment Readiness Checklist (compact)</h3>
    <pre><code>---
artifact: Deployment Readiness Checklist
release: &lt;Release name&gt;
deployment date: &lt;YYYY-MM-DD HH:MM&gt;
---

## Technical readiness
| Item | Status | Evidence | Checked by | Date |
|------|--------|----------|------------|------|
| Transport list matches release doc | Pass | TR list attached | Deploy Lead | 2026-06-12 |
| All dependencies in place | Pass | Dependency matrix verified | Deploy Lead | 2026-06-12 |
| Rollback plan documented and tested | Pass | Rollback tested in QA | QA Lead | 2026-06-12 |
| Scripts and data loads validated | Pass | Validation report attached | QA Lead | 2026-06-12 |
| Environment space and availability | Pass | Basis check confirmed | Ops Lead | 2026-06-12 |
| Backup completed before window | Pass | Backup log attached | Ops Lead | 2026-06-12 |

## Procedural readiness
| Item | Status | Evidence | Checked by | Date |
|------|--------|----------|------------|------|
| Maintenance window approved | Pass | Change ticket CHG-001 | Ops Lead | 2026-06-12 |
| Communication plan executed | Pass | Email sent 2026-06-11 | Project Lead | 2026-06-12 |
| Support team briefed | Pass | Briefing minutes attached | Support Lead | 2026-06-12 |
| Business owner available | Pass | Confirmed by email | Business Owner | 2026-06-12 |

## Monitoring readiness
| Item | Status | Evidence | Checked by | Date |
|------|--------|----------|------------|------|
| Job alerts configured | Pass | Alert rule ID 101 | Ops Lead | 2026-06-12 |
| Interface monitoring active | Pass | Dashboard link attached | Ops Lead | 2026-06-12 |
| Error log monitoring active | Pass | SM21 filter set | Basis | 2026-06-12 |

## Sign-off
- Deployment Lead: ___________________ Date: _________
- QA Lead: ___________________ Date: _________
- Ops Lead: ___________________ Date: _________
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every checklist item has a status of Pass, Fail, or Not Applicable.</li>
      <li>Every Pass item has evidence referenced or attached.</li>
      <li>Every Fail item has a remediation plan and is re-verified before deployment.</li>
      <li>The rollback plan is present and tested or validated.</li>
      <li>Dependencies are verified against a dependency matrix, not by memory.</li>
      <li>Communication and monitoring are confirmed as active, not just planned.</li>
      <li>The support team is briefed on the change, not just notified of the window.</li>
      <li>The checklist is signed off by deployment lead, QA lead, and operations lead before the window opens.</li>
      <li>No deployment proceeds with a Fail item that has not been re-verified.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Treating the checklist as a formality after the decision to deploy is already made.</strong> Consequence: the checklist is filled in retroactively, failures are overlooked, and the deployment proceeds with missing prerequisites. The checklist is a gate, not a record.</li>
      <li><strong>Skipping the rollback plan verification.</strong> Consequence: the deployment fails and the team spends hours reconstructing the rollback steps. Downtime extends and business impact increases.</li>
      <li><strong>Assuming dependencies are in place without verification.</strong> Consequence: the transport import fails because a prerequisite table or configuration is missing. The deployment window is wasted.</li>
      <li><strong>Not briefing the support team.</strong> Consequence: the first production issue is escalated to the development team because the support team does not know how to diagnose or work around the new component.</li>
      <li><strong>Missing monitoring configuration.</strong> Consequence: a silent failure (e.g., a background job that stops running) is not detected until a business user reports missing data. The delay increases the impact.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A verbal confirmation or a one-line email: "We are good to go. The transport is ready. The team knows what to do. See you at the window." No checklist, no evidence, no rollback verification, no dependency check, no monitoring confirmation, no signatures.</p>
    <p><strong>Why it fails:</strong> It cannot be audited. It provides no proof that prerequisites were met. If the deployment fails, there is no record of what was checked and what was missed. It relies on individual memory and trust.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Deployment Readiness Checklist
release: S/4 2026.06 Wave 2
deployment date: 2026-06-14 22:00
---

## Technical readiness
| Item | Status | Evidence | Checked by | Date |
|------|--------|----------|------------|------|
| Transport list matches release doc | Pass | TR-123456, TR-123457 | Deploy Lead | 2026-06-12 |
| All dependencies in place | Pass | Matrix verified | Deploy Lead | 2026-06-12 |
| Rollback plan documented and tested | Pass | Tested in QA client 300 | QA Lead | 2026-06-12 |
| Environment space and availability | Pass | Basis ticket BASIS-001 | Ops Lead | 2026-06-12 |
| Backup completed before window | Pass | Backup log 2026-06-12 | Ops Lead | 2026-06-12 |

## Procedural readiness
| Item | Status | Evidence | Checked by | Date |
|------|--------|----------|------------|------|
| Maintenance window approved | Pass | CHG-001 | Ops Lead | 2026-06-12 |
| Communication plan executed | Pass | Email 2026-06-11 | Project Lead | 2026-06-12 |
| Support team briefed | Pass | Minutes 2026-06-10 | Support Lead | 2026-06-12 |
| Business owner available | Pass | Email confirmation | Business Owner | 2026-06-12 |

## Monitoring readiness
| Item | Status | Evidence | Checked by | Date |
|------|--------|----------|------------|------|
| Job alerts configured | Pass | Rule 101 | Ops Lead | 2026-06-12 |
| Interface monitoring active | Pass | Dashboard link | Ops Lead | 2026-06-12 |

## Sign-off
- Deployment Lead: [Name], 2026-06-12
- QA Lead: D. Kharlanau, 2026-06-12
- Ops Lead: [Name], 2026-06-12
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Deployment readiness coordinator for an enterprise SAP release.</p>
    <p><strong>Context:</strong> You have a QA sign-off, a release package, a rollback plan, a deployment schedule, and a communication plan. You need to produce a Deployment Readiness Checklist that verifies every prerequisite before the deployment window opens.</p>
    <p><strong>Task:</strong> Check technical, procedural, and monitoring readiness. Verify dependencies, rollback plan, communication, support briefing, and environment status. Produce a checklist with Pass/Fail/Not Applicable status and evidence for every item.</p>
    <p><strong>Output format:</strong> Deployment Readiness Checklist in Markdown, using the compact template with sections for Technical, Procedural, and Monitoring readiness.</p>

    <ul>
      <li><strong>Never approve a deployment if any checklist item is Fail.</strong> Mark the deployment as blocked and document the remediation plan.</li>
      <li><strong>Always verify the rollback plan.</strong> Untested or missing rollback plans are blockers regardless of other readiness.</li>
      <li><strong>Always verify dependencies against a matrix, not by memory.</strong> If a dependency matrix does not exist, create one from the transport list and object list before proceeding.</li>
      <li><strong>Always confirm that monitoring and alerting are active.</strong> Planned monitoring is not enough; it must be configured and tested before the deployment.</li>
      <li><strong>Always confirm that the support team is briefed, not just notified.</strong> The briefing must cover what changed, how to detect failure, and how to work around common issues.</li>
      <li><strong>Do not invent transport numbers, backup logs, or stakeholder confirmations.</strong> Use the evidence provided. If evidence is missing, flag the gap and mark the item as Fail.</li>
      <li><strong>Link to Atlas diagnostics</strong> when deployment changes touch SAP processes. Reference the relevant diagnostic page for monitoring and troubleshooting context.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/testing-quality-delivery/qa-review-sign-off-working-skill/">QA Review and Sign-Off</a> — Provides the QA approval that is a prerequisite for deployment readiness.</li>
      <li><a href="/skill-hub/testing-quality-delivery/release-risk-review-working-skill/">Release Risk Review</a> — Assesses overall risk before the deployment decision.</li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a> — Provides the dependency matrix used in readiness verification.</li>
      <li><a href="/skill-hub/testing-quality-delivery/test-evidence-review-working-skill/">Test Evidence Review</a> — Verifies that test evidence is complete before deployment.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Reference for monitoring and validating scheduled jobs after deployment.</li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — Context for interface monitoring and alerting setup.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of deployment readiness practices. It is not official ITIL, SAP, or DevOps framework documentation. It focuses on enterprise SAP deployments where transports, batch jobs, and interfaces require coordinated readiness checks across functional, technical, and operations teams.</p>
    <p>Known limitations: the skill assumes a deployment window and maintenance schedule exist. It does not cover blue-green deployments, canary releases, or container orchestration rollouts. It assumes manual or semi-automated deployment processes. Organizations with fully automated CI/CD pipelines may need a lighter checklist focused on pipeline gates and automated tests.</p>
  </section>
</article>
