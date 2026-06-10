---
layout: default
title: "Metadata Management Working Skill"
description: "Catalog business, technical, and operational metadata. Identify gaps that block reporting, integration, or AI readiness. Produce a metadata inventory with ownership."
permalink: /skill-hub/dama-dmbok/metadata-management-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></li>
    <li aria-current="page">Metadata Management</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — DAMA / Data</p>
  <h1>Metadata Management Working Skill</h1>
  <p class="lead">Catalog business, technical, and operational metadata. Identify gaps that block reporting, integration, or AI readiness. Produce a metadata inventory with ownership.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you document what your data means, where it lives, how it is structured, who maintains it, and how it is used. It produces a metadata inventory that resolves "what does this field mean?" disputes, unblocks integration projects, and prepares data for AI consumption. The output is a working catalog, not a theoretical model.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A report column has no documented definition and three departments give three different explanations.</li>
      <li>An integration project stalls because the source and target teams cannot agree on field semantics.</li>
      <li>A data scientist or AI agent cannot use a dataset because field meanings, formats, and update frequencies are unknown.</li>
      <li>A system migration requires mapping old fields to new fields, and no one knows what the old fields mean.</li>
      <li>An audit requires data lineage documentation and the existing documentation is outdated or missing.</li>
      <li>A new system is being integrated and the API schema lacks descriptions, examples, or ownership.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Example 1: The mystery report column</h3>
    <p>A BI report shows "Net Revenue." Finance says it is after discounts. Sales says it is before discounts. Operations says it excludes returns. No documentation exists. The skill produces a metadata entry for the column with a business definition, the calculation formula, the source tables, and the owner who can approve the definition.</p>

    <h3>Example 2: API integration confusion</h3>
    <p>A team builds an API to expose customer data. The field <code>customer_status</code> accepts values 1, 2, 3. The consuming team does not know what these values mean. The API documentation is a swagger file with no descriptions. The skill produces a metadata catalog for the API with business definitions, allowed values, examples, and update frequency.</p>

    <h3>Example 3: Migration mapping deadlock</h3>
    <p>A legacy system is being replaced. The migration team needs to map 400 fields. Half have no description in the legacy system. The skill produces a metadata discovery plan: interview legacy system experts, sample data for inferred meanings, document assumptions, and validate with business owners.</p>

    <h3>Example 4: AI readiness gap</h3>
    <p>An AI project needs structured data to train a model. The available datasets have no documentation on field meanings, data quality, update frequency, or ownership. The skill produces a metadata inventory that rates each dataset on AI readiness and flags gaps that must be closed before the dataset is usable.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>List of data elements, tables, APIs, or report columns in scope.</li>
      <li>System documentation, data dictionaries, or ER diagrams (even if outdated).</li>
      <li>Subject matter experts who know the business meaning of the data.</li>
      <li>Technical contacts who know the physical implementation (tables, fields, data types).</li>
      <li>Sample data for each element (to infer formats, ranges, and anomalies).</li>
      <li>List of consumers: reports, integrations, applications, or AI models that use the data.</li>
      <li>Existing metadata tools or catalogs (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What does this field mean in business terms, not technical terms?</li>
      <li>Who uses this field, and what decision do they make with it?</li>
      <li>What are the allowed values, and what does each value mean?</li>
      <li>Where is this field physically stored: table, column, system, database?</li>
      <li>How often is this field updated, and by what process or user?</li>
      <li>What other fields or tables depend on this field?</li>
      <li>Who is the authoritative source for the definition of this field?</li>
      <li>What is the data quality of this field: completeness, accuracy, timeliness?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Scope the metadata domain.</strong> Choose a bounded scope: one system, one data domain, one report, or one API. Do not attempt to catalog the entire enterprise at once.</li>
      <li><strong>Identify metadata types needed.</strong> For each element, decide which types you need: business metadata (meaning, owner, rules), technical metadata (table, column, type, length), operational metadata (update frequency, source job, last change date), or usage metadata (consumers, reports, integrations).</li>
      <li><strong>Collect existing documentation.</strong> Gather data dictionaries, ER diagrams, API specs, and wiki pages. Mark each source with a freshness date and trust level.</li>
      <li><strong>Interview subject matter experts.</strong> Use the questions above. Record answers as facts or assumptions. If two experts disagree, document both views and flag for resolution.</li>
      <li><strong>Sample and inspect data.</strong> Query the actual database or API to confirm physical names, data types, value distributions, and anomalies. Do not trust documentation alone.</li>
      <li><strong>Document each element.</strong> For each data element, produce a metadata entry with: name, definition, type, source system, physical location, allowed values, owner, consumers, update frequency, and quality notes.</li>
      <li><strong>Identify metadata gaps.</strong> Flag elements with missing definitions, missing owners, unknown consumers, undocumented values, or stale documentation. Classify each gap by business risk.</li>
      <li><strong>Validate with owners and consumers.</strong> Ask the named owner to confirm the definition. Ask a consumer to confirm that the documented meaning matches their usage. Adjust if they differ.</li>
      <li><strong>Produce the metadata inventory.</strong> Compile all entries into a single catalog. Include a gap summary, a risk assessment, and a closure plan.</li>
      <li><strong>Set maintenance rules.</strong> Define who updates the catalog when systems change, how often the catalog is reviewed, and what triggers an update.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a field has no business definition, do not use it in a report or integration until the definition is documented and approved.</li>
      <li>If two systems use the same field name with different meanings, rename one or document the semantic difference explicitly.</li>
      <li>If a field's allowed values are undocumented, sample the data and present the inferred values to the owner for confirmation.</li>
      <li>If a field has no owner, flag it as a governance gap and assign an owner before the metadata entry is marked complete.</li>
      <li>If documentation contradicts the actual data, trust the data and flag the documentation as stale.</li>
      <li>If a metadata entry is only technical (no business meaning), it is incomplete; add business metadata before marking it done.</li>
      <li>If a dataset has no documented consumers, question whether it should be maintained; unused data has a cost.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Metadata Inventory</strong> — catalog of data elements with business, technical, and operational metadata.</li>
      <li><strong>Metadata Gap Report</strong> — list of missing or stale metadata with business risk and closure actions.</li>
      <li><strong>AI Readiness Assessment</strong> — rating of datasets on metadata completeness, quality, and ownership.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Metadata Entry (compact)</h3>
    <pre><code>---
element: Customer.TaxNumber1
domain: Customer Master
system: SAP S/4
---

## Business metadata
- Definition: VAT or tax identification number for the customer
- Business owner: Finance Director
- Consumers: Billing, VAT reporting, EDI outbound
- Decisions made: Invoice tax calculation, compliance reporting

## Technical metadata
- Table: BUT000
- Field: STCD1
- Data type: CHAR(20)
- Source system: SAP MDG
- Update frequency: On change via MDG workflow
- Last modified: 2026-05-15

## Operational metadata
- Quality: 94% complete for DE customers; 62% for non-DE
- Validation: Required for DE; optional for others
- Known issues: CRM integration sometimes sends empty values

## Status
- Definition verified: Yes (by Finance Director, 2026-06-01)
- Owner assigned: Yes
- AI ready: Partial (quality gap noted)
</code></pre>

    <h3>Metadata Gap Note</h3>
    <pre><code>| Element | Gap | Risk | Closure Action | Owner | Due Date |
|---------|-----|------|----------------|-------|----------|
| Product.CostGroup | No business definition | COGS report cannot be validated | Interview Product Manager | Data Steward | 2026-06-20 |
| SalesOrder.DeliveryBlock | Allowed values undocumented | Integration failures | Sample data and confirm with Logistics | Integration Lead | 2026-06-15 |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every data element in scope has a business definition in plain language.</li>
      <li>Every element has a named owner who has confirmed the definition.</li>
      <li>Technical metadata (table, column, type) has been verified against the actual system.</li>
      <li>Allowed values are documented and confirmed.</li>
      <li>Consumers are listed and at least one has validated the usage description.</li>
      <li>All gaps are flagged with business risk and a closure action.</li>
      <li>The inventory has a maintenance owner and a review cycle.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Cataloging only technical metadata (tables, columns, types) without business meaning. <strong>Consequence:</strong> The catalog is useless for business users, data scientists, and integration analysts.</li>
      <li><strong>Mistake:</strong> Trusting outdated documentation without sampling the actual data. <strong>Consequence:</strong> The catalog documents a system that no longer exists; decisions based on it are wrong.</li>
      <li><strong>Mistake:</strong> Letting technical teams define business meanings without business validation. <strong>Consequence:</strong> Definitions are technically accurate but business-wrong; reports and integrations fail.</li>
      <li><strong>Mistake:</strong> Trying to catalog everything at once. <strong>Consequence:</strong> The effort never finishes; stakeholders lose confidence; the catalog is abandoned.</li>
      <li><strong>Mistake:</strong> Producing a catalog with no maintenance plan. <strong>Consequence:</strong> The catalog is accurate on day one and stale by month three.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Scope tightly.</strong> Ask the user to name the specific system, domain, API, or report to catalog. Do not attempt enterprise-wide metadata extraction.</li>
      <li><strong>Separate facts from assumptions.</strong> If a definition comes from documentation, label it "from docs." If it comes from expert interview, label it "from SME." If inferred from data, label it "inferred — needs validation."</li>
      <li><strong>Produce structured entries.</strong> Output metadata entries in the compact template format. Do not produce narrative descriptions.</li>
      <li><strong>Flag gaps explicitly.</strong> For every missing definition, owner, or consumer, produce a gap note with risk and action.</li>
      <li><strong>Avoid inventing definitions.</strong> If the meaning of a field is unknown, say "unknown" and ask for an SME. Do not guess based on field names.</li>
      <li><strong>Link to Atlas pages.</strong> If metadata gaps involve SAP master data, link to <a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> or <a href="/atlas/concepts/data-contracts/">Data Contracts</a>.</li>
      <li><strong>Handle missing information.</strong> If system access or SMEs are unavailable, produce a discovery checklist and ask the user to fill gaps.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a> — when metadata gaps reveal ownership or rule problems.</li>
      <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> — when metadata must include source-to-consumer paths.</li>
      <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> — when metadata gaps cause defects.</li>
      <li><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a> — when the metadata scope is master data.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — formal agreements that depend on accurate metadata.</li>
      <li><a href="/atlas/concepts/data-quality-controls/">Data Quality Controls</a> — controls that rely on metadata for enforcement.</li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — metadata patterns for SAP master data.</li>
      <li><a href="/atlas/concepts/sap-data-product/">SAP Data Product</a> — packaging data for consumption.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of metadata management practice. It is not official DAMA-DMBOK or ISO 11179 documentation. It has been applied in SAP and BI contexts but may need adaptation for cloud data lakes, NoSQL databases, or real-time streaming schemas.</p>
    <p>Limitations: This skill does not cover automated metadata extraction tools, data catalog software selection, or semantic ontology design. It focuses on manual and semi-automated metadata inventory methods suitable for project and support contexts.</p>
  </section>
</article>
