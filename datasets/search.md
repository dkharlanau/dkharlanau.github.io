---
layout: default
title: "Dataset Search"
description: "Search all dataset bytes by Dzmitryi Kharlanau (SAP Lead)."
permalink: /datasets/search/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Datasets</p>
  <h1 class="dataset-hero__title">Search all bytes</h1>
  <p class="lead">Fast client-side search across all collections. Filter by dataset and entity type.</p>
  <div class="dataset-actions">
    <a class="button" href="/datasets/">All datasets</a>
    <a class="button button--secondary" href="/datasets/types/">Browse by type</a>
  </div>
</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="dataset-panel">
    <div class="dataset-filter">
      <div class="dataset-filter__row">
        <div>
          <label for="globalSearch"><strong>Search</strong></label>
          <input id="globalSearch" type="search" placeholder="Search by title, ID, tag, summary…" autocomplete="off" />
        </div>
        <div>
          <label for="globalDataset"><strong>Dataset</strong></label>
          <select id="globalDataset" class="dataset-select"><option value="">All</option></select>
        </div>
        <div>
          <label for="globalType"><strong>Type</strong></label>
          <select id="globalType" class="dataset-select"><option value="">All</option></select>
        </div>
      </div>
      <div class="dataset-hero__meta"><span class="pill" id="globalCount">Loading…</span></div>
    </div>
    <div class="dataset-list" id="globalList"></div>
  </div>
</div>

<script>
(function(){
  var input = document.getElementById('globalSearch');
  var dsSel = document.getElementById('globalDataset');
  var typeSel = document.getElementById('globalType');
  var list = document.getElementById('globalList');
  var count = document.getElementById('globalCount');
  if(!input || !dsSel || !typeSel || !list || !count) return;
  var all = [];
  function escHtml(s){
    return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  }
  function uniq(arr){
    var m = {};
    var out = [];
    arr.forEach(function(x){ if(x && !m[x]){ m[x]=1; out.push(x);} });
    return out;
  }
  function opt(el, value){
    var o = document.createElement('option');
    o.value = value;
    o.textContent = value;
    el.appendChild(o);
  }
  function render(){
    var q = (input.value||'').trim().toLowerCase();
    var d = (dsSel.value||'').trim();
    var t = (typeSel.value||'').trim();
    var shown = 0;
    var html = [];
    all.forEach(function(e){
      if(d && e.dataset !== d) return;
      if(t && e.entity_type !== t) return;
      var hay = (e.id+' '+e.title+' '+(e.summary||'')+' '+(e.tags||[]).join(' ')).toLowerCase();
      if(q && hay.indexOf(q) === -1) return;
      shown++;
      var pills = [];
      if(e.entity_type) pills.push('<span class="pill pill--type">'+escHtml(e.entity_type)+'</span>');
      pills.push('<span class="pill pill--dataset">'+escHtml(e.dataset)+'</span>');
      pills.push('<span class="pill">'+escHtml(e.id)+'</span>');
      (e.tags||[]).slice(0,5).forEach(function(tag){ pills.push('<span class="pill">'+escHtml(tag)+'</span>'); });
      pills.push('<a class="pill" href="/datasets/'+escHtml(e.dataset)+'/'+escHtml(e.id)+'.json">json</a>');
      html.push('<article class="dataset-item">'
        + '<h2 class="dataset-item__title"><a href="/datasets/view/'+escHtml(e.dataset)+'/'+escHtml(e.id)+'/">'+escHtml(e.title||e.id)+'</a></h2>'
        + (e.summary ? '<p class="dataset-item__summary">'+escHtml(e.summary)+'</p>' : '')
        + '<div class="dataset-item__meta">'+pills.join(' ')+'</div>'
      + '</article>');
    });
    list.innerHTML = html.join('\n') || '<p class="dataset-empty">No matches.</p>';
    count.textContent = shown + ' results';
  }
  input.addEventListener('input', render);
  dsSel.addEventListener('change', render);
  typeSel.addEventListener('change', render);
  fetch('/datasets/manifest.json', {cache: 'no-cache'})
    .then(function(r){ return r.json(); })
    .then(function(m){
      all = (m.entries||[]).map(function(e){
        return {
          dataset: e.dataset,
          id: e.id,
          title: e.title || e.id,
          tags: e.tags || [],
          entity_type: e.entity_type || '',
          summary: e.summary || ''
        };
      });
      uniq(all.map(function(e){return e.dataset;})).sort().forEach(function(v){ opt(dsSel, v); });
      uniq(all.map(function(e){return e.entity_type;})).sort().forEach(function(v){ opt(typeSel, v); });
      render();
    })
    .catch(function(){ count.textContent = 'Failed to load manifest.json'; });
})();
</script>
