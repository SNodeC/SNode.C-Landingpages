#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "usage: $0 <qualified-echo-bin-dir> <output.png>" >&2
    exit 2
fi

bin_dir=$1
output=$2
display=:94
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
XDG_CONFIG_HOME="$capture_tmp/config" \
    "$bin_dir/echoserver-legacy-in" echoserver local \
    --host 127.0.0.1 --port 18001 >"$capture_tmp/server.log" 2>&1 &
server_app_pid=$!
pids+=("$server_app_pid")
sleep 1
XDG_CONFIG_HOME="$capture_tmp/config" \
    "$bin_dir/echoclient-legacy-in" echoclient remote \
    --host 127.0.0.1 --port 18001 >"$capture_tmp/client.log" 2>&1 &
client_app_pid=$!
pids+=("$client_app_pid")
sleep 2

setsid Xvfb "$display" -screen 0 3200x1800x24 -nolisten tcp &
xvfb_pid=$!
pids+=("$xvfb_pid")
sleep 1

DISPLAY="$display" setsid xterm -fa 'DejaVu Sans Mono' -fs 20 -geometry 72x30+20+20 \
    -bg '#07101c' -fg '#dbe7f5' -bd '#304766' -bw 3 \
    -title 'SNode.C · echo server' -e bash --noprofile --norc -c \
    'printf "$ echoserver-legacy-in echoserver local --host 127.0.0.1 --port 18001\n\n"; cat "$1"; sleep 30' \
    capture "$capture_tmp/server.log" &
server_term_pid=$!
pids+=("$server_term_pid")
server_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^SNode.C · echo server$' | tail -n 1)

DISPLAY="$display" setsid xterm -fa 'DejaVu Sans Mono' -fs 20 -geometry 72x30+1620+20 \
    -bg '#07101c' -fg '#dbe7f5' -bd '#304766' -bw 3 \
    -title 'SNode.C · echo client' -e bash --noprofile --norc -c \
    'printf "$ echoclient-legacy-in echoclient remote --host 127.0.0.1 --port 18001\n\n"; cat "$1"; sleep 30' \
    capture "$capture_tmp/client.log" &
client_term_pid=$!
pids+=("$client_term_pid")
client_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^SNode.C · echo client$' | tail -n 1)
sleep 1

DISPLAY="$display" magick import -window "$server_window" "png:$capture_tmp/server.png"
DISPLAY="$display" magick import -window "$client_window" "png:$capture_tmp/client.png"

magick montage "$capture_tmp/server.png" "$capture_tmp/client.png" \
    -tile 2x1 -geometry '1530x1420+28+28' -background '#0b1020' \
    "$capture_tmp/composite-2x.png"
magick "$capture_tmp/composite-2x.png" -gravity north \
    -background '#0b1020' -splice 0x180 \
    -fill '#f8fafc' -font DejaVu-Sans-Bold -pointsize 64 \
    -annotate +0+48 'SNode.C · qualified IPv4 echo connection' \
    -filter Lanczos -resize 1600x900 -background '#0b1020' -gravity center \
    -extent 1600x900 -depth 8 -strip "$output"

identify "$output"
