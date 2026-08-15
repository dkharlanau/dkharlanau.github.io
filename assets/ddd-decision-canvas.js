(() => {
  'use strict';

  const STORAGE_KEY = 'ddd-acting-systems-decision-canvas-v03';

  const byId = (id) => document.getElementById(id);
  const form = byId('ddd-decision-form');
  const output = byId('ddd-decision-json');
  const status = byId('ddd-decision-status');
  const postureName = byId('ddd-posture-name');
  const postureReason = byId('ddd-posture-reason');
  const examplePicker = byId('ddd-example-picker');

  if (!form || !output) return;

  const value = (name) => {
    const field = form.elements.namedItem(name);
    return field ? String(field.value || '').trim() : '';
  };

  const checked = (name) => {
    const field = form.elements.namedItem(name);
    return Boolean(field && field.checked);
  };

  const lines = (name) => value(name)
    .split('\n')
    .map((item) => item.trim())
    .filter(Boolean);

  const slugify = (text) => text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80) || 'decision';

  function postureFromEconomics() {
    const ambiguity = value('ambiguity');
    const costOfError = value('cost_of_error');
    const reversibility = value('reversibility_score');
    const evidenceQuality = value('evidence_quality');
    const createsCommitment = checked('creates_business_effect');

    if (ambiguity === 'low') {
      return {
        id: 'prefer-deterministic',
        label: 'Prefer deterministic logic',
        reason: 'Ambiguity is low. A rule, decision table, workflow, or domain service may solve the problem with less uncertainty and governance overhead.'
      };
    }

    if (costOfError === 'high' && reversibility === 'low') {
      return {
        id: 'advisory-ai',
        label: 'Advisory AI',
        reason: 'Error cost is high and the outcome is hard to reverse. Keep final commitment authority with a human or deterministic policy.'
      };
    }

    if (createsCommitment && (costOfError === 'high' || evidenceQuality === 'low')) {
      return {
        id: 'prepare-with-review',
        label: 'Prepare with review',
        reason: 'The decision may create a business commitment, while risk or evidence quality still justifies an explicit review before execution.'
      };
    }

    if (ambiguity === 'high' && reversibility === 'high' && evidenceQuality !== 'low' && costOfError !== 'high') {
      return {
        id: 'bounded-execution-candidate',
        label: 'Bounded execution candidate',
        reason: 'Judgment is useful, evidence is usable, and the action is reversible. Start lower and promote only after evaluation proves the bounded action is reliable.'
      };
    }

    return {
      id: 'prepare-with-review',
      label: 'Prepare with review',
      reason: 'There is useful judgment, but the safest default is to let AI prepare a structured action while authority remains explicit.'
    };
  }

  function buildDecisionCard() {
    const posture = postureFromEconomics();
    const outcome = value('business_outcome');
    const decisionId = value('decision_id') || slugify(outcome);

    return {
      schema_version: '0.3.0',
      decision_id: decisionId,
      business_outcome: outcome,
      home_context: value('home_context'),
      decision_type: value('decision_type'),
      truth: {
        authoritative_inputs: lines('authoritative_inputs'),
        contextual_inputs: lines('contextual_inputs'),
        freshness_rule: value('freshness_rule'),
        invariants: lines('invariants')
      },
      judgment: {
        allowed: lines('judgment_allowed'),
        forbidden: lines('judgment_forbidden'),
        design_posture: posture.id,
        design_posture_reason: posture.reason
      },
      authority: {
        autonomy_level: value('autonomy_level'),
        scope: value('authority_scope'),
        value_limit: value('value_limit'),
        frequency_limit: value('frequency_limit'),
        time_window: value('time_window'),
        reversibility: value('authority_reversibility'),
        approval: value('approval'),
        delegation_rule: value('delegation_rule') || 'Delegation may preserve or reduce authority but never amplify it.'
      },
      commitment: {
        creates_business_effect: checked('creates_business_effect'),
        commitment_type: value('commitment_type'),
        owner: value('commitment_owner'),
        domain_command: value('domain_command'),
        transactional_system: value('transactional_system'),
        preconditions: lines('preconditions'),
        idempotency_or_duplicate_control: value('idempotency'),
        reversal_or_compensation: value('reversal_or_compensation'),
        resulting_event: value('resulting_event')
      },
      economics: {
        ambiguity: value('ambiguity'),
        volume: value('volume'),
        cost_of_delay: value('cost_of_delay'),
        cost_of_error: value('cost_of_error'),
        reversibility: value('reversibility_score'),
        evidence_quality: value('evidence_quality'),
        human_review_cost: value('human_review_cost')
      },
      evidence: {
        retain: lines('evidence_retain'),
        outcome_observation: value('outcome_observation'),
        sensitive_data_notes: value('sensitive_data_notes')
      },
      evaluation: {
        cases: lines('evaluation_cases'),
        promotion_gate: value('promotion_gate'),
        runtime_must_not_change: lines('runtime_must_not_change')
      },
      notes: value('notes')
    };
  }

  function requiredGaps(card) {
    const gaps = [];
    if (!card.business_outcome) gaps.push('business outcome');
    if (!card.home_context) gaps.push('home context');
    if (!card.truth.authoritative_inputs.length) gaps.push('authoritative inputs');
    if (!card.truth.freshness_rule) gaps.push('freshness rule');
    if (!card.truth.invariants.length) gaps.push('invariants');
    if (!card.authority.scope) gaps.push('authority scope');
    if (card.commitment.creates_business_effect) {
      if (!card.commitment.owner) gaps.push('commitment owner');
      if (!card.commitment.domain_command) gaps.push('domain command');
      if (!card.commitment.transactional_system) gaps.push('transactional system');
      if (!card.commitment.reversal_or_compensation) gaps.push('reversal or compensation');
    }
    if (!card.evidence.retain.length) gaps.push('evidence to retain');
    if (!card.evaluation.cases.length) gaps.push('evaluation cases');
    return gaps;
  }

  function render(save = true) {
    const card = buildDecisionCard();
    const posture = postureFromEconomics();
    const gaps = requiredGaps(card);

    output.textContent = JSON.stringify(card, null, 2);
    postureName.textContent = posture.label;
    postureReason.textContent = posture.reason;
    status.textContent = gaps.length
      ? `Draft · ${gaps.length} design gap${gaps.length === 1 ? '' : 's'}: ${gaps.join(', ')}`
      : 'Draft · core fields complete';

    if (save) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(card));
      } catch (_) {
        // Local storage is optional. The canvas still works without it.
      }
    }
  }

  function setField(name, rawValue) {
    const field = form.elements.namedItem(name);
    if (!field) return;
    if (field.type === 'checkbox') {
      field.checked = Boolean(rawValue);
    } else if (Array.isArray(rawValue)) {
      field.value = rawValue.join('\n');
    } else if (rawValue !== undefined && rawValue !== null) {
      field.value = String(rawValue);
    }
  }

  function loadCard(card) {
    if (!card) return;
    setField('decision_id', card.decision_id);
    setField('business_outcome', card.business_outcome);
    setField('home_context', card.home_context);
    setField('decision_type', card.decision_type);

    const truth = card.truth || {};
    setField('authoritative_inputs', truth.authoritative_inputs);
    setField('contextual_inputs', truth.contextual_inputs);
    setField('freshness_rule', truth.freshness_rule);
    setField('invariants', truth.invariants);

    const judgment = card.judgment || {};
    setField('judgment_allowed', judgment.allowed);
    setField('judgment_forbidden', judgment.forbidden);

    const authority = card.authority || {};
    setField('autonomy_level', authority.autonomy_level);
    setField('authority_scope', authority.scope);
    setField('value_limit', authority.value_limit);
    setField('frequency_limit', authority.frequency_limit);
    setField('time_window', authority.time_window);
    setField('authority_reversibility', authority.reversibility);
    setField('approval', authority.approval);
    setField('delegation_rule', authority.delegation_rule);

    const commitment = card.commitment || {};
    setField('creates_business_effect', commitment.creates_business_effect);
    setField('commitment_type', commitment.commitment_type);
    setField('commitment_owner', commitment.owner);
    setField('domain_command', commitment.domain_command);
    setField('transactional_system', commitment.transactional_system);
    setField('preconditions', commitment.preconditions);
    setField('idempotency', commitment.idempotency_or_duplicate_control);
    setField('reversal_or_compensation', commitment.reversal_or_compensation);
    setField('resulting_event', commitment.resulting_event);

    const economics = card.economics || {};
    setField('ambiguity', economics.ambiguity);
    setField('volume', economics.volume);
    setField('cost_of_delay', economics.cost_of_delay);
    setField('cost_of_error', economics.cost_of_error);
    setField('reversibility_score', economics.reversibility);
    setField('evidence_quality', economics.evidence_quality);
    setField('human_review_cost', economics.human_review_cost);

    const evidence = card.evidence || {};
    setField('evidence_retain', evidence.retain);
    setField('outcome_observation', evidence.outcome_observation);
    setField('sensitive_data_notes', evidence.sensitive_data_notes);

    const evaluation = card.evaluation || {};
    setField('evaluation_cases', evaluation.cases);
    setField('promotion_gate', evaluation.promotion_gate);
    setField('runtime_must_not_change', evaluation.runtime_must_not_change);
    setField('notes', card.notes);

    render();
  }

  async function loadExamples() {
    if (!examplePicker) return;
    try {
      const response = await fetch('/ddd/examples.json', { credentials: 'same-origin' });
      if (!response.ok) throw new Error('examples unavailable');
      const catalog = await response.json();
      const examples = Array.isArray(catalog.examples) ? catalog.examples : [];

      examples.forEach((example) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.textContent = example.title;
        button.addEventListener('click', () => loadCard(example.decision_card));
        examplePicker.appendChild(button);
      });
    } catch (_) {
      examplePicker.textContent = 'Example catalog is unavailable in this build.';
    }
  }

  function restoreDraft() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return false;
      loadCard(JSON.parse(raw));
      return true;
    } catch (_) {
      return false;
    }
  }

  form.addEventListener('input', () => render());
  form.addEventListener('change', () => render());
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    render();
  });

  byId('ddd-copy-json')?.addEventListener('click', async () => {
    render();
    try {
      await navigator.clipboard.writeText(output.textContent || '');
      status.textContent = 'JSON copied to clipboard';
    } catch (_) {
      status.textContent = 'Clipboard access is unavailable. Select the JSON manually.';
    }
  });

  byId('ddd-reset')?.addEventListener('click', () => {
    form.reset();
    try { localStorage.removeItem(STORAGE_KEY); } catch (_) {}
    render(false);
  });

  if (!restoreDraft()) render(false);
  loadExamples();
})();
