---
layout: default
title: "Professional Radar — Dzmitryi Kharlanau"
description: "Monitored professional signals, observations, and review candidates. Durable knowledge belongs in the Atlas after review."
permalink: /radar/
robots: noindex,follow
sitemap: false
---

{% assign items = site.radar | sort: 'date' | reverse %}
<main class="signal-log signal-log--radar">
  <section class="signal-log__hero" aria-labelledby="radar-title">
    <p class="signal-log__eyebrow">Professional radar</p>
    <h1 id="radar-title">Signals under review.</h1>
    <p>Observations and review candidates stay separate from the <a href="/atlas/">Knowledge Atlas</a> until they are ready to become durable guidance.</p>
    <dl class="signal-log__ledger" aria-label="Radar scope">
      <div><dt>Items</dt><dd>{{ items | size }}</dd></div>
      <div><dt>Purpose</dt><dd>Review</dd></div>
      <div><dt>Status</dt><dd>Noindex</dd></div>
    </dl>
  </section>

  <section class="signal-log__register" aria-labelledby="radar-register-title">
    <header class="signal-log__register-head">
      <div><p class="signal-log__eyebrow">Review register</p><h2 id="radar-register-title">Current radar</h2></div>
      <p>Entries are dated observations, not evergreen recommendations.</p>
    </header>
    {% if items == empty %}
    <p class="signal-log__empty">No radar signals published yet. This section is being prepared.</p>
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
            <p class="signal-log__meta">{% if item.source %}<span>Source: {{ item.source }}</span>{% endif %}{% if item.confidence %}<span>Confidence: {{ item.confidence }}</span>{% endif %}{% if item.topics %}<span>{{ item.topics | join: ', ' }}</span>{% elsif item.tags %}<span>{{ item.tags | join: ', ' }}</span>{% endif %}</p>
          </div>
          <a class="signal-log__open" href="{{ item.url }}"><span>Open</span><span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
        </article>
      </li>
      {% endfor %}
    </ol>
    {% endif %}
  </section>
</main>
