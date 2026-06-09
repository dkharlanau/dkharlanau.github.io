---
layout: default
title: "Change Impact Analysis — Working Skill"
description: "Before applying a transport, configuration change, or master data update, know which processes, interfaces, and stakeholders are affected."
permalink: /skill-hub/sap-ams/change-impact-analysis-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/sap-ams/">SAP AMS</a></li>
    <li aria-current="page">Change Impact Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — SAP AMS / Operations</p>
  <h1>Change Impact Analysis</h1>
  <p class="lead">Before applying a transport, configuration change, or master data update, know which processes, interfaces, and stakeholders are affected.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you predict what will break, slow down, or behave differently after a change goes live. It produces a Change Impact Assessment that lists affected systems, data, interfaces, processes, and stakeholders, with a risk level and a rollback plan. The goal is to prevent the all-too-common pattern where a "small" config change breaks an interface that no one remembered existed.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A transport is ready for production and the release note only says "config update."</li>
      <li>A master data change (new plant, new company code, new payment term) is planned and downstream systems may be affected.</li>
      <li>An interface schema or API contract is being modified and consumers need to adapt.</li>
      <li>A new validation rule or incompletion procedure is being introduced.</li>
      <li>A user role or authorization change is planned and sensitive transactions may be affected.</li>
      <li>A periodic process timing or scheduling change is proposed.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: New payment term in SAP</h3>
    <p>A finance team requests a new payment term for a specific customer segment. The change seems small: one new entry in T052. Impact analysis reveals that the payment term is used in credit limit calculations in a custom report, in the dunning procedure configuration, and in the Ariba integration that sends payment terms to suppliers. The assessment prevents a go-live until the custom report and the Ariba mapping are updated.</p>

    <h3>Example 2: Adding a mandatory field to a sales document type</h3>
    <p>A business analyst proposes adding a mandatory reference field to a sales order type to improve traceability. Impact analysis checks the incompletion procedure, the web service API that creates orders from the e-commerce platform, the EDI ORDERS interface, and the BW extractor. The API and EDI interfaces do not send the new field, so orders would fail. The assessment delays the change until interface specifications are updated.</p>

    <h3>Example 3: Changing a background job schedule</h3>
    <p>A Basis team wants to move a billing job earlier to avoid peak hours. Impact analysis checks downstream jobs that depend on billing completion: the invoice print job, the IDoc generation job, and the BW delta extraction. Moving billing earlier without adjusting the dependent jobs would cause the invoice print job to run on incomplete data. The assessment proposes a coordinated schedule change for all three jobs.</p>

    <h3>Example 4: Updating a business partner grouping</h3>
    <p>An MDG team plans to change the business partner grouping for a customer category to align with a new organizational structure. Impact analysis checks CVI synchronization settings, customer account groups, the CRM replication filter, and the tax reporting interface. The CRM filter uses the old grouping as a selection criterion, so the change would stop replication for the affected customers. The assessment adds a CRM filter update to the change scope.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>A precise description of the proposed change: what object, what value, what system, and what the intended outcome is.</li>
      <li>The transport or change request documentation with object list and developer notes.</li>
      <li>System landscape diagram or list: DEV, QAS, PRD, and connected systems (CRM, SRM, BW, Ariba, Salesforce, etc.).</li>
      <li>Interface ownership matrix or list of interfaces that touch the changed object.</li>
      <li>Process documentation for the business process that uses the changed object.</li>
      <li>Where-used lists: for config objects, tables, fields, and custom code.</li>
      <li>Stakeholder list: functional owners, integration team, data stewards, business users who will test.</li>
      <li>Test environment availability and data freshness.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What exact object is changing, and what is the current value versus the proposed value?</li>
      <li>Which transactions, reports, batch jobs, and interfaces read or write this object?</li>
      <li>Which downstream systems receive data derived from this object?</li>
      <li>Which business process steps depend on this object, and what happens if the value is different?</li>
      <li>Which users or user groups will see a change in behavior, screen layout, or available options?</li>
      <li>Which validations, incompletion procedures, or workflow steps reference this object?</li>
      <li>Which custom code, enhancement, or user exit references this object?</li>
      <li>What is the rollback plan if the change causes unexpected failures in production?</li>
      <li>Who will test this change, and do they have representative test data?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the change boundary.</strong> Document exactly what is changing: object name, table, field, transaction, program, or configuration path. Include current and proposed values.</li>
      <li><strong>Map direct consumers.</strong> Use where-used search, cross-reference tools, or SE11/SE16 to find all programs, classes, reports, and transactions that reference the object.</li>
      <li><strong>Map interface consumers.</strong> Check all interfaces (IDoc, RFC, API, file) that send or receive the object. Review the segment structures, API schemas, and mapping tables.</li>
      <li><strong>Map process consumers.</strong> Identify business process steps that use the object. Check process documentation or interview the process owner.</li>
      <li><strong>Map data consumers.</strong> Check BW extractors, reporting tables, data warehouse loads, and analytics tools that reference the object.</li>
      <li><strong>Identify authorization impacts.</strong> If the change affects transactions or data access, check roles and profiles that grant access. Use SUIM or similar tools.</li>
      <li><strong>Assess risk for each consumer.</strong> For each affected component, rate the risk: Low (no change needed), Medium (monitor or minor adjustment), High (breaks without update), Critical (revenue-impacting failure).</li>
      <li><strong>Define testing scope.</strong> List what must be tested: unit test, integration test, regression test, user acceptance test. Name the tester and the test data requirements.</li>
      <li><strong>Define rollback plan.</strong> How can the change be reversed? Transport reversal, config rollback, data restore, or emergency procedure?</li>
      <li><strong>Document in a Change Impact Assessment.</strong> Use the template below or the <a href="/skill-hub/artifact-templates/">Artifact Templates</a> page.</li>
      <li><strong>Obtain approval.</strong> The assessment must be reviewed by the functional owner, integration lead, and change manager before implementation.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the change affects a table or field used by more than one interface, treat the risk as High until each interface is verified.</li>
      <li>If the change introduces a new mandatory field, check all creation channels (GUI, API, EDI, batch) before approving.</li>
      <li>If the change affects master data, check replication and synchronization settings in all target systems.</li>
      <li>If the change affects a background job schedule, check all dependent jobs and their schedules.</li>
      <li>If the change affects authorization objects, test with at least one user from each affected role.</li>
      <li>If no rollback plan exists, do not approve the change.</li>
      <li>If testing cannot be performed with representative data, delay the change until test data is available.</li>
      <li>If the change was developed in DEV but the object exists differently in PRD, verify the production state before impact analysis.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Change Impact Assessment</strong> — The primary artifact. See <a href="/skill-hub/artifact-templates/">Artifact Templates</a> for the full format.</li>
      <li><strong>Affected Component List</strong> — A table of all systems, interfaces, processes, and reports affected, with risk levels.</li>
      <li><strong>Test Plan</strong> — What to test, who tests, with what data, and what success looks like.</li>
      <li><strong>Rollback Procedure</strong> — Step-by-step instructions to reverse the change if it fails.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Change Impact Assessment (compact)</h3>
    <pre><code>---
artifact: Change Impact Assessment
id: CIA-001
date: YYYY-MM-DD
change: Description
status: draft | reviewed | approved
---

## Change description
<!-- Exact object, current value, proposed value, system -->

## Change driver
<!-- Why this change is needed -->

## Systems affected
<!-- Direct and indirect system impacts -->

| System | Component | Risk | Action Required | Owner |
|--------|-----------|------|-----------------|-------|
| SAP PRD | T052 | Medium | Update dunning config | FI Lead |

## Data affected
<!-- Tables, fields, records that change -->

## Interfaces affected
<!-- APIs, IDocs, events that may break or need update -->

| Interface | Direction | Risk | Action Required | Owner |
|-----------|-----------|------|-----------------|-------|
| INVOIC02 | Outbound | High | Update segment version | Integration |

## Processes affected
<!-- Business processes that change -->

## Stakeholders affected
<!-- Who needs to know or act -->

## Testing required
<!-- What must be tested before go-live -->

| Test | Tester | Data | Success Criteria |
|------|--------|------|------------------|
| Sales order creation | SD Team | Customer 12345 | Order creates without error |

## Rollback plan
<!-- How to undo if the change fails -->

## Risk level
<!-- Low | Medium | High | Critical -->

## Approval required
<!-- Who must approve before implementation -->

## Owner
<!-- Who drives this assessment and the change -->

## Related changes
<!-- Links to other change impact assessments -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The change is described with exact object names, table/field references, and current versus proposed values.</li>
      <li>At least one direct consumer (program, report, transaction) was identified through where-used search.</li>
      <li>All interfaces that touch the changed object were checked and documented.</li>
      <li>All business process steps that depend on the object were identified.</li>
      <li>Each affected component has a risk rating and a required action.</li>
      <li>A test plan exists with named testers, test data, and success criteria.</li>
      <li>A rollback plan exists and has been validated as technically feasible.</li>
      <li>The assessment was reviewed by the functional owner and change manager before approval.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Assuming a change is "small" without checking where-used. <strong>Consequence:</strong> A single config field change breaks three interfaces and a custom report.</li>
      <li><strong>Mistake:</strong> Checking only the primary system and ignoring connected systems. <strong>Consequence:</strong> The change works in SAP but fails in CRM, BW, or the data warehouse.</li>
      <li><strong>Mistake:</strong> Not testing with realistic data. <strong>Consequence:</strong> The change works in QAS with simple test data but fails in PRD with complex real-world records.</li>
      <li><strong>Mistake:</strong> Omitting the rollback plan. <strong>Consequence:</strong> When the change fails, the team spends hours improvising a reversal under pressure.</li>
      <li><strong>Mistake:</strong> Not involving the integration team early. <strong>Consequence:</strong> Interface impacts are discovered after go-live, when messages are already failing.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Demand precision.</strong> Ask for the exact object, table, field, transaction, or configuration path being changed. Do not proceed with vague descriptions like "update the sales config."</li>
      <li><strong>Systematically check consumers.</strong> Ask the user to run where-used searches or provide interface documentation. Do not assume you know all consumers from general knowledge.</li>
      <li><strong>Separate direct from indirect impact.</strong> Direct impact: the object itself changes. Indirect impact: a derived value, dependent job, or downstream system is affected. List both.</li>
      <li><strong>Always ask for the rollback plan.</strong> If the user does not have one, refuse to approve the change in the assessment and flag it as a blocker.</li>
      <li><strong>Produce a Change Impact Assessment.</strong> Use the template above. Fill every section. If a section is unknown, state what information is missing and who can provide it.</li>
      <li><strong>Link to Atlas diagnostics for interface and integration checks.</strong> Reference the relevant Atlas pages for IDoc, RFC, or background job diagnostics when interfaces are affected.</li>
      <li><strong>Do not invent system names or interface IDs.</strong> Use only the systems, interfaces, and objects the user confirms exist in their landscape.</li>
      <li><strong>Flag high-risk combinations.</strong> Any change that affects master data + interfaces + batch jobs should be flagged as High or Critical risk by default.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage</a> — Use when a change has already caused an incident.</li>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a> — Use when a change caused unexpected failures and you need to understand why.</li>
      <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — Use to understand how interfaces are monitored before and after changes.</li>
      <li><a href="/skill-hub/architecture/solution-architecture-review-working-skill/">Solution Architecture Review</a> — Use for larger changes that require architectural assessment.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — When interfaces are affected.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — When job schedules change.</li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — When BP or CVI changes are planned.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — When new validations or mandatory fields are introduced.</li>
      <li><a href="/atlas/automation/sap-ams-operating-model/">SAP AMS Operating Model</a> — How change management fits into AMS operations.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of change impact analysis practice. It is not official SAP change management documentation. The where-used tools and cross-reference capabilities vary by SAP release and system configuration. Some landscapes lack comprehensive interface documentation, making indirect impact identification difficult. The skill assumes the user has access to development and quality systems; restricted production-only access limits the depth of analysis.</p>
  </section>
</article>
