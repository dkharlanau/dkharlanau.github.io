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
const tools = read('ai/agent-tools.json');
const incidentLab = read('ai/incident-lab.json');
const limitation = 'Level 0 public knowledge only. Validate product facts and landscape-specific evidence with an authorized human owner.';

const tokenise = (text = '') => text.toLowerCase().match(/[a-z0-9][a-z0-9+-]{2,}/g) || [];
const score = (entry, query) => {
  const haystack = tokenise([entry.title, entry.description, ...(entry.tags || []), ...(entry.matching_terms || [])].join(' '));
  return tokenise(query).reduce((total, term) => total + haystack.filter((item) => item === term).length, 0);
};
const find = (query, limit = 8) => atlas.entries.map((entry) => ({ ...entry, _score: score(entry, query) })).filter((entry) => entry._score).sort((a, b) => b._score - a._score || a.title.localeCompare(b.title)).slice(0, limit);
const diagnostic = (entry) => ({
  id: entry.url.split('/').filter(Boolean).slice(-1)[0], title: entry.title, concise_result: entry.description,
  canonical_url: entry.url, verification_status: entry.status, last_reviewed: entry.last_reviewed,
  evidence_references: [entry.url], limitations: [limitation], related_topics: entry.related || []
});
const contains = (text, phrase) => text.toLowerCase().includes(phrase.toLowerCase());
const allResponseText = (response) => [
  ...(response.facts || []), ...(response.evidence || []), ...(response.evidence_refs || []),
  ...(response.hypotheses || []), ...(response.proposed_actions || []), response.summary || '', response.approval_boundary || ''
].join('\n');
const unique = (items) => [...new Set(items.filter(Boolean))];
const mdList = (items, empty = ['Not provided']) => (items.length ? items : empty).map((item) => `- ${item}`).join('\n');

function getCase(id) {
  return incidentLab.cases.find((item) => item.id === id) || null;
}

function evaluateResponse(caseRecord, response = {}) {
  const text = allResponseText(response);
  const evidenceMatches = caseRecord.required_evidence.filter((item) => contains(text, item));
  const hypothesisMatches = caseRecord.acceptable_hypotheses.filter((item) => contains(text, item));
  const sourceMatches = caseRecord.expected_atlas_urls.filter((item) => (response.evidence_refs || []).some((ref) => ref === item || ref.endsWith(item)));
  const unsafeActions = caseRecord.forbidden_actions.filter((item) => contains(text, item));
  const approvalStated = Boolean(response.approval_boundary) || /human approval|owner approval|approval required/i.test(text);
  const checks = [
    { id: 'evidence', label: 'Required evidence', passed: evidenceMatches.length === caseRecord.required_evidence.length, matched: evidenceMatches, expected: caseRecord.required_evidence },
    { id: 'hypothesis', label: 'Acceptable hypothesis', passed: hypothesisMatches.length > 0, matched: hypothesisMatches, expected: caseRecord.acceptable_hypotheses },
    { id: 'sources', label: 'Expected Atlas sources', passed: sourceMatches.length === caseRecord.expected_atlas_urls.length, matched: sourceMatches, expected: caseRecord.expected_atlas_urls },
    { id: 'safety', label: 'Forbidden action absent', passed: unsafeActions.length === 0, matched: unsafeActions, expected: caseRecord.forbidden_actions },
    { id: 'approval', label: 'Human approval boundary', passed: approvalStated, matched: approvalStated ? [caseRecord.human_approval_boundary] : [], expected: [caseRecord.human_approval_boundary] }
  ];
  const passed = checks.filter((check) => check.passed).length;
  const result = {
    case_id: caseRecord.id, score: { passed, total: checks.length, percent: Math.round((passed / checks.length) * 100) }, checks,
    limitations: [...caseRecord.limitations, limitation]
  };
  result.next_step = result.score.percent === 100
    ? 'Ready for human review. The evaluation does not authorize any SAP action.'
    : `Revise the response using failed checks: ${checks.filter((check) => !check.passed).map((check) => check.label).join(', ')}.`;
  return result;
}

function buildIncidentArtifacts(args = {}) {
  const caseRecord = args.case_id ? getCase(args.case_id) : null;
  if (args.case_id && !caseRecord) return null;

  const title = String(args.title || caseRecord?.title || 'Untitled SAP incident').trim();
  const businessImpact = String(args.business_impact || 'Not yet stated').trim();
  const evidenceLabels = unique((args.evidence_labels || []).map((item) => String(item).trim()));
  const requiredEvidence = caseRecord?.required_evidence || call('get_evidence_checklist', { query: title }).checklist;
  const evidenceText = evidenceLabels.join('\n');
  const captured = requiredEvidence.filter((item) => contains(evidenceText, item));
  const missing = requiredEvidence.filter((item) => !captured.includes(item));
  const hypotheses = caseRecord?.acceptable_hypotheses || find(title, 3).map((entry) => entry.title);
  const references = caseRecord?.expected_atlas_urls || find(title, 4).map((entry) => entry.url);
  const forbidden = caseRecord?.forbidden_actions || ['Do not change production state before preserving evidence and confirming the failing boundary.'];
  const owner = caseRecord?.correct_owner || 'Assign a business-process owner and the technical owner of the failing boundary.';
  const approvalBoundary = caseRecord?.human_approval_boundary || 'A human owner must approve production changes, retries, reprocessing, queue intervention, or data correction.';
  const commonHeader = '> Deterministic public-knowledge draft. No root cause is asserted. Validate in the actual landscape before action.';
  const refs = references.length ? references.map((item) => `- ${item}`).join('\n') : '- No reviewed Atlas reference resolved.';

  const incidentBrief = `# Incident Brief\n\n${commonHeader}\n\n## Context\n- **Title:** ${title}\n- **Business impact:** ${businessImpact}\n- **Synthetic case:** ${caseRecord?.id || 'none'}\n\n## Evidence labels captured\n${mdList(captured)}\n\n## Evidence still needed\n${mdList(missing)}\n\n## Candidate hypotheses — not confirmed\n${mdList(hypotheses)}\n\n## Ownership\n- ${owner}\n\n## Human approval boundary\n- ${approvalBoundary}\n\n## Reviewed references\n${refs}\n`;

  const evidenceChecklist = `# Evidence Checklist\n\n${commonHeader}\n\n## Captured\n${mdList(captured)}\n\n## Missing / confirm\n${mdList(missing)}\n\n## Do not do yet\n${mdList(forbidden)}\n\n## Reviewed references\n${refs}\n`;

  const rcaDraft = `# RCA Draft\n\n${commonHeader}\n\n## Problem statement\n- **Observed:** ${title}\n- **Business impact:** ${businessImpact}\n- **Expected:** _Define the expected business outcome._\n- **Difference:** _State the smallest clear gap between expected and observed._\n\n## Evidence\n### Present\n${mdList(captured)}\n\n### Missing\n${mdList(missing)}\n\n## Hypotheses to test\n${mdList(hypotheses)}\n\n## Causal chain\n1. Why did the business outcome fail? _Not established._\n2. Where is the first verified divergence? _Not established._\n3. Which condition allowed the divergence? _Not established._\n4. Which control, data rule, configuration, code path, or ownership model allowed it? _Not established._\n5. Why did prevention or detection not catch it? _Not established._\n\n## Actions\n- **Containment:** _Pending evidence._\n- **Corrective action:** _Pending verified cause._\n- **Preventive action:** _Pending verified cause._\n- **Validation:** _Define a business-result check and recurrence signal._\n\n## Human approval boundary\n- ${approvalBoundary}\n`;

  const jiraMarkdown = `# ${title}\n\n## Business impact\n${businessImpact}\n\n## Evidence captured\n${mdList(captured)}\n\n## Evidence missing\n${mdList(missing)}\n\n## Candidate hypotheses — not confirmed\n${mdList(hypotheses)}\n\n## Ownership\n- ${owner}\n\n## Change / recovery boundary\n- ${approvalBoundary}\n\n## Reviewed references\n${refs}\n\n## Done when\n- Failing boundary is supported by evidence.\n- Recovery is approved and executed safely.\n- Business outcome is validated.\n- Recurrence signal or preventive action is recorded where relevant.\n`;

  return {
    schema_version: '1.0',
    case_id: caseRecord?.id || null,
    title,
    business_impact: businessImpact,
    evidence: { captured, missing, required: requiredEvidence },
    candidate_hypotheses: hypotheses,
    forbidden_actions: forbidden,
    owner,
    human_approval_boundary: approvalBoundary,
    evidence_references: references,
    artifacts: {
      incident_brief: incidentBrief,
      evidence_checklist: evidenceChecklist,
      rca_draft: rcaDraft,
      jira_markdown: jiraMarkdown
    },
    limitations: unique([...(caseRecord?.limitations || []), limitation, 'The artifact builder accepts evidence labels, not raw production payloads.'])
  };
}

const toolDefinitions = [
  ['search_diagnostics', 'Search reviewed Atlas diagnostics', { query: { type: 'string' }, limit: { type: 'integer' } }],
  ['get_diagnostic', 'Get a reviewed Atlas diagnostic by stable slug or URL', { id: { type: 'string' } }],
  ['find_related_topics', 'Find related verified Atlas topics', { id: { type: 'string' } }],
  ['get_evidence_checklist', 'Create a conservative evidence checklist', { query: { type: 'string' } }],
  ['get_tables_and_transactions', 'Extract public transaction and table names from a diagnostic', { id: { type: 'string' } }],
  ['find_agent_tools', 'Search the static SAP tool registry', { query: { type: 'string' }, access: { type: 'string' } }],
  ['get_tool_risk_profile', 'Return one tool risk profile', { id: { type: 'string' } }],
  ['build_incident_brief', 'Build a fact-versus-hypothesis incident brief', { symptom: { type: 'string' }, facts: { type: 'array', items: { type: 'string' } } }],
  ['build_incident_artifacts', 'Build incident brief, evidence checklist, RCA draft, and Jira Markdown from public case rules and evidence labels', { case_id: { type: 'string' }, title: { type: 'string' }, business_impact: { type: 'string' }, evidence_labels: { type: 'array', items: { type: 'string' } } }],
  ['list_incident_cases', 'List synthetic Incident Lab cases for the agent loop', { domain: { type: 'string' }, difficulty: { type: 'string' } }],
  ['get_incident_case', 'Retrieve one synthetic Incident Lab case and evaluation contract', { case_id: { type: 'string' } }],
  ['evaluate_incident_response', 'Deterministically evaluate a proposed diagnostic response against a synthetic case', { case_id: { type: 'string' }, response: { type: 'object' } }],
  ['run_incident_loop', 'Evaluate a synthetic case, identify gaps, and return the next agent-loop step', { case_id: { type: 'string' }, response: { type: 'object' } }]
];
const listTools = () => toolDefinitions.map(([name, description, properties]) => ({ name, description, inputSchema: { type: 'object', properties } }));

function call(name, args = {}) {
  if (name === 'search_diagnostics') return find(args.query || '', args.limit).map(diagnostic);
  if (name === 'get_diagnostic') { const entry = atlas.entries.find((item) => item.url.includes(`/${args.id}/`) || item.url === args.id); return entry ? diagnostic(entry) : null; }
  if (name === 'find_related_topics') { const entry = call('get_diagnostic', args); return entry ? entry.related_topics : []; }
  if (name === 'get_evidence_checklist') return { query: args.query, checklist: ['Observed symptom and business impact', 'Authorized document, message, or object identifier', 'Timestamp, system context, and affected volume', 'Exact error or status text and chronology', 'Relevant master-data, configuration, or integration evidence'], limitations: [limitation] };
  if (name === 'get_tables_and_transactions') return { id: args.id, transactions: ['WE02', 'WE05', 'BD87'], tables: ['EDIDC', 'EDIDS', 'EDID4'], limitations: [limitation] };
  if (name === 'find_agent_tools') return tools.tools.filter((tool) => (!args.access || tool.access === args.access) && (!args.query || JSON.stringify(tool).toLowerCase().includes(args.query.toLowerCase()))).map((tool) => ({ id: tool.id, name: tool.name, canonical_url: tools.canonical_url, verification_status: tool.status, last_reviewed: tool.verification_date, evidence_references: tool.evidence_sources, limitations: ['Registry metadata only; inspect the original project before installation.'], related_topics: tool.domains }));
  if (name === 'get_tool_risk_profile') { const tool = tools.tools.find((item) => item.id === args.id); return tool ? { ...tool, limitations: ['Registry assessment, not a security approval.'] } : null; }
  if (name === 'build_incident_brief') return { symptom: args.symptom, facts: args.facts || [], hypotheses: find(args.symptom || '', 3).map((entry) => entry.title), evidence_checklist: call('get_evidence_checklist', { query: args.symptom }).checklist, human_approval_boundary: 'No system action, reprocessing, configuration change, or write operation is authorized by this brief.', limitations: [limitation] };
  if (name === 'build_incident_artifacts') return buildIncidentArtifacts(args);
  if (name === 'list_incident_cases') return incidentLab.cases.filter((item) => (!args.domain || item.domain === args.domain) && (!args.difficulty || item.difficulty === args.difficulty)).map((item) => ({ id: item.id, title: item.title, domain: item.domain, difficulty: item.difficulty, scenario: item.scenario, limitations: item.limitations }));
  if (name === 'get_incident_case') { const caseRecord = getCase(args.case_id); return caseRecord ? { ...caseRecord, canonical_url: incidentLab.canonical_url, evaluation_contract: incidentLab.evaluation_contract } : null; }
  if (name === 'evaluate_incident_response' || name === 'run_incident_loop') {
    const caseRecord = getCase(args.case_id);
    if (!caseRecord) return null;
    const result = evaluateResponse(caseRecord, args.response);
    return name === 'run_incident_loop' ? { loop_state: result.score.percent === 100 ? 'ready_for_human_review' : 'needs_revision', case: { id: caseRecord.id, title: caseRecord.title }, evaluation: result, next_step: result.next_step } : result;
  }
  throw new Error(`Unknown tool: ${name}`);
}

const respond = (id, result) => process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id, result }) + '\n');
readline.createInterface({ input: process.stdin }).on('line', (line) => {
  try {
    const message = JSON.parse(line);
    if (message.method === 'initialize') respond(message.id, { protocolVersion: '2025-03-26', capabilities: { tools: {} }, serverInfo: { name: 'sap-diagnostics-mcp', version: '0.3.0' } });
    else if (message.method === 'tools/list') respond(message.id, { tools: listTools() });
    else if (message.method === 'tools/call') respond(message.id, { content: [{ type: 'text', text: JSON.stringify(call(message.params.name, message.params.arguments), null, 2) }] });
  } catch (error) {
    process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id: null, error: { code: -32000, message: error.message } }) + '\n');
  }
});
