---
layout: default
title: "AI Ready Lab — Read-only MCP Workspace"
description: "A hands-on MCP lab using synthetic projects, notes, and tasks to learn tool contracts, resources, transport, authorization, and traces."
permalink: /labs/ai-ready/labs/mcp-readonly/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, lab, mcp, tools, resources, integration]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Read-only MCP Workspace</li></ol>
</nav>

# Lab 01: Read-only MCP Workspace

Build a tiny MCP server around synthetic workspace data. The goal is to understand the protocol and tool boundaries without hiding behind a large business system.

## Scenario

Create local JSON files for:

- projects;
- tasks;
- notes;
- people or teams;
- project status history.

Keep the dataset small enough to inspect by hand.

## Tool set

Start with three narrow read tools:

```text
list_projects(status?)
get_project(project_id)
search_notes(query, project_id?)
```

Add one resource such as:

```text
workspace://projects/{project_id}/summary
```

Do not add write tools yet.

## Good contract shape

A tool should have:

- one clear job;
- typed input;
- bounded output;
- stable IDs;
- explicit not-found and permission errors;
- no secret fields;
- predictable latency.

Avoid a tool such as `do_workspace_action(text)`. It moves every design problem into one vague string and then acts surprised when the model guesses.

## Local first

Run the server locally and connect one MCP client. Test:

1. tool discovery;
2. valid tool call;
3. missing required input;
4. unknown project ID;
5. empty search result;
6. large result that must be bounded;
7. malformed local data;
8. client disconnect or timeout.

## Add authorization as an application boundary

Create two synthetic users:

- user A may read projects `alpha` and `beta`;
- user B may read only `beta`.

The model may ask for `alpha`. The server or gateway decides whether the caller may see it.

Do not let the model infer permissions from text such as “I am an admin”.

## Add trace fields

Record:

```text
trace_id
client_id
user_id
tool_name
sanitized_arguments
authorization_result
result_status
latency_ms
server_version
```

Do not log secrets or full sensitive content only because logging is easy.

## Compare direct tool vs MCP

Implement one capability twice:

```text
application -> direct function -> data
application -> MCP client -> MCP server -> data
```

Write down what MCP adds:

- reusable discovery;
- shared tool/resource contract;
- client portability;
- central observability or policy.

Also write down its cost: another protocol layer, versioning, transport, and operational surface.

## Done when

You can explain:

1. why each tool is narrow;
2. when a resource is better than a tool;
3. where authorization runs;
4. what MCP adds over a direct function;
5. how errors are represented;
6. which metadata appears in traces;
7. why no write tool exists yet.

Next: [RAG with Evals](/labs/ai-ready/labs/rag-evals/) · Read first: [Tools and MCP](/labs/ai-ready/tools-mcp/)
