---
name: enterprise-ai-deployment-review
description: Use when planning or reviewing an enterprise AI rollout, extending an agent to a new business workflow, changing an AI trust boundary, or deciding if a pilot is ready to scale. Produce an evidence-based decision register, ownership map, permission boundaries, economics and launch recommendation. Do not use for routine prompt editing or as automatic deployment approval.
---

# Enterprise AI Deployment Review

## Purpose

Turn a rollout objective into a bounded, accountable and testable operating design, independent of the AI vendor.

## Use when

- A new enterprise AI platform or agent is proposed.
- A pilot will gain new users, data, tools, autonomy or audiences.
- Security, finance or a process owner asks for a deployment review.

## Do not use when

- Only a model benchmark or prompt rewrite is needed.
- A technical change has no impact on the AI operating model.
- The request is to approve or execute a production change without authorized human decisions.

## Required inputs

- Business workflow, baseline, expected outcome, non-negotiable constraints.
- Candidate platform and documented control capabilities, if known.
- Users, workloads, identities, roles, source systems, data classes and tools.
- Budget, proposed autonomy, risk owners and current evaluation evidence.

Mark missing information explicitly. Separate facts, assumptions and design proposals.

## Workflow

1. Compare the status quo, deterministic automation, AI assistance and bounded autonomy.
2. Map tenants, identity sources, effective role grants, execution identities, data and output audiences. Verify platform-specific semantics; do not assume deny overrides or additive grants.
3. Classify actions by read, propose, validate, approve and execute. Define action policy, source-system authorization, approval, failure behavior and duplicate prevention.
4. Define how workflows move from sandbox to reviewed publication, with version, tests, owner, rollback and retirement.
5. Estimate full costs and value per accepted result. Distinguish group/member/workload limits from shared budgets. Record assumptions and sensitivity.
6. Design privacy-aware audit, operational telemetry, evaluations and business measures before access. Identify alert and review owners, retention and stop mechanisms.
7. Trace downstream impact of any identity, access, governance, budget or data-boundary change. Test overlapping grants and shared-channel audiences.
8. Produce decision records, unresolved questions and a go, conditional go or hold recommendation. Assign each gap to an accountable owner.
9. Identify triggers for reassessment: new model, data class, audience, connector, write permission, execution identity or scale.

## Decision rules

- Technical access is not business authority. No model can authorize itself.
- Default to the least authority needed for a useful workflow; no unreviewed production writes.
- Do not claim a product feature, compliance outcome or successful test without evidence.
- Use deterministic controls for identity, hard policy, exact calculations and transaction validation.
- Missing evidence is not a pass. For high-impact or irreversible decisions require accountable approval.
- Keep secrets and private exports out of public examples and artifacts.
- Expand only when quality, safety, unit cost and operational ownership support it.

## Output format

Produce an Enterprise AI Deployment Review containing:

- Objective, baseline, scope, alternatives and recommendation.
- Six decision records with owners, dependencies, change cost, evidence and review triggers.
- Identity and trust-boundary map; tool and action authority matrix.
- Cost model and measurement assumptions.
- Test cases, audit coverage, monitoring, stop and recovery design.
- Go / conditional go / hold with blockers, owners and acceptance conditions.

## Quality gates

- [ ] Every action has a permitted execution identity and audience boundary.
- [ ] Each significant decision has an owner, alternatives and change-impact analysis.
- [ ] Business outcomes, costs and quality are comparable against a baseline.
- [ ] Negative tests, failure handling and recovery are explicit.
- [ ] No assumed controls are presented as verified.
- [ ] A named decision-maker, not the agent, owns release approval.

## References

- references/method.md — Design logic and impact analysis.
- references/templates.md — Decision and test records.
- references/examples.md — Synthetic SAP support example.

This is a proposed method. It does not replace vendor documentation, security review, legal analysis or production acceptance.
