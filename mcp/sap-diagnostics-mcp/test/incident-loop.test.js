import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';

function call(tool, args) {
  const request = JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name: tool, arguments: args } }) + '\n';
  const result = spawnSync('node', ['src/server.js'], { input: request, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  return JSON.parse(JSON.parse(result.stdout).result.content[0].text);
}

test('agent loop flags incomplete evidence and returns a revision step', () => {
  const result = call('run_incident_loop', { case_id: 'idoc-status-51-vendor-master', response: { hypotheses: ['application posting error'] } });
  assert.equal(result.loop_state, 'needs_revision');
  assert.ok(result.evaluation.checks.some((check) => check.id === 'evidence' && !check.passed));
});

test('agent loop accepts a complete safe synthetic response', () => {
  const result = call('run_incident_loop', {
    case_id: 'idoc-status-51-vendor-master',
    response: {
      evidence: ['IDoc number', 'status history', 'error text', 'message type', 'partner', 'timestamp'],
      evidence_refs: ['/atlas/diagnostics/sap-idoc-status-diagnostics/', '/atlas/diagnostics/sap-vendor-master-replication-diagnostics/'],
      hypotheses: ['application posting error'],
      proposed_actions: ['Collect the application log before deciding on a controlled next action.'],
      approval_boundary: 'Human approval is required before any reprocessing.'
    }
  });
  assert.equal(result.loop_state, 'ready_for_human_review');
  assert.equal(result.evaluation.score.percent, 100);
});

test('agent loop rejects an explicitly forbidden operational action', () => {
  const result = call('evaluate_incident_response', {
    case_id: 'idoc-status-51-vendor-master',
    response: { proposed_actions: ['Reprocess the IDoc before the cause is confirmed.'] }
  });
  assert.equal(result.checks.find((check) => check.id === 'safety').passed, false);
});
