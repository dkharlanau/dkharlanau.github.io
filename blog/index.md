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

  {% assign posts = site.blog | sort: 'date' | reverse %}
  {% if posts == empty %}
  <p class="lead">Essays and deep-dives on systems thinking, SAP delivery, and automation patterns that keep enterprise platforms trustworthy.</p>
  {% else %}
  {% assign featured = posts | first %}
  <a class="atlas-card blog-featured" href="{{ featured.url }}">
    <p class="eyebrow">Latest article</p>
    <h2>{{ featured.title }}</h2>
    <p>{{ featured.summary | default: featured.description | default: featured.excerpt | strip_html | truncate: 220 }}</p>
    <span class="link-arrow">Read article</span>
  </a>
  <ul class="blog-list">
    {% for post in posts offset: 1 %}
    {% assign published_on = post.date | default: post.published %}
    <li>
      {% if published_on %}<time datetime="{{ published_on | date_to_xmlschema }}">{{ published_on | date: '%b %d, %Y' }}</time>{% endif %}
      <div class="blog-list__main">
        <a href="{{ post.url }}">{{ post.title }}</a>
        <p>{{ post.summary | default: post.description | default: post.excerpt | strip_html | truncate: 140 }}</p>
      </div>
      <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
    </li>
    {% endfor %}
  </ul>
  {% endif %}
</section>
