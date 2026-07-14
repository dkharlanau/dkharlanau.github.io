#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = process.env.SAP_ATLAS_DATA_DIR || path.resolve(here, '../../..');
const read = (file) => JSON.parse(fs.readFileSync(path.join(root, file), 'utf8'));
const atlas = read('atlas/manifest.json');
const compact = read('ai/atlas-compact-index.json');
const related = read('ai/rag/related.json');
const tools = read('ai/agent-tools.json');
const tokenise = (s='') => s.toLowerCase().match(/[a-z0-9][a-z0-9+-]{2,}/g) || [];
const score = (entry, q) => { const hay = tokenise([entry.title, entry.description, ...(entry.tags||[]), ...(entry.matching_terms||[])].join(' ')); return tokenise(q).reduce((n,t) => n + hay.filter(x => x === t).length, 0); };
const limitation = 'Level 0 public knowledge only. Validate product facts and landscape-specific evidence with an authorized human owner.';
const diagnostic = (entry) => ({id: entry.url.split('/').filter(Boolean).slice(-1)[0], title:entry.title, concise_result:entry.description, canonical_url:entry.url, verification_status:entry.status, last_reviewed:entry.last_reviewed, evidence_references:[entry.url], limitations:[limitation], related_topics:entry.related||[]});
const find = (q, limit=8) => atlas.entries.map(e => ({...e, _score:score(e,q)})).filter(e => e._score).sort((a,b) => b._score || a.title.localeCompare(b.title)).slice(0,limit);
const listTools = () => ['search_diagnostics', 'get_diagnostic', 'find_related_topics', 'get_evidence_checklist', 'get_tables_and_transactions', 'find_agent_tools', 'get_tool_risk_profile', 'build_incident_brief'].map(name => ({ name, description: name.replaceAll('_', ' '), inputSchema: { type: 'object', properties: { query: { type: 'string' }, id: { type: 'string' }, symptom: { type: 'string' } } } }));
function call(name, args = {}) {
  if (name === 'search_diagnostics') return find(args.query || '', args.limit).map(diagnostic);
  if (name === 'get_diagnostic') { const entry = atlas.entries.find(e => e.url.includes(`/${args.id}/`) || e.url === args.id); return entry ? diagnostic(entry) : null; }
  if (name === 'find_related_topics') { const entry = call('get_diagnostic', args); return entry ? entry.related_topics : []; }
  if (name === 'get_evidence_checklist') return { query: args.query, checklist: ['Observed symptom and business impact', 'Authorized document, message, or object identifier', 'Timestamp, system context, and affected volume', 'Exact error or status text and chronology', 'Relevant master-data, configuration, or integration evidence'], limitations: [limitation] };
  if (name === 'get_tables_and_transactions') return { id: args.id, transactions: ['WE02', 'WE05', 'BD87'], tables: ['EDIDC', 'EDIDS', 'EDID4'], limitations: [limitation] };
  if (name === 'find_agent_tools') return tools.tools.filter(t => (!args.access || t.access === args.access) && (!args.query || JSON.stringify(t).toLowerCase().includes(args.query.toLowerCase()))).map(t => ({ id: t.id, name: t.name, canonical_url: tools.canonical_url, verification_status: t.status, last_reviewed: t.verification_date, evidence_references: t.evidence_sources, limitations: ['Registry metadata only; inspect the original project before installation.'], related_topics: t.domains }));
  if (name === 'get_tool_risk_profile') { const tool = tools.tools.find(t => t.id === args.id); return tool ? { ...tool, limitations: ['Registry assessment, not a security approval.'] } : null; }
  if (name === 'build_incident_brief') return { symptom: args.symptom, facts: args.facts || [], hypotheses: find(args.symptom || '', 3).map(e => e.title), evidence_checklist: call('get_evidence_checklist', { query: args.symptom }).checklist, human_approval_boundary: 'No system action, reprocessing, configuration change, or write operation is authorized by this brief.', limitations: [limitation] };
  throw new Error(`Unknown tool: ${name}`);
}
const respond=(id,result)=>process.stdout.write(JSON.stringify({jsonrpc:'2.0',id,result})+'\n');
readline.createInterface({ input: process.stdin }).on('line', (line) => {
  try {
    const message = JSON.parse(line);
    if (message.method === 'initialize') {
      respond(message.id, { protocolVersion: '2025-03-26', capabilities: { tools: {} }, serverInfo: { name: 'sap-diagnostics-mcp', version: '0.1.0' } });
    } else if (message.method === 'tools/list') {
      respond(message.id, { tools: listTools() });
    } else if (message.method === 'tools/call') {
      respond(message.id, { content: [{ type: 'text', text: JSON.stringify(call(message.params.name, message.params.arguments), null, 2) }] });
    }
  } catch (error) {
    process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id: null, error: { code: -32000, message: error.message } }) + '\n');
  }
});
