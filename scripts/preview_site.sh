#!/usr/bin/env bash
set -euo pipefail

# Local preview for this Jekyll site (no git commit/push required).
# Usage:
#   ./scripts/preview_site.sh
#
# Notes:
# - Installs Ruby gems via Bundler (into vendor/bundle) if needed.
# - Runs `jekyll serve` with livereload at http://127.0.0.1:4000
# - If ports are busy, the script stops an existing Jekyll for this repo (when found),
#   otherwise it automatically increments to the next free port.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# Some environments can have a minimal PATH.
# Keep user toolchains (rbenv/asdf/homebrew) first, and only append missing system paths.
PATH="${PATH:-}"
for p in /opt/homebrew/bin /opt/homebrew/sbin /usr/local/bin /usr/local/sbin /usr/bin /bin /usr/sbin /sbin; do
  case ":$PATH:" in
    *":$p:"*) ;;
    *) PATH="${PATH:+$PATH:}$p" ;;
  esac
done
export PATH

# If rbenv is installed but the current shell didn't initialize it, `ruby` may still
# resolve to the system Ruby. Prepend rbenv shims so `.ruby-version` is honored.
if command -v rbenv >/dev/null 2>&1; then
  RBENV_ROOT="$(rbenv root 2>/dev/null || true)"
  if [[ -n "${RBENV_ROOT}" && -d "${RBENV_ROOT}/shims" ]]; then
    export PATH="${RBENV_ROOT}/shims:${PATH}"
  fi

  if [[ -f ".ruby-version" ]]; then
    RBENV_VERSION="$(tr -d '[:space:]' < .ruby-version)"
    export RBENV_VERSION
  fi
fi

rb_exec() {
  if command -v rbenv >/dev/null 2>&1; then
    rbenv exec "$@"
  else
    "$@"
  fi
}

port_pids() {
  local port="$1"
  if command -v lsof >/dev/null 2>&1; then
    lsof -nP -iTCP:"$port" -sTCP:LISTEN -t 2>/dev/null | tr '\n' ' '
  fi
}

port_in_use() {
  local port="$1"
  local pids
  pids="$(port_pids "$port")"
  [[ -n "${pids// /}" ]]
}

stop_pid() {
  local pid="$1"
  local i

  if ! kill -0 "$pid" >/dev/null 2>&1; then
    return 0
  fi

  kill "$pid" >/dev/null 2>&1 || true
  for i in $(seq 1 20); do
    if ! kill -0 "$pid" >/dev/null 2>&1; then
      return 0
    fi
    sleep 0.25
  done
  kill -9 "$pid" >/dev/null 2>&1 || true
}

ensure_free_port() {
  local label="$1"
  local port="$2"
  local tries=0

  while port_in_use "$port"; do
    local pids cmd pid stopped_any=0
    pids="$(port_pids "$port")"

    for pid in $pids; do
      cmd="$(ps -p "$pid" -o command= 2>/dev/null || true)"
      if [[ -n "$cmd" && "$cmd" == *jekyll* && "$cmd" == *"$ROOT_DIR"* ]]; then
        echo "Port ${port} is in use by an existing Jekyll for this repo (pid ${pid}). Stopping it..." >&2
        stop_pid "$pid"
        stopped_any=1
      fi
    done

    if port_in_use "$port"; then
      if [[ "$stopped_any" -eq 1 ]]; then
        echo "Port ${port} is still busy after stopping Jekyll. Picking a new port..." >&2
      else
        echo "Port ${port} is in use. Picking a new port..." >&2
      fi

      port="$((port + 1))"
      tries="$((tries + 1))"
      if [[ "$tries" -gt 30 ]]; then
        echo "ERROR: Could not find a free ${label} port after 30 attempts (starting from ${2})." >&2
        echo "Try setting ${label} explicitly, e.g.: ${label}=4011 ..." >&2
        exit 3
      fi
    fi
  done

  echo "$port"
}

if [[ ! -f "Gemfile" ]]; then
  echo "ERROR: Gemfile not found in repo root: $ROOT_DIR" >&2
  exit 1
fi

if ! command -v ruby >/dev/null 2>&1; then
  echo "ERROR: ruby not found. Install Ruby (or use your existing Ruby toolchain), then re-run." >&2
  exit 1
fi

ruby_major="$(rb_exec ruby -e 'print RUBY_VERSION.split(".")[0]' 2>/dev/null || echo 0)"
if [[ "${ruby_major}" -lt 3 ]]; then
  echo "ERROR: Ruby >= 3.0 is required for this site (your Ruby is: $(rb_exec ruby -v))." >&2
  echo "" >&2
  echo "Fix options:" >&2
  echo "  1) Install Ruby 3.2.x (recommended) and re-run. This repo includes .ruby-version: $(cat .ruby-version 2>/dev/null || echo '3.2.x')." >&2
  echo "  2) If you have Docker, run: ./scripts/preview_site_docker.sh" >&2
  exit 2
fi

if ! command -v bundle >/dev/null 2>&1; then
  echo "Bundler not found. Installing bundler..." >&2
  rb_exec gem install bundler
fi

# Keep gems local to the repo so the script is safe/repeatable.
rb_exec bundle config set --local path "vendor/bundle" >/dev/null

echo "Checking gems..."
if ! rb_exec bundle check >/dev/null 2>&1; then
  echo "Installing gems (this can take a few minutes the first time)..." >&2
  rb_exec bundle install
fi

echo "Starting Jekyll dev server..."
JEKYLL_HOST="${JEKYLL_HOST:-127.0.0.1}"
JEKYLL_PORT="$(ensure_free_port "JEKYLL_PORT" "${JEKYLL_PORT:-4000}")"
JEKYLL_LIVERELOAD_PORT="$(ensure_free_port "JEKYLL_LIVERELOAD_PORT" "${JEKYLL_LIVERELOAD_PORT:-35729}")"

echo "- URL:        http://${JEKYLL_HOST}:${JEKYLL_PORT}/" >&2
echo "- LiveReload: http://${JEKYLL_HOST}:${JEKYLL_LIVERELOAD_PORT}" >&2
echo "Cleaning _site cache to avoid stale output..." >&2
rb_exec bundle exec jekyll clean >/dev/null 2>&1 || true
if command -v rbenv >/dev/null 2>&1; then
  exec rbenv exec bundle exec jekyll serve \
    --livereload \
    --livereload-port "$JEKYLL_LIVERELOAD_PORT" \
    --host "$JEKYLL_HOST" \
    --port "$JEKYLL_PORT"
else
  exec bundle exec jekyll serve \
    --livereload \
    --livereload-port "$JEKYLL_LIVERELOAD_PORT" \
    --host "$JEKYLL_HOST" \
    --port "$JEKYLL_PORT"
fi
