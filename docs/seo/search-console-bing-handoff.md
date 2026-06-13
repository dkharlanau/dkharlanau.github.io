---
layout: default
title: "Search Console / Bing Manual Setup Handoff"
description: "What must be configured outside the repository for search coverage and how to interpret IndexNow reports."
robots: noindex,follow
sitemap: false
---

# Search Console / Bing Manual Setup Handoff

This document describes the manual steps that cannot be performed from inside the repository, plus how to verify that automated signals are working.

## What is automated from the repository

- **Sitemaps** are generated during `bundle exec jekyll build`:
  - `https://dkharlanau.github.io/sitemap.xml`
  - `https://dkharlanau.github.io/sitemap-pages.xml`
  - `https://dkharlanau.github.io/sitemap-data.xml`
  - `https://dkharlanau.github.io/sitemap-atlas.xml`
- **IndexNow submission** runs from `.github/workflows/indexnow.yml`:
  - Dry-run on every pull request.
  - Real submission on pushes to `main` only when the `INDEXNOW_KEY` repository secret is configured.
  - The workflow uploads `indexnow-report.json` as an artifact and writes a sanitized summary to the job summary.
- **Local validation** is run before publishing:
  - `python3 scripts/check_seo.py _site`
  - `python3 scripts/check_structured_data.py _site`
  - `python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical`

## What must be configured manually

### Google Search Console

1. Verify ownership of `https://dkharlanau.github.io` using the HTML file or DNS method.
2. Submit the sitemap index: `https://dkharlanau.github.io/sitemap.xml`.
3. Monitor Coverage, Core Web Vitals, and structured-data reports after each main build.

### Bing Webmaster Tools

1. Add the site and verify ownership.
2. Submit the same sitemap index.
3. If using IndexNow, confirm the key file `{INDEXNOW_KEY}.txt` is publicly accessible at `https://dkharlanau.github.io/{INDEXNOW_KEY}.txt`.

### IndexNow key

- Store the key value in the repository secret `INDEXNOW_KEY`.
- Place a file named `{INDEXNOW_KEY}.txt` at the repository root so the real submission step (`--require-key-file`) can verify it.
- Do not commit the key value in plain text.

## Interpreting the IndexNow report

The workflow artifact `indexnow-report.json` contains:

- `mode`: `"dry-run"` or `"submit"`.
- `submitted`: list of canonical URLs selected for submission.
- `skipped`: list of URLs or paths that were excluded, each with a reason.
- `summary`: counts of submitted and skipped URLs.

On a pull request, `mode` is always `"dry-run"` and no network call is made. On a push to `main` with a configured key, `mode` is `"submit"` and the selected URLs are sent to the IndexNow endpoint.

## Safety reminders

- Never include Search Console verification tokens, API keys, or Bing credentials in the repository.
- Do not attach private screenshots to public issues or PRs.
- If search coverage looks wrong, run the local validation commands first; most indexability problems are caught before submission.

## Related files

- `.github/workflows/indexnow.yml`
- `scripts/indexnow_submit.py`
- `docs/seo/INDEXNOW.md`
- `docs/seo/page-quality-checks.md`
