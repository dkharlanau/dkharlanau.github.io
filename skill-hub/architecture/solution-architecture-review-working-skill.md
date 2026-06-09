---
layout: default
title: "Solution Architecture Review"
description: "Review a proposed solution design against requirements, constraints, risks, and non-functional needs before commitment."
permalink: /skill-hub/architecture/solution-architecture-review-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/architecture/">Architecture</a></li>
    <li aria-current="page">Solution Architecture Review</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Architecture</p>
  <h1>Solution Architecture Review</h1>
  <p class="lead">Review a proposed solution design against requirements, constraints, risks, and non-functional needs before commitment.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill provides a structured method for evaluating a proposed solution design before build or procurement begins. It checks whether the design satisfies known requirements, respects constraints, handles identified risks, and meets non-functional needs. The output is a review report with findings classified as blocking, major, minor, or informational, plus actionable recommendations. It prevents projects from committing to designs that contain hidden integration failures, scalability bottlenecks, or unverified assumptions.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A vendor has submitted a solution design and the project team must validate it before contract signature.</li>
      <li>An internal team has produced a high-level design for a new integration, module, or platform, and you need an independent review.</li>
      <li>A design was created six months ago and the requirements have changed; you need to revalidate it.</li>
      <li>A proof-of-concept succeeded in a sandbox and now must be reviewed for production readiness.</li>
      <li>You are the architect responsible for a design review gate in a gated project methodology.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: SAP BTP integration design review</h3>
    <p>A team proposes using SAP Integration Suite to connect S/4HANA with a third-party logistics platform. The design shows synchronous API calls for every shipment event. The review reveals that the logistics platform has a 99.5% uptime SLA while the business requires 99.9% order visibility. The synchronous design creates a single point of failure. The review recommends event-driven asynchronous messaging with a local queue and retry mechanism.</p>

    <h3>Example 2: Data warehouse platform selection</h3>
    <p>A project selects a cloud data warehouse for SAP analytics. The design focuses on query performance and storage cost. The review finds that the design omits data lineage, master data synchronization with SAP MDG, and GDPR deletion workflows. These are classified as blocking findings because they are required by compliance and cannot be retrofitted without significant rework.</p>

    <h3>Example 3: Custom Fiori app approval workflow</h3>
    <p>A development team designs a custom Fiori application for purchase order approval with mobile support. The review checks against the existing SAP S/4HANA authorization concept, Fiori launchpad configuration, and mobile device management policy. It finds that the app requires custom OData services that bypass standard approval logic, creating a maintenance and audit risk. The review recommends using standard workflow APIs with extension points instead.</p>

    <h3>Example 4: Consolidation of two CRM systems</h3>
    <p>A merger project designs a consolidation of two CRM systems into one. The review checks data migration, user access, integration with SAP SD, and historical reporting needs. It discovers that one CRM contains contractual data with 10-year retention requirements that the target CRM does not support natively. The review adds a data archiving and retrieval requirement to the design.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The solution design document, diagram set, or architecture proposal under review.</li>
      <li>Requirements brief or specification that the design claims to satisfy.</li>
      <li>Non-functional requirements (performance, availability, security, scalability, maintainability).</li>
      <li>Constraints list: budget, timeline, technology standards, compliance requirements, vendor lock-in limits.</li>
      <li>System context map or integration landscape showing what the new solution must connect to.</li>
      <li>Risk register or known issues from previous phases.</li>
      <li>Stakeholder list: who produced the design, who must approve it, who will operate it.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which requirement is not covered by this design? Which design element does not trace to a requirement?</li>
      <li>What happens if the primary component fails? Is there a failover, and has it been tested?</li>
      <li>Which integration points are new, which are reused, and which are assumed to work without change?</li>
      <li>What data volume is the design sized for, and what happens at 2x or 10x that volume?</li>
      <li>Who will operate this solution, and do they have the skills and tools to monitor and troubleshoot it?</li>
      <li>What is the rollback plan if the design fails during implementation or after go-live?</li>
      <li>Which decisions in this design are irreversible or expensive to reverse?</li>
      <li>Does the design introduce new single points of failure or new critical dependencies?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Establish the review scope.</strong> Define what is in scope (components, decisions, interfaces) and what is out of scope. Confirm the review authority: advisory, gate, or final approval.</li>
      <li><strong>Gather inputs.</strong> Collect the design, requirements, constraints, NFRs, and context maps. If any input is missing, record it as a review limitation.</li>
      <li><strong>Trace requirements to design elements.</strong> For each requirement, identify which design element satisfies it. Flag orphan requirements with no design coverage and orphan design elements with no requirement.</li>
      <li><strong>Check non-functional requirements.</strong> Verify that each NFR is addressed with a specific mechanism, not just a general statement. For example, "high availability" must become "active-passive cluster with 30-second failover."</li>
      <li><strong>Evaluate integration points.</strong> For each interface, check direction, protocol, data format, error handling, ownership, and monitoring. Reference the <a href="/skill-hub/artifact-templates/">Interface Ownership Matrix</a> template if one exists.</li>
      <li><strong>Assess risks and constraints.</strong> Check each known risk against the design. Does the design mitigate, accept, or ignore the risk? Does it violate any stated constraint?</li>
      <li><strong>Identify assumptions.</strong> List all assumptions embedded in the design (for example: "the API will be available by Q3," "users will adopt the new process immediately"). Classify each as validated, pending, or unverified.</li>
      <li><strong>Classify findings.</strong> For each issue found, assign a classification: Blocking (must resolve before proceed), Major (significant impact, needs plan), Minor (should fix, not blocking), Informational (noted for awareness).</li>
      <li><strong>Produce recommendations.</strong> For every Blocking and Major finding, provide one or more specific, actionable recommendations. Avoid vague advice like "consider alternatives."</li>
      <li><strong>Write the review report.</strong> Structure: Executive summary, Review scope, Requirements traceability, NFR assessment, Integration review, Risk and constraint check, Assumptions register, Findings with recommendations, Next steps.</li>
      <li><strong>Conduct review meeting.</strong> Present findings to the design team and stakeholders. Record agreements, disputes, and action items.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a requirement has no corresponding design element, classify as a Blocking finding unless the requirement is explicitly deferred.</li>
      <li>If a design element has no corresponding requirement, classify as a Major finding unless it is a standard platform capability that does not need project-level justification.</li>
      <li>If an NFR is stated but not measurable, require the design team to provide metrics before the review can pass.</li>
      <li>If an integration point lacks error handling or retry logic, classify as Major for external interfaces and Blocking for critical business flows.</li>
      <li>If the design depends on an unverified assumption that affects feasibility, classify as Major and require validation before proceed.</li>
      <li>If the design introduces a new single point of failure with no mitigation, classify as Blocking.</li>
      <li>If the design reuses an existing component with known technical debt, flag as Major and require a debt remediation plan.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Solution Architecture Review Report</strong> — Structured document with scope, traceability, assessments, findings, and recommendations.</li>
      <li><strong>Requirements Traceability Matrix</strong> — Table mapping each requirement to design elements, with coverage status.</li>
      <li><strong>Findings Register</strong> — Classified list of issues with severity, evidence, recommendation, and owner.</li>
      <li><strong>Assumptions Register</strong> — List of design assumptions with validation status and risk if the assumption is wrong.</li>
      <li><strong>Review Meeting Minutes</strong> — Record of presentation, disputes, agreements, and action items.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Findings Register (Markdown table)</h3>
    <pre><code>| ID | Finding | Category | Severity | Evidence | Recommendation | Owner | Due Date |
|----|---------|----------|----------|----------|----------------|-------|----------|
| SAR-001 | Synchronous API calls to logistics platform with 99.5% SLA | Integration | Blocking | Design doc v2.3, section 4.2 | Replace with event-driven messaging and local queue; define retry policy | Solution Architect | YYYY-MM-DD |
| SAR-002 | GDPR deletion workflow not addressed in data warehouse design | Compliance | Blocking | NFR-07, design doc v2.3 | Add data lifecycle management with deletion API and audit log | Data Architect | YYYY-MM-DD |
| SAR-003 | Custom OData service bypasses standard PO approval logic | Maintainability | Major | Design doc v2.3, section 5.1 | Use standard workflow APIs with BAdI extension points | ABAP Lead | YYYY-MM-DD |
| SAR-004 | Design assumes API v3 will be available by Q3; vendor roadmap unconfirmed | Assumption | Major | Vendor communication dated YYYY-MM-DD | Confirm API v3 GA date with vendor; define fallback to v2 if delayed | Project Manager | YYYY-MM-DD |
</code></pre>

    <h3>Assumptions Register</h3>
    <pre><code>| ID | Assumption | Source | Validation Status | Risk if Wrong | Mitigation |
|----|------------|--------|-------------------|---------------|------------|
| ASM-001 | Logistics platform API v3 available by Q3 | Vendor roadmap slide | Unconfirmed | Delayed integration, fallback rework | Confirm in writing; design v2 fallback | Project Manager |
| ASM-002 | 10,000 orders/day peak volume | Business forecast 2026 | Pending | Performance failure at go-live | Load test at 2x forecast before UAT | Performance Lead |
| ASM-003 | Operations team trained on new monitoring tools | HR training plan | Validated | Incident response delays | Training complete by go-live minus 4 weeks | Operations Manager |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every requirement is traced to at least one design element or explicitly marked as deferred.</li>
      <li>Every NFR has a measurable target and a specific mechanism in the design.</li>
      <li>Every integration point is checked for protocol, error handling, ownership, and monitoring.</li>
      <li>Every finding has a severity classification and a specific recommendation with an owner.</li>
      <li>All assumptions are listed and at least one unverified assumption is flagged as a risk.</li>
      <li>The review report has been shared with the design team before the review meeting.</li>
      <li>Review meeting minutes record all disputes and whether they were resolved or escalated.</li>
      <li>No Blocking finding remains unresolved without an explicit management decision to accept the risk.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Reviewing the design without the requirements. <strong>Consequence:</strong> The review becomes an opinion on aesthetics rather than a validation of fitness for purpose.</li>
      <li><strong>Mistake:</strong> Classifying everything as Major because the reviewer is uncertain. <strong>Consequence:</strong> The design team loses trust in the review process and ignores legitimate findings.</li>
      <li><strong>Mistake:</strong> Focusing only on functional coverage and ignoring NFRs. <strong>Consequence:</strong> The solution works in demo but fails under production load or compliance audit.</li>
      <li><strong>Mistake:</strong> Accepting vendor claims without independent verification. <strong>Consequence:</strong> The design assumes capabilities that do not exist, and the project discovers this too late.</li>
      <li><strong>Mistake:</strong> Producing a report but not conducting a review meeting. <strong>Consequence:</strong> Disputes and misunderstandings are not surfaced, and the design team proceeds with unchallenged flaws.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ol>
      <li><strong>Request all inputs before reviewing.</strong> Do not review a design without access to requirements, constraints, and NFRs. If inputs are missing, state what is missing and how it limits the review.</li>
      <li><strong>Trace requirements explicitly.</strong> Produce a Requirements Traceability Matrix as a Markdown table. Do not claim coverage without citing specific design sections or elements.</li>
      <li><strong>Classify findings rigorously.</strong> Use the four severity levels. Provide evidence for every finding. A finding without evidence is an opinion.</li>
      <li><strong>Make recommendations actionable.</strong> Every recommendation must name a specific action, a responsible role, and a target outcome. Avoid generic advice.</li>
      <li><strong>Surface assumptions.</strong> Extract assumptions from the design text and list them in the Assumptions Register. Flag unverified assumptions that affect feasibility or risk.</li>
      <li><strong>Do not invent requirements.</strong> If the design appears to miss something the agent considers important, flag it as a question or observation, not as a Blocking finding, unless it violates an explicit stated requirement.</li>
      <li><strong>Link to Atlas diagnostics.</strong> If integration or data architecture issues are found, reference <a href="/atlas/concepts/api-contracts/">API Contracts</a>, <a href="/atlas/concepts/data-contracts/">Data Contracts</a>, or <a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> for deeper context.</li>
    </ol>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/non-functional-requirements-working-skill/">Non-Functional Requirements</a> — Define the measurable quality attributes the review checks against.</li>
      <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a> — Capture the significant choices made during or after the review.</li>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a> — Define the boundaries and dependencies the review evaluates.</li>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Deep-dive skill for reviewing API-centric integration designs.</li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a> — Assess how design changes affect existing systems and processes.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/api-contracts/">API Contracts</a> — Diagnostic context for reviewing API integration designs.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — How data agreements constrain solution design.</li>
      <li><a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> — Patterns for asynchronous integration reviewed in solution designs.</li>
      <li><a href="/atlas/concepts/sap-clean-core-strategy/">SAP Clean Core Strategy</a> — How clean core principles constrain extension and customization designs.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of solution architecture review practice. It is not an official SAP, TOGAF, or IEEE review standard. It focuses on the practical subset used during enterprise and SAP project design gates. It does not cover detailed code review, security penetration testing, or infrastructure capacity planning. Use it as a structured review method for design documents and proposals, not as a substitute for specialized technical audits.</p>
  </section>
</article>
