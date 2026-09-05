---
layout: default
title: "Compose Target Enterprise Architecture — Explainable Architecture Workbench"
description: "A public deterministic workbench for composing target enterprise architecture from business scope, explicit constraints, current landscape facts, and reviewable decisions."
permalink: /services/compose-target-enterprise-architecture/
last_modified_at: 2026-09-05
---

<section class="section note-detail">
  <article class="note-article neub-card">
    <header class="note-header">
      <p class="eyebrow">Public architecture product</p>
      <h1>Compose a target enterprise architecture from explicit business context</h1>
      <p class="note-subtitle">Business scope in. Explainable responsibilities, integration choices, migration steps, trust boundaries, and delivery work out.</p>
    </header>

    <div class="note-body">
      <p><strong>Enterprise Architecture Composer</strong> is a public, deterministic architecture-synthesis workbench. It starts from selected business processes, operating constraints, current application facts, and explicit non-functional requirements. It then derives a reviewable target blueprint and shows why each recommendation exists.</p>

      <p><a href="https://dkharlanau.github.io/enterprise-architecture-composer/">Open the live workbench</a> · <a href="https://github.com/dkharlanau/enterprise-architecture-composer">View the source and contracts on GitHub</a></p>

      <h2>What the product does</h2>
      <ul>
        <li>Composes capabilities, logical system responsibilities, data ownership, and cross-system integration needs from a bounded business scope.</li>
        <li>Evaluates integration patterns from explicit drivers such as latency, consistency, fan-out, replay, ordering, volume, and partner boundaries.</li>
        <li>Separates current application instances from target system roles and models introduce-before-retire migration dependencies.</li>
        <li>Makes public, private, partner, identity, privileged, sensitive-data, residency, and audit trust boundaries visible without claiming compliance.</li>
        <li>Turns architecture decisions into deterministic work packages and dependency waves.</li>
        <li>Exports Git-reviewable bundles, architecture review reports, visual projections, and starter handoffs to specialized as-code repositories.</li>
      </ul>

      <h2>What makes it different from a catalog or modeling tool</h2>
      <p>The product does not try to become a universal enterprise repository. A CMDB or application portfolio tool records what exists. A diagram editor records how someone drew a model. Composer answers a narrower decision question: <em>given these explicit business facts and constraints, what architecture responsibilities and decisions are implied, what remains unknown, and what delivery work follows?</em></p>

      <p>The canvas is therefore a projection, not the source of truth. Stable IDs, rules, evidence, human overrides, and exported contracts remain inspectable outside the UI. There is deliberately no opaque universal architecture score.</p>

      <h2>Reference workflow</h2>
      <div class="process-rail" aria-label="Enterprise Architecture Composer workflow">
        <div class="process-rail__step"><strong>1. Shape context</strong><span>Select process scope, scale, current systems, constraints, NFRs, and security facts.</span></div>
        <div class="process-rail__step"><strong>2. Compose</strong><span>Derive the target responsibilities, flows, data ownership, trust boundaries, and open decisions.</span></div>
        <div class="process-rail__step"><strong>3. Review</strong><span>Inspect rule traces, compare options, record human acceptance or overrides, and test scenarios.</span></div>
        <div class="process-rail__step"><strong>4. Deliver</strong><span>Generate dependency-aware work packages and hand adopted semantics to their owning repositories.</span></div>
      </div>

      <h2>Public reference boundary</h2>
      <ul>
        <li>The reference catalog is synthetic and focused on B2B manufacturing.</li>
        <li>The browser workbench has no backend and does not require an AI provider.</li>
        <li>Unknown facts are surfaced as decisions instead of being guessed.</li>
        <li>Industry and vendor packs are advisory overlays; they cannot silently replace deterministic core rules.</li>
        <li>Security composition identifies review boundaries and required controls but reports compliance as <code>not-assessed</code>.</li>
      </ul>

      <h2>Related architecture-as-code projects</h2>
      <p>Composer owns the architecture proposal and rationale, then hands adopted semantics to the project that should maintain them:</p>
      <ul>
        <li><a href="https://github.com/dkharlanau/process-as-code">Process as Code</a> — maintained process semantics.</li>
        <li><a href="https://github.com/dkharlanau/interface-as-code">Interface as Code</a> — operational integration contracts.</li>
        <li><a href="https://github.com/dkharlanau/mapping-as-code">Mapping as Code</a> — field and value transformation intent.</li>
        <li><a href="https://github.com/dkharlanau/enterprise-change-graph">Enterprise Change Graph</a> — change-specific impact analysis.</li>
        <li><a href="https://github.com/dkharlanau/visual-workbench">Visual Workbench</a> — presentation and rendering.</li>
      </ul>

      <h2>Try a reference scenario</h2>
      <p>Open the <a href="https://dkharlanau.github.io/enterprise-architecture-composer/">browser workbench</a> for the interactive manufacturing scenario, or use the <a href="https://github.com/dkharlanau/enterprise-architecture-composer/tree/main/examples/scenarios">versioned scenario files</a> and CLI for reproducible architecture review.</p>

      <h2>Where this fits in my work</h2>
      <p>This project is part of a wider architecture-as-code direction: make enterprise decisions explicit, testable, reviewable in Git, and easier to hand from architecture into delivery without hiding uncertainty behind presentation layers.</p>

      <p><a href="/services/sap-integration-architecture/">SAP integration architecture</a> · <a href="/services/enterprise-ai-pilot-design/">Enterprise AI pilot design</a> · <a href="/about/">Professional profile</a></p>
    </div>
  </article>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Enterprise Architecture Composer",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web browser; Node.js CLI",
  "isAccessibleForFree": true,
  "url": "https://dkharlanau.github.io/enterprise-architecture-composer/",
  "codeRepository": "https://github.com/dkharlanau/enterprise-architecture-composer",
  "author": {
    "@type": "Person",
    "@id": "https://dkharlanau.github.io/#dkharlanau"
  },
  "description": "A deterministic workbench for composing explainable target enterprise architecture from explicit business context and constraints."
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://dkharlanau.github.io/"},
    {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://dkharlanau.github.io/services/"},
    {"@type": "ListItem", "position": 3, "name": "Compose Target Enterprise Architecture", "item": "https://dkharlanau.github.io/services/compose-target-enterprise-architecture/"}
  ]
}
</script>
