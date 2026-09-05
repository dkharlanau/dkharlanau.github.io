---
layout: default
title: Trust Center
description: Canonical trust, evidence, citation, crawler, correction and security boundaries for dkharlanau.github.io.
permalink: /trust/
sitemap: true
---

# Trust Center

This page is the canonical trust surface for `dkharlanau.github.io`. It explains what the site publishes, how evidence is reviewed, which machine-readable interfaces are authoritative, and which claims should remain bounded.

## Identity and source of record

- Canonical site: <https://dkharlanau.github.io/>
- Canonical identity: <https://dkharlanau.github.io/ai/identity.json>
- Canonical entity graph: <https://dkharlanau.github.io/ai/entity-graph.jsonld>
- Agent-Ready Web Profile: <https://dkharlanau.github.io/ai/site-profile.json>
- AI Search & Citation Profile: <https://dkharlanau.github.io/ai/ai-search-profile.json>

## Evidence and review model

The site distinguishes authored material, generated structure, reviewed retrieval-ready content, external evidence, and independent validation. Build success or machine-readable completeness does not by itself make a technical or professional claim verified.

For public retrieval, the site's review state remains authoritative. Where a page or dataset carries explicit review, verification, evidence, confidence, or limitation metadata, agents should preserve those boundaries rather than infer stronger claims.

The professional knowledge model uses the route `Domain → Decision → Scenario → Evidence`. For technical claims, prefer a reviewed decision or evidence surface over an isolated summary.

## Citation and provenance

- Citation guidance: <https://dkharlanau.github.io/CITATION/>
- Repository history: <https://github.com/dkharlanau/dkharlanau.github.io/commits/main>
- Knowledge publication contract: <https://raw.githubusercontent.com/dkharlanau/dkharlanau.github.io/main/_data/knowledge_publication_contract.yml>
- Machine-readable Trust Center: <https://dkharlanau.github.io/trust/trust.json>

Repository history provides source provenance. It is not an independent correctness, expertise, or security certificate.

## Crawler and AI access policy

The canonical enforcement surface is `robots.txt`; the human explanation and dated matrix make that policy easier to inspect.

- Robots policy: <https://dkharlanau.github.io/robots.txt>
- Human AI crawler policy: <https://dkharlanau.github.io/legal/ai-crawler-policy/>
- Machine-readable crawler matrix: <https://dkharlanau.github.io/crawler-matrix/crawlers.json>

The current policy intentionally separates search and user-directed AI retrieval from model-training crawlers. Agents should read the actual published policy rather than infer permission from the existence of AI-readable files.

## Corrections

Material factual corrections should be recorded rather than silently rewriting important history. The current ledger and policy are published at:

- <https://dkharlanau.github.io/trust/corrections/>
- <https://dkharlanau.github.io/trust/corrections.json>

Minor spelling, layout, broken-link, or generated-inventory refreshes do not require a material correction entry unless they change the meaning of a published claim.

## Security

Security reporting guidance is published in <https://github.com/dkharlanau/dkharlanau.github.io/blob/main/SECURITY.md>. A passing CI run, static deployment, schema validation, crawler configuration, or trust metadata must not be represented as a security certification.

## Reuse and limitations

Licensing and reuse rules are defined by the repository license and the specific policy attached to a dataset or surface. The presence of public machine-readable content does not override an explicit license, attribution requirement, crawler rule, or professional disclosure.

This site is a professional knowledge and portfolio system. It does not represent employer systems, production SAP environments, client data, or independent validation of every authored conclusion.
