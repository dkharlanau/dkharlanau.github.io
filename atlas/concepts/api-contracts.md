---
layout: default
title: "API Contracts"
permalink: /atlas/concepts/api-contracts/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-architecture-map/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/data-contracts/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/sap/odata/
  - /atlas/sap/rest-apis/
  - /atlas/sap/soap/
  - /atlas/sap/sap-integration-suite/
---

# API Contracts

> **Status**: Skeleton — under review.  
> **Scope**: Contract design, versioning, and governance for SAP APIs.

## What it is

An API contract is a formal specification of request/response schemas, authentication, error codes, rate limits, and versioning policies. In SAP landscapes, contracts govern OData services, REST APIs, SOAP WSDLs, and RFC interfaces.

## When to use it

- Publishing APIs to external consumers or internal domains
- Defining stability commitments for S/4HANA released APIs
- Migrating from legacy SOAP/IDoc to modern REST/OData
- Enforcing consumer-driven contract testing in CI/CD

## When not to use it

- Internal-only, single-consumer, tightly coupled interfaces where contract overhead exceeds value
- Rapidly evolving experimental endpoints not yet ready for public commitment
- Legacy IDoc scenarios where the format is industry-standard and immutable

## SAP landscape fit

- **OData**: EDMX metadata serves as the machine-readable contract; CDS annotations extend semantics
- **REST/OpenAPI**: SAP API Business Hub publishes OpenAPI specs; CAP generates OpenAPI from CDS
- **SOAP**: WSDL defines the contract; SOAMANAGER manages runtime bindings
- **RFC**: SE37 function module signature is the implicit contract; no formal schema enforcement

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Schema format | OData EDMX for SAP-native; OpenAPI for external/third-party |
| Versioning | URL path versioning (/v1/, /v2/); avoid breaking changes in minor versions |
| Deprecation | 6-month notice period; sunset headers; migration guide |
| Error format | RFC 7807 Problem Details or consistent JSON error envelope |
| Rate limiting | Token bucket per client ID; communicate via Retry-After header |

## Operational failure modes

- Breaking change deployed without version bump → consumer parsing failures
- Missing required field in response → downstream system exceptions
- OAuth scope change → 403 errors for existing consumers
- WSDL drift between producer and consumer proxy classes → XML parsing errors

## Monitoring/support model

- API Management analytics for request volume, latency, and error rates
- Consumer-driven contract tests in CI (Pact, Spring Cloud Contract)
- Gateway error logs (/IWFND/ERROR_LOG for OData)
- API Business Hub changelog tracking for released APIs

## Ownership model

- **API producer domain**: owns schema, versioning, deprecation schedule, and documentation
- **Integration platform team**: owns gateway, rate limiting, and security enforcement
- **Consumer domains**: own contract tests and migration planning

## AMS incident patterns

- Consumer reports 400 Bad Request → validate payload against current schema version
- Sudden 403 spike → check OAuth scope or certificate expiry
- Latency regression → review CDS view complexity or database index health
- WSDL mismatch after upgrade → regenerate consumer proxy and redeploy

## AI/agent opportunity

- Auto-generate OpenAPI specs from CDS view metadata
- Detect breaking changes in pull requests via schema diff
- Suggest migration paths for deprecated API versions
- Generate consumer contract tests from API specifications

## Related Atlas pages

- [Event Contracts](/atlas/concepts/event-contracts/)
- [Data Contracts](/atlas/concepts/data-contracts/)
- [Integration Pattern Decision Matrix](/atlas/concepts/integration-pattern-decision-matrix/)
- [OData](/atlas/sap/odata/)
- [REST APIs](/atlas/sap/rest-apis/)
- [SOAP](/atlas/sap/soap/)
- [SAP API Business Hub](https://api.sap.com)

## Source references

- [SAP API Business Hub](https://api.sap.com)
- [SAP Help — OData Services](https://help.sap.com/docs/abap-cloud-development/sap-btp-abap-environment/developing-and-exposing-odata-services)

## Verification limitations

- Content is synthesized from public SAP documentation and API design practice.
- Contract tooling availability varies by SAP release.
- No private implementation details are included.
