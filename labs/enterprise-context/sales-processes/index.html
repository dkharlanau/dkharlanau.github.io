---
layout: default
title: "SAP Sales Process Atlas — Standard, Special and Cross-Process Variants"
description: "A memory-first map of SAP S/4HANA sales processes: steps, control points, data hinges, impacts, constraints, extensions, and stable mnemonic codes."
permalink: /labs/enterprise-context/sales-processes/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
sales_process_atlas: true
tags:
  - sap
  - s4hana
  - sales
  - sd
  - order-to-cash
  - special-processes
---

{% assign atlas_groups = site.data.labs.enterprise_context.processes.sales_process_atlas %}
{% assign atlas = atlas_groups.index %}
{% assign group_keys = "01_baseline,02_fulfillment,03_intercompany,04_commercial,05_execution,06_overlays" | split: "," %}
{% assign registry = site.data.labs.enterprise_context.sources.sales_process_registry %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Sales Process Atlas</li></ol>
</nav>

<div class="research-canvas sales-process-atlas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Sales process atlas / memory first</p>
      <h1>Learn the branch, not the transaction code.</h1>
      <p>A special sales process becomes memorable when you can explain what changed from ordinary sell-from-stock: ownership, procurement, legal entity, production, billing, or the customer promise. The page is built around those changes.</p>
      <a class="research-canvas__button" href="#memory-cards">Open the memory cards <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Atlas inventory">
      <p>Working inventory</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>20</strong><small>Processes & overlays</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ atlas.extension_surfaces | size }}</strong><small>Extension surfaces</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ registry.sources | size }}</strong><small>Primary references</small></div>
      <em>Author codes are stable memory keys. SAP scope-item IDs remain external references.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">fork_right</span>
    <p><strong>Memory rule.</strong> Start from <code>SD.SFS</code>. Every special process is the baseline plus a changed control rule: who supplies, who owns stock, when control transfers, what triggers billing, or whether supply is made specifically for one customer.</p>
    <a href="/labs/enterprise-context/data/sales-process-atlas.json">Open JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Our code system</p>
      <h2>One stable mnemonic. Vendor IDs stay references.</h2>
      <p><code>SD.&lt;code&gt;</code> means a process or process variant. <code>SD+&lt;code&gt;</code> means an overlay or cross-cutting capability. That keeps the learning key stable even when scope items, apps, or release labels move around.</p>
    </header>
    <div class="spa-code-grid">
      <article><span>SD.</span><strong>Process / variant</strong><p>Examples: <code>SD.TPO</code>, <code>SD.CON</code>, <code>SD.AIC</code>.</p></article>
      <article><span>SD+</span><strong>Overlay / capability</strong><p>Examples: <code>SD+OSP</code> promotions and <code>SD+REL</code> related-object navigation.</p></article>
      <article><span>EXT-</span><strong>Extension surface</strong><p>Field, logic, API, copy/reference, or side-by-side extension.</p></article>
    </div>
  </section>

  <section class="spa-memory-model" data-reveal>
    <div>
      <p class="research-canvas__eyebrow">Seven questions</p>
      <h2>If you can answer these, you own the process.</h2>
    </div>
    <ol>
      {% for question in atlas.memory_model.questions %}
      <li><span>0{{ forloop.index }}</span><p>{{ question }}</p></li>
      {% endfor %}
    </ol>
  </section>

  <section class="research-canvas__inventory" id="memory-cards" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Memory cards</p>
      <h2>Twenty branches, each reduced to the decisions that matter.</h2>
      <p>The first screen gives the mnemonic, promise, and flow. Expand a card for the controlling elements, data hinges, limits, lead-level questions, and extension points.</p>
    </header>

    <div class="spa-card-grid">
      {% for group_key in group_keys %}
      {% assign group = atlas_groups[group_key] %}
      {% for process in group.processes %}
      <article class="spa-card" id="{{ process.code | downcase | replace: '.', '-' | replace: '+', '-plus-' }}">
        <header class="spa-card__head">
          <div>
            <span class="spa-code">{{ process.code }}</span>
            <span class="spa-kind">{{ process.kind | replace: "_", " " }}</span>
          </div>
          {% if process.sap_scope_items and process.sap_scope_items.size > 0 %}
          <p class="spa-scope">
            {% for scope in process.sap_scope_items %}<span>{{ scope.id }}</span>{% endfor %}
          </p>
          {% endif %}
        </header>
        <h3>{{ process.title }}</h3>
        <p class="spa-hook">{{ process.memory_hook }}</p>
        <p class="spa-intent">{{ process.business_intent }}</p>

        <div class="spa-flow" aria-label="{{ process.title }} flow">
          {% for step in process.flow %}
          <span>{{ step }}</span>{% unless forloop.last %}<i aria-hidden="true">→</i>{% endunless %}
          {% endfor %}
        </div>

        {% if process.modes %}
        <div class="spa-modes">
          {% for mode in process.modes %}
          <span><b>{{ mode.code }}</b> {{ mode.title }}</span>
          {% endfor %}
        </div>
        {% endif %}

        <details>
          <summary>Controls, data and boundaries <span class="material-symbols-outlined" aria-hidden="true">expand_more</span></summary>
          <div class="spa-detail-grid">
            <section>
              <h4>Control plane</h4>
              <ul>{% for item in process.control_plane %}<li><strong>{{ item.control }}</strong><span>{{ item.why }}</span></li>{% endfor %}</ul>
            </section>
            <section>
              <h4>Data hinges</h4>
              <ul>{% for item in process.data_hinges %}<li><strong>{{ item.data }}</strong><span>{{ item.changes }}</span></li>{% endfor %}</ul>
            </section>
            <section>
              <h4>What changes</h4>
              <ul>{% for item in process.impact_summary %}<li>{{ item }}</li>{% endfor %}</ul>
            </section>
            <section>
              <h4>Constraints</h4>
              <ul>{% for item in process.constraints %}<li>{{ item }}</li>{% endfor %}</ul>
            </section>
          </div>

          <div class="spa-lead">
            <p>Lead questions</p>
            <ol>{% for q in process.lead_questions %}<li>{{ q }}</li>{% endfor %}</ol>
          </div>

          <div class="spa-extension-row">
            <span>Extensions</span>
            {% for ext in process.extension_points %}<code>{{ ext }}</code>{% endfor %}
          </div>
        </details>
      </article>
      {% endfor %}
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Fast comparisons</p>
      <h2>Most assessment questions hide inside a contrast.</h2>
      <p>The useful answer is rarely a definition. It is the boundary between two processes that look similar until one document, stock segment, or billing trigger changes.</p>
    </header>

    <div class="spa-compare-grid">
      <article><span>SD.TPO ↔ SD.PTO</span><h3>Direct ship vs order-specific supply</h3><p><b>TPO:</b> the external vendor can ship directly to the customer. <b>PTO:</b> procurement is pegged to the sales item so the acquired supply cannot quietly satisfy another demand.</p></article>
      <article><span>SD.ICO ↔ SD.AIC</span><h3>Classic relationship vs orchestrated value chain</h3><p><b>ICO:</b> selling and delivering company roles are connected through delivery and intercompany billing. <b>AIC:</b> additional intercompany purchase/sales documents and transfer-of-control logistics make the internal leg explicit.</p></article>
      <article><span>SD.SFS ↔ SD.VST</span><h3>Physical goods issue vs transfer of control</h3><p><b>SFS:</b> ordinary stock leaves the plant. <b>VST:</b> goods may have physically left while value still remains in a controlled transit stock segment until transfer of control.</p></article>
      <article><span>SD.CSH ↔ SD.RSH</span><h3>Immediate payment vs immediate delivery</h3><p><b>Cash sales:</b> payment and order-related cash billing are immediate. <b>Rush order:</b> delivery is immediate, but normal delivery-related invoicing follows later.</p></article>
      <article><span>SD.BOM.ERLA ↔ SD.BOM.LUMF</span><h3>Main item vs component ownership</h3><p><b>ERLA:</b> commercial and logistics behavior sits mainly on the higher-level item. <b>LUMF:</b> subitems become operationally relevant, including delivery-group behavior.</p></article>
      <article><span>SD.CON.FILL ↔ SD.CON.ISSUE</span><h3>Move stock vs transfer ownership</h3><p><b>Fill-up:</b> stock moves to the customer site but stays yours. <b>Issue:</b> customer withdrawal consumes consignment stock and becomes billing relevant.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extension layer</p>
      <h2>Extend the branch without losing ownership of the core.</h2>
      <p>Extensions are modeled separately because “we can code it” is not an architecture principle. First decide which process contract owns the behavior, then choose the smallest extension surface that preserves that boundary.</p>
    </header>

    <div class="spa-extension-grid">
      {% for ext in atlas.extension_surfaces %}
      <article>
        <span>{{ ext.code }}</span>
        <h3>{{ ext.title }}</h3>
        <p class="spa-hook">{{ ext.memory_hook }}</p>
        <p>{{ ext.applies_to | join: " · " }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="spa-machine" data-reveal>
    <div>
      <p class="research-canvas__eyebrow">For datasets and AI</p>
      <h2>The cards are a view. The structured process records are the asset.</h2>
      <p>The same codes, flows, controls, data hinges, constraints, sources, and extension points are published as JSON so they can be reused for study prompts, comparison tasks, synthetic cases, impact analysis, and later graph traversal.</p>
    </div>
    <div>
      <a class="research-canvas__button" href="/labs/enterprise-context/data/sales-process-atlas.json">Process atlas JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
      <a class="spa-text-link" href="/labs/enterprise-context/data/sales-process-sources.json">Source registry</a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Source boundary</p>
      <h2>Use SAP documentation as evidence, not as website copy.</h2>
      <p>Primary references are registered with access dates and product scope. The explanations, mnemonics, comparisons, diagrams, and memory hooks on this page are independently written.</p>
    </header>
    <div class="research-route-list">
      {% for source in registry.sources %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.title }}</strong><small>{{ source.product_scope }}{% if source.release_scope %} · {{ source.release_scope }}{% endif %} · accessed {{ source.accessed_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
