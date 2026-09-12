import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';

function call(tool, args) {
  const request = JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name: tool, arguments: args } }) + '\n';
  const result = spawnSync('node', ['src/server.js'], { input: request, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  return JSON.parse(JSON.parse(result.stdout).result.content[0].text);
}

test('artifact builder produces four bounded markdown artifacts for a synthetic case', () => {
  const result = call('build_incident_artifacts', {
    case_id: 'idoc-status-51-vendor-master',
    title: 'Inbound vendor IDoc failed',
    business_impact: 'Vendor updates are delayed',
    evidence_labels: ['IDoc number', 'status history', 'error text']
  });
  assert.equal(result.case_id, 'idoc-status-51-vendor-master');
  assert.ok(result.evidence.missing.includes('message type'));
  assert.ok(result.artifacts.incident_brief.startsWith('# Incident Brief'));
  assert.ok(result.artifacts.evidence_checklist.startsWith('# Evidence Checklist'));
  assert.ok(result.artifacts.rca_draft.startsWith('# RCA Draft'));
  assert.ok(result.artifacts.jira_markdown.startsWith('# Inbound vendor IDoc failed'));
  assert.match(result.human_approval_boundary, /human|owner/i);
  assert.ok(result.evidence_references.length >= 1);
});

test('artifact builder accepts a generic incident without inventing a root cause', () => {
  const result = call('build_incident_artifacts', {
    title: 'Recurring SAP support incident',
    business_impact: 'Manual recovery repeats every week',
    evidence_labels: ['Observed symptom and business impact']
  });
  assert.equal(result.case_id, null);
  assert.match(result.artifacts.rca_draft, /Not established/);
  assert.match(result.limitations.join(' '), /evidence labels/i);
});
