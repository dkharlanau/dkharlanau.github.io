---
title: "Synthesis: Artifact Template Map"
robots: noindex
sitemap: false
---

# Artifact Template Map

| Artifact | Used by skills | Source support | Template status | Gap |
|---|---|---|---|---|
| Data governance charter / operating model | data-governance-ownership, federated-governance | src-001, src-010, src-011 | Partial (concepts in working skill) | Needs structured template with RACI and policy-as-code sections |
| RBAC matrix and access control policy | data-governance-ownership, purview-governance | src-003, src-011 | No | Needs cloud-agnostic RBAC template with least-privilege checklist |
| Data classification taxonomy | data-governance-ownership, data-lake-governance | src-002, src-011 | No | Needs tiered classification template with propagation rules |
| Business glossary with domain boundaries | data-governance-ownership, metadata-management | src-001, src-006 | Partial | Needs term-to-asset linkage template |
| Expectation Suite (JSON/YAML) | expectation-suite-design, pipeline-quality-gates | src-008, src-009 | Partial (dbt schema.yml exists) | Needs Great Expectations suite template with profiling baseline |
| Data quality scorecard | data-quality-root-cause, master-data-quality | src-012, src-008 | Partial | Needs dimension-weighted scoring template |
| Metadata model schema | metadata-platform-architecture | src-006 | No | Needs entity-type definition template for DataHub-style ingestion |
| Lineage event schema (JSON) | openlineage-integration | src-007 | No | Needs OpenLineage Job/Run/Dataset event template |
| Discovery sprint report | discovery-sprint-facilitation | src-101, src-102 | Partial | Needs structured report template with findings/recommendations sections |
| BPMN process diagram | process-mapping-with-bpmn | src-105 | Partial | Needs BPMN 2.0 diagram checklist and validation rules |
| Business vocabulary (SBVR-style) | business-vocabulary-modeling | src-106 | No | Needs term/fact-type/rule statement template |
| Requirements Traceability Matrix | requirements-traceability-management | src-109 | Partial | Needs lightweight RTM template for non-regulated contexts |
| Given-When-Then scenario | acceptance-criteria-authoring | src-104, src-108 | Yes (in acceptance-criteria skill) | Needs edge-case expansion checklist |
| Definition of Done checklist | definition-of-done-crafting | src-104 | Partial | Needs product-level DoD template with NFR coverage |
| Architecture Decision Record (MADR) | adr-authoring-madr | src-206, src-212 | Yes (in architecture-decision-record skill) | Needs SAP-contextualized ADR template |
| Quality Attribute Scenario | nfr-scenario-writing | src-209 | No | Needs SEI-style scenario template (stimulus-response-measure) |
| Well-Architected Review report | well-architected-review | src-201, src-202, src-203 | Partial | Needs consolidated multi-cloud review template |
| Capability map (Level 1–3) | capability-map-design | src-204, src-210 | Yes (in capability-mapping skill) | Needs application-rationalization overlay template |
| OpenAPI specification | openapi-design-first | src-301, src-312 | Partial | Needs linting-ready spec template with Spectral ruleset |
| AsyncAPI specification | asyncapi-contract-design | src-302 | No | Needs channel/message/bindings template with compatibility policy |
| Idempotency key schema | idempotency-key-design | src-305 | No | Needs key store schema with TTL and hash validation |
| Retry policy configuration | retry-and-backoff-strategy | src-305, src-311 | No | Needs exponential-backoff config template with jitter settings |
| Circuit breaker config | circuit-breaker-implementation | src-311 | No | Needs threshold/timeout/state-transition template |
| OpenTelemetry instrumentation config | opentelemetry-instrumentation | src-303 | No | Needs auto-instrumentation + custom span template |
| SLO / error budget policy | slo-and-error-budget-design | src-401, src-403 | Partial | Needs burn-rate alert template |
| Incident declaration record | incident-commander-basics | src-401, src-404 | Partial (in incident-triage skill) | Needs severity-classification decision tree template |
| Blameless postmortem template | blameless-postmortem-writing | src-402, src-405 | Yes (in root-cause-analysis skill) | Needs multi-provider outage variant template |
| Change request with impact assessment | change-impact-assessment | src-405, src-418 | Partial (in change-impact-analysis skill) | Needs dependency-map + blast-radius estimation template |
| Problem statement document | problem-statement-crafting | src-501, src-502 | No | Needs USDS-style problem statement template |
| Assumption log | assumption-log-maintenance | src-506 | No | Needs IF-THEN assumption-to-risk conversion template |
| Escalation brief | escalation-brief-writing | src-507, src-508 | No | Needs concise-problem-statement + severity + action-oriented template |
| Risk register | risk-triage-and-register-management | src-504, src-505 | Partial | Needs ISO 31000-aligned risk treatment template |
| Evidence assessment checklist | evidence-assessment-checklist | src-509 | No | Needs VHA-style strength-of-evidence grading template |
| Decision journal | decision-journal-keeping | src-503 | No | Needs decision-quality template with pre-mortem section |
| `SKILL.md` with YAML frontmatter | structured-output-designer, tool-use-orchestrator | src-601, src-602 | Yes (in agent-skills repo) | Needs cross-platform compatibility checklist |
| Function JSON schema (strict mode) | tool-use-orchestrator | src-602 | Partial | Needs namespace + deferral pattern template |
| Safety evaluation rubric | safety-gatekeeper | src-605 | No | Needs jailbreak/misuse/sycophancy test case template |
| Human approval queue schema | human-approval-gate | src-603, src-604 | No | Needs pending/approved/denied/logged state template |
| Reflection prompt template | reflection-loop-designer | src-609 | No | Needs generator-critic-refiner prompt chain template |
| Context compression prompt | context-compressor | src-610 | No | Needs three-tier compression instruction template |