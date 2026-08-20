(() => {
  'use strict';

  const node = document.getElementById('mastery-data');
  if (!node) return;

  let DATA;
  try {
    DATA = JSON.parse(node.textContent);
  } catch (error) {
    console.error('Mastery data could not be parsed.', error);
    return;
  }

  const contract = DATA.contract || {};
  const cards = Array.isArray(DATA.cards) ? DATA.cards : [];
  const STORAGE_KEY = contract.storage_key || 'sapLeadMasteryHistoryV1';
  const PASS_SCORE = Number(contract.pass_score ?? 2);
  const SESSION_SIZE = Number(contract.session_size ?? 5);
  const REVIEW_INTERVALS = Array.isArray(contract.review_intervals_days) ? contract.review_intervals_days.map(Number) : [1, 3, 7, 14, 30];
  const RETAINED_SUCCESSES = Number(contract.retained_successes ?? 3);
  const RETAINED_SPAN_DAYS = Number(contract.retained_span_days ?? 7);
  const MODES = new Set(['recall', 'connect', 'apply', 'defend', 'review']);
  const TRACK_LABELS = {sales:'Sales', logistics:'Procurement & Logistics', integration:'Integration & Architecture', ai:'AI & Data'};
  const MODE_LABELS = {recall:'Recall', connect:'Connect', apply:'Apply', defend:'Defend', review:'Retain'};
  const STATE_LABELS = Object.fromEntries((contract.states || []).map(item => [item.id, item.label]));
  const DAY = 86400000;
  const $ = id => document.getElementById(id);
  let currentSkillId = null;

  function validAttempt(row) {
    return row && typeof row === 'object' && typeof row.skill_id === 'string' && MODES.has(row.mode) && Number.isInteger(row.score) && row.score >= 0 && row.score <= 3 && typeof row.reviewed_at === 'string' && !Number.isNaN(Date.parse(row.reviewed_at));
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

  function rowsFor(skillId, rows = history()) {
    return rows.filter(row => row.skill_id === skillId).sort((a, b) => Date.parse(a.reviewed_at) - Date.parse(b.reviewed_at));
  }

  function spanDays(rows) {
    if (rows.length < 2) return 0;
    return (Date.parse(rows[rows.length - 1].reviewed_at) - Date.parse(rows[0].reviewed_at)) / DAY;
  }

  function stateFor(card, rows = history()) {
    const attempts = rowsFor(card.skill_id, rows);
    if (!attempts.length) return 'new';
    const passed = new Set(attempts.filter(row => row.score >= PASS_SCORE).map(row => row.mode));
    const advanced = attempts.filter(row => row.score >= PASS_SCORE && (row.mode === 'defend' || row.mode === 'review'));
    if (passed.has('defend') && advanced.length >= RETAINED_SUCCESSES && spanDays(advanced) >= RETAINED_SPAN_DAYS) return 'retained';
    if (passed.has('defend')) return 'defended';
    if (passed.has('apply')) return 'applied';
    if (passed.has('connect')) return 'connected';
    if (passed.has('recall')) return 'recalled';
    return 'new';
  }

  function lastAttempt(card, rows = history()) {
    const attempts = rowsFor(card.skill_id, rows);
    return attempts.length ? attempts[attempts.length - 1] : null;
  }

  function dueAt(card, rows = history()) {
    const attempts = rowsFor(card.skill_id, rows);
    if (!attempts.length) return null;
    const last = attempts[attempts.length - 1];
    if (last.score < PASS_SCORE) return new Date(0);
    let streak = 0;
    for (let i = attempts.length - 1; i >= 0; i -= 1) {
      if (attempts[i].score < PASS_SCORE) break;
      streak += 1;
    }
    const interval = REVIEW_INTERVALS[Math.min(Math.max(streak - 1, 0), REVIEW_INTERVALS.length - 1)] || 1;
    return new Date(Date.parse(last.reviewed_at) + interval * DAY);
  }

  function isDue(card, rows = history(), now = Date.now()) {
    const due = dueAt(card, rows);
    return Boolean(due && due.getTime() <= now);
  }

  function priority(card, rows, now) {
    const last = lastAttempt(card, rows);
    if (isDue(card, rows, now)) return 0;
    if (last && last.score < PASS_SCORE) return 1;
    if (!last) return 2;
    return 3;
  }

  function selectSession(rows = history()) {
    const now = Date.now();
    const ranked = cards.slice().sort((a, b) => {
      const pa = priority(a, rows, now);
      const pb = priority(b, rows, now);
      if (pa !== pb) return pa - pb;
      const da = dueAt(a, rows)?.getTime() ?? Number.MAX_SAFE_INTEGER;
      const db = dueAt(b, rows)?.getTime() ?? Number.MAX_SAFE_INTEGER;
      if (da !== db) return da - db;
      return a.skill_id.localeCompare(b.skill_id);
    });

    const selected = [];
    const selectedIds = new Set();
    const tracks = new Set();

    ranked.filter(card => priority(card, rows, now) <= 1).forEach(card => {
      if (selected.length >= SESSION_SIZE) return;
      selected.push(card);
      selectedIds.add(card.skill_id);
      tracks.add(card.track);
    });

    ranked.forEach(card => {
      if (selected.length >= SESSION_SIZE || selectedIds.has(card.skill_id) || tracks.has(card.track)) return;
      selected.push(card);
      selectedIds.add(card.skill_id);
      tracks.add(card.track);
    });

    ranked.forEach(card => {
      if (selected.length >= SESSION_SIZE || selectedIds.has(card.skill_id)) return;
      selected.push(card);
      selectedIds.add(card.skill_id);
    });
    return selected;
  }

  function modeFor(card, rows = history()) {
    const last = lastAttempt(card, rows);
    if (last && last.score < PASS_SCORE) return last.mode === 'review' ? 'recall' : last.mode;
    const state = stateFor(card, rows);
    if (state === 'new') return 'recall';
    if (state === 'recalled') return 'connect';
    if (state === 'connected') return 'apply';
    if (state === 'applied') return 'defend';
    return 'review';
  }

  function promptFor(card, mode) {
    if (mode === 'recall') return 'Without notes, rebuild the Five-Link model: trigger, flow, objects and rules, failure boundary, and Lead decision.';
    if (mode === 'connect') return card.connect_prompt;
    if (mode === 'apply') return card.apply_prompt;
    if (mode === 'defend') return card.defend_prompt;
    return 'Cold review: explain the Five-Link model in about 90 seconds, then add one failure boundary and one Lead decision without opening the source.';
  }

  function formatDue(card, rows = history()) {
    const due = dueAt(card, rows);
    if (!due) return 'new';
    const delta = Math.ceil((due.getTime() - Date.now()) / DAY);
    if (delta <= 0) return 'due now';
    if (delta === 1) return 'due tomorrow';
    return `due in ${delta} days`;
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
    const metrics = $('mt-metrics');
    if (!metrics) return;
    const states = cards.map(card => stateFor(card, rows));
    metrics.replaceChildren(
      createMetric(rows.length, 'Scored retrievals'),
      createMetric(cards.filter(card => isDue(card, rows)).length, 'Due reviews'),
      createMetric(states.filter(state => state === 'retained').length, 'Retained skills'),
      createMetric(states.filter(state => state !== 'new').length, `Covered of ${cards.length}`)
    );
  }

  function renderStateStrip(rows) {
    const strip = $('mt-state-strip');
    if (!strip) return;
    strip.replaceChildren();
    (contract.states || []).forEach(item => {
      const count = cards.filter(card => stateFor(card, rows) === item.id).length;
      const card = document.createElement('article');
      const strong = document.createElement('strong');
      const span = document.createElement('span');
      const small = document.createElement('small');
      strong.textContent = String(count);
      span.textContent = item.label;
      small.textContent = item.evidence;
      card.append(strong, span, small);
      strip.appendChild(card);
    });
  }

  function renderSession(rows) {
    const host = $('mt-session');
    if (!host) return [];
    const session = selectSession(rows);
    host.replaceChildren();
    session.forEach((card, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'mastery-session-item';
      button.dataset.skillId = card.skill_id;
      button.setAttribute('aria-pressed', currentSkillId === card.skill_id ? 'true' : 'false');

      const number = document.createElement('span');
      number.textContent = String(index + 1).padStart(2, '0');
      const copy = document.createElement('div');
      const strong = document.createElement('strong');
      const small = document.createElement('small');
      strong.textContent = card.title;
      small.textContent = `${TRACK_LABELS[card.track] || card.track} · ${MODE_LABELS[modeFor(card, rows)]} · ${formatDue(card, rows)}`;
      copy.append(strong, small);
      button.append(number, copy);
      button.addEventListener('click', () => {
        currentSkillId = card.skill_id;
        render(rows);
        $('practice')?.scrollIntoView({behavior:'smooth', block:'start'});
      });
      host.appendChild(button);
    });
    return session;
  }

  function addLinkRow(host, label, value) {
    const article = document.createElement('article');
    const kicker = document.createElement('p');
    const p = document.createElement('p');
    kicker.className = 'ir-kicker';
    kicker.textContent = label;
    p.textContent = value;
    article.append(kicker, p);
    host.appendChild(article);
  }

  function renderPractice(rows, session) {
    const card = cards.find(item => item.skill_id === currentSkillId) || session[0];
    const panel = $('mt-card');
    if (!card || !panel) {
      if (panel) panel.hidden = true;
      return;
    }
    currentSkillId = card.skill_id;
    const mode = modeFor(card, rows);
    const state = stateFor(card, rows);
    panel.hidden = false;
    $('mt-title').textContent = card.title;
    $('mt-meta').textContent = `${TRACK_LABELS[card.track] || card.track} · ${MODE_LABELS[mode]} · ${formatDue(card, rows)}`;
    $('mt-track').textContent = TRACK_LABELS[card.track] || card.track;
    $('mt-mode').textContent = MODE_LABELS[mode];
    $('mt-state').textContent = STATE_LABELS[state] || state;
    $('mt-prompt-title').textContent = mode === 'review' ? 'Delayed retrieval' : `${MODE_LABELS[mode]} task`;
    $('mt-prompt').textContent = promptFor(card, mode);
    $('mt-source').href = card.source;

    const reference = $('mt-reference');
    reference.hidden = true;
    $('mt-answer').value = '';
    const five = $('mt-five-link');
    five.replaceChildren();
    [
      ['01 / Trigger', card.trigger],
      ['02 / Flow', card.flow],
      ['03 / Objects & rules', card.objects_rules],
      ['04 / Failure boundary', card.failure_boundary],
      ['05 / Lead decision', card.lead_decision]
    ].forEach(([label, value]) => addLinkRow(five, label, value));

    const scores = $('mt-score-buttons');
    scores.replaceChildren();
    (contract.scores || []).forEach(score => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'mastery-score-button';
      const strong = document.createElement('strong');
      const small = document.createElement('small');
      strong.textContent = `${score.id} · ${score.label}`;
      small.textContent = score.meaning;
      button.append(strong, small);
      button.addEventListener('click', () => recordAttempt(card, mode, Number(score.id)));
      scores.appendChild(button);
    });
  }

  function recordAttempt(card, mode, score) {
    const rows = history();
    rows.push({
      id: typeof crypto !== 'undefined' && crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random().toString(16).slice(2)}`,
      skill_id: card.skill_id,
      track: card.track,
      mode,
      score,
      reviewed_at: new Date().toISOString()
    });
    saveHistory(rows);
    currentSkillId = null;
    render();
  }

  function renderProfile(rows) {
    const host = $('mt-profile');
    if (!host) return;
    const table = document.createElement('table');
    table.className = 'mastery-table';
    const thead = document.createElement('thead');
    const headRow = document.createElement('tr');
    ['Skill', 'Track', 'State', 'Last score', 'Review'].forEach(label => {
      const th = document.createElement('th');
      th.textContent = label;
      headRow.appendChild(th);
    });
    thead.appendChild(headRow);
    const tbody = document.createElement('tbody');
    cards.forEach(card => {
      const tr = document.createElement('tr');
      const last = lastAttempt(card, rows);
      [
        card.title,
        TRACK_LABELS[card.track] || card.track,
        STATE_LABELS[stateFor(card, rows)] || stateFor(card, rows),
        last ? `${last.score} / 3` : '—',
        formatDue(card, rows)
      ].forEach(value => {
        const td = document.createElement('td');
        td.textContent = value;
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
    table.append(thead, tbody);
    host.replaceChildren(table);
  }

  function render(rows = history()) {
    renderMetrics(rows);
    renderStateStrip(rows);
    const session = renderSession(rows);
    renderPractice(rows, session);
    renderProfile(rows);
  }

  $('mt-reveal')?.addEventListener('click', () => {
    const reference = $('mt-reference');
    reference.hidden = false;
    reference.scrollIntoView({behavior:'smooth', block:'nearest'});
  });

  $('mt-export')?.addEventListener('click', () => {
    const payload = {
      schema: 'dkharlanau.sap-lead-mastery-history',
      version: 1,
      exported_at: new Date().toISOString(),
      attempts: history()
    };
    const blob = new Blob([JSON.stringify(payload, null, 2) + '\n'], {type:'application/json'});
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = 'sap-lead-mastery-history.json';
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    URL.revokeObjectURL(url);
  });

  $('mt-clear')?.addEventListener('click', () => {
    if (!window.confirm('Clear all local mastery history in this browser?')) return;
    localStorage.removeItem(STORAGE_KEY);
    currentSkillId = null;
    render();
  });

  render();
})();
