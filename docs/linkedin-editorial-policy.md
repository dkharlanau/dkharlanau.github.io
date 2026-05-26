# LinkedIn Editorial Policy and Author Voice

## Purpose

This document governs how Professional Radar produces LinkedIn draft candidates from site/radar signals. It ensures output remains human-reviewed, low-frequency, source-backed, and clearly useful.

## Core Principles

- **Draft-only.** No automatic publishing.
- **No scheduled posting.** No automation of any LinkedIn interaction.
- **Manual approval required.** Every draft must be reviewed before publish.
- **Quality over quantity.** Max 2-3 strong candidates per week.
- **Source-backed.** Every claim must have a source URL.
- **No confidential data.** Never use employer/client-specific information.

## Prohibited Actions

The following are explicitly forbidden:

- Automatic publishing to LinkedIn
- Scheduled LinkedIn posting
- Automatic commenting, liking, or reposting
- Automatic connection requests or direct messages
- Generic promotional calls to action
- Fabricated personal experience or client stories
- Invented emotions, achievements, numbers, or results

## Quality Gate

Each LinkedIn draft candidate must pass these checks:

### 1. Human Value
- Specific insight, practical lesson, or decision implication
- Not just a summary of a news item
- Clear relevance to SAP AMS, SD/MM, clean core, data, integration, or AI-enabled delivery

### 2. Originality
- Not copied from source text
- Includes professional interpretation
- Not near-duplicate of recent drafts or published items

### 3. Source Backing
- Source URLs in metadata
- No invented claims
- No confidential employer/client data

### 4. Anti-Repetition
- Compare topic, angle, opening sentence, structure, and final takeaway against recent content
- Reject or rewrite if too similar
- Do not reuse the same opening style twice in a row
- Do not use the same post structure more than once per week

### 5. Professional Tone
- No hype
- No clickbait
- No excessive hashtags
- No generic AI buzzword posts
- Concise professional English (B2 level)

### 6. Frequency/Cooldown
- Do not generate another draft for the same topic within 7 days unless explicitly requested
- Default: max 2-3 strong candidates per week
- Prefer weekly digest for multiple weak/moderate signals

## Draft Status Model

| Status | Meaning |
|---|---|
| `candidate` | Identified from signal, not yet drafted |
| `drafted` | Draft created, pending review |
| `needs_review` | Flagged for quality concerns |
| `approved_manually` | Approved by human review |
| `rejected` | Rejected by quality gate or human review |
| `published_manually` | Published by manual action |

## Required Draft Metadata

Every draft must include:

```yaml
draft_id: "linkedin-2026-05-27-sap-ai-units"
source_signal_id: "signal-2026-05-27-001"
source_urls:
  - "https://help.sap.com/docs/SAP_S4HANA_CLOUD"
topic: "sap_business_ai"
angle: "cost_implication"
target_audience: "sap_ams_leads"
why_it_matters: "AI Units pricing changes affect AMS budget planning"
duplicate_check_result: "no_similar_recent"
quality_risk: low  # low | medium | high
recommended_publish_window: "2026-05-29"
status: drafted
style_pattern: consultant_takeaway
opening_type: problem_first
repeated_structure_check: pass
similar_recent_post: null
human_voice_score: 4  # 1-5
template_risk: low  # low | medium | high
rewrite_reason: null
```

## Rejection Rules

Reject draft generation if:

- Source is weak or unclear
- Topic is too generic
- Draft is mostly summary without professional insight
- Draft is too similar to recent content
- Content sounds promotional without substance
- It needs confidential/client-specific examples
- It would create too many posts in a short period

## Author Voice

### Preferred Voice
- Direct
- Practical
- Slightly skeptical
- Operational, not inspirational
- Clear B2-level English
- Short paragraphs
- Concrete SAP/AMS/process implications
- One useful idea per post
- No hype

### Banned Patterns

Never use:

- "In today's fast-paced world..."
- "AI is transforming everything..."
- "Here are 5 reasons why..."
- "I'm excited to share..."
- "Game-changer"
- "Revolutionary"
- "Unlock the power of..."
- "The future of X is here"
- "This got me thinking..."
- Repeated emoji bullets
- Hook → 3 bullets → CTA template
- Generic "What do you think?" ending
- Excessive hashtags

## Style Patterns

Each draft must intentionally choose one pattern:

### 1. signal_note
Start with the external signal. Explain why it matters. End with operational implication.

### 2. consultant_takeaway
Start with a practical SAP/AMS problem. Connect source signal to that problem. End with what teams should check.

### 3. risk_note
Start with a risk or hidden cost. Explain the mechanism. End with a small control/check.

### 4. process_note
Start with a process failure mode. Explain where AI/automation helps or does not help. End with a realistic next step.

### 5. contrarian_note
Start with what people may overestimate. Explain what matters more. End with balanced takeaway.

### 6. mini_field_checklist
Start with a short context line. Provide 3-5 checks. End without weak engagement bait.

### 7. weekly_digest
Use only when there are multiple weak/moderate signals. Group into one useful summary. Do not create separate posts for every small signal.

## Anti-Repetition Rules

Before creating a draft:

- Compare with recent LinkedIn drafts and published records
- Check topic, angle, opening sentence, structure, and final takeaway
- Reject or rewrite if too similar
- Do not reuse the same opening style twice in a row
- Do not use the same post structure more than once per week
- Do not repeat the same CTA style

## Rewrite Process

If a draft feels generic:

1. Remove hype
2. Remove generic opening
3. Add one concrete SAP/AMS/process implication
4. Shorten
5. Change structure
6. Remove weak CTA
7. Re-check similarity

## Two-Variant Generation (Optional)

For each approved signal, optionally generate exactly two draft variants:

- Variant A: practical consultant note
- Variant B: risk/process takeaway

Then select the stronger one and mark the other as `rejected_variant`. Do not save both as active drafts unless explicitly requested.

## Quality Gate Checklist

A draft is acceptable only if:

- [ ] `human_voice_score >= 4`
- [ ] `template_risk = low`
- [ ] `repeated_structure_check = pass`
- [ ] Has a specific SAP/AMS/process takeaway
- [ ] Does not sound like generic marketing content

## Sample Accepted Draft

```yaml
draft_id: "linkedin-2026-05-20-clean-core-dashboard"
source_signal_id: "signal-2026-05-15-002"
source_urls:
  - "https://support.sap.com/en/alm/sap-cloud-alm.html"
topic: "sap_clean_core"
angle: "operational_visibility"
target_audience: "sap_ams_leads"
why_it_matters: "Clean Core dashboard gives AMS teams visibility into custom code health without manual audits"
duplicate_check_result: "no_similar_recent"
quality_risk: low
recommended_publish_window: "2026-05-22"
status: approved_manually
style_pattern: consultant_takeaway
opening_type: problem_first
repeated_structure_check: pass
similar_recent_post: null
human_voice_score: 4
template_risk: low
```

**Draft body:**

> Most AMS teams discover custom code issues during upgrades or incidents. By then, the cleanup cost is already high.
>
> SAP Cloud ALM now has a Clean Core dashboard that shows custom code health continuously. For AMS teams, this means proactive monitoring instead of reactive cleanup.
>
> What to check:
> - Is your custom code inventory mapped against SAP standard objects?
> - Are you tracking compatibility pack deadlines?
> - Do you have a plan for custom code remediation before the next upgrade cycle?
>
> The dashboard won't replace architecture discipline. But it gives AMS teams a starting point for conversations about technical debt that were previously hard to quantify.

## Sample Rejected Draft

```yaml
draft_id: "linkedin-2026-05-20-ai-revolution"
source_signal_id: "signal-2026-05-20-003"
source_urls:
  - "https://news.sap.com/ai-announcement"
topic: "sap_business_ai"
angle: "generic_hype"
target_audience: "general"
why_it_matters: null
duplicate_check_result: "similar_to_draft-2026-05-15"
quality_risk: high
recommended_publish_window: null
status: rejected
style_pattern: signal_note
opening_type: generic_hype
repeated_structure_check: fail
similar_recent_post: "draft-2026-05-15"
human_voice_score: 2
template_risk: high
rewrite_reason: "Generic hype opening, no operational takeaway, similar to recent post"
```

**Rejection reason:** Generic hype language ("revolutionary", "game-changer"), no specific SAP/AMS implication, too similar to recent post about AI adoption.

## No Automatic Publishing

This policy explicitly prohibits any automatic LinkedIn publishing. All drafts remain in `drafted`, `needs_review`, or `approved_manually` status until a human manually publishes them.

## Related

- #18 — LinkedIn editorial quality and manual approval policy
- #19 — LinkedIn author voice and style variation gate
- `docs/content-taxonomy.md` — Content type definitions
- `docs/classification-rules.md` — Content classification pipeline
