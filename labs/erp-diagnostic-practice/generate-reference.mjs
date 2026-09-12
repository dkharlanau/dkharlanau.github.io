// Keep the static, accessible case guide in sync with the interactive dataset.
// Run from the repository root: node labs/erp-diagnostic-practice/generate-reference.mjs
import { readFileSync, writeFileSync } from 'node:fs';
import { cases } from './cases.mjs';
const escape = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const evidence = source => `<h4>${escape(source.id)} · ${escape(source.title)}</h4><p>${escape(source.intro)}</p><div class="erp-table-scroll" role="region" tabindex="0" aria-label="Reference table: ${escape(source.title)}"><table><caption class="erp-sr-only">${escape(source.title)}</caption><thead><tr>${source.columns.map(label => `<th scope="col">${escape(label)}</th>`).join('')}</tr></thead><tbody>${source.rows.map(row => `<tr>${row.map(value => `<td>${escape(value)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
const html = `<section class="erp-reference" aria-labelledby="erp-reference-title"><h2 id="erp-reference-title">Case guide and original records</h2><p>Read the complete case evidence here, including when JavaScript is unavailable. All examples are synthetic. The interactive desk above uses exactly these records.</p>${cases.map(item => `<details><summary>${escape(item.category)}: ${escape(item.title)}</summary><div class="erp-reference-body"><p>${escape(item.brief)}</p><p><strong>Your task:</strong> ${escape(item.objective)}</p>${item.evidence.map(evidence).join('')}</div></details>`).join('')}</section>`;
const path = new URL('./index.html', import.meta.url);
const before = readFileSync(path, 'utf8');
const after = before.replace(/<!-- ERP-CASE-GUIDE:START -->[\s\S]*?<!-- ERP-CASE-GUIDE:END -->/, `<!-- ERP-CASE-GUIDE:START -->\n  ${html}\n  <!-- ERP-CASE-GUIDE:END -->`);
if (process.argv.includes('--check')) {
  if (after !== before) { console.error('Static ERP case guide is stale. Run generate-reference.mjs.'); process.exitCode = 1; }
  else console.log('Static ERP case guide is current.');
} else { writeFileSync(path, after); console.log('Updated the static ERP case guide.'); }
