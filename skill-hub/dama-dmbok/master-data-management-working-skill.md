---
layout: default
title: "Master Data Management Working Skill"
description: "Map master data domains, identify duplication and fragmentation, define golden record logic, and design replication governance."
permalink: /skill-hub/dama-dmbok/master-data-management-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></li>
    <li aria-current="page">Master Data Management</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — DAMA / Data</p>
  <h1>Master Data Management Working Skill</h1>
  <p class="lead">Map master data domains, identify duplication and fragmentation, define golden record logic, and design replication governance.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you bring order to master data chaos. It provides a method to map which systems create, own, and consume master data; find duplication and fragmentation; decide what a "single version of the truth" means for each domain; and design governance that keeps master data consistent across the landscape. The output is a master data governance plan that a project or operations team can execute.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Customer, vendor, material, or employee records exist in multiple systems with no clear source of truth.</li>
      <li>Business processes fail because different systems show different values for the same master data object.</li>
      <li>A merger or acquisition requires harmonizing two code sets, two customer bases, or two org structures.</li>
      <li>Master data replication fails frequently and the failure pattern is not understood.</li>
      <li>A new system is being introduced and needs to consume or contribute master data.</li>
      <li>An MDG (Master Data Governance) implementation is being planned or reviewed.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Example 1: Customer fragmentation after acquisition</h3>
    <p>Company A acquires Company B. Both have customer databases. The integration team maps customers by name and address, but 30% are duplicates with slight variations. Sales uses the CRM. Finance uses SAP. Service uses a third portal. No system has the complete customer view. The skill produces a customer master data map, a deduplication strategy, a golden record definition, and a replication governance model.</p>

    <h3>Example 2: Material master divergence</h3>
    <p>Materials are created in PLM, enriched in SAP, and consumed in BW and EDI. Descriptions, units of measure, and classification differ across systems. Procurement orders the wrong unit because the EDI system shows "EA" while SAP shows "KG." The skill maps the material lifecycle, identifies the authoritative source for each attribute, and defines a synchronization rule.</p>

    <h3>Example 3: Business partner replication chaos</h3>
    <p>SAP Business Partners are replicated to CRM, a data warehouse, and an external tax system. Changes in SAP sometimes do not arrive. When they do, they overwrite manual corrections in CRM. No one knows which system wins. The skill produces a replication ownership matrix, a conflict resolution rule, and a monitoring checklist.</p>

    <h3>Example 4: Vendor master duplication</h3>
    <p>Procurement creates vendors in SAP. Finance maintains payment details. A separate supplier portal registers new vendors. The same supplier exists three times with different codes. Payment runs are split. Negotiation leverage is lost. The skill maps vendor creation channels, defines a deduplication rule, and designs a single entry point.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>List of master data domains in scope: customer, vendor, material, employee, chart of accounts, etc.</li>
      <li>System landscape showing which systems create, modify, and consume each domain.</li>
      <li>Sample records from each system for the same domain (to find duplication and divergence).</li>
      <li>Integration documentation: IDoc types, APIs, replication flows, and middleware.</li>
      <li>Business process descriptions that depend on the master data.</li>
      <li>Existing MDM or MDG setup documentation (if any).</li>
      <li>Stakeholders: business owners, data stewards, integration architects, and application owners.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which system creates the master data record first, and who approves the creation?</li>
      <li>For each attribute, which system is the authoritative source: creation system, enrichment system, or a dedicated MDM hub?</li>
      <li>How do you know if two records are the same entity: exact match, fuzzy match, or manual review?</li>
      <li>What happens when the same attribute is updated in two systems at the same time?</li>
      <li>Which business process breaks when master data is inconsistent between systems?</li>
      <li>Who is accountable for the quality of each master data domain?</li>
      <li>How are master data changes monitored, and who is alerted when replication fails?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the master data domains.</strong> List the domains in scope. For each, identify the key entities (e.g., customer account, business partner, vendor) and the key attributes (e.g., name, tax number, classification).</li>
      <li><strong>Map the system landscape.</strong> For each domain, create a system map showing: creation systems, enrichment systems, consuming systems, and the integration paths between them.</li>
      <li><strong>Identify duplication.</strong> Compare sample records across systems. Use exact match on key fields (tax number, email, material number) and fuzzy match on names and addresses. Document duplication rate and patterns.</li>
      <li><strong>Identify fragmentation.</strong> For each entity, check whether all key attributes exist in one system or are spread across many. Document which system holds which attributes.</li>
      <li><strong>Define golden record logic.</strong> For each domain and attribute, decide: which system is the source of truth, how conflicts are resolved (last-write-wins, hub-wins, manual review), and how the golden record is composed from multiple sources.</li>
      <li><strong>Design replication governance.</strong> For each integration path, define: what data flows, in which direction, how often, what triggers it, who owns it, and how failures are handled.</li>
      <li><strong>Define deduplication rules.</strong> Specify matching criteria, survivorship rules (which value wins when sources conflict), and the approval workflow for merges.</li>
      <li><strong>Assign ownership.</strong> For each domain, name: business owner, data steward, technical owner, and integration owner. Confirm they accept the role.</li>
      <li><strong>Produce the master data governance plan.</strong> Combine domain maps, duplication analysis, golden record logic, replication governance, deduplication rules, and ownership into a single document.</li>
      <li><strong>Validate with a pilot.</strong> Test the golden record logic and replication governance on a small subset of data. Adjust before scaling.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a master data attribute is created in one system and never changed elsewhere, that system is the source of truth for that attribute.</li>
      <li>If an attribute is updated in multiple systems, designate a hub or a winning system; do not allow ambiguous conflict resolution.</li>
      <li>If duplication rate exceeds 10%, prioritize deduplication before any new integration or migration.</li>
      <li>If a system consumes master data but also modifies it, the consumption path must include write-back governance or the system must be reclassified as a contributor.</li>
      <li>If replication failures are frequent, fix the monitoring and error handling before optimizing the data model.</li>
      <li>If no one accepts ownership of a master data domain, do not proceed with tooling; resolve ownership first.</li>
      <li>If a merger requires code harmonization, decide on the target code set before mapping; mapping without a target is wasted effort.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Master Data Domain Map</strong> — domains, systems, attributes, and ownership.</li>
      <li><strong>Duplication and Fragmentation Analysis</strong> — rates, patterns, and business impact.</li>
      <li><strong>Golden Record Definition</strong> — source of truth per attribute, conflict resolution, and composition logic.</li>
      <li><strong>Replication Governance Model</strong> — flows, triggers, frequencies, failure handling, and monitoring.</li>
      <li><strong>Master Data Governance Plan</strong> — combined document with priorities and actions.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Master Data Domain Map (compact)</h3>
    <pre><code>| Domain | Entity | Creation System | Enrichment System | Consumers | Key Attributes | Source of Truth |
|--------|--------|-----------------|-------------------|-----------|----------------|-----------------|
| Customer | Business Partner | CRM | SAP MDG | S/4, BW, EDI | Name, Tax, Address, Status | MDG for core; CRM for sales attributes |
| Material | Material Master | PLM | SAP S/4 | BW, EDI, WMS | Description, UoM, Group, Price | S/4 for operational; PLM for technical |
</code></pre>

    <h3>Golden Record Attribute Logic</h3>
    <pre><code>| Domain | Attribute | Source System | Conflict Rule | Fallback | Approval Needed |
|--------|-----------|---------------|---------------|----------|-----------------|
| Customer | TaxNumber1 | MDG | MDG always wins | None | No |
| Customer | CreditLimit | CRM | CRM wins if newer than MDG | MDG | Yes, if increase > 20% |
| Material | Description | PLM | PLM wins | S/4 | No |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every master data domain in scope has a named business owner and data steward.</li>
      <li>Every key attribute has a defined source of truth and a conflict resolution rule.</li>
      <li>Duplication rate has been measured and documented.</li>
      <li>Replication paths are documented with direction, frequency, trigger, and owner.</li>
      <li>Failure handling and monitoring are defined for every replication path.</li>
      <li>Deduplication rules include matching criteria, survivorship logic, and approval workflow.</li>
      <li>The governance plan has been validated with at least one pilot subset.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Buying an MDM tool before defining golden record logic. <strong>Consequence:</strong> The tool enforces an undefined model; conflicts are resolved arbitrarily; users lose trust.</li>
      <li><strong>Mistake:</strong> Treating all attributes as if they have the same source of truth. <strong>Consequence:</strong> Overwrites in one system destroy valuable enrichments made in another.</li>
      <li><strong>Mistake:</strong> Deduplicating without survivorship rules. <strong>Consequence:</strong> Merged records contain conflicting values; downstream systems break.</li>
      <li><strong>Mistake:</strong> Ignoring manual corrections in downstream systems. <strong>Consequence:</strong> Replication overwrites local knowledge; users disable the integration.</li>
      <li><strong>Mistake:</strong> Mapping codes during a merger without deciding the target standard. <strong>Consequence:</strong> Mapping tables grow indefinitely; reporting remains inconsistent.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Start with domains, not tools.</strong> Ask the user to name the master data domains and systems before discussing MDM, MDG, or any software.</li>
      <li><strong>Map before judging.</strong> Produce a system landscape map and a duplication analysis before proposing golden record logic. Do not guess sources of truth.</li>
      <li><strong>Define attribute-level logic.</strong> The source of truth may differ per attribute. Do not assume one system owns the entire record.</li>
      <li><strong>Surface conflict scenarios.</strong> Ask: what happens when two systems update the same attribute? If the answer is unclear, flag it as a governance gap.</li>
      <li><strong>Produce artifacts, not advice.</strong> Output a Master Data Domain Map and a Golden Record Definition in the templates provided. Do not write a generic MDM strategy document.</li>
      <li><strong>Link to Atlas diagnostics.</strong> If replication failures are involved, link to <a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a>, <a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a>, or <a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP CVI Synchronization Diagnostics</a>.</li>
      <li><strong>Handle missing information.</strong> If system documentation or record samples are unavailable, produce a data collection checklist and ask the user to gather them.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a> — when MDM reveals ownership or rule gaps.</li>
      <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> — when master data defects need tracing.</li>
      <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> — when master data flows need tracing.</li>
      <li><a href="/skill-hub/dama-dmbok/reference-data-management-working-skill/">Reference Data Management</a> — when code lists and status values are part of the master data scope.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — diagnostic patterns for SAP master data.</li>
      <li><a href="/atlas/data-quality/sap-mdg-governance-patterns/">SAP MDG Governance Patterns</a> — governance structures for SAP MDG.</li>
      <li><a href="/atlas/data-quality/sap-master-data-replication-patterns/">SAP Master Data Replication Patterns</a> — replication models and failure modes.</li>
      <li><a href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">SAP Master Data Duplicate Diagnostics</a> — finding and resolving duplicates.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of master data management practice. It is not official DAMA-DMBOK or SAP MDG documentation. It has been applied in SAP-centric enterprise contexts but may need adaptation for cloud-native CRM, HR, or custom applications.</p>
    <p>Limitations: This skill does not cover advanced probabilistic matching, entity resolution algorithms, or MDM platform selection. It focuses on governance, ownership, and replication logic suitable for project and operations contexts.</p>
  </section>
</article>
