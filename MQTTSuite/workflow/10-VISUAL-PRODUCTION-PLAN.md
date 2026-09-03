# MQTTSuite final visual production plan

**Established:** 31 August 2026  
**Status:** canonical post-review visual-production scope  
**Supersedes for figure-count/ownership decisions:** the original three-visual-only production scope in `05-VISUALS.md`  
**Preserves:** the Step-5A technical/runtime evidence and capture provenance recorded in `05-VISUALS.md`

## Why this file exists

`05-VISUALS.md` records the original Step-5A validation and its V1/V2/V3 evidence. That historical validation remains useful and must not be rewritten as though it happened after the later README expansion.

Subsequent source-aligned README work introduced deeper application and HTTP/SSE references. Independent reviews then found 29 figure placeholders with several duplicate concepts. The reader-facing documentation has now been consolidated to **24 canonical figure briefs** with explicit ownership. This file is the authoritative production inventory for the next Figma/capture phase.

The rule is simple: **produce each canonical brief once at its owning location.** Other documents may link to or reuse that figure, but should not commission a second diagram that answers the same question.

## Current evidence baseline

- Current MQTTSuite source behavior: `SNodeC/mqttsuite@6c0ff62c612694a6111ff971c446327938130cf0`.
- Narrow Integrator wildcard correction: PR #22 / `d15f70a2818d291638c50aa2e2116a9e49ebd9e1`.
- Recorded Step-5A runtime qualification: MQTTSuite `52de563...` against SNode.C `60f26d9...`; see `05-VISUALS.md` and `MQTTSuite/assets/src/` provenance.
- Source-only and runtime-exercised claims must remain visually distinguishable.

## Canonical inventory — 24 figure briefs

### MQTTSuite root README — 5

1. **Five applications, five responsibilities** — suite identity and application-role chooser.
2. **Broker + CLI first success** — real runtime-qualified terminal proof; use captured application output, never a reconstructed transcript.
3. **Configuration hierarchy and persistence** — defaults/config files/CLI plus separate domain documents.
4. **Logical bridge forwarding** — root-level fan-out concept, source exclusion, subscription-selected inputs, prefix order.
5. **Raw envelope and optional projections** — suite-level Store split between raw persistence and optional typed projections.

The root ASCII deployment-topology block is intentionally not duplicated as a figure. The root also does not own a second Integrator mapping-pipeline figure.

### MQTTBroker README — 3

6. **Listener families around one broker core** — direct MQTT and HTTP/WebSocket listeners converging on shared broker/session state.
7. **Dashboard, SSE, API, and MQTT WebSocket relationship** — Broker HTTP router product surface.
8. **Optional embedded mapper** — shared `MqttMapper` running inside MQTTBroker without inventing a child MQTTIntegrator process.

### MQTTIntegrator README — 3

9. **MQTTIntegrator mapping pipeline** — canonical mapping-pipeline figure: broker subscription → topic-tree match → mapping → immediate/delayed republish. Label subscription QoS and publish QoS independently.
10. **Topic-tree matching** — literal, `+`, terminal `#`, zero-level `parent/#`, sibling/document-order behavior.
11. **Static, scalar, JSON, and fan-out mapping** — mapping modes and one-to-many outputs.

The draft/validate/deploy/history/rollback lifecycle figure is not duplicated here; it is owned by the Integrator HTTP reference.

### MQTTBridge README — 4

12. **Bridge definition to runtime clients** — `bridges[]` → logical bridge → broker members → SNode.C outbound MQTT clients.
13. **Bridge-definition hierarchy** — bridge/member fields, network, MQTT session, subscriptions, prefixes, session store.
14. **Prefix and forwarding construction** — build the exact forwarded topic token by token.
15. **Loop boundaries** — distinguish immediate source exclusion, topology/subscription design, and the private SNode.C reflection-suppression mechanism.

The PATCH/close/activate/restart/SSE lifecycle figure is not duplicated here; it is owned by the Bridge HTTP/SSE reference.

### MQTTCli README — 1

16. **MQTTCli command hierarchy** — enabled connection instance → remote/HTTP transport → session → subscribe/publish actions.

### MQTTStore README — 1

17. **JSON/topic projection extraction** — show `topic_level`, `json_pointer`, and `literal` feeding typed SQL columns while raw storage remains independent.

The raw-envelope-first split is not duplicated here; the suite-level version is owned by the root README.

### Shared configuration reference — 2

18. **MQTTSuite configuration hierarchy** — application → named instance → address/transport/TLS → MQTT session → application action, tied to CLI/config-file/introspection.
19. **Subscription QoS versus publish QoS** — explicit visual distinction between requested delivery QoS and outgoing PUBLISH QoS; include Integrator `subscription.qos` vs output `qos` and MQTTCli `##<qos>` override semantics.

### Broker HTTP/SSE reference — 1

20. **Broker trust boundary** — MQTT data plane separate from unauthenticated dashboard/admin/SSE operator surface; show current credential-sensitive boundary without implying TLS is authorization.

### Integrator HTTP reference — 2

21. **Integrator administration trust boundary** — MQTT data plane separate from Basic-authenticated admin plane with fixed source-known `admin/admin` defaults and secret-bearing mapping state.
22. **Mapping administration lifecycle** — active → draft via PATCH/POST → validate → deploy/history/rollback → subscription delta or reconnect.

### Bridge HTTP/SSE reference — 2

23. **Bridge administration trust boundary** — outbound MQTT data plane separate from unauthenticated HTTP/HTTPS config + SSE operator plane.
24. **Bridge PATCH + SSE lifecycle** — patch accepted/staged → disconnect/close → activate/persist → restart → SSE state progression.

## Explicit non-owners

`docs/integrator-mapping.md` intentionally owns **no separate figure brief**. It is the detailed grammar/behavior reference and routes readers to the canonical Integrator figures where appropriate.

`docs/bridge-definition.md` and `docs/store-storage.md` are routing/signpost pages and own no independent visual production task.

The complete sibling-topic and three-broker worked examples are primarily copyable configuration references; they do not require decorative duplicate diagrams unless a later usability review demonstrates a specific unresolved reader question.

## Shared visual grammar

The 24 figures should read as one product family rather than 24 unrelated illustrations:

- application names, MQTT topic tokens, prefixes, QoS, HTTP/SSE routes, and evidence labels use a consistent typography hierarchy;
- diagrams use the MQTTSuite visual language established for V1, while application-specific figures may emphasize the owning application;
- arrow direction always represents real message/state/configuration flow, never vague association;
- every directional connector is one continuous path with the arrowhead attached to that path; never draw a line and place a separate arrowhead on top of or beside it;
- connectors leave and enter a box border orthogonally at 90 degrees, using the middle of the relevant border by default;
- when several connectors share one border, distribute their source and destination attachment points evenly along that border rather than stacking them at one point;
- off-axis connectors use orthogonal/Manhattan routing; unmotivated diagonal lines or arrows are forbidden, and a diagonal is acceptable only when a specific semantic or geometric reason makes it clearer than orthogonal routing;
- use labels/shapes in addition to color; meaning must survive grayscale and color-vision differences;
- separate data plane from operator/control plane where relevant;
- mark source-only versus runtime-qualified evidence where the distinction affects interpretation;
- do not turn known limitations into visual badges implying support or security;
- desktop/mobile art direction is required where a desktop figure would become unreadable at GitHub mobile width;
- final figures require meaningful alt text and adjacent prose that preserves the essential meaning when images are unavailable.

## Trust-boundary family

The three HTTP trust-boundary figures are intentionally separate because the applications differ materially:

- Broker: no application authentication; permissive API/SSE CORS; credential-sensitive event representation.
- Integrator: Basic Auth exists but uses fixed source-known `admin/admin`; no supported built-in credential replacement path.
- Bridge: no application authentication; full definition read-back and mutation plus SSE.

Produce them from one shared visual template so the differences are immediately comparable.

## Runtime-capture rule

Any terminal or Web UI figure that claims runtime evidence must use real captured application output from the qualified scenario. Figma may crop, align, frame, annotate outside the captured product pixels, and compose multiple real captures; it must not redraw, retype, or reconstruct application output.

The Step-5A raw capture provenance under `MQTTSuite/assets/src/` remains authoritative for those historical qualified scenarios. If a figure is recaptured against newer source, record the exact new implementation SHAs, commands, environment, capture method, and teardown separately.

## Production order

1. Reuse/refresh V1–V3 evidence assets from the historical Step-5A plan where still semantically applicable.
2. Produce the root/shared figures that establish suite grammar.
3. Produce application-owned deep figures in Broker → Integrator → Bridge → CLI → Store order.
4. Produce the three HTTP trust-boundary figures from one template.
5. Produce the Integrator and Bridge administration lifecycle figures.
6. Validate desktop/mobile rendering, light/dark GitHub presentation, alt text, source/runtime evidence labels, and duplicate ownership.
7. Before publication, verify that every figure appears at its canonical owner and that no placeholder remains unowned or duplicated.

## Freeze condition

Figure production may begin only from the reader-facing documentation state in which the 24 briefs above are present and the text-correctness audit has no publication blocker. If the final audit changes a reader-facing contract, update the affected visual brief before Figma production rather than letting the figure preserve superseded behavior.
