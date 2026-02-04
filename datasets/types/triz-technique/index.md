---
layout: default
title: "triz_technique"
description: "Dataset bytes of type triz_technique by Dzmitryi Kharlanau (SAP Lead)."
permalink: /datasets/types/triz-technique/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Type</p>
  <h1 class="dataset-hero__title">triz_technique</h1>
  <p class="lead">4 entries across multiple collections.</p>
  <div class="dataset-actions">
    <a class="button" href="/datasets/types/">All types</a>
    <a class="button button--secondary" href="/datasets/search/">Search all</a>
  </div>
</div>

<div class="dataset-grid">
  <div class="dataset-panel">
    <div class="dataset-filter">
      <div class="dataset-filter__row">
        <div>
          <label for="datasetSearch"><strong>Search</strong></label>
          <input id="datasetSearch" type="search" placeholder="Search by ID, title, tag, summary…" autocomplete="off" />
        </div>
        <div>
          <label for="datasetType"><strong>Subtype</strong></label>
          <select id="datasetType" class="dataset-select"><option value="">All</option><option value="triz_technique">triz_technique</option></select>
        </div>
      </div>
      <div class="dataset-hero__meta"><span class="pill" id="datasetCount"></span></div>
    </div>
    <div class="dataset-list" id="datasetList">
<article class="dataset-item" data-id="TRIZ-TECH-01" data-title="contradiction formulation (engineering contradiction)" data-tags="" data-type="triz_technique">
  <h2 class="dataset-item__title"><a href="/datasets/view/TRIZ-bytes/TRIZ-TECH-01/">Contradiction Formulation (Engineering Contradiction)</a></h2>
  <p class="dataset-item__summary">Turn a messy situation into a solvable TRIZ problem by expressing it as a trade-off between two parameters.</p>
  <div class="dataset-item__meta"><span class="pill pill--type">triz_technique</span> <span class="pill pill--dataset">TRIZ-bytes</span> <span class="pill">TRIZ-TECH-01</span> <a class="pill" href="/datasets/TRIZ-bytes/TRIZ-TECH-01.json">json</a></div>
</article>
<article class="dataset-item" data-id="TRIZ-TECH-02" data-title="physical contradiction + separation principles" data-tags="" data-type="triz_technique">
  <h2 class="dataset-item__title"><a href="/datasets/view/TRIZ-bytes/TRIZ-TECH-02/">Physical Contradiction + Separation Principles</a></h2>
  <p class="dataset-item__summary">Break a deadlock where the same parameter must be simultaneously high and low by separating requirements across conditions.</p>
  <div class="dataset-item__meta"><span class="pill pill--type">triz_technique</span> <span class="pill pill--dataset">TRIZ-bytes</span> <span class="pill">TRIZ-TECH-02</span> <a class="pill" href="/datasets/TRIZ-bytes/TRIZ-TECH-02.json">json</a></div>
</article>
<article class="dataset-item" data-id="TRIZ-TECH-03" data-title="system operator (9 windows)" data-tags="" data-type="triz_technique">
  <h2 class="dataset-item__title"><a href="/datasets/view/TRIZ-bytes/TRIZ-TECH-03/">System Operator (9 Windows)</a></h2>
  <p class="dataset-item__summary">Escape tunnel vision by analyzing the problem across time (past/present/future) and hierarchy (subsystem/system/supersystem).</p>
  <div class="dataset-item__meta"><span class="pill pill--type">triz_technique</span> <span class="pill pill--dataset">TRIZ-bytes</span> <span class="pill">TRIZ-TECH-03</span> <a class="pill" href="/datasets/TRIZ-bytes/TRIZ-TECH-03.json">json</a></div>
</article>
<article class="dataset-item" data-id="TRIZ-TECH-04" data-title="x-operator (exaggeration / extremes)" data-tags="" data-type="triz_technique">
  <h2 class="dataset-item__title"><a href="/datasets/view/TRIZ-bytes/TRIZ-TECH-04/">X-Operator (Exaggeration / Extremes)</a></h2>
  <p class="dataset-item__summary">Force breakthrough ideas by pushing a system parameter to an extreme and observing what must change to make it work.</p>
  <div class="dataset-item__meta"><span class="pill pill--type">triz_technique</span> <span class="pill pill--dataset">TRIZ-bytes</span> <span class="pill">TRIZ-TECH-04</span> <a class="pill" href="/datasets/TRIZ-bytes/TRIZ-TECH-04.json">json</a></div>
</article>
    </div>
  </div>
  <aside class="dataset-panel">
    <div class="neub-card">
      <h2>Attribution</h2>
      <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
      <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
    </div>
  </aside>
</div>

<script>
(function(){
  var input = document.getElementById('datasetSearch');
  var list = document.getElementById('datasetList');
  var count = document.getElementById('datasetCount');
  var typeSel = document.getElementById('datasetType');
  if(!input || !list || !count) return;
  var items = Array.prototype.slice.call(list.querySelectorAll('.dataset-item'));
  function render(){
    var q = (input.value || '').trim().toLowerCase();
    var t = (typeSel && typeSel.value || '').trim().toLowerCase();
    var shown = 0;
    items.forEach(function(el){
      var hay = (el.getAttribute('data-id')||'') + ' ' + (el.getAttribute('data-title')||'') + ' ' + (el.getAttribute('data-tags')||'');
      var okQ = !q || hay.indexOf(q) !== -1;
      var okT = !t || (el.getAttribute('data-type')||'').indexOf(t) !== -1;
      var ok = okQ && okT;
      el.style.display = ok ? '' : 'none';
      if(ok) shown++;
    });
    count.textContent = shown + ' / 4 visible';
  }
  input.addEventListener('input', render);
  if(typeSel) typeSel.addEventListener('change', render);
  render();
})();
</script>
