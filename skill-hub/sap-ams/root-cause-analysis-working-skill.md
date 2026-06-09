---
layout: default
title: "Root Cause Analysis — Working Skill"
description: "Separate symptoms from causes, trace defects to their entry point, and produce a correction and prevention plan for SAP incidents."
permalink: /skill-hub/sap-ams/root-cause-analysis-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/sap-ams/">SAP AMS</a></li>
    <li aria-current="page">Root Cause Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — SAP AMS / Operations</p>
  <h1>Root Cause Analysis</h1>
  <p class="lead">Separate symptoms from causes, trace defects to their entry point, and produce a correction and prevention plan.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you find why a defect happened, not just what went wrong. It produces a clear chain from observed symptom to underlying cause to entry point in the lifecycle. The output is a Root Cause Analysis Note that tells a correction team what to fix and a prevention team what to control.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>An incident has been triaged and the same symptom has occurred at least twice.</li>
      <li>A high-impact incident blocked a critical business process for more than four hours.</li>
      <li>A change went live and caused unexpected failures in a different module or system.</li>
      <li>A data quality report shows a spike in defects and the source is unknown.</li>
      <li>A background job or interface has been failing intermittently and the failure pattern is unclear.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: Duplicate customer master records blocking invoicing</h3>
    <p>The symptom is duplicate customers in the system. The immediate cause is a failed merge. The root cause is that the customer creation process allows manual entry in both SAP and a downstream CRM without a uniqueness check against the central MDG system. The entry point is the CRM create API that bypasses MDG validation. The correction is a data merge and deduplication run. The prevention is enforcing MDG as the single point of entry for customer creation.</p>

    <h3>Example 2: Sales order incompletion procedure causing nightly batch failures</h3>
    <p>The symptom is batch job cancellation every night at 02:00. The immediate cause is a missing required field in 3% of orders. The root cause is a recent incompletion procedure change that added a mandatory field for a specific sales document type, but existing open orders were not updated. The entry point is the transport that changed the incompletion procedure without a data migration. The correction is a mass update of the affected field. The prevention is a change process that requires data impact assessment for incompletion procedure changes.</p>

    <h3>Example 3: qRFC queue buildup after a system restart</h3>
    <p>The symptom is SMQ1 showing thousands of queued messages. The immediate cause is a backlog after a system restart. The root cause is that the restart procedure does not include a step to verify RFC destination availability before releasing queues, and one destination was down for maintenance. The entry point is the restart runbook. The correction is manual queue release after destination verification. The prevention is updating the runbook and adding an automated destination health check before queue release.</p>

    <h3>Example 4: Billing documents created with wrong tax code</h3>
    <p>The symptom is incorrect tax codes on invoices. The immediate cause is a condition record with an expired validity period. The root cause is that tax condition records are maintained manually by a regional team with no review process, and the expired record was not flagged. The entry point is the manual maintenance process without validation. The correction is a reversal and re-billing with the correct condition. The prevention is a periodic review report for expiring condition records.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The triage record or incident ticket with full symptom description, timestamps, and affected scope.</li>
      <li>System logs: SM21, SLG1, ST22, SM37, SM58, SMQ1/SMQ2, WE02/WE05.</li>
      <li>Change history: transport logs, change documents (SCU3), configuration changes in the relevant time window.</li>
      <li>Master data samples: affected records with before/after comparison if available.</li>
      <li>Process documentation or runbooks for the affected area.</li>
      <li>Stakeholder access: functional consultant, data steward, Basis, integration team, business user who reported the issue.</li>
      <li>Ticket history for the last 30–90 days to check for recurrence.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What exactly was observed, and what is the earliest point in time this symptom could have started?</li>
      <li>What changed in the system, process, data, or organization just before the first occurrence?</li>
      <li>Where did the defect enter the lifecycle: user entry, interface, batch load, system replication, or configuration change?</li>
      <li>Which validation or control should have caught this, and why did it not?</li>
      <li>Is the defect isolated to a specific data object, user, time window, or document type?</li>
      <li>What business process is affected, and what is the quantified impact (orders blocked, invoices delayed, revenue at risk)?</li>
      <li>Has this exact symptom or a closely related one occurred before? When and how was it resolved?</li>
      <li>Who owns the process or data object where the defect entered, and who owns the process that should prevent it?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Confirm the symptom.</strong> Reproduce or verify the reported defect with your own eyes. Do not rely on second-hand descriptions. Document the exact error text, transaction, and record IDs.</li>
      <li><strong>Define the defect boundary.</strong> Determine: affected system, module, document type, time window, number of records, and whether the defect is ongoing or historical.</li>
      <li><strong>Build a timeline.</strong> List events in chronological order: first failure, last success, any changes, any maintenance windows, any data loads. Use system logs and change documents.</li>
      <li><strong>Identify the immediate cause.</strong> What directly produced the symptom? A missing field? A failed validation? A timeout? A wrong condition record? State it in one sentence.</li>
      <li><strong>Trace to the root cause.</strong> Ask "why" up to five times or until you reach a process, configuration, or governance gap that explains the immediate cause. The root cause is the thing that, if fixed, prevents recurrence.</li>
      <li><strong>Identify the entry point.</strong> Where in the lifecycle did the defect first enter? User entry, interface, batch, replication, manual config, or code change?</li>
      <li><strong>Classify the defect type.</strong> Use one of: data, configuration, custom code, process, integration, infrastructure, user error, or unknown. If unknown, state what is missing to determine it.</li>
      <li><strong>Quantify business impact.</strong> Count affected records, estimate cost, identify downstream processes that are blocked or delayed.</li>
      <li><strong>Design the correction.</strong> How will affected records or systems be fixed? Manual, mass update, reprocessing, reversal, or configuration rollback?</li>
      <li><strong>Design the prevention control.</strong> What validation, workflow, monitoring, or process change will stop this from recurring? The prevention must address the root cause, not the symptom.</li>
      <li><strong>Assign owners and deadlines.</strong> Name a person or team for correction and a person or team for prevention. Set realistic deadlines.</li>
      <li><strong>Document in a Root Cause Analysis Note.</strong> Use the template below or the <a href="/skill-hub/artifact-templates/">Artifact Templates</a> page.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the symptom cannot be reproduced, stop the analysis and gather more data before building theories.</li>
      <li>If the timeline shows a change within 24 hours of first failure, treat the change as the primary suspect until disproven.</li>
      <li>If the defect affects fewer than 10 records and the rule is clear, correct through the governed manual process.</li>
      <li>If the defect affects more than 100 records, prepare a mass correction with validation, approval, and a rollback plan.</li>
      <li>If the root cause is a missing validation, fix the validation before correcting existing records.</li>
      <li>If the root cause is a process gap, produce a process change proposal, not just a one-time fix.</li>
      <li>If the defect has occurred before and was "fixed," the previous fix was not a root cause fix. Escalate to find the deeper cause.</li>
      <li>If the entry point is an interface, check the source system validation before blaming SAP configuration.</li>
      <li>If the root cause is unknown after 4 hours of analysis, document what is known, what was ruled out, and what data is missing.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Root Cause Analysis Note</strong> — The primary artifact. Contains symptom, timeline, root cause, entry point, impact, correction, and prevention. Use the <a href="/skill-hub/artifact-templates/">Artifact Templates</a> page for the full format.</li>
      <li><strong>Remediation Backlog Item</strong> — If correction requires significant work, create a tracked backlog item with scope, method, and validation. See <a href="/skill-hub/artifact-templates/">Artifact Templates</a>.</li>
      <li><strong>Prevention Control Proposal</strong> — A short proposal for the validation, monitoring, or process change that prevents recurrence.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Root Cause Analysis Note (compact)</h3>
    <pre><code>---
artifact: Root Cause Analysis Note
id: RCA-001
date: YYYY-MM-DD
author: Name
status: draft | reviewed | closed
---

## Symptom
<!-- Exact observation. Error text, transaction, record IDs. -->

## Defect classification
<!-- data | config | code | process | integration | infrastructure | user error | unknown -->

## Affected scope
<!-- Systems, records, users, business areas, time period -->

## Timeline
<!-- Chronological list of events: last success, first failure, changes, maintenance -->

## Immediate cause
<!-- What directly produced the symptom -->

## Root cause
<!-- The underlying reason. Ask "why" until you reach a process or governance gap. -->

## Entry point
<!-- Where the defect entered the lifecycle -->

## Business impact
<!-- Quantified: orders blocked, invoices delayed, revenue at risk, hours lost -->

## Correction approach
<!-- Manual, mass update, reprocessing, reversal, rollback -->

## Prevention control
<!-- What stops recurrence: validation, workflow, monitoring, process change -->

## Correction owner
<!-- Who fixes the affected records -->

## Prevention owner
<!-- Who implements the control -->

## Deadlines
<!-- Correction by: YYYY-MM-DD. Prevention by: YYYY-MM-DD. -->

## Verification
<!-- How we confirm the fix and the control work -->

## Related incidents
<!-- Ticket numbers, IDocs, change requests, previous RCAs -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The symptom is described with exact error text, transaction code, and at least one example record ID.</li>
      <li>A timeline exists with at least three data points: last known success, first failure, and any relevant change or event.</li>
      <li>The root cause is distinct from the symptom and the immediate cause.</li>
      <li>The entry point is identified: where the defect first entered the lifecycle.</li>
      <li>Business impact is quantified or at least estimated with a clear method.</li>
      <li>The correction approach addresses affected records or systems, not just the root cause.</li>
      <li>The prevention control addresses the root cause, not the symptom.</li>
      <li>Both correction and prevention have named owners and deadlines.</li>
      <li>Ticket history for the last 30 days was checked for recurrence.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Treating the symptom as the root cause. <strong>Consequence:</strong> You correct the blocked orders but the missing validation that allowed bad data remains, so the defect recurs.</li>
      <li><strong>Mistake:</strong> Stopping at the immediate cause. <strong>Consequence:</strong> You fix the failed IDoc but the sender system keeps sending invalid data because the root cause is an upstream schema mismatch.</li>
      <li><strong>Mistake:</strong> Not checking for recurrence. <strong>Consequence:</strong> You treat a systemic issue as a one-off and miss the opportunity to justify a permanent fix.</li>
      <li><strong>Mistake:</strong> Proposing prevention that is too expensive or complex to implement. <strong>Consequence:</strong> The prevention is never approved, and the defect recurs because no simpler control was proposed.</li>
      <li><strong>Mistake:</strong> Failing to name owners and deadlines. <strong>Consequence:</strong> The RCA sits in a document repository and nothing changes.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Never accept the user's first description as the root cause.</strong> Ask "why" repeatedly until a process, configuration, or governance gap is identified.</li>
      <li><strong>Build a timeline before proposing theories.</strong> Use timestamps from logs, change documents, and tickets. Do not guess at chronology.</li>
      <li><strong>Separate three layers:</strong> symptom (what was seen), immediate cause (what directly failed), and root cause (why the failure was possible). Label each layer explicitly.</li>
      <li><strong>Check for recurrence.</strong> Ask the user for ticket history or similar incidents in the last 30–90 days. If recurrence exists, flag it and reference the Recurring Ticket Pattern Analysis skill.</li>
      <li><strong>Quantify impact.</strong> Ask for numbers: records affected, orders blocked, hours lost, revenue at risk. If numbers are unavailable, state the estimation method.</li>
      <li><strong>Produce a Root Cause Analysis Note.</strong> Use the template above. Fill every field. If data is missing, state what is missing and who can provide it.</li>
      <li><strong>Link to Atlas diagnostics for technical depth.</strong> If the root cause involves IDocs, RFCs, background jobs, or master data, reference the relevant Atlas page for detailed technical steps — but do not replace the RCA with a technical procedure.</li>
      <li><strong>Avoid generic prevention.</strong> "Better training" is not a prevention control. "Mandatory field validation in MDG workflow step 3" is.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage</a> — Use before RCA to classify and contain the incident.</li>
      <li><a href="/skill-hub/sap-ams/recurring-ticket-pattern-analysis-working-skill/">Recurring Ticket Pattern Analysis</a> — Use when the same symptom appears multiple times.</li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a> — Use when the root cause traces back to a recent change.</li>
      <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> — Use when the defect is a data quality failure.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Technical depth on IDoc failures.</li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC/tRFC Diagnostics</a> — Queue and RFC failure patterns.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Job failure analysis.</li>
      <li><a href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">SAP Master Data Duplicate Diagnostics</a> — When duplicates are the symptom.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — When missing fields cause blocks.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of root cause analysis practice. It is not official SAP, ITIL, or Six Sigma documentation. The "5 Whys" method is a simplification; complex failures may require fault tree analysis or Ishikawa diagrams. The skill focuses on operational incidents rather than strategic or organizational failures. Some root causes may require access to proprietary system logs or vendor documentation that is not available in all landscapes.</p>
  </section>
</article>
