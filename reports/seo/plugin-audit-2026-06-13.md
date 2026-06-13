# Plugin & Metadata Audit Report

**Date:** 2026-06-13
**Branch:** `feat/seo-visibility-swarm`
**Site:** https://dkharlanau.github.io

## Summary

The site already has a **strong, custom metadata implementation** that surpasses what `jekyll-seo-tag` provides out of the box. No new plugins are needed. The highest-value action is to **keep the custom implementation** and **document why**.

---

## Current Plugin State

| Plugin | Status | Source | Notes |
|--------|--------|--------|-------|
| `jekyll-seo-tag` | Listed in `_config.yml` | `_config.yml` line 29 | **Not actively used** in layouts (no `{% seo %}` tag found) |
| `jekyll-sitemap` | Listed in `_config.yml` | `_config.yml` line 30 | **Present** — generates default `sitemap.xml` |
| `jekyll-feed` | Listed in `_config.yml` | `_config.yml` line 31 | **Present** — generates `feed.xml` for Atom feed |

**Gemfile:** Uses `github-pages` gem (line 2), which bundles the above plugins natively.

**Build mode:** Native GitHub Pages build (no custom GitHub Actions build workflow for Jekyll itself; the CI workflow only validates).

---

## Metadata Implementation Audit

### Custom `head.html` vs. `jekyll-seo-tag`

The site uses `_includes/head.html` (128 lines) with handcrafted tags rather than the `{% seo %}` tag from `jekyll-seo-tag`.

**What `head.html` covers:**

| Tag | Present | Quality |
|-----|---------|---------|
| `<title>` | ✅ | Dynamic per page type (home, CV, notes, default) |
| `<meta name="description">` | ✅ | Truncated to 160 chars; dynamic fallback chain |
| `<meta name="robots">` | ✅ | Supports `page.robots` frontmatter; rich defaults |
| `<link rel="canonical">` | ✅ | Absolute URL |
| `<link rel="alternate" hreflang="en">` | ✅ | English + x-default |
| `og:title` | ✅ | Dynamic per page |
| `og:description` | ✅ | Truncated to 200 chars |
| `og:url` | ✅ | Matches canonical |
| `og:image` | ✅ | Falls back to `/assets/og/default.png` |
| `og:type` | ✅ | `article` for notes/blog, `website` otherwise |
| `og:locale` | ✅ | `en_US` |
| `og:site_name` | ✅ | "Dzmitryi Kharlanau" |
| `twitter:card` | ✅ | `summary_large_image` |
| `twitter:site` | ✅ | `@dkharlanau` |
| `twitter:title` | ✅ | Matches OG title |
| `twitter:description` | ✅ | Matches OG description |
| `twitter:image` | ✅ | Matches OG image |
| `article:modified_time` | ✅ | Conditional, based on `last_modified_at` / `updated` |
| Atom feed link | ✅ | `application/atom+xml` |
| Sitemap links | ✅ | `sitemap.xml`, `sitemap-data.xml` |
| AI discovery links | ✅ | `llms.txt`, `ai/catalog.json`, `ai/discovery-map.json`, etc. |
| Favicon set | ✅ | SVG + PNG multi-size + apple-touch-icon + webmanifest |
| Preconnect + fonts | ✅ | Google Fonts with `preconnect` |
| Preload hero image | ✅ | `DzmitryiKharlanau.webp` |

**Verdict:** The custom `head.html` is **more comprehensive** than `jekyll-seo-tag` for this site's needs. Switching to `jekyll-seo-tag` would **lose** the AI discovery links, the custom title logic, and the granular robots control.

### Recommendation: Keep `jekyll-seo-tag` in `_config.yml` but do not use `{% seo %}`

**Rationale:**
- `jekyll-seo-tag` is bundled by `github-pages` gem anyway; removing it from `_config.yml` has no effect.
- The custom `head.html` is the source of truth.
- If GitHub Pages ever changes its behavior, having `jekyll-seo-tag` listed ensures backward compatibility.

---

## Structured Data Audit (`_includes/seo/structured-data.html`)

The structured data include is **exceptionally comprehensive** (425 lines). It covers:

| Schema Type | Pages | Quality |
|-------------|-------|---------|
| `WebSite` | All pages | ✅ With `SearchAction` potentialAction |
| `WebPage` / `CollectionPage` | Most pages | ✅ With `isPartOf`, `author`, `primaryImageOfPage` |
| `ProfilePage` | About page | ✅ With `mainEntity`, `hasPart` |
| `Person` | About page | ✅ Rich: `sameAs`, `knowsAbout`, `worksFor`, `alumniOf`, `hasCredential` |
| `Organization` | About page | ✅ EPAM reference |
| `DataCatalog` | AI catalog, dataset catalog | ✅ With `dataset` array |
| `Article` | Notes, blog | ✅ With `datePublished`, `dateModified`, `publisher`, `keywords` |
| `TechArticle` | Atlas pages | ✅ With `about` (domain/concept_type), `keywords` |
| `BreadcrumbList` | Atlas, notes, blog, datasets, services, about, AI, blog index, notes index | ✅ Multi-level for Atlas (4 levels) |
| `FAQPage` | Home page | ✅ Dynamic from `site.data.home.faq` |

**Verdict:** Best-in-class structured data for a personal Jekyll site. No changes needed.

**Minor observation:** There is a duplicated block for `blog` / `collection == 'blog'` (lines 204–245 and 246–287). This is harmless but could be cleaned up in a future maintenance pass.

---

## Sitemap Architecture

| File | Type | Quality |
|------|------|---------|
| `sitemap.xml` | Sitemap index | ✅ References section sitemaps |
| `sitemap-pages.xml` | URLset | ✅ Rigorous: excludes noindex, research, unverified Atlas |
| `sitemap-data.xml` | URLset | ✅ Dataset references |
| `sitemap-atlas.xml` | URLset | ✅ Verified Atlas only |

**Verdict:** Excellent. The sitemap templates correctly enforce the verification policy.

---

## Recommended Additions

| Plugin | Justification | Risk |
|--------|--------------|------|
| None | Current setup is sufficient | — |

**Rejected plugins:**

| Plugin | Reason |
|--------|--------|
| `jekyll-redirect-from` | Not needed; no evidence of broken external links from renamed URLs |
| `jekyll-paginate` | Not needed; site has few enough blog/radar items |
| `jekyll-archives` | Not needed; tag pages not implemented |
| `jekyll-minifier` | GitHub Pages already compresses HTML/CSS; `sass: style: compressed` is set |
| `jekyll-compress-images` | Not a GitHub Pages supported plugin; would require custom build |

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| GitHub Pages stops supporting `github-pages` gem | Low | High | Site uses standard Jekyll; can switch to custom Actions build |
| `jekyll-seo-tag` conflicts with custom `head.html` if `{% seo %}` is accidentally added | Low | Medium | No `{% seo %}` tag in any layout; documented in this report |
| Duplicate metadata if `jekyll-seo-tag` is enabled and `head.html` also outputs tags | Low | Low | `head.html` does not include `{% seo %}`; safe |

---

## Concrete Metadata Fixes Needed

1. **None critical.** The metadata system is mature and comprehensive.
2. **Minor:** Clean up duplicated `blog` Article/BreadcrumbList block in `structured-data.html` (lines 204–287).
3. **Minor:** Consider adding `article:published_time` for Atlas pages (currently only `last_reviewed` is used as `datePublished` fallback).

---

## Score

| Surface | Score |
|---------|-------|
| Plugin selection | 10/10 |
| Title implementation | 10/10 |
| Description implementation | 9/10 |
| Canonical / OG / Twitter | 10/10 |
| Structured data coverage | 10/10 |
| BreadcrumbList | 10/10 |
| Sitemap integration | 10/10 |
| AI discovery links | 10/10 |
| **Overall metadata** | **10/10** |
