---
layout: default
title: "About Dzmitryi Kharlanau — Verified Public Profile"
description: "Canonical public profile for Dzmitryi Kharlanau, focused on verified work history, publications, credentials, and machine-readable profile sources."
permalink: /about/
last_modified_at: 2026-04-19
profile_page: true
hide_global_cta: true
---

{% assign resume = site.data.resume %}
{% assign social_links = site.data.social.links %}

<section class="section" id="person">
  <header class="section-heading">
    <p class="eyebrow">Profile</p>
    <h1>Dzmitryi Kharlanau</h1>
    <p class="lead">Canonical public profile page for verified work history, public writing, and machine-readable profile data.</p>
  </header>

  <div class="section-shell section-shell--flat profile-hero">
    <div class="profile-hero__meta">
      <p><strong>Current context:</strong> {{ resume.headline }} at <a href="https://www.epam.com" target="_blank" rel="noopener noreferrer">EPAM Systems</a>.</p>
      <p><strong>Core domains:</strong> {{ resume.core_domains | join: ", " }}.</p>
      <p><strong>Last reviewed:</strong> {{ page.last_modified_at | date: "%B %-d, %Y" }}</p>
    </div>
    <div class="section-actions">
      <a class="button button--primary" href="{{ resume.contact.linkedin }}" target="_blank" rel="noopener noreferrer">Contact on LinkedIn</a>
      <a class="button button--secondary" href="/ai/resume.yml">Resume YAML</a>
      <a class="button button--secondary" href="/ai/profile-audit.json">Profile audit JSON</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-shell">
    <header class="section-heading">
      <p class="eyebrow">Summary</p>
      <h2>Evidence-backed professional snapshot</h2>
    </header>
    <div class="prose">
      <p>{{ resume.summary }}</p>
      <p>This page intentionally keeps claims narrower than the broader site messaging. The source-of-truth audit for confidence levels, verification issues, and credential status is available at <a href="/ai/profile-audit.json">/ai/profile-audit.json</a>.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-shell">
    <header class="section-heading">
      <p class="eyebrow">Focus Areas</p>
      <h2>Consistent themes across roles and writing</h2>
    </header>
    <ul class="profile-chip-list">
      {% for skill in resume.skills %}
      <li>{{ skill }}</li>
      {% endfor %}
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-shell">
    <header class="section-heading">
      <p class="eyebrow">Work History</p>
      <h2>Roles represented in the current public dataset</h2>
    </header>
    <div class="profile-list">
      {% for item in resume.experience limit: 6 %}
      <article class="profile-list__item">
        <h3>{{ item.title }}</h3>
        <p>{{ item.company }} · {{ item.start }}{% if item.current %} to present{% elsif item.end %} to {{ item.end }}{% endif %}</p>
        <p>{{ item.summary }}</p>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="section-shell">
    <header class="section-heading">
      <p class="eyebrow">Machine-readable Sources</p>
      <h2>Profile files for retrieval and verification</h2>
    </header>
    <div class="profile-grid">
      <article class="profile-card">
        <h3>Canonical resume data</h3>
        <p>Public subset of verified profile data for AI systems and search engines.</p>
        <p><a href="/ai/resume.yml">Resume YAML</a> · <a href="/ai/resume.json">Resume JSON</a></p>
      </article>
      <article class="profile-card">
        <h3>Audit registry</h3>
        <p>Confidence levels, credential registry, publication themes, and verification issues.</p>
        <p><a href="/ai/profile-audit.json">Profile audit JSON</a></p>
      </article>
      <article class="profile-card">
        <h3>LLM access manifest</h3>
        <p>Retrieval guidance for AI systems and links to canonical profile surfaces.</p>
        <p><a href="/llms.txt">llms.txt</a></p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-shell">
    <header class="section-heading">
      <p class="eyebrow">Selected Credentials</p>
      <h2>Publicly linkable credentials</h2>
    </header>
    <div class="profile-list">
      {% for cert in resume.certifications limit: 8 %}
      <article class="profile-list__item">
        <h3>{{ cert.name }}</h3>
        <p>{{ cert.issuer }}{% if cert.issued %} · {{ cert.issued }}{% endif %}</p>
        {% if cert.url %}
        <p><a href="{{ cert.url }}" target="_blank" rel="noopener noreferrer">Open credential</a></p>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="section-shell">
    <header class="section-heading">
      <p class="eyebrow">Public Writing</p>
      <h2>Writing signals used in the profile audit</h2>
    </header>
    <div class="profile-list">
      {% for publication in resume.publications %}
      <article class="profile-list__item">
        <h3>{{ publication.name }}</h3>
        <p>{{ publication.publisher }}{% if publication.published %} · {{ publication.published | date: "%B %-d, %Y" }}{% endif %}</p>
        <p><a href="{{ publication.url }}" target="_blank" rel="noopener noreferrer">Open source</a></p>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="section-shell">
    <header class="section-heading">
      <p class="eyebrow">Profiles</p>
      <h2>External identity links</h2>
    </header>
    <div class="profile-chip-links">
      {% for link in social_links %}
      <a href="{{ link.url }}" target="_blank" rel="noopener noreferrer">{{ link.label }}</a>
      {% endfor %}
    </div>
  </div>
</section>
