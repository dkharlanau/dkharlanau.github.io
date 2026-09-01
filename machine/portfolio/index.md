---
layout: default
title: "Public Project Map — Enterprise Work and Practical AI"
description: "A reader-first map of 17 public repositories grouped into enterprise design, transformation assurance, and SAP and practical AI tracks."
permalink: /machine/portfolio/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-01
hide_global_cta: true
hide_site_share: true
ai_sidecar: /ai/public-portfolio.json
tags:
  - public-projects
  - enterprise-architecture
  - transformation-assurance
  - practical-ai
---

{% assign portfolio = site.data.public_portfolio %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/machine/">Machine Layer</a></li><li aria-current="page">Public Project Map</li></ol>
</nav>

<div class="research-canvas portfolio-map">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Machine layer / public project map</p>
      <h1>Choose the project by the decision you need to make.</h1>
      <p>{{ portfolio.description }}</p>
      <a class="research-canvas__button" href="#portfolio-tracks">Open the three tracks <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Portfolio tracks">
      <p>{{ portfolio.scope.repository_count }} public repositories / three starting points</p>
      {% for track in portfolio.tracks %}
      <div class="research-canvas__signal-line"><span>{{ track.number }}</span><strong>{{ track.title }}</strong><small>{{ track.question }}</small></div>
      {% endfor %}
      <em>Observed {{ portfolio.observed_at }}. The central website repository is outside this inventory.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Project map boundary">
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Scope:</strong> this is a navigation map, not a compatibility claim. {{ portfolio.boundaries.compatibility }} {{ portfolio.boundaries.adoption }}</p>
    <a href="{{ portfolio.machine_url }}">Read JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="portfolio-map__reference" data-reveal aria-labelledby="portfolio-reference-title">
    <div>
      <p class="research-canvas__eyebrow">Reproducible reference case</p>
      <h2 id="portfolio-reference-title">{{ portfolio.reference_case.title }}</h2>
      <p>{{ portfolio.reference_case.summary }}</p>
      <div class="portfolio-map__reference-actions">
        <a class="research-canvas__button" href="{{ portfolio.reference_case.human_url }}">Run the evidence pack <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
        <a href="{{ portfolio.reference_case.machine_url }}">Inspect the machine manifest <span aria-hidden="true">↗</span></a>
      </div>
    </div>
    <aside aria-label="Reference case boundary">
      <span>{{ portfolio.reference_case.status | replace: '-', ' ' }}</span>
      <p>{{ portfolio.reference_case.boundary }}</p>
      <a href="{{ portfolio.reference_case.source_url }}">Source and fixtures <span aria-hidden="true">↗</span></a>
    </aside>
  </section>

  <section class="portfolio-map__tracks" id="portfolio-tracks" data-reveal>
    <header class="portfolio-map__intro">
      <p class="research-canvas__eyebrow">Reader-first routes</p>
      <h2>Start with one track, then narrow the problem.</h2>
      <p>Primary projects are the suggested entry points for each question. Supporting repositories stay compact because they solve narrower jobs.</p>
    </header>

    {% for track in portfolio.tracks %}
    {% assign primary_projects = portfolio.projects | where: "track_id", track.id | where: "role", "primary" %}
    {% assign supporting_projects = portfolio.projects | where: "track_id", track.id | where: "role", "supporting" %}
    <article class="portfolio-track" id="{{ track.id }}">
      <header class="portfolio-track__header">
        <span>{{ track.number }}</span>
        <div>
          <p class="portfolio-track__question">{{ track.question }}</p>
          <h2>{{ track.title }}</h2>
          <p>{{ track.summary }}</p>
        </div>
      </header>

      <div class="portfolio-track__primary{% if primary_projects.size == 1 %} portfolio-track__primary--single{% endif %}" aria-label="{{ track.title }} primary projects">
        {% for project in primary_projects %}
        <section class="portfolio-project-card">
          <p>Primary project</p>
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <div>
            <a href="{{ project.public_url }}">Open public entry <span aria-hidden="true">↗</span></a>
            <a href="{{ project.repository_url }}">Repository <span aria-hidden="true">↗</span></a>
          </div>
        </section>
        {% endfor %}
      </div>

      {% if supporting_projects.size > 0 %}
      <section class="portfolio-track__supporting" aria-labelledby="{{ track.id }}-supporting">
        <header><p class="research-canvas__eyebrow">{{ track.supporting_label }}</p><h3 id="{{ track.id }}-supporting">Open only the next boundary you need.</h3></header>
        <ul>
          {% for project in supporting_projects %}
          <li>
            <a class="portfolio-supporting-project__main" href="{{ project.public_url }}"><strong>{{ project.title }}</strong><span>{{ project.description }}</span></a>
            <a class="portfolio-supporting-project__repo" href="{{ project.repository_url }}" aria-label="{{ project.title }} repository">GitHub <span aria-hidden="true">↗</span></a>
          </li>
          {% endfor %}
        </ul>
      </section>
      {% endif %}
    </article>
    {% endfor %}
  </section>

  <section class="research-canvas__method portfolio-map__method" aria-labelledby="portfolio-method-title">
    <div><p class="research-canvas__eyebrow">Use the map carefully</p><h2 id="portfolio-method-title">Inspect before you connect.</h2></div>
    <ol>
      <li><span>01</span><strong>Choose the problem</strong><p>Start with one primary project rather than adopting the portfolio as a package.</p></li>
      <li><span>02</span><strong>Read its boundary</strong><p>Use the repository's README, examples, schemas, and validation commands as the local authority.</p></li>
      <li><span>03</span><strong>Verify any handoff</strong><p>Treat a cross-project workflow as supported only when the participating repositories document and test it.</p></li>
    </ol>
  </section>

  <section class="portfolio-map__actions" data-reveal aria-labelledby="portfolio-actions-title">
    <header>
      <p class="research-canvas__eyebrow">One useful next step</p>
      <h2 id="portfolio-actions-title">Move from browsing to evidence.</h2>
      <p>Run one bounded workflow, propose one testable handoff, or bring one concrete problem. Public availability alone is not an adoption result.</p>
    </header>
    <div>
      {% for action in portfolio.actions %}
      <a href="{{ action.href }}"{% if action.href contains 'http' %} target="_blank" rel="noopener noreferrer"{% endif %}>
        <span>0{{ forloop.index }}</span>
        <strong>{{ action.label }}</strong>
        <small>{{ action.description }}</small>
        <em aria-hidden="true">↗</em>
      </a>
      {% endfor %}
    </div>
  </section>
</div>
