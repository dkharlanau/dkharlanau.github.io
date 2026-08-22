---
layout: default
title: "Search — Dzmitryi Kharlanau"
description: "Search across SAP O2C articles, notes, CV highlights, FAQs, and machine-readable datasets on dkharlanau.github.io in one place."
permalink: /search/
sitemap: false
robots: "noindex,follow"
---

<section class="search-canvas">
  <header class="search-canvas__hero">
    <p class="search-canvas__eyebrow">Search / site knowledge</p>
    <h1>Find the SAP problem, route, or proof.</h1>
    <p>Search across services, diagnostics, scenarios, technical writing, profile evidence, and public datasets.</p>
  </header>

  <form class="search-canvas__form" role="search" method="get" action="/search/">
    <label for="search-query">Search the public knowledge base</label>
    <div><input type="search" id="search-query" name="q" placeholder="Try delivery block, IDoc, duplicate business partner" autocomplete="off" /><button type="submit">Search <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></button></div>
  </form>

  <nav class="search-canvas__routes" aria-label="Start routes">
    <a href="/atlas/diagnostics/"><span>Diagnostics</span><small>Trace a SAP symptom</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/scenarios/"><span>Scenarios</span><small>Start from business impact</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    <a href="/services/"><span>Services</span><small>Choose an improvement route</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
  </nav>

  <div class="search-canvas__result-area">
    <div id="search-status" class="search-canvas__status" role="status" aria-live="polite" aria-atomic="true"></div>
    <ul id="search-results" class="search-result-list"></ul>
    <p id="search-help" class="search-canvas__help">Search reads public titles and descriptions. Use the business symptom, SAP object, or decision area rather than broad terms.</p>
  </div>
</section>

<script>
(function () {
  const params = new URLSearchParams(window.location.search);
  const queryInput = document.getElementById('search-query');
  const resultsList = document.getElementById('search-results');
  const statusEl = document.getElementById('search-status');
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
          "url": {{ page_path | absolute_url | jsonify }},
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
            "url": {{ doc.url | absolute_url | jsonify }},
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

  function render(items, query) {
    resultsList.innerHTML = '';
    if (!items.length) {
      statusEl.textContent = `No results for “${query}”. Try another keyword.`;
      return;
    }

    statusEl.textContent = `Found ${items.length} result${items.length === 1 ? '' : 's'} for “${query}”:`;
    items.slice(0, 30).forEach(item => {
      const li = document.createElement('li');
      li.className = 'search-result';
      const link = document.createElement('a');
      link.href = item.url;
      const meta = document.createElement('p');
      meta.className = 'search-result__meta';
      meta.textContent = item.type ? item.type.toUpperCase() : 'PAGE';
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
    statusEl.textContent = 'Enter a query to search notes, blog, and CV.';
    helpEl.style.display = '';
    return;
  }

  const results = SEARCH_INDEX
    .map(item => ({ item, relevance: score(item, terms) }))
    .filter(result => result.relevance > 0)
    .sort((a, b) => b.relevance - a.relevance || a.item.title.localeCompare(b.item.title))
    .map(result => result.item);
  helpEl.style.display = 'none';
  render(results, query);
})();
</script>
