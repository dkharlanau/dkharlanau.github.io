---
layout: default
title: "Interface Requirement Analysis Working Skill"
description: "Define what data crosses a system boundary, in which direction, under what conditions, and with what quality and error-handling requirements."
permalink: /skill-hub/systems-analysis/interface-requirement-analysis-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/systems-analysis/">Systems Analysis</a></li>
    <li aria-current="page">Interface Requirement Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Systems Analysis</p>
  <h1>Interface Requirement Analysis</h1>
  <p class="lead">Define what data crosses a system boundary, in which direction, under what conditions, and with what quality and error-handling requirements.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill produces a clear, stakeholder-validated specification of what an interface must do before any technical design begins. It answers: what business event triggers data to cross a boundary, which data elements are required, who owns each element, how often the transfer must happen, what quality and validation rules apply, and what happens when something fails. The output bridges business needs and integration architecture, preventing scope creep and late discovery of mismatched expectations.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Business needs to send sales orders from SAP S/4HANA to a third-party logistics platform.</li>
      <li>A new vendor onboarding process requires master data synchronization from SAP MDG to an external procurement system.</li>
      <li>Finance requires invoice data from SAP S/4HANA to a data warehouse, with a defined frequency and format.</li>
      <li>An incident reveals that an existing interface has no documented error-handling requirements, and teams argue about who owns the failure.</li>
      <li>Procurement wants real-time purchase order confirmations from suppliers, but the current interface is batch-only.</li>
      <li>You are scoping an integration project and need to separate functional requirements from non-functional requirements before the technical team estimates effort.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: Sales order outbound to 3PL with missing error handling</h3>
    <p>A company sends SAP S/4HANA sales orders to a third-party logistics platform via IDoc. The interface transmits order header, items, and schedule lines. The 3PL rejects incomplete orders, but the interface requirement never specified a retry policy, an alert threshold, or a fallback action. When the 3PL returns a rejection, the IDoc status remains 53 (success) because the technical handshake succeeded, but the business process stops. The requirement analysis reveals that functional error handling was never defined, and the non-functional requirement for latency was described as "as soon as possible" instead of a specific SLA.</p>

    <h3>Example 2: MDG business partner to Salesforce with identity mismatch</h3>
    <p>SAP MDG distributes customer master data to Salesforce. The functional requirement assumed that MDG would send the Salesforce external ID, but MDG does not store it. The data element boundary was never analyzed: MDG owns the SAP customer number, Salesforce owns the external ID, and the integration middleware performs the mapping. The interface requirement analysis shows that the mapping ownership was undefined, leading to duplicate records in Salesforce when the mapping table was corrupted.</p>

    <h3>Example 3: Material master bidirectional sync with PLM bypassing approval</h3>
    <p>A material master interface between SAP S/4HANA and a PLM system is bidirectional: basic data and classification flow from PLM to S/4HANA, and procurement-relevant data flows back. The functional requirement did not specify who owns the approval step when PLM changes overwrite S/4HANA data. The non-functional requirement did not specify a maximum latency for the reverse flow. As a result, a PLM change reached S/4HANA production before the procurement team could review it, causing a purchase order with incorrect material data.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Source system name, version, and primary purpose (one sentence).</li>
      <li>Target system name, version, and primary purpose (one sentence).</li>
      <li>Business process or event that triggers the need for data transfer (e.g., sales order creation, material master release, invoice posting).</li>
      <li>Data element list required by the target system, with format, length, and mandatory/optional classification.</li>
      <li>System of record assignment for each data element.</li>
      <li>Frequency and volume profile: expected transfers per hour, day, or month; peak load timing.</li>
      <li>Non-functional requirements from business: maximum latency, availability window, throughput, security class.</li>
      <li>Error handling expectations from business and operations: retry count, alert threshold, escalation path, manual fallback.</li>
      <li>Data ownership and governance rules: who can create, change, and approve each data element.</li>
      <li>Existing interface documentation, API specifications, or data contracts (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What business event triggers the need for data to cross this boundary? Is it a creation, an update, a deletion, or a scheduled batch?</li>
      <li>Which system is the system of record for each data element that crosses the boundary?</li>
      <li>What happens if the interface is unavailable for 1 hour? For 1 day? Does the business process stop, queue, or proceed with stale data?</li>
      <li>What validation must occur before data leaves the source system? What validation must occur after it arrives at the target?</li>
      <li>How are duplicates detected and handled? Is there a unique key that both systems agree on?</li>
      <li>What is the maximum acceptable latency from the business event to data delivery at the target?</li>
      <li>Who owns the interface when it fails: the source system team, the target system team, or the integration team?</li>
      <li>What is the escalation path if data quality errors are detected at the boundary after delivery?</li>
      <li>Does the target system require data in a different format, code set, or unit of measure than the source?</li>
      <li>Is there a requirement for audit trail, logging, or compliance documentation across the boundary?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the business event and trigger.</strong> Define the exact business event (sales order created, material released, invoice posted) that causes data to cross the boundary. If the trigger is not a business event but a schedule, state the schedule and the business reason.</li>
      <li><strong>Define the data boundary.</strong> List every data element that must cross. For each element, state whether it is created, updated, or only referenced. Identify what data stays inside each system.</li>
      <li><strong>Classify data elements by ownership and direction.</strong> For each element, name the system of record. Classify direction as outbound (source to target), inbound (target to source), or bidirectional. If direction is bidirectional, define the trigger for each direction separately.</li>
      <li><strong>Specify frequency, volume, and timing.</strong> Quantify how often transfers occur, how many records per transfer, and whether timing is real-time, near-real-time, hourly, daily, or event-driven. Identify peak periods.</li>
      <li><strong>Define transformation and validation rules.</strong> For each data element that changes format, code, or structure across the boundary, document the transformation rule. Define validation rules at the source exit and the target entry.</li>
      <li><strong>Define error handling and recovery rules.</strong> For each failure mode (source unavailable, target unavailable, data validation failure, duplicate detected, timeout), specify the expected behavior: retry, alert, queue, manual fallback, or abort.</li>
      <li><strong>Define non-functional requirements.</strong> Translate business needs into measurable constraints: maximum latency in seconds, minimum availability percentage, maximum throughput in records per minute, security classification, and retention requirements.</li>
      <li><strong>Validate with stakeholders.</strong> Review the requirement with the source system owner, target system owner, business process owner, and integration team. Confirm that each party agrees on ownership, error handling, and SLAs.</li>
      <li><strong>Classify and document.</strong> Separate functional requirements (what data, when, how validated) from non-functional requirements (how fast, how available, how secure). Publish the requirement before technical design begins.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If data is created in the source and consumed in the target, the direction is outbound. If the target updates the source, the direction is inbound or bidirectional, and each direction must be specified separately.</li>
      <li>If the interface specification lacks an error-handling requirement for at least three failure modes (source unavailable, target unavailable, data validation failure), do not approve it for design.</li>
      <li>If the target system has stricter validation than the source, define a transformation or enrichment step; do not assume the source will change.</li>
      <li>If the interface is real-time but one system is batch-oriented, flag a frequency mismatch and require a business decision.</li>
      <li>If duplicate detection is not specified, assume duplicates are possible and require a detection and handling rule.</li>
      <li>If data ownership is unclear for any element, produce an ownership matrix before interface design proceeds.</li>
      <li>If the volume exceeds 10,000 records per hour or the latency requirement is under 5 seconds, require performance testing as a non-functional requirement.</li>
      <li>If the interface crosses an organizational boundary (external vendor, SaaS, acquired company), include data classification, compliance, and audit requirements explicitly.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Interface Requirement Specification</strong> — Document containing business event, data boundary, element ownership, direction, frequency, validation, error handling, and non-functional requirements.</li>
      <li><strong>Data Element Boundary Table</strong> — Table of all data elements with source system of record, target requirement, direction, mandatory/optional status, and transformation rule.</li>
      <li><strong>Error Handling Specification</strong> — For each failure mode, the expected behavior, retry policy, alert threshold, escalation path, and manual fallback.</li>
      <li><strong>Frequency and Volume Profile</strong> — Quantified transfer schedule, peak load, and growth assumption.</li>
      <li><strong>Interface Ownership Matrix</strong> — For each data element and failure mode, the named owner and escalation contact.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Interface Requirement Analysis (Markdown format)</h3>
    <pre><code>## Interface: &lt;Source&gt; to &lt;Target&gt;

### Business trigger
<!-- One sentence. Example: Sales order created in SAP S/4HANA (type OR) triggers outbound transfer to 3PL. -->

### Data boundary

| Data Element | Source System of Record | Direction | Mandatory? | Format (Source) | Format (Target) | Transformation Rule | Validation (Exit) | Validation (Entry) |
|--------------|------------------------|-----------|------------|-----------------|-----------------|---------------------|-------------------|--------------------|
| Order number | SAP S/4HANA | Outbound | Yes | CHAR 10 | VARCHAR 20 | Prefix with region code | Exists in VBAK | Unique in 3PL |
| Delivery block | SAP S/4HANA | Outbound | No | CHAR 2 | VARCHAR 5 | Map internal code to 3PL code | Valid in TVLS | Recognized by 3PL |
| External ID | 3PL | Inbound | Yes | VARCHAR 30 | CHAR 20 | Strip leading zeros | 3PL validation | Exists in mapping table |
| Shipment status | 3PL | Inbound | No | VARCHAR 10 | CHAR 2 | Map 3PL status to SAP delivery status | 3PL format check | Valid in TVLS |

### Frequency and volume

| Scenario | Frequency | Volume | Peak Timing | Latency Requirement |
|----------|-----------|--------|-------------|---------------------|
| Standard orders | Event-driven | 500/hour | 09:00–11:00 | < 60 seconds |
| Bulk orders | Daily batch | 10,000/day | 02:00–04:00 | < 30 minutes |
| Returns | Event-driven | 50/hour | 14:00–16:00 | < 5 minutes |

### Error handling

| Failure Mode | Retry Policy | Alert Threshold | Escalation Path | Manual Fallback |
|--------------|--------------|-----------------|-----------------|-----------------|
| Source system unavailable | Retry 3x, 5 min interval | After 3 failures | SAP Basis team | Manual IDoc reprocessing (BD87) |
| Target system unavailable | Retry 5x, exponential backoff | After 5 failures | Integration team | Hold in queue, notify logistics supervisor |
| Data validation failure (exit) | No retry | Immediate | Source data steward | Correct in SAP (VA02), re-trigger |
| Data validation failure (entry) | No retry | Immediate | Target data steward | Correct in 3PL, request re-sync |
| Duplicate detected | No retry | Immediate | Integration team | Manual deduplication by logistics supervisor |
| Timeout (> 60s) | Retry 2x | After 2 failures | Integration team | Manual check in SXMB_MONI / WE02 |

### Non-functional requirements

| Attribute | Requirement | Measurement Method | Owner |
|-----------|-------------|--------------------|-------|
| Latency | < 60 seconds (event), < 30 min (batch) | IDoc creation to 3PL acknowledgement timestamp | Integration team |
| Availability | 99.5% during business hours (08:00–18:00) | Monitoring dashboard uptime | Integration team |
| Throughput | 500 events/hour sustained, 1000/hour peak | Message queue depth metric | Integration team |
| Security | Data encrypted in transit (TLS 1.2+) | Certificate audit | Security team |
| Retention | IDoc logs retained 90 days | SAP archiving policy | SAP Basis team |

### Ownership matrix

| Element / Failure | Source Owner | Target Owner | Integration Owner | Escalation Contact |
|-------------------|--------------|--------------|-------------------|--------------------|
| Order number | Sales process owner | Logistics supervisor | Integration team | Integration lead |
| Delivery block | Sales config owner | Logistics supervisor | Integration team | Integration lead |
| Source unavailable | SAP Basis team | — | Integration team | SAP Basis lead |
| Target unavailable | — | 3PL support | Integration team | 3PL account manager |
| Data validation | Source data steward | Target data steward | Integration team | Data governance lead |

### What this interface does NOT do

- Does not perform business logic validation (credit check, pricing) — that happens inside SAP.
- Does not archive data long-term — both systems retain independently.
- Does not serve as a backup for either system.
- Does not handle real-time inventory queries — only order and status events.
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every data element has a defined source system of record.</li>
      <li>Every interface has a named business event trigger, not a technical schedule alone.</li>
      <li>Error handling is specified for at least three failure modes: source unavailable, target unavailable, and data validation failure.</li>
      <li>Frequency and volume are quantified, not described as "as needed" or "as soon as possible."</li>
      <li>Non-functional requirements include latency, availability, and throughput with measurable numbers.</li>
      <li>Ownership is assigned for source, target, and integration for each data element and failure mode.</li>
      <li>A business stakeholder has validated the requirement, not only technical staff.</li>
      <li>The "does NOT do" section clarifies boundaries to prevent scope creep.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Documenting technical interface design (protocol, endpoints, payload structure) instead of requirements. <strong>Consequence:</strong> The solution is locked in before business needs are fully understood, and change requests are expensive.</li>
      <li><strong>Mistake:</strong> Omitting error handling requirements. <strong>Consequence:</strong> Production failures require ad-hoc decisions, cause SLA breaches, and damage trust between teams.</li>
      <li><strong>Mistake:</strong> Confusing functional requirements with non-functional ones. <strong>Consequence:</strong> Performance, availability, and reliability issues are discovered late in integration testing or after go-live.</li>
      <li><strong>Mistake:</strong> Assuming the target system can accept whatever the source sends. <strong>Consequence:</strong> Data transformation gaps are discovered during integration testing, causing project delays and data quality incidents.</li>
      <li><strong>Mistake:</strong> Not defining ownership for each data element and failure mode. <strong>Consequence:</strong> When the interface fails, teams argue about responsibility and resolution time increases.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — Generic interface wish list</h3>
    <blockquote>
      <p>The interface should be secure and reliable. It should use a modern API standard like REST or OData. The data should be transferred in JSON format. Error handling should be robust, with retries and logging. The system should be available during business hours. Performance should be fast enough for users.</p>
    </blockquote>
    <p><strong>Why it is weak:</strong> No specific data elements, no direction, no ownership, no quantified SLAs, no failure modes, no business event trigger. It is a list of aspirations that cannot be reviewed, tested, or held accountable.</p>

    <h3>Strong output — Copy-paste ready interface requirement table</h3>
    <pre><code>## Interface: SAP S/4HANA (IDoc) to 3PL (REST API)

### Business trigger
Sales order created or changed in SAP S/4HANA (type OR) triggers
outbound transfer to 3PL within 60 seconds of save.

### Data elements

| Element | Source | Direction | Mandatory | Target format | Transform | Exit validation | Entry validation |
|---------|--------|-----------|-----------|---------------|-----------|-----------------|------------------|
| VBELN | SAP | Outbound | Yes | VARCHAR 20 | Prefix "SO-" | Exists in VBAK | Unique in 3PL |
| POSNR | SAP | Outbound | Yes | VARCHAR 6 | Zero-pad to 6 | Exists in VBAP | Matches header |
| MATNR | SAP | Outbound | Yes | VARCHAR 18 | No leading zeros | Exists in MARA | Valid in 3PL catalog |
| LFIMG | SAP | Outbound | Yes | DECIMAL | Same | > 0 | > 0 |
| Delivery block | SAP | Outbound | No | VARCHAR 5 | Map TVLS to 3PL code | Valid in TVLS | Recognized by 3PL |

### Error handling

| Failure | Retry | Alert | Escalation | Fallback |
|---------|-------|-------|------------|----------|
| SAP IDoc failure | 3x, 5 min | After 3 | SAP Basis | BD87 manual reprocess |
| 3PL HTTP 4xx | No retry | Immediate | Integration | Correct data in SAP, re-trigger |
| 3PL HTTP 5xx | 5x, exponential | After 5 | 3PL support | Queue + notify logistics lead |
| Timeout > 60s | 2x | After 2 | Integration | SXMB_MONI check + manual retry |

### Non-functional requirements

- Latency: IDoc created to 3PL ACK < 60s (p95)
- Availability: 99.5% during 08:00–18:00 CET
- Throughput: 500 orders/hour sustained, 1000/hour peak
- Security: TLS 1.2+, mutual auth certificate
- Retention: IDoc logs 90 days, 3PL ACK logs 1 year
</code></pre>
    <p><strong>Why it is strong:</strong> It names the exact data elements, transformations, validations, retry policies, and SLAs. An integration team can estimate effort from this, a tester can write test cases, and an operations team can set up monitoring.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>You are a systems analyst defining interface requirements for an enterprise SAP landscape. Before you produce any output, gather:
1. The source system name and the target system name.
2. The business event that triggers data transfer (e.g., sales order created, material released, invoice posted).
3. The data element list required by the target system, with format and mandatory/optional status.
4. The system of record for each data element.
5. The frequency, volume, and peak load from the business process owner.
6. The business-defined maximum latency and availability expectations.
7. The error handling expectations from operations: retry, alert, escalation, manual fallback.

Produce the output in the Interface Requirement Analysis template format: data element boundary table, frequency and volume profile, error handling table, non-functional requirements table, ownership matrix. Separate functional requirements from non-functional requirements. For every data element, state the source of record, direction, and validation rules. For every failure mode, state the retry policy, alert threshold, and escalation path. End with a "does NOT do" section.
</code></pre>

    <ul>
      <li><strong>Do</strong> gather the business event, data element list, and stakeholder expectations before producing any output. Do not guess requirements.</li>
      <li><strong>Do</strong> separate functional requirements (what data, when, how validated) from non-functional requirements (how fast, how available, how secure).</li>
      <li><strong>Do</strong> specify error handling for at least three failure modes: source unavailable, target unavailable, and data validation failure.</li>
      <li><strong>Do</strong> name the system of record for every data element. If ownership is unclear, flag it and ask for assignment.</li>
      <li><strong>Do</strong> quantify frequency, volume, and latency. "As soon as possible" is not a requirement.</li>
      <li><strong>Do</strong> link to Atlas integration patterns when the interface involves SAP S/4HANA, MDG, or SAP Integration Suite.</li>
      <li><strong>Don't</strong> write technical design. Do not specify protocols, endpoints, or payload structures unless the stakeholder explicitly requested them.</li>
      <li><strong>Don't</strong> omit the ownership matrix. An interface without ownership will fail in production with no one accountable.</li>
      <li><strong>Don't</strong> skip the "does NOT do" section. Scope creep in interface projects is common and expensive.</li>
      <li><strong>Don't</strong> invent data elements or SLAs. If the stakeholder cannot provide them, list placeholders and ask for confirmation.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a> — Define the system boundaries where the interface operates.</li>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Technical design and implementation of API-based interfaces.</li>
      <li><a href="/skill-hub/dama-dmbok/data-integration-interoperability-working-skill/">Data Integration and Interoperability</a> — How data flows across systems and how interoperability is governed.</li>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation</a> — How to extract and structure stakeholder needs before interface analysis begins.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> — Patterns and constraints for SAP system interfaces.</li>
      <li><a href="/atlas/concepts/api-contracts/">API Contracts</a> — How API agreements define interface boundaries and responsibilities.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — How data agreements constrain what crosses system boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of interface requirements analysis for enterprise and SAP systems. It is not official BABOK, TOGAF, or SAP integration documentation. It focuses on the practical subset of requirements work that prevents integration failures before technical design begins. It does not cover detailed protocol design, security architecture, or infrastructure sizing. Use it as a structured starting point for requirements workshops and stakeholder reviews, not as a comprehensive framework substitute.</p>
  </section>
</article>
