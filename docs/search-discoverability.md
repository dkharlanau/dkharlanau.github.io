# Search Discoverability Model

This document defines how public site content moves from working material to search-ready knowledge.

## Core rule

Do not make a page indexable just because it exists.

A governed knowledge page moves through this publication path:

`draft / needs_verification -> reviewed -> verified -> indexable`

For governed surfaces such as Labs, Atlas, Skill Hub, Scenarios, and Research, the safe working state is:

```yaml
status: draft
verified: false
robots: noindex,follow
sitemap: false
```

The normal published state is:

```yaml
status: reviewed
verified: true
robots: index,follow
sitemap: true
```

The exact metadata may be inherited from `_config.yml`, but the effective result must match the publication state.

## Route classifications

The source inventory in `scripts/search_discoverability_inventory.py` assigns one operational classification to each Markdown route.

- `INDEX` — allowed to be discovered and indexed.
- `KEEP_NOINDEX` — intentionally excluded working, low-value, private, or search-noise surface.
- `REVIEW_TO_INDEX` — reviewed and verified content that is still hidden. Promote consciously or downgrade the review state.
- `BLOCK_INDEX` — immature governed content escaped the publication gate. This is a policy error.
- `REVIEW_METADATA` — indexable content is missing essential search metadata.
- `REVIEW_DUPLICATE_TITLE` — multiple indexable routes use the same title and may compete for the same intent.
- `MERGE_OR_FIX_ROUTE` — multiple source pages resolve to the same route.

A page can optionally declare an explicit planning action:

```yaml
search_action: merge
```

Supported values are `index`, `keep_noindex`, `merge`, and `remove`. This field is for editorial planning; it does not replace `robots` or `sitemap` controls.

## Search intent

Every important published knowledge page should answer one clear question or task. Add a stable intent when the title alone is not precise enough:

```yaml
search_intent: "SAP route determination in S/4HANA Sales"
```

Prefer specific consultant questions over broad product keywords. A strong page should normally connect:

`question -> short answer -> process context -> mechanism -> configuration/data -> failure modes -> integration -> example -> related pages -> sources`

## Internal links

Knowledge-graph relationships should also become ordinary crawlable HTML links where they help a reader.

Use links to connect:

- process -> decision mechanism
- process -> master data
- process -> integration
- symptom -> diagnostic page
- concept -> working skill
- Lab deep dive -> reviewed Atlas reference

Do not create links only to manipulate ranking. The graph should reflect a real reading or diagnostic path.

## Structured data

The shared structured-data dispatcher is `_includes/seo/structured-data.html`.

Do not add page-specific JSON-LD when the shared dispatcher already covers the page type. Prefer front matter and shared rules so entity IDs stay stable.

Important stable entities:

- Person: `https://dkharlanau.github.io/#dkharlanau`
- WebSite: `https://dkharlanau.github.io/#website`
- Page/article entity: canonical URL plus `#webpage` or `#article`

## CI controls

The main CI workflow runs:

- SEO metadata validation
- indexing policy validation
- source-level search discoverability inventory
- Lab publication gate
- sitemap policy validation
- built-site indexability audit
- internal-link audit
- AI endpoint validation

The generated inventory is uploaded as a CI artifact:

- `reports/seo/search-discoverability.csv`
- `reports/seo/search-discoverability.md`

Use the CSV for filtering and the Markdown report for the publication review queue.

## Promotion checklist

Before changing a governed page to indexable:

1. Confirm the page has one clear search intent.
2. Confirm factual review is complete.
3. Set `status: reviewed` and `verified: true`.
4. Confirm title, description, H1, canonical, and meaningful internal links.
5. Confirm important claims have source support where needed.
6. Remove draft markers and private references.
7. Change the effective robots policy to indexable and include the route in the sitemap.
8. Run CI and check the search discoverability artifact.

The goal is not maximum URL count. The goal is a smaller set of strong, connected pages that are useful enough to retrieve, cite, and recommend.
