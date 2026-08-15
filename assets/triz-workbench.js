(() => {
  const root = document.querySelector('[data-triz-workbench]');
  if (!root) return;

  const form = root.querySelector('[data-triz-form]');
  const presetSelect = root.querySelector('[data-triz-preset]');
  const output = root.querySelector('[data-triz-output]');
  const status = root.querySelector('[data-triz-status]');
  const jsonNode = root.querySelector('[data-triz-json]');
  const copyButton = root.querySelector('[data-triz-copy]');
  const resetButton = root.querySelector('[data-triz-reset]');
  const leadNode = root.querySelector('[data-triz-lead-answer]');

  const operatorNames = {
    O1_time: 'O1 · Time',
    O2_condition: 'O2 · Condition',
    O3_context: 'O3 · Context',
    O4_system_level: 'O4 · System level',
    O5_authority: 'O5 · Authority',
    O6_representation: 'O6 · Representation'
  };

  const fallbackRoute = {
    operators: ['O2_condition', 'O5_authority'],
    patterns: ['P01', 'P08', 'P12'],
    resource_focus: ['information', 'time', 'history', 'policy_permission'],
    simplify_prompt: 'Remove steps and copies that do not protect a useful function or independent risk.',
    deterministic_move: 'Make state, rules, ownership, and transitions explicit before adding probabilistic behavior.',
    uncertainty_move: 'Use AI only for the remaining interpretation or search problem, with bounded authority.',
    primary_metric: 'useful_outcome',
    counter_metric: 'new_failure_or_complexity_rate'
  };

  let presets = [];
  let decisionMap = null;

  const value = (name) => form.elements[name]?.value?.trim() || '';
  const splitList = (text) => text ? text.split(/\n|;/).map((item) => item.trim()).filter(Boolean) : [];

  function escapeHtml(text) {
    return String(text || '').replace(/[&<>"']/g, (char) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;'
    }[char]));
  }

  function setStatus(message) {
    status.textContent = message;
  }

  async function loadData() {
    try {
      const [presetResponse, mapResponse] = await Promise.all([
        fetch('/datasets/triz-digital-framework/workbench-presets.json', { credentials: 'same-origin' }),
        fetch('/datasets/triz-digital-framework/decision-map.json', { credentials: 'same-origin' })
      ]);
      if (!presetResponse.ok || !mapResponse.ok) throw new Error('Dataset unavailable');
      const presetData = await presetResponse.json();
      decisionMap = await mapResponse.json();
      presets = presetData.presets || [];
      presets.forEach((preset) => {
        const option = document.createElement('option');
        option.value = preset.id;
        option.textContent = preset.label;
        presetSelect.appendChild(option);
      });
      setStatus('Ready. Choose a synthetic preset or frame your own problem.');
    } catch (error) {
      setStatus('Workbench ready with generic routing. Preset data could not be loaded.');
    }
  }

  function fillPreset(id) {
    const preset = presets.find((item) => item.id === id);
    if (!preset) return;
    Object.entries(preset).forEach(([key, val]) => {
      if (form.elements[key] && typeof val === 'string') form.elements[key].value = val;
    });
    form.elements['contradiction_type'].value = preset.contradiction_type || '';
    form.elements['risk_tier'].value = preset.risk_tier || 'R1';
  }

  function getRoute(type) {
    return decisionMap?.contradictions?.[type] || fallbackRoute;
  }

  function authorityFor(riskTier) {
    return decisionMap?.risk_authority?.[riskTier] || {
      read: 'authorized read',
      propose: 'allowed',
      validate: 'deterministic validation',
      approve: riskTier === 'R0' ? 'not required for advice' : 'policy-based approval',
      execute: riskTier === 'R0' ? 'none' : 'bounded audited execution'
    };
  }

  function resourcePrompts(route) {
    const resources = decisionMap?.resources || [];
    const focus = route.resource_focus || [];
    if (!resources.length) {
      return focus.map((id) => ({ id, name: id.replaceAll('_', ' '), prompt: 'What useful resource already exists here?' }));
    }
    return focus.map((id) => resources.find((item) => item.id === id)).filter(Boolean);
  }

  function buildResult() {
    const data = {
      domain: value('domain'),
      observed_behavior: value('observed_behavior'),
      useful_function: value('useful_function'),
      actor: value('actor'),
      business_object: value('business_object'),
      improve: value('improve'),
      preserve: value('preserve'),
      contradiction_type: value('contradiction_type') || 'other',
      risk_tier: value('risk_tier') || 'R1',
      evidence: value('evidence'),
      constraints: value('constraints')
    };

    const missing = ['observed_behavior', 'useful_function', 'improve', 'preserve'].filter((key) => !data[key]);
    if (missing.length) {
      setStatus('Add the observed behavior, useful function, and both sides of the contradiction.');
      return;
    }

    const route = getRoute(data.contradiction_type);
    const authority = authorityFor(data.risk_tier);
    const resources = resourcePrompts(route);
    const contradictionStatement = `If we improve ${data.improve}, ${data.preserve} becomes harder to preserve. Both are useful, so the design should separate the conditions instead of accepting a weak compromise.`;

    const optionA = {
      id: 'A',
      name: 'Remove or simplify',
      system_shape: route.simplify_prompt,
      benefits: ['Lower coordination and operating load', 'Fewer components or handoffs to own'],
      complexity_tax: ['May require changing current responsibility or policy assumptions'],
      reversibility: 'high'
    };
    const optionB = {
      id: 'B',
      name: 'Deterministic redesign',
      system_shape: route.deterministic_move,
      benefits: ['Clear state and testable rules', 'Predictable controls and easier regression testing'],
      complexity_tax: ['Adds explicit rule, workflow, state, or event design'],
      reversibility: 'medium'
    };
    const optionC = {
      id: 'C',
      name: 'Uncertainty-assisted redesign',
      system_shape: route.uncertainty_move,
      benefits: ['Handles ambiguous input or adaptive investigation', 'Can reduce manual evidence collection'],
      complexity_tax: ['Needs evaluation, guardrails, cost control, and stronger observability'],
      reversibility: 'medium'
    };

    const result = {
      problem: {
        statement: data.observed_behavior,
        observed_behavior: splitList(data.observed_behavior),
        desired_outcome: data.useful_function,
        actors: splitList(data.actor),
        business_objects: splitList(data.business_object),
        constraints: splitList(data.constraints),
        evidence: splitList(data.evidence),
        risk_tier: data.risk_tier,
        domain: data.domain
      },
      useful_function: {
        actor: data.actor || 'actor_to_confirm',
        action: data.useful_function,
        object: data.business_object || 'business_object_to_confirm',
        outcome: data.useful_function,
        current_mechanism: data.observed_behavior
      },
      ideal_result: {
        statement: `${data.useful_function} with less coordination, duplicated state, manual collection, and irreversible risk.`,
        complexity_to_avoid: ['unnecessary_handoffs', 'duplicate_state', 'new_unowned_runtime_dependency', 'broad_authority']
      },
      contradiction: {
        improving_property: data.improve,
        worsening_property: data.preserve,
        statement: contradictionStatement,
        type: data.contradiction_type
      },
      separation: {
        tested_operators: ['O1_time', 'O2_condition', 'O3_context', 'O4_system_level', 'O5_authority', 'O6_representation'],
        selected_operators: route.operators || fallbackRoute.operators,
        reasoning: [
          'Selected from the contradiction type as a starting hypothesis.',
          'Confirm operator fit against real evidence before architecture is chosen.'
        ]
      },
      resource_scan: Object.fromEntries(resources.map((item) => [item.id, [item.prompt]])),
      system_map: {
        actors: splitList(data.actor),
        business_objects: splitList(data.business_object),
        events: ['event_or_trigger_to_map'],
        decisions: ['decision_that_resolves_the_contradiction'],
        rules: splitList(data.constraints),
        states: ['current_state_to_map', 'desired_state_to_map'],
        delays: ['waiting_or_latency_to_measure'],
        evidence: splitList(data.evidence),
        side_effects: ['counter_metric_failure_to_observe'],
        relationships: ['Map who owns the decision, who has context, and who carries the consequence.']
      },
      selected_patterns: route.patterns || fallbackRoute.patterns,
      options: [optionA, optionB, optionC],
      technology_allocation: {
        deterministic_rules: ['Exact constraints, authorization, thresholds, and invariants stay deterministic.'],
        workflow: ['Use a workflow or state machine when the sequence is known.'],
        events: ['Use events only where reaction should not block the producer.'],
        retrieval_or_read_tools: ['Use purpose-scoped reads for fresh or private facts.'],
        ai_models: ['Use a model for interpretation, classification, synthesis, or candidate generation only when useful.'],
        agents: ['Use a bounded agent only if the next useful step depends on evidence discovered during the task.'],
        human_judgment: [authority.approve]
      },
      authority_chain: {
        read: [authority.read],
        propose: [authority.propose],
        validate: [authority.validate],
        approve: [authority.approve],
        execute: [authority.execute]
      },
      experiment: {
        hypothesis: `A redesigned path improves ${data.improve} without unacceptable damage to ${data.preserve}.`,
        change: 'Choose one reversible slice of the preferred system shape and test it against the current baseline.',
        primary_metric: route.primary_metric || fallbackRoute.primary_metric,
        counter_metrics: [route.counter_metric || fallbackRoute.counter_metric],
        failure_condition: `Stop or redesign if the counter-metric shows material damage to ${data.preserve}.`,
        scope: 'One low-risk process variant, interface, country, user group, or shadow/replay slice.',
        rollback_or_recovery: 'Keep the current path available until the experiment proves both sides of the contradiction.'
      },
      risks: ['wrong_boundary', 'hidden_manual_workaround', 'new_unowned_dependency'],
      assumptions: ['Workbench routing is a hypothesis based on the selected contradiction type.'],
      unknowns: ['Real thresholds, ownership, current configuration, and evidence quality must be confirmed.']
    };

    renderResult(result, route);
  }

  function renderResult(result, route) {
    const operatorHtml = result.separation.selected_operators
      .map((id) => `<span class="triz-workbench__chip">${escapeHtml(operatorNames[id] || id)}</span>`)
      .join('');

    const resourceHtml = Object.entries(result.resource_scan)
      .map(([key, prompts]) => `<li><strong>${escapeHtml(key.replaceAll('_', ' '))}</strong><span>${escapeHtml(prompts[0])}</span></li>`)
      .join('');

    const optionsHtml = result.options.map((option) => `
      <article class="triz-workbench__option">
        <p class="triz-workbench__index">Option ${escapeHtml(option.id)}</p>
        <h3>${escapeHtml(option.name)}</h3>
        <p>${escapeHtml(option.system_shape)}</p>
        <dl>
          <div><dt>Benefit</dt><dd>${escapeHtml(option.benefits[0])}</dd></div>
          <div><dt>Complexity tax</dt><dd>${escapeHtml(option.complexity_tax[0])}</dd></div>
          <div><dt>Reversibility</dt><dd>${escapeHtml(option.reversibility)}</dd></div>
        </dl>
      </article>`).join('');

    const chain = result.authority_chain;
    const chainHtml = ['read', 'propose', 'validate', 'approve', 'execute']
      .map((step, index) => `<li><span>${String(index + 1).padStart(2, '0')}</span><strong>${step}</strong><small>${escapeHtml(chain[step][0])}</small></li>`)
      .join('');

    output.innerHTML = `
      <section class="triz-workbench__result-block">
        <p class="triz-workbench__index">Contradiction</p>
        <h3>${escapeHtml(result.contradiction.statement)}</h3>
        <div class="triz-workbench__chips">${operatorHtml}</div>
      </section>
      <section class="triz-workbench__result-block">
        <p class="triz-workbench__index">Resource scan</p>
        <ul class="triz-workbench__resources">${resourceHtml}</ul>
      </section>
      <section class="triz-workbench__result-block">
        <p class="triz-workbench__index">Different system shapes</p>
        <div class="triz-workbench__options">${optionsHtml}</div>
      </section>
      <section class="triz-workbench__result-block">
        <p class="triz-workbench__index">Authority chain · ${escapeHtml(result.problem.risk_tier)}</p>
        <ol class="triz-workbench__authority">${chainHtml}</ol>
      </section>
      <section class="triz-workbench__result-block">
        <p class="triz-workbench__index">Experiment</p>
        <h3>${escapeHtml(result.experiment.hypothesis)}</h3>
        <p><strong>Primary:</strong> ${escapeHtml(result.experiment.primary_metric)} · <strong>Counter:</strong> ${escapeHtml(result.experiment.counter_metrics[0])}</p>
        <p><strong>Failure condition:</strong> ${escapeHtml(result.experiment.failure_condition)}</p>
      </section>`;

    const leadAnswer = `I would not start from a product. First, I would frame the useful function and evidence. The main contradiction is ${result.contradiction.improving_property} versus ${result.contradiction.worsening_property}. I would test ${result.separation.selected_operators.map((id) => operatorNames[id]?.replace(/^O\d · /, '') || id).join(', ')} before choosing technology. Then I would compare a simpler boundary, a deterministic redesign, and an uncertainty-assisted option. For ${result.problem.risk_tier} risk, I would separate read, propose, validate, approve, and execute. Finally, I would test ${result.experiment.primary_metric} together with ${result.experiment.counter_metrics[0]}, because improving only one side is not a real resolution.`;

    leadNode.textContent = leadAnswer;
    jsonNode.textContent = JSON.stringify(result, null, 2);
    copyButton.disabled = false;
    output.hidden = false;
    root.querySelector('[data-triz-machine]').hidden = false;
    root.querySelector('[data-triz-lead]').hidden = false;
    setStatus(`Draft built. Suggested patterns: ${(route.patterns || []).join(', ') || 'inspect manually'}. Treat it as a hypothesis, not an architecture decision.`);
    output.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
  }

  async function copyJson() {
    if (!jsonNode.textContent.trim()) return;
    try {
      await navigator.clipboard.writeText(jsonNode.textContent);
      copyButton.textContent = 'Copied';
      window.setTimeout(() => { copyButton.textContent = 'Copy JSON'; }, 1400);
    } catch (error) {
      setStatus('Clipboard access is blocked. Select the JSON manually.');
    }
  }

  function resetWorkbench() {
    form.reset();
    presetSelect.value = '';
    output.hidden = true;
    root.querySelector('[data-triz-machine]').hidden = true;
    root.querySelector('[data-triz-lead]').hidden = true;
    jsonNode.textContent = '';
    leadNode.textContent = '';
    copyButton.disabled = true;
    setStatus('Cleared. Frame the useful function before choosing a solution.');
  }

  presetSelect.addEventListener('change', (event) => fillPreset(event.target.value));
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    buildResult();
  });
  copyButton.addEventListener('click', copyJson);
  resetButton.addEventListener('click', resetWorkbench);

  loadData();
})();
