---
layout: default
title: "Operational Templates — RCA and Procedures"
description: "Reusable protocols for root cause analysis, troubleshooting, integration failures, process deviations, runbooks, change impact, decisions, and cutover control."
permalink: /labs/templates/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags:
  - sap
  - root-cause-analysis
  - troubleshooting
  - procedures
  - operations
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">Operational Templates</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lab 05 / Operational Templates</p>
      <h1>Follow the protocol.<br />Then use judgment.</h1>
      <p>Reusable templates for incidents, root cause analysis, process deviations, integration failures, changes, decisions, cutover, and repeatable operational work.</p>
      <a class="research-canvas__button" href="#template-library">Open the template library <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Protocol model">
      <p>Default reasoning chain</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Impact</strong><small>What is broken?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Evidence</strong><small>What do we know?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Cause</strong><small>What explains it?</small></div>
      <em>A fix is not complete until the result is validated.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Template rules">
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Working rule:</strong> do not jump from symptom to solution. Capture impact, expected behavior, evidence, scope, and recent changes before choosing a fix.</p>
    <p><strong>Closure rule:</strong> separate containment, root cause, corrective action, preventive action, and validation. They are not the same thing.</p>
    <a href="/labs/templates/data/catalog.json">Open machine-readable catalog <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" id="template-library" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Template selector</p>
      <h2>Choose by problem shape.</h2>
      <p>The templates share one reasoning model, but each one asks for different evidence.</p>
    </header>
    <div class="research-route-list">
      <a href="#root-cause-analysis"><span>RCA</span><strong>Root Cause Analysis</strong><small>A recurring or important problem needs a verified causal explanation.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#incident-triage"><span>INC</span><strong>Incident Triage</strong><small>Restore service while keeping enough evidence for later diagnosis.</small><i class="material-symbols-outlined" aria-hidden="true">medical_services</i></a>
      <a href="#integration-failure"><span>INT</span><strong>Integration Failure Analysis</strong><small>A message, API, IDoc, event, file, or middleware flow did not complete correctly.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#process-deviation"><span>PROC</span><strong>Process Deviation Analysis</strong><small>An order, delivery, invoice, purchase order, goods movement, or other process object followed the wrong path.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#runbook"><span>SOP</span><strong>Procedure / Runbook</strong><small>Turn repeated operational work into a controlled procedure.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="#change-impact"><span>CHG</span><strong>Change Impact Review</strong><small>Understand dependencies before changing configuration, code, data, or integration.</small><i class="material-symbols-outlined" aria-hidden="true">device_hub</i></a>
      <a href="#decision-record"><span>ADR</span><strong>Decision Record</strong><small>Keep context, options, trade-offs, and consequences of an important decision.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#cutover-hypercare"><span>CUT</span><strong>Cutover / Hypercare Control</strong><small>Coordinate go-live readiness, execution, monitoring, rollback, and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Common protocol</p><h2>Eight steps before closure.</h2></div>
    <ol>
      <li><span>01</span><strong>Impact</strong><p>State the business effect, affected users or objects, severity, and time window.</p></li>
      <li><span>02</span><strong>Expected</strong><p>Describe what should happen. Use a known-good case when possible.</p></li>
      <li><span>03</span><strong>Evidence</strong><p>Collect document IDs, timestamps, logs, status records, payloads, screenshots, and recent changes.</p></li>
      <li><span>04</span><strong>Scope</strong><p>Find what is affected and what is not. Scope often removes weak hypotheses quickly.</p></li>
      <li><span>05</span><strong>Isolate</strong><p>Test process, master data, configuration, code, integration, authorization, job, and platform layers.</p></li>
      <li><span>06</span><strong>Cause</strong><p>Build a causal chain and verify the root cause against evidence.</p></li>
      <li><span>07</span><strong>Action</strong><p>Separate containment, correction, prevention, owner, risk, and rollback.</p></li>
      <li><span>08</span><strong>Validate</strong><p>Prove the business outcome, record evidence, and define what will show a recurrence.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" id="root-cause-analysis" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / RCA</p><h2>Root Cause Analysis</h2><p>Use when a problem is important, recurring, or not explained by the first fix.</p></header>

### Case
- Case ID / date / owner:
- Business process and system:
- Severity and business impact:
- First observed / last observed:
- Affected users, documents, plants, sales areas, purchasing organizations, interfaces, or jobs:

### Problem statement
- **Observed:** What happened?
- **Expected:** What should have happened?
- **Difference:** What is the smallest clear statement of the gap?
- **Known-good comparison:** Which similar case works correctly?

### Evidence
- Document or message IDs:
- Timestamps and sequence of events:
- Logs / status records / dumps / monitoring results:
- Master data and configuration values relevant to the case:
- Recent transports, deployments, data loads, job changes, or interface changes:
- Reproduction result:

### Scope
- What is affected?
- What is not affected?
- When did the behavior start?
- Is it object-specific, organizational, time-based, user-specific, interface-specific, or system-wide?

### Hypotheses
For every hypothesis record: **reason**, **test**, **evidence**, **result**, **keep/reject**.

### Causal chain
Use 5 Whys only when each answer is supported by evidence. Stop when the cause becomes actionable and explains the observed behavior.

1. Why did the business outcome fail?
2. Why did the process or system behave this way?
3. Why was that condition possible?
4. Which control, design, data rule, configuration, code path, or ownership model allowed it?
5. Why did detection or prevention not catch it earlier?

### Conclusion
- **Root cause:**
- **Contributing factors:**
- **Immediate containment:**
- **Corrective action:**
- **Preventive action:**
- **Owner / due date:**
- **Validation evidence:**
- **Recurrence signal / monitoring:**
- **Lesson worth reusing:**

### Lead checks
- A symptom is not a root cause.
- “User error” is incomplete unless the missing control, design, training, or responsibility is explained.
- A transport or code change that happened at the same time is evidence, not proof.
- The proposed cause must explain both failed and known-good cases.
- Closure needs a business result, not only a green technical status.
  </section>

  <section class="research-canvas__inventory" id="incident-triage" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / Incident</p><h2>Incident Triage</h2><p>Use during an active issue. The goal is safe recovery without destroying diagnostic evidence.</p></header>

### Intake
- Incident ID / owner / start time:
- Business impact and severity:
- Affected process, users, locations, documents, channels, or interfaces:
- Last known good time:
- Recent change before first failure:
- Workaround available? Yes / No

### Fast isolation
Check only what is relevant, but do it in a clear order:
1. Business input and document state.
2. Master data.
3. Configuration and determination logic.
4. Application code / enhancement / extension.
5. Integration and middleware.
6. Background job / queue / scheduler.
7. Authorization and identity.
8. Platform, database, network, or external dependency.

### Record before changing
- Example failing object:
- Example working object:
- Error text / status / log reference:
- Timestamp and user / technical user:
- Relevant payload or field values:
- Current queue / job / interface state:

### Recovery
- Containment or workaround:
- Risk of retry / reprocessing:
- Is the action idempotent?
- Data consistency check after recovery:
- Escalation owner and trigger:
- Exit criteria for incident closure:
- RCA required? Yes / No, and why:
  </section>

  <section class="research-canvas__inventory" id="integration-failure" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / Integration</p><h2>Integration Failure Analysis</h2><p>Use for APIs, IDocs, RFC, events, queues, files, EDI, middleware, or external services.</p></header>

### Flow identity
- Business event / process step:
- Source → middleware → target:
- Interface / API / message type:
- Direction and sync / async mode:
- Message, correlation, IDoc, event, or file ID:
- Trigger and expected completion:

### Layer checks
- **Trigger:** Was the message created when expected?
- **Connectivity:** DNS, endpoint, network, certificate, destination, channel.
- **Authentication:** User, token, certificate, role, expiry.
- **Contract:** Schema, version, mandatory fields, format.
- **Mapping:** Source value → transformation → target value.
- **Business validation:** Did the target reject valid transport for a business reason?
- **Processing:** Queue, retry, ordering, duplicate handling, transaction boundary.
- **Persistence:** Was the object committed or rolled back?
- **Return path:** Was acknowledgement or error returned and handled?
- **Monitoring:** Could support detect and trace the failure end to end?

### Recovery and prevention
- Safe retry point:
- Duplicate / idempotency risk:
- Data correction needed:
- Owner by system boundary:
- Permanent fix:
- Monitoring or alert improvement:
- Test case that proves the fix:
  </section>

  <section class="research-canvas__inventory" id="process-deviation" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / Process</p><h2>Process Deviation Analysis</h2><p>Use when a business document exists, but the process took the wrong route or produced the wrong result.</p></header>

### Process trace
- Process / scenario:
- Business object and document flow:
- Expected step sequence:
- Actual step sequence:
- First point where expected and actual behavior differ:

### Compare the decision inputs
- Organizational data:
- Business partner / customer / supplier data:
- Material / product data:
- Document type / item category / schedule line / movement type or equivalent control fields:
- Dates, quantities, units, statuses, blocks, and partner roles:
- Determination results:
- Pricing / tax / ATP / shipping / sourcing / account assignment inputs when relevant:
- Interface or external decision involved:

### Isolate the layer
- Master data?
- Configuration or determination rule?
- User input?
- Enhancement / extension / custom code?
- Integration payload or timing?
- Background processing?
- Authorization or workflow?

### Closure
- Failed control point:
- Root cause:
- Corrective change:
- Regression scope:
- Business validation case:
- Reusable rule or diagnostic note:
  </section>

  <section class="research-canvas__inventory" id="runbook" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / SOP</p><h2>Procedure / Runbook</h2><p>Use for repeated work where execution quality should not depend on memory.</p></header>

### Definition
- Procedure name / ID / version:
- Purpose and business outcome:
- Trigger / frequency:
- Scope and exclusions:
- Preconditions:
- Required access, tools, transactions, apps, reports, or monitoring:
- Roles: executor / approver / business owner / escalation owner:

### Steps
For each step record:
1. **Action** — what to do.
2. **Input** — what is required.
3. **Expected result** — what success looks like.
4. **Evidence** — what to save.
5. **Decision point** — continue, retry, stop, rollback, or escalate.

### Controls
- Stop conditions:
- Rollback / recovery path:
- Segregation of duties or approval requirement:
- Data or financial risk:
- Escalation path:
- Done criteria:
- Last reviewed / next review:
- Change history:
  </section>

  <section class="research-canvas__inventory" id="change-impact" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / Change</p><h2>Change Impact Review</h2><p>Use before a change moves from “small request” to the traditional enterprise surprise.</p></header>

### Change
- Request / owner / reason:
- Current behavior:
- Target behavior:
- Configuration, code, data, integration, workflow, job, or platform change:

### Impact map
Check dependencies across:
- Business processes and document flow.
- Organizational units and countries.
- Master data and migration rules.
- Determination and configuration logic.
- Enhancements, extensions, APIs, IDocs, events, files, and middleware.
- Authorizations and workflow.
- Forms, output, reporting, analytics, and reconciliation.
- Jobs, queues, monitoring, and support procedures.
- Compliance, audit, tax, finance, or data-retention controls.

### Delivery control
- Assumptions:
- Dependencies:
- Test scope and regression cases:
- Transport / deployment sequence:
- Data conversion or reprocessing:
- Rollback plan:
- Monitoring after release:
- Go / no-go criteria:
- Business owner acceptance:
  </section>

  <section class="research-canvas__inventory" id="decision-record" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / Decision</p><h2>Decision Record</h2><p>Use for architecture and process choices that somebody will question six months later, usually after everyone forgot why they were made.</p></header>

### Decision
- Decision ID / date / owner:
- Context and problem:
- Constraints:
- Decision criteria:
- Options considered:
- Evidence and assumptions:
- Chosen option:
- Why this option:
- Trade-offs accepted:
- Risks and mitigations:
- Consequences / follow-up work:
- Conditions that would make us revisit the decision:
- Review date:
  </section>

  <section class="research-canvas__inventory" id="cutover-hypercare" data-reveal>
    <header><p class="research-canvas__eyebrow">Template / Cutover</p><h2>Cutover / Hypercare Control</h2><p>Use for go-live, migration, major release, or a process activation with many dependencies.</p></header>

### Readiness
- Scope / release / go-live date:
- Business owner / technical lead / cutover lead:
- Open critical defects and accepted risks:
- Data readiness and reconciliation:
- Interface readiness:
- Authorization readiness:
- Jobs and schedules:
- Monitoring and support channels:
- Freeze rules:

### Execution
For every activity record: **sequence, owner, planned time, dependency, evidence, result, rollback point**.

### Go / no-go
- Mandatory checks completed:
- Business smoke test:
- Financial / inventory / order reconciliation where relevant:
- Critical integrations healthy:
- Rollback still possible? Until when?
- Decision owner:

### Hypercare
- KPIs and error signals:
- Daily reconciliation:
- Incident severity rules:
- Known issues and workarounds:
- Business feedback owner:
- Exit criteria from hypercare:
- Handover to steady-state support:
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Lead answer pattern</p><h2>Make the reasoning visible.</h2></div>
    <ol>
      <li><span>01</span><strong>Impact</strong><p>Start with the business problem and scope.</p></li>
      <li><span>02</span><strong>Evidence</strong><p>Show what you would inspect before changing anything.</p></li>
      <li><span>03</span><strong>Isolation</strong><p>Explain how you separate process, data, configuration, code, integration, and platform causes.</p></li>
      <li><span>04</span><strong>Action</strong><p>Separate recovery from permanent correction and prevention.</p></li>
      <li><span>05</span><strong>Validation</strong><p>Close with business proof, monitoring, and ownership.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
