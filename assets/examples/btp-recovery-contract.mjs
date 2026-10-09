/**
 * Teaching model only. In-memory state, fake receiver, no HTTP or SAP calls.
 * The caller supplies trusted server-side approval evidence in this exercise.
 * Production code must load and verify that evidence itself, authenticate the
 * caller, persist the ledger durably, and verify the real receiver contract.
 */
import { createHash } from 'node:crypto';

export class ContractError extends Error {
  constructor(code, message) { super(message); this.name = 'ContractError'; this.code = code; }
}
const fail = (code, message) => { throw new ContractError(code, message); };
const required = (value, name) => {
  if (typeof value !== 'string' || !value.trim() || value.length > 160) {
    fail('INVALID', `${name} must be a nonempty string of at most 160 characters`);
  }
  return value;
};
const keyOf = (tenantId, requestId) => JSON.stringify([
  required(tenantId, 'tenantId'), required(requestId, 'requestId')
]);
function normalize(operation) {
  if (!operation || typeof operation !== 'object') fail('INVALID', 'Missing operation');
  const result = {};
  for (const field of ['tenantId', 'requestId', 'businessPartner', 'evidenceReference']) {
    result[field] = required(operation[field], field);
  }
  if (operation.decision !== 'ACCEPT') fail('INVALID', 'Only the accepted teaching action is supported');
  if (!Number.isSafeInteger(operation.version) || operation.version < 1) fail('INVALID', 'Invalid version');
  return { ...result, decision: 'ACCEPT', version: operation.version };
}
const digest = operation => createHash('sha256').update(JSON.stringify(normalize(operation))).digest('hex');
function assertApproval(operation, approval, now) {
  if (!Number.isFinite(now)) fail('INVALID', 'Invalid clock');
  if (!approval || approval.status !== 'AUTHORIZED') fail('FORBIDDEN', 'Internal authorization required');
  if (approval.tenantId !== operation.tenantId || approval.requestId !== operation.requestId ||
      approval.operationDigest !== digest(operation)) fail('FORBIDDEN', 'Approval does not cover this operation');
  required(approval.reviewedBy, 'reviewedBy'); required(approval.approvedBy, 'approvedBy');
  if (approval.reviewedBy === approval.approvedBy) fail('FORBIDDEN', 'Independent approval required');
  if (!Number.isFinite(approval.expiresAt) || approval.expiresAt <= now) fail('EXPIRED', 'Approval expired');
}

export function teachingApproval(operation, overrides = {}) {
  // Fixture factory, NOT a signature, authentication service or ERP approval API.
  return {
    status: 'AUTHORIZED', tenantId: operation.tenantId, requestId: operation.requestId,
    operationDigest: digest(operation), reviewedBy: 'demo-reviewer',
    approvedBy: 'demo-approver', expiresAt: Date.UTC(2030, 0, 1), ...overrides
  };
}

export class FakeReceiver {
  #records = new Map();
  constructor({ mode = 'normal', lookupAvailable = true } = {}) {
    if (!['normal', 'commit-then-timeout', 'timeout-before-commit', 'reject'].includes(mode)) {
      fail('INVALID', 'Unsupported fake receiver mode');
    }
    this.mode = mode; this.lookupAvailable = lookupAvailable; this.writes = 0;
  }
  async apply(operation) {
    const normalized = normalize(operation), key = keyOf(normalized.tenantId, normalized.requestId);
    const operationDigest = digest(normalized), existing = this.#records.get(key);
    if (existing) {
      if (existing.operationDigest !== operationDigest) fail('CONFLICT', 'Request key reused for different content');
      return { ...existing };
    }
    if (this.mode === 'reject') fail('BUSINESS_REJECTED', 'Fake receiver rejected the operation');
    if (this.mode === 'timeout-before-commit') fail('TIMEOUT', 'No confirmed result');
    const record = { tenantId: normalized.tenantId, requestId: normalized.requestId,
      businessPartner: normalized.businessPartner, operationDigest,
      documentId: `DEMO-DOC-${++this.writes}` };
    this.#records.set(key, record);
    if (this.mode === 'commit-then-timeout') fail('TIMEOUT', 'Reply lost after commit');
    return { ...record };
  }
  async lookup(tenantId, requestId) {
    if (!this.lookupAvailable) fail('LOOKUP_UNAVAILABLE', 'No authoritative lookup available');
    const record = this.#records.get(keyOf(tenantId, requestId));
    return record ? { ...record } : null;
  }
}

export class RecoveryCoordinator {
  #ledger = new Map();
  constructor(receiver, { clock = () => Date.now() } = {}) {
    if (!receiver || typeof receiver.apply !== 'function' || typeof receiver.lookup !== 'function') {
      fail('INVALID', 'Receiver apply and lookup methods required');
    }
    this.receiver = receiver; this.clock = clock;
  }
  async submit(operation, approval) {
    const normalized = normalize(operation), key = keyOf(normalized.tenantId, normalized.requestId);
    const operationDigest = digest(normalized);
    assertApproval(normalized, approval, this.clock());
    const previous = this.#ledger.get(key);
    if (previous) {
      if (previous.operationDigest !== operationDigest) fail('CONFLICT', 'Existing request content differs');
      return { ...previous }; // No automatic resubmission of UNKNOWN or IN_FLIGHT.
    }
    // Registered synchronously before the first await: single-process example only.
    const attempt = { tenantId: normalized.tenantId, requestId: normalized.requestId,
      operationDigest, status: 'IN_FLIGHT' };
    this.#ledger.set(key, attempt);
    try {
      const receipt = await this.receiver.apply(normalized);
      if (!receipt || receipt.tenantId !== normalized.tenantId || receipt.requestId !== normalized.requestId ||
          receipt.operationDigest !== operationDigest || !receipt.documentId) {
        attempt.status = 'RECONCILIATION_REQUIRED';
      } else { attempt.status = 'CONFIRMED'; attempt.documentId = receipt.documentId; }
    } catch (error) {
      // Only a receiver's explicit no-commit rejection is treated as REJECTED.
      attempt.status = error.code === 'BUSINESS_REJECTED' ? 'REJECTED' : 'UNKNOWN';
    }
    return { ...attempt };
  }
  async reconcile(tenantId, requestId) {
    const attempt = this.#ledger.get(keyOf(tenantId, requestId));
    if (!attempt) fail('NOT_FOUND', 'No request for this tenant');
    if (attempt.status === 'CONFIRMED' || attempt.status === 'REJECTED') return { ...attempt };
    try {
      const receipt = await this.receiver.lookup(tenantId, requestId);
      if (receipt && receipt.tenantId === tenantId && receipt.requestId === requestId &&
          receipt.operationDigest === attempt.operationDigest && receipt.documentId) {
        attempt.status = 'CONFIRMED'; attempt.documentId = receipt.documentId;
      } else { attempt.status = 'RECONCILIATION_REQUIRED'; }
    } catch { attempt.status = 'RECONCILIATION_REQUIRED'; }
    // Missing or unavailable lookup never authorizes a blind retry.
    return { ...attempt };
  }
}
