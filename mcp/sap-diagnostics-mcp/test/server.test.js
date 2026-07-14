import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
test('server advertises MCP tools', () => { const r=spawnSync('node',['src/server.js'],{input:'{"jsonrpc":"2.0","id":1,"method":"tools/list"}\n',encoding:'utf8'}); assert.equal(r.status,0); assert.match(r.stdout,/search_diagnostics/); });
