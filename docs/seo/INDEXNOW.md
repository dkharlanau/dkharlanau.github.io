# IndexNow Support

**Path:** `scripts/indexnow_submit.py`  
**Purpose:** Manual submission of indexable URLs to IndexNow after content updates.

---

## What is IndexNow?

[IndexNow](https://www.indexnow.org/) is a protocol that lets websites notify search engines (Bing, Yandex, Seznam.cz, and others) about content changes immediately, rather than waiting for crawlers to discover them.

---

## Setup

1. **Key file** — A verification key file (`31ff0ffa67bc49f3bca0a4a719e30fa2.txt`) already exists at the site root.
2. **API key** — The key must be provided via environment variable or `.env.local`:

   ```bash
   export INDEXNOW_KEY=31ff0ffa67bc49f3bca0a4a719e30fa2
   ```

   Or add to `.env.local` (which is gitignored):

   ```
   INDEXNOW_KEY=31ff0ffa67bc49f3bca0a4a719e30fa2
   ```

---

## Usage

### Dry run (recommended first step)

```bash
python3 scripts/indexnow_submit.py --dry-run
```

This prints the URLs that would be submitted without making any network request.

### Submit core URLs only

```bash
python3 scripts/indexnow_submit.py
```

Submits the stable core URL set (homepage, about, services, atlas, sitemaps, etc.).

### Submit explicit paths

```bash
python3 scripts/indexnow_submit.py --urls /about/ /atlas/concepts/order-to-cash/
```

### Submit all discovered indexable URLs

```bash
python3 scripts/indexnow_submit.py --all
```

Walks the repository and submits every indexable page. Use with caution.

---

## Safety Rules

- **No secrets in repo.** The key is never hardcoded in the script.
- **Dry-run mode required.** Always use `--dry-run` first to review.
- **Only indexable URLs.** The script checks frontmatter for `noindex`, `sitemap: false`, and Atlas `verified`/`status`.
- **No draft/noindex/research pages.** Research pages (`/research/**`) and unverified Atlas pages are never submitted.
- **Not wired to CI.** This is a manual script. Do not add to automatic CI publishing unless explicitly safe.

---

## What Gets Submitted

### Core URLs (default)

- `/`
- `/about/`
- `/ai/`
- `/services/`
- `/datasets/`
- `/notes/`
- `/blog/`
- `/atlas/`
- `/robots.txt`
- `/llms.txt`, `/LLM.txt`
- `/sitemap.xml`, `/sitemap-pages.xml`, `/sitemap-data.xml`, `/sitemap-atlas.xml`

### Page URLs (when using `--all` or explicit paths)

A Markdown file is submitted only if:

1. `robots` frontmatter does not contain `noindex`
2. `sitemap` is not `false`
3. For Atlas pages: `verified: true` and `status: reviewed`
4. Not under `/research/`

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `INDEXNOW_KEY not set` | Export the key or add to `.env.local` |
| HTTP 400 / 403 | Verify the key file exists at the site root and is accessible |
| URLs rejected | Check that submitted URLs are canonical, indexable, and return 200 |

---

## Change Log

| Date | Change |
|------|--------|
| 2026-06-08 | v1.0 — Refactored from `submit_indexnow.py` to use env-based key, add dry-run, and enforce indexability checks |
