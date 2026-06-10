---
title: "Domain Research: Root Cause Analysis"
robots: noindex
sitemap: false
---

# Root Cause Analysis

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from blameless postmortems, causal analysis, and action item tracking?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [Postmortem Culture (Google SRE Workbook)](https://sre.google/workbook/postmortem-culture/) (src-402) | 1 | Definitive public chapter on blameless postmortems | Postmortem templates, action item tracking, cultural incentives |
| [Google SRE Incident Management Guide](https://sre.google/resources/practices-and-processes/incident-management-guide/) (src-404) | 1 | Condensed guide on learning from incidents | Postmortem timeliness, aggregate data analysis |
| [AWS Post-Event Summaries](https://aws.amazon.com/message/41926) (src-405) | 1 | Detailed technical postmortems from major outages | Timeline structure, remediation categories, customer communication |
| [GitHub October 21 Post-Incident Analysis](https://github.blog/2018-10-30-oct21-post-incident-analysis/) (src-406) | 2 | Detailed public postmortem of 24-hour outage | Orchestrator guardrails, status page design, data integrity trade-offs |
| [Defensive Cloud Outage Postmortem Template](https://defensive.cloud/outage-postmortem-template-and-playbook-based-on-x-cloudflar) (src-418) | 2 | Reusable template for multi-provider outages | RCA exercises, metrics, organizational safeguards |
| [Netflix AWS Degradation Postmortem](http://techblog.netflix.com/2012/10/post-mortem-of-october-222012-aws.html) (src-419) | 2 | Classic example of zone evacuation drill value | Resilience design, drill practice, tooling |

## Key practical patterns

- Use at least two complementary RCA methods per major incident: timeline reconstruction + 5 Whys or fishbone.
- Stop the 5 Whys when you reach an actionable fix, not an unactionable abstraction like "human error."
- Distinguish trigger (proximate event) from root cause (systemic condition that allowed the trigger to cause harm).
- Include "what went well," "what went wrong," and "where we got lucky" in every postmortem.
- Aggregate postmortem data across the organization to identify recurring patterns and systemic investment areas.

## Artifacts found

- Blameless postmortem document (summary, timeline, trigger, propagation, root cause, impact, action items)
- Causal diagram or fishbone diagram
- 5 Whys analysis sheet
- Action item tracker with owners and due dates
- Customer-facing postmortem summary (for external incidents)

## Decision rules found

- If a postmortem names an individual as the cause, then rewrite it to focus on the system or process that enabled the failure.
- If the 5 Whys chain ends at "human error," then continue asking why the system allowed that human action to cause harm.
- If a SEV1 incident occurs, then run an RCA workshop and publish the timeline within 10 days.
- If postmortem action items exist, then prioritize them in the team backlog alongside feature work.
- If a pattern appears across multiple postmortems, then escalate from team-level fixes to organizational infrastructure investment.

## Quality gates found

- Postmortems must be blameless and reviewed for judgmental language before publishing.
- Action items must be specific, assigned, and tracked to completion; vague items like "be more careful" are rejected.
- Postmortems must distinguish customer-impact window from technical window.
- RCA must include at least two methods (timeline + causal technique).
- Postmortem completion must have an SLO agreed with stakeholders.

## Common failure modes

- Stopping at the first convenient cause rather than the systemic root.
- Blameful language that prevents honest reporting and hides true causes.
- Postmortems filed and forgotten; action items never tracked or completed.
- Incomplete timelines due to lack of centralized logging or poor channel hygiene.
- Confusing trigger with root cause, leading to fixes that only address symptoms.

## Candidate skills

- `blameless-postmortem-writing`
- `5-whys-facilitation`
- `timeline-reconstruction`
- `action-item-tracking`
- `pattern-analysis`

## Source-backed notes

- Google SRE Workbook provides a side-by-side case study of a "bad" vs. "good" postmortem and recommends Wheel of Misfortune training (src-402).
- AWS post-event summaries use a structured format: Window, Summary, Architecture Primer, Trigger, Propagation, Recovery, Remediations, Timeline (src-405).
- Defensive Cloud template recommends using at least two RCA methods and tracking MTTD, MTTR, request success rate, and change failure rate (src-418).

## Gaps / further research needed

- Root cause analysis method diversity is underrepresented; 5 Whys and fishbone are well-documented, but Fault Tree Analysis, STAMP/STPA, and Causal Analysis based on System Theory are harder to find in free, operationally focused sources.
- NASA Lessons Learned Database and "How Complex Systems Fail" (Richard Cook) would add valuable cross-industry resilience engineering perspective.