#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 3 ]]; then
    echo "usage: $0 <native-2x.png> <browser-2x.png> <output.png>" >&2
    exit 2
fi

native_source=$1
browser_source=$2
output=$3
capture_tmp=$(mktemp -d)
trap 'rm -rf "$capture_tmp"' EXIT

# Work at 2× throughout. Both panels preserve real application pixels; the
# only transformations are crop, scale, labels, border, and final downsample.
magick "$native_source" \
    -resize '1472x920^' -gravity center -extent 1472x920 \
    "$capture_tmp/native.png"
magick "$browser_source" \
    -resize '1472x920' -gravity center -background '#f8fafc' -extent 1472x920 \
    "$capture_tmp/browser.png"

magick -size 3200x1800 'gradient:#0b1020-#182238' \
    -fill '#f8fafc' -font DejaVu-Sans-Bold -pointsize 92 \
    -draw "text 96,138 'One workflow. Two presentations.'" \
    -fill '#aebbd0' -font DejaVu-Sans -pointsize 39 \
    -draw "text 100,210 'Matching synthetic state from qualified native and browser builds'" \
    -fill '#182238' -stroke '#33435f' -strokewidth 3 \
    -draw 'roundrectangle 78,278 1570,1222 28,28' \
    -draw 'roundrectangle 1630,278 3122,1222 28,28' \
    "$capture_tmp/canvas.png"

magick "$capture_tmp/canvas.png" \
    "$capture_tmp/native.png" -geometry +88+288 -composite \
    "$capture_tmp/browser.png" -geometry +1640+288 -composite \
    -fill '#2563eb' -stroke none -draw 'roundrectangle 96,1266 508,1350 42,42' \
    -fill '#ffffff' -font DejaVu-Sans-Bold -pointsize 36 \
    -draw "text 140,1322 'NATIVE · Qt 6'" \
    -fill '#d97706' -draw 'roundrectangle 1648,1266 2146,1350 42,42' \
    -fill '#ffffff' -draw "text 1692,1322 'BROWSER · React'" \
    -fill '#d6deeb' -font DejaVu-Sans -pointsize 38 \
    -draw "text 98,1442 'Select a thread · inspect activity · continue the conversation'" \
    -fill '#7f8da6' -pointsize 31 \
    -draw "text 100,1520 'CodexUI presents shared protocol state without owning conversation semantics.'" \
    -filter Lanczos -resize 1600x900 -depth 8 -strip \
    "$output"
