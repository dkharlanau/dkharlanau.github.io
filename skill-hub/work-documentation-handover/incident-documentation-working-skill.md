---
layout: default
title: "Incident Documentation Working Skill"
description: "Write an incident record that captures symptom, diagnosis, resolution, and prevention so the next incident is handled faster and patterns are visible."
permalink: /skill-hub/work-documentation-handover/incident-documentation-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Incident Documentation</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Incident Documentation Working Skill</h1>
  <p class="lead">Write an incident record that captures symptom, diagnosis, resolution, and prevention so the next incident is handled faster and patterns are visible.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Incidents are expensive, but undocumented incidents are more expensive because every recurrence becomes a new investigation. This skill produces an Incident Record: a structured document that captures what happened, how it was detected, what was tried, what worked, and what must change to prevent recurrence. The output is designed to be read by the next on-call engineer, the incident review team, and pattern analysis tools. It is different from incident-triage, which classifies and routes incidents, and from root-cause-analysis, which finds deep causes. This skill documents the incident after it is resolved so the knowledge survives and patterns become visible.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>An incident has been resolved and the team needs to capture the resolution for future reference.</li>
      <li>An incident review or post-mortem meeting is scheduled and the team needs a structured record to discuss.</li>
      <li>A recurring incident pattern is suspected and the team needs documented evidence to compare symptoms and resolutions.</li>
      <li>A new team member needs to understand how previous incidents were handled without asking the original responder.</li>
      <li>An AI agent is analyzing incident history to suggest preventive measures or automate detection.</li>
      <li>A customer or audit requires evidence of incident handling and resolution.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP IDoc failure: documenting a recurring mapping error</h3>
    <p>A sales order IDoc fails with status 51 in WE02 due to a missing delivery block mapping in SAP PI. The responder fixes the mapping, reprocesses the IDoc, and closes the ticket. Two weeks later, the same IDoc type fails again with the same error. The responder is on vacation. The new responder spends two hours re-investigating because the original ticket only says "mapping fixed, IDoc reprocessed." An Incident Record would have captured: the symptom (status 51, error text "delivery block not found"), the diagnosis (PI mapping missing field for delivery block for new plant 1002), the resolution (update mapping, add plant 1002 to condition table, reprocess IDoc), and the prevention (review PI mapping for all new plants before go-live). Without this record, the organization pays for the same investigation twice.</p>

    <h3>Background job failure: documenting a timeout pattern</h3>
    <p>A monthly customer reconciliation job ZCUST_REP fails with a timeout after running for two hours. The basis team increases the job runtime limit and restarts the job. The job completes. The ticket is closed with "runtime limit increased." Three months later, the job fails again. The new basis team member increases the limit again, but the job still fails because the underlying cause is a missing database index on the customer table. An Incident Record would have captured: the symptom (timeout after 2 hours), the diagnosis (runtime limit too low, but also query execution plan shows full table scan), the resolution (increase runtime limit temporarily and create index on KNA1), and the prevention (add index creation to change request for next release). Without the record, the temporary fix becomes the permanent fix and performance degrades.</p>

    <h3>BP replication failure: documenting a complex multi-system incident</h3>
    <p>A business partner created in SAP MDG fails to replicate to S/4HANA, blocking a critical sales order. The incident involves MDG, S/4, and a middleware queue. The responder clears the queue, re-triggers the replication, and the BP appears. The ticket is closed. The next week, the same failure occurs. An Incident Record would have captured: the symptom (BP missing in S/4, order blocked), the systems involved (MDG, S/4, SAP PI), the diagnosis (queue worker stuck due to RFC destination timeout), the resolution (restart queue worker, clear SM58, re-trigger replication), and the prevention (add queue depth alert, increase RFC connection pool). Without this record, the incident becomes a chronic mystery.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Incident ticket or alert showing the initial symptom, timestamp, and affected system.</li>
      <li>Responder notes showing what was checked, what was tried, and what the results were.</li>
      <li>System logs, error messages, screenshots, or trace files from the incident period.</li>
      <li>Root cause analysis findings if a separate RCA was performed.</li>
      <li>Change records or deployment history showing what changed before the incident.</li>
      <li>Communication records: emails, chat threads, or bridge call notes showing stakeholder involvement.</li>
      <li>Resolution confirmation: evidence that the issue is resolved and the system is stable.</li>
      <li>Prevention plan: what will be changed to reduce recurrence likelihood or impact.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What was the symptom? What did the user or system report, and when?</li>
      <li>What systems, transactions, and programs were involved?</li>
      <li>What was the business impact? How many users, orders, or processes were affected?</li>
      <li>What was the sequence of events? What happened first, second, third?</li>
      <li>What was tried that did not work? Failed attempts are as valuable as successful ones.</li>
      <li>What was the actual resolution? What specific action fixed the issue?</li>
      <li>What was the root cause? If unknown, say so. Do not guess.</li>
      <li>What could have detected this earlier? What monitoring or alert is missing?</li>
      <li>What must change to prevent recurrence? If nothing can be done, say so.</li>
      <li>Who was involved, and what did each person do?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Gather the inputs.</strong> Collect the ticket, responder notes, logs, screenshots, and communication records. If the responder did not take notes, interview them immediately while memory is fresh.</li>
      <li><strong>Write the timeline.</strong> Create a chronological sequence of events: detection, initial response, diagnosis, attempts, resolution, and confirmation. Include timestamps. Distinguish what was known at each point from what was discovered later.</li>
      <li><strong>Describe the symptom.</strong> State what the user or system reported. Include error messages, status codes, transaction IDs, and affected objects. Be specific enough that the next responder can search for the same symptom.</li>
      <li><strong>Describe the diagnosis.</strong> Explain what was checked, what was found, and what the conclusion was. Include the tools and transactions used: SM58, SM50, WE02, ST22, etc. If the diagnosis was uncertain, state the uncertainty.</li>
      <li><strong>Record failed attempts.</strong> Document what was tried and why it did not work. This prevents future responders from repeating the same failed attempts.</li>
      <li><strong>State the resolution.</strong> Describe the exact action that resolved the issue. Include transaction codes, program names, parameter changes, and restart steps. If the resolution was temporary, state that.</li>
      <li><strong>State the root cause if known.</strong> If a separate root cause analysis was performed, summarize it. If the root cause is unknown, state "Root cause unknown" and describe the leading hypothesis.</li>
      <li><strong>Propose prevention.</strong> List what will be changed to reduce recurrence or detect it earlier: monitoring, process change, configuration change, training, or documentation. If no prevention is feasible, say so.</li>
      <li><strong>Write the Incident Record.</strong> Use the template below. Keep it concise but complete. One to two pages is the target.</li>
      <li><strong>Review and publish.</strong> Validate the record with the responder and the incident review team. Store it in the incident knowledge base with searchable tags.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the root cause is unknown, do not invent one. State "Unknown" and describe the leading hypothesis.</li>
      <li>If the resolution was temporary, label it as a workaround, not a fix. Document the permanent fix separately.</li>
      <li>If the incident involved a third party, document the third-party response and any handoffs. Do not hide vendor involvement.</li>
      <li>If the incident was caused by a recent change, document the change ID and the rollback option if applicable.</li>
      <li>If the prevention plan requires a change request, document the change request ID and the expected completion date.</li>
      <li>If the incident is part of a pattern, link to previous incident records and update the pattern analysis.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Incident Record</strong> — Structured document capturing symptom, timeline, diagnosis, resolution, root cause, and prevention. See template below.</li>
      <li><strong>Timeline Diagram</strong> — Optional visual timeline showing events, decisions, and handoffs during the incident.</li>
      <li><strong>Prevention Plan</strong> — List of actions to reduce recurrence, with owners and deadlines.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Incident Record (compact)</h3>
    <pre><code>---
artifact: Incident Record
id: INC-&lt;system&gt;-&lt;date&gt;-&lt;number&gt;
incident_type: &lt;Type: system, data, integration, user error&gt;
severity: &lt;P1 / P2 / P3 / P4&gt;
affected_system: &lt;System name and component&gt;
detection_time: YYYY-MM-DD HH:MM
resolution_time: YYYY-MM-DD HH:MM
mttr: &lt;Minutes or hours&gt
doc_author: &lt;Name&gt
doc_reviewer: &lt;Name&gt
doc_status: draft | reviewed | closed
---

## Symptom
- What was observed: &lt;Error message, status, behavior&gt;
- Who reported it: &lt;User, system, monitor&gt;
- Business impact: &lt;What was affected and how&gt;

## Timeline
| Time | Event | What was known | Action taken |
|------|-------|----------------|--------------|
| HH:MM | &lt;Detection&gt; | &lt;What was known&gt; | &lt;What was done&gt; |
| HH:MM | &lt;Diagnosis&gt; | &lt;What was discovered&gt; | &lt;What was done&gt; |
| HH:MM | &lt;Resolution&gt; | &lt;What was fixed&gt; | &lt;What was done&gt; |

## Diagnosis
- Systems checked: &lt;Transactions, tools, logs used&gt;
- Findings: &lt;What was found&gt;
- Leading hypothesis: &lt;Most likely cause&gt;

## Failed Attempts
| Attempt | Reason it was tried | Result |
|---------|---------------------|--------|
| &lt;Action&gt; | &lt;Why&gt; | &lt;Outcome&gt; |

## Resolution
- Action taken: &lt;Exact fix&gt;
- Verification: &lt;How we confirmed it worked&gt;
- Temporary or permanent: &lt;Workaround or fix&gt;

## Root Cause (if known)
- Cause: &lt;What fundamentally went wrong&gt;
- Evidence: &lt;Log, trace, or data that confirms it&gt;
- If unknown: &lt;State unknown and leading hypothesis&gt;

## Prevention Plan
| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| &lt;Prevention action&gt; | &lt;Name&gt; | YYYY-MM-DD | &lt;open | done&gt; |

## Related Incidents
- &lt;Link to previous incident records with similar symptoms&gt;
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The symptom is specific enough that the next responder can search for it in the knowledge base.</li>
      <li>The timeline includes timestamps and distinguishes known facts from later discoveries.</li>
      <li>Failed attempts are documented to prevent repeated dead ends.</li>
      <li>The resolution describes the exact action, not a generic summary.</li>
      <li>The root cause is stated or explicitly marked as unknown.</li>
      <li>The prevention plan has an owner, a deadline, and a verifiable action.</li>
      <li>The record is reviewed by the responder and the incident review team.</li>
      <li>The record is stored in a searchable location with tags for system, symptom, and component.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing a ticket closure summary instead of an incident record.</strong> Consequence: the record says "fixed, closed" with no detail. The next responder has no starting point.</li>
      <li><strong>Guessing the root cause when it is unknown.</strong> Consequence: the organization invests in fixing the wrong problem. The real root cause continues to cause incidents.</li>
      <li><strong>Omitting failed attempts.</strong> Consequence: future responders waste time trying the same unsuccessful actions. The incident record is incomplete.</li>
      <li><strong>Writing the record days or weeks after the incident.</strong> Consequence: memory fades, details are lost, and the timeline becomes inaccurate.</li>
      <li><strong>Skipping the prevention plan.</strong> Consequence: the incident recurs because nothing was changed. The organization pays for the same failure repeatedly.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A ticket closure note: "IDoc failed with status 51. Checked mapping and found missing field. Updated mapping in PI. Reprocessed IDoc. Issue resolved. Ticket closed." No timeline, no error text, no system details, no failed attempts, no root cause, no prevention plan. When the same IDoc fails two weeks later, the new responder starts from zero.</p>
    <p><strong>Why it fails:</strong> The record is too thin to be useful for pattern analysis or future response. It does not help the next responder, it does not reveal recurrence patterns, and it provides no evidence for improvement.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Incident Record
id: INC-PI-2026-06-10-001
incident_type: integration
severity: P2
affected_system: SAP PI / S/4HANA Sales Order Processing
detection_time: 2026-06-10 08:15
resolution_time: 2026-06-10 10:45
mttr: 2h 30m
doc_author: M. Chen
doc_reviewer: T. Nguyen
doc_status: closed
---

## Symptom
- What was observed: Sales order IDoc type ORDERS05 failed in WE02 with status 51. Error text: "Delivery block for plant 1002 not found in mapping table."
- Who reported it: EDI monitoring alert at 08:15, followed by customer service escalation at 08:30.
- Business impact: 12 sales orders blocked for plant 1002. Customer service manually creating orders in VA01 as workaround.

## Timeline
| Time | Event | What was known | Action taken |
|------|-------|----------------|--------------|
| 08:15 | Monitoring alert fires | Status 51 on ORDERS05 for plant 1002 | Checked WE02 for error details |
| 08:25 | Error text confirmed | "Delivery block not found in mapping table" | Checked SAP PI mapping for plant 1002 |
| 08:40 | Mapping gap identified | Plant 1002 added last week; mapping not updated | Attempted to add plant 1002 to mapping table (failed — table locked) |
| 09:00 | Basis team engaged | Table locked by background job | Basis team terminated background job, released table lock |
| 09:30 | Mapping updated | Plant 1002 delivery block added to mapping | Tested with one IDoc — processed successfully |
| 10:00 | Batch reprocessing | 12 affected IDocs identified | Reprocessed all 12 IDocs via WE19 |
| 10:45 | Verification complete | All orders created in S/4, no errors | Confirmed with customer service that manual entry can stop |

## Failed Attempts
| Attempt | Reason it was tried | Result |
|---------|---------------------|--------|
| Add plant 1002 to mapping table immediately | Direct fix seemed possible | Failed because table was locked by background job |
| Reprocess IDoc without fixing mapping | Thought error was transient | Failed with same status 51, error text unchanged |

## Resolution
- Action taken: Updated SAP PI mapping table ZDLV_BLOCK_MAP to include delivery block "01" for plant 1002. Reprocessed 12 failed IDocs via WE19.
- Verification: All 12 IDocs processed with status 53. Sales orders created in VA01. Customer service confirmed.
- Temporary or permanent: Permanent fix. Table lock issue was one-time background job conflict.

## Root Cause
- Cause: Plant 1002 was added to the organizational model on 2026-06-05 but the PI mapping table was not updated. The change process for new plants does not include a PI mapping checklist.
- Evidence: Change record CHG-2026-045 (plant 1002 creation) with no PI mapping task. Mapping table ZDLV_BLOCK_MAP last updated 2026-05-01.

## Prevention Plan
| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Add PI mapping checklist to plant creation change request | S. Mueller | 2026-06-20 | open |
| Create alert for IDoc status 51 with "delivery block not found" error | T. Nguyen | 2026-06-25 | open |
| Review all plants added since 2026-01-01 for PI mapping completeness | M. Chen | 2026-06-18 | open |

## Related Incidents
- INC-PI-2026-05-15-003: Similar mapping missing for plant 1001 (different field, same root cause).
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Incident documentation writer for SAP operational support.</p>
    <p><strong>Context:</strong> You have a resolved incident ticket, responder notes, and system logs. You need to produce an Incident Record that captures the full response narrative for future responders and pattern analysis.</p>
    <p><strong>Task:</strong> Create a structured Incident Record using the template below. Include a timeline, specific symptoms, failed attempts, exact resolution, root cause, and prevention plan.</p>
    <p><strong>Output format:</strong> Structured Incident Record in Markdown with tables for timeline, failed attempts, and prevention plan.</p>

    <ul>
      <li><strong>Never guess the root cause.</strong> If the root cause is unknown, state "Unknown" and describe the leading hypothesis. Do not invent certainty.</li>
      <li><strong>Always document failed attempts.</strong> Future responders must know what was already tried and why it did not work.</li>
      <li><strong>Always describe the exact resolution.</strong> Include transaction codes, program names, parameter values, and verification steps. "Fixed mapping" is not enough.</li>
      <li><strong>Always include a prevention plan with an owner and a deadline.</strong> If no prevention is possible, state why.</li>
      <li><strong>Write the timeline with timestamps.</strong> Distinguish what was known at each point from what was discovered later.</li>
      <li><strong>Link to related incidents.</strong> If the same symptom or root cause has appeared before, reference the previous record. This makes patterns visible.</li>
      <li><strong>Do not include sensitive data.</strong> Use anonymized IDs, not real customer names, account numbers, or personal data.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the incident touches documented SAP failure modes. For example, IDoc incidents should reference <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage Working Skill</a> — Use to classify and route incidents before they are documented.</li>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis Working Skill</a> — Use to perform deep cause analysis before writing the root cause section of the incident record.</li>
      <li><a href="/skill-hub/work-documentation-handover/runbook-writing-working-skill/">Runbook Writing Working Skill</a> — Use to document the resolution steps as a reusable operational procedure.</li>
      <li><a href="/skill-hub/work-documentation-handover/knowledge-article-writing-working-skill/">Knowledge Article Writing Working Skill</a> — Use to convert incident records into self-service knowledge articles for common issues.</li>
      <li><a href="/skill-hub/sap-ams/recurring-ticket-pattern-analysis-working-skill/">Recurring Ticket Pattern Analysis Working Skill</a> — Use to analyze incident records for patterns and systemic issues.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Diagnostic context for IDoc-related incidents.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Diagnostic context for background job incidents.</li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — Monitoring context for integration incidents.</li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — Error handling context for multi-system incidents.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of incident documentation practices. It is not official ITIL, SAP, or ISO documentation. It focuses on operational incident records in enterprise and SAP environments where incidents are frequent, responders rotate, and pattern visibility is essential for improvement.</p>
    <p>Known limitations: the skill does not cover incident response procedures, escalation protocols, or communication management during an incident. It assumes the incident is resolved and the task is to document it. It does not replace formal post-mortem facilitation or blameless post-mortem culture frameworks. It does not cover security incident documentation, which may have classification and handling requirements beyond this template.</p>
  </section>
</article>
