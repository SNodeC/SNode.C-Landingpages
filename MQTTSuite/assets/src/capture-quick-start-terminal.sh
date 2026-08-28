#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "usage: $0 <qualified-mqttsuite-build-dir> <output.png>" >&2
    exit 2
fi

build_dir=$1
output=$2
display=:93
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
broker=(
    "$build_dir/mqttbroker/mqttbroker" --config-file /dev/null --log-level 4
    in-mqtt local --host 127.0.0.1 --port 18885
    in-mqtts --disabled in6-mqtt --disabled in6-mqtts --disabled
    un-mqtt --disabled un-mqtts --disabled in-http --disabled
    in-https --disabled in6-http --disabled in6-https --disabled
    un-http --disabled un-https --disabled
)
subscriber=(
    "$build_dir/mqttcli/mqttcli" --config-file /dev/null --log-level 4
    in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885
    session --client-id landing-subscriber --qos 1
    sub --topic edge-lab/room-01/temperature
)
publisher=(
    "$build_dir/mqttcli/mqttcli" --config-file /dev/null --log-level 4
    in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885
    session --client-id landing-publisher --qos 1
    pub --topic edge-lab/room-01/temperature
    --message '{"value":21.7,"unit":"C"}'
)

XDG_CONFIG_HOME="$capture_tmp/config" "${broker[@]}" >"$capture_tmp/broker.log" 2>&1 &
broker_pid=$!
pids+=("$broker_pid")
sleep 1
XDG_CONFIG_HOME="$capture_tmp/config" "${subscriber[@]}" >"$capture_tmp/subscriber.log" 2>&1 &
subscriber_pid=$!
pids+=("$subscriber_pid")
sleep 1
XDG_CONFIG_HOME="$capture_tmp/config" "${publisher[@]}" >"$capture_tmp/publisher.log" 2>&1 &
publisher_pid=$!
pids+=("$publisher_pid")
sleep 2
kill -KILL "$publisher_pid" 2>/dev/null || true

rg 'listener started|client connected|SUBSCRIBE|PUBLISH|edge-lab|routed|disconnected' \
    "$capture_tmp/broker.log" | head -n 12 >"$capture_tmp/broker-display.log" || true
rg 'connected|MQTT Subscribe|MQTT Publish|edge-lab|QoS:|Retain:|"unit"|"value"' \
    "$capture_tmp/subscriber.log" | head -n 14 >"$capture_tmp/subscriber-display.log" || true
rg 'connected|MQTT Publish|edge-lab|QoS:|acknowledg|disconnected' \
    "$capture_tmp/publisher.log" | head -n 10 >"$capture_tmp/publisher-display.log" || true

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
        -bd '#304766' -bw 3 -title "$title" -e bash --noprofile --norc -c \
        'printf "%s\n\n" "$1"; cat "$2"; sleep 30' capture "$command_text" "$log_file" &
    pane_pid=$!
    pids+=("$pane_pid")
}

launch_pane 'MQTTSuite · broker' '60x38+10+10' \
    '$ mqttbroker --config-file /dev/null --log-level 4 in-mqtt local --host 127.0.0.1 --port 18885 in-mqtts --disabled in6-mqtt --disabled in6-mqtts --disabled un-mqtt --disabled un-mqtts --disabled in-http --disabled in-https --disabled in6-http --disabled in6-https --disabled un-http --disabled un-https --disabled' \
    "$capture_tmp/broker-display.log"
broker_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^MQTTSuite · broker$' | tail -n 1)

launch_pane 'MQTTSuite · subscriber' '60x38+1070+10' \
    '$ mqttcli --config-file /dev/null --log-level 4 in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 session --client-id landing-subscriber --qos 1 sub --topic edge-lab/room-01/temperature' \
    "$capture_tmp/subscriber-display.log"
subscriber_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^MQTTSuite · subscriber$' | tail -n 1)

launch_pane 'MQTTSuite · publisher' '60x38+2130+10' \
    '$ mqttcli --config-file /dev/null --log-level 4 in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 session --client-id landing-publisher --qos 1 pub --topic edge-lab/room-01/temperature --message {"value":21.7,"unit":"C"}' \
    "$capture_tmp/publisher-display.log"
publisher_window=$(DISPLAY="$display" xdotool search --sync --onlyvisible --name '^MQTTSuite · publisher$' | tail -n 1)
sleep 1

DISPLAY="$display" magick import -window "$broker_window" "png:$capture_tmp/broker.png"
DISPLAY="$display" magick import -window "$subscriber_window" "png:$capture_tmp/subscriber.png"
DISPLAY="$display" magick import -window "$publisher_window" "png:$capture_tmp/publisher.png"

for pane in broker subscriber publisher; do
    magick "$capture_tmp/$pane.png" -resize '1000x1450' -gravity north \
        -background '#07101c' -extent 1000x1450 "$capture_tmp/$pane-panel.png"
done
magick -size 3200x1800 xc:'#0b1020' \
    -fill '#f8fafc' -font DejaVu-Sans-Bold -pointsize 62 \
    -gravity north -annotate +0+42 'MQTTSuite · one MQTT 3.1.1 message, end to end' \
    -fill '#55d67a' -pointsize 34 -gravity northwest \
    -annotate +40+170 'BROKER' -annotate +1100+170 'SUBSCRIBER' \
    -annotate +2160+170 'PUBLISHER' \
    "$capture_tmp/broker-panel.png" -geometry +40+230 -composite \
    "$capture_tmp/subscriber-panel.png" -geometry +1100+230 -composite \
    "$capture_tmp/publisher-panel.png" -geometry +2160+230 -composite \
    -filter Lanczos -resize 1600x900 -depth 8 -strip "$output"

identify "$output"
