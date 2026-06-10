---
layout: default
title: "Data Governance Working Skill"
description: "Diagnose missing data ownership, undefined rules, and unenforced policies. Produce a governance action plan with named owners, decision rights, and enforcement mechanisms."
permalink: /skill-hub/dama-dmbok/data-governance-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">DAMA / Data</a></li>
    <li aria-current="page">Data Governance</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — DAMA / Data</p>
  <h1>Data Governance Working Skill</h1>
  <p class="lead">Diagnose missing data ownership, undefined rules, and unenforced policies. Produce a governance action plan with named owners, decision rights, and enforcement mechanisms.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill turns vague complaints like "our data is a mess" into a structured governance action plan. It helps you identify who should own which data, what rules should exist, where enforcement is missing, and what decisions must be made before any tool or automation is introduced. The output is a working document that a project team or data steward can act on immediately.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A data quality initiative has stalled because no one can agree who fixes bad data.</li>
      <li>A new system is being integrated and there is no agreed data ownership model between source and target.</li>
      <li>Master data changes require three emails and two meetings to approve.</li>
      <li>Reports from different systems show different values for the same metric and no one owns the reconciliation.</li>
      <li>An audit or compliance review requires documented data ownership, retention rules, or access policies.</li>
      <li>You are preparing for AI or automation and need to know which data is trustworthy and who vouches for it.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Example 1: Customer master ownership gap</h3>
    <p>A sales team creates customers in a CRM. Finance maintains tax data in SAP. The integration breaks when tax numbers are updated in SAP but not in CRM. Neither team accepts ownership of the end-to-end customer record. Orders are blocked. The skill produces an ownership matrix that assigns business ownership to Sales, technical ownership to IT, and data stewardship to a named person.</p>

    <h3>Example 2: Post-merger data chaos</h3>
    <p>Two companies merge. Both have product codes, supplier codes, and chart of accounts. The integration team proposes a mapping, but no one has decision rights over which code set survives. Projects stall. The skill surfaces the decision rights gap and produces a governance council charter with voting rules.</p>

    <h3>Example 3: Unenforced retention policy</h3>
    <p>A regulation requires customer data to be deleted after seven years. IT has a policy document. The database has no automated deletion. The policy is ignored. The skill identifies the missing enforcement mechanism and produces a rule with a technical owner, a validation query, and a review cycle.</p>

    <h3>Example 4: Report reconciliation dispute</h3>
    <p>Finance and Operations both publish "revenue" numbers. They differ by 12%. Each team claims their number is correct. There is no agreed definition, no system of record, and no reconciliation owner. The skill produces a data element register with definitions, sources, owners, and a reconciliation procedure.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>List of data domains or data elements in scope (e.g., customer, product, financial transaction).</li>
      <li>System inventory showing which systems create, modify, and consume each data domain.</li>
      <li>Organizational chart or contact list for business and technical stakeholders.</li>
      <li>Existing policies, standards, or guidelines (even if outdated or ignored).</li>
      <li>Recent data quality incident log or ticket history (optional but valuable).</li>
      <li>Compliance or audit requirements that apply to the data (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Who is fired if this data is wrong? If no one, ownership is missing.</li>
      <li>Which system is the source of truth for this data element, and who certified it?</li>
      <li>What rule should prevent this defect, and where is it enforced?</li>
      <li>Who approves a change to this data definition, and how long does that take?</li>
      <li>What happens when two systems disagree on the value of this field?</li>
      <li>Is there a documented policy for this data, and is it technically enforceable?</li>
      <li>Who reviews access to this data, and when was the last review?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Scope the data domain.</strong> List the data elements, tables, or objects in scope. Do not try to govern everything at once. Pick one domain with visible pain.</li>
      <li><strong>Map the system landscape.</strong> For each data element, identify: source system, consuming systems, transformation points, and the system of record.</li>
      <li><strong>Identify stakeholders.</strong> For each data element, name: business owner (accountable for quality), technical owner (accountable for systems), data steward (day-to-day caretaker), and consumer representatives.</li>
      <li><strong>Surface ownership gaps.</strong> Flag data elements with missing owners, conflicting owners, or owners who lack authority. Document each gap with business risk.</li>
      <li><strong>Catalog existing rules.</strong> Collect policies, standards, validation rules, and access controls. Note which are enforced technically, which are enforced by process, and which exist only on paper.</li>
      <li><strong>Identify enforcement gaps.</strong> For each rule, ask: where is this checked? What happens when it fails? Who is notified? If any answer is missing, the rule is unenforced.</li>
      <li><strong>Define decision rights.</strong> For each data domain, document who can: create, update, delete, approve changes, approve access, and define rules.</li>
      <li><strong>Produce the governance action plan.</strong> Combine ownership matrix, rule catalog, enforcement gaps, and decision rights into a single document with priorities and owners.</li>
      <li><strong>Validate with stakeholders.</strong> Walk through the plan with named owners. Confirm they accept the role and the authority. Adjust if they refuse.</li>
      <li><strong>Set review cycle.</strong> Define how often ownership, rules, and enforcement are reviewed. Assign a review owner.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If ownership is unclear, produce an ownership matrix before proposing automation.</li>
      <li>If a rule exists only in a policy document and is not enforced technically, classify it as "process-dependent" and flag the risk.</li>
      <li>If two systems both claim to be the source of truth for the same data element, escalate to architecture; do not guess.</li>
      <li>If a data steward is named but lacks system access or decision authority, the ownership is ceremonial; surface the gap.</li>
      <li>If a compliance requirement has no technical enforcement, treat it as a high-priority gap regardless of current incident count.</li>
      <li>If a data element has no consumers, question whether it should be governed at all; governance has a cost.</li>
      <li>If a rule is enforced in one system but not in another that receives the same data, the rule is porous; document the bypass.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Data Ownership Matrix</strong> — data elements, owners, stewards, systems, and gap flags. <a href="/skill-hub/artifact-templates/">See Artifact Templates</a>.</li>
      <li><strong>Rule Catalog</strong> — rules, enforcement mechanisms, failure actions, and gap status.</li>
      <li><strong>Governance Action Plan</strong> — prioritized actions, owners, deadlines, and success criteria.</li>
      <li><strong>Decision Rights Charter</strong> — who decides what for each data domain.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Data Ownership Matrix (compact)</h3>
    <pre><code>| Data Element | System of Record | Business Owner | Technical Owner | Data Steward | Consumers | Ownership Gap |
|--------------|------------------|----------------|-----------------|--------------|-----------|---------------|
| Customer.TaxNumber1 | SAP BP | Sales Director | IT Data Lead | (vacant) | CRM, BW | Steward vacant; no one reviews daily changes |
| Product.MaterialGroup | MDG | Product Manager | IT MDG Admin | Maria K. | S/4, PLM, EDI | None |
</code></pre>

    <h3>Rule Enforcement Check</h3>
    <pre><code>| Rule | Applies To | Enforcement Point | Failure Action | Review Frequency | Gap |
|------|------------|-------------------|--------------|------------------|-----|
| Tax number required for DE customers | Customer.TaxNumber1 | MDG workflow validation | Block creation | Monthly | None |
| Customer name max 40 chars | Customer.Name1 | API schema | Reject payload | Quarterly | Not enforced in manual SAP GUI entry |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every data element in scope has a named business owner and technical owner.</li>
      <li>Every owner has been asked and has not refused the role.</li>
      <li>Every rule has a documented enforcement point and failure action.</li>
      <li>Every enforcement gap has a business risk statement and a proposed closure action.</li>
      <li>Decision rights are documented and validated with at least one stakeholder per domain.</li>
      <li>The governance action plan has priorities, owners, and deadlines.</li>
      <li>No automation or tool purchase is proposed before ownership is clear.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Proposing a data governance tool before ownership is defined. <strong>Consequence:</strong> The tool enforces nothing because no one configures or maintains the rules.</li>
      <li><strong>Mistake:</strong> Naming a business unit as owner without naming a specific person. <strong>Consequence:</strong> Accountability diffuses; decisions stall.</li>
      <li><strong>Mistake:</strong> Treating a policy document as governance. <strong>Consequence:</strong> Rules are ignored because there is no enforcement, no review, and no consequence for violation.</li>
      <li><strong>Mistake:</strong> Defining governance for all data at once. <strong>Consequence:</strong> The effort collapses under scope; nothing gets implemented.</li>
      <li><strong>Mistake:</strong> Ignoring informal data caretakers who already do the work. <strong>Consequence:</strong> The formal owner lacks operational knowledge; the caretaker resists the new structure.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Gather context first.</strong> Ask for: the data domain in scope, the systems involved, the stakeholders by name and role, and any existing policy documents. Do not proceed with generic assumptions.</li>
      <li><strong>Separate facts from assumptions.</strong> If an owner is named but not confirmed, label it "proposed." If a rule is described but not verified in a system, label it "claimed."</li>
      <li><strong>Produce artifacts, not summaries.</strong> Output a Data Ownership Matrix and a Rule Catalog in the formats provided. Do not produce a narrative essay.</li>
      <li><strong>Flag gaps explicitly.</strong> For every missing owner, unenforced rule, or unclear decision right, produce a gap statement with business risk. Do not hide gaps in general recommendations.</li>
      <li><strong>Avoid generic language.</strong> Do not write "data governance is important." Write "Customer.TaxNumber1 has no steward; tax reporting risk is unowned."</li>
      <li><strong>Link to Atlas diagnostics when relevant.</strong> If the governance gap involves SAP master data, link to <a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> or <a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a>.</li>
      <li><strong>Handle missing information.</strong> If stakeholders or systems are unknown, produce a discovery checklist instead of guessing. Ask the user to fill gaps before proceeding.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> — when governance gaps cause recurring defects.</li>
      <li><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a> — when the governance scope is master data domains.</li>
      <li><a href="/skill-hub/dama-dmbok/metadata-management-working-skill/">Metadata Management</a> — when definitions, lineage, and catalogs are part of the governance gap.</li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a> — when stakeholder mapping precedes ownership assignment.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — diagnostic patterns for SAP master data defects.</li>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a> — common governance breakdowns in SAP landscapes.</li>
      <li><a href="/atlas/data-quality/sap-mdg-governance-patterns/">SAP MDG Governance Patterns</a> — governance structures that work in SAP MDG contexts.</li>
      <li><a href="/atlas/concepts/data-contracts/">Data Contracts</a> — formal agreements at system boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of data governance practice. It is not official DAMA-DMBOK documentation. It has been applied in SAP-centric enterprise contexts but may need adaptation for cloud-native, decentralized, or heavily regulated environments.</p>
    <p>Limitations: This skill does not cover privacy engineering, data security architecture, or advanced AI governance. It focuses on operational ownership, rules, and enforcement. For legal or regulatory compliance, consult specialized counsel.</p>
  </section>
</article>
