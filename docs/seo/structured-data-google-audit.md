---
layout: default
title: "Structured Data Audit — Google-aligned Foundation"
description: "Audit and implementation map for Google-aligned structured data on dkharlanau.github.io."
robots: noindex,follow
sitemap: false
---

# Structured Data Audit — Google-aligned Foundation

**Scope:** Audit the public site’s JSON-LD structured data against Google Search Central documentation, then implement a conservative, maintainable foundation.

**Date:** 2026-06-13

## 1. Official Google documentation used

- [Introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Structured data gallery / supported Google Search features](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)
- [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Breadcrumb structured data](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)
- [Dataset structured data](https://developers.google.com/search/docs/appearance/structured-data/dataset)
- [Event structured data](https://developers.google.com/search/docs/appearance/structured-data/event)
- [Course structured data](https://developers.google.com/search/docs/appearance/structured-data/course)
- [ProfilePage structured data](https://developers.google.com/search/docs/appearance/structured-data/profile-page)
- [Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization)
- [Rich Results Test](https://support.google.com/webmasters/answer/7445569)

## 2. Key principle

> Structured data must describe the visible page content accurately. Do not claim eligibility for Google rich results unless the type is documented by Google Search Central.

Google Search uses schema.org as vocabulary, but the Google Search Central docs are the authoritative source for Google behavior. Generic schema.org types that are not listed in the structured data gallery are **not** Google-supported rich result types, even if they are valid schema.org.

## 3. Google-supported rich result types vs. schema.org metadata

| Category | Examples | Google rich result? | Usage on this site |
|---|---|---|---|
| Google-supported rich result | `Article`, `BreadcrumbList`, `Dataset`, `Event`, `Course`, `ProfilePage`, `Organization` | Yes | Emit only on indexable pages with real, visible data. |
| Valid schema.org metadata, no Google rich result promise | `WebPage`, `CollectionPage`, `DataCatalog`, `Person` (as author), `TechArticle` | No | May be used for machine readability, but documented as metadata only. |
| Not relevant / not used | `Product`, `Review`, `AggregateRating`, `JobPosting`, `Recipe`, `LocalBusiness`, `Movie`, `VideoObject`, `SoftwareApplication` | Some are supported but not applicable | Do not use. |

**Important:** `TechArticle` is valid schema.org but is **not** one of the Google-supported Article subtypes (`Article`, `NewsArticle`, `BlogPosting`). This audit replaces `TechArticle` with `Article` for Atlas pages.

## 4. Relevant types for this site

- `Article` — notes, blog posts, news items, radar signals, verified Atlas pages, Skill Hub pages.
- `BreadcrumbList` — any indexable page with a clear hierarchy.
- `Dataset` — dataset detail pages (currently emitted as inline JSON-LD generated into the page; include support added for future use).
- `ProfilePage` + `Person` — the canonical `/about/` profile page.
- `Organization` — the profile page’s employer (`/about/` only; homepage is deferred).
- `CollectionPage` — aggregator/list pages (schema.org metadata only).

## 5. Types intentionally not used

- `TechArticle` — not a Google-supported Article subtype.
- `Product`, `Review`, `AggregateRating` — no products or user reviews on the site; fake ratings/reviews would violate guidelines.
- `Event`, `Course` — no real events or courses currently exist. Guarded support is added but not activated.
- `LocalBusiness` — not a local business site.
- `FAQPage` — already exists on the homepage only; left untouched in this pass.
- `Organization` on the homepage — deferred because the homepage is off-limits for this implementation pass.

## 6. Risks identified

| Risk | Current issue | Mitigation |
|---|---|---|
| Misleading markup | `TechArticle` used for Atlas pages; generic default image used as `Article.image` for every article. | Use Google-supported `Article`; only emit `image` when an explicit page-level image exists. |
| Rich results on noindex pages | `Article` + `BreadcrumbList` emitted for notes/blog/Atlas regardless of `robots`. | Single `allow_indexing` guard skips all rich-result JSON-LD on noindex pages. |
| Duplicate/conflicting `@id` | Article blocks had no `@id`; multiple blocks could describe the same page ambiguously. | Assign one `@id` per entity (`#webpage`, `#article`, `#breadcrumb`, `#dataset`, etc.). |
| Wrong dates | `last_reviewed` was used as `datePublished` for Atlas pages. | Use `date`/`published` for `datePublished`; use `last_modified_at`/`updated`/`last_reviewed` for `dateModified`; omit when absent. |
| Fake entities | Organization was emitted only from public resume data; no fake reviews/offers. | Continue using only verified public data. |
| Over-marking | DataCatalog emitted on catalog pages; valid but not a Google rich result. | Retain as schema.org metadata only and document it. |

## 7. Implementation map by page family

| Page family | Structured data type | Reason / guard |
|---|---|---|
| Notes, blog, news, radar (detail) | `Article` + `BreadcrumbList` | Indexable article-like pages. |
| Verified Atlas pages (`verified:true`, `status:reviewed`) | `Article` + `BreadcrumbList` | Google supports Article for technical/expert content; no `TechArticle`. |
| Unverified Atlas / review candidates | None | `noindex` pages must not carry rich-result markup. |
| Scenarios, Research | None | All are `noindex` by policy. |
| Skill Hub pages | `Article` + `BreadcrumbList` | Indexable, article-like working-skill pages. |
| Services pages | `WebPage` + `BreadcrumbList` | Indexable landing pages, not articles. |
| Dataset detail pages | Inline `Dataset` | Already generated into pages; validated for correctness and duplicate `@id`. |
| Dataset / AI catalog pages | `CollectionPage` + `DataCatalog` + `BreadcrumbList` | `CollectionPage` is schema.org metadata; `DataCatalog` is metadata only, not a Google rich result. |
| About page | `ProfilePage` + `Person` + `Organization` + `BreadcrumbList` | Canonical profile page; Organization does not require homepage changes. |
| Homepage | Untouched | `WebSite` + `FAQPage` remain in `_includes/head.html`. |

## 8. Decision table

| Page family | Example URLs/files | Available metadata | Recommended type | Missing fields | Action | Reason |
|---|---|---|---|---|---|---|
| Standard articles | `_notes/*.md`, `_blog/*.md`, `_news/*.md`, `_radar/*.md` | title, description, date, tags | `Article` | none | implement now | Google-supported, content is visible |
| Verified Atlas | `atlas/**/*.md` (verified) | title, description, last_reviewed, atlas_section, tags | `Article` | none | implement now | Replace `TechArticle`; accurate |
| Unverified Atlas | most `atlas/**/*.md` | title, description | none | n/a | skip while noindex | Avoid rich results on noindex pages |
| Scenarios | `scenarios/*.md` | title, description | none | n/a | do not use | Intentionally noindex |
| Research | `research/**/*.md` | title, description, date | none | n/a | do not use | Intentionally noindex |
| Skill Hub | `skill-hub/**/*.md` | title, description, status/verified | `Article` | none | implement now | Indexable article-like content |
| Services | `services/*.md` | title, description | `WebPage` | none | implement now | Landing pages, not articles |
| Dataset detail | `datasets/view/**/*.md` | title, description, inline JSON-LD | `Dataset` | already present | keep inline; validate | Real downloadable datasets |
| Dataset catalog | `/datasets/`, `/datasets/<collection>/` | data_catalog_page flag | `CollectionPage` + `DataCatalog` | none | keep metadata | Helps machine discovery; not a rich result |
| AI catalog | `/ai/` | page.url | `CollectionPage` + `DataCatalog` | none | keep metadata | Machine-readable catalog |
| About | `about.md` | profile_page flag, resume data | `ProfilePage` + `Person` + `Organization` | none | keep/improve | Real public profile |
| Event / Course | none | n/a | `Event` / `Course` | requires explicit front matter | guarded support only | No real events/courses yet |
| Homepage | `index.md` | n/a | untouched | n/a | defer Organization | Hard constraint |

## 9. Known limitations

- The `DataCatalog` block embeds the full `_data/datasets.yml` array. It is schema.org metadata and is not claimed as a Google rich result.
- Breadcrumbs are auto-built from URL patterns and known page families. Pages with unusual hierarchies can supply an explicit `breadcrumbs` array in front matter.
- Event and Course support is template-guarded but not activated because no real event/course content exists.
- Organization markup is only on `/about/`; homepage Organization is deferred.

## 10. Validation

After build, run:

```bash
python3 scripts/check_structured_data.py _site
```

This checks valid JSON, no duplicate `@id`, no rich-result markup on noindex pages, real dates, no private paths, and type-specific required fields.

After deployment, manually test key URLs in the [Google Rich Results Test](https://search.google.com/test/rich-results).
