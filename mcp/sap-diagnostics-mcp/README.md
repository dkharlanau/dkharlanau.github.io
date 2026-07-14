# SAP Diagnostics MCP

Local-first, credential-free, read-only MCP server for the public SAP Atlas. It uses stdio and reads committed static artifacts from a local checkout. Version 1 never contacts SAP, fetches remote URLs, stores credentials, writes files, or sends telemetry.

## Install and run

From this directory, run `npm install .` (there are no runtime dependencies), then either run `node src/server.js` or point an MCP client at the server. Copy `examples/mcp.json` and replace both absolute paths. The shown configuration is a generic stdio shape; verify the exact configuration syntax against your selected client’s current official documentation.

`SAP_ATLAS_DATA_DIR` must point to a checkout containing `atlas/manifest.json`, `ai/atlas-compact-index.json`, `ai/rag/related.json`, and `ai/agent-tools.json`.

## Tools

`search_diagnostics`, `get_diagnostic`, `find_related_topics`, `get_evidence_checklist`, `get_tables_and_transactions`, `find_agent_tools`, `get_tool_risk_profile`, and `build_incident_brief` provide deterministic local retrieval. Responses preserve URLs, review state, limitations, and public evidence references.

The synthetic Incident Lab adds `list_incident_cases`, `get_incident_case`, `evaluate_incident_response`, and `run_incident_loop`. The loop checks a proposed response against a public-safe fixture for evidence coverage, Atlas source use, unsafe actions, and a stated human approval boundary. It does not generate an answer, call an LLM, or authorize a SAP action.

## Test

Run `npm test` and `npm run smoke`. The smoke test is a stdio JSON-RPC protocol check; use the current MCP Inspector separately when validating a client integration.

## Boundaries

Every result is Level 0 public knowledge. It is not a SAP connector, production approval, or source of landscape-specific fact. A human owner must approve any later access to SAP or write-capable tool.
