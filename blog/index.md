---
layout: default
title: "SAP operations, integration, and automation blog"
description: "Practical long-form articles on SAP AMS operations, integration architecture, logistics, data, and automation."
permalink: /blog/
schema_type: CollectionPage
---

<section class="section notes-landing">
  <header class="section-heading">
    <p class="eyebrow">Blog</p>
    <h1>{{ page.title }}</h1>
    <p class="lead">Long-form articles for SAP practitioners working through support operations, integration architecture, logistics, data, and automation decisions.</p>
    <p><a class="link-arrow" href="/blog/topics/">Browse categories and tags</a></p>
  </header>

  <div class="notes-grid">
    {% assign posts = site.blog | sort: 'date' | reverse %}
    {% if posts == empty %}
    <p class="lead">Essays and deep-dives on systems thinking, SAP delivery, and automation patterns that keep enterprise platforms trustworthy.</p>
    {% else %}
    {% for post in posts %}
    <article class="note-card neub-card">
      <header>
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        {% if post.subtitle %}<p class="note-card-subtitle">{{ post.subtitle }}</p>{% endif %}
      </header>
      <div class="note-card-meta">
        {% assign published_on = post.date | default: post.published %}
        {% if published_on %}
        <span>{{ published_on | date: "%d %b %Y" }}</span>
        {% endif %}
        {% if post.tags %}
        <ul class="note-tags">
          {% for tag in post.tags %}
          <li>{{ tag }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
      <p>{{ post.summary | default: post.description | default: post.excerpt }}</p>
      <a class="link-arrow" href="{{ post.url }}">Read article</a>
    </article>
    {% endfor %}
    {% endif %}
  </div>
</section>
