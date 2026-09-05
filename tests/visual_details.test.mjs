import test from 'node:test';
import assert from 'node:assert/strict';
import { inspectPortraitFrames } from '../scripts/lib/visual_details.mjs';

const corners = ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius'];
function fixture({ outer = '24px', inner = '0px', inset = 1, overflow = 'hidden', imageOverrides = {} } = {}) {
  const rect = (start, end) => ({ left: start, top: start, right: end, bottom: end, width: end - start, height: end - start });
  const baseStyle = { opacity: '1', visibility: 'visible', overflowX: overflow, overflowY: overflow, borderTopWidth: '1px', borderRightWidth: '1px', borderBottomWidth: '1px', borderLeftWidth: '1px' };
  const img = { style: { ...baseStyle, ...Object.fromEntries(corners.map(key => [key, inner])), ...imageOverrides }, getBoundingClientRect: () => rect(inset, 270 - inset) };
  const frame = { tagName: 'PICTURE', classList: ['personal-hero__portrait'], style: { ...baseStyle, ...Object.fromEntries(corners.map(key => [key, outer])) }, querySelector: () => img, getBoundingClientRect: () => rect(0, 270) };
  globalThis.document = { querySelectorAll: () => [frame] };
  globalThis.getComputedStyle = node => node.style;
}

test('detects the square frame / rounded image regression from the homepage', () => {
  fixture({ outer: '3px', inner: '24px' });
  assert.equal(inspectPortraitFrames().length, 4);
});

test('accepts frame-owned clipping, a fitted inner curve, and circular avatars', () => {
  for (const options of [{ inner: '0px' }, { inner: '23px' }, { outer: '50%', inner: '50%' }]) {
    fixture(options);
    assert.deepEqual(inspectPortraitFrames(), []);
  }
});

test('detects a one-pixel background crescent and asymmetric corner regressions', () => {
  fixture({ imageOverrides: { borderBottomLeftRadius: '24px' } });
  assert.deepEqual(inspectPortraitFrames().map(issue => issue.corner), ['borderBottomLeftRadius']);
});

test('ignores intentional inset shapes and non-clipping wrappers', () => {
  for (const options of [{ outer: '3px', inner: '24px', inset: 12 }, { outer: '3px', inner: '24px', overflow: 'visible' }]) {
    fixture(options);
    assert.deepEqual(inspectPortraitFrames(), []);
  }
});

test('does not report hidden portrait variants', () => {
  fixture({ outer: '3px', inner: '24px', imageOverrides: { visibility: 'hidden' } });
  assert.deepEqual(inspectPortraitFrames(), []);
});
