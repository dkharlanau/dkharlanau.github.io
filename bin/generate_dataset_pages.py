#!/usr/bin/env python3
"""Generate GitHub Pages-friendly dataset pages from ./datasets/manifest.json.

Outputs (all static, GH Pages compatible):
  - /datasets/ (landing)
  - /datasets/search/ (global search; fetches manifest.json client-side)
  - /datasets/types/ + /datasets/types/<type>/ (browse across collections)
  - /datasets/<collection>/ (collection list)
  - /datasets/view/<collection>/<id>/ (entry page with attribution + JSON viewer)

Design goals:
  - Reader-first UX: clear cards, summaries, filters, copyable JSON.
  - Crawler-first metadata: JSON-LD Dataset on entry pages and stable canonical URLs.
"""

from __future__ import annotations

import html
import json
import os
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
DATASETS_DIR = ROOT / "datasets"
MANIFEST = DATASETS_DIR / "manifest.json"
CONFIG_YML = ROOT / "_config.yml"


def read_site_url() -> str:
    # Avoid PyYAML dependency; simple parsing for `url:`.
    if not CONFIG_YML.exists():
        return "https://dkharlanau.github.io"
    for line in CONFIG_YML.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip().startswith("url:"):
            _, v = line.split(":", 1)
            v = v.strip().strip('"').strip("'")
            if v:
                return v.rstrip("/")
    return "https://dkharlanau.github.io"


def load_manifest() -> Dict[str, Any]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def safe_text(s: Any) -> str:
    return ("" if s is None else str(s)).replace("\r\n", "\n").replace("\r", "\n")


def esc(s: Any) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def slug(s: str) -> str:
    s = (s or "").strip().lower()
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch in ("_", "-", " "):
            out.append("-")
    s2 = "".join(out).strip("-")
    while "--" in s2:
        s2 = s2.replace("--", "-")
    return s2 or "unknown"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def json_ld_dataset(
    *,
    site_url: str,
    page_url: str,
    raw_url: str,
    name: str,
    description: str,
    keywords: List[str],
) -> str:
    payload: Dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": name,
        "description": description,
        "url": page_url,
        "isAccessibleForFree": True,
        "creator": {
            "@type": "Person",
            "@id": f"{site_url}/#dkharlanau",
            "name": "Dzmitryi Kharlanau",
            "url": f"{site_url}/",
        },
        "distribution": [
            {
                "@type": "DataDownload",
                "encodingFormat": "application/json",
                "contentUrl": raw_url,
            }
        ],
    }
    if keywords:
        payload["keywords"] = keywords
    return "<script type=\"application/ld+json\">\n" + json.dumps(payload, ensure_ascii=False, indent=2) + "\n</script>"


def build_item_card(*, dataset: str, entry_id: str, title: str, summary: str, entity_type: str, tags: List[str]) -> str:
    pills = []
    if entity_type:
        pills.append(f"<span class=\"pill pill--type\">{esc(entity_type)}</span>")
    pills.append(f"<span class=\"pill pill--dataset\">{esc(dataset)}</span>")
    pills.append(f"<span class=\"pill\">{esc(entry_id)}</span>")
    for t in tags[:5]:
        pills.append(f"<span class=\"pill\">{esc(t)}</span>")
    pills.append(f"<a class=\"pill\" href=\"/datasets/{esc(dataset)}/{esc(entry_id)}.json\">json</a>")

    title_l = (title or entry_id).lower()
    tags_l = " ".join(str(t).lower() for t in tags)
    type_l = (entity_type or "").lower()

    return "\n".join(
        [
            f"<article class=\"dataset-item\" data-id=\"{esc(entry_id)}\" data-title=\"{esc(title_l)}\" data-tags=\"{esc(tags_l)}\" data-type=\"{esc(type_l)}\">",
            f"  <h2 class=\"dataset-item__title\"><a href=\"/datasets/view/{esc(dataset)}/{esc(entry_id)}/\">{esc(title or entry_id)}</a></h2>",
            f"  <p class=\"dataset-item__summary\">{esc(summary)}</p>" if summary else "",
            "  <div class=\"dataset-item__meta\">" + " ".join(pills) + "</div>",
            "</article>",
        ]
    )


def filter_script(*, total: int) -> str:
    # Lightweight client-side filter (no dependencies).
    return (
        "<script>\n"
        "(function(){\n"
        "  var input = document.getElementById('datasetSearch');\n"
        "  var list = document.getElementById('datasetList');\n"
        "  var count = document.getElementById('datasetCount');\n"
        "  var typeSel = document.getElementById('datasetType');\n"
        "  if(!input || !list || !count) return;\n"
        "  var items = Array.prototype.slice.call(list.querySelectorAll('.dataset-item'));\n"
        "  function render(){\n"
        "    var q = (input.value || '').trim().toLowerCase();\n"
        "    var t = (typeSel && typeSel.value || '').trim().toLowerCase();\n"
        "    var shown = 0;\n"
        "    items.forEach(function(el){\n"
        "      var hay = (el.getAttribute('data-id')||'') + ' ' + (el.getAttribute('data-title')||'') + ' ' + (el.getAttribute('data-tags')||'');\n"
        "      var okQ = !q || hay.indexOf(q) !== -1;\n"
        "      var okT = !t || (el.getAttribute('data-type')||'').indexOf(t) !== -1;\n"
        "      var ok = okQ && okT;\n"
        "      el.style.display = ok ? '' : 'none';\n"
        "      if(ok) shown++;\n"
        "    });\n"
        f"    count.textContent = shown + ' / {total} visible';\n"
        "  }\n"
        "  input.addEventListener('input', render);\n"
        "  if(typeSel) typeSel.addEventListener('change', render);\n"
        "  render();\n"
        "})();\n"
        "</script>\n"
    )


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: missing {MANIFEST}")
        return 2

    site_url = read_site_url()
    manifest = load_manifest()
    entries: List[Dict[str, Any]] = manifest.get("entries", [])

    by_dataset: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    by_type: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for e in entries:
        ds = str(e.get("dataset") or "unknown")
        by_dataset[ds].append(e)
        et = str(e.get("entity_type") or ds or "unknown")
        by_type[et].append(e)

    # /datasets/ landing
    cards = []
    for name in sorted(by_dataset.keys()):
        count = len(by_dataset[name])
        cards.append(
            "\n".join(
                [
                    f"<a class=\"neub-card dataset-card\" href=\"/datasets/{esc(name)}/\">",
                    f"  <h2 class=\"dataset-card__title\">{esc(name)}</h2>",
                    f"  <p class=\"dataset-card__desc\">Browse {count} reusable bytes with attribution and raw JSON downloads.</p>",
                    "  <div class=\"dataset-card__footer\">",
                    f"    <span class=\"pill\">{count} entries</span>",
                    "    <span class=\"link-arrow\">Open</span>",
                    "  </div>",
                    "</a>",
                ]
            )
        )

    landing = (
        "---\n"
        "layout: default\n"
        "title: \"Datasets\"\n"
        "description: \"Reusable dataset bytes by Dzmitryi Kharlanau (SAP Lead).\"\n"
        "permalink: /datasets/\n"
        "sitemap: true\n"
        "---\n\n"
        "<div class=\"dataset-hero\">\n"
        "  <p class=\"eyebrow\">Datasets</p>\n"
        "  <h1 class=\"dataset-hero__title\">Reusable bytes for readers and AI</h1>\n"
        "  <p class=\"lead\">Curated building blocks (TRIZ, AMS, Agentic development, LLM prompts, DAMA/MDG) — published with attribution so people and crawlers can cite the source.</p>\n"
        "  <div class=\"dataset-actions\">\n"
        "    <a class=\"button\" href=\"/datasets/search/\">Search all</a>\n"
        "    <a class=\"button button--secondary\" href=\"/datasets/types/\">Browse by type</a>\n"
        "    <a class=\"button button--secondary\" href=\"/datasets/manifest.json\">manifest.json</a>\n"
        "    <a class=\"button button--secondary\" href=\"/datasets/schema.json\">schema.json</a>\n"
        "  </div>\n"
        "</div>\n\n"
        "<div class=\"dataset-kpis\">\n"
        f"  <div class=\"dataset-kpi\"><div class=\"dataset-kpi__label\">Total entries</div><p class=\"dataset-kpi__value\">{manifest.get('count', len(entries))}</p><p class=\"dataset-kpi__hint\">Across all collections</p></div>\n"
        f"  <div class=\"dataset-kpi\"><div class=\"dataset-kpi__label\">Collections</div><p class=\"dataset-kpi__value\">{len(by_dataset)}</p><p class=\"dataset-kpi__hint\">Browse by topic</p></div>\n"
        f"  <div class=\"dataset-kpi\"><div class=\"dataset-kpi__label\">Entity types</div><p class=\"dataset-kpi__value\">{len(by_type)}</p><p class=\"dataset-kpi__hint\">Filter across datasets</p></div>\n"
        "</div>\n\n"
        "<div class=\"dataset-collection-grid\">\n" + "\n".join(cards) + "\n</div>\n"
    )
    write(DATASETS_DIR / "index.md", landing)

    # /datasets/search/ (client-side, powered by manifest.json)
    search_page = (
        "---\n"
        "layout: default\n"
        "title: \"Dataset Search\"\n"
        "description: \"Search all dataset bytes by Dzmitryi Kharlanau (SAP Lead).\"\n"
        "permalink: /datasets/search/\n"
        "sitemap: true\n"
        "---\n\n"
        "<div class=\"dataset-hero\">\n"
        "  <p class=\"eyebrow\">Datasets</p>\n"
        "  <h1 class=\"dataset-hero__title\">Search all bytes</h1>\n"
        "  <p class=\"lead\">Fast client-side search across all collections. Filter by dataset and entity type.</p>\n"
        "  <div class=\"dataset-actions\">\n"
        "    <a class=\"button\" href=\"/datasets/\">All datasets</a>\n"
        "    <a class=\"button button--secondary\" href=\"/datasets/types/\">Browse by type</a>\n"
        "  </div>\n"
        "</div>\n\n"
        "<div class=\"dataset-grid dataset-grid--wide\">\n"
        "  <div class=\"dataset-panel\">\n"
        "    <div class=\"dataset-filter\">\n"
        "      <div class=\"dataset-filter__row\">\n"
        "        <div>\n"
        "          <label for=\"globalSearch\"><strong>Search</strong></label>\n"
        "          <input id=\"globalSearch\" type=\"search\" placeholder=\"Search by title, ID, tag, summary…\" autocomplete=\"off\" />\n"
        "        </div>\n"
        "        <div>\n"
        "          <label for=\"globalDataset\"><strong>Dataset</strong></label>\n"
        "          <select id=\"globalDataset\" class=\"dataset-select\"><option value=\"\">All</option></select>\n"
        "        </div>\n"
        "        <div>\n"
        "          <label for=\"globalType\"><strong>Type</strong></label>\n"
        "          <select id=\"globalType\" class=\"dataset-select\"><option value=\"\">All</option></select>\n"
        "        </div>\n"
        "      </div>\n"
        "      <div class=\"dataset-hero__meta\"><span class=\"pill\" id=\"globalCount\">Loading…</span></div>\n"
        "    </div>\n"
        "    <div class=\"dataset-list\" id=\"globalList\"></div>\n"
        "  </div>\n"
        "</div>\n\n"
        "<script>\n"
        "(function(){\n"
        "  var input = document.getElementById('globalSearch');\n"
        "  var dsSel = document.getElementById('globalDataset');\n"
        "  var typeSel = document.getElementById('globalType');\n"
        "  var list = document.getElementById('globalList');\n"
        "  var count = document.getElementById('globalCount');\n"
        "  if(!input || !dsSel || !typeSel || !list || !count) return;\n"
        "  var all = [];\n"
        "  function escHtml(s){\n"
        "    return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\"/g,'&quot;').replace(/'/g,'&#39;');\n"
        "  }\n"
        "  function uniq(arr){\n"
        "    var m = {};\n"
        "    var out = [];\n"
        "    arr.forEach(function(x){ if(x && !m[x]){ m[x]=1; out.push(x);} });\n"
        "    return out;\n"
        "  }\n"
        "  function opt(el, value){\n"
        "    var o = document.createElement('option');\n"
        "    o.value = value;\n"
        "    o.textContent = value;\n"
        "    el.appendChild(o);\n"
        "  }\n"
        "  function render(){\n"
        "    var q = (input.value||'').trim().toLowerCase();\n"
        "    var d = (dsSel.value||'').trim();\n"
        "    var t = (typeSel.value||'').trim();\n"
        "    var shown = 0;\n"
        "    var html = [];\n"
        "    all.forEach(function(e){\n"
        "      if(d && e.dataset !== d) return;\n"
        "      if(t && e.entity_type !== t) return;\n"
        "      var hay = (e.id+' '+e.title+' '+(e.summary||'')+' '+(e.tags||[]).join(' ')).toLowerCase();\n"
        "      if(q && hay.indexOf(q) === -1) return;\n"
        "      shown++;\n"
        "      var pills = [];\n"
        "      if(e.entity_type) pills.push('<span class=\"pill pill--type\">'+escHtml(e.entity_type)+'</span>');\n"
        "      pills.push('<span class=\"pill pill--dataset\">'+escHtml(e.dataset)+'</span>');\n"
        "      pills.push('<span class=\"pill\">'+escHtml(e.id)+'</span>');\n"
        "      (e.tags||[]).slice(0,5).forEach(function(tag){ pills.push('<span class=\"pill\">'+escHtml(tag)+'</span>'); });\n"
        "      pills.push('<a class=\"pill\" href=\"/datasets/'+escHtml(e.dataset)+'/'+escHtml(e.id)+'.json\">json</a>');\n"
        "      html.push('<article class=\"dataset-item\">'\n"
        "        + '<h2 class=\"dataset-item__title\"><a href=\"/datasets/view/'+escHtml(e.dataset)+'/'+escHtml(e.id)+'/\">'+escHtml(e.title||e.id)+'</a></h2>'\n"
        "        + (e.summary ? '<p class=\"dataset-item__summary\">'+escHtml(e.summary)+'</p>' : '')\n"
        "        + '<div class=\"dataset-item__meta\">'+pills.join(' ')+'</div>'\n"
        "      + '</article>');\n"
        "    });\n"
        "    list.innerHTML = html.join('\\n') || '<p class=\"dataset-empty\">No matches.</p>';\n"
        "    count.textContent = shown + ' results';\n"
        "  }\n"
        "  input.addEventListener('input', render);\n"
        "  dsSel.addEventListener('change', render);\n"
        "  typeSel.addEventListener('change', render);\n"
        "  fetch('/datasets/manifest.json', {cache: 'no-cache'})\n"
        "    .then(function(r){ return r.json(); })\n"
        "    .then(function(m){\n"
        "      all = (m.entries||[]).map(function(e){\n"
        "        return {\n"
        "          dataset: e.dataset,\n"
        "          id: e.id,\n"
        "          title: e.title || e.id,\n"
        "          tags: e.tags || [],\n"
        "          entity_type: e.entity_type || '',\n"
        "          summary: e.summary || ''\n"
        "        };\n"
        "      });\n"
        "      uniq(all.map(function(e){return e.dataset;})).sort().forEach(function(v){ opt(dsSel, v); });\n"
        "      uniq(all.map(function(e){return e.entity_type;})).sort().forEach(function(v){ opt(typeSel, v); });\n"
        "      render();\n"
        "    })\n"
        "    .catch(function(){ count.textContent = 'Failed to load manifest.json'; });\n"
        "})();\n"
        "</script>\n"
    )
    write(DATASETS_DIR / "search.md", search_page)

    # /datasets/types/ + /datasets/types/<type>/
    type_cards = []
    for t_name in sorted(by_type.keys()):
        count = len(by_type[t_name])
        type_cards.append(
            "\n".join(
                [
                    f"<a class=\"neub-card dataset-card\" href=\"/datasets/types/{esc(slug(t_name))}/\">",
                    f"  <h2 class=\"dataset-card__title\">{esc(t_name)}</h2>",
                    f"  <p class=\"dataset-card__desc\">Browse {count} entries across all collections.</p>",
                    "  <div class=\"dataset-card__footer\">",
                    f"    <span class=\"pill\">{count} entries</span>",
                    "    <span class=\"link-arrow\">Open</span>",
                    "  </div>",
                    "</a>",
                ]
            )
        )

    types_index = (
        "---\n"
        "layout: default\n"
        "title: \"Dataset Types\"\n"
        "description: \"Browse dataset bytes by entity type.\"\n"
        "permalink: /datasets/types/\n"
        "sitemap: true\n"
        "---\n\n"
        "<div class=\"dataset-hero\">\n"
        "  <p class=\"eyebrow\">Datasets</p>\n"
        "  <h1 class=\"dataset-hero__title\">Browse by type</h1>\n"
        "  <p class=\"lead\">Entity types are normalized so tools and readers can navigate across collections.</p>\n"
        "  <div class=\"dataset-actions\">\n"
        "    <a class=\"button\" href=\"/datasets/\">All datasets</a>\n"
        "    <a class=\"button button--secondary\" href=\"/datasets/search/\">Search all</a>\n"
        "  </div>\n"
        "</div>\n\n"
        "<div class=\"dataset-collection-grid\">\n" + "\n".join(type_cards) + "\n</div>\n"
    )
    write(DATASETS_DIR / "types" / "index.md", types_index)

    for t_name, t_items in by_type.items():
        t_sorted = sorted(t_items, key=lambda x: (str(x.get("dataset")), str(x.get("id"))))
        list_cards = []
        types_in_type = sorted({str(e.get("entity_type") or t_name) for e in t_sorted})
        for e in t_sorted:
            ds = str(e.get("dataset") or "unknown")
            entry_id = str(e.get("id"))
            title = str(e.get("title") or entry_id)
            tags = e.get("tags") if isinstance(e.get("tags"), list) else []
            summary = str(e.get("summary") or "")
            entity_type = str(e.get("entity_type") or t_name)
            list_cards.append(
                build_item_card(
                    dataset=ds,
                    entry_id=entry_id,
                    title=title,
                    summary=summary,
                    entity_type=entity_type,
                    tags=tags,
                )
            )

        type_opts = "".join([f"<option value=\"{esc(t)}\">{esc(t)}</option>" for t in types_in_type])
        type_page = (
            "---\n"
            "layout: default\n"
            f"title: \"{esc(t_name)}\"\n"
            f"description: \"Dataset bytes of type {esc(t_name)} by Dzmitryi Kharlanau (SAP Lead).\"\n"
            f"permalink: /datasets/types/{slug(t_name)}/\n"
            "sitemap: true\n"
            "---\n\n"
            "<div class=\"dataset-hero\">\n"
            "  <p class=\"eyebrow\">Type</p>\n"
            f"  <h1 class=\"dataset-hero__title\">{esc(t_name)}</h1>\n"
            f"  <p class=\"lead\">{len(t_sorted)} entries across multiple collections.</p>\n"
            "  <div class=\"dataset-actions\">\n"
            "    <a class=\"button\" href=\"/datasets/types/\">All types</a>\n"
            "    <a class=\"button button--secondary\" href=\"/datasets/search/\">Search all</a>\n"
            "  </div>\n"
            "</div>\n\n"
            "<div class=\"dataset-grid\">\n"
            "  <div class=\"dataset-panel\">\n"
            "    <div class=\"dataset-filter\">\n"
            "      <div class=\"dataset-filter__row\">\n"
            "        <div>\n"
            "          <label for=\"datasetSearch\"><strong>Search</strong></label>\n"
            "          <input id=\"datasetSearch\" type=\"search\" placeholder=\"Search by ID, title, tag, summary…\" autocomplete=\"off\" />\n"
            "        </div>\n"
            "        <div>\n"
            "          <label for=\"datasetType\"><strong>Subtype</strong></label>\n"
            "          <select id=\"datasetType\" class=\"dataset-select\"><option value=\"\">All</option>"
            + type_opts
            + "</select>\n"
            "        </div>\n"
            "      </div>\n"
            "      <div class=\"dataset-hero__meta\"><span class=\"pill\" id=\"datasetCount\"></span></div>\n"
            "    </div>\n"
            "    <div class=\"dataset-list\" id=\"datasetList\">\n"
            + "\n".join(list_cards)
            + "\n    </div>\n"
            "  </div>\n"
            "  <aside class=\"dataset-panel\">\n"
            "    <div class=\"neub-card\">\n"
            "      <h2>Attribution</h2>\n"
            "      <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>\n"
            "      <p><a class=\"link-arrow\" href=\"https://www.linkedin.com/in/dkharlanau\" target=\"_blank\" rel=\"noopener noreferrer\">LinkedIn</a></p>\n"
            "    </div>\n"
            "  </aside>\n"
            "</div>\n\n"
            + filter_script(total=len(t_sorted))
        )
        write(DATASETS_DIR / "types" / slug(t_name) / "index.md", type_page)

    # Per-dataset index pages + per-entry pages
    for dataset_name, items in by_dataset.items():
        items_sorted = sorted(items, key=lambda x: str(x.get("id")))
        list_cards = []
        types_in_dataset = sorted({str(e.get("entity_type") or "") for e in items_sorted if str(e.get("entity_type") or "").strip()})
        for e in items_sorted:
            entry_id = str(e.get("id"))
            title = str(e.get("title") or entry_id)
            tags = e.get("tags") if isinstance(e.get("tags"), list) else []
            summary = str(e.get("summary") or "")
            entity_type = str(e.get("entity_type") or "")
            list_cards.append(
                build_item_card(
                    dataset=dataset_name,
                    entry_id=entry_id,
                    title=title,
                    summary=summary,
                    entity_type=entity_type,
                    tags=tags,
                )
            )

        type_opts = "".join([f"<option value=\"{esc(t)}\">{esc(t)}</option>" for t in types_in_dataset])

        dataset_index = (
            "---\n"
            "layout: default\n"
            f"title: \"{esc(dataset_name)} Datasets\"\n"
            f"description: \"{esc(dataset_name)} dataset bytes by Dzmitryi Kharlanau (SAP Lead).\"\n"
            f"permalink: /datasets/{esc(dataset_name)}/\n"
            "sitemap: true\n"
            "---\n\n"
            "<div class=\"dataset-hero\">\n"
            "  <p class=\"eyebrow\">Dataset</p>\n"
            f"  <h1 class=\"dataset-hero__title\">{esc(dataset_name)}</h1>\n"
            f"  <p class=\"lead\">{len(items_sorted)} entries. Filter by search and type. Each entry has a clean page + raw JSON.</p>\n"
            "  <div class=\"dataset-actions\">\n"
            "    <a class=\"button\" href=\"/datasets/\">All datasets</a>\n"
            "    <a class=\"button button--secondary\" href=\"/datasets/search/\">Search all</a>\n"
            "    <a class=\"button button--secondary\" href=\"/datasets/types/\">Browse by type</a>\n"
            "  </div>\n"
            "</div>\n\n"
            "<div class=\"dataset-grid\">\n"
            "  <div class=\"dataset-panel\">\n"
            "    <div class=\"dataset-filter\">\n"
            "      <div class=\"dataset-filter__row\">\n"
            "        <div>\n"
            "          <label for=\"datasetSearch\"><strong>Search</strong></label>\n"
            "          <input id=\"datasetSearch\" type=\"search\" placeholder=\"Search by ID, title, tag, summary…\" autocomplete=\"off\" />\n"
            "        </div>\n"
            "        <div>\n"
            "          <label for=\"datasetType\"><strong>Type</strong></label>\n"
            "          <select id=\"datasetType\" class=\"dataset-select\"><option value=\"\">All</option>"
            + type_opts
            + "</select>\n"
            "        </div>\n"
            "      </div>\n"
            "      <div class=\"dataset-hero__meta\"><span class=\"pill\" id=\"datasetCount\"></span></div>\n"
            "    </div>\n"
            "    <div class=\"dataset-list\" id=\"datasetList\">\n"
            + "\n".join(list_cards)
            + "\n    </div>\n"
            "  </div>\n"
            "  <aside class=\"dataset-panel\">\n"
            "    <div class=\"neub-card\">\n"
            "      <h2>Attribution</h2>\n"
            "      <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>\n"
            "      <p>When you reference these bytes, please link back to the site or LinkedIn.</p>\n"
            "      <p><a class=\"link-arrow\" href=\"https://www.linkedin.com/in/dkharlanau\" target=\"_blank\" rel=\"noopener noreferrer\">LinkedIn</a></p>\n"
            "    </div>\n"
            "    <div class=\"neub-card\">\n"
            "      <h2>For tools</h2>\n"
            "      <p><a href=\"/datasets/schema.json\">schema.json</a> describes the attribution contract.</p>\n"
            "      <p><a href=\"/datasets/manifest.json\">manifest.json</a> lists every entry with ids, titles, tags, types, and paths.</p>\n"
            "    </div>\n"
            "  </aside>\n"
            "</div>\n\n"
            + filter_script(total=len(items_sorted))
        )
        write(DATASETS_DIR / dataset_name / "index.md", dataset_index)

        for e in items_sorted:
            entry_id = str(e.get("id"))
            title = safe_text(e.get("title") or entry_id)
            raw_path = f"/datasets/{dataset_name}/{entry_id}.json"
            raw_url = f"{site_url}{raw_path}"
            page_url = f"{site_url}/datasets/view/{dataset_name}/{entry_id}/"

            tags = e.get("tags") if isinstance(e.get("tags"), list) else []
            summary = str(e.get("summary") or "")
            entity_type = str(e.get("entity_type") or "")
            description = summary or f"{dataset_name} dataset byte by Dzmitryi Kharlanau (SAP Lead). ID: {entry_id}."

            json_file = DATASETS_DIR / dataset_name / f"{entry_id}.json"
            try:
                raw_json_text = json_file.read_text(encoding="utf-8")
            except Exception:
                raw_json_text = ""

            tag_pills = " ".join([f"<span class=\"pill\">{esc(t)}</span>" for t in tags])

            content = (
                "---\n"
                "layout: default\n"
                f"title: \"{esc(title)}\"\n"
                f"description: \"{esc(description)}\"\n"
                f"permalink: /datasets/view/{esc(dataset_name)}/{esc(entry_id)}/\n"
                "sitemap: true\n"
                "---\n\n"
                "<div class=\"dataset-hero\">\n"
                "  <p class=\"eyebrow\">Dataset entry</p>\n"
                f"  <h1 class=\"dataset-hero__title\">{esc(title)}</h1>\n"
                "  <div class=\"dataset-hero__meta\">\n"
                f"    <span class=\"pill pill--dataset\">{esc(dataset_name)}</span>\n"
                + (f"    <span class=\"pill pill--type\">{esc(entity_type)}</span>\n" if entity_type else "")
                + f"    <span class=\"pill\">{esc(entry_id)}</span>\n"
                + (f"    {tag_pills}\n" if tag_pills else "")
                + "  </div>\n"
                "  <div class=\"dataset-actions\">\n"
                f"    <a class=\"button\" href=\"{esc(raw_path)}\">Open JSON</a>\n"
                f"    <a class=\"button button--secondary\" href=\"/datasets/{esc(dataset_name)}/\">Back to list</a>\n"
                "  </div>\n"
                "</div>\n\n"
                + (f"<div class=\"neub-card dataset-entry-lead\">{esc(summary)}</div>\n\n" if summary else "")
                + "<div class=\"dataset-grid dataset-grid--wide\">\n"
                "  <div class=\"neub-card\">\n"
                "    <h2>Attribution</h2>\n"
                "    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>\n"
                f"    <p>Canonical: <a href=\"{esc(raw_url)}\">{esc(raw_url)}</a></p>\n"
                "    <p><a class=\"link-arrow\" href=\"https://www.linkedin.com/in/dkharlanau\" target=\"_blank\" rel=\"noopener noreferrer\">LinkedIn</a></p>\n"
                "  </div>\n"
                "</div>\n\n"
            )

            content += json_ld_dataset(
                site_url=site_url,
                page_url=page_url,
                raw_url=raw_url,
                name=title,
                description=description,
                keywords=[str(t) for t in tags],
            )

            # Copy-friendly JSON panel.
            content += "\n\n<div class=\"dataset-json\">\n"
            content += "<details open>\n<summary>JSON (copy / reuse)</summary>\n\n"
            content += (
                "<pre><code class=\"language-json\">"
                + safe_text(raw_json_text)
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                + "</code></pre>\n"
            )
            content += "\n</details>\n</div>\n"

            write(DATASETS_DIR / "view" / dataset_name / f"{entry_id}.md", content)

    print("Generated dataset pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
