---
layout: default
title: "Architecture Decision Record"
description: "Record why a significant architectural choice was made, what options were rejected, and what consequences follow."
permalink: /skill-hub/architecture/architecture-decision-record-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/architecture/">Architecture</a></li>
    <li aria-current="page">Architecture Decision Record</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Architecture</p>
  <h1>Architecture Decision Record</h1>
  <p class="lead">Record why a significant architectural choice was made, what options were rejected, and what consequences follow.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill produces a concise, durable record of a significant architecture decision. It captures the context that forced a choice, the options that were considered, the decision that was made, and the consequences — positive and negative — that follow from it. The output prevents future teams from revisiting the same question without context, and it protects against the gradual erosion of architectural intent as personnel change.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You must choose between two or more technical approaches and the choice will be hard to reverse.</li>
      <li>A design review identified a decision point that needs explicit documentation.</li>
      <li>A new team member or vendor is questioning a design choice that was made two years ago.</li>
      <li>An audit or compliance review requires evidence that architecture decisions were made with due diligence.</li>
      <li>You are standardizing decision records across a program so that all projects produce comparable documentation.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: Synchronous vs asynchronous customer master distribution</h3>
    <p>A project must decide how to distribute customer master data from SAP MDG to three downstream systems. Option A is synchronous SOAP services with immediate consistency. Option B is asynchronous events via SAP Event Mesh with eventual consistency. The ADR records that Option B was chosen because two downstream systems have lower availability than MDG, and synchronous calls would create cascading failures. The consequence is that downstream systems may see stale data for up to 30 seconds, which is acceptable for this business domain.</p>

    <h3>Example 2: Custom development vs standard SAP functionality</h3>
    <p>A business unit requests a custom pricing calculation in SAP SD because the standard procedure does not support their regional discount matrix. The ADR records that custom development was rejected in favor of configuring the standard condition technique with a new condition type and scale base. The consequence is that the solution stays within clean core boundaries but requires more complex condition record maintenance.</p>

    <h3>Example 3: Cloud vs on-premise data warehouse</h3>
    <p>A company must replace its aging SAP Business Warehouse system. The ADR evaluates cloud data warehouse, SAP Datasphere, and on-premise HANA upgrade. It records that SAP Datasphere was chosen because it preserves existing BW query investments while adding cloud scalability. The consequence is a hybrid landscape with data federation complexity that the operations team must manage.</p>

    <h3>Example 4: Microservices vs modular monolith for extensions</h3>
    <p>A development team wants to build a set of extensions to SAP S/4HANA using microservices on SAP BTP. The ADR records that a modular monolith on BTP Cloud Foundry was chosen instead because the team size is four developers, the expected load is moderate, and the operational overhead of distributed tracing and service mesh exceeds the team's capacity. The consequence is that future scaling beyond the monolith will require a deliberate re-architecture.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The decision question, stated as a single sentence (for example: "How should customer master data be distributed to downstream systems?").</li>
      <li>The context: what situation, constraint, or requirement forces this decision now.</li>
      <li>At least two viable options with descriptions, not just one preferred option.</li>
      <li>Evaluation criteria: what dimensions matter (cost, time, risk, maintainability, scalability, compliance).</li>
      <li>Stakeholder input: who advocated for each option and why.</li>
      <li>Reversibility assessment: how hard and expensive it would be to change this decision later.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What specific situation forces this decision now, rather than later or never?</li>
      <li>What is the cheapest option, what is the fastest option, and what is the safest option? Are they the same?</li>
      <li>Who will maintain this decision in two years, and do they have the skills for the chosen option?</li>
      <li>What happens if we need to reverse this decision in six months? What would it cost?</li>
      <li>Which option keeps us closest to standard SAP or standard platform functionality?</li>
      <li>What are we giving up by choosing this option? What capability do we lose?</li>
      <li>Does this decision create a new dependency, a new vendor lock-in, or a new single point of failure?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>State the decision question.</strong> Write one sentence that captures exactly what must be decided. Avoid framing the question to favor one option.</li>
      <li><strong>Describe the context.</strong> Explain the situation, constraints, and requirements that make this decision necessary. Include deadlines, budget limits, and regulatory factors.</li>
      <li><strong>Define evaluation criteria.</strong> List 3–5 criteria that will be used to compare options. Weight them if the team agrees on relative importance.</li>
      <li><strong>List options.</strong> Describe each option at a consistent level of detail. Include at least two viable options and a "do nothing" or status quo option where relevant.</li>
      <li><strong>Evaluate each option.</strong> Against each criterion, record pros, cons, and risks. Be honest about drawbacks of the option you prefer.</li>
      <li><strong>Make the decision.</strong> State which option is chosen and why. Cite the criteria that tipped the balance.</li>
      <li><strong>Record consequences.</strong> List positive consequences (what we gain) and negative consequences (what we accept or lose). Include technical debt, new dependencies, and skill requirements.</li>
      <li><strong>Assess reversibility.</strong> Rate the decision as easily reversible, moderately reversible, or irreversible. Describe what would be required to reverse it.</li>
      <li><strong>Assign ownership and review date.</strong> Name the person or role accountable for this decision. Set a date when the decision should be revisited.</li>
      <li><strong>Link related decisions.</strong> Reference other ADRs that this decision depends on or affects.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If only one option is viable, the decision is not architectural — it is a constraint. Record it as a constraint note, not an ADR.</li>
      <li>If the preferred option is custom development when a standard alternative exists, require explicit justification with named trade-offs.</li>
      <li>If a decision is irreversible or expensive to reverse, escalate to program or enterprise architecture for approval before recording.</li>
      <li>If an option introduces a new vendor or platform, evaluate exit cost and data portability explicitly.</li>
      <li>If two options score equally on all criteria, choose the one that is closer to existing team skills and operational tooling.</li>
      <li>If a decision contradicts a previous ADR, record the superseding relationship and update the status of the old ADR.</li>
      <li>If no one can be named as the decision owner, the decision is not ready to be recorded.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Architecture Decision Record (ADR)</strong> — The primary artifact: context, options, decision, consequences, reversibility, owner, review date.</li>
      <li><strong>Decision Log Entry</strong> — One-line summary for a master decision log: ID, date, question, decision, status.</li>
      <li><strong>Stakeholder Input Summary</strong> — Who advocated for which option and their key arguments (optional but valuable for contentious decisions).</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Architecture Decision Record (Markdown)</h3>
    <pre><code>---
artifact: Architecture Decision Record
id: ADR-001
date: YYYY-MM-DD
status: proposed | accepted | deprecated | superseded
owner: Name | Role
review_date: YYYY-MM-DD
---

## Decision question
<!-- One sentence. Example: How should customer master data be distributed to downstream systems? -->

## Context
<!-- What situation forces this decision? Constraints, requirements, deadlines. -->

## Evaluation criteria
<!-- 3-5 criteria used to compare options. Weight if agreed. -->

## Options considered

### Option 1: &lt;Name&gt;
- Description:
- Pros:
- Cons:
- Risks:

### Option 2: &lt;Name&gt;
- Description:
- Pros:
- Cons:
- Risks:

### Option 3: &lt;Name&gt; (if applicable)
- Description:
- Pros:
- Cons:
- Risks:

## Decision
<!-- Which option was chosen and why. Cite the criteria that tipped the balance. -->

## Consequences

### Positive
- 

### Negative
- 

## Reversibility
<!-- Easily reversible | Moderately reversible | Irreversible. What would be required to reverse? -->

## Related decisions
<!-- Links to other ADRs this depends on or affects -->
</code></pre>

    <h3>Decision Log Entry</h3>
    <pre><code>| ID | Date | Question | Decision | Status | Owner | Review Date |
|----|------|----------|----------|--------|-------|-------------|
| ADR-001 | YYYY-MM-DD | How to distribute customer master data | Async via Event Mesh | Accepted | Integration Architect | YYYY-MM-DD |
| ADR-002 | YYYY-MM-DD | Custom pricing vs standard condition technique | Standard with new condition type | Accepted | SD Functional Lead | YYYY-MM-DD |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The decision question is a single sentence with no embedded preference.</li>
      <li>At least two viable options are described at a consistent level of detail.</li>
      <li>Every option has at least one con or risk recorded honestly.</li>
      <li>The decision explicitly cites which criteria tipped the balance.</li>
      <li>Consequences include both positive and negative outcomes.</li>
      <li>Reversibility is rated and the reversal cost is described.</li>
      <li>A named owner and a review date are assigned.</li>
      <li>The ADR is linked to related decisions where applicable.</li>
      <li>The ADR has been shared with the team that will implement and operate it.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Recording only the chosen option, not the rejected ones. <strong>Consequence:</strong> Future teams revisit the same question because they do not know why alternatives were discarded.</li>
      <li><strong>Mistake:</strong> Framing the decision question to favor one answer. <strong>Consequence:</strong> The ADR becomes rationalization, not documentation, and loses credibility.</li>
      <li><strong>Mistake:</strong> Omitting negative consequences. <strong>Consequence:</strong> The team is surprised by technical debt, operational burden, or capability loss that was known but not communicated.</li>
      <li><strong>Mistake:</strong> Writing ADRs for trivial decisions. <strong>Consequence:</strong> The decision log becomes noise, and important decisions are lost in volume.</li>
      <li><strong>Mistake:</strong> Never revisiting decisions. <strong>Consequence:</strong> An ADR accepted three years ago under different constraints continues to constrain the architecture even though the context has changed.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ol>
      <li><strong>Extract the decision question.</strong> If the user describes a situation without a clear question, help them formulate one neutral sentence.</li>
      <li><strong>Require at least two options.</strong> If the user presents only one option, ask what alternatives were considered or what the status quo would look like.</li>
      <li><strong>Be honest about drawbacks.</strong> For every option, including the preferred one, list at least one con or risk. Do not sanitize the record.</li>
      <li><strong>Use the template.</strong> Produce the ADR in the exact Markdown template format provided. Fill every section.</li>
      <li><strong>Do not invent stakeholder input.</strong> If the user does not provide who advocated for which option, leave the stakeholder summary empty or ask for it.</li>
      <li><strong>Assess reversibility realistically.</strong> Do not default to "moderately reversible." Consider data migration, contract terms, skill retraining, and integration rework.</li>
      <li><strong>Link to related skills.</strong> If the ADR concerns integration, reference <a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a> or <a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a>. If it concerns data, reference <a href="/atlas/concepts/data-contracts/">Data Contracts</a>.</li>
    </ol>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/solution-architecture-review-working-skill/">Solution Architecture Review</a> — The review process that often surfaces decisions needing ADRs.</li>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a> — Define the boundaries that decisions affect.</li>
      <li><a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a> — Deep-dive for decisions about asynchronous patterns.</li>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Deep-dive for decisions about API design and ownership.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-event-driven-architecture/">SAP Event-Driven Architecture</a> — Context for decisions about event-based integration in SAP landscapes.</li>
      <li><a href="/atlas/concepts/sap-clean-core-strategy/">SAP Clean Core Strategy</a> — How clean core principles constrain custom vs standard decisions.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — How data agreements affect architectural choices.</li>
      <li><a href="/atlas/concepts/api-contracts/">API Contracts</a> — How API design commitments constrain and enable decisions.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of architecture decision recording practice. It is not an official standard from any framework body. It focuses on the lightweight ADR format suitable for project and program use. It does not cover enterprise architecture board governance, formal architectural review boards, or compliance-mandated decision processes. Use it as a practical method for capturing context and rationale, not as a substitute for organizational governance where required.</p>
  </section>
</article>
