---
layout: default
title: "Notes — Dzmitryi Kharlanau | SAP O2C & Integration"
description: "Working notes on SAP order-to-cash consulting, clean-core S/4HANA strategy, event-driven integration, and AI-enabled operations."
permalink: /notes/
---

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Notes</p>
    <h1>Thinking in transition</h1>
    <p class="lead">Short-form perspectives on SAP transformation, AMS, integration, clean core, and AI-supported operations.</p>
  </header>

  <ul class="topic-cloud notes-topic-cloud">
    <li><a href="/notes/ams/">AMS</a></li>
    <li><a href="/notes/process-audit/">Process audit</a></li>
    <li><a href="/notes/composable-erp/">Composable ERP</a></li>
    <li><a href="/notes/ai-ml/">AI around SAP</a></li>
  </ul>

  <div class="notes-grid">
    {% assign notes = site.notes | sort: 'date' | reverse %}
    {% for note in notes %}
    <article class="note-card">
      <header class="note-card-header">
        <h3 class="note-card-title"><a href="{{ note.url }}">{{ note.title }}</a></h3>
        {% if note.subtitle %}<p class="note-card-subtitle">{{ note.subtitle }}</p>{% endif %}
      </header>
      <div class="note-card-meta">
        {% assign published_on = note.date | default: note.published %}
        {% if published_on %}
        <span class="note-card-date">{{ published_on | date: "%d %b %Y" }}</span>
        {% endif %}
        {% if note.tags %}
        <ul class="note-tags">
          {% for tag in note.tags %}
          <li>{{ tag }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
      <p class="note-card-summary">{{ note.summary | default: note.excerpt }}</p>
      <div class="note-card-footer">
        <a class="link-arrow" href="{{ note.url }}">Read note</a>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

