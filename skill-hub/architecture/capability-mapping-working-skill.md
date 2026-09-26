---
layout: default
title: "Capability Mapping"
description: "Map what the organization does, what systems support it, and where gaps exist between business functions and technical enablement."
permalink: /skill-hub/architecture/capability-mapping-working-skill/
last_modified_at: 2026-09-26
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/architecture/">Architecture</a></li>
    <li aria-current="page">Capability Mapping</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Architecture</p>
  <h1>Capability Mapping</h1>
  <p class="lead">Map what the organization does, what systems support it, and where gaps exist between business functions and technical enablement.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill produces a structured view of organizational capabilities and their system support. It answers three questions: <mark class="key-idea">what functions does the organization perform, which systems enable each function, and where is the coverage incomplete, duplicated, or outdated?</mark> The output is used during discovery, transformation planning, and vendor selection to ground conversations in observable reality rather than aspirational diagrams.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You are starting a transformation project and no one can agree on what the current systems actually do.</li>
      <li>A business unit claims a function is unsupported, but IT believes it is already covered.</li>
      <li>You need to evaluate a vendor proposal against actual organizational needs, not just feature lists.</li>
      <li>You are consolidating systems after a merger and need to identify overlap.</li>
      <li>You are scoping an SAP module rollout and need to know which business processes it must cover.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: SAP S/4HANA migration scoping</h3>
    <p>A manufacturing division runs production planning on a legacy MES, inventory on SAP ECC, and scheduling on spreadsheets. The project team needs to know which ECC functions move to S/4, which stay with the MES, and which spreadsheet-based scheduling must be replaced or integrated. Capability mapping reveals that capacity planning is double-maintained in ECC and spreadsheets, creating a data consistency risk.</p>

    <h3>Example 2: Post-merger integration</h3>
    <p>Two companies with separate ERPs merge. The integration team must decide which system becomes the record for each function. Mapping capabilities shows that both companies perform supplier qualification, but one uses a dedicated SRM module while the other uses email and shared folders. <mark class="key-idea">The gap is not technical — it is process maturity</mark> — and the map makes this visible to decision-makers.</p>

    <h3>Example 3: Cloud procurement evaluation</h3>
    <p>A procurement director wants a new e-sourcing platform. IT lists 47 requirements from the vendor. The capability map shows that 12 of those requirements are already met by an existing SAP Ariba module that is underutilized because of poor training. The map prevents redundant purchase and redirects effort toward adoption.</p>

    <h3>Example 4: AI readiness assessment</h3>
    <p>A data science team wants to deploy predictive maintenance models. The capability map reveals that equipment sensor data is collected by SCADA but never reaches the data warehouse, and that maintenance work orders are created in SAP PM but not linked to asset condition. The map identifies the integration and data quality gaps that must close before AI can operate.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Organizational chart or business unit list (to know who does what).</li>
      <li>System inventory with primary function descriptions (not just names and versions).</li>
      <li>Process documentation, SOPs, or training materials (to understand how work is performed).</li>
      <li>Interviews with at least one business representative and one IT representative per major function.</li>
      <li>Existing architecture diagrams, if any (to validate or challenge them).</li>
      <li>Project scope or transformation objectives (to know which capabilities matter most).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What business outcome does this function produce? Who receives it?</li>
      <li>If this system were unavailable for 48 hours, which functions would stop and what would the business consequence be?</li>
      <li>Is this capability performed in one place or in multiple systems with different owners?</li>
      <li>Who is the single person who could explain how this function works end to end?</li>
      <li>What data enters this function, what data leaves it, and who owns each dataset?</li>
      <li>Is this capability automated, semi-automated, or manual? Where are the handoffs?</li>
      <li>What regulation, SLA, or audit requirement applies to this function?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the scope.</strong> <mark class="key-idea">Identify the business domain, time horizon, and decision the map must support.</mark> A map for merger integration has different granularity than a map for module selection.</li>
      <li><strong>Identify capability categories.</strong> Group functions into 5–10 categories relevant to the domain (for example: Plan, Source, Make, Deliver, Sell, Support, Govern). Do not use generic framework categories unless they fit the organization's language.</li>
      <li><strong>List capabilities within each category.</strong> Name each capability as a verb-noun phrase at a consistent level of granularity (for example: "Manage supplier qualification," "Generate production schedule," "Process customer return"). Aim for 15–40 capabilities total.</li>
      <li><strong>Map system support.</strong> For each capability, record which system or systems enable it. Use four support levels: Fully supported, Partially supported, Supported by workaround, Not supported.</li>
      <li><strong>Record ownership.</strong> For each capability, note the business owner (who is accountable for the outcome) and the technical owner (who maintains the supporting system).</li>
      <li><strong>Identify gaps and overlaps.</strong> Flag capabilities with no support, multiple conflicting systems, manual workarounds, or outdated technology. Classify each as: gap, overlap, risk, or technical debt.</li>
      <li><strong>Validate with stakeholders.</strong> Walk the draft map with business and IT representatives separately, then together. Correct misattributions and missing capabilities.</li>
      <li><strong>Produce the final artifact.</strong> Format as a matrix or structured document. Include a summary of top 5 gaps and overlaps with business impact.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Capability mapping decision rules">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Condition</th>
            <th scope="col">Decision</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>No business owner is confirmed.</td>
            <td>Do not assign a system until ownership is clarified.</td>
          </tr>
          <tr>
            <td>Two systems support the same capability with different data.</td>
            <td>Flag a data consistency risk, not just a duplication.</td>
          </tr>
          <tr>
            <td>The capability runs through a spreadsheet or email workflow.</td>
            <td>Classify it as a workaround, not as supported.</td>
          </tr>
          <tr>
            <td>A regulation requires the capability, but it is unsupported.</td>
            <td>Mark it as a compliance gap regardless of business priority.</td>
          </tr>
          <tr>
            <td>The system supports the capability, but the business does not use it.</td>
            <td>Classify it as an adoption gap, not a capability gap.</td>
          </tr>
          <tr>
            <td>The map contains more than 50 capabilities.</td>
            <td>The granularity is probably too fine. Merge related capabilities into higher-level groups.</td>
          </tr>
          <tr>
            <td>A capability cannot be described with one clear verb-noun phrase.</td>
            <td>It is probably a process rather than a capability. Decompose it or rename it.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Deliverables</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Capability mapping deliverables">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Deliverable</th>
            <th scope="col">What it contains</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Capability Map Matrix</th>
            <td>Categories, capabilities, system support levels, owners, and gap flags in one view.</td>
          </tr>
          <tr>
            <th scope="row">Gap and Overlap Register</th>
            <td>Prioritized gaps and overlaps with business impact, risk level, proposed action, and owner.</td>
          </tr>
          <tr>
            <th scope="row">System Coverage Summary</th>
            <td>A per-system view of capabilities that are fully supported, partially supported, or missing.</td>
          </tr>
          <tr>
            <th scope="row">Stakeholder Validation Notes</th>
            <td>Who reviewed the map, what changed after review, and which points remain disputed.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Templates</h2>
    <p>Use the first table to build the capability view. Use the second to turn gaps and overlaps into decisions and actions.</p>

    <h3>Capability Map Matrix</h3>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Capability Map Matrix example">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Category</th>
            <th scope="col">Capability</th>
            <th scope="col">Business owner</th>
            <th scope="col">System</th>
            <th scope="col">Support level</th>
            <th scope="col">Gap type</th>
            <th scope="col">Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Source</td>
            <td>Manage supplier qualification</td>
            <td>Procurement Director</td>
            <td>SAP SRM</td>
            <td>Fully supported</td>
            <td>—</td>
            <td>—</td>
          </tr>
          <tr>
            <td>Source</td>
            <td>Evaluate supplier performance</td>
            <td>Procurement Director</td>
            <td>Excel + Email</td>
            <td>Workaround</td>
            <td>Gap</td>
            <td>No central record; audit risk</td>
          </tr>
          <tr>
            <td>Plan</td>
            <td>Generate production schedule</td>
            <td>Plant Manager</td>
            <td>SAP PP + Excel</td>
            <td>Partial</td>
            <td>Overlap</td>
            <td>Scheduling exists in both; data mismatch weekly</td>
          </tr>
          <tr>
            <td>Deliver</td>
            <td>Process customer return</td>
            <td>Customer Service Lead</td>
            <td>SAP SD</td>
            <td>Fully supported</td>
            <td>—</td>
            <td>—</td>
          </tr>
          <tr>
            <td>Govern</td>
            <td>Maintain material master data</td>
            <td>MDM Lead</td>
            <td>SAP MDG</td>
            <td>Fully supported</td>
            <td>—</td>
            <td>—</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>Gap and Overlap Register</h3>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Gap and Overlap Register example">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Capability</th>
            <th scope="col">Gap type</th>
            <th scope="col">Business impact</th>
            <th scope="col">Risk</th>
            <th scope="col">Proposed action</th>
            <th scope="col">Owner</th>
            <th scope="col">Due date</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>GAP-001</td>
            <td>Evaluate supplier performance</td>
            <td>Missing system</td>
            <td>Audit findings, delayed sourcing</td>
            <td>High</td>
            <td>Implement SRM supplier scorecard or the relevant Ariba capability.</td>
            <td>Procurement Director</td>
            <td>YYYY-MM-DD</td>
          </tr>
          <tr>
            <td>OVL-001</td>
            <td>Generate production schedule</td>
            <td>System overlap</td>
            <td>Weekly reconciliation effort, planning errors</td>
            <td>Medium</td>
            <td>Consolidate scheduling in SAP PP and retire the spreadsheet.</td>
            <td>Plant Manager</td>
            <td>YYYY-MM-DD</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every capability has a named business owner who can confirm its accuracy.</li>
      <li>Every system listed is identifiable by name and version or instance.</li>
      <li>Support levels use the four standard categories consistently.</li>
      <li>At least one gap and one overlap are identified and classified.</li>
      <li>The map has been reviewed by both business and IT stakeholders.</li>
      <li>Capabilities are described at a consistent level of granularity.</li>
      <li>The top 5 gaps and overlaps are summarized with business impact.</li>
      <li>No capability is described as a system feature or a process step.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Common capability mapping mistakes and consequences">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Mistake</th>
            <th scope="col">Consequence</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Mapping systems instead of capabilities</th>
            <td>The map becomes a system inventory with no business meaning, so gaps remain invisible because every system is simply “present.”</td>
          </tr>
          <tr>
            <th scope="row">Using generic framework categories that do not match the organization’s language</th>
            <td>Stakeholders struggle to validate the map because they do not recognize their work in the labels.</td>
          </tr>
          <tr>
            <th scope="row">Treating spreadsheet workarounds as supported capabilities</th>
            <td>Transformation projects underestimate integration, control, and data-quality effort.</td>
          </tr>
          <tr>
            <th scope="row">Creating the map in isolation and presenting it as final</th>
            <td>Business stakeholders reject it because ownership is wrong or shadow processes are missing.</td>
          </tr>
          <tr>
            <th scope="row">Using too many capabilities at too fine a granularity</th>
            <td>The map becomes hard to scan and the important gaps disappear in detail.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ol>
      <li><strong>Gather context first.</strong> Ask for the business domain, scope, and decision the map must support before producing any output.</li>
      <li><strong>Use the organization's language.</strong> Do not impose generic framework categories unless the user confirms they are used internally.</li>
      <li><strong>Separate facts from assumptions.</strong> Label every capability and system assignment as confirmed, inferred, or disputed. Do not present inferred mappings as validated.</li>
      <li><strong>Produce the matrix and register.</strong> Generate the Capability Map Matrix and Gap and Overlap Register as structured Markdown tables. Include placeholder rows with realistic examples.</li>
      <li><strong>Flag missing inputs.</strong> If the user cannot provide business owners, system names, or process descriptions, explicitly list what is missing and how it limits the map's accuracy.</li>
      <li><strong>Avoid generic language.</strong> Do not write "the organization needs to align its capabilities with its strategic objectives." Write "Procurement needs supplier performance evaluation; current workaround is Excel and email."</li>
      <li><strong>Link to Atlas diagnostics.</strong> If the map reveals integration gaps, reference <a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> or <a href="/atlas/concepts/composable-erp-for-sap-operations/">Composable ERP for SAP Operations</a> for deeper diagnostic context.</li>
    </ol>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a> — Define system boundaries within the capability landscape.</li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis</a> — Analyze the difference between current and target states for specific capabilities.</li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a> — Identify and engage the owners needed to validate the capability map.</li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a> — Assess how capability changes affect systems and processes.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-clean-core-strategy/">SAP Clean Core Strategy</a> — How capability mapping supports clean core scoping.</li>
      <li><a href="/atlas/concepts/composable-erp-for-sap-operations/">Composable ERP for SAP Operations</a> — How capabilities map to composable architecture decisions.</li>
      <li><a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> — Diagnostic context for integration gaps found during capability mapping.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of capability mapping practice. It is not official TOGAF or ArchiMate guidance. It focuses on the practical subset used during enterprise discovery and SAP transformation projects. It does not cover detailed business architecture modeling, value stream analysis, or strategic planning at the portfolio level. Use it as a structured starting point for capability discovery, not as a comprehensive enterprise architecture methodology.</p>
  </section>
</article>
