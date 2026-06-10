---
title: "Domain Research: Change Impact Analysis"
robots: noindex
sitemap: false
---

# Change Impact Analysis

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from change risk assessment, dependency mapping, and deployment guardrails?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [AWS Post-Event Summaries](https://aws.amazon.com/message/41926) (src-405) | 1 | Detailed technical postmortems showing change-related failures | Trigger/propagation analysis, remediation categories |
| [GitHub October 21 Post-Incident](https://github.blog/2018-10-30-oct21-post-incident-analysis/) (src-406) | 2 | Outage caused by orchestrator-driven topology change | Orchestrator guardrails, failover testing, status reporting |
| [Defensive Cloud Outage Template](https://defensive.cloud/outage-postmortem-template-and-playbook-based-on-x-cloudflar) (src-418) | 2 | Multi-provider outage playbook with change correlation | Canary windows, synthetic tests, multi-party approval |
| [Netflix AWS Degradation Postmortem](http://techblog.netflix.com/2012/10/post-mortem-of-october-222012-aws.html) (src-419) | 2 | Zone evacuation driven by automated tooling | Resilience design, drill practice, blast radius control |
| [DORA 2024 Report](https://dora.dev/) (src-308) | 2 | Change Failure Rate as a primary metric | Deployment quality, recovery time benchmarking |

## Key practical patterns

- Correlate recent changes (deployments, config changes, infrastructure updates) with incident onset; change failure rate is a primary DORA metric.
- Require multi-party approval for DNS, global-edge, and critical configuration changes.
- Use canary windows and synthetic tests that exercise production paths before full rollout.
- Maintain a dependency map so blast radius of a change can be estimated before deployment.
- Include rollback steps in every change plan; test rollback before it is needed.

## Artifacts found

- Change request with impact assessment (affected services, blast radius, rollback plan)
- Dependency map / service topology diagram
- Canary release plan with success criteria and abort thresholds
- Pre- and post-deployment synthetic test results
- Change failure rate report (DORA metric)

## Decision rules found

- If a deployment window coincides with incident onset, then treat the deployment as the primary suspect until ruled out.
- If a change touches DNS or global-edge configuration, then require multi-party approval and a documented rollback.
- If canary metrics exceed abort thresholds, then automatically halt rollout and trigger rollback.
- If a service has no dependency map, then do not approve production changes until the map is documented.
- If change failure rate exceeds 15%, then halt feature work and invest in testing and deployment guardrails.

## Quality gates found

- Every production change must have a rollback plan that has been tested in staging.
- Canary releases must have explicit success criteria and automatic abort thresholds.
- Changes to shared infrastructure require cross-team review.
- Post-change monitoring must cover at least one full business cycle before declaring success.
- Change failure rate must be tracked and reviewed monthly.

## Common failure modes

- Deploying without a tested rollback, forcing teams to debug forward under pressure.
- Missing dependency maps, so changes to shared services surprise downstream teams.
- Canary windows that are too short or lack real traffic patterns, missing latent bugs.
- Manual config changes without version control or peer review.
- Retry storms and cascading failures triggered by a seemingly minor change.

## Candidate skills

- `change-impact-assessment`
- `canary-release-guardrails`
- `deployment-correlation`
- `rollback-testing`
- `config-change-control`

## Source-backed notes

- AWS post-event summaries categorize remediations as immediate, short-term (≤30 days), and architectural (src-405).
- GitHub's postmortem highlights the risk of automated orchestrator actions that are "correct" but architecturally unsafe (src-406).
- DORA identifies Change Failure Rate as a key metric; elite performers keep it under 5% (src-308).

## Gaps / further research needed

- Change impact analysis is often treated as a sub-section of change management rather than a dedicated discipline.
- Few public, reputable frameworks specifically for operational change impact analysis outside of ITIL Change Enablement.