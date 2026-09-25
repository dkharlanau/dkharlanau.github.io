---
layout: default
title: "AI Ready — Tools and MCP"
description: "A practical guide to function tools, MCP, resource boundaries, authorization, the MCP 2026-07-28 protocol, retries, and write safety."
permalink: /labs/ai-ready/tools-mcp/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
hide_global_cta: true
tags: [ai, mcp, tools, api, authorization, integration]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Tools and MCP</li></ol>
</nav>

# Tools and MCP

A model should not guess a current ticket state, deployment status, inventory balance, or private policy from its training data. It should read that information through a controlled capability.

The practical question is not “Should we use MCP?”. It is **what capability do we need, who is allowed to use it, and which interface keeps that capability easy to control?** Sometimes the answer is a direct function call. Sometimes it is an existing API. MCP becomes useful when the same AI-facing capabilities need a shared protocol and discovery model.

## Start with the capability

For one application and one backend, a direct tool can be the simplest design:

```text
AI application -> typed function/API -> backend
```

If several AI clients need the same tools or resources, repeating the integration in every client becomes harder to maintain:

```text
AI client A ----\
AI client B ----- MCP server -> governed backend capabilities
AI client C ----/
```

MCP standardizes how clients and servers describe and invoke capabilities. It does not replace the backend API, domain rules, identity, authorization, monitoring, or audit controls behind those capabilities.

That distinction is easy to miss. A protocol can make integration portable; it cannot decide who is allowed to close an incident or read another tenant's data.

## What MCP exposes

The three familiar MCP primitives serve different purposes:

| Primitive | Main job | Example |
|---|---|---|
| Tool | Perform a query or controlled action | `get_issue(issue_id)` |
| Resource | Expose addressable context | handbook, schema, reference document |
| Prompt | Offer a reusable interaction template | incident review template |

A clean server does not expose a vague “do anything” tool. It exposes small contracts that describe one capability well.

For example:

```text
get_issue(issue_id)
get_deployment_status(deployment_id)
search_project_notes(query, project_id)
prepare_issue_close(issue_id, resolution_code)
```

These names tell the model and the operator what each tool can do. Typed parameters, stable identifiers, bounded outputs, explicit errors, and a clear read/write classification make the contract easier to test and govern.

## The 2026-07-28 MCP protocol changed the lifecycle

This page was rechecked against the current MCP material on **22 September 2026**. The `2026-07-28` protocol revision uses a stateless protocol lifecycle: the earlier `initialize` / `initialized` handshake and protocol-level `Mcp-Session-Id` were removed. Protocol and client metadata travel with requests, and `server/discover` is available when a client wants server capabilities before making another call.

The important architectural consequence is not that every application must become stateless. Application state can still exist. The change means the **protocol no longer requires a shared session to route a request to the same server instance**. That makes horizontal routing simpler at the protocol layer.

The revision also introduced mechanisms such as Multi Round-Trip Requests for request-scoped server-to-client interaction and cache hints for relevant list/read responses. Older MCP examples may still use the handshake-era lifecycle, so copying an old transport example without checking its protocol version is risky.

Primary reference: [Model Context Protocol — The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/).

## Authorization stays outside the model

The model may choose a tool, but the application or gateway still has to establish:

- the caller's identity;
- whether the caller may invoke the capability;
- which tenant, workspace, repository, account, or object is in scope;
- whether the requested fields may be returned;
- whether approval is required;
- which backend credential is used.

Tool descriptions and client metadata help with coordination. They are not security proof.

This becomes especially important with reusable MCP servers. Reuse is valuable only if the server can preserve the access boundaries of the systems behind it.

## Read and write tools deserve different treatment

Read tools are usually easier to expose safely because a failed call can often be retried without changing business state. Writes are different. A timeout can happen after the backend committed the change but before the caller received the response.

For a meaningful write, we prefer a sequence such as:

```text
request
 -> validate parameters
 -> read current state / preconditions
 -> prepare the intended change
 -> approve when required
 -> execute with duplicate protection
 -> return the committed object ID
 -> record an audit event
```

A prepared-change tool can be useful because it keeps diagnosis and execution separate. For example, an agent may prepare the resolution for an incident without receiving permission to close it.

Idempotency or another duplicate-protection mechanism is part of this design. Retrying a payment, message, deployment, or destructive update after an uncertain network result must not accidentally perform the business action twice.

## When MCP is worth the extra layer

MCP is a good fit when multiple AI clients need the same governed capabilities, when discovery reduces client-specific integration work, or when a shared server gives the organization a clearer place for observability and access control.

A direct tool remains a strong choice when only one application uses the capability and the backend API already gives us the right boundary. Adding MCP only to rename an existing function does not create useful architecture.

We should therefore decide at two levels. First design the capability well. Then decide whether a shared protocol makes that capability easier to reuse and operate.

## What to test

Tool testing should cover more than the happy path. Useful cases include invalid input, unknown objects, forbidden scope, backend timeout, malformed backend output, stale preconditions, duplicate write requests, rejected approval, and hostile instructions returned inside a tool result.

For MCP integrations, test protocol-version compatibility as well. The server and client may support different lifecycle eras, and a transport example that works for a handshake-era client may not describe a `2026-07-28` interaction.

The model can make tool use flexible. The contract around the tool should make the result predictable.

Related: [Read-only MCP Lab](/labs/ai-ready/labs/mcp-readonly/) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Security and Governance](/labs/ai-ready/security-governance/)
