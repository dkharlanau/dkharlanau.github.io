---
layout: default
title: "Citation Frontmatter Pattern"
description: "How to add public source citations to verified pages using the sources frontmatter field."
robots: noindex,follow
sitemap: false
---

# Citation Frontmatter Pattern

## Purpose

Verified Atlas and knowledge pages can declare public sources in frontmatter. The shared structured-data include emits Schema.org `citation` JSON-LD for pages that declare sources, supporting E-E-A-T and AI attribution without requiring template edits for every new citation.

## Schema

Add a `sources:` list to frontmatter. Each source is an object with:

| Field | Required | Description |
|---|---|---|
| `url` | yes | Public, verifiable URL of the source. |
| `title` | no | Short human-readable title. Defaults to the URL if omitted. |
| `date` | no | Publication or retrieval date in `YYYY-MM-DD` format. |

Example:

```yaml
---
title: "Example Verified Page"
description: "..."
verified: true
status: reviewed
sources:
  - url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/example
    title: "SAP S/4HANA Cloud documentation"
    date: 2026-06-01
  - url: https://blogs.sap.com/2026/01/01/example/
    title: "SAP Community blog post"
---
```

## Output

When `sources:` is present, the Article/TechArticle JSON-LD block gains a `citation` array:

```json
{
  "@type": "WebPage",
  "name": "SAP S/4HANA Cloud documentation",
  "url": "https://help.sap.com/docs/SAP_S4HANA_CLOUD/example",
  "datePublished": "2026-06-01T00:00:00+00:00"
}
```

## Safety rules

- Only cite public, verifiable sources.
- Do not cite client documents, internal wikis, or private correspondence.
- Do not invent URLs or publication dates.
- When in doubt, leave `sources:` empty and add citations during explicit human review.

## Validation

- `bundle exec jekyll build` must succeed.
- `python3 scripts/check_structured_data.py _site` must report no JSON-LD errors.
- `python3 scripts/check_public_repo.py` must not flag private URLs in built output.

## Files involved

- `_includes/seo/structured-data.html` — emits `citation` JSON-LD.
- Verified Atlas `.md` files — add `sources:` frontmatter during review.
