---
layout: default
title: "SAP Key Mapping Diagnostics"
description: "A conservative diagnostic frame for key mapping issues in SAP multi-system landscapes."
permalink: /atlas/diagnostics/sap-key-mapping-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "Key mapping / multi-system"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - integration
related:
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
  - /atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/
  - /atlas/diagnostics/sap-vendor-master-replication-diagnostics/
  - /atlas/diagnostics/sap-customer-master-replication-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Key Mapping Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP key mapping diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why objects have different keys across systems, causing duplicates, broken links, or failed replications.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>Key mapping / multi-system</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until key mapping behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>In multi-system SAP landscapes, the same business object may have different keys in different systems. Key mapping maintains the relationship between these keys. When mapping is missing, wrong, or inconsistent, replication creates duplicates, interfaces fail, and reporting produces fragmented results. The support goal is to identify which object type is affected, which systems are involved, and whether the gap is in the mapping table, the replication model, or the interface logic.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Replication creates a new object in the target system instead of updating the existing one.</li>
      <li>Interface reports 'object not found' even though the object exists under a different key.</li>
      <li>Reporting or analytics shows duplicate records for the same business entity.</li>
      <li>MDG or ALE replication log shows key mapping errors.</li>
      <li>Customer or vendor number in S/4 does not match the corresponding BP number or external system key.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing mapping entry:</strong> the object was created directly in the target system without going through the mapping process.</li>
      <li><strong>Wrong mapping entry:</strong> the source key is mapped to a different target key than intended.</li>
      <li><strong>Number range conflict:</strong> source and target systems use overlapping number ranges, causing collisions.</li>
      <li><strong>Mapping table not maintained for new object type:</strong> the interface or replication expects mapping but the object type was recently added and mapping is not set up.</li>
      <li><strong>Manual creation bypass:</strong> the object was created manually in the target system, bypassing the mapping logic.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>Key mapping tables — landscape-specific tables that map source keys to target keys.</li>
      <li>MDG key mapping UI — if MDG manages the mapping.</li>
      <li>WE02 — IDoc status for ALE replication to see if key mapping errors are reported.</li>
      <li>Object display in both source and target systems — compare keys and attributes.</li>
      <li>Number range status (SNRO) — check if ranges overlap between systems.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>Key mapping tables</strong> — landscape-specific (e.g., USMD1700 for MDG).</li>
      <li><strong>CVI_LINK</strong> — CVI link between BP and customer/vendor.</li>
      <li><strong>NRIV</strong> — number range intervals.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the object type, source system key, target system, and expected target key.</li>
      <li>Check the key mapping table or MDG key mapping UI for an existing entry.</li>
      <li>If no entry exists, determine if the object was created manually in the target system or if the mapping was never maintained.</li>
      <li>If the entry exists but is wrong, trace how the wrong mapping was created.</li>
      <li>Check number ranges in both systems for overlaps or conflicts.</li>
      <li>Verify the interface or replication model uses the correct mapping logic.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create the missing key mapping entry between source and target systems.</li>
      <li>Correct the wrong mapping entry and evaluate the impact on existing transactions.</li>
      <li>Adjust number ranges to prevent future collisions.</li>
      <li>If duplicates were created, evaluate merge, deactivation, or re-keying options with master data governance.</li>
      <li>Update the interface or replication model to enforce mapping for new object types.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Key mapping issues are usually maintenance gaps or number range conflicts. A useful ticket should include: object type, source system, source key, target system, expected target key, actual target key, and whether the object was created manually or via replication.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a key mapping configuration guide. It does not cover number range design, MDG key mapping setup, or interface mapping logic. It does not replace SAP's multi-system integration documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/">SAP Mdg To S4 Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">SAP Vendor Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
