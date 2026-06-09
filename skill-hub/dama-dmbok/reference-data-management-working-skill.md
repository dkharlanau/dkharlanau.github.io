---
layout: default
title: "Reference Data Management Working Skill"
description: "Manage code lists, status values, and classification schemes. Prevent drift between systems. Design distribution and change control for reference data."
permalink: /skill-hub/dama-dmbok/reference-data-management-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></li>
    <li aria-current="page">Reference Data Management</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — DAMA / Data</p>
  <h1>Reference Data Management Working Skill</h1>
  <p class="lead">Manage code lists, status values, and classification schemes. Prevent drift between systems. Design distribution and change control for reference data.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you manage the small data that controls big processes: country codes, order statuses, material groups, payment terms, and classification schemes. It provides a method to inventory reference data, detect drift between systems, define a single source of truth for each code list, and design change control that prevents integration failures. The output is a reference data governance model that keeps code values consistent across the landscape.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>An integration fails because a code value in the source system does not exist in the target.</li>
      <li>A report groups data incorrectly because classification codes have diverged between systems.</li>
      <li>A new country, product category, or business unit is added and the change must propagate to multiple systems.</li>
      <li>A system migration requires harmonizing two code sets that evolved independently.</li>
      <li>Users complain that dropdown lists show different values in different systems.</li>
      <li>An audit requires documented reference data ownership, change history, and approval workflows.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Example 1: IDoc failure on country code</h3>
    <p>A customer master replication IDoc fails with status 51. The error is "Country code XK not defined." The source system added Kosovo (XK) last month. The target system and the EDI partner still use the old country list. The skill produces a reference data synchronization plan: identify all systems that maintain country codes, define the authoritative source, and design a change notification workflow.</p>

    <h3>Example 2: Material group divergence</h3>
    <p>Procurement reports spend by material group. The numbers do not match Finance's cost center reports. The skill traces the material group code from the material master through to the procurement system and finds that two different code lists are in use: one from 2019 and one from 2023. The skill produces a harmonization plan with mapping, migration, and governance rules.</p>

    <h3>Example 3: Order status confusion</h3>
    <p>The CRM shows orders as "Confirmed." The ERP shows them as "In Process." The warehouse shows them as "Ready to Ship." These are not the same status mapped differently; they are different status schemes maintained by different teams. The skill maps each status scheme, defines the canonical status list, and designs a synchronization rule.</p>

    <h3>Example 4: Post-merger chart of accounts</h3>
    <p>Two companies merge. Each has a chart of accounts. The consolidation system needs a unified view. The skill inventories both code sets, identifies overlaps and gaps, defines the target chart of accounts, and produces a mapping table with conversion rules and validation checks.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>List of reference data domains in scope: country codes, status values, material groups, payment terms, etc.</li>
      <li>Code values and descriptions from each system that maintains or uses the domain.</li>
      <li>System landscape showing which systems create, modify, and consume each code list.</li>
      <li>Integration documentation showing how code values are transmitted between systems.</li>
      <li>Business process descriptions that depend on the reference data.</li>
      <li>Change history or audit log showing recent additions, modifications, or deletions (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which system is the authoritative source for this code list, and who approves changes to it?</li>
      <li>What are the allowed values, and do all systems use the same set?</li>
      <li>What happens when a code is added in the source but not yet in the target?</li>
      <li>Are there deprecated codes that still exist in some systems but should not be used?</li>
      <li>Which business process fails when a code value is missing or mismatched?</li>
      <li>How are code changes communicated to downstream systems and teams?</li>
      <li>Is there a mapping layer between code lists, and who maintains it?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Inventory reference data domains.</strong> List the code lists, status values, and classification schemes in scope. For each, identify the business purpose and the systems that use it.</li>
      <li><strong>Collect code values from each system.</strong> Extract the current values and descriptions from every system that maintains or consumes the domain. Include custom values, legacy values, and local extensions.</li>
      <li><strong>Compare and identify drift.</strong> Align code values across systems. Flag: values missing in one system, values with different descriptions, values with different meanings, and custom values that exist only locally.</li>
      <li><strong>Define the canonical code set.</strong> For each domain, decide the authoritative list of values, descriptions, and meanings. Document which system is the source of truth and which values are deprecated.</li>
      <li><strong>Design the mapping layer.</strong> If systems cannot use the same codes directly, define mapping tables with source value, target value, transformation rule, and owner.</li>
      <li><strong>Design change control.</strong> Define: who can request a change, who approves it, how it is tested, how it is communicated, and how it is deployed to all systems.</li>
      <li><strong>Design distribution.</strong> Define how code changes flow from the source of truth to each consumer: API, batch file, database replication, or manual update. Include frequency and failure handling.</li>
      <li><strong>Define monitoring.</strong> Design checks that detect drift: scheduled comparisons, integration validation, or report reconciliation. Define who is alerted and how they respond.</li>
      <li><strong>Produce the reference data governance model.</strong> Combine inventory, canonical set, mapping, change control, distribution, and monitoring into a single document.</li>
      <li><strong>Validate with a pilot change.</strong> Test the change control and distribution process on a low-risk code addition. Adjust before applying to critical codes.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If two systems use different code lists for the same business concept, define a canonical set and a mapping layer; do not force one system to adopt the other's codes unless agreed.</li>
      <li>If a code is added to the source system, it must not be usable in downstream processes until the target systems have confirmed receipt.</li>
      <li>If a code is deprecated, it must remain in the code list for historical reporting but be blocked from new transactions.</li>
      <li>If a mapping table is required, assign an owner who reviews it quarterly; unmaintained mappings become a source of silent errors.</li>
      <li>If a system maintains local extensions to a global code list, document the extensions and their business justification; unauthorized extensions are drift.</li>
      <li>If a code change affects financial reporting, compliance, or integration, it requires approval from both business and technical owners.</li>
      <li>If reference data drift is detected, treat it as a data quality incident; run root cause analysis before correcting.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Reference Data Inventory</strong> — domains, systems, values, and drift analysis.</li>
      <li><strong>Canonical Code Set Definition</strong> — authoritative values, descriptions, deprecation status, and source of truth.</li>
      <li><strong>Mapping Specification</strong> — source-to-target mappings with transformation rules and owners.</li>
      <li><strong>Reference Data Governance Model</strong> — change control, distribution, monitoring, and ownership.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Reference Data Drift Comparison (compact)</h3>
    <pre><code>| Domain | System A Values | System B Values | Missing in A | Missing in B | Different Meaning | Action |
|--------|-----------------|-----------------|--------------|--------------|-------------------|--------|
| Country | 249 codes | 247 codes | XK, XZ | — | XK = Kosovo in A, not defined in B | Add XK to B; retire XZ in A |
| MaterialGroup | 45 groups | 52 groups | — | MG_NEW_1 to MG_NEW_7 | MG_10 = "Electronics" in A, "Hardware" in B | Harmonize definitions; update B |
</code></pre>

    <h3>Code Change Request (compact)</h3>
    <pre><code>---
request: Code Change
id: CR-REF-001
domain: Country
date: 2026-06-09
---

## Proposed change
- Add: XK — Kosovo
- Deprecate: XZ — Temporary code for testing

## Business reason
XK recognized for tax reporting. XZ was a test code never cleaned up.

## Systems affected
- SAP S/4 (source of truth)
- CRM
- EDI gateway
- BW

## Approval
- Business owner: Finance Director
- Technical owner: Integration Lead

## Test plan
1. Add XK in SAP dev
2. Verify replication to CRM and EDI
3. Run sample transaction
4. Confirm BW load

## Rollback
- Remove XK from all systems if test fails

## Communication
- Notify: EDI partners, Tax team, Reporting team
- Method: Email + wiki update
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every reference data domain in scope has a named source of truth system.</li>
      <li>Code values have been collected from every system that uses the domain.</li>
      <li>Drift has been documented with specific values, not just "some differences."</li>
      <li>The canonical code set is defined and approved by the business owner.</li>
      <li>Mapping tables have owners and review cycles.</li>
      <li>Change control includes request, approval, test, communication, and rollback steps.</li>
      <li>Distribution paths are documented with frequency and failure handling.</li>
      <li>Monitoring detects drift and alerts a named owner.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Treating reference data as "just configuration" with no governance. <strong>Consequence:</strong> Codes diverge silently; integrations fail; reports are wrong; no one knows why.</li>
      <li><strong>Mistake:</strong> Adding a code in the source system without notifying downstream systems. <strong>Consequence:</strong> IDocs fail, APIs reject payloads, and business processes halt.</li>
      <li><strong>Mistake:</strong> Deleting deprecated codes instead of marking them deprecated. <strong>Consequence:</strong> Historical records lose meaning; reports break; audit trails are damaged.</li>
      <li><strong>Mistake:</strong> Maintaining mapping tables without ownership or review. <strong>Consequence:</strong> Mappings become stale; silent data corruption occurs.</li>
      <li><strong>Mistake:</strong> Allowing every system to maintain local extensions without documentation. <strong>Consequence:</strong> The "standard" code list becomes a patchwork; consolidation is impossible.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Start with the failure.</strong> If an integration failed due to a code mismatch, name the exact code, the source system, and the target system. Do not generalize.</li>
      <li><strong>Inventory before harmonizing.</strong> Collect all code values from all systems before proposing a canonical set. Do not assume one system is correct.</li>
      <li><strong>Document drift precisely.</strong> List exact missing values, different descriptions, and different meanings. Do not write "codes are out of sync."</li>
      <li><strong>Design change control, not just codes.</strong> A canonical set without a change process will drift again. Always include request, approval, test, communication, and monitoring.</li>
      <li><strong>Produce artifacts, not advice.</strong> Output a Reference Data Inventory, a Canonical Code Set, and a Code Change Request in the templates provided.</li>
      <li><strong>Link to Atlas diagnostics.</strong> If reference data issues involve SAP, link to <a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a> or <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a>.</li>
      <li><strong>Handle missing information.</strong> If code lists from some systems are unavailable, produce a collection checklist and ask the user to gather them.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/dama-dmbok/data-integration-interoperability-working-skill/">Data Integration &amp; Interoperability</a> — when reference data issues cause integration failures.</li>
      <li><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a> — when reference data is part of master data governance.</li>
      <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a> — when reference data lacks ownership or change control.</li>
      <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> — when a code mismatch needs root cause analysis.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a> — resolving key and code mapping issues.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — when reference data causes IDoc failures.</li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — reference data as part of master data quality.</li>
      <li><a href="/atlas/concepts/data-quality-controls/">Data Quality Controls</a> — controls for code validation.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of reference data management practice. It is not official DAMA-DMBOK or SAP documentation. It has been applied in SAP and multi-system integration contexts but may need adaptation for cloud-native applications, microservices with independent code lists, or heavily regulated environments.</p>
    <p>Limitations: This skill does not cover advanced reference data platforms, semantic ontologies, or automated code synchronization tools. It focuses on governance, inventory, and change control suitable for project and operations contexts.</p>
  </section>
</article>
