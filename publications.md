---
layout: default
title: "Publications | Dzmitryi Kharlanau"
description: "Public articles, SAP technical notes, architecture writing, and machine-readable knowledge surfaces by Dzmitryi Kharlanau."
permalink: /publications/
sitemap: true
last_modified_at: 2026-04-24
---

{% assign publications = site.data.publications.items %}
{% assign sap_count = publications | where: "category", "SAP technical notes" | size %}
{% assign knowledge_count = publications | where: "category", "Datasets and knowledge surfaces" | size %}
{% assign architecture_count = publications | where: "category", "Architecture and product thinking" | size %}
{% assign grouped = publications | group_by: "category" %}
{% assign publishers = publications | group_by: "publisher" %}

<section class="section publications-page publications-page__hero">
  <div class="publications-hero">
    <div class="publications-hero__copy">
      <p class="eyebrow">Publications</p>
      <h1>Technical writing, knowledge maps, and reusable SAP notes.</h1>
      <p class="lead">A cleaned public register of articles, SAP Community notes, Hashnode posts, dataset surfaces, and DOI-backed publication metadata from the LinkedIn export.</p>
      <div class="publications-hero__actions">
        <a class="button button--primary" href="#publication-register">View register</a>
        <a class="button button--secondary" href="/ai/publications/">Open Markdown dataset</a>
      </div>
    </div>
    <dl class="publications-hero__stats" aria-label="Publication summary">
      <div class="publications-stat">
        <dt>Total records</dt>
        <dd>{{ publications | size }}</dd>
      </div>
      <div class="publications-stat">
        <dt>Publishers</dt>
        <dd>{{ publishers | size }}</dd>
      </div>
      <div class="publications-stat">
        <dt>SAP notes</dt>
        <dd>{{ sap_count }}</dd>
      </div>
      <div class="publications-stat">
        <dt>Knowledge surfaces</dt>
        <dd>{{ knowledge_count }}</dd>
      </div>
    </dl>
  </div>
</section>

<section class="section publications-page" id="publication-signals">
  <header class="section-heading">
    <p class="eyebrow">Reading the record</p>
    <h2>What the publications show</h2>
    <p class="lead">The writing pattern is practical: SAP implementation notes first, then broader architecture and machine-readable knowledge assets for AMS, MDG, and agentic systems.</p>
  </header>

  <div class="publications-signal-grid">
    <article class="publications-signal-card">
      <p class="publications-signal-card__meta">Implementation depth</p>
      <h3>SAP technical notes</h3>
      <p>Posts cover BOPF, MRP, OData testing, SAP TM inbound debugging, CDS e-mail templates, MB52 extensions, ME5*N field control, and scheduling agreements.</p>
    </article>
    <article class="publications-signal-card">
      <p class="publications-signal-card__meta">Architecture thread</p>
      <h3>Systems and product thinking</h3>
      <p>Architecture-oriented writing covers event-driven architecture, DDD reading notes, and human-centered backlog thinking as a bridge between implementation and operating model design.</p>
    </article>
    <article class="publications-signal-card">
      <p class="publications-signal-card__meta">Reusable assets</p>
      <h3>Knowledge surfaces</h3>
      <p>Dataset and knowledge-map publications make the work easier to cite, crawl, and reuse across human readers and AI retrieval systems.</p>
    </article>
  </div>
</section>

<section class="section publications-page" id="publication-categories">
  <header class="section-heading">
    <p class="eyebrow">Dataset structure</p>
    <h2>Publication groups</h2>
    <p class="lead">Categories are editorial groupings for the page. The dataset keeps each public URL separately, including publisher and publication date where available.</p>
  </header>

  <div class="publications-category-grid">
    {% for group in grouped %}
    <article class="publications-category-card">
      <p class="publications-category-card__count">{{ group.items | size }}</p>
      <h3>{{ group.name }}</h3>
      <p>{{ group.items | map: "publisher" | uniq | join: ", " }}</p>
    </article>
    {% endfor %}
  </div>
</section>

<section class="section publications-page" id="publication-register">
  <header class="section-heading">
    <p class="eyebrow">Register</p>
    <h2>Publication records</h2>
    <p class="lead">{{ site.data.publications.privacy_note }}</p>
  </header>

  <div class="publications-register">
    {% for item in publications %}
    <article class="publications-record">
      <div class="publications-record__date">
        <span>{{ item.published | default: "No date" }}</span>
      </div>
      <div class="publications-record__body">
        <p class="publications-record__meta">{{ item.publisher }}</p>
        <h3>{{ item.name }}</h3>
        {% if item.description %}<p class="publications-record__description">{{ item.description }}</p>{% endif %}
        <p class="publications-record__category">{{ item.category }}</p>
      </div>
      <a class="publications-record__link" href="{{ item.url }}" target="_blank" rel="noopener noreferrer">Open</a>
    </article>
    {% endfor %}
  </div>
</section>
