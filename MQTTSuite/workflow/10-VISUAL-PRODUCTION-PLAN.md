# MQTTSuite final visual production plan

**Established:** 31 August 2026  
**Updated:** 3 September 2026  
**Status:** canonical post-review visual-production scope  
**Supersedes for figure-count/ownership decisions:** the original three-visual-only production scope in `05-VISUALS.md`  
**Preserves:** the Step-5A technical/runtime evidence and capture provenance recorded in `05-VISUALS.md`

## Why this file exists

`05-VISUALS.md` records the original Step-5A validation and its V1/V2/V3 evidence. That historical validation remains useful and must not be rewritten as though it happened after the later README expansion.

Subsequent source-aligned README work introduced deeper application and HTTP/SSE references. Independent reviews then found 29 figure placeholders with several duplicate concepts. The reader-facing documentation has now been consolidated to **24 canonical figure briefs** with explicit ownership. This file is the authoritative MQTTSuite visual-production inventory.

The rule is simple: **produce each canonical brief once at its owning location.** Other documents may link to or reuse that figure, but should not commission a second diagram that answers the same question.

## Current evidence baseline

- Current MQTTSuite source behavior: `SNodeC/mqttsuite@83de1acdf692896787c1e86f5322bd0ae0534f84`.
- Current SNode.C foundation behavior: `SNodeC/snode.c@1f0f728fc9b3b45174f2cd790d83b2f493e58af1`.
- Narrow Integrator wildcard correction: PR #22 / `d15f70a2818d291638c50aa2e2116a9e49ebd9e1`.
- Recorded Step-5A runtime qualification: MQTTSuite `52de563...` against SNode.C `60f26d9...`; see `05-VISUALS.md` and `MQTTSuite/assets/src/` provenance.
- Source-only and runtime-exercised claims must remain visually distinguishable.
- When a brief, README, prior review, schema, and current implementation disagree, current implementation behavior controls the figure claim; schema-only availability must not be drawn as runtime support.

## Canonical source and publication rule

For the current MQTTSuite technical figure family:

- canonical editable technical sources are `MQTTSuite/assets/src/tikz/*.tex` plus `mqttsystem-figure-system.tex`;
- generated technical SVGs under `MQTTSuite/assets/` are publication outputs and must never be hand-edited;
- real terminal/Web-UI evidence remains real raster capture and is not recreated in TikZ;
- desktop/mobile technical variants use independently art-directed TikZ sources when both are published;
- every published technical variant must have a canonical source; no permanent generated-asset exception is allowed;
- the final publication SVG set must be regenerated from the accepted TikZ sources and validated before publication.

The older Figma technical diagrams remain historical provenance only. Figma may still compose/crop/annotate genuine raster evidence; it is not the canonical source for the current MQTTSuite technical-diagram family.

## Canonical inventory — 24 figure briefs

### MQTTSuite root README — 5

1. **Five applications, five responsibilities** — suite identity and application-role chooser. Make MQTTBroker the real connection/topic-space anchor; do not imply an all-five application runtime pipeline.
2. **Broker + CLI first success** — real runtime-qualified terminal proof; distinguish startup order (Broker → Subscriber → Publisher) from MQTT delivery flow (Publisher → Broker → Subscriber); use captured application output, never a reconstructed transcript.
3. **Configuration hierarchy and persistence** — defaults/config files/CLI converge into effective parsed configuration; inspection and `--write-config` are sibling outcomes, not a sequence; writing serializes effective parsed configuration and does not prove runtime success. Keep separate domain documents distinct.
4. **Logical bridge forwarding** — root-level fan-out concept, source exclusion, subscription-selected inputs, and preserved payload/received QoS/retain; prefix construction may point to #14 rather than duplicating it.
5. **Raw envelope and optional projections** — suite-level Store split: raw insert is attempted/queued first, while JSON/topic projection evaluation and writes proceed independently of raw-insert success. Never claim the raw row is always successfully written.

The root ASCII deployment-topology block is intentionally not duplicated as a figure. The root also does not own a second Integrator mapping-pipeline figure.

### MQTTBroker README — 3

6. **Listener families around one broker core** — direct MQTT and HTTP/WebSocket listeners converging on shared broker/session state; preserve per-connection server context where shown.
7. **Dashboard, SSE, API, and MQTT WebSocket relationship** — one shared Broker HTTP listener/router feeding dashboard, API/SSE, and MQTT WebSocket routes. Do not classify the shared ingress/router itself as exclusively admin or data plane; split only where the routed surfaces actually diverge.
8. **Optional embedded mapper** — shared `MqttMapper` running inside MQTTBroker without inventing a child MQTTIntegrator process. Mapped publications re-enter the Broker publish-processing path and may be mapped again; show this re-entry explicitly enough to prevent a one-pass interpretation.

### MQTTIntegrator README — 3

9. **MQTTIntegrator mapping pipeline** — broker subscription → topic-tree match → mapping → immediate/delayed republish. Subscription QoS belongs to subscription setup, not the per-message processing spine. Publish QoS remains mapping-output control.
10. **Topic-tree matching** — literal, `+`, terminal `#`, zero-level `parent/#`, sibling/document-order first-match behavior. Do not imply an inherent literal-before-wildcard precedence; any displayed order is an example/document order. Qualify the zero-level child-`#` fallback correctly.
11. **Static, scalar, JSON, and fan-out mapping** — `static`, `value`, and `json` are independently present mapping-mode keys, not mutually exclusive pipeline stages. A matching configuration may produce **zero, one, or many** mapped outputs; arrays provide fan-out.

The draft/validate/deploy/history/rollback lifecycle figure is not duplicated here; it is owned by the Integrator HTTP reference.

### MQTTBridge README — 4

12. **Bridge definition to runtime clients** — `bridges[]` → logical bridge → broker members → SNode.C outbound MQTT clients. Qualify materialization as one client per enabled, runtime-supported, compiled member; schema admission alone is not runtime support.
13. **Bridge-definition hierarchy** — bridge/member fields, network, MQTT session, subscriptions, prefixes, session store. Use containment/association semantics rather than process-flow arrows for hierarchy.
14. **Prefix and forwarding construction** — build the exact forwarded topic token by token: bridge prefix + source-member prefix + destination-member prefix + original topic; preserve the literal-separator caveat and payload/QoS/retain preservation.
15. **Loop boundaries** — distinguish immediate source exclusion, topology/subscription design, and the private non-standard SNode.C reflection-suppression mechanism. Present the three boundaries as independent safeguards/limits, not a temporal sequence.

The PATCH/close/activate/restart/SSE lifecycle figure is not duplicated here; it is owned by the Bridge HTTP/SSE reference.

### MQTTCli README — 1

16. **MQTTCli command/configuration hierarchy** — one enabled connection instance owns sibling sections including `remote`, optional `http`, `session`, `sub`, and `pub`. Do not nest `sub`/`pub` below `session`; runtime use/order is a different concept from configuration ownership.

### MQTTStore README — 1

17. **JSON/topic projection extraction** — from the receive/store step, branch independently into raw-insert attempt and projection evaluation. Show `topic_level`, `json_pointer`, and `literal` feeding typed SQL columns only when valid JSON/topic matching permits it. Desktop/mobile must retain the actual decision/optional path.

The raw-envelope-first split is not duplicated here; the suite-level version is owned by the root README.

### Shared configuration reference — 2

18. **MQTTSuite configuration hierarchy** — application → named instance → instance-owned typed/application-specific configuration sections. Do not present address/transport/TLS → MQTT session → application action as one universal ownership chain; runtime protocol layering is a separate concept. Tie the configuration tree to CLI/config-file/introspection without conflating those surfaces with runtime layering.
19. **Subscription QoS versus publish QoS** — explicit visual distinction between requested delivery QoS and outgoing PUBLISH QoS; include Integrator `subscription.qos` versus output `qos` and MQTTCli `##<qos>` override semantics. Keep the two decisions visually independent in desktop and mobile.

### Broker HTTP/SSE reference — 1

20. **Broker trust boundary** — model the shared HTTP listener/router exposure accurately: dashboard, JSON admin/API, SSE, and MQTT-over-WebSocket share the Broker HTTP routing surface. The application does not create the drawn trusted network boundary; label it as a **required external / trusted deployment boundary** where such isolation is recommended. Keep current unauthenticated/wildcard-CORS/credential-sensitive warnings precise and do not imply TLS is authorization.

### Integrator HTTP reference — 2

21. **Integrator administration trust boundary** — MQTT data plane includes both subscribed inbound publications and mapped outbound republishing through the MQTT client. Separate it from the Basic-authenticated admin surface with fixed source-known `admin/admin` defaults and secret-bearing mapping state. Label any dashed trusted region as a required external/trusted deployment boundary, not protection supplied by the application.
22. **Mapping administration lifecycle** — active → draft via PATCH/POST → validate/deploy; prior-active history backup occurs before active apply/reload; persistence is attempted and its success is not currently used as the HTTP-success gate; runtime reload chooses subscription delta or reconnect; rollback is a later optional operator action that re-enters the apply/reload path, not a mandatory post-deploy stage.

### Bridge HTTP/SSE reference — 2

23. **Bridge administration trust boundary** — Bridge MQTT clients both receive selected publications and transmit forwarded publications to other broker members. Separate this data plane from the unauthenticated HTTP/HTTPS config + SSE operator surface. Label any trusted region as a required external/trusted deployment boundary, not application-enforced authorization.
24. **Bridge PATCH + SSE lifecycle** — show staged/validated PATCH outcomes including restart-in-progress and patch/validation failure; HTTP success acknowledges the patch before connection settlement. Stopping/disconnecting SSE events align with teardown initiation. Restart may proceed immediately when no flows remain or resume after the final flow-completion callback. Activation performs an active-definition write attempt, rebuilds runtime bridge state, starts clients, then connection events settle. Replay covers events retained since the current `bridges_starting` boundary; `Last-Event-ID` is ignored; keep-alive is 39 s. Desktop/mobile must carry equivalent branches and qualifiers, and both must have canonical TikZ sources.

## Explicit non-owners

`docs/integrator-mapping.md` intentionally owns **no separate figure brief**. It is the detailed grammar/behavior reference and routes readers to the canonical Integrator figures where appropriate.

`docs/bridge-definition.md` and `docs/store-storage.md` are routing/signpost pages and own no independent visual production task.

The complete sibling-topic and three-broker worked examples are primarily copyable configuration references; they do not require decorative duplicate diagrams unless a later usability review demonstrates a specific unresolved reader question.

## Shared visual grammar

The 24 figures should read as one product family rather than 24 unrelated illustrations:

- use the shared TikZ system for typography, spacing, radii, semantic colors, containers, arrow styles, responsive typography, and connector ports;
- application names, MQTT topic tokens, prefixes, QoS, HTTP/SSE routes, and evidence labels use a consistent typography hierarchy;
- the current technical family uses the restrained light TikZ language aligned with SNode.C's publication quality; do not mix it with the superseded dark Figma technical family;
- arrow direction always represents real message/state/configuration flow, never vague association;
- ownership/containment uses association/containment semantics, not directional flow arrows;
- every directional connector is one continuous path with the arrowhead attached to that path; never draw a line and place a separate arrowhead on top of or beside it;
- connectors leave and enter a box border orthogonally at 90 degrees, using the middle of the relevant border by default;
- when several connectors share one border, distribute their source and destination attachment points evenly along that border rather than stacking them at one point;
- off-axis connectors use orthogonal/Manhattan routing; unmotivated diagonal lines or arrows are forbidden, and a diagonal is acceptable only when a specific semantic or geometric reason makes it clearer than orthogonal routing;
- a neutral whole-figure frame is not a semantic lane/plane/group; draw the neutral frame first and never let its fill overpaint semantic containers;
- desktop/mobile variants are independently art-directed but semantically equivalent: branches remain branches, siblings remain siblings, error paths/qualifiers are not silently dropped;
- desktop/mobile composition must stay inside the shared width/legibility budgets; recompose oversized figures instead of shrinking them;
- automatic word hyphenation is forbidden inside diagram labels and technical notes;
- green/success styling is reserved for a real successful outcome, not generic emphasis, destinations, final stages, or actions;
- use labels/shapes in addition to color; meaning must survive grayscale and color-vision differences;
- separate data plane from operator/control plane only where the implementation actually supplies or the figure explicitly labels the deployment distinction;
- mark source-only versus runtime-qualified evidence where the distinction affects interpretation;
- do not turn known limitations into visual badges implying support or security;
- final figures require meaningful alt text and adjacent prose that preserves the essential meaning when images are unavailable.

## Trust-boundary family

The three HTTP trust-boundary figures are intentionally separate because the applications differ materially:

- Broker: no application authentication; permissive API/SSE CORS; credential-sensitive event representation; MQTT WebSocket shares the HTTP listener/router.
- Integrator: Basic Auth exists but uses fixed source-known `admin/admin`; no supported built-in credential replacement path.
- Bridge: no application authentication; full definition read-back and mutation plus SSE.

Produce them from one shared visual template so the differences are immediately comparable. The dashed trusted region is a **deployment requirement/recommendation**, not an application-provided authorization boundary unless source proves otherwise.

## Runtime-capture rule

Any terminal or Web UI figure that claims runtime evidence must use real captured application output from the qualified scenario. Figma may crop, align, frame, annotate outside the captured product pixels, and compose multiple real captures; it must not redraw, retype, or reconstruct application output.

The Step-5A raw capture provenance under `MQTTSuite/assets/src/` remains authoritative for those historical qualified scenarios. If a figure is recaptured against newer source, record the exact new implementation SHAs, commands, environment, capture method, and teardown separately.

## Build, proof, and publication loop

Technical-diagram repair is not complete when the `.tex` compiles. For each accepted change and again for the complete family:

1. verify the claim against current MQTTSuite/SNode.C source where technical behavior is involved;
2. edit the canonical TikZ source and shared system only where required;
3. run the canonical CMake figure build;
4. inspect the actual generated desktop/mobile render at realistic GitHub widths;
5. inspect connector attachment, arrowhead alignment, orthogonal routing, spacing, container layering, typography, hyphenation, clipping, and desktop/mobile semantic equivalence;
6. repair and repeat until the concrete figure passes;
7. after all figures pass individually, rebuild the full family from clean state and repeat a cross-family/contact-sheet review;
8. re-run the accepted defect register and prove every item fixed or explicitly rejected with source/render evidence;
9. only then regenerate/publish the final SVG set and run README-level validation.

Do not declare the figure system complete or publication-ready while any accepted issue remains unproved.

## Production order

1. Repair canonical build/source-of-truth and shared TikZ-system defects.
2. Correct the implementation-sensitive figure briefs and adjacent README claims before drawing against them.
3. Repair root/shared figures that establish suite grammar.
4. Repair application-owned deep figures in Broker → Integrator → Bridge → CLI → Store order, prioritizing technical blockers.
5. Repair the three HTTP trust-boundary figures from one template.
6. Repair the Integrator and Bridge administration lifecycle figures.
7. Validate each desktop/mobile pair through the proof loop above.
8. Validate the whole family, accessibility/alt text, source/runtime evidence labels, canonical ownership, and duplicate ownership.
9. Publish regenerated SVGs only after the clean whole-family gate passes.

## Freeze condition

Figure repair/production may proceed only from reader-facing documentation whose current contracts match the verified implementation. If a final audit changes a reader-facing contract, update this brief and the affected prose before repairing the figure rather than letting a figure preserve superseded behavior.
