# IndexNow Support

**Path:** `scripts/indexnow_submit.py`  
**Purpose:** Manual submission of indexable URLs to IndexNow after content updates.

---

## What is IndexNow?

[IndexNow](https://www.indexnow.org/) is a protocol that lets websites notify search engines (Bing, Yandex, Seznam.cz, and others) about content changes immediately, rather than waiting for crawlers to discover them.

**Important:** IndexNow is **not a Google indexing guarantee**. It notifies participating search engines; Google does not use IndexNow. Use it as a signal to Bing/Yandex, not as a replacement for sitemap hygiene or canonical quality.

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

3. **Key verification (optional but recommended)** — Pass `--require-key-file` to confirm the key file exists at the site root before submitting:

   ```bash
   python3 scripts/indexnow_submit.py --submit --require-key-file
   ```

---

## Usage

### Default: dry run (recommended first step)

```bash
python3 scripts/indexnow_submit.py
```

This prints the URLs that would be submitted without making any network request. **Dry-run is the default.** No network request is made unless you explicitly pass `--submit`.

### Submit core URLs only

```bash
python3 scripts/indexnow_submit.py --submit
```

Submits the stable core URL set (homepage, about, services, atlas, sitemaps, etc.).

### Submit explicit paths

```bash
python3 scripts/indexnow_submit.py --submit --urls /about/ /atlas/concepts/order-to-cash/
```

### Submit all discovered indexable URLs

```bash
python3 scripts/indexnow_submit.py --submit --all
```

Walks the repository and submits every indexable page. Use with caution.

### Submit only URLs changed in the latest git diff

```bash
python3 scripts/indexnow_submit.py --submit --from-git-diff HEAD~1 HEAD
```

Maps changed files to their public URLs and submits only those. Useful for targeted post-merge updates.

### Limit the number of URLs

```bash
python3 scripts/indexnow_submit.py --submit --all --max-urls 50
```

Caps the submission batch. If more URLs are discovered, the script reports the overflow and exits without submitting.

---

## Discovery Audit

Before submitting, run the post-build discovery audit to validate that the built `_site/` output contains only indexable, canonical URLs and that no private or noindex pages have leaked into sitemaps or structured data:

```bash
python3 scripts/audit_discovery_outputs.py _site
```

Run this after `bundle exec jekyll build` and before any real IndexNow submission.

---

## Safety Rules

- **No secrets in repo.** The key is never hardcoded in the script.
- **Dry-run by default.** The script defaults to dry-run. Real submission requires `--submit`.
- **Only indexable URLs.** The script checks frontmatter for `noindex`, `sitemap: false`, and Atlas `verified`/`status`.
- **No draft/noindex/research pages.** Research pages (`/research/**`) and unverified Atlas pages are never submitted.
- **No private paths.** Paths blocked in `robots.txt` (e.g., `/DAMA/`, `/agentic-bytes/`, `/TRIZ-bytes/`, `/LLM-prompts/`) are never submitted.
- **Manual real submission only.** Real submission is never automatic in CI. The GitHub workflow runs dry-run on every push; real submission requires a manual `workflow_dispatch`.

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

### Page URLs (when using `--all`, `--from-git-diff`, or explicit paths)

A Markdown file is submitted only if:

1. `robots` frontmatter does not contain `noindex`
2. `sitemap` is not `false`
3. For Atlas pages: `verified: true` and `status: reviewed`
4. Not under `/research/`
5. Not under private paths blocked in `robots.txt`

---

## GitHub Workflow

- **Dry-run on push:** `.github/workflows/indexnow-dry-run.yml` runs `python3 scripts/indexnow_submit.py` (dry-run by default) on every push to `main`.
- **Manual real submit:** Use `workflow_dispatch` with `submit: true` to run a real submission. This requires the `INDEXNOW_KEY` repository secret and uses `--from-git-diff` by default.
- **No automatic real submission.** Real submission is gated behind manual dispatch to prevent accidental bulk notifies.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `INDEXNOW_KEY not set` | Export the key or add to `.env.local` |
| `Key file not found` | Pass `--require-key-file` only after verifying the `.txt` key file is deployed to the site root |
| HTTP 400 / 403 | Verify the key file exists at the site root and is accessible |
| URLs rejected | Check that submitted URLs are canonical, indexable, and return 200 |
| `--max-urls` exceeded | Reduce scope (use `--from-git-diff` or explicit `--urls`) or raise the limit intentionally |
| Workflow dry-run fails | Check that `INDEXNOW_KEY` secret is configured for manual dispatch; dry-run does not need it |
| URLs skipped unexpectedly | Run `python3 scripts/audit_discovery_outputs.py _site` to verify indexability flags in the built output |

---

## Change Log

| Date | Change |
|------|--------|
| 2026-06-08 | v2.0 — Hardened script: dry-run by default, added `--submit`, `--from-git-diff`, `--max-urls`, `--require-key-file`; added discovery audit; separated manual real-submit workflow |
| 2026-06-08 | v1.0 — Refactored from `submit_indexnow.py` to use env-based key, add dry-run, and enforce indexability checks |
