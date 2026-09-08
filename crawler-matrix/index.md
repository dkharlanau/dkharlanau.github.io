---
layout: default
title: AI crawler and access matrix
description: Dated human-readable summary of the site's published search, AI retrieval and model-training crawler policy.
permalink: /crawler-matrix/
sitemap: true
last_modified_at: 2026-09-08
tags: [ai-crawlers, access-policy, search]
---

# AI crawler and access matrix

This page summarizes the crawler choices published in [robots.txt](/robots.txt). Its scope is the site configuration: an allowed crawler is not evidence that a provider has fetched, indexed or cited a page.

If a page is missing from an answer, first separate an access problem from an indexing or retrieval problem. Compare the relevant user-agent rule with the exact page response, then check the search or citation evidence separately. The table records the role intended by this site; it does not attest to an external provider's processing behavior.

| Crawler | Intended role | Site policy |
|---|---|---|
| OAI-SearchBot | OpenAI search indexing | Allow |
| ChatGPT-User | User-directed ChatGPT retrieval | Allow |
| GPTBot | OpenAI model-training crawler | Block |
| Claude-SearchBot | Anthropic search indexing | Allow |
| Claude-User | User-directed Claude retrieval | Allow |
| ClaudeBot | Anthropic model-training crawler | Block |
| Google-Extended | Google AI training/grounding control token | Block |
| PerplexityBot | Perplexity search/retrieval | Allow |
| CCBot | Common Crawl | Allow |
| FacebookBot | Meta search/retrieval | Allow |

The site also publishes `Content-Signal: ai-train=no, search=yes, ai-input=yes` as an informational preference. This header-like robots directive is not represented here as universally enforceable behavior.

For the evidence and reuse boundaries behind this policy, see the [Trust Center](/trust/).

Canonical policy sources:

- <https://dkharlanau.github.io/robots.txt>
- <https://dkharlanau.github.io/legal/ai-crawler-policy/>
- <https://dkharlanau.github.io/crawler-matrix/crawlers.json>

Last reviewed: 2026-09-05.
