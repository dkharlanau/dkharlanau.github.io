---
layout: default
title: "Professional Signals — Dzmitryi Kharlanau"
description: "Dated professional signals on SAP AMS, integration reliability, master data, and practical AI for support operations."
permalink: /news/
robots: noindex,follow
sitemap: false
---

<section class="section notes-landing">
  <header class="section-heading">
    <p class="eyebrow">Professional Signals</p>
    <h1>{{ page.title }}</h1>
    <p class="lead">Short, dated observations on SAP releases, support patterns, and operational signals that affect AMS and integration work.</p>
  </header>

  <div class="notes-grid">
    {% assign items = site.news | sort: 'date' | reverse %}
    {% if items == empty %}
    <p class="lead">No signals published yet. This section is being prepared.</p>
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
