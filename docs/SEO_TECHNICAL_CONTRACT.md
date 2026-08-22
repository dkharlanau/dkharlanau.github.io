# SEO, structured data, and discovery contract

This document is the practical entry point for technical SEO, structured data, indexing, sharing metadata, and machine discovery changes in this repository.

It does not replace the underlying policies. Use it to decide what to change, where the source of truth lives, and which checks must pass.

## Objectives

Every public route should:

1. have one stable canonical URL;
2. expose accurate title and description metadata;
3. declare an indexing state consistent with its verification state;
4. emit structured data that matches visible content;
5. appear only in the appropriate sitemap and AI exports;
6. remain understandable to people without relying on metadata;
7. pass rendered-site validation before publication.

## Sources of truth

| Concern | Source of truth | Do not duplicate in |
| --- | --- | --- |
| Public route and canonical URL | Page frontmatter, `_config.yml`, stable route rules in `ARCHITECTURE.md` | Ad-hoc scripts or duplicate pages |
| Verification and indexing eligibility | `docs/ai/CONTENT_VERIFICATION_POLICY.md` and shared content model | Page-specific exceptions without policy |
| Normalised public-page model | `scripts/lib/content_model.py` | A second crawler or eligibility model |
| Quality rules | `config/content-quality.yml` | Hard-coded one-off checks where policy can express them |
| Sitewide JSON-LD | `_includes/seo/structured-data.html` | Page templates with duplicate primary entities |
| Knowledge relationships | `_includes/seo/structured-data-sitewide-graph.html` | Separate conflicting JSON-LD fragments |
| Canonical entity model | `docs/ai/ENTITY_MODEL.md` and entity datasets | Repeated free-text identities |
| AI/search visibility workflow | `docs/ai/AI_VISIBILITY_AUDIT.md` | Unsupported visibility claims |
| Generated AI artifacts | `scripts/generate_atlas_artifacts.py` | Manual edits to generated JSON or `llms-full.txt` |

## Required frontmatter

Every indexable page should define or inherit:

```yaml
title: "Clear page title"
description: "Specific description of the page and its practical value."
permalink: /stable-route/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: YYYY-MM-DD
```

Every review candidate or working page should use:

```yaml
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
```

Rules:

- Never mark a page verified without human review.
- `noindex` pages must not appear in public sitemaps or retrieval-eligible AI exports.
- Do not use a baseline to suppress canonical, privacy, safety, broken-link, or indexing errors.
- `last_modified_at` must represent a meaningful content change, not a mechanical rebuild.

## Titles and descriptions

### Title

- Describe the page first; add the person/site identity only where useful.
- Keep titles distinct across routes.
- Avoid keyword lists, vague slogans, and repeated site-section names.
- The visible H1 and metadata title may differ, but they must describe the same page intent.

### Description

- Explain what the visitor will find and why it matters.
- Prefer a concrete SAP process, diagnostic task, or decision context.
- Do not invent outcomes, experience, endorsements, or client evidence.
- Avoid duplicating the same description across a cluster.

## Canonical URLs and route stability

- Use one canonical URL per public concept.
- Keep established deep URLs stable.
- Use hubs, aliases, redirects, metadata, and graph links instead of moving entire directories.
- Never allow localhost URLs to become a production canonical.
- Judge canonical and `og:url` output from a production-base-url build, not only localhost.
- Internal links should point directly to the canonical route, not to compatibility aliases.

## Indexing contract

| Content state | Robots | Sitemap | Search / AI export |
| --- | --- | --- | --- |
| Reviewed and verified | `index,follow` | Included | Eligible |
| Needs verification | `noindex,follow` | Excluded | Not retrieval eligible |
| Private or unsafe | Not committed | Excluded | Excluded |
| Compatibility route | Follow route policy | Normally excluded as a distinct canonical | Must not duplicate the canonical entity |

Indexing is a publication decision, not a design treatment. A visually polished page remains `noindex` until review requirements are met.

## Structured data

### Primary graph rules

- Emit one primary page identity per canonical route.
- Use `jsonify` for dynamic values; never concatenate unescaped JSON manually.
- The JSON-LD title, description, author, dates, and organisation context must agree with visible content and frontmatter.
- Do not emit rich-result-oriented markup on `noindex` pages.
- Do not add a schema type only because Schema.org defines it; distinguish Google-supported rich results from general machine-readable metadata.
- Do not emit duplicate `Article`, `WebPage`, `Person`, `WebSite`, or breadcrumb identities from several includes.

### Current type routing

The sitewide dispatcher currently resolves pages into types such as:

- `ProfilePage`
- `WebPage`
- `CollectionPage`
- `Article`
- `TechArticle`
- `Dataset`
- `DefinedTerm`
- `DefinedTermSet`
- explicitly supported page overrides

Before adding a new type:

1. confirm the visible page actually satisfies that type;
2. confirm whether it has a supported search feature or is metadata only;
3. add fixture coverage in `tests/test_rendered_structured_data.py`;
4. validate the built JSON-LD, not only the Liquid source.

### Entity relationships

- Use canonical `@id` values consistently.
- Connect pages with `isPartOf`, `about`, `mentions`, `citation`, `subjectOf`, and `relatedLink` only when the relationship is true and useful.
- EPAM may appear as current employment context. Do not imply EPAM publishes, endorses, or owns the personal site.
- Client names, ticket numbers, private projects, and proprietary system identifiers never belong in metadata or structured data.

## Breadcrumbs

- Breadcrumbs should represent the user-visible information hierarchy.
- Item positions must be contiguous.
- The final breadcrumb URL must equal the page canonical URL.
- Compatibility aliases must not create a second canonical breadcrumb trail.
- Breadcrumb labels should be meaningful words, not raw directory slugs.

## Open Graph and sharing

Every important indexable page should have:

- a useful `og:title`;
- a specific `og:description`;
- canonical `og:url`;
- an intentional image or the approved site default;
- image dimensions and accessible descriptive metadata where supported.

The default share visual should use the site’s blue diagnostic-signal language. Do not place small body text in social images.

## Sitemaps and discovery files

- Sitemaps contain canonical, indexable URLs only.
- Generated sitemap files are never hand-edited.
- `robots.txt`, `llms.txt`, `llms-full.txt`, AI indexes, and data sitemaps must agree with verification and indexing policy.
- Machine-readable endpoints need stable content types, canonical URLs, and links from the relevant human-readable hub.
- Generated Atlas/AI artifacts are regenerated through their owner script and checked for drift.

## Internal linking

- Every flagship page should link to its parent hub, relevant evidence, and a reasonable next action.
- Link text must describe the destination; avoid repeated `Read more` links.
- Do not create dense automated link blocks that make pages harder to read.
- Topic relationships are graph-like. Do not duplicate content only to force it into one directory hierarchy.
- Broken public links are hard failures.

## Content and design alignment

- Metadata cannot compensate for weak visible content.
- The first screen should make the page topic and audience clear.
- Structured data claims must be supported by visible text or canonical datasets.
- Review status should remain visible where it changes how readers interpret evidence.
- Navigation, headings, breadcrumbs, and metadata should use the same product vocabulary.
- Follow `DESIGN.md` for text contrast, component sizing, hierarchy, and responsive quality.

## Performance and crawlability

- Important content and links must be present in generated HTML without requiring client-side JavaScript.
- Use explicit image dimensions and optimised formats to reduce layout shift.
- Avoid blocking the first readable paint with decorative assets.
- JavaScript enhancements must preserve canonical links and readable fallback content.
- Error pages, redirect routes, and empty search results must not accidentally become duplicate indexable content.

## Change workflow

For a new or materially changed page:

1. Choose the canonical product area and stable route.
2. Set verification, robots, and sitemap state.
3. Write a unique title, H1, and description.
4. Select or confirm the structured-data type.
5. Add breadcrumbs and useful internal relationships.
6. Build the production site.
7. Inspect the rendered HTML and JSON-LD.
8. Run the relevant validators.
9. Visually check desktop and mobile.
10. Regenerate owned discovery artifacts when required.

## Validation commands

Run the smallest relevant checks first, then the full publication sequence.

```sh
bundle exec jekyll build --trace
python3 scripts/check_seo.py _site
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_rendered_structured_data.py
python3 scripts/check_structured_data.py _site
python3 scripts/check_sitemap_policy.py --site-dir _site --repo-dir . --fail-on-critical
python3 scripts/check_links.py _site
python3 scripts/content_quality.py check --site-dir _site
python3 scripts/generate_atlas_artifacts.py --check
git diff --check
```

Do not report SEO, structured-data, indexing, or AI-discovery success unless the corresponding rendered checks actually pass.

## Review checklist

Before accepting a change, confirm:

- [ ] Canonical URL is stable and production-correct.
- [ ] Title, H1, and description express the same intent.
- [ ] Robots, sitemap, verification, and AI eligibility agree.
- [ ] JSON-LD parses and has no duplicate primary entities.
- [ ] Structured claims match visible content.
- [ ] Breadcrumb positions and terminal URL are correct.
- [ ] Internal links resolve and use descriptive labels.
- [ ] Social metadata has the correct URL, copy, and image.
- [ ] No client data, private identifiers, or unsupported claims are exposed.
- [ ] Rendered desktop and mobile pages remain readable and navigable.
- [ ] Required generators and checks pass.

## Related documentation

- `ARCHITECTURE.md` — stable routes and product architecture.
- `PROJECT_MAP.md` — repository and product map.
- `docs/content-quality-pipeline.md` — publication quality architecture.
- `docs/ai/CONTENT_VERIFICATION_POLICY.md` — verification and indexing levels.
- `docs/ai/ENTITY_MODEL.md` — canonical public entity model.
- `docs/ai/AI_VISIBILITY_AUDIT.md` — search and AI visibility testing.
- `docs/ai/RECOMMENDATION_POSITIONING.md` — relevance and recommendation boundaries.
- `DESIGN.md` — visual, content, component, and accessibility contract.
