---
layout: default
title: "SAP Build Work Zone — Enterprise Context Lab"
description: "Learn SAP Build Work Zone: system class, goals, editions, Fiori and SAP Start boundaries, federation, identity, tasks, Joule, and Lead design."
permalink: /labs/enterprise-context/experience-platforms/sap-build-work-zone/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-experience-review-2026-09"
review_method: "current SAP Build Work Zone standard/advanced + SAP Task Center primary sources + page-level architecture-boundary review"
search_intent: "SAP Build Work Zone standard advanced edition Workspaces Workpages content federation Task Center Fiori launchpad SAP Start"
structured_data:
  type: TechArticle
primary_topic: "sap-build-work-zone"
hide_global_cta: true
enterprise_context_graph: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-ownership
  - lead-decision
tags:
  - sap-build-work-zone
  - sap-btp
  - enterprise-experience
  - digital-workplace
  - fiori
  - integration-architecture
---

{% assign graph = site.data.labs.enterprise_context.graphs.sap_build_work_zone %}
{% assign evidence = site.data.labs.enterprise_context.sources.sap_build_work_zone %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/experience-platforms/">Experience Platforms</a></li><li aria-current="page">SAP Build Work Zone</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Experience Platforms / SAP Build Work Zone</p>
      <h1>One front door.<br />Many systems behind it.</h1>
      <p>{{ graph.summary }}</p>
      <a class="research-canvas__button" href="#system-class">Start with the system class <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Work Zone mental model">
      <p>Remember this</p>
      <div class="research-canvas__signal-line"><span>CLASS</span><strong>Experience</strong><small>Cross-solution user layer</small></div>
      <div class="research-canvas__signal-line"><span>STD</span><strong>Access</strong><small>Access + compose</small></div>
      <div class="research-canvas__signal-line"><span>ADV</span><strong>Workplace</strong><small>Access + collaborate</small></div>
      <em>Workplace ≠ business truth.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">route</span>
    <p><strong>The fastest mental model:</strong> {{ graph.architecture.memory_path }}</p>
    <a href="/labs/enterprise-context/data/sap-build-work-zone-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" id="system-class" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">System class</p>
      <h2>{{ graph.classification.architecture_class }}</h2>
      <p>SAP uses terms such as <strong>{{ graph.classification.official_terms | join: ", " }}</strong>. For architecture reasoning, the useful interpretation is an enterprise experience or system-of-engagement layer because it sits across applications rather than becoming their system of record.</p>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">memory</span>
      <p><strong>{{ graph.classification.memory_rule }}</strong></p>
      <p>{{ graph.classification.one_sentence }}</p>
    </div>
    <div class="ecg-memory-grid">
      {% for item in graph.classification.not_a %}
      <article class="ecg-memory-card"><span>NOT</span><strong>{{ item.title }}</strong><h3>{{ item.explanation }}</h3></article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Why it exists</p>
      <h2>A correct landscape can still create a bad working day.</h2>
      <p>{{ graph.why_it_exists.problem }}</p>
      <p><strong>Work Zone's answer:</strong> {{ graph.why_it_exists.answer }}</p>
    </header>
    <div class="ecg-memory-grid">
      {% for goal in graph.why_it_exists.goals %}
      <article class="ecg-memory-card"><span>GOAL</span><strong>{{ goal.title }}</strong><h3>{{ goal.explanation }}</h3></article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="architecture" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture</p>
      <h2>Central experience. Distributed ownership.</h2>
      <p>{{ graph.architecture.principle }}</p>
    </header>
    <div class="ecg-determination-list">
      {% for layer in graph.architecture.layers %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">{% if layer.order < 10 %}0{% endif %}{{ layer.order }}</div>
        <div class="ecg-determination-card__copy"><h3>{{ layer.layer }}</h3><p>{{ layer.owns }}</p><p><strong>Lead check:</strong> {{ layer.lead_check }}</p></div>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="editions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Standard vs Advanced</p>
      <h2>{{ graph.editions.rule }}</h2>
      <p>The useful difference is not “small versus big”. It is the responsibility the workplace must own.</p>
    </header>
    <div class="ecg-memory-grid">
      {% for option in graph.editions.options %}
      <article class="ecg-memory-card">
        <span>{{ option.edition | upcase }}</span>
        <strong>{{ option.short }}</strong>
        <h3>{{ option.best_fit }}</h3>
        <p><strong>Core:</strong> {{ option.core_model | join: " · " }}</p>
        <p><strong>Choose when:</strong> {{ option.choose_when | join: " · " }}</p>
        <p><strong>Watch:</strong> {{ option.caution }}</p>
      </article>
      {% endfor %}
    </div>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">compare_arrows</span><p><strong>Memory:</strong> Standard = access and composition. Advanced = access, composition, and collaboration.</p></div>
  </section>

  <section class="research-canvas__inventory" id="neighbors" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">The confusing part</p>
      <h2>Products can appear next to each other without owning the same job.</h2>
      <p>A Lead should say what each component owns and what remains outside it.</p>
    </header>
    <div class="ecg-determination-list">
      {% for item in graph.adjacent_products %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">{% if forloop.index < 10 %}0{% endif %}{{ forloop.index }}</div>
        <div class="ecg-determination-card__copy"><p class="research-canvas__eyebrow">{{ item.class }}</p><h3>{{ item.product }}</h3><p><strong>Owns:</strong> {{ item.owns }}</p><p>{{ item.relationship }}</p><p><strong>Memory:</strong> {{ item.memory }}</p></div>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Core vocabulary</p>
      <h2>Learn the nouns by what they control.</h2>
    </header>
    <div class="ecg-memory-grid">
      {% for item in graph.concepts %}
      <article class="ecg-memory-card"><span>TERM</span><strong>{{ item.term }}</strong><h3>{{ item.meaning }}</h3><p><strong>Remember:</strong> {{ item.remember }}</p></article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="integration-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">How work appears in the site</p>
      <h2>Not every integration is an interface.</h2>
      <p>Sometimes the right pattern is federation or navigation. Sometimes data must be integrated. The design should make that difference explicit.</p>
    </header>
    <div class="ecg-determination-list">
      {% for pattern in graph.integration_patterns %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">{% if forloop.index < 10 %}0{% endif %}{{ forloop.index }}</div>
        <div class="ecg-determination-card__copy"><h3>{{ pattern.pattern }}</h3><p>{{ pattern.use }}</p><p><strong>Benefit:</strong> {{ pattern.benefit }}</p><p><strong>Lead check:</strong> {{ pattern.lead_check }}</p></div>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="logistics-examples" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics and Sales examples</p>
      <h2>The value is easier to see through a working day.</h2>
      <p>These are synthetic learning scenarios. They show the architecture boundary, not a claim about a specific customer implementation.</p>
    </header>
    <div class="ecg-memory-grid">
      {% for example in graph.logistics_examples %}
      <article class="ecg-memory-card"><span>ROLE</span><strong>{{ example.persona }}</strong><h3>{{ example.goal }}</h3><p><strong>Workplace:</strong> {{ example.composition | join: " · " }}</p><p><strong>Boundary:</strong> {{ example.boundary }}</p><p><strong>Lead value:</strong> {{ example.lead_value }}</p></article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="lead-design" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead design questions</p>
      <h2>Ask these before implementation starts.</h2>
      <p>The weak requirement is “we need one portal”. The useful requirement explains the user, work, source ownership, entry pattern, identity, and operating model.</p>
    </header>
    <div class="research-route-list">
      {% for question in graph.decision_questions %}
      <a href="#lead-design"><span>?</span><strong>{{ question }}</strong><small>Answer the business and ownership question before choosing the technical configuration.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="diagnostics" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure boundaries</p>
      <h2>Do not debug the visible symptom at the wrong layer.</h2>
      <p>A missing tile, failed launch, bad SSO, broken embedded app, and failed business action can look similar to the user. Their owners are different.</p>
    </header>
    <div class="ecg-determination-list">
      {% for failure in graph.failure_modes %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">{% if forloop.index < 10 %}0{% endif %}{{ forloop.index }}</div>
        <div class="ecg-determination-card__copy"><h3>{{ failure.symptom }}</h3><p><strong>Likely causes:</strong> {{ failure.likely_causes | join: " · " }}</p><p><strong>First check:</strong> {{ failure.first_check }}</p></div>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="quick-test" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">30-second decision test</p>
      <h2>{{ graph.standard_vs_advanced_quick_test.question }}</h2>
      <p>The answer often reveals whether the requirement is Work Zone Standard, Advanced, SAP Start, workflow automation, or integration.</p>
    </header>
    <div class="research-route-list">
      {% for row in graph.standard_vs_advanced_quick_test.answers %}
      <a href="#quick-test"><span>→</span><strong>{{ row.if_missing }}</strong><small>{{ row.choice }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="current-signals" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Current product signals / reviewed 2026-09-03</p>
      <h2>The experience layer is broader than a tile launchpad.</h2>
      <p>These points are release-sensitive and should be checked again for a real project.</p>
    </header>
    <div class="ecg-memory-grid">
      {% for item in graph.fresh_2026_signals %}
      <article class="ecg-memory-card"><span>2026</span><strong>{{ item.signal }}</strong><h3>{{ item.explanation }}</h3></article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="memory" data-reveal>
    <header><p class="research-canvas__eyebrow">Memory anchors</p><h2>If you remember seven lines, remember these.</h2></header>
    <div class="research-route-list">
      {% for item in graph.memory_anchors %}
      <a href="#memory"><span>{% if forloop.index < 10 %}0{% endif %}{{ forloop.index }}</span><strong>{{ item }}</strong><small>Use the sentence as a boundary check, then explain the reason in your own words.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment answer</p>
      <h2>Start with the class. Then prove the boundaries.</h2>
      <p>A strong answer does not begin with a list of UI features. It says what problem the product owns, what remains outside it, and how the edition decision changes the operating model.</p>
    </header>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">timer</span><p><strong>Short answer:</strong> {{ graph.assessment_answer_short }}</p></div>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span><p><strong>Lead answer:</strong> {{ graph.assessment_answer_lead }}</p></div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Source ledger</p>
      <h2>Current SAP documentation behind the product claims.</h2>
      <p>The explanatory model is independently written. Product behavior and current boundaries are checked against SAP sources below.</p>
    </header>
    <div class="research-route-list">
      {% for source in evidence.sources %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SAP</span><strong>{{ source.title }}</strong><small>{{ source.source_type }}{% if source.release_scope %} · {{ source.release_scope }}{% endif %} · checked {{ source.accessed_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Next:</strong> return to the class view when you want to compare the experience layer with other SAP entry and workplace patterns.</p>
    <a href="/labs/enterprise-context/experience-platforms/">Back to Experience Platforms <span class="material-symbols-outlined" aria-hidden="true">arrow_back</span></a>
  </section>
</div>