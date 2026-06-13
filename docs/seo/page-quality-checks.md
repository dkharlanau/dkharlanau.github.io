---
layout: default
title: "Page Quality Checks"
description: "Technical page-quality gate for built HTML on dkharlanau.github.io."
robots: noindex,follow
sitemap: false
---

{% raw %}

# Page Quality Checks

**Path:** `scripts/check_page_quality.py`  
**Purpose:** Strict, page-type-aware technical quality gate for built HTML.  
**Complements:** `scripts/check_seo.py`, `scripts/check_structured_data.py`.

This checker inspects every built HTML file in `_site/` and assigns it a page type. Rules and severity are applied per type, so a missing `<h1>` on a collection page is treated differently than on an article, and `noindex` review candidates are not held to the same metadata bar as published articles.

---

## 1. Page classification

| Type | How it is detected | Typical examples |
|---|---|---|
| `indexable_atlas_verified` | Path starts with `atlas/` and JSON-LD `@type` is `TechArticle` | Verified Atlas pages |
| `indexable_skill_hub` | Path starts with `skill-hub/` or JSON-LD `@type` is `Article` | Skill Hub pages and skill-group indexes |
| `indexable_collection` | JSON-LD `@type` is `CollectionPage` or path ends with `/index.html` | Section indexes, generated agent-skill listings |
| `indexable_dataset_detail` | Path starts with `datasets/` but is not the root index | Dataset detail pages |
| `indexable_service_or_profile` | Path contains `/about/`, `/cv/`, or `/services/` | Profile, CV, service pages |
| `indexable_article` | Default for remaining indexable pages | Notes, news, radar signals |
| `noindex_review_candidate` | `robots: noindex` and path is Atlas, Scenario, or Diagnostics | Draft Atlas/Scenario pages |
| `noindex_research_or_draft` | `robots: noindex` and path is Notes, Blog, News, Radar, or Research | Working notes, drafts |
| `utility_page` | `robots: noindex` and does not match above | Error pages, utility outputs |

---

## 2. Severity levels

- **critical** — Must be fixed before publishing. Causes `--fail-on-critical` to exit with code `2`.
- **warning** — Should be reviewed; currently allowed in CI.
- **info** — Advisory only (not currently emitted).

---

## 3. Critical rules

| Rule | Applies to | Meaning |
|---|---|---|
| `ARTICLE_TITLE_MISSING` | article-like pages | No `<title>` tag. |
| `ARTICLE_H1_MISSING` | article-like pages | No visible `<h1>`. |
| `ARTICLE_H1_DUPLICATE` | article-like pages | More than one `<h1>`. |
| `ARTICLE_H1_EMPTY` | article-like pages | `<h1>` is empty. |
| `ARTICLE_META_DESCRIPTION_MISSING` | article-like pages | No meta description. |
| `ARTICLE_META_DESCRIPTION_GENERIC` | article-like pages | Description is generic or shorter than 20 characters. |
| `ARTICLE_JSONLD_MISSING` | article-like pages | No `Article`/`TechArticle` JSON-LD. |
| `ARTICLE_AUTHOR_MISSING` | article-like pages | Article JSON-LD has no `author`. |
| `ARTICLE_AUTHOR_NAME_MISSING` | article-like pages | Article author has no `name` or `@id`. |
| `ARTICLE_PUBLISHER_MISSING` | article-like pages | Article JSON-LD has no `publisher`. |
| `ARTICLE_PUBLISHER_NAME_MISSING` | article-like pages | Article publisher has no `name` or `@id`. |
| `ARTICLE_DATE_ORDER_INVALID` | article-like pages | `dateModified` is earlier than `datePublished`. |
| `ARTICLE_CANONICAL_MISSING` | article-like pages | No canonical link. |
| `ARTICLE_CANONICAL_NOT_ABSOLUTE` | article-like pages | Canonical is not absolute HTTPS. |
| `ARTICLE_CANONICAL_LOCALHOST` | article-like pages | Canonical points to localhost. |
| `ARTICLE_OG_IMAGE_LOCALHOST` | article-like pages | Open Graph image points to localhost. |
| `ARTICLE_PLACEHOLDER_TEXT` | article-like pages | Placeholder text (`TODO`, `FIXME`, `TBD`, `lorem ipsum`, `coming soon`) outside documented weak-example contexts. |
| `ARTICLE_PLACEHOLDER_HEADING` | article-like pages | Heading contains `TODO`, `FIXME`, `PLACEHOLDER`, or `SECTION`. |
| `COLLECTION_TITLE_MISSING` | collection pages | No `<title>`. |
| `COLLECTION_H1_MISSING` | collection pages | No `<h1>`. |
| `COLLECTION_META_DESCRIPTION_MISSING` | collection pages | No meta description. |
| `COLLECTION_CANONICAL_MISSING` | collection pages | No canonical link. |
| `PRIVATE_PATH_LEAK` | all pages | Private path or local token appears outside `<code>`/`<pre>`/`<samp>`/`<kbd>` blocks or in a URL value (`href`, `src`, canonical, JSON-LD URL fields, etc.). |
| `LOCALHOST_URL` | all pages | A URL value contains `localhost`, `127.0.0.1`, or `0.0.0.0`. |
| `BROKEN_TEMPLATE_TOKEN` | all pages | Unrendered `{{` or `{%` tokens appear outside code blocks. |
| `NOINDEX_CANONICAL_LOCALHOST` | noindex pages | Canonical points to localhost. |
| `METADATA_TEMPLATE_TOKEN` | noindex pages | Title, description, or canonical contains unrendered template tokens. |

### Private-path patterns

The checker flags these literal patterns when they escape into public HTML or URL values:

- `/Users/`
- `.env.local`
- `Kimi_Agent_SAP Atlas Expansion`
- `Basic_LinkedInDataExport` / `Basic_LinkInDataExport`
- `li2resume.local`

Generic documentation terms such as "private-source" are intentionally ignored.

---

## 4. Warning rules

| Rule | Applies to | Meaning |
|---|---|---|
| `ARTICLE_TITLE_TOO_SHORT` / `ARTICLE_TITLE_TOO_LONG` | article-like pages | Title outside the 35–70 character sweet spot. |
| `ARTICLE_H1_TITLE_MISMATCH` | article-like pages | `<h1>` and `<title>` do not overlap. |
| `ARTICLE_HEADLINE_MISMATCH` | article-like pages | JSON-LD `headline` does not align with `<title>`. |
| `ARTICLE_DESCRIPTION_MISMATCH` | article-like pages | JSON-LD `description` does not align with meta description. |
| `ARTICLE_META_DESCRIPTION_SHORT` / `ARTICLE_META_DESCRIPTION_LONG` | article-like pages | Description outside 80–170 characters. |
| `ARTICLE_LEAD_MISSING` | article-like pages | No visible lead, subtitle, or summary block. |
| `ARTICLE_AUTHOR_NOT_VISIBLE` | article-like pages | Author is in JSON-LD but not rendered visibly. |
| `ARTICLE_CONTENT_TOO_THIN` | article-like pages | Fewer than 150 visible words. |
| `ARTICLE_NO_SECTION_HEADINGS` | article-like pages | 300+ words with no `h2`–`h6`. |
| `ARTICLE_NO_INTERNAL_LINKS` | article-like pages | 200+ words with no internal links. |
| `ARTICLE_OG_*_MISSING` | article-like pages | Missing Open Graph title, description, URL, or type. |
| `ARTICLE_TWITTER_CARD_MISSING` | article-like pages | Missing `twitter:card` meta tag. |
| `ARTICLE_OG_IMAGE_INSECURE` | article-like pages | OG image uses `http://`. |
| `COLLECTION_H1_DUPLICATE` | collection pages | More than one `<h1>` (collection pages are allowed one). |
| `COLLECTION_CONTENT_EMPTY` | collection pages | Very little content and no visible list/grid. |
| `NOINDEX_RICH_STRUCTURED_DATA` | noindex pages | Page emits Article/TechArticle/Product/etc. JSON-LD despite being `noindex`. |

---

## 5. Exemptions

### Code blocks

Content inside `<code>`, `<pre>`, `<samp>`, and `<kbd>` tags is ignored for placeholder and private-path checks. This lets documentation show example paths like `/Users/` or `.env.local` without raising false positives.

### Weak-example contexts

Placeholder patterns are allowed when they appear inside a documented weak/bad-example context. The checker scans ~200 characters around the match for terms such as:

- `weak output`, `bad example`, `poor example`
- `why this is weak`, `why it fails`, `anti-pattern`
- `example of`, `sample output`, `incorrect example`, `do not use`

---

## 6. How to run

### Default run (warnings shown, exit 0 unless critical)

```bash
python3 scripts/check_page_quality.py --site-dir _site
```

### Fail on critical (CI mode)

```bash
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
```

Exit codes:

- `0` — no critical findings (warnings may be present)
- `1` — missing `_site` directory or other runtime error
- `2` — one or more critical findings

### JSON output

```bash
python3 scripts/check_page_quality.py --site-dir _site --json > reports/page-quality.json
```

### Run the full validation suite

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_structured_data.py _site
python3 scripts/check_page_quality.py _site --fail-on-critical
```

---

## 7. Current baseline

As of the latest run on this branch:

- **Pages scanned:** 703
- **Critical findings:** 0
- **Warnings:** 167
- **Info:** 0

The remaining warnings are almost entirely `COLLECTION_H1_DUPLICATE` on auto-generated agent-skill collection pages (`/.well-known/agent-skills/...` and `/agent-skills/...`). These pages render both a section title and a list title as `<h1>`; they should be consolidated into a single `<h1>` in the generator template.

No critical private-path, localhost, broken-template, or missing-article-metadata issues remain.

---

## 8. When to update this document

Update this page when:

- New rules are added to `scripts/check_page_quality.py`.
- Page-type classification logic changes.
- The private-path pattern list changes.
- The baseline warning count shifts significantly after a content or template fix.

{% endraw %}
