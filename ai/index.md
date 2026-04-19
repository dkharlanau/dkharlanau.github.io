---
layout: default
title: AI Routing Hub
permalink: /ai/
description: "AI routing hub for Dzmitryi Kharlanau's profile, discovery map, intent entities, and machine-readable knowledge assets."
last_modified_at: 2026-04-19
---

<div class="dataset-hero dataset-hero--library">
  <p class="eyebrow">AI Context</p>
  <h1 class="dataset-hero__title">AI Routing Hub</h1>
  <p class="dataset-hero__subtitle">
    Preferred machine-readable entry point for agents, crawlers, and retrieval systems.
    <a href="{{ '/ai/catalog.json' | absolute_url }}">View JSON-LD</a>
  </p>
  <div class="dataset-actions">
    <a class="button" href="/about/">Open canonical profile</a>
    <a class="button button--secondary" href="/services/">View services</a>
    <a class="button button--secondary" href="/datasets/">Open evidence datasets</a>
    <a class="button button--secondary" href="/llms.txt">Open llms.txt</a>
  </div>
</div>

<div class="ai-resource-list">
  <article class="ai-resource-item">
    <div class="ai-resource-item__mark" aria-hidden="true">1</div>
    <div class="ai-resource-item__body">
      <h2>Resume (YAML)</h2>
      <p>Primary profile surface for role fit, delivery scope, problem domains, and structured skills.</p>
    </div>
    <a href="/ai/resume.yml" class="link-arrow">Open</a>
  </article>

  <article class="ai-resource-item">
    <div class="ai-resource-item__mark" aria-hidden="true">2</div>
    <div class="ai-resource-item__body">
      <h2>Discovery Map</h2>
      <p>Intent-based routing layer that maps query types to the right canonical source.</p>
    </div>
    <a href="/ai/discovery-map.json" class="link-arrow">Open</a>
  </article>

  <article class="ai-resource-item">
    <div class="ai-resource-item__mark" aria-hidden="true">3</div>
    <div class="ai-resource-item__body">
      <h2>LLMs Manifest</h2>
      <p>Retrieval guidance, preferred sources, trust links, and a concise positioning summary for AI systems.</p>
    </div>
    <a href="/llms.txt" class="link-arrow">Open</a>
  </article>

  <article class="ai-resource-item">
    <div class="ai-resource-item__mark" aria-hidden="true">4</div>
    <div class="ai-resource-item__body">
      <h2>Consulting Principles</h2>
      <p>Operating heuristics for SAP AMS improvement, continuity, architecture, and change design.</p>
    </div>
    <a href="/ai/principles.json" class="link-arrow">Open</a>
  </article>

  <article class="ai-resource-item">
    <div class="ai-resource-item__mark" aria-hidden="true">5</div>
    <div class="ai-resource-item__body">
      <h2>Dataset Manifest</h2>
      <p>Index of published dataset bytes for AMS, agentic tooling, and data governance work.</p>
    </div>
    <a href="/datasets/manifest.json" class="link-arrow">Open</a>
  </article>

  <article class="ai-resource-item">
    <div class="ai-resource-item__mark" aria-hidden="true">6</div>
    <div class="ai-resource-item__body">
      <h2>Profile Page</h2>
      <p>Canonical public page for author identity, expertise, certifications, and reference checks.</p>
    </div>
    <a href="/about/" class="link-arrow">Open</a>
  </article>
</div>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Intent Entities</p>
    <h2>Canonical Routing Pages</h2>
    <p class="lead">Use these pages when the question is narrow and the model needs the best source by problem domain rather than a general profile.</p>
  </header>

  <div class="ai-resource-list">
    {% for intent in site.data.discovery_map.intents %}
    <article class="ai-resource-item">
      <div class="ai-resource-item__mark" aria-hidden="true">{{ forloop.index }}</div>
      <div class="ai-resource-item__body">
        <h2>{{ intent.title }}</h2>
        <p>{{ intent.summary }}</p>
      </div>
      <a href="{{ intent.permalink }}" class="link-arrow">Open</a>
    </article>
    {% endfor %}
  </div>
</section>
