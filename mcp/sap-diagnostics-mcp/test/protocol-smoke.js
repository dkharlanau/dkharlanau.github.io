import {spawnSync} from 'node:child_process';
const input=['{"jsonrpc":"2.0","id":1,"method":"initialize"}','{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"search_diagnostics","arguments":{"query":"IDoc status"}}}'].join('\n')+'\n';
const r=spawnSync('node',['src/server.js'],{input,encoding:'utf8'}); if(r.status || !r.stdout.includes('sap-diagnostics-mcp') || !r.stdout.includes('SAP IDoc')) process.exit(1); console.log('MCP stdio smoke passed');
