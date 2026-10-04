---
layout: default
title: "AI Ready — Tools and MCP"
description: "A practical guide to function tools, MCP, resource boundaries, authorization, the MCP 2026-07-28 protocol, retries, and write safety."
permalink: /labs/ai-ready/tools-mcp/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-10-04
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


## Design the tool surface for the agent

MCP solves a protocol problem. It does not automatically make a large tool catalog easy for a model to use.

A common failure mode is to expose hundreds of tools at once and place every schema into the model context. The model then has to spend attention on tools that are irrelevant to the current task, infer prerequisites between calls, and combine separate application models by itself.

For large enterprise environments, a better pattern is **progressive tool discovery**:

```text
user goal
 -> search / discover the relevant capability
 -> return a small tool set and required prerequisites
 -> execute the reads
 -> keep large intermediate data outside the model context
 -> load only the evidence needed for the next decision
 -> propose or execute a controlled final action
```

This changes the design target. The interface is no longer only an API for developers. It is also a task surface for an agent.

A good agent-facing capability should make five things easy to understand:

1. **Purpose** — what business job the tool performs.
2. **Prerequisites** — which identifier, connection, scope, or earlier lookup is required.
3. **Authority** — whether the tool reads, prepares, approves, or commits a change.
4. **Result shape** — whether the model receives compact evidence, a stable object ID, a page of results, or a file handle for larger data.
5. **Next useful step** — which follow-up tools are valid when the result is incomplete.

This matters because enterprise tasks are usually cross-system. An incident may begin in a chat message, continue through monitoring data, require a code or configuration check, and end with a ticket update or controlled change. If every server describes only itself, the model must reconstruct the dependency graph on every run.

### Context is a budget

Tool definitions, skills, retrieved data, conversation history, and instructions all compete for the same model context. More context is not automatically better.

Use progressive disclosure where practical:

- expose only the tool family relevant to the current task;
- retrieve full schemas after the capability is selected;
- return stable IDs instead of repeating large objects;
- use pagination, files, or remote processing for large datasets;
- summarize intermediate results only after deterministic filtering;
- keep reusable dependency knowledge outside the prompt when the platform can discover it at runtime.

This is not only a token-cost optimization. Smaller relevant context reduces tool confusion and makes the execution path easier to inspect.

### Example: SAP incident investigation

Consider a customer report: *“The outbound delivery is not progressing.”*

A weak agent surface may expose hundreds of Sales, EWM, TM, integration, and support tools and expect the model to choose correctly.

A stronger surface starts from the task:

```text
investigate outbound delivery
 -> identify sales / delivery object
 -> read document and status flow
 -> if warehouse-owned: inspect EWM state
 -> if message-owned: inspect IDoc / AIF / queue evidence
 -> if transport-owned: inspect TM execution state
 -> compare the first wrong state
 -> prepare the next action or human handoff
```

The agent does not need every SAP capability in context. It needs the smallest relevant map of tools, ownership boundaries, and prerequisites for this case.

The same rule applies to procurement, GR/IR, master-data replication, and integration recovery: **discover from the business task, not from the complete technical catalog**.

### Human UI still has a job

Agent-friendly design does not make every dashboard obsolete. Humans still need visual monitoring, pattern recognition, approval, exception review, audit, and operational control.

The architectural shift is narrower: do not force an agent to imitate a human clicking through a visual interface when the underlying capability can be exposed as a governed, typed, discoverable operation.

### Case evidence

A 2026 Composio talk demonstrates this pattern with a cross-application debugging task. The agent first searches for the capabilities needed for Slack, Sentry, and Datadog, receives the relevant tools and dependency guidance, then executes the investigation. A second example keeps a large intermediate user-ID set outside the model context and processes it through a remote workbench before returning the useful result.

Current Composio documentation describes Tool Router / session search as a way to find matching tools and workflow guidance, and Remote Workbench as a persistent sandbox for processing large remote files or repeated tool executions without pushing all data into chat context.

Sources: [Composio — tool search API](https://docs.composio.dev/reference/api-reference/tool-router/postToolRouterSessionBySessionIdSearch) · [Composio — Remote Workbench](https://docs.composio.dev/toolkits/meta-tools/remote_workbench) · [Anthropic — Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) · [Video case](https://youtu.be/YiFqcu9YA38?si=hOlfGA_uO1mAUsLr)

## What to test

Tool testing should cover more than the happy path. Useful cases include invalid input, unknown objects, forbidden scope, backend timeout, malformed backend output, stale preconditions, duplicate write requests, rejected approval, and hostile instructions returned inside a tool result.

For MCP integrations, test protocol-version compatibility as well. The server and client may support different lifecycle eras, and a transport example that works for a handshake-era client may not describe a `2026-07-28` interaction.

The model can make tool use flexible. The contract around the tool should make the result predictable.

Related: [Read-only MCP Lab](/labs/ai-ready/labs/mcp-readonly/) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Security and Governance](/labs/ai-ready/security-governance/)
