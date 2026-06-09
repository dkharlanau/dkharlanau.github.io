---
layout: default
title: "Gap Analysis Working Skill"
description: "Compare what exists today against what is required, classify the difference, and produce a closure plan with effort and ownership."
permalink: /skill-hub/business-analysis/gap-analysis-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Gap Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Gap Analysis Working Skill</h1>
  <p class="lead">Find the space between what you have and what you need, classify it, and build a plan to close it with known effort and clear ownership.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Projects fail when they assume the current state is "mostly fine" and the target state is "well understood." This skill forces a structured comparison: what exists today with evidence, what is required with source, and what is missing with classification. The output is a Gap Analysis Note and Gap Register that tell decision-makers exactly what to build, buy, configure, or train — and who must do it.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project scoping phase needs to move from "we need a new system" to "we need these 17 specific capabilities."</li>
      <li>A post-merger integration must reconcile two different processes, data models, or system landscapes.</li>
      <li>A regulatory compliance assessment asks whether current controls meet new requirements.</li>
      <li>A system replacement evaluation needs to know which current customizations are essential and which are obsolete.</li>
      <li>A process redesign starts and no one has documented what the current process actually produces.</li>
      <li>A data governance maturity assessment shows the organization is at level 1 and needs to reach level 3.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4 migration: customizations vs clean core</h3>
    <p>An organization plans to migrate from SAP ECC to S/4HANA. The target state is "clean core." The gap analysis must compare: current custom transactions, user exits, modified tables, and Z-programs against standard S/4 functionality. Gaps are classified as: retire (standard covers it), refactor (custom still needed but must be compliant), or replace (custom must become extension). Without this classification, the migration either carries dead code or breaks critical processes.</p>

    <h3>New VAT reporting requirement</h3>
    <p>A new regulation requires additional fields on every invoice for VAT reporting. The gap analysis compares current invoice structures (header fields, line item fields, tax calculation logic) against the regulatory mandatory fields. Gaps are classified as: missing field, incomplete logic, or ungoverned data source. The closure plan identifies which fields need to be added to the billing document, which tax procedures need updating, and which master data fields need validation.</p>

    <h3>Integration with new e-commerce platform</h3>
    <p>A retailer wants to connect a new e-commerce platform to SAP. The gap analysis compares current API capabilities (order creation, stock check, pricing, customer lookup) against required volume and response times. Gaps are classified as: missing endpoint, insufficient throughput, or missing error handling. The closure plan identifies whether to extend existing APIs, build new middleware, or reconfigure SAP.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Current state documentation, system configuration exports, or <a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Notes</a>.</li>
      <li>Target state requirements with a clear source: regulation, project scope, best practice, or stakeholder decision.</li>
      <li>System configuration exports or screenshots showing current settings.</li>
      <li>Stakeholder interviews confirming current state and target state.</li>
      <li>Regulatory documents or compliance frameworks (if applicable).</li>
      <li>Previous gap analyses or audit reports for the same area.</li>
      <li>Effort estimation guidelines or historical data from similar closures.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What exists today that must stop, and what is missing that must be built?</li>
      <li>Which gaps are blocking progress and which are cosmetic or nice-to-have?</li>
      <li>Who owns the current state, and who will own the target state?</li>
      <li>What is the business cost of not closing this gap: money, time, compliance, reputation?</li>
      <li>Is the target state a requirement or an aspiration? What is the source?</li>
      <li>Which gaps share a common root cause, and can be closed together?</li>
      <li>What must happen first before this gap can be closed?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define current state with evidence.</strong> Document what exists today using system exports, screenshots, process notes, or user demonstrations. Do not rely on memory.</li>
      <li><strong>Define target state with source.</strong> State what is required and where that requirement comes from: regulation, project charter, stakeholder decision, or best practice.</li>
      <li><strong>Compare and list gaps.</strong> For each target element, ask: does the current state have it? If not, that is a gap. If partially, that is also a gap.</li>
      <li><strong>Classify each gap type.</strong> Use: missing (does not exist), incomplete (exists but insufficient), inconsistent (exists but contradicts target), outdated (exists but obsolete), ungoverned (exists but no owner).</li>
      <li><strong>Assess business impact.</strong> For each gap, state what happens because of it: blocked orders, delayed invoices, compliance violation, manual rework.</li>
      <li><strong>Identify closure approach.</strong> Choose from: build, buy, configure, process change, training, or retire. Justify the choice.</li>
      <li><strong>Assign owner and estimate effort.</strong> Every gap must have a person who is responsible for closure and a rough sizing.</li>
      <li><strong>Document in Gap Analysis Note.</strong> One note per major gap area. Link related gaps. Include dependencies and risks.</li>
      <li><strong>Validate with stakeholders.</strong> Confirm that the current state is accurate, the target state is still required, and the closure plan is feasible.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If current state cannot be verified with evidence, do not assess the gap — verify first.</li>
      <li>If target state is vague or unsourced, the gap is a requirements problem, not a current-state problem.</li>
      <li>If gap type is "missing," check whether it is truly missing or just undocumented before classifying.</li>
      <li>If closure approach is "build," verify that "buy" or "configure" was considered and rejected with reason.</li>
      <li>If many gaps share the same root cause, group them and fix the root cause first.</li>
      <li>If gap closure has no owner, the gap stays open — effort estimates without owners are fiction.</li>
      <li>If a gap closure depends on another gap, sequence them and flag the dependency.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Gap Analysis Note</strong> — One per major gap area. Contains current state, target state, gap description, type, impact, closure approach, effort, owner, dependencies, risks. See template below.</li>
      <li><strong>Gap Register</strong> — Consolidated table of all gaps with status, priority, owner, and target date.</li>
      <li><strong>Closure Plan</strong> — Sequenced actions with dependencies, grouped by root cause where applicable.</li>
      <li><strong>Risk Register updates</strong> — New risks identified during gap analysis: unowned gaps, unverified current state, conflicting target states.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Gap Analysis Note (compact)</h3>
    <pre><code>---
artifact: Gap Analysis Note
id: GAP-001
date: YYYY-MM-DD
scope: Process | System | Data | Organization
---

## Current state
<!-- What exists today. Be specific. Example: "Credit check is performed manually by the credit controller using transaction FD32. No automatic block exists." -->

## Target state
<!-- What is required. Source: regulation, project scope, best practice. Example: "Automatic credit check at order creation with real-time update from payment postings." -->

## Gap description
<!-- The difference between current and target -->

## Gap type
<!-- missing | incomplete | inconsistent | outdated | ungoverned -->

## Business impact
<!-- What happens because of this gap. Example: "Orders ship to customers with exceeded credit limits, causing bad debt." -->

## Affected stakeholders
<!-- Who is impacted -->

## Closure approach
<!-- Build | Buy | Configure | Process change | Training -->

## Effort estimate
<!-- Rough sizing: small | medium | large | unknown -->

## Owner
<!-- Who is responsible for closing the gap -->

## Dependencies
<!-- What must happen first -->

## Risks
<!-- What could prevent closure -->

## Related gaps
<!-- Links to other gap notes -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every gap has a verified current state with evidence.</li>
      <li>Every gap has a specific target state with a documented source.</li>
      <li>Gap type is classified using the defined taxonomy.</li>
      <li>Business impact is stated in operational or financial terms.</li>
      <li>Closure approach is selected and justified.</li>
      <li>Every gap has a named owner.</li>
      <li>Effort is estimated, even if rough.</li>
      <li>Dependencies between gaps are identified and sequenced.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Comparing against an ideal instead of a required state.</strong> Consequence: scope inflation. The project tries to reach perfection instead of compliance.</li>
      <li><strong>Assessing gaps without verifying current state.</strong> Consequence: gaps are imaginary. Time is spent closing gaps that do not exist.</li>
      <li><strong>Failing to classify gap type.</strong> Consequence: wrong closure approach. A missing field is treated as a configuration change when it needs custom development.</li>
      <li><strong>Not assigning owners.</strong> Consequence: gaps remain open. The gap register becomes a list of wishes.</li>
      <li><strong>Ignoring dependencies between gaps.</strong> Consequence: sequence errors. A team starts building before the data model is ready.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>AI agents should use this skill to produce structured gap assessments before recommending solutions or estimating effort.</p>
    <ul>
      <li><strong>Verify current state with system evidence or user demonstration</strong> before writing any gap. Do not rely on documentation alone.</li>
      <li><strong>Separate "missing" from "incomplete" from "outdated."</strong> The closure approach depends on the classification.</li>
      <li><strong>Always state the source of the target state.</strong> If the source is unclear, flag it as a requirements gap first.</li>
      <li><strong>Group gaps by root cause when possible.</strong> Fixing one root cause is cheaper than treating ten symptoms.</li>
      <li><strong>Assign an owner to every gap.</strong> If no owner exists, flag a governance gap.</li>
      <li><strong>Produce a Gap Analysis Note per major gap area.</strong> Link related notes. Do not bundle unrelated gaps.</li>
      <li><strong>Do not compare against ideal states.</strong> Compare against required states with documented sources.</li>
      <li><strong>Link to Atlas diagnostics</strong> when gaps relate to SAP processes. For example, invoice verification gaps should reference <a href="/scenarios/invoice-verification-three-way-match-delays/">Invoice Verification Three-Way Match Delays</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a></li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for process gaps.</li>
      <li><a href="/scenarios/master-data-issues-blocking-sales-orders/">Master Data Issues Blocking Sales Orders</a> — Scenario with current/target state gaps.</li>
      <li><a href="/scenarios/invoice-verification-three-way-match-delays/">Invoice Verification Three-Way Match Delays</a> — Gap scenario in P2P.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of gap analysis practices. It is not official BABOK, TOGAF, or SAP documentation. It focuses on practical enterprise and system migration contexts.</p>
    <p>Known limitations: the skill requires access to current system evidence and clear target state sources. In environments with poor documentation or shifting requirements, gap analysis becomes a continuous activity rather than a one-time exercise. The skill does not cover formal capability maturity modeling or enterprise architecture gap frameworks.</p>
  </section>
</article>
