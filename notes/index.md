---
layout: default
title: "Notes — Dzmitryi Kharlanau | SAP O2C & Integration"
description: "Working notes on SAP order-to-cash consulting, clean-core S/4HANA strategy, event-driven integration, and AI-enabled operations."
permalink: /notes/
hide_global_cta: true
---

{% assign notes = site.notes | sort: 'date' | reverse %}

<div class="notes-canvas">
  <header class="notes-canvas__hero" data-reveal>
    <div>
      <p class="notes-canvas__eyebrow">Notes / working context</p>
      <h1>SAP field notes for work in progress.</h1>
      <p>Short, practical perspectives on transformation, AMS, integration, clean core, and AI-supported operations. These notes frame a problem; the Atlas carries the deeper diagnostic material.</p>
    </div>
    <div class="notes-canvas__guide">
      <p>Use a note when</p>
      <ul>
        <li>the operating question is still taking shape;</li>
        <li>a decision needs a compact point of view;</li>
        <li>a deeper Atlas route is not yet the right starting point.</li>
      </ul>
      <a href="/atlas/">Open the Knowledge Atlas <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
  </header>

  <nav class="notes-canvas__topics" data-reveal aria-label="Note topics">
    <a href="/notes/ams/"><span>01</span><strong>AMS</strong><small>Support improvement and operational memory</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/notes/process-audit/"><span>02</span><strong>Process audit</strong><small>Breakpoints, controls, and business evidence</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/notes/composable-erp/"><span>03</span><strong>Composable ERP</strong><small>Clean core and replaceable edge services</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/notes/ai-ml/"><span>04</span><strong>AI around SAP</strong><small>Reviewable AI work around ERP boundaries</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
  </nav>

  <section class="notes-canvas__archive" data-reveal>
    <header><p class="notes-canvas__eyebrow">Note archive</p><h2>Choose the perspective that fits the delivery question.</h2></header>
    <ol class="notes-route-list">
      {% for note in notes %}
      {% assign published_on = note.date | default: note.published %}
      {% assign note_tag = note.tags | first | default: 'Field note' %}
      <li><a href="{{ note.url }}"><time datetime="{{ published_on | date_to_xmlschema }}">{% if published_on %}{{ published_on | date: '%Y.%m.%d' }}{% endif %}</time><strong>{{ note.title }}</strong><small>{{ note.summary | default: note.subtitle | default: note.excerpt | strip_html | truncate: 150 }}</small><em>{{ note_tag }}</em><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a></li>
      {% endfor %}
    </ol>
  </section>
</div>
