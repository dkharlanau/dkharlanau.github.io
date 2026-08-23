---
layout: default
title: "Search — Dzmitryi Kharlanau"
description: "Search across SAP O2C articles, notes, CV highlights, FAQs, and machine-readable datasets on dkharlanau.github.io in one place."
permalink: /search/
sitemap: false
robots: "noindex,follow"
last_modified_at: 2026-08-22
hide_global_cta: true
hide_site_share: true
---

<section class="search-canvas">
  <header class="search-canvas__hero">
    <div class="search-canvas__hero-copy">
      <p class="search-canvas__eyebrow">Search / site knowledge</p>
      <h1>Find the SAP problem, route, or proof.</h1>
      <p>Search services, diagnostics, scenarios, labs, research, profile evidence, and public datasets.</p>
    </div>
    <figure class="search-canvas__visual">
      <img src="/assets/img/systems/erp-document-flow-field.webp" alt="An ERP operating signal branching through document, data, warehouse, and integration evidence routes." width="1728" height="1106" decoding="async" fetchpriority="high" />
      <figcaption>One operating question, several evidence boundaries.</figcaption>
    </figure>
  </header>

  <form class="search-canvas__form" role="search" method="get" action="/search/">
    <label for="search-query">Search the public knowledge base</label>
    <div><input type="search" id="search-query" name="q" placeholder="Try delivery block, IDoc, duplicate business partner" autocomplete="off" /><button type="submit">Search <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></button></div>
  </form>

  <div class="search-canvas__result-area">
    <div id="search-status" class="search-canvas__status" role="status" aria-live="polite" aria-atomic="true"></div>
    <div id="search-filters" class="search-canvas__filters" aria-label="Filter search results" hidden></div>
    <ul id="search-results" class="search-result-list"></ul>
    <div id="search-help" class="search-canvas__help">
      <p>Use a business symptom, SAP object, integration signal, or decision area. Search reads public titles and descriptions.</p>
      <nav aria-label="Suggested searches">
        <a href="/search/?q=delivery%20block">Delivery block</a>
        <a href="/search/?q=IDoc">IDoc</a>
        <a href="/search/?q=business%20partner">Business partner</a>
        <a href="/search/?q=AMS%20cost">AMS cost</a>
      </nav>
    </div>
  </div>

  <section class="search-canvas__browse" aria-labelledby="search-browse-title">
    <header><p class="search-canvas__eyebrow">Browse instead</p><h2 id="search-browse-title">Start from the kind of work.</h2></header>
    <nav class="search-canvas__routes" aria-label="Start routes">
      <a href="/atlas/diagnostics/"><span>Diagnostics</span><small>Trace a SAP symptom</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/scenarios/"><span>Scenarios</span><small>Start from business impact</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/services/"><span>Services</span><small>Choose an improvement route</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </nav>
  </section>
</section>

<script>
(function () {
  const params = new URLSearchParams(window.location.search);
  const queryInput = document.getElementById('search-query');
  const resultsList = document.getElementById('search-results');
  const statusEl = document.getElementById('search-status');
  const filtersEl = document.getElementById('search-filters');
  const helpEl = document.getElementById('search-help');

  {% assign first_entry = true %}
  const SEARCH_INDEX = [
  {% for page in site.pages %}
    {% assign page_path = page.url | default: page.permalink %}
    {% if page_path and page.sitemap != false and page.search != false and page.title %}
      {% unless page_path contains 'sitemap' or page_path contains 'feed.xml' or page_path contains '404' or page_path contains '/assets/' or page_path contains '/ai/' or page_path == '/search/' %}
        {% if first_entry == false %},{% endif %}
        {% assign first_entry = false %}
        {
          "title": {{ page.title | strip_html | normalize_whitespace | jsonify }},
          "url": {{ page_path | relative_url | jsonify }},
          "description": {{ page.description | default: page.summary | default: page.excerpt | strip_html | normalize_whitespace | truncate: 200 | jsonify }},
          "type": "page"
        }
      {% endunless %}
    {% endif %}
  {% endfor %}
  {% for collection in site.collections %}
    {% unless collection.label == 'posts' %}
      {% for doc in collection.docs %}
        {% if doc.sitemap != false and doc.search != false %}
          {% if first_entry == false %},{% endif %}
          {% assign first_entry = false %}
          {
            "title": {{ doc.title | strip_html | normalize_whitespace | jsonify }},
            "url": {{ doc.url | relative_url | jsonify }},
            "description": {{ doc.description | default: doc.summary | default: doc.excerpt | strip_html | normalize_whitespace | truncate: 200 | jsonify }},
            "type": "{{ collection.label }}",
            "date": "{{ doc.date | default: doc.published | date_to_xmlschema }}"
          }
        {% endif %}
      {% endfor %}
    {% endunless %}
  {% endfor %}
  ];

  function tokenize(value) {
    return (value || '').toLowerCase().split(/\s+/).filter(Boolean);
  }

  function score(item, terms) {
    if (!terms.length) return 0;
    const title = item.title.toLowerCase();
    const description = (item.description || '').toLowerCase();
    return terms.reduce((total, term) => {
      if (title.includes(term)) return total + 3;
      if (description.includes(term)) return total + 1;
      return total;
    }, 0);
  }

  function sectionFor(url) {
    const path = new URL(url, window.location.origin).pathname;
    if (path.startsWith('/atlas/')) return 'Atlas';
    if (path.startsWith('/scenarios/')) return 'Scenarios';
    if (path.startsWith('/services/')) return 'Services';
    if (path.startsWith('/labs/')) return 'Labs';
    if (path.startsWith('/research/') || path.startsWith('/radar/') || path.startsWith('/news/')) return 'Research';
    if (path.startsWith('/datasets/')) return 'Datasets';
    if (path.startsWith('/machine/') || path.startsWith('/agent-tools/') || path.startsWith('/agent-skills/') || path.startsWith('/mcp/')) return 'Machine';
    if (path.startsWith('/about/') || path.startsWith('/cv/') || path.startsWith('/certifications/') || path.startsWith('/education/')) return 'Profile';
    return 'Knowledge';
  }

  function renderFilters(items, query) {
    filtersEl.innerHTML = '';
    const counts = items.reduce((map, item) => map.set(item.section, (map.get(item.section) || 0) + 1), new Map());
    const entries = [['All', items.length], ...[...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))];
    entries.forEach(([section, count], index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = `${section} ${count}`;
      button.setAttribute('aria-pressed', String(index === 0));
      button.addEventListener('click', () => {
        filtersEl.querySelectorAll('button').forEach(control => control.setAttribute('aria-pressed', 'false'));
        button.setAttribute('aria-pressed', 'true');
        render(section === 'All' ? items : items.filter(item => item.section === section), query, section);
      });
      filtersEl.appendChild(button);
    });
    filtersEl.hidden = entries.length <= 2;
  }

  function render(items, query, section = 'All') {
    resultsList.innerHTML = '';
    if (!items.length) {
      statusEl.textContent = `No results for “${query}”. Try another keyword.`;
      filtersEl.hidden = true;
      helpEl.style.display = '';
      return;
    }

    statusEl.textContent = section === 'All'
      ? `Found ${items.length} result${items.length === 1 ? '' : 's'} for “${query}”.`
      : `${items.length} ${section.toLowerCase()} result${items.length === 1 ? '' : 's'} for “${query}”.`;
    items.slice(0, 30).forEach(item => {
      const li = document.createElement('li');
      li.className = 'search-result';
      const link = document.createElement('a');
      link.href = item.url;
      const meta = document.createElement('p');
      meta.className = 'search-result__meta';
      meta.textContent = item.section;
      const title = document.createElement('strong');
      title.textContent = item.title;
      const desc = document.createElement('p');
      desc.className = 'search-result__description';
      desc.textContent = item.description || '';
      const arrow = document.createElement('span');
      arrow.className = 'material-symbols-outlined';
      arrow.setAttribute('aria-hidden', 'true');
      arrow.textContent = 'arrow_forward';
      link.append(meta, title, desc, arrow);
      li.appendChild(link);
      resultsList.appendChild(li);
    });
  }

  const query = (params.get('q') || '').trim();
  if (queryInput && query) {
    queryInput.value = query;
  }

  const terms = tokenize(query);
  if (!terms.length) {
    statusEl.textContent = 'Enter a query to search the public knowledge system.';
    helpEl.style.display = '';
    return;
  }

  const results = SEARCH_INDEX
    .map(item => ({ item, relevance: score(item, terms) }))
    .filter(result => result.relevance > 0)
    .sort((a, b) => b.relevance - a.relevance || a.item.title.localeCompare(b.item.title))
    .map(result => ({ ...result.item, section: sectionFor(result.item.url) }));
  helpEl.style.display = 'none';
  renderFilters(results, query);
  render(results, query);
})();
</script>
