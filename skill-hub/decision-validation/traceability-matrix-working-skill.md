---
layout: default
title: "Traceability Matrix Drafting Working Skill"
description: "Map requirements to source, design, test, and release so that every requirement can be traced from origin to verification and no requirement is orphaned."
permalink: /skill-hub/decision-validation/traceability-matrix-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/decision-validation/">Decision & Validation</a></li>
    <li aria-current="page">Traceability Matrix</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Decision & Validation</p>
  <h1>Traceability Matrix Drafting Working Skill</h1>
  <p class="lead">Map every requirement from its origin through design, test, and release so that gaps, orphans, and untested requirements are visible before they become production defects.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>A requirement that cannot be traced to a test is a requirement that may never be verified. A test that cannot be traced to a requirement is waste. This skill creates and maintains traceability matrices that link requirements to their sources, design artifacts, test scenarios, and release packages. The matrix becomes a diagnostic tool: it reveals orphan requirements with no tests, orphan tests with no requirements, and gaps where design or implementation is missing. It also provides the evidence auditors and release managers need to confirm that every approved requirement has been addressed.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Requirements are approved and need to be tracked through design, build, and test.</li>
      <li>A requirement changes mid-project and you need to know which design documents, test cases, and code modules are affected.</li>
      <li>Test planning starts and you need to measure coverage: which requirements have tests and which do not.</li>
      <li>An audit or compliance review asks for evidence that all requirements were tested before release.</li>
      <li>A release is scoped and you need to bundle only the requirements, tests, and transports that belong together.</li>
      <li>A production defect occurs and you need to trace it back to the requirement it violates.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4 upgrade: order-to-cash process changes</h3>
    <p>An upgrade project changes pricing procedures, delivery blocks, and billing routines. The traceability matrix maps each business requirement to the SAP functional design document, the configuration change in the transport request, the test scenario in the test tool, and the release package. Without the matrix, a pricing requirement is implemented but never tested because the test team did not know it changed. The transport reaches production and pricing errors appear on the first invoice run.</p>

    <h3>Integration project: e-commerce to SAP IDoc flow</h3>
    <p>A new e-commerce channel sends orders to SAP via IDoc. The matrix maps the business requirement "orders must create within 5 minutes" to the interface design document, the mapping specification, the IDoc test scenario, the monitoring alert configuration, and the go-live release. Without the matrix, the monitoring alert is built but never linked to the requirement, so when the alert fires in production, no one knows which requirement it validates or who owns the response.</p>

    <h3>Regulatory compliance: customer master data validation</h3>
    <p>A tax regulation requires that customer tax numbers be validated before invoice creation. The matrix maps the regulatory source to the validation rule in the business rules catalog, the MDG change request configuration, the test scenario for invalid tax numbers, and the audit report. Without the matrix, the audit cannot demonstrate that the requirement was tested, and the organization faces compliance penalties.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Approved requirements list with unique IDs and source references.</li>
      <li>Design documents: functional specifications, configuration guides, interface mappings, workflow definitions.</li>
      <li>Test plan or test scenario set with IDs and descriptions.</li>
      <li>Release plan or transport list showing what will be deployed and when.</li>
      <li>Source documents: stakeholder requests, regulatory texts, defect reports, change requests.</li>
      <li>Tool selection: spreadsheet, ALM tool (Jira, Azure DevOps), or simple Markdown table.</li>
      <li>Change log or version history of requirements, designs, and tests (if available).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which requirement has no design artifact? Who will create it?</li>
      <li>Which requirement has no test scenario? Is it untested or was the test never written?</li>
      <li>Which test scenario does not trace to any requirement? Is it an orphan test or a missing requirement?</li>
      <li>Which design change affects which requirements, and have the related tests been updated?</li>
      <li>Which requirements are included in the upcoming release, and do they have complete traceability chains?</li>
      <li>Which requirements were deferred, and are they excluded from the current release traceability?</li>
      <li>What is the minimum viable traceability: source → requirement → test → release, or do we need more dimensions?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>List all requirements.</strong> Create a column with requirement IDs and short descriptions. Include status: approved, deferred, or changed.</li>
      <li><strong>Identify traceability dimensions.</strong> Decide which columns you need. Minimum: Source → Requirement → Design → Test → Release. Add columns for Owner, Priority, or Compliance if needed.</li>
      <li><strong>Map requirements to sources.</strong> For each requirement, link to the stakeholder request, regulation, defect, or change request that originated it. If a requirement has no source, flag it as orphan.</li>
      <li><strong>Map requirements to design.</strong> For each requirement, link to the functional specification, configuration document, or code module that implements it. If a requirement has no design, flag it as unimplemented.</li>
      <li><strong>Map requirements to tests.</strong> For each requirement, link to the test scenario or test case that verifies it. If a requirement has no test, flag it as untested.</li>
      <li><strong>Map requirements to releases.</strong> For each requirement, link to the release package, transport request, or deployment plan that contains it. If a requirement is approved but not assigned to a release, flag it as unscheduled.</li>
      <li><strong>Identify gaps and orphans.</strong> Scan the matrix for empty cells, broken links, and mismatches. Produce a Gap Report with severity and owner.</li>
      <li><strong>Establish change control.</strong> When a requirement changes, update all downstream links. When a test is added, link it to the requirement. When a release is scoped, verify all included requirements have complete chains.</li>
      <li><strong>Maintain and review.</strong> Update the matrix within one business day of any change. Review the matrix weekly for gaps and stale entries.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a requirement has no test, flag it as untested and block release until a test is defined.</li>
      <li>If a test has no requirement, flag it as orphan: either remove the test or add the missing requirement.</li>
      <li>If a requirement changes, update all downstream links (design, test, release) before the next review.</li>
      <li>If a release excludes a requirement, document the deferral and remove the requirement from the release traceability.</li>
      <li>If a source document is updated, verify that linked requirements are still valid and update if not.</li>
      <li>If the matrix has more than seven dimensions, consider splitting into multiple matrices to avoid unreadability.</li>
      <li>If a requirement is approved but has no design or release assignment, it is not ready for build.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Traceability Matrix</strong> — Table or tool artifact linking requirements to source, design, test, and release. See template below.</li>
      <li><strong>Gap Report</strong> — List of orphan requirements, orphan tests, missing design links, and untested requirements with severity and owner.</li>
      <li><strong>Orphan Register</strong> — Running list of items that were removed from the matrix and why, for audit trail.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Traceability Matrix (Markdown compact)</h3>
    <pre><code>---
artifact: Traceability Matrix
id: TM-001
project: &lt;Project Name&gt;
dimensions: Source, Requirement, Design, Test, Release
last_updated: YYYY-MM-DD
---

| Req ID | Requirement | Source | Design Doc | Test Scenario | Release | Status | Owner |
|--------|-------------|--------|------------|---------------|---------|--------|-------|
| REQ-001 | &lt;Short description&gt; | SRC-001 | FSD-001 | TS-001 | REL-1.0 | complete | &lt;Name&gt; |
| REQ-002 | &lt;Short description&gt; | SRC-002 | — | TS-002 | REL-1.0 | missing design | &lt;Name&gt; |
| REQ-003 | &lt;Short description&gt; | — | FSD-003 | TS-003 | REL-1.0 | orphan source | &lt;Name&gt; |
| REQ-004 | &lt;Short description&gt; | SRC-004 | FSD-004 | — | REL-1.0 | untested | &lt;Name&gt; |

## Gap Report

### Untested Requirements
- REQ-004: &lt;description&gt;. Action: &lt;what to do&gt;. Owner: &lt;name&gt;. Due: &lt;date&gt;.

### Orphan Tests
- TS-005: &lt;description&gt;. No linked requirement. Action: remove or add requirement. Owner: &lt;name&gt;.

### Missing Design Links
- REQ-002: &lt;description&gt;. No design document. Action: create FSD. Owner: &lt;name&gt;. Due: &lt;date&gt;.

## Change Log
| Date | Change | Affected Req IDs | Updated By |
|------|--------|------------------|------------|
| YYYY-MM-DD | &lt;description&gt; | REQ-001, REQ-002 | &lt;Name&gt; |
</code></pre>

    <h3>Traceability Matrix (spreadsheet compact)</h3>
    <pre><code>Columns: Req ID | Requirement | Source ID | Source Type | Design Doc | Test ID | Release | Status | Owner | Gap Notes

Status values: complete | missing design | untested | orphan source | orphan test | deferred

Use conditional formatting to highlight: untested (yellow), orphan (red), complete (green).
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every approved requirement traces to at least one source document or stakeholder request.</li>
      <li>Every approved requirement traces to at least one design artifact or implementation item.</li>
      <li>Every approved requirement traces to at least one test scenario or test case.</li>
      <li>Every approved requirement traces to a release or deployment package.</li>
      <li>No test scenario exists without a linked requirement, unless it is explicitly labeled as regression or exploratory.</li>
      <li>The matrix is updated within one business day of any requirement, design, or test change.</li>
      <li>All gaps are documented in a Gap Report with severity, owner, and due date.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Creating the matrix after testing is complete.</strong> Consequence: the matrix is a backward-looking record, not a planning tool. Gaps are discovered too late to fix.</li>
      <li><strong>Not updating the matrix when requirements change.</strong> Consequence: the matrix becomes stale, tests verify outdated requirements, and release scope is unclear.</li>
      <li><strong>Adding too many dimensions.</strong> Consequence: the matrix becomes unreadable and maintenance is abandoned. Seven columns is usually the practical maximum.</li>
      <li><strong>Treating traceability as a one-time documentation task.</strong> Consequence: the matrix is accurate on day one and wrong by day ten. Traceability is a living artifact.</li>
      <li><strong>Not linking to the actual artifact IDs.</strong> Consequence: the matrix says "see FSD" but does not name the document, so no one can find it.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A sparse table with vague references and no status: "Requirements are linked to designs and tests where applicable. Most requirements have coverage. Some gaps exist in the test area. The matrix is stored in the project folder." No requirement IDs, no test IDs, no release IDs, no gap owners, no due dates.</p>
    <p><strong>Why it fails:</strong> Cannot be used for planning, auditing, or release scoping. No one can find the artifacts. No one is accountable for gaps. The matrix is a decorative document.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Traceability Matrix
id: TM-S4-O2C-2026-001
project: S/4 Order-to-Cash Enhancement
last_updated: 2026-06-12
---

| Req ID | Requirement | Source | Design Doc | Test Scenario | Release | Status | Owner |
|--------|-------------|--------|------------|---------------|---------|--------|-------|
| REQ-101 | Credit limit block at 50k EUR | CR-2026-044 | FSD-101 | TS-101, TS-102 | REL-2.3 | complete | A. Kumar |
| REQ-102 | Emergency order bypass | CR-2026-044 | FSD-102 | — | REL-2.3 | untested | A. Kumar |
| REQ-103 | Incompletion procedure for incoterms | DEF-2025-891 | FSD-103 | TS-103 | REL-2.3 | complete | M. Chen |
| REQ-104 | Delivery block for incomplete orders | DEF-2025-891 | — | TS-104 | REL-2.3 | missing design | R. Patel |

## Gap Report — 2026-06-12

### Critical
- REQ-102 (Emergency order bypass): approved but no test scenario. Blocks REL-2.3. Action: create TS-105 by 2026-06-14. Owner: A. Kumar.
- REQ-104 (Delivery block): approved but no design document. Blocks REL-2.3. Action: create FSD-104 by 2026-06-15. Owner: R. Patel.

### Major
- TS-201 (Pricing check): no linked requirement. Orphan from REL-2.2. Action: verify if still needed or remove. Owner: M. Chen. Due: 2026-06-13.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Traceability analyst for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have an approved requirements list, design documents, test scenarios, and a release plan. You need to build or update a traceability matrix.</p>
    <p><strong>Task:</strong> Create a Traceability Matrix linking requirements to source, design, test, and release. Identify gaps and orphans. Produce a Gap Report with severity and owner.</p>
    <p><strong>Output format:</strong> Markdown table with columns: Req ID, Requirement, Source, Design Doc, Test Scenario, Release, Status, Owner. Follow with a Gap Report section.</p>

    <ul>
      <li><strong>Always use actual artifact IDs.</strong> Do not write "see FSD." Write "FSD-101."</li>
      <li><strong>Flag every empty cell.</strong> An untested requirement is not "mostly covered." It is untested.</li>
      <li><strong>Update the matrix when requirements change.</strong> Do not produce a static snapshot. Include a change log.</li>
      <li><strong>Keep dimensions practical.</strong> Do not add more than seven columns. Split complex matrices by domain or release.</li>
      <li><strong>Do not invent artifacts.</strong> If a design document does not exist, flag it as missing. Do not make up an ID.</li>
      <li><strong>Link to Atlas diagnostics</strong> when requirements touch SAP processes. For example, order-to-cash requirements should reference <a href="/scenarios/delivery-billing-block-order-to-cash-delays/">Delivery Billing Block Order-to-Cash Delays</a> for process context.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a> — Use to produce the requirements list that feeds the matrix.</li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria Working Skill</a> — Use to define the test scenarios that trace to requirements.</li>
      <li><a href="/skill-hub/decision-validation/test-scenario-derivation-working-skill/">Test Scenario Derivation Working Skill</a> — Use to create the test scenarios that populate the Test column.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for linking requirements to actual process behavior and system checks.</li>
      <li><a href="/scenarios/delivery-billing-block-order-to-cash-delays/">Delivery Billing Block Order-to-Cash Delays</a> — Scenario with traceability from business pain to process touchpoints and system checks.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of traceability practices. It is not official IEEE, CMMI, or SAP documentation. It focuses on practical traceability for enterprise projects where requirements must be demonstrably tested before release.</p>
    <p>Known limitations: the skill assumes requirements have unique IDs and that design and test artifacts exist or can be created. It does not cover automated traceability extraction from code repositories or test automation tools. It does not address regulatory traceability for safety-critical systems or medical devices.</p>
  </section>
</article>
