import { cases } from './cases.mjs';
import { blankAnswer, evaluateCase, missingAnswers, parseQuantity } from './engine.mjs';

const $ = id => document.getElementById(id);
const states = new Map(cases.map(item => [item.id, { answer: blankAnswer(), opened: new Set(), result: null }]));
let active = cases[0];
const node = (tag, text, className) => {
  const element = document.createElement(tag);
  if (text != null) element.textContent = text;
  if (className) element.className = className;
  return element;
};
function snapshot() {
  const values = new FormData($('erp-answer-form'));
  const answer = Object.fromEntries(['quantity', 'cause', 'action', 'verification'].map(key => [key, String(values.get(key) || '')]));
  answer.citations = values.getAll('citations');
  answer.reasoning = $('erp-reasoning').value;
  answer.uncertainty = $('erp-uncertainty').value;
  states.get(active.id).answer = answer;
  return answer;
}
function renderNavigation() {
  const nav = $('erp-case-nav');
  nav.replaceChildren();
  cases.forEach((item, index) => {
    const button = node('button', null, 'erp-case-button');
    button.type = 'button';
    button.dataset.case = item.id;
    button.setAttribute('aria-pressed', String(item.id === active.id));
    button.append(node('span', `0${index + 1}`, 'erp-case-number'), node('strong', item.category));
    const state = states.get(item.id);
    button.append(node('small', state.result ? `${state.result.correct}/${state.result.total} checks matched` : 'Not checked'));
    button.addEventListener('click', () => switchCase(item));
    nav.append(button);
  });
}
function inspectionStatus() {
  $('erp-inspected').textContent = `${states.get(active.id).opened.size} of ${active.evidence.length} sources opened in this case.`;
}
function renderEvidence() {
  const root = $('erp-evidence');
  const caseId = active.id;
  const caseState = states.get(caseId);
  root.replaceChildren();
  for (const source of active.evidence) {
    const details = node('details', null, 'erp-evidence-card');
    details.open = states.get(active.id).opened.has(source.id);
    const summary = node('summary');
    summary.append(node('span', source.id, 'erp-evidence-id'), node('span', source.title));
    const content = node('div', null, 'erp-evidence-content');
    content.append(node('p', source.intro));
    const scroll = node('div', null, 'erp-table-scroll');
    scroll.tabIndex = 0;
    scroll.setAttribute('role', 'region');
    scroll.setAttribute('aria-label', `Evidence ${source.id}: ${source.title}. Scroll table horizontally if needed.`);
    const table = node('table');
    const caption = node('caption', `Evidence ${source.id} — ${source.title}`, 'erp-sr-only');
    const head = node('thead');
    const headings = node('tr');
    source.columns.forEach(label => { const th = node('th', label); th.scope = 'col'; headings.append(th); });
    head.append(headings);
    const body = node('tbody');
    source.rows.forEach(row => { const tr = node('tr'); row.forEach(value => tr.append(node('td', value))); body.append(tr); });
    table.append(caption, head, body);
    scroll.append(table);
    content.append(scroll);
    details.append(summary, content);
    details.addEventListener('toggle', () => {
      if (details.open) caseState.opened.add(source.id);
      if (active.id === caseId) inspectionStatus();
    });
    root.append(details);
  }
  inspectionStatus();
}
function choiceGroup(key, question, answer) {
  const group = node('fieldset', null, 'erp-question');
  group.append(node('legend', question.label));
  for (const [value, text] of question.options) {
    const label = node('label', null, 'erp-choice');
    const input = node('input');
    input.type = 'radio'; input.name = key; input.value = value; input.checked = answer[key] === value;
    label.append(input, node('span', text));
    group.append(label);
  }
  return group;
}
function renderQuestions() {
  const answer = states.get(active.id).answer;
  const root = $('erp-questions');
  root.replaceChildren();
  const label = node('label', null, 'erp-field');
  label.htmlFor = 'erp-quantity';
  label.append(node('span', active.calculation.label));
  const row = node('div', null, 'erp-quantity-row');
  const input = node('input');
  input.id = 'erp-quantity'; input.name = 'quantity'; input.type = 'text'; input.inputMode = 'decimal'; input.autocomplete = 'off'; input.maxLength = 30; input.value = answer.quantity;
  input.setAttribute('aria-describedby', 'erp-quantity-unit');
  const unit = node('span', active.calculation.suffix); unit.id = 'erp-quantity-unit';
  row.append(input, unit); label.append(row); root.append(label, choiceGroup('cause', active.cause, answer));
  const citations = node('fieldset', null, 'erp-question');
  citations.append(node('legend', 'Which sources support the complete diagnosis?'), node('p', 'Select every source needed to link the records to the failure rule.', 'erp-help'));
  active.evidence.forEach(source => {
    const item = node('label', null, 'erp-choice');
    const checkbox = node('input');
    checkbox.type = 'checkbox'; checkbox.name = 'citations'; checkbox.value = source.id; checkbox.checked = answer.citations.includes(source.id);
    item.append(checkbox, node('span', `${source.id} · ${source.title}`)); citations.append(item);
  });
  root.append(citations, choiceGroup('action', active.action, answer), choiceGroup('verification', active.verification, answer));
  $('erp-reasoning').value = answer.reasoning;
  $('erp-uncertainty').value = answer.uncertainty;
}
function renderResult() {
  const state = states.get(active.id);
  $('erp-result').hidden = !state.result;
  if (!state.result) return;
  const result = state.result;
  $('erp-result-title').textContent = result.complete ? 'All five checked conclusions match.' : `${result.correct} of ${result.total} checked conclusions match.`;
  $('erp-result-summary').textContent = result.complete ? 'Compare your explanation with the evidence chain below, then try another case.' : 'Use the explanations to find the unsupported step. You can revise your answer and check again.';
  const grid = $('erp-checks'); grid.replaceChildren();
  result.checks.forEach(check => {
    const card = node('article', null, `erp-check ${check.passed ? 'erp-check-pass' : ''}`);
    card.append(node('p', check.passed ? 'Matched' : 'Revisit', 'erp-check-status'), node('h3', check.title), node('p', check.explanation)); grid.append(card);
  });
  const explanation = $('erp-explanation'); explanation.replaceChildren();
  active.explanation.forEach(text => explanation.append(node('p', text)));
  $('erp-your-reasoning').textContent = state.answer.reasoning.trim() || 'No written explanation added. Explain which fact rules out the nearest alternative before moving on.';
  $('erp-your-uncertainty').textContent = state.answer.uncertainty.trim() ? `Still to verify: ${state.answer.uncertainty}` : 'No further verification note added.';
  $('erp-next').textContent = active === cases.at(-1) ? 'Return to the first case' : 'Next case';
}
function renderCase(focus = false) {
  $('erp-case-kicker').textContent = `Case ${cases.indexOf(active) + 1} of ${cases.length} · ${active.category}`;
  $('erp-case-title').textContent = active.title;
  $('erp-case-brief').textContent = active.brief;
  $('erp-case-objective').textContent = active.objective;
  $('erp-reset-confirm').hidden = true;
  $('erp-form-error').hidden = true;
  renderNavigation(); renderEvidence(); renderQuestions(); renderResult();
  if (focus) $('erp-case-title').focus({ preventScroll: false });
}
function switchCase(next, updateHash = true) {
  snapshot(); active = next;
  if (updateHash) history.replaceState(null, '', `#case-${next.id}`);
  renderCase(true);
}
$('erp-answer-form').addEventListener('input', () => {
  snapshot();
  if (states.get(active.id).result) {
    states.get(active.id).result = null;
    renderResult(); renderNavigation();
  }
  $('erp-form-error').hidden = true;
});
$('erp-answer-form').addEventListener('submit', event => {
  event.preventDefault();
  const answer = snapshot();
  const missing = missingAnswers(answer);
  if (missing.length) {
    $('erp-form-error').textContent = missing.join(' ');
    $('erp-form-error').hidden = false;
    const first = parseQuantity(answer.quantity) === null ? $('erp-quantity') : !answer.cause ? document.querySelector('[name="cause"]') : !answer.citations.length ? document.querySelector('[name="citations"]') : !answer.action ? document.querySelector('[name="action"]') : document.querySelector('[name="verification"]');
    first.focus();
    return;
  }
  states.get(active.id).result = evaluateCase(active, answer);
  renderResult(); renderNavigation();
  $('erp-result-title').focus();
});
$('erp-restart').addEventListener('click', () => { $('erp-reset-confirm').hidden = false; $('erp-reset-no').focus(); });
$('erp-reset-no').addEventListener('click', () => { $('erp-reset-confirm').hidden = true; $('erp-restart').focus(); });
$('erp-reset-yes').addEventListener('click', () => { states.set(active.id, { answer: blankAnswer(), opened: new Set(), result: null }); renderCase(true); });
$('erp-next').addEventListener('click', () => switchCase(cases[(cases.indexOf(active) + 1) % cases.length]));
window.addEventListener('hashchange', () => { const item = cases.find(candidate => `#case-${candidate.id}` === location.hash); if (item && item !== active) switchCase(item, false); });
active = cases.find(candidate => `#case-${candidate.id}` === location.hash) || cases[0];
renderCase();
$('erp-loading').hidden = true;
$('erp-workbench').hidden = false;
