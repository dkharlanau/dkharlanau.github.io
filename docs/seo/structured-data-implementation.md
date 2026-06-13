---
layout: default
title: "Structured Data Implementation Guide"
description: "Implementation guide and front-matter conventions for Google-aligned JSON-LD on dkharlanau.github.io."
robots: noindex,follow
sitemap: false
---

# Structured Data Implementation Guide

This document describes the Google-aligned structured data implementation for the site.

## 1. Architecture

- **Single dispatcher:** `_includes/seo/structured-data.html` is included at the bottom of `_layouts/default.html`. It decides which JSON-LD blocks to emit based on page metadata.
- **No hand-written JSON-LD in content pages** except for dataset detail pages, which are generated with inline `Dataset` markup. The dispatcher does not emit `Dataset` for those pages, so there is no conflict.
- **Indexability guard:** If a page has `robots: noindex`, the dispatcher emits **no** JSON-LD at all.
- **Homepage untouched:** The existing `WebSite` + `SearchAction` and `FAQPage` blocks in `_includes/head.html` are not changed.

## 2. Implemented schema types

### Google-supported rich result types

- `Article` — notes, blog posts, news, radar signals, verified Atlas pages, Skill Hub pages.
- `BreadcrumbList` — indexable pages with a clear hierarchy.
- `Dataset` — supported via inline markup on dataset detail pages; dispatcher has guarded support for future pages.
- `ProfilePage` + `Person` — `/about/`.
- `Organization` — `/about/` (employer only).

### schema.org metadata only (no Google rich result promise)

- `WebPage` — generic indexable pages (e.g., services, dataset detail pages, AI pages).
- `CollectionPage` — aggregator/list pages.
- `DataCatalog` — dataset/AI catalog pages. Documented as metadata only.

### Guarded but not currently activated

- `Event` — only emits when explicit `structured_data` event fields exist.
- `Course` + `ItemList` — only emits when `structured_data.courses` has 3+ real courses.

### Not implemented

- `TechArticle`, `Product`, `Review`, `AggregateRating`, `LocalBusiness`, `Recipe`, `JobPosting`, etc.

## 3. `@id` conventions

| Entity | `@id` pattern |
|---|---|
| Page (WebPage/ProfilePage/CollectionPage) | `{{ canonical_url }}#webpage` |
| Article | `{{ canonical_url }}#article` |
| BreadcrumbList | `{{ canonical_url }}#breadcrumb` |
| Event | `{{ canonical_url }}#event` |
| Course list | `{{ canonical_url }}#courses` |
| Dataset (include) | `{{ canonical_url }}#dataset` |
| Person / author | `{{ site.url }}#dkharlanau` |
| Organization | `{{ employer.url }}#organization` |
| DataCatalog | `https://dkharlanau.github.io/ai/catalog.json#catalog` |

## 4. Front-matter conventions

### Standard article-like page

```yaml
---
title: "Page title"
description: "Page description"
date: 2026-06-13
last_modified_at: 2026-06-13
og_image: "/assets/og/specific.png"   # optional; only used in structured data if set
tags: [sap, ams]
---
```

### Override the detected type

```yaml
---
structured_data:
  type: article   # article | webpage | event | course | dataset
---
```

Allowed override values are normalized by the dispatcher:

| Front-matter value | Emitted `@type` |
|---|---|
| `article` | `Article` |
| `webpage` | `WebPage` |
| `event` | `Event` |
| `course` | `Course` |
| `dataset` | `Dataset` |

### Provide a custom breadcrumb

If the auto-built breadcrumb is wrong, provide an explicit `breadcrumbs` array:

```yaml
---
breadcrumbs:
  - name: "Skill Hub"
    item: "https://dkharlanau.github.io/skill-hub/"
  - name: "DAMA / Data"
    item: "https://dkharlanau.github.io/skill-hub/dama-dmbok/"
---
```

The dispatcher does not yet consume `breadcrumbs` directly in this version; the array is reserved for future generic breadcrumb generation. Currently, breadcrumbs are emitted via URL-family conditionals.

### Event (example, not activated)

```yaml
---
title: "Workshop title"
description: "Workshop description"
structured_data:
  type: event
  name: "Real Event Name"
  start_date: 2026-09-15T09:00:00+03:00
  end_date: 2026-09-15T17:00:00+03:00
  event_status: "https://schema.org/EventScheduled"
  location:
    "@type": "Place"
    name: "Venue Name"
    address:
      "@type": "PostalAddress"
      addressLocality: "City"
      addressCountry: "Country"
---
```

### Course list (example, not activated)

```yaml
---
title: "Course list"
structured_data:
  type: course
  courses:
    - name: "Course One"
      description: "Short description"
      provider:
        "@type": "Organization"
        name: "Provider Name"
        sameAs: "https://example.com"
      url: "https://example.com/course-one"
    - name: "Course Two"
      description: "Short description"
      provider:
        "@type": "Organization"
        name: "Provider Name"
      url: "https://example.com/course-two"
    - name: "Course Three"
      description: "Short description"
      provider:
        "@type": "Organization"
        name: "Provider Name"
      url: "https://example.com/course-three"
---
```

## 5. Image handling

- `og_image` is used for Open Graph / Twitter meta tags in `_includes/head.html` with a site default.
- Structured data only emits `image` when `page.og_image` is explicitly set, because a generic default image is not representative of an individual article.

## 6. Date handling

- `datePublished`: from `page.date` or `page.published`. Omitted if absent.
- `dateModified`: from `page.last_modified_at` or `page.updated`, with `page.last_reviewed` as a fallback. Omitted if absent.
- Dates are emitted only when Jekyll can parse them.

## 7. Author / publisher

All article-like pages use:

```json
{
  "@type": "Person",
  "@id": "https://dkharlanau.github.io/#dkharlanau",
  "name": "Dzmitryi Kharlanau",
  "url": "https://dkharlanau.github.io/about/"
}
```

Both `author` and `publisher` point to the same canonical person.

## 8. Validation commands

After any change, run the full sequence:

```bash
bundle exec jekyll build
python3 scripts/check_public_repo.py
python3 scripts/check_indexing_policy.py --repo-dir . --site-dir _site --fail-on-critical
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_structured_data.py _site
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
```

## 9. Manual Google Rich Results Test checklist

After deployment, test these live URLs:

| URL | Expected types |
|---|---|
| `https://dkharlanau.github.io/about/` | `ProfilePage`, `Person`, `Organization`, `BreadcrumbList` |
| `https://dkharlanau.github.io/notes/<slug>/` | `Article`, `BreadcrumbList` |
| `https://dkharlanau.github.io/blog/<slug>/` | `Article`, `BreadcrumbList` |
| `https://dkharlanau.github.io/atlas/<section>/<slug>/` (verified) | `Article`, `BreadcrumbList` |
| `https://dkharlanau.github.io/skill-hub/<section>/<slug>/` | `Article`, `BreadcrumbList` |
| `https://dkharlanau.github.io/datasets/view/<collection>/<id>/` | `Dataset` (inline) |
| `https://dkharlanau.github.io/datasets/` | `CollectionPage`, `DataCatalog`, `BreadcrumbList` |

Confirm no rich-result types appear on:

- `https://dkharlanau.github.io/research/...`
- `https://dkharlanau.github.io/scenarios/...`
- any unverified Atlas page (these are `noindex`).

## 10. Deferred recommendations

- **Organization on homepage:** Google recommends placing `Organization` markup on the homepage or a single organization page. Add it to `index.md` or `_includes/head.html` in a future pass.
- **Generic breadcrumb builder:** Replace URL-family conditionals with a generic builder that consumes `page.breadcrumbs`.
- **Dataset detail inline → include:** Move dataset detail JSON-LD from generated markdown into the dispatcher once the generator supports front-matter-driven dataset metadata.
- **Rich Results Test API:** Automate post-deployment validation via the Google Search Console API when feasible.
