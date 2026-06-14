---
layout: default
title: "Project Technical Baseline Audit - 2026-06-14"
description: "Read-only baseline audit for repository health, build, CI, deploy, SEO, analytics, AI-readiness, content architecture, linking, public safety, and maintainability."
robots: noindex,follow
sitemap: false
---

# Project Technical Baseline Audit - 2026-06-14

Repository: `dkharlanau/dkharlanau.github.io`
Branch: `audit/project-technical-baseline`
Audit type: read-only technical baseline with one report-only commit.

## Executive summary

- **Overall state: Yellow.** The site is buildable, deployable, measurable, and guarded by a mature validation suite. The remaining risks are mostly quality debt in generated/docs surfaces and broad content architecture growth.
- **Main risk:** Page quality and accessibility warnings are not critical, but they are numerous and clustered around duplicate H1s, heading hierarchy, thin short-form entries, generated docs, and source-document renders.
- **Main opportunity:** The repository already has strong AI-readiness surfaces, analytics coverage, sitemaps, and validation scripts. The highest-value next move is to turn audit warnings into small, separate cleanup PRs rather than broad rewrites.
- **Recommended next move:** Add a CI/reporting layer for quality-warning budgets and a cleanup PR for generated/research/agent-skill duplicate H1 output.

## Scorecard

| Area | Score | Status | Notes |
|---|---:|---|---|
| Repo hygiene | 8/10 | Green | 1,192 tracked files; public hygiene check passed; ignored local artifacts exist but are not tracked. |
| Build reproducibility | 8/10 | Green | Local build passes with Homebrew Ruby on `PATH`; system Ruby is too old for `.ruby-version`. |
| CI/deploy | 9/10 | Green | Latest CI, IndexNow, and Pages deployment runs are successful. |
| SEO/findability | 8/10 | Green | SEO metadata and structured data checks pass for 762 HTML files; residual warnings are editorial/template quality. |
| Analytics | 10/10 | Green | GA4 configured; 762/762 HTML pages tagged; no duplicate tags; no non-HTML analytics leakage. |
| AI-readiness | 9/10 | Green | `llms.txt`, `llms-full.txt`, `/ai/`, datasets, manifests, and `.well-known/agent-skills` build and validate. |
| Content architecture | 7/10 | Yellow | Clear journey exists, but generated docs/research/report pages add duplicate-title/H1 and generic-description noise. |
| Internal linking | 6/10 | Yellow | Pass/fail local link check passes; graph audit reports 179 orphans, 190 broken classifications, and 742 indexable-to-noindex relationships. |
| Public safety | 8/10 | Green | Public hygiene check passed; broad grep finds mostly policy/test/example matches and ignored local metadata. |
| Maintainability | 8/10 | Green | Strong scripts/tests/docs; warning cleanup should be converted into smaller repeatable quality gates. |

## Validation results

| Command | Result | Summary |
|---|---|---|
| `git status --short` | Pass | Initial worktree was clean before branch creation. |
| `git fetch origin` | Pass | Fetched successfully. |
| `git switch -c audit/project-technical-baseline origin/main` | Pass | Created audit branch from `origin/main`. `main` was not checked out locally because it is used by a sibling worktree. |
| `git log --oneline -10` | Pass | Latest commit on `origin/main` was `a6d9ac4 fix(seo): verify analytics coverage and findability quality (#223)`. |
| `PATH="/opt/homebrew/opt/ruby/bin:$PATH" ./bin/setup` | Pass | Ruby 3.4.7 used; bundle complete; 3 Gemfile dependencies and 99 gems installed into `vendor/bundle`. |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests` | Pass | 262 tests passed in 25.28s. |
| `python3 scripts/check_public_repo.py` | Pass | Public repo hygiene check passed for 1,192 tracked files. |
| `python3 scripts/generate_atlas_artifacts.py --check` | Pass with warnings | Artifacts up to date. Existing YAML parse warnings appeared for excluded/template docs and one docs page with non-frontmatter list syntax. |
| `bundle exec jekyll clean && bundle exec jekyll build` | Pass | Clean build completed in 24.764s using Homebrew Ruby path. |
| `python3 scripts/check_links.py _site` | Pass | No broken local links detected. |
| `python3 scripts/check_seo.py _site` | Pass | SEO checks passed for 762 HTML files. |
| `python3 scripts/check_structured_data.py _site` | Pass | Structured data check passed for 762 HTML files. |
| `python3 scripts/check_indexing_policy.py --site-dir _site --fail-on-critical` | Pass | Indexing policy check passed. |
| `python3 scripts/check_sitemap_policy.py --site-dir _site --repo-dir . --fail-on-critical` | Pass | Sitemap policy check passed for 423 URLs. |
| `python3 scripts/check_date_consistency.py --site-dir _site --repo-dir . --fail-on-critical` | Pass | Date consistency check passed for 375 URLs with `lastmod`. |
| `python3 scripts/check_content_quality.py --fail-on-critical` | Pass | Content quality check passed. |
| `python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical` | Pass with warnings | 73 warnings across 762 pages; 0 critical. |
| `python3 scripts/audit_indexability.py --site-dir _site --fail-on-critical --output-dir /tmp/cv-ai-validation-reports` | Pass | 762 pages scanned; no critical issues. |
| `python3 scripts/audit_internal_links.py --site-dir _site --output-dir /tmp/cv-ai-validation-reports` | Pass with diagnostics | 762 pages scanned; 179 orphans, 190 broken classifications, 742 indexable-to-noindex relationships. |
| `python3 scripts/accessibility_audit.py --site-dir _site --fail-on-critical` | Pass with warnings | 0 critical; 91 warnings. Mostly duplicate H1s in generated/research/agent-skill pages plus a few heading-order warnings. |
| `python3 scripts/validate_ai_endpoints.py _site` | Pass | AI endpoint validation passed. |
| `python3 scripts/check_analytics_coverage.py --site-dir _site` | Pass | 762 HTML pages; 762 tagged; 0 missing; 0 duplicate; 0 non-HTML files with analytics snippets. |
| `git diff --check` | Pass | No whitespace/error output. |

Validation side effects cleaned before report commit:

- `data/content-maintenance/page-registry.json` was regenerated with timestamp/order-only churn; reverted.
- `indexnow-report.json` appeared as an untracked local report artifact; removed from the audit commit scope.

Post-report PR readiness checks:

- `PATH="/opt/homebrew/opt/ruby/bin:$PATH" bundle exec jekyll build` passed after adding this report.
- `python3 scripts/check_seo.py _site` passed for 763 HTML files after adding this report.
- `python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical` still reported 73 warnings and 0 critical issues across 763 pages.
- `python3 scripts/check_sitemap_policy.py --site-dir _site --repo-dir . --fail-on-critical` still passed for 423 URLs.
- `python3 scripts/check_analytics_coverage.py --site-dir _site` passed with 763 tagged HTML pages, 0 missing pages, 0 duplicate-tag pages, and 0 non-HTML files with analytics snippets.

## GitHub state

Open PRs:

- None returned by `gh pr list --state open --limit 50`.

Open issues:

- `#157` — "Add content inventory report generation for future audits" — open since 2026-06-13.

Latest workflow state:

- Latest `CI` on `main`: success, run `27494146926`, 1m31s, 2026-06-14T09:07:15Z.
- Latest `IndexNow Submit` on `main`: success, run `27494146924`, 56s, 2026-06-14T09:07:15Z.
- Latest `pages-build-deployment` on `main`: success, run `27494146606`, 1m16s, 2026-06-14T09:07:14Z.
- Last 20 listed runs were successful.

Workflows:

- `CI` — active.
- `IndexNow Submit` — active.
- `pages-build-deployment` — active.

GitHub Pages:

- Status: `built`.
- URL: `https://dkharlanau.github.io/`.
- Source: `main` branch, `/`.
- Public: true.
- HTTPS enforced: true.
- Build type: legacy.

## Findings

### P0 - must fix now

No P0 findings.

### P1 - should fix soon

1. **Generated/docs surfaces produce duplicate H1 and accessibility warnings.**
   Page quality reports 73 warnings and accessibility reports 91 warnings. Most are duplicate H1s in generated agent-skill pages, research/skill-hub pages, root docs rendered as pages, and report pages. This is not breaking deployment, but it weakens semantic quality.

2. **Internal-link graph audit is noisy and not yet operationalized.**
   The pass/fail link checker reports no broken local links, but the graph audit reports 179 orphans, 190 broken classifications, and 742 indexable-to-noindex links. Some are expected because noindex/generated surfaces are intentionally outside the human navigation graph, but the report is too noisy to guide triage without classification rules.

3. **Default meta description appears on many generated/source-document pages.**
   Built metadata scan found 104 pages sharing the default SAP AMS description. This affects generated research/source-document pages more than core commercial pages, but it creates duplicate-description noise.

4. **Local build requires non-default Ruby path.**
   The repo requires Ruby `3.3.4+`; local system Ruby is too old. Builds pass with Homebrew Ruby first in `PATH`, but this should remain documented for future agents.

### P2 - useful improvement

1. **Atlas and Skill Hub section H1s use editorial phrases rather than exact title alignment.**
   This is intentional-looking and not critical, but it triggers page-quality warnings and may weaken machine scoring on section hubs.

2. **Short news/radar entries are thin by page-quality heuristics.**
   Several short entries are technically valid but thin. Either expand them with durable context or keep them out of the index depending on editorial intent.

3. **Search discoverability is strong at hub level but uneven at long-tail route level.**
   Homepage, About, Services, Atlas, Skill Hub, AI, and datasets are clear. Long-tail discoverability is weaker for some generated docs, noindex scenario content, and duplicated DAMA dataset/doc views.

4. **Repository root remains understandable but large.**
   The layout is agent-readable thanks to `AGENTS.md`, `PROJECT_MAP.md`, and architecture docs. Still, root-level rendered docs and generated artifacts can confuse future agents unless task-specific guidance is followed.

### P3 - optional / later

1. **Open issue #157 remains relevant.**
   A content inventory report generator would help turn future audits into repeatable data instead of manual page review.

2. **Review whether static `docs/dama/*.html` and dataset views need separate public surfaces.**
   They are valid and measured, but duplicate titles/descriptions with dataset views. Keep both only if each route has a clear audience.

3. **Consider separating public report pages from source docs in page-quality scoring.**
   Current checks treat many docs/reports as collection-like public pages, which is useful but noisy.

## Repository structure audit

Tracked file count: 1,192.

Largest top-level tracked areas:

- `datasets/` — 320 files; canonical dataset JSON and generated dataset views.
- `atlas/` — 249 files; Knowledge Atlas content and manifest.
- `skill-hub/` — 100 files; practical skills hub pages.
- `docs/` — 88 files; architecture, AI, SEO, research, scenario, and maintenance docs.
- `_includes/` — 60 files; Jekyll components and SEO/analytics includes.
- `agent-skills/` — 59 files; portable agent skill packages and exporters.
- `research/` — 43 files; research briefs, comparisons, watchlists, and skill-hub research.
- `scripts/` — 38 files; validators, generators, audit tools.
- `tests/` — 36 files; pytest suite.
- `ai/` — 26 files; AI-readable endpoints and manifests.

Main directory purposes are clear and well documented in `AGENTS.md`.

Suspicious or high-attention root/worktree items:

- `.env.local` exists locally but is ignored and not tracked. Do not inspect or commit.
- `_site/`, `vendor/`, `.pytest_cache/`, `.ruby-lsp/`, `.tmp/`, and `.bundle/` exist locally and should remain untracked/generated.
- `li2resume.local.md` exists locally and is excluded by config; do not publish.
- Root `sitemap*.xml`, `llms*.txt`, and `robots.txt` are intentionally tracked/generated public discovery files.
- `31ff0ffa67bc49f3bca0a4a719e30fa2.txt` appears intentionally included for site verification or ownership.

Generated files intentionally tracked:

- `llms-full.txt`, `llms.txt`, `sitemap*.xml`, `atlas/manifest.json`, `ai/atlas-compact-index.json`, `ai/verified-pages.json`, `ai/rag/related.json`, `datasets/manifest.json`, dataset view pages, DAMA static docs, and agent-skill export surfaces.

Likely obsolete or review-worthy areas:

- `professional-radar/` appears excluded from Jekyll but tracked; it should be documented as supporting tooling or archived deliberately.
- Rendered docs/reports are useful, but their public page metadata quality is uneven.
- DAMA static docs duplicate dataset-view content in places.

## SEO and findability

Built HTML pages: 762.

Indexing:

- Indexable pages: 410.
- Noindex pages: 352.
- Sitemap policy passed for 423 URLs.
- Indexing policy passed.

Metadata:

- Missing titles: 0.
- Missing meta descriptions: 0.
- Duplicate titles: 4 title groups.
- Duplicate descriptions: 12 description groups.
- H1 count issues in built scan: 115 pages.
- Structured data parse: passed for 762 HTML files.
- Canonical/OG URL checks: passed via `scripts/check_seo.py`.

Top pages that should attract search:

1. `/` — SAP AMS and AI support automation positioning.
2. `/about/` — canonical profile.
3. `/services/` — SAP consulting services.
4. `/services/sap-ams-consulting/` — AMS improvement.
5. `/services/sap-o2c-process-audit/` — O2C process audit.
6. `/atlas/` — Knowledge Atlas hub.
7. `/atlas/diagnostics/` — SAP support diagnostics hub.
8. `/atlas/sap/` — SAP support/concepts section.
9. `/skill-hub/` — practical working skills.
10. `/ai/` — AI routing hub.

Technically valid but weak/noisy for discoverability:

1. Root rendered docs such as `/AGENTS/`, `/ARCHITECTURE/`, `/PROJECT_MAP/`.
2. `.well-known/agent-skills/*` HTML pages with duplicate H1s.
3. `research/skill-hub/*` rendered research pages with duplicate H1/default descriptions.
4. `docs/dama/*.html` duplicated against dataset views.
5. Short `news/*` entries with low word count.
6. Short `radar/*` entries with low word count.
7. `CITATION/` duplicate H1 and generic description.
8. Report pages with duplicate H1s.
9. Agent skill reference pages that are noindex but still semantically noisy.
10. Generated source-document pages that inherit the default site description.

Pages that should probably not be indexed:

- Scenario pages remain Level 1 and correctly noindex by policy.
- Agent skill source/reference pages under `agent-skills/skills` are noindex by config.
- Research working surfaces and raw source docs should remain noindex unless promoted.
- Generated reports should remain noindex unless they are intended as public evidence.

## Analytics

Source state:

- GA4 is configured in `_config.yml` as `google_analytics_id`.
- Shared include: `_includes/analytics.html`.
- Standard HTML injection: `_includes/head.html`.
- Standalone DAMA pages receive analytics through `scripts/generate_dama_pages.js`.
- Regression check exists: `scripts/check_analytics_coverage.py` plus `tests/test_analytics_coverage.py`.

Built state:

- HTML pages: 762.
- Analytics marker grep count in HTML: 1,524, which is expected because each GA4 page includes script and config markers.
- Coverage checker: 762 tagged, 0 missing, 0 duplicate, 0 non-HTML analytics snippets.
- XML/JSON/TXT analytics grep returned no output.

The broad requested grep using `G-[A-Z0-9]` is too noisy because it matches ordinary text fragments. A tighter follow-up search confirms true analytics implementation is limited to analytics config/includes/scripts/tests and generated DAMA HTML.

## AI-readiness and retrieval surfaces

Built and validated:

- `_site/llms.txt`
- `_site/llms-full.txt`
- `_site/robots.txt`
- `_site/sitemap.xml`
- `_site/.well-known/agent-skills/index.json`
- `_site/ai/catalog.json`
- `_site/ai/discovery-map.json`
- `_site/ai/resume.json`
- `_site/ai/resume.yml`
- `_site/ai/atlas-compact-index.json`
- `_site/ai/verified-pages.json`
- `_site/ai/rag/related.json`
- `_site/datasets/manifest.json`
- `_site/datasets/schema.json`
- `_site/agent-skills/`

Policy state:

- `validate_ai_endpoints.py` passed.
- `generate_atlas_artifacts.py --check` passed.
- Existing tests guard `llms-full.txt` policy and private-path leakage.
- No evidence from validation that unverified/noindex Atlas pages leak into `llms-full.txt`.

AI surfaces are understandable for future agents because `AGENTS.md`, `PROJECT_MAP.md`, `/ai/`, `llms.txt`, and manifests all point to canonical sources. The main improvement is reducing duplicate/default metadata on generated docs so retrieval systems have clearer page-level summaries.

## Content and site architecture audit

User journey:

- Homepage explains SAP AMS, AI support automation, and process optimization with clear contact path.
- About page is a strong canonical profile with LinkedIn contact and machine-readable sources.
- Services page is visible and well connected from `/about/`, `/ai/`, and homepage navigation surfaces.
- Atlas supports expertise with reviewed diagnostic and conceptual content.
- Skill Hub supports professional/agent positioning with practical working skills.
- AI hub and datasets provide strong retrieval/evidence surfaces.
- Scenarios are intentionally noindex Level 1 and support business-pain mapping without being promoted prematurely.

Audience clarity:

- Recruiter: can use `/about/`, `/cv/`, `/ai/resume.yml`, and citation/profile audit files.
- SAP manager: can use `/services/`, `/atlas/diagnostics/`, and AMS/O2C service pages.
- Consultant: can use Atlas, Skill Hub, research, and datasets.
- AI agent: can use `/ai/`, `llms.txt`, `llms-full.txt`, manifests, and `.well-known/agent-skills`.

Where content looks generic, duplicated, or overbuilt:

- Rendered root docs and generated research pages often inherit generic site descriptions.
- Some DAMA static docs duplicate dataset views.
- Short radar/news entries are valid but thin for indexable article-like content.
- Internal-link graph is large enough that future agents need task-specific rules before editing navigation.

## Public safety audit

Automated safety checks:

- `scripts/check_public_repo.py` passed for 1,192 tracked files.
- Tests include guards for private paths, source files, and `llms-full.txt` leakage.
- Broad grep produced many matches for policy text, tests, public incident-management research, synthetic examples, and ignored local metadata.

True-positive risks:

- Ignored local `.env.local` exists in the worktree. It is not tracked and was not read.
- Ignored local tool metadata includes local filesystem paths. These are not tracked.
- Professional Radar documentation references external secret-management paths and environment-variable names as documentation, not values.

False positives:

- `password`, `token`, `secret`, `client`, `ticket`, and `incident` appear heavily in tests, policy docs, synthetic examples, public research, and site content because the repository intentionally discusses support incidents, ticket triage, and secret-safety rules.
- Test fixtures intentionally include fake private paths and fake secret strings to validate scanners.

Recommended public-safety improvements:

- Keep `.env.local`, `_site`, `vendor`, local caches, and private exports ignored.
- Add a lightweight audit-summary mode to the public-safety scanner so future reports can include counts/categories without exposing raw matches.
- Continue requiring `check_public_repo.py` before any report/content PR.

## Recommended next PRs

1. **`fix(quality): reduce duplicate h1 warnings in generated docs`**
   Purpose: update generated/research/agent-skill render patterns to avoid duplicate H1s.
   Expected files: generator/templates for agent-skill/research/doc rendering, focused tests.
   Risk: medium.
   Validation: Jekyll build, page quality, accessibility audit.

2. **`chore(audit): classify internal-link graph findings`**
   Purpose: separate expected noindex/generated orphan routes from actionable orphan/broken classifications.
   Expected files: `scripts/audit_internal_links.py`, tests, docs.
   Risk: low.
   Validation: unit tests and internal-link audit.

3. **`fix(seo): improve generated page descriptions`**
   Purpose: reduce duplicate default descriptions on generated docs/research/source-document pages.
   Expected files: shared metadata include or relevant generators.
   Risk: medium.
   Validation: Jekyll build, SEO check, page quality.

4. **`docs(audit): add content inventory report generator`**
   Purpose: address issue `#157` and make future audits less manual.
   Expected files: new report script, tests, docs.
   Risk: low.
   Validation: pytest, generated sample report in `/tmp`.

5. **`fix(content): decide DAMA static docs vs dataset-view canonicality`**
   Purpose: reduce duplicate DAMA descriptions/titles or document why both surfaces exist.
   Expected files: DAMA generator and/or canonical metadata.
   Risk: medium.
   Validation: Jekyll build, SEO check, sitemap policy.

## Do not touch list

- Do not edit `_site/` directly.
- Do not edit `llms-full.txt` by hand; use `scripts/generate_atlas_artifacts.py`.
- Do not promote Atlas or Scenario pages to `verified: true` without human review.
- Do not change `robots`, sitemap status, or indexing policy on Level 1 pages as part of cleanup.
- Do not commit `.env.local`, local configs, private exports, raw LinkedIn archives, caches, bytecode, or local report artifacts.
- Do not rewrite homepage, About, Services, or legal pages as part of technical cleanup unless a specific content task authorizes it.
- Do not expose raw grep output for secret-like searches in public reports.

## Appendix

Repository counts:

- Tracked files: 1,192.
- Built HTML pages: 762.
- Indexable pages: 410.
- Noindex pages: 352.
- Sitemap URLs checked: 423.
- URLs with `lastmod` checked: 375.
- Atlas articles discovered by artifact check: 206.

Warning counts:

- Page quality: 73 warnings, 0 critical.
- Accessibility: 91 warnings, 0 critical.
- Internal-link graph: 179 orphans, 190 broken classifications, 742 indexable-to-noindex relationships.
- Indexability audit: no critical issues.

Duplicate metadata scan:

- Duplicate title groups: 4.
- Duplicate description groups: 12.
- Missing titles: 0.
- Missing descriptions: 0.
- H1 count issues in simple scan: 115 pages.

GitHub state:

- Open PRs: 0.
- Open issues: 1.
- Latest `main` CI, IndexNow, and Pages deploy: successful.

Environment note:

- System Ruby is not suitable for this repo. Use `PATH="/opt/homebrew/opt/ruby/bin:$PATH"` for local setup and Jekyll commands.
