---
title: Source Quality Rules
robots: noindex
sitemap: false
---

# Source Quality Rules

## Acceptance Criteria

A source is accepted into the registry only if it meets at least one of these criteria:

1. **Official documentation** from a recognized framework body, standards organization, or vendor
2. **Public architecture guidance** from a major cloud provider or technology organization
3. **Well-maintained open-source documentation** with clear authorship and versioning
4. **Public postmortem or ADR** from a reputable organization with operational depth
5. **Recognized professional community material** with clear authorship and technical substance
6. **Academic or government digital service playbook** with practical applicability

## Rejection Criteria

Reject sources that exhibit any of the following:

- SEO spam or content farms
- Thin LinkedIn posts without technical depth
- Unsourced AI-generated articles
- Vendor marketing pages with no operational depth
- Generic "top 10 best practices" posts without specifics
- Copied framework summaries without original analysis
- Paywalled standards text that cannot be quoted or verified
- Sources with no identifiable author or publisher
- Sources older than 10 years without historical relevance justification

## Tier Assignment Rules

### Tier 1 — Primary / Authoritative

Must be:
- Official documentation from the owning organization
- Standards published by recognized standards bodies (ISO, NIST, etc.)
- Official vendor architecture guidance (SAP Help, AWS Well-Architected, etc.)
- Official SRE / reliability engineering books or docs
- Official security / architecture / governance references

### Tier 2 — Strong Practitioner

Must be:
- Respected engineering blogs from major technology organizations (Google, Microsoft, AWS, etc.)
- Public postmortem collections with clear lessons
- Public architecture decision record examples from real projects
- Public templates from reputable organizations
- Well-maintained open-source documentation with active community
- Recognized professional communities with clear authorship

### Tier 3 — Supporting

May be:
- Useful practitioner articles with concrete examples
- Conference talks with actionable takeaways
- Public case studies with measurable outcomes
- Educational material from reputable institutions

## Source Diversity Requirement

For each domain:
- Minimum 3 independent publishers or organizations
- No more than 40% of sources from a single vendor or framework
- At least one Tier 1 source per domain
- At least one open-source or community source per domain

## Citation Rules

- Do not copy long passages (max 2-3 sentences with attribution)
- Do not reproduce paid framework text
- Prefer paraphrase and link
- Always keep URLs accessible
- If paywalled, record only metadata and note the restriction
- Do not claim official endorsement
- Do not invent citations
- Do not cite a source unless it actually supports the point

## Copyright Notes

- Record copyright status in `source-registry.yml`
- Note license type when available (CC, MIT, Apache, etc.)
- For official docs, note terms of use if known
- When in doubt, record metadata only and do not copy content
