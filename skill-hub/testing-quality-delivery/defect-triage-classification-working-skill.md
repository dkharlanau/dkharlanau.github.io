---
layout: default
title: "Defect Triage and Classification Working Skill"
description: "Classify incoming defects by severity, priority, root cause area, and owner so the right team fixes the right defects in the right order."
permalink: /skill-hub/testing-quality-delivery/defect-triage-classification-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">Defect Triage and Classification</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>Defect Triage and Classification Working Skill</h1>
  <p class="lead">Produce a Defect Triage Log that assigns every found defect to a severity, priority, root cause area, and owner so the development team knows what to fix first and the project lead knows what risks remain open.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Defect triage is the QA process of reviewing newly found defects, determining their impact, deciding who should fix them, and setting the order of work. It is distinct from incident triage, which is operational and reactive. Defect triage is part of the testing lifecycle: it happens after a defect is found during test execution, UAT, or regression, and before the fix is assigned to a developer. This skill ensures that defects are not merely logged but are classified with enough structure to support prioritization, trend analysis, and release decisions. The output is a Defect Triage Log that serves as the single source of truth for defect status during the test phase.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Defects are being reported during test execution, UAT, or regression and the team needs to decide which to fix first.</li>
      <li>A daily or weekly triage meeting is scheduled and the QA lead needs a structured log to drive the meeting.</li>
      <li>The project lead needs a summary of open defect risk to decide whether the release can proceed.</li>
      <li>Defects are being misrouted to the wrong team and rework is increasing because fixes are attempted by people without the right expertise.</li>
      <li>Defect trends must be reported to a steering committee or quality gate review.</li>
      <li>An audit requires evidence that defects were classified, tracked, and resolved with appropriate priority.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP pricing defect: severity vs priority confusion</h3>
    <p>A tester reports that a discount condition is not applied correctly in a sales order. The business impact is high for one customer who uses that discount, but the overall process is not blocked because standard orders still calculate correctly. The triage must classify: severity (critical for the affected customer, but the system does not crash), priority (fix before release if the customer is in the go-live scope, otherwise fix in the next wave), root cause area (pricing procedure configuration or condition record data), and owner (functional consultant or master data team). Without triage, the defect is labeled "critical" and all work stops, even though the scope of impact is narrow and the workaround is to use the old condition type temporarily.</p>

    <h3>Integration IDoc failure: routing to the wrong team</h3>
    <p>A tester reports that customer IDocs from the e-commerce platform are failing with status 51. The defect could be caused by: invalid data from the source system, incorrect mapping in the IDoc processing function, missing partner profile configuration, or a custom validation rule that is too strict. The triage must determine which layer is failing before assigning the defect. Without triage, the IDoc is sent to the ABAP developer, who fixes the mapping but misses the real cause: the source system is sending an invalid tax classification. The defect returns in production with different data.</p>

    <h3>Data migration defect: duplicate customer records</h3>
    <p>A tester reports that migrated customer records have duplicates in the target system. The triage must classify: severity (duplicates block invoicing and reporting), priority (must be fixed before go-live), root cause area (migration matching logic, source data quality, or target system deduplication rules), and owner (data migration lead or master data team). Without triage, the duplicates are fixed one by one manually, and the migration job is run again without correcting the root cause, producing more duplicates.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Defect reports from testers, business users, or automated tools, including description, reproduction steps, screenshots, and expected vs actual behavior.</li>
      <li>Requirements and acceptance criteria to determine whether the reported behavior is actually a defect or a misunderstood requirement.</li>
      <li>Test environment details: system, client, transaction, user, and data used when the defect was found.</li>
      <li>Business process map and go-live scope to assess business impact and priority.</li>
      <li>Team roster and ownership matrix showing which team handles which area (functional, technical, data, integration, infrastructure).</li>
      <li>Historical defect data for trend analysis and to identify recurring issues.</li>
      <li>Release schedule and quality gate criteria defining how many defects of each severity can be open at each gate.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the exact symptom, and can it be reproduced consistently?</li>
      <li>Which requirement or acceptance criterion is violated, and is the report actually a defect or a change request?</li>
      <li>How many users, transactions, or records are affected?</li>
      <li>Is there a workaround, and how much effort does it require?</li>
      <li>Which business process is blocked or degraded, and is it in the go-live scope?</li>
      <li>Which system layer is failing: data, configuration, code, interface, or infrastructure?</li>
      <li>Which team has the expertise and access to fix this layer?</li>
      <li>Has this defect or a similar symptom appeared before?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Gather defect reports.</strong> Collect all new defects since the last triage. Verify that each report includes: reporter, date, system, transaction, steps, expected behavior, actual behavior, and evidence (screenshot, log, IDoc number).</li>
      <li><strong>Reproduce the defect.</strong> Before classification, attempt to reproduce the defect in the test environment. If it cannot be reproduced, request more information or close it as "cannot reproduce." Do not classify unreproduced defects.</li>
      <li><strong>Determine if it is a defect or a change request.</strong> Compare the actual behavior to the approved requirement and acceptance criteria. If the behavior matches the requirement but the user wants it changed, convert the item to a change request and route it to the backlog. Do not treat change requests as defects in the triage log.</li>
      <li><strong>Classify severity.</strong> Use a four-level scale: Critical (system crash, data corruption, complete process block), Major (significant functional error with workaround), Minor (cosmetic, spelling, non-standard behavior with no business impact), Trivial (typos, alignment). Record the severity in the log.</li>
      <li><strong>Classify priority.</strong> Use a three-level scale: High (fix before next test cycle or release), Medium (fix before go-live), Low (fix in next release or maintenance window). Priority is driven by business impact, go-live scope, and workaround availability, not by severity alone.</li>
      <li><strong>Identify root cause area.</strong> Classify the defect into one of: data quality, configuration, custom code, standard code, interface, infrastructure, user error, or requirement gap. This classification drives trend analysis and prevents misrouting.</li>
      <li><strong>Assign owner.</strong> Map the root cause area to the team roster. Assign the defect to a named individual or team, not to a generic queue. Include a due date based on priority.</li>
      <li><strong>Record in the Defect Triage Log.</strong> Use the template below. Include defect ID, summary, severity, priority, root cause area, owner, due date, and status.</li>
      <li><strong>Run the triage meeting.</strong> Review the log with the project lead, QA lead, and team leads. Resolve disputes about severity or priority. Escalate disagreements to the steering committee if needed.</li>
      <li><strong>Track to closure.</strong> Update the log daily. Verify that fixes are retested before closure. Do not close defects without retest evidence.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a defect cannot be reproduced, do not classify it. Request more information or close it as "cannot reproduce."</li>
      <li>If a defect is actually a change request, remove it from the triage log and create a backlog item with the original report attached.</li>
      <li>If a defect affects a business process in the go-live scope, priority is at least Medium regardless of severity.</li>
      <li>If a defect has no workaround and blocks testing, priority is High regardless of the number of affected users.</li>
      <li>If a defect is assigned to a team that does not own the root cause area, reassign it immediately. Do not let misrouted defects age.</li>
      <li>If a defect recurs after a fix, escalate severity by one level and require root cause analysis before the next fix attempt.</li>
      <li>If the number of open Critical defects exceeds the quality gate threshold, halt the release until the count is below the threshold.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Defect Triage Log</strong> — Per test cycle or per release. Contains defect ID, summary, severity, priority, root cause area, owner, due date, and status. See template below.</li>
      <li><strong>Triage Meeting Minutes</strong> — Record of decisions made, disputes resolved, and escalations initiated.</li>
      <li><strong>Defect Trend Report</strong> — Count of defects by severity, priority, and root cause area over time, showing whether quality is improving or degrading.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Defect Triage Log (compact)</h3>
    <pre><code>---
artifact: Defect Triage Log
cycle: &lt;Test cycle name&gt;
release: &lt;Release version&gt;
status: open | closed
---

| ID | Summary | Severity | Priority | Root Cause Area | Owner | Due Date | Status |
|----|---------|----------|----------|-----------------|-------|----------|--------|
| DEF-001 | Discount not applied in sales order | Major | High | Configuration | Functional Consultant A | 2026-06-14 | Open |
| DEF-002 | IDoc status 51 on customer create | Critical | High | Interface | Integration Developer B | 2026-06-13 | Open |
| DEF-003 | Duplicate customer after migration | Critical | High | Data Quality | Migration Lead C | 2026-06-14 | Open |
| DEF-004 | Label misspelling on invoice form | Trivial | Low | Custom Code | ABAP Developer D | 2026-06-20 | Open |
| DEF-005 | Report variant missing new filter | Minor | Medium | Custom Code | ABAP Developer D | 2026-06-16 | Open |

## Trend summary
- Critical: 2 open | Major: 1 open | Minor: 1 open | Trivial: 1 open
- Data Quality: 1 | Configuration: 1 | Interface: 1 | Custom Code: 2
- Total open: 5 | Total closed this cycle: 12
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every defect in the log has been reproduced before classification.</li>
      <li>Every defect is classified as either a defect or a change request, with no ambiguity.</li>
      <li>Every defect has a severity, priority, root cause area, and owner.</li>
      <li>Severity and priority are independent: a high-severity defect can be low priority if a workaround exists and it is out of scope.</li>
      <li>Owners are named individuals or teams, not generic queues.</li>
      <li>Due dates are realistic and based on priority and release schedule.</li>
      <li>The trend summary shows counts by severity and root cause area.</li>
      <li>Open Critical defects are below the quality gate threshold.</li>
      <li>All closures are supported by retest evidence.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Treating every reported issue as a defect.</strong> Consequence: the triage log is polluted with change requests and requirements questions, making trend analysis meaningless and diluting developer attention.</li>
      <li><strong>Conflating severity and priority.</strong> Consequence: all defects are labeled critical and the team cannot prioritize. A crash in a report used monthly is not the same priority as a missing discount for the top customer.</li>
      <li><strong>Assigning defects to generic queues.</strong> Consequence: defects sit unassigned, age past the due date, and are discovered late in the release cycle when they are harder to fix.</li>
      <li><strong>Skipping reproduction before classification.</strong> Consequence: defects are classified, assigned, and fixed based on a misunderstanding. The fix does not address the real problem, and the defect returns.</li>
      <li><strong>Closing defects without retest evidence.</strong> Consequence: the defect is assumed fixed but still exists. It is found again in UAT or production, causing rework and trust erosion.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A plain list of defects with no classification: "Bug 1: discount is wrong. Bug 2: IDoc fails. Bug 3: duplicate customer. Bug 4: label typo. All need to be fixed ASAP." No severity levels, no priority, no root cause area, no owner, no due dates, no reproduction status, no trend summary.</p>
    <p><strong>Why it fails:</strong> Developers do not know what to fix first. The project lead cannot assess release risk. The QA team cannot show improvement trends. Defects are fixed in random order, and critical items may be delayed while trivial items are addressed first.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Defect Triage Log
cycle: UAT Wave 2
release: S/4 2026.06
status: open
---

| ID | Summary | Severity | Priority | Root Cause Area | Owner | Due Date | Status |
|----|---------|----------|----------|-----------------|-------|----------|--------|
| DEF-002 | IDoc status 51 on customer create | Critical | High | Interface | Integration Developer B | 2026-06-13 | Open |
| DEF-003 | Duplicate customer after migration | Critical | High | Data Quality | Migration Lead C | 2026-06-14 | Open |
| DEF-001 | Discount not applied in sales order | Major | High | Configuration | Functional Consultant A | 2026-06-14 | Open |
| DEF-005 | Report variant missing new filter | Minor | Medium | Custom Code | ABAP Developer D | 2026-06-16 | Open |
| DEF-004 | Label misspelling on invoice form | Trivial | Low | Custom Code | ABAP Developer D | 2026-06-20 | Open |

## Trend summary
- Critical: 2 open | Major: 1 open | Minor: 1 open | Trivial: 1 open
- Data Quality: 1 | Configuration: 1 | Interface: 1 | Custom Code: 2
- Total open: 5 | Closed this cycle: 12
- Quality gate: max 0 Critical open at go-live. Action: resolve DEF-002 and DEF-003 by 2026-06-14.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> QA defect triage lead for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have defect reports from testers, requirements, and a team roster. You need to produce a Defect Triage Log that classifies each defect so the project can prioritize fixes and assess release risk.</p>
    <p><strong>Task:</strong> Reproduce, classify severity and priority, determine root cause area, assign a named owner, set a due date, and produce a trend summary.</p>
    <p><strong>Output format:</strong> Defect Triage Log in Markdown table format, plus a trend summary section.</p>

    <ul>
      <li><strong>Never classify a defect that has not been reproduced.</strong> Request more information or close it as "cannot reproduce."</li>
      <li><strong>Always separate defects from change requests.</strong> If the behavior matches the approved requirement, convert the item to a change request and remove it from the triage log.</li>
      <li><strong>Always classify severity and priority independently.</strong> Severity is technical impact. Priority is business urgency. Do not default both to the same level.</li>
      <li><strong>Always assign a named owner or team.</strong> Generic queues are not acceptable. If ownership is unclear, produce an ownership matrix before assigning.</li>
      <li><strong>Do not close defects without retest evidence.</strong> A fix is not complete until the original tester or a QA analyst has verified it in the test environment.</li>
      <li><strong>Do not invent defect reports, requirements, or team rosters.</strong> Use the inputs provided. If inputs are missing, flag the gap.</li>
      <li><strong>Link to Atlas diagnostics</strong> when defects touch SAP processes. For example, IDoc failures should reference <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> to help classify root cause area accurately.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/testing-quality-delivery/test-case-design-working-skill/">Test Case Design</a> — Provides the cases that defects are found against.</li>
      <li><a href="/skill-hub/testing-quality-delivery/qa-review-sign-off-working-skill/">QA Review and Sign-Off</a> — Uses the triage log to assess release readiness.</li>
      <li><a href="/skill-hub/testing-quality-delivery/test-evidence-review-working-skill/">Test Evidence Review</a> — Verifies that defects are properly documented with evidence.</li>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage</a> — Distinct operational triage for production incidents, not QA defects.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Reference for classifying interface-related defects and root cause areas.</li>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Context for defects in pricing and credit blocking.</li>
      <li><a href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">SAP Master Data Duplicate Diagnostics</a> — Reference for data quality and migration-related defect classification.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of QA defect triage practices. It is not official ISTQB, ITIL, or SAP documentation. It focuses on structured classification within the testing lifecycle, not on production incident management or DevOps error tracking.</p>
    <p>Known limitations: the skill assumes a defect reporting process exists and that testers can provide reproduction steps. It does not cover automated defect classification using AI or log parsing. It does not address security vulnerability classification (CVSS), which requires specialized scoring. Severity and priority scales are suggestions; organizations with established scales should use their own definitions.</p>
  </section>
</article>
