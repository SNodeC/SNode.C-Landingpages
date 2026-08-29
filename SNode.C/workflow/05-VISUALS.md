# SNode.C Step 5a — visual design

**Workflow stage:** Step 5a only  
**Design date:** 29 August 2026  
**Project:** SNode.C  
**Output:** `SNode.C/workflow/05-VISUALS.md`  
**Technical baseline inherited from Step 3:** public `SNodeC/snode.c` `master` at `bf01683a53b48220a840522e8ccaf3b48e58c240`  
**Freshness check for Step 5a:** public `master` still resolves to `bf01683a53b48220a840522e8ccaf3b48e58c240`; no Step 3 refresh is required before this visual-design handoff.

This document is the visual-design handoff for Codex Step 5b. It defines what the SNode.C README visuals must communicate and how they should be composed. It does **not** validate source relationships itself, create final SVG/PNG assets, recapture terminal evidence, or modify the README.

The design follows the canonical workflow and governance, the SNode.C Step 3 fact base, the approved Step 4 README design, the scoped SNode.C instructions, and the shared page-system principles. The old mandatory V1–V4 system is not reused.

## Visual strategy

SNode.C is a framework README. Its visuals should explain mechanisms or show genuine evidence; they should not decorate the page.

The approved inventory is three candidate in-page visuals:

1. **Programming-model lifecycle** — required principal technical figure.
2. **Echo connection evidence** — conditional real terminal capture; retain only if the recapture is legible and adds credibility beyond the adjacent expected-output block.
3. **HTTP → WebSocket context replacement** — required mechanism figure showing application-context replacement while retaining the same `SocketConnection`.

The README may therefore ship with **two or three** in-page visuals. The design target remains three candidates, but Visual 2 must be omitted rather than published if a real recapture cannot meet the legibility and evidence requirements below.

No separate decorative hero asset is proposed. No generic stacked architecture figure is proposed. No capability matrix is converted into an image; the capability/evidence summary remains accessible Markdown.

## Shared visual language for SNode.C

### Art direction

- Technical, calm, modern, and precise.
- Use generous whitespace and a clear left-to-right or top-to-bottom reading order.
- Use a restrained **foundation-blue** accent only for emphasis; neutral text, borders, and containers carry most of the information.
- Color must never be the only carrier of meaning. Labels, shape, placement, line style, and captions must remain sufficient in monochrome.
- Use ordinary system sans-serif typography for labels and a system monospace stack only for API names, enum values, commands, or terminal text.
- Avoid gradients, shadows, pseudo-3D cards, decorative network icons, stock imagery, protocol logos, or badge-like clutter inside figures.
- Prefer one explicit neutral canvas/background that remains readable in both GitHub themes. Create separate light/dark exports only if a single neutral asset fails contrast testing.

### Diagram semantics

The shared page-system arrow grammar remains in force:

- **solid directed arrow:** a verified runtime action, dispatch, creation call, or lifecycle transition;
- **thin undirected connector / containment:** ownership, association, or persistent identity, not runtime communication;
- **dashed arrow:** reserved for package/build dependencies; none are currently needed in the two proposed SNode.C technical figures.

Every technical relationship specified below remains **PENDING CODEX VALIDATION** until Step 5b checks it against current source and tests.

### Accessibility and fallback

- Every meaningful figure needs concise information-bearing alt text.
- The surrounding README prose must restate the important mechanism; no figure may be the only explanation.
- Terminal evidence must be accompanied by a textual expected-output excerpt because screenshot text cannot remain equally legible on narrow mobile displays.
- Do not encode state solely through color.
- Ensure text and line contrast works in GitHub light and dark modes.
- Keep critical labels large enough that the figure is understandable at normal GitHub content width without opening the asset.

### Asset-source convention for Step 5 implementation

Final exported assets, if approved, should live under:

```text
SNode.C/assets/<asset-name>.svg|png
```

Editable source, composition scripts, raw qualified captures, and capture notes should live under:

```text
SNode.C/assets/src/
```

For vector figures, keep an unminified editable source under `assets/src/` and export an optimized SVG to `assets/`. For the terminal visual, preserve the raw qualified server/client captures plus a deterministic composition script or documented composition recipe under `assets/src/`.

---

# Visual 1 — Programming-model lifecycle

**Status:** DESIGN COMPLETE — **PENDING CODEX VALIDATION**  
**Role:** principal technical figure; required  
**Proposed export:** `SNode.C/assets/programming-model.svg`  
**Editable source requirement:** unminified vector source under `SNode.C/assets/src/programming-model.*`

## Single communication goal

Make the recurring SNode.C application model understandable at a glance:

> a configured server or client endpoint establishes a `SocketConnection`; the endpoint's `SocketContextFactory` creates the per-connection `SocketContext`; the event loop drives lifecycle and I/O into the connection/context path.

## Five-second reader takeaway

A reader should be able to point at the figure and say:

> “Server or client endpoint → connection → factory-created per-connection context, all driven by the event loop.”

The figure must make clear that application/protocol behavior is attached **per connection**, rather than placing application behavior inside the endpoint object itself.

## Exact concepts to show

Show these named public concepts and no broader class inventory:

- `SocketServer` / `SocketClient` — two endpoint roles that converge on the same recurring model;
- `SocketConnection` — the established connection object;
- `SocketContextFactory` — the creation boundary associated with the endpoint flow;
- `SocketContext` — the per-connection application/protocol behavior;
- Event loop — shared runtime that drives descriptor/timer/lifecycle work.

### Technical relationships

Each relationship below is **PENDING CODEX VALIDATION**:

1. `SocketServer` accepts or `SocketClient` initiates an established stream path that results in a `SocketConnection`. — **PENDING CODEX VALIDATION**
2. The configured endpoint flow owns/uses a `SocketContextFactory`. — **PENDING CODEX VALIDATION**
3. The factory creates the connection-local `SocketContext` for a newly established connection. — **PENDING CODEX VALIDATION**
4. One `SocketConnection` has one active `SocketContext` at a time. — **PENDING CODEX VALIDATION**
5. The event loop drives descriptor/timer/lifecycle processing that ultimately dispatches into the connection/context behavior. — **PENDING CODEX VALIDATION**
6. Framework callbacks are dispatched synchronously on the thread calling `start()` or `tick()`; the figure must not imply worker-thread dispatch. — **PENDING CODEX VALIDATION**

## Composition

Use one wide, shallow lifecycle figure rather than a class diagram.

Recommended geometry:

```text
        ┌──────────────────┐
        │   SocketServer   │──┐
        └──────────────────┘  │
                              ├── establish ──► ┌──────────────────┐
        ┌──────────────────┐  │                 │ SocketConnection │
        │   SocketClient   │──┘                 └────────┬─────────┘
        └──────────────────┘                             │
                                                        │ connection-local
        ┌──────────────────────┐                        ▼
        │ SocketContextFactory │ ── create() ──► ┌──────────────────┐
        └──────────────────────┘                  │  SocketContext   │
                                                  └──────────────────┘

        ───────────────────── Event loop / start() / tick() ────────────────────
                    descriptor + timer + lifecycle dispatch
```

This ASCII sketch is conceptual only; the final vector should be more compact and visually balanced.

### Hierarchy

1. **Primary emphasis:** `SocketConnection` + `SocketContext` relationship.
2. **Secondary emphasis:** `SocketServer` / `SocketClient` converge on the same connection model.
3. **Secondary emphasis:** `SocketContextFactory` is the creation boundary, not the application behavior itself.
4. **Supporting rail:** event loop underpins the model without becoming the dominant object.

The `SocketConnection` and `SocketContext` cards should be visually paired but remain separate shapes. `SocketServer` and `SocketClient` should have equal visual weight and merge into one lifecycle rather than become two duplicated diagrams.

## Labels and terminology

Use exactly:

- `SocketServer`
- `SocketClient`
- `SocketConnection`
- `SocketContextFactory`
- `SocketContext`
- `Event loop`
- `accept / connect` or a similarly concise validated label for endpoint-to-connection runtime action
- `create()` on the factory-to-context runtime arrow if Step 5b confirms that this is the clearest public API wording
- `per connection` as a small descriptive label near `SocketContext`
- `start() / tick()` only in the event-loop rail or caption, not as a large API callout

Do not add implementation namespaces unless required to disambiguate public classes.

## Arrow and lifecycle semantics

- Endpoint → connection: solid runtime arrow, labeled with the validated accept/connect concept. — **PENDING CODEX VALIDATION**
- Factory → context: solid runtime arrow, labeled `create()` if validated. — **PENDING CODEX VALIDATION**
- Endpoint ↔ factory association: use containment or an undirected association, not a directed runtime arrow, unless Step 5b finds a more accurate representation. — **PENDING CODEX VALIDATION**
- Event-loop relationship: use a restrained runtime/dispatch rail or two short solid arrows into the connection/context path; do not depict a separate worker pool. — **PENDING CODEX VALIDATION**
- Connection ↔ context association: use a persistent association/containment cue rather than suggesting that every event recreates the context. — **PENDING CODEX VALIDATION**

## Deliberate omissions

Do **not** show:

- IPv4, IPv6, Unix domain, RFCOMM, L2CAP, TLS, HTTP, MQTT, or any family/protocol list;
- template type stacks or concrete `legacy`/TLS endpoint aliases;
- CMake component names;
- configuration-file or CLI hierarchy;
- callback inventories;
- `epoll` / `poll` / `select` comparisons;
- threads, worker pools, queues, or performance claims;
- Node.js or Express references;
- context replacement details — Visual 3 owns that mechanism.

The figure must explain the programming model, not prove breadth.

## Relationship to surrounding README prose/code

Place immediately in the **Programming model** section, directly after the one-paragraph explanation and before or beside the small real `SocketContext` code excerpt.

The surrounding prose should define the five concepts in words. The code excerpt should then demonstrate the *feel* of context callbacks. The figure must not duplicate the code or become an API reference.

## Evidence requirements for Step 5b

Codex must validate the relationship against the Step 3 source baseline, especially:

- public `SocketServer` and `SocketClient` roles;
- where the factory is owned/referenced;
- exact `SocketContextFactory::create(...)` signature and when it is called;
- `SocketConnection` ownership of the active context;
- event-loop dispatch path into connection/context behavior;
- `start()` / `tick()` thread semantics;
- whether the proposed `accept / connect` label is precise enough for both endpoint roles.

No runtime screenshot is required for Visual 1; source and tests are the evidence basis.

## Accessibility / alt-text target

Proposed alt-text intent:

> Diagram of the SNode.C programming model: SocketServer or SocketClient establishes a SocketConnection, a SocketContextFactory creates the per-connection SocketContext, and the event loop drives lifecycle and I/O dispatch.

Step 5b should adjust the wording if technical validation changes the arrows.

## GitHub-width, mobile, and theme requirements

- Prefer a wide SVG with at most five major labeled nodes plus the event-loop rail.
- At desktop GitHub width, every class name should be readable without zoom.
- On mobile, the left-to-right endpoint merge may compress; if necessary, use a responsive-friendly two-row composition where server/client sit above a centered connection/context sequence.
- Avoid tiny explanatory text. Put nuance in the caption/prose instead.
- Use explicit node outlines and labels so the figure remains understandable if the blue accent is visually muted.
- Test one neutral export in both GitHub themes before introducing light/dark variants.

---

# Visual 2 — Genuine echo connection evidence

**Status:** CONDITIONAL DESIGN — **PENDING CODEX VALIDATION AND REAL RECAPTURE**  
**Role:** optional evidence screenshot  
**Proposed export if retained:** `SNode.C/assets/echo-connection-evidence.png`  
**Editable/capture source requirement:** raw qualified captures plus deterministic composition material under `SNode.C/assets/src/echo-capture/`

## Retention decision

Retain this visual **only** if Step 5b can reproduce a real current-baseline server/client run and the resulting capture is sufficiently compact and legible to add credibility beyond the adjacent Markdown expected-output excerpt.

If the real output is visually noisy, too wide, dominated by timestamps/log metadata, or illegible at normal GitHub width, omit the screenshot. Do not redesign, fabricate, or “clean up” terminal lines to rescue it.

## Single communication goal

Show genuine runtime evidence for the first-success path:

> the plain IPv4 echo server reaches a listening state and the client reaches a real connection to it.

The screenshot is **not** payload proof.

## Five-second reader takeaway

A reader should immediately see two real terminal states:

- **Server:** listener is up on loopback.
- **Client:** connection to that listener succeeded.

Nothing in the visual should suggest that the terminal visibly proves an echoed payload.

## Exact concepts to show

- real `echoserver-legacy-in` run from the qualified source revision;
- real `echoclient-legacy-in` run from the same compatible build;
- loopback IPv4 first-success path only;
- only the relevant command line and verified listener/connection evidence lines;
- simple external panel labels such as `Server` and `Client` are allowed as composition labels.

### Technical/evidence relationships

Each statement below is **PENDING CODEX VALIDATION**:

1. The selected server line visibly proves that the listener is active for the approved plain IPv4 loopback run. — **PENDING CODEX VALIDATION**
2. The selected client/server connection line(s) visibly prove transport connection success. — **PENDING CODEX VALIDATION**
3. The echo contexts read available bytes and send the same bytes back in source behavior, but the default information-level capture does not visibly print the reflected payload. — **PENDING CODEX VALIDATION**
4. Context-attach and payload-oriented diagnostic lines are not part of the default information-level evidence unless the approved run explicitly changes logging and Step 5b documents that change. — **PENDING CODEX VALIDATION**

## Composition

Prefer a **vertically stacked two-panel terminal composite** over two narrow side-by-side terminals. This preserves line length and type size better at GitHub width.

Recommended order:

1. **Server** panel — command plus the smallest contiguous region containing the real listening line and relevant connection evidence.
2. **Client** panel — command plus the smallest contiguous region containing the real successful connection line(s).

Use a tight crop. Preserve real terminal text. External labels may identify the panels, but no synthetic terminal output may be inserted.

If the actual output remains readable in a side-by-side composition at final size, Step 5b may recommend that alternative; legibility takes precedence over symmetry.

## Labels and terminology

External composition labels may use:

- `Server`
- `Client`
- optionally `plain IPv4 loopback` in the caption, not necessarily inside the image

Do not label the image `Echo succeeded`, `Payload echoed`, `Round trip`, or similar unless the visible captured output itself actually proves that claim.

## Deliberate omissions

Do **not** include:

- a fabricated payload line;
- trace/debug output solely to make the screenshot look more impressive unless the README's first-success path intentionally uses that exact validated logging configuration;
- TLS, IPv6, or Unix-domain evidence in the same visual;
- certificate commands;
- build logs;
- package installation logs;
- unrelated shell history;
- usernames, home paths, hostnames, LAN addresses, credentials, private certificates, or local repository paths;
- visual callouts claiming performance, security, or platform support.

## Relationship to surrounding README prose/code

Place after the run commands and textual expected-output excerpt in **Run the echo pair / First verified connection**.

The Markdown expected-output block remains the primary accessible proof text. The screenshot supplements it by showing that the captured output came from a real qualified run.

The adjacent prose must explicitly say that the supplied echo code reflects bytes but the current default-visible output proves listener/connection success rather than visibly displaying the echoed payload.

## Evidence and recapture requirements for Step 5b

Codex must provide or record:

- exact SNode.C commit;
- build type and exact two targets used;
- launch commands;
- listening address/port or configuration used;
- logging level/defaults;
- deterministic startup order;
- exact lines selected as listener evidence;
- exact lines selected as connection evidence;
- Ctrl-C teardown behavior;
- confirmation that no private/local identity data appears;
- raw server and client capture files;
- composition/crop procedure.

The capture must be from the same exact master revision used for README command qualification.

## Legibility gate

Visual 2 is retained only if all of these pass:

1. the meaningful terminal lines are readable at normal desktop GitHub content width without opening the image;
2. the crop does not remove context needed to understand what command produced the output;
3. the screenshot remains useful when scaled on mobile, while the adjacent text carries the same essential evidence;
4. timestamps, logging prefixes, and terminal chrome do not dominate the information;
5. no synthetic terminal content is needed to make the story understandable.

If any of these fail, mark the visual **OMIT — TEXTUAL EVIDENCE IS STRONGER** in Step 5b.

## Accessibility / alt-text target

If retained:

> Two terminal captures from the verified plain IPv4 echo pair: the server is listening on loopback and the client establishes a connection. The capture does not show echoed payload text.

## GitHub-width, mobile, and theme requirements

- PNG capture with high-density source and one controlled downsample.
- Keep panel width and line count small enough that terminal text stays readable on desktop.
- Use terminal colors with strong luminance contrast and avoid relying on ANSI color to distinguish state.
- A dark terminal theme is acceptable in both GitHub themes if contrast is strong and the crop has a clear boundary.
- Because mobile downscaling inevitably reduces terminal text, key evidence must be duplicated in Markdown text immediately adjacent to the image.

---

# Visual 3 — HTTP → WebSocket context replacement

**Status:** DESIGN COMPLETE — **PENDING CODEX VALIDATION**  
**Role:** required mechanism/extension-point figure  
**Proposed export:** `SNode.C/assets/http-websocket-context-switch.svg`  
**Editable source requirement:** unminified vector source under `SNode.C/assets/src/http-websocket-context-switch.*`

## Single communication goal

Show why the `SocketConnection` / `SocketContext` split matters:

> during an HTTP-to-WebSocket upgrade, the active application context changes while the established `SocketConnection` remains the same connection object/stream path.

The figure is about **context replacement**, not about advertising a transport matrix.

## Five-second reader takeaway

A reader should see one continuous connection underneath two application states:

> **HTTP context → context switch → WebSocket context, same `SocketConnection`.**

The persistent connection should be the strongest visual continuity cue in the figure.

## Exact concepts to show

- one existing `SocketConnection` spanning the whole figure;
- initial **HTTP application context** attached to that connection;
- an HTTP Upgrade / WebSocket handshake transition marker;
- context replacement through the connection's context-switch mechanism;
- old context detaches with `DetachReason::ContextSwitch`;
- new **WebSocket application context** attaches;
- the underlying connection remains in place through the transition.

### Technical relationships

Each relationship below is **PENDING CODEX VALIDATION**:

1. `SocketConnection::setSocketContext()` can stage/perform replacement of the active context while the connection remains established. — **PENDING CODEX VALIDATION**
2. The old active context detaches with `DetachReason::ContextSwitch`. — **PENDING CODEX VALIDATION**
3. The replacement context attaches to the same `SocketConnection`. — **PENDING CODEX VALIDATION**
4. The HTTP-to-WebSocket upgrade path uses this implemented context-replacement mechanism. — **PENDING CODEX VALIDATION**
5. The WebSocket behavior shown corresponds to WebSocket version 13 where protocol version is named in surrounding copy. — **PENDING CODEX VALIDATION**
6. The figure intentionally does not state or imply which address-family × plain/TLS combinations are qualified. — **PENDING CODEX VALIDATION**

## Composition

Use a three-phase horizontal mechanism figure with a **continuous lower connection rail**.

Recommended geometry:

```text
 BEFORE UPGRADE                 SWITCH                         AFTER UPGRADE

 ┌──────────────────┐      HTTP Upgrade / handshake       ┌──────────────────┐
 │ HTTP application │ ───────────────►                    │ WebSocket        │
 │ context          │      context replacement            │ application      │
 └────────┬─────────┘                                      │ context          │
          │                                                └────────┬─────────┘
          │                                                         │
 ═════════╧══════════════════ same SocketConnection ════════════════╧══════════
              established stream / connection identity retained

        old context: detach(ContextSwitch)   new context: attach
```

The continuous `SocketConnection` rail should visually span all three phases without breaks. The context cards above it should clearly change identity.

Do not draw a second socket/connection on the right side. Do not use a network-family icon or TLS badge anywhere in this figure.

## Hierarchy

1. **Primary emphasis:** one continuous `SocketConnection`.
2. **Primary state change:** HTTP context becomes WebSocket context.
3. **Supporting lifecycle detail:** `ContextSwitch` detach / attach semantics.
4. **Supporting protocol marker:** HTTP Upgrade / WebSocket handshake initiates the transition.

The figure should visually answer “what stays?” and “what changes?” before the reader reads the caption.

A small textual pair such as:

- **stays:** `SocketConnection`
- **changes:** active `SocketContext`

may be used if it improves five-second comprehension without adding clutter.

## Labels and terminology

Use:

- `HTTP application context`
- `WebSocket application context`
- `same SocketConnection`
- `HTTP Upgrade`
- `DetachReason::ContextSwitch`
- `attach`
- optionally `setSocketContext()` if Step 5b confirms it is the correct public mechanism to expose in the figure

If version labels appear at all, use `HTTP/1.0 and HTTP/1.1` only in surrounding capability prose and `WebSocket 13` only where validated and relevant. The mechanism figure itself does not need version numbers.

## Arrow / lifecycle semantics

- HTTP context → transition marker: solid runtime/lifecycle arrow for the validated upgrade path. — **PENDING CODEX VALIDATION**
- Context replacement: solid runtime/lifecycle arrow; label with the validated mechanism rather than a generic `magic upgrade`. — **PENDING CODEX VALIDATION**
- Connection rail: no directional arrow; it represents persistent identity/association across the state change. — **PENDING CODEX VALIDATION**
- Detach/attach: compact lifecycle annotations, not separate giant arrows. — **PENDING CODEX VALIDATION**

## Deliberate omissions

Do **not** show:

- IPv4, IPv6, Unix domain, RFCOMM, L2CAP;
- plain/TLS badges or a TLS lock icon;
- a matrix suggesting HTTP or WebSocket qualification across all families/modes;
- MQTT or MQTT-over-WebSocket;
- Express-style routing/middleware;
- Node.js/Express compatibility language;
- HTTP request headers or complete handshake text;
- socket file descriptors, kernel sockets, internal parser classes, or template types;
- a second connection on the WebSocket side;
- performance, security, stability, or production-readiness claims.

## Relationship to surrounding README prose/code

Place in **Architecture and extension points** after the compact textual layer decomposition and the paragraph explaining that custom factories/contexts are the application extension point.

The prose before the figure should establish that one connection has an active context. The figure then makes the replacement mechanism concrete. The prose after it can point to deeper architecture documentation rather than expanding into a WebSocket tutorial.

This visual should not appear before the main programming-model figure; it depends on the reader already understanding `SocketConnection` and `SocketContext`.

## Evidence requirements for Step 5b

Codex must validate:

- exact implementation path and public API for context replacement;
- whether replacement is staged and when detach/attach occur;
- exact detach reason enum spelling and semantics;
- that the HTTP → WebSocket upgrade path uses this mechanism in current source;
- component/integration tests that exercise the path;
- whether any proposed label could falsely imply an address-family or TLS coverage matrix.

No screenshot is required. This is a mechanism diagram grounded in source/tests.

## Accessibility / alt-text target

Proposed alt-text intent:

> HTTP-to-WebSocket context switch in SNode.C: the HTTP application context detaches, a WebSocket context attaches, and the same SocketConnection remains established throughout the upgrade.

Step 5b should adjust the wording if validation changes the exact lifecycle description.

## GitHub-width, mobile, and theme requirements

- Use a wide but shallow SVG with three clearly labeled phases.
- Make the continuous connection rail thick enough to remain obvious after mobile scaling.
- Keep lifecycle annotations short; move detailed explanation to the caption.
- If three horizontal phases become cramped on mobile, stack the before/after context cards vertically while preserving one visually continuous connection spine.
- Use shape and labels, not color alone, to distinguish HTTP and WebSocket contexts.
- Test one neutral export against both GitHub themes before adding theme-specific variants.

---

# Cross-visual consistency

The two technical SVGs should clearly belong to one visual family:

- same node corner radius and border weight;
- same system typography and monospace treatment for API symbols;
- same foundation-blue accent role;
- same label hierarchy;
- same arrowheads and runtime-arrow style;
- same caption voice;
- similar whitespace density.

They should **not** share a mandatory canvas size. Visual 1 may be moderately wide; Visual 3 should be shallower and mechanism-focused. Visual 2 is real terminal evidence and therefore should retain authentic terminal appearance rather than imitate the SVG card language.

Do not number or publicly label the final assets as V1/V2/V3. Their identity comes from descriptive filenames and captions.

## README visual placement summary

| Candidate | README location | Status after Step 5a | Why it earns space |
| --- | --- | --- | --- |
| Programming-model lifecycle | `Programming model` | Required; **PENDING CODEX VALIDATION** | Explains the framework's defining object/lifecycle model faster than prose alone. |
| Echo connection evidence | `Run the echo pair` / `First verified connection` | Conditional; **PENDING CODEX VALIDATION AND REAL RECAPTURE** | Provides genuine runtime proof only if the real capture stays compact and readable. |
| HTTP → WebSocket context replacement | `Architecture and extension points` | Required; **PENDING CODEX VALIDATION** | Demonstrates the concrete architectural value of separating connection identity from application context. |

## Evidence-boundary guardrails for Step 5b and implementation

The following rules apply across all three visuals:

- implementation presence is not runtime qualification;
- build availability is not runtime qualification;
- runtime qualification is not public package/release availability;
- no visual may imply a universal address-family × connection-mode × protocol support matrix;
- Bluetooth RFCOMM/L2CAP currently have source/build evidence without hardware runtime qualification;
- TLS runtime evidence is currently limited to one mutual-TLS IPv4 echo arrangement;
- the default echo evidence proves listener/connection success, not visible payload reflection;
- protocol versions, where named in surrounding copy, remain HTTP 1.0/1.1, WebSocket 13, and MQTT 3.1.1 at the Step 3 baseline;
- Node.js/Express inspiration must not be rendered as compatibility;
- no platform, performance, security, stability, production-readiness, or current 2.0 release/package claim belongs in these visuals.

## Step 5b handoff checklist

Codex Step 5b should update this file in place and, for each candidate:

1. validate every item marked **PENDING CODEX VALIDATION** against current source/tests;
2. correct technical labels without changing the communication goal unless validation requires it;
3. add exact source/test evidence for each nontrivial relationship;
4. for Visual 2, document the deterministic real recapture procedure and make an explicit **RETAIN** or **OMIT** decision based on the legibility gate;
5. assign final validated asset filenames and editable-source paths;
6. add implementation notes sufficient to create the SVG/PNG assets reproducibly;
7. mark each technical visual `VALIDATED` only after its semantics are source-aligned;
8. leave `Human approval: PENDING` until the rendered assets are visually reviewed.

No Step 5b validation should broaden Step 3 evidence boundaries merely because a relationship is visually convenient.

## Step 5a completion status

- **Final proposed visual count:** three candidates; two required technical figures plus one conditional real terminal evidence screenshot. The final README may use two visuals if the echo recapture fails the legibility/usefulness gate.
- **Visual 1 purpose:** make the endpoint → connection → factory-created per-connection context model, under the event loop, immediately understandable.
- **Visual 2 purpose:** show genuine plain-IPv4 listener/connection evidence without pretending the default output visibly proves payload echo.
- **Visual 3 purpose:** show HTTP → WebSocket application-context replacement while retaining the same `SocketConnection`.
- **Echo screenshot decision:** retained as an **optional candidate pending real recapture**; omission is preferred over an illegible or misleading capture.
- **Major design decisions:** no decorative hero, no generic architecture stack, no visual capability matrix, one consistent restrained technical SVG language, authentic terminal treatment for runtime evidence, and explicit separation between mechanism diagrams and qualification boundaries.
- **Output path:** `SNode.C/workflow/05-VISUALS.md`.
- **Validation performed in Step 5a:** canonical workflow/governance and all five scoped `AGENTS.md` files were read; the SNode.C Step 3 and Step 4 handoffs were followed; shared page-system visual/capture/accessibility principles were applied; public `SNodeC/snode.c` `master` was rechecked and remains at the Step 3 SHA. Technical relationship validation and real screenshot reproduction remain intentionally deferred to Codex Step 5b.
