---
layout: default
title: Data Catalog
permalink: /ai/
description: "A machine-readable catalog of datasets, schemas, and structured knowledge for AI agents."
---

<div class="dataset-hero">
  <p class="eyebrow">AI Context</p>
  <h1 class="dataset-hero__title">Data Catalog</h1>
  <p class="dataset-hero__subtitle">
    Structured datasets, schemas, and knowledge graphs optimized for LLM consumption.
    <a href="{{ '/ai/catalog.json' | absolute_url }}">View JSON-LD</a>
  </p>
</div>

<div class="dataset-grid">
  {% assign catalog = site.data.catalog %} 
  <!-- Note: We can't easily parse catalog.json if it is not in _data. 
       We will manually list the core datasets or rely on the JSON-LD for machines. -->
  
  <div class="neub-card">
    <h3>Resume (YAML)</h3>
    <p>Structured professional profile.</p>
    <a href="/ai/resume.yml" class="link-arrow">Download</a>
  </div>

  <div class="neub-card">
    <h3>Dataset Manifest</h3>
    <p>Index of all published dataset bytes.</p>
    <a href="/datasets/manifest.json" class="link-arrow">Download</a>
  </div>

   <div class="neub-card">
    <h3>Consulting Principles</h3>
    <p>Core heuristics for engagement.</p>
    <a href="/ai/principles.json" class="link-arrow">Download</a>
  </div>
</div>

<script type="application/ld+json">
{% include_relative catalog.json %}
</script>
