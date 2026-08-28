#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 4 ]]; then
    echo "usage: $0 <codex-bridge> <codex-bridge-client> <synthetic-app-server> <output.png>" >&2
    exit 2
fi

bridge=$1
client=$2
provider=$3
output=$4
display=:92
capture_tmp=$(mktemp -d)
pids=()

cleanup() {
    for pid in "${pids[@]}"; do
        kill -KILL -- "-$pid" 2>/dev/null || kill -KILL "$pid" 2>/dev/null || true
    done
    rm -rf "$capture_tmp"
}
trap cleanup EXIT

mkdir -p "$capture_tmp/config"
setsid env XDG_CONFIG_HOME="$capture_tmp/config" \
    "$bridge" --config-file /dev/null --log-level 4 \
    codex-bridge --disabled \
    codex-bridge-ipv4 --disabled=false local --host 127.0.0.1 --port 14500 \
    codex --app-server-transport stdio --app-server-executable "$provider" \
    >"$capture_tmp/bridge.log" 2>&1 &
bridge_pid=$!
pids+=("$bridge_pid")
sleep 2

{
    sleep 3
    printf 'threads\n'
    sleep 2
    printf 'quit\n'
} | timeout 10 "$client" --config-file /dev/null --log-level 4 \
    codex-bridge-client-unix --disabled \
    codex-bridge-client-ipv4 --disabled=false \
    remote --host 127.0.0.1 --port 14500 codex-client \
    >"$capture_tmp/client.log" 2>&1 || true

kill -KILL -- "-$bridge_pid" 2>/dev/null || true
rg 'synthetic app-server|app-server spawned|observing app-server' \
    "$capture_tmp/bridge.log" >"$capture_tmp/provider-display.log" || true
rg 'listener bound|listener started|frontend connected|frontend disconnected|app-server spawned' \
    "$capture_tmp/bridge.log" >"$capture_tmp/bridge-display.log" || true
rg 'connected using|bridge.connection|bridge.provider|bridge.controller|"role"|"state"|"name"|"cwd"|"data"|disconnected' \
    "$capture_tmp/client.log" | head -n 22 >"$capture_tmp/client-display.log" || true

setsid Xvfb "$display" -screen 0 3200x1800x24 -nolisten tcp &
xvfb_pid=$!
pids+=("$xvfb_pid")
sleep 1

launch_pane() {
    local title=$1
    local geometry=$2
    local command_text=$3
    local log_file=$4
    DISPLAY="$display" setsid xterm -fa 'DejaVu Sans Mono' -fs 16 \
        -geometry "$geometry" -bg '#07101c' -fg '#dbe7f5' \
        -bd '#564178' -bw 3 -title "$title" -e bash --noprofile --norc -c \
        'printf "%s\n\n" "$1"; cat "$2"; sleep 30' capture "$command_text" "$log_file" &
    pane_pid=$!
    pids+=("$pane_pid")
}

launch_pane 'AISuite · provider' '60x38+10+10' \
    '$ synthetic-app-server.mjs app-server  # isolated stdio qualification fixture' \
    "$capture_tmp/provider-display.log"
provider_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^AISuite · provider$' | tail -n 1)

launch_pane 'AISuite · bridge' '60x38+1070+10' \
    '$ codex-bridge --config-file /dev/null --log-level 4 codex-bridge --disabled codex-bridge-ipv4 --disabled=false local --host 127.0.0.1 --port 14500 codex --app-server-transport stdio --app-server-executable synthetic-app-server.mjs' \
    "$capture_tmp/bridge-display.log"
bridge_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^AISuite · bridge$' | tail -n 1)

launch_pane 'AISuite · reference client' '60x38+2130+10' \
    '$ codex-bridge-client --config-file /dev/null --log-level 4 codex-bridge-client-unix --disabled codex-bridge-client-ipv4 --disabled=false remote --host 127.0.0.1 --port 14500 codex-client\n> threads' \
    "$capture_tmp/client-display.log"
client_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^AISuite · reference client$' | tail -n 1)
sleep 1

DISPLAY="$display" magick import -window "$provider_window" "png:$capture_tmp/provider.png"
DISPLAY="$display" magick import -window "$bridge_window" "png:$capture_tmp/bridge.png"
DISPLAY="$display" magick import -window "$client_window" "png:$capture_tmp/client.png"

for pane in provider bridge client; do
    magick "$capture_tmp/$pane.png" -resize '1000x1450' -gravity north \
        -background '#07101c' -extent 1000x1450 "$capture_tmp/$pane-panel.png"
done
magick -size 3200x1800 xc:'#0b1020' \
    -fill '#f8fafc' -font DejaVu-Sans-Bold -pointsize 62 \
    -gravity north -annotate +0+42 'AISuite · provider, bridge, and reference client' \
    -fill '#c596ff' -pointsize 34 -gravity northwest \
    -annotate +40+170 'PROVIDER · STDIO' -annotate +1100+170 'CODEX-BRIDGE · IPv4' \
    -annotate +2160+170 'REFERENCE CLIENT' \
    "$capture_tmp/provider-panel.png" -geometry +40+230 -composite \
    "$capture_tmp/bridge-panel.png" -geometry +1100+230 -composite \
    "$capture_tmp/client-panel.png" -geometry +2160+230 -composite \
    -filter Lanczos -resize 1600x900 -depth 8 -strip "$output"

identify "$output"
