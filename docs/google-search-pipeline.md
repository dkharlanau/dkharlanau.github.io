# Google Search Pipeline

The repository can submit the public sitemap to Google Search Console and audit the indexing state of sitemap pages without using the restricted Google Indexing API.

## What the workflow does

The `Google Search Pipeline` workflow runs after a successful Pages deployment on `main`, once per day, on relevant pipeline changes, and on manual request.

It:

1. Reads `https://dkharlanau.github.io/sitemap.xml` and all child sitemaps.
2. Submits the sitemap index through the Search Console Sitemaps API.
3. Sends page URLs to the Search Console URL Inspection API.
4. Skips machine endpoints and static assets by default; URL Inspection focuses on HTML pages.
5. Classifies page results into `P0`, `P1`, `P2`, `REVIEW`, or `OK`.
6. Downloads the previous successful workflow artifact when available and calculates changes in indexing counts.
7. Publishes `google-indexing.json` and `google-indexing.md` as a 90-day GitHub Actions artifact and as a workflow summary.

The workflow does not pretend that URL Inspection is an indexing request. Google does not provide a general-purpose API for the Search Console **Request indexing** button.

## One-time Google setup

1. Create or select a Google Cloud project.
2. Enable the Google Search Console API for that project.
3. Create a service account and a JSON key.
4. In Google Search Console, open the property `https://dkharlanau.github.io/` and add the service account email as an owner or a user with enough permission to manage sitemaps and inspect URLs.
5. In the GitHub repository, create the Actions secret `GOOGLE_SEARCH_CONSOLE_SERVICE_ACCOUNT` and paste the complete service account JSON as its value.
6. Run **Actions → Google Search Pipeline → Run workflow** once.

Do not commit the JSON key to the repository.

Production runs fail closed when the secret is absent or invalid. A green workflow therefore means the Search Console connection was actually used; credential-free sitemap parsing is available only as an explicit local dry run.

The scheduled run inspects the 12 URLs in `config/google-search-monitor-urls.json` first, then uses the remainder of its bounded budget for a rotating sample. Deployment and pipeline-change runs use the same monitored URLs when their cooldown permits inspection, then prioritize new and previously problematic URLs. All monitored URLs must be page URLs in the property's sitemap; a missing or duplicate entry fails the run for review. A manual budget below 12 inspects only the first URLs that fit. Use the manual `all` mode for an occasional full baseline, not as a daily crawl. The URL Inspection API has a per-property daily quota, and sitemap submission is a discovery hint rather than a guarantee that Google will index every URL.

## Reports

The workflow creates:

- `reports/seo/google-search/google-indexing.json` — complete machine-readable result.
- `reports/seo/google-search/google-indexing.md` — monitored articles with their latest inspection times and a sitewide review queue. The same table appears in the GitHub Actions run summary.

Each successful URL Inspection records `inspected_at` in UTC. The rolling inventory preserves that timestamp when it carries a result forward; `stale: true` means the URL was not inspected in the current run. A failed attempt records `inspection_attempted_at` and leaves `inspected_at` null. Older results that have no per-URL timestamp remain unknown rather than inheriting the report generation time or Google's last crawl time. These timestamps date the API observation, not the crawl or an indexing request.

Priority meaning:

- `P0` — Google does not know the page, cannot fetch it, or indexing is blocked.
- `P1` — Google crawled the page but did not index it.
- `P2` — Google discovered the page but has not crawled it yet.
- `REVIEW` — the API returned a state that needs manual review.
- `OK` — Google reports the page as indexed.

For `P0` and selected `P1` pages, the report can be used as the short manual queue for Search Console **Request indexing**. This keeps the manual work focused on the pages that need it most.

## Local dry run without Google credentials

The script can still validate and expand the live sitemap without API credentials:

```bash
python scripts/google_search_pipeline.py \
  --site-url https://dkharlanau.github.io/ \
  --sitemap-url https://dkharlanau.github.io/sitemap.xml
```

In this mode the report shows that API setup is required and no Google API request is sent.
