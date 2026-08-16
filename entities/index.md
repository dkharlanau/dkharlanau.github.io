---
layout: default
title: "Knowledge Entity Registry — SAP, Logistics and AI Topics"
description: "Canonical topic identities used across SAP logistics, integration, data governance, Business AI and AI architecture pages on this site."
permalink: /entities/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-16
last_reviewed: 2026-08-16
hide_global_cta: true
structured_data:
  type: CollectionPage
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li aria-current="page">Knowledge Entities</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Knowledge / Entity Registry</p>
      <h1>One topic.<br />One stable identity.</h1>
      <p>This registry gives important SAP and AI topics a stable identity across articles, graphs, datasets, search metadata and machine-readable pages. It helps connect different views without pretending that a tag is an entity.</p>
    </div>
  </header>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Canonical topics</p>
      <h2>Entities used by the knowledge graph.</h2>
      <p>The descriptions are short on purpose. Detailed explanations stay on the topic pages; this page is the canonical identity layer.</p>
    </header>
    <div class="ecg-heuristic-grid">
      {% for pair in site.data.knowledge_entities.entities %}
      {% assign key = pair[0] %}
      {% assign entity = pair[1] %}
      <article id="{{ key }}">
        <span>ENTITY</span>
        <h3>{{ entity.name }}</h3>
        <p>{{ entity.description }}</p>
        {% if entity.same_as and entity.same_as.size > 0 %}
        <p><a href="{{ entity.same_as | first }}" rel="external">External reference</a></p>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>
</div>
