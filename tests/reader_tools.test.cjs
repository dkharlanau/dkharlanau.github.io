const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '../assets/reader-tools.js'), 'utf8');
const origin = 'https://dkharlanau.github.io';

// Small DOM adapter: tests drive the real widget handlers, without a browser
// dependency in the Python/Jekyll publication gate. Layout is checked in browser QA.
function fixture(options = {}) {
  let document;
  class Element {
    constructor(tag, className = '') {
      this.tagName = tag.toUpperCase();
      this.className = className;
      this.children = [];
      this.attributes = {};
      this.handlers = {};
      this.dataset = {};
      this.hidden = false;
      this.textContent = '';
    }
    append(...children) { for (const child of children) { child.parent = this; this.children.push(child); } }
    remove() { this.parent.children = this.parent.children.filter((child) => child !== this); }
    contains(node) { return this === node || this.children.some((child) => child.contains(node)); }
    matches(selector) {
      return selector.split(',').some((part) => {
        part = part.trim();
        if (part.startsWith('.')) return this.className.split(' ').includes(part.slice(1));
        if (part.startsWith('[')) return Object.hasOwn(this.attributes, part.slice(1, -1));
        return this.tagName.toLowerCase() === part;
      });
    }
    querySelector(selector) {
      if (selector === 'span:last-child') return this.children.filter((child) => child.tagName === 'SPAN').at(-1);
      for (const child of this.children) {
        if (child.matches(selector)) return child;
        const match = child.querySelector(selector);
        if (match) return match;
      }
      return null;
    }
    setAttribute(key, value) { this.attributes[key] = String(value); }
    getAttribute(key) { return this.attributes[key] ?? null; }
    addEventListener(event, handler) { this.handlers[event] = handler; }
    get disabled() { return this.isDisabled || false; }
    set disabled(value) {
      this.isDisabled = value;
      if (value && document?.activeElement === this) document.activeElement = document.body;
    }
    focus() {
      if (this.disabled || document.activeElement === this) return;
      document.activeElement = this;
      document.dispatch('focusin', { target: this });
    }
    select() { this.focus(); this.selected = true; }
    async click() {
      if (this.disabled) return;
      this.focus();
      await this.handlers.click?.({ preventDefault() {} });
    }
  }
  const widget = new Element('aside', 'site-share');
  widget.dataset = {
    siteShareOrigin: origin,
    siteShareUrl: `${origin}/atlas/example/`,
    siteShareTitle: 'A practical diagnostic',
    siteShareAuthor: 'Dzmitryi Kharlanau',
  };
  const controls = {};
  for (const name of ['copy', 'citation', 'native', 'email', 'like', 'status']) {
    const control = new Element(name === 'status' ? 'p' : name === 'email' ? 'a' : 'button');
    control.setAttribute(`data-site-share-${name}`, '');
    control.hidden = !['status', 'email'].includes(name);
    control.append(new Element('span'));
    widget.append(control);
    controls[name] = control;
  }
  const main = new Element('main');
  const heading = new Element(options.targetTag || 'h2');
  heading.id = 'evidence';
  if (!options.outsideContent) main.append(heading);
  const body = new Element('body');
  body.append(main, widget);
  const canonical = new Element('link');
  canonical.setAttribute('href', options.canonical ?? `${origin}/atlas/example/?utm_source=tracking`);
  const clipboard = [];
  const legacy = [];
  const shares = [];
  const storage = new Map();
  const windowHandlers = {};
  const window = {
    location: new URL(options.location || 'http://localhost:4000/atlas/example/?token=private#evidence'),
    addEventListener: (name, handler) => { windowHandlers[name] = handler; },
    localStorage: {
      getItem: (key) => storage.get(key),
      setItem: (key, value) => { storage.set(key, value); },
      removeItem: (key) => storage.delete(key),
    },
  };
  if (options.storageBlocked) Object.defineProperty(window, 'localStorage', { get() { throw new Error('Blocked'); } });
  const navigator = {};
  if (!options.clipboardMissing) navigator.clipboard = { async writeText(value) {
    if (options.clipboardWait) await options.clipboardWait;
    if (options.clipboardBlocked) throw new Error('Denied');
    clipboard.push(value);
  } };
  if (options.nativeShare) navigator.share = async (value) => {
    if (options.shareError) throw Object.assign(new Error('Sharing failed'), { name: options.shareError });
    shares.push(value);
  };
  const documentHandlers = new Map();
  document = {
    readyState: 'complete', title: 'A diagnostic | Site', body, activeElement: body,
    createElement: (tag) => new Element(tag),
    getElementById: (id) => !options.headingPending && id === heading.id ? heading : null,
    addEventListener: (event, handler) => {
      if (!documentHandlers.has(event)) documentHandlers.set(event, new Set());
      documentHandlers.get(event).add(handler);
    },
    removeEventListener: (event, handler) => documentHandlers.get(event)?.delete(handler),
    dispatch: (event, details) => { documentHandlers.get(event)?.forEach((handler) => handler(details)); },
    querySelectorAll: () => [],
    querySelector: (selector) => ({
      '[data-site-share]': widget,
      '#content': main,
      'link[rel="canonical"]': options.canonicalMissing ? null : canonical,
      'meta[property="article:modified_time"]': options.date ? { content: options.date } : null,
      'meta[name="author"]': { content: 'Dzmitryi Kharlanau' },
    })[selector] || null,
    execCommand: () => {
      legacy.push(body.children.find((child) => child.tagName === 'TEXTAREA').value);
      if (options.execThrows) throw new Error('Blocked');
      return options.execResult ?? false;
    },
  };
  vm.runInNewContext(source, { window, document, navigator, URL, Date, console });
  return { controls, widget, window, windowHandlers, document, clipboard, legacy, shares, storage, options };
}

test('copy and citation use canonical production URLs, actual metadata, and known headings', async () => {
  const f = fixture({ date: '2026-08-20T12:30:00+03:00' });
  await f.controls.copy.click();
  assert.deepEqual(f.clipboard, [`${origin}/atlas/example/#evidence`]);
  assert.equal(f.controls.status.textContent, 'Link copied to the clipboard.');
  assert.equal(f.controls.copy.disabled, false);
  assert.equal(f.legacy.length, 0);
  await f.controls.citation.click();
  assert.equal(f.clipboard[1], `Dzmitryi Kharlanau. “A practical diagnostic”. Updated 2026-08-20. ${origin}/atlas/example/`);
  assert.equal(f.controls.status.textContent, 'Citation copied to the clipboard.');
});

test('external, credentialed, insecure, and script canonicals never enter shared URLs', async () => {
  for (const canonical of [
    'https://example.com/atlas/example/', 'https://dkharlanau.github.io.evil.test/atlas/example/',
    'https://secret:password@dkharlanau.github.io/atlas/example/', 'javascript:alert(1)',
    'http://dkharlanau.github.io/atlas/example/', '//evil.test/atlas/example/',
  ]) {
    const f = fixture({ canonical });
    await f.controls.copy.click();
    assert.equal(f.clipboard[0], `${origin}/atlas/example/#evidence`, canonical);
  }
});

test('aliases use their canonical destination and preview/missing canonicals use production fallback', async () => {
  const alias = fixture({ canonical: `${origin}/machine/portfolio/`, location: `${origin}/products/?private=yes#evidence` });
  await alias.controls.copy.click();
  assert.equal(alias.clipboard[0], `${origin}/machine/portfolio/`);
  for (const options of [{ canonicalMissing: true }, { canonical: '  ' }, { canonical: 'http://localhost:4000/atlas/example/' }, { canonical: '/atlas/example/' }]) {
    const f = fixture(options);
    await f.controls.copy.click();
    assert.equal(f.clipboard[0], `${origin}/atlas/example/#evidence`);
  }
});

test('unknown, non-heading, outside-content, and malformed fragments are dropped', async () => {
  for (const options of [
    { location: `${origin}/atlas/example/#private-token` }, { targetTag: 'input' },
    { outsideContent: true }, { location: `${origin}/atlas/example/#%E0%A4%A` },
    { location: `${origin}/atlas/example/#:~:text=private` },
  ]) {
    const f = fixture(options);
    await f.controls.copy.click();
    assert.equal(f.clipboard[0], `${origin}/atlas/example/`);
  }
});

test('copy, email, and native sharing follow the current valid heading without sending on load', async () => {
  const f = fixture({ nativeShare: true });
  assert.equal(f.shares.length, 0);
  assert.equal(f.clipboard.length, 0);
  assert.equal(f.controls.native.hidden, false);
  assert.equal(new URL(f.controls.email.href).searchParams.get('body'), `${origin}/atlas/example/#evidence`);
  f.window.location.hash = '#unknown';
  f.windowHandlers.hashchange();
  assert.equal(new URL(f.controls.email.href).searchParams.get('body'), `${origin}/atlas/example/`);
  await f.controls.native.click();
  assert.equal(f.shares[0].url, `${origin}/atlas/example/`);
  await f.controls.copy.click();
  assert.equal(f.clipboard[0], `${origin}/atlas/example/`);
});

test('blocked or absent clipboard can succeed only when the legacy command reports success', async () => {
  for (const options of [{ clipboardBlocked: true }, { clipboardMissing: true }]) {
    const f = fixture({ ...options, execResult: true });
    await f.controls.copy.click();
    assert.equal(f.clipboard.length, 0);
    assert.deepEqual(f.legacy, [`${origin}/atlas/example/#evidence`]);
    assert.equal(f.controls.status.textContent, 'Link copied to the clipboard.');
    assert.equal(f.widget.querySelector('.reader-copy-fallback'), null);
    assert.equal(f.document.activeElement, f.controls.copy);
    assert.equal(f.document.body.children.filter((node) => node.tagName === 'TEXTAREA').length, 0);
  }
});

test('successful copy restores keyboard focus only after the trigger is re-enabled', async () => {
  for (const options of [{}, { clipboardMissing: true, execResult: true }]) {
    const f = fixture(options);
    await f.controls.copy.click();
    assert.equal(f.controls.copy.disabled, false);
    assert.equal(f.document.activeElement, f.controls.copy);
    await f.controls.citation.click();
    assert.equal(f.document.activeElement, f.controls.citation);
  }
});

test('asynchronous copy never takes focus back after the reader moves to another control', async () => {
  for (const options of [{}, { clipboardBlocked: true, execResult: true }, { clipboardBlocked: true, execResult: false }]) {
    let resolveCopy;
    const clipboardWait = new Promise((resolve) => { resolveCopy = resolve; });
    const f = fixture({ ...options, clipboardWait });
    const copying = f.controls.copy.click();
    assert.equal(f.controls.copy.disabled, true);
    f.controls.email.focus();
    resolveCopy();
    await copying;
    assert.equal(f.controls.copy.disabled, false);
    assert.equal(f.document.activeElement, f.controls.email);
    if (options.execResult === false) {
      const field = f.widget.querySelector('.reader-copy-fallback').querySelector('textarea');
      assert.equal(field.value, `${origin}/atlas/example/#evidence`);
      assert.notEqual(field.selected, true);
    }
  }
});

test('email activation finds a TOC heading created after initial sharing setup', async () => {
  const f = fixture({ headingPending: true });
  assert.equal(new URL(f.controls.email.href).searchParams.get('body'), `${origin}/atlas/example/`);
  f.options.headingPending = false;
  // TOC construction does not emit hashchange. Mouse and keyboard activation
  // both dispatch click; the refreshed href must exist before mailto navigation.
  await f.controls.email.click();
  assert.equal(new URL(f.controls.email.href).searchParams.get('body'), `${origin}/atlas/example/#evidence`);
  const alias = fixture({ headingPending: true, canonical: `${origin}/machine/portfolio/`, location: `${origin}/products/#evidence` });
  alias.options.headingPending = false;
  await alias.controls.email.click();
  assert.equal(new URL(alias.controls.email.href).searchParams.get('body'), `${origin}/machine/portfolio/`);
});

test('copy failure offers a labelled selected manual field, supports retry and restores focus on close', async () => {
  for (const options of [{ execResult: false }, { execThrows: true }]) {
    const f = fixture({ ...options, clipboardBlocked: true });
    await f.controls.copy.click();
    const panel = f.widget.querySelector('.reader-copy-fallback');
    const field = panel.querySelector('textarea');
    assert.equal(field.parent.tagName, 'LABEL');
    assert.equal(field.readOnly, true);
    assert.equal(field.selected, true);
    assert.equal(f.document.activeElement, field);
    assert.equal(field.value, `${origin}/atlas/example/#evidence`);
    assert.match(f.controls.status.textContent, /Automatic copy is unavailable/);
    assert.equal(f.controls.copy.disabled, false);
    await f.controls.citation.click();
    assert.equal(f.widget.children.filter((child) => child.className === 'reader-copy-fallback').length, 1);
    assert.match(field.value, /Dzmitryi Kharlanau/);
    await panel.querySelector('button').click();
    assert.equal(panel.hidden, true);
    assert.equal(f.document.activeElement, f.controls.citation);
    f.options.clipboardBlocked = false;
    await f.controls.copy.click();
    assert.equal(panel.hidden, true);
    assert.equal(f.controls.status.textContent, 'Link copied to the clipboard.');
  }
});

test('no date or invalid dates do not invent update/review dates', async () => {
  for (const date of [undefined, 'yesterday', '2026-02-31', '2026-08-20 definitely reviewed', '2026-08-20Tnot-a-date']) {
    const f = fixture({ date });
    await f.controls.citation.click();
    assert.equal(f.clipboard[0], `Dzmitryi Kharlanau. “A practical diagnostic”. ${origin}/atlas/example/`);
  }
});

test('helpful is local, removable, and honest when device storage is unavailable', async () => {
  const f = fixture();
  assert.equal(f.controls.native.hidden, true);
  assert.equal(f.controls.like.hidden, false);
  await f.controls.like.click();
  assert.equal(f.controls.like.getAttribute('aria-pressed'), 'true');
  assert.equal(f.storage.get('dkh-page-helpful:/atlas/example/'), 'true');
  await f.controls.like.click();
  assert.equal(f.storage.size, 0);
  const blocked = fixture({ storageBlocked: true });
  await blocked.controls.like.click();
  assert.equal(blocked.controls.like.getAttribute('aria-pressed'), 'true');
  assert.match(blocked.controls.status.textContent, /for this visit/);
  await blocked.controls.copy.click();
  assert.equal(blocked.clipboard.length, 1);
});

test('native cancellation is silent and real native failures give a usable alternative', async () => {
  const cancelled = fixture({ nativeShare: true, shareError: 'AbortError' });
  const before = cancelled.controls.status.textContent;
  await cancelled.controls.native.click();
  assert.equal(cancelled.controls.status.textContent, before);
  const denied = fixture({ nativeShare: true, shareError: 'NotAllowedError' });
  await denied.controls.native.click();
  assert.equal(denied.controls.status.textContent, 'Sharing is unavailable. Use Copy link or Send by email.');
});
