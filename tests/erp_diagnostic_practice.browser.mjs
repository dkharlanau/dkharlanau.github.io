import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { readFile, stat, mkdir, writeFile } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
const { chromium } = await import(process.env.ERP_PLAYWRIGHT_MODULE || 'playwright-core');
const root = process.env.ERP_SITE_DIR || resolve('_site');
const out = process.env.ERP_QA_OUTPUT || resolve('output/playwright/erp-diagnostic-practice');
await mkdir(out, { recursive: true });
const mime = { '.html': 'text/html', '.mjs': 'text/javascript', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2' };
const server = createServer(async (req, res) => {
  try {
    let path = resolve(root, '.' + decodeURIComponent(new URL(req.url, 'http://local').pathname));
    if (!path.startsWith(resolve(root) + sep) && path !== resolve(root)) throw Error('path');
    if ((await stat(path)).isDirectory()) path = resolve(path, 'index.html');
    res.writeHead(200, { 'Content-Type': mime[extname(path)] || 'application/octet-stream' });
    res.end(await readFile(path));
  } catch { res.writeHead(404); res.end('Not found'); }
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const base = `http://127.0.0.1:${server.address().port}`;
const route = '/labs/erp-diagnostic-practice/';
const browser = await chromium.launch({ channel: 'chrome', headless: true });
const failures = [];
const evidence = [];
try {
  for (const width of [1440, 390]) {
    const context = await browser.newContext({ viewport: { width, height: 1000 }, reducedMotion: 'reduce' });
    await context.route('**/*', request => /^https:\/\/fonts\.(googleapis|gstatic)\.com\//.test(request.request().url()) || request.request().url().startsWith(base) ? request.continue() : request.abort());
    const page = await context.newPage();
    page.on('pageerror', error => failures.push(error.message));
    await page.goto(base + route);
    await page.locator('#erp-workbench').waitFor({ state: 'visible' });
    await page.evaluate(() => document.fonts.ready);
    assert.equal(await page.locator('.erp-hero h1').evaluate(node => getComputedStyle(node).color), 'rgb(255, 255, 255)');
    assert.equal(await page.locator('meta[name="robots"]').getAttribute('content'), 'noindex,follow');
    assert.equal(await page.locator('link[rel="canonical"]').getAttribute('href'), 'https://dkharlanau.github.io' + route);
    assert.equal(await page.locator('#erp-case-title').textContent(), 'Ten ordered. One hundred delivered?');
    await page.screenshot({ path: `${out}/${width}-intro.png` });
    await page.locator('#erp-evidence summary').first().focus();
    await page.keyboard.press('Enter');
    await page.locator('#erp-evidence details').nth(1).locator('summary').click();
    await page.locator('#erp-evidence details').nth(2).locator('summary').click();
    await page.waitForFunction(() => document.getElementById('erp-inspected').textContent.startsWith('3 of'));
    assert.ok(await page.locator('#erp-evidence table').first().isVisible());
    await page.locator('#erp-case-title').evaluate(node => node.scrollIntoView({ block: 'start' }));
    await page.screenshot({ path: `${out}/${width}-evidence.png` });
    await page.getByRole('button', { name: 'Check my answer', exact: true }).click();
    assert.equal(await page.locator('#erp-form-error').isVisible(), true);
    assert.equal(await page.locator('#erp-quantity').evaluate(node => node === document.activeElement), true);
    const answers = { units: ['100', 'report', 'normalize', 'two'], duplicate: ['176', 'key', 'controlled', 'replay-new'], migration: ['3', 'offset', 'hold', 'outer'] };
    for (const [id, [quantity, cause, action, verification]] of Object.entries(answers)) {
      await page.locator(`[data-case="${id}"]`).click();
      await page.locator('#erp-quantity').fill(quantity);
      await page.locator(`[name="cause"][value="${cause}"]`).check();
      for (const ref of ['A', 'B', 'C']) await page.locator(`[name="citations"][value="${ref}"]`).check();
      await page.locator(`[name="action"][value="${action}"]`).check();
      await page.locator(`[name="verification"][value="${verification}"]`).check();
      await page.locator('#erp-reasoning').fill('<img src=x onerror="window.badInput=true"> Evidence A and B explain the records; C identifies the failed control.');
      if (id === 'units') {
        await page.locator('#erp-quantity').fill('90');
        await page.getByRole('button', { name: 'Check my answer', exact: true }).click();
        assert.match(await page.locator('#erp-result-title').textContent(), /4 of 5/);
        await page.locator('#erp-quantity').fill('100');
        assert.equal(await page.locator('#erp-result').isVisible(), false);
      }
      await page.getByRole('button', { name: 'Check my answer', exact: true }).click();
      assert.equal(await page.locator('#erp-result-title').textContent(), 'All five checked conclusions match.');
      assert.equal(await page.locator('#erp-result-title').evaluate(node => node === document.activeElement), true);
      assert.equal(await page.locator('#erp-your-reasoning img').count(), 0);
      assert.equal(await page.evaluate(() => window.badInput), undefined);
      if (id === 'units') {
        await page.locator('#erp-reasoning').fill('A and B show that 10 BOX equals 100 EA. C compares raw quantities without converting their units, so the exception does not prove an over-delivery.');
        await page.getByRole('button', { name: 'Check my answer', exact: true }).click();
        await page.screenshot({ path: `${out}/${width}-feedback.png` });
      }
    }
    await page.locator('[data-case="units"]').click();
    assert.equal(await page.locator('#erp-quantity').inputValue(), '100');
    assert.equal(await page.locator('#erp-result').isVisible(), true);
    await page.locator('#erp-restart').click();
    await page.locator('#erp-reset-no').click();
    assert.equal(await page.locator('#erp-quantity').inputValue(), '100');
    await page.locator('#erp-restart').click();
    await page.locator('#erp-reset-yes').click();
    assert.equal(await page.locator('#erp-quantity').inputValue(), '');
    assert.equal(await page.locator('#erp-result').isVisible(), false);
    await page.locator('[data-case="migration"]').click();
    assert.equal(await page.locator('#erp-quantity').inputValue(), '3');
    await page.reload();
    await page.locator('#erp-workbench').waitFor({ state: 'visible' });
    assert.equal(await page.locator('#erp-case-title').textContent(), 'The totals match. The migration does not.');
    assert.equal(await page.locator('#erp-quantity').inputValue(), '');
    const overflow = await page.evaluate(() => ({ document: document.documentElement.scrollWidth, viewport: innerWidth }));
    assert.ok(overflow.document <= overflow.viewport, JSON.stringify(overflow));
    const duplicateIds = await page.evaluate(() => { const ids = [...document.querySelectorAll('[id]')].map(node => node.id); return ids.filter((id, index) => ids.indexOf(id) !== index); });
    assert.deepEqual(duplicateIds, []);
    evidence.push({ width, checks: 'All 3 correct paths, wrong answer, required fields, keyboard evidence, XSS text, preserved drafts, isolated restart, hash route, reload clearing, no overflow, canonical/noindex passed' });
    await context.close();
  }
  const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  await context.route('**/*', request => /^https:\/\/fonts\.(googleapis|gstatic)\.com\//.test(request.request().url()) || request.request().url().startsWith(base) ? request.continue() : request.abort());
  const page = await context.newPage();
  await page.goto(base + route);
  await page.locator('.erp-reference > details').first().locator('summary').click();
  assert.equal(await page.locator('.erp-reference table').first().isVisible(), true);
  assert.equal(await page.locator('.erp-reference table').count(), 9);
  assert.equal(await page.locator('.erp-faq details').count(), 3);
  await page.screenshot({ path: `${out}/390-no-javascript.png` });
  await context.close();
  assert.deepEqual(failures, []);
  await writeFile(`${out}/result.json`, JSON.stringify({ evidence, noJavaScript: 'all nine original evidence tables and three FAQ answers are in static HTML', errors: failures }, null, 2));
  console.log(JSON.stringify({ evidence, noJavaScript: 'passed', errors: failures, output: out }, null, 2));
} finally {
  await browser.close();
  await new Promise(resolve => server.close(resolve));
}
