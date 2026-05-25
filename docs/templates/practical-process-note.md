<!-- TEMPLATE: practical-process-note.md -->
<!-- Copy this file, replace all [bracketed] placeholders, and remove these comments. -->

---
layout: default
title: "[Process or pattern title]"
description: "[One-line summary of the pattern and when to use it.]"
permalink: /atlas/[section]/[slug]/
last_modified_at: YYYY-MM-DD
atlas_section: [concepts | diagnostics | ai-operations | automation | data-quality | sap | maps]
domain: [domain label]
subdomain: [subdomain label]
concept_type: [operating pattern | diagnostic guide | checklist | automation pattern]
sap_area: "[SAP area label]"
business_process: "[process name]"
status: reviewed
verified: [true | false]
last_reviewed: YYYY-MM-DD
author: Dzmitryi Kharlanau
related:
  - /atlas/[section]/[related-page]/
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
    <p class="note-subtitle">[Subtitle — what this pattern covers.]</p>
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
    <h2>When to use this</h2>
    <p>[Describe the situation where this pattern applies. Be specific about symptoms or triggers.]</p>

    <h2>The pattern</h2>
    <p>[Step-by-step or structured description of the pattern. Use lists for clarity.]</p>
    <ul>
      <li><strong>Step 1:</strong> [First action or check.]</li>
      <li><strong>Step 2:</strong> [Second action or check.]</li>
      <li><strong>Step 3:</strong> [Third action or check.]</li>
    </ul>

    <h2>Evidence to collect</h2>
    <p>[What data, documents, or logs are needed to apply this pattern safely.]</p>

    <h2>Boundaries and non-goals</h2>
    <p>[What this pattern does not cover. Prevent misuse by stating limits clearly.]</p>

    <h2>Source</h2>
    <p><a href="[source-url]">[source label]</a> (checked YYYY-MM-DD)</p>
    <p><strong>Confidence:</strong> [high | medium | low]</p>

    <h2>Practical implication</h2>
    <p>[What a team should do differently after reading this.]</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>

<!-- SAMPLE OUTPUT (remove when using the template) -->
<!--
---
layout: default
title: "IDoc Retry Assistant — Practical Process Note"
description: "A conservative pattern for retrying failed IDocs without creating duplicates or incorrect follow-on documents."
permalink: /atlas/automation/idoc-retry-assistant/
last_modified_at: 2026-05-26
atlas_section: automation
domain: Automation
subdomain: SAP support
concept_type: operating pattern
sap_area: "AIF / IDoc"
business_process: Support operations
status: reviewed
verified: false
last_reviewed: 2026-05-26
author: Dzmitryi Kharlanau
related:
  - /atlas/automation/operational-memory-for-sap-ams/
  - /ai/integration-reliability/
source_files:
  - "private-source/kb-drafts/sap-domain-atlas/domains/automation/concepts/idoc-retry.md"
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern (not yet verified against public SAP documentation)
**Date checked:** 2026-05-26
**Confidence:** medium
**Related page/topic:** /atlas/automation/operational-memory-for-sap-ams/
**Practical implication:** Always check for existing follow-on documents before retrying an IDoc.
**Tags:** integration, idoc, aif, automation

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/automation/">Automation</a></li>
    <li aria-current="page">IDoc Retry Assistant</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Automation</p>
    <h1>IDoc retry assistant</h1>
    <p class="note-subtitle">A conservative pattern for retrying failed IDocs without creating duplicates or incorrect follow-on documents.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Support operations</dd></div>
      <div><dt>SAP area</dt><dd>AIF / IDoc</dd></div>
      <div><dt>Reviewed</dt><dd>26 May 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>When to use this</h2>
    <p>Use this pattern when an IDoc has failed in status 51 or 64, the error is transient (network, temporary lock, missing master data that has since been corrected), and the business needs the document posted without creating a duplicate.</p>

    <h2>The pattern</h2>
    <ul>
      <li><strong>Step 1:</strong> Check WE02/WE05 for the IDoc status and error text. Capture the message type, partner, and status record.</li>
      <li><strong>Step 2:</strong> Verify whether any follow-on document was already created. Check the target application table or transaction for existing records.</li>
      <li><strong>Step 3:</strong> If no follow-on document exists, correct the root cause (master data, configuration, or transient condition).</li>
      <li><strong>Step 4:</strong> Retry the IDoc using BD87 or the relevant AIF retry function. Monitor for new errors.</li>
      <li><strong>Step 5:</strong> Document the failure cause, correction, and retry result in the operational memory (KEDB or runbook).</li>
    </ul>

    <h2>Evidence to collect</h2>
    <p>IDoc number, message type, partner, status history, error text, target document number (if any), and the business impact of the delay.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This pattern does not cover structural IDoc changes, partner profile reconfiguration, or mass retry scenarios. Those require change control and testing.</p>

    <h2>Source</h2>
    <p>Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.</p>
    <p><strong>Confidence:</strong> medium</p>

    <h2>Practical implication</h2>
    <p>Always check for existing follow-on documents before retrying an IDoc. A blind retry in a landscape with complex posting logic can create duplicates that are harder to clean up than the original error.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
-->
