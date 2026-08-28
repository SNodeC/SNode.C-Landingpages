#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 2 || $# -gt 4 ]]; then
    echo "usage: $0 <qualified-codex-ui> <output-2x.png> [bridge-port=14581] [display=:97]" >&2
    exit 2
fi

codex_ui=$1
output=$2
bridge_port=${3:-14581}
x_display=${4:-:97}
xvfb_pid=
ui_pid=

cleanup() {
    if [[ -n "$ui_pid" ]]; then
        kill "$ui_pid" 2>/dev/null || true
        wait "$ui_pid" 2>/dev/null || true
    fi
    if [[ -n "$xvfb_pid" ]]; then
        kill "$xvfb_pid" 2>/dev/null || true
        wait "$xvfb_pid" 2>/dev/null || true
    fi
}
trap cleanup EXIT

Xvfb "$x_display" -screen 0 3200x2000x24 -nolisten tcp &
xvfb_pid=$!
sleep 1

env DISPLAY="$x_display" QT_QPA_PLATFORM=xcb QT_SCALE_FACTOR=2 \
    "$codex_ui" \
    codex-ui-unix --disabled \
    codex-ui-ipv4 --disabled=false \
    remote --host 127.0.0.1 --port "$bridge_port" &
ui_pid=$!

window_id=$(DISPLAY="$x_display" xdotool search --sync --onlyvisible --pid "$ui_pid" | head -n 1)
sleep 2

# The synthetic fixture's first thread is the transport-boundary review. At 2×
# UI scale this click selects that real row and exposes the matching completed
# turn used by the browser capture.
DISPLAY="$x_display" xdotool mousemove --window "$window_id" 280 540 click 1
sleep 2
DISPLAY="$x_display" magick import -window "$window_id" "png:$output"

identify "$output"
