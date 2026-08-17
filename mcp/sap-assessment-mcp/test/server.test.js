import test from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const packageRoot = path.resolve(here, '..');
const repoRoot = path.resolve(packageRoot, '../..');

function rpc(requests) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [path.join(packageRoot, 'src/server.js')], {
      cwd: packageRoot,
      env: { ...process.env, SAP_ASSESSMENT_DATA_DIR: repoRoot },
      stdio: ['pipe', 'pipe', 'pipe']
    });
    let stdout = '';
    let stderr = '';
    const timer = setTimeout(() => {
      child.kill('SIGKILL');
      reject(new Error(`MCP test timed out. stderr: ${stderr}`));
    }, 5000);
    child.stdout.on('data', (chunk) => {
      stdout += chunk.toString();
      const lines = stdout.trim().split(/\r?\n/).filter(Boolean);
      if (lines.length >= requests.length) {
        clearTimeout(timer);
        child.kill();
        resolve(lines.slice(0, requests.length).map((line) => JSON.parse(line)));
      }
    });
    child.stderr.on('data', (chunk) => { stderr += chunk.toString(); });
    child.on('error', reject);
    for (const request of requests) child.stdin.write(JSON.stringify(request) + '\n');
  });
}

test('legacy client can list and read assessment resources', async () => {
  const [init, list, read] = await rpc([
    { jsonrpc: '2.0', id: 1, method: 'initialize', params: { protocolVersion: '2025-11-25' } },
    { jsonrpc: '2.0', id: 2, method: 'resources/list', params: {} },
    { jsonrpc: '2.0', id: 3, method: 'resources/read', params: { uri: 'sap-assessment://catalog/tracks' } }
  ]);
  assert.equal(init.result.serverInfo.name, 'sap-assessment-mcp');
  assert.ok(list.result.resources.length > 3);
  assert.ok(JSON.parse(read.result.contents[0].text).total_cases > 0);
});

test('modern discovery and case search work', async () => {
  const meta = {
    'io.modelcontextprotocol/protocolVersion': '2026-07-28',
    'io.modelcontextprotocol/clientInfo': { name: 'test-client', version: '1.0.0' },
    'io.modelcontextprotocol/clientCapabilities': {}
  };
  const [discover, search] = await rpc([
    { jsonrpc: '2.0', id: 1, method: 'server/discover', params: { _meta: meta } },
    { jsonrpc: '2.0', id: 2, method: 'tools/call', params: { name: 'search_assessment_cases', arguments: { track: 'procurement-logistics', limit: 2 }, _meta: meta } }
  ]);
  assert.ok(discover.result.supportedVersions.includes('2026-07-28'));
  const cases = JSON.parse(search.result.content[0].text);
  assert.ok(cases.length > 0);
  assert.ok(cases.every((item) => item.track === 'procurement-logistics'));
});
