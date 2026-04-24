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

<section class="section certifications-page certifications-page__hero">
  <div class="certifications-hero">
    <div class="certifications-hero__copy">
      <p class="eyebrow">Certifications</p>
      <h1>Public learning record across SAP, AI, and delivery systems.</h1>
      <p class="lead">A cleaned, public version of the certification export. The emphasis is on linkable credentials and the visible pattern behind the learning record, not inflated badge counting.</p>
      <div class="certifications-hero__actions">
        <a class="button button--primary" href="#certification-register">View register</a>
        <a class="button button--secondary" href="/ai/certifications/">Open Markdown dataset</a>
      </div>
    </div>
    <dl class="certifications-hero__stats" aria-label="Certification summary">
      <div class="certifications-stat">
        <dt>Total records</dt>
        <dd>{{ certifications | size }}</dd>
      </div>
      <div class="certifications-stat">
        <dt>Public links</dt>
        <dd>{{ public_count }}</dd>
      </div>
      <div class="certifications-stat">
        <dt>AI records</dt>
        <dd>{{ ai_count }}</dd>
      </div>
      <div class="certifications-stat">
        <dt>SAP records</dt>
        <dd>{{ sap_count }}</dd>
      </div>
    </dl>
  </div>
</section>

<section class="section certifications-page" id="credential-signals">
  <header class="section-heading">
    <p class="eyebrow">Reading the signal</p>
    <h2>What the certification record supports</h2>
    <p class="lead">The record is strongest when it is read as a direction of travel: SAP delivery depth, newer AI tooling, and practical operating skills around data, analysis, and team execution.</p>
  </header>

  <div class="certifications-signal-grid">
    <article class="certifications-signal-card">
      <p class="certifications-signal-card__meta">Established base</p>
      <h3>SAP and enterprise systems</h3>
      <p>Older SAP certification plus recent SAP Learning and Credly records support SAP process, clean core, retail, MDG, HCM, service, and event-driven integration themes.</p>
    </article>
    <article class="certifications-signal-card">
      <p class="certifications-signal-card__meta">Recent concentration</p>
      <h3>AI and agentic systems</h3>
      <p>The 2025-2026 cluster is concentrated around Claude, MCP, subagents, agent skills, AI fluency, Copilot, reasoning models, and practical agent design.</p>
    </article>
    <article class="certifications-signal-card">
      <p class="certifications-signal-card__meta">Supporting layer</p>
      <h3>Delivery, data, and language</h3>
      <p>Language, analytics, conflict resolution, management, Git, Excel, and TRIZ entries round out the profile without being framed as the main specialization.</p>
    </article>
  </div>
</section>

<section class="section certifications-page" id="certification-categories">
  <header class="section-heading">
    <p class="eyebrow">Dataset structure</p>
    <h2>Credential groups</h2>
    <p class="lead">Categories are editorial groupings for the public page. The source dataset keeps each record separately so crawlers and readers can verify the underlying entries.</p>
  </header>

  <div class="certifications-category-grid">
    {% for group in grouped %}
    <article class="certifications-category-card">
      <p class="certifications-category-card__count">{{ group.items | size }}</p>
      <h3>{{ group.name }}</h3>
      <p>{{ group.items | map: "authority" | uniq | join: ", " }}</p>
    </article>
    {% endfor %}
  </div>
</section>

<section class="section certifications-page" id="certification-register">
  <header class="section-heading">
    <p class="eyebrow">Register</p>
    <h2>Certification records</h2>
    <p class="lead">{{ site.data.certifications.privacy_note }}</p>
  </header>

  <div class="certifications-register">
    {% for item in certifications %}
    <article class="certifications-record">
      <div class="certifications-record__date">
        <span>{{ item.issued | default: "No date" }}</span>
      </div>
      <div class="certifications-record__body">
        <p class="certifications-record__meta">{{ item.authority }}{% if item.expires %} · expires {{ item.expires }}{% endif %}</p>
        <h3>{{ item.name }}</h3>
        <p class="certifications-record__category">{{ item.category }}</p>
      </div>
      {% if item.url %}
      <a class="certifications-record__link" href="{{ item.url }}" target="_blank" rel="noopener noreferrer">Verify</a>
      {% endif %}
    </article>
    {% endfor %}
  </div>
</section>
