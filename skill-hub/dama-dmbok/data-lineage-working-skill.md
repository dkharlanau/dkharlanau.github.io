---
layout: default
title: "Data Lineage Working Skill"
description: "Trace data from source to consumer. Document transformations, hops, and ownership at each stage. Identify lineage gaps that create audit or trust risk."
permalink: /skill-hub/dama-dmbok/data-lineage-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></li>
    <li aria-current="page">Data Lineage</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — DAMA / Data</p>
  <h1>Data Lineage Working Skill</h1>
  <p class="lead">Trace data from source to consumer. Document transformations, hops, and ownership at each stage. Identify lineage gaps that create audit or trust risk.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you answer "where did this number come from?" It provides a method to trace a data element from its origin through every transformation, system, and handoff until it reaches the final consumer. The output is a documented lineage path with named owners at each hop, plus a gap list for hops that are unknown, untrusted, or unowned.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A report value is questioned in an audit and no one can explain its source.</li>
      <li>A data defect is found in a downstream system and the team does not know which upstream system introduced it.</li>
      <li>An integration is being redesigned and the existing data flows are undocumented.</li>
      <li>A regulation requires data lineage documentation for specific domains (e.g., financial reporting, personal data).</li>
      <li>An AI model produces unexpected results and the training data provenance is unclear.</li>
      <li>A system migration requires understanding which data flows must be preserved, rerouted, or retired.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Example 1: Audit challenge on revenue recognition</h3>
    <p>An auditor asks how the "recognized revenue" figure in the quarterly report is calculated. Finance points to a BW report. BW points to an SAP extractor. The extractor pulls from multiple tables with custom logic. No one has documented the full path. The skill traces the lineage from report column back to source transactions, documents each transformation, and identifies the owner of each step.</p>

    <h3>Example 2: Wrong customer segment in campaign</h3>
    <p>Marketing sends a campaign to the wrong customer segment. The segment value in the campaign tool does not match the segment in SAP. The skill traces the segment field from SAP through the data warehouse, a segmentation algorithm, and an API to the campaign tool. It finds that the algorithm was updated two weeks ago without notifying Marketing.</p>

    <h3>Example 3: Migration scope uncertainty</h3>
    <p>A legacy system is being retired. The team knows some data flows to SAP, but they are unsure about secondary flows to BI, a data lake, and an external partner. The skill produces a complete lineage map showing all consumers, which flows must be migrated, and which can be retired.</p>

    <h3>Example 4: AI model drift</h3>
    <p>An AI model's accuracy drops. The training data is supposed to come from a curated data product. The skill traces the data product back to its source tables and finds that a source table was modified by a recent change request, altering the feature distribution. The lineage gap was the missing change impact assessment on the AI pipeline.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The data element, report column, or dataset whose lineage is needed.</li>
      <li>The consumer system or report where the data is observed.</li>
      <li>System landscape documentation: databases, applications, integration middleware, and ETL tools.</li>
      <li>Technical documentation: ETL jobs, API specs, database views, stored procedures, and transformation logic.</li>
      <li>Subject matter experts who know the data flows for each system.</li>
      <li>Access to query systems or logs to verify actual data movement (optional but recommended).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the original system and table where this data was first recorded?</li>
      <li>What transformations does this data undergo: aggregation, filtering, mapping, calculation, enrichment?</li>
      <li>Which system or job moves the data from one hop to the next?</li>
      <li>Who owns each hop: the source system, the transformation job, the integration, and the consumer?</li>
      <li>When was the last time this lineage path was verified, and what changed since then?</li>
      <li>What happens if a hop fails: is data delayed, lost, or stale?</li>
      <li>Is there a parallel path where the same data flows through a different route?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the lineage target.</strong> Name the exact data element, report column, or dataset to trace. Include the consumer system and the business question that requires lineage.</li>
      <li><strong>Start from the consumer and walk backward.</strong> Identify the immediate source of the data in the consumer system. Then identify the source of that source. Continue until you reach the original creation point.</li>
      <li><strong>Document each hop.</strong> For each step, record: system name, component (table, file, API, job), transformation (if any), owner, and trust level (verified, inferred, claimed).</li>
      <li><strong>Identify transformations.</strong> For each hop where data changes (format, value, structure), document the transformation logic, the business reason, and the owner who maintains it.</li>
      <li><strong>Map parallel and alternate paths.</strong> Check if the same data flows through multiple routes. Document each route and note which is primary, which is backup, and which is deprecated.</li>
      <li><strong>Identify lineage gaps.</strong> Flag hops where: the source is unknown, the transformation logic is undocumented, the owner is missing, the path has changed without documentation, or the hop is untrusted.</li>
      <li><strong>Assess business risk per gap.</strong> For each gap, describe what business decision or process is affected if the lineage is wrong or unknown.</li>
      <li><strong>Produce the lineage map.</strong> Create a visual or tabular lineage path from source to consumer. Include hops, transformations, owners, and gap flags.</li>
      <li><strong>Produce the gap closure plan.</strong> For each gap, define: verification approach, documentation action, owner, and target date.</li>
      <li><strong>Validate with owners.</strong> Walk through the lineage map with the owner of each hop. Confirm accuracy and update where needed.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a hop is claimed by an expert but not verified in system logs or code, label it "inferred" and plan verification.</li>
      <li>If a transformation changes the business meaning of a field, document it as a semantic transformation, not just a technical conversion.</li>
      <li>If two parallel paths produce different values for the same consumer, flag it as a data quality risk, not just a lineage variation.</li>
      <li>If a lineage path includes a manual step (spreadsheet, email, manual upload), treat it as a high-risk hop because it is unlogged and ungoverned.</li>
      <li>If a hop owner is missing or has left the organization, the lineage is unmaintained; assign a new owner before closing the gap.</li>
      <li>If a source system is being retired, the lineage path is time-bound; document the retirement date and the replacement path.</li>
      <li>If lineage is required for compliance, prioritize gaps that affect regulated data elements over non-regulated ones.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Data Lineage Map</strong> — source-to-consumer path with hops, transformations, and owners.</li>
      <li><strong>Lineage Gap Report</strong> — unknown hops, undocumented transformations, missing owners, and business risk. <a href="/skill-hub/artifact-templates/">See Data Lineage Gap Note template</a>.</li>
      <li><strong>Gap Closure Plan</strong> — actions, owners, and deadlines to close lineage gaps.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Lineage Hop Log (compact)</h3>
    <pre><code>| Hop | System | Component | Transformation | Owner | Trust Level | Notes |
|-----|--------|-----------|--------------|-------|-------------|-------|
| 1 | SAP S/4 | Table VBRK | None | Finance | Verified | Source transaction |
| 2 | BW | Extractor 0FI_AR_4 | Filter: posting date in period | BI Team | Verified | Monthly load |
| 3 | BW | DSO ZDSO_REV | Aggregate by customer | BI Team | Verified | Sum of revenue |
| 4 | BW | Report ZREV_CUST | Format currency | BI Team | Verified | EUR conversion |
| 5 | BI Portal | Dashboard "Revenue" | None | BI Team | Inferred | Claimed by BI; not verified |
</code></pre>

    <h3>Lineage Gap Note (compact)</h3>
    <pre><code>| Data Element | Gap | Gap Type | Business Risk | Verification Approach | Owner | Due Date |
|--------------|-----|----------|-------------|----------------------|-------|----------|
| Customer.Segment | Algorithm update not documented | Missing documentation | Wrong campaign targeting | Review algorithm version history | Data Science Lead | 2026-06-20 |
| Product.Cost | Manual spreadsheet between PLM and SAP | Untrusted hop | COGS reporting unreliable | Replace with API or document procedure | Integration Lead | 2026-07-01 |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The lineage path reaches the original source system and table for the data element.</li>
      <li>Every hop has a named system, component, and owner.</li>
      <li>Every transformation is documented with logic and business reason.</li>
      <li>Every hop is labeled as verified, inferred, or claimed.</li>
      <li>All gaps are flagged with a business risk statement.</li>
      <li>Parallel or alternate paths are documented.</li>
      <li>The lineage map has been validated with at least one hop owner.</li>
      <li>A gap closure plan exists with owners and target dates.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Trusting a single expert's memory without verifying in code or logs. <strong>Consequence:</strong> The lineage is wrong; the audit fails; the defect recurs.</li>
      <li><strong>Mistake:</strong> Documenting only the happy path and ignoring error handling, fallback loads, or manual corrections. <strong>Consequence:</strong> The lineage is incomplete; exceptions are unexplained.</li>
      <li><strong>Mistake:</strong> Treating lineage as a one-time documentation exercise. <strong>Consequence:</strong> The lineage is stale after the next system change; trust is lost.</li>
      <li><strong>Mistake:</strong> Focusing on technical hops and ignoring business ownership. <strong>Consequence:</strong> When a hop breaks, no one is accountable; resolution stalls.</li>
      <li><strong>Mistake:</strong> Producing a visual diagram without a tabular backup. <strong>Consequence:</strong> The diagram is hard to update; details are lost in abstraction.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Start from the consumer.</strong> Ask the user to name the exact report, dataset, or data element that needs lineage. Do not start from "the enterprise data landscape."</li>
      <li><strong>Walk backward step by step.</strong> For each hop, ask: what is the immediate source? What transformation happened? Who owns it? Do not skip hops.</li>
      <li><strong>Label trust levels.</strong> If a hop is based on documentation, label it "from docs." If based on expert statement, label it "claimed." If verified in code or logs, label it "verified."</li>
      <li><strong>Flag manual steps.</strong> Any hop involving a spreadsheet, email, or manual upload is high-risk. Document it explicitly and recommend automation or formalization.</li>
      <li><strong>Produce artifacts, not descriptions.</strong> Output a Lineage Hop Log and a Lineage Gap Report in the templates provided. Do not write a narrative.</li>
      <li><strong>Link to Atlas pages.</strong> If lineage involves SAP data, link to <a href="/atlas/concepts/data-lineage/">Data Lineage</a> or <a href="/atlas/concepts/data-quality-controls/">Data Quality Controls</a>.</li>
      <li><strong>Handle missing information.</strong> If system access or code is unavailable, produce a discovery checklist and ask the user to verify specific hops.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/dama-dmbok/metadata-management-working-skill/">Metadata Management</a> — when lineage gaps reveal missing metadata.</li>
      <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> — when a defect needs tracing from symptom to source.</li>
      <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a> — when lineage gaps reveal ownership problems.</li>
      <li><a href="/skill-hub/dama-dmbok/data-integration-interoperability-working-skill/">Data Integration &amp; Interoperability</a> — when lineage crosses system boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/data-lineage/">Data Lineage</a> — conceptual foundation for lineage in SAP landscapes.</li>
      <li><a href="/atlas/concepts/data-quality-controls/">Data Quality Controls</a> — controls that depend on accurate lineage.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — agreements at system boundaries that lineage must respect.</li>
      <li><a href="/atlas/concepts/sap-data-product/">SAP Data Product</a> — packaging data with lineage for consumption.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of data lineage practice. It is not official DAMA-DMBOK or ISO documentation. It has been applied in SAP, BI, and data warehouse contexts but may need adaptation for cloud-native pipelines, streaming data, or machine learning feature stores.</p>
    <p>Limitations: This skill does not cover automated lineage extraction tools, graph-based lineage databases, or real-time lineage tracking. It focuses on manual and semi-automated lineage documentation suitable for audit, migration, and defect tracing.</p>
  </section>
</article>
