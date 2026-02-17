#!/usr/bin/env python3
import argparse
import os
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"}:
                self.links.append(value)
            if name == "srcset":
                for candidate in value.split(","):
                    url = candidate.strip().split(" ")[0]
                    if url:
                        self.links.append(url)


def is_external(url):
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https", "mailto", "tel", "data", "javascript"}


def normalize_path(base_dir, url):
    if url.startswith("/"):
        return url.lstrip("/")
    return os.path.normpath(os.path.join(base_dir, url))


def main():
    parser = argparse.ArgumentParser(description="Check local links in a built Jekyll site.")
    parser.add_argument(
        "root",
        nargs="?",
        default="_site",
        help="Root directory of built site (default: _site)",
    )
    args = parser.parse_args()
    root = args.root

    if not os.path.isdir(root):
        print(f"Missing directory: {root}. Build the site before running.")
        return 1

    broken = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if not filename.endswith(".html"):
                continue
            path = os.path.join(dirpath, filename)
            rel_dir = os.path.relpath(dirpath, root)
            rel_dir = "" if rel_dir == "." else rel_dir
            with open(path, "r", encoding="utf-8") as handle:
                contents = handle.read()
            parser = LinkParser()
            parser.feed(contents)
            for url in parser.links:
                if not url or url.startswith("#") or is_external(url):
                    continue
                candidate = normalize_path(rel_dir, url)
                target = os.path.join(root, candidate)
                if os.path.isdir(target):
                    target = os.path.join(target, "index.html")
                if not os.path.exists(target):
                    broken.append((os.path.relpath(path, root), url))

    if broken:
        print("Broken local links:")
        for page, url in broken:
            print(f"- {page}: {url}")
        return 2

    print("No broken local links detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
