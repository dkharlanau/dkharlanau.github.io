---
layout: default
title: "Use Case Analysis Working Skill"
description: "Identify actors, goals, and system interactions to produce structured use cases that reveal missing requirements and boundary conditions."
permalink: /skill-hub/business-analysis/use-case-analysis-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Use Case Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Use Case Analysis Working Skill</h1>
  <p class="lead">Identify actors, goals, and system interactions to produce structured use cases that reveal missing requirements and boundary conditions.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill analyzes a business situation through the lens of use cases: who initiates the action, what they want to achieve, and how the system responds. It produces structured use cases that expose hidden actors, missing system steps, and boundary conditions that vague requirements miss. The output is a Use Case Brief that can be validated with stakeholders and translated into requirements, test cases, or integration contracts.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A new feature or system is being designed and no one has mapped the end-to-end interaction sequence.</li>
      <li>An integration failure reveals that one system assumed a step the other system never performed.</li>
      <li>A process redesign needs to know which human decisions can be automated and which require approval.</li>
      <li>A requirements document lists system functions but never states who triggers them or what happens when they fail.</li>
      <li>A support team needs to document how a process actually works, not how it is supposed to work.</li>
      <li>An AI automation opportunity is being scoped and the boundary between human and machine decisions is unclear.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4 sales order creation</h3>
    <p>A project to streamline order entry needs a use case for "Create sales order." The primary actor is the sales representative. Secondary actors are the credit management system (checks exposure), the ATP engine (checks availability), and the pricing engine (calculates conditions). The use case reveals that the current process has no extension for "customer master incomplete," causing silent blocks. The main success scenario must include: enter order, validate customer, check credit, check ATP, calculate price, confirm order. Extensions must include: credit block, ATP failure, pricing mismatch, and incomplete customer data. Without this analysis, the project automates only the happy path and misses the failure modes that generate 80 percent of support tickets.</p>

    <h3>E-commerce to SAP integration</h3>
    <p>A retailer wants to connect a Shopify frontend to SAP S/4. The use case "Place customer order" reveals three primary actors: the customer (initiates), the e-commerce platform (validates cart), and SAP (creates order). Secondary actors: the inventory system (stock reservation), the payment gateway (authorization), and the tax engine (VAT calculation). The analysis reveals a missing extension: "Reservation times out before SAP order is created." Without this, the integration silently drops orders when the warehouse is slow to confirm.</p>

    <h3>Returns processing</h3>
    <p>A customer service team wants to automate returns. The use case "Process return order" shows the primary actor is the customer service rep, but a secondary actor is the warehouse clerk who must confirm goods receipt before finance can issue a credit memo. The analysis reveals that the current system does not notify finance when the warehouse step completes, causing credit memos to be delayed by days. The use case extension "Goods receipt confirmed late" becomes a requirement for a status-triggered notification to the accounts receivable clerk.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Business event description or stakeholder request that triggers the use case.</li>
      <li>Process documentation or <a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Notes</a> for the affected workflow.</li>
      <li>System documentation showing which systems, transactions, and APIs are involved.</li>
      <li>Incident tickets or error logs showing where the current process breaks.</li>
      <li>Stakeholder interviews with people who perform, approve, or suffer from the process.</li>
      <li>Integration contracts or interface specifications for cross-system use cases.</li>
      <li>User role assignments to verify who has access to which transactions.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the actor's goal, and how do they know when it is achieved?</li>
      <li>What event triggers this use case, and what prevents it from starting?</li>
      <li>Which other systems or actors must respond before the goal is met?</li>
      <li>What happens when the primary actor is unavailable or the system is down?</li>
      <li>What are the most common failure modes, and who handles them today?</li>
      <li>Where does the process hand off from one actor to another, and what information must transfer?</li>
      <li>Which steps are manual today and could be automated? Which must stay manual?</li>
      <li>What would a developer or tester need to know that is not stated in the current documentation?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the business event.</strong> What triggers the use case? A user action, a system timer, an incoming message, or a status change?</li>
      <li><strong>Name the primary actor.</strong> The person or system that initiates the use case to achieve a goal. If there are multiple initiators, split or generalize carefully.</li>
      <li><strong>Identify secondary actors.</strong> Systems, people, or external services that respond to or constrain the primary actor's progress.</li>
      <li><strong>Write the goal statement.</strong> Format: "The [primary actor] achieves [goal] by [main action]." Keep it one sentence and outcome-focused.</li>
      <li><strong>Define preconditions.</strong> What must be true before the use case starts: data exists, user is authenticated, system is available, credit limit is valid.</li>
      <li><strong>Map the main success scenario.</strong> Numbered steps from trigger to goal completion. Each step must be a single action by a single actor. Include system responses.</li>
      <li><strong>Identify extension points.</strong> At each step, ask: what could go wrong, what could vary, and what decision branches exist? Document each as an extension with a trigger condition and handling steps.</li>
      <li><strong>Derive requirements.</strong> From each step and extension, extract requirements: functional requirements for the system, data requirements for inputs, and non-functional requirements for performance or reliability.</li>
      <li><strong>Validate with actors.</strong> Walk through the main success scenario and each extension with the people who perform the work. Confirm that the sequence matches reality.</li>
      <li><strong>Document in a Use Case Brief.</strong> One brief per use case. Include actor list, goal, preconditions, main success scenario, extensions, and derived requirements.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a use case has no secondary actor, verify whether it truly operates in isolation or whether secondary actors have been overlooked.</li>
      <li>If an extension point has no handling steps, it is a missing requirement — flag it.</li>
      <li>If two use cases share the same trigger and the same primary actor, merge them or differentiate by goal.</li>
      <li>If a step involves two actors simultaneously, split it into two sequential steps.</li>
      <li>If an extension occurs in more than 20 percent of executions, consider it a variant rather than an exception and give it its own use case or sub-flow.</li>
      <li>If a use case requires data from a system that is not listed as a secondary actor, add the system.</li>
      <li>If the main success scenario has more than 12 steps, the use case is too granular or too broad — split or simplify.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Use Case Brief</strong> — One per use case. Contains actor list, goal statement, preconditions, main success scenario, extensions, and derived requirements. See template below.</li>
      <li><strong>Actor Catalog</strong> — List of all primary and secondary actors with their roles, goals, and system access.</li>
      <li><strong>Extension Register</strong> — Consolidated table of all extension points with trigger conditions, handling steps, and priority.</li>
      <li><strong>Derived Requirements List</strong> — Requirements extracted from the use case, mapped to steps and extensions.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Use Case Brief (compact)</h3>
    <pre><code>---
artifact: Use Case Brief
id: UC-001
status: draft | reviewed | approved
---

## Use case name
<!-- Short, descriptive. Example: "Create sales order" -->

## Primary actor
<!-- Who initiates. Example: "Sales representative (SAP user with VA01 authorization)" -->

## Secondary actors
<!-- Systems or people that respond. Example: "Credit management system, ATP engine, pricing engine" -->

## Goal statement
<!-- One sentence. Example: "The sales representative creates a confirmed sales order that passes credit check, availability check, and pricing validation." -->

## Preconditions
<!-- What must be true before the use case starts -->
- Customer master exists in the relevant sales area (XD03).
- Material master exists and is active in the plant.
- User has VA01 authorization for the sales organization.

## Main success scenario
1. Sales representative enters order header: customer, sales organization, order type.
2. System validates customer master and sales area data.
3. Sales representative enters line items: material, quantity, requested delivery date.
4. System performs ATP check and confirms availability.
5. System performs credit check and confirms exposure is within limit.
6. System calculates pricing conditions.
7. Sales representative saves the order.
8. System assigns order number and confirms status.

## Extensions
### Extension 1: Credit block
- Trigger: Step 5 — credit exposure exceeds limit.
- Handling: System blocks order with status "Credit block." Routes to credit controller worklist (UKM_CASE). Sales representative cannot proceed without override.

### Extension 2: ATP failure
- Trigger: Step 4 — insufficient stock.
- Handling: System displays shortage. Sales representative chooses: confirm partial quantity, change requested date, or cancel line item.

### Extension 3: Incomplete customer data
- Trigger: Step 2 — missing sales area or shipping point.
- Handling: System displays incompletion log. Sales representative updates customer master or contacts MDG steward.

## Derived requirements
- REQ-001: The system must perform real-time credit check at order save.
- REQ-002: The system must display ATP result with available quantity and confirmed date.
- REQ-003: The system must validate customer master completeness before line item entry.

## Related use cases
<!-- Links to other briefs -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every use case has a single primary actor and a clear goal statement.</li>
      <li>Preconditions are stated and verifiable before the use case starts.</li>
      <li>The main success scenario has 4 to 12 steps, each with a single actor and action.</li>
      <li>Every step that can fail has at least one documented extension.</li>
      <li>Extensions include a trigger condition and specific handling steps.</li>
      <li>Derived requirements trace back to specific steps or extensions.</li>
      <li>Secondary actors are named and linked to the systems or roles they represent.</li>
      <li>The use case has been validated with at least one person who performs the primary actor's role.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing use cases as system design documents.</strong> Consequence: the use case prescribes screens, buttons, and database tables instead of describing actor goals and system responsibilities. The result is brittle and hard to validate with business users.</li>
      <li><strong>Skipping secondary actors.</strong> Consequence: integration failures are discovered late because the use case never acknowledged that another system was involved.</li>
      <li><strong>Documenting only the happy path.</strong> Consequence: 80 percent of support effort goes to unhandled exceptions that were never analyzed.</li>
      <li><strong>Mixing two primary actors in one use case.</strong> Consequence: the use case tries to describe both the sales rep and the customer service rep, creating confusion about who initiates and who responds.</li>
      <li><strong>Leaving extensions as vague "system handles error."</strong> Consequence: the requirement is incomplete. Developers guess at error handling, and testers have no pass/fail standard.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output — Vague description with no structure</h3>
    <p>A weak AI output describes a process in paragraphs without separating actors, steps, or failure modes:</p>
    <blockquote>
      <p><strong>Use case:</strong> Process customer order.</p>
      <p><strong>Description:</strong> The system receives a customer order, validates it, checks stock, and creates a delivery. If something goes wrong, the system handles the error and notifies the user. The sales team uses this feature daily. It is important for revenue.</p>
      <p><strong>Actors:</strong> User, System.</p>
      <p><strong>Requirements:</strong> The system must process orders efficiently and handle errors gracefully.</p>
    </blockquote>
    <p><strong>Why this is weak:</strong> No primary actor is named. No step-by-step sequence. No preconditions. No specific extensions. "System handles error" is not a handling step. No derived requirements. No next action. A developer cannot build from this, and a tester cannot verify it.</p>

    <h3>Strong output — Structured Use Case Brief</h3>
    <p>A strong AI output produces a copy-paste-ready artifact with specific actors, steps, extensions, and derived requirements:</p>
    <pre><code>---
artifact: Use Case Brief
id: UC-O2C-015
status: reviewed
---

## Use case name
Create sales order with credit and ATP validation

## Primary actor
Sales representative (SAP user with VA01 authorization for sales org 1000)

## Secondary actors
- SAP Credit Management system (UKM_BP exposure check)
- SAP ATP engine (scope of check for plant 1100)
- SAP Pricing engine (condition type PR00 and tax determination)

## Goal statement
The sales representative creates a confirmed sales order that passes credit check, availability check, and pricing validation for standard order type ZOR.

## Preconditions
- Customer master exists in sales area 1000 / 10 / 00 (XD03).
- Material master exists and is active in plant 1100.
- User has VA01 authorization for sales org 1000.
- Pricing procedure is assigned to the order type and customer.

## Main success scenario
1. Sales representative enters order header: customer 1000001234, sales org 1000, order type ZOR.
2. System validates customer master and confirms sales area data is complete.
3. Sales representative enters line item: material MAT-001, quantity 100, requested delivery date 2026-07-15.
4. System performs ATP check for plant 1100 and confirms full quantity available.
5. System performs credit check via UKM_BP and confirms exposure within 50,000 EUR limit.
6. System calculates pricing: PR00 = 120.00 EUR, tax = 22.80 EUR.
7. Sales representative saves the order.
8. System assigns order number 4500012345 and confirms status "Complete."

## Extensions
### Extension 1: Credit block
- Trigger: Step 5 — credit exposure exceeds 50,000 EUR.
- Handling: System sets order status "Credit block." Routes case to UKM_CASE worklist for credit controller Maria Chen. Sales representative cannot proceed without override. Notification sent within 5 minutes.

### Extension 2: ATP partial availability
- Trigger: Step 4 — only 60 units available in plant 1100.
- Handling: System displays confirmed quantity 60 with confirmed date 2026-07-15 and shortage 40 with next availability 2026-07-22. Sales representative chooses: confirm partial, change date, or cancel line.

### Extension 3: Incomplete customer data
- Trigger: Step 2 — missing shipping point determination (VBAK-VSTEL).
- Handling: System displays incompletion log (V.26). Order saves but blocks for delivery. Sales representative contacts MDG steward to update customer master shipping conditions.

## Derived requirements
- REQ-001: The system must perform real-time credit check at order save using UKM_BP exposure data.
- REQ-002: The system must display ATP result with available quantity, confirmed date, and next availability date.
- REQ-003: The system must validate customer master completeness (shipping point, payment terms, tax classification) before allowing delivery creation.
- REQ-004: The system must route credit block cases to UKM_CASE worklist and notify the assigned credit controller within 5 minutes.

## Related use cases
- UC-O2C-016: Create delivery for confirmed sales order
- UC-O2C-017: Process billing for delivered order
</code></pre>
    <p><strong>Why this is strong:</strong> It names the primary actor with authorization context, lists secondary actors with specific systems, states verifiable preconditions, breaks the process into discrete steps, documents specific extensions with triggers and handling, and derives requirements that trace back to steps. A developer can build against it, a tester can verify each step, and a stakeholder can validate the sequence against reality.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><em>"You are a business analyst documenting use cases for enterprise systems. You receive a business event description and system context. Produce a Use Case Brief with: Use Case Name, Primary Actor (with role/system access), Secondary Actors (with systems involved), Goal Statement (one sentence), Preconditions (verifiable), Main Success Scenario (numbered steps, one actor per step), Extensions (trigger + handling for each failure point), and Derived Requirements (tracing to steps). If a system or actor is missing from the context, flag it. Do not describe screens or database tables. Focus on actor goals and system responsibilities."</em></p>

    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Start with the business event, not the system.</strong> What triggers the use case and what goal does the primary actor want to achieve?</li>
      <li><strong>Name primary and secondary actors explicitly.</strong> Include their system access or role if relevant. Do not use generic "user" or "system."</li>
      <li><strong>Write the main success scenario as numbered steps.</strong> One action per step, one actor per step. Include the system response if it affects the next step.</li>
      <li><strong>Identify at least three extensions.</strong> Normal case, boundary case, and error case. If an extension has no handling steps, flag it as a missing requirement.</li>
      <li><strong>Derive requirements from steps and extensions.</strong> Each requirement must trace back to a specific step or extension number.</li>
      <li><strong>Validate the use case with someone who performs the primary actor's role.</strong> Do not publish without business validation.</li>
      <li><strong>Do not describe user interfaces or database schemas.</strong> Use cases describe behavior, not implementation.</li>
      <li><strong>Link to Atlas diagnostics</strong> when use cases relate to SAP processes. For example, order creation use cases should reference <a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a> — Process context for O2C use cases.</li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a> — Extension handling for order blocks.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of use case analysis practices. It is not official UML or BABOK documentation. It focuses on practical enterprise and SAP contexts where use cases reveal integration gaps and failure modes.</p>
    <p>Known limitations: the skill assumes access to process documentation and stakeholders who can validate the scenario. In environments with complex custom workflows or poor documentation, use case analysis becomes a discovery exercise rather than a documentation exercise. The skill does not cover formal UML notation or use case point estimation.</p>
  </section>
</article>
