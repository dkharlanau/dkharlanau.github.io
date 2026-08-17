# SAP Assessment MCP

Local-first, credential-free, read-only MCP server for the public SAP Lead assessment dataset.

The server reads the committed assessment manifest and JSONL case sets from a local checkout. It exposes the same source material through MCP resources and deterministic tools. It does not call an LLM, connect to SAP, write files, store attempts, or send telemetry.

## Install and run

Requirements: Node.js 20 or newer.

From this directory:

```sh
npm install .
npm test
npm run smoke
node src/server.js
```

For an MCP client, copy `examples/mcp.json` and replace the two absolute paths. `SAP_ASSESSMENT_DATA_DIR` must point to the repository root that contains `labs/assessment/data/case-sets.json`.

The configuration file uses a common stdio shape. MCP clients still differ in configuration details, so check the current documentation of the selected client.

## Resources

The server supports `resources/list`, `resources/read`, and `resources/templates/list`.

Catalog resources:

- `sap-assessment://catalog/case-sets`
- `sap-assessment://catalog/case-schema`
- `sap-assessment://catalog/tracks`

Case resources use stable assessment IDs:

- `sap-assessment://case/ASSESS-SALES-001`

Track resources are available through the resource template:

- `sap-assessment://track/sales`
- `sap-assessment://track/procurement-logistics`
- `sap-assessment://track/integration-architecture`
- `sap-assessment://track/ai-data`

## Tools

- `search_assessment_cases` — search by text, track, and reasoning level.
- `get_assessment_case` — return one full case by ID.
- `list_assessment_tracks` — return counts, level coverage, and study routes.
- `build_practice_set` — create a deterministic filtered practice set.
- `build_mock_set` — create a balanced deterministic set across tracks.
- `get_study_sources` — return the human-readable site routes linked to a case.

## Recommended practice loop

1. Use `search_assessment_cases` or `build_practice_set` to select a case.
2. Read the case prompt without showing `expected_points` to the candidate.
3. Ask the candidate to answer aloud or in writing.
4. Reveal expected points, follow-up questions, and red flags.
5. Use `get_study_sources` to open only the pages that address the weak area.
6. Repeat with a related case.

The MCP server does not grade free-form answers. Scoring remains a separate assessment contract and should remain visible to the human reviewer.

## Protocol compatibility

The stdio server supports the modern MCP `2026-07-28` discovery model through `server/discover` and per-request protocol metadata. It also supports the legacy `initialize` flow used by 2025-era clients. This is intentional while client implementations migrate at different speeds.

## Boundaries

Everything exposed by this server is public training material. It is not a SAP connector, an official SAP knowledge source, or an assessment authority. Release-sensitive product facts still require primary-source verification, and final evaluation remains human-owned.
