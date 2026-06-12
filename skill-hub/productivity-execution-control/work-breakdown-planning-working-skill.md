---
layout: default
title: "Work Breakdown Planning Working Skill"
description: "Decompose a project or phase into work packages with clear boundaries, dependencies, and deliverables so the team can estimate, assign, and execute without overlap or gaps."
permalink: /skill-hub/productivity-execution-control/work-breakdown-planning-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/productivity-execution-control/">Productivity and Execution Control</a></li>
    <li aria-current="page">Work Breakdown Planning</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Productivity and Execution Control</p>
  <h1>Work Breakdown Planning Working Skill</h1>
  <p class="lead">Decompose a project or phase into discrete work packages with defined boundaries, dependencies, and deliverables so the team can estimate effort, assign ownership, and execute without overlap or gaps.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Large projects fail when work is described in paragraphs instead of packages. This skill converts a project charter, scope statement, or phase objective into a Work Breakdown Structure (WBS): a hierarchical set of work packages that are mutually exclusive, collectively exhaustive, and small enough to estimate and assign. Each work package has a clear boundary statement, a deliverable, a dependency list, and an owner. The WBS becomes the foundation for scheduling, resource allocation, risk identification, and status tracking. Without it, teams duplicate effort, miss dependencies, and discover gaps when it is too late to recover.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project or phase is starting and the team needs a shared map of what must be built, configured, tested, or delivered.</li>
      <li>A scope statement exists but no one can answer "what exactly are we doing this week?"</li>
      <li>Multiple teams or vendors are involved and the boundary between their work is unclear.</li>
      <li>Estimates are requested but the work is too coarse to estimate reliably.</li>
      <li>A workstream has been running for weeks and progress reporting is still vague.</li>
      <li>An AI agent is planning a delivery and needs a structured decomposition to avoid hallucinating tasks.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4HANA migration: missing cutover work packages</h3>
    <p>A project plan lists "data migration" as a single task. When the team starts work, they discover that data migration includes extraction, cleansing, validation, load, reconciliation, and rollback preparation. None of these are planned separately. The extraction team waits for cleansing rules. The validation team assumes the load team will handle errors. The cutover plan has no time allocated for reconciliation. A proper WBS would have decomposed data migration into six work packages with handoff criteria between each.</p>

    <h3>Integration project: overlapping ownership between middleware and SAP teams</h3>
    <p>A project to build an API between SAP and a third-party logistics system lists "integration build" as one work package. Both the middleware team and the SAP team claim it. Neither owns error handling, monitoring, or retry logic. The result is an API that works in the happy path but fails in production with no owner. A proper WBS would have separated interface specification, middleware development, SAP mapping, error handling, and monitoring into distinct packages with explicit owners.</p>

    <h3>Operational improvement: vague "process optimization" task</h3>
    <p>An AMS improvement initiative lists "optimize order-to-cash process" as a three-week task. The consultant spends two weeks trying to understand what "optimize" means. A WBS would have decomposed this into: current-state mapping, bottleneck identification, root cause analysis, solution design, configuration change, testing, and documentation. Each package has a deliverable and a stop criterion. The team knows when each piece is done and what comes next.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Project charter, scope statement, or phase objective with approved boundaries.</li>
      <li>Stakeholder list showing who owns decisions, who provides input, and who receives output.</li>
      <li>Existing system or process documentation that describes the current state.</li>
      <li>Constraints: budget, timeline, resource availability, regulatory or compliance requirements.</li>
      <li>Assumption log capturing what the team is taking as given.</li>
      <li>Dependency list: external systems, teams, approvals, or data that the project needs.</li>
      <li>Risk register or known issues that may affect work sequencing (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the smallest deliverable that, if completed, proves tangible progress?</li>
      <li>Which work packages can be done in parallel, and which must be done in sequence?</li>
      <li>What is the handoff criteria between this package and the next one?</li>
      <li>Who is the single owner accountable for the quality and completion of this package?</li>
      <li>What would happen if this work package were removed from scope?</li>
      <li>What external dependency could block this package, and when must that dependency be ready?</li>
      <li>Can this package be estimated in hours or days, or is it still too large to estimate?</li>
      <li>What artifact or evidence proves this package is complete?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Confirm the scope boundary.</strong> Read the project charter or scope statement. Identify what is in scope and what is out of scope. If the boundary is unclear, stop and clarify it before decomposing.</li>
      <li><strong>Define the top-level deliverables.</strong> List the major outcomes the project must produce. For an SAP project, these might be: configuration, data migration, integration, testing, training, and cutover. Each outcome becomes a level-one branch.</li>
      <li><strong>Decompose each outcome into work packages.</strong> Break each branch down until every package is small enough to estimate, assign, and complete within one reporting period. A rule of thumb: a work package should be 4–40 hours for a single owner. Stop decomposing when you reach that threshold.</li>
      <li><strong>Define the boundary statement for each package.</strong> Write one sentence that says what is included and what is excluded. Example: "This package includes the RFC destination configuration for the e-commerce interface. It excludes the middleware endpoint configuration, which is in package INT-002."</li>
      <li><strong>Define the deliverable for each package.</strong> Name the artifact or evidence that proves completion. Example: "Updated RFC destination in SM59 with successful connection test log."</li>
      <li><strong>Map dependencies.</strong> For each package, list which other packages must be complete before it starts, and which external inputs or approvals it needs. Use a dependency matrix or network diagram if the project is complex.</li>
      <li><strong>Assign ownership.</strong> Name one person who is accountable for each package. If no single owner exists, split the package or elevate the ownership decision before proceeding.</li>
      <li><strong>Validate mutual exclusivity and collective exhaustiveness.</strong> Check that no two packages overlap and that no required work is missing. Walk through the WBS with the team and ask: "Is there any work in this project that does not fit into one of these packages?" and "Is there any package that duplicates another?"</li>
      <li><strong>Document the WBS.</strong> Use the template below. Include package ID, name, boundary, deliverable, owner, estimated effort, dependencies, and status.</li>
      <li><strong>Baseline and review.</strong> Freeze the WBS at the start of the phase. Review it weekly. If scope changes, add or remove packages with a change log entry, not by silently editing the WBS.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a work package cannot be assigned to a single owner, split it or escalate the ownership gap before proceeding.</li>
      <li>If a work package is larger than 40 hours, decompose it further unless it is a single well-understood repeatable task.</li>
      <li>If two packages share the same deliverable, merge them or redefine the boundary so each has a unique output.</li>
      <li>If a package has no external dependencies, flag it as a candidate for early execution to build momentum.</li>
      <li>If a package depends on an external team with no committed date, place it late in the sequence and create a risk entry.</li>
      <li>If scope changes, update the WBS with a change log entry; do not silently edit the baseline.</li>
      <li>If a package has no clear completion criteria, define the deliverable before the package is approved for execution.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Work Breakdown Structure</strong> — Hierarchical list of work packages with IDs, names, boundaries, deliverables, owners, effort estimates, dependencies, and status. See template below.</li>
      <li><strong>Dependency Matrix</strong> — Table showing package-to-package and package-to-external dependencies with required dates.</li>
      <li><strong>Change Log</strong> — Record of additions, removals, and modifications to the WBS after baseline.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Work Breakdown Structure (compact)</h3>
    <pre><code>---
artifact: Work Breakdown Structure
project: &lt;project name&gt;
phase: &lt;phase name&gt;
baseline_date: YYYY-MM-DD
status: draft | baseline | revised
---

## 1.0 &lt;Outcome 1&gt;
### 1.1 &lt;Package name&gt;
- ID: WP-001
- Boundary: &lt;What is included and excluded&gt;
- Deliverable: &lt;Artifact or evidence that proves completion&gt;
- Owner: &lt;Name&gt;
- Effort: &lt;hours or days&gt;
- Dependencies: &lt;WP-XXX, external item&gt;
- Status: not started | in progress | complete | blocked

### 1.2 &lt;Package name&gt;
- ID: WP-002
- Boundary: &lt;What is included and excluded&gt;
- Deliverable: &lt;Artifact or evidence that proves completion&gt;
- Owner: &lt;Name&gt;
- Effort: &lt;hours or days&gt;
- Dependencies: &lt;WP-XXX, external item&gt;
- Status: not started | in progress | complete | blocked

## 2.0 &lt;Outcome 2&gt;
### 2.1 &lt;Package name&gt;
- ID: WP-003
- Boundary: &lt;What is included and excluded&gt;
- Deliverable: &lt;Artifact or evidence that proves completion&gt;
- Owner: &lt;Name&gt;
- Effort: &lt;hours or days&gt;
- Dependencies: &lt;WP-XXX, external item&gt;
- Status: not started | in progress | complete | blocked

## Change log
| Date | Change | Reason | Approved by |
|------|--------|--------|-------------|
| YYYY-MM-DD | &lt;description&gt; | &lt;reason&gt; | &lt;name&gt; |
</code></pre>

    <h3>Dependency Matrix (compact)</h3>
    <pre><code>| Package ID | Depends on | Type | Required by | Source | Risk level |
|------------|------------|------|-------------|--------|------------|
| WP-003 | WP-001 | internal | 2026-07-15 | team | low |
| WP-005 | vendor API spec | external | 2026-07-20 | vendor | high |
| WP-007 | security approval | external | 2026-07-10 | security | medium |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every approved scope item is covered by at least one work package.</li>
      <li>No two work packages overlap in deliverable or boundary.</li>
      <li>Every work package has a single named owner.</li>
      <li>Every work package has a defined deliverable that proves completion.</li>
      <li>Every work package is small enough to estimate and complete within one reporting period.</li>
      <li>Dependencies are identified for every package that is not a pure starting point.</li>
      <li>External dependencies have a required-by date and a source.</li>
      <li>The WBS has been validated with the team for completeness and exclusivity.</li>
      <li>Changes after baseline are recorded in the change log with a reason and approver.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Decomposing by organizational chart instead of deliverable.</strong> Consequence: work packages follow team boundaries rather than logical outcomes, creating handoff gaps and integration failures at the end of the project.</li>
      <li><strong>Stopping at the activity level instead of the deliverable level.</strong> Consequence: the WBS lists "meetings" and "analysis" instead of "updated RFC destination" or "validated customer master extract." Progress is unmeasurable.</li>
      <li><strong>Assigning a package to a group instead of a person.</strong> Consequence: no one is accountable. When the package is delayed, everyone assumes someone else is handling it.</li>
      <li><strong>Ignoring dependencies until execution starts.</strong> Consequence: teams wait idle for external inputs, or work proceeds on assumptions that are later invalidated, requiring rework.</li>
      <li><strong>Editing the WBS silently when scope changes.</strong> Consequence: the baseline is lost, the change log is empty, and no one can explain why the project grew or what was removed.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A vague bullet list of tasks with no hierarchy: "Plan the project. Do the analysis. Build the integration. Test everything. Go live." No owners, no boundaries, no deliverables, no dependencies. The list is indistinguishable from a project name and provides no guidance for estimation, assignment, or tracking.</p>
    <p><strong>Why it fails:</strong> The team cannot estimate effort because the units are too large. They cannot assign work because no one owns a specific deliverable. They cannot track progress because "analysis" is either 0% or 100% with no intermediate evidence. The project drifts until a deadline forces panic.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Work Breakdown Structure
project: S/4HANA O2C Process Improvement — Phase 1
phase: Configuration and Testing
baseline_date: 2026-06-12
status: baseline
---

## 1.0 Configuration
### 1.1 Credit management setup
- ID: WP-101
- Boundary: Includes credit limit rules, risk class assignment, and VKM1 blocking logic. Excludes customer master data migration.
- Deliverable: Updated credit management config in S/4 with test customer C-10001 blocked at 50,000 EUR.
- Owner: Maria Chen
- Effort: 3 days
- Dependencies: None
- Status: in progress

### 1.2 Incompletion procedure mapping
- ID: WP-102
- Boundary: Includes incompletion procedure assignment for sales order header and item. Excludes partner determination changes.
- Deliverable: Incompletion procedure ZO2C-01 assigned and tested in VA01 with log.
- Owner: Dmitri Volkov
- Effort: 2 days
- Dependencies: WP-101 (credit blocking must be stable first)
- Status: not started

## 2.0 Data Preparation
### 2.1 Customer master validation
- ID: WP-201
- Boundary: Includes validation of 500 active customer records for credit limit and payment terms. Excludes vendor master.
- Deliverable: Validation report with error list and correction instructions.
- Owner: Sarah Okafor
- Effort: 4 days
- Dependencies: None
- Status: not started

## 3.0 Testing
### 3.1 Integration test — credit block to release
- ID: WP-301
- Boundary: Includes end-to-end test from order creation through credit block to manual release. Excludes automated regression.
- Deliverable: Test log with pass/fail per scenario and defect list.
- Owner: Maria Chen
- Effort: 3 days
- Dependencies: WP-101, WP-102
- Status: not started

## Change log
| Date | Change | Reason | Approved by |
|------|--------|--------|-------------|
| — | — | — | — |
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Work breakdown planner for an enterprise project.</p>
    <p><strong>Context:</strong> You have a project charter or scope statement with approved boundaries. You need to create a Work Breakdown Structure that the team can use for estimation, assignment, and tracking.</p>
    <p><strong>Task:</strong> Decompose the scope into outcomes, then into work packages with boundaries, deliverables, owners, effort estimates, and dependencies. Produce a WBS document and a dependency matrix.</p>
    <p><strong>Output format:</strong> Structured Work Breakdown Structure per the template, followed by a dependency matrix table.</p>

    <ul>
      <li><strong>Never decompose without an approved scope boundary.</strong> If the scope is unclear, stop and request clarification before creating packages.</li>
      <li><strong>Always decompose to the deliverable level, not the activity level.</strong> A work package is defined by what is produced, not by what is done.</li>
      <li><strong>Every package must have a single owner.</strong> If ownership is shared, split the package or escalate.</li>
      <li><strong>Every package must have a completion criterion.</strong> Define the artifact or evidence that proves it is done.</li>
      <li><strong>Map dependencies explicitly.</strong> Internal dependencies link to other packages. External dependencies name the source and required-by date.</li>
      <li><strong>Do not invent scope, owners, or estimates.</strong> Use the inputs provided. If information is missing, flag the gap rather than guessing.</li>
      <li><strong>Validate mutual exclusivity and collective exhaustiveness.</strong> Check that no work is duplicated and no required work is missing.</li>
      <li><strong>Link to Atlas diagnostics</strong> when work packages touch SAP configuration. For example, credit management setup should reference <a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/productivity-execution-control/task-clarification-working-skill/">Task Clarification Working Skill</a> — Use after decomposition to make each work package actionable.</li>
      <li><a href="/skill-hub/productivity-execution-control/priority-triage-working-skill/">Priority Triage Working Skill</a> — Use to sequence work packages when capacity is limited.</li>
      <li><a href="/skill-hub/productivity-execution-control/scope-creep-detection-working-skill/">Scope Creep Detection Working Skill</a> — Use to guard the WBS boundary against unplanned expansion.</li>
      <li><a href="/skill-hub/business-analysis/scope-boundary-definition-working-skill/">Scope Boundary Definition Working Skill</a> — Use to define the scope boundary before decomposition begins.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for decomposing process improvement work.</li>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a> — How work breakdown feeds into operational knowledge capture.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of work breakdown practices. It is not official PMP, WBS dictionary, or SAP methodology. It focuses on practical decomposition for enterprise projects where packages must be small enough to estimate and track.</p>
    <p>Known limitations: the skill assumes a scope boundary exists. It does not cover earned value management, critical path calculation, or agile backlog breakdown. It treats the WBS as a planning and tracking artifact, not a financial accounting structure. Effort estimates are rough sizing, not detailed bottom-up estimates. For projects with heavy regulatory or safety requirements, additional decomposition standards may apply.</p>
  </section>
</article>
