---
layout: default
title: "Search — Dzmitryi Kharlanau"
description: "Search across SAP O2C articles, notes, CV highlights, FAQs, and machine-readable datasets on dkharlanau.github.io in one place."
permalink: /search/
sitemap: false
robots: "noindex,follow"
---

<section class="section search">
  <header class="section-heading">
    <p class="eyebrow">Search</p>
    <h1>Search the site</h1>
    <p class="lead">Find content across the blog, notes, CV, and structured datasets.</p>
  </header>

  <form class="search-form" role="search" method="get" action="/search/">
    <label for="search-query">Query</label>
    <input type="search" id="search-query" name="q" placeholder="e.g., clean core, integration, SAP" />
    <button type="submit">Search</button>
  </form>

  <div id="search-status" class="lead" role="status" aria-live="polite" aria-atomic="true"></div>
  <ul id="search-results" class="notes-grid"></ul>
  <p id="search-help" class="note-subtitle">Search looks at page titles and descriptions. Try specific keywords for better matches.</p>
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

  function matches(item, terms) {
    if (!terms.length) return false;
    const haystack = (item.title + ' ' + (item.description || '')).toLowerCase();
    return terms.every(term => haystack.includes(term));
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
      li.className = 'note-card neub-card';
      const title = document.createElement('h2');
      const link = document.createElement('a');
      link.href = item.url;
      link.textContent = item.title;
      title.appendChild(link);
      const meta = document.createElement('p');
      meta.className = 'note-subtitle';
      meta.textContent = item.type ? item.type.toUpperCase() : 'PAGE';
      const desc = document.createElement('p');
      desc.textContent = item.description || '';
      li.appendChild(title);
      li.appendChild(meta);
      li.appendChild(desc);
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

  const results = SEARCH_INDEX.filter(item => matches(item, terms));
  helpEl.style.display = 'none';
  render(results, query);
})();
</script>
