---
layout: default
title: "SAP operations, integration, and automation blog"
description: "Practical long-form articles on SAP AMS operations, integration architecture, logistics, data, and automation."
permalink: /blog/
schema_type: CollectionPage
hide_global_cta: true
---

{% assign posts = site.blog | sort: 'date' | reverse %}
{% assign featured = posts | first %}

<div class="journal-canvas">
  <header class="journal-canvas__hero" data-reveal>
    <div>
      <p class="journal-canvas__eyebrow">Journal / field notes</p>
      <h1>Technical writing for SAP operating decisions.</h1>
      <p>Long-form analysis of support work, integration architecture, logistics, data, and controlled automation. Each article starts with the operating constraint rather than a product pitch.</p>
    </div>
    <dl class="journal-canvas__scope">
      <div><dt>Read for</dt><dd>Evidence, boundaries, and practical next checks.</dd></div>
      <div><dt>Use with</dt><dd><a href="/atlas/">Knowledge Atlas</a> for diagnostic context.</dd></div>
      <div><dt>Browse by</dt><dd><a href="/blog/topics/">Categories and tags</a></dd></div>
    </dl>
  </header>

  {% if featured %}
  {% assign featured_tag = featured.tags | first | default: featured.category | default: 'Field note' %}
  {% assign featured_on = featured.date | default: featured.published %}
  <section class="journal-canvas__featured blog-featured" data-reveal aria-labelledby="journal-featured-title">
    <p class="journal-canvas__eyebrow">Latest article</p>
    <a href="{{ featured.url }}">
      <span class="journal-canvas__featured-meta">{{ featured_tag }}{% if featured_on %} · {{ featured_on | date: '%d %b %Y' }}{% endif %}</span>
      <h2 id="journal-featured-title">{{ featured.title }}</h2>
      <p>{{ featured.summary | default: featured.description | default: featured.excerpt | strip_html | truncate: 220 }}</p>
      <span class="journal-canvas__read">Read the article <i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></span>
    </a>
  </section>
  {% endif %}

  <section class="journal-canvas__archive" data-reveal aria-labelledby="journal-archive-title">
    <header><p class="journal-canvas__eyebrow">Article archive</p><h2 id="journal-archive-title">Choose the question that matches the work.</h2><a href="/blog/topics/">Browse topics <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a></header>
    {% if posts == empty %}
    <p class="journal-canvas__empty">No articles have been published yet.</p>
    {% else %}
    <ol class="journal-route-list blog-list">
      {% for post in posts offset: 1 %}
      {% assign published_on = post.date | default: post.published %}
      {% assign post_tag = post.tags | first | default: post.category | default: 'Field note' %}
      <li><a href="{{ post.url }}"><time datetime="{{ published_on | date_to_xmlschema }}">{% if published_on %}{{ published_on | date: '%Y.%m.%d' }}{% endif %}</time><strong>{{ post.title }}</strong><small>{{ post_tag }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a></li>
      {% endfor %}
    </ol>
    {% endif %}
  </section>
</div>
