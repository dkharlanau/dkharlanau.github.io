---
layout: default
title: "Blog — Dzmitryi Kharlanau on resilient systems"
description: "Long-form essays on operating models, integration architecture, and data systems that stay reliable under pressure."
permalink: /blog/
---

<section class="section notes-landing">
  <header class="section-heading">
    <p class="eyebrow">Blog</p>
    <h1>{{ page.title }}</h1>
    <p class="lead">Deep-dive essays on systems thinking, SAP delivery, and automation patterns that keep enterprise platforms trustworthy.</p>
  </header>

  <div class="notes-grid">
    {% assign posts = site.blog | sort: 'date' | reverse %}
    {% if posts == empty %}
    <p class="lead">First article coming soon. Check back shortly.</p>
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
      <p>{{ post.summary | default: post.excerpt }}</p>
      <a class="link-arrow" href="{{ post.url }}">Read article</a>
    </article>
    {% endfor %}
    {% endif %}
  </div>
</section>
