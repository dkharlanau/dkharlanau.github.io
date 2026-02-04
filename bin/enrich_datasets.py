#!/usr/bin/env python3
"""
Enrich JSON datasets with consistent attribution metadata for AI/crawlers.

This script:
  - Scans ./datasets recursively for *.json
  - Adds/merges a top-level `meta` block with creator + provenance
  - Writes a consolidated ./datasets/manifest.json and ./datasets/README.md

Design notes:
  - We avoid changing existing semantic fields (id/title/etc.).
  - We put attribution under `meta.*` to reduce schema collisions.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parent.parent
DATASETS_DIR = ROOT / "datasets"
CONFIG_YML = ROOT / "_config.yml"


@dataclass(frozen=True)
class SiteIdentity:
    website: str
    linkedin: str


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def load_site_identity() -> SiteIdentity:
    """
    Pull `url:` and LinkedIn profile from the site config.
    Keep parsing resilient (no PyYAML dependency).
    """
    website = ""
    linkedin = ""

    if CONFIG_YML.exists():
        text = _read_text(CONFIG_YML)

        # url: "https://example.com"
        m = re.search(r'^\s*url:\s*["\']?([^"\']+)["\']?\s*$', text, flags=re.M)
        if m:
            website = m.group(1).strip()

        # Any LinkedIn in the config.
        m2 = re.search(r'https?://www\.linkedin\.com/in/[A-Za-z0-9_-]+/?', text)
        if m2:
            linkedin = m2.group(0).rstrip("/")

    return SiteIdentity(website=website, linkedin=linkedin)


def iter_json_files(root: Path) -> Iterable[Path]:
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".json"):
                yield Path(dirpath) / name


def _safe_json_load(path: Path) -> Optional[Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _merge_dict(dst: Dict[str, Any], src: Dict[str, Any]) -> Dict[str, Any]:
    """
    Shallow merge: keep existing keys, fill missing keys from src.
    For nested dicts, merge recursively.
    """
    for k, v in src.items():
        if k not in dst:
            dst[k] = v
            continue
        if isinstance(dst.get(k), dict) and isinstance(v, dict):
            _merge_dict(dst[k], v)
    return dst


def infer_title_from_id(entry_id: str) -> str:
    """
    Create a human title from an id when `title` is missing.
    Keep this conservative: better an okay label than an empty title for crawlers.
    """
    s = entry_id.strip()
    if not s:
        return ""

    if s == "TRIZ-XX":
        return "TRIZ Byte Template"

    # Drop common version suffixes like _v0_1, _v1_0, etc.
    s = re.sub(r"_v\\d+_\\d+$", "", s)

    # Normalize separators.
    s = s.replace("_", " ").replace("-", " ").strip()

    # Lightweight title-casing while preserving acronyms.
    words = []
    for w in s.split():
        if w.isupper() and len(w) <= 6:
            words.append(w)
        else:
            words.append(w[:1].upper() + w[1:])
    return " ".join(words)


def infer_entity_type(obj: Dict[str, Any], dataset_name: str) -> str:
    """
    Normalize entity types so UX can group/filter entries across datasets.
    """
    entry_id = obj.get("id") or obj.get("byte_id") or ""
    if isinstance(entry_id, str):
        if entry_id.startswith("TRIZ-TECH-"):
            return "triz_technique"
        if entry_id.startswith("TRIZ-"):
            return "triz_byte"
        if entry_id.startswith("ams-"):
            return "ams_byte"
        if entry_id.startswith("agentic_"):
            return "agentic_byte"
        if entry_id.startswith("PE-") or entry_id.startswith("CE-"):
            return "llm_prompt_byte"
        if entry_id.startswith("db_governance_"):
            return "data_governance_byte"
        if entry_id.startswith("mdg_"):
            return "mdg_byte"

    # Use explicit type/category when present.
    t = obj.get("type")
    if isinstance(t, str) and t.strip():
        return t.strip()

    c = obj.get("category")
    if isinstance(c, str) and c.strip():
        return c.strip()

    # Fall back to dataset name.
    return dataset_name


def infer_entity_subtype(obj: Dict[str, Any]) -> str:
    # Optional: useful for grouping within types.
    for key in ("level", "domain", "category", "version", "status"):
        v = obj.get(key)
        if isinstance(v, str) and v.strip():
            return f"{key}:{v.strip()}"
        if key == "domain" and isinstance(v, list) and v:
            first = v[0]
            if isinstance(first, str) and first.strip():
                return f"domain:{first.strip()}"
    return ""


def infer_summary(obj: Dict[str, Any]) -> str:
    """
    Pick the best short human summary for list pages.
    Keep it short and deterministic; do not generate new text with an LLM here.
    """
    candidates = []

    def add(v: Any) -> None:
        if isinstance(v, str):
            s = " ".join(v.split())
            if s:
                candidates.append(s)

    add(obj.get("intent"))
    add(obj.get("hook"))
    add(obj.get("purpose"))
    add(obj.get("description"))
    add(obj.get("core_idea", {}).get("one_liner") if isinstance(obj.get("core_idea"), dict) else None)

    if not candidates:
        t = obj.get("title")
        if isinstance(t, str) and t.strip():
            s = " ".join(t.split())
            return s[:220] + ("…" if len(s) > 220 else "")
        return ""

    s = candidates[0]
    return s[:220] + ("…" if len(s) > 220 else "")


def enrich_one(obj: Dict[str, Any], *, dataset_name: str, path_rel: str, identity: SiteIdentity) -> Dict[str, Any]:
    # Keep "role" as requested (SAP Lead) while leaving page titles intact.
    creator = {
        "name": "Dzmitryi Kharlanau",
        "role": "SAP Lead",
        "website": identity.website,
        "linkedin": identity.linkedin,
    }

    canonical_url = ""
    if identity.website:
        canonical_url = identity.website.rstrip("/") + "/datasets/" + path_rel

    # Preserve created_at across reruns; set updated_at on each run.
    now = _now_iso()
    created_at = now
    existing_meta = obj.get("meta") if isinstance(obj.get("meta"), dict) else {}
    if isinstance(existing_meta, dict):
        if isinstance(existing_meta.get("created_at_utc"), str) and existing_meta["created_at_utc"].strip():
            created_at = existing_meta["created_at_utc"]
        elif isinstance(existing_meta.get("generated_at_utc"), str) and existing_meta["generated_at_utc"].strip():
            # Back-compat: first enrichment used generated_at_utc only.
            created_at = existing_meta["generated_at_utc"]

    base_meta = {
        "schema": "dkharlanau.dataset.byte",
        "schema_version": "1.1",
        "dataset": dataset_name,
        "source_project": "cv-ai",
        "source_path": path_rel,
        "canonical_url": canonical_url,
        "created_at_utc": created_at,
        "updated_at_utc": now,
        "creator": creator,
        "links": {
            "website": identity.website,
            "linkedin": identity.linkedin,
        },
        "contact": {
            "preferred": "linkedin",
            "linkedin": identity.linkedin,
        },
        "provenance": {
            "source_type": "chat_export_extraction",
            "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing.",
        },
        "entity_type": infer_entity_type(obj, dataset_name),
        "entity_subtype": infer_entity_subtype(obj),
        "summary": infer_summary(obj),
        "attribution": {
            "attribution_required": True,
            "preferred_citation": "Dzmitryi Kharlanau (SAP Lead). Dataset bytes: "
            + (identity.website or "https://dkharlanau.github.io"),
        },
        "license": {
            "name": "",
            "spdx": "",
            "url": "",
        },
    }

    if isinstance(existing_meta, dict):
        obj["meta"] = _merge_dict(existing_meta, base_meta)
    else:
        obj["meta"] = base_meta

    # Force-update a small set of meta keys that should always reflect the latest contract.
    meta = obj.get("meta")
    if isinstance(meta, dict):
        meta["schema_version"] = "1.1"
        if canonical_url:
            meta["canonical_url"] = canonical_url
        meta["updated_at_utc"] = now
        meta.setdefault("created_at_utc", created_at)
        meta["entity_type"] = base_meta["entity_type"]
        meta["entity_subtype"] = base_meta["entity_subtype"]
        meta["summary"] = base_meta["summary"]

        # Ensure links/contact are present even if an older meta exists.
        meta.setdefault("links", {})
        if isinstance(meta["links"], dict):
            meta["links"].setdefault("website", identity.website)
            meta["links"].setdefault("linkedin", identity.linkedin)
        meta.setdefault("contact", {})
        if isinstance(meta["contact"], dict):
            meta["contact"].setdefault("preferred", "linkedin")
            meta["contact"].setdefault("linkedin", identity.linkedin)

        # Ensure creator object is present + minimally filled.
        meta.setdefault("creator", {})
        if isinstance(meta["creator"], dict):
            meta["creator"].setdefault("name", "Dzmitryi Kharlanau")
            meta["creator"].setdefault("role", "SAP Lead")
            meta["creator"].setdefault("website", identity.website)
            meta["creator"].setdefault("linkedin", identity.linkedin)

    # Fill missing titles for crawler readability (opt-in only when empty).
    title = obj.get("title")
    if not isinstance(title, str) or not title.strip():
        entry_id = obj.get("id") or obj.get("byte_id") or ""
        if isinstance(entry_id, str) and entry_id.strip():
            inferred = infer_title_from_id(entry_id)
            if inferred:
                obj["title"] = inferred
                meta = obj.get("meta")
                if isinstance(meta, dict):
                    meta["title_inferred"] = True

    return obj


def extract_entry_fields(obj: Dict[str, Any], file_path: Path, dataset_name: str) -> Dict[str, Any]:
    entry_id = obj.get("id") or obj.get("byte_id") or file_path.stem
    title = obj.get("title") or ""
    tags = obj.get("tags") if isinstance(obj.get("tags"), list) else []
    meta = obj.get("meta") if isinstance(obj.get("meta"), dict) else {}
    entity_type = meta.get("entity_type") if isinstance(meta.get("entity_type"), str) else ""
    summary = meta.get("summary") if isinstance(meta.get("summary"), str) else ""
    return {
        "dataset": dataset_name,
        "id": entry_id,
        "title": title,
        "path": str(file_path.relative_to(DATASETS_DIR)),
        "tags": tags,
        "entity_type": entity_type,
        "summary": summary,
    }


def write_manifest(entries: List[Dict[str, Any]], identity: SiteIdentity) -> None:
    entries_sorted = sorted(entries, key=lambda e: (e["dataset"], str(e["id"])))
    manifest = {
        "schema": "dkharlanau.dataset.manifest",
        "schema_version": "1.1",
        "generated_at_utc": _now_iso(),
        "creator": {
            "name": "Dzmitryi Kharlanau",
            "role": "SAP Lead",
            "website": identity.website,
            "linkedin": identity.linkedin,
        },
        "datasets_root": "datasets",
        "count": len(entries_sorted),
        "entries": entries_sorted,
    }
    (DATASETS_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_readme(identity: SiteIdentity) -> None:
    website = identity.website or "https://dkharlanau.github.io"
    linkedin = identity.linkedin or "https://www.linkedin.com/in/dkharlanau"
    text = (
        "# Datasets\n\n"
        "Curated, machine-readable \"bytes\" for writing and reuse.\n\n"
        "Creator\n"
        "- Name: Dzmitryi Kharlanau\n"
        "- Role: SAP Lead\n"
        f"- Website: {website}\n"
        f"- LinkedIn: {linkedin}\n\n"
        "Attribution\n"
        "- Please cite: Dzmitryi Kharlanau (SAP Lead) and link back to the Website/LinkedIn.\n\n"
        "Index\n"
        "- See `manifest.json` for a complete machine-readable index of all entries.\n"
    )
    (DATASETS_DIR / "README.md").write_text(text, encoding="utf-8")


def main() -> int:
    if not DATASETS_DIR.exists():
        print(f"ERROR: datasets dir not found: {DATASETS_DIR}")
        return 2

    identity = load_site_identity()
    entries: List[Dict[str, Any]] = []

    for path in iter_json_files(DATASETS_DIR):
        # Skip manifest we generate.
        if path.name in ("manifest.json", "schema.json"):
            continue

        rel = path.relative_to(DATASETS_DIR)
        dataset_name = rel.parts[0] if rel.parts else "datasets"

        parsed = _safe_json_load(path)
        if not isinstance(parsed, dict):
            continue

        enriched = enrich_one(parsed, dataset_name=dataset_name, path_rel=str(rel), identity=identity)
        path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        entries.append(extract_entry_fields(enriched, path, dataset_name))

    write_manifest(entries, identity)
    write_readme(identity)

    print(f"Enriched {len(entries)} JSON files under {DATASETS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
