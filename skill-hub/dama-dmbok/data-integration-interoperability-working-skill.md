---
layout: default
title: "Data Integration & Interoperability Working Skill"
description: "Diagnose integration failures caused by data mismatch, schema drift, or mapping errors. Define data contracts and validation rules at interface boundaries."
permalink: /skill-hub/dama-dmbok/data-integration-interoperability-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></li>
    <li aria-current="page">Data Integration &amp; Interoperability</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — DAMA / Data</p>
  <h1>Data Integration &amp; Interoperability Working Skill</h1>
  <p class="lead">Diagnose integration failures caused by data mismatch, schema drift, or mapping errors. Define data contracts and validation rules at interface boundaries.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you fix the data layer of integration failures. It provides a method to diagnose why data does not flow correctly between systems: schema mismatches, field mapping errors, validation gaps, reference data drift, and timing issues. The output is a corrected interface specification with a data contract, validation rules, and monitoring that prevents recurrence.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>An integration fails and the error is in the data payload: missing fields, wrong format, or unexpected values.</li>
      <li>A source system sends data that the target system rejects or misinterprets.</li>
      <li>An API schema changes and downstream consumers break.</li>
      <li>Data arrives at the target system but is stored in the wrong field or table.</li>
      <li>An IDoc, message, or file transfer succeeds technically but produces wrong business results.</li>
      <li>A new interface is being designed and needs a data contract before development starts.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Example 1: API schema drift breaks mobile app</h3>
    <p>A backend API adds a new required field <code>region_code</code> without versioning. The mobile app does not send it. The API rejects requests with a generic 400 error. The skill diagnoses the schema change, defines a backward-compatible versioning rule, and produces a data contract that specifies required vs optional fields and notification rules for schema changes.</p>

    <h3>Example 2: IDoc field mapped to wrong target</h3>
    <p>A customer master IDoc from SAP to CRM maps <code>STCD1</code> (tax number) to the CRM "VAT" field. After a system upgrade, the mapping silently changes to "Company Registration Number." Tax reports in CRM are now wrong. The skill traces the mapping, identifies the change point, and produces a mapping validation test and a change notification rule.</p>

    <h3>Example 3: File load with wrong delimiter encoding</h3>
    <p>A daily CSV file load from a supplier shifts all columns by one position because the file switches from comma-delimited to semicolon-delimited. The load succeeds but product descriptions are stored in the price field. The skill defines a file format contract with validation rules: delimiter, encoding, header row, and column count check.</p>

    <h3>Example 4: Real-time event payload too large</h3>
    <p>An event-driven architecture sends order events to a warehouse system. During peak hours, the payload exceeds the message broker limit. Events are dropped silently. The skill defines a payload size contract, a splitting rule for large orders, and a monitoring alert for dropped messages.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The interface identifier: API endpoint, IDoc type, message queue, file transfer, or integration flow name.</li>
      <li>Source system schema: fields, types, lengths, formats, and validation rules.</li>
      <li>Target system schema: expected fields, types, lengths, and constraints.</li>
      <li>Mapping documentation or configuration showing how source fields map to target fields.</li>
      <li>Error logs, failed payloads, or incident tickets showing the failure pattern.</li>
      <li>Business process description of what the integration is supposed to achieve.</li>
      <li>Integration ownership: technical owner, business owner, and operational support contact.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the exact data element that fails, and what is the expected vs actual value?</li>
      <li>Which field in the source maps to which field in the target, and is the mapping still correct?</li>
      <li>What validation does the target apply, and does the source data meet it?</li>
      <li>Has the source schema, target schema, or mapping changed recently?</li>
      <li>What reference data or code values are involved, and are they synchronized?</li>
      <li>What is the payload size, format, encoding, and frequency? Are any limits being exceeded?</li>
      <li>What happens to failed data: is it rejected, quarantined, retried, or lost?</li>
      <li>Who is notified when the interface fails, and how long does it take to respond?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Document the interface.</strong> Record: interface ID, source system, target system, direction, data domain, business purpose, and owners. <a href="/skill-hub/artifact-templates/">Use the Interface Ownership Matrix template</a>.</li>
      <li><strong>Capture the failure symptom.</strong> Record: error message, failed payload sample, timestamp, frequency, and business impact. Be exact.</li>
      <li><strong>Compare source and target schemas.</strong> List source fields with types, lengths, and formats. List target fields with constraints. Identify mismatches: missing fields, type conflicts, length overflows, and format errors.</li>
      <li><strong>Verify the mapping.</strong> Trace each source field to its target field. Check for: missing mappings, wrong mappings, stale mappings, and silent truncation.</li>
      <li><strong>Check reference data.</strong> Verify that code values, status values, and identifiers used in the payload are valid in the target system.</li>
      <li><strong>Check timing and sequencing.</strong> Verify that data arrives in the correct order, at the correct frequency, and within time windows that the target expects.</li>
      <li><strong>Classify the failure type.</strong> Use: schema mismatch, mapping error, validation failure, reference data mismatch, format error, size limit, timing issue, or unknown.</li>
      <li><strong>Design the fix.</strong> Choose: correct mapping, add validation, synchronize reference data, change format, split payload, add sequencing, or redesign the interface.</li>
      <li><strong>Define the data contract.</strong> Document: schema version, required and optional fields, types, lengths, formats, allowed values, payload limits, frequency, error handling, and change notification rules.</li>
      <li><strong>Define monitoring and alerting.</strong> Design checks for: schema compliance, mapping integrity, reference data sync, payload size, error rate, and latency. Define thresholds and alert owners.</li>
      <li><strong>Produce the Integration Failure Review.</strong> Document symptom, classification, fix, contract, and monitoring. <a href="/skill-hub/artifact-templates/">Use the template</a>.</li>
      <li><strong>Validate with a test transaction.</strong> Run a controlled test through the fixed interface. Verify that the data arrives correctly and that monitoring catches intentional errors.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the source schema changes, the data contract must be versioned and consumers must be notified before the change is deployed.</li>
      <li>If a field is mapped incorrectly, fix the mapping before correcting data in the target; otherwise the next load will reintroduce the error.</li>
      <li>If reference data mismatch causes the failure, synchronize codes before reprocessing payloads.</li>
      <li>If the payload exceeds size limits, split the payload or increase the limit; do not silently truncate data.</li>
      <li>If validation fails at the target, add validation at the source or in the integration layer; do not weaken target validation.</li>
      <li>If an interface has no owner, assign one before designing fixes; unmaintained interfaces break again.</li>
      <li>If the failure type is unknown, add logging and payload capture before the next occurrence; do not guess.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Interface Ownership Matrix entry</strong> — documented interface with owners and SLA. <a href="/skill-hub/artifact-templates/">See Artifact Templates</a>.</li>
      <li><strong>Integration Failure Review</strong> — classified failure, root cause, fix, and monitoring. <a href="/skill-hub/artifact-templates/">See Artifact Templates</a>.</li>
      <li><strong>Data Contract</strong> — schema, validation, format, frequency, and change rules.</li>
      <li><strong>Mapping Validation Test</strong> — automated or manual test that verifies source-to-target mapping.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Data Contract (compact)</h3>
    <pre><code>---
contract: Data Interface
id: DC-001
interface: Customer Master to CRM
version: 2.1
status: active
---

## Schema
| Source Field | Source Type | Target Field | Target Type | Required | Validation |
|--------------|-------------|--------------|-------------|----------|------------|
| KUNNR | CHAR(10) | customer_id | VARCHAR(20) | Yes | Numeric, leading zeros preserved |
| NAME1 | CHAR(40) | name | VARCHAR(100) | Yes | Trim trailing spaces |
| STCD1 | CHAR(20) | tax_number | VARCHAR(20) | Conditional | Required if country = DE |
| LAND1 | CHAR(3) | country_code | CHAR(2) | Yes | Must exist in target country list |

## Format
- Payload: JSON
- Encoding: UTF-8
- Max size: 512 KB
- Array max: 100 customers per message

## Frequency
- Real-time for changes
- Full sync: daily at 02:00 UTC

## Error handling
- Schema violation: reject with 400, log error, alert integration owner
- Reference data mismatch: quarantine payload, alert data steward
- Size limit exceeded: split payload, alert technical owner

## Change process
- Minor changes: notify consumers 5 business days in advance
- Major changes: version bump, consumer migration required
- Notification: email to interface owners + wiki update
</code></pre>

    <h3>Mapping Validation Checklist</h3>
    <pre><code>| Check | Method | Owner | Frequency | Last Run | Status |
|-------|--------|-------|-----------|----------|--------|
| All source fields mapped | Compare source schema to mapping doc | Integration Lead | Monthly | 2026-06-01 | Pass |
| Target constraints satisfied | Test payload against target validation | QA | Weekly | 2026-06-08 | Pass |
| Reference data sync | Compare code lists in source and target | Data Steward | Daily | 2026-06-09 | Fail — 3 missing codes |
| Payload size within limit | Monitor message broker metrics | Ops | Continuous | 2026-06-09 | Pass |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The interface has a named technical owner, business owner, and operational owner.</li>
      <li>Source and target schemas are documented and compared.</li>
      <li>Every source field is mapped to a target field or explicitly marked as unmapped.</li>
      <li>The failure is classified into a specific type, not described as "integration error."</li>
      <li>The fix addresses the root cause, not just the symptom.</li>
      <li>A data contract exists with schema, validation, format, frequency, and change rules.</li>
      <li>Monitoring checks schema, mapping, reference data, size, and error rate.</li>
      <li>A test transaction has validated the fix and the monitoring.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Fixing the target data without fixing the mapping or source. <strong>Consequence:</strong> The next integration run reintroduces the same error; the fix becomes a recurring manual task.</li>
      <li><strong>Mistake:</strong> Weakening target validation to accept bad data. <strong>Consequence:</strong> The target system becomes polluted; downstream reports and processes fail.</li>
      <li><strong>Mistake:</strong> Changing a schema without versioning or notification. <strong>Consequence:</strong> All consumers break simultaneously; incident volume spikes.</li>
      <li><strong>Mistake:</strong> Ignoring payload size and frequency limits. <strong>Consequence:</strong> Silent message loss during peak hours; data gaps are discovered days later.</li>
      <li><strong>Mistake:</strong> Documenting the interface in a wiki with no link to the actual code or configuration. <strong>Consequence:</strong> Documentation drifts from reality; troubleshooting takes longer.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Start with the exact failure.</strong> Ask for: interface ID, error message, payload sample, and timestamp. Do not proceed with "the integration is not working."</li>
      <li><strong>Compare schemas explicitly.</strong> List source fields and target fields side by side. Identify mismatches. Do not assume the mapping is correct.</li>
      <li><strong>Check reference data.</strong> If codes or identifiers are involved, verify they exist in the target. Reference data mismatch is a common hidden cause.</li>
      <li><strong>Classify the failure type.</strong> Use the defined types. If none fit, say "unknown" and propose logging improvements.</li>
      <li><strong>Produce a data contract.</strong> Even for existing interfaces, document the contract that should have existed. This prevents future drift.</li>
      <li><strong>Produce artifacts, not advice.</strong> Output an Integration Failure Review and a Data Contract in the templates provided.</li>
      <li><strong>Link to Atlas diagnostics.</strong> If the integration involves SAP, link to <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a>, <a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a>, or <a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP CVI Synchronization Diagnostics</a>.</li>
      <li><strong>Handle missing information.</strong> If schema documentation or payload samples are unavailable, produce a collection checklist and ask the user to gather them.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/dama-dmbok/reference-data-management-working-skill/">Reference Data Management</a> — when code values cause integration failures.</li>
      <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> — when data defects need deeper tracing.</li>
      <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> — when the data path across systems is unclear.</li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — when ownership gaps block resolution.</li>
      <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — when error handling patterns need design.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — classifying IDoc failures.</li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — BP replication data issues.</li>
      <li><a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP CVI Synchronization Diagnostics</a> — customer-vendor integration data issues.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — formal agreements at interface boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of data integration and interoperability practice. It is not official DAMA-DMBOK, SAP, or API design documentation. It has been applied in SAP-centric and API-centric integration contexts but may need adaptation for event-driven architectures, streaming platforms, or microservices mesh.</p>
    <p>Limitations: This skill does not cover advanced API gateway configuration, message broker tuning, or cloud integration platform administration. It focuses on data-layer diagnosis, contract design, and validation suitable for integration analysts and data stewards.</p>
  </section>
</article>
