# Search Console / IndexNow Handoff Report

**Date:** 2026-06-13
**Branch:** `feat/seo-visibility-swarm`
**Site:** https://dkharlanau.github.io

---

## Sitemap URLs

| URL | Type | Notes |
|-----|------|-------|
| `https://dkharlanau.github.io/sitemap.xml` | Sitemap index | References 3 section sitemaps |
| `https://dkharlanau.github.io/sitemap-pages.xml` | Pages + collections | Excludes noindex, research, unverified Atlas |
| `https://dkharlanau.github.io/sitemap-data.xml` | Datasets | Machine-readable dataset references |
| `https://dkharlanau.github.io/sitemap-atlas.xml` | Atlas | Verified Atlas pages only |
| `https://dkharlanau.github.io/robots.txt` | robots.txt | AI crawler policy, sitemap references, Content-Signal |

Submit all 4 sitemap URLs to Google Search Console and Bing Webmaster Tools.

---

## Top Indexable URLs to Inspect Manually

These URLs should be verified in Search Console for coverage, indexing, and mobile usability:

1. `https://dkharlanau.github.io/` — Home
2. `https://dkharlanau.github.io/about/` — About / Profile
3. `https://dkharlanau.github.io/services/` — Services
4. `https://dkharlanau.github.io/atlas/` — Knowledge Atlas
5. `https://dkharlanau.github.io/skill-hub/` — Skill Hub
6. `https://dkharlanau.github.io/datasets/` — Datasets
7. `https://dkharlanau.github.io/ai/` — AI Sources
8. `https://dkharlanau.github.io/blog/` — Blog
9. `https://dkharlanau.github.io/notes/` — Notes
10. `https://dkharlanau.github.io/certifications/` — Certifications

---

## URLs That Should NOT Be Indexed

These are correctly excluded from sitemap and have `robots: noindex`:

- All `atlas/diagnostics/*` pages (175 pages, status: `needs_verification`, `verified: false`)
- All `scenarios/*` pages (12 pages, unverified)
- All `research/*` pages (~40 pages, explicitly excluded from sitemap)
- `_radar/*` collection pages (signal tracking, noindex by default)
- `_news/*` collection pages (news updates, noindex by default)
- `docs/` internal documentation

**Safety confirmation:** No unverified Atlas page is in the sitemap. No research page is in the sitemap. The sitemap templates enforce this correctly.

---

## URLs with Metadata / Schema Issues

From the indexability audit of the built site (`_site`, stale from 2026-06-12):

| Issue | Count | Action |
|-------|-------|--------|
| Missing `og:image` on some pages | ~30 | Pages inherit default image from `_includes/head.html`; verify in fresh build |
| Missing `article:modified_time` | Many | Pages without `last_modified_at` or `updated` frontmatter; not a bug |

No critical metadata issues found.

---

## Sitemap / Noindex Conflict Check

**Result:** No conflicts detected.

All noindex pages are excluded from sitemaps. The sitemap templates (`sitemap-pages.xml`, `sitemap-atlas.xml`) explicitly filter:
- `robots` containing `noindex`
- `is_research` paths
- `verified != true` + `status != 'reviewed'` for Atlas pages

---

## IndexNow Workflow Safety Audit

### Workflow: `.github/workflows/indexnow.yml`

**Status:** ✅ Secure and well-designed.

| Safety Check | Result |
|-------------|--------|
| Dry-run on PR | ✅ Yes |
| Real submit only on push to main or manual dispatch | ✅ Yes |
| Sitemap-backed URL filtering | ✅ Yes (`filter_urls_by_sitemap`) |
| Noindex defense-in-depth | ✅ Yes (`check_url_noindex_in_site`) |
| Key verification (`--require-key-file`) | ✅ Yes |
| Max URL cap (`--max-urls`) | ✅ Yes (default 100) |
| Git diff scope (default) | ✅ Yes (only changed URLs) |
| All-URLs option (`--all`) | ✅ Yes, with manual dispatch opt-in |

**Script:** `scripts/indexnow_submit.py` (611 lines)

- `public_url_for_path()` correctly maps changed files to canonical URLs.
- `check_indexable()` enforces frontmatter rules (noindex, sitemap:false, unverified Atlas, research paths).
- `check_url_noindex_in_site()` performs a second noindex check on the built HTML before submission.
- `CORE_URLS` set ensures that layout/config changes trigger core URL resubmission.

**No secrets exposed in repo files.**

---

## Manual Search Console Steps

1. **Verify ownership** of `dkharlanau.github.io` via GitHub Pages DNS or HTML file.
2. **Submit sitemap index:** `https://dkharlanau.github.io/sitemap.xml`
3. **Submit section sitemaps:**
   - `https://dkharlanau.github.io/sitemap-pages.xml`
   - `https://dkharlanau.github.io/sitemap-data.xml`
   - `https://dkharlanau.github.io/sitemap-atlas.xml`
4. **Inspect the 10 top URLs** manually for coverage and mobile usability.
5. **Check "Pages" report** for any noindex pages that appear as "Excluded" — verify they are intentional.
6. **Monitor "Core Web Vitals"** after the first crawl.
7. **Request indexing** for the 10 top URLs after verifying they are high-quality.

---

## Bing / IndexNow Steps

1. **Bing Webmaster Tools:** Add site and verify ownership.
2. **Submit sitemaps** (same URLs as Search Console).
3. **IndexNow key:** Ensure `INDEXNOW_KEY` secret is configured in repository settings.
4. **Verify key file:** The key `.txt` file must exist in repo root (enforced by `--require-key-file`).
5. **Trigger workflow** manually after first PR merge to submit core URLs.
6. **Monitor IndexNow report** artifact (`indexnow-report.json`) for skipped URLs.

---

## Handoff Checklist

- [ ] Google Search Console ownership verified
- [ ] Bing Webmaster Tools ownership verified
- [ ] Sitemap index submitted to both
- [ ] Section sitemaps submitted to both
- [ ] IndexNow key configured in repo secrets
- [ ] IndexNow key file present in repo root
- [ ] Manual URL inspection completed for top 10 pages
- [ ] Noindex exclusions confirmed intentional in Search Console
- [ ] First IndexNow submission triggered after merge
- [ ] `INDEXNOW_KEY` never exposed in logs or files
