<!-- TEMPLATE: atlas-fact-update.md -->
<!-- Copy this file, replace all [bracketed] placeholders, and remove these comments. -->

---
layout: default
title: "[Atlas page title — updated]"
description: "[One-line summary of the update. Keep the original description if only adding a fact.]"
permalink: /atlas/[section]/[slug]/
last_modified_at: YYYY-MM-DD
atlas_section: [concepts | diagnostics | ai-operations | automation | data-quality | sap | maps]
domain: [domain label]
subdomain: [subdomain label]
concept_type: [concept | diagnostic guide | operating pattern | data quality | process map | automation pattern]
sap_area: "[SAP area label]"
business_process: "[process name]"
status: reviewed
verified: [true | false]
last_reviewed: YYYY-MM-DD
author: Dzmitryi Kharlanau
related:
  - /atlas/[section]/[related-page]/
  - /atlas/[section]/[another-related-page]/
source_files:
  - "private-source/[path-to-source-draft]"
robots: index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1
---

<!-- REQUIRED METADATA BLOCK -->
<!-- All fields below must be filled before publishing. -->

**Source:** [URL or citation]
**Date checked:** YYYY-MM-DD
**Confidence:** [high | medium | low]
**Related page/topic:** [URL or topic cluster from atlas_index.yml]
**Practical implication:** [One sentence: what should a reader do differently?]
**Tags:** [tag-1, tag-2]

<!-- NO PRIVATE/CLIENT DATA
Do not include internal system names, client identifiers, ticket numbers,
or any data that could trace back to a specific customer or employer.
Use generic process language.
-->

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/[section]/">[Section title]</a></li>
    <li aria-current="page">[Page title]</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas [Section]</p>
    <h1>[Page title]</h1>
    <p class="note-subtitle">[Subtitle — what this page explains.]</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>[process name]</dd></div>
      <div><dt>SAP area</dt><dd>[SAP area]</dd></div>
      <div><dt>Reviewed</dt><dd>[DD Mon YYYY]</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>[Main concept or diagnostic frame. One to three short paragraphs.]</p>

    <h2>Updated fact</h2>
    <p>[The new fact, correction, or addition. State what changed and why.]</p>
    <p><strong>Source:</strong> <a href="[source-url]">[source label]</a> (checked [date])</p>
    <p><strong>Confidence:</strong> [high | medium | low]</p>

    <h2>Practical implication</h2>
    <p>[What a support team or architect should do differently based on this update.]</p>

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
title: "SAP ATP Is Not Inventory"
description: "A practical explanation of why SAP available-to-promise is customer commitment logic, not a simple inventory count."
permalink: /atlas/concepts/sap-atp-is-not-inventory/
atlas_section: concepts
domain: SAP operations
subdomain: Sales and fulfillment
concept_type: business concept
sap_area: "Availability check / ATP"
business_process: Order to cash
status: reviewed
verified: true
last_reviewed: 2026-05-06
author: Dzmitryi Kharlanau
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /services/sap-ams-consulting/
source_files:
  - "private-source/kb-drafts/sap-domain-atlas/domains/sales/concepts/atp.md"
robots: index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1
---

**Source:** https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ (public documentation)
**Date checked:** 2026-05-06
**Confidence:** high
**Related page/topic:** /atlas/concepts/order-to-cash/
**Practical implication:** Support teams should diagnose ATP from document context and commitment logic, not from stock quantity alone.
**Tags:** sap-ams, o2c, logistics

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">SAP ATP Is Not Inventory</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Concept</p>
    <h1>SAP ATP is not inventory</h1>
    <p class="note-subtitle">ATP is promise logic. Inventory is stock visibility. Confusing the two creates bad support tickets and bad customer commitments.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Availability check / ATP</dd></div>
      <div><dt>Reviewed</dt><dd>06 May 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Available-to-promise answers a commitment question: what quantity can the business responsibly promise to a customer, and when? It is not the same as asking what quantity exists physically in a plant or warehouse.</p>

    <h2>Updated fact</h2>
    <p>SAP S/4HANA 2023 FPS01 introduced aATP (advanced ATP) with product allocation integration. The core principle remains: ATP is commitment logic, not stock quantity.</p>
    <p><strong>Source:</strong> <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/">SAP Help Portal</a> (checked 2026-05-06)</p>
    <p><strong>Confidence:</strong> high</p>

    <h2>Practical implication</h2>
    <p>Support teams should continue diagnosing ATP from document context and commitment logic, not from stock quantity alone. aATP adds allocation rules but does not change the fundamental distinction.</p>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
-->