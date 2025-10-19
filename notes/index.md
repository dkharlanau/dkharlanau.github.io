---
layout: default
title: "Notes — Dzmitryi Kharlanau | SAP O2C & Integration"
description: "Working notes on SAP order-to-cash consulting, clean-core S/4HANA strategy, event-driven integration, and AI-enabled operations."
permalink: /notes/
---

<section class="section notes-landing">
  <header class="section-heading">
    <p class="eyebrow">Notes</p>
    <h1>{{ page.title }}</h1>
    <p class="lead">Short-form thinking, architecture playbooks, and transformation diaries that keep the operating model learnable.</p>
  </header>

  <div class="notes-grid">
    {% assign notes = site.notes | sort: 'date' | reverse %}
    {% for note in notes %}
    <article class="note-card neub-card">
      <header>
        <h2><a href="{{ note.url }}">{{ note.title }}</a></h2>
        {% if note.subtitle %}<p class="note-card-subtitle">{{ note.subtitle }}</p>{% endif %}
      </header>
      <div class="note-card-meta">
        {% assign published_on = note.date | default: note.published %}
        {% if published_on %}
        <span>{{ published_on | date: "%d %b %Y" }}</span>
        {% endif %}
        {% if note.tags %}
        <ul class="note-tags">
          {% for tag in note.tags %}
          <li>{{ tag }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
      <p>{{ note.summary | default: note.excerpt }}</p>
      <a class="link-arrow" href="{{ note.url }}">Read note</a>
    </article>
    {% endfor %}
  </div>
</section>
