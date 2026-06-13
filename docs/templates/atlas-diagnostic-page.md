<!-- TEMPLATE: atlas-diagnostic-page.md -->
<!-- Copy this file, replace all [bracketed] placeholders, and remove these comments. -->

---
layout: default
title: "[Descriptive diagnostic title]"
description: "[Conservative one-line summary of the symptom or failure this page diagnoses.]"
permalink: /atlas/diagnostics/[slug]/
last_modified_at: YYYY-MM-DD
atlas_section: diagnostics
domain: SAP AMS
subdomain: [e.g., Master data and MDG | Integration | Order to cash | Procure to pay]
concept_type: diagnostic guide
sap_area: "[SAP area label]"
business_process: "[Business process name]"
status: needs_verification
verified: false
last_reviewed: YYYY-MM-DD
author: Dzmitryi Kharlanau
tags:
  - <tag-1>
  - <tag-2>
related:
  - /atlas/diagnostics/[related-page]/
source_files:
  - "private-source/[path-to-source-draft]"
robots: noindex,follow
sitemap: false
---

<!-- REQUIRED METADATA BLOCK -->
<!-- All fields below must be filled before publishing. -->

**Source:** [URL or citation]
**Date checked:** YYYY-MM-DD
**Confidence:** [high | medium | low]
**Related page/topic:** [URL or topic cluster from atlas_index.yml]
**Practical implication:** [One sentence: what should a reader do differently after reading this?]
**Tags:** [tag-1, tag-2]

<!-- NO PRIVATE/CLIENT DATA
Do not include internal system names, client identifiers, ticket numbers,
or any data that could trace back to a specific customer or employer.
Use generic process language and synthetic examples only.
-->

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">[Page title]</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>[Page title]</h1>
    <p class="note-subtitle">[Subtitle — what symptom or failure this page covers.]</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>[business process]</dd></div>
      <div><dt>SAP area</dt><dd>[SAP area]</dd></div>
      <div><dt>Reviewed</dt><dd>[DD Mon YYYY]</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>[One to three short paragraphs framing the diagnostic: what failure pattern it covers, why it matters, and the boundary between this page and related pages.]</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>[Symptom 1 — observed behavior or user report.]</li>
      <li>[Symptom 2 — downstream effect or business impact.]</li>
      <li>[Symptom 3 — error message, status, or exception category.]</li>
    </ul>

    <h2>Likely causes</h2>
    <p>[Group causes by category: master data, configuration, integration, timing, or user action. Keep each cause concrete enough to test.]</p>
    <ul>
      <li><strong>Master data:</strong> [e.g., missing or inconsistent partner, material, or account record.]</li>
      <li><strong>Configuration:</strong> [e.g., condition type, release strategy, or output type not set as expected.]</li>
      <li><strong>Integration:</strong> [e.g., IDoc failure, qRFC queue, or middleware timeout.]</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <p>[List transactions, tables, or monitoring objects. Be conservative: note landscape-dependent behavior and avoid prescribing customizing changes.]</p>
    <ul>
      <li><strong>[Transaction or tool]:</strong> [What to look for.]</li>
      <li><strong>[Table or log]:</strong> [What field or status indicates the cause.]</li>
    </ul>

    <h2>Evidence to collect</h2>
    <ul>
      <li>[Data point 1 — document number, status, timestamp.]</li>
      <li>[Data point 2 — master data key or configuration object.]</li>
      <li>[Data point 3 — integration object such as IDoc number or queue name.]</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>[State what this page does not cover. Prevent misuse by clearly marking topics that need change control, custom development, or functional consultation.]</p>

    <h2>Safe automation opportunity</h2>
    <p>[Optional: describe how an AI-assisted support agent or script could help gather evidence or flag patterns, with conservative limits.]</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/[next-page]/">[Next page title]</a> — [why to go there.]</li>
      <li><a href="/atlas/diagnostics/[next-page]/">[Next page title]</a> — [why to go there.]</li>
    </ul>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/[section]/[related-page]/">[Related page title]</a></li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>

<!-- SAMPLE OUTPUT (remove when using the template) -->
<!--
---
layout: default
title: "SAP Purchase Order Diagnostics"
description: "A diagnostic guide for purchase order failures, release strategy blocks, and price mismatch symptoms in SAP MM."
permalink: /atlas/diagnostics/sap-purchase-order-diagnostics/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procure to pay
concept_type: diagnostic guide
sap_area: "Materials Management / Purchasing"
business_process: "Procure to pay"
status: needs_verification
verified: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - p2p
  - procurement
related:
  - /atlas/diagnostics/sap-release-strategy-diagnostics/
  - /atlas/diagnostics/sap-invoice-verification-diagnostics/
  - /atlas/maps/procure-to-pay-map/
source_files:
  - "private-source/kb-drafts/sap-domain-atlas/domains/procurement/diagnostics/purchase-order.md"
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/maps/procure-to-pay-map/
**Practical implication:** Use the PO number and status to decide whether the blocker is master data, release strategy, price, or integration before opening a support ticket.
**Tags:** sap-ams, p2p, procurement

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Purchase Order Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP Purchase Order Diagnostics</h1>
    <p class="note-subtitle">A diagnostic guide for purchase order failures, release strategy blocks, and price mismatch symptoms in SAP MM.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>Materials Management / Purchasing</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Purchase order issues usually cluster around release strategy, price or account determination, vendor or material master data, and follow-on integration. This page gives a first-pass split so the team collects the right evidence before escalation.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>PO status remains incomplete or blocked and cannot be converted to a goods receipt or invoice.</li>
      <li>Release strategy does not trigger, or approvers do not see the PO in their worklist.</li>
      <li>Price or account assignment does not match the purchase requisition or contract.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Master data:</strong> vendor, material, or info record missing or inconsistent.</li>
      <li><strong>Configuration:</strong> release strategy, pricing procedure, or account assignment category mismatch.</li>
      <li><strong>Integration:</strong> IDoc or AIF failure when PO is sent to a supplier or downstream system.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>ME21N/ME22N/ME23N:</strong> PO header and item status, release strategy tab, account assignment.</li>
      <li><strong>ME54N/ME55:</strong> release strategy traces if the workflow path is unclear.</li>
      <li><strong>WE02/WE05:</strong> outbound IDoc status if supplier integration is involved.</li>
    </ul>

    <h2>Evidence to collect</h2>
    <ul>
      <li>PO number, item number, and current status.</li>
      <li>Release strategy code and approval log.</li>
      <li>Vendor, material, and purchasing organization.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page does not cover customizing changes to release strategies, pricing procedures, or message determination. Those require functional review and change control.</p>

    <h2>Safe automation opportunity</h2>
    <p>A support agent could summarize PO status, release strategy, and recent IDoc errors from the document header to reduce the time spent on status collection.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-release-strategy-diagnostics/">SAP Release Strategy Diagnostics</a> — if the PO is blocked on approval.</li>
      <li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a> — if the symptom appears during invoice receipt.</li>
    </ul>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure-to-Pay Map</a></li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
-->
