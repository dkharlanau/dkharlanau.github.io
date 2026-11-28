# Data Architecture Selection — Detailed Method

## Start with a consumer, not a product

Write: “For [role] to [take action], the system must answer [question] with [freshness], [accuracy], [history], [authorization] and [recovery] under [cost constraint].” If the sentence cannot be completed, do discovery first.

## Separate the architecture dimensions

| Dimension | Choices to compare | Evidence needed |
| --- | --- | --- |
| Serving | Governed warehouse/semantic model, lakehouse SQL, federation | Representative query, response-time and concurrency tests |
| Storage | Relational, object, hybrid | Retention, source types, table format and lifecycle policy |
| Movement | Batch, scheduled incremental, CDC, streaming, virtualization | Change volume, deletes, replay, latency, source load |
| Modeling | 3NF, dimensions/facts, Data Vault, logical semantic layer | Grain, identity, history and self-service usability |
| Governance | MDM, catalog, lineage, access, data contracts | Owner, quality tests, policies, stewardship workflow |
| Organization | Central platform, domain-owned products, federated governance | Product owner, funding, operations and standards |

Data fabric can strengthen metadata, policy and access across different stores. Data mesh needs domain ownership, data as a product, a self-service platform and federated computational governance. They are not warehouse replacements by default.

## Evidence hierarchy

1. Measured behavior in the relevant environment.
2. Source-system interface/schema documentation and security requirements.
3. Current vendor documentation with deployment and licensing scope.
4. Domain expert explanations, captured as claims until tested.
5. Design assumptions and estimates, always labeled.

Never convert an estimated cost, benchmark or uptime into an observed fact.

## Trade-off lenses

For each candidate, evaluate:
- **Correctness:** identifier semantics, row grain, duplicate and deletion handling.
- **Freshness:** source update cadence, ingestion lag, transformation lag, serving lag.
- **History:** effective dating, event retention, source replay, SCD behavior.
- **Access:** classification, least privilege, residency, tenant/row security.
- **Usability:** self-service, SQL, catalog, semantic consistency, skill fit.
- **Reliability:** missed updates, retries, ordering, idempotency, recovery time.
- **Economics:** compute, storage, network/egress, maintenance, staffing, migration.
- **Portability:** lock-in, table formats, contracts and exit path.

Prefer qualitative judgments with reasons to false precision. If using numerical weights, get stakeholder approval for weights before scoring.

## Thin slice

Select a single business question and make an end-to-end path:
source → approved ingestion/access → verified keys → modeled measure → authorized consumer.

Test at least: a missing attribute, a duplicate, a changed/deleted record, replay after failure, freshness at load, historical query, denied-access case and result reconciliation.

## Human review

Architect selects the pattern and accepts trade-offs. Data owners confirm semantics, privacy/security validates authorization, platform team validates operating costs and SRE/operations accepts recovery design. This skill generates evidence and proposals, never production changes.

## Key sources

- James Serra, *Deciphering Data Architectures*, O'Reilly (2024), chapters on design sessions, modeling, ingestion, MDW, fabric, lakehouse, mesh and operating models.
- Zhamak Dehghani: https://martinfowler.com/articles/data-mesh-principles.html
- Kimball: https://www.kimballgroup.com/2008/08/slowly-changing-dimensions/
- SAP Datasphere: https://help.sap.com/docs/portfolio-category/data-cloud
- Kafka Streams state: https://docs.confluent.io/platform/current/streams/architecture.html
