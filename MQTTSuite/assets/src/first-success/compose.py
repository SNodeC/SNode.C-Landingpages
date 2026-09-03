#!/usr/bin/env python3
"""Compose canonical first-success runtime evidence from qualified raw pixels.

The terminal content is never reconstructed. This script crops/scales the three
qualified raw captures and adds only publication framing plus explanatory labels.
Visual constants mirror SNode.C-Book/assets/figures/src/snodec-figure-style.tex.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
BROKER = ROOT / 'broker-raw.png'
SUBSCRIBER = ROOT / 'subscriber-raw.png'
PUBLISHER = ROOT / 'publisher-raw.png'
OUT_DESKTOP = ROOT.parent.parent / 'first-success-terminal.png'
OUT_MOBILE = ROOT.parent.parent / 'first-success-terminal-mobile.png'

# Canonical SNode.C figure palette, mirrored from snodec-figure-style.tex.
INK = '#17212B'
MUTED = '#4B5F68'
RULE = '#7A8B93'
BLUE = '#0B4F6C'
BLUE_SOFT = '#E3F2F8'
GREEN = '#1F7A68'
GREEN_SOFT = '#E5F4EF'
GRAY_SOFT = '#F1F3F2'
WHITE = '#FFFFFF'

import subprocess


def tex_font(name: str) -> str:
    return subprocess.check_output(['kpsewhich', name], text=True).strip()


FONT_REG = tex_font('lmsans10-regular.otf')
FONT_BOLD = tex_font('lmsans10-bold.otf')


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def rounded(draw, box, fill, outline=RULE, width=2, radius=10):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def crop_scale(src, crop, width):
    im = Image.open(src).convert('RGB').crop(crop)
    scale = width / im.width
    return im.resize((width, max(1, round(im.height * scale))), Image.Resampling.LANCZOS)


def arrow(draw, x1, y, x2, color=MUTED, width=3):
    # One continuous shaft with attached triangular head, matching the canonical
    # directionality rule even though this composition is raster evidence.
    head = 12
    draw.line((x1, y, x2 - head, y), fill=color, width=width)
    draw.polygon([(x2, y), (x2 - head, y - 7), (x2 - head, y + 7)], fill=color)


def role_chip(draw, x, y, w, h, text, kind='client'):
    if kind == 'broker':
        fill, line = BLUE_SOFT, BLUE
    else:
        fill, line = GREEN_SOFT, GREEN
    rounded(draw, (x, y, x+w, y+h), fill, line, 2, 8)
    f = font(17, True)
    bbox = draw.textbbox((0, 0), text, font=f)
    draw.text((x + (w - (bbox[2]-bbox[0]))/2,
               y + (h - (bbox[3]-bbox[1]))/2 - bbox[1]), text, font=f, fill=INK)


def semantic_row(draw, y, label, roles, canvas_w, left=40):
    label_f = font(18, True)
    draw.text((left, y + 8), label, font=label_f, fill=INK)
    label_w = draw.textbbox((0, 0), label, font=label_f)[2]
    x = max(left + label_w + 28, 250)
    chip_w, chip_h, gap = 122, 38, 40
    for i, role in enumerate(roles):
        role_chip(draw, x, y, chip_w, chip_h, role, 'broker' if role == 'Broker' else 'client')
        if i < len(roles)-1:
            arrow(draw, x + chip_w + 8, y + chip_h/2, x + chip_w + gap - 8)
        x += chip_w + gap


def evidence_card(canvas, xy, size, title, number, source, crop, accent, soft):
    x, y = xy
    w, h = size
    d = ImageDraw.Draw(canvas)
    rounded(d, (x, y, x+w, y+h), WHITE, accent, 2, 10)
    header_h = 50
    d.rounded_rectangle((x, y, x+w, y+header_h), radius=10, fill=soft)
    d.rectangle((x, y+header_h-10, x+w, y+header_h), fill=soft)
    r = 16
    d.ellipse((x+18, y+9, x+18+2*r, y+9+2*r), fill=accent)
    nf = font(17, True)
    nb = d.textbbox((0,0), str(number), font=nf)
    d.text((x+18+r-(nb[2]-nb[0])/2, y+9+r-(nb[3]-nb[1])/2-nb[1]), str(number), font=nf, fill=WHITE)
    d.text((x+62, y+13), title, font=font(20, True), fill=accent)
    pad = 14
    screenshot_w = w - 2*pad
    shot = crop_scale(source, crop, screenshot_w)
    max_h = h - header_h - 2*pad
    if shot.height > max_h:
        shot = shot.resize((screenshot_w, max_h), Image.Resampling.LANCZOS)
    canvas.paste(shot, (x+pad, y+header_h+pad))


def make_desktop():
    W = 1536
    margin = 28
    # Full-width evidence cards keep terminal text legible at GitHub's typical
    # ~830 px content width. The historical side-by-side layout made the proof
    # unreadably small after README scaling.
    broker_crop = (0, 0, 1588, 150)
    subscriber_crop = (0, 0, 1588, 575)
    publisher_crop = (0, 0, 1588, 430)
    card_w = W - 2*margin
    shot_w = card_w - 28
    def card_height(crop):
        crop_h = crop[3] - crop[1]
        crop_w = crop[2] - crop[0]
        shot_h = round(crop_h * shot_w / crop_w)
        return 50 + 28 + shot_h

    broker_h = card_height(broker_crop)
    subscriber_h = card_height(subscriber_crop)
    publisher_h = card_height(publisher_crop)
    note_h = 78
    top = 238
    gap = 24
    H = top + broker_h + gap + subscriber_h + gap + publisher_h + gap + note_h + 24

    im = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(im)

    d.text((margin, 20), 'First successful end-to-end MQTT publication', font=font(41, True), fill=INK)
    d.text((margin, 72), 'Real runtime evidence · startup and MQTT delivery shown separately', font=font(21), fill=MUTED)

    rounded(d, (margin, 112, W-margin, 214), GRAY_SOFT, RULE, 2, 10)
    semantic_row(d, 124, 'Startup order', ['Broker', 'Subscriber', 'Publisher'], W, margin+20)
    semantic_row(d, 169, 'MQTT delivery', ['Publisher', 'Broker', 'Subscriber'], W, margin+20)

    y = top
    evidence_card(im, (margin, y), (card_w, broker_h),
                  'MQTTBroker — listener ready', 1,
                  BROKER, broker_crop, BLUE, BLUE_SOFT)
    y += broker_h + gap
    evidence_card(im, (margin, y), (card_w, subscriber_h),
                  'MQTTCli subscriber — subscribe before publish', 2,
                  SUBSCRIBER, subscriber_crop, GREEN, GREEN_SOFT)
    y += subscriber_h + gap
    evidence_card(im, (margin, y), (card_w, publisher_h),
                  'MQTTCli publisher — one PUBLISH', 3,
                  PUBLISHER, publisher_crop, GREEN, GREEN_SOFT)
    y += publisher_h + gap

    rounded(d, (margin, y, W-margin, y+note_h), BLUE_SOFT, BLUE, 2, 10)
    note = 'Observed delivery · QoS 1 · Retain false · Dup false · edge-lab/room-01/temperature · {"value":21.7,"unit":"C"}'
    d.text((margin+20, y+26), note, font=font(18), fill=INK)
    return im

def mobile_semantic_line(d, y, label, roles, W):
    d.text((28, y), label, font=font(19, True), fill=INK)
    value = '  →  '.join(roles)
    d.text((28, y+27), value, font=font(17), fill=MUTED)


def make_mobile():
    W = 887
    margin = 24
    broker_crop = (0, 0, 1588, 150)
    subscriber_crop = (0, 0, 1588, 575)
    publisher_crop = (0, 0, 1588, 430)
    card_w = W - 2*margin
    shot_w = card_w - 28
    def card_height(crop):
        crop_h = crop[3] - crop[1]
        crop_w = crop[2] - crop[0]
        shot_h = round(crop_h * shot_w / crop_w)
        return 50 + 28 + shot_h

    broker_h = card_height(broker_crop)
    subscriber_h = card_height(subscriber_crop)
    publisher_h = card_height(publisher_crop)
    top = 302
    gap = 24
    note_h = 82
    H = top + broker_h + gap + subscriber_h + gap + publisher_h + gap + note_h + 24

    im = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(im)

    d.text((margin, 18), 'First successful', font=font(38, True), fill=INK)
    d.text((margin, 63), 'end-to-end MQTT publication', font=font(38, True), fill=INK)
    d.text((margin, 112), 'Real runtime evidence', font=font(20), fill=MUTED)

    rounded(d, (margin, 150, W-margin, 276), GRAY_SOFT, RULE, 2, 10)
    mobile_semantic_line(d, 164, 'Startup order', ['Broker', 'Subscriber', 'Publisher'], W)
    mobile_semantic_line(d, 218, 'MQTT delivery', ['Publisher', 'Broker', 'Subscriber'], W)

    y = top
    evidence_card(im, (margin, y), (card_w, broker_h),
                  'MQTTBroker — listener ready', 1,
                  BROKER, broker_crop, BLUE, BLUE_SOFT)
    y += broker_h + gap
    evidence_card(im, (margin, y), (card_w, subscriber_h),
                  'MQTTCli subscriber — subscribed first', 2,
                  SUBSCRIBER, subscriber_crop, GREEN, GREEN_SOFT)
    y += subscriber_h + gap
    evidence_card(im, (margin, y), (card_w, publisher_h),
                  'MQTTCli publisher — one PUBLISH', 3,
                  PUBLISHER, publisher_crop, GREEN, GREEN_SOFT)
    y += publisher_h + gap

    rounded(d, (margin, y, W-margin, y+note_h), BLUE_SOFT, BLUE, 2, 10)
    d.text((margin+18, y+14), 'Observed: QoS 1 · Retain false · Dup false', font=font(18), fill=INK)
    d.text((margin+18, y+43), 'edge-lab/room-01/temperature · {"value":21.7,"unit":"C"}', font=font(15), fill=MUTED)
    return im


def save_indexed(image, path):
    # The scene uses a constrained palette; indexed PNG keeps repository assets
    # compact without changing the captured terminal content.
    indexed = image.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    indexed.save(path, optimize=True)


if __name__ == '__main__':
    save_indexed(make_desktop(), OUT_DESKTOP)
    save_indexed(make_mobile(), OUT_MOBILE)
    print(OUT_DESKTOP)
    print(OUT_MOBILE)
