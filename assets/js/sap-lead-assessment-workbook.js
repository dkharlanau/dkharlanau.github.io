(function () {
  'use strict';

  const FACTORY_URL = '/ai/career-factory.json';
  const FILE_NAME = 'sap-lead-assessment-master.xlsx';
  const STATUS_VALUES = ['Not Started', 'Reading', 'Practicing', 'Ready'];
  const TIER_PRIORITY = { core: 'P1', cross_boundary: 'P2', differentiator: 'P3' };

  function text(value) {
    if (value === null || value === undefined) return '';
    return String(value);
  }

  function list(value) {
    return Array.isArray(value) ? value : [];
  }

  function absoluteUrl(path) {
    if (!path) return '';
    if (/^https?:\/\//i.test(path)) return path;
    return 'https://dkharlanau.github.io' + (path.startsWith('/') ? path : '/' + path);
  }

  function parseRoadmap() {
    const node = document.getElementById('sap-lead-roadmap-data');
    if (!node) throw new Error('Roadmap data is missing.');
    return JSON.parse(node.textContent);
  }

  async function loadFactory() {
    const response = await fetch(FACTORY_URL, { cache: 'no-store' });
    if (!response.ok) throw new Error('Career Factory data is unavailable.');
    return response.json();
  }

  function inferComponent(item) {
    const value = (text(item.route) + ' ' + text(item.title)).toLowerCase();
    const rules = [
      ['SAP AIF', ['\/aif', 'application interface framework']],
      ['SAP aATP / ATP', ['\/atp', 'available-to-promise', 'available to promise']],
      ['SAP Automotive JIT/JIS', ['automotive-jit', 'just-in-time', 'just-in-sequence']],
      ['SAP Billing', ['\/billing', 'billing']],
      ['Business Partner / CVI', ['business-partner', 'business partner', 'cvi']],
      ['Condition Contract Management', ['condition-contract-management', 'condition contract']],
      ['SAP Credit Management', ['\/credit', 'credit management']],
      ['Data Governance', ['data-governance', 'data governance']],
      ['S/4HANA Deployment Models', ['deployment-models', 'public cloud', 'private cloud']],
      ['ABAP / Extensibility', ['\/development', 'extensibility', 'clean core']],
      ['Analytics / Observability', ['end-to-end-analytics', 'observability', 'analytics']],
      ['SAP EWM', ['\/ewm', 'extended warehouse management']],
      ['Integration Architecture', ['\/integrations', 'integration architecture']],
      ['Integration Operations', ['integration-operations', 'idoc', 'qrf', 'trfc', 'interface operations']],
      ['SAP Inventory Management', ['inventory-management', 'inventory management', 'movement type']],
      ['SAP Kanban', ['\/kanban', 'kanban']],
      ['SAP Logistics', ['logistics-capabilities', 'logistics']],
      ['SAP Master Data', ['master-data', 'material-behavior', 'material master']],
      ['SAP MDG / DRF', ['\/mdg', '\/drf', 'master data governance', 'data replication framework']],
      ['SAP Migration', ['migration', 'migration cockpit', 'data migration']],
      ['SAP Performance', ['performance', 'sm50', 'sm12', 'sm13', 'sm58', 'smq1', 'smq2']],
      ['SAP Pricing', ['\/pricing', 'pricing']],
      ['SAP Procurement / MM', ['\/procurement', 'procure-to-pay', 'purchasing']],
      ['SAP Production / PP', ['\/production', 'production planning']],
      ['SAP Quality Management', ['quality-management', 'quality management']],
      ['SAP Sales / SD', ['sales-processes', 'sales-order', 'sales diagnostics', 'sales-diagnostics']],
      ['SAP Shipping', ['\/shipping', 'shipping', 'delivery execution']],
      ['SAP TM', ['transportation-management', 'transportation management']],
      ['Variant Configuration', ['variant-configuration', 'variant configuration']],
      ['Business AI', ['business-ai', 'business ai']],
      ['AI / RAG / Agents', ['ai-ready', 'rag', 'agent', 'mcp', 'retrieval']],
      ['Assessment Practice', ['\/assessment', 'assessment']],
      ['Interview Readiness', ['interview-readiness', 'interview']],
      ['Reusable Data Procedures', ['reusable-data-procedures']],
      ['Enterprise Assurance', ['enterprise-assurance']],
      ['Tooling / Roadmap', ['tool-roadmap']],
      ['Templates / Work Artifacts', ['\/templates', 'template']]
    ];
    for (const rule of rules) {
      if (rule[1].some(function (token) { return value.indexOf(token) !== -1; })) return rule[0];
    }
    return 'Other / Cross-domain';
  }

  function suggestedSkillIds(item) {
    return list(item.suggested_skills).map(function (candidate) { return text(candidate.skill_id); }).filter(Boolean);
  }

  function sourceSummary(skill) {
    return list(skill.sources).map(function (source) { return text(source.label) + ' — ' + absoluteUrl(source.href); }).join('\n');
  }

  function skillPriority(skill) {
    return TIER_PRIORITY[skill.tier] || 'P2';
  }

  function topicPriority(item, skillById) {
    const ids = list(item.skills).concat(suggestedSkillIds(item));
    let best = 'P3';
    ids.forEach(function (id) {
      const skill = skillById[id];
      const priority = skill ? skillPriority(skill) : 'P2';
      if (priority === 'P1') best = 'P1';
      else if (priority === 'P2' && best === 'P3') best = 'P2';
    });
    if (item.state === 'needs_decision' && ids.length === 0) return 'P2';
    return best;
  }

  function addSheet(workbook, name, rows, widths, filter) {
    const sheet = XLSX.utils.aoa_to_sheet(rows);
    sheet['!cols'] = widths.map(function (wch) { return { wch: wch }; });
    if (filter && rows.length > 1) {
      sheet['!autofilter'] = { ref: 'A1:' + XLSX.utils.encode_col(rows[0].length - 1) + rows.length };
    }
    XLSX.utils.book_append_sheet(workbook, sheet, name.substring(0, 31));
    return sheet;
  }

  function buildWorkbook(roadmap, factory) {
    const workbook = XLSX.utils.book_new();
    const skills = list(roadmap.skills);
    const labs = list(factory.lab_inventory);
    const tracks = roadmap.tracks || {};
    const skillById = {};
    skills.forEach(function (skill) { skillById[skill.id] = skill; });

    const mapped = labs.filter(function (item) { return item.state === 'mapped'; }).length;
    const needsDecision = labs.filter(function (item) { return item.state === 'needs_decision'; }).length;
    const coreSkills = skills.filter(function (skill) { return skill.tier === 'core'; }).length;

    addSheet(workbook, 'Dashboard', [
      ['SAP Lead Assessment Master Workbook'],
      ['Generated from the live Career Factory and Career Roadmap.'],
      [],
      ['Metric', 'Value'],
      ['Lead skills', skills.length],
      ['Core P1 skills', coreSkills],
      ['Lab pages', labs.length],
      ['Mapped Lab pages', mapped],
      ['Lab pages needing career mapping', needsDecision],
      ['Career decision coverage', factory.summary && factory.summary.decision_coverage_percent !== undefined ? factory.summary.decision_coverage_percent + '%' : ''],
      [],
      ['Start here'],
      ['1', 'Filter Lead Skills to P1 and choose three skills.'],
      ['2', 'Use Site Topics to find the detailed Lab pages behind each skill.'],
      ['3', 'Answer from memory before opening the link.'],
      ['4', 'Add one real project example and update confidence/status.'],
      ['5', 'Use Needs Mapping as a content backlog: useful Lab pages should be connected to a career skill.']
    ], [8, 88], false);

    const skillRows = [[
      'Track', 'Skill ID', 'Skill', 'Tier', 'Priority', 'Capabilities', 'Why it matters',
      'Interview signal', 'Sources', 'Confidence (1-5)', 'Status', 'Project example', 'Notes'
    ]];
    skills.forEach(function (skill) {
      const track = tracks[skill.track] || {};
      skillRows.push([
        track.label || skill.track, skill.id, skill.title, skill.tier, skillPriority(skill),
        list(skill.capabilities).join(', '), skill.why, skill.interview_signal, sourceSummary(skill),
        1, STATUS_VALUES[0], '', ''
      ]);
    });
    addSheet(workbook, 'Lead Skills', skillRows, [28, 24, 36, 18, 10, 26, 56, 56, 70, 16, 16, 45, 40], true);

    const topicRows = [[
      'Component / Area', 'Topic', 'Route', 'Source file', 'Career state', 'Career impact',
      'Mapped skills', 'Suggested skills', 'Priority', 'Confidence (1-5)', 'Status', 'URL', 'Notes'
    ]];
    labs.forEach(function (item) {
      topicRows.push([
        inferComponent(item), item.title, item.route, item.source_file, item.state, item.career_impact,
        list(item.skills).join(', '), suggestedSkillIds(item).join(', '), topicPriority(item, skillById),
        1, STATUS_VALUES[0], absoluteUrl(item.route), ''
      ]);
    });
    addSheet(workbook, 'Site Topics', topicRows, [28, 48, 48, 54, 18, 18, 34, 34, 10, 16, 16, 58, 40], true);

    const components = {};
    labs.forEach(function (item) {
      const component = inferComponent(item);
      if (!components[component]) components[component] = { total: 0, mapped: 0, gaps: 0, p1: 0 };
      const bucket = components[component];
      bucket.total += 1;
      if (item.state === 'mapped') bucket.mapped += 1;
      if (item.state === 'needs_decision') bucket.gaps += 1;
      if (topicPriority(item, skillById) === 'P1') bucket.p1 += 1;
    });
    const componentRows = [['Component / Area', 'Site topics', 'Mapped', 'Needs mapping', 'P1 topics']];
    Object.keys(components).sort().forEach(function (name) {
      const value = components[name];
      componentRows.push([name, value.total, value.mapped, value.gaps, value.p1]);
    });
    addSheet(workbook, 'Components', componentRows, [34, 14, 14, 18, 14], true);

    const gapRows = [[
      'Component / Area', 'Topic', 'Route', 'Suggested skills', 'Priority', 'URL', 'Decision / Notes'
    ]];
    labs.filter(function (item) { return item.state === 'needs_decision'; }).forEach(function (item) {
      gapRows.push([
        inferComponent(item), item.title, item.route, suggestedSkillIds(item).join(', '),
        topicPriority(item, skillById), absoluteUrl(item.route), ''
      ]);
    });
    addSheet(workbook, 'Needs Mapping', gapRows, [30, 50, 50, 38, 10, 58, 46], true);

    Object.keys(tracks).sort(function (a, b) {
      return (tracks[a].order || 999) - (tracks[b].order || 999);
    }).forEach(function (trackId) {
      const rows = [['Skill ID', 'Skill', 'Tier', 'Priority', 'Capabilities', 'Interview signal', 'Sources', 'Confidence (1-5)', 'Status', 'Project example', 'Notes']];
      skills.filter(function (skill) { return skill.track === trackId; }).forEach(function (skill) {
        rows.push([
          skill.id, skill.title, skill.tier, skillPriority(skill), list(skill.capabilities).join(', '),
          skill.interview_signal, sourceSummary(skill), 1, STATUS_VALUES[0], '', ''
        ]);
      });
      addSheet(workbook, tracks[trackId].short_label || tracks[trackId].label || trackId, rows, [24, 38, 18, 10, 26, 58, 70, 16, 16, 45, 40], true);
    });

    const sprintRows = [['Date', 'Track', 'Skill / Topic', 'Goal', '20-minute block', 'Result / Gap', 'Next action', 'Done']];
    for (let i = 0; i < 30; i += 1) sprintRows.push(['', '', '', '', 'Recall → review → project example', '', '', 'No']);
    addSheet(workbook, 'Daily Sprint', sprintRows, [14, 24, 42, 44, 34, 44, 44, 10], true);

    addSheet(workbook, 'How to Use', [
      ['Rule', 'Action'],
      ['1. Start with P1', 'P1 is the minimum Lead-level core. Do not try to learn the whole site at once.'],
      ['2. Recall before reading', 'Answer from memory first. The gap in your first answer is what you need to study.'],
      ['3. Move from skill to detail', 'Lead Skills gives the assessment capability. Site Topics gives the detailed pages and components.'],
      ['4. Use project evidence', 'For every important topic, add one real project decision, incident, trade-off, or result.'],
      ['5. Rate confidence', '1 = cannot explain; 3 = can explain basics; 5 = can lead a design or troubleshooting discussion.'],
      ['6. Mark Ready carefully', 'Ready means you can explain purpose, flow, one design decision, one failure path, and one project example.'],
      ['7. Treat Needs Mapping as backlog', 'These pages exist on the site but are not yet connected to a career skill. Review the suggested mapping before changing the roadmap.'],
      ['8. Regenerate, do not maintain manually', 'Use the web generator again after Career Factory changes. The workbook is a view of the current source data.']
    ], [30, 104], true);

    workbook.Props = {
      Title: 'SAP Lead Assessment Master Workbook',
      Subject: 'SAP Lead interview and assessment preparation',
      Author: 'DKHARLANAU.github.io',
      Comments: 'Generated from Career Factory and Career Roadmap.'
    };
    return workbook;
  }

  function setMetric(id, value) {
    const node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  async function refreshMetrics() {
    try {
      const roadmap = parseRoadmap();
      const factory = await loadFactory();
      setMetric('sap-lead-skill-count', list(roadmap.skills).length);
      setMetric('sap-lead-page-count', list(factory.lab_inventory).length);
      setMetric('sap-lead-gap-count', list(factory.lab_inventory).filter(function (item) { return item.state === 'needs_decision'; }).length);
      setMetric('sap-lead-coverage', factory.summary && factory.summary.decision_coverage_percent !== undefined ? factory.summary.decision_coverage_percent + '%' : '—');
    } catch (error) {
      setMetric('sap-lead-coverage', 'data unavailable');
    }
  }

  async function downloadWorkbook() {
    const button = document.getElementById('download-sap-lead-tracker');
    const status = document.getElementById('download-sap-lead-status');
    if (!button || !status) return;
    button.disabled = true;
    status.textContent = ' Building workbook from current site data…';
    try {
      if (!window.XLSX) throw new Error('Spreadsheet library did not load.');
      const roadmap = parseRoadmap();
      const factory = await loadFactory();
      const workbook = buildWorkbook(roadmap, factory);
      XLSX.writeFileXLSX(workbook, FILE_NAME, { compression: true });
      status.textContent = ' Workbook generated from the current Career Factory.';
    } catch (error) {
      console.error(error);
      status.textContent = ' Workbook generation failed. Please retry.';
    } finally {
      button.disabled = false;
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('download-sap-lead-tracker');
    if (button) button.addEventListener('click', downloadWorkbook);
    refreshMetrics();
  });
}());
