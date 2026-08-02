---
layout: default
title: "Professional Signals — Dzmitryi Kharlanau"
description: "Dated professional signals on SAP AMS, integration reliability, master data, and practical AI for support operations."
permalink: /news/
robots: noindex,follow
sitemap: false
---

{% assign items = site.news | sort: 'date' | reverse %}
<main class="signal-log signal-log--news">
  <section class="signal-log__hero" aria-labelledby="signals-title">
    <p class="signal-log__eyebrow">Professional signals</p>
    <h1 id="signals-title">What changed. What needs review.</h1>
    <p>Dated source notes on SAP operations and AI. Durable explanations move to the <a href="/atlas/">Knowledge Atlas</a> only after review.</p>
    <dl class="signal-log__ledger" aria-label="Signal log scope">
      <div><dt>Items</dt><dd>{{ items | size }}</dd></div>
      <div><dt>Purpose</dt><dd>Track</dd></div>
      <div><dt>Status</dt><dd>Noindex</dd></div>
    </dl>
  </section>

  <section class="signal-log__register" aria-labelledby="signals-register-title">
    <header class="signal-log__register-head">
      <div><p class="signal-log__eyebrow">Source register</p><h2 id="signals-register-title">Recent signals</h2></div>
      <p>Each entry keeps its date, source, and confidence visible.</p>
    </header>
    {% if items == empty %}
    <p class="signal-log__empty">No signals published yet. This section is being prepared.</p>
    {% else %}
    <ol class="signal-log__list">
      {% for item in items %}
      {% assign published_on = item.date | default: item.published %}
      <li>
        <article class="signal-log__entry">
          <time datetime="{{ published_on | date_to_xmlschema }}">{{ published_on | date: "%d %b %Y" }}</time>
          <div class="signal-log__entry-copy">
            <h2><a href="{{ item.url }}">{{ item.title }}</a></h2>
            {% if item.subtitle %}<p class="signal-log__subtitle">{{ item.subtitle }}</p>{% endif %}
            <p>{{ item.summary | default: item.excerpt }}</p>
            <p class="signal-log__meta">{% if item.source %}<span>Source: {{ item.source }}</span>{% endif %}{% if item.confidence %}<span>Confidence: {{ item.confidence }}</span>{% endif %}{% if item.topics %}<span>{{ item.topics | join: ', ' }}</span>{% endif %}</p>
          </div>
          <a class="signal-log__open" href="{{ item.url }}"><span>Open</span><span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
        </article>
      </li>
      {% endfor %}
    </ol>
    {% endif %}
  </section>
</main>
