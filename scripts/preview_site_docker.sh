#!/usr/bin/env bash
set -euo pipefail

# Docker-based preview for this Jekyll site.
# Usage:
#   ./scripts/preview_site_docker.sh
#
# Requires Docker Desktop.
# Opens the site at: http://127.0.0.1:4000/

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# Keep user toolchains first, and only append missing system paths.
PATH="${PATH:-}"
for p in /opt/homebrew/bin /opt/homebrew/sbin /usr/local/bin /usr/local/sbin /usr/bin /bin /usr/sbin /sbin; do
  case ":$PATH:" in
    *":$p:"*) ;;
    *) PATH="${PATH:+$PATH:}$p" ;;
  esac
done
export PATH

if ! command -v docker >/dev/null 2>&1; then
  echo "ERROR: docker not found. Install Docker Desktop, then re-run." >&2
  exit 1
fi

IMAGE="jekyll/jekyll:4.3"

echo "Starting Jekyll dev server in Docker..." >&2
echo "- Image: $IMAGE" >&2
echo "- URL:   http://127.0.0.1:4000/" >&2

# NOTE: We run as root inside the container to avoid permission issues on mounted volumes.
exec docker run --rm -it \
  -p 4000:4000 \
  -v "$ROOT_DIR:/srv/jekyll" \
  -w /srv/jekyll \
  "$IMAGE" \
  bash -lc "bundle install && bundle exec jekyll serve --livereload --incremental --host 0.0.0.0 --port 4000"
