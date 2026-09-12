const test = require('node:test');
const assert = require('node:assert/strict');
const {sequenceSteps} = require('../assets/learning-diagrams.js');
test('preserves supplied ordered stage wording', () => {
  assert.deepEqual(sequenceSteps('Active source?\n→ selected by DRF?\n→ target committed?', 'text'), ['Active source?', 'selected by DRF?', 'target committed?']);
  assert.deepEqual(sequenceSteps('Evidence → Review → Decision'), ['Evidence', 'Review', 'Decision']);
  assert.deepEqual(sequenceSteps('question -> source IDs -> retrieval -> ranking', 'text'), ['question', 'source IDs', 'retrieval', 'ranking']);
});
test('does not reinterpret commands, branches or programming languages', () => {
  assert.equal(sequenceSteps('a → b → c', 'javascript'), null);
  assert.equal(sequenceSteps('a -> b -> c', 'javascript'), null);
  assert.equal(sequenceSteps('a\n→ b\notherwise c'), null);
  assert.equal(sequenceSteps('a → b | c → d'), null);
  assert.equal(sequenceSteps('a → b'), null);
  assert.equal(sequenceSteps('a → → c'), null);
  assert.equal(sequenceSteps('a\n→ b → c\n→ d'), null);
});
