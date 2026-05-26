---
# Homepage Datasets Section Review

## Findings

### Current State
- `_includes/sections/datasets.html` exists and is functional
- `page-builder.html` supports `datasets` section type
- Homepage `index.md` does NOT include `datasets` in its `sections` list
- `_data/home.yml` does NOT have a `datasets` key
- Datasets have their own page at `/datasets/` with footer navigation

### Infrastructure Present
| Component | Status |
|---|---|
| `/datasets/` standalone page | Active |
| Footer link to `/datasets/` | Present |
| SEO structured data for datasets | Present |
| `datasets.html` include | Orphaned (not used on homepage) |
| `_data/home.yml` datasets key | Missing |

### Decision
**Intentionally excluded.** The homepage is optimized for AMS service positioning. Datasets are a separate knowledge product with their own page and navigation.

### Rationale
1. Homepage already has 7 sections (hero, analysis-problem, ai-costs-outcomes, strategic-context, credibility, faq, contact)
2. Adding datasets would make the homepage longer without clear service-value connection
3. Datasets are discoverable via `/datasets/` and footer link
4. No traffic data suggests homepage datasets placement is needed

### Action
No code change. Document decision in `docs/homepage-design-decisions.md`.

## Related
- #6 — Site structure inventory (documents orphaned components)
- #2 — Topic index (datasets have their own taxonomy)
