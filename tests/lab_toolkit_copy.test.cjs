const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');

function fixture(clipboard) {
  const disclosure = { open: false };
  const prompt = { textContent: '  Public source prompt  ', closest: () => disclosure };
  const status = { textContent: '' };
  let click;
  let selected;
  const button = {
    textContent: 'Copy agent prompt',
    getAttribute: (name) => ({ 'data-copy-target': 'prompt', 'data-copy-status': 'status' }[name]),
    addEventListener: (event, callback) => { click = callback; },
  };
  const document = {
    querySelectorAll: () => [button],
    getElementById: (id) => ({ prompt, status }[id]),
    createRange: () => ({ selectNodeContents: (node) => { selected = node; } }),
  };
  const window = {
    setTimeout: () => {},
    getSelection: () => ({ removeAllRanges() {}, addRange() {} }),
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../assets/lab-toolkit.js'), 'utf8'), { document, window, navigator: { clipboard } });
  return { click: () => click(), button, status, disclosure, selected: () => selected };
}

test('copy succeeds with the displayed prompt and an announced next step', async () => {
  let copied;
  const f = fixture({ writeText: async (text) => { copied = text; } });
  await f.click();
  assert.equal(copied, 'Public source prompt');
  assert.equal(f.button.textContent, 'Copied');
  assert.match(f.status.textContent, /Paste it into your agent/);
  assert.equal(f.disclosure.open, false);
});

test('missing or blocked clipboard reveals text for manual copy without claiming success', async () => {
  for (const clipboard of [undefined, { writeText: async () => { throw new Error('blocked'); } }]) {
    const f = fixture(clipboard);
    await f.click();
    assert.equal(f.disclosure.open, true);
    assert.equal(f.selected().textContent.trim(), 'Public source prompt');
    assert.match(f.status.textContent, /copy it manually/);
    assert.doesNotMatch(f.status.textContent, /Prompt copied/);
  }
});
