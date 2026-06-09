---
layout: default
title: "Data Quality Root Cause Working Skill"
description: "Trace a data defect from symptom to entry point. Classify the root cause type. Produce a correction plan and a prevention control."
permalink: /skill-hub/dama-dmbok/data-quality-root-cause-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></li>
    <li aria-current="page">Data Quality Root Cause</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — DAMA / Data</p>
  <h1>Data Quality Root Cause Working Skill</h1>
  <p class="lead">Trace a data defect from symptom to entry point. Classify the root cause type. Produce a correction plan and a prevention control.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you stop treating data quality symptoms as root causes. It provides a repeatable method to trace a defect backward through systems, processes, and decisions until you find the point where bad data entered the lifecycle. The output is a classified root cause, a correction plan for affected records, and a prevention control that stops recurrence.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A report shows incorrect values and someone says "the data is bad" without explaining why.</li>
      <li>Orders are blocked because customer master data is incomplete, and the fix is always manual.</li>
      <li>Duplicate records appear in a system and deduplication campaigns keep finding more.</li>
      <li>An integration sends data to a target system, but the target rejects it or stores it incorrectly.</li>
      <li>A data steward spends more than 20% of their time correcting the same type of defect.</li>
      <li>An audit or incident review requires a documented root cause and prevention plan.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Example 1: Invoice blocked by missing tax number</h3>
    <p>Invoices for German customers fail because TaxNumber1 is empty. The symptom is in the billing document. The root cause is that the CRM integration creates customers without validating the tax number, and the SAP incompletion procedure does not block the customer until invoice time. The correction updates affected customers. The prevention adds validation at the CRM-to-SAP interface and strengthens the incompletion procedure.</p>

    <h3>Example 2: Duplicate vendors in procurement</h3>
    <p>Buyers create new vendor records because they cannot find existing ones. The symptom is duplicate payment runs. The root cause is a search help that requires exact name matching and a governance gap: no one reviews new vendor requests against existing records. The correction merges duplicates. The prevention adds a fuzzy search and a data steward approval step.</p>

    <h3>Example 3: Wrong material group in COGS report</h3>
    <p>The COGS report groups materials incorrectly. The symptom is wrong financial reporting. The root cause is a mapping table updated by IT six months ago without notifying Finance. The correction remaps historical transactions. The prevention adds a change notification workflow and a report validation step.</p>

    <h3>Example 4: IDoc failure in customer replication</h3>
    <p>Customer master changes fail to replicate to a downstream system. The symptom is an IDoc status 51. The root cause is a reference data mismatch: the target system does not recognize a new country code added in the source. The correction reprocesses with the correct mapping. The prevention adds reference data synchronization to the change process.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The exact symptom: field, value, record count, system, and business process affected.</li>
      <li>Sample records showing the defect (anonymized if needed).</li>
      <li>System landscape: where the data is created, transformed, stored, and consumed.</li>
      <li>Data entry points: user interfaces, integrations, batch loads, API calls.</li>
      <li>Validation rules that should have caught the defect (if any exist).</li>
      <li>Ticket or incident history showing recurrence frequency (optional).</li>
      <li>Stakeholders who can explain the business process and the data flow (optional but recommended).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which field is wrong, what is the wrong value, and what should it be?</li>
      <li>When did the defect first appear, and has it happened before?</li>
      <li>Where was this record created, and who or what created it?</li>
      <li>What validation should have caught this, and why did it not?</li>
      <li>Which business process fails when this field is wrong?</li>
      <li>How many records are affected, and how many more could be affected?</li>
      <li>Who corrected this last time, and what did they do?</li>
      <li>Is the defect caused by a rule that does not exist, a rule that exists but is not enforced, or a rule that is wrong?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Document the symptom precisely.</strong> Record: data element, wrong value, expected value, system where observed, business process affected, number of records, and first occurrence date. Do not proceed with vague symptoms.</li>
      <li><strong>Identify the business impact.</strong> Quantify if possible: orders blocked, invoices delayed, reports wrong, compliance risk. If you cannot quantify, describe the business consequence in process terms.</li>
      <li><strong>Trace backward to the entry point.</strong> Follow the data from the symptom system to the system that created or last modified the record. Check integrations, batch jobs, user transactions, and API calls.</li>
      <li><strong>Classify the root cause type.</strong> Use one of: missing rule, unenforced rule, wrong rule, upstream data error, integration mapping error, reference data mismatch, user error without guardrail, system bug, unknown.</li>
      <li><strong>Identify the entry point detail.</strong> Name the exact system, transaction, interface, or user action where the defect entered. Include timestamp and user or process ID if available.</li>
      <li><strong>Assess scope.</strong> Determine how many records are affected now, how many could be affected in the future, and whether the defect is spreading to downstream systems.</li>
      <li><strong>Design the correction.</strong> Choose: manual correction, mass update with validation, reprocessing, mapping fix, or record merge. Define validation and approval steps.</li>
      <li><strong>Design the prevention control.</strong> Choose: add validation, strengthen workflow, fix mapping, synchronize reference data, add monitoring, or change the user interface. The prevention must address the root cause, not the symptom.</li>
      <li><strong>Assign ownership.</strong> Name who corrects, who validates, who implements the prevention, and who monitors.</li>
      <li><strong>Produce the Root Cause Analysis Note.</strong> Document symptom, classification, entry point, impact, correction, prevention, and owners. <a href="/skill-hub/artifact-templates/">Use the template</a>.</li>
      <li><strong>Validate with stakeholders.</strong> Confirm the root cause, correction approach, and prevention control with business and technical owners before execution.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the defect recurs, the root cause is not the symptom; trace further upstream.</li>
      <li>If only a few records are affected and the rule is clear, correct records through the governed process.</li>
      <li>If many records are affected, prepare mass correction with validation and approval; never mass-update without a sample check.</li>
      <li>If the root cause is "user error," look for the missing guardrail or validation that should have prevented it.</li>
      <li>If the root cause is an integration mapping error, fix the mapping before correcting records, or the correction will be overwritten.</li>
      <li>If the root cause is a reference data mismatch, synchronize reference data before reprocessing affected transactions.</li>
      <li>If no validation rule exists for this data element, the root cause is "missing rule" even if the data looks obviously wrong.</li>
      <li>If a rule exists but is bypassed by a specific path (API, batch, direct DB), the root cause is "unenforced rule."</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Root Cause Analysis Note</strong> — classified root cause, entry point, impact, correction, and prevention. <a href="/skill-hub/artifact-templates/">See Artifact Templates</a>.</li>
      <li><strong>Remediation Backlog Item</strong> — if mass correction or prevention implementation is needed. <a href="/skill-hub/artifact-templates/">See Artifact Templates</a>.</li>
      <li><strong>Data Quality Rule</strong> — if a new or updated rule is required. <a href="/skill-hub/artifact-templates/">See Artifact Templates</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Root Cause Classification Quick Reference</h3>
    <pre><code>| Type | Definition | Typical Fix | Prevention |
|------|------------|-------------|------------|
| Missing rule | No validation or policy exists | Define rule | Add enforcement point |
| Unenforced rule | Rule exists but is bypassed | Close bypass | Strengthen enforcement |
| Wrong rule | Rule exists but allows bad data | Correct rule | Change validation logic |
| Upstream data error | Source system sends bad data | Fix source or add mapping | Source validation |
| Integration mapping error | Field mapped incorrectly | Correct mapping | Mapping test + monitoring |
| Reference data mismatch | Code values out of sync | Synchronize codes | Reference data governance |
| User error without guardrail | User entered wrong data | Correct records | Add UI validation or workflow |
| System bug | Software defect | Patch or workaround | Regression test |
| Unknown | Cannot determine root cause | Escalate | Add logging or monitoring |
</code></pre>

    <h3>Defect Trace Log (compact)</h3>
    <pre><code>| Step | System | Field Value | Rule Checked? | Result | Next Step |
|------|--------|-------------|---------------|--------|-----------|
| 1 | Billing | TaxNumber1 = empty | Incompletion procedure | Failed at invoice, not at customer creation | Check CRM integration |
| 2 | CRM | TaxNumber1 = empty | CRM validation | None exists | Root cause: missing rule at CRM entry |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The symptom is documented with exact field, value, system, and business process.</li>
      <li>The root cause is classified into one of the defined types, not described as a narrative.</li>
      <li>The entry point is named: specific system, transaction, interface, or user action.</li>
      <li>The correction approach includes validation and approval steps.</li>
      <li>The prevention control addresses the root cause, not the symptom.</li>
      <li>All owners are named, not just roles.</li>
      <li>The analysis has been validated with at least one business and one technical stakeholder.</li>
      <li>If the root cause is unknown, there is a plan to add monitoring or logging to discover it.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Treating the symptom as the root cause. <strong>Consequence:</strong> The defect recurs because the upstream validation was never fixed.</li>
      <li><strong>Mistake:</strong> Mass-correcting records before fixing the source or mapping. <strong>Consequence:</strong> The next integration run reintroduces the same defect.</li>
      <li><strong>Mistake:</strong> Blaming "user error" without investigating why the system allowed it. <strong>Consequence:</strong> Users keep making the same mistake; morale drops; no systemic fix occurs.</li>
      <li><strong>Mistake:</strong> Skipping the scope assessment. <strong>Consequence:</strong> A "small" correction turns into a multi-system remediation when downstream impacts are discovered late.</li>
      <li><strong>Mistake:</strong> Proposing prevention controls that are not enforceable. <strong>Consequence:</strong> The prevention is ignored, and the defect recurs within the next project cycle.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Demand precise symptoms.</strong> If the user says "data is bad," ask: which field, which records, which system, which business process, and what is the expected value? Do not proceed with vague input.</li>
      <li><strong>Trace backward systematically.</strong> Ask about the data lifecycle: creation, modification, integration, storage, consumption. Do not guess the entry point.</li>
      <li><strong>Classify the root cause.</strong> Use the classification table. If none fit, say "unknown" and propose monitoring.</li>
      <li><strong>Separate correction from prevention.</strong> Always produce both. A correction without prevention is incomplete. A prevention without correction leaves existing defects in place.</li>
      <li><strong>Produce artifacts, not explanations.</strong> Output a Root Cause Analysis Note and, if needed, a Remediation Backlog Item. Use the templates.</li>
      <li><strong>Link to Atlas diagnostics.</strong> If the defect involves SAP master data, link to <a href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">SAP Master Data Duplicate Diagnostics</a>, <a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a>, or <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a>.</li>
      <li><strong>Handle missing information.</strong> If system logs or record samples are unavailable, produce a discovery checklist and ask the user to gather them before completing the analysis.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a> — when root causes reveal ownership or rule gaps.</li>
      <li><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a> — when defects are in master data domains.</li>
      <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> — when the data path from source to symptom is unclear.</li>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a> — for broader operational root cause methods.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/data-quality-controls/">Data Quality Controls</a> — types of controls and where to apply them.</li>
      <li><a href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">SAP Master Data Duplicate Diagnostics</a> — finding and resolving duplicates.</li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — tracing BP replication failures.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — classifying IDoc failures.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of data quality root cause analysis. It is not official DAMA-DMBOK or Six Sigma documentation. It has been applied in SAP-centric support and project contexts but may need adaptation for real-time streaming, IoT, or unstructured data pipelines.</p>
    <p>Limitations: This skill assumes you can access system logs, record samples, and stakeholders. It does not cover statistical process control, advanced data profiling, or automated anomaly detection. For large-scale automated root cause, specialized tooling is required.</p>
  </section>
</article>
