#!/usr/bin/env python3
"""Stage a small Jekyll source tree for rendered feed contract checks.

The fixture copies the real feed templates, real reviewed publication sources,
real changelog data, and the shared RSS autodiscovery include. It deliberately
avoids building the rest of the site so the subscription gate stays fast and
independent from unrelated page-generation failures.
"""

from __future__ import annotations

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / ".rss-ci-source"


def copy_path(relative: str) -> None:
    source = ROOT / relative
    target = FIXTURE / relative
    if not source.exists():
        raise SystemExit(f"RSS CI fixture source is missing: {relative}")
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, target)
    else:
        shutil.copy2(source, target)


def main() -> None:
    if FIXTURE.exists():
        shutil.rmtree(FIXTURE)
    FIXTURE.mkdir(parents=True)

    for relative in (
        "_blog",
        "_data/changelog.yml",
        "_includes/seo/page-machine-links.html",
        "feed.xml",
        "rss.xml",
        "blog/feed.xml",
    ):
        copy_path(relative)

    (FIXTURE / "index.html").write_text(
        """---
layout: null
permalink: /
---
<!doctype html>
<html lang="en">
<head>
{% include seo/page-machine-links.html %}
</head>
<body></body>
</html>
""",
        encoding="utf-8",
    )

    # Production metadata/config remains the first config file. This override
    # disables unrelated plugins/output while preserving the real blog URL
    # contract used by the feed templates.
    (FIXTURE / "_config.rss-ci.yml").write_text(
        """plugins: []
collections:
  blog:
    output: false
    permalink: /blog/:slug/
  notes:
    output: false
  radar:
    output: false
  news:
    output: false
  glossary:
    output: false
defaults: []
""",
        encoding="utf-8",
    )

    print(f"Staged RSS CI fixture at {FIXTURE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
