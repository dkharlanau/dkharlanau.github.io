---
layout: default
title: "Knowledge Entity Registry — SAP, Logistics and AI Topics"
description: "Canonical topic identities used across SAP logistics, integration, data governance, Business AI and AI architecture pages on this site."
permalink: /entities/
status: reviewed
verified: true
content_model: reference
robots: index,follow
sitemap: true
last_modified_at: 2026-08-16
schema_updated_at: 2026-11-21
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
      <p>The scope is SAP and enterprise AI concepts used on this site. The registry gives each topic a stable ID, and the related guides explain its application and limitations.</p>
      <p>A topic ID refers to one concept. For example, the <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">IDoc status guide</a> uses <a href="#sap-idoc-status">IDoc status records</a> as its subject and links the related <a href="#sap-idoc">IDoc message</a>. Use the related guide for release-specific checks and recovery boundaries.</p>
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

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {% for pair in site.data.knowledge_entities.entities %}
    {% assign entity = pair[1] %}
    {
      "@id": {{ entity.id | absolute_url | jsonify }},
      "@type": {{ entity.type | jsonify }},
      "name": {{ entity.name | jsonify }},
      "description": {{ entity.description | jsonify }}{% if entity.same_as and entity.same_as.size > 0 %},
      "sameAs": {{ entity.same_as | jsonify }}{% endif %}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>
