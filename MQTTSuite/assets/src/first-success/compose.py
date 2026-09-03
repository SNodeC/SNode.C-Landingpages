#!/usr/bin/env python3
"""Compose the canonical MQTTSuite first-success runtime evidence.

The terminal pixels come exclusively from the three qualified raw captures in
this directory.  This script crops/scales those real pixels and adds only
external publication framing and explanatory labels.

The layout was approved in Figma `MQTTSuite Publication Visuals`:
- desktop frame: 183:2
- mobile frame: 183:36

Two relationships are deliberately shown separately:
- setup order: Broker -> Subscriber -> Publisher;
- MQTT delivery: Publisher -> Broker -> Subscriber.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent

BG = (251, 253, 255)
INK = (15, 33, 74)
MUTED = (56, 82, 133)
BLUE = (38, 103, 240)
PURPLE = (109, 54, 230)
ORANGE = (235, 87, 13)
PANEL = (246, 250, 255)
BLACK = (9, 15, 24)


def font_path(pattern: str) -> str:
    return subprocess.check_output(
        ["fc-match", "-f", "%{file}\n", pattern], text=True
    ).splitlines()[0]


FONT_REGULAR = font_path("Inter:style=Regular")
FONT_BOLD = font_path("Inter:style=Bold")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def rounded(draw, box, radius, fill, outline, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, size, bold=False, fill=INK):
    draw.text(xy, value, font=font(size, bold), fill=fill)


def fit_capture(base: Image.Image, capture: Image.Image, box):
    x0, y0, x1, y1 = box
    width, height = x1 - x0, y1 - y0
    base.paste(BLACK, box)
    scale = min(width / capture.width, height / capture.height)
    resized = capture.resize(
        (round(capture.width * scale), round(capture.height * scale)),
        Image.Resampling.LANCZOS,
    )
    x = x0 + (width - resized.width) // 2
    base.paste(resized, (x, y0))


def pill(draw, x, y, width, label, color, height=34, size=14):
    rounded(draw, (x, y, x + width, y + height), 8, (246, 249, 255), color)
    draw.text(
        (x + width / 2, y + height / 2),
        label,
        font=font(size, True),
        fill=color,
        anchor="mm",
    )


def arrow(draw, x1, y, x2, color=BLUE, thickness=3, head=10):
    """Draw one filled connector shape; shaft and arrowhead cannot drift apart."""
    xh = x2 - head
    draw.polygon(
        [
            (x1, y - thickness / 2),
            (xh, y - thickness / 2),
            (xh, y - head / 2),
            (x2, y),
            (xh, y + head / 2),
            (xh, y + thickness / 2),
            (x1, y + thickness / 2),
        ],
        fill=color,
    )


def raw_captures():
    broker = Image.open(HERE / "broker-raw.png").convert("RGB").crop((0, 0, 1588, 170))
    subscriber = Image.open(HERE / "subscriber-raw.png").convert("RGB").crop((0, 0, 1588, 590))
    publisher = Image.open(HERE / "publisher-raw.png").convert("RGB").crop((0, 0, 1588, 450))
    return broker, subscriber, publisher


def desktop(broker, subscriber, publisher):
    image = Image.new("RGB", (1500, 860), BG)
    draw = ImageDraw.Draw(image)

    text(draw, (36, 24), "First successful end-to-end MQTT publication", 38, True)
    text(
        draw,
        (36, 76),
        "Real runtime capture · setup order and MQTT delivery shown separately",
        18,
        fill=MUTED,
    )

    text(draw, (36, 119), "Setup order", 15, True)
    pill(draw, 145, 111, 125, "1  Broker", BLUE)
    arrow(draw, 278, 128, 330)
    pill(draw, 338, 111, 150, "2  Subscriber", ORANGE)
    arrow(draw, 496, 128, 548)
    pill(draw, 556, 111, 142, "3  Publisher", PURPLE)

    text(draw, (790, 119), "MQTT delivery", 15, True)
    pill(draw, 914, 111, 120, "Publisher", PURPLE)
    arrow(draw, 1042, 128, 1094)
    pill(draw, 1102, 111, 105, "Broker", BLUE)
    arrow(draw, 1215, 128, 1267)
    pill(draw, 1275, 111, 145, "Subscriber", ORANGE)

    rounded(draw, (28, 165, 1472, 375), 14, PANEL, BLUE, 2)
    text(draw, (48, 180), "Broker", 20, True, BLUE)
    rounded(draw, (46, 214, 1454, 355), 10, BLACK, BLACK)
    fit_capture(image, broker, (46, 214, 1454, 355))

    rounded(draw, (28, 395, 734, 750), 14, (251, 249, 255), ORANGE, 2)
    text(draw, (48, 410), "Subscriber", 20, True, ORANGE)
    rounded(draw, (46, 444, 716, 730), 10, BLACK, BLACK)
    fit_capture(image, subscriber, (46, 444, 716, 730))

    rounded(draw, (766, 395, 1472, 750), 14, (252, 250, 255), PURPLE, 2)
    text(draw, (786, 410), "Publisher", 20, True, PURPLE)
    rounded(draw, (784, 444, 1454, 730), 10, BLACK, BLACK)
    fit_capture(image, publisher, (784, 444, 1454, 730))

    rounded(draw, (28, 780, 1472, 832), 14, (247, 250, 255), (180, 204, 245))
    text(
        draw,
        (50, 797),
        "QoS 1 representative publication · edge-lab/room-01/temperature · subscriber receipt: QoS 1 · Retain false · Dup false",
        14,
        fill=MUTED,
    )
    image.save(OUT / "first-success-terminal.png", optimize=True)


def mobile(broker, subscriber, publisher):
    image = Image.new("RGB", (620, 1350), BG)
    draw = ImageDraw.Draw(image)

    text(draw, (24, 20), "First successful end-to-end", 29, True)
    text(draw, (24, 55), "MQTT publication", 29, True)
    text(draw, (24, 98), "Real runtime capture", 16, fill=MUTED)

    text(draw, (24, 135), "Setup order", 14, True)
    pill(draw, 116, 127, 110, "1  Broker", BLUE, 32, 12)
    arrow(draw, 234, 143, 266, thickness=2, head=8)
    pill(draw, 274, 127, 134, "2  Subscriber", ORANGE, 32, 12)
    arrow(draw, 416, 143, 448, thickness=2, head=8)
    pill(draw, 456, 127, 140, "3  Publisher", PURPLE, 32, 12)

    def panel(y, height, label, color, capture):
        rounded(draw, (20, y, 600, y + height), 14, (249, 251, 255), color, 2)
        text(draw, (38, y + 12), label, 18, True, color)
        rounded(draw, (36, y + 44, 584, y + height - 16), 10, BLACK, BLACK)
        fit_capture(image, capture, (36, y + 44, 584, y + height - 16))

    panel(180, 205, "1  Broker", BLUE, broker)
    panel(405, 330, "2  Subscriber", ORANGE, subscriber)
    panel(755, 290, "3  Publisher", PURPLE, publisher)

    text(draw, (24, 1070), "MQTT delivery", 14, True)
    pill(draw, 125, 1062, 105, "Publisher", PURPLE, 32, 12)
    arrow(draw, 238, 1078, 270, thickness=2, head=8)
    pill(draw, 278, 1062, 90, "Broker", BLUE, 32, 12)
    arrow(draw, 376, 1078, 408, thickness=2, head=8)
    pill(draw, 416, 1062, 135, "Subscriber", ORANGE, 32, 12)

    rounded(draw, (20, 1120, 600, 1200), 14, (247, 250, 255), (180, 204, 245))
    text(draw, (38, 1137), "QoS 1 · edge-lab/room-01/temperature", 13, fill=MUTED)
    text(
        draw,
        (38, 1162),
        "Subscriber receipt proves delivery (QoS 1 · Retain false · Dup false)",
        12,
        fill=MUTED,
    )
    image.save(OUT / "first-success-terminal-mobile.png", optimize=True)


def main():
    captures = raw_captures()
    desktop(*captures)
    mobile(*captures)


if __name__ == "__main__":
    main()
