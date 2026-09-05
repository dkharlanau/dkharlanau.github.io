---
layout: default
title: AI crawler and access matrix
description: Dated human-readable summary of the site's published search, AI retrieval and model-training crawler policy.
permalink: /crawler-matrix/
sitemap: true
---

# AI crawler and access matrix

This page summarizes the crawler choices currently published in `robots.txt`. The robots file remains the canonical enforcement surface; this matrix exists to make the intent easier for people and agents to inspect.

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

Canonical policy sources:

- <https://dkharlanau.github.io/robots.txt>
- <https://dkharlanau.github.io/legal/ai-crawler-policy/>
- <https://dkharlanau.github.io/crawler-matrix/crawlers.json>

Last reviewed: 2026-09-05.
