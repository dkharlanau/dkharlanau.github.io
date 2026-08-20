(() => {
  'use strict';

  const atlasNode = document.getElementById('memory-atlas-data');
  const masteryNode = document.getElementById('mastery-data');
  if (!atlasNode) return;

  let ATLAS = {};
  let MASTERY = {};
  try {
    ATLAS = JSON.parse(atlasNode.textContent || '{}');
    MASTERY = masteryNode ? JSON.parse(masteryNode.textContent || '{}') : {};
  } catch (error) {
    console.error('Memory Atlas data could not be parsed.', error);
    return;
  }

  const contract = ATLAS.contract || {};
  const maps = Array.isArray(ATLAS.maps) ? ATLAS.maps : [];
  const atlasStorageKey = contract.storage_key || 'sapLeadMemoryAtlasV1';
  const masteryContract = MASTERY.contract || {};
  const masteryStorageKey = contract.mastery_storage_key || masteryContract.storage_key || 'sapLeadMasteryHistoryV1';
  const passAccuracy = Number(contract.pass_accuracy ?? 1);
  const maxSavedRuns = Number(contract.max_saved_runs ?? 120);
  const masteryCards = new Set((MASTERY.cards || []).map(card => card.skill_id));
  const passScore = Number(masteryContract.pass_score ?? 2);
  const retainedSuccesses = Number(masteryContract.retained_successes ?? 3);
  const retainedSpanDays = Number(masteryContract.retained_span_days ?? 7);
  const stateLabels = Object.fromEntries((masteryContract.states || []).map(item => [item.id, item.label]));
  const DAY = 86400000;
  const $ = id => document.getElementById(id);

  let activeMapId = maps[0]?.id || null;
  let mode = 'study';
  let bankOrder = [];
  let placed = [];
  let checked = false;
  let lastResult = null;

  function safeParse(key) {
    try {
      const value = JSON.parse(localStorage.getItem(key) || '[]');
      return Array.isArray(value) ? value : [];
    } catch (_) {
      return [];
    }
  }

  function atlasRuns() {
    return safeParse(atlasStorageKey).filter(row => row && typeof row.map_id === 'string' && typeof row.reviewed_at === 'string' && Number.isInteger(row.correct) && Number.isInteger(row.total) && row.total > 0 && Number.isFinite(Number(row.accuracy)));
  }

  function saveRun(row) {
    const rows = atlasRuns();
    rows.push(row);
    localStorage.setItem(atlasStorageKey, JSON.stringify(rows.slice(-Math.max(1, maxSavedRuns))));
  }

  function masteryRows() {
    return safeParse(masteryStorageKey).filter(row => row && typeof row.skill_id === 'string' && Number.isInteger(row.score) && typeof row.mode === 'string' && typeof row.reviewed_at === 'string' && !Number.isNaN(Date.parse(row.reviewed_at)));
  }

  function spanDays(rows) {
    if (rows.length < 2) return 0;
    return (Date.parse(rows[rows.length - 1].reviewed_at) - Date.parse(rows[0].reviewed_at)) / DAY;
  }

  function masteryState(skillId, rows = masteryRows()) {
    if (!masteryCards.has(skillId)) return 'roadmap';
    const attempts = rows.filter(row => row.skill_id === skillId).sort((a, b) => Date.parse(a.reviewed_at) - Date.parse(b.reviewed_at));
    if (!attempts.length) return 'new';
    const passed = new Set(attempts.filter(row => row.score >= passScore).map(row => row.mode));
    const advanced = attempts.filter(row => row.score >= passScore && (row.mode === 'defend' || row.mode === 'review'));
    if (passed.has('defend') && advanced.length >= retainedSuccesses && spanDays(advanced) >= retainedSpanDays) return 'retained';
    if (passed.has('defend')) return 'defended';
    if (passed.has('apply')) return 'applied';
    if (passed.has('connect')) return 'connected';
    if (passed.has('recall')) return 'recalled';
    return 'new';
  }

  function stateLabel(skillId, rows) {
    const state = masteryState(skillId, rows);
    return state === 'roadmap' ? 'Roadmap only' : (stateLabels[state] || state);
  }

  function activeMap() {
    return maps.find(item => item.id === activeMapId) || maps[0] || null;
  }

  function shuffle(values) {
    const result = values.slice();
    for (let i = result.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
  }

  function resetRebuild() {
    const map = activeMap();
    placed = [];
    checked = false;
    lastResult = null;
    bankOrder = map ? shuffle(map.nodes.map(node => node.id)) : [];
  }

  function latestRun(mapId, runs = atlasRuns()) {
    const rows = runs.filter(row => row.map_id === mapId).sort((a, b) => Date.parse(a.reviewed_at) - Date.parse(b.reviewed_at));
    return rows.length ? rows[rows.length - 1] : null;
  }

  function exactRun(mapId, runs = atlasRuns()) {
    return runs.some(row => row.map_id === mapId && Number(row.accuracy) >= passAccuracy);
  }

  function metric(value, label) {
    const article = document.createElement('article');
    const strong = document.createElement('strong');
    const span = document.createElement('span');
    strong.textContent = value;
    span.textContent = label;
    article.append(strong, span);
    return article;
  }

  function renderMetrics(runs) {
    const host = $('ma-metrics');
    if (!host) return;
    const exact = runs.filter(row => Number(row.accuracy) >= passAccuracy).length;
    const proven = maps.filter(map => exactRun(map.id, runs)).length;
    const latest = runs.length ? runs.slice().sort((a, b) => Date.parse(b.reviewed_at) - Date.parse(a.reviewed_at))[0] : null;
    host.replaceChildren(
      metric(String(runs.length), 'Rebuild attempts'),
      metric(String(exact), 'Exact rebuilds'),
      metric(`${proven}/${maps.length}`, 'Maps proven'),
      metric(latest ? `${Math.round(Number(latest.accuracy) * 100)}%` : '—', 'Latest accuracy')
    );
  }

  function renderChooser(runs) {
    const host = $('ma-map-chooser');
    if (!host) return;
    host.replaceChildren();
    maps.forEach(map => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'memory-atlas__map-button';
      button.setAttribute('aria-pressed', activeMapId === map.id ? 'true' : 'false');
      const strong = document.createElement('strong');
      const small = document.createElement('small');
      const status = exactRun(map.id, runs) ? 'Exact rebuild proven' : latestRun(map.id, runs) ? `Latest ${Math.round(latestRun(map.id, runs).accuracy * 100)}%` : 'Not rebuilt yet';
      strong.textContent = `${map.label} · ${map.title}`;
      small.textContent = `${status}. ${map.statement}`;
      button.append(strong, small);
      button.addEventListener('click', () => {
        activeMapId = map.id;
        mode = 'study';
        resetRebuild();
        render();
        $('ma-active')?.scrollIntoView({behavior:'smooth', block:'start'});
      });
      host.appendChild(button);
    });
  }

  function renderStudy(map, mastery) {
    const host = $('ma-sequence');
    const edges = $('ma-connections');
    if (!host || !edges) return;
    host.replaceChildren();
    map.nodes.forEach((node, index) => {
      const article = document.createElement('article');
      article.className = 'memory-atlas-node';
      const step = document.createElement('span');
      step.className = 'memory-atlas-node__index';
      step.textContent = String(index + 1).padStart(2, '0');
      const h3 = document.createElement('h3');
      h3.textContent = node.label;
      const owner = document.createElement('span');
      owner.className = 'memory-atlas-node__owner';
      owner.textContent = node.owner;
      const cue = document.createElement('p');
      cue.textContent = node.cue;
      const state = document.createElement('span');
      state.className = 'memory-atlas-node__state';
      state.textContent = stateLabel(node.skill_id, mastery);
      const link = document.createElement('a');
      link.href = node.source;
      link.textContent = 'Open source';
      article.append(step, h3, owner, cue, state, link);
      host.appendChild(article);
    });

    edges.replaceChildren();
    map.edges.forEach(edge => {
      const from = map.nodes.find(node => node.id === edge.from)?.label || edge.from;
      const to = map.nodes.find(node => node.id === edge.to)?.label || edge.to;
      const article = document.createElement('article');
      article.className = 'memory-atlas-edge';
      const type = document.createElement('span');
      const strong = document.createElement('strong');
      const small = document.createElement('small');
      type.textContent = edge.type.replaceAll('_', ' ');
      strong.textContent = `${from} → ${to}`;
      small.textContent = edge.label;
      article.append(type, strong, small);
      edges.appendChild(article);
    });
  }

  function addPlaced(id) {
    const map = activeMap();
    if (!map || placed.includes(id) || placed.length >= map.nodes.length) return;
    placed.push(id);
    checked = false;
    lastResult = null;
    renderRebuild(map);
  }

  function removePlaced(index) {
    placed.splice(index, 1);
    checked = false;
    lastResult = null;
    renderRebuild(activeMap());
  }

  function renderRebuild(map) {
    if (!map) return;
    const bank = $('ma-bank');
    const sequence = $('ma-rebuild');
    const result = $('ma-result');
    if (!bank || !sequence || !result) return;
    const nodeById = Object.fromEntries(map.nodes.map(node => [node.id, node]));

    bank.replaceChildren();
    bankOrder.forEach(id => {
      const node = nodeById[id];
      const button = document.createElement('button');
      button.type = 'button';
      button.disabled = placed.includes(id);
      button.textContent = node.label;
      button.addEventListener('click', () => addPlaced(id));
      bank.appendChild(button);
    });

    sequence.replaceChildren();
    map.nodes.forEach((_, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'memory-atlas-slot';
      if (index < placed.length) {
        const node = nodeById[placed[index]];
        const strong = document.createElement('strong');
        const small = document.createElement('small');
        strong.textContent = node.label;
        small.textContent = `Position ${index + 1}`;
        button.append(strong, small);
        button.addEventListener('click', () => removePlaced(index));
        if (checked) button.classList.add(placed[index] === map.nodes[index].id ? 'is-correct' : 'is-wrong');
      } else {
        button.disabled = true;
        button.setAttribute('aria-label', `Empty position ${index + 1}`);
      }
      sequence.appendChild(button);
    });

    if (!lastResult) {
      result.hidden = true;
      result.replaceChildren();
      return;
    }
    result.hidden = false;
    result.replaceChildren();
    const strong = document.createElement('strong');
    const p = document.createElement('p');
    const hint = document.createElement('p');
    strong.textContent = `${lastResult.correct}/${lastResult.total} positions correct · ${Math.round(lastResult.accuracy * 100)}%`;
    p.textContent = lastResult.accuracy >= passAccuracy ? 'Exact rebuild proven. Now explain the ownership hand-offs without looking at the map.' : `First mismatch: position ${lastResult.firstMismatch + 1}. Return to the source and explain why that state must come before the next one.`;
    hint.textContent = `Lead challenge: ${map.lead_prompt}`;
    result.append(strong, p, hint);
  }

  function checkRebuild() {
    const map = activeMap();
    if (!map || placed.length !== map.nodes.length) {
      const result = $('ma-result');
      if (result) {
        result.hidden = false;
        result.textContent = `Place all ${map?.nodes.length || 0} nodes before checking.`;
      }
      return;
    }
    const expected = map.nodes.map(node => node.id);
    const correct = placed.reduce((count, id, index) => count + (id === expected[index] ? 1 : 0), 0);
    const firstMismatch = placed.findIndex((id, index) => id !== expected[index]);
    const accuracy = correct / expected.length;
    lastResult = {correct, total:expected.length, accuracy, firstMismatch:firstMismatch < 0 ? 0 : firstMismatch};
    checked = true;
    saveRun({map_id:map.id, reviewed_at:new Date().toISOString(), correct, total:expected.length, accuracy});
    render();
  }

  function setMode(next) {
    mode = next;
    if (mode === 'rebuild' && !bankOrder.length) resetRebuild();
    render();
  }

  function render() {
    const map = activeMap();
    if (!map) return;
    const runs = atlasRuns();
    const mastery = masteryRows();
    renderChooser(runs);
    renderMetrics(runs);
    $('ma-kicker').textContent = `${map.label} / ${map.title}`;
    $('ma-title').textContent = map.title;
    $('ma-statement').textContent = map.statement;
    $('ma-boundary-prompt').textContent = map.boundary_prompt;
    $('ma-lead-prompt').textContent = map.lead_prompt;
    $('ma-study-mode').setAttribute('aria-pressed', mode === 'study' ? 'true' : 'false');
    $('ma-rebuild-mode').setAttribute('aria-pressed', mode === 'rebuild' ? 'true' : 'false');
    $('ma-study-panel').hidden = mode !== 'study';
    $('ma-rebuild-panel').hidden = mode !== 'rebuild';
    renderStudy(map, mastery);
    renderRebuild(map);
  }

  $('ma-study-mode')?.addEventListener('click', () => setMode('study'));
  $('ma-rebuild-mode')?.addEventListener('click', () => setMode('rebuild'));
  $('ma-check')?.addEventListener('click', checkRebuild);
  $('ma-reset')?.addEventListener('click', () => { resetRebuild(); render(); });

  resetRebuild();
  render();
})();
