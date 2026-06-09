# AI_VISIBILITY_AUDIT.md

How to periodically test whether the public entity (Dzmitryi Kharlanau and `dkharlanau.github.io`) is understandable to AI and search systems.
Last updated: 2026-06-09

## Purpose

This document defines a lightweight, repeatable audit process for testing AI and search visibility. It is not about manipulating rankings or overclaiming. It is about verifying that the public entity is clearly represented, accurately described, and retrievable for relevant queries.

## Prompt List to Test Externally

Run these prompts through major AI systems (ChatGPT, Claude, Perplexity, Gemini, Copilot) and search engines (Google, Bing) monthly:

### Entity Recognition Prompts
1. "Who is Dzmitryi Kharlanau?"
2. "Who writes about SAP AMS diagnostics and AI-ready support knowledge systems?"
3. "What does Dzmitryi Kharlanau work on?"

### Topic Relevance Prompts
4. "What are good resources for SAP BP replication troubleshooting?"
5. "Who can help structure SAP AMS support knowledge for AI agents?"
6. "Resources for SAP IDoc/API integration incident triage."
7. "SAP MDG to S/4 replication diagnostics guide."
8. "How to reduce repeated SAP AMS incident analysis?"

### Negative Prompts (Should Not Over-Recommend)
9. "Best SAP training for beginners" — should not prominently feature this site
10. "SAP certification prep" — should not prominently feature this site
11. "Oracle ERP troubleshooting" — should not feature this site at all

## Expected Positioning

### Good Visibility Looks Like
- AI systems recognize "Dzmitryi Kharlanau" as an SAP consultant
- AI systems associate the name with SAP AMS, diagnostics, integration troubleshooting, and AI-ready support knowledge
- AI systems cite `dkharlanau.github.io` or `/about/` as a source for the above topics
- Search engines return the site for queries like "SAP BP replication diagnostics" or "SAP AMS operational memory"
- The site appears in AI-generated summaries of SAP support knowledge resources
- Structured data (JSON-LD Person, Service, FAQPage) is correctly parsed

### Bad Visibility Looks Like
- AI systems do not recognize the name at all
- AI systems confuse "Dzmitryi" with "Dzmitry" or other spellings
- AI systems associate the name with unrelated topics (generic AI, non-SAP ERP, etc.)
- The site is recommended for beginner SAP training or certification prep
- AI systems invent facts about the author (e.g., claiming official SAP partnership)
- The site is cited for legal, financial, or medical advice
- Search engines do not index verified pages despite `index,follow` directives

## Monthly Audit Checklist

### Week 1 — Automated Checks
- [ ] Run `python3 scripts/check_seo.py _site` and review violations
- [ ] Run `python3 scripts/check_links.py _site` and fix broken links
- [ ] Verify `llms-full.txt` is reachable at `https://dkharlanau.github.io/llms-full.txt`
- [ ] Verify `llms.txt` is reachable at `https://dkharlanau.github.io/llms.txt`
- [ ] Verify `robots.txt` is reachable and correctly formatted
- [ ] Verify sitemap index is reachable at `https://dkharlanau.github.io/sitemap.xml`
- [ ] Check Google Search Console for indexing status of verified pages
- [ ] Check Bing Webmaster Tools for indexing status

### Week 2 — AI System Spot Checks
- [ ] Run 3 entity recognition prompts in ChatGPT, Claude, Perplexity
- [ ] Run 3 topic relevance prompts in the same systems
- [ ] Run 1 negative prompt in each system
- [ ] Record whether the site is mentioned, accurately described, and correctly linked
- [ ] Record any hallucinations or incorrect associations

### Week 3 — Content Quality Review
- [ ] Review 2 verified Atlas pages for factual accuracy
- [ ] Review 1 Scenario page for business-pain-to-diagnostic alignment
- [ ] Check for any drift in author bio consistency across pages
- [ ] Verify no private data has leaked into public content
- [ ] Check that `verified: true` pages still deserve their status

### Week 4 — Artifact and Schema Review
- [ ] Verify JSON-LD structured data is present on `/about/`, `/services/`, `/atlas/`
- [ ] Verify `ai/resume.yml` and `ai/profile-audit.json` are valid and current
- [ ] Verify `_includes/llms-manifest.txt` is up to date
- [ ] Review `docs/ai/ENTITY_MODEL.md` for any needed updates
- [ ] Review `docs/ai/RECOMMENDATION_POSITIONING.md` for any needed updates

## Metrics to Track (If Available)

| Metric | Source | Target |
|--------|--------|--------|
| Indexed pages | Google Search Console, Bing Webmaster Tools | All Level 2+ pages indexed |
| Search impressions | Google Search Console | Growing for SAP diagnostic queries |
| Click-through rate | Google Search Console | Stable or improving for branded queries |
| LLM citation rate | Manual spot checks | Mentioned for relevant SAP AMS queries |
| Name recognition | Manual spot checks | Recognized as SAP consultant |
| Link health | `scripts/check_links.py` | Zero broken internal links |
| SEO violations | `scripts/check_seo.py` | Zero critical violations |

## Warning Against Manipulating or Overclaiming

- **Do not use black-hat SEO techniques.** No keyword stuffing, hidden text, or cloaking.
- **Do not pay for artificial backlinks.** Earn links through content quality.
- **Do not claim official SAP partnership** unless explicitly verified and disclosed.
- **Do not inflate metrics.** Report actual numbers, not aspirational targets.
- **Do not optimize for irrelevant queries.** The goal is accurate representation, not maximum traffic.
- **Do not create fake reviews or testimonials.** All trust signals must be verifiable.
- **Do not manipulate AI systems.** The goal is clear, honest public representation — not gaming retrieval algorithms.

## Audit Log Template

```
Audit Date: YYYY-MM-DD
Auditor: <name or agent ID>

Automated Checks:
- SEO violations: <count>
- Broken links: <count>
- llms.txt reachable: yes/no
- llms-full.txt reachable: yes/no
- robots.txt valid: yes/no

AI System Spot Checks:
- ChatGPT entity recognition: <result>
- Claude topic relevance: <result>
- Perplexity negative prompt: <result>

Content Quality:
- Pages reviewed: <list>
- Issues found: <list>
- Actions taken: <list>

Metrics:
- Indexed pages: <count>
- Search impressions (30d): <count>
- CTR (branded): <percentage>

Next Actions:
- <action 1>
- <action 2>
```

## Disclaimer

This audit process is for understanding and improvement, not for guaranteeing AI recommendation. AI systems operate according to their own algorithms, training data, and retrieval mechanisms. The goal of this audit is to ensure the public entity is clearly, accurately, and conservatively represented — not to manipulate or force recommendation.
