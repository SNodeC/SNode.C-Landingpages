#!/usr/bin/env python3
"""Compose canonical first-success runtime evidence from qualified raw pixels.

The terminal content is never reconstructed. This script crops/scales the three
qualified raw captures and adds only publication framing plus explanatory labels.
All framing geometry is expressed through the canonical SNode.C figure contract.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess

ROOT = Path(__file__).resolve().parent
BROKER = ROOT / 'broker-raw.png'
SUBSCRIBER = ROOT / 'subscriber-raw.png'
PUBLISHER = ROOT / 'publisher-raw.png'
OUT_DESKTOP = ROOT.parent.parent / 'first-success-terminal.png'
OUT_MOBILE = ROOT.parent.parent / 'first-success-terminal-mobile.png'

# Canonical SNode.C palette.
INK = '#17212B'
MUTED = '#4B5F68'
RULE = '#7A8B93'
BLUE = '#0B4F6C'
GREEN = '#1F7A68'
GREEN_SOFT = '#E5F4EF'
WHITE = '#FFFFFF'


def mix_with_white(hex_color: str, pct: float) -> str:
    """xcolor-like COLOR!pct, i.e. pct% color + (100-pct)% white."""
    h = hex_color.lstrip('#')
    rgb = [int(h[i:i+2], 16) for i in (0, 2, 4)]
    out = [round((pct / 100.0) * v + (1.0 - pct / 100.0) * 255) for v in rgb]
    return '#' + ''.join(f'{v:02X}' for v in out)


# Exact adapter-derived colors used by the TikZ family.
RULE_82 = mix_with_white(RULE, 82)
MUTED_76 = mix_with_white(MUTED, 76)
GREEN_78 = mix_with_white(GREEN, 78)


def tex_font(name: str) -> str:
    return subprocess.check_output(['kpsewhich', name], text=True).strip()


FONT_REG = tex_font('lmsans10-regular.otf')
FONT_BOLD = tex_font('lmsans10-bold.otf')
FONT_MONO = tex_font('lmmono10-regular.otf')


class Metrics:
    """Canonical physical SNode.C dimensions mapped into one raster canvas."""
    def __init__(self, canvas_width_px: int, budget_mm: float, mobile: bool):
        self.px_per_mm = canvas_width_px / budget_mm
        self.mobile = mobile

    def mm(self, value: float) -> int:
        return max(1, round(value * self.px_per_mm))

    def pt(self, value: float) -> int:
        # TeX point: 72.27 pt/in.
        return max(1, round(value * (25.4 / 72.27) * self.px_per_mm))

    @property
    def title_font(self):
        return font(self.pt(12), bold=True)

    @property
    def body_font(self):
        return font(self.pt(10 if self.mobile else 9))

    @property
    def section_font(self):
        return font(self.pt(10 if self.mobile else 9), bold=True)

    @property
    def annotation_font(self):
        return font(self.pt(9 if self.mobile else 8))

    @property
    def annotation_bold_font(self):
        return font(self.pt(9 if self.mobile else 8), bold=True)

    @property
    def code_small_font(self):
        return mono_font(self.pt(9 if self.mobile else 8))


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def mono_font(size):
    return ImageFont.truetype(FONT_MONO, size)


def rounded(draw, box, fill, outline, width, radius):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def crop_scale(src, crop, width):
    im = Image.open(src).convert('RGB').crop(crop)
    scale = width / im.width
    return im.resize((width, max(1, round(im.height * scale))), Image.Resampling.LANCZOS)


def text_size(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0], b[3] - b[1], b


def draw_centered_text(draw, box, text, fnt, fill):
    x1, y1, x2, y2 = box
    w, h, b = text_size(draw, text, fnt)
    draw.text(((x1+x2-w)/2, (y1+y2-h)/2 - b[1]), text, font=fnt, fill=fill)


def _cubic(p0, p1, p2, p3, steps=8):
    points = []
    for i in range(1, steps+1):
        t = i/steps
        u = 1.0-t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        points.append((x, y))
    return points


def _latex_arrow_local(length_px, m: Metrics):
    """One filled shaft + curved PGF Latex-like tip polygon in local +x coordinates."""
    shaft = m.pt(0.70)
    head_len = m.mm(2.2)
    head_half = m.mm(1.6)/2.0
    half = shaft/2.0
    hs = length_px-head_len
    points = [(0, -half), (hs, -half), (hs, -head_half)]
    points += _cubic(
        (hs, -head_half),
        (hs+0.337381*head_len, -0.519480*head_half),
        (hs+0.877192*head_len, -0.077922*head_half),
        (length_px, 0),
    )
    points += _cubic(
        (length_px, 0),
        (hs+0.877192*head_len, 0.077922*head_half),
        (hs+0.337381*head_len, 0.519480*head_half),
        (hs, head_half),
    )
    points += [(hs, half), (0, half)]
    return points


def draw_flow_arrow(draw, x1, y, x2, m: Metrics):
    """Canonical straight mqtt-flow: one geometry, exact border endpoints."""
    local = _latex_arrow_local(x2-x1, m)
    draw.polygon([(x1+lx, y+ly) for lx, ly in local], fill=MUTED_76)


def draw_flow_arrow_vertical(draw, x, y1, y2, m: Metrics):
    """Canonical downward mqtt-flow: one geometry, exact border endpoints."""
    local = _latex_arrow_local(y2-y1, m)
    draw.polygon([(x+ly, y1+lx) for lx, ly in local], fill=MUTED_76)


def application_node(draw, x, y, w, h, text, m: Metrics):
    # mqtt application from snodec-canonical-figure-system.tex.
    rounded(draw, (x, y, x+w, y+h), GREEN_SOFT, GREEN_78,
            m.pt(0.70), m.pt(2.5))
    draw_centered_text(draw, (x, y, x+w, y+h), text, m.body_font, INK)


def semantic_group_desktop(draw, x, y, w, m: Metrics):
    pad = m.mm(4.5)
    row_gap = m.mm(6)
    node_w = m.mm(25)
    node_h = m.mm(10)
    node_gap = m.mm(8)
    label_w = m.mm(31)
    group_h = pad*2 + node_h*2 + row_gap
    rounded(draw, (x, y, x+w, y+group_h), WHITE, RULE_82,
            m.pt(0.58), m.pt(3.0))

    rows = [
        ('Startup order', ['Broker', 'Subscriber', 'Publisher']),
        ('MQTT delivery', ['Publisher', 'Broker', 'Subscriber']),
    ]
    for r, (label, roles) in enumerate(rows):
        yy = y + pad + r*(node_h+row_gap)
        _, th, bb = text_size(draw, label, m.section_font)
        draw.text((x+pad, yy + (node_h-th)/2 - bb[1]), label,
                  font=m.section_font, fill=BLUE)
        nodes_x = x + pad + label_w
        for i, role in enumerate(roles):
            nx = nodes_x + i*(node_w+node_gap)
            application_node(draw, nx, yy, node_w, node_h, role, m)
            if i < len(roles)-1:
                draw_flow_arrow(draw, nx+node_w, yy+node_h/2,
                                nx+node_w+node_gap, m)
    return group_h


def semantic_group_mobile(draw, x, y, w, m: Metrics):
    # Independent mobile composition: two vertical sequences in parallel columns.
    # This preserves canonical 25 mm nodes and the 8 mm safe margin without
    # shrinking or letting the group border intersect the nodes.
    pad = m.mm(4.5)
    node_w = m.mm(25)
    node_h = m.mm(10)
    node_gap = m.mm(8)
    label_gap = m.mm(3)
    column_gap = m.mm(8)
    sequence_h = node_h*3 + node_gap*2
    label_h = m.pt(10) + m.mm(1)
    group_h = pad*2 + label_h + label_gap + sequence_h
    rounded(draw, (x, y, x+w, y+group_h), WHITE, RULE_82,
            m.pt(0.58), m.pt(3.0))

    columns = [
        ('Startup order', ['Broker', 'Subscriber', 'Publisher']),
        ('MQTT delivery', ['Publisher', 'Broker', 'Subscriber']),
    ]
    total_w = node_w*2 + column_gap
    first_x = x + (w-total_w)/2
    for c, (label, roles) in enumerate(columns):
        cx = first_x + c*(node_w+column_gap)
        label_w, _, _ = text_size(draw, label, m.section_font)
        draw.text((cx + (node_w-label_w)/2, y+pad), label,
                  font=m.section_font, fill=BLUE)
        yy = y+pad+label_h+label_gap
        for i, role in enumerate(roles):
            ny = yy + i*(node_h+node_gap)
            application_node(draw, cx, ny, node_w, node_h, role, m)
            if i < len(roles)-1:
                draw_flow_arrow_vertical(draw, cx+node_w/2, ny+node_h,
                                         ny+node_h+node_gap, m)
    return group_h


def runtime_evidence_card(canvas, x, y, w, title, number, source, crop, m: Metrics):
    """A card using the canonical mqtt-evidence-runtime semantic style."""
    d = ImageDraw.Draw(canvas)
    border = m.pt(0.60)
    radius = m.pt(2.5)
    pad_x = m.pt(4)
    pad_y = m.pt(2)
    title_font = m.annotation_bold_font
    title_text = f'{number} · {title}'
    _, title_h, title_bbox = text_size(d, title_text, title_font)
    header_h = title_h + 2*pad_y
    screenshot_w = w - 2*pad_x
    shot = crop_scale(source, crop, screenshot_w)
    card_h = header_h + pad_y + shot.height + pad_y

    rounded(d, (x, y, x+w, y+card_h), GREEN_SOFT, GREEN_78,
            border, radius)
    d.text((x+pad_x, y+pad_y-title_bbox[1]), title_text,
           font=title_font, fill=GREEN_78)
    canvas.paste(shot, (x+pad_x, y+header_h+pad_y))
    return card_h


def runtime_evidence_card_snippets(canvas, x, y, w, title, number, source, crops, m: Metrics):
    """Mobile runtime evidence using only crops of the original captured pixels."""
    d = ImageDraw.Draw(canvas)
    border = m.pt(0.60)
    radius = m.pt(2.5)
    pad_x = m.pt(4)
    pad_y = m.pt(2)
    snippet_gap = m.mm(1.5)
    title_font = m.annotation_bold_font
    title_text = f'{number} · {title}'
    _, title_h, title_bbox = text_size(d, title_text, title_font)
    header_h = title_h + 2*pad_y
    screenshot_w = w - 2*pad_x
    shots = [crop_scale(source, crop, screenshot_w) for crop in crops]
    screenshots_h = sum(s.height for s in shots) + snippet_gap*(len(shots)-1)
    card_h = header_h + pad_y + screenshots_h + pad_y
    rounded(d, (x, y, x+w, y+card_h), GREEN_SOFT, GREEN_78,
            border, radius)
    d.text((x+pad_x, y+pad_y-title_bbox[1]), title_text,
           font=title_font, fill=GREEN_78)
    sy = y+header_h+pad_y
    for shot in shots:
        canvas.paste(shot, (x+pad_x, sy))
        sy += shot.height+snippet_gap
    return card_h


def draw_mixed_line(draw, x, y, segments):
    cursor = x
    for text, fnt, color in segments:
        draw.text((cursor, y), text, font=fnt, fill=color)
        b = draw.textbbox((cursor, y), text, font=fnt)
        cursor = b[2]
    return cursor


def success_note(draw, x, y, w, m: Metrics, mobile=False):
    # mqtt success: body typography, green-soft/green!78, canonical node geometry.
    pad_x = m.mm(3)
    pad_y = m.mm(2.5)
    radius = m.pt(2.5)
    border = m.pt(0.70)
    body = m.body_font
    code = m.code_small_font
    gap = m.mm(1.5)

    line1 = 'Observed delivery · QoS 1 · Retain false · Dup false'
    topic = 'edge-lab/room-01/temperature'
    payload = '{"value":21.7,"unit":"C"}'
    h1 = text_size(draw, line1, body)[1]
    h2 = text_size(draw, topic, code)[1]

    if not mobile:
        segments2 = [(topic, code, INK), (' · ', body, INK), (payload, code, INK)]
        h = max(m.mm(10), h1+h2+gap+2*pad_y)
        rounded(draw, (x, y, x+w, y+h), GREEN_SOFT, GREEN_78, border, radius)
        yy = y+pad_y
        draw.text((x+pad_x, yy), line1, font=body, fill=INK)
        yy += h1+gap
        draw_mixed_line(draw, x+pad_x, yy, segments2)
        return h

    mobile_line1 = 'Observed delivery · QoS 1'
    mobile_line2 = 'Retain false · Dup false'
    mh1 = text_size(draw, mobile_line1, body)[1]
    mh2 = text_size(draw, mobile_line2, body)[1]
    h3 = text_size(draw, payload, code)[1]
    h = max(m.mm(10), mh1+mh2+h2+h3+3*gap+2*pad_y)
    rounded(draw, (x, y, x+w, y+h), GREEN_SOFT, GREEN_78, border, radius)
    yy = y+pad_y
    draw.text((x+pad_x, yy), mobile_line1, font=body, fill=INK); yy += mh1+gap
    draw.text((x+pad_x, yy), mobile_line2, font=body, fill=INK); yy += mh2+gap
    draw.text((x+pad_x, yy), topic, font=code, fill=INK); yy += h2+gap
    draw.text((x+pad_x, yy), payload, font=code, fill=INK)
    return h


def make_desktop():
    W = 1536
    m = Metrics(W, 160.0, mobile=False)
    safe = m.mm(8)
    left = safe
    right = left
    content_w = W-left-right

    broker_crop = (0, 0, 1588, 150)
    subscriber_crop = (0, 0, 1588, 575)
    publisher_crop = (0, 0, 1588, 430)
    gap = m.mm(6)

    temp = Image.new('RGB', (W, 4000), WHITE)
    td = ImageDraw.Draw(temp)
    title_y = m.mm(3)
    title_h = text_size(td, 'First successful end-to-end MQTT publication', m.title_font)[1]
    subtitle_y = title_y + title_h + m.mm(1.5)
    subtitle_h = text_size(td, 'Real runtime evidence · startup and MQTT delivery shown separately', m.annotation_font)[1]
    group_y = subtitle_y + subtitle_h + m.mm(4)
    group_h = semantic_group_desktop(td, left, group_y, content_w, m)
    y = group_y + group_h + gap

    for title, number, source, crop in [
        ('MQTTBroker — listener ready', 1, BROKER, broker_crop),
        ('MQTTCli subscriber — subscribed, then received', 2, SUBSCRIBER, subscriber_crop),
        ('MQTTCli publisher — one PUBLISH', 3, PUBLISHER, publisher_crop),
    ]:
        h = runtime_evidence_card(temp, left, y, content_w, title, number, source, crop, m)
        y += h+gap
    note_h = success_note(td, left, y, content_w, m, mobile=False)
    H = y+note_h+safe

    im = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(im)
    d.text((left, title_y), 'First successful end-to-end MQTT publication', font=m.title_font, fill=INK)
    d.text((left, subtitle_y), 'Real runtime evidence · startup and MQTT delivery shown separately', font=m.annotation_font, fill=MUTED)
    semantic_group_desktop(d, left, group_y, content_w, m)
    y = group_y+group_h+gap
    for title, number, source, crop in [
        ('MQTTBroker — listener ready', 1, BROKER, broker_crop),
        ('MQTTCli subscriber — subscribed, then received', 2, SUBSCRIBER, subscriber_crop),
        ('MQTTCli publisher — one PUBLISH', 3, PUBLISHER, publisher_crop),
    ]:
        h = runtime_evidence_card(im, left, y, content_w, title, number, source, crop, m)
        y += h+gap
    success_note(d, left, y, content_w, m, mobile=False)
    return im


def make_mobile():
    W = 887
    m = Metrics(W, 100.0, mobile=True)
    safe = m.mm(8)
    left = safe
    content_w = W-2*left
    gap = m.mm(6)

    temp = Image.new('RGB', (W, 5000), WHITE)
    td = ImageDraw.Draw(temp)
    title_y = m.mm(3)
    title1 = 'First successful'
    title2 = 'end-to-end MQTT publication'
    t1h = text_size(td, title1, m.title_font)[1]
    t2y = title_y+t1h+m.mm(1)
    t2h = text_size(td, title2, m.title_font)[1]
    subtitle_y = t2y+t2h+m.mm(2)
    sub = 'Real runtime evidence'
    subh = text_size(td, sub, m.annotation_font)[1]
    group_y = subtitle_y+subh+m.mm(4)
    group_h = semantic_group_mobile(td, left, group_y, content_w, m)
    y = group_y+group_h+gap
    mobile_evidence = [
        ('MQTTBroker — listener ready', 1, BROKER, [(520, 78, 1320, 145)]),
        ('MQTTCli subscriber — subscribed, then received', 2, SUBSCRIBER,
         [(560, 260, 1320, 360), (560, 385, 1320, 455), (560, 455, 1000, 560)]),
        ('MQTTCli publisher — one PUBLISH', 3, PUBLISHER,
         [(700, 0, 1450, 65), (600, 275, 1260, 325)]),
    ]
    for title, number, source, crops in mobile_evidence:
        h = runtime_evidence_card_snippets(temp, left, y, content_w, title, number, source, crops, m)
        y += h+gap
    note_h = success_note(td, left, y, content_w, m, mobile=True)
    H = y+note_h+safe

    im = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(im)
    d.text((left, title_y), title1, font=m.title_font, fill=INK)
    d.text((left, t2y), title2, font=m.title_font, fill=INK)
    d.text((left, subtitle_y), sub, font=m.annotation_font, fill=MUTED)
    semantic_group_mobile(d, left, group_y, content_w, m)
    y = group_y+group_h+gap
    for title, number, source, crops in mobile_evidence:
        h = runtime_evidence_card_snippets(im, left, y, content_w, title, number, source, crops, m)
        y += h+gap
    success_note(d, left, y, content_w, m, mobile=True)
    return im


def save_png(image, path):
    # Preserve the exact canonical palette and the captured terminal pixels.
    # Palette quantization would alter both and is therefore intentionally avoided.
    image.save(path, optimize=True)


if __name__ == '__main__':
    save_png(make_desktop(), OUT_DESKTOP)
    save_png(make_mobile(), OUT_MOBILE)
    print(OUT_DESKTOP)
    print(OUT_MOBILE)
