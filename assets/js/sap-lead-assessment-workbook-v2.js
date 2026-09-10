(function () {
  'use strict';

  const FACTORY_URL = '/ai/career-factory.json';
  const FILE_NAME = 'sap-lead-assessment-master.xlsx';
  const STATUS_DEFAULT = 'Not Started';
  const TIER_PRIORITY = { core: 'P1', cross_boundary: 'P2', differentiator: 'P3' };

  function asList(value) { return Array.isArray(value) ? value : []; }
  function asText(value) { return value === null || value === undefined ? '' : String(value); }
  function absoluteUrl(path) {
    if (!path) return '';
    if (/^https?:\/\//i.test(path)) return path;
    return 'https://dkharlanau.github.io' + (path.startsWith('/') ? path : '/' + path);
  }
  function parseJsonNode(id) {
    const node = document.getElementById(id);
    if (!node) throw new Error('Missing data node: ' + id);
    return JSON.parse(node.textContent);
  }
  async function loadFactory() {
    const response = await fetch(FACTORY_URL, { cache: 'no-store' });
    if (!response.ok) throw new Error('Career Factory data is unavailable.');
    return response.json();
  }

  function inferComponent(item) {
    const value = (asText(item.route) + ' ' + asText(item.title)).toLowerCase();
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
      ['Integration Operations', ['integration-operations', 'idoc', 'qrfc', 'trfc', 'interface operations']],
      ['SAP Inventory Management', ['inventory-management', 'inventory management', 'movement type']],
      ['SAP Kanban', ['\/kanban', 'kanban']],
      ['SAP Logistics', ['logistics-capabilities', 'logistics']],
      ['SAP Master Data', ['master-data', 'material-behavior', 'material master']],
      ['SAP MDG / DRF', ['\/mdg', '\/drf', 'master data governance', 'data replication framework']],
      ['SAP Migration', ['migration', 'migration cockpit', 'data migration']],
      ['SAP Performance', ['performance', 'sm50', 'sm12', 'sm13', 'sm58', 'smq1', 'smq2', 'st03n', 'st05']],
      ['SAP Pricing', ['\/pricing', 'pricing']],
      ['SAP Procurement / MM', ['\/procurement', 'procure-to-pay', 'purchasing']],
      ['SAP Production / PP', ['\/production', 'production planning']],
      ['SAP Quality Management', ['quality-management', 'quality management']],
      ['SAP Sales / SD', ['sales-processes', 'sales-order', 'sales-diagnostics']],
      ['SAP Shipping', ['\/shipping', 'shipping', 'delivery execution']],
      ['SAP Tax', ['\/tax', 'tax']],
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

  function addSheet(workbook, name, rows, widths, withFilter) {
    const sheet = XLSX.utils.aoa_to_sheet(rows);
    sheet['!cols'] = widths.map(function (wch) { return { wch: wch }; });
    if (withFilter && rows.length > 1) {
      const end = XLSX.utils.encode_col(rows[0].length - 1) + rows.length;
      sheet['!autofilter'] = { ref: 'A1:' + end };
    }
    XLSX.utils.book_append_sheet(workbook, sheet, name.substring(0, 31));
    return sheet;
  }

  function skillPriority(skill) { return TIER_PRIORITY[skill.tier] || 'P2'; }
  function sourceSummary(skill) {
    return asList(skill.sources).map(function (source) {
      return asText(source.label) + ' — ' + absoluteUrl(source.href);
    }).join('\n');
  }
  function suggestedSkillIds(item) {
    return asList(item.suggested_skills).map(function (candidate) { return asText(candidate.skill_id); }).filter(Boolean);
  }
  function topicPriority(item, skillById) {
    const ids = asList(item.skills).concat(suggestedSkillIds(item));
    let best = 'P3';
    ids.forEach(function (id) {
      const priority = skillById[id] ? skillPriority(skillById[id]) : 'P2';
      if (priority === 'P1') best = 'P1';
      else if (priority === 'P2' && best === 'P3') best = 'P2';
    });
    return item.state === 'needs_decision' && ids.length === 0 ? 'P2' : best;
  }

  function buildWorkbook(roadmap, requirementsModel, factory) {
    const workbook = XLSX.utils.book_new();
    const skills = asList(roadmap.skills);
    const requirements = asList(requirementsModel.requirements);
    const domains = requirementsModel.domains || {};
    const tracks = roadmap.tracks || {};
    const labs = asList(factory.lab_inventory);
    const skillById = {};
    const routeSet = {};
    skills.forEach(function (skill) { skillById[skill.id] = skill; });
    labs.forEach(function (item) { if (item.route) routeSet[item.route] = true; });

    const p1Required = requirements.filter(function (item) { return item.priority === 'P1'; }).length;
    const requiredCovered = requirements.filter(function (item) {
      return asList(item.sources).some(function (route) { return !!routeSet[route]; });
    }).length;
    const mappedLabs = labs.filter(function (item) { return item.state === 'mapped'; }).length;
    const needsDecision = labs.filter(function (item) { return item.state === 'needs_decision'; }).length;

    addSheet(workbook, 'Dashboard', [
      ['SAP Lead Assessment Master Workbook'],
      ['Three layers: required assessment topics, Lead capabilities, and the complete site inventory.'],
      [],
      ['Metric', 'Value'],
      ['Assessment requirements', requirements.length],
      ['P1 required topics', p1Required],
      ['Lead skills', skills.length],
      ['Lab pages', labs.length],
      ['Required topics with at least one exact source page', requiredCovered],
      ['Mapped Lab pages', mappedLabs],
      ['Lab pages needing career mapping', needsDecision],
      ['Career decision coverage', factory.summary && factory.summary.decision_coverage_percent !== undefined ? factory.summary.decision_coverage_percent + '%' : ''],
      [],
      ['Preparation rule'],
      ['1', 'Start with Required Topics and filter P1.'],
      ['2', 'Answer the prompt from memory before opening a source page.'],
      ['3', 'Use Lead Skills to move from configuration detail to design, diagnosis and leadership.'],
      ['4', 'Use Site Topics when you need deeper component material.'],
      ['5', 'Add one real project example before you mark a topic Ready.']
    ], [8, 92], false);

    const reqRows = [[
      'Domain', 'Component', 'Requirement ID', 'Required Topic', 'Priority', 'Assessment Prompt',
      'Source Pages', 'Site Coverage', 'Confidence (1-5)', 'Status', 'Last Review', 'Next Review',
      'Project Example', 'Notes'
    ]];
    requirements.forEach(function (item) {
      const domain = domains[item.domain] || {};
      const sources = asList(item.sources);
      const covered = sources.some(function (route) { return !!routeSet[route]; });
      reqRows.push([
        domain.label || item.domain, item.component, item.id, item.title, item.priority, item.prompt,
        sources.map(absoluteUrl).join('\n'), covered ? 'Covered' : 'Check source', 1, STATUS_DEFAULT, '', '', '', ''
      ]);
    });
    addSheet(workbook, 'Required Topics', reqRows, [34, 26, 28, 46, 10, 66, 74, 16, 16, 16, 14, 14, 48, 42], true);

    Object.keys(domains).sort(function (a, b) {
      return (domains[a].order || 999) - (domains[b].order || 999);
    }).forEach(function (domainId) {
      const rows = [['Component', 'Requirement ID', 'Required Topic', 'Priority', 'Assessment Prompt', 'Sources', 'Confidence (1-5)', 'Status', 'Project Example', 'Notes']];
      requirements.filter(function (item) { return item.domain === domainId; }).forEach(function (item) {
        rows.push([item.component, item.id, item.title, item.priority, item.prompt, asList(item.sources).map(absoluteUrl).join('\n'), 1, STATUS_DEFAULT, '', '']);
      });
      addSheet(workbook, domains[domainId].label || domainId, rows, [28, 28, 44, 10, 64, 72, 16, 16, 48, 42], true);
    });

    const skillRows = [['Track', 'Skill ID', 'Skill', 'Tier', 'Priority', 'Capabilities', 'Why it matters', 'Interview signal', 'Sources', 'Confidence (1-5)', 'Status', 'Project Example', 'Notes']];
    skills.forEach(function (skill) {
      const track = tracks[skill.track] || {};
      skillRows.push([track.label || skill.track, skill.id, skill.title, skill.tier, skillPriority(skill), asList(skill.capabilities).join(', '), skill.why, skill.interview_signal, sourceSummary(skill), 1, STATUS_DEFAULT, '', '']);
    });
    addSheet(workbook, 'Lead Skills', skillRows, [30, 26, 42, 18, 10, 26, 60, 60, 74, 16, 16, 48, 42], true);

    const siteRows = [['Component / Area', 'Topic', 'Route', 'Source File', 'Career State', 'Career Impact', 'Mapped Skills', 'Suggested Skills', 'Priority', 'Confidence (1-5)', 'Status', 'URL', 'Notes']];
    labs.forEach(function (item) {
      siteRows.push([inferComponent(item), item.title, item.route, item.source_file, item.state, item.career_impact, asList(item.skills).join(', '), suggestedSkillIds(item).join(', '), topicPriority(item, skillById), 1, STATUS_DEFAULT, absoluteUrl(item.route), '']);
    });
    addSheet(workbook, 'Site Topics', siteRows, [30, 50, 50, 56, 18, 18, 34, 34, 10, 16, 16, 60, 42], true);

    const componentMap = {};
    function componentBucket(name) {
      if (!componentMap[name]) componentMap[name] = { required: 0, p1: 0, pages: 0, mapped: 0, gaps: 0 };
      return componentMap[name];
    }
    requirements.forEach(function (item) {
      const bucket = componentBucket(item.component || 'Other / Cross-domain');
      bucket.required += 1;
      if (item.priority === 'P1') bucket.p1 += 1;
    });
    labs.forEach(function (item) {
      const bucket = componentBucket(inferComponent(item));
      bucket.pages += 1;
      if (item.state === 'mapped') bucket.mapped += 1;
      if (item.state === 'needs_decision') bucket.gaps += 1;
    });
    const componentRows = [['Component / Area', 'Required Topics', 'P1 Required', 'Site Pages', 'Mapped Pages', 'Career Mapping Gaps']];
    Object.keys(componentMap).sort().forEach(function (name) {
      const bucket = componentMap[name];
      componentRows.push([name, bucket.required, bucket.p1, bucket.pages, bucket.mapped, bucket.gaps]);
    });
    addSheet(workbook, 'Components', componentRows, [38, 16, 14, 14, 16, 20], true);

    const gapRows = [['Component / Area', 'Topic', 'Route', 'Suggested Skills', 'Priority', 'URL', 'Decision / Notes']];
    labs.filter(function (item) { return item.state === 'needs_decision'; }).forEach(function (item) {
      gapRows.push([inferComponent(item), item.title, item.route, suggestedSkillIds(item).join(', '), topicPriority(item, skillById), absoluteUrl(item.route), '']);
    });
    addSheet(workbook, 'Needs Mapping', gapRows, [32, 52, 52, 38, 10, 60, 48], true);

    const sprintRows = [['Date', 'Domain', 'Topic', 'Goal', '20-minute Block', 'Result / Gap', 'Next Action', 'Done']];
    for (let i = 0; i < 30; i += 1) sprintRows.push(['', '', '', '', 'Recall → review → project example', '', '', 'No']);
    addSheet(workbook, 'Daily Sprint', sprintRows, [14, 30, 44, 44, 36, 44, 44, 10], true);

    addSheet(workbook, 'How to Use', [
      ['Rule', 'Action'],
      ['1. Required Topics are the syllabus', 'This sheet is the detailed assessment programme. Start with P1.'],
      ['2. Lead Skills are the capability model', 'Use them to turn module knowledge into diagnosis, architecture and leadership answers.'],
      ['3. Site Topics are the knowledge inventory', 'Every Lab page is visible, but not every page is automatically mandatory for the assessment.'],
      ['4. Recall before reading', 'Answer from memory first. Study the gap in your answer, not the whole page again.'],
      ['5. Add project evidence', 'For important topics, add one real incident, design decision, trade-off or result.'],
      ['6. Rate confidence', '1 = cannot explain; 3 = can explain basics; 5 = can lead a design or troubleshooting discussion.'],
      ['7. Ready has a strict meaning', 'You can explain purpose, flow, one design decision, one failure path and one project example.'],
      ['8. Needs Mapping is content debt', 'These Lab pages exist but still need a career decision. Keep them visible until mapped or explicitly excluded.'],
      ['9. Regenerate instead of maintaining manually', 'Generate a new workbook after Career Factory or Assessment Requirements changes.']
    ], [34, 108], true);

    workbook.Props = { Title: 'SAP Lead Assessment Master Workbook', Subject: 'SAP Lead assessment preparation', Author: 'DKHARLANAU.github.io', Comments: 'Generated from Assessment Requirements, Career Roadmap and Career Factory.' };
    return workbook;
  }

  function setMetric(id, value) {
    const node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  async function refreshMetrics() {
    try {
      const roadmap = parseJsonNode('sap-lead-roadmap-data');
      const requirements = parseJsonNode('sap-lead-requirements-data');
      const factory = await loadFactory();
      const reqs = asList(requirements.requirements);
      setMetric('sap-lead-required-count', reqs.length);
      setMetric('sap-lead-p1-count', reqs.filter(function (item) { return item.priority === 'P1'; }).length);
      setMetric('sap-lead-skill-count', asList(roadmap.skills).length);
      setMetric('sap-lead-page-count', asList(factory.lab_inventory).length);
      setMetric('sap-lead-gap-count', asList(factory.lab_inventory).filter(function (item) { return item.state === 'needs_decision'; }).length);
      setMetric('sap-lead-coverage', factory.summary && factory.summary.decision_coverage_percent !== undefined ? factory.summary.decision_coverage_percent + '%' : '—');
    } catch (error) {
      console.error(error);
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
      const roadmap = parseJsonNode('sap-lead-roadmap-data');
      const requirements = parseJsonNode('sap-lead-requirements-data');
      const factory = await loadFactory();
      XLSX.writeFileXLSX(buildWorkbook(roadmap, requirements, factory), FILE_NAME, { compression: true });
      status.textContent = ' Workbook generated from the current assessment model and site inventory.';
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
