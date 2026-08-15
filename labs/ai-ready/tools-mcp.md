---
layout: default
title: "AI Ready — Tools and MCP"
description: "A practical guide to function tools, MCP, resource boundaries, authorization, stateless MCP 2026-07-28, retries, and write safety."
permalink: /labs/ai-ready/tools-mcp/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, mcp, tools, api, authorization, integration]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Tools and MCP</li></ol>
</nav>

# Tools and MCP

A model should not “know” current stock, create an order, or read a private policy from memory. It should call a controlled capability. The architecture question is whether that capability should be a direct application tool, a normal API integration, or an MCP server.

## Tool first, protocol second

Use a direct function tool when one application needs one controlled capability. Use MCP when several AI clients or agent runtimes benefit from the same discoverable tool/resource contract.

```text
One AI app -> direct function/API -> backend

Several AI clients
      |       |       |
      +---- MCP server ---- governed backend capabilities
```

MCP can reduce duplicate client integrations. It does not remove the need for API design, identity, authorization, monitoring, or business rules.

## MCP 2026-07-28 baseline

Reviewed: **15 Aug 2026**. Current protocol revision used by this page: **2026-07-28**.

The revision moved MCP to a stateless protocol core. Protocol-level `initialize` / `initialized` and session IDs are removed. Requests carry their own protocol and client metadata. Remote HTTP calls also expose method and tool names in headers, which makes gateway routing, rate limiting, and authorization easier to apply without parsing the full body.

The revision also introduced cache hints for list/read responses and Multi Round-Trip Requests for cases where a tool needs more input during an active request. Tasks now live in an extension. Legacy HTTP+SSE and some older core capabilities are on a deprecation path, so implementations should check the current specification before copying older examples.

Primary source: [MCP 2026-07-28 specification release](https://blog.modelcontextprotocol.io/posts/2026-07-28/).

## Tools, resources, prompts

Use the MCP primitives for different jobs:

| Primitive | Use it for | Example |
|---|---|---|
| Tool | Controlled action or query | `get_stock(material, plant)` |
| Resource | Addressable context | material policy, schema, reference document |
| Prompt | Reusable interaction template | diagnostic review template |

Do not expose the same backend operation in five vague tools. Small contracts are easier for the model to select, easier to authorize, and easier to test.

## Design a tool like an API

A good tool has:

- a clear name with one business meaning;
- typed required and optional inputs;
- useful field descriptions;
- bounded output;
- stable identifiers;
- explicit error states;
- no secret fields;
- a known read/write risk class.

Bad:

```text
run_sap_action(text)
```

Better:

```text
get_sales_order(order_id)
get_atp_snapshot(material, plant, requested_date)
prepare_delivery_block(order_id, reason_code)
```

The last tool should prepare a change, not silently execute a high-impact write.

## Authorization is not a model decision

The model may choose a tool. The application or gateway must still decide:

- who the caller is;
- whether the caller may use this tool;
- which plants, sales areas, customers, or fields are allowed;
- whether approval is required;
- which backend credential is used.

Self-reported client metadata and tool descriptions are useful context, not security proof.

## Read and write boundaries

Default to read-only tools. For writes, add more friction on purpose:

1. validate all inputs;
2. check current state and preconditions;
3. return a dry-run or prepared change where practical;
4. require approval for high-impact operations;
5. use request IDs or business keys for duplicate protection;
6. return the committed backend object ID;
7. write an audit event.

Retries are normal. A tool that creates two deliveries because the network timed out after the first commit is not “agentic”; it is simply broken.

## SAP logistics example

For an order-confirmation assistant, expose narrow reads such as:

- `get_sales_order`;
- `get_material_sales_data`;
- `get_atp_snapshot`;
- `get_credit_status`;
- `get_delivery_blocks`;
- `get_recent_integration_errors`.

The agent can investigate across these reads. A later write such as removing a delivery block should live behind a separate permission and approval path.

## When MCP is worth it

Choose MCP when:

- multiple AI clients need the same tools;
- capabilities should be discovered through a shared contract;
- central authorization and observability add value;
- you want a vendor-neutral integration surface.

Stay with direct tools when:

- only one service uses the capability;
- the integration is small and stable;
- adding a protocol layer creates no reuse;
- the backend API already gives the right governance boundary.

## Test cases

- valid read;
- missing required input;
- forbidden plant or customer;
- backend timeout;
- malformed backend response;
- duplicate write request;
- stale precondition;
- user rejects approval;
- tool result contains hostile instructions;
- tool catalog changes between versions.

Related: [SAP Diagnostics MCP Lab](/mcp/sap-diagnostics-mcp/) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Security and Governance](/labs/ai-ready/security-governance/)