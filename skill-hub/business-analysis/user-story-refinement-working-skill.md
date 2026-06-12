---
layout: default
title: "User Story Refinement Working Skill"
description: "Turn vague user stories into structured, implementable backlog items with acceptance criteria, boundaries, and dependencies."
permalink: /skill-hub/business-analysis/user-story-refinement-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">User Story Refinement</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>User Story Refinement Working Skill</h1>
  <p class="lead">Turn backlog items that are too large, vague, or unbounded into sprint-ready stories with acceptance criteria, boundaries, and dependencies.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill takes an existing user story or backlog item — written by a product owner, stakeholder, or team member — and transforms it into a structured, implementable unit. It adds acceptance criteria, identifies hidden assumptions, maps dependencies, defines boundaries, and splits stories that are too large for a single sprint. The output is a Story Brief that a development team can estimate, a tester can verify, and a product owner can defend.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Sprint planning when a story is rejected as "too big" or "not ready."</li>
      <li>Backlog refinement when acceptance criteria are missing, ambiguous, or untestable.</li>
      <li>A story touches multiple systems (SAP, CRM, middleware) and no one knows who owns which part.</li>
      <li>A stakeholder adds a "quick fix" to an existing story that doubles its scope.</li>
      <li>An integration story lacks clarity on which system validates which field.</li>
      <li>A data migration story says "move everything" without specifying cutoff, deduplication, or validation.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>"As a sales rep, I want to create a customer in the system"</h3>
    <p>A raw story from a sales manager lacks detail on which fields are mandatory, which system creates the record (SAP S/4 vs MDG vs CRM), what validation rules apply, and what happens when a duplicate exists. Refinement must split this into: create business partner in MDG with tax validation, replicate to SAP S/4 sales area, and handle duplicate account group detection. Without refinement, developers build a UI that bypasses MDG governance and loads invalid data into SAP.</p>

    <h3>"The system should handle returns"</h3>
    <p>A product owner writes a one-line story for the returns process. Missing: the actor (customer service rep or warehouse clerk?), the trigger (customer request or goods receipt?), the boundary (does it include credit memo creation or just the return order?), and the acceptance criteria (what status must the return order reach before finance is notified?). Refinement must produce a use case-level breakdown with clear actor and system boundaries, splitting credit memo creation into a separate story if it crosses into FI.</p>

    <h3>"Improve order processing speed"</h3>
    <p>A stakeholder asks to "make order processing faster." The raw story lacks a metric (from what baseline to what target?), a system boundary (SAP VA01? IDoc processing? E-commerce checkout?), and a scenario (all order types or just standard ZOR?). Refinement must reframe the story as: "Reduce average SAP S/4 sales order creation time (VA01) for standard order type ZOR from 45 seconds to under 10 seconds for orders with 20 line items or fewer, measured under peak load conditions." Without this, the team optimizes the wrong layer and misses the real bottleneck.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Raw user stories or backlog items from the current sprint or product backlog.</li>
      <li>Sprint context: team velocity, sprint goal, and known capacity.</li>
      <li>System documentation showing which systems, transactions, and fields are involved.</li>
      <li>Business rules or validation logic that constrain the story.</li>
      <li>List of known dependencies: other stories, system upgrades, external APIs, data availability.</li>
      <li>Stakeholder availability to confirm boundaries and acceptance criteria.</li>
      <li>Non-functional requirements: performance, security, compliance constraints.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the smallest version of this story that still delivers value to the user?</li>
      <li>What must be true before this story can start: data readiness, system availability, another story completed?</li>
      <li>Which system owns the data creation, and which system owns the validation?</li>
      <li>What happens when the happy path fails: missing data, duplicate record, system timeout?</li>
      <li>Who will confirm this story is done, and what will they look at?</li>
      <li>What is explicitly not included in this story? What would a reasonable person assume is included but should not be?</li>
      <li>If this story were completed in two days instead of two weeks, what would be cut?</li>
      <li>Which fields, tables, or transactions must be present for this story to execute correctly?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the raw story.</strong> Identify the actor, the need, and the intended outcome. If any are missing, flag the story as unready.</li>
      <li><strong>Identify missing elements.</strong> Check for: acceptance criteria, boundaries, dependencies, assumptions, non-functional requirements, and owner.</li>
      <li><strong>Split if the story is too large.</strong> If it touches multiple systems, spans multiple process steps, or cannot be completed in one sprint, split it into smaller stories that each deliver a coherent increment.</li>
      <li><strong>Write acceptance criteria.</strong> Use Given/When/Then format. Include at least one normal case, one boundary case, and one error case.</li>
      <li><strong>Identify dependencies.</strong> List other stories, systems, data, or decisions that must be ready before this story can be implemented or tested.</li>
      <li><strong>Surface hidden assumptions.</strong> Document what the story assumes about data quality, system behavior, user knowledge, or external conditions.</li>
      <li><strong>Define boundaries.</strong> State what is in scope and what is out of scope for this story. Link boundaries to business rules and process ownership.</li>
      <li><strong>Package into a Story Brief.</strong> One brief per refined story. Include the refined statement, acceptance criteria, dependencies, assumptions, boundaries, and estimation notes.</li>
      <li><strong>Validate with the product owner.</strong> Walk through the brief and confirm that the refined story still matches the original intent.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a story has no acceptance criteria, it is not ready for sprint planning.</li>
      <li>If a story touches more than one system and there is no integration contract, split the story or add a dependency on contract definition.</li>
      <li>If a story describes a solution ("add a button"), separate the underlying need from the proposed implementation.</li>
      <li>If a story cannot be completed within one sprint, split it. The split must be vertical (end-to-end slice) rather than horizontal (layer by layer).</li>
      <li>If a dependency has no owner or delivery date, the story is at risk — flag it before commitment.</li>
      <li>If a stakeholder asks to add scope during refinement, require a formal decision: swap out existing scope, extend the sprint, or create a new story.</li>
      <li>If acceptance criteria contain implementation instructions ("use table X"), rewrite them as outcomes ("data is available in table X").</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Story Brief</strong> — One per refined story. Contains refined statement, acceptance criteria, dependencies, assumptions, boundaries, and estimation notes. See template below.</li>
      <li><strong>Dependency List</strong> — Table of dependencies with owner, status, and risk level.</li>
      <li><strong>Assumptions Log</strong> — List of assumptions with validation plan and risk if false.</li>
      <li><strong>Sprint Ready Checklist</strong> — Per-story verification before commitment.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Story Brief (compact)</h3>
    <pre><code>---
artifact: Story Brief
id: STORY-001
source: Backlog item | Stakeholder request | Incident
status: draft | refined | ready | committed
---

## Refined story statement
<!-- As a [actor], I want [need] so that [outcome]. Example: "As a credit controller, I want blocked orders to route to my worklist automatically so that I do not rely on email alerts." -->

## Acceptance criteria
### Normal case
Given &lt;precondition&gt;
When &lt;action&gt;
Then &lt;expected outcome&gt;

### Boundary case
Given &lt;precondition&gt;
When &lt;action&gt;
Then &lt;expected outcome&gt;

### Error case
Given &lt;precondition&gt;
When &lt;action&gt;
Then &lt;expected outcome&gt;

## Dependencies
<!-- What must be ready before this story can start or be tested -->
- Dependency: &lt;description&gt; | Owner: &lt;name&gt; | Status: &lt;status&gt; | Risk: &lt;level&gt;

## Assumptions
<!-- What we assume to be true. Example: "Customer master data is fully replicated from MDG to S/4 before this story is tested." -->
- Assumption: &lt;description&gt; | Validation: &lt;method&gt; | Risk if false: &lt;impact&gt;

## Boundaries
### In scope
<!-- Specific items included in this story -->

### Out of scope
<!-- Specific items excluded. Example: "Credit memo creation is handled in STORY-002." -->

## Estimation notes
<!-- Story points, complexity, or rough hours. Include rationale. -->

## Product owner
<!-- Name of the person who can confirm this story is correct -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every story has at least one acceptance criterion written in Given/When/Then format.</li>
      <li>Every story has a named product owner who can confirm intent.</li>
      <li>Dependencies are identified with owner and expected delivery date.</li>
      <li>Assumptions are separated from facts and have a validation plan.</li>
      <li>Boundaries are stated explicitly: what is in scope and what is out of scope.</li>
      <li>Stories are sized to fit within one sprint.</li>
      <li>No acceptance criterion contains implementation detail or solution design.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Refining without splitting.</strong> Consequence: the story is too large for a sprint, carries hidden work, and fails to deliver at the review boundary.</li>
      <li><strong>Adding implementation detail instead of acceptance criteria.</strong> Consequence: the team is constrained to a specific technical solution that may be suboptimal.</li>
      <li><strong>Skipping boundary definition.</strong> Consequence: stakeholders assume scope that was never agreed, leading to mid-sprint scope creep and estimation failure.</li>
      <li><strong>Ignoring dependencies until the sprint starts.</strong> Consequence: the team discovers on day two that the API is not ready or the data is missing, blocking progress.</li>
      <li><strong>Treating assumptions as facts.</strong> Consequence: the story fails because the assumed data quality or system behavior does not match reality.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output — Generic story with no structure</h3>
    <p>A weak AI output restates the raw story with vague qualifiers and no actionable detail:</p>
    <blockquote>
      <p><strong>Refined story:</strong> As a user, I want the system to process orders faster so that I can work better.</p>
      <p><strong>Acceptance criteria:</strong></p>
      <ul>
        <li>The system should be fast.</li>
        <li>The system should handle errors gracefully.</li>
        <li>The system should be user-friendly.</li>
      </ul>
      <p><strong>Dependencies:</strong> None identified.</p>
      <p><strong>Owner:</strong> TBD.</p>
    </blockquote>
    <p><strong>Why this is weak:</strong> No metric for "fast." No boundary for which order types or systems. No owner. No testable criteria. No next action. A developer cannot build against this, and a tester cannot verify it.</p>

    <h3>Strong output — Sprint-ready Story Brief</h3>
    <p>A strong AI output produces a copy-paste-ready artifact with specific evidence, boundaries, and next actions:</p>
    <pre><code>---
artifact: Story Brief
id: STORY-O2C-042
source: Backlog refinement — sales ops request
status: refined
---

## Refined story statement
As a sales operations specialist, I want SAP S/4 to block outbound delivery creation (VL01N) for customers with exceeded credit limits so that unauthorized shipments do not occur.

## Acceptance criteria
### Normal case
Given a customer with an open credit limit of 50,000 EUR and current exposure of 48,000 EUR
When a new standard order (ZOR) of 5,000 EUR is created and delivery is attempted
Then the system blocks delivery creation with status "Credit block" and routes the case to the credit controller worklist (UKM_CASE)

### Boundary case
Given a customer with exceeded credit limit
When an emergency order marked "Express" under 1,000 EUR is created
Then the system allows delivery with a warning, logs to audit, and notifies the credit controller within 15 minutes

### Error case
Given a customer with missing credit segment (UKM_BP)
When a delivery is attempted
Then the system blocks delivery, logs error "Credit segment missing," and routes to the MDG data steward

## Dependencies
- Dependency: Credit limit update job runs every 4 hours | Owner: Basis team | Status: planned | Risk: medium
- Dependency: UKM_CASE worklist configuration complete | Owner: SD consultant | Status: in progress | Risk: low

## Assumptions
- Assumption: Customer credit limits are maintained in FD32 and replicated to UKM_BP in real time.
  Validation: Check UKM_BP for 10 sample customers before sprint start. | Risk if false: blocks will be incorrect.
- Assumption: Emergency orders are flagged by order reason code "EXP" in VBAK-AUGRU.
  Validation: Confirm with sales ops that this code is used consistently. | Risk if false: boundary case cannot be tested.

## Boundaries
### In scope
- Standard order type ZOR
- Delivery creation via VL01N and VL10
- Credit block status and routing to UKM_CASE

### Out of scope
- Credit memo creation or billing block logic
- Customer master creation or MDG change requests
- Other order types (ZOR2, ZCR)

## Estimation notes
- 8 story points. Complexity: medium. Integration with UKM_CASE requires SD-FI alignment.

## Product owner
- Maria Chen, Sales Operations Manager
</code></pre>
    <p><strong>Why this is strong:</strong> It names the actor, the system, the transaction, the order type, the specific threshold, the routing destination, and the boundary cases. It includes dependencies with owners and a validation plan for assumptions. A developer can build it, a tester can verify it, and the product owner can sign off.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><em>"You are a backlog refinement assistant. You receive a raw user story and the following context: [system name, involved transactions, sprint length, team velocity, known constraints]. Produce a Story Brief with: Refined Story Statement (As a/I want/so that), Acceptance Criteria (Given/When/Then for normal, boundary, and error cases), Dependencies (with owner and status), Assumptions (with validation method), and explicit Boundaries (in scope and out of scope). If information is missing, flag it. Do not add implementation detail. Do not invent owners or system names."</em></p>

    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Gather system context before refining.</strong> Know which transactions, tables, and systems are involved before writing acceptance criteria.</li>
      <li><strong>Use Given/When/Then format for all acceptance criteria.</strong> Be specific about preconditions, actions, and outcomes.</li>
      <li><strong>Split stories that touch multiple systems or process steps.</strong> Vertical slices only.</li>
      <li><strong>Flag missing information instead of guessing.</strong> If an actor, owner, or field name is unknown, state it as an open question.</li>
      <li><strong>Separate the need from the proposed solution.</strong> If the raw story says "add a button," ask what problem the button solves.</li>
      <li><strong>Produce one Story Brief per story.</strong> Do not bundle multiple stories into one brief.</li>
      <li><strong>Do not write acceptance criteria that contain implementation instructions.</strong> Criteria state what must be true, not how to build it.</li>
      <li><strong>Link to Atlas diagnostics</strong> when stories relate to SAP processes. For example, credit management stories should reference <a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/scope-boundary-definition-working-skill/">Scope Boundary Definition Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a> — Process context for O2C user stories.</li>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for process-related story boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of user story refinement practices. It is not official Scrum Guide or BABOK documentation. It focuses on enterprise and SAP contexts where stories must account for system boundaries, integration dependencies, and data governance.</p>
    <p>Known limitations: the skill assumes the raw story exists and that the product owner is available for validation. In environments with no product owner or no backlog discipline, this skill cannot create readiness from chaos. It does not cover formal requirements engineering or model-driven specification methods.</p>
  </section>
</article>
