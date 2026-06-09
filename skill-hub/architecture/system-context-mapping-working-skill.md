---
layout: default
title: "System Context Mapping"
description: "Define what a system does, what it depends on, what depends on it, and where the integration boundaries lie."
permalink: /skill-hub/architecture/system-context-mapping-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/architecture/">Architecture</a></li>
    <li aria-current="page">System Context Mapping</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Architecture</p>
  <h1>System Context Mapping</h1>
  <p class="lead">Define what a system does, what it depends on, what depends on it, and where the integration boundaries lie.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill produces a clear, bounded description of a single system within its environment. It answers: what is this system's responsibility, what does it need from other systems, what do other systems need from it, and where are the integration boundaries? The output is used during design, onboarding, incident response, and change impact analysis to prevent scope creep and boundary confusion.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You are designing a new system and need to define what it will and will not do.</li>
      <li>You are onboarding a development or operations team and they need to understand system boundaries.</li>
      <li>An incident spans multiple systems and no one can agree which system is responsible for the failure.</li>
      <li>You are planning a change to one system and need to know which other systems might break.</li>
      <li>You are documenting a legacy system whose original architects have left the organization.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: SAP MDG as master data hub</h3>
    <p>A company uses SAP MDG to govern material and customer master data. The system context map defines that MDG receives creation requests from SAP S/4HANA (via workflow), enriches and validates them, and distributes golden records to S/4HANA, Salesforce, and the data warehouse. The map shows that MDG does not perform transactional processing, does not store historical pricing, and does not send data to the logistics platform. This boundary prevents a project from incorrectly asking MDG to handle shipment tracking data.</p>

    <h3>Example 2: Custom pricing engine on SAP BTP</h3>
    <p>A development team builds a custom pricing engine on SAP BTP that calculates complex regional discounts. The system context map defines that the engine receives product and customer data from S/4HANA via OData, receives competitor price feeds from an external market data service, and returns calculated prices to S/4HANA and a mobile sales app. The map explicitly states that the engine does not update master data, does not handle currency conversion, and does not store historical prices. This prevents scope creep during enhancement requests.</p>

    <h3>Example 3: Data warehouse in a mixed landscape</h3>
    <p>A SAP Datasphere instance serves as the enterprise data warehouse. The context map shows that it receives replicated data from S/4HANA CDS views, master data from MDG, and sales forecasts from Salesforce. It provides reporting to Power BI, self-service analytics to business users, and aggregated feeds to a planning system. The map records that Datasphere does not receive real-time transactional events, does not write back to S/4HANA, and is not the system of record for any master data. This boundary prevents operational teams from expecting real-time operational reporting.</p>

    <h3>Example 4: Integration middleware after a merger</h3>
    <p>After a merger, SAP Integration Suite becomes the central integration layer. The context map defines that it routes messages between S/4HANA, the acquired company's ERP, Salesforce, and logistics platforms. It performs protocol translation, message mapping, and basic error handling. It does not store business data long-term, does not perform business logic validation, and does not serve as a backup for failed downstream systems. This clarity prevents the integration team from being asked to implement data archiving or business rule enforcement.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The system name, version, and primary purpose (one sentence).</li>
      <li>List of systems that send data or events to this system (upstream dependencies).</li>
      <li>List of systems that receive data or events from this system (downstream dependencies).</li>
      <li>Human actors who interact with the system (users, administrators, data stewards).</li>
      <li>Data flows: what data enters, what data leaves, and what data is stored.</li>
      <li>Integration mechanisms: APIs, events, files, database links, message queues.</li>
      <li>Known boundary disputes: areas where other teams have asked this system to do something outside its scope.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>If this system were removed tomorrow, which business processes would stop and which would continue?</li>
      <li>Which data does this system create, which does it receive, and which does it only pass through?</li>
      <li>What is the one thing this system does that no other system in the landscape does?</li>
      <li>Which requests from other teams have you rejected because they were outside this system's scope?</li>
      <li>What is the slowest or most unreliable integration point, and what happens when it fails?</li>
      <li>Who is responsible for this system when it is healthy, and who is responsible when it fails?</li>
      <li>What would a new developer get wrong about this system's boundaries in their first week?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Name the system and state its primary purpose.</strong> One sentence. If you cannot state it in one sentence, the system's scope is probably undefined.</li>
      <li><strong>Identify the system in the center of a context diagram.</strong> Draw or describe the system as a single box. Everything else is outside.</li>
      <li><strong>Map upstream systems.</strong> List every system that sends data, events, commands, or requests to this system. For each, note the data, the mechanism, and the frequency.</li>
      <li><strong>Map downstream systems.</strong> List every system that receives data, events, or responses from this system. For each, note the data, the mechanism, and whether the delivery is synchronous or asynchronous.</li>
      <li><strong>Map human actors.</strong> List users, administrators, and operators who interact with the system. Note what they do and what they expect.</li>
      <li><strong>Define what the system does not do.</strong> Explicitly list responsibilities that are commonly assumed but outside scope. This is the most valuable part of the map.</li>
      <li><strong>Map data at rest.</strong> Note what data the system stores, how long it retains it, and whether it is the system of record for that data.</li>
      <li><strong>Identify integration boundaries.</strong> For each interface, note the protocol, the data format, the ownership, and the error handling approach.</li>
      <li><strong>Validate with stakeholders.</strong> Review the map with the system owner, upstream and downstream system owners, and operations. Correct misattributions.</li>
      <li><strong>Publish and maintain.</strong> Store the map where developers, operations, and project teams can find it. Review when the system changes or when boundary disputes recur.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a system both sends and receives data from another system, draw two separate arrows, not one bidirectional line, because the failure modes differ.</li>
      <li>If an integration uses a shared database or file system, classify it as a high-coupling boundary that requires explicit ownership.</li>
      <li>If a human actor performs a function that could be automated but is not, note it as a manual boundary, not as a system capability.</li>
      <li>If the system stores data but is not the system of record, note the actual system of record and the synchronization mechanism.</li>
      <li>If a boundary is disputed between two teams, record both views, flag the dispute, and escalate to architecture governance.</li>
      <li>If the context map contains more than 15 external systems, consider decomposing into subsystem context maps.</li>
      <li>If an upstream system is external or SaaS, note the SLA, support channel, and escalation path explicitly.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>System Context Map</strong> — Diagram or structured text showing the system at the center with upstream, downstream, and human actors.</li>
      <li><strong>Boundary Definition Document</strong> — Text description of what the system does, what it does not do, and why.</li>
      <li><strong>Interface Summary</strong> — Table of all integration points with direction, data, mechanism, and ownership.</li>
      <li><strong>Data Responsibility Matrix</strong> — Table of data elements stored, with system of record, retention, and synchronization notes.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>System Context Map (Text format)</h3>
    <pre><code>## System: &lt;Name&gt;

### Primary purpose
<!-- One sentence. Example: Govern and distribute golden master data for materials and customers. -->

### Upstream systems (send to this system)

| System | Data / Event | Mechanism | Frequency | Owner |
|--------|--------------|-----------|-----------|-------|
| SAP S/4HANA | Material creation request | MDG workflow trigger | On demand | MDM Team |
| Salesforce | Customer update event | Event Mesh | Real-time | CRM Team |

### Downstream systems (receive from this system)

| System | Data / Event | Mechanism | Frequency | Owner |
|--------|--------------|-----------|-----------|-------|
| SAP S/4HANA | Golden material record | IDoc | Batch, hourly | MDM Team |
| Data Warehouse | Master data snapshot | OData extract | Daily | Data Team |

### Human actors

| Actor | Action | System area |
|-------|--------|-------------|
| Data Steward | Review and approve master data changes | MDG workflow inbox |
| MDM Administrator | Monitor distribution errors | MDG error log |

### What this system does NOT do

- Does not perform transactional processing (sales, procurement, production).
- Does not store historical pricing or contract terms.
- Does not send data directly to the logistics platform.
- Does not replace source system validation; it adds governance layer validation.

### Data at rest

| Data element | System of record | Retention | Notes |
|--------------|------------------|-----------|-------|
| Golden material master | This system (MDG) | 10 years | Archival after 2 years of inactivity |
| Customer master | This system (MDG) | 10 years | GDPR deletion workflow required |

### Integration boundaries

| Interface ID | Direction | Protocol | Data format | Error handling | Owner |
|--------------|-----------|----------|-------------|----------------|-------|
| IF-001 | Inbound | OData | JSON | Retry 3x, then alert | Integration Team |
| IF-002 | Outbound | IDoc | EDIFACT | Queue and retry | Integration Team |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The system's primary purpose is stated in one sentence.</li>
      <li>Every upstream and downstream system is named with specific data and mechanism.</li>
      <li>At least three "does NOT do" items are listed to clarify boundaries.</li>
      <li>Every integration point has a defined error handling approach.</li>
      <li>Data at rest is listed with system of record and retention.</li>
      <li>The map has been validated by the system owner and at least one adjacent system owner.</li>
      <li>Human actors are included, not just systems.</li>
      <li>No boundary dispute remains unflagged or unresolved.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Drawing the system context map as a network diagram without defining boundaries. <strong>Consequence:</strong> The diagram shows connectivity but not responsibility, and incident response teams still argue about ownership.</li>
      <li><strong>Mistake:</strong> Omitting what the system does not do. <strong>Consequence:</strong> Scope creep is inevitable because every adjacent team assumes the system can absorb new responsibilities.</li>
      <li><strong>Mistake:</strong> Treating a shared database as a clean integration boundary. <strong>Consequence:</strong> Changes by one team break another team's queries, and no one knows who is responsible.</li>
      <li><strong>Mistake:</strong> Creating the map once and never updating it. <strong>Consequence:</strong> New integrations, retired systems, and changed data flows make the map misleading.</li>
      <li><strong>Mistake:</strong> Including only technical systems and ignoring human actors. <strong>Consequence:</strong> Manual steps, approvals, and data steward actions are invisible, leading to automation proposals that ignore human checkpoints.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ol>
      <li><strong>Start with the primary purpose.</strong> Do not produce a context map until the system's one-sentence purpose is confirmed.</li>
      <li><strong>Use the text template.</strong> Generate the System Context Map in the exact Markdown template format. Include all sections: upstream, downstream, actors, does NOT do, data at rest, integration boundaries.</li>
      <li><strong>Be specific about mechanisms.</strong> Do not write "integrated with SAP." Write "receives material master via IDoc from SAP S/4HANA, batch hourly."</li>
      <li><strong>Explicitly list negative boundaries.</strong> The "does NOT do" section is mandatory. Ask the user for common scope creep requests if they cannot list them.</li>
      <li><strong>Flag missing ownership.</strong> If any integration point lacks an owner, flag it and ask for assignment.</li>
      <li><strong>Do not invent systems.</strong> If the user describes a system but cannot name adjacent systems, list placeholders and ask for confirmation.</li>
      <li><strong>Link to Atlas for integration patterns.</strong> If the system is part of an SAP landscape, reference <a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> and <a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> for pattern guidance.</li>
    </ol>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/capability-mapping-working-skill/">Capability Mapping</a> — Map the business functions that the system supports.</li>
      <li><a href="/skill-hub/architecture/solution-architecture-review-working-skill/">Solution Architecture Review</a> — Review a design against the boundaries this map defines.</li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — Define ownership for each integration boundary.</li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a> — Assess how changes affect the mapped boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> — Patterns and constraints for SAP system boundaries.</li>
      <li><a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> — How event patterns affect system context and coupling.</li>
      <li><a href="/atlas/concepts/api-contracts/">API Contracts</a> — How API agreements define integration boundaries.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — How data agreements constrain what crosses system boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of system context mapping practice. It is not official C4 model, UML, or ArchiMate documentation. It focuses on the lightweight text-based context map suitable for project and operational use. It does not cover detailed container or component-level decomposition. Use it as a boundary-clarification tool for teams that need to agree on system responsibilities, not as a comprehensive modeling methodology.</p>
  </section>
</article>
