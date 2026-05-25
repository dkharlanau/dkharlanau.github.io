<!-- TEMPLATE: source-addition.md -->
<!-- Copy this file, replace all [bracketed] placeholders, and remove these comments. -->

---
layout: default
title: "[Page title — source update]"
description: "[One-line summary. Keep original if only adding sources.]"
permalink: /[section]/[slug]/
last_modified_at: YYYY-MM-DD
robots: noindex,follow
sitemap: false
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

<article class="section note-detail">
  <header class="note-header">
    <p class="eyebrow">Source addition</p>
    <h1>[Page title]</h1>
    <p class="note-subtitle">[Subtitle or context for the source addition.]</p>
  </header>

  <div class="note-body">
    <h2>New source</h2>
    <p><strong>[Source label or title]</strong></p>
    <p>[Brief description of what the source says and why it matters to this topic.]</p>
    <p><a href="[source-url]">[source-url]</a> (checked YYYY-MM-DD)</p>
    <p><strong>Confidence:</strong> [high | medium | low]</p>

    <h2>Why this source was added</h2>
    <p>[Explain the gap this source fills: stronger evidence, newer data, contradictory finding, or broader context.]</p>

    <h2>Practical implication</h2>
    <p>[What a reader should change or consider based on this source.]</p>

    <h2>Related pages</h2>
    <p><a href="[related-page-url]">[Related page title]</a></p>
  </div>
</article>

<!-- SAMPLE OUTPUT (remove when using the template) -->
<!--
---
layout: default
title: "SAP Master Data Quality — Source Update"
description: "Added SAP Help Portal reference for Business Partner CVI alignment."
permalink: /atlas/data-quality/sap-master-data-quality/
last_modified_at: 2026-05-26
robots: noindex,follow
sitemap: false
---

**Source:** https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ee3fd5c0d5ab4f6495515c71f108cdce/c6f59e9e8c5c4b8e8e0b8d1e3a6c7f8d.html
**Date checked:** 2026-05-26
**Confidence:** high
**Related page/topic:** /atlas/data-quality/sap-master-data-quality/
**Practical implication:** BP governance should include CVI synchronization checks before mass updates.
**Tags:** master-data, mdg, bp

<article class="section note-detail">
  <header class="note-header">
    <p class="eyebrow">Source addition</p>
    <h1>SAP Master Data Quality — Source Update</h1>
    <p class="note-subtitle">Added authoritative source on BP/CVI alignment checks.</p>
  </header>

  <div class="note-body">
    <h2>New source</h2>
    <p><strong>SAP Help Portal: Business Partner — Customer/Vendor Integration (CVI)</strong></p>
    <p>The official documentation clarifies the sequence for BP-to-customer/vendor synchronization and the tables involved (CVI_CUST_LINK, CVI_VEND_LINK). This fills a gap in the original page where the technical mechanism was described from practice but not cross-referenced to vendor documentation.</p>
    <p><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ee3fd5c0d5ab4f6495515c71f108cdce/c6f59e9e8c5c4b8e8e0b8d1e3a6c7f8d.html">SAP Help Portal</a> (checked 2026-05-26)</p>
    <p><strong>Confidence:</strong> high</p>

    <h2>Why this source was added</h2>
    <p>The original page described CVI misalignment as a common failure mode but did not cite the official synchronization mechanism. Adding the SAP Help Portal reference strengthens the claim and makes it easier for readers to verify.</p>

    <h2>Practical implication</h2>
    <p>BP governance should include CVI synchronization checks before mass updates. Support teams diagnosing BP-related order blocks should verify CVI_LINK table consistency.</p>

    <h2>Related pages</h2>
    <p><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a></p>
  </div>
</article>
-->
