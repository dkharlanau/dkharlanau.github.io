---
title: "Synthesis: Recommended Next Skill Batches"
robots: noindex
sitemap: false
---

# Recommended Next Skill Batches

## Batch 1: High-Value, Strong Evidence, Low Effort (Immediate)

| Skill | Type | Why now | Source support | Effort |
|---|---|---|---|---|
| `expectation-suite-design-and-maintenance` | Agent skill | Strong open-source docs (Great Expectations); fills data quality gap | src-008 | Low |
| `pipeline-quality-gate-engineering` | Agent skill | Complements existing data-governance skill; dbt and GX docs are strong | src-008, src-009 | Low |
| `openapi-design-first` | Public skill | Google AIPs are stable and authoritative; high demand for API governance | src-301, src-312 | Low |
| `asyncapi-contract-design` | Public skill | AsyncAPI 3.x is maturing; event-driven architecture is common | src-302, src-306 | Low |
| `blameless-postmortem-writing` | Agent skill | Strong Google SRE source; complements existing root-cause-analysis skill | src-402, src-405 | Low |
| `escalation-brief-writing` | Public skill | Strong practitioner frameworks (Front, CX Foundation); universal need | src-507, src-508 | Low |

## Batch 2: High-Value, Strong Evidence, Medium Effort (Next Sprint)

| Skill | Type | Why next | Source support | Effort |
|---|---|---|---|---|
| `nfr-scenario-writing` | Agent skill | SEI ATAM is authoritative; fills architecture gap between ADRs and Well-Architected | src-209 | Medium |
| `well-architected-review` | Agent skill | AWS/Azure/GCP frameworks are mature; need consolidated multi-cloud skill | src-201, src-202, src-203 | Medium |
| `slo-and-error-budget-design` | Agent skill | Google SRE sources are strong; complements observability skill | src-401, src-403 | Medium |
| `opentelemetry-instrumentation` | Agent skill | CNCF standard is production-ready; high demand for distributed tracing | src-303 | Medium |
| `idempotency-key-design` | Agent skill | Stripe reference is industry standard; critical for integration reliability | src-305 | Medium |
| `problem-statement-crafting` | Public skill | USDS and GDS sources are strong; foundational for all discovery work | src-501, src-502 | Medium |
| `risk-triage-and-register-management` | Public skill | NIST and ISO 31000 are authoritative; universal for project governance | src-504, src-505 | Medium |

## Batch 3: Strategic, Emerging, or Complex (Future)

| Skill | Type | Why future | Source support | Effort |
|---|---|---|---|---|
| `agent-memory-curator` | Agent skill | Academic sources are promising but still emerging; wait for production patterns to stabilize | src-610 | High |
| `reflection-loop-designer` | Agent skill | Research is active but not yet consolidated into enterprise playbooks | src-609 | High |
| `context-compressor` | Agent skill | Three-tier compression is cutting-edge; needs more real-world validation | src-610 | High |
| `safety-gatekeeper` | Agent skill | Cross-lab evaluation is new; safety standards are still evolving | src-605 | High |
| `human-approval-gate` | Agent skill | UX patterns are under-documented; needs concrete interface research | src-603, src-604 | High |
| `evidence-assessment-checklist` | Public skill | VHA case study is strong but domain-specific; needs broader enterprise adaptation | src-509 | Medium |
| `psychological-safety-facilitation` | Public skill | Google re:Work is strong but soft-skill delivery is harder to templatize | src-503 | High |

## Batch 4: Strengthen Existing Skills (Ongoing)

| Existing Skill | Enhancement | Source support |
|---|---|---|
| `data-governance-ownership` | Add policy-as-code section and classification taxonomy template | src-002, src-003, src-011 |
| `architecture-decision-record` | Add SAP-contextualized ADR template and trade-off heatmap | src-205, src-212 |
| `acceptance-criteria` | Add edge-case expansion checklist and NFR coverage guide | src-104, src-108 |
| `incident-triage` | Add severity-classification decision tree and SAP-specific incident quality criteria | src-401, src-415 |
| `root-cause-analysis` | Add multi-provider outage postmortem template and 5-Whys facilitation guide | src-402, src-418 |
| `change-impact-analysis` | Add dependency-map + blast-radius estimation template | src-405, src-418 |
| `non-functional-requirements` | Add SLO/SLI design guide and cloud-specific NFR mapping | src-201, src-209 |

## Deferred / Needs More Research

| Skill | Why deferred | Research needed |
|---|---|---|
| `capability-map-design` | Existing skill is adequate; Avolution source is Tier 3 | Better Tier 1/2 capability mapping case studies |
| `business-vocabulary-modeling` | SBVR is strong but niche; need more practitioner adoption examples | Public case studies of SBVR in enterprise settings |
| `metadata-platform-architecture` | DataHub docs are strong but rapidly evolving | Stable reference architecture patterns |
| `circuit-breaker-implementation` | Slys.dev source is Tier 3; need stronger authoritative guidance | Netflix or AWS official circuit breaker patterns |
| `event-sourcing-operations` | Fowler warns of complexity; need more operational success stories | Production event sourcing runbooks and recovery patterns |