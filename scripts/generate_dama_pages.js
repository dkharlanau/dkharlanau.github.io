#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const repoRoot = process.cwd();
const datasetsDir = path.join(repoRoot, "datasets", "DAMA");
const outputDir = path.join(repoRoot, "docs", "dama");
const tagsDir = path.join(outputDir, "tags");
const assetsDir = path.join(outputDir, "assets");

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function slugifyTag(tag) {
  return String(tag)
    .toLowerCase()
    .trim()
    .replace(/\s+/g, "-")
    .replace(/[^a-z0-9\-]/g, "")
    .replace(/\-+/g, "-")
    .replace(/^\-+|\-+$/g, "");
}

function truncateDescription(text, maxLength) {
  const clean = String(text || "")
    .replace(/\s+/g, " ")
    .trim();
  if (clean.length <= maxLength) return clean;
  return clean.slice(0, maxLength - 1).trimEnd() + "…";
}

function pickDescription(data) {
  const meta = data.meta || {};
  const candidates = [
    meta.summary,
    data.decision_question,
    data.title,
  ];
  const chosen = candidates.find((value) => value && String(value).trim());
  return truncateDescription(chosen || "DAMA decision block", 160);
}

function resolveSlug(fileName, data) {
  const canonical = data?.meta?.canonical_url;
  if (canonical) {
    try {
      const url = new URL(canonical);
      const base = path.basename(url.pathname);
      return base.replace(/\.json$/i, "");
    } catch (error) {
      // fall through
    }
  }
  return path.basename(fileName, path.extname(fileName));
}

function resolveBaseSite(data) {
  const meta = data.meta || {};
  const links = meta.links || {};
  const creator = meta.creator || {};
  return (
    links.website ||
    creator.website ||
    meta.website ||
    ""
  ).replace(/\/$/, "");
}

function buildAbsoluteUrl(siteBase, pathValue) {
  return siteBase ? `${siteBase}${pathValue}` : pathValue;
}

function renderList(items) {
  if (!items || items.length === 0) return "<p class=\"muted\">None.</p>";
  return `<ul>${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`;
}

function renderKeyValueTable(items) {
  if (!items || items.length === 0) return "<p class=\"muted\">None.</p>";
  const keys = Array.from(
    new Set(items.flatMap((item) => Object.keys(item || {})))
  );
  return `
<table>
  <thead>
    <tr>${keys.map((key) => `<th>${escapeHtml(key)}</th>`).join("")}</tr>
  </thead>
  <tbody>
    ${items
      .map((item) =>
        `<tr>${keys
          .map((key) => `<td>${escapeHtml(item?.[key] ?? "")}</td>`)
          .join("")}</tr>`
      )
      .join("")}
  </tbody>
</table>`;
}

function renderDefinitionList(obj) {
  if (!obj || Object.keys(obj).length === 0) return "<p class=\"muted\">None.</p>";
  const rows = Object.entries(obj).map(([key, value]) => {
    const rendered = Array.isArray(value)
      ? renderList(value)
      : value && typeof value === "object"
      ? renderDefinitionList(value)
      : `<p>${escapeHtml(value)}</p>`;
    return `<dt>${escapeHtml(key)}</dt><dd>${rendered}</dd>`;
  });
  return `<dl>${rows.join("")}</dl>`;
}

function renderJsonDetails(label, value) {
  const json = escapeHtml(JSON.stringify(value, null, 2));
  return `
<details class="json-block">
  <summary>${escapeHtml(label)}</summary>
  <pre><code>${json}</code></pre>
</details>`;
}

function renderTags(tags, basePath) {
  if (!tags || tags.length === 0) return "<p class=\"muted\">None.</p>";
  return `
<div class="tags">
  ${tags
    .map((tag) => {
      const slug = slugifyTag(tag);
      return `<a class="tag" href="${basePath}tags/${slug}.html">${escapeHtml(tag)}</a>`;
    })
    .join("")}
</div>`;
}

function renderBreadcrumb(title, basePath) {
  return `
<nav class="breadcrumb">
  <a href="${basePath}index.html">DAMA</a>
  <span>/</span>
  <span>${escapeHtml(title)}</span>
</nav>`;
}

function renderSectionAnchor(id, title) {
  return `
<h2 id="${escapeHtml(id)}">
  <a class="anchor" href="#${escapeHtml(id)}">#</a>
  ${escapeHtml(title)}
</h2>`;
}

function renderDecisionPage(data, slug) {
  const title = data.title || slug;
  const description = pickDescription(data);
  const baseSite = resolveBaseSite(data);
  const canonicalPath = `/docs/dama/${slug}.html`;
  const canonicalUrl = baseSite ? `${baseSite}${canonicalPath}` : canonicalPath;
  const creatorName = data?.meta?.creator?.name || "";
  const tags = Array.isArray(data.tags) ? data.tags.slice().sort() : [];
  const createdAt = data?.meta?.created_at_utc || "";
  const updatedAt = data?.meta?.updated_at_utc || "";

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: title,
    description,
    keywords: tags.join(", "),
    datePublished: createdAt || undefined,
    dateModified: updatedAt || undefined,
    url: canonicalUrl,
    author: creatorName
      ? {
          "@type": "Person",
          name: creatorName,
        }
      : undefined,
  };

  const basePath = "./";

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>${escapeHtml(title)} | DAMA</title>
  <meta name="description" content="${escapeHtml(description)}" />
  <link rel="canonical" href="${escapeHtml(canonicalUrl)}" />
  <meta property="og:title" content="${escapeHtml(title)}" />
  <meta property="og:description" content="${escapeHtml(description)}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="${escapeHtml(canonicalUrl)}" />
  <meta property="og:site_name" content="DAMA" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="${escapeHtml(title)}" />
  <meta name="twitter:description" content="${escapeHtml(description)}" />
  <link rel="stylesheet" href="${basePath}assets/dama.css" />
  <script type="application/ld+json">${escapeHtml(JSON.stringify(jsonLd))}</script>
</head>
<body>
  <div class="page">
    ${renderBreadcrumb(title, basePath)}
    <header>
      <p class="eyebrow">DAMA Decision Block</p>
      <h1>${escapeHtml(title)}</h1>
      <p class="lead">${escapeHtml(description)}</p>
      <div class="meta">
        ${creatorName ? `<span>Creator: ${escapeHtml(creatorName)}</span>` : ""}
        ${createdAt ? `<span>Created: ${escapeHtml(createdAt)}</span>` : ""}
        ${updatedAt ? `<span>Updated: ${escapeHtml(updatedAt)}</span>` : ""}
      </div>
      ${renderTags(tags, basePath)}
    </header>

    <section>
      ${renderSectionAnchor("decision-question", "Decision Question")}
      <p>${escapeHtml(data.decision_question || "")}</p>
      ${renderJsonDetails("JSON snippet", data.decision_question || "")}
    </section>

    <section>
      ${renderSectionAnchor("context", "Context")}
      ${renderDefinitionList(data.context || {})}
      ${renderJsonDetails("JSON snippet", data.context || {})}
    </section>

    <section>
      ${renderSectionAnchor("inputs", "Inputs")}
      ${renderDefinitionList(data.inputs || {})}
      ${renderJsonDetails("JSON snippet", data.inputs || {})}
    </section>

    <section>
      ${renderSectionAnchor("options", "Options")}
      <div class="cards">
        ${(data.options || [])
          .map((option) => {
            const tradeoffs = renderList(option.tradeoffs || []);
            return `
<div class="card">
  <h3>${escapeHtml(option.id || "")}. ${escapeHtml(option.name || "Option")}</h3>
  <p>${escapeHtml(option.summary || "")}</p>
  <h4>Tradeoffs</h4>
  ${tradeoffs}
  ${renderJsonDetails("JSON snippet", option)}
</div>`;
          })
          .join("")}
      </div>
    </section>

    <section>
      ${renderSectionAnchor("decision-logic", "Decision Logic")}
      <h3>Preferred Option Rules</h3>
      ${(data.decision_logic?.preferred_option_rules || [])
        .map((rule) => {
          return `
<div class="rule">
  <p class="rule-title">If</p>
  ${renderList(rule.if || [])}
  <p class="rule-title">Then</p>
  <p>${escapeHtml(rule.then || "")}</p>
</div>`;
        })
        .join("")}
      <h3>Anti-patterns to Avoid</h3>
      ${renderList(data.decision_logic?.anti_patterns_to_avoid || [])}
      <h3>Exceptions Flow</h3>
      ${renderList(data.decision_logic?.exceptions_flow || [])}
      ${renderJsonDetails("JSON snippet", data.decision_logic || {})}
    </section>

    <section>
      ${renderSectionAnchor("controls-enforcement", "Controls & Enforcement")}
      <h3>Policies</h3>
      ${renderKeyValueTable(data.controls_enforcement?.policies || [])}
      <h3>Standards</h3>
      ${renderKeyValueTable(data.controls_enforcement?.standards || [])}
      <h3>Technical Controls</h3>
      ${renderList(data.controls_enforcement?.technical_controls || [])}
      ${renderJsonDetails("JSON snippet", data.controls_enforcement || {})}
    </section>

    <section>
      ${renderSectionAnchor("metrics", "Metrics")}
      <h3>Operational</h3>
      ${renderKeyValueTable(data.metrics?.operational || [])}
      <h3>Data Quality Dimensions</h3>
      ${renderList(data.metrics?.data_quality_dimensions || [])}
      <h3>Governance Health</h3>
      ${renderKeyValueTable(data.metrics?.governance_health || [])}
      ${renderJsonDetails("JSON snippet", data.metrics || {})}
    </section>

    <section>
      ${renderSectionAnchor("examples", "Examples")}
      ${(data.examples_generic || [])
        .map((example) => `
<div class="example">
  <p><strong>Scenario:</strong> ${escapeHtml(example.scenario || "")}</p>
  <p><strong>Application:</strong> ${escapeHtml(example.application || "")}</p>
  ${renderJsonDetails("JSON snippet", example)}
</div>`)
        .join("")}
    </section>

    <footer>
      <a href="${basePath}index.html">Back to DAMA index</a>
    </footer>
  </div>
</body>
</html>`;
}

function renderIndexPage(items, siteBase) {
  const basePath = "./";
  const tags = Array.from(new Set(items.flatMap((item) => item.tags || []))).sort();
  const canonicalPath = "/docs/dama/index.html";
  const canonicalUrl = buildAbsoluteUrl(siteBase, canonicalPath);
  const indexJsonLd = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: "DAMA Decision Blocks",
    url: canonicalUrl,
    description: "DAMA decision blocks index.",
    isPartOf: buildAbsoluteUrl(siteBase, "/"),
    mainEntity: items.map((item) => ({
      "@type": "CreativeWork",
      name: item.title,
      url: buildAbsoluteUrl(siteBase, `/docs/dama/${item.slug}.html`),
    })),
  };
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>DAMA Index</title>
  <meta name="description" content="DAMA decision blocks index." />
  <link rel="canonical" href="${escapeHtml(canonicalUrl)}" />
  <meta property="og:title" content="DAMA Index" />
  <meta property="og:description" content="DAMA decision blocks index." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="${escapeHtml(canonicalUrl)}" />
  <meta name="twitter:card" content="summary" />
  <link rel="stylesheet" href="${basePath}assets/dama.css" />
  <script type="application/ld+json">${JSON.stringify(indexJsonLd)}</script>
</head>
<body>
  <div class="page">
    <header>
      <p class="eyebrow">DAMA</p>
      <h1>DAMA Decision Blocks</h1>
      <p class="lead">Browse decision blocks, filter by tag, or search by keyword.</p>
    </header>

    <section class="filters">
      <input id="search" type="search" placeholder="Search by title or decision question" />
      <select id="tagFilter">
        <option value="">All tags</option>
        ${tags.map((tag) => `<option value="${escapeHtml(tag)}">${escapeHtml(tag)}</option>`).join("")}
      </select>
    </section>

    <section>
      <div id="results" class="cards"></div>
    </section>
  </div>

  <script>
    const items = ${JSON.stringify(items)};
    const resultsEl = document.getElementById('results');
    const searchEl = document.getElementById('search');
    const tagFilterEl = document.getElementById('tagFilter');

    function escapeHtml(value) {
      return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/\"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }

    function renderItems(list) {
      if (!list.length) {
        resultsEl.innerHTML = '<p class="muted">No matches.</p>';
        return;
      }
      resultsEl.innerHTML = list.map(item => {
        const tagsHtml = item.tags.map(tag => {
          return '<a class=\"tag\" href=\"' + basePath + 'tags/' + slugifyTagPlaceholder(tag) + '.html\">' + escapeHtml(tag) + '</a>';
        }).join('');
        return '<div class=\"card\">' +
          '<h3><a href=\"' + basePath + item.slug + '.html\">' + escapeHtml(item.title) + '</a></h3>' +
          '<p>' + escapeHtml(item.description) + '</p>' +
          '<div class=\"tags\">' + tagsHtml + '</div>' +
        '</div>';
      }).join('');
    }

    function slugifyTagPlaceholder(tag) {
      return String(tag)
        .toLowerCase()
        .trim()
        .replace(/\s+/g, '-')
        .replace(/[^a-z0-9\-]/g, '')
        .replace(/\-+/g, '-')
        .replace(/^\-+|\-+$/g, '');
    }

    function filterItems() {
      const query = searchEl.value.trim().toLowerCase();
      const tag = tagFilterEl.value;
      const filtered = items.filter(item => {
        const haystack = (String(item.title) + ' ' + String(item.decision_question)).toLowerCase();
        const matchesQuery = !query || haystack.includes(query);
        const matchesTag = !tag || item.tags.includes(tag);
        return matchesQuery && matchesTag;
      });
      renderItems(filtered);
    }

    searchEl.addEventListener('input', filterItems);
    tagFilterEl.addEventListener('change', filterItems);

    renderItems(items);
  </script>
</body>
</html>`;
}

function renderTagPage(tag, items, siteBase) {
  const basePath = "../";
  const canonicalPath = `/docs/dama/tags/${slugifyTag(tag)}.html`;
  const canonicalUrl = buildAbsoluteUrl(siteBase, canonicalPath);
  const tagJsonLd = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: `DAMA Tag: ${tag}`,
    url: canonicalUrl,
    description: `DAMA decision blocks tagged ${tag}.`,
    isPartOf: buildAbsoluteUrl(siteBase, "/docs/dama/index.html"),
    mainEntity: items.map((item) => ({
      "@type": "CreativeWork",
      name: item.title,
      url: buildAbsoluteUrl(siteBase, `/docs/dama/${item.slug}.html`),
    })),
  };
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>DAMA Tag: ${escapeHtml(tag)}</title>
  <meta name="description" content="DAMA decision blocks tagged ${escapeHtml(tag)}." />
  <link rel="canonical" href="${escapeHtml(canonicalUrl)}" />
  <meta property="og:title" content="DAMA Tag: ${escapeHtml(tag)}" />
  <meta property="og:description" content="DAMA decision blocks tagged ${escapeHtml(tag)}." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="${escapeHtml(canonicalUrl)}" />
  <meta name="twitter:card" content="summary" />
  <link rel="stylesheet" href="${basePath}assets/dama.css" />
  <script type="application/ld+json">${JSON.stringify(tagJsonLd)}</script>
</head>
<body>
  <div class="page">
    <nav class="breadcrumb">
      <a href="${basePath}index.html">DAMA</a>
      <span>/</span>
      <span>${escapeHtml(tag)}</span>
    </nav>

    <header>
      <p class="eyebrow">Tag</p>
      <h1>${escapeHtml(tag)}</h1>
      <p class="lead">${items.length} decision block${items.length === 1 ? "" : "s"} tagged.</p>
    </header>

    <section>
      <div class="cards">
        ${items
          .map(
            (item) => `
<div class="card">
  <h3><a href="${basePath}${item.slug}.html">${escapeHtml(item.title)}</a></h3>
  <p>${escapeHtml(item.description)}</p>
  <div class="tags">
    ${item.tags
      .map(
        (itemTag) => `<a class="tag" href="${basePath}tags/${slugifyTag(itemTag)}.html">${escapeHtml(itemTag)}</a>`
      )
      .join("")}
  </div>
</div>`
          )
          .join("")}
      </div>
    </section>

    <footer>
      <a href="${basePath}index.html">Back to DAMA index</a>
    </footer>
  </div>
</body>
</html>`;
}

function buildItems(dataEntries) {
  return dataEntries.map(({ data, slug }) => {
    return {
      title: data.title || slug,
      slug,
      description: pickDescription(data),
      tags: Array.isArray(data.tags) ? data.tags.slice().sort() : [],
      decision_question: data.decision_question || "",
    };
  });
}

function buildCss() {
  return `:root {
  color-scheme: light;
  --bg: #ffffff;
  --text: #1f2933;
  --muted: #55606a;
  --border: #e2e8f0;
  --accent: #2b6cb0;
  --accent-soft: #ebf4ff;
  --code-bg: #f7fafc;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}

.page {
  max-width: 980px;
  margin: 0 auto;
  padding: 32px 24px 64px;
}

header {
  margin-bottom: 32px;
}

h1, h2, h3, h4 {
  margin: 0 0 12px;
  line-height: 1.3;
}

h2 { margin-top: 32px; }

p { margin: 0 0 12px; }

.lead {
  font-size: 1.1rem;
  color: var(--muted);
}

.eyebrow {
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 8px;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.9rem;
  margin-bottom: 20px;
  color: var(--muted);
}

.breadcrumb a {
  color: var(--accent);
  text-decoration: none;
}

.meta {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 0.9rem;
  color: var(--muted);
  margin: 16px 0;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  background: var(--accent-soft);
  color: var(--accent);
  text-decoration: none;
  font-size: 0.85rem;
  border: 1px solid rgba(43, 108, 176, 0.2);
}

.anchor {
  font-size: 0.8rem;
  color: var(--accent);
  text-decoration: none;
  margin-right: 8px;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 16px;
}

.card {
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  background: #fff;
}

.rule {
  border-left: 3px solid var(--accent);
  padding: 12px 16px;
  margin: 16px 0;
  background: #f9fbff;
}

.rule-title {
  font-weight: 600;
  margin-bottom: 8px;
}

dl {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 12px 24px;
  margin: 0;
}

dt {
  font-weight: 600;
}

dd {
  margin: 0;
}

ul {
  padding-left: 18px;
  margin: 0 0 12px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 16px;
}

table th,
table td {
  border: 1px solid var(--border);
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
}

table th {
  background: #f5f7fa;
}

.json-block {
  margin: 12px 0 0;
}

pre {
  background: var(--code-bg);
  padding: 12px;
  border-radius: 8px;
  overflow: auto;
  border: 1px solid var(--border);
}

code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.85rem;
}

.filters {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

input[type="search"],
select {
  padding: 10px 12px;
  border: 1px solid var(--border);
  border-radius: 8px;
  min-width: 220px;
}

.muted {
  color: var(--muted);
}

footer {
  margin-top: 40px;
}
`;
}

function main() {
  if (!fs.existsSync(datasetsDir)) {
    console.error(`Missing datasets dir: ${datasetsDir}`);
    process.exit(1);
  }

  const files = fs
    .readdirSync(datasetsDir)
    .filter((file) => file.endsWith(".json"))
    .sort((a, b) => a.localeCompare(b));

  const entries = files.map((fileName) => {
    const filePath = path.join(datasetsDir, fileName);
    const raw = fs.readFileSync(filePath, "utf8");
    const data = JSON.parse(raw);
    const slug = resolveSlug(fileName, data);
    return { fileName, data, slug };
  });

  const siteBase =
    entries.map((entry) => resolveBaseSite(entry.data)).find((value) => value) || "";
  const items = buildItems(entries).sort((a, b) => a.title.localeCompare(b.title));

  fs.rmSync(outputDir, { recursive: true, force: true });
  ensureDir(outputDir);
  ensureDir(tagsDir);
  ensureDir(assetsDir);

  fs.writeFileSync(path.join(assetsDir, "dama.css"), buildCss(), "utf8");

  for (const entry of entries) {
    const html = renderDecisionPage(entry.data, entry.slug);
    fs.writeFileSync(path.join(outputDir, `${entry.slug}.html`), html, "utf8");
  }

  fs.writeFileSync(path.join(outputDir, "index.html"), renderIndexPage(items, siteBase), "utf8");

  const tagMap = new Map();
  for (const item of items) {
    for (const tag of item.tags || []) {
      if (!tagMap.has(tag)) tagMap.set(tag, []);
      tagMap.get(tag).push(item);
    }
  }

  const sortedTags = Array.from(tagMap.keys()).sort((a, b) => a.localeCompare(b));
  for (const tag of sortedTags) {
    const tagItems = tagMap.get(tag) || [];
    const tagPage = renderTagPage(tag, tagItems, siteBase);
    fs.writeFileSync(path.join(tagsDir, `${slugifyTag(tag)}.html`), tagPage, "utf8");
  }

  console.log(`Generated ${entries.length} DAMA pages, ${sortedTags.length} tag pages.`);
}

main();
