#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

URL="${PREVIEW_URL:-http://127.0.0.1:${JEKYLL_PORT:-4000}/}"

# Start the local Jekyll preview; this process stays attached until stopped.
"$ROOT_DIR/scripts/preview_site.sh" &
SERVER_PID=$!

cleanup() {
  if kill -0 "$SERVER_PID" >/dev/null 2>&1; then
    kill "$SERVER_PID" >/dev/null 2>&1 || true
  fi
}

trap cleanup EXIT INT TERM

for _ in $(seq 1 40); do
  if curl -fsS "$URL" >/dev/null 2>&1; then
    break
  fi
  sleep 0.5
done

open -a "Google Chrome" "$URL"

wait "$SERVER_PID"
