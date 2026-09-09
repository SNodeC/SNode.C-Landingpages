# SNode.C visual system — canonical TikZ redesign

**Status:** IMPLEMENTED AND REVIEWED  
**Landing-pages baseline:** `bdb3a35ae8b67e730281b050951eca9e27a9df3e` plus this change  
**Reviewed SNode.C source:** `SNodeC/snode.c` `master` at `1f0f728fc9b3b45174f2cd790d83b2f493e58af1`  
**Review date:** 2026-09-09

This artifact supersedes the earlier three-visual/Figma-era SNode.C inventory for the current landing-page implementation. Existing SVGs were treated as historical evidence, not design authority. Current source and adjacent documentation control semantics; `shared/assets/src/tikz/landingpages-figure-system.tex` controls presentation.

## Non-negotiable figure rules

1. Every SNode.C technical figure loads only `landingpages-figure-system.tex`.
2. Figure sources may compose canonical styles but may not define figure-local visual styles, colors, radii, line widths, fonts, arrowheads, shadows, or connector grammar.
3. All layout is relative. Absolute `at (x,y)` placement and absolute canvas coordinates are forbidden.
4. Directional connectors use canonical connector styles and attach to box borders. Off-axis routing is orthogonal unless a specific semantic reason requires otherwise.
5. Ownership/containment uses association/containment semantics, not flow arrows.
6. Green/success styling is reserved for actual successful states/outcomes.
7. Desktop and mobile variants are independently composed but semantically equivalent.
8. Desktop width budget: 160 mm. Mobile width budget: 100 mm. Oversized figures are recomposed, not scaled down by shrinking type.
9. Generated SVGs are derived publication output. CI regenerates and publishes them; TikZ source plus the shared system file remain authoritative.
10. Genuine runtime/UI evidence remains genuine raster capture and is never reconstructed in TikZ.

## Implemented inventory

| ID | Figure | Primary placement | Reader question | Final width desktop / mobile |
| --- | --- | --- | --- | --- |
| S1 | `programming-model` | README programming model | Which objects participate in one connection and who creates the context? | 137.9 / 89.9 mm |
| S2 | `event-loop-dispatch` | Architecture §1 | What does event-driven mean at runtime? | 139.6 / 88.4 mm |
| S3 | `endpoint-composition` | Architecture introduction | Which choices compose one endpoint without implying an arbitrary cross-product? | 125.8 / 93.1 mm |
| S4 | `protocol-relationships` | Architecture §6 | How do custom contexts, HTTP, Express, SSE, WebSocket, and MQTT actually relate? | 131.6 / 95.9 mm |
| S5 | `http-websocket-context-switch` | README + Architecture §5 | How can HTTP become WebSocket without replacing the connection? | 154.7 / 93.0 mm |
| S6 | `configuration-hierarchy` | Configuration opening | Where do named endpoints, application configuration, sections, and anonymous instances live? | 129.6 / 85.8 mm |
| S7 | `configuration-resolution` | Configuration surfaces/precedence | How do API, file, and CLI values resolve and how is effective state inspected? | 131.4 / 93.6 mm |
| S8 | `retry-vs-reconnect` | Configuration retry/reconnect | Which failures use retry and which use reconnect? | 159.8 / 97.0 mm |

Each figure has a desktop and `-mobile` TikZ source under `SNode.C/assets/src/tikz/`.

## Semantic contracts

### S1 — Connection-local programming model

- Server and client are separate endpoint flows.
- Each flow retains its own `SocketContextFactory`.
- Listen/accept or connect completion produces a distinct `SocketConnection`.
- The connection calls the retained factory with `create(this)`.
- The returned `SocketContext` becomes the one active context for that connection.
- The event-loop rail represents caller-thread dispatch; no worker pool is implied.

### S2 — Event-loop dispatch

- One multiplexer backend (`epoll`, `poll`, or `select`) is selected at configure time.
- `SNodeC::start()` runs the loop on the caller thread.
- Descriptor readiness and timer activity feed event-queue dispatch.
- The loop repeats while running.
- No performance, fairness, or real-time guarantee is encoded.

### S3 — Typed endpoint composition

- One endpoint chooses a compatible address family, endpoint role, connection mode, and protocol/application context.
- The endpoint uses the shared event runtime.
- RFCOMM/L2CAP are visibly source-verified rather than runtime-qualified here.
- The figure explicitly rejects a universal cross-product interpretation.

### S4 — Higher-protocol relationships

- Custom byte-protocol contexts can attach directly to a stream.
- Direct MQTT 3.1.1 can attach directly to a stream.
- Express-style routing/middleware is above HTTP.
- SSE/EventSource stays within HTTP.
- WebSocket is reached through HTTP Upgrade/context replacement.
- MQTT can compose as a WebSocket subprotocol.
- The figure is a relationship map, not a flat protocol stack.

### S5 — HTTP → WebSocket context replacement

- The same established `SocketConnection` persists.
- HTTP remains active while the WebSocket replacement is staged.
- The current HTTP read callback returns before replacement becomes active.
- Old context detaches with `ContextSwitch`; staged context is selected and attaches.
- No two active contexts or second transport connection are implied.

### S6 — Configuration ownership hierarchy

- `ConfigRoot` owns named application and endpoint branches.
- A named endpoint assembles applicable local/remote/connection/socket/TLS sections.
- Exact section availability depends on concrete role/family/mode.
- Anonymous endpoint instances sit outside the named root tree: API-configurable but not instance-addressable through CLI/config file.

### S7 — Configuration resolution and inspection

- Precedence is API/default < configuration file < CLI.
- Resolution produces effective configuration.
- `--show-config` and `--command-line=...` inspect effective values.
- `--write-config` persists configuration values; it is not arbitrary runtime-state serialization.
- `--help=expanded` inspects hierarchy and is kept conceptually separate.

### S8 — Retry versus reconnect

- Retry handles failed listen/connect establishment.
- Reconnect is client-only policy after a connection was established and later interrupted.
- Reconnect starts a new connect cycle.
- If that new connect cycle fails to establish, ordinary retry policy can apply.

## Final source/style audit

The 16 final sources were checked for:

- no absolute `at (...)` placement;
- no numeric absolute coordinate pairs;
- no `xshift` / `yshift` placement;
- no figure-local `\tikzset`;
- no figure-local visual overrides (`draw`, `fill`, line width, radii, font, text color, opacity, shadows, or arrowhead definitions);
- canonical node/container/connector styles for every constructed element;
- relative positioning through `positioning`, `fit`, anchors, canonical spacing tokens, and relative `calc`/midpoint coordinates;
- successful LaTeX compilation;
- desktop/mobile width-budget compliance;
- visual inspection at GitHub-like desktop/mobile render widths.

## Deliberately rejected figure candidates

No additional figure is created for the capability matrix, build/install pipeline, dependency graph, TLS configuration, queue/backpressure policy, a duplicate factory/context diagram, a separate SSE lifecycle, a separate MQTT architecture, ecosystem project relations, release/version state, or CMake component graph. Those topics are better represented as text/tables or would risk implying unsupported cross-product/runtime relationships.
