# Search and AI Discovery Technical Readiness Audit — 2026-07-03

## Scope and counting rules

This audit covers the rendered Jekyll site, source frontmatter, custom sitemaps, JSON-LD, internal links, and generated Atlas/AI discovery artifacts. It does not assess ranking, traffic, or external index coverage.

- **Public pages** are rendered HTML files in `_site`.
- **Indexable/noindex pages** are counted from rendered `meta[name=robots]`.
- **Verified/unverified pages** are source pages with explicit `verified: true` or `verified: false`; pages outside the verification system are not silently classified as verified.
- **Sitemap URLs** are unique `<loc>` values across the rendered section sitemaps. This includes machine-readable data endpoints as well as HTML pages.
- **Broken links** are local rendered-site links checked against files in `_site`.
- Duplicate metadata counts below apply to indexable HTML pages.

## Executive result

The site has a consistent discovery boundary after the fixes in this task:

- all 151 reviewed/verified inventory pages are present in the sitemap and `ai/verified-pages.json`;
- all 41 verified Atlas articles are present in `llms-full.txt`;
- no rendered noindex page is present in a sitemap;
- no unverified Atlas page is present in a sitemap or `llms-full.txt`;
- indexable pages have unique canonicals, titles, and descriptions;
- article-like indexable pages emit truthful Article/TechArticle and BreadcrumbList schema;
- generated Radar/News drafts remain public but are now noindex until review;
- internal operational documentation and reports are noindex, while `docs/dama/` remains indexable;
- the homepage source and homepage data were not changed.

## 1. Current technical search state

| Metric | Baseline | Final |
|---|---:|---:|
| Rendered public HTML pages | 762 | 763 |
| Indexable HTML pages | 410 | 365 |
| Noindex HTML pages | 352 | 398 |
| Explicitly verified source pages | 151 | 151 |
| Explicitly unverified source pages | 218 | 218 |
| Sitemap URLs | 423 | 380 |
| `llms-full.txt` pages | 41 | 41 |
| Broken local links | 0 | 0 |
| Duplicate canonical values | 0 | 0 |
| Duplicate title values | 2 | 0 |
| Duplicate description values | 2 | 0 |

The sitemap has 15 more URLs than the indexable HTML count because it intentionally includes machine-readable endpoints such as resume, catalog, dataset, and AI index files.

## 2. Coverage map

### Indexable technical clusters

The verified inventory contains 151 pages:

- 51 Atlas pages, including 28 diagnostic routes/indexes;
- 100 Skill Hub pages across SAP AMS, integration architecture, AI-assisted analysis and development, business analysis, data governance, testing, decision validation, documentation, and execution control.

The Atlas full-text artifact contains 41 verified articles:

- diagnostics: 27;
- concepts: 4;
- AI operations: 3;
- automation: 3;
- data quality: 2;
- maps: 2.

The sitemap and AI inventory have full coverage of these verified pages. No verified inventory page is missing from the sitemap. `llms-full.txt` intentionally remains Atlas-only under the verification policy; the broader site-wide route is `ai/verified-pages.json`.

### Internal linking

Before the fix, three reviewed diagnostics had only one inbound HTML link:

- SAP IDoc Diagnostics;
- SAP Authorization and Role Diagnostics;
- SAP Transport Governance Diagnostics.

They are now linked from both the Atlas hub and the diagnostics index. The only verified Atlas route with one inbound link after the fix is the low-priority Atlas Links reference index.

Remaining zero-inbound indexable pages are deliberate machine endpoints, repository source documents, legal/utility pages, and profile-support surfaces. They are listed as deferred items below rather than being bulk-linked into editorial hubs.

### Metadata and schema

- Missing canonical URLs on indexable pages: 0.
- Duplicate canonical values on indexable pages: 0.
- Duplicate titles on indexable pages: 0.
- Duplicate descriptions on indexable pages: 0.
- Missing descriptions on indexable pages: 0.
- Indexable article-like pages missing Article/TechArticle schema: 0.
- Indexable article-like pages missing BreadcrumbList schema: 0.

Article publisher schema now identifies the author/site owner, not the author's employer. The employer Organization remains represented only as the truthful `worksFor` relationship on the profile.

## 3. Risk map

| Risk | Baseline | Disposition |
|---|---|---|
| Generated Radar/News drafts were indexable despite “manual review required” text | Present on 10 pages | Fixed with collection-level noindex and sitemap exclusion |
| Noindex pages in sitemap | None detected | Guarded by rendered sitemap validation |
| Unverified Atlas pages in sitemap or `llms-full.txt` | None detected | Guarded by generator and tests |
| Verified pages missing from sitemap/AI inventory | None detected | Confirmed against all 151 inventory entries |
| Broken local links | None in rendered-site checker | Confirmed; link-graph auditor fixed to agree |
| Duplicate canonicals | None | Confirmed |
| Duplicate indexable titles/descriptions | Two values each | Fixed through page-content metadata fallback and noindex policy |
| Employer represented as article publisher | Present | Fixed; publisher is now the Person/site author |
| Operational docs and reports consuming crawl space | Present | Fixed with scoped defaults; DAMA public pages explicitly remain indexable |
| Artifact scanner emitted YAML warnings for templates/non-pages | Present | Fixed with strict frontmatter boundaries and template exclusion |
| Private path leakage through generated artifacts | Not detected | Existing generator/test controls retained |
| Homepage source drift | Not present | Homepage source, data, sections, navigation, and design untouched |

## 4. Action list

### Fix now

- Make Radar/News review candidates noindex and exclude them from sitemaps.
- Noindex repository documentation, reports, and agent-skill source pages while preserving public DAMA pages.
- Use page content as the metadata fallback instead of repeating a site-wide generic description.
- Correct personal article publisher schema.
- Strengthen Atlas routes to three high-value reviewed diagnostics.
- Improve those diagnostics' descriptions without changing review dates or verification state.
- Fix artifact frontmatter parsing and link-graph URL normalization.
- Add regression tests for noindex defaults, DAMA overrides, and article publisher identity.
- Regenerate Atlas manifest, compact index, related graph, verified inventory, and `llms-full.txt`.
- Regenerate the content-maintenance registry so freshness/watch status reflects the audit date.

### Leave unchanged

- Homepage source, homepage data, hero, CTA, navigation, and visual design.
- Verification state and review dates for all pages.
- Atlas-only scope of `llms-full.txt`; site-wide verified discovery remains in `ai/verified-pages.json`.
- `.well-known/agent-skills/` HTML endpoints, which are expected to be reached through machine discovery rather than normal HTML navigation.
- Public DAMA pages under `docs/dama/`.

### Defer

- Link or noindex the remaining profile-support and legal utility orphans only after deciding whether each should be a search landing page. Bulk linking would create navigation noise.
- Resolve non-critical page-quality warnings such as section-index H1/title wording and thin noindex signal drafts in a separate editorial task.
- Review whether root `CITATION.md`, certifications, publications, changelog, and legal utility pages need dedicated hub links; this task did not edit protected profile surfaces.
