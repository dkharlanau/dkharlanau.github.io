---
layout: default
title: "Requirements Review Checklist Working Skill"
description: "Review requirements for completeness, consistency, testability, and feasibility before they are approved for implementation."
permalink: /skill-hub/decision-validation/requirements-review-checklist-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/decision-validation/">Decision & Validation</a></li>
    <li aria-current="page">Requirements Review Checklist</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Decision & Validation</p>
  <h1>Requirements Review Checklist Working Skill</h1>
  <p class="lead">Catch gaps, contradictions, and untestable requirements before they enter implementation, so that rework and production failures are prevented at the source.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Requirements that reach development with ambiguities or missing acceptance criteria become expensive defects later. This skill provides a structured checklist-based review process that reads drafted requirements, checks them against SMART criteria, verifies traceability to business sources, finds missing acceptance criteria, checks consistency with business rules, assesses technical feasibility, and documents review findings in a format that authors can act on. This is a gatekeeping activity: it happens <strong>after</strong> elicitation and <strong>before</strong> approval, not during discovery.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A requirements document is drafted and needs formal review before approval for implementation.</li>
      <li>A change request is proposed and the scope, impact, or testability is unclear.</li>
      <li>A user story is written but has no acceptance criteria, no owner, or no data source defined.</li>
      <li>Requirements from multiple stakeholders contradict each other or overlap.</li>
      <li>A previous requirement caused rework because it was ambiguous about system behavior or data needs.</li>
      <li>An audit or governance process requires evidence that requirements were reviewed before build.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4 sales order incompletion procedure</h3>
    <p>A requirement states: "The system must block incomplete sales orders." On review, the requirement lacks: which fields trigger the block (customer reference, delivery date, incoterms), which order types are in scope, what "incomplete" means in terms of field population, and who receives the alert. Without review, developers build a generic block that either over-blocks standard orders or under-blocks rush orders, causing order entry delays or delivery failures.</p>

    <h3>Integration requirement: IDoc error handling</h3>
    <p>A requirement states: "IDoc errors must be handled automatically." On review, the requirement is missing: error types that trigger automatic retry versus manual intervention, retry count and interval, notification recipients, monitoring dashboard expectations, and SLA for resolution. Without review, operations receives a black box that retries indefinitely on data errors, flooding the queue with invalid IDocs.</p>

    <h3>Master data governance: business partner replication</h3>
    <p>A requirement states: "Business partner changes must replicate to all downstream systems in real time." On review, the requirement contradicts existing batch replication windows, assumes all systems can receive real-time events, omits conflict resolution rules for simultaneous updates, and has no acceptance criteria for latency measurement. Without review, the project launches a replication architecture that fails during peak hours because downstream systems cannot handle the event volume.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Draft requirements document, user story, or change request with numbered requirement statements.</li>
      <li>Business rules catalog or documented decision logic that governs the process area.</li>
      <li>System documentation showing current behavior, available fields, and transaction codes involved.</li>
      <li>Previous review findings or post-implementation defect reports from similar requirements (if available).</li>
      <li>Stakeholder contact list with requirement owners and technical reviewers identified.</li>
      <li>Non-functional requirements: performance, availability, security, compliance constraints.</li>
      <li>Test environment summary showing what data, systems, and tools are available for verification.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which requirement statements lack acceptance criteria, and what must be added?</li>
      <li>Which requirements contradict each other, existing business rules, or current system behavior?</li>
      <li>Which requirements cannot be tested with existing data, tools, or environments?</li>
      <li>Which requirements assume a system capability that does not exist?</li>
      <li>Which requirements are missing non-functional criteria: performance, availability, security, compliance?</li>
      <li>Which requirements have no traceable source: who asked for this, and what business outcome does it serve?</li>
      <li>Which requirements use vague terms like "fast," "easy," or "user-friendly" that prevent verification?</li>
      <li>What existing behavior must remain unchanged, and is that stated explicitly?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the requirement statement.</strong> Read each requirement in isolation. Note its ID, author, and date. If it is longer than three sentences, flag it for decomposition.</li>
      <li><strong>Check SMART criteria.</strong> For each requirement, verify it is Specific, Measurable, Achievable, Relevant, and Time-bound. If any criterion is missing, document the gap.</li>
      <li><strong>Verify traceability to source.</strong> Confirm each requirement links to a business need, stakeholder request, regulation, or defect. If no source exists, flag the requirement as orphan.</li>
      <li><strong>Identify missing acceptance criteria.</strong> Check that every requirement has at least one verifiable pass/fail criterion. If criteria are missing, note what must be added.</li>
      <li><strong>Check consistency with business rules.</strong> Compare the requirement against documented business rules, process maps, and regulatory constraints. Flag contradictions.</li>
      <li><strong>Assess technical feasibility.</strong> Verify the requirement can be met with current system capabilities, data, and resources. If feasibility is unclear, request a technical review.</li>
      <li><strong>Check for ambiguity.</strong> Replace vague terms with measurable thresholds. Flag words like "appropriate," "sufficient," or "as needed."</li>
      <li><strong>Document findings in a Review Report.</strong> For each requirement, list findings by severity: critical (blocks approval), major (requires revision), minor (suggested improvement). Link to the template below.</li>
      <li><strong>Route for revision.</strong> Return the report to the requirement author with clear revision instructions and a deadline. Re-review after revision.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a requirement has no acceptance criteria, mark it incomplete and block approval until criteria are added.</li>
      <li>If two requirements contradict each other, escalate to the business owner with both statements and the conflict description.</li>
      <li>If a requirement is not testable with current data or tools, flag a test environment gap before approval.</li>
      <li>If a requirement assumes a system capability that does not exist, require a feasibility assessment or scope change.</li>
      <li>If a requirement uses vague language, reject it and request a rewrite with measurable thresholds.</li>
      <li>If a requirement duplicates an existing requirement, merge or remove the duplicate and update traceability.</li>
      <li>If non-functional criteria are missing, require them as a condition of approval.</li>
      <li>If a requirement changes existing behavior without stating what must remain unchanged, flag the omission.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Requirements Review Report</strong> — Per requirement document. Contains findings classified by severity, with specific revision instructions and references to source documents.</li>
      <li><strong>Defect Register</strong> — List of requirements that fail review, with reason, owner, and resolution deadline.</li>
      <li><strong>Revision Plan</strong> — Ordered list of required changes, priority, and re-review schedule.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Requirements Review Checklist (compact)</h3>
    <pre><code>---
artifact: Requirements Review Report
id: RR-001
requirement_doc: Link to requirement document
reviewer: Name
review_date: YYYY-MM-DD
status: draft | reviewed | approved
---

## Requirement ID: &lt;REQ-001&gt;

### SMART Check
- [ ] Specific: The requirement names a system, process, or field.
- [ ] Measurable: The requirement includes a metric or threshold.
- [ ] Achievable: The requirement can be met with current capabilities.
- [ ] Relevant: The requirement links to a business outcome or source.
- [ ] Time-bound: The requirement has a deadline or maintenance window.

### Acceptance Criteria Check
- [ ] At least one verifiable pass/fail criterion exists.
- [ ] Normal case is specified.
- [ ] Boundary case is specified.
- [ ] Error case is specified.

### Consistency Check
- [ ] No contradiction with business rules.
- [ ] No contradiction with existing system behavior.
- [ ] No duplication with other requirements.

### Feasibility Check
- [ ] Required data exists in the system.
- [ ] Required transactions or APIs are available.
- [ ] Test environment can verify the requirement.

### Findings
| Severity | Finding | Revision Required | Owner |
|----------|---------|-------------------|-------|
| critical | &lt;description&gt; | &lt;yes/no&gt; | &lt;name&gt; |
| major | &lt;description&gt; | &lt;yes/no&gt; | &lt;name&gt; |
| minor | &lt;description&gt; | &lt;yes/no&gt; | &lt;name&gt; |

### Sign-off
- Reviewer: _______________
- Date: _______________
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every requirement has at least one acceptance criterion.</li>
      <li>All contradictions with business rules or other requirements are flagged and assigned.</li>
      <li>Every requirement is traceable to a source document, stakeholder, or defect.</li>
      <li>No requirement contains vague terms without measurable thresholds.</li>
      <li>Non-functional criteria (performance, availability, security, compliance) are checked for every requirement.</li>
      <li>All findings are classified by severity and have an assigned owner.</li>
      <li>The review report is returned to the author with clear revision instructions.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Treating review as elicitation.</strong> Consequence: the review never ends because requirements are still being discovered. Reviews must be gatekeeping, not discovery sessions.</li>
      <li><strong>Approving vague requirements with a comment to "clarify later."</strong> Consequence: ambiguity enters implementation, causing rework when the clarification contradicts what was built.</li>
      <li><strong>Checking only functional requirements and ignoring non-functional criteria.</strong> Consequence: the solution passes functional tests but fails under load, lacks audit trails, or violates compliance.</li>
      <li><strong>Reviewing without access to business rules or system documentation.</strong> Consequence: the reviewer cannot detect contradictions or feasibility issues, making the review a grammar check instead of a quality gate.</li>
      <li><strong>Not documenting findings in a structured format the author can act on.</strong> Consequence: the author receives vague feedback like "make it clearer" and produces another unclear revision.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A generic summary with no actionable findings: "The requirements document looks mostly complete. A few items need clarification. Please review acceptance criteria and make sure everything is testable. Some requirements may conflict with existing rules, so check with the business owner. Overall, this is a good start but needs refinement before approval."</p>
    <p><strong>Why it fails:</strong> No specific requirement is named. No finding is classified by severity. The author has no clear instructions and no deadline. The review is indistinguishable from a polite rejection.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Requirements Review Report
id: RR-2026-044
requirement_doc: REQ-S4-O2C-2026-044
reviewer: M. Chen
review_date: 2026-06-12
status: reviewed — revisions required
---

## Critical Findings (blocks approval)

### REQ-004: "Block incomplete sales orders"
- Missing: which fields trigger the block (customer reference, delivery date, incoterms).
- Missing: which order types are in scope (standard, rush, consignment).
- Missing: acceptance criteria for alert routing and escalation.
- Action: Decompose into 3 requirements. Add acceptance criteria for each field and order type. Assign to J. Schmidt by 2026-06-15.

### REQ-007: "IDoc errors must be handled automatically"
- Vague: "automatically" is not defined. No retry count, no interval, no error classification.
- Contradiction: assumes real-time processing but current system uses batch every 4 hours.
- Action: Rewrite with explicit error classification and retry rules. Request feasibility review from integration team. Assign to R. Patel by 2026-06-16.

## Major Findings (requires revision)

### REQ-002: "Migrate all active customers"
- Missing non-functional criteria: expected migration window, rollback procedure, data validation threshold.
- Action: Add performance and availability criteria. Reference atlas/diagnostics/sap-process-audit for validation checklist.

## Minor Findings (suggested improvements)

### REQ-001: "Enable credit limit check"
- Acceptable as written. Suggest adding edge case for emergency orders under 1,000 EUR.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Requirements reviewer for an SAP enterprise project.</p>
    <p><strong>Context:</strong> You have a drafted requirements document with numbered requirements. You also have business rules, system documentation, and non-functional constraints.</p>
    <p><strong>Task:</strong> Review each requirement against the SMART criteria, check for acceptance criteria, verify consistency with business rules, assess feasibility, and produce a Requirements Review Report with classified findings.</p>
    <p><strong>Output format:</strong> Structured report with critical/major/minor findings, each containing: requirement ID, specific finding, reason, and clear revision instruction with owner and deadline.</p>

    <ul>
      <li><strong>Never approve a requirement that lacks acceptance criteria.</strong> Flag it as incomplete with specific guidance on what criteria are missing.</li>
      <li><strong>Use the template above.</strong> Produce structured output that the requirement author can act on without asking for clarification.</li>
      <li><strong>Separate facts from assumptions.</strong> If feasibility is unclear, state the assumption and recommend a technical review rather than guessing.</li>
      <li><strong>Check for contradictions.</strong> Compare requirements against each other and against documented business rules. Escalate conflicts.</li>
      <li><strong>Do not rewrite requirements yourself.</strong> Identify the gap and instruct the author to revise. The author owns the requirement, not the reviewer.</li>
      <li><strong>Do not skip non-functional criteria.</strong> Performance, availability, security, and compliance must be checked for every requirement.</li>
      <li><strong>Link to Atlas diagnostics</strong> when requirements touch SAP processes. For example, incompletion procedure requirements should reference <a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a> — Use before this skill; review happens after elicitation is complete.</li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria Working Skill</a> — Use to add the missing acceptance criteria that review discovers.</li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery Working Skill</a> — Use to obtain the business rules catalog needed for consistency checks.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for verifying that requirements align with actual process behavior.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Validation context for completeness requirements in order-to-cash processes.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of requirements review practices. It is not official BABOK, IIBA, or SAP documentation. It focuses on enterprise and SAP contexts where requirements must be verifiable by business owners and traceable to system behavior.</p>
    <p>Known limitations: the skill assumes a requirements document exists and that business rules are documented. It does not cover elicitation techniques, stakeholder negotiation, or change control processes. It does not address agile-specific review ceremonies such as backlog refinement or sprint planning.</p>
  </section>
</article>
