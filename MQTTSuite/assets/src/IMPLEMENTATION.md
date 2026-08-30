# MQTTSuite visual asset implementation notes

Implementation date: 30 August 2026

## Source qualification

- MQTTSuite: `52de5631245c6318bfa5b7cca700f0754014f34d`
- SNode.C: `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`
- Landingpages raw-capture handoff: `2e605a881f4075ebd3c0b0c4fdbf1040f48ba524`
- Four final V2/V3 publication PNGs added on Landingpages `main`: `79a174a562b3421e25451b8c0a4bf9ea81f4ea7d`

## Publication asset set

- `../application-message-flow.svg`
- `../application-message-flow-mobile.svg`
- `../first-success-terminal.png`
- `../first-success-terminal-mobile.png`
- `../broker-web-ui.png`
- `../broker-web-ui-mobile.png`

## V1 — application message flow

Canonical editable source is the Figma file `MQTTSuite Publication Visuals`:

- file: `https://www.figma.com/design/HuY71IdB8iuRB46oUA5RRi`
- desktop frame: `1:2` — 1200 × 800
- mobile frame: `1:3` — 620 × 1240

The desktop and mobile publication SVGs were exported directly from those Figma frames with the Figma Plugin API using `SVG_STRING`, `svgOutlineText: false`, `svgIdAttribute: false`, and `svgSimplifyStroke: true`. No geometry was redrawn or edited after export. The generated `font-family="Inter"` declarations were broadened only to the fallback stack `Inter, Arial, sans-serif` so the repository asset does not depend on an external font resource.

The publication and source/export counterparts are byte-identical:

- `../application-message-flow.svg` = `application-message-flow.svg`
- `../application-message-flow-mobile.svg` = `application-message-flow-mobile.svg`

Safety checks on both repository-ready SVG strings passed:

- no `<script>`;
- no `<foreignObject>`;
- no `<image>`;
- no `@font-face`;
- no external HTTP resource reference;
- no `file://` URI;
- no `/home/...` path;
- no `/Users/...` path.

Both retain the required evidence boundary:

`Source-verified application role model · not an all-app runtime run`

The desktop and mobile compositions remain separately art-directed; mobile is not a scaled desktop figure.

## V2 — first-success terminal proof

Final publication candidates:

- `../first-success-terminal.png`
- `../first-success-terminal-mobile.png`

Raw qualified source/provenance:

- `first-success/README.md`
- `first-success/broker-raw.png`
- `first-success/subscriber-raw.png`
- `first-success/publisher-raw.png`

The scoped runtime proof remains one plain IPv4 loopback MQTTBroker, one MQTTCli subscriber, one MQTTCli publisher, canonical topic/payload, QoS 1, and subscriber evidence containing `QoS: 1`, `Retain: false`, and `Dup: false`. It is not a broader transport/platform/conformance claim.

No trustworthy V2 Figma node IDs were retained; none are invented here.

## V3 — MQTTBroker live dashboard

Final publication candidates:

- `../broker-web-ui.png`
- `../broker-web-ui-mobile.png`

Raw qualified source/provenance:

- `broker-web-ui/README.md`
- `broker-web-ui/dashboard-desktop-raw.png`
- `broker-web-ui/dashboard-620-raw.png`

The mobile raw capture was genuinely rendered at a 620 CSS-pixel viewport and is not a desktop crop. V3 proves only the visible staged MQTTBroker dashboard state and does not establish Integrator, Bridge, Store, or Web-API authentication behavior.

No trustworthy V3 Figma node IDs were retained; none are invented here.

## Responsive and evidence validation

- V1 desktop/mobile: separate Figma compositions.
- V2 desktop/mobile: separate publication compositions from the same qualified runtime scene.
- V3 mobile: based on a genuine 620 CSS-pixel product viewport.
- V1 semantics are carried by labels, roles, and directions rather than color alone.
- V1 owns a self-contained dark surface suitable for GitHub light/dark surroundings.
- V2/V3 raw provenance uses synthetic identities/data and loopback state.
- Step 5A technical semantics and evidence classes are unchanged.
- `MQTTSuite/README.md` is not part of this Step 5B repository closure.

## Human gate

**Human approval: PENDING**

The six-asset Step 5B candidate package is ready for human visual review once this implementation note and the two V1 SVGs are committed. Step 6 remains blocked until explicit approval of the final visual set.
