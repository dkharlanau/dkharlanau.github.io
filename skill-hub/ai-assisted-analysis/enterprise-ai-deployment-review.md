---
layout: default
title: "Enterprise AI Deployment Review — Working Skill"
description: "Run a vendor-neutral enterprise AI architecture workshop and produce a rollout decision register, authority matrix, cost model, evaluation plan and go-live recommendation."
permalink: /skill-hub/ai-assisted-analysis/enterprise-ai-deployment-review/
author: "Dzmitryi Kharlanau"
last_modified_at: 2026-11-25
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

# Enterprise AI Deployment Review

Use this working skill when a company is considering a new AI platform, adding an AI agent to a business process, expanding tool access, or reviewing a pilot before production.

The aim is to turn a platform discussion into an architecture decision with accountable owners and testable controls. Read the [AI Deployment Decision Map](/blog/enterprise-ai-deployment-decision-map/) for the reasoning behind the method.

## Run a discovery workshop

| Workstream | Ask | Produce |
| --- | --- | --- |
| Business value | Which task, baseline, outcome and constraint? | Scope and success criteria |
| Identity | Who acts, who can invoke it, and who can see the result? | Trust boundary and effective roles |
| Authority | What can be read, proposed, approved or executed? | Tool/action permission matrix |
| Governance | How are workflows reviewed, versioned and retired? | Release and ownership policy |
| Economics | What costs money, who pays, and what is the cost per accepted result? | Budget, limits and unit economics |
| Evidence | How will we detect failure, test controls and stop the workflow? | Evaluation, audit and operational plan |

Begin with the smallest workflow that can prove value. Compare it with the existing process and a deterministic alternative. Invite the business owner, IAM/security, system owners, platform operations, finance and risk representatives as needed.

## Decision record template

Copy this into a working document. Make a separate record for each significant decision.

```text
Decision ID:
Business objective and constraint:
Decision question:
Options and trade-offs:
Recommended option and reason:
Accountable owner / required approvers:
Affected identities, data, tools and workflows:
Dependencies and downstream impact:
Evidence required before launch:
Cost and reversibility:
Rollback or stop mechanism:
Status: proposed / accepted / deferred / rejected
Review trigger and date:
```

## Launch gate

- Business baseline and success criteria are measurable.
- Effective access, execution identities and audience boundaries are tested.
- Read, draft, approve and execute are separately scoped.
- Negative tests cover unauthorized actions, unsafe input, stale evidence, duplicates and failures.
- Cost limits, alert routing, audit retention and operational ownership are agreed.
- A stop mechanism and recovery procedure have been tested.

If evidence is missing, record the gap and its owner. Recommend **hold** or a bounded conditional pilot rather than inventing readiness. Do not approve deployment on behalf of a stakeholder.

## Practice case

A logistics company wants AI to investigate delivery and master-data errors and create tickets in its service desk. Its support and finance teams share an identity directory, but finance records are sensitive.

Design a read-only first phase. Then explain the changes required to permit draft ticket creation and, separately, production data changes. Decide whether a shared service identity is appropriate. Identify the owner of every control, the expected test evidence and how to stop the pilot.

Use the [portable agent skill source](https://github.com/dkharlanau/dkharlanau.github.io/tree/main/agent-skills/skills/enterprise-ai-deployment-review) after the change is merged.

## Related methods

- [AI Agent Authority Design](/skill-hub/ai-assisted-analysis/ai-agent-authority-design-working-skill/) for detailed action-level authority.
- [Architecture Decision Record](/skill-hub/architecture/architecture-decision-record-working-skill/) for significant design choices.
- [ERP Agent Gateway pilot](/labs/business-ai/erp-agent-gateway/) for a bounded enterprise integration design.

This is a proposed working method, not a certification or a production-readiness guarantee. Use synthetic or explicitly approved inputs and validate the platform's actual controls.
