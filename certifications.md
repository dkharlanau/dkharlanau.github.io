---
layout: default
title: "Certifications | Dzmitryi Kharlanau"
description: "Public certifications and learning record for Dzmitryi Kharlanau across SAP, AI, data, language, and delivery topics."
permalink: /certifications/
sitemap: true
last_modified_at: 2026-04-24
---

{% assign certifications = site.data.certifications.items %}
{% assign ai_count = certifications | where: "category", "AI and agentic systems" | size %}
{% assign sap_count = certifications | where: "category", "SAP and enterprise systems" | size %}
{% assign public_count = certifications | where_exp: "item", "item.url" | size %}
{% assign grouped = certifications | group_by: "category" %}

<main class="evidence-canvas certifications-page" data-evidence-canvas>
  <section class="evidence-canvas__hero section" aria-labelledby="certification-title">
    <div>
      <p class="evidence-canvas__eyebrow">Public record / credentials</p>
      <h1 id="certification-title">Credentials with a visible source.</h1>
      <p>A public learning record across SAP, AI, data, and delivery. Links are kept where a verification source is available.</p>
      <div class="evidence-canvas__actions">
        <a href="#certification-register">Browse the register <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
        <a href="/ai/certifications/">Open the Markdown dataset <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
      </div>
    </div>
    <dl class="evidence-ledger" aria-label="Certification summary">
      <div><dt>Records</dt><dd>{{ certifications | size }}</dd></div>
      <div><dt>Public links</dt><dd>{{ public_count }}</dd></div>
      <div><dt>AI records</dt><dd>{{ ai_count }}</dd></div>
      <div><dt>SAP records</dt><dd>{{ sap_count }}</dd></div>
    </dl>
  </section>

  <section class="evidence-canvas__section section" aria-labelledby="certification-scope-title">
    <header class="evidence-canvas__heading">
      <p class="evidence-canvas__eyebrow">How to read the record</p>
      <h2 id="certification-scope-title">SAP remains the operating base.</h2>
    </header>
    <div class="evidence-signals">
      <article><span>01</span><div><h3>Enterprise systems</h3><p>SAP process, master data, clean core, and integration learning.</p></div></article>
      <article><span>02</span><div><h3>AI around operational work</h3><p>AI fluency, MCP, agents, and reviewable automation practices.</p></div></article>
      <article><span>03</span><div><h3>Delivery support</h3><p>Data, analysis, collaboration, and practical working tools.</p></div></article>
    </div>
  </section>

  <section class="evidence-canvas__section section" id="certification-register" aria-labelledby="certification-register-title">
    <header class="evidence-canvas__heading evidence-canvas__heading--split">
      <div><p class="evidence-canvas__eyebrow">Source register</p><h2 id="certification-register-title">Certification records</h2></div>
      <p>{{ site.data.certifications.privacy_note }}</p>
    </header>
    <div class="evidence-filter" role="toolbar" aria-label="Filter certification records">
      <button type="button" data-evidence-filter="all" aria-pressed="true">All <span>{{ certifications | size }}</span></button>
      {% for group in grouped %}<button type="button" data-evidence-filter="{{ group.name | escape }}" aria-pressed="false">{{ group.name }} <span>{{ group.items | size }}</span></button>{% endfor %}
    </div>
    <p class="evidence-filter__status" aria-live="polite" data-evidence-status>{{ certifications | size }} records shown</p>
    <ol class="evidence-register">
      {% for item in certifications %}
      <li data-evidence-record data-evidence-category="{{ item.category | escape }}">
        <time datetime="{{ item.issued | default: '' }}">{{ item.issued | default: "No date" }}</time>
        <div><p>{{ item.authority }}{% if item.expires %} · expires {{ item.expires }}{% endif %}</p><h3>{{ item.name }}</h3></div>
        <span>{{ item.category }}</span>
        {% if item.url %}<a href="{{ item.url }}" target="_blank" rel="noopener noreferrer">Verify <span class="material-symbols-outlined" aria-hidden="true">north_east</span></a>{% else %}<span class="evidence-register__unlinked">No public link</span>{% endif %}
      </li>
      {% endfor %}
    </ol>
  </section>
</main>
