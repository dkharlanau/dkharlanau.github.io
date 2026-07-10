# AI and Search Visibility Technical Audit — 2026-07-10

## Scope

This audit covers the repository, rendered Jekyll site, production responses, structured data, internal link graph, indexing boundaries, and public AI-readable artifacts for `https://dkharlanau.github.io`.

The scores below measure technical readiness, not rankings, traffic, backlinks, or whether an AI system will recommend the author. A higher score means the site gives crawlers and retrieval systems clearer, safer, more consistent evidence.

## Executive result

The strongest risk was not missing metadata. It was trust-boundary ambiguity: public Atlas machine indexes exposed metadata for 165 unverified/noindex articles alongside 41 reviewed articles, while several artifacts used relative URLs. An answer engine could detect the status fields, but the safest retrieval path was not explicit.

The implementation now makes the public Atlas manifest, compact index, relationship graph, and full-text pack verified-only. Every entry uses a canonical production URL. Structured data connects the author, website, topic collection, article, breadcrumb, and eligible related pages through stable IDs. Homepage copy and layout were not changed.

## Before and after scores

| Area | Before | After | Evidence behind the change |
|---|---:|---:|---|
| Crawlability | 90 | 94 | All required endpoints return `200`; data sitemap coverage increased from 13 to 16 endpoints; broken local links remain zero. |
| Structured data | 72 | 92 | `WebSite` is now declared once; verified Atlas and Skill Hub section indexes emit `CollectionPage`; articles connect to website, author, collection, breadcrumb, section, and eligible related pages. |
| Author/entity clarity | 78 | 94 | One canonical Person ID is used across HTML, catalog, and `llms.txt`; two verified hubs missing author metadata were corrected. |
| Topic-cluster strength | 74 | 84 | Verified collection hubs expose eligible children with `hasPart`; articles point back to topic collections; Notes, Certifications, and Publications gained a hub inlink. |
| Verified-content trust | 65 | 96 | Public Atlas artifacts changed from 206 mixed-status entries to 41 reviewed/verified/indexable entries; noindex and review-candidate metadata is excluded. |
| AI-readable artifacts | 60 | 94 | Manifest, compact index, related graph, verified inventory, and full-text pack use canonical URLs and deterministic eligibility rules. |
| Citation readiness | 78 | 90 | Stable entity IDs, canonical article URLs, author/publisher links, review metadata, and eligible related links are machine-readable. |
| Search visibility foundations | 83 | 92 | Crawl, canonical, sitemap, metadata, JSON-LD, internal-link, and verification checks are aligned; external authority remains outside repository control. |
| Deployment reliability | 74 | 88 | The repository build succeeds with the required Ruby; a date-sensitive test and its tracked-file side effect were corrected; CI and Pages still provide the final gate. |

## Findings by priority

### P0 — none found

No production outage, robots-wide block, canonical collapse, sitemap failure, private-path leak, or unverified full-text leak was found. The live homepage, robots file, `llms.txt`, `llms-full.txt`, verified-page inventory, and sitemap returned `200` during the audit.

### P1 — mixed verification states in public AI indexes

**Evidence before:**

- `atlas/manifest.json`: 206 entries — 41 verified and 165 unverified.
- `ai/atlas-compact-index.json`: 206 entries, including noindex review candidates.
- `ai/rag/related.json`: 926 relationships across mixed verification states.
- `llms-full.txt`: 41 verified articles only.

This made the full-text boundary safe but left the surrounding routing artifacts ambiguous.

**Affected URLs:**

- `https://dkharlanau.github.io/atlas/manifest.json`
- `https://dkharlanau.github.io/ai/atlas-compact-index.json`
- `https://dkharlanau.github.io/ai/rag/related.json`
- `https://dkharlanau.github.io/llms-full.txt`

**Fix:** one eligibility rule now governs all public Atlas retrieval artifacts: `verified: true`, `status: reviewed`, indexable robots state, and `sitemap: true`. The manifest and compact index now contain 41 entries; the relationship graph contains 126 edges where both source and target are eligible. Review candidates remain in repository source but are not advertised as retrieval-ready.

### P1 — incomplete entity and topic relationships

**Evidence before:**

- `WebSite` was redefined on every indexable page.
- Atlas section hubs and Skill Hub group indexes were classified as articles instead of collections.
- Article schema did not connect to its canonical topic collection.
- Article schema lacked `articleSection`, `inLanguage`, `breadcrumb`, and filtered related-page relationships.
- `llms.txt` documented both `https://dkharlanau.github.io/#dkharlanau` and a non-emitted `https://dkharlanau.github.io/about/#person` anchor.

**Affected URLs:** all indexable HTML pages, especially:

- `https://dkharlanau.github.io/`
- `https://dkharlanau.github.io/about/`
- `https://dkharlanau.github.io/atlas/diagnostics/`
- `https://dkharlanau.github.io/atlas/diagnostics/sap-idoc-status-diagnostics/`
- `https://dkharlanau.github.io/skill-hub/ai-assisted-development/`

**Fix:** the homepage owns the single `WebSite` declaration; other entities reference its stable ID. Verified section hubs emit `CollectionPage` and `hasPart`. Articles emit stable `#article` IDs and connect to the Person, WebSite, topic CollectionPage, BreadcrumbList, section, and only verified/indexable related pages. The Person ID is consolidated to `https://dkharlanau.github.io/#dkharlanau`.

### P1 — non-canonical URLs in machine artifacts

**Evidence before:** entry URLs in the Atlas manifest, compact index, related graph, verified-page inventory, and `llms-full.txt` were root-relative.

**Fix:** public URL fields now use `https://dkharlanau.github.io/...`. Generator checks and regression tests enforce the origin.

### P2 — incomplete machine-endpoint discovery

**Evidence before:** `sitemap-data.xml` listed 13 endpoints but omitted the full-text pack, Atlas manifest, and Atlas relationship graph.

**Fix:** the data sitemap now lists 16 endpoints, including:

- `https://dkharlanau.github.io/llms-full.txt`
- `https://dkharlanau.github.io/atlas/manifest.json`
- `https://dkharlanau.github.io/ai/rag/related.json`

Shared page metadata also exposes the verified-page inventory and full-text pack through typed `<link>` elements.

### P2 — sparse hub metadata and internal links

**Evidence before:** two verified hubs lacked an author; ten verified Atlas hubs lacked tags; Notes, Certifications, and Publications had zero indexable inlinks in the rendered graph.

**Fix:** verified hubs now have consistent author/tag metadata, and the AI routing hub links to those three public profile-support surfaces. Indexable orphan count decreased from 12 to 9. The remaining orphans are machine-skill endpoints, citation/changelog utilities, and legal pages; bulk-linking them would add navigation noise without strengthening topic relevance.

### P2 — validation was date-sensitive and modified a tracked registry

The maintenance test assumed there could never be a high-priority page after a one-time override. That became false as research pages aged. The test also rewrote `data/content-maintenance/page-registry.json` without restoring it.

The test now validates the real invariant — an explicit `none` priority override cannot remain high priority — and restores the registry after its mutation test.

### P3 — editorial and external authority limitations

- The page-quality checker still reports non-critical title/H1 and long-title warnings.
- Nine low-value utility/legal URLs remain orphaned.
- Search Console, Bing Webmaster Tools, crawl/index coverage, query impressions, and rich-result reports require account access.
- Backlinks, independent mentions, citations, and editorial authority cannot be created by repository metadata.
- Some reviewed pages need stronger source citation depth before they should be treated as flagship evidence.

## Entity graph after the change

```text
Person  https://dkharlanau.github.io/#dkharlanau
  ├── publishes WebSite  https://dkharlanau.github.io/#website
  ├── main entity of ProfilePage  https://dkharlanau.github.io/about/#webpage
  └── authors Article / TechArticle entities

WebSite
  └── contains/refers to CollectionPage topic hubs
        └── hasPart Article / TechArticle
              ├── mainEntityOfPage WebPage
              ├── breadcrumb BreadcrumbList
              ├── articleSection topic label
              └── relatedLink reviewed/indexable pages only
```

Stable IDs use these conventions:

- Person: `https://dkharlanau.github.io/#dkharlanau`
- WebSite: `https://dkharlanau.github.io/#website`
- Page or collection: canonical URL plus `#webpage`
- Article: canonical URL plus `#article`
- Breadcrumb: canonical URL plus `#breadcrumb`

## Measured final state

| Check | Result |
|---|---:|
| Rendered HTML pages | 764 |
| Indexable / noindex HTML pages | 365 / 399 |
| Verified inventory entries | 151 |
| Verified Atlas full-text pages | 41 |
| Public verified Atlas manifest entries | 41 |
| Public verified compact-index entries | 41 |
| Eligible related-content edges | 126 |
| Verified inventory pages missing from sitemap | 0 |
| Duplicate non-global JSON-LD IDs | 0 |
| Noindex pages with rich-result JSON-LD | 0 |
| Verified pages missing date / author / Atlas tags | 0 / 0 / 0 |
| Broken local links | 0 |
| Data sitemap endpoints | 16 |

## Validation results

| Validation | Result |
|---|---|
| `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests` | 272 passed |
| `python3 scripts/check_public_repo.py` | Passed for 1,194 tracked files |
| `python3 scripts/generate_atlas_artifacts.py --check` | Passed; all generated artifacts current |
| Repeated generator run with SHA-256 comparison | Passed; all five generated artifacts were byte-identical |
| `bundle exec jekyll build` with repository-required Ruby | Passed; 764 HTML pages rendered |
| `python3 scripts/check_links.py _site` | Passed; zero broken local links |
| `python3 scripts/check_seo.py _site` | Passed |
| `python3 scripts/check_indexing_policy.py --repo-dir . --site-dir _site --fail-on-critical` | Passed |
| `python3 scripts/check_structured_data.py _site` | Passed for 764 HTML pages |
| `python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical` | Passed; zero critical issues, nine warnings |
| `git diff --check` | Passed |

## Homepage impact

`index.md`, `_data/home.yml`, homepage sections, copy, CTA text, and layout were not changed. The rendered homepage receives only shared technical-head changes: one canonical `WebSite` entity, a Person publisher reference, and links to verified AI discovery artifacts.

## Remaining work outside this repository change

1. Verify sitemap processing and index coverage in Google Search Console and Bing Webmaster Tools.
2. Monitor crawl and query data before deciding whether utility or legal pages should be linked or noindexed.
3. Earn independent backlinks, third-party mentions, and source citations from relevant SAP, data-governance, and AI-operations publications.
4. Promote content to flagship status only after human review and stronger primary-source citation coverage.
5. Validate live rich-result parsing after deployment and watch for schema-consumer warnings; schema correctness does not guarantee a rich result.
