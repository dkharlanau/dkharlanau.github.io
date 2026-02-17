---
layout: default
title: "LLM Prompt Library"
description: "Advanced LLM prompt engineering bytes by Dzmitryi Kharlanau (SAP Lead)."
permalink: /datasets/LLM-prompts/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Prompt Library</p>
  <h1 class="dataset-hero__title">LLM Prompts</h1>
  <p class="lead">4 entries. Filter by search and type. Each entry has a clean page + raw JSON.</p>
  <div class="dataset-actions">
    <a class="button" href="/datasets/">All datasets</a>
    <a class="button button--secondary" href="/datasets/search/">Search all</a>
    <a class="button button--secondary" href="/datasets/types/">Browse by type</a>
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
          <label for="datasetType"><strong>Type</strong></label>
          <select id="datasetType" class="dataset-select"><option value="">All</option><option value="llm_prompt_byte">llm_prompt_byte</option></select>
        </div>
      </div>
      <div class="dataset-hero__meta"><span class="pill" id="datasetCount"></span></div>
    </div>
    <div class="dataset-list" id="datasetList">
<article class="dataset-item" data-id="CE-01" data-title="context engineering is a discipline, not a prompt trick" data-tags="" data-type="llm_prompt_byte">
  <h2 class="dataset-item__title"><a href="/datasets/view/LLM-prompts/CE-01/">Context Engineering is a Discipline, Not a Prompt Trick</a></h2>
  <p class="dataset-item__summary">Context Engineering is a Discipline, Not a Prompt Trick</p>
  <div class="dataset-item__meta"><span class="pill pill--type">llm_prompt_byte</span> <span class="pill pill--dataset">LLM-prompts</span> <span class="pill">CE-01</span> <a class="pill" href="/datasets/LLM-prompts/CE-01.json">json</a></div>
</article>
<article class="dataset-item" data-id="CE-02" data-title="positional strategy: engineering around &#x27;lost in the middle&#x27; in long context + rag" data-tags="" data-type="llm_prompt_byte">
  <h2 class="dataset-item__title"><a href="/datasets/view/LLM-prompts/CE-02/">Positional Strategy: Engineering Around &#x27;Lost in the Middle&#x27; in Long Context + RAG</a></h2>
  <p class="dataset-item__summary">Positional Strategy: Engineering Around &#x27;Lost in the Middle&#x27; in Long Context + RAG</p>
  <div class="dataset-item__meta"><span class="pill pill--type">llm_prompt_byte</span> <span class="pill pill--dataset">LLM-prompts</span> <span class="pill">CE-02</span> <a class="pill" href="/datasets/LLM-prompts/CE-02.json">json</a></div>
</article>
<article class="dataset-item" data-id="CE-03" data-title="retrieval as a product: rag refinement, compression, and long-context noise control" data-tags="" data-type="llm_prompt_byte">
  <h2 class="dataset-item__title"><a href="/datasets/view/LLM-prompts/CE-03/">Retrieval as a Product: RAG Refinement, Compression, and Long-Context Noise Control</a></h2>
  <p class="dataset-item__summary">Retrieval as a Product: RAG Refinement, Compression, and Long-Context Noise Control</p>
  <div class="dataset-item__meta"><span class="pill pill--type">llm_prompt_byte</span> <span class="pill pill--dataset">LLM-prompts</span> <span class="pill">CE-03</span> <a class="pill" href="/datasets/LLM-prompts/CE-03.json">json</a></div>
</article>
<article class="dataset-item" data-id="CE-04" data-title="prompt optimization as engineering: from handcrafted prompts to optimized systems" data-tags="" data-type="llm_prompt_byte">
  <h2 class="dataset-item__title"><a href="/datasets/view/LLM-prompts/CE-04/">Prompt Optimization as Engineering: From Handcrafted Prompts to Optimized Systems</a></h2>
  <p class="dataset-item__summary">Prompt Optimization as Engineering: From Handcrafted Prompts to Optimized Systems</p>
  <div class="dataset-item__meta"><span class="pill pill--type">llm_prompt_byte</span> <span class="pill pill--dataset">LLM-prompts</span> <span class="pill">CE-04</span> <a class="pill" href="/datasets/LLM-prompts/CE-04.json">json</a></div>
</article>
    </div>
  </div>
  <aside class="dataset-panel">
    <div class="neub-card">
      <h2>Attribution</h2>
      <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
      <p>When you reference these bytes, please link back to the site or LinkedIn.</p>
      <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
    </div>
    <div class="neub-card">
      <h2>For tools</h2>
      <p><a href="/datasets/schema.json">schema.json</a> describes the attribution contract.</p>
      <p><a href="/datasets/manifest.json">manifest.json</a> lists every entry with ids, titles, tags, types, and paths.</p>
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
