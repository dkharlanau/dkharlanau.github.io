---
title: "AMS Next Gen"
description: "A practical SAP operations decision system: recover business flow, remove repeat work, govern change, automate known work, and turn operations evidence into better decisions."
subtitle: "From ticket queue to operations decision system."
permalink: /notes/ams/
tags:
  - AMS
  - SAP
  - Operations
  - AI
  - Decision Systems
excerpt: "Signals become decisions, verified actions, reusable knowledge, and less future work."
date: 2025-10-03
last_modified_at: 2026-08-16
further_reading:
  - label: "Practice evidence-first diagnosis in Incident Lab"
    url: "/datasets/incident-lab/"
  - label: "Use Atlas for SAP diagnostics"
    url: "/atlas/diagnostics/"
  - label: "Turn repeated data work into reusable procedures"
    url: "/reusable-data-procedures/"
---

<style>
.ams-next { --ams-gap: clamp(1rem, 2vw, 1.6rem); }
.ams-next * { box-sizing: border-box; }
.ams-next__hero { padding: clamp(1.25rem, 4vw, 2.5rem); border: 1px solid var(--color-border); border-radius: 24px; background: linear-gradient(145deg, var(--color-surface, #fff), var(--color-accent-soft)); margin: 0 0 2rem; }
.ams-next__eyebrow { margin: 0 0 .55rem; font-size: .78rem; font-weight: 800; letter-spacing: .09em; text-transform: uppercase; color: var(--color-accent); }
.ams-next__hero h2 { margin: 0; max-width: 17ch; font-size: clamp(2rem, 6vw, 4rem); line-height: .98; letter-spacing: -.035em; }
.ams-next__lede { max-width: 760px; margin: 1rem 0 0; font-size: clamp(1rem, 1.8vw, 1.18rem); line-height: 1.65; }
.ams-next__truth { margin-top: 1.2rem; padding: 1rem 1.1rem; border-left: 4px solid var(--color-accent); background: var(--color-surface, rgba(255,255,255,.6)); border-radius: 0 14px 14px 0; }
.ams-next__links { display: flex; flex-wrap: wrap; gap: .65rem; margin-top: 1.2rem; }
.ams-next__link { display: inline-flex; align-items: center; min-height: 42px; padding: .65rem .9rem; border: 1px solid var(--color-border); border-radius: 999px; text-decoration: none; font-weight: 700; background: var(--color-surface, #fff); }
.ams-next__section { margin: clamp(2.2rem, 6vw, 4.5rem) 0; }
.ams-next__section-head { max-width: 760px; margin-bottom: 1.2rem; }
.ams-next__section-head h2 { margin-bottom: .45rem; }
.ams-next__section-head p { margin: 0; color: var(--color-text-muted); }
.ams-loop { display: grid; grid-template-columns: repeat(8, minmax(92px, 1fr)); gap: .55rem; overflow-x: auto; padding-bottom: .4rem; }
.ams-loop__step { position: relative; min-width: 92px; padding: 1rem .75rem; border: 1px solid var(--color-border); border-radius: 16px; background: var(--color-surface, #fff); text-align: center; font-weight: 800; text-transform: capitalize; }
.ams-loop__step:not(:last-child)::after { content: "→"; position: absolute; right: -.5rem; top: 50%; transform: translateY(-50%); color: var(--color-text-muted); z-index: 2; }
.ams-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--ams-gap); }
.ams-card { padding: 1.15rem; border: 1px solid var(--color-border); border-radius: 18px; background: var(--color-surface, #fff); }
.ams-card h3 { margin: .15rem 0 .55rem; font-size: 1.05rem; }
.ams-card p { margin: 0; color: var(--color-text-muted); line-height: 1.55; }
.ams-card__meta { display: flex; justify-content: space-between; gap: .6rem; align-items: center; margin-bottom: .75rem; }
.ams-card__count { font-size: .78rem; font-weight: 800; color: var(--color-text-muted); }
.ams-entry { cursor: pointer; text-align: left; width: 100%; color: inherit; font: inherit; }
.ams-entry:hover, .ams-entry:focus-visible { border-color: var(--color-accent); transform: translateY(-1px); }
.ams-entry__verb { font-size: .75rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: var(--color-accent); }
.ams-cluster { min-height: 190px; }
.ams-cluster__question { margin-top: .8rem !important; font-size: .9rem; }
.ams-maturity { display: grid; grid-template-columns: repeat(5, minmax(150px, 1fr)); gap: .75rem; overflow-x: auto; padding-bottom: .4rem; }
.ams-maturity__item { min-width: 150px; padding: 1rem; border: 1px solid var(--color-border); border-radius: 16px; background: var(--color-surface, #fff); }
.ams-maturity__level { font-size: .75rem; font-weight: 900; color: var(--color-accent); }
.ams-maturity__item h3 { margin: .3rem 0 .5rem; font-size: 1rem; }
.ams-maturity__item p { margin: 0; font-size: .9rem; color: var(--color-text-muted); }
.ams-stack { display: grid; grid-template-columns: repeat(5, minmax(150px, 1fr)); gap: .75rem; overflow-x: auto; }
.ams-stack__item { min-width: 150px; padding: 1rem; border: 1px solid var(--color-border); border-radius: 16px; text-decoration: none; color: inherit; background: var(--color-surface, #fff); }
.ams-stack__item strong { display: block; margin-bottom: .35rem; }
.ams-stack__item span { display: block; color: var(--color-text-muted); font-size: .88rem; line-height: 1.45; }
.ams-explorer { border: 1px solid var(--color-border); border-radius: 22px; padding: clamp(1rem, 3vw, 1.5rem); background: var(--color-surface, #fff); }
.ams-explorer__toolbar { display: grid; grid-template-columns: minmax(220px, 1fr) 220px; gap: .75rem; align-items: end; }
.ams-explorer__label { display: block; margin-bottom: .35rem; font-size: .75rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; }
.ams-explorer input, .ams-explorer select { width: 100%; min-height: 44px; border: 1px solid var(--color-border); border-radius: 12px; padding: .65rem .75rem; background: var(--color-surface, #fff); color: inherit; font: inherit; }
.ams-filter-row { display: flex; flex-wrap: wrap; gap: .5rem; margin: 1rem 0; }
.ams-filter { border: 1px solid var(--color-border); border-radius: 999px; padding: .55rem .8rem; background: transparent; color: inherit; font: inherit; font-weight: 700; cursor: pointer; }
.ams-filter.is-active { background: var(--color-accent); color: #fff; border-color: var(--color-accent); }
.ams-byte-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .85rem; }
.ams-byte { padding: 1rem; border: 1px solid var(--color-border); border-radius: 16px; background: var(--color-surface, #fff); }
.ams-byte__top { display: flex; justify-content: space-between; gap: .6rem; margin-bottom: .55rem; }
.ams-byte__id { font-size: .72rem; font-weight: 900; letter-spacing: .06em; text-transform: uppercase; color: var(--color-text-muted); }
.ams-byte__level { font-size: .72rem; font-weight: 900; color: var(--color-accent); }
.ams-byte h3 { margin: 0 0 .55rem; font-size: 1rem; line-height: 1.35; }
.ams-byte h3 a { text-decoration: none; }
.ams-byte p { margin: 0; color: var(--color-text-muted); font-size: .9rem; line-height: 1.5; }
.ams-byte__meta { margin-top: .75rem; font-size: .74rem; font-weight: 800; color: var(--color-text-muted); }
.ams-empty { display: none; padding: 1rem; border: 1px dashed var(--color-border); border-radius: 14px; color: var(--color-text-muted); }
.ams-lead { display: grid; grid-template-columns: 1.1fr .9fr; gap: var(--ams-gap); }
.ams-lead__panel { padding: 1.2rem; border: 1px solid var(--color-border); border-radius: 18px; background: var(--color-surface, #fff); }
.ams-lead__panel h3 { margin-top: 0; }
.ams-lead__panel ul { margin-bottom: 0; }
@media (max-width: 900px) { .ams-grid, .ams-byte-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .ams-lead { grid-template-columns: 1fr; } }
@media (max-width: 640px) { .ams-grid, .ams-byte-grid, .ams-explorer__toolbar { grid-template-columns: 1fr; } .ams-next__hero { border-radius: 18px; } }
</style>

<div class="ams-next">
  <section class="ams-next__hero">
    <p class="ams-next__eyebrow">SAP Operations Decision System</p>
    <h2>Support should reduce future support.</h2>
    <p class="ams-next__lede">AMS Next Gen is my operating model for SAP support and continuous improvement. The goal is not to close more tickets. The goal is to restore business flow, remove repeat demand, make changes safer, turn known work into reusable procedures, and use operations evidence for better architecture and business decisions.</p>
    <div class="ams-next__truth"><strong>The unit of value is not a closed ticket.</strong> It is a verified decision that leaves the system easier to operate next time.</div>
    <div class="ams-next__links">
      <a class="ams-next__link" href="#situations">Start from a situation</a>
      <a class="ams-next__link" href="#maturity">Check maturity</a>
      <a class="ams-next__link" href="#knowledge">Explore the knowledge system</a>
    </div>
  </section>

  <section class="ams-next__section" aria-labelledby="ams-loop-title">
    <div class="ams-next__section-head">
      <h2 id="ams-loop-title">The operating loop</h2>
      <p>Every serious AMS activity should move through the same logic. Skipping a step usually creates the next ticket.</p>
    </div>
    <div class="ams-loop" aria-label="AMS operating loop">
      {% for step in site.data.ams_taxonomy.loop %}
      <div class="ams-loop__step">{{ step }}</div>
      {% endfor %}
    </div>
  </section>

  <section class="ams-next__section" id="situations" aria-labelledby="ams-situations-title">
    <div class="ams-next__section-head">
      <h2 id="ams-situations-title">Start with the work, not the library</h2>
      <p>A user rarely wakes up wanting to browse AMS theory. They have an incident, a risky change, a repeated workaround, an architecture question, or a cost problem.</p>
    </div>
    <div class="ams-grid">
      {% for mode in site.data.ams_taxonomy.entry_modes %}
      <button class="ams-card ams-entry" type="button" data-cluster-target="{{ mode.cluster }}">
        <span class="ams-entry__verb">{{ mode.id }}</span>
        <h3>{{ mode.label }}</h3>
        <p>{{ mode.prompt }}</p>
      </button>
      {% endfor %}
    </div>
  </section>

  <section class="ams-next__section" aria-labelledby="ams-capabilities-title">
    <div class="ams-next__section-head">
      <h2 id="ams-capabilities-title">Six capability clusters</h2>
      <p>SAP modules are a domain filter, not the operating model. These clusters describe what AMS must be able to do across O2C, P2P, master data, integrations, warehouse, finance, and platform work.</p>
    </div>
    <div class="ams-grid">
      {% for cluster_pair in site.data.ams_taxonomy.clusters %}
        {% assign cluster_key = cluster_pair[0] %}
        {% assign cluster = cluster_pair[1] %}
        <article class="ams-card ams-cluster">
          <div class="ams-card__meta">
            <span class="ams-entry__verb">{{ cluster_key | replace: '-', ' ' }}</span>
            <span class="ams-card__count">{{ cluster.bytes | size }} bytes</span>
          </div>
          <h3>{{ cluster.label }}</h3>
          <p>{{ cluster.short }}</p>
          <p class="ams-cluster__question"><strong>Lead question:</strong> {{ cluster.question }}</p>
        </article>
      {% endfor %}
    </div>
  </section>

  <section class="ams-next__section" id="maturity" aria-labelledby="ams-maturity-title">
    <div class="ams-next__section-head">
      <h2 id="ams-maturity-title">Maturity is a change in behaviour</h2>
      <p>A team is not mature because production is currently quiet. Maturity means the operating system needs less hero work and creates better decisions from the evidence it already has.</p>
    </div>
    <div class="ams-maturity">
      {% for level_pair in site.data.ams_taxonomy.maturity %}
        {% assign level_key = level_pair[0] %}
        {% assign level = level_pair[1] %}
        <article class="ams-maturity__item">
          <span class="ams-maturity__level">L{{ level_key }}</span>
          <h3>{{ level.label }}</h3>
          <p>{{ level.description }}</p>
        </article>
      {% endfor %}
    </div>
  </section>

  <section class="ams-next__section" aria-labelledby="ams-stack-title">
    <div class="ams-next__section-head">
      <h2 id="ams-stack-title">One knowledge stack, different jobs</h2>
      <p>AMS becomes useful when diagnosis, process context, skills, datasets, and executable procedures reinforce each other instead of living as separate site sections.</p>
    </div>
    <div class="ams-stack">
      {% for item in site.data.ams_taxonomy.knowledge_stack %}
      <a class="ams-stack__item" href="{{ item.url }}">
        <strong>{{ item.label }}</strong>
        <span>{{ item.role }}</span>
      </a>
      {% endfor %}
    </div>
  </section>

  <section class="ams-next__section" id="knowledge" aria-labelledby="ams-knowledge-title">
    <div class="ams-next__section-head">
      <h2 id="ams-knowledge-title">Knowledge explorer</h2>
      <p>The original AMS bytes remain stable source material. This layer reorganises them by capability and maturity so the library behaves more like a system.</p>
    </div>

    <div class="ams-explorer">
      <div class="ams-explorer__toolbar">
        <div>
          <label class="ams-explorer__label" for="amsByteSearch">Search</label>
          <input id="amsByteSearch" type="search" placeholder="incident, vendor, RAG, cost, change..." autocomplete="off" />
        </div>
        <div>
          <label class="ams-explorer__label" for="amsMaturityFilter">Maturity</label>
          <select id="amsMaturityFilter">
            <option value="all">All maturity levels</option>
            {% for level_pair in site.data.ams_taxonomy.maturity %}
              {% assign level_key = level_pair[0] %}
              {% assign level = level_pair[1] %}
              <option value="{{ level_key }}">L{{ level_key }} · {{ level.label }}</option>
            {% endfor %}
          </select>
        </div>
      </div>

      <div class="ams-filter-row" aria-label="Capability filters">
        <button class="ams-filter is-active" type="button" data-cluster-filter="all">All</button>
        {% for cluster_pair in site.data.ams_taxonomy.clusters %}
          {% assign cluster_key = cluster_pair[0] %}
          {% assign cluster = cluster_pair[1] %}
          <button class="ams-filter" type="button" data-cluster-filter="{{ cluster_key }}">{{ cluster.label }}</button>
        {% endfor %}
      </div>

      <p class="ams-card__count" id="amsByteCount"></p>

      <div class="ams-byte-grid" id="amsByteList">
        {% for byte in site.data.ams_bytes %}
          {% assign byte_cluster = "unclassified" %}
          {% assign byte_cluster_label = "Explore" %}
          {% for cluster_pair in site.data.ams_taxonomy.clusters %}
            {% assign cluster_key = cluster_pair[0] %}
            {% assign cluster = cluster_pair[1] %}
            {% if cluster.bytes contains byte.id %}
              {% assign byte_cluster = cluster_key %}
              {% assign byte_cluster_label = cluster.label %}
            {% endif %}
          {% endfor %}
          {% assign byte_maturity = "3" %}
          {% for level_pair in site.data.ams_taxonomy.maturity %}
            {% assign level_key = level_pair[0] %}
            {% assign level = level_pair[1] %}
            {% if level.bytes contains byte.id %}
              {% assign byte_maturity = level_key %}
            {% endif %}
          {% endfor %}
          <article class="ams-byte" data-id="{{ byte.id }}" data-title="{{ byte.title | downcase | escape }}" data-summary="{{ byte.summary | downcase | escape }}" data-cluster="{{ byte_cluster }}" data-maturity="{{ byte_maturity }}">
            <div class="ams-byte__top">
              <span class="ams-byte__id">{{ byte.id }}</span>
              <span class="ams-byte__level">L{{ byte_maturity }}</span>
            </div>
            <h3><a href="/datasets/view/ams/{{ byte.id }}/">{{ byte.title }}</a></h3>
            <p>{{ byte.summary }}</p>
            <div class="ams-byte__meta">{{ byte_cluster_label }}</div>
          </article>
        {% endfor %}
      </div>
      <div class="ams-empty" id="amsEmpty">No byte matches this combination. That is usually a useful signal too: either the filter is too narrow or the model has a gap.</div>
    </div>
  </section>

  <section class="ams-next__section ams-lead" aria-label="Lead perspective">
    <div class="ams-lead__panel">
      <h3>What I expect from a Lead</h3>
      <ul>
        <li>Separate symptom, evidence, hypothesis, decision, and action.</li>
        <li>See the business process behind the SAP object and the integration behind the symptom.</li>
        <li>Protect recovery speed without turning production into an uncontrolled laboratory.</li>
        <li>Convert repeated work into a Problem, a procedure, a control, or an architecture improvement.</li>
        <li>Make vendor, business, data, and technical ownership explicit before escalation starts.</li>
        <li>Explain cost, risk, and trade-offs in language a business owner can use.</li>
      </ul>
    </div>
    <div class="ams-lead__panel">
      <h3>AI belongs inside the loop</h3>
      <p>AI is not a separate AMS tower. It can extract evidence, suggest hypotheses, challenge a decision, generate diagnostic checks, compare incidents, draft communication, and turn a proven fix into a reusable procedure. The human boundary stays around risky production actions, business decisions, and changes that alter data, configuration, code, access, or message sequencing.</p>
    </div>
  </section>
</div>

<script>
(function(){
  var input = document.getElementById('amsByteSearch');
  var maturity = document.getElementById('amsMaturityFilter');
  var list = document.getElementById('amsByteList');
  var count = document.getElementById('amsByteCount');
  var empty = document.getElementById('amsEmpty');
  var filters = Array.prototype.slice.call(document.querySelectorAll('[data-cluster-filter]'));
  var entries = Array.prototype.slice.call(document.querySelectorAll('[data-cluster-target]'));
  if(!input || !maturity || !list || !count) return;

  var items = Array.prototype.slice.call(list.querySelectorAll('.ams-byte'));
  var activeCluster = 'all';

  function setCluster(value){
    activeCluster = value || 'all';
    filters.forEach(function(btn){
      btn.classList.toggle('is-active', btn.getAttribute('data-cluster-filter') === activeCluster);
    });
    render();
  }

  function render(){
    var q = (input.value || '').trim().toLowerCase();
    var level = maturity.value;
    var shown = 0;

    items.forEach(function(el){
      var hay = [el.getAttribute('data-id'), el.getAttribute('data-title'), el.getAttribute('data-summary')].join(' ').toLowerCase();
      var clusterOk = activeCluster === 'all' || el.getAttribute('data-cluster') === activeCluster;
      var maturityOk = level === 'all' || el.getAttribute('data-maturity') === level;
      var searchOk = !q || hay.indexOf(q) !== -1;
      var ok = clusterOk && maturityOk && searchOk;
      el.style.display = ok ? '' : 'none';
      if(ok) shown++;
    });

    count.textContent = shown + ' / ' + items.length + ' knowledge bytes visible';
    if(empty) empty.style.display = shown ? 'none' : 'block';
  }

  filters.forEach(function(btn){
    btn.addEventListener('click', function(){ setCluster(btn.getAttribute('data-cluster-filter')); });
  });
  entries.forEach(function(btn){
    btn.addEventListener('click', function(){
      setCluster(btn.getAttribute('data-cluster-target'));
      document.getElementById('knowledge').scrollIntoView({behavior: 'smooth', block: 'start'});
    });
  });
  input.addEventListener('input', render);
  maturity.addEventListener('change', render);
  render();
})();
</script>
