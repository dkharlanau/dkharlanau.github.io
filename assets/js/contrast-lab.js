(() => {
  'use strict';

  const dataNode = document.getElementById('contrast-data');
  if (!dataNode) return;

  let DATA;
  try {
    DATA = JSON.parse(dataNode.textContent);
  } catch (error) {
    console.error('Contrast data could not be parsed.', error);
    return;
  }

  const contract = DATA.contract || {};
  const pairs = Array.isArray(DATA.pairs) ? DATA.pairs : [];
  const STORAGE_KEY = contract.storage_key || 'sapLeadContrastHistoryV1';
  const DEFAULT_CONFIDENCE = Number(contract.confidence_default ?? 50);
  const REPEAT_GAP = Number(contract.pair_repeat_gap ?? 2);
  const $ = id => document.getElementById(id);
  let current = null;
  let answered = false;

  function validAttempt(row) {
    return Boolean(
      row && typeof row === 'object' &&
      typeof row.pair_id === 'string' &&
      typeof row.item_id === 'string' &&
      (row.choice === 'left' || row.choice === 'right') &&
      typeof row.correct === 'boolean' &&
      Number.isInteger(row.confidence) && row.confidence >= 0 && row.confidence <= 100 &&
      typeof row.reviewed_at === 'string' && !Number.isNaN(Date.parse(row.reviewed_at))
    );
  }

  function history() {
    try {
      const rows = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
      return Array.isArray(rows) ? rows.filter(validAttempt) : [];
    } catch (_) {
      return [];
    }
  }

  function saveHistory(rows) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(rows.filter(validAttempt)));
  }

  function flatItems() {
    return pairs.flatMap(pair => (pair.items || []).map(item => ({pair, item})));
  }

  function rowsForPair(pairId, rows) {
    return rows.filter(row => row.pair_id === pairId);
  }

  function pairAccuracy(pairId, rows) {
    const attempts = rowsForPair(pairId, rows);
    if (!attempts.length) return null;
    return attempts.filter(row => row.correct).length / attempts.length;
  }

  function itemAttempts(pairId, itemId, rows) {
    return rows.filter(row => row.pair_id === pairId && row.item_id === itemId);
  }

  function lastReviewed(pairId, itemId, rows) {
    const attempts = itemAttempts(pairId, itemId, rows);
    if (!attempts.length) return 0;
    return Math.max(...attempts.map(row => Date.parse(row.reviewed_at)));
  }

  function recentPairIds(rows) {
    return rows.slice(-Math.max(REPEAT_GAP, 0)).map(row => row.pair_id);
  }

  function selectNext(rows = history()) {
    const items = flatItems();
    if (!items.length) return null;
    const recent = new Set(recentPairIds(rows));
    const unseen = items.filter(entry => itemAttempts(entry.pair.id, entry.item.id, rows).length === 0);
    const pool = unseen.length ? unseen : items;
    const nonRecent = pool.filter(entry => !recent.has(entry.pair.id));
    const candidates = nonRecent.length ? nonRecent : pool;

    return candidates.slice().sort((a, b) => {
      const aa = pairAccuracy(a.pair.id, rows);
      const ab = pairAccuracy(b.pair.id, rows);
      const scoreA = aa == null ? -1 : aa;
      const scoreB = ab == null ? -1 : ab;
      if (scoreA !== scoreB) return scoreA - scoreB;
      const countA = rowsForPair(a.pair.id, rows).length;
      const countB = rowsForPair(b.pair.id, rows).length;
      if (countA !== countB) return countA - countB;
      const lastA = lastReviewed(a.pair.id, a.item.id, rows);
      const lastB = lastReviewed(b.pair.id, b.item.id, rows);
      if (lastA !== lastB) return lastA - lastB;
      return a.item.id.localeCompare(b.item.id);
    })[0];
  }

  function calibrationGap(row) {
    const target = row.correct ? 100 : 0;
    return Math.abs(row.confidence - target);
  }

  function averageCalibration(rows) {
    if (!rows.length) return null;
    return Math.round(rows.reduce((sum, row) => sum + calibrationGap(row), 0) / rows.length);
  }

  function createMetric(value, label) {
    const article = document.createElement('article');
    const strong = document.createElement('strong');
    const span = document.createElement('span');
    strong.textContent = String(value);
    span.textContent = label;
    article.append(strong, span);
    return article;
  }

  function renderMetrics(rows) {
    const host = $('ct-metrics');
    if (!host) return;
    const correct = rows.filter(row => row.correct).length;
    const accuracy = rows.length ? Math.round(correct / rows.length * 100) : 0;
    const calibration = averageCalibration(rows);
    const seenPairs = new Set(rows.map(row => row.pair_id)).size;
    host.replaceChildren(
      createMetric(rows.length, 'Classifications'),
      createMetric(`${accuracy}%`, 'Accuracy'),
      createMetric(calibration == null ? '—' : `${calibration} pp`, 'Calibration gap'),
      createMetric(`${seenPairs} / ${pairs.length}`, 'Pairs practised')
    );
  }

  function renderPairSummary(rows) {
    const host = $('ct-pair-summary');
    if (!host) return;
    host.replaceChildren();
    pairs.forEach(pair => {
      const attempts = rowsForPair(pair.id, rows);
      const accuracy = pairAccuracy(pair.id, rows);
      const article = document.createElement('article');
      const strong = document.createElement('strong');
      const span = document.createElement('span');
      const small = document.createElement('small');
      strong.textContent = accuracy == null ? '—' : `${Math.round(accuracy * 100)}%`;
      span.textContent = pair.title;
      small.textContent = attempts.length ? `${attempts.length} classifications` : 'Not tested yet';
      article.append(strong, span, small);
      host.appendChild(article);
    });
  }

  function choiceButton(side, model) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'contrast-choice';
    button.dataset.choice = side;
    const strong = document.createElement('strong');
    const small = document.createElement('small');
    strong.textContent = model.label;
    small.textContent = model.skill_id;
    button.append(strong, small);
    button.addEventListener('click', () => answer(side));
    return button;
  }

  function resetConfidence() {
    const slider = $('ct-confidence');
    if (!slider) return;
    slider.value = String(DEFAULT_CONFIDENCE);
    slider.disabled = false;
    $('ct-confidence-value').textContent = `${DEFAULT_CONFIDENCE}%`;
  }

  function renderCurrent(rows = history()) {
    current = selectNext(rows);
    answered = false;
    const card = $('ct-card');
    if (!current || !card) {
      if (card) card.hidden = true;
      return;
    }
    const {pair, item} = current;
    card.hidden = false;
    $('ct-title').textContent = pair.title;
    $('ct-meta').textContent = `${pair.left.label} vs ${pair.right.label} · ${item.id}`;
    $('ct-prompt').textContent = item.prompt;
    resetConfidence();
    $('ct-feedback').hidden = true;
    const choices = $('ct-choices');
    choices.replaceChildren(choiceButton('left', pair.left), choiceButton('right', pair.right));
  }

  function recordChoice(choice, correct, confidence) {
    const rows = history();
    rows.push({
      pair_id: current.pair.id,
      item_id: current.item.id,
      choice,
      correct,
      confidence,
      reviewed_at: new Date().toISOString()
    });
    saveHistory(rows);
    return rows;
  }

  function sourceLink(model) {
    const anchor = document.createElement('a');
    anchor.href = model.source;
    anchor.textContent = `${model.label} source`;
    return anchor;
  }

  function answer(choice) {
    if (!current || answered) return;
    answered = true;
    const confidence = Number($('ct-confidence')?.value || DEFAULT_CONFIDENCE);
    const correct = choice === current.item.answer;
    const rows = recordChoice(choice, correct, confidence);
    $('ct-confidence').disabled = true;
    $('ct-choices').querySelectorAll('button').forEach(button => { button.disabled = true; });

    $('ct-feedback').hidden = false;
    $('ct-result-label').textContent = correct ? 'Correct boundary' : 'Boundary miss';
    $('ct-result-title').textContent = correct ? 'The leading model is correct.' : `The leading model should be ${current.item.answer === 'left' ? current.pair.left.label : current.pair.right.label}.`;
    $('ct-explanation').textContent = current.item.explanation;
    $('ct-discriminator').textContent = current.pair.discriminator;
    $('ct-failure').textContent = current.pair.failure_if_confused;
    $('ct-sources').replaceChildren(sourceLink(current.pair.left), sourceLink(current.pair.right));
    renderMetrics(rows);
    renderPairSummary(rows);
    $('ct-feedback').scrollIntoView({behavior:'smooth', block:'nearest'});
  }

  $('ct-confidence')?.addEventListener('input', event => {
    $('ct-confidence-value').textContent = `${event.target.value}%`;
  });

  $('ct-next')?.addEventListener('click', () => {
    renderCurrent();
    $('contrast-session')?.scrollIntoView({behavior:'smooth', block:'start'});
  });

  const rows = history();
  renderMetrics(rows);
  renderPairSummary(rows);
  renderCurrent(rows);
})();