#!/usr/bin/env node
import { chromium } from 'playwright-core';
import { createServer } from 'node:http';
import { createReadStream, existsSync } from 'node:fs';
import { mkdir, stat, writeFile } from 'node:fs/promises';
import { extname, resolve, sep } from 'node:path';
import process from 'node:process';

const DEFAULT_ROUTES = [
  '/',
  '/knowledge/',
  '/labs/',
  '/labs/tool-roadmap/',
  '/frameworks/',
  '/machine/',
  '/services/',
];

const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 1000, isMobile: false },
  { name: 'mobile', width: 390, height: 844, isMobile: true },
];

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
};

function parseArgs(argv) {
  const out = {
    siteDir: '_site',
    outputDir: 'reports/visual-smoke',
    routes: DEFAULT_ROUTES,
  };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--site-dir') out.siteDir = argv[++i];
    else if (arg === '--output-dir') out.outputDir = argv[++i];
    else if (arg === '--routes') out.routes = argv[++i].split(',').map((v) => v.trim()).filter(Boolean);
  }
  return out;
}

function slugifyRoute(route) {
  if (route === '/') return 'home';
  return route.replace(/^\/+|\/+$/g, '').replace(/[^a-zA-Z0-9._-]+/g, '__') || 'page';
}

function safePath(siteDir, urlPath) {
  let decoded;
  try {
    decoded = decodeURIComponent(urlPath.split('?')[0].split('#')[0]);
  } catch {
    return null;
  }
  let relative = decoded.replace(/^\/+/, '');
  if (!relative || relative.endsWith('/')) relative += 'index.html';
  const root = resolve(siteDir);
  const candidate = resolve(root, relative);
  if (candidate !== root && !candidate.startsWith(`${root}${sep}`)) return null;
  return candidate;
}

async function startStaticServer(siteDir) {
  const server = createServer(async (req, res) => {
    const requestUrl = new URL(req.url || '/', 'http://127.0.0.1');
    let filePath = safePath(siteDir, requestUrl.pathname);
    if (!filePath) {
      res.writeHead(400).end('Bad request');
      return;
    }

    try {
      let info = await stat(filePath);
      if (info.isDirectory()) {
        filePath = resolve(filePath, 'index.html');
        info = await stat(filePath);
      }
      if (!info.isFile()) throw new Error('not a file');
      const contentType = MIME_TYPES[extname(filePath).toLowerCase()] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': contentType, 'Cache-Control': 'no-store' });
      if (req.method === 'HEAD') res.end();
      else createReadStream(filePath).pipe(res);
    } catch {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }).end('Not found');
    }
  });

  await new Promise((resolveReady, reject) => {
    server.once('error', reject);
    server.listen(0, '127.0.0.1', resolveReady);
  });
  const address = server.address();
  return { server, baseUrl: `http://127.0.0.1:${address.port}` };
}

async function launchBrowser() {
  const launchOptions = {
    headless: true,
    args: ['--disable-dev-shm-usage', '--no-sandbox'],
  };
  try {
    return await chromium.launch({ ...launchOptions, channel: 'chrome' });
  } catch (channelError) {
    const candidates = [
      process.env.CHROME_BIN,
      '/usr/bin/google-chrome',
      '/usr/bin/google-chrome-stable',
      '/usr/bin/chromium',
      '/usr/bin/chromium-browser',
    ].filter(Boolean);
    for (const executablePath of candidates) {
      if (!existsSync(executablePath)) continue;
      try {
        return await chromium.launch({ ...launchOptions, executablePath });
      } catch {
        // Try the next installed browser path.
      }
    }
    throw new Error(`Could not launch an installed Chrome/Chromium browser. First error: ${channelError.message}`);
  }
}

function buildFailureSummary(result) {
  const failures = [];
  if (result.status >= 400) failures.push(`HTTP ${result.status}`);
  if (result.pageErrors.length) failures.push(`${result.pageErrors.length} page error(s)`);
  if (result.audit.rootOverflow > 2) failures.push(`page overflows viewport by ${result.audit.rootOverflow}px`);
  if (result.audit.brokenImages.length) failures.push(`${result.audit.brokenImages.length} broken image(s)`);
  if (result.audit.hugeTextBlocks.length) failures.push(`${result.audit.hugeTextBlocks.length} huge text block(s)`);
  if (result.audit.interactiveOverlaps.length) failures.push(`${result.audit.interactiveOverlaps.length} overlapping interactive pair(s)`);
  return failures;
}

async function auditPage(page, viewport) {
  return page.evaluate(({ viewportWidth, viewportHeight }) => {
    const isVisible = (el) => {
      const style = window.getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      return style.display !== 'none' && style.visibility !== 'hidden' && Number.parseFloat(style.opacity || '1') > 0.01 && rect.width > 1 && rect.height > 1;
    };

    const label = (el) => {
      const id = el.id ? `#${el.id}` : '';
      const classes = [...el.classList].slice(0, 2).map((name) => `.${name}`).join('');
      const text = (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 90);
      return `${el.tagName.toLowerCase()}${id}${classes}${text ? ` :: ${text}` : ''}`;
    };

    const root = document.documentElement;
    const rootOverflow = Math.max(0, Math.round(root.scrollWidth - root.clientWidth));

    const brokenImages = [...document.images]
      .filter((img) => isVisible(img) && img.complete && img.naturalWidth === 0)
      .slice(0, 20)
      .map((img) => ({ src: img.currentSrc || img.src, label: label(img) }));

    const textNodes = [...document.querySelectorAll('p, li, td, th, blockquote, dd, dt, figcaption')]
      .filter(isVisible);

    const hugeTextBlocks = textNodes
      .map((el) => ({
        el,
        textLength: (el.textContent || '').trim().length,
        rect: el.getBoundingClientRect(),
      }))
      .filter(({ textLength, rect }) => textLength > 1600 && rect.height > Math.max(420, viewportHeight * 0.55))
      .slice(0, 12)
      .map(({ el, textLength, rect }) => ({
        label: label(el),
        textLength,
        height: Math.round(rect.height),
      }));

    const clippedText = textNodes
      .filter((el) => {
        const style = window.getComputedStyle(el);
        const textLength = (el.textContent || '').trim().length;
        const hidesOverflow = ['hidden', 'clip'].includes(style.overflowX);
        const intentionalEllipsis = style.textOverflow === 'ellipsis';
        return textLength > 30 && hidesOverflow && !intentionalEllipsis && el.scrollWidth > el.clientWidth + 4;
      })
      .slice(0, 20)
      .map((el) => ({ label: label(el), hiddenPixels: Math.round(el.scrollWidth - el.clientWidth) }));

    const tinyText = textNodes
      .filter((el) => Number.parseFloat(window.getComputedStyle(el).fontSize) < 9.5 && (el.textContent || '').trim().length > 0)
      .slice(0, 20)
      .map((el) => ({ label: label(el), fontSize: window.getComputedStyle(el).fontSize }));

    const rawMarkdownSignals = [];
    const bodyText = document.body.innerText || '';
    if (/^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$/m.test(bodyText)) rawMarkdownSignals.push('table delimiter row visible');
    if (/^\s*(?:```+|~~~+)/m.test(bodyText)) rawMarkdownSignals.push('fenced-code marker visible');

    const interactive = [...document.querySelectorAll('a[href], button, input:not([type="hidden"]), select, textarea, summary')]
      .filter(isVisible)
      .map((el) => ({ el, rect: el.getBoundingClientRect(), label: label(el) }))
      .filter(({ rect }) => rect.width > 3 && rect.height > 3)
      .slice(0, 180);

    const interactiveOverlaps = [];
    for (let i = 0; i < interactive.length; i += 1) {
      for (let j = i + 1; j < interactive.length; j += 1) {
        const a = interactive[i];
        const b = interactive[j];
        if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
        const overlapWidth = Math.max(0, Math.min(a.rect.right, b.rect.right) - Math.max(a.rect.left, b.rect.left));
        const overlapHeight = Math.max(0, Math.min(a.rect.bottom, b.rect.bottom) - Math.max(a.rect.top, b.rect.top));
        if (!overlapWidth || !overlapHeight) continue;
        const overlapArea = overlapWidth * overlapHeight;
        const minArea = Math.min(a.rect.width * a.rect.height, b.rect.width * b.rect.height);
        if (minArea > 0 && overlapArea / minArea >= 0.45) {
          interactiveOverlaps.push({ a: a.label, b: b.label, ratio: Number((overlapArea / minArea).toFixed(2)) });
          if (interactiveOverlaps.length >= 20) break;
        }
      }
      if (interactiveOverlaps.length >= 20) break;
    }

    return {
      viewportWidth,
      viewportHeight,
      documentWidth: root.scrollWidth,
      documentHeight: root.scrollHeight,
      rootOverflow,
      brokenImages,
      hugeTextBlocks,
      clippedText,
      tinyText,
      rawMarkdownSignals,
      interactiveOverlaps,
      h1Count: document.querySelectorAll('h1').length,
    };
  }, { viewportWidth: viewport.width, viewportHeight: viewport.height });
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const siteDir = resolve(args.siteDir);
  const outputDir = resolve(args.outputDir);
  await mkdir(outputDir, { recursive: true });

  const { server, baseUrl } = await startStaticServer(siteDir);
  let browser;
  const report = {
    generatedAt: new Date().toISOString(),
    siteDir,
    routes: args.routes,
    viewports: VIEWPORTS,
    results: [],
  };

  try {
    browser = await launchBrowser();
    for (const viewport of VIEWPORTS) {
      const viewportDir = resolve(outputDir, viewport.name);
      await mkdir(viewportDir, { recursive: true });
      const context = await browser.newContext({
        viewport: { width: viewport.width, height: viewport.height },
        deviceScaleFactor: 1,
        isMobile: viewport.isMobile,
        hasTouch: viewport.isMobile,
        locale: 'en-US',
      });

      for (const route of args.routes) {
        const page = await context.newPage();
        const pageErrors = [];
        const consoleErrors = [];
        page.on('pageerror', (error) => pageErrors.push(error.message));
        page.on('console', (message) => {
          if (message.type() === 'error') consoleErrors.push(message.text());
        });

        let status = 0;
        let screenshot = '';
        let audit = {
          rootOverflow: 0,
          brokenImages: [],
          hugeTextBlocks: [],
          clippedText: [],
          tinyText: [],
          rawMarkdownSignals: [],
          interactiveOverlaps: [],
          h1Count: 0,
        };
        let navigationError = '';

        try {
          await page.emulateMedia({ reducedMotion: 'reduce' });
          const response = await page.goto(`${baseUrl}${route}`, { waitUntil: 'domcontentloaded', timeout: 20_000 });
          status = response?.status() || 0;
          await page.addStyleTag({ content: '*,*::before,*::after{animation-duration:.001s!important;animation-delay:0s!important;transition-duration:.001s!important;scroll-behavior:auto!important}' });
          await page.evaluate(async () => { if (document.fonts?.ready) await document.fonts.ready; });
          await page.waitForTimeout(300);
          audit = await auditPage(page, viewport);
          screenshot = `${viewport.name}/${slugifyRoute(route)}.png`;
          try {
            await page.screenshot({ path: resolve(outputDir, screenshot), fullPage: true, animations: 'disabled' });
          } catch (error) {
            consoleErrors.push(`Full-page screenshot failed: ${error.message}`);
            await page.screenshot({ path: resolve(outputDir, screenshot), fullPage: false, animations: 'disabled' });
          }
        } catch (error) {
          navigationError = error.message;
          pageErrors.push(error.message);
        }

        const result = {
          route,
          viewport: viewport.name,
          status,
          screenshot,
          navigationError,
          pageErrors,
          consoleErrors: consoleErrors.slice(0, 20),
          audit,
        };
        result.failures = buildFailureSummary(result);
        if (audit.rawMarkdownSignals?.length) result.failures.push(...audit.rawMarkdownSignals);
        if (audit.h1Count === 0 && status > 0 && status < 400) result.failures.push('no H1 found');
        report.results.push(result);
        await page.close();
      }
      await context.close();
    }
  } finally {
    if (browser) await browser.close();
    await new Promise((resolveClosed) => server.close(resolveClosed));
  }

  const failures = report.results.flatMap((result) => result.failures.map((failure) => ({
    route: result.route,
    viewport: result.viewport,
    failure,
  })));
  report.summary = {
    checked: report.results.length,
    failedChecks: failures.length,
    warningCounts: {
      clippedText: report.results.reduce((sum, result) => sum + (result.audit.clippedText?.length || 0), 0),
      tinyText: report.results.reduce((sum, result) => sum + (result.audit.tinyText?.length || 0), 0),
      consoleErrors: report.results.reduce((sum, result) => sum + result.consoleErrors.length, 0),
    },
  };

  await writeFile(resolve(outputDir, 'report.json'), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
  const md = [
    '# Visual smoke test',
    '',
    `Checked ${report.summary.checked} route/viewport combinations.`,
    `Failures: ${report.summary.failedChecks}.`,
    '',
    ...(failures.length
      ? ['## Failures', '', ...failures.map((item) => `- \`${item.viewport}\` \`${item.route}\`: ${item.failure}`)]
      : ['No blocking visual-layout failures detected.']),
    '',
    `Warnings: clipped text ${report.summary.warningCounts.clippedText}, tiny text ${report.summary.warningCounts.tinyText}, console errors ${report.summary.warningCounts.consoleErrors}.`,
    '',
  ].join('\n');
  await writeFile(resolve(outputDir, 'report.md'), md, 'utf8');

  console.log(md.trim());
  if (failures.length) process.exitCode = 1;
}

main().catch((error) => {
  console.error(`Visual smoke test could not run: ${error.stack || error.message}`);
  process.exitCode = 2;
});
