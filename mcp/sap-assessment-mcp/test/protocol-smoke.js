import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const packageRoot = path.resolve(here, '..');
const repoRoot = path.resolve(packageRoot, '../..');
const child = spawn(process.execPath, [path.join(packageRoot, 'src/server.js')], {
  cwd: packageRoot,
  env: { ...process.env, SAP_ASSESSMENT_DATA_DIR: repoRoot },
  stdio: ['pipe', 'pipe', 'pipe']
});

const requests = [
  { jsonrpc: '2.0', id: 1, method: 'initialize', params: { protocolVersion: '2025-11-25' } },
  { jsonrpc: '2.0', id: 2, method: 'resources/list', params: {} },
  { jsonrpc: '2.0', id: 3, method: 'resources/read', params: { uri: 'sap-assessment://catalog/case-sets' } },
  { jsonrpc: '2.0', id: 4, method: 'tools/call', params: { name: 'search_assessment_cases', arguments: { track: 'sales', limit: 1 } } },
  { jsonrpc: '2.0', id: 5, method: 'server/discover', params: { _meta: { 'io.modelcontextprotocol/protocolVersion': '2026-07-28', 'io.modelcontextprotocol/clientInfo': { name: 'sap-assessment-smoke', version: '1.0.0' }, 'io.modelcontextprotocol/clientCapabilities': {} } } }
];

let stdout = '';
let stderr = '';
child.stdout.on('data', (chunk) => { stdout += chunk.toString(); });
child.stderr.on('data', (chunk) => { stderr += chunk.toString(); });
for (const request of requests) child.stdin.write(JSON.stringify(request) + '\n');

const timeout = setTimeout(() => {
  child.kill('SIGKILL');
  throw new Error(`MCP smoke test timed out. stderr: ${stderr}`);
}, 5000);

const poll = setInterval(() => {
  const lines = stdout.trim().split(/\r?\n/).filter(Boolean);
  if (lines.length < requests.length) return;
  clearInterval(poll);
  clearTimeout(timeout);
  child.kill();
  const responses = lines.slice(0, requests.length).map((line) => JSON.parse(line));
  assert.equal(responses[0].result.serverInfo.name, 'sap-assessment-mcp');
  assert.ok(responses[1].result.resources.some((item) => item.uri === 'sap-assessment://catalog/case-sets'));
  assert.equal(JSON.parse(responses[2].result.contents[0].text).id, 'sap-lead-assessment-case-sets');
  assert.equal(JSON.parse(responses[3].result.content[0].text)[0].track, 'sales');
  assert.ok(responses[4].result.supportedVersions.includes('2026-07-28'));
  process.stdout.write('SAP Assessment MCP smoke test passed.\n');
}, 25);
