---
layout: default
title: "Incident Triage — Working Skill"
description: "Classify SAP incidents fast, contain business impact, and route to the right owner without wasting time on premature diagnosis."
permalink: /skill-hub/sap-ams/incident-triage-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/sap-ams/">SAP AMS</a></li>
    <li aria-current="page">Incident Triage</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — SAP AMS / Operations</p>
  <h1>Incident Triage</h1>
  <p class="lead">Classify incidents fast, contain business impact, and route to the right owner without wasting time on premature diagnosis.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you decide what an incident is, who should handle it, and what to do in the first 15 minutes. It stops you from debugging a sales order block when the real problem is a failed IDoc that never created the customer. It stops you from assigning a master data issue to the ABAP team when the data steward is the actual owner.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A ticket arrives with a vague subject like "system not working" and no error message.</li>
      <li>Multiple users report the same symptom through different channels (ticket, chat, email).</li>
      <li>An interface failure is blocking downstream processes and business users are escalating.</li>
      <li>A background job failed and you need to decide if this is a one-off or a systemic issue.</li>
      <li>A production change went live and unexpected errors are appearing in multiple areas.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: Sales orders stuck in delivery block</h3>
    <p>A business user reports that 40 sales orders created this morning are blocked for delivery. The first instinct is to check delivery block reasons in VBAK/VBAP. Triage reveals that all 40 orders share the same newly created ship-to party. The ship-to party was replicated from MDG with an incomplete address. The right owner is the BP/MDG data steward, not the SD functional team.</p>

    <h3>Example 2: IDoc status 51 after a weekend transport</h3>
    <p>On Monday morning, 200 IDocs are in status 51 in WE02. The ticket says "interface broken." Triage shows the error segment contains a new mandatory field that was added in Saturday's transport. The segment version changed but the sender system was not updated. The owner is the integration team, and the immediate containment is to roll back the segment change or coordinate a sender update.</p>

    <h3>Example 3: Background job cancellation with no obvious error</h3>
    <p>A periodic billing job cancelled overnight. The ticket says "billing did not run." Triage checks SM37, finds the job log points to a table space issue, and confirms with the Basis team that a database maintenance window ran longer than expected. The owner is Basis, the containment is a job reschedule, and the follow-up is to adjust maintenance windows or job timing.</p>

    <h3>Example 4: Multiple users locked out after password policy change</h3>
    <p>Helpdesk reports 15 users cannot log in. Triage checks SU01 and finds a password policy change was applied to the wrong user group. The owner is security administration, the containment is an emergency policy revert for the affected group, and the correction is a review of policy assignment rules.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The original ticket or alert with timestamp, reporter, and initial description.</li>
      <li>System landscape map or at least a list of systems in the scope (DEV, QAS, PRD, MDG, PI/PO/CPI).</li>
      <li>Interface ownership matrix or a list of known interfaces and their owners.</li>
      <li>Monitoring tool access: SM37, SM58, SMQ1/SMQ2, WE02/WE05, SLG1, ST22, DBACOCKPIT.</li>
      <li>Contact list for functional teams, Basis, security, data stewards, and integration.</li>
      <li>Recent change log: transports, configuration changes, master data loads, password policy updates.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What exactly stopped working, and what was the last successful execution or transaction?</li>
      <li>How many users, records, orders, or IDocs are affected? Is the number growing?</li>
      <li>Did anything change in the system in the last 24–48 hours: transport, config, data load, patch?</li>
      <li>Is this a known error message or a new one? Search the ticket history for the same message.</li>
      <li>Which business process is blocked, and what is the financial or operational cost per hour?</li>
      <li>Does the symptom match a single system, a single interface, or a single data object, or is it scattered?</li>
      <li>Who owns the failing component: functional, Basis, integration, security, or data stewardship?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the ticket once.</strong> Do not start debugging. Extract: reporter, timestamp, system, transaction, error text, number of affected items, business process.</li>
      <li><strong>Classify by business impact.</strong>
        <ul>
          <li>Critical: revenue-impacting process stopped for multiple users.</li>
          <li>High: single user or small group blocked on a time-sensitive process.</li>
          <li>Medium: workaround exists, no immediate business deadline.</li>
          <li>Low: cosmetic, reporting lag, or single non-urgent request.</li>
        </ul>
      </li>
      <li><strong>Classify by technical domain.</strong> Map the symptom to one of: master data, configuration, custom code, integration, infrastructure, security, user error, or unknown.</li>
      <li><strong>Check for recent changes.</strong> Look at transport logs, change documents, transport of copies, and scheduled jobs in the last 48 hours. Correlation is not causation, but it is the fastest filter.</li>
      <li><strong>Contain the impact.</strong>
        <ul>
          <li>If data is being created incorrectly, stop the creation process.</li>
          <li>If an interface is failing, pause or queue the messages.</li>
          <li>If a job is failing, disable the schedule until the cause is known.</li>
          <li>If users are locked out, apply an emergency workaround and document it.</li>
        </ul>
      </li>
      <li><strong>Route to the right owner.</strong> Use the interface ownership matrix and team contact list. Do not assign to "AMS team" as a whole. Assign to a named functional area with a specific question.</li>
      <li><strong>Document the triage decision.</strong> Record classification, containment action, owner assignment, and what you checked. This becomes the input for root cause analysis if needed.</li>
      <li><strong>Set expectations.</strong> Tell the reporter: what you found, what you did, who is working on it, and when they will hear next.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the ticket has no error message and no screenshot, ask for both before assigning to a technical team.</li>
      <li>If the symptom matches a recent transport or config change, assign to the team that performed the change first.</li>
      <li>If multiple users are affected and the symptom is identical, treat as systemic and escalate to the relevant functional lead.</li>
      <li>If the symptom is scattered across modules with no common data object, check infrastructure and integration first.</li>
      <li>If an interface is involved, check the IDoc or message status before checking application logic.</li>
      <li>If a background job failed, check SM37 for the job log and ST22 for dumps before asking the functional team.</li>
      <li>If master data is involved, verify the data object in the source system before assuming SAP is misconfigured.</li>
      <li>If containment requires a system change, get approval from the change manager or document it as an emergency change.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Triage Record</strong> — A short document with classification, impact, containment, owner, and next steps. Use the template below.</li>
      <li><strong>Owner Assignment Note</strong> — Who was assigned and why, with the specific question they need to answer.</li>
      <li><strong>Containment Log</strong> — What was stopped, paused, or worked around, and when it can be reversed.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Incident Triage Record</h3>
    <pre><code>---
artifact: Incident Triage Record
id: TRI-001
date: YYYY-MM-DD
reporter: Name / Team
---

## Symptom
<!-- What was reported. Exact error text if available. -->

## System / Transaction
<!-- Where it happened -->

## Business impact
<!-- Critical / High / Medium / Low. Quantify if possible. -->

## Number affected
<!-- Users, records, orders, IDocs -->

## Recent changes (last 48h)
<!-- Transports, config, data loads, patches -->

## Technical domain
<!-- master data | config | code | integration | infrastructure | security | user error | unknown -->

## Containment action
<!-- What was stopped, paused, or worked around -->

## Owner assigned
<!-- Name and team. Specific question they must answer. -->

## Next update
<!-- When the reporter will hear back -->

## Related tickets
<!-- Links to similar or duplicate tickets -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The triage record names the exact system and transaction where the symptom was observed.</li>
      <li>Business impact is classified and quantified (users affected, orders blocked, cost per hour).</li>
      <li>At least one containment action was taken or a clear reason is given why none was needed.</li>
      <li>The owner assignment includes a named team or person, not a generic queue.</li>
      <li>Recent changes in the last 48 hours were checked and documented.</li>
      <li>The reporter received an update with expected next communication time.</li>
      <li>No premature technical diagnosis was made before classification and containment.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Starting to debug before classifying. <strong>Consequence:</strong> You spend two hours tracing ABAP code when the issue is a missing address in a replicated business partner.</li>
      <li><strong>Mistake:</strong> Assigning to the wrong team because the symptom looks technical. <strong>Consequence:</strong> The ticket bounces between teams for days while the business user escalates.</li>
      <li><strong>Mistake:</strong> Failing to contain impact while investigating. <strong>Consequence:</strong> More incorrect data is created, more IDocs fail, and the cleanup effort multiplies.</li>
      <li><strong>Mistake:</strong> Not documenting the triage decision. <strong>Consequence:</strong> The next shift or the root cause analyst has to start from scratch.</li>
      <li><strong>Mistake:</strong> Treating every incident as unique. <strong>Consequence:</strong> You miss patterns that would reveal a systemic failure and a permanent fix.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Gather context first.</strong> Ask for the ticket text, system, transaction, error message, number of affected items, and timestamp before proposing any diagnosis.</li>
      <li><strong>Separate facts from assumptions.</strong> State clearly what is known from the ticket and what is inferred. Label every inference as an assumption.</li>
      <li><strong>Do not debug prematurely.</strong> The agent's job is classification, containment, and routing — not root cause analysis. If the user asks for a technical fix during triage, redirect to the Root Cause Analysis skill.</li>
      <li><strong>Produce a Triage Record.</strong> Use the template above. Fill every field that has data. Leave unknown fields blank with a note about what is missing.</li>
      <li><strong>Check for patterns.</strong> Before declaring an incident unique, ask whether similar tickets exist in the last 30 days. If yes, flag for Recurring Ticket Pattern Analysis.</li>
      <li><strong>Link to Atlas diagnostics when relevant.</strong> If the symptom involves IDocs, RFCs, background jobs, or master data, reference the relevant Atlas diagnostic page for deeper technical context — but do not perform that diagnosis during triage.</li>
      <li><strong>Avoid generic language.</strong> Do not write "the system is experiencing issues." Write "40 sales orders are blocked for delivery due to incomplete ship-to party address."</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a> — Use after triage when the incident needs permanent resolution.</li>
      <li><a href="/skill-hub/sap-ams/recurring-ticket-pattern-analysis-working-skill/">Recurring Ticket Pattern Analysis</a> — Use when the same symptom appears multiple times.</li>
      <li><a href="/skill-hub/sap-ams/operational-knowledge-capture-working-skill/">Operational Knowledge Capture</a> — Use to record the triage method and outcome for future reuse.</li>
      <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — Use when triage reveals an interface or IDoc failure.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Deep dive on IDoc status codes and failure patterns.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — How to diagnose job failures and cancellations.</li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — Error handling patterns for interfaces.</li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — When BP replication is the suspected cause.</li>
      <li><a href="/atlas/automation/sap-ams-operating-model/">SAP AMS Operating Model</a> — How triage fits into the broader AMS support structure.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of SAP AMS operational practice. It is not official SAP or ITIL documentation. The classification criteria (Critical/High/Medium/Low) should be aligned with your organization's specific SLA definitions. The monitoring transactions listed (SM37, WE02, etc.) are common but may vary by SAP release and landscape. Always validate tool availability and naming conventions against your system.</p>
  </section>
</article>
