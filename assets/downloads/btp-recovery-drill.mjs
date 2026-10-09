/**
 * Original teaching exercise: a receiver commits, but its response is lost.
 * Run: node btp-recovery-drill.mjs
 *
 * No SAP connection, credentials, network requests or chargeable services.
 * This receiver explicitly supports idempotency and lookup by request key.
 * A real ERP API may not. Check its released contract before using this pattern.
 * In-memory maps and a synchronous critical section are NOT durable production
 * storage, database transactions, distributed locks or multi-worker tests.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

class ContractError extends Error {}
class ConflictError extends Error {}
class LostResponse extends Error {}

/** @param {unknown} value @param {string} name */
function identifier(value, name) {
  if (typeof value !== 'string' || !/^[A-Za-z0-9_-]{1,64}$/.test(value)) {
    throw new ContractError(`${name} must be a short non-empty identifier`);
  }
  return value;
}

/** Validate and canonicalize the specific operation's supported input. */
function fingerprint(input) {
  if (!input || typeof input !== 'object' || Array.isArray(input)) {
    throw new ContractError('Payload must be an object');
  }
  const allowed = ['reviewId', 'decision', 'approvedBy'];
  if (Object.keys(input).some(k => !allowed.includes(k))) {
    throw new ContractError('Unexpected payload field');
  }
  const reviewId = identifier(input.reviewId, 'reviewId');
  const approvedBy = identifier(input.approvedBy, 'approvedBy');
  if (!['ACCEPT', 'REJECT'].includes(input.decision)) {
    throw new ContractError('Decision must be ACCEPT or REJECT');
  }
  // A string naming an approver is audit data, NOT proof of authorization.
  // Real identity and approval verification happen outside this simulation.
  return JSON.stringify({ reviewId, decision: input.decision, approvedBy });
}

class Receiver {
  #records = new Map();
  #effects = 0;
  get effects() { return this.#effects; }

  #scope(tenant, requestId) {
    return JSON.stringify([
      identifier(tenant, 'tenant'), identifier(requestId, 'requestId')
    ]);
  }

  /**
   * Simulated atomic record + business-effect commit, within this process only.
   * A production receiver needs its own transactional and idempotency contract.
   */
  execute(tenant, requestId, payload, { loseResponse = false } = {}) {
    const scope = this.#scope(tenant, requestId);
    const digest = fingerprint(payload);
    let record = this.#records.get(scope);
    if (record && record.digest !== digest) {
      throw new ConflictError('Request key reused with different business input');
    }
    if (!record) {
      this.#effects += 1;
      record = Object.freeze({
        digest,
        result: Object.freeze({
          reference: `SIM-${tenant}-${this.#effects}`,
          outcome: 'APPLIED',
          reviewId: payload.reviewId
        })
      });
      this.#records.set(scope, record);
    }
    // Failure is deliberately AFTER the business effect was recorded.
    if (loseResponse) throw new LostResponse('Receiver committed; reply was lost');
    return { ...record.result };
  }

  lookup(tenant, requestId, payload) {
    const scope = this.#scope(tenant, requestId);
    const digest = fingerprint(payload);
    const record = this.#records.get(scope);
    if (!record) return null;
    if (record.digest !== digest) {
      throw new ConflictError('Reconciliation input does not match request key');
    }
    return { ...record.result };
  }
}

class Client {
  constructor(receiver, tenant, requestId, payload) {
    this.receiver = receiver;
    this.tenant = identifier(tenant, 'tenant');
    this.requestId = identifier(requestId, 'requestId');
    fingerprint(payload);
    this.payload = Object.freeze({ ...payload });
    this.state = 'READY';
    this.result = null;
  }

  submit(options = {}) {
    if (this.state === 'CONFIRMED') return this.result;
    if (this.state === 'UNKNOWN') {
      throw new ContractError('Reconcile the unknown result before submitting');
    }
    try {
      this.result = this.receiver.execute(
        this.tenant, this.requestId, this.payload, options
      );
      this.state = 'CONFIRMED';
      return this.result;
    } catch (error) {
      if (error instanceof LostResponse) {
        this.state = 'UNKNOWN';
        return null;
      }
      // Keep errors visible; no automatic retry or invented success.
      throw error;
    }
  }

  reconcile() {
    const found = this.receiver.lookup(this.tenant, this.requestId, this.payload);
    if (found) {
      this.result = found;
      this.state = 'CONFIRMED';
    }
    // In general, 'not found' may mean delayed visibility. Do not change an
    // unknown outcome into a failure or retry until the real contract permits it.
    return found;
  }
}

const input = () => ({ reviewId: 'R-001', decision: 'ACCEPT', approvedBy: 'internal-approver' });

test('Normal response confirms one simulated business effect', () => {
  const receiver = new Receiver();
  const client = new Client(receiver, 'tenantA', 'request1', input());
  assert.equal(client.submit().outcome, 'APPLIED');
  assert.equal(client.state, 'CONFIRMED');
  assert.equal(receiver.effects, 1);
});

test('Lost response leaves an unknown result, not a failed business action', () => {
  const receiver = new Receiver();
  const client = new Client(receiver, 'tenantA', 'request1', input());
  assert.equal(client.submit({ loseResponse: true }), null);
  assert.equal(client.state, 'UNKNOWN');
  assert.equal(receiver.effects, 1);
});

test('Blind resubmission is blocked while the result is unknown', () => {
  const receiver = new Receiver();
  const client = new Client(receiver, 'tenantA', 'request1', input());
  client.submit({ loseResponse: true });
  assert.throws(() => client.submit(), ContractError);
  assert.equal(receiver.effects, 1);
});

test('Reconciliation confirms the committed result without another effect', () => {
  const receiver = new Receiver();
  const client = new Client(receiver, 'tenantA', 'request1', input());
  client.submit({ loseResponse: true });
  assert.equal(client.reconcile().reference, 'SIM-tenantA-1');
  assert.equal(client.state, 'CONFIRMED');
  assert.equal(receiver.effects, 1);
});

test('Same key and business payload return the original receiver result', () => {
  const receiver = new Receiver();
  const first = receiver.execute('tenantA', 'request1', input());
  assert.deepEqual(receiver.execute('tenantA', 'request1', input()), first);
  assert.equal(receiver.effects, 1);
});

test('Same key with changed business input is rejected', () => {
  const receiver = new Receiver();
  receiver.execute('tenantA', 'request1', input());
  assert.throws(() => receiver.execute('tenantA', 'request1', {
    ...input(), decision: 'REJECT'
  }), ConflictError);
  assert.equal(receiver.effects, 1);
});

test('Tenant scopes do not share idempotency records', () => {
  const receiver = new Receiver();
  receiver.execute('tenantA', 'request1', input());
  assert.equal(receiver.lookup('tenantB', 'request1', input()), null);
  assert.equal(receiver.execute('tenantB', 'request1', input()).reference, 'SIM-tenantB-2');
  assert.equal(receiver.effects, 2);
});

test('Missing or invalid identifiers and payloads cannot create an effect', () => {
  const receiver = new Receiver();
  assert.throws(() => receiver.execute('', 'request1', input()), ContractError);
  assert.throws(() => receiver.execute('tenantA', 'request1', {
    ...input(), decision: 'MAYBE'
  }), ContractError);
  assert.throws(() => receiver.execute('tenantA', 'request1', {
    ...input(), bypass: true
  }), ContractError);
  assert.equal(receiver.effects, 0);
});

test('Client double-submit after confirmation reuses the known result', () => {
  const receiver = new Receiver();
  const client = new Client(receiver, 'tenantA', 'request1', input());
  const first = client.submit();
  assert.deepEqual(client.submit(), first);
  assert.equal(receiver.effects, 1);
});

test('Reconciliation with inconsistent payload is not accepted as proof', () => {
  const receiver = new Receiver();
  receiver.execute('tenantA', 'request1', input());
  assert.throws(() => receiver.lookup('tenantA', 'request1', {
    ...input(), reviewId: 'R-999'
  }), ConflictError);
  assert.equal(receiver.effects, 1);
});

test('A temporarily invisible receipt does not turn UNKNOWN into a safe retry', () => {
  const receiver = new Receiver();
  const laggingView = {
    execute: (...args) => receiver.execute(...args),
    lookup: () => null
  };
  const client = new Client(laggingView, 'tenantA', 'request1', input());
  client.submit({ loseResponse: true });
  assert.equal(client.reconcile(), null);
  assert.equal(client.state, 'UNKNOWN');
  assert.throws(() => client.submit(), ContractError);
  assert.equal(receiver.effects, 1);
});

console.log('Teaching boundary: simulated receiver, in-memory state, no SAP deployment.');
console.log('Prove the actual API, identity, persistence and concurrency separately.');
