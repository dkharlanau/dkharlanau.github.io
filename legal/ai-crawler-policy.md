---
layout: default
title: "AI Crawler Policy"
description: "How this site handles AI crawlers, search/retrieval bots, and training bots. We welcome search and user-facing retrieval, but block model-training crawlers."
permalink: /legal/ai-crawler-policy/
last_modified_at: 2026-06-13
---

# AI Crawler Policy

This page documents the crawler policy for `dkharlanau.github.io`. It explains which automated agents are allowed to access the site and why.

## Allowed: search and retrieval bots

The following crawlers are allowed because they use site content for search indexing, citation, or user-directed retrieval:

- **OAI-SearchBot** — powers ChatGPT Search results.
- **ChatGPT-User** — user-facing ChatGPT browsing.
- **Claude-SearchBot** — powers Claude search results.
- **Claude-User** — user-facing Claude browsing.
- **PerplexityBot** — Perplexity search/answer retrieval.
- **CCBot** — Common Crawl retrieval.
- **FacebookBot** — Meta search/retrieval.

These agents may index, cite, or retrieve publicly visible content in accordance with their own terms of service.

## Blocked: training crawlers

The following crawlers are blocked because they collect content for model training without a clear per-page opt-in:

- **GPTBot** — OpenAI training crawler.
- **ClaudeBot** — Anthropic training crawler.
- **Google-Extended** — Google training crawler for AI models.

Search/retrieval bots operated by the same organisations are allowed separately.

## Content-Signal

`robots.txt` includes an informational `Content-Signal` line:

```text
Content-Signal: ai-train=no, search=yes, ai-input=yes
```

This signal means:

- `ai-train=no` — do not use content for model training without permission.
- `search=yes` — search indexing is welcome.
- `ai-input=yes` — AI retrieval and user-directed answering are allowed.

`Content-Signal` is voluntary and not yet widely enforced. The canonical enforcement mechanism remains `robots.txt` rules and page-level `robots` meta tags.

## Sitemap and AI-readable endpoints

Indexable content is listed in:

- `sitemap.xml`
- `sitemap-pages.xml`
- `sitemap-atlas.xml`
- `sitemap-data.xml`

AI-readable endpoints include:

- `/llms.txt`
- `/llms-full.txt`
- `/ai/resume.json`
- `/ai/catalog.json`
- `/ai/discovery-map.json`

`llms-full.txt` contains only reviewed and verified Atlas pages. Unverified or `noindex` content is excluded.

## Unverified and research content

Atlas pages and scenarios marked as `needs_verification` are set to `robots: noindex` and are not included in sitemaps or `llms-full.txt`. Research notes live under `docs/research/` and are similarly excluded from indexing.

## Scope and limitations

This policy applies to automated crawlers and agents. Human visitors, RSS readers, and browser-based tools are not affected. The policy may be updated as crawler standards evolve.
