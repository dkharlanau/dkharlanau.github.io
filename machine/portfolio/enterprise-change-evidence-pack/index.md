---
layout: default
title: "Enterprise Change Evidence Pack — Reproducible Reference Case"
description: "A synthetic reference case connecting research context, architecture composition, visual rendering, and project assurance with explicit trust boundaries."
permalink: /machine/portfolio/enterprise-change-evidence-pack/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-01
hide_global_cta: true
hide_site_share: true
ai_sidecar: /products/reference-cases/enterprise-change-evidence-pack/manifest.json
tags:
  - public-projects
  - reference-case
  - enterprise-architecture
  - project-assurance
---

{% assign case = site.data.portfolio_reference_case %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/machine/">Machine Layer</a></li><li><a href="/machine/portfolio/">Public Project Map</a></li><li aria-current="page">Enterprise Change Evidence Pack</li></ol>
</nav>

<div class="research-canvas portfolio-map portfolio-case">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Synthetic reference case / bounded evidence chain</p>
      <h1>Follow one change. Keep every claim bounded.</h1>
      <p><strong>The problem:</strong> a source-backed concern can lose its provenance when it becomes an architecture decision, a presentation visual, and a project claim. This pack preserves the difference between an implemented handoff, a documented boundary, and a manually authored demonstration bridge.</p>
      <a class="research-canvas__button" href="#reference-workflow">Inspect the workflow <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Reference case status">
      <p>{{ case.artifacts.file_count }} digest-bound files / {{ case.edges.size }} declared edges</p>
      <div class="research-canvas__signal-line"><span>{{ case.status_counts.implemented }}</span><strong>Implemented</strong><small>Reproduced by committed fixtures and product commands.</small></div>
      <div class="research-canvas__signal-line"><span>{{ case.status_counts["demonstration-only"] }}</span><strong>Demonstration-only</strong><small>Explicit synthetic bridges; no runtime adapter claim.</small></div>
      <div class="research-canvas__signal-line"><span>{{ case.status_counts.documented }}</span><strong>Documented</strong><small>Known boundary, intentionally not exercised here.</small></div>
      <em>Client-free public fixture. Human approval and production authority are absent.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Evidence boundary">
    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>
    <p><strong>Evidence boundary:</strong> structural validity, exact file digests, and the two executed product paths can be reproduced. Architecture fitness, implementation, external adoption, live SAP execution, and business approval are not proven.</p>
    <a href="{{ case.urls.manifest }}">Read manifest <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="portfolio-case__overview" data-reveal aria-labelledby="case-overview-title">
    <header>
      <p class="research-canvas__eyebrow">The practical job</p>
      <h2 id="case-overview-title">Turn a source-backed concern into reviewable project evidence.</h2>
    </header>
    <div>
      <article><span>01</span><h3>Context</h3><p>A public research packet raises a durability and recovery concern for a synthetic sales-order integration.</p></article>
      <article><span>02</span><h3>Decision</h3><p>Enterprise Architecture Composer evaluates explicit patterns and retains the selected architecture, alternatives, and decision trace.</p></article>
      <article><span>03</span><h3>Review</h3><p>Visual Workbench renders the coordinate-free projection; Project Evidence Graph analyzes the digest-bound assurance relationships.</p></article>
    </div>
  </section>

  <section class="portfolio-case__workflow" id="reference-workflow" data-reveal aria-labelledby="case-workflow-title">
    <header>
      <p class="research-canvas__eyebrow">Producer → consumer ledger</p>
      <h2 id="case-workflow-title">The status belongs to each edge.</h2>
      <p>A product appearing in the pack does not imply that every adjacent runtime integration exists.</p>
    </header>
    <ol>
      {% for edge in case.edges %}
      <li>
        <div class="portfolio-case__edge-heading">
          <span>{{ edge.status }}</span>
          <h3>{{ edge.producer | replace: '-', ' ' }} <em aria-hidden="true">→</em> {{ edge.consumer | replace: '-', ' ' }}</h3>
        </div>
        <p>{{ edge.boundary }}</p>
        <details>
          <summary>Verification and contract</summary>
          <code>{{ edge.verification_command }}</code>
          <a href="{{ edge.source_contract_url }}">Open source contract <span aria-hidden="true">↗</span></a>
        </details>
      </li>
      {% endfor %}
    </ol>
  </section>

  <section class="portfolio-case__artifact" data-reveal aria-labelledby="case-artifact-title">
    <div>
      <p class="research-canvas__eyebrow">Business-readable projection</p>
      <h2 id="case-artifact-title">The visual stays a view, not the architecture source.</h2>
      <p>The SVG is produced from the Composer visual projection and validated by Visual Workbench. Its exact bytes are pinned in the artifact inventory. Changing the diagram does not silently change the upstream decision.</p>
      <a href="/products/reference-cases/enterprise-change-evidence-pack/artifacts/architecture.executive.svg">Open SVG artifact <span aria-hidden="true">↗</span></a>
    </div>
    <a class="portfolio-case__artifact-preview" href="/products/reference-cases/enterprise-change-evidence-pack/artifacts/architecture.executive.svg" aria-label="Open the executive architecture SVG">
      <img src="/products/reference-cases/enterprise-change-evidence-pack/artifacts/architecture.executive.svg" alt="Synthetic executive architecture showing channels, an API gateway, order orchestration, SAP S/4HANA, idempotency, queuing, monitoring, and human review boundaries.">
    </a>
  </section>

  <section class="portfolio-case__ledger" data-reveal aria-labelledby="case-ledger-title">
    <header>
      <p class="research-canvas__eyebrow">Artifact ledger</p>
      <h2 id="case-ledger-title">Every retained file has an owner, contract, size, and digest.</h2>
      <p>{{ case.artifacts.digest_scope | capitalize }}. SHA-256 establishes content identity; it does not establish authority or approval.</p>
    </header>
    <ul>
      {% for artifact in case.artifacts.files %}
      <li>
        <a href="/products/reference-cases/enterprise-change-evidence-pack/{{ artifact.path }}"><strong>{{ artifact.path }}</strong><span>{{ artifact.kind | replace: '_', ' ' }}</span></a>
        <small>{{ artifact.producer }} · {{ artifact.bytes }} bytes · <code>{{ artifact.sha256 | slice: 0, 12 }}…</code></small>
      </li>
      {% endfor %}
    </ul>
  </section>

  <section class="research-canvas__method portfolio-case__run" aria-labelledby="case-run-title">
    <div><p class="research-canvas__eyebrow">Run locally</p><h2 id="case-run-title">Verify the retained pack first.</h2></div>
    <ol>
      <li><span>01</span><strong>Clone</strong><p><code>git clone https://github.com/dkharlanau/dkharlanau.github.io.git</code></p></li>
      <li><span>02</span><strong>Open the case</strong><p><code>cd dkharlanau.github.io/products/reference-cases/enterprise-change-evidence-pack</code></p></li>
      <li><span>03</span><strong>Validate</strong><p><code>python3 validate.py</code></p></li>
    </ol>
  </section>

  <section class="portfolio-map__actions portfolio-case__actions" data-reveal aria-labelledby="case-actions-title">
    <header>
      <p class="research-canvas__eyebrow">Continue with evidence</p>
      <h2 id="case-actions-title">Challenge the pack or propose one bounded edge.</h2>
      <p>The local validator checks the retained pack. Full regeneration requires the participating product checkouts and their documented commands.</p>
    </header>
    <div>
      <a href="{{ case.urls.source }}" target="_blank" rel="noopener noreferrer"><span>01</span><strong>Read the source guide</strong><small>Use the complete regeneration sequence, product prerequisites, and expected results.</small><em aria-hidden="true">↗</em></a>
      <a href="{{ case.urls.expected_artifacts }}"><span>02</span><strong>Inspect exact digests</strong><small>Review the byte counts, SHA-256 bindings, and bounded assertions.</small><em aria-hidden="true">↗</em></a>
      <a href="{{ case.urls.integration_proposal }}" target="_blank" rel="noopener noreferrer"><span>03</span><strong>Propose an integration</strong><small>Name the producer, consumer, safe fixture, trust boundary, and verification command.</small><em aria-hidden="true">↗</em></a>
    </div>
  </section>
</div>
