import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { cases } from '../labs/erp-diagnostic-practice/cases.mjs';
import { blankAnswer, evaluateCase, missingAnswers, parseQuantity } from '../labs/erp-diagnostic-practice/engine.mjs';
const correct = item => ({ quantity: String(item.calculation.expected), cause: item.cause.correct, citations: [...item.citations.expected], action: item.action.correct, verification: item.verification.correct, reasoning: '', uncertainty: '' });

test('reject blank, non-finite and ambiguous numeric inputs rather than treating them as zero', () => {
  for (const value of ['', ' ', null, 'NaN', 'Infinity', '0x64', '1e2', '100 EA', '100,000.00']) assert.equal(parseQuantity(value), null, String(value));
  assert.equal(parseQuantity(' 100.00 '), 100);
  assert.equal(parseQuantity('100,00'), 100);
  assert.equal(missingAnswers(blankAnswer()).length, 5);
});
for (const item of cases) {
  test(`${item.id}: each checked conclusion matters independently`, () => {
    const answer = correct(item);
    assert.equal(evaluateCase(item, answer).complete, true);
    assert.deepEqual(missingAnswers(answer), []);
    for (const key of ['quantity', 'cause', 'citations', 'action', 'verification']) {
      const changed = { ...answer, [key]: key === 'citations' ? ['A', 'B'] : key === 'quantity' ? '0' : 'unsupported' };
      const result = evaluateCase(item, changed);
      assert.equal(result.correct, 4, key);
      assert.equal(result.complete, false);
    }
    assert.equal(evaluateCase(item, { ...answer, citations: ['C', 'A', 'B'] }).complete, true);
    assert.equal(evaluateCase(item, { ...answer, citations: ['A', 'B', 'C', 'unknown'] }).complete, false);
  });
}
test('units: source quantities reconcile after conversion, while a real excess remains visible', () => {
  const item = cases.find(item => item.id === 'units');
  const requested = Number(item.evidence[0].rows[0][1]);
  const shipped = Number(item.evidence[0].rows[1][1]);
  const factor = Number(item.evidence[1].rows[0][3].match(/= (\d+) EA/)[1]);
  assert.equal(requested * factor, item.calculation.expected);
  assert.equal(shipped - requested * factor, 0);
  assert.equal(110 - requested * factor, 10);
  assert.equal(evaluateCase(item, { ...correct(item), action: 'reverse' }).complete, false);
});
test('duplicate: one business event produced two postings, and success cannot prove uniqueness', () => {
  const item = cases.find(item => item.id === 'duplicate');
  const messages = item.evidence[0].rows;
  const postings = item.evidence[1].rows;
  assert.equal(new Set(messages.map(row => row[1])).size, 1);
  assert.equal(new Set(messages.map(row => row[0])).size, 2);
  assert.equal(postings.length, 2);
  assert.equal(200 - 24, item.calculation.expected);
  assert.equal(evaluateCase(item, { ...correct(item), cause: 'timeout' }).checks.find(check => check.id === 'cause').passed, false);
  assert.equal(evaluateCase(item, { ...correct(item), verification: 'status' }).complete, false);
});
test('migration: aggregate match hides three distinct key exceptions', () => {
  const item = cases.find(item => item.id === 'migration');
  const source = new Map(item.evidence[0].rows.map(row => [row[0], Number(row[1])]));
  const target = new Map(item.evidence[1].rows.map(row => [row[0], Number(row[1])]));
  const total = map => [...map.values()].reduce((a, b) => a + b, 0);
  assert.equal(total(source), total(target));
  const exceptions = [...new Set([...source.keys(), ...target.keys()])].filter(key => source.get(key) !== target.get(key));
  assert.deepEqual(exceptions, ['item-b', 'item-c', 'item-d']);
  assert.equal(exceptions.length, item.calculation.expected);
  assert.equal(evaluateCase(item, { ...correct(item), action: 'accept' }).complete, false);
});
test('free prose never becomes a fabricated competence score', () => {
  const item = cases[0];
  assert.deepEqual(evaluateCase(item, { ...correct(item), reasoning: 'Wrong explanation.' }), evaluateCase(item, { ...correct(item), reasoning: 'A long convincing answer with made-up experience.' }));
});
test('page remains review-gated and the static evidence guide stays in sync', () => {
  const page = readFileSync(new URL('../labs/erp-diagnostic-practice/index.html', import.meta.url), 'utf8');
  assert.match(page, /verified: false/);
  assert.match(page, /robots: noindex,follow/);
  assert.match(page, /sitemap: false/);
  assert.match(page, /status: needs_verification/);
  for (const item of cases) assert.ok(page.includes(item.brief), item.id);
  execFileSync(process.execPath, [new URL('../labs/erp-diagnostic-practice/generate-reference.mjs', import.meta.url).pathname, '--check']);
});
