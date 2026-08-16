# Search Promotion Loop

This workflow turns mature Lab material into search-ready pages without publishing drafts by accident.

## Order of operations

1. `python3 scripts/audit_assessment_promotion_readiness.py`
   - checks structure and primary-source review state;
   - does not change publication status.
2. `python3 scripts/search_discoverability_inventory.py`
   - inventories Markdown and HTML Jekyll sources;
   - classifies routes as INDEX, KEEP_NOINDEX, REVIEW_TO_INDEX, BLOCK_INDEX, or review states.
3. `python3 scripts/lab_search_promotion_loop.py`
   - combines factual readiness, explicit search intent, metadata, body depth, evidence, links, H1 and freshness;
   - ranks `HUMAN_VERIFY_NEXT` pages;
   - never sets `verified: true`.
4. `python3 scripts/audit_lab_search_intents.py`
   - checks intent ownership and possible cannibalization.
5. `python3 scripts/lab_link_gap_loop.py`
   - finds weak inbound/outbound Lab relationships and suggests contextual targets.
6. Human page review
   - confirm the page as a whole, including authored heuristics and scope boundaries;
   - only then set `status: reviewed` and `verified: true`.
7. `python3 scripts/lab_search_promotion_loop.py --apply`
   - changes only reviewed+verified READY_TO_PROMOTE pages to `robots: index,follow` and `sitemap: true`.
8. Build and CI
   - publication gate, sitemap checks, metadata checks, link checks and IndexNow run as normal.

## Publication invariant

A Lab page must never become indexable while it is draft or unverified.

```text
draft + verified:false
        ↓ factual/source review
human review candidate
        ↓ page-level human verification
reviewed + verified:true
        ↓ search promotion
index,follow + sitemap:true
```

Search quality is not factual verification. A long page with excellent metadata can still contain a wrong claim. Likewise, a source-supported page can still be a poor search landing page. The loop keeps those decisions separate.

## Reports

CI uploads these files in the `search-discoverability-inventory` artifact:

- `reports/seo/search-discoverability.csv`
- `reports/seo/search-discoverability.md`
- `reports/seo/lab-promotion-queue.csv`
- `reports/seo/lab-promotion-queue.md`
- `reports/seo/lab-search-intents.json`
- `reports/seo/lab-search-intents.md`
- `reports/seo/lab-link-gaps.csv`
- `reports/seo/lab-link-gaps.md`

## Current priority rule

Prefer source-supported P1 pages with a clear long-tail intent and strong links. Core assessment topics normally come before broad catalog pages: Sales Order, Pricing, ATP/aATP, Shipping, Procurement, EWM, Integration, Inventory Management, Automotive JIT, Production, Quality Management and Transportation Management.
