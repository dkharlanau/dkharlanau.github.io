---
title: "Synthesis: Decision Rule Map"
robots: noindex
sitemap: false
---

# Decision Rule Map

| Decision rule | Domain | Supported by source IDs | Used by skill | Notes |
|---|---|---|---|---|
| If data is a strategic asset, then establish a formal governance program with executive sponsorship. | data-governance | src-001, src-010 | data-governance-ownership | Foundation rule from DAMA and Data Mesh |
| If multiple autonomous domains exist, then federate governance rather than centralizing all decisions. | data-governance | src-010, src-011 | federated-governance-operating-model | Data Mesh and Databricks guidance |
| If sensitive data is present, then classify at ingestion and propagate tags through lineage. | data-governance | src-002, src-003 | data-governance-ownership | AWS and Microsoft guidance |
| If data enters a pipeline, then validate at ingestion before downstream consumption. | data-quality | src-008, src-009 | pipeline-quality-gate-engineering | Great Expectations and dbt principle |
| If schema evolves, then update quality rules in version control simultaneously. | data-quality | src-008, src-009 | expectation-suite-design-and-maintenance | Prevents drift between code and checks |
| If metadata is stale, then move from batch to real-time streaming ingestion. | metadata-management | src-006, src-007 | metadata-platform-architecture | DataHub and OpenLineage guidance |
| If multiple orchestrators are used, then standardize lineage collection on an open standard. | data-lineage | src-007 | openlineage-integration-and-instrumentation | OpenLineage specification principle |
| If a requirement cannot be traced to a user need, then it should not be in scope. | business-analysis | src-101, src-102 | discovery-sprint-facilitation | USDS and GDS principle |
| If a process map cannot be validated by the people who perform the work, then it is fiction. | business-analysis | src-105 | process-mapping-with-bpmn | BPMN validation principle |
| If a story has no acceptance criteria, then it is not ready for development. | requirements | src-104, src-108 | given-when-then-authoring | Scrum Guide and Agile Alliance |
| If a Product Backlog item does not meet the Definition of Done, then it cannot be released. | requirements | src-104 | definition-of-done-crafting | Scrum Guide canonical rule |
| If a decision affects more than one team, then use MADR with full RACI front matter. | architecture | src-206, src-212 | adr-authoring-madr | MADR template guidance |
| If a decision changes, then create a new superseding ADR rather than editing the accepted one. | architecture | src-206, src-212 | adr-governance | Immutability principle |
| If a quality attribute scenario cannot be mapped to an architectural approach, then the architecture has a risk. | architecture | src-209 | nfr-scenario-writing | SEI ATAM principle |
| If a workload is business-critical, then prioritize Reliability and Security over Cost Optimization. | architecture | src-201, src-202, src-203 | well-architected-review | Cloud pillar trade-off rule |
| If an API exposes a collection, it must support standard List with pagination. | api-design | src-301 | openapi-design-first | Google AIP rule |
| If a POST operation has side effects, require an idempotency key. | integration | src-305 | idempotency-key-design | Stripe canonical rule |
| If a failure is transient, retry with capped exponential backoff and jitter. | integration | src-305, src-311 | retry-and-backoff-strategy | Industry standard pattern |
| If a service is consistently failing, open the circuit breaker and fail fast. | integration | src-311 | circuit-breaker-implementation | Resilience pattern |
| If a request crosses a service boundary, propagate trace context. | observability | src-303 | opentelemetry-instrumentation | OpenTelemetry principle |
| If an alert fires and meets SEV1/SEV2 criteria, then auto-create a dedicated incident channel and page the primary on-call within 2 minutes. | incident-management | src-401, src-404 | incident-commander-basics | Google SRE guidance |
| If mitigation and root cause investigation are competing for attention, then prioritize mitigation first. | incident-management | src-401, src-403 | mitigation-first-response | Google SRE principle |
| If a postmortem names an individual as the cause, then rewrite it to focus on the system or process that enabled the failure. | root-cause-analysis | src-402, src-405 | blameless-postmortem-writing | Blamelessness rule |
| If the 5 Whys chain ends at "human error," then continue asking why the system allowed that human action to cause harm. | root-cause-analysis | src-402, src-418 | 5-whys-facilitation | Systems thinking rule |
| If a deployment window coincides with incident onset, then treat the deployment as the primary suspect until ruled out. | change-impact-analysis | src-405, src-406 | deployment-correlation | AWS/GitHub postmortem pattern |
| If a change touches DNS or global-edge configuration, then require multi-party approval and a documented rollback. | change-impact-analysis | src-418 | config-change-control | Defensive Cloud rule |
| If a problem statement includes a proposed solution, then rewrite it to describe the issue only. | professional-skills | src-501 | problem-statement-crafting | USDS discovery sprint rule |
| If an assumption has high probability of being false and high impact, then convert it to a risk and add to the risk register. | professional-skills | src-506 | assumption-log-maintenance | PMBOK/RAID principle |
| If an escalation loses context between handoffs, then redesign the process to preserve full history. | professional-skills | src-508 | escalation-brief-writing | Front escalation framework |
| If a risk exceeds organizational risk appetite, then escalate to senior leadership before proceeding. | professional-skills | src-504, src-505 | risk-triage-and-register-management | NIST/ISO 31000 principle |
| If the model must decide between multiple external actions, use function calling; if it only needs to format data, use structured outputs. | ai-agent-skills | src-602 | tool-use-orchestrator | OpenAI canonical rule |
| If you have >20 functions, use namespaces or deferred loading. | ai-agent-skills | src-602 | tool-use-orchestrator | Context management rule |
| If deploying a general-purpose model, add extra output filters because non-reasoning models are more susceptible to misuse. | ai-agent-skills | src-605 | safety-gatekeeper | Cross-lab safety evaluation |
| If context exceeds 40% of the window, begin compressing inactive files. | ai-agent-skills | src-610 | context-compressor | Three-tier compression rule |