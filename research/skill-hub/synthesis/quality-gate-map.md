---
title: "Synthesis: Quality Gate Map"
robots: noindex
sitemap: false
---

# Quality Gate Map

| Quality gate | Domain | Applies to | Source support | Notes |
|---|---|---|---|---|
| Classification coverage audit for all tier-1 data assets | data-governance | Data governance program | src-002, src-003 | AWS and Microsoft guidance |
| Periodic access review and recertification cycle | data-governance | RBAC policies | src-003 | Microsoft Purview best practice |
| Policy compliance scan against metadata catalog | data-governance | Governance policies | src-006, src-011 | DataHub and Databricks guidance |
| Stewardship accountability check (ownership assigned and active) | data-governance | Data ownership model | src-001, src-012 | DAMA and SAP MDG principle |
| Not-null and uniqueness constraints on primary keys | data-quality | Pipeline ingestion | src-008, src-009 | Great Expectations and dbt standard |
| Accepted-values checks for categorical fields | data-quality | Data validation | src-008, src-009 | Standard declarative checks |
| Freshness thresholds for time-sensitive data | data-quality | Data pipelines | src-008, src-009 | SLO-aligned quality gate |
| Relationship integrity between fact and dimension tables | data-quality | Data warehouse | src-008, src-009 | Referential integrity gate |
| Metadata freshness check (last ingestion timestamp) | metadata-management | Metadata pipelines | src-006, src-007 | DataHub and OpenLineage |
| Connector health and failure monitoring | metadata-management | Ingestion infrastructure | src-006 | DataHub operational gate |
| Coverage audit for tier-1 pipelines | data-lineage | Lineage collection | src-007 | OpenLineage completeness gate |
| Every requirement must have a unique ID and a verification method | business-analysis | Requirements management | src-109 | Jama RTM guidance |
| Service/design must pass assessment against explicit standard before next phase | business-analysis | Phase transitions | src-102 | GDS Service Manual gate |
| Research findings must be demonstrably linked to design decisions | business-analysis | User research | src-102, src-110 | GDS assessment criteria |
| Acceptance criteria must be reviewed and agreed upon before sprint start | requirements | Sprint planning | src-104, src-108 | Scrum Guide and Agile Alliance |
| DoD must be met for every Increment; undone work returns to Product Backlog | requirements | Increment release | src-104 | Scrum Guide canonical gate |
| Every ADR must list considered options, not just the chosen one | architecture | ADR review | src-206, src-212 | MADR template requirement |
| ADR status must be actively maintained (Proposed → Accepted → Deprecated/Superseded) | architecture | ADR lifecycle | src-206, src-212 | MADR operational gate |
| Architecture must be evaluated against quality attribute scenarios before implementation | architecture | Architecture review | src-209 | SEI ATAM gate |
| Well-Architected Review must be completed before production go-live | architecture | Production readiness | src-201, src-202, src-203 | Cloud framework gate |
| OpenAPI linting passes in CI/CD (Spectral or equivalent) | api-design | API publication | src-301, src-312 | Google AIPs and Treblle |
| Breaking-change detection on PR blocks merge if breaking | api-design | API evolution | src-312 | Treblle guidance |
| Contract tests validate implementation against spec | api-design | API implementation | src-301, src-312 | Design-first validation |
| Idempotency key collision detection and request hash validation | integration | Retry safety | src-305 | Stripe implementation gate |
| Circuit breaker monitoring (error rate, open-state duration) | integration | Resilience | src-311 | Resilience engineering gate |
| Auto-instrumentation coverage for all services | observability | Observability rollout | src-303 | OpenTelemetry gate |
| Context propagation validated through service mesh / proxy layers | observability | Distributed tracing | src-303 | OpenTelemetry integration gate |
| SLO review meetings with error budget burn rate tracking | observability | Reliability management | src-401, src-403 | Google SRE gate |
| Service Catalog is complete: every service has owner, severity, linked runbook | incident-management | Incident readiness | src-401, src-411 | Google SRE and incident.io |
| 100% of SEV1 and SEV2 incidents have scheduled postmortem within 48–72 hours | incident-management | Learning culture | src-401, src-411 | Google SRE and incident.io |
| Postmortems must be blameless and reviewed for judgmental language | root-cause-analysis | Postmortem publication | src-402, src-405 | Google SRE Workbook gate |
| Action items must be specific, assigned, and tracked to completion | root-cause-analysis | Remediation | src-402, src-418 | Google SRE and Defensive Cloud |
| Every production change must have a tested rollback plan | change-impact-analysis | Change approval | src-405, src-418 | AWS and Defensive Cloud |
| Canary releases must have explicit success criteria and automatic abort thresholds | change-impact-analysis | Deployment safety | src-418 | Defensive Cloud gate |
| Change failure rate must be tracked and reviewed monthly | change-impact-analysis | Continuous improvement | src-308 | DORA metric gate |
| Problem statements must be validated by the people experiencing the problem | professional-skills | Problem framing | src-501 | USDS discovery sprint gate |
| Assumptions must be reviewed and validated at regular intervals | professional-skills | Project management | src-506 | PMBOK/RAID gate |
| Escalation briefs must include: concise problem statement, severity, action-oriented language, context, status updates | professional-skills | Escalation quality | src-507, src-508 | CX Foundation and Front gates |
| Risk register must be reviewed at project milestones and when assumptions change | professional-skills | Risk management | src-504, src-505 | NIST/ISO 31000 gate |
| Run `validate_agent_skills.py` before committing changes | ai-agent-skills | Skill quality | src-601 | Repository validation gate |
| Pass the "intern test": a human given only the function description should know how to call it | ai-agent-skills | Tool design | src-602 | OpenAI guidance |
| Run adversarial suites (StrongREJECT) before every major model update | ai-agent-skills | Safety validation | src-605 | Cross-lab evaluation gate |
| Terminate reflection loops if the score does not improve between iterations | ai-agent-skills | Reflection efficiency | src-609 | Self-reflection research gate |