---
layout: default
title: "Findability, Analytics, and Quality Audit - 2026-06-14"
description: "Noindex audit report for analytics coverage, search findability, metadata quality, indexing policy, AI discovery, and site quality checks."
robots: noindex,follow
sitemap: false
---

# Findability, Analytics, and Quality Audit - 2026-06-14

Repository: `dkharlanau/dkharlanau.github.io`  
Branch: `fix/findability-analytics-quality-audit`  
Scope: public GitHub Pages website analytics, search discoverability, technical SEO, AI-discovery surfaces, internal linking, metadata, and quality gates.

## Executive Summary

GA4 was already installed before this audit, but the implementation was hardcoded directly in `_includes/head.html`. The measured tag was `G-T2TS9NCN2N`. No Google Tag Manager container was detected.

The implementation is now config-driven through `_config.yml` and `_includes/analytics.html`. Standard Jekyll HTML pages, the layoutless purchase-order redirect page, and generated DAMA HTML pages all receive the same GA4 snippet. XML, JSON, TXT, `robots.txt`, `llms.txt`, `llms-full.txt`, and sitemap outputs remain untagged.

Analytics coverage after fixes:

- Total built HTML pages checked: 762
- Tagged HTML pages: 762
- Missing analytics tags: 0
- Duplicate analytics tags: 0
- Non-HTML files with analytics snippets: 0

Metadata and quality improvements:

- Added `scripts/check_analytics_coverage.py` and focused tests.
- Reduced page-quality warnings from 105 to 73 by aligning JSON-LD description truncation with meta-description truncation.
- Kept Atlas verification and noindex policy unchanged.
- Kept homepage, About, Services, and legal copy unchanged.

## Search Intent Map

| Query | Best current landing page | Support status |
|---|---|---|
| SAP AMS consultant | `/` and `/services/` | Strong. Homepage and services metadata use SAP AMS language without stuffing. |
| SAP support diagnostics | `/atlas/diagnostics/` | Strong for diagnostic intent; H1/title alignment is a non-critical warning. |
| SAP AMS support improvement | `/services/sap-ams-improvement/` and `/ai/sap-ams-improvement/` | Good. Commercial and AI-readable routes exist. |
| SAP SD MM consultant | `/about/`, `/services/`, `/atlas/sap/` | Moderate. SD/MM appears in entity positioning, but no single SD/MM service landing page is dedicated to this exact query. |
| SAP incident analysis | `/atlas/diagnostics/` and `/ai/incident-prevention-rca/` | Good. Diagnostic and AI intent surfaces both exist. |
| SAP master data diagnostics | `/atlas/data-quality/` and relevant Atlas diagnostics | Good. Master data and data-quality pages are discoverable. |
| SAP IDoc diagnostics | `/atlas/diagnostics/sap-idoc-diagnostics/` | Strong if the page remains verified/indexable; policy checks passed. |
| SAP procurement diagnostics | `/atlas/diagnostics/` and procurement Atlas pages | Good. Several procurement pages exist; some are noindex candidates by policy. |
| SAP order-to-cash support | `/services/sap-ams-improvement/` and Atlas O2C pages | Good. Services describe O2C stabilization. |
| SAP procure-to-pay support | `/atlas/diagnostics/` and procurement pages | Moderate. Coverage exists, but a clean P2P hub could improve intent matching later. |
| AI agents for SAP support | `/atlas/ai-operations/ai-agent-for-sap-support/` and `/ai/practical-ai-for-sap-support/` | Strong. Dedicated AI-operation and AI-readable routes exist. |
| AI-assisted SAP AMS | `/`, `/services/`, `/atlas/ai-operations/` | Strong. Repeated in site positioning and Atlas hubs. |
| enterprise support knowledge systems | `/atlas/ai-operations/` and `/skill-hub/work-documentation-handover/` | Good. Concept is present, but exact phrase can be strengthened in a future content pass. |
| side-by-side automation for SAP | `/atlas/automation/` and `/services/side-by-side-sap-automation/` if present | Moderate. Automation coverage exists; route naming should be checked before adding more links. |
| SAP support knowledge reuse | `/skill-hub/work-documentation-handover/`, `/atlas/ai-operations/`, `/ai/` | Good. Human and AI surfaces exist. |

## Analytics Findings

Before:

- GA4 present: yes.
- GA4 ID: `G-T2TS9NCN2N`.
- GTM present: no.
- Injection path: hardcoded snippet in `_includes/head.html`.
- Coverage gap: 26 built HTML pages were missing analytics because they bypassed the shared layout or were generated standalone.
- Non-HTML injection: none detected.

After:

- GA4 present: yes.
- GA4 ID: `G-T2TS9NCN2N`.
- GTM present: no.
- Injection path: `_config.yml` -> `_includes/analytics.html` -> `_includes/head.html`, with generator support in `scripts/generate_dama_pages.js`.
- Coverage: 762/762 built HTML pages.
- Non-HTML injection: none detected.

The checker fails on:

- missing HTML tags,
- incomplete GA4 snippets,
- duplicate GA4 script/config markers,
- mixed GA4 and GTM markers on one page,
- analytics markers in XML, JSON, TXT, `robots.txt`, `llms.txt`, `llms-full.txt`, or sitemap-like files.

## Metadata and Structured Data

Current state:

- `scripts/check_seo.py _site` passed for 762 HTML files.
- `scripts/check_structured_data.py _site` passed for 762 HTML files.
- Canonical and `og:url` metadata are present and aligned on indexable pages checked by the existing SEO script.
- JSON-LD parses across the built site.
- Structured-data description truncation now matches meta-description truncation, reducing page-quality warnings from 105 to 73.

Residual warnings:

- Some Atlas and Skill Hub section pages use editorial H1s that do not exactly match HTML titles.
- Some note and radar titles exceed the page-quality preferred length.
- Some short news/radar entries are thin by the page-quality heuristic.
- Generated docs and agent-skill exports contain duplicate H1s.

These are non-critical, broad editorial/template issues. They should be handled in a separate content-quality branch, not as a side effect of analytics coverage.

## Indexing and Sitemap Policy

Validation state:

- Indexing policy check passed.
- Sitemap policy check passed for 423 URLs.
- No unverified Atlas pages were promoted.
- No noindex pages were intentionally added to the sitemap.
- `llms-full.txt` was not edited by hand.

Important policy note:

- The scenarios area remains Level 1 by repository policy.
- This audit did not change `verified`, `status`, `robots`, or `sitemap` frontmatter on Atlas or scenario content.

## Internal Linking

Validation state:

- `scripts/check_links.py _site` reported no broken local links.
- `scripts/audit_internal_links.py` produced a diagnostic graph report with 178 orphans, 190 pages with broken-link classifications, and 742 indexable-to-noindex relationships.

Interpretation:

- The local-link validator is the pass/fail gate and found no broken local links.
- The graph audit is broader and noisy for this repository because generated docs, noindex skills, `.well-known` pages, report pages, and source-document renders are intentionally not part of the normal human navigation graph.
- No broad internal-link rewrite was made in this branch.

## AI Discovery

Checked surfaces exist in the build:

- `/llms.txt`
- `/llms-full.txt`
- `/ai/`
- `/ai/atlas-compact-index.json`
- `/ai/verified-pages.json`
- `/atlas/manifest.json`
- `/datasets/manifest.json`
- `/.well-known/agent-skills/index.json`
- `/agent-skills/`

Validation state:

- `scripts/validate_ai_endpoints.py _site` passed.
- Analytics markers are absent from `llms.txt`, `llms-full.txt`, JSON endpoints, and sitemap files.

## Top Page Quality Review

| Page | Status |
|---|---|
| `/` | Strong title, H1, description, canonical, social metadata, and analytics coverage. No homepage copy changes made. |
| `/about/` | Strong canonical profile surface. No private data added. |
| `/services/` | Strong commercial routing surface for SAP AMS, O2C, integration, operational memory, and automation. |
| `/atlas/` | Strong knowledge hub. H1/title style is editorial rather than exact-match; warning only. |
| `/skill-hub/` | Strong skills hub for human and agent workflows. |
| `/ai/` | Strong AI routing hub. Endpoint validation passed. |
| `/datasets/` | Dataset hub builds and links to machine-readable surfaces. |
| Top verified Atlas pages | Build, SEO, structured data, indexing, and sitemap policy checks passed. |

## Fixes Made

- Added `google_analytics_id: "G-T2TS9NCN2N"` to `_config.yml`.
- Added `_includes/analytics.html` with GA4/GTM branching. GA4 is active; GTM is available only if configured later.
- Replaced the hardcoded GA4 snippet in `_includes/head.html` with the shared include.
- Added analytics to the layoutless purchase-order redirect page.
- Updated `scripts/generate_dama_pages.js` so generated DAMA pages include analytics from `_config.yml`.
- Regenerated `docs/dama/*.html` and `docs/dama/tags/*.html`.
- Added `scripts/check_analytics_coverage.py`.
- Added `tests/test_analytics_coverage.py`.
- Aligned JSON-LD description truncation with meta-description truncation in `_includes/seo/structured-data.html`.

## Validation Snapshot

Commands already run during the audit:

```text
python3 -m pytest tests/test_analytics_coverage.py
PATH="/opt/homebrew/opt/ruby/bin:$PATH" ./bin/setup
PATH="/opt/homebrew/opt/ruby/bin:$PATH" bundle exec jekyll clean
PATH="/opt/homebrew/opt/ruby/bin:$PATH" bundle exec jekyll build
python3 scripts/check_analytics_coverage.py --site-dir _site
python3 scripts/check_seo.py _site
python3 scripts/check_structured_data.py _site
python3 scripts/check_indexing_policy.py --site-dir _site --fail-on-critical
python3 scripts/check_sitemap_policy.py --site-dir _site --repo-dir . --fail-on-critical
python3 scripts/validate_ai_endpoints.py _site
python3 scripts/check_links.py _site
python3 scripts/check_content_quality.py --fail-on-critical
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
python3 scripts/audit_indexability.py --site-dir _site --fail-on-critical --output-dir /tmp/cv-ai-validation-reports
python3 scripts/audit_internal_links.py --site-dir _site --output-dir /tmp/cv-ai-validation-reports
```

Known local environment note:

- Running `bundle exec jekyll` without the Homebrew Ruby path uses system Ruby 2.6.10 and fails.
- Running `./bin/setup` without the Homebrew Ruby path also fails for the same reason.
- With `PATH="/opt/homebrew/opt/ruby/bin:$PATH"`, setup and Jekyll build pass using Ruby 3.4.7.

## Safety Confirmations

- No secrets, API keys, or credentials were added.
- GA4 measurement ID is public tracking configuration, not a secret.
- No private corpus content, client names, tickets, or internal incident IDs were added.
- No Atlas page was promoted to verified.
- No unverified page was intentionally indexed.
- No sitemap or `llms-full.txt` file was edited by hand.
- No homepage, About, Services, or legal copy was rewritten.
