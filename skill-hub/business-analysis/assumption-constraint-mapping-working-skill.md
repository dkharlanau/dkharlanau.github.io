---
layout: default
title: "Assumption and Constraint Mapping Working Skill"
description: "Surface hidden assumptions, separate them from known constraints, and map the risk of each assumption being wrong before it breaks the project."
permalink: /skill-hub/business-analysis/assumption-constraint-mapping-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Assumption and Constraint Mapping</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Assumption and Constraint Mapping Working Skill</h1>
  <p class="lead">Surface hidden assumptions, separate them from known constraints, and map the risk of each assumption being wrong before it breaks the project.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Every project rests on assumptions that are treated as facts until they fail. This skill identifies, documents, and validates assumptions before they become risks. It separates assumptions from constraints: assumptions can be proven true or false, constraints are immovable. The output is an Assumptions Log and Constraint Map that help project managers decide where to invest validation effort, and where to accept limits.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project starts and the team says "we assume the data is clean" without verifying it.</li>
      <li>An estimate is produced but no one has validated the assumptions behind the sizing.</li>
      <li>An integration project assumes an API contract is stable, but the vendor has not confirmed it.</li>
      <li>A post-mortem reveals that a project failed because an unstated assumption turned out to be false.</li>
      <li>A regulatory requirement is treated as a constraint, but it actually allows multiple compliance paths.</li>
      <li>A stakeholder insists a timeline is fixed, but the constraint has not been documented with source or authority.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4 migration: "The data is clean"</h3>
    <p>A migration project assumes that customer master data in the source ECC system is complete, consistent, and ready to load. The assumption mapping reveals that 12 percent of customer records lack sales area data, 8 percent have duplicate account groups, and tax numbers fail validation for three country codes. The assumption "data is clean" is false. The project must either add a data cleansing phase (effort: 3 weeks) or accept that the migration will load incomplete data and trigger incompletion blocks in S/4. Without mapping this assumption, the project plans for a 2-week migration that actually requires 5 weeks of prep.</p>

    <h3>Integration project: "The API is stable"</h3>
    <p>An e-commerce integration assumes the partner API v2.1 will not change during the 3-month project. The constraint mapping reveals that the vendor's roadmap shows a v2.2 release in 6 weeks with breaking changes to the authentication model. The assumption is unvalidated and high-risk. The project must either negotiate a stability commitment with the vendor, build an adapter layer, or accept that the integration will require rework mid-project. Without mapping this, the team builds against a moving target and discovers the break during user acceptance testing.</p>

    <h3>Credit management rollout: "All customers have credit segments"</h3>
    <p>A project to implement automatic credit checks assumes that every customer in the sales area has a credit segment in UKM_BP. The mapping reveals that customers created before 2022 were never migrated to the new credit management framework, and new customers created via a legacy CRM bypass do not receive credit segments. The assumption is false for 15 percent of the active customer base. The project must either add a data remediation step or build a fallback rule that routes non-segment customers to manual review. Without mapping this, the automatic check fails silently for a subset of orders, creating a new support ticket category.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Project charter or scope statement with stated and implied assumptions.</li>
      <li>Requirements list or <a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Briefs</a> with assumptions embedded in the text.</li>
      <li>System documentation showing current state, versions, and known limitations.</li>
      <li>Data quality reports or sample extracts representing the current state.</li>
      <li>Stakeholder interviews with people who have seen similar projects fail.</li>
      <li>Vendor contracts, API documentation, or integration roadmaps.</li>
      <li>Regulatory documents or compliance constraints with source and validity period.</li>
      <li>Previous project post-mortems or risk registers for the same domain.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What are we assuming about data quality, completeness, and timeliness?</li>
      <li>What are we assuming about system availability, performance, and version stability?</li>
      <li>What are we assuming about user knowledge, training, and willingness to change?</li>
      <li>What constraints are truly immovable: budget, timeline, regulation, technology?</li>
      <li>What is the source of each constraint: who said it is fixed and can they change it?</li>
      <li>What happens if this assumption is wrong? How much time, money, or scope is at risk?</li>
      <li>Which assumptions can be validated before the project starts, and which must be validated during?</li>
      <li>Which constraints are actually policies that could be waived with the right approval?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Brainstorm all assumptions.</strong> Gather everything the team, stakeholders, or documents say that starts with "we assume," "presumably," "usually," or "as far as we know." Do not filter yet.</li>
      <li><strong>Separate assumptions from constraints.</strong> An assumption can be proven true or false. A constraint is a limit that the project must work within. If it can be changed with a decision, it is not a constraint — it is a rule or a preference.</li>
      <li><strong>Classify assumptions by type.</strong> Use: data (quality, completeness, timeliness), system (availability, version, performance), process (workflow, ownership, handoffs), external (vendor, regulation, market), and organizational (skills, capacity, authority).</li>
      <li><strong>Assess impact if wrong.</strong> For each assumption, state what happens if it is false: delay, cost increase, scope reduction, quality failure, or cancellation. Rate impact as high, medium, or low.</li>
      <li><strong>Rate likelihood of being false.</strong> Use evidence, history, and data samples to estimate how likely the assumption is to fail. Rate as high, medium, or low.</li>
      <li><strong>Create a validation plan.</strong> For each high-impact or high-likelihood assumption, define: how to validate it, who will do it, by when, and what the pass/fail criteria are.</li>
      <li><strong>Map constraints.</strong> For each constraint, document: the type (technical, budget, regulatory, timeline), the source (who imposed it), the validity period, and the consequence of violating it.</li>
      <li><strong>Document in an Assumptions Log.</strong> One log per project. Include assumption, type, impact, likelihood, validation plan, owner, and status.</li>
      <li><strong>Review regularly.</strong> Revisit the log at sprint boundaries, milestones, or when new risks surface. Update statuses and add new assumptions as they emerge.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If an assumption has no validation plan, it is a risk — not a managed assumption.</li>
      <li>If a constraint is not documented with a source and an authority, it is not a constraint — it is a preference.</li>
      <li>If an assumption is proven false, update the requirements, scope, and estimate before proceeding.</li>
      <li>If two assumptions conflict, flag the conflict and require a stakeholder decision before the project continues.</li>
      <li>If an assumption has high impact and high likelihood of being false, validate it before the project starts. Do not defer.</li>
      <li>If a constraint is a policy that could be waived, document the waiver path and the approver.</li>
      <li>If an assumption is validated and confirmed true, move it to the "facts" section and remove it from the risk register.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Assumptions Log</strong> — One per project. Contains assumption, type, impact, likelihood, validation plan, owner, and status. See template below.</li>
      <li><strong>Constraint Map</strong> — Table of constraints with type, source, validity period, and consequence of violation.</li>
      <li><strong>Risk Register updates</strong> — Assumptions that are unvalidated or high-risk are added to the project risk register with mitigation plans.</li>
      <li><strong>Validation Plan</strong> — Scheduled activities with owners, pass/fail criteria, and due dates for high-risk assumptions.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Assumptions Log (compact)</h3>
    <pre><code>---
artifact: Assumptions Log
id: ASM-001
project: &lt;project name&gt;
date: YYYY-MM-DD
status: draft | reviewed | active
---

## Assumption
<!-- What we assume. Example: "Customer master data in the source system is complete and ready for migration." -->

## Type
<!-- data | system | process | external | organizational -->

## Impact if wrong
<!-- What happens if this assumption is false. Example: "Migration loads incomplete data, triggering incompletion blocks in S/4 and generating support tickets." -->
- Impact: &lt;description&gt;
- Severity: high | medium | low

## Likelihood of being false
<!-- Based on evidence and history. -->
- Likelihood: high | medium | low
- Evidence: &lt;data sample, incident history, or expert opinion&gt;

## Validation plan
- Method: &lt;how to validate&gt;
- Owner: &lt;who validates&gt;
- Due date: &lt;YYYY-MM-DD&gt;
- Pass criteria: &lt;what confirms the assumption is true&gt;
- Fail criteria: &lt;what confirms the assumption is false&gt;

## Status
<!-- unvalidated | validated true | validated false | obsolete -->

## Related assumptions
<!-- Links to other assumptions that interact with this one -->

## Constraint link
<!-- If this assumption is actually a constraint, link to the Constraint Map entry -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every assumption has a named type and a clear statement of what is assumed.</li>
      <li>Impact if wrong is stated in operational or financial terms, not vague language.</li>
      <li>Likelihood of being false is based on evidence, not gut feeling.</li>
      <li>Every high-impact or high-likelihood assumption has a validation plan with owner and due date.</li>
      <li>Constraints are separated from assumptions and documented with source and authority.</li>
      <li>Assumptions are reviewed at regular intervals, not just at project start.</li>
      <li>Validated false assumptions trigger an update to requirements, scope, or risk register before work continues.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Treating assumptions as facts.</strong> Consequence: the project plan is built on sand. When the assumption fails, the plan collapses and there is no contingency.</li>
      <li><strong>Not documenting the source of constraints.</strong> Consequence: the team treats a stakeholder preference as a hard limit, or challenges a regulatory constraint without knowing the authority behind it.</li>
      <li><strong>Skipping validation for "obvious" assumptions.</strong> Consequence: the most damaging failures come from assumptions that "everyone knows" are true but no one has checked.</li>
      <li><strong>Confusing assumptions with risks.</strong> Consequence: assumptions are logged but never validated, while risks are managed without understanding their root cause. The team treats symptoms instead of causes.</li>
      <li><strong>Failing to update the log when assumptions change.</strong> Consequence: the project continues based on outdated assumptions that were invalidated weeks ago. Decisions are made with stale information.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output — Generic assumptions list</h3>
    <p>A weak AI output produces a list of vague assumptions with no validation plan, no evidence, and no owner:</p>
    <blockquote>
      <p><strong>Assumptions:</strong></p>
      <ul>
        <li>The data is clean.</li>
        <li>The system will be available.</li>
        <li>Users will adopt the new process.</li>
        <li>The vendor will deliver on time.</li>
      </ul>
      <p><strong>Validation:</strong> To be confirmed.</p>
      <p><strong>Owner:</strong> Project manager.</p>
    </blockquote>
    <p><strong>Why this is weak:</strong> "Clean" is not defined. "Available" has no threshold. No evidence is cited. No validation method is stated. No due date. No impact assessment. A project manager cannot prioritize validation effort, and a stakeholder cannot assess risk from this list.</p>

    <h3>Strong output — Assumptions Log entry</h3>
    <p>A strong AI output produces a copy-paste-ready artifact with specific evidence, validation plans, and clear ownership:</p>
    <pre><code>---
artifact: Assumptions Log
id: ASM-MIG-2026-003
project: SAP ECC to S/4 Customer Master Migration
date: 2026-06-12
status: active
---

## Assumption
All customer master records in the source ECC system contain complete sales area data (sales org, distribution channel, division) required for S/4 order creation.

## Type
data

## Impact if wrong
- Impact: Incomplete customer records will trigger incompletion blocks in S/4 at order creation (VA01), generating SD support tickets and delaying revenue recognition.
- Severity: high

## Likelihood of being false
- Likelihood: high
- Evidence: Sample of 1,000 customer records from KNA1/KNVV shows 12% lack required sales area data. Historical AMS data shows 8% of blocked orders are due to missing customer master fields.

## Validation plan
- Method: Run automated completeness check on full KNVV extract for all active sales orgs. Flag records missing VSTEL, INCO1, or ZTERM.
- Owner: Data migration lead, Peter Schmidt
- Due date: 2026-06-20
- Pass criteria: &lt; 2% of active customer records have missing sales area data.
- Fail criteria: &gt; 5% of active customer records have missing sales area data.

## Status
unvalidated

## Related assumptions
- ASM-MIG-2026-004: Tax numbers in source system pass country-specific validation.
- ASM-MIG-2026-005: Customer-to-business partner mapping is complete for all accounts.

## Constraint link
- None. This is an assumption, not a constraint.
</code></pre>
    <p><strong>Why this is strong:</strong> It states the assumption with specific fields (VSTEL, INCO1, ZTERM). It cites evidence (sample of 1,000 records, historical AMS data). It assesses impact in operational terms (support tickets, revenue delay). It defines a validation method with a pass/fail threshold, a named owner, and a due date. A project manager can prioritize this, a data team can execute it, and a steering committee can understand the risk.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><em>"You are a project risk analyst. You receive a project scope, requirements, and system context. Produce an Assumptions Log and Constraint Map. For each assumption: state the specific assumption, classify the type (data, system, process, external, organizational), assess impact if wrong with evidence, rate likelihood of being false, and define a validation plan with owner, method, due date, and pass/fail criteria. For each constraint: state the limit, the source, the authority, and the consequence of violation. Do not use vague qualifiers like 'clean' or 'fast' without defining thresholds. Flag assumptions that lack evidence as high-risk."</em></p>

    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Gather all stated and implied assumptions before analysis.</strong> Read requirements, project charters, and stakeholder statements for hidden assumptions.</li>
      <li><strong>Separate assumptions from constraints.</strong> An assumption can be validated. A constraint is a fixed limit with a source and authority.</li>
      <li><strong>Assess impact and likelihood with evidence.</strong> Use data samples, incident history, or expert opinion. Do not guess.</li>
      <li><strong>Define validation plans for all high-impact or high-likelihood assumptions.</strong> Include method, owner, due date, and pass/fail criteria.</li>
      <li><strong>Produce one Assumptions Log per project.</strong> Link related assumptions. Update statuses as validation completes.</li>
      <li><strong>Do not treat stakeholder preferences as constraints.</strong> If a limit can be changed with a decision, it is a rule, not a constraint.</li>
      <li><strong>Flag validated-false assumptions as project risks.</strong> Update requirements, scope, or estimates before continuing.</li>
      <li><strong>Link to Atlas diagnostics</strong> when assumptions relate to SAP processes. For example, data migration assumptions should reference <a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for validating process assumptions.</li>
      <li><a href="/scenarios/delivery-billing-block-order-to-cash-delays/">Delivery Billing Block Order-to-Cash Delays</a> — Scenario showing assumption failures in O2C.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of assumption and constraint management practices. It is not official PMBOK, BABOK, or risk management framework documentation. It focuses on practical enterprise and SAP contexts where data quality and system stability assumptions are common failure points.</p>
    <p>Known limitations: the skill requires access to data samples, system documentation, and stakeholder expertise to validate assumptions. In environments with poor documentation or no historical data, likelihood assessment is speculative. The skill does not cover formal quantitative risk modeling or Monte Carlo simulation.</p>
  </section>
</article>
