---
layout: default
title: "Professional Radar — Dzmitryi Kharlanau"
description: "Monitored professional signals, observations, and review candidates. Durable knowledge belongs in the Atlas after review."
permalink: /radar/
robots: noindex,follow
sitemap: false
---

<section class="section notes-landing">
  <header class="section-heading">
    <p class="eyebrow">Professional Radar</p>
    <h1>{{ page.title }}</h1>
    <p class="lead">Professional Radar collects signals, observations, and review candidates. Durable knowledge belongs in the <a href="/atlas/">Knowledge Atlas</a> after review.</p>
  </header>

  <div class="notes-grid">
    {% assign items = site.radar | sort: 'date' | reverse %}
    {% if items == empty %}
    <p class="lead">No radar signals published yet. This section is being prepared.</p>
    {% else %}
    {% for item in items %}
    <article class="note-card neub-card">
      <header>
        <h2><a href="{{ item.url }}">{{ item.title }}</a></h2>
        {% if item.subtitle %}<p class="note-card-subtitle">{{ item.subtitle }}</p>{% endif %}
      </header>
      <div class="note-card-meta">
        {% assign published_on = item.date | default: item.published %}
        {% if published_on %}
        <span>{{ published_on | date: "%d %b %Y" }}</span>
        {% endif %}
        {% if item.source %}
        <span>Source: {{ item.source }}</span>
        {% endif %}
        {% if item.confidence %}
        <span>Confidence: {{ item.confidence }}</span>
        {% endif %}
        {% if item.topics %}
        <ul class="note-tags">
          {% for topic in item.topics %}
          <li>{{ topic }}</li>
          {% endfor %}
        </ul>
        {% endif %}
        {% if item.tags %}
        <ul class="note-tags">
          {% for tag in item.tags %}
          <li>{{ tag }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
      <p>{{ item.summary | default: item.excerpt }}</p>
      <a class="link-arrow" href="{{ item.url }}">Read signal</a>
    </article>
    {% endfor %}
    {% endif %}
  </div>
</section>
