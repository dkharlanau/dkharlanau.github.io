(() => {
  const root = document.querySelector('.dataset-hero');
  const jsonLink = document.querySelector('.dataset-actions a[href$=".json"]');
  if (!root || !jsonLink) {
    return;
  }

  const insertAfter = (target, node) => {
    const parent = target.parentNode;
    if (!parent) return;
    if (target.nextSibling) {
      parent.insertBefore(node, target.nextSibling);
    } else {
      parent.appendChild(node);
    }
  };

  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  };

  const titleCase = (value) => value.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());

  const renderPills = (items) => {
    if (!items || !items.length) return null;
    const wrap = el('div', 'dataset-pill-group');
    items.forEach((item) => {
      wrap.appendChild(el('span', 'dataset-pill', item));
    });
    return wrap;
  };

  const renderList = (items) => {
    if (!items || !items.length) return null;
    const ul = el('ul', 'dataset-list');
    items.forEach((item) => {
      const li = el('li');
      if (typeof item === 'string' || typeof item === 'number') {
        li.textContent = String(item);
      } else {
        li.appendChild(renderObject(item));
      }
      ul.appendChild(li);
    });
    return ul;
  };

  const renderObject = (obj) => {
    const wrap = el('div', 'dataset-kv');
    Object.entries(obj || {}).forEach(([key, value]) => {
      const item = el('div', 'dataset-kv__item');
      item.appendChild(el('div', 'dataset-kv__label', titleCase(key)));
      if (Array.isArray(value)) {
        const list = renderList(value);
        if (list) item.appendChild(list);
      } else if (value && typeof value === 'object') {
        item.appendChild(renderObject(value));
      } else {
        item.appendChild(el('div', 'dataset-kv__value', value == null ? '' : String(value)));
      }
      wrap.appendChild(item);
    });
    return wrap;
  };

  const renderSection = (title, bodyNodes) => {
    if (!bodyNodes || (Array.isArray(bodyNodes) && bodyNodes.length === 0)) return null;
    const section = el('section', 'dataset-section');
    section.appendChild(el('h2', 'dataset-section__title', title));
    if (Array.isArray(bodyNodes)) {
      bodyNodes.filter(Boolean).forEach((node) => section.appendChild(node));
    } else {
      section.appendChild(bodyNodes);
    }
    return section;
  };

  const renderCardGrid = (items, renderFn) => {
    if (!items || !items.length) return null;
    const grid = el('div', 'dataset-card-grid');
    items.forEach((item) => {
      const card = el('article', 'dataset-card');
      renderFn(card, item);
      grid.appendChild(card);
    });
    return grid;
  };

  const resolveType = (data) => {
    if (data.type) return data.type;
    if (data.decision_question) return 'decision_block';
    if (data.phases) return 'sequence_playbook';
    if (data.layers) return 'architecture_blueprint';
    if (data.patterns) return 'pattern_pack';
    if (data.tools) return 'tool_pack';
    return 'object';
  };

  const renderOverview = (data) => {
    const facts = [];
    const addFact = (label, value) => {
      if (value === undefined || value === null || value === '') return;
      facts.push({ label, value: String(value) });
    };
    addFact('ID', data.id || data.byte_id);
    addFact('Version', data.version);
    addFact('Status', data.status);
    addFact('Level', data.level);
    addFact('Domain', data.domain);
    addFact('Focus', data.focus);
    addFact('Goal', data.goal);
    addFact('Purpose', data.purpose);

    const wrap = el('div', 'dataset-overview');
    if (facts.length) {
      const grid = el('div', 'dataset-overview__grid');
      facts.forEach((fact) => {
        const card = el('div', 'dataset-overview__item');
        card.appendChild(el('div', 'dataset-overview__label', fact.label));
        card.appendChild(el('div', 'dataset-overview__value', fact.value));
        grid.appendChild(card);
      });
      wrap.appendChild(grid);
    }

    const tags = data.tags || data.meta?.tags;
    const pillGroup = renderPills(tags || []);
    if (pillGroup) wrap.appendChild(pillGroup);
    return wrap.childNodes.length ? wrap : null;
  };

  const renderDecisionBlock = (data) => {
    const container = el('div', 'dataset-view');
    const overview = renderOverview(data);
    if (overview) container.appendChild(renderSection('Overview', overview));

    if (data.decision_question) {
      container.appendChild(renderSection('Decision Question', el('p', 'dataset-lead', data.decision_question)));
    }

    const contextBlocks = [];
    if (data.context?.when_to_use) contextBlocks.push(el('div', 'dataset-subsection', null));
    const context = el('div', 'dataset-subsection');
    if (data.context?.when_to_use) {
      context.appendChild(el('h3', 'dataset-subsection__title', 'When to Use'));
      context.appendChild(renderList(data.context.when_to_use));
    }
    if (data.context?.preconditions) {
      context.appendChild(el('h3', 'dataset-subsection__title', 'Preconditions'));
      context.appendChild(renderList(data.context.preconditions));
    }
    if (context.childNodes.length) container.appendChild(renderSection('Context', context));

    const inputs = el('div', 'dataset-subsection');
    if (data.inputs?.signals_observable) {
      inputs.appendChild(el('h3', 'dataset-subsection__title', 'Signals Observable'));
      inputs.appendChild(renderList(data.inputs.signals_observable));
    }
    if (data.inputs?.constraints) {
      inputs.appendChild(el('h3', 'dataset-subsection__title', 'Constraints'));
      inputs.appendChild(renderList(data.inputs.constraints));
    }
    if (data.inputs?.stakeholders) {
      inputs.appendChild(el('h3', 'dataset-subsection__title', 'Stakeholders'));
      inputs.appendChild(renderList(data.inputs.stakeholders));
    }
    if (inputs.childNodes.length) container.appendChild(renderSection('Inputs', inputs));

    const optionsGrid = renderCardGrid(data.options, (card, option) => {
      card.appendChild(el('h3', 'dataset-card__title', option.name || option.id));
      if (option.summary) card.appendChild(el('p', 'dataset-card__summary', option.summary));
      if (option.tradeoffs) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Tradeoffs'));
        card.appendChild(renderList(option.tradeoffs));
      }
    });
    if (optionsGrid) container.appendChild(renderSection('Options', optionsGrid));

    const logic = el('div', 'dataset-subsection');
    if (data.decision_logic?.preferred_option_rules) {
      const rules = renderCardGrid(data.decision_logic.preferred_option_rules, (card, rule) => {
        card.appendChild(el('h3', 'dataset-card__title', 'Decision Rule'));
        if (rule.if) {
          card.appendChild(el('h4', 'dataset-card__subtitle', 'If'));
          card.appendChild(renderList(rule.if));
        }
        if (rule.then) {
          card.appendChild(el('h4', 'dataset-card__subtitle', 'Then'));
          card.appendChild(el('p', 'dataset-card__summary', rule.then));
        }
      });
      if (rules) {
        logic.appendChild(el('h3', 'dataset-subsection__title', 'Preferred Option Rules'));
        logic.appendChild(rules);
      }
    }
    if (data.decision_logic?.anti_patterns_to_avoid) {
      logic.appendChild(el('h3', 'dataset-subsection__title', 'Anti-Patterns to Avoid'));
      logic.appendChild(renderList(data.decision_logic.anti_patterns_to_avoid));
    }
    if (logic.childNodes.length) container.appendChild(renderSection('Decision Logic', logic));

    if (data.expected_outcomes) {
      container.appendChild(renderSection('Expected Outcomes', renderList(data.expected_outcomes)));
    }

    if (data.controls_enforcement) {
      container.appendChild(renderSection('Controls & Enforcement', renderList(data.controls_enforcement)));
    }

    if (data.owner_rights_raci) {
      const raci = el('div', 'dataset-raci');
      Object.entries(data.owner_rights_raci).forEach(([role, items]) => {
        const block = el('div', 'dataset-raci__item');
        block.appendChild(el('h3', 'dataset-card__title', titleCase(role)));
        block.appendChild(renderList(items));
        raci.appendChild(block);
      });
      container.appendChild(renderSection('RACI', raci));
    }

    if (data.metrics) {
      container.appendChild(renderSection('Metrics', renderList(data.metrics)));
    }

    if (data.examples_generic) {
      container.appendChild(renderSection('Examples', renderList(data.examples_generic)));
    }

    return container;
  };

  const renderSequencePlaybook = (data) => {
    const container = el('div', 'dataset-view');
    const overview = renderOverview(data);
    if (overview) container.appendChild(renderSection('Overview', overview));

    const phasesGrid = renderCardGrid(data.phases, (card, phase) => {
      card.appendChild(el('h3', 'dataset-card__title', phase.name || phase.phase_id));
      if (phase.primary_patterns) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Primary Patterns'));
        card.appendChild(renderList(phase.primary_patterns));
      }
      if (phase.decisions_to_make) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Decisions to Make'));
        card.appendChild(renderList(phase.decisions_to_make));
      }
      if (phase.required_artifacts) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Required Artifacts'));
        card.appendChild(renderList(phase.required_artifacts));
      }
      if (phase.exit_criteria) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Exit Criteria'));
        card.appendChild(renderList(phase.exit_criteria));
      }
      if (phase.gating_metrics) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Gating Metrics'));
        card.appendChild(renderList(phase.gating_metrics.map((metric) => `${metric.metric_id}: ${metric.target} — ${metric.why_gate}`)));
      }
    });
    if (phasesGrid) container.appendChild(renderSection('Phases', phasesGrid));
    return container;
  };

  const renderArchitectureBlueprint = (data) => {
    const container = el('div', 'dataset-view');
    const overview = renderOverview(data);
    if (overview) container.appendChild(renderSection('Overview', overview));
    if (data.scope) container.appendChild(renderSection('Scope', renderList(data.scope)));
    if (data.principles) container.appendChild(renderSection('Principles', renderList(data.principles)));

    const layersGrid = renderCardGrid(data.layers, (card, layer) => {
      card.appendChild(el('h3', 'dataset-card__title', layer.name || layer.layer_id));
      if (layer.purpose) card.appendChild(el('p', 'dataset-card__summary', layer.purpose));
      if (layer.typical_assets) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Typical Assets'));
        card.appendChild(renderList(layer.typical_assets));
      }
      if (layer.controls) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Controls'));
        card.appendChild(renderList(layer.controls));
      }
      if (layer.outputs) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Outputs'));
        card.appendChild(renderList(layer.outputs));
      }
    });
    if (layersGrid) container.appendChild(renderSection('Layers', layersGrid));

    if (data.event_model) {
      const eventModel = el('div', 'dataset-subsection');
      if (data.event_model.event_types) {
        eventModel.appendChild(el('h3', 'dataset-subsection__title', 'Event Types'));
        eventModel.appendChild(renderList(data.event_model.event_types));
      }
      if (data.event_model.load_event_schema) {
        eventModel.appendChild(el('h3', 'dataset-subsection__title', 'Load Event Schema'));
        eventModel.appendChild(renderObject(data.event_model.load_event_schema));
      }
      container.appendChild(renderSection('Event Model', eventModel));
    }

    if (data.governance_controls) container.appendChild(renderSection('Governance Controls', renderList(data.governance_controls)));
    if (data.key_metrics_for_gating) container.appendChild(renderSection('Key Metrics for Gating', renderList(data.key_metrics_for_gating)));
    if (data.deliverables_mapping) container.appendChild(renderSection('Deliverables Mapping', renderObject(data.deliverables_mapping)));
    if (data.ai_reasoning_hooks) container.appendChild(renderSection('AI Reasoning Hooks', renderList(data.ai_reasoning_hooks)));

    return container;
  };

  const renderPatternPack = (data) => {
    const container = el('div', 'dataset-view');
    const overview = renderOverview(data);
    if (overview) container.appendChild(renderSection('Overview', overview));
    if (data.purpose) container.appendChild(renderSection('Purpose', el('p', 'dataset-lead', data.purpose)));

    const patternsGrid = renderCardGrid(data.patterns, (card, pattern) => {
      card.appendChild(el('h3', 'dataset-card__title', pattern.title || pattern.pattern_id));
      if (pattern.category) card.appendChild(el('p', 'dataset-card__meta', pattern.category));
      if (pattern.problem) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Problem'));
        card.appendChild(el('p', 'dataset-card__summary', pattern.problem));
      }
      if (pattern.forces) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Forces'));
        card.appendChild(renderList(pattern.forces));
      }
      if (pattern.solution) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Solution'));
        card.appendChild(el('p', 'dataset-card__summary', pattern.solution));
      }
      if (pattern.mdg_mechanics) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'MDG Mechanics'));
        card.appendChild(renderList(pattern.mdg_mechanics));
      }
      if (pattern.pitfalls) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Pitfalls'));
        card.appendChild(renderList(pattern.pitfalls));
      }
      if (pattern.evidence_metrics) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Evidence Metrics'));
        card.appendChild(renderList(pattern.evidence_metrics));
      }
      if (pattern.best_for) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Best For'));
        card.appendChild(renderList(pattern.best_for));
      }
    });
    if (patternsGrid) container.appendChild(renderSection('Patterns', patternsGrid));

    if (data.recommended_next_actions) {
      container.appendChild(renderSection('Recommended Next Actions', renderList(data.recommended_next_actions)));
    }
    return container;
  };

  const renderToolPack = (data) => {
    const container = el('div', 'dataset-view');
    const overview = renderOverview(data);
    if (overview) container.appendChild(renderSection('Overview', overview));
    if (data.purpose) container.appendChild(renderSection('Purpose', el('p', 'dataset-lead', data.purpose)));

    const toolsGrid = renderCardGrid(data.tools, (card, tool) => {
      card.appendChild(el('h3', 'dataset-card__title', tool.title || tool.tool_id));
      if (tool.type) card.appendChild(el('p', 'dataset-card__meta', titleCase(tool.type)));
      if (tool.description) card.appendChild(el('p', 'dataset-card__summary', tool.description));
      if (tool.entities) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Entities'));
        card.appendChild(renderList(tool.entities));
      }
      if (tool.relations) {
        card.appendChild(el('h4', 'dataset-card__subtitle', 'Relations'));
        card.appendChild(renderList(tool.relations));
      }
    });
    if (toolsGrid) container.appendChild(renderSection('Tools', toolsGrid));

    if (data.how_to_use_minimum) {
      container.appendChild(renderSection('How to Use (Minimum)', renderList(data.how_to_use_minimum)));
    }
    return container;
  };

  const renderObjectType = (data) => {
    const container = el('div', 'dataset-view');
    const overview = renderOverview(data);
    if (overview) container.appendChild(renderSection('Overview', overview));

    const priorityKeys = [
      'hook',
      'idea',
      'intent',
      'core_idea',
      'core_principles',
      'inputs',
      'reasoning_steps',
      'output_schema',
      'forbidden_behaviors',
      'example_minimal_prompt',
      'problem_understanding',
      'solution_logic',
      'triz_principle',
      'loop_steps',
      'how_it_works',
      'rules',
      'automation',
      'metrics_you_get',
      'why_it_beats_old_school',
      'application_patterns',
      'anti_patterns',
      'anti_patterns_to_kill',
      'when_to_use',
      'when_not_to_use',
      'practical_checklist',
      'pitfalls',
      'example',
      'micro_example',
      'starter_template',
      'usage_guidance',
      'teach_it_in_english'
    ];

    priorityKeys.forEach((key) => {
      if (!(key in data)) return;
      const value = data[key];
      if (Array.isArray(value)) {
        const list = renderList(value);
        if (list) container.appendChild(renderSection(titleCase(key), list));
      } else if (value && typeof value === 'object') {
        container.appendChild(renderSection(titleCase(key), renderObject(value)));
      } else if (value) {
        container.appendChild(renderSection(titleCase(key), el('p', 'dataset-lead', String(value))));
      }
    });

    if (data.meta && Object.keys(data.meta).length) {
      container.appendChild(renderSection('Meta', renderObject(data.meta)));
    }
    return container;
  };

  const renderByType = (data) => {
    switch (resolveType(data)) {
      case 'decision_block':
        return renderDecisionBlock(data);
      case 'sequence_playbook':
        return renderSequencePlaybook(data);
      case 'architecture_blueprint':
        return renderArchitectureBlueprint(data);
      case 'pattern_pack':
        return renderPatternPack(data);
      case 'tool_pack':
        return renderToolPack(data);
      default:
        return renderObjectType(data);
    }
  };

  fetch(jsonLink.href)
    .then((resp) => resp.json())
    .then((data) => {
      const view = renderByType(data);
      const anchor = document.querySelector('.dataset-entry-lead') || root;
      insertAfter(anchor, view);
      document.body.classList.add('dataset-rendered');
    })
    .catch(() => {
      // If JSON fails, leave the raw block visible.
    });
})();
