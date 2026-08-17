#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = process.env.SAP_ASSESSMENT_DATA_DIR || path.resolve(here, '../../..');
const serverInfo = { name: 'sap-assessment-mcp', version: '0.1.0' };
const modernVersion = '2026-07-28';
const legacyVersions = ['2025-11-25', '2025-06-18', '2025-03-26'];
const limitation = 'Public assessment material only. Validate release-sensitive SAP facts against primary sources and keep final assessment judgment human-owned.';

const resolveRepoPath = (value) => {
  const relative = value.replace(/^https?:\/\/[^/]+/, '').replace(/^\//, '');
  const target = path.resolve(root, relative);
  const base = path.resolve(root) + path.sep;
  if (target !== path.resolve(root) && !target.startsWith(base)) throw new Error('Path escapes repository root');
  return target;
};
const readText = (repoPath) => fs.readFileSync(resolveRepoPath(repoPath), 'utf8');
const readJson = (repoPath) => JSON.parse(readText(repoPath));
const readJsonl = (repoPath) => readText(repoPath).split(/\r?\n/).filter(Boolean).map((line, index) => {
  try { return JSON.parse(line); } catch (error) { throw new Error(`Invalid JSONL in ${repoPath} at line ${index + 1}: ${error.message}`); }
});

const caseSets = readJson('/labs/assessment/data/case-sets.json');
const caseSchema = readJson('/labs/assessment/data/case-schema.json');
const cases = caseSets.sets.flatMap((set) => readJsonl(set.url).map((item) => ({ ...item, case_set: set.id })));
const byId = new Map(cases.map((item) => [item.id, item]));
const tracks = [...new Set(cases.map((item) => item.track))].sort();
const levels = ['explain', 'trace', 'diagnose', 'design', 'challenge'];

const tokens = (value = '') => value.toLowerCase().match(/[a-z0-9][a-z0-9+.\/-]{1,}/g) || [];
const scoreCase = (item, query) => {
  if (!query) return 1;
  const haystack = tokens([item.id, item.track, item.level, item.title, item.prompt, ...(item.expected_points || []), ...(item.red_flags || [])].join(' '));
  return tokens(query).reduce((score, token) => score + haystack.filter((candidate) => candidate === token).length, 0);
};
const publicCase = (item) => ({ ...item, canonical_url: `/labs/assessment/#${item.id.toLowerCase()}`, limitations: [limitation] });
const trackSummary = () => tracks.map((track) => {
  const items = cases.filter((item) => item.track === track);
  return {
    track,
    count: items.length,
    levels: levels.filter((level) => items.some((item) => item.level === level)),
    source_routes: [...new Set(items.flatMap((item) => item.human_refs || []))].sort()
  };
});

const resources = [
  {
    uri: 'sap-assessment://catalog/case-sets',
    name: 'Case set manifest',
    title: 'SAP Lead Assessment Case Sets',
    description: 'Manifest of active assessment case files and coverage.',
    mimeType: 'application/json'
  },
  {
    uri: 'sap-assessment://catalog/case-schema',
    name: 'Case schema',
    title: 'SAP Lead Assessment Case Schema',
    description: 'JSON Schema used by every assessment case.',
    mimeType: 'application/schema+json'
  },
  {
    uri: 'sap-assessment://catalog/tracks',
    name: 'Assessment tracks',
    title: 'SAP Lead Assessment Tracks',
    description: 'Derived track, level, case-count, and study-route map.',
    mimeType: 'application/json'
  },
  ...cases.map((item) => ({
    uri: `sap-assessment://case/${item.id}`,
    name: item.id,
    title: item.title,
    description: `${item.track} · ${item.level} · ${item.case_set}`,
    mimeType: 'application/json'
  }))
];

const resourceTemplates = [
  {
    uriTemplate: 'sap-assessment://case/{case_id}',
    name: 'Assessment case',
    title: 'Assessment case by ID',
    description: 'Read one case using an ID such as ASSESS-SALES-001.',
    mimeType: 'application/json'
  },
  {
    uriTemplate: 'sap-assessment://track/{track}',
    name: 'Assessment track',
    title: 'Assessment track cases',
    description: 'Read all cases for one assessment track.',
    mimeType: 'application/json'
  }
];

const toolDefinitions = [
  ['search_assessment_cases', 'Search SAP Lead assessment cases by text, track, and reasoning level.', {
    query: { type: 'string' },
    track: { type: 'string', enum: tracks },
    level: { type: 'string', enum: levels },
    limit: { type: 'integer', minimum: 1, maximum: 20 }
  }],
  ['get_assessment_case', 'Get one assessment case with rubric points, follow-ups, red flags, and study routes.', {
    case_id: { type: 'string' }
  }],
  ['list_assessment_tracks', 'List tracks, reasoning-level coverage, case counts, and source routes.', {}],
  ['build_practice_set', 'Build a deterministic practice set from track and reasoning-level filters.', {
    track: { type: 'string', enum: tracks },
    level: { type: 'string', enum: levels },
    size: { type: 'integer', minimum: 1, maximum: 12 }
  }],
  ['build_mock_set', 'Build a balanced deterministic mock set across assessment tracks.', {
    size: { type: 'integer', minimum: 4, maximum: 12 }
  }],
  ['get_study_sources', 'Return the human-readable site routes linked to a case.', {
    case_id: { type: 'string' }
  }]
];
const listTools = () => toolDefinitions.map(([name, description, properties]) => ({
  name,
  description,
  inputSchema: { type: 'object', properties, additionalProperties: false }
}));

function searchCases(args = {}) {
  const limit = Math.max(1, Math.min(Number(args.limit || 8), 20));
  return cases
    .filter((item) => !args.track || item.track === args.track)
    .filter((item) => !args.level || item.level === args.level)
    .map((item) => ({ item, score: scoreCase(item, args.query || '') }))
    .filter(({ score }) => score > 0)
    .sort((a, b) => b.score - a.score || a.item.id.localeCompare(b.item.id))
    .slice(0, limit)
    .map(({ item }) => ({
      id: item.id,
      title: item.title,
      track: item.track,
      level: item.level,
      prompt: item.prompt,
      case_set: item.case_set,
      human_refs: item.human_refs,
      limitations: [limitation]
    }));
}

function buildPracticeSet(args = {}) {
  const size = Math.max(1, Math.min(Number(args.size || 5), 12));
  return cases
    .filter((item) => !args.track || item.track === args.track)
    .filter((item) => !args.level || item.level === args.level)
    .sort((a, b) => a.id.localeCompare(b.id))
    .slice(0, size)
    .map(publicCase);
}

function buildMockSet(args = {}) {
  const size = Math.max(4, Math.min(Number(args.size || 8), 12));
  const buckets = Object.fromEntries(tracks.map((track) => [track, cases.filter((item) => item.track === track).sort((a, b) => {
    const levelDelta = levels.indexOf(a.level) - levels.indexOf(b.level);
    return levelDelta || a.id.localeCompare(b.id);
  })]));
  const selected = [];
  let round = 0;
  while (selected.length < size) {
    let added = false;
    for (const track of tracks) {
      if (selected.length >= size) break;
      const candidate = buckets[track][round];
      if (candidate) { selected.push(candidate); added = true; }
    }
    if (!added) break;
    round += 1;
  }
  return { cases: selected.map(publicCase), limitations: [limitation] };
}

function callTool(name, args = {}) {
  if (name === 'search_assessment_cases') return searchCases(args);
  if (name === 'get_assessment_case') return byId.has(args.case_id) ? publicCase(byId.get(args.case_id)) : null;
  if (name === 'list_assessment_tracks') return { tracks: trackSummary(), total_cases: cases.length, manifest_total: caseSets.total_cases, limitations: [limitation] };
  if (name === 'build_practice_set') return { cases: buildPracticeSet(args), limitations: [limitation] };
  if (name === 'build_mock_set') return buildMockSet(args);
  if (name === 'get_study_sources') {
    const item = byId.get(args.case_id);
    return item ? { case_id: item.id, routes: item.human_refs || [], graph_refs: item.graph_refs || [], limitations: [limitation] } : null;
  }
  throw Object.assign(new Error(`Unknown tool: ${name}`), { code: -32602 });
}

function readResource(uri) {
  if (uri === 'sap-assessment://catalog/case-sets') return caseSets;
  if (uri === 'sap-assessment://catalog/case-schema') return caseSchema;
  if (uri === 'sap-assessment://catalog/tracks') return { tracks: trackSummary(), total_cases: cases.length, manifest_total: caseSets.total_cases };
  const caseMatch = uri.match(/^sap-assessment:\/\/case\/(ASSESS-[A-Z]+-[0-9]{3})$/);
  if (caseMatch && byId.has(caseMatch[1])) return publicCase(byId.get(caseMatch[1]));
  const trackMatch = uri.match(/^sap-assessment:\/\/track\/([a-z0-9-]+)$/);
  if (trackMatch && tracks.includes(trackMatch[1])) return cases.filter((item) => item.track === trackMatch[1]).map(publicCase);
  const error = new Error(`Resource not found: ${uri}`);
  error.code = -32002;
  throw error;
}

const isModern = (message) => message?.params?._meta?.['io.modelcontextprotocol/protocolVersion'] === modernVersion;
const modernMeta = { 'io.modelcontextprotocol/serverInfo': serverInfo };
const resultEnvelope = (payload, modern = false, cache = false) => modern
  ? { resultType: 'complete', ...payload, ...(cache ? { ttlMs: 300000, cacheScope: 'public' } : {}), _meta: modernMeta }
  : payload;
const respond = (id, result) => process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id, result }) + '\n');
const fail = (id, code, message, data) => process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id, error: { code, message, ...(data ? { data } : {}) } }) + '\n');

readline.createInterface({ input: process.stdin }).on('line', (line) => {
  let message;
  try {
    message = JSON.parse(line);
    const modern = isModern(message) || message.method === 'server/discover';
    if (message.method === 'server/discover') {
      respond(message.id, {
        resultType: 'complete',
        supportedVersions: [modernVersion],
        capabilities: { tools: {}, resources: {} },
        instructions: 'Use resources for stable assessment context and tools for filtered case selection. Human-readable study routes are returned as site paths.',
        ttlMs: 300000,
        cacheScope: 'public',
        _meta: modernMeta
      });
    } else if (message.method === 'initialize') {
      const requested = message.params?.protocolVersion;
      const protocolVersion = legacyVersions.includes(requested) ? requested : legacyVersions[0];
      respond(message.id, { protocolVersion, capabilities: { tools: {}, resources: {} }, serverInfo });
    } else if (message.method === 'tools/list') {
      respond(message.id, resultEnvelope({ tools: listTools() }, modern, true));
    } else if (message.method === 'tools/call') {
      const output = callTool(message.params?.name, message.params?.arguments || {});
      respond(message.id, resultEnvelope({ content: [{ type: 'text', text: JSON.stringify(output, null, 2) }] }, modern));
    } else if (message.method === 'resources/list') {
      respond(message.id, resultEnvelope({ resources }, modern, true));
    } else if (message.method === 'resources/templates/list') {
      respond(message.id, resultEnvelope({ resourceTemplates }, modern, true));
    } else if (message.method === 'resources/read') {
      const uri = message.params?.uri;
      const data = readResource(uri);
      respond(message.id, resultEnvelope({ contents: [{ uri, mimeType: 'application/json', text: JSON.stringify(data, null, 2) }] }, modern, true));
    } else if (message.method?.startsWith('notifications/')) {
      return;
    } else {
      fail(message.id ?? null, -32601, `Method not found: ${message.method}`);
    }
  } catch (error) {
    fail(message?.id ?? null, error.code || -32603, error.message);
  }
});
