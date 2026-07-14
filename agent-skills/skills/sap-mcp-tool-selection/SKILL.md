---
name: sap-mcp-tool-selection
description: Select SAP MCP tools using access, ownership, and production-risk boundaries.
---
# SAP MCP Tool Selection

Trigger when choosing, connecting, or enabling an MCP server for SAP work.

Inputs: task, client, data sensitivity, target environment, required access, and owner approval.

Workflow: prefer Level 0 Atlas content; query `/ai/agent-tools.json`; inspect maintainer, license, transport, tools, authentication, and risks; enable the smallest suitable set.

Safety: default deny. Never enable write-capable tools or submit credentials without explicit human approval. Reject missing license, unclear ownership, or undocumented production APIs.

Output: selected tool or rejection, rationale, access level, prerequisites, and approval boundary.

Atlas: `/agent-tools/security/`, `/agent-tools/evaluate/`.

## Purpose
Choose an SAP MCP tool with explicit risk boundaries.
## Use when
Use when selecting or enabling an MCP server.
## Do not use when
Do not use to bypass owner approval.
## Required inputs
Task, target, client, access need, and approval status.
## Workflow
Prefer static knowledge, evaluate registry metadata, then minimize tools.
## Decision rules
Default deny and require approval for credentials or writes.
## Output format
Selection or rejection, rationale, risks, and approval boundary.
## Quality gates
No unlicensed, unclear, or broad-production tool enabled.
## References
See `references/` and linked Agent Tools pages.
