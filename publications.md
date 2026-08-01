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

<main class="evidence-canvas publications-page" data-evidence-canvas>
  <section class="evidence-canvas__hero section" aria-labelledby="publication-title">
    <div>
      <p class="evidence-canvas__eyebrow">Public record / writing</p>
      <h1 id="publication-title">Technical writing that can be checked.</h1>
      <p>Public SAP notes, architecture writing, and machine-readable knowledge surfaces. Each item retains its source and date where available.</p>
      <div class="evidence-canvas__actions">
        <a href="#publication-register">Browse the register <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
        <a href="/ai/publications/">Open the Markdown dataset <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
      </div>
    </div>
    <dl class="evidence-ledger" aria-label="Publication summary">
      <div><dt>Records</dt><dd>{{ publications | size }}</dd></div>
      <div><dt>Publishers</dt><dd>{{ publishers | size }}</dd></div>
      <div><dt>SAP notes</dt><dd>{{ sap_count }}</dd></div>
      <div><dt>Knowledge assets</dt><dd>{{ knowledge_count }}</dd></div>
    </dl>
  </section>

  <section class="evidence-canvas__section section" aria-labelledby="publication-scope-title">
    <header class="evidence-canvas__heading">
      <p class="evidence-canvas__eyebrow">What the record covers</p>
      <h2 id="publication-scope-title">Writing follows the work.</h2>
    </header>
    <div class="evidence-signals">
      <article><span>01</span><div><h3>SAP technical work</h3><p>Configuration, debugging, extension, and process-support notes.</p></div></article>
      <article><span>02</span><div><h3>Architecture and delivery</h3><p>Event-driven systems, bounded contexts, and implementation choices.</p></div></article>
      <article><span>03</span><div><h3>Public knowledge assets</h3><p>Structured material for readers, search, and AI retrieval.</p></div></article>
    </div>
  </section>

  <section class="evidence-canvas__section section" id="publication-register" aria-labelledby="publication-register-title">
    <header class="evidence-canvas__heading evidence-canvas__heading--split">
      <div><p class="evidence-canvas__eyebrow">Source register</p><h2 id="publication-register-title">Publication records</h2></div>
      <p>{{ site.data.publications.privacy_note }}</p>
    </header>
    <div class="evidence-filter" role="toolbar" aria-label="Filter publication records">
      <button type="button" data-evidence-filter="all" aria-pressed="true">All <span>{{ publications | size }}</span></button>
      {% for group in grouped %}<button type="button" data-evidence-filter="{{ group.name | escape }}" aria-pressed="false">{{ group.name }} <span>{{ group.items | size }}</span></button>{% endfor %}
    </div>
    <p class="evidence-filter__status" aria-live="polite" data-evidence-status>{{ publications | size }} records shown</p>
    <ol class="evidence-register">
      {% for item in publications %}
      <li data-evidence-record data-evidence-category="{{ item.category | escape }}">
        <time datetime="{{ item.published | default: '' }}">{{ item.published | default: "No date" }}</time>
        <div><p>{{ item.publisher }}</p><h3>{{ item.name }}</h3>{% if item.description %}<small>{{ item.description }}</small>{% endif %}</div>
        <span>{{ item.category }}</span>
        <a href="{{ item.url }}" target="_blank" rel="noopener noreferrer">Open <span class="material-symbols-outlined" aria-hidden="true">north_east</span></a>
      </li>
      {% endfor %}
    </ol>
  </section>
</main>
