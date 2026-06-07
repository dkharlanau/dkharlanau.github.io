---
layout: default
title: "MCP and Enterprise Tool Use"
description: "Anthropic's Model Context Protocol as a standard for connecting AI agents to enterprise tools and data sources."
type: research_brief
status: draft
date: 2026-06-07
updated: 2026-06-07
robots: noindex,follow
sitemap: false
evidence_level: high
topics:
  - mcp
  - model-context-protocol
  - ai-agents
  - enterprise-tools
source_count: 5
related_atlas:
  - /atlas/ai-operations/ai-agent-for-sap-support/
related_research:
  - /research/watchlists/agentic-ams/
  - /research/comparisons/joule-sap-business-ai-vs-general-enterprise-agents/
next_actions:
  - Evaluate MCP SDK for connecting agents to SAP APIs
  - Track OpenAI and Google MCP support announcements
  - Assess MCP security model for production enterprise use
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/research/">Research</a></li>
    <li aria-current="page">MCP and Enterprise Tool Use</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Research Brief</p>
    <h1>MCP and Enterprise Tool Use</h1>
    <p class="note-subtitle">Anthropic's Model Context Protocol as a standard for connecting AI agents to enterprise tools.</p>
  </header>

  <div class="note-body">

## Research question

Is the Model Context Protocol (MCP) mature enough to standardize how enterprise AI agents connect to tools, databases, and APIs?

## Short answer

MCP is the most promising emerging standard for agent-tool integration. Released by Anthropic in November 2024 and now supported by OpenAI, Google, and a growing ecosystem, MCP provides a client-server architecture where agents discover and call tools through a standardized protocol. For enterprise use, MCP is ready for pilot projects but requires careful security review: it exposes tools to LLMs, which creates new attack surfaces (prompt injection, unauthorized tool calls). The protocol itself is sound; the risk lies in implementation.

## What changed

- **MCP announced by Anthropic (Nov 2024).** Anthropic introduced MCP as "a universal standard for AI data integration," with official SDKs for Python, TypeScript, Java, and C#. [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- **MCP specification stabilized (Mar 2025).** The MCP specification reached a stable 2025-03-26 revision, defining core protocol, transports (stdio, HTTP/SSE), and capabilities (tools, resources, prompts). [Model Context Protocol: Specification](https://modelcontextprotocol.io/specification/2025-03-26)
- **OpenAI adopted MCP (Mar 2025).** OpenAI added MCP support to its Agents SDK and Responses API, signaling industry-wide adoption beyond Anthropic. [OpenAI: Introducing the Responses API](https://community.openai.com/t/introducing-the-responses-api/1140929)
- **Google added MCP support (Apr 2025).** Demis Hassabis announced MCP support for Gemini models, expanding the protocol to Google's ecosystem. [Hassabis post on X](https://x.com/demishassabis/status/1910107859041271977)
- **MCP security research emerged.** Academic papers identified MCP security threats including unauthorized tool invocation, prompt injection via tool responses, and data exfiltration. [Hou et al.: MCP Landscape, Security Threats, and Future Research](https://arxiv.org/abs/2503.23278)

## Evidence

| Signal | Source | Confidence |
|--------|--------|------------|
| MCP announced by Anthropic | Anthropic official blog | High |
| MCP specification stable | modelcontextprotocol.io | High |
| OpenAI adopted MCP | OpenAI community forum | High |
| Google Gemini MCP support | Demis Hassabis (Google CEO) post | High |
| MCP security threats identified | arXiv security paper | High |

## Why it matters

Today, connecting an AI agent to enterprise tools requires custom integrations for each tool: one for SAP OData, one for ServiceNow API, one for Jira, one for email. MCP replaces this fragmentation with a single protocol. An MCP server exposes tools (e.g., "query SAP sales order," "create ServiceNow ticket"), and any MCP-compatible agent can discover and call them. This is the "USB-C for AI applications" metaphor that MCP's creators use. For enterprises with multiple agent platforms, MCP reduces integration duplication.

## Practical implications

- **Tool standardization.** Instead of building custom connectors for each agent platform, build one MCP server per tool. SAP OData APIs, ServiceNow tables, and internal databases can all expose MCP servers.
- **Agent portability.** An agent built with Anthropic's SDK, OpenAI's SDK, or a framework like LangChain can use the same MCP servers. This reduces vendor lock-in at the tool layer.
- **Discovery and documentation.** MCP servers advertise their tools with names, descriptions, and schemas. Agents can discover available tools at runtime, making agent behavior more transparent and maintainable.
- **Security boundaries.** MCP does not define enterprise security policies; it defines the protocol. You must add authentication, authorization, audit logging, and input validation around MCP servers. Treat MCP servers as API endpoints with the same security rigor.
- **SAP integration potential.** An MCP server for SAP could expose tools like: `get_sales_order_status`, `check_material_stock`, `list_open_invoices`. The agent calls these tools through MCP instead of generating raw SQL or RFC calls. This is safer because the tool logic is controlled, not generated.

## Risks and unknowns

- **Prompt injection via tool responses.** If an MCP tool returns data that includes malicious instructions, the LLM may follow them. Sanitize tool outputs and use prompt hardening.
- **Unauthorized tool chaining.** An agent with access to multiple MCP tools may chain them in unintended ways (e.g., read customer data → send email → delete record). Define tool-level permissions and workflow boundaries.
- **Enterprise authentication.** MCP's core spec does not mandate OAuth, SAML, or enterprise SSO. Implementing secure authentication for MCP servers in production requires additional work.
- **Observability gaps.** MCP tool calls need logging, tracing, and cost attribution. Standard observability tools (OpenTelemetry, Datadog) do not yet have native MCP integrations.
- **Governance immaturity.** There is no enterprise MCP governance framework yet. Each organization must define its own policies for which tools to expose, which agents can access them, and what audit trails are required.

## Related Atlas links

- [AI Agent for SAP Support](/atlas/ai-operations/ai-agent-for-sap-support/)

## Next actions

- [ ] Evaluate the MCP Python or TypeScript SDK for a pilot project connecting an agent to one SAP API.
- [ ] Track OpenAI and Google MCP support announcements for your agent platform.
- [ ] Assess MCP security: implement authentication, sanitize tool outputs, and log all tool calls.
- [ ] Define a policy for which enterprise tools may expose MCP servers and which agents may access them.

## Sources

1. [Introducing the Model Context Protocol — Anthropic](https://www.anthropic.com/news/model-context-protocol)
   - type: official
   - accessed: 2026-06-07
   - confidence: high
   - used for: MCP announcement, protocol purpose, SDK availability

2. [Model Context Protocol Specification — modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-03-26)
   - type: official
   - accessed: 2026-06-07
   - confidence: high
   - used for: Protocol architecture, transports, capabilities

3. [OpenAI: Introducing the Responses API](https://community.openai.com/t/introducing-the-responses-api/1140929)
   - type: official
   - accessed: 2026-06-07
   - confidence: high
   - used for: OpenAI MCP adoption, Agents SDK integration

4. [Demis Hassabis post on X about MCP support for Gemini](https://x.com/demishassabis/status/1910107859041271977)
   - type: official
   - accessed: 2026-06-07
   - confidence: high
   - used for: Google Gemini MCP support confirmation

5. [Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions — Hou et al., arXiv 2025](https://arxiv.org/abs/2503.23278)
   - type: paper
   - accessed: 2026-06-07
   - confidence: high
   - used for: MCP security analysis, threat taxonomy, mitigation strategies

  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
