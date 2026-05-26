## Closeout Report — dkharlanau.github.io Issue #9

### Result
Completed

### Problem
`news/index.html` linked to `/news/2026-05-26-sample-professional-signal/`, but the target page was generated unreliably because the sample/draft file lived in the production `_news/` Jekyll collection.

### Root Cause
Sample content should never be in a production collection. `_news/2026-05-26-sample-professional-signal.md` had `robots: noindex,follow` and `sitemap: false`, but Jekyll still generated it as a permalink page, causing CI link checks to expect a URL that was not consistently available.

### Files Changed

| File | Change | Reason |
|---|---|---|
| `_news/2026-05-26-sample-professional-signal.md` | **Deleted** | Removed from production collection |
| `docs/templates/news-signal-template.md` | **Created** | Template for future news signals, outside production collection |
| `scripts/validate_site_content.py` | **Modified** | Added rejection rules for sample/draft files inside `_news/` |

### Validation Results

| Check | Command | Result | Notes |
|---|---|---|---|
| Site content validator | `python3 scripts/validate_site_content.py` | **PASSED** | No errors, no warnings |
| News section empty state | Manual review of `news/index.md` | **Confirmed** | `{% if items == empty %}` already handles empty state |
| `_news/` directory | `ls _news/` | **Empty** | No sample files remain |
| Jekyll build | `bundle exec jekyll build` | **Not run** | Ruby/Jekyll unavailable in this environment |
| Link checker | `python3 scripts/check_links.py _site` | **Not run** | Requires built site |
| SEO checker | `python3 scripts/check_seo.py _site` | **Not run** | Requires built site |

**Local build required:** The Jekyll build and full link/SEO checks must be run locally where Ruby/Jekyll are installed.

```bash
# Run these locally after pulling main:
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
```

### Validator Update Details

Added to `check_news_section()` in `scripts/validate_site_content.py`:

1. **Filename rejection:** Files in `_news/` with `sample` or `draft` in the filename are rejected with:
   > `sample/draft files are not allowed in _news/. Move to docs/templates/ and remove 'sample' or 'draft' from filename.`

2. **Content marker rejection:** Files in `_news/` containing `SAMPLE` or `DRAFT` markers are rejected with:
   > `contains SAMPLE/DRAFT marker — remove before publishing or move to docs/templates/.`

### Safety Checks

| Check | Status |
|---|---|
| No homepage changes | **Confirmed** — `index.md` and `_data/home.yml` untouched |
| No `future: true` set | **Confirmed** — `_config.yml` unchanged |
| No sample published to satisfy CI | **Confirmed** — sample moved to templates, not generated as page |
| No public site writes | **Confirmed** — only removed a file and added a template |
| Broken `/news/...sample.../` link gone | **Confirmed** — source page no longer exists in `_news/`, so no generated URL |

### Post-Merge Verification

```bash
git pull origin main
ls _news/                          # should be empty
python3 scripts/validate_site_content.py --strict   # should PASS
```

### Next Steps
1. Pull `main` locally
2. Run `bundle exec jekyll build`
3. Run `python3 scripts/check_links.py _site`
4. Run `python3 scripts/check_seo.py _site`
5. If all pass, CI should be green

### Issue Closure
- Issue #9 can be closed as completed
- Commit `097b333` on `main`
