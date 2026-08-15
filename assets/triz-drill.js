(() => {
  const root = document.querySelector('[data-triz-drill]');
  if (!root) return;

  const domainSelect = root.querySelector('[data-drill-domain]');
  const difficultySelect = root.querySelector('[data-drill-difficulty]');
  const newCaseButton = root.querySelector('[data-drill-new]');
  const caseTitle = root.querySelector('[data-drill-title]');
  const casePrompt = root.querySelector('[data-drill-prompt]');
  const caseMeta = root.querySelector('[data-drill-meta]');
  const pressureBox = root.querySelector('[data-drill-pressure]');
  const pressureList = root.querySelector('[data-drill-pressure-list]');
  const pressureButton = root.querySelector('[data-drill-pressure-button]');
  const answer = root.querySelector('[data-drill-answer]');
  const answerCount = root.querySelector('[data-drill-count]');
  const timerNode = root.querySelector('[data-drill-timer]');
  const timerStart = root.querySelector('[data-drill-timer-start]');
  const timerReset = root.querySelector('[data-drill-timer-reset]');
  const revealButton = root.querySelector('[data-drill-reveal]');
  const debrief = root.querySelector('[data-drill-debrief]');
  const debriefGrid = root.querySelector('[data-drill-debrief-grid]');
  const rubricSection = root.querySelector('[data-drill-rubric]');
  const rubricGrid = root.querySelector('[data-drill-rubric-grid]');
  const scoreValue = root.querySelector('[data-drill-score]');
  const scoreBand = root.querySelector('[data-drill-band]');
  const scoreCopy = root.querySelector('[data-drill-band-copy]');
  const payloadNode = root.querySelector('[data-drill-payload]');
  const copyPayload = root.querySelector('[data-drill-copy-payload]');
  const status = root.querySelector('[data-drill-status]');

  let cases = [];
  let rubric = null;
  let currentCase = null;
  let timerId = null;
  let secondsLeft = 90;

  const domainLabels = {
    sales: 'Sales',
    procurement: 'Procurement',
    logistics: 'Logistics',
    integration: 'Integration',
    master_data: 'Master Data',
    ai: 'AI / Agents'
  };

  const operatorLabels = {
    O1_time: 'O1 · Time',
    O2_condition: 'O2 · Condition',
    O3_context: 'O3 · Context',
    O4_system_level: 'O4 · System level',
    O5_authority: 'O5 · Authority',
    O6_representation: 'O6 · Representation'
  };

  const escapeHtml = (value) => String(value ?? '').replace(/[&<>"']/g, (char) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;'
  }[char]));

  const listHtml = (items) => `<ul>${(items || []).map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ul>`;

  function setStatus(message) {
    if (status) status.textContent = message;
  }

  async function loadData() {
    try {
      const [caseResponse, rubricResponse] = await Promise.all([
        fetch('/datasets/triz-digital-framework/drill-cases.json', { credentials: 'same-origin' }),
        fetch('/datasets/triz-digital-framework/lead-rubric.json', { credentials: 'same-origin' })
      ]);
      if (!caseResponse.ok || !rubricResponse.ok) throw new Error('Assessment data unavailable');
      const caseData = await caseResponse.json();
      rubric = await rubricResponse.json();
      cases = caseData.cases || [];
      renderRubric();
      chooseCase();
      setStatus(`${cases.length} synthetic cases loaded. No answer data is sent to the site.`);
    } catch (error) {
      setStatus('Assessment data could not be loaded. Reload the page after the site build is available.');
      newCaseButton.disabled = true;
    }
  }

  function filteredCases() {
    const domain = domainSelect.value;
    const difficulty = difficultySelect.value;
    return cases.filter((item) => (!domain || item.domain === domain) && (!difficulty || item.difficulty === difficulty));
  }

  function chooseCase() {
    const pool = filteredCases();
    if (!pool.length) {
      currentCase = null;
      caseTitle.textContent = 'No case matches the filters';
      casePrompt.textContent = 'Change the domain or difficulty filter.';
      caseMeta.innerHTML = '';
      return;
    }
    const alternatives = currentCase && pool.length > 1 ? pool.filter((item) => item.id !== currentCase.id) : pool;
    currentCase = alternatives[Math.floor(Math.random() * alternatives.length)];
    renderCase();
    resetAttempt();
  }

  function renderCase() {
    caseTitle.textContent = currentCase.title;
    casePrompt.textContent = currentCase.prompt;
    caseMeta.innerHTML = `
      <span class="triz-drill__tag">${escapeHtml(domainLabels[currentCase.domain] || currentCase.domain)}</span>
      <span class="triz-drill__tag">${escapeHtml(currentCase.difficulty)}</span>
      <span class="triz-drill__tag">${escapeHtml(currentCase.contradiction.type.replaceAll('_', ' '))}</span>
    `;
    pressureList.innerHTML = listHtml(currentCase.pressure);
    pressureBox.hidden = true;
    pressureButton.textContent = 'Show interviewer pressure';
  }

  function resetAttempt() {
    stopTimer();
    secondsLeft = 90;
    renderTimer();
    answer.value = '';
    answerCount.textContent = '0 characters';
    debrief.hidden = true;
    rubricSection.hidden = true;
    payloadNode.textContent = '';
    if (rubricGrid) rubricGrid.querySelectorAll('select').forEach((select) => { select.value = '0'; });
    updateScore();
  }

  function renderTimer() {
    const minutes = Math.floor(secondsLeft / 60);
    const seconds = String(secondsLeft % 60).padStart(2, '0');
    timerNode.textContent = `${minutes}:${seconds}`;
    timerNode.setAttribute('aria-label', `${secondsLeft} seconds remaining`);
  }

  function startTimer() {
    if (timerId) return;
    if (secondsLeft <= 0) secondsLeft = 90;
    timerId = window.setInterval(() => {
      secondsLeft -= 1;
      renderTimer();
      if (secondsLeft <= 0) {
        stopTimer();
        timerNode.textContent = '0:00';
        setStatus('Time. Finish the sentence, then reveal the debrief.');
      }
    }, 1000);
  }

  function stopTimer() {
    if (timerId) window.clearInterval(timerId);
    timerId = null;
  }

  function resetTimer() {
    stopTimer();
    secondsLeft = 90;
    renderTimer();
  }

  function togglePressure() {
    pressureBox.hidden = !pressureBox.hidden;
    pressureButton.textContent = pressureBox.hidden ? 'Show interviewer pressure' : 'Hide interviewer pressure';
  }

  function renderDebrief() {
    if (!currentCase) return;
    stopTimer();
    const c = currentCase;
    const shapeItems = [
      ['A · Simplify', c.system_shapes.simplify],
      ['B · Deterministic', c.system_shapes.deterministic],
      ['C · Uncertainty-assisted', c.system_shapes.uncertainty_assisted]
    ];
    debriefGrid.innerHTML = `
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">Useful function</p>
        <h3>Protect the outcome.</h3>
        <p>${escapeHtml(c.useful_function)}</p>
      </article>
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">Contradiction</p>
        <h3>${escapeHtml(c.contradiction.type.replaceAll('_', ' '))}</h3>
        <p>Improve <strong>${escapeHtml(c.contradiction.improve)}</strong> while preserving <strong>${escapeHtml(c.contradiction.preserve)}</strong>.</p>
      </article>
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">Separation</p>
        <h3>Operators worth testing</h3>
        ${listHtml(c.operators.map((id) => operatorLabels[id] || id))}
      </article>
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">Evidence</p>
        <h3>Ask before recommending.</h3>
        ${listHtml(c.evidence)}
      </article>
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">System shapes</p>
        <h3>Create design distance.</h3>
        <div class="triz-drill__shape-list">${shapeItems.map(([name, text]) => `<div class="triz-drill__shape"><strong>${escapeHtml(name)}</strong><p>${escapeHtml(text)}</p></div>`).join('')}</div>
      </article>
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">Authority</p>
        <h3>Who may change state?</h3>
        <p>${escapeHtml(c.authority)}</p>
      </article>
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">Experiment</p>
        <h3>Measure both sides.</h3>
        <p><strong>Primary:</strong> ${escapeHtml(c.experiment.primary)}</p>
        <p><strong>Counter:</strong> ${escapeHtml(c.experiment.counter)}</p>
        <p><strong>Scope:</strong> ${escapeHtml(c.experiment.scope)}</p>
      </article>
      <article class="triz-drill__debrief-card">
        <p class="triz-drill__eyebrow">Lead signals</p>
        <h3>What a strong answer shows</h3>
        ${listHtml(c.lead_signals)}
        <p><strong>Watch:</strong></p>
        ${listHtml(c.red_flags)}
      </article>
    `;
    debrief.hidden = false;
    rubricSection.hidden = false;
    updatePayload();
    debrief.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function renderRubric() {
    if (!rubric) return;
    rubricGrid.innerHTML = rubric.dimensions.map((dimension) => `
      <div class="triz-drill__rubric-row" data-rubric-row="${escapeHtml(dimension.id)}">
        <h3>${escapeHtml(dimension.name)}</h3>
        <p data-rubric-anchor>${escapeHtml(dimension.anchors['0'])}</p>
        <div class="triz-drill__field">
          <label for="rubric-${escapeHtml(dimension.id)}">Score</label>
          <select id="rubric-${escapeHtml(dimension.id)}" data-rubric-score="${escapeHtml(dimension.id)}">
            ${[0,1,2,3,4].map((score) => `<option value="${score}">${score} / 4</option>`).join('')}
          </select>
        </div>
      </div>
    `).join('');

    rubricGrid.querySelectorAll('[data-rubric-score]').forEach((select) => {
      select.addEventListener('change', () => {
        const dimension = rubric.dimensions.find((item) => item.id === select.dataset.rubricScore);
        const row = select.closest('[data-rubric-row]');
        row.querySelector('[data-rubric-anchor]').textContent = dimension.anchors[select.value];
        updateScore();
        updatePayload();
      });
    });
  }

  function selfScores() {
    if (!rubricGrid) return {};
    return Object.fromEntries([...rubricGrid.querySelectorAll('[data-rubric-score]')].map((select) => [select.dataset.rubricScore, Number(select.value)]));
  }

  function updateScore() {
    if (!rubric) return;
    const scores = selfScores();
    const total = Object.values(scores).reduce((sum, value) => sum + value, 0);
    const band = rubric.bands.find((item) => total >= item.min && total <= item.max) || rubric.bands[0];
    scoreValue.textContent = `${total}/${rubric.max_score}`;
    scoreBand.textContent = band.name;
    scoreCopy.textContent = band.interpretation;
  }

  function buildPayload() {
    if (!currentCase || !rubric) return null;
    return {
      task: 'Evaluate this SAP Lead assessment answer against the supplied rubric. Do not reward keyword matching. Judge the reasoning, ownership, trade-offs, evidence and communication. Separate missing evidence from wrong reasoning.',
      case_id: currentCase.id,
      case: currentCase,
      candidate_answer: answer.value.trim(),
      rubric_id: rubric.rubric_id,
      rubric,
      candidate_self_score: selfScores(),
      required_output: {
        total_score: `0-${rubric.max_score}`,
        dimension_scores: 'score and short evidence for every rubric dimension',
        strongest_signal: 'one concrete Lead-level strength',
        biggest_gap: 'one concrete gap limiting the answer',
        improved_60_90_second_answer: 'rewrite in concise B2 English without inventing system facts',
        follow_up_questions: 'two interviewer follow-ups based on missing evidence or weak trade-offs'
      }
    };
  }

  function updatePayload() {
    const payload = buildPayload();
    if (payload) payloadNode.textContent = JSON.stringify(payload, null, 2);
  }

  async function copyEvaluationPayload() {
    const payload = buildPayload();
    if (!payload) return;
    try {
      await navigator.clipboard.writeText(JSON.stringify(payload, null, 2));
      copyPayload.textContent = 'Copied';
      window.setTimeout(() => { copyPayload.textContent = 'Copy agent evaluation payload'; }, 1400);
    } catch (error) {
      payloadNode.focus();
      setStatus('Clipboard access is unavailable. The evaluation payload is visible below for manual copy.');
    }
  }

  domainSelect.addEventListener('change', chooseCase);
  difficultySelect.addEventListener('change', chooseCase);
  newCaseButton.addEventListener('click', chooseCase);
  pressureButton.addEventListener('click', togglePressure);
  timerStart.addEventListener('click', startTimer);
  timerReset.addEventListener('click', resetTimer);
  revealButton.addEventListener('click', renderDebrief);
  copyPayload.addEventListener('click', copyEvaluationPayload);
  answer.addEventListener('input', () => {
    answerCount.textContent = `${answer.value.length} characters`;
    updatePayload();
  });

  loadData();
})();
