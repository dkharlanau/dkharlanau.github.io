---
layout: default
title: "Blog topics: SAP operations, integration, and automation"
description: "Browse the blog by SAP operations, automation, integration, logistics, solution architecture, and precise practitioner tags."
permalink: /blog/topics/
schema_type: CollectionPage
---

<section class="section notes-landing">
  <header class="section-heading">
    <p class="eyebrow">Blog navigation</p>
    <h1>{{ page.title }}</h1>
    <p class="lead">A compact map of the operational questions covered in the blog. Articles awaiting factual review remain intentionally noindex.</p>
  </header>

  {% assign posts = site.blog | where_exp: 'post', 'post.category != nil' | sort: 'migration_sequence' %}
  {% assign categories = posts | map: 'category' | uniq | sort %}
  <nav class="note-further" aria-label="Blog categories">
    <h2>Categories</h2>
    <ul class="note-further__list">
      {% for category in categories %}<li><a class="link-arrow" href="#{{ category | slugify }}">{{ category }}</a></li>{% endfor %}
    </ul>
  </nav>

  {% for category in categories %}
  {% assign category_posts = posts | where: 'category', category %}
  <section class="notes-landing" id="{{ category | slugify }}">
    <h2>{{ category }}</h2>
    <div class="notes-grid">
      {% for post in category_posts %}
      <article class="note-card neub-card">
        <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
        <p>{{ post.description }}</p>
        <ul class="note-tags">{% for tag in post.tags %}<li>{{ tag }}</li>{% endfor %}</ul>
      </article>
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  {% assign tags = posts | map: 'tags' | join: ',' | split: ',' | uniq | sort %}
  <section class="notes-landing" aria-labelledby="tag-index-title">
    <h2 id="tag-index-title">Tags</h2>
    <nav class="note-further" aria-label="Blog tags"><ul class="note-further__list">{% for tag in tags %}<li><a class="link-arrow" href="#{{ tag | slugify }}">{{ tag }}</a></li>{% endfor %}</ul></nav>
    {% for tag in tags %}
    {% assign tag_posts = posts | where_exp: 'post', 'post.tags contains tag' %}
    <section id="{{ tag | slugify }}">
      <h3>{{ tag }}</h3>
      <ul>{% for post in tag_posts %}<li><a href="{{ post.url }}">{{ post.title }}</a></li>{% endfor %}</ul>
    </section>
    {% endfor %}
  </section>
</section>
