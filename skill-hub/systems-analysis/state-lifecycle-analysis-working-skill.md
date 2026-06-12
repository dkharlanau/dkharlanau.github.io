---
layout: default
title: "State and Lifecycle Analysis Working Skill"
description: "Map the states an entity passes through, the events that trigger transitions, and the conditions that must hold at each stage so that no invalid state reaches production."
permalink: /skill-hub/systems-analysis/state-lifecycle-analysis-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/systems-analysis/">Systems Analysis</a></li>
    <li aria-current="page">State and Lifecycle Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Systems Analysis</p>
  <h1>State and Lifecycle Analysis</h1>
  <p class="lead">Map the states an entity passes through, the events that trigger transitions, and the conditions that must hold at each stage so that no invalid state reaches production.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill produces a precise, verifiable map of an entity's lifecycle: the states it can occupy, the events that move it between states, the guard conditions that must be satisfied, and the error or recovery paths when something goes wrong. The output is used to find missing validation, undocumented transitions, race conditions between parallel workflows, and states that should not exist in production.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A sales order is blocked in an unexpected status and no one can explain how it got there.</li>
      <li>A business partner record shows as active in SAP S/4HANA but is still incomplete in the CRM system.</li>
      <li>An IDoc reaches status 53 (success) in WE02 but the downstream document was never created because a parallel workflow failed.</li>
      <li>A material master bypasses the quality approval stage and appears as released in the procurement system.</li>
      <li>You are designing a new document type or workflow and need to define valid states and transitions before configuration begins.</li>
      <li>A recurring incident involves records stuck in a terminal state with no defined correction path.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: Sales order credit block after delivery creation</h3>
    <p>An SAP S/4HANA sales order (type OR) is created and passes credit check. The delivery is created immediately by a background job. A later credit re-check fails and the order is blocked. The delivery already exists and the goods issue is pending. The lifecycle map reveals that the credit re-check event does not guard against the existence of an open delivery, and there is no defined transition from "blocked with delivery" back to a clean state.</p>

    <h3>Example 2: Business partner vendor role missing after CVI replication</h3>
    <p>A business partner is created in SAP S/4HANA with customer and vendor roles. The customer role replicates to Salesforce via CVI, but the vendor role does not. The business partner lifecycle map shows two parallel sub-lifecycles (customer, vendor) triggered by the same creation event, but only the customer sub-lifecycle has a defined outbound event. The vendor role remains invisible to downstream procurement processes.</p>

    <h3>Example 3: Material master status bypasses quality gate</h3>
    <p>A material master in SAP S/4HANA changes from status "In Design" (01) to "Released" (51) without the quality management approval that the procedure requires. The lifecycle map reveals that the release event can be triggered by a mass update program that does not enforce the incompletion procedure guard condition. The map also shows that no invalid-state detection exists to catch the bypass.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Entity type and document type (e.g., sales order type OR, business partner grouping, material type).</li>
      <li>Status schema from SAP configuration: status profile, user status, system status, or workflow status values.</li>
      <li>Event sources: transactions, background jobs, workflow events, IDoc triggers, API calls, batch programs.</li>
      <li>Business rules that govern transitions: release strategy, incompletion procedure, credit check, availability check.</li>
      <li>Data sample from production showing actual status distributions and stuck records.</li>
      <li>Stakeholder: process owner, configuration owner, AMS support lead, workflow administrator.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the complete, ordered set of states this entity can occupy, and which are terminal?</li>
      <li>Which event triggers each transition, and which system or user role generates that event?</li>
      <li>What condition must be true before a transition is allowed? Where is that condition enforced?</li>
      <li>What happens if the same event occurs twice in succession? Is the transition idempotent?</li>
      <li>Which states can the entity be rolled back to, and which transitions are irreversible?</li>
      <li>Are there parallel lifecycles for the same entity (e.g., document status, workflow status, IDoc status)? How are they synchronized?</li>
      <li>What is the business impact if an entity remains in an intermediate state for more than 24 hours?</li>
      <li>Which program or transaction can move an entity to a state that bypasses the normal sequence?</li>
      <li>What happens when a downstream system rejects a state that SAP considers valid?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Name the entity and its scope.</strong> Define the document type, material type, or business partner grouping. One sentence. If you cannot define the entity precisely, the lifecycle scope is undefined.</li>
      <li><strong>Collect all possible states.</strong> From configuration (status profile, workflow template, incompletion procedure) and from production data. Compare: if a state exists in data but not in configuration, it is a legacy or error state.</li>
      <li><strong>Map the happy-path transitions.</strong> For each state, identify the event that moves the entity to the next state. Name the transaction, program, or API endpoint.</li>
      <li><strong>Map error and recovery paths.</strong> Identify rejection states, block statuses, rollback transactions, and correction programs. Include who is authorized to trigger recovery.</li>
      <li><strong>Define guard conditions for each transition.</strong> For each arrow between states, list the business rule, configuration check, or validation that must pass. Note where the guard is enforced (standard, enhancement, custom code).</li>
      <li><strong>Identify parallel lifecycles.</strong> Check if the same entity has independent status tracks (e.g., sales order header status, delivery status, billing status, workflow status). Map synchronization points and race conditions.</li>
      <li><strong>Find invalid states and gaps.</strong> List states that should not exist in production, transitions that have no guard, and events that can bypass the intended sequence. Quantify the business impact.</li>
      <li><strong>Validate with stakeholders.</strong> Review the map with the process owner, configuration owner, and an AMS support analyst who has seen real incidents. Correct misattributions.</li>
      <li><strong>Publish and maintain.</strong> Store the lifecycle map where support, testing, and project teams can find it. Update when the status profile, workflow, or release strategy changes.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a state has no exit event and is not marked as terminal, flag it as a potential deadlock.</li>
      <li>If two states can be reached from the same event without mutual exclusion, flag a race condition.</li>
      <li>If a transition has no guard condition, document it as high-risk and require a business justification.</li>
      <li>If a state exists in production data but not in configuration, treat it as an invalid state requiring correction.</li>
      <li>If parallel lifecycles for the same entity are not synchronized, treat it as an integration gap, not a business process gap.</li>
      <li>If a background job can trigger a transition that bypasses a user approval step, flag it as a governance risk.</li>
      <li>If an error state has no defined recovery path, require one before the lifecycle is approved for production.</li>
      <li>If a downstream system rejects a state that the source considers valid, define an escalation state and a retry policy.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>State Transition Diagram or Table</strong> — All states, transitions, events, and guards for the entity.</li>
      <li><strong>Event-Trigger Matrix</strong> — Table mapping each event to its source (transaction, program, API, workflow step) and the states it can move the entity from and to.</li>
      <li><strong>Guard Condition Specification</strong> — For each transition, the rule, configuration object, or custom code that enforces it.</li>
      <li><strong>Invalid State Analysis</strong> — List of states that should not exist, how they occur, their business impact, and the correction method.</li>
      <li><strong>Parallel Lifecycle Map</strong> — Synchronization points between independent status tracks for the same entity.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>State Lifecycle Analysis (Markdown table format)</h3>
    <pre><code>## Entity: &lt;Document type / Material type / BP grouping&gt;

### Scope
<!-- One sentence. Example: SAP S/4HANA sales order type OR, standard order. -->

### States

| State ID | State Name | Source | Terminal | Notes |
|----------|------------|--------|----------|-------|
| 10 | Created | VBSTAT / VBAK | No | Initial status after VA01 |
| 20 | Credit check ok | VBSTAT / VBAK | No | After VKM1/VKM3 approval |
| 30 | Delivery created | VBSTAT / LIKP | No | After VL01N / background job |
| 40 | Invoiced | VBSTAT / VBRK | No | After VF01 |
| 50 | Complete | VBSTAT / VBAK | Yes | No further processing |
| 90 | Blocked | VBSTAT / VBAK | No | Credit, delivery, or billing block |

### Transitions

| From State | To State | Event | Source System / User | Guard Condition | Guard Location |
|------------|----------|-------|----------------------|-----------------|----------------|
| Created | Credit check ok | Credit check passed | VKM3 / Credit team | Credit limit >= order value | SAP standard + custom enhancement ZSD_CREDIT_001 |
| Credit check ok | Delivery created | Delivery generated | VL01N / Background job | Availability check passed | SAP ATP check |
| Delivery created | Invoiced | Billing generated | VF01 / Batch job | PGI completed | Delivery status check |
| Invoiced | Complete | Posting complete | System | Accounting document created | VBRK billing status |
| Created | Blocked | Credit check failed | VKM1 / Credit team | Credit limit < order value | SAP standard credit check |
| Blocked | Created | Block released | VKM3 / Authorized user | Manual approval + reason code | Custom workflow WS12345678 |

### Error and recovery paths

| Error State | How It Occurs | Recovery Transaction | Authorized Role | Business Impact |
|-------------|---------------|----------------------|-----------------|-----------------|
| Stuck in Created | Incompletion procedure incomplete | VA02 / V.25 mass update | Sales admin | Delivery cannot be created |
| Blocked with delivery | Credit re-check after VL01N | VL02N cancel + VKM3 release | Credit manager | Goods issue blocked |
| Invoiced without PGI | Billing run bypassed delivery | VF11 cancel + VL02N correction | Billing clerk | Inventory mismatch |

### Parallel lifecycles

| Lifecycle | Status Table | Events | Synchronization Point | Risk |
|-----------|--------------|--------|----------------------|------|
| Sales order header | VBAK-VBSTAT | VA01, VA02, mass update | — | Base lifecycle |
| Delivery | LIKP-WBSTK | VL01N, VL02N, background | PGI completed | Desync if delivery cancelled after billing |
| Workflow | SWW_WIHEAD | WS12345678 steps | Approval complete | Stuck if workflow admin cancels without order update |
| IDoc status | EDIDS | WE20, background | Status 53 | False positive if application error after IDoc success |

### Invalid states

| Invalid State | How It Occurs | Detection Query | Correction Method | Prevention |
|---------------|---------------|-----------------|-------------------|------------|
| Status 30 with no delivery | Mass update set wrong status | SELECT * FROM VBAK WHERE VBSTAT = '30' AND NOT EXISTS (SELECT * FROM VBFA WHERE VBELV = VBAK.VBELN AND VBTYP_N = 'J') | VA02 manual correction | ZSD_STATUS_GUARD enhancement |
| Complete with open delivery | Cancellation workflow incomplete | SELECT * FROM VBAK WHERE VBSTAT = '50' AND VBELN IN (SELECT VBELV FROM VBFA WHERE LFSTAT <> 'C') | VL02N complete + re-run billing | Workflow step gate before terminal status |

### What this lifecycle does NOT cover

- Does not cover partner determination or pricing procedure logic.
- Does not cover batch-specific status or serial number lifecycle.
- Does not cover external system statuses (e.g., logistics platform, CRM) unless explicitly mapped as parallel lifecycle.
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every state has at least one entry event and one exit event, or is explicitly marked as terminal.</li>
      <li>Every transition has a named trigger event (transaction, program, API, workflow step).</li>
      <li>Every transition has a documented guard condition and the location where it is enforced.</li>
      <li>At least one error or recovery path is documented for non-terminal states.</li>
      <li>Invalid states are identified with a detection query and a correction method.</li>
      <li>Parallel lifecycles are mapped with synchronization points and desynchronization risks.</li>
      <li>The map has been reviewed by a process owner and at least one AMS support analyst.</li>
      <li>The "does NOT cover" section clarifies boundaries to prevent scope creep.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Confusing status field values with lifecycle states. <strong>Consequence:</strong> Technical status transitions are mapped without business process meaning, so critical guards (credit check, approval) are missed.</li>
      <li><strong>Mistake:</strong> Mapping only the happy path and ignoring rejections, cancellations, and rollbacks. <strong>Consequence:</strong> Edge cases create invalid states in production with no defined correction.</li>
      <li><strong>Mistake:</strong> Ignoring parallel lifecycles such as document status, workflow status, and IDoc status. <strong>Consequence:</strong> Race conditions cause one system to proceed while another believes the entity is blocked.</li>
      <li><strong>Mistake:</strong> Treating configuration as ground truth without checking actual production data. <strong>Consequence:</strong> Legacy statuses, bypass programs, and direct database updates remain invisible.</li>
      <li><strong>Mistake:</strong> Defining recovery paths without naming the authorized role and transaction. <strong>Consequence:</strong> Support teams use ad-hoc corrections that bypass audit trails and governance.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — Generic lifecycle description</h3>
    <blockquote>
      <p>A sales order lifecycle has several important states: Created, Processing, Completed, and Blocked. Each state represents a different phase in the order fulfillment process. States are important because they help track progress and identify issues. The order moves from Created to Processing when it is approved, and from Processing to Completed when the goods are delivered. Blocked status indicates a problem that needs to be resolved. It is important to monitor these states to ensure smooth operations.</p>
    </blockquote>
    <p><strong>Why it is weak:</strong> No specific events, no guard conditions, no SAP transactions, no error paths, no parallel lifecycles, no detection method. It is a textbook definition that cannot be used to find or fix a production issue.</p>

    <h3>Strong output — Copy-paste ready state transition table</h3>
    <pre><code>## Entity: SAP S/4HANA Sales Order (Type OR)

### States
| State | Name | Terminal |
|-------|------|----------|
| 10 | Created | No |
| 20 | Credit ok | No |
| 30 | Delivery ready | No |
| 40 | PGI complete | No |
| 50 | Invoiced | No |
| 60 | Complete | Yes |
| 90 | Blocked | No |

### Transitions
| From | To | Event | Guard | Guard Location |
|------|----|-------|-------|----------------|
| 10 | 20 | Credit check passed | Credit limit >= order value | FD32 + ZSD_CREDIT_001 |
| 20 | 30 | Delivery created | ATP confirmed | VL01N / VL10A |
| 30 | 40 | PGI posted | Stock available | VL02N GI |
| 40 | 50 | Billing posted | Pricing complete | VF01 |
| 50 | 60 | Accounting doc posted | RV document released | VFX3 |
| 10 | 90 | Credit check failed | Credit limit < order value | VKM1 |
| 90 | 10 | Block released | Manual approval + reason code | VKM3 + WS99900001 |

### Parallel lifecycle: IDoc status
| IDoc status | Meaning | Sync point | Risk |
|-------------|---------|------------|------|
| 30 | IDoc created | — | — |
| 53 | Application doc posted | Order saved | False positive if order later blocked |
| 51 | Application error | Order not saved | Desync: IDoc shows error but order may exist |

### Invalid state detection
```sql
-- Orders with status 30 but no delivery item
SELECT VBELN FROM VBAK
WHERE VBSTAT = '30'
AND VBELN NOT IN (SELECT VBELV FROM VBFA WHERE VBTYP_N = 'J');
```
</code></pre>
    <p><strong>Why it is strong:</strong> It names the exact transactions, configuration objects, guard conditions, and detection queries. A support analyst can run the query, check the guard, and fix the issue tomorrow.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>You are a systems analyst mapping entity lifecycles in an SAP landscape. Before you produce any output, gather:
1. The entity type and document type (e.g., sales order OR, business partner grouping 0001, material type HAWA).
2. The status profile or workflow template from SAP configuration.
3. A sample of production data showing the status distribution.
4. The business rules (credit check, release strategy, incompletion procedure) that govern transitions.

Produce the output in the State Lifecycle Analysis template format: states table, transitions table, error/recovery paths, parallel lifecycles, invalid states. For every transition, name the trigger event, guard condition, and where the guard is enforced. For every parallel lifecycle, note the synchronization point and desynchronization risk. Include at least one detection query for invalid states. End with a "does NOT cover" section.
</code></pre>

    <ul>
      <li><strong>Do</strong> gather configuration and production data before mapping. Do not guess states or transitions.</li>
      <li><strong>Do</strong> include error states, recovery paths, and rollback transactions. The happy path is never enough.</li>
      <li><strong>Do</strong> name the exact SAP transaction, program, or workflow step that triggers each event.</li>
      <li><strong>Do</strong> map parallel lifecycles (document status, workflow status, IDoc status) and their synchronization points.</li>
      <li><strong>Do</strong> write detection queries for invalid states. A state is not "invalid" unless you can find it in data.</li>
      <li><strong>Do</strong> link to Atlas diagnostics when the entity is a sales order, delivery, business partner, or purchase order.</li>
      <li><strong>Don't</strong> write generic state machine definitions. Every state and transition must be specific to the entity.</li>
      <li><strong>Don't</strong> treat configuration as the only truth. Check production data for legacy statuses and bypasses.</li>
      <li><strong>Don't</strong> skip the "does NOT cover" section. Scope creep in lifecycle mapping is common.</li>
      <li><strong>Don't</strong> invent guard conditions or custom code names. If you cannot verify the guard, flag it as unconfirmed.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a> — Define the system boundaries where the entity lifecycle operates.</li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a> — Identify the guard conditions and business rules that constrain transitions.</li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a> — Map the business process that the entity lifecycle supports.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a> — Diagnostic patterns for sales orders stuck in blocked or invalid states.</li>
      <li><a href="/atlas/diagnostics/sap-delivery-block-analysis/">SAP Delivery Block Analysis</a> — How delivery blocks interact with sales order and billing lifecycles.</li>
      <li><a href="/atlas/diagnostics/sap-release-strategy-diagnostics/">SAP Release Strategy Diagnostics</a> — How approval workflows affect document state transitions.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of state and lifecycle analysis for SAP and enterprise systems. It is not official SAP workflow documentation or UML state machine specification. It focuses on the practical subset of lifecycle mapping used during support, testing, and design. It does not cover advanced formal verification, Petri nets, or complex multi-instance workflows. Use it as a diagnostic and design tool, not as a comprehensive modeling methodology.</p>
  </section>
</article>
