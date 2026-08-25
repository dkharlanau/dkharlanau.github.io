# Google Search Pipeline

The repository can submit the public sitemap to Google Search Console and audit the indexing state of sitemap pages without using the restricted Google Indexing API.

## What the workflow does

The `Google Search Pipeline` workflow runs after a successful `CI` run on `main`, once per day, and on manual request.

It:

1. Reads `https://dkharlanau.github.io/sitemap.xml` and all child sitemaps.
2. Submits the sitemap index through the Search Console Sitemaps API.
3. Sends page URLs to the Search Console URL Inspection API.
4. Skips JSON, YAML, XML, TXT, and CSV endpoints by default.
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

## Reports

The workflow creates:

- `reports/seo/google-search/google-indexing.json` — complete machine-readable result.
- `reports/seo/google-search/google-indexing.md` — compact human review queue.

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
