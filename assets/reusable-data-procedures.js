(() => {
  'use strict';

  const app = document.querySelector('[data-rdp-app]');
  if (!app) return;

  const STORAGE_KEY = 'rdp.procedures.v1';
  const state = {
    tables: [],
    mappings: [],
    validations: [],
    resultRows: [],
    resultColumns: [],
    activeStep: 'files'
  };

  const $ = (selector, root = app) => root.querySelector(selector);
  const $$ = (selector, root = app) => Array.from(root.querySelectorAll(selector));
  const esc = (value) => String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
  const normalize = (value) => String(value ?? '').trim().toLowerCase().replace(/[^a-z0-9]+/g, '');
  const clamp = (value, min = 0, max = 1) => Math.max(min, Math.min(max, value));
  const percent = (value) => `${Math.round(clamp(value) * 100)}%`;
  const compactNumber = (value) => new Intl.NumberFormat('en', { notation: 'compact', maximumFractionDigits: 1 }).format(value || 0);
  const uid = (prefix = 'id') => `${prefix}-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;

  const dom = {
    status: $('[data-rdp-status]'),
    fileInput: $('[data-rdp-files]'),
    fileList: $('[data-rdp-file-list]'),
    dropzone: $('[data-rdp-dropzone]'),
    discovery: $('[data-rdp-discovery]'),
    discoverySummary: $('[data-rdp-discovery-summary]'),
    mappings: $('[data-rdp-mappings]'),
    validation: $('[data-rdp-validation]'),
    validationScore: $('[data-rdp-validation-score]'),
    resultSummary: $('[data-rdp-result-summary]'),
    resultTable: $('[data-rdp-result-table]'),
    exportCsv: $('[data-rdp-export-csv]'),
    saveForm: $('[data-rdp-save-form]'),
    savedList: $('[data-rdp-saved-list]'),
    importInput: $('[data-rdp-import]')
  };

  function setStatus(message, tone = '') {
    dom.status.textContent = message;
    dom.status.classList.toggle('is-error', tone === 'error');
    dom.status.classList.toggle('is-success', tone === 'success');
  }

  function goStep(step) {
    state.activeStep = step;
    $$('[data-rdp-step]').forEach((button) => button.classList.toggle('is-active', button.dataset.rdpStep === step));
    $$('[data-rdp-panel]').forEach((panel) => {
      const active = panel.dataset.rdpPanel === step;
      panel.hidden = !active;
      panel.classList.toggle('is-active', active);
    });
    if (step === 'discover') renderDiscovery();
    if (step === 'map') renderMappings();
    if (step === 'validate') runValidation();
    if (step === 'result') buildResult();
    if (step === 'save') renderSaved();
    const panel = $(`[data-rdp-panel="${step}"]`);
    panel?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function makeUniqueHeaders(row) {
    const seen = new Map();
    return row.map((value, index) => {
      const base = String(value ?? '').trim() || `Column_${index + 1}`;
      const count = seen.get(base) || 0;
      seen.set(base, count + 1);
      return count ? `${base}_${count + 1}` : base;
    });
  }

  function matrixToRows(matrix) {
    const nonEmpty = matrix.filter((row) => Array.isArray(row) && row.some((cell) => String(cell ?? '').trim() !== ''));
    if (!nonEmpty.length) return { rows: [], headers: [] };
    const headers = makeUniqueHeaders(nonEmpty[0]);
    const rows = nonEmpty.slice(1).map((row) => Object.fromEntries(headers.map((header, index) => [header, row[index] ?? null])));
    return { rows, headers };
  }

  function inferType(values) {
    const sample = values.filter((value) => value !== null && value !== undefined && String(value).trim() !== '').slice(0, 500);
    if (!sample.length) return 'empty';
    let numbers = 0;
    let dates = 0;
    let booleans = 0;
    sample.forEach((value) => {
      if (typeof value === 'number' && Number.isFinite(value)) numbers += 1;
      else if (value instanceof Date && !Number.isNaN(value.getTime())) dates += 1;
      else if (/^(true|false|yes|no|x)$/i.test(String(value).trim())) booleans += 1;
      else if (/^-?\d+(\.\d+)?$/.test(String(value).trim())) numbers += 1;
      else if (/^\d{4}[-/.]\d{1,2}[-/.]\d{1,2}/.test(String(value).trim())) dates += 1;
    });
    const threshold = sample.length * 0.85;
    if (numbers >= threshold) return 'number';
    if (dates >= threshold) return 'date';
    if (booleans >= threshold) return 'boolean';
    return 'text';
  }

  function profileTable(table) {
    table.columns = table.headers.map((name) => {
      const values = table.rows.map((row) => row[name]);
      const nonEmptyValues = values.filter((value) => value !== null && value !== undefined && String(value).trim() !== '');
      const normalizedValues = nonEmptyValues.map((value) => normalize(value)).filter(Boolean);
      const unique = new Set(normalizedValues);
      const completeness = table.rows.length ? nonEmptyValues.length / table.rows.length : 0;
      const uniqueness = nonEmptyValues.length ? unique.size / nonEmptyValues.length : 0;
      const type = inferType(nonEmptyValues);
      const keyScore = (uniqueness * 0.7) + (completeness * 0.3);
      return {
        name,
        type,
        completeness,
        uniqueness,
        keyScore,
        likelyKey: table.rows.length >= 3 && completeness >= 0.9 && uniqueness >= 0.92,
        samples: nonEmptyValues.slice(0, 4).map((value) => String(value)),
        distinctValues: Array.from(unique).slice(0, 500)
      };
    });
    return table;
  }

  function createTable(fileName, sheetName, matrix, explicitId = null) {
    const converted = matrixToRows(matrix);
    const table = {
      id: explicitId || uid('table'),
      fileName,
      sheetName,
      label: fileName === sheetName ? fileName : `${fileName} · ${sheetName}`,
      headers: converted.headers,
      rows: converted.rows,
      columns: []
    };
    return profileTable(table);
  }

  async function parseFiles(files) {
    if (!files.length) return;
    if (typeof window.XLSX === 'undefined') {
      setStatus('Spreadsheet parser did not load. Check the network connection and reload the page.', 'error');
      return;
    }
    setStatus(`Reading ${files.length} file${files.length === 1 ? '' : 's'} in the browser…`);
    const tables = [];
    for (const file of files) {
      try {
        const buffer = await file.arrayBuffer();
        const workbook = window.XLSX.read(buffer, { type: 'array', cellDates: true });
        workbook.SheetNames.forEach((sheetName) => {
          const matrix = window.XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], { header: 1, defval: null, raw: true });
          const table = createTable(file.name, sheetName, matrix);
          if (table.headers.length) tables.push(table);
        });
      } catch (error) {
        console.error(error);
        setStatus(`Could not read ${file.name}. The file may be damaged, encrypted, or in an unsupported format.`, 'error');
      }
    }
    state.tables = tables;
    state.mappings = suggestMappings(tables);
    state.validations = [];
    state.resultRows = [];
    renderFiles();
    renderDiscovery();
    renderMappings();
    updateNextButtons();
    if (tables.length) setStatus(`Loaded ${files.length} file${files.length === 1 ? '' : 's'} as ${tables.length} table${tables.length === 1 ? '' : 's'}. Discovery is ready.`, 'success');
  }

  function tokenSet(value) {
    return new Set(String(value || '').toLowerCase().split(/[^a-z0-9]+/).filter(Boolean));
  }

  function nameSimilarity(a, b) {
    const na = normalize(a);
    const nb = normalize(b);
    if (!na || !nb) return 0;
    if (na === nb) return 1;
    if (na.includes(nb) || nb.includes(na)) return 0.82;
    const ta = tokenSet(a);
    const tb = tokenSet(b);
    const intersection = [...ta].filter((token) => tb.has(token)).length;
    const union = new Set([...ta, ...tb]).size || 1;
    const tokenScore = intersection / union;
    let prefix = 0;
    const limit = Math.min(na.length, nb.length);
    while (prefix < limit && na[prefix] === nb[prefix]) prefix += 1;
    const prefixScore = prefix / Math.max(na.length, nb.length);
    return clamp(Math.max(tokenScore, prefixScore * 0.8));
  }

  function valueOverlap(a, b) {
    const sa = new Set(a.distinctValues || []);
    const sb = new Set(b.distinctValues || []);
    if (!sa.size || !sb.size) return 0;
    let intersection = 0;
    sa.forEach((value) => { if (sb.has(value)) intersection += 1; });
    return intersection / Math.max(1, Math.min(sa.size, sb.size));
  }

  function mappingEvidence(fromColumn, toColumn) {
    const name = nameSimilarity(fromColumn.name, toColumn.name);
    const overlap = valueOverlap(fromColumn, toColumn);
    const type = fromColumn.type === toColumn.type || fromColumn.type === 'empty' || toColumn.type === 'empty' ? 1 : 0.25;
    const score = clamp((name * 0.45) + (overlap * 0.45) + (type * 0.1));
    return { name, overlap, type, score };
  }

  function suggestMappings(tables) {
    const candidates = [];
    for (let i = 0; i < tables.length; i += 1) {
      for (let j = i + 1; j < tables.length; j += 1) {
        const left = tables[i];
        const right = tables[j];
        left.columns.forEach((fromColumn) => {
          right.columns.forEach((toColumn) => {
            const evidence = mappingEvidence(fromColumn, toColumn);
            if (evidence.score >= 0.42 || evidence.overlap >= 0.55) {
              candidates.push({
                id: uid('mapping'),
                fromTableId: left.id,
                fromColumn: fromColumn.name,
                toTableId: right.id,
                toColumn: toColumn.name,
                enabled: evidence.score >= 0.62 || evidence.overlap >= 0.8,
                source: 'suggested',
                evidence
              });
            }
          });
        });
      }
    }
    candidates.sort((a, b) => b.evidence.score - a.evidence.score);
    const kept = [];
    const pairCounts = new Map();
    candidates.forEach((candidate) => {
      const key = [candidate.fromTableId, candidate.toTableId].sort().join('|');
      const count = pairCounts.get(key) || 0;
      if (count < 8 && kept.length < 30) {
        kept.push(candidate);
        pairCounts.set(key, count + 1);
      }
    });
    return kept;
  }

  function tableById(id) { return state.tables.find((table) => table.id === id); }
  function columnByName(table, name) { return table?.columns.find((column) => column.name === name); }

  function renderFiles() {
    if (!state.tables.length) {
      dom.fileList.innerHTML = '<p class="rdp__empty">No files loaded yet.</p>';
      return;
    }
    const grouped = new Map();
    state.tables.forEach((table) => {
      const item = grouped.get(table.fileName) || { fileName: table.fileName, tables: [] };
      item.tables.push(table);
      grouped.set(table.fileName, item);
    });
    dom.fileList.innerHTML = [...grouped.values()].map((group) => {
      const rows = group.tables.reduce((sum, table) => sum + table.rows.length, 0);
      const sheets = group.tables.map((table) => table.sheetName).join(', ');
      return `<div class="rdp__file-card"><span class="material-symbols-outlined" aria-hidden="true">table_view</span><div><strong>${esc(group.fileName)}</strong><small>${esc(sheets)} · ${compactNumber(rows)} data rows</small></div><em>${group.tables.length} table${group.tables.length === 1 ? '' : 's'}</em></div>`;
    }).join('');
  }

  function renderDiscovery() {
    if (!state.tables.length) {
      dom.discovery.innerHTML = '<p class="rdp__empty">Load files first.</p>';
      dom.discoverySummary.innerHTML = '<strong>0</strong><span>tables</span>';
      return;
    }
    const keyCount = state.tables.reduce((sum, table) => sum + table.columns.filter((column) => column.likelyKey).length, 0);
    dom.discoverySummary.innerHTML = `<strong>${state.tables.length}</strong><span>${keyCount} key candidates</span>`;
    dom.discovery.innerHTML = state.tables.map((table) => `
      <article class="rdp__table-card">
        <header><strong>${esc(table.label)}</strong><span>${compactNumber(table.rows.length)} rows · ${table.columns.length} columns</span></header>
        <div class="rdp__table-wrap">
          <table class="rdp__profile-table">
            <thead><tr><th>Column</th><th>Type</th><th>Complete</th><th>Unique</th></tr></thead>
            <tbody>${table.columns.map((column) => `<tr><td title="${esc(column.samples.join(' · '))}">${esc(column.name)}</td><td><span class="rdp__badge ${column.likelyKey ? 'rdp__badge--key' : ''}">${column.likelyKey ? 'key · ' : ''}${esc(column.type)}</span></td><td>${percent(column.completeness)}</td><td>${percent(column.uniqueness)}</td></tr>`).join('')}</tbody>
          </table>
        </div>
      </article>`).join('');
  }

  function tableOptions(selectedId) {
    return state.tables.map((table) => `<option value="${esc(table.id)}" ${table.id === selectedId ? 'selected' : ''}>${esc(table.label)}</option>`).join('');
  }

  function columnOptions(tableId, selectedName) {
    const table = tableById(tableId);
    return (table?.columns || []).map((column) => `<option value="${esc(column.name)}" ${column.name === selectedName ? 'selected' : ''}>${esc(column.name)}</option>`).join('');
  }

  function recalculateMapping(mapping) {
    const fromTable = tableById(mapping.fromTableId);
    const toTable = tableById(mapping.toTableId);
    const fromColumn = columnByName(fromTable, mapping.fromColumn);
    const toColumn = columnByName(toTable, mapping.toColumn);
    mapping.evidence = fromColumn && toColumn ? mappingEvidence(fromColumn, toColumn) : { name: 0, overlap: 0, type: 0, score: 0 };
  }

  function renderMappings() {
    if (state.tables.length < 2) {
      dom.mappings.innerHTML = '<p class="rdp__empty">At least two tables are needed to map fields between sources.</p>';
      return;
    }
    if (!state.mappings.length) addManualMapping(false);
    dom.mappings.innerHTML = state.mappings.map((mapping) => {
      const ev = mapping.evidence || { score: 0, name: 0, overlap: 0 };
      return `<article class="rdp__mapping ${mapping.enabled ? '' : 'is-disabled'}" data-mapping-id="${esc(mapping.id)}">
        <label class="rdp__mapping-toggle" title="Use this mapping"><input type="checkbox" data-field="enabled" ${mapping.enabled ? 'checked' : ''} /></label>
        <div class="rdp__mapping-fields">
          <div class="rdp__mapping-side"><select data-field="fromTableId" aria-label="Source table">${tableOptions(mapping.fromTableId)}</select><select data-field="fromColumn" aria-label="Source column">${columnOptions(mapping.fromTableId, mapping.fromColumn)}</select></div>
          <span class="material-symbols-outlined rdp__mapping-arrow" aria-hidden="true">arrow_forward</span>
          <div class="rdp__mapping-side"><select data-field="toTableId" aria-label="Target table">${tableOptions(mapping.toTableId)}</select><select data-field="toColumn" aria-label="Target column">${columnOptions(mapping.toTableId, mapping.toColumn)}</select></div>
        </div>
        <div class="rdp__mapping-score"><strong>${percent(ev.score)}</strong><span>${mapping.source === 'manual' ? 'manual' : 'confidence'}</span><button type="button" class="rdp__text-button rdp__mapping-remove" data-remove-mapping="${esc(mapping.id)}">remove</button></div>
        <div class="rdp__mapping-evidence">Header similarity ${percent(ev.name)} · value overlap ${percent(ev.overlap)} · ${ev.type >= 1 ? 'compatible type' : 'type differs'}</div>
      </article>`;
    }).join('');
  }

  function addManualMapping(render = true) {
    if (state.tables.length < 2) {
      setStatus('Load at least two tables before adding a mapping.', 'error');
      return;
    }
    const fromTable = state.tables[0];
    const toTable = state.tables[1];
    const mapping = {
      id: uid('mapping'),
      fromTableId: fromTable.id,
      fromColumn: fromTable.columns[0]?.name || '',
      toTableId: toTable.id,
      toColumn: toTable.columns[0]?.name || '',
      enabled: true,
      source: 'manual',
      evidence: { name: 0, overlap: 0, type: 0, score: 0 }
    };
    recalculateMapping(mapping);
    state.mappings.push(mapping);
    if (render) renderMappings();
  }

  function validateMapping(mapping) {
    const fromTable = tableById(mapping.fromTableId);
    const toTable = tableById(mapping.toTableId);
    if (!fromTable || !toTable) return null;
    const sourceValues = fromTable.rows.map((row) => row[mapping.fromColumn]);
    const targetValues = toTable.rows.map((row) => row[mapping.toColumn]);
    const sourceNonEmpty = sourceValues.map(normalize).filter(Boolean);
    const targetNonEmpty = targetValues.map(normalize).filter(Boolean);
    const targetSet = new Set(targetNonEmpty);
    const targetUnique = new Set(targetNonEmpty);
    const matched = sourceNonEmpty.filter((value) => targetSet.has(value));
    const unmatched = [...new Set(sourceNonEmpty.filter((value) => !targetSet.has(value)))].slice(0, 5);
    const coverage = sourceNonEmpty.length ? matched.length / sourceNonEmpty.length : 0;
    const sourceNullRate = fromTable.rows.length ? 1 - (sourceNonEmpty.length / fromTable.rows.length) : 1;
    const targetDuplicateRate = targetNonEmpty.length ? 1 - (targetUnique.size / targetNonEmpty.length) : 1;
    let status = 'weak';
    if (coverage >= 0.9 && targetDuplicateRate <= 0.05) status = 'strong';
    else if (coverage >= 0.7) status = 'review';
    return { mappingId: mapping.id, coverage, sourceNullRate, targetDuplicateRate, status, unmatched };
  }

  function runValidation() {
    const active = state.mappings.filter((mapping) => mapping.enabled);
    state.validations = active.map(validateMapping).filter(Boolean);
    if (!active.length) {
      dom.validation.innerHTML = '<p class="rdp__empty">Select at least one mapping before validation.</p>';
      dom.validationScore.innerHTML = '<strong>—</strong><span>overall</span>';
      setStatus('No mapping is selected.', 'error');
      return;
    }
    const average = state.validations.reduce((sum, item) => sum + item.coverage, 0) / Math.max(1, state.validations.length);
    dom.validationScore.innerHTML = `<strong>${percent(average)}</strong><span>avg coverage</span>`;
    dom.validation.innerHTML = state.validations.map((validation) => {
      const mapping = state.mappings.find((item) => item.id === validation.mappingId);
      const fromTable = tableById(mapping.fromTableId);
      const toTable = tableById(mapping.toTableId);
      return `<article class="rdp__validation">
        <div class="rdp__validation-title"><strong>${esc(fromTable.label)}.${esc(mapping.fromColumn)} → ${esc(toTable.label)}.${esc(mapping.toColumn)}</strong><span>Validation uses the rows loaded in this run.</span></div>
        <div class="rdp__validation-metric"><strong>${percent(validation.coverage)}</strong><span>coverage</span></div>
        <div class="rdp__validation-metric"><strong>${percent(validation.sourceNullRate)}</strong><span>source nulls</span></div>
        <div class="rdp__validation-metric"><strong>${percent(validation.targetDuplicateRate)}</strong><span>target duplicates</span></div>
        <span class="rdp__validation-status is-${validation.status}">${validation.status}</span>
        <div class="rdp__validation-details">${validation.unmatched.length ? `Unmatched examples: ${validation.unmatched.map(esc).join(', ')}` : 'No unmatched source values in the sampled mapping direction.'}</div>
      </article>`;
    }).join('');
    setStatus(`Validated ${state.validations.length} mapping${state.validations.length === 1 ? '' : 's'} with ${percent(average)} average source coverage.`, average >= 0.9 ? 'success' : '');
  }

  function buildResult() {
    const active = state.mappings.filter((mapping) => mapping.enabled);
    if (!active.length) {
      state.resultRows = [];
      state.resultColumns = [];
      dom.resultSummary.innerHTML = '<span>No active mappings.</span>';
      dom.resultTable.innerHTML = '<tbody><tr><td>Select a mapping first.</td></tr></tbody>';
      dom.exportCsv.disabled = true;
      return;
    }
    const baseId = active[0].fromTableId;
    const base = tableById(baseId);
    const applicable = active.filter((mapping) => mapping.fromTableId === baseId);
    const result = base.rows.map((row) => ({ ...row }));
    let duplicateTargets = 0;

    applicable.forEach((mapping) => {
      const target = tableById(mapping.toTableId);
      const index = new Map();
      target.rows.forEach((targetRow) => {
        const key = normalize(targetRow[mapping.toColumn]);
        if (!key) return;
        if (!index.has(key)) index.set(key, []);
        index.get(key).push(targetRow);
      });
      index.forEach((rows) => { if (rows.length > 1) duplicateTargets += 1; });
      result.forEach((outputRow, rowIndex) => {
        const sourceValue = base.rows[rowIndex][mapping.fromColumn];
        const matches = index.get(normalize(sourceValue)) || [];
        const match = matches[0];
        target.headers.forEach((header) => {
          const prefix = target.sheetName || target.fileName;
          const outputName = `${prefix}.${header}`;
          outputRow[outputName] = match ? match[header] : null;
        });
      });
    });

    state.resultRows = result;
    state.resultColumns = result.length ? Object.keys(result[0]) : base.headers.slice();
    const preview = result.slice(0, 100);
    dom.resultSummary.innerHTML = `<span><strong>${compactNumber(result.length)}</strong> result rows</span><span><strong>${state.resultColumns.length}</strong> columns</span><span><strong>${applicable.length}</strong> joins applied</span>${duplicateTargets ? `<span><strong>${duplicateTargets}</strong> duplicate target keys use the first row</span>` : ''}`;
    dom.resultTable.innerHTML = `<thead><tr>${state.resultColumns.map((column) => `<th>${esc(column)}</th>`).join('')}</tr></thead><tbody>${preview.map((row) => `<tr>${state.resultColumns.map((column) => `<td title="${esc(row[column])}">${esc(row[column])}</td>`).join('')}</tr>`).join('')}</tbody>`;
    dom.exportCsv.disabled = !result.length;
    setStatus(`Built a preview from ${base.label}. ${result.length > 100 ? 'The table shows the first 100 rows; CSV export contains all rows.' : 'All result rows are shown.'}`, 'success');
  }

  function csvCell(value) {
    const text = value === null || value === undefined ? '' : String(value);
    return /[",\n\r]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
  }

  function downloadText(filename, text, type = 'text/plain;charset=utf-8') {
    const blob = new Blob([text], { type });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  }

  function exportResultCsv() {
    if (!state.resultRows.length) return;
    const csv = [state.resultColumns.map(csvCell).join(','), ...state.resultRows.map((row) => state.resultColumns.map((column) => csvCell(row[column])).join(','))].join('\n');
    downloadText('reusable-data-procedure-result.csv', csv, 'text/csv;charset=utf-8');
  }

  function loadSaved() {
    try {
      const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
      return Array.isArray(parsed) ? parsed : [];
    } catch (_) {
      return [];
    }
  }

  function saveSaved(items) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
  }

  function fileStem(name) {
    return normalize(String(name || '').replace(/\.[^.]+$/, '').replace(/20\d{2}[-_.]?\d{1,2}[-_.]?\d{1,2}/g, '').replace(/\d{6,}/g, ''));
  }

  function buildProcedure(formData) {
    const signatures = state.tables.map((table, index) => ({
      id: `source-${index + 1}`,
      fileName: table.fileName,
      fileStem: fileStem(table.fileName),
      sheetName: table.sheetName,
      expectedColumns: table.columns.map((column) => ({ name: column.name, type: column.type, likelyKey: column.likelyKey }))
    }));
    const signatureByTable = new Map(state.tables.map((table, index) => [table.id, signatures[index].id]));
    return {
      kind: 'reusable-data-procedure',
      version: '1.0',
      id: uid('procedure'),
      name: String(formData.get('name') || '').trim(),
      purpose: String(formData.get('purpose') || '').trim(),
      createdAt: new Date().toISOString(),
      sources: signatures,
      mappings: state.mappings.filter((mapping) => mapping.enabled).map((mapping) => ({
        fromSource: signatureByTable.get(mapping.fromTableId),
        fromColumn: mapping.fromColumn,
        toSource: signatureByTable.get(mapping.toTableId),
        toColumn: mapping.toColumn,
        direction: 'lookup',
        evidenceAtSave: {
          confidence: Number((mapping.evidence?.score || 0).toFixed(4)),
          valueOverlap: Number((mapping.evidence?.overlap || 0).toFixed(4))
        }
      })),
      validationPolicy: {
        requireSameColumns: formData.get('strict') === 'on',
        minimumCoverage: formData.get('minCoverage') === 'on' ? 0.9 : 0,
        targetKeyPreference: 'unique-or-review'
      },
      dataStored: false
    };
  }

  function scoreTableForSignature(table, signature) {
    const expected = new Set((signature.expectedColumns || []).map((column) => normalize(column.name)));
    const actual = new Set(table.headers.map(normalize));
    const matches = [...expected].filter((name) => actual.has(name)).length;
    const columnScore = expected.size ? matches / expected.size : 0;
    const sheetScore = normalize(table.sheetName) === normalize(signature.sheetName) ? 0.2 : 0;
    const fileScore = signature.fileStem && fileStem(table.fileName) === signature.fileStem ? 0.15 : 0;
    return clamp((columnScore * 0.65) + sheetScore + fileScore);
  }

  function resolveProcedure(procedure) {
    const sourceMap = new Map();
    (procedure.sources || []).forEach((signature) => {
      const ranked = state.tables.map((table) => ({ table, score: scoreTableForSignature(table, signature) })).sort((a, b) => b.score - a.score);
      if (ranked[0] && ranked[0].score >= 0.55) sourceMap.set(signature.id, ranked[0].table.id);
    });
    const mappings = (procedure.mappings || []).map((saved) => {
      const fromTableId = sourceMap.get(saved.fromSource);
      const toTableId = sourceMap.get(saved.toSource);
      if (!fromTableId || !toTableId) return null;
      const mapping = {
        id: uid('mapping'),
        fromTableId,
        fromColumn: saved.fromColumn,
        toTableId,
        toColumn: saved.toColumn,
        enabled: true,
        source: 'procedure',
        evidence: { name: 0, overlap: 0, type: 0, score: 0 }
      };
      recalculateMapping(mapping);
      return mapping;
    }).filter(Boolean);
    return { sourceMap, mappings };
  }

  function applyProcedure(id) {
    const procedure = loadSaved().find((item) => item.id === id);
    if (!procedure) return;
    if (!state.tables.length) {
      setStatus('Load the new export files first, then apply the saved procedure.', 'error');
      goStep('files');
      return;
    }
    const resolved = resolveProcedure(procedure);
    if (!resolved.mappings.length) {
      setStatus('The current files do not match this procedure closely enough. Check sheets and column names.', 'error');
      return;
    }
    state.mappings = resolved.mappings;
    renderMappings();
    setStatus(`Applied “${procedure.name}” to the current files. Review the resolved mappings before validation.`, 'success');
    goStep('map');
  }

  function renderSaved() {
    const items = loadSaved();
    if (!items.length) {
      dom.savedList.innerHTML = '<p class="rdp__empty">No saved procedures yet.</p>';
      return;
    }
    dom.savedList.innerHTML = items.map((item) => `<article class="rdp__saved-card"><div><strong>${esc(item.name)}</strong><small>${esc(item.purpose || 'No purpose recorded.')} · ${(item.sources || []).length} sources · ${(item.mappings || []).length} mappings</small></div><div class="rdp__saved-actions"><button type="button" data-action="apply" data-id="${esc(item.id)}">Apply</button><button type="button" data-action="export" data-id="${esc(item.id)}">JSON</button><button type="button" data-action="delete" data-id="${esc(item.id)}">Delete</button></div></article>`).join('');
  }

  function importProcedure(file) {
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const procedure = JSON.parse(String(reader.result || ''));
        if (procedure.kind !== 'reusable-data-procedure' || !Array.isArray(procedure.sources) || !Array.isArray(procedure.mappings)) throw new Error('Invalid procedure');
        procedure.id = procedure.id || uid('procedure');
        const items = loadSaved().filter((item) => item.id !== procedure.id);
        items.unshift(procedure);
        saveSaved(items);
        renderSaved();
        setStatus(`Imported “${procedure.name || 'procedure'}”.`, 'success');
      } catch (_) {
        setStatus('This JSON file is not a valid reusable data procedure.', 'error');
      }
    };
    reader.readAsText(file);
  }

  function loadDemo() {
    const sales = [
      ['Sales Order', 'Material', 'Customer', 'Quantity'],
      ['500001', 'MAT-100', 'C-1000', 4],
      ['500002', 'MAT-200', 'C-2000', 7],
      ['500003', 'MAT-300', 'C-1000', 2],
      ['500004', 'MAT-999', 'C-3000', 1]
    ];
    const materials = [
      ['Material ID', 'Description', 'Plant', 'Product Group'],
      ['MAT-100', 'Drive Unit', '1000', 'A10'],
      ['MAT-200', 'Sensor', '1000', 'B20'],
      ['MAT-300', 'Control Module', '2000', 'A10']
    ];
    state.tables = [
      createTable('sales_export_2026-08.csv', 'Sales', sales, 'demo-sales'),
      createTable('material_master.xlsx', 'Materials', materials, 'demo-materials')
    ];
    state.mappings = suggestMappings(state.tables);
    state.validations = [];
    state.resultRows = [];
    renderFiles();
    renderDiscovery();
    renderMappings();
    updateNextButtons();
    setStatus('Demo loaded. The missing MAT-999 reference is intentional so validation has something useful to complain about.', 'success');
  }

  function updateNextButtons() {
    const discoverButton = $('[data-rdp-next="discover"]');
    if (discoverButton) discoverButton.disabled = !state.tables.length;
  }

  dom.fileInput.addEventListener('change', (event) => parseFiles(Array.from(event.target.files || [])));
  dom.dropzone.addEventListener('dragover', (event) => { event.preventDefault(); dom.dropzone.classList.add('is-dragging'); });
  dom.dropzone.addEventListener('dragleave', () => dom.dropzone.classList.remove('is-dragging'));
  dom.dropzone.addEventListener('drop', (event) => {
    event.preventDefault();
    dom.dropzone.classList.remove('is-dragging');
    parseFiles(Array.from(event.dataTransfer?.files || []));
  });

  $$('[data-rdp-step]').forEach((button) => button.addEventListener('click', () => goStep(button.dataset.rdpStep)));
  $$('[data-rdp-next]').forEach((button) => button.addEventListener('click', () => goStep(button.dataset.rdpNext)));
  $$('[data-rdp-back]').forEach((button) => button.addEventListener('click', () => goStep(button.dataset.rdpBack)));
  $('[data-rdp-load-demo]').addEventListener('click', loadDemo);
  $('[data-rdp-add-mapping]').addEventListener('click', () => addManualMapping(true));
  dom.exportCsv.addEventListener('click', exportResultCsv);

  dom.mappings.addEventListener('change', (event) => {
    const card = event.target.closest('[data-mapping-id]');
    if (!card) return;
    const mapping = state.mappings.find((item) => item.id === card.dataset.mappingId);
    if (!mapping) return;
    const field = event.target.dataset.field;
    if (!field) return;
    if (field === 'enabled') mapping.enabled = event.target.checked;
    else mapping[field] = event.target.value;
    if (field === 'fromTableId') mapping.fromColumn = tableById(mapping.fromTableId)?.columns[0]?.name || '';
    if (field === 'toTableId') mapping.toColumn = tableById(mapping.toTableId)?.columns[0]?.name || '';
    recalculateMapping(mapping);
    renderMappings();
  });

  dom.mappings.addEventListener('click', (event) => {
    const button = event.target.closest('[data-remove-mapping]');
    if (!button) return;
    state.mappings = state.mappings.filter((mapping) => mapping.id !== button.dataset.removeMapping);
    renderMappings();
  });

  dom.saveForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!state.tables.length || !state.mappings.some((mapping) => mapping.enabled)) {
      setStatus('A procedure needs source signatures and at least one approved mapping.', 'error');
      return;
    }
    const procedure = buildProcedure(new FormData(dom.saveForm));
    if (!procedure.name) return;
    const items = loadSaved();
    items.unshift(procedure);
    saveSaved(items);
    renderSaved();
    dom.saveForm.reset();
    $('[name="strict"]', dom.saveForm).checked = true;
    $('[name="minCoverage"]', dom.saveForm).checked = true;
    setStatus(`Saved “${procedure.name}”. Business data was not stored.`, 'success');
  });

  dom.savedList.addEventListener('click', (event) => {
    const button = event.target.closest('[data-action]');
    if (!button) return;
    const { action, id } = button.dataset;
    const items = loadSaved();
    const procedure = items.find((item) => item.id === id);
    if (action === 'apply') applyProcedure(id);
    if (action === 'export' && procedure) downloadText(`${normalize(procedure.name) || 'procedure'}.json`, JSON.stringify(procedure, null, 2), 'application/json;charset=utf-8');
    if (action === 'delete') {
      saveSaved(items.filter((item) => item.id !== id));
      renderSaved();
      setStatus('Procedure removed from this browser.');
    }
  });

  $('[data-rdp-import-trigger]').addEventListener('click', () => dom.importInput.click());
  dom.importInput.addEventListener('change', (event) => {
    const file = event.target.files?.[0];
    if (file) importProcedure(file);
    event.target.value = '';
  });

  renderFiles();
  renderDiscovery();
  renderMappings();
  renderSaved();
  updateNextButtons();
})();
