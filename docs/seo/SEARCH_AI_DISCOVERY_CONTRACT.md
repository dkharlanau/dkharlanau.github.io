# Search and AI Discovery Trust Contract

**Version:** 1.0  
**Date:** 2026-06-08  
**Scope:** `dkharlanau.github.io` — public discovery layer for search engines and AI crawlers  
**Canonical:** `https://dkharlanau.github.io/docs/seo/SEARCH_AI_DISCOVERY_CONTRACT.md`

---

## 1. Purpose

This contract defines the rules for which pages enter public discovery surfaces (sitemap, structured data, llms files) and which must stay excluded. It governs how `verified`, `robots`, `sitemap`, `source_confidence`, and `last_reviewed` interact, and it documents the AI crawler policy.

The goal is a **robust discovery/trust layer using standard mechanisms** — sitemap, robots.txt, structured data, and existing llms files — without creating non-standard "AI sitemaps" or treating robots.txt as the only protection for private content.

---

## 2. Sitemap Inclusion Rules

### 2.1 Pages that MAY enter sitemap

A page is eligible for the public sitemap **only if all** of the following are true:

1. `sitemap` frontmatter is not `false` (default: include unless explicitly excluded).
2. `robots` frontmatter does **not** contain `noindex`.
3. The page has a canonical, stable permalink.
4. For **Atlas pages** only: `verified: true` **and** `status: reviewed`.
5. For **Research pages** (under `/research/`): **never** included, regardless of frontmatter. Research is a noindex working area by design.
6. The page is not a generated sitemap, feed, or 404 file.

### 2.2 Pages that MUST stay excluded

| Category | Rule |
|----------|------|
| Draft / unverified Atlas | `verified: false` or `status != reviewed` → exclude |
| Research / watchlists / briefs | `/research/**` → exclude unconditionally |
| Noindex pages | `robots` contains `noindex` → exclude |
| Sitemap:false pages | `sitemap: false` → exclude |
| Private paths | `/DAMA/`, `/agentic-bytes/`, `/TRIZ-bytes/`, `/LLM-prompts/` → already blocked in robots.txt, also exclude from sitemap |
| Generated files | `sitemap.xml`, `sitemap-pages.xml`, `sitemap-data.xml`, `sitemap-atlas.xml`, `feed.xml`, `404.html` → exclude |
| Template / docs pages | `/docs/templates/`, `/docs/routing-contract.md`, etc. → exclude via `sitemap: false` or Jekyll exclude |

### 2.3 Lastmod policy

- `<lastmod>` is added **only** from reliable source data:
  - `last_modified_at` frontmatter
  - `date` frontmatter (for posts/notes)
  - `updated` frontmatter
  - `last_reviewed` frontmatter
- **Do not invent dates.** If no reliable date exists, omit `<lastmod>`.
- **Do not add `<changefreq>` or `<priority>`** unless already used and meaningful. The existing sitemap removes these where unsupported.

---

## 3. Sitemap Architecture

### 3.1 Sitemap index

`sitemap.xml` is the sitemap index. It references section sitemaps:

```xml
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap><loc>https://dkharlanau.github.io/sitemap-pages.xml</loc></sitemap>
  <sitemap><loc>https://dkharlanau.github.io/sitemap-data.xml</loc></sitemap>
  <sitemap><loc>https://dkharlanau.github.io/sitemap-atlas.xml</loc></sitemap>
</sitemapindex>
```

### 3.2 Section sitemaps

| Sitemap | Contents | Inclusion logic |
|---------|----------|-----------------|
| `sitemap-pages.xml` | All indexable pages, collections, posts | `sitemap != false`, `robots` lacks `noindex`, Atlas pages must be `verified: true` + `status: reviewed` |
| `sitemap-data.xml` | Machine-readable data files (resume, principles, catalog, datasets manifest, etc.) | Hardcoded list of stable data endpoints |
| `sitemap-atlas.xml` | Verified Atlas pages only | `verified: true`, `status: reviewed`, `sitemap != false`, `robots` lacks `noindex` |

### 3.3 Removed / deprecated

- `ai/sitemap.xml` with custom `ai:` namespace is **non-standard** and has been removed from the sitemap index. The AI discovery layer is served through `llms.txt`, `llms-full.txt`, and `atlas/manifest.json` instead.

---

## 4. LLMs Files vs. Sitemap

| Surface | Purpose | Inclusion scope |
|---------|---------|-----------------|
| `sitemap.xml` / section sitemaps | Search engine crawling and indexability | Only canonical, indexable, public pages |
| `llms.txt` | AI agent discovery manifest — machine-readable entry points | Static list of machine endpoints (resume, catalog, discovery map, etc.) |
| `llms-full.txt` | Full-text corpus for RAG / retrieval | **Only verified + reviewed Atlas pages** (14 pages as of 2026-06-08). Draft/unverified pages are excluded. Source file paths are never exposed. |
| `atlas/manifest.json` | Machine-readable index of all Atlas pages | All Atlas pages (verified and unverified) with metadata. Unverified pages are marked `verified: false`. |

**Key distinction:** sitemap drives search indexing; llms files drive AI retrieval. A page can be in `atlas/manifest.json` (for discovery) without being in `sitemap.xml` (if it is noindex) and without being in `llms-full.txt` (if unverified).

---

## 5. AI Crawler Policy (robots.txt)

### 5.1 Current policy

| Bot | Directive | Rationale |
|-----|-----------|-----------|
| `OAI-SearchBot` | `Allow: /` | ChatGPT Search visibility is desired |
| `ChatGPT-User` | `Allow: /` | User-facing ChatGPT browsing |
| `GPTBot` | `Disallow: /` | Training crawler blocked; search bot is separate |
| `Claude-SearchBot` | `Allow: /` | Claude search visibility desired |
| `Claude-User` | `Allow: /` | User-facing Claude browsing |
| `ClaudeBot` | `Disallow: /` | Training crawler blocked |
| `Google-Extended` | `Disallow: /` | Training crawler blocked |
| `PerplexityBot` | `Allow: /` | Search visibility desired |
| `CCBot` | `Allow: /` | Common Crawl allowed (used for retrieval, not training here) |
| `FacebookBot` | `Allow: /` | Meta search/retrieval visibility |
| `*` (default) | `Allow: /` | General search crawling allowed for public content |

### 5.2 Content-Signal header

`robots.txt` includes:

```
Content-Signal: ai-train=no, search=yes, ai-input=yes
```

This is an **informational signal**, not an enforceable directive. It communicates:
- `ai-train=no`: Do not use for model training without permission.
- `search=yes`: Search indexing is welcome.
- `ai-input=yes`: AI retrieval and user-directed answering is allowed.

### 5.3 Safety note

`robots.txt` is **not** the only protection for private content. Private/draft paths are also:
- Excluded from sitemap
- Marked `noindex` in page meta tags
- Kept outside the public Jekyll build via `_config.yml` `exclude`
- Not linked from public navigation

---

## 6. Structured Data (JSON-LD)

### 6.1 Site-wide types

| Type | Where | Source |
|------|-------|--------|
| `WebSite` | Every page (`_includes/head.html`) | Hardcoded site metadata |
| `Person` | About/profile pages (`_includes/seo/structured-data.html`) | `_data/resume.yml` |
| `Organization` | About/profile pages (if `worksFor` present) | `_data/resume.yml` schema |

### 6.2 Per-page types

| Page type | JSON-LD type | BreadcrumbList |
|-----------|--------------|----------------|
| Atlas article | `TechArticle` (or `Article` if `TechArticle` unsupported) | Yes — Home → Atlas → Section → Page |
| Notes / Blog post | `Article` | Yes — Home → Notes/Blog → Page |
| Index/list pages | `CollectionPage` | Yes — Home → Section |
| Dataset catalog | `DataCatalog` | Yes — Home → Datasets |
| About / Profile | `ProfilePage` + `Person` | Yes — Home → About |
| All other pages | `WebPage` | Yes (where applicable) |

### 6.3 Rules

- JSON-LD must **reflect visible page content**. No fake ratings, reviews, offers, or organization claims.
- No fake `sameAs` links. Only links present in `resume.yml` schema are emitted.
- No structured data on noindex pages **unless** the project already allows it and it does not imply indexing. The current `_includes/seo/structured-data.html` wraps schema in `{% raw %}{% if allow_indexing %}{% endraw %}`.
- Prefer shared includes/layouts over duplicated page-by-page markup.

---

## 7. Atlas Page Structured Data Detail

Atlas pages receive:

1. `TechArticle` (or `Article`) with:
   - `headline`: page title
   - `description`: page description
   - `author`: `Person` → Dzmitryi Kharlanau
   - `datePublished`: `last_reviewed` or `date`
   - `dateModified`: `last_modified_at` or `updated`
   - `publisher`: same as author (personal site)
   - `about`: linked to `Thing` with `name` = domain / concept_type
   - `keywords`: tags array

2. `BreadcrumbList` with:
   - Home (`/`)
   - Knowledge Atlas (`/atlas/`)
   - Section (`/atlas/{section}/`)
   - Current page

3. `CreativeWork` (optional, for broader compatibility) is not added separately; `TechArticle` is sufficient.

---

## 8. Discovery Audit and IndexNow Workflow

### 8.1 Post-build discovery audit

After Jekyll builds `_site/`, run the discovery audit to validate that the built output contains only intended discovery surfaces:

```bash
# Strict mode (default) — fails on any violation
python3 scripts/audit_discovery_outputs.py _site

# Safe CI mode — reports violations but exits 0 if all are baselined
python3 scripts/audit_discovery_outputs.py _site --warn-only
```

The audit checks:
- Sitemap validity (well-formed XML, correct namespace, no duplicate entries)
- Canonical URL consistency (all sitemap URLs use `https://dkharlanau.github.io/`)
- Noindex leak detection (no `noindex` pages appear in sitemap)
- Private path leak detection (no `/research/`, `/DAMA/`, `/agentic-bytes/`, `/TRIZ-bytes/`, `/LLM-prompts/` in sitemap)
- JSON-LD validity (no malformed structured data in built HTML)
- Fake schema field detection (no invented ratings, reviews, or organization claims)

**Baseline mode:** Pre-existing known violations are documented in `data/seo/discovery-audit-baseline.json`. In `--warn-only` mode, baselined violations are reported as `[KNOWN]` but do not block CI. **New violations not in the baseline still fail** even in warn-only mode.

Run this **after** `bundle exec jekyll build` and **before** any real IndexNow submission. In CI, it runs automatically on every push to `main` as part of the dry-run workflow in `--warn-only` mode.

### 8.2 IndexNow dry-run-first workflow

IndexNow submission follows a **dry-run-first, manual-submit-only** policy:

1. **Default is dry-run.** `python3 scripts/indexnow_submit.py` (no flags) prints the URLs that would be submitted without making any network request.
2. **Real submission requires `--submit`.** Explicit opt-in prevents accidental bulk notifies.
3. **GitHub workflow runs dry-run on every push.** `.github/workflows/indexnow-dry-run.yml` executes the script in dry-run mode automatically.
4. **Real submission is manual only.** Use `workflow_dispatch` with `submit: true` to trigger a real submission. This requires the `INDEXNOW_KEY` repository secret.

### 8.3 IndexNow safety confirmations

- **No automatic real submission in CI.** The push-triggered workflow never passes `--submit`.
- **Changed-URL targeting by default.** Manual dispatch uses `--from-git-diff` to submit only URLs affected by the latest commit range, minimizing noise.
- **Batch limits.** `--max-urls N` caps the submission batch; overflow exits without submitting.
- **Key verification.** `--require-key-file` confirms the verification `.txt` file is present at the site root before any network request.
- **Indexability gate.** The script enforces the same rules as sitemap inclusion (see §2.1). Noindex, draft, research, unverified Atlas, and private paths are never submitted.

### 8.4 IndexNow scope and limitations

- IndexNow notifies Bing, Yandex, Seznam.cz, and other participating engines.
- **Google does not participate in IndexNow.** It is not a Google indexing guarantee.
- Use IndexNow as a supplementary signal, not a replacement for sitemap hygiene, canonical quality, or structured-data correctness.

---

## 9. Validation Commands

Run these in order before committing:

```bash
# 1. Public repo hygiene (secrets, disallowed paths)
python3 scripts/check_public_repo.py

# 2. Atlas artifact consistency
python3 scripts/generate_atlas_artifacts.py --check

# 3. Build the site
bundle exec jekyll build

# 4. Post-build discovery audit (sitemap, canonical, noindex leaks, JSON-LD)
python3 scripts/audit_discovery_outputs.py _site

# 4a. Safe CI mode — report violations but do not block if baselined
python3 scripts/audit_discovery_outputs.py _site --warn-only

# 4b. Explicit strict mode — fail on any violation
python3 scripts/audit_discovery_outputs.py _site --strict

# 5. SEO metadata in built HTML
python3 scripts/check_seo.py _site

# 6. Broken link check
python3 scripts/check_links.py _site

# 7. Sitemap / robots / structured-data tests
pytest tests/test_seo_discovery.py -v

# 8. All existing tests
pytest tests/ -v

# 9. Git whitespace check
git diff --check
```

If Jekyll is unavailable locally, rely on GitHub CI for the `_site`-dependent checks (`audit_discovery_outputs.py`, `check_seo.py`, `check_links.py`). Do not claim those passed locally.

---

## 10. Change Log

| Date | Change |
|------|--------|
| 2026-06-08 | v1.1 — Added discovery audit (`audit_discovery_outputs.py`), IndexNow dry-run-first workflow, manual real-submit gating, and updated validation pipeline |
| 2026-06-08 | v1.0 — Initial contract after sitemap architecture refactor, structured data additions, and IndexNow support |
