from pathlib import Path

path = Path("scripts/audit_indexability.py")
text = path.read_text(encoding="utf-8")
start_marker = "    for canonical, paths in all_canonicals.items():\n"
end_marker = "    # --- CSV output"
start = text.find(start_marker)
if start == -1:
    raise SystemExit("Duplicate canonical section start not found")
end = text.find(end_marker, start)
if end == -1:
    raise SystemExit("Duplicate canonical section end not found")

replacement = '''    for canonical, paths in all_canonicals.items():
        if len(paths) > 1:
            canonical_rows = [row for row in rows if row["canonical"] == canonical]
            indexable_rows = [row for row in canonical_rows if "noindex" not in row["robots"].lower()]
            if len(indexable_rows) > 1:
                indexable_paths = [row["output_path"] for row in indexable_rows]
                for row in indexable_rows:
                    if "duplicate_canonical" not in row["classification"]:
                        row["classification"] += ", duplicate_canonical" if row["classification"] != "indexable_ok" else "duplicate_canonical"
                critical_issues.append(f"Duplicate canonical '{canonical}' on {', '.join(indexable_paths)}")

'''

path.write_text(text[:start] + replacement + text[end:], encoding="utf-8")
