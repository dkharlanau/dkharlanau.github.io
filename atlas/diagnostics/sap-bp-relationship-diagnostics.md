---
layout: default
title: "SAP BP Relationship Diagnostics"
description: "Trace missing SAP BP contacts from migration identity and relationship evidence to sales-area assignments and document partner determination."
search_intent: "Diagnose missing SAP BP contact person after migration or replication"
last_modified_at: 2026-11-26
permalink: /atlas/diagnostics/sap-bp-relationship-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "BP / relationships / CVI"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - business-partner
related:
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
  - /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
  - /atlas/sap/sap-partner-determination-failures/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP BP Relationship Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP BP relationship diagnostics</h1>
    <p class="note-subtitle">Find why a migrated or replicated BP contact exists but is missing from the expected sales process.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>BP / relationships / CVI</dd></div>
      <div><dt>Indexing</dt><dd>Noindex; new editorial review pending.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Start with the missing business result</h2>
    <p>A customer may have a valid contact person in Business Partner (BP) master data, yet that person may not appear in a sales order. A BP relationship records a link between two business partners. A sales partner function describes the responsibility of a partner in a business transaction. These are related controls, not the same control.</p>
    <p>In SAP S/4HANA, a contact person is represented by a person BP linked to a customer or supplier. SAP Sales also supports the contact-person partner type (AP). Whether and how a particular contact is selected in a sales document depends on the relevant partner determination procedure and data. The presence of a relationship alone does not prove that a particular sales document must contain that contact. See SAP references 1–3 below.</p>

    <h2>Find the first missing link</h2>
    <p>For a contact-person migration or replication incident, follow the chain: approved source relationship → source-to-target contact identity mapping → target BP relationship → customer sales-area partner data → sales document partner determination. Check each stage separately. The following is a proposed diagnostic control, not a standard SAP migration report.</p>
    <ol>
      <li><strong>Business requirement and source:</strong> obtain the approved customer, contact, relationship category, relevant date, expected sales area (sales organization, distribution channel and division), and document type. Confirm whether the contact is mandatory, optional or outside migration scope. The approved scope and mapping specification are the authority for intended data, not simply every row in a legacy extract.</li>
      <li><strong>Identity:</strong> reconcile both the organization and person identifiers in the target. Use the approved mapping or migration result; do not assume that the legacy contact identifier is also the target contact partner number. A mapping with multiple possible targets needs human resolution.</li>
      <li><strong>Relationship:</strong> display the target BP and the linked person in the release-appropriate BP app or transaction. Confirm both endpoints, category, direction and validity against the relevant key date. If the relationship is absent, compare the approved source, the actual message or load result and the target state. A successful technical message is not proof of the relationship. Check whether the evidence is complete and authorized before calling an empty result a defect.</li>
      <li><strong>Sales-area assignment:</strong> display the customer partner functions for the exact sales area and verify the contact partner number where the approved design requires an explicit assignment. Use the actual partner type and configured function; the presence of a BP relationship does not prove that this assignment exists.</li>
      <li><strong>Document determination:</strong> inspect the affected document's partner list, its type, the relevant header or item procedure, mandatory settings and configured source. SAP can use another customer master record or other sources for partner determination (reference 3). Verify the determination path before assuming that a missing explicit assignment is an error. Check whether the document predates the master-data change; do not assume that correcting the master will refresh existing documents. Prove the expected behavior in an approved test environment without posting a production transaction.</li>
    </ol>

    <h2>One synthetic migration case</h2>
    <p>Assume customer C-100 and legacy contact L-17 must be migrated for two sales areas. The target person BP is P-701, with contact partner number CP-92. The approved requirement explicitly calls for CP-92 in sales area A; the contact is optional and not in scope for sales area B. All identifiers here are invented.</p>
    <p>The target relationship between C-100's BP and P-701 is present and valid. Area A has no required assignment; area B has none either. A new test order for area A does not propose the contact. A count of migrated BP relationships would report success. A blanket completeness rule across all sales areas would report two defects. The evidence supports only one candidate defect: the missing assignment in area A. Confirm the document's configured source before approving correction.</p>
    <p>SAP documents an example of this sequencing issue for the staging-table migration object <em>Customer - extend existing record by new org levels</em> in S/4HANA Cloud Public Edition 2608 (reference 4). Contact IDs are assigned during migration; SAP provides a post-migration contact mapping task. This object has restrictions, including no updates to existing sales areas and a same-ID requirement for customer and BP. Check the supported object and release in your own project; do not treat that example as a general instruction to rerun migration.</p>

    <h2>Choose a correction at the failing control</h2>
    <ul>
      <li><strong>Repair identity or relationship data:</strong> if the target link is absent or wrong, the data owner confirms the two identities and approved relationship dates before a controlled correction or replay. Do not create a second person BP or extend an expired relationship merely to remove an error. Verify the target relationship and intended contact number afterwards.</li>
      <li><strong>Repair the required sales-area assignment:</strong> when identity and relationship are correct but the approved explicit assignment is missing, the customer master-data owner corrects that segment through the governed process. Reconcile only the authorized sales areas and test a new document. If the gap repeats, repair the mapping or migration sequence rather than adding contacts one by one.</li>
      <li><strong>Correct the determination rule or the expectation:</strong> if the target master data satisfies the approved design, ask the SD process owner to review partner source, procedure and document history. A configuration change has wider effects and needs regression tests across affected document types. If the contact is optional or outside scope, record a valid exception instead of changing master data.</li>
    </ul>

    <h2>A ten-day AI-assisted reconciliation test</h2>
    <p>Hypothesis: an assistant can group incomplete migration evidence faster than a consultant reading individual exports, without increasing incorrect defect flags. It is not needed for exact joins, date comparisons or scope checks; use deterministic rules for those.</p>
    <p>Prepare 40 synthetic or approved anonymized cases: 20 real defects (identity, relationship, assignment or determination) and 20 valid exceptions or inconclusive cases. Include optional contacts, excluded sales areas, multiple possible mappings, restricted evidence and old documents. A data steward and SD consultant label the expected next check and defect status before evaluation. Keep identifiers consistent but remove names, addresses and communication data.</p>
    <p>Baseline: a spreadsheet joins approved scope, contact mapping, target relationships and sales-area assignments, with explicit missing-evidence and exception rules; a consultant checks the determination evidence. AI variant: give an offline assistant the same rule output and sanitized notes or log excerpts. It returns the case ID, proposed failing stage, evidence row IDs, missing evidence and next read-only check, or abstains. It cannot create a BP, change a mapping, assign a partner, call SAP or approve a change.</p>
    <p>Run both methods on the same cases in counterbalanced order. Count correct next checks out of 40, missed defects out of 20 confirmed defects, and false positives (valid or inconclusive cases incorrectly called defects) out of 20 non-confirmed cases. Count abstentions separately; include human verification time in the median minutes per case. Require at least 20% lower median time, no increase in false positives or missed defects versus baseline, and no reduction in next-check accuracy. Stop immediately on an invented identity match, unauthorized data exposure or a recommendation to bypass approval. If the targets are missed, keep the rules and manual review. These are proposed acceptance criteria, not measured results.</p>

    <h2>Evidence and boundaries</h2>
    <p>Record the source and target systems, extraction time, mapping version, approved scope, both BP identifiers, contact partner number, relationship category and dates, sales area, document type, actual partner list and exact error. A steward approves data changes; the SD owner approves process-rule changes. CVI synchronization, cross-system replication, and document partner determination have different evidence and owners. This guide does not prescribe direct table updates or universal transaction codes. Check release-specific display tools and local configuration.</p>

    <h2>Official SAP references</h2>
    <ol>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/0871bd534f22b44ce10000000a174cb4.html">Partner Type and Partner Function</a> — contact-person identity and partner type in Sales.</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/3ca897ae1c384861ab8df820af8859e4.html">Address Determination in SD Documents</a> — BP contact data and the separation of sales-area partner determination from address determination (S/4HANA 2025 FPS01).</li>
      <li><a href="https://learning.sap.com/courses/fundamental-customizing-in-sap-s-4hana-sales/configuring-partner-functions-and-a-partner-determination-procedure_b9d77500-5034-440e-86bb-883b1961fc51">Configuring Partner Functions and a Partner Determination Procedure</a> — procedure assignment and alternative sources.</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/b127a62235874379bd4f8fbaf1cea619.html">Customer - extend existing record by new org levels</a> — contact mapping, sequencing and migration-object restrictions (Public Edition 2608).</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9cd0efd395874f248a69ce2d5f770b85/2ac9145598f03f6ae10000000a44176d.html">Find Business Partner Relationship Basic Data by Elements</a> — relationship category, key date, validity and authorization limits in the documented Transactional Banking service; not a required Sales API.</li>
    </ol>
    <p>Source check: 2026-11-26 (public SAP documentation and SAP Learning). Author: Dzmitryi Kharlanau. New editorial and SAP review pending author approval.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP CVI Synchronization Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-partner-determination-failures/">SAP Partner Determination Failures</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
