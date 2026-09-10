(function () {
  'use strict';

  const FACTORY_URL = '/ai/career-factory.json';
  const FILE_NAME = 'sap-lead-assessment-master.xlsx';
  const STATUS_DEFAULT = 'Not Started';
  const TIER_PRIORITY = { core: 'P1', cross_boundary: 'P2', differentiator: 'P3' };
  const MIME_XLSX = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';

  function asList(value) { return Array.isArray(value) ? value : []; }
  function asText(value) { return value === null || value === undefined ? '' : String(value); }
  function cell(value) {
    if (value === null || value === undefined) return '';
    if (typeof value === 'string' || typeof value === 'number' || typeof value === 'boolean') return value;
    try { return JSON.stringify(value); } catch (_) { return String(value); }
  }
  function absoluteUrl(path) {
    if (!path) return '';
    if (/^https?:\/\//i.test(path)) return path;
    return 'https://dkharlanau.github.io' + (path.startsWith('/') ? path : '/' + path);
  }
  function parseJsonNode(id) {
    const node = document.getElementById(id);
    if (!node) throw new Error('Missing embedded data: ' + id);
    return JSON.parse(node.textContent);
  }
  async function loadFactory() {
    const response = await fetch(FACTORY_URL, { cache: 'no-store' });
    if (!response.ok) throw new Error('Career Factory data returned HTTP ' + response.status + '.');
    return response.json();
  }

  function inferComponent(item) {
    const value = (asText(item.route) + ' ' + asText(item.title)).toLowerCase();
    const rules = [
      ['SAP AIF', ['/aif', 'application interface framework']],
      ['SAP aATP / ATP', ['/atp', 'available-to-promise', 'available to promise']],
      ['SAP Automotive JIT/JIS', ['automotive-jit', 'just-in-time', 'just-in-sequence']],
      ['SAP Billing', ['/billing', 'billing']],
      ['Business Partner / CVI', ['business-partner', 'business partner', 'cvi']],
      ['Condition Contract Management', ['condition-contract-management', 'condition contract']],
      ['SAP Credit Management', ['/credit', 'credit management']],
      ['Data Governance', ['data-governance', 'data governance']],
      ['S/4HANA Deployment Models', ['deployment-models', 'public cloud', 'private cloud']],
      ['ABAP / Extensibility', ['/development', 'extensibility', 'clean core']],
      ['Analytics / Observability', ['end-to-end-analytics', 'observability', 'analytics']],
      ['SAP EWM', ['/ewm', 'extended warehouse management']],
      ['Integration Architecture', ['/integrations', 'integration architecture']],
      ['Integration Operations', ['integration-operations', 'idoc', 'qrfc', 'trfc', 'interface operations']],
      ['SAP Inventory Management', ['inventory-management', 'inventory management', 'movement type']],
      ['SAP Kanban', ['/kanban', 'kanban']],
      ['SAP Logistics', ['logistics-capabilities', 'logistics']],
      ['SAP Master Data', ['master-data', 'material-behavior', 'material master']],
      ['SAP MDG / DRF', ['/mdg', '/drf', 'master data governance', 'data replication framework']],
      ['SAP Migration', ['migration', 'migration cockpit', 'data migration']],
      ['SAP Performance', ['performance', 'sm50', 'sm12', 'sm13', 'sm58', 'smq1', 'smq2', 'st03n', 'st05']],
      ['SAP Pricing', ['/pricing', 'pricing']],
      ['SAP Procurement / MM', ['/procurement', 'procure-to-pay', 'purchasing']],
      ['SAP Production / PP', ['/production', 'production planning']],
      ['SAP Quality Management', ['quality-management', 'quality management']],
      ['SAP Sales / SD', ['sales-processes', 'sales-order', 'sales-diagnostics']],
      ['SAP Shipping', ['/shipping', 'shipping', 'delivery execution']],
      ['SAP Tax', ['/tax', 'tax']],
      ['SAP TM', ['transportation-management', 'transportation management']],
      ['Variant Configuration', ['variant-configuration', 'variant configuration']],
      ['Business AI', ['business-ai', 'business ai']],
      ['AI / RAG / Agents', ['ai-ready', 'rag', 'agent', 'mcp', 'retrieval']],
      ['Assessment Practice', ['/assessment', 'assessment']],
      ['Interview Readiness', ['interview-readiness', 'interview']],
      ['Reusable Data Procedures', ['reusable-data-procedures']],
      ['Enterprise Assurance', ['enterprise-assurance']],
      ['Tooling / Roadmap', ['tool-roadmap']],
      ['Templates / Work Artifacts', ['/templates', 'template']]
    ];
    for (const rule of rules) {
      if (rule[1].some(function (token) { return value.indexOf(token) !== -1; })) return rule[0];
    }
    return 'Other / Cross-domain';
  }

  function safeSheetName(existingNames, name) {
    let base = asText(name || 'Sheet')
      .replace(/[\\\/?*\[\]:]/g, '-')
      .replace(/\s+/g, ' ')
      .trim();
    base = (base || 'Sheet').substring(0, 31);
    let candidate = base;
    let index = 2;
    while (existingNames.indexOf(candidate) !== -1) {
      const suffix = ' ' + index;
      candidate = base.substring(0, 31 - suffix.length) + suffix;
      index += 1;
    }
    return candidate;
  }

  function skillPriority(skill) { return TIER_PRIORITY[skill.tier] || 'P2'; }
  function sourceSummary(skill) {
    return asList(skill.sources).map(function (source) {
      return asText(source.label) + ' — ' + absoluteUrl(source.href);
    }).join('\n');
  }
  function suggestedSkillIds(item) {
    return asList(item.suggested_skills).map(function (candidate) {
      if (typeof candidate === 'string') return candidate;
      return asText(candidate && candidate.skill_id);
    }).filter(Boolean);
  }
  function topicPriority(item, skillById) {
    const ids = asList(item.skills).map(asText).concat(suggestedSkillIds(item));
    let best = 'P3';
    ids.forEach(function (id) {
      const priority = skillById[id] ? skillPriority(skillById[id]) : 'P2';
      if (priority === 'P1') best = 'P1';
      else if (priority === 'P2' && best === 'P3') best = 'P2';
    });
    return item.state === 'needs_decision' && ids.length === 0 ? 'P2' : best;
  }

  function sheet(name, rows, widths, withFilter) {
    return { name: name, rows: rows, widths: widths, withFilter: !!withFilter };
  }

  function buildSheetModel(roadmap, requirementsModel, factory) {
    const sheets = [];
    const skills = asList(roadmap.skills);
    const requirements = asList(requirementsModel.requirements);
    const domains = requirementsModel.domains || {};
    const tracks = roadmap.tracks || {};
    const labs = asList(factory.lab_inventory);
    const skillById = {};
    const routeSet = {};

    skills.forEach(function (skill) { if (skill && skill.id) skillById[skill.id] = skill; });
    labs.forEach(function (item) { if (item && item.route) routeSet[item.route] = true; });

    const p1Required = requirements.filter(function (item) { return item.priority === 'P1'; }).length;
    const requiredCovered = requirements.filter(function (item) {
      return asList(item.sources).some(function (route) { return !!routeSet[route]; });
    }).length;
    const mappedLabs = labs.filter(function (item) { return item.state === 'mapped'; }).length;
    const needsDecision = labs.filter(function (item) { return item.state === 'needs_decision'; }).length;

    sheets.push(sheet('Dashboard', [
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
    ], [8, 92], false));

    const reqRows = [['Domain', 'Component', 'Requirement ID', 'Required Topic', 'Priority', 'Assessment Prompt', 'Source Pages', 'Site Coverage', 'Confidence (1-5)', 'Status', 'Last Review', 'Next Review', 'Project Example', 'Notes']];
    requirements.forEach(function (item) {
      const domain = domains[item.domain] || {};
      const sources = asList(item.sources);
      const covered = sources.some(function (route) { return !!routeSet[route]; });
      reqRows.push([domain.label || item.domain, item.component, item.id, item.title, item.priority, item.prompt, sources.map(absoluteUrl).join('\n'), covered ? 'Covered' : 'Check source', 1, STATUS_DEFAULT, '', '', '', '']);
    });
    sheets.push(sheet('Required Topics', reqRows, [34, 26, 28, 46, 10, 66, 74, 16, 16, 16, 14, 14, 48, 42], true));

    Object.keys(domains).sort(function (a, b) { return (domains[a].order || 999) - (domains[b].order || 999); }).forEach(function (domainId) {
      const rows = [['Component', 'Requirement ID', 'Required Topic', 'Priority', 'Assessment Prompt', 'Sources', 'Confidence (1-5)', 'Status', 'Project Example', 'Notes']];
      requirements.filter(function (item) { return item.domain === domainId; }).forEach(function (item) {
        rows.push([item.component, item.id, item.title, item.priority, item.prompt, asList(item.sources).map(absoluteUrl).join('\n'), 1, STATUS_DEFAULT, '', '']);
      });
      sheets.push(sheet(domains[domainId].label || domainId, rows, [28, 28, 44, 10, 64, 72, 16, 16, 48, 42], true));
    });

    const skillRows = [['Track', 'Skill ID', 'Skill', 'Tier', 'Priority', 'Capabilities', 'Why it matters', 'Interview signal', 'Sources', 'Confidence (1-5)', 'Status', 'Project Example', 'Notes']];
    skills.forEach(function (skill) {
      const track = tracks[skill.track] || {};
      skillRows.push([track.label || skill.track, skill.id, skill.title, skill.tier, skillPriority(skill), asList(skill.capabilities).join(', '), skill.why, skill.interview_signal, sourceSummary(skill), 1, STATUS_DEFAULT, '', '']);
    });
    sheets.push(sheet('Lead Skills', skillRows, [30, 26, 42, 18, 10, 26, 60, 60, 74, 16, 16, 48, 42], true));

    const siteRows = [['Component / Area', 'Topic', 'Route', 'Source File', 'Career State', 'Career Impact', 'Mapped Skills', 'Suggested Skills', 'Priority', 'Confidence (1-5)', 'Status', 'URL', 'Notes']];
    labs.forEach(function (item) {
      siteRows.push([inferComponent(item), item.title, item.route, item.source_file, item.state, item.career_impact, asList(item.skills).join(', '), suggestedSkillIds(item).join(', '), topicPriority(item, skillById), 1, STATUS_DEFAULT, absoluteUrl(item.route), '']);
    });
    sheets.push(sheet('Site Topics', siteRows, [30, 50, 50, 56, 18, 18, 34, 34, 10, 16, 16, 60, 42], true));

    const componentMap = {};
    function bucket(name) {
      const key = asText(name || 'Other / Cross-domain');
      if (!componentMap[key]) componentMap[key] = { required: 0, p1: 0, pages: 0, mapped: 0, gaps: 0 };
      return componentMap[key];
    }
    requirements.forEach(function (item) {
      const itemBucket = bucket(item.component);
      itemBucket.required += 1;
      if (item.priority === 'P1') itemBucket.p1 += 1;
    });
    labs.forEach(function (item) {
      const itemBucket = bucket(inferComponent(item));
      itemBucket.pages += 1;
      if (item.state === 'mapped') itemBucket.mapped += 1;
      if (item.state === 'needs_decision') itemBucket.gaps += 1;
    });
    const componentRows = [['Component / Area', 'Required Topics', 'P1 Required', 'Site Pages', 'Mapped Pages', 'Career Mapping Gaps']];
    Object.keys(componentMap).sort().forEach(function (name) {
      const itemBucket = componentMap[name];
      componentRows.push([name, itemBucket.required, itemBucket.p1, itemBucket.pages, itemBucket.mapped, itemBucket.gaps]);
    });
    sheets.push(sheet('Components', componentRows, [38, 16, 14, 14, 16, 20], true));

    const gapRows = [['Component / Area', 'Topic', 'Route', 'Suggested Skills', 'Priority', 'URL', 'Decision / Notes']];
    labs.filter(function (item) { return item.state === 'needs_decision'; }).forEach(function (item) {
      gapRows.push([inferComponent(item), item.title, item.route, suggestedSkillIds(item).join(', '), topicPriority(item, skillById), absoluteUrl(item.route), '']);
    });
    sheets.push(sheet('Needs Mapping', gapRows, [32, 52, 52, 38, 10, 60, 48], true));

    const sprintRows = [['Date', 'Domain', 'Topic', 'Goal', '20-minute Block', 'Result / Gap', 'Next Action', 'Done']];
    for (let i = 0; i < 30; i += 1) sprintRows.push(['', '', '', '', 'Recall → review → project example', '', '', 'No']);
    sheets.push(sheet('Daily Sprint', sprintRows, [14, 30, 44, 44, 36, 44, 44, 10], true));

    sheets.push(sheet('How to Use', [
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
    ], [34, 108], true));

    const usedNames = [];
    sheets.forEach(function (item) {
      item.name = safeSheetName(usedNames, item.name);
      usedNames.push(item.name);
    });
    return sheets;
  }

  function xmlEscape(value) {
    return asText(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&apos;');
  }
  function columnName(index) {
    let n = index + 1;
    let out = '';
    while (n > 0) {
      n -= 1;
      out = String.fromCharCode(65 + (n % 26)) + out;
      n = Math.floor(n / 26);
    }
    return out;
  }
  function cellXml(value, ref) {
    const normalized = cell(value);
    if (typeof normalized === 'number' && Number.isFinite(normalized)) {
      return '<c r="' + ref + '" t="n"><v>' + normalized + '</v></c>';
    }
    if (typeof normalized === 'boolean') {
      return '<c r="' + ref + '" t="b"><v>' + (normalized ? '1' : '0') + '</v></c>';
    }
    const text = asText(normalized);
    if (!text) return '<c r="' + ref + '" t="inlineStr"><is><t></t></is></c>';
    return '<c r="' + ref + '" t="inlineStr"><is><t xml:space="preserve">' + xmlEscape(text) + '</t></is></c>';
  }
  function worksheetXml(model) {
    const rows = asList(model.rows);
    const cols = asList(model.widths).map(function (width, index) {
      const col = index + 1;
      return '<col min="' + col + '" max="' + col + '" width="' + Number(width || 12) + '" customWidth="1"/>';
    }).join('');
    const data = rows.map(function (row, rowIndex) {
      const r = rowIndex + 1;
      const cells = asList(row).map(function (value, colIndex) {
        return cellXml(value, columnName(colIndex) + r);
      }).join('');
      return '<row r="' + r + '">' + cells + '</row>';
    }).join('');
    let filter = '';
    if (model.withFilter && rows.length > 1 && asList(rows[0]).length > 0) {
      filter = '<autoFilter ref="A1:' + columnName(rows[0].length - 1) + rows.length + '"/>';
    }
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">' +
      (cols ? '<cols>' + cols + '</cols>' : '') +
      '<sheetData>' + data + '</sheetData>' + filter + '</worksheet>';
  }

  function contentTypesXml(sheetCount) {
    let sheetOverrides = '';
    for (let i = 1; i <= sheetCount; i += 1) {
      sheetOverrides += '<Override PartName="/xl/worksheets/sheet' + i + '.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>';
    }
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">' +
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>' +
      '<Default Extension="xml" ContentType="application/xml"/>' +
      '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>' +
      '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>' +
      '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>' +
      '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>' +
      sheetOverrides + '</Types>';
  }
  function rootRelsXml() {
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
      '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>' +
      '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>' +
      '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>' +
      '</Relationships>';
  }
  function workbookXml(models) {
    const entries = models.map(function (model, index) {
      return '<sheet name="' + xmlEscape(model.name) + '" sheetId="' + (index + 1) + '" r:id="rId' + (index + 1) + '"/>';
    }).join('');
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">' +
      '<bookViews><workbookView activeTab="0"/></bookViews><sheets>' + entries + '</sheets></workbook>';
  }
  function workbookRelsXml(sheetCount) {
    let rels = '';
    for (let i = 1; i <= sheetCount; i += 1) {
      rels += '<Relationship Id="rId' + i + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet' + i + '.xml"/>';
    }
    rels += '<Relationship Id="rId' + (sheetCount + 1) + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>';
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + rels + '</Relationships>';
  }
  function stylesXml() {
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">' +
      '<fonts count="1"><font><sz val="11"/><name val="Calibri"/><family val="2"/></font></fonts>' +
      '<fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>' +
      '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>' +
      '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>' +
      '<cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>' +
      '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>' +
      '</styleSheet>';
  }
  function appXml(models) {
    const titles = models.map(function (model) { return '<vt:lpstr>' + xmlEscape(model.name) + '</vt:lpstr>'; }).join('');
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">' +
      '<Application>DKHARLANAU.github.io</Application><DocSecurity>0</DocSecurity><ScaleCrop>false</ScaleCrop>' +
      '<HeadingPairs><vt:vector size="2" baseType="variant"><vt:variant><vt:lpstr>Worksheets</vt:lpstr></vt:variant><vt:variant><vt:i4>' + models.length + '</vt:i4></vt:variant></vt:vector></HeadingPairs>' +
      '<TitlesOfParts><vt:vector size="' + models.length + '" baseType="lpstr">' + titles + '</vt:vector></TitlesOfParts>' +
      '<Company></Company><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc><HyperlinksChanged>false</HyperlinksChanged><AppVersion>1.0</AppVersion></Properties>';
  }
  function coreXml() {
    const now = new Date().toISOString();
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' +
      '<dc:title>SAP Lead Assessment Master Workbook</dc:title><dc:subject>SAP Lead assessment preparation</dc:subject><dc:creator>DKHARLANAU.github.io</dc:creator>' +
      '<cp:lastModifiedBy>DKHARLANAU.github.io</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">' + now + '</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">' + now + '</dcterms:modified></cp:coreProperties>';
  }

  const CRC_TABLE = (function () {
    const table = new Uint32Array(256);
    for (let n = 0; n < 256; n += 1) {
      let c = n;
      for (let k = 0; k < 8; k += 1) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
      table[n] = c >>> 0;
    }
    return table;
  }());
  function crc32(bytes) {
    let crc = 0xFFFFFFFF;
    for (let i = 0; i < bytes.length; i += 1) crc = CRC_TABLE[(crc ^ bytes[i]) & 0xFF] ^ (crc >>> 8);
    return (crc ^ 0xFFFFFFFF) >>> 0;
  }
  function dosDateTime(date) {
    const year = Math.max(1980, date.getFullYear());
    const dosTime = ((date.getHours() & 31) << 11) | ((date.getMinutes() & 63) << 5) | ((Math.floor(date.getSeconds() / 2)) & 31);
    const dosDate = (((year - 1980) & 127) << 9) | (((date.getMonth() + 1) & 15) << 5) | (date.getDate() & 31);
    return { time: dosTime, date: dosDate };
  }
  function u16(view, offset, value) { view.setUint16(offset, value, true); }
  function u32(view, offset, value) { view.setUint32(offset, value >>> 0, true); }
  function concatParts(parts) {
    const total = parts.reduce(function (sum, part) { return sum + part.length; }, 0);
    const out = new Uint8Array(total);
    let offset = 0;
    parts.forEach(function (part) { out.set(part, offset); offset += part.length; });
    return out;
  }
  function zipStore(files) {
    const encoder = new TextEncoder();
    const now = dosDateTime(new Date());
    const localParts = [];
    const centralParts = [];
    let localOffset = 0;

    files.forEach(function (file) {
      const nameBytes = encoder.encode(file.name);
      const dataBytes = typeof file.data === 'string' ? encoder.encode(file.data) : file.data;
      const crc = crc32(dataBytes);

      const local = new Uint8Array(30 + nameBytes.length);
      const lv = new DataView(local.buffer);
      u32(lv, 0, 0x04034B50); u16(lv, 4, 20); u16(lv, 6, 0x0800); u16(lv, 8, 0);
      u16(lv, 10, now.time); u16(lv, 12, now.date); u32(lv, 14, crc); u32(lv, 18, dataBytes.length); u32(lv, 22, dataBytes.length);
      u16(lv, 26, nameBytes.length); u16(lv, 28, 0); local.set(nameBytes, 30);
      localParts.push(local, dataBytes);

      const central = new Uint8Array(46 + nameBytes.length);
      const cv = new DataView(central.buffer);
      u32(cv, 0, 0x02014B50); u16(cv, 4, 20); u16(cv, 6, 20); u16(cv, 8, 0x0800); u16(cv, 10, 0);
      u16(cv, 12, now.time); u16(cv, 14, now.date); u32(cv, 16, crc); u32(cv, 20, dataBytes.length); u32(cv, 24, dataBytes.length);
      u16(cv, 28, nameBytes.length); u16(cv, 30, 0); u16(cv, 32, 0); u16(cv, 34, 0); u16(cv, 36, 0); u32(cv, 38, 0); u32(cv, 42, localOffset);
      central.set(nameBytes, 46); centralParts.push(central);

      localOffset += local.length + dataBytes.length;
    });

    const localData = concatParts(localParts);
    const centralData = concatParts(centralParts);
    const end = new Uint8Array(22);
    const ev = new DataView(end.buffer);
    u32(ev, 0, 0x06054B50); u16(ev, 4, 0); u16(ev, 6, 0); u16(ev, 8, files.length); u16(ev, 10, files.length);
    u32(ev, 12, centralData.length); u32(ev, 16, localData.length); u16(ev, 20, 0);
    return concatParts([localData, centralData, end]);
  }

  function createXlsxBytes(models) {
    const files = [
      { name: '[Content_Types].xml', data: contentTypesXml(models.length) },
      { name: '_rels/.rels', data: rootRelsXml() },
      { name: 'docProps/app.xml', data: appXml(models) },
      { name: 'docProps/core.xml', data: coreXml() },
      { name: 'xl/workbook.xml', data: workbookXml(models) },
      { name: 'xl/_rels/workbook.xml.rels', data: workbookRelsXml(models.length) },
      { name: 'xl/styles.xml', data: stylesXml() }
    ];
    models.forEach(function (model, index) {
      files.push({ name: 'xl/worksheets/sheet' + (index + 1) + '.xml', data: worksheetXml(model) });
    });
    return zipStore(files);
  }

  function setMetric(id, value) {
    const node = document.getElementById(id);
    if (node) node.textContent = value;
  }
  function setStatus(message) {
    const status = document.getElementById('download-sap-lead-status');
    if (status) status.textContent = message;
  }
  function setLinkReady(link, objectUrl) {
    link.href = objectUrl;
    link.download = FILE_NAME;
    link.setAttribute('aria-disabled', 'false');
    link.textContent = 'Download current Excel workbook';
  }
  function setLinkDisabled(link, label) {
    link.href = '#';
    link.removeAttribute('download');
    link.setAttribute('aria-disabled', 'true');
    link.textContent = label;
  }

  async function prepareWorkbook() {
    const link = document.getElementById('download-sap-lead-tracker');
    if (!link) return;

    setLinkDisabled(link, 'Preparing Excel workbook…');
    link.addEventListener('click', function (event) {
      if (link.getAttribute('aria-disabled') === 'true') event.preventDefault();
    });

    try {
      const roadmap = parseJsonNode('sap-lead-roadmap-data');
      const requirementsModel = parseJsonNode('sap-lead-requirements-data');
      const factory = await loadFactory();
      const requirements = asList(requirementsModel.requirements);
      const labs = asList(factory.lab_inventory);

      setMetric('sap-lead-required-count', requirements.length);
      setMetric('sap-lead-p1-count', requirements.filter(function (item) { return item.priority === 'P1'; }).length);
      setMetric('sap-lead-skill-count', asList(roadmap.skills).length);
      setMetric('sap-lead-page-count', labs.length);
      setMetric('sap-lead-gap-count', labs.filter(function (item) { return item.state === 'needs_decision'; }).length);
      setMetric('sap-lead-coverage', factory.summary && factory.summary.decision_coverage_percent !== undefined ? factory.summary.decision_coverage_percent + '%' : '—');

      setStatus(' Building the workbook…');
      const models = buildSheetModel(roadmap, requirementsModel, factory);
      const bytes = createXlsxBytes(models);
      const blob = new Blob([bytes], { type: MIME_XLSX });
      const objectUrl = URL.createObjectURL(blob);

      setLinkReady(link, objectUrl);
      setStatus(' Workbook ready. The download is generated from the current site data without external spreadsheet libraries.');
      window.addEventListener('pagehide', function () { URL.revokeObjectURL(objectUrl); }, { once: true });
    } catch (error) {
      console.error('SAP Lead workbook preparation failed:', error);
      setLinkDisabled(link, 'Workbook unavailable');
      setStatus(' Workbook preparation failed: ' + (error && error.message ? error.message : 'Unknown error.'));
    }
  }

  window.__SAP_LEAD_WORKBOOK_V4__ = {
    safeSheetName: safeSheetName,
    createXlsxBytes: createXlsxBytes,
    buildSheetModel: buildSheetModel
  };

  function boot() { prepareWorkbook(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, { once: true });
  else boot();
}());