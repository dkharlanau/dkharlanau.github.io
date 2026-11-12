---
layout: default
title: "SAP Master Data Duplicate Diagnostics"
description: "Diagnose SAP BP duplicate candidates with identity evidence, MDG controls, safe remediation and a read-only AI review experiment."
search_intent: "How to investigate SAP Business Partner duplicate candidates without merging different entities"
permalink: /atlas/diagnostics/sap-master-data-duplicate-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "Master data quality / duplicates"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
last_modified_at: 2026-11-12
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - data-quality
related:
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/diagnostics/sap-number-range-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/data-quality/master-data-governance-failure-modes/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Master Data Duplicate Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP master data duplicate diagnostics</h1>
    <p class="note-subtitle">A matching score is a lead, not proof. Follow the creation path, identity evidence and downstream references before correcting a Business Partner.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>Master data quality / duplicates</dd></div>
      <div><dt>Indexing</dt><dd>Noindex. Revised guidance awaits independent human SAP and editorial review.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>The failed control: a possible match is treated as a confirmed duplicate</h2>
    <p>A supplier appears twice in a Business Partner (BP) search. Both entries have a similar name and address. It is tempting to select the newer one, block it and call the incident solved. That can be a costly mistake: a shared address, group brand or payment service can create a strong match between two different legal entities.</p>
    <p>The business control is not “remove every similar record”. It is <strong>decide whether two technical records represent the same governed business identity before an approved creation, migration or consolidation step changes data</strong>. A duplicate-search result is a candidate for investigation, not permission to merge, block or change existing transactions.</p>
    <p><strong>Product boundary:</strong> the examples below focus on SAP S/4HANA Business Partner and SAP Master Data Governance (MDG). Search methods, matching attributes, rules, thresholds, roles and consolidation availability depend on the release and configuration. Do not apply BP-specific steps to materials without checking their own model.</p>

    <h2>Trace the end-to-end path, not just the two names</h2>
    <ol>
      <li><strong>Origin:</strong> a business owner requests an entity; an external system, migration load or user supplies the identity evidence.</li>
      <li><strong>Preventive check:</strong> the active BP or MDG creation process runs its configured search, validation and duplicate checks, if available and enabled. A candidate should reach an authorised reviewer before approval.</li>
      <li><strong>Governed decision:</strong> the steward decides whether to reuse an existing BP, create a genuinely separate BP, or investigate an unresolved match. A workflow approval does not prove legal identity by itself.</li>
      <li><strong>Distribution:</strong> source-to-target key mapping and interface processing determine which target record receives updates. An empty or wrong mapping can make the apparent duplicate a replication problem instead.</li>
      <li><strong>Consumption:</strong> Sales, Procurement, Finance and analytics may already reference either BP or its customer/supplier role. The remediation must protect these references and the audit trail.</li>
    </ol>

    <h2>Three explanations that need different evidence</h2>
    <div class="decision-table"><table><thead><tr><th>Hypothesis</th><th>What would distinguish it?</th><th>Control and owner</th></tr></thead><tbody>
      <tr><td>True duplicate created during migration or local maintenance</td><td>Two BPs are confirmed to be the same legal/business identity; creation batch, request and registration evidence agree.</td><td>Business steward approves identity; migration owner checks source-to-target crosswalk and load exceptions.</td></tr>
      <tr><td>False positive: two valid entities with similar data</td><td>Different verified registration identities, business purposes or authorised legal-entity records; shared name or address is not decisive.</td><td>Business/legal owner resolves the entity distinction; match-rule owner reviews the alert quality.</td></tr>
      <tr><td>Replication or key-mapping gap</td><td>The intended source object and existing target key do not match the interface mapping or target creation history.</td><td>MDG/integration owner verifies governed identity, logical-system context and target application result before a mapping correction.</td></tr>
    </tbody></table></div>
    <p><strong>SAP standard versus local design:</strong> SAP documentation for S/4HANA 2025 FPS01 describes configurable duplicate checks with selected attributes and scored potential matches. It does not establish that one email, bank account or tax value must be globally unique in every deployment. Which evidence is mandatory, where the check is activated, and who can approve an exception are <em>local governance decisions</em>. See <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/74b0b157c81944ffaac6ebc07245b9dc/dd32582b161d4dd390ef994735e6af1d-155.html">SAP Help: Configure and Check Potential Duplicates of Master Data Records</a>.</p>

    <h2>Where is the source of truth?</h2>
    <div class="decision-table"><table><thead><tr><th>Question</th><th>Authoritative evidence to request</th><th>Check point</th></tr></thead><tbody>
      <tr><td>Are these legally or operationally the same entity?</td><td>Approved identity documents or a trusted business registry, as permitted by policy; business owner decision.</td><td>Before accepting or rejecting a match candidate. A fuzzy score is not the source of truth.</td></tr>
      <tr><td>Which BP should be maintained?</td><td>Approved creation request, MDG active record, governance scope, role/organisation assignments and change history.</td><td>Before authorising a create, extend or consolidation action.</td></tr>
      <tr><td>Which key does another system use?</td><td>Owned migration crosswalk or active replication/key-mapping evidence, with source and target system IDs.</td><td>Before resending data or changing cross-system mapping.</td></tr>
      <tr><td>What would break if one BP is retired?</td><td>Actual target objects and referenced orders, POs, invoices, payments, contracts and interface subscriptions.</td><td>Before any block, consolidation or cutover; confirm again afterwards.</td></tr>
    </tbody></table></div>
    <p>The authoritative source can differ by attribute and process. An external register may support legal identity; MDG may govern the active BP; a target system owns its processed transactions. <strong>No single table proves all three.</strong> In SAP, <code>BUT000</code> is useful for BP core identity, while <code>KNA1</code> and <code>LFA1</code> relate to customer/supplier data; <code>CDHDR</code>/<code>CDPOS</code> may help where change documents exist. These are investigation aids, not a universal duplicate or lineage report.</p>

    <h2>Worked example: two supplier candidates, one risky shortcut</h2>
    <p><strong>Entirely synthetic:</strong> BP <code>BP-100</code> and <code>BP-200</code> share the trading name “Northshore Parts” and an office address. A migration report flags a 92% name-and-address similarity. However, their approved legal registration IDs differ, and BP-200 has an open purchasing document. The percentage here is invented for illustration, not an SAP threshold or a measured production result.</p>
    <p><strong>Decision:</strong> label the pair <em>needs identity review</em>, not <em>confirmed duplicate</em>. The business owner checks whether these are separate companies, branches or one entity recorded twice. The data steward records the decision and source evidence. The integration team separately checks whether the migration crosswalk and target mapping created an unintended second object. No user should re-key the open PO as an informal cleanup.</p>

    <h2>Three safe outcomes</h2>
    <ol>
      <li><strong>Two valid entities:</strong> retain both records, document why the candidate is a false positive and improve the review criteria if similar alerts repeat. Do not suppress all shared-address matches without checking missed duplicates.</li>
      <li><strong>Confirmed duplicate:</strong> use the supported, configured and approved MDG cleansing/consolidation process where available. Review the proposed best record, field provenance, roles, downstream documents and rollback/reconciliation plan. There is no universal “merge BP” operation that safely rewrites every existing business document.</li>
      <li><strong>Identity or mapping defect:</strong> repair the owned migration crosswalk, creation gate or replication mapping only after the source and target identities are confirmed. Test the next authorised create/replicate scenario, then reconcile both keys and dependent references. Do not use a blind resend to resolve a disputed identity.</li>
    </ol>
    <p>SAP describes MDG consolidation as a configurable sequence and matching as producing candidate groups for review. These features are not proof that consolidation is installed or suitable in your landscape. See <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5c1f0c571db4124ce10000000a4450e5.html">SAP Help: Consolidating Master Data</a> and <a href="https://help.sap.com/docs/PRODUCT_ID/6d52de87aa0d4fb6a90924720a5b0549/aebd1cbd6ee04e79970f3076af689204.html">SAP Help: Configure Matching for Business Partner</a>. Match review and governance approval are separate from technical similarity.</p>

    <h2>Read-only AI experiment: group evidence before the steward decides</h2>
    <p><strong>Proposal, not a delivered tool:</strong> run a 10-business-day offline review on 40 synthetic or properly de-identified BP candidate pairs with independently recorded decisions: confirmed same entity, separate entities and unresolved. Keep the same cases, evidence packet and reviewer for the baseline and AI-assisted trial; randomise the order to reduce learning bias. Remove personal and financial identifiers before any model use.</p>
    <div class="decision-table"><table><thead><tr><th>Baseline (no AI)</th><th>Assistant task</th><th>Human control</th></tr></thead><tbody>
      <tr><td>Deterministic rules group pairs by equal identifiers, normalised name/address, mapping presence and missing evidence. A reviewer opens the evidence in a fixed checklist.</td><td>Read-only assistant clusters the already approved evidence, lists conflicts and missing proofs, and suggests the next verification question with evidence references.</td><td>Steward approves or rejects candidate grouping and owns all create, merge, blocking and mapping decisions; model has no SAP credentials or write-back.</td></tr>
    </tbody></table></div>
    <p><strong>Measure both value and harm:</strong> precision of “same entity” suggestions = correctly suggested confirmed pairs / all suggested same-entity pairs; recall = correctly suggested confirmed pairs / all confirmed pairs in the labelled set; false-positive rate = separate-entity pairs wrongly suggested as same / all labelled separate-entity pairs. Also record unresolved/abstained pairs, missing or fabricated evidence links, median reviewer minutes per case and correction minutes. Publish actual numerators, denominators and median times; do not claim improvement from this proposed pilot.</p>
    <p><strong>Stop conditions:</strong> stop if any source record leaves the approved environment, if the assistant invents a reference or implies an SAP write, or if a false-positive “same entity” recommendation would be treated as automatic action. Do not advance beyond a feasibility test if false-positive rate exceeds 5% on the small labelled set, or reviewer time does not improve without loss of decision quality. A 40-pair pilot cannot establish a production safety rate.</p>

    <h2>Control proof and sources</h2>
    <p>Keep a small evidence record: object category, both BP IDs, source systems, creation channel, match rule/version, candidate score if available, approved identity evidence reference, mapping check, downstream usage check, reviewer, decision, and approval timestamp. Redact the identity content in any public example. Track <em>candidate-to-confirmed conversion</em>, false-positive review cost and post-migration unmatched keys by batch, not only the number of alerts.</p>
    <p>SAP's <a href="https://help.sap.com/docs/SAP_ERP_SPV/de1b9c94c8594d6f94fe66ae423d5d70/4d523f354bf74b049cfd5f59aa56aac4.html">MDG Duplicate Check</a> explains why a potential-match score is a warning rather than a final decision (older ERP MDG documentation; do not reuse its configuration path for all S/4HANA releases). The S/4HANA 2025 FPS01 SAP Help pages linked above support the newer configurable check, matching and consolidation boundaries. The controls, experiment thresholds and synthetic example in this article are editorial proposals, not SAP-delivered defaults.</p>
    <p><strong>Editorial state — 12 November 2026:</strong> source links were researched for this draft revision; the new diagnosis and AI experiment still require independent SAP and editorial approval by Dzmitryi Kharlanau. The earlier <code>last_reviewed</code> value is historical and does not certify this revision. This page remains <code>needs_verification</code>, <code>verified: false</code>, <code>noindex</code> and excluded from the sitemap.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-number-range-diagnostics/">SAP Number Range Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
