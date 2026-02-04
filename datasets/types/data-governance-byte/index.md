---
layout: default
title: "data_governance_byte"
description: "Dataset bytes of type data_governance_byte by Dzmitryi Kharlanau (SAP Lead)."
permalink: /datasets/types/data-governance-byte/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Type</p>
  <h1 class="dataset-hero__title">data_governance_byte</h1>
  <p class="lead">3 entries across multiple collections.</p>
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
          <select id="datasetType" class="dataset-select"><option value="">All</option><option value="data_governance_byte">data_governance_byte</option></select>
        </div>
      </div>
      <div class="dataset-hero__meta"><span class="pill" id="datasetCount"></span></div>
    </div>
    <div class="dataset-list" id="datasetList">
<article class="dataset-item" data-id="db_governance_decision_rights_v0_1" data-title="decision rights &amp; raci for master data (who decides what?)" data-tags="governance raci ownership accountability operating_model" data-type="data_governance_byte">
  <h2 class="dataset-item__title"><a href="/datasets/view/DAMA/db_governance_decision_rights_v0_1/">Decision Rights &amp; RACI for Master Data (Who decides what?)</a></h2>
  <p class="dataset-item__summary">Decision Rights &amp; RACI for Master Data (Who decides what?)</p>
  <div class="dataset-item__meta"><span class="pill pill--type">data_governance_byte</span> <span class="pill pill--dataset">DAMA</span> <span class="pill">db_governance_decision_rights_v0_1</span> <span class="pill">governance</span> <span class="pill">raci</span> <span class="pill">ownership</span> <span class="pill">accountability</span> <span class="pill">operating_model</span> <a class="pill" href="/datasets/DAMA/db_governance_decision_rights_v0_1.json">json</a></div>
</article>
<article class="dataset-item" data-id="db_governance_drift_detection_response_v0_1" data-title="governance drift: how to detect degradation early and respond without panic fixes" data-tags="governance_drift operating_model leading_indicators bypass exceptions mdg" data-type="data_governance_byte">
  <h2 class="dataset-item__title"><a href="/datasets/view/DAMA/db_governance_drift_detection_response_v0_1/">Governance Drift: How to detect degradation early and respond without panic fixes</a></h2>
  <p class="dataset-item__summary">Governance Drift: How to detect degradation early and respond without panic fixes</p>
  <div class="dataset-item__meta"><span class="pill pill--type">data_governance_byte</span> <span class="pill pill--dataset">DAMA</span> <span class="pill">db_governance_drift_detection_response_v0_1</span> <span class="pill">governance_drift</span> <span class="pill">operating_model</span> <span class="pill">leading_indicators</span> <span class="pill">bypass</span> <span class="pill">exceptions</span> <a class="pill" href="/datasets/DAMA/db_governance_drift_detection_response_v0_1.json">json</a></div>
</article>
<article class="dataset-item" data-id="db_governance_maturity_model_mdg_v0_1" data-title="mdg governance maturity model: assess current level and choose the next upgrade (level 1–5)" data-tags="maturity_model assessment roadmap mdg governance continuous_improvement" data-type="data_governance_byte">
  <h2 class="dataset-item__title"><a href="/datasets/view/DAMA/db_governance_maturity_model_mdg_v0_1/">MDG Governance Maturity Model: assess current level and choose the next upgrade (Level 1–5)</a></h2>
  <p class="dataset-item__summary">MDG Governance Maturity Model: assess current level and choose the next upgrade (Level 1–5)</p>
  <div class="dataset-item__meta"><span class="pill pill--type">data_governance_byte</span> <span class="pill pill--dataset">DAMA</span> <span class="pill">db_governance_maturity_model_mdg_v0_1</span> <span class="pill">maturity_model</span> <span class="pill">assessment</span> <span class="pill">roadmap</span> <span class="pill">mdg</span> <span class="pill">governance</span> <a class="pill" href="/datasets/DAMA/db_governance_maturity_model_mdg_v0_1.json">json</a></div>
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
    count.textContent = shown + ' / 3 visible';
  }
  input.addEventListener('input', render);
  if(typeSel) typeSel.addEventListener('change', render);
  render();
})();
</script>
