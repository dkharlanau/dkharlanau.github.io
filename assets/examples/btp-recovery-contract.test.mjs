import test from 'node:test';
import assert from 'node:assert/strict';
import { FakeReceiver, RecoveryCoordinator, teachingApproval } from './btp-recovery-contract.mjs';
const now = Date.UTC(2026, 9, 9);
const op = (overrides = {}) => ({ tenantId: 'DEMO-TENANT-A', requestId: 'DEMO-REQ-1',
  businessPartner: 'DEMO-BP-1', evidenceReference: 'DEMO-EVIDENCE-1', decision: 'ACCEPT', version: 1, ...overrides });
const setup = (options = {}) => {
  const receiver = new FakeReceiver(options);
  return { receiver, service: new RecoveryCoordinator(receiver, { clock: () => now }) };
};
const code = wanted => error => error.code === wanted;

test('a valid accepted operation receives a business receipt', async () => {
  const { receiver, service } = setup(), request = op();
  const result = await service.submit(request, teachingApproval(request));
  assert.equal(result.status, 'CONFIRMED'); assert.equal(result.documentId, 'DEMO-DOC-1'); assert.equal(receiver.writes, 1);
});
test('an absent internal authorization blocks the write', async () => {
  const { receiver, service } = setup();
  await assert.rejects(service.submit(op(), null), code('FORBIDDEN')); assert.equal(receiver.writes, 0);
});
test('a reviewer cannot approve their own action', async () => {
  const { receiver, service } = setup(), request = op();
  await assert.rejects(service.submit(request, teachingApproval(request, { approvedBy: 'demo-reviewer' })), code('FORBIDDEN'));
  assert.equal(receiver.writes, 0);
});
test('an expired approval blocks a new write', async () => {
  const { receiver, service } = setup(), request = op();
  await assert.rejects(service.submit(request, teachingApproval(request, { expiresAt: now })), code('EXPIRED'));
  assert.equal(receiver.writes, 0);
});
test('approval for one tenant cannot authorize another tenant', async () => {
  const { receiver, service } = setup(), request = op();
  await assert.rejects(service.submit(op({ tenantId: 'DEMO-TENANT-B' }), teachingApproval(request)), code('FORBIDDEN'));
  assert.equal(receiver.writes, 0);
});
test('approval is tied to evidence and the actual operation content', async () => {
  const { receiver, service } = setup(), request = op();
  await assert.rejects(service.submit(op({ evidenceReference: 'DEMO-DIFFERENT' }), teachingApproval(request)), code('FORBIDDEN'));
  assert.equal(receiver.writes, 0);
});
test('repeated identical request does not write twice', async () => {
  const { receiver, service } = setup(), request = op(), approval = teachingApproval(request);
  const first = await service.submit(request, approval), again = await service.submit(request, approval);
  assert.equal(first.documentId, again.documentId); assert.equal(receiver.writes, 1);
});
test('reuse of a request key with changed content is a conflict', async () => {
  const { receiver, service } = setup(), first = op(), changed = op({ version: 2 });
  await service.submit(first, teachingApproval(first));
  await assert.rejects(service.submit(changed, teachingApproval(changed)), code('CONFLICT'));
  assert.equal(receiver.writes, 1);
});
test('concurrent identical submissions are registered before awaiting the receiver', async () => {
  const { receiver, service } = setup(), request = op(), approval = teachingApproval(request);
  const results = await Promise.all([service.submit(request, approval), service.submit(request, approval)]);
  assert.equal(receiver.writes, 1); assert.ok(results.every(r => ['CONFIRMED', 'IN_FLIGHT'].includes(r.status)));
});
test('lost reply after commit is UNKNOWN rather than a failure to retry blindly', async () => {
  const { receiver, service } = setup({ mode: 'commit-then-timeout' }), request = op(), approval = teachingApproval(request);
  assert.equal((await service.submit(request, approval)).status, 'UNKNOWN');
  assert.equal((await service.submit(request, approval)).status, 'UNKNOWN'); assert.equal(receiver.writes, 1);
});
test('authoritative reconciliation confirms a lost reply without a new write', async () => {
  const { receiver, service } = setup({ mode: 'commit-then-timeout' }), request = op();
  await service.submit(request, teachingApproval(request));
  const recovered = await service.reconcile(request.tenantId, request.requestId);
  assert.equal(recovered.status, 'CONFIRMED'); assert.equal(recovered.documentId, 'DEMO-DOC-1'); assert.equal(receiver.writes, 1);
});
test('unavailable status lookup creates a manual reconciliation state', async () => {
  const { receiver, service } = setup({ mode: 'commit-then-timeout', lookupAvailable: false }), request = op();
  await service.submit(request, teachingApproval(request));
  assert.equal((await service.reconcile(request.tenantId, request.requestId)).status, 'RECONCILIATION_REQUIRED');
  assert.equal(receiver.writes, 1);
});
test('not found after a timeout does not itself grant permission to repost', async () => {
  const { receiver, service } = setup({ mode: 'timeout-before-commit' }), request = op();
  await service.submit(request, teachingApproval(request));
  assert.equal((await service.reconcile(request.tenantId, request.requestId)).status, 'RECONCILIATION_REQUIRED');
  assert.equal(receiver.writes, 0);
});
test('receiver business rejection is not a transport success', async () => {
  const { receiver, service } = setup({ mode: 'reject' }), request = op();
  assert.equal((await service.submit(request, teachingApproval(request))).status, 'REJECTED'); assert.equal(receiver.writes, 0);
});
test('the same request ID in different tenants has distinct ownership', async () => {
  const { receiver, service } = setup(), a = op(), b = op({ tenantId: 'DEMO-TENANT-B' });
  const x = await service.submit(a, teachingApproval(a)), y = await service.submit(b, teachingApproval(b));
  assert.notEqual(x.documentId, y.documentId); assert.equal(receiver.writes, 2);
});
test('cross-tenant status reads cannot find another tenant ledger entry', async () => {
  const { service } = setup(), request = op(); await service.submit(request, teachingApproval(request));
  await assert.rejects(service.reconcile('DEMO-TENANT-B', request.requestId), code('NOT_FOUND'));
});
test('invalid operation input is blocked before a receiver call', async () => {
  const { receiver, service } = setup();
  await assert.rejects(service.submit(op({ version: -1 }), {}), code('INVALID'));
  await assert.rejects(service.submit(op({ decision: 'ANYTHING' }), {}), code('INVALID'));
  assert.equal(receiver.writes, 0);
});
test('a mismatched receiver receipt is not trusted as confirmation', async () => {
  const request = op(), fake = { apply: async () => ({ tenantId: 'OTHER', documentId: 'DEMO-X' }), lookup: async () => null };
  const service = new RecoveryCoordinator(fake, { clock: () => now });
  assert.equal((await service.submit(request, teachingApproval(request))).status, 'RECONCILIATION_REQUIRED');
});
