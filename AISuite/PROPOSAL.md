# Proposal — AISuite Repository Landing Page

[← Working landing page](README.md) · [Launch roadmap](../README.md) ·
[Shared page system](../PAGE-SYSTEM.md)

This proposal defines AISuite-specific content and visuals within the approved
shared page system. Shared editorial, accessibility, asset, capture, and
visual-placement rules are not duplicated here.

## Current-master scope decision

The public page tracks AISuite `master`/`HEAD`. At the 28 August 2026 evidence
baseline, master is C++-only: it contains no TypeScript package. All TypeScript,
npm, and browser-listener material below is retained as conditional future
planning, not approved current public copy. The current implementation uses
source version `0.7.0`; there is no same-baseline CMake/npm version conflict.
See [`EVIDENCE.md`](EVIDENCE.md).

## Purpose

Present AISuite as a usable integration product rather than an internal
architecture report. The current-master page must explain the value of typed
asynchronous C++ access to the Codex app-server, the role of the stateless
multi-client bridge, exact compatibility, and the quickest path to a successful
request.

## Audience and jobs to be done

### Primary audiences

- C++ developers integrating Codex into applications or tools;
- systems engineers operating one provider connection for multiple clients.

### Secondary audiences

- CodexUI contributors;
- protocol and code-generation reviewers;
- developers evaluating SNode.C for AI transports;
- security reviewers assessing authority and data-flow boundaries.

### Visitor questions

- What does AISuite provide beyond raw JSON-RPC?
- Which code runs on the provider side and which runs in clients?
- Why is the bridge stateless, and where is persistence owned?
- Which Codex app-server schema/revision is supported?
- Can multiple controllers and observers connect safely?
- How do I build, install, and use the C++ API?

## Positioning

### Working headline

> Typed asynchronous Codex integration for C++ clients.

### Supporting statement

> AISuite adapts the Codex app-server protocol into generated typed views,
> asynchronous C++ facades, and a bounded
> multi-client bridge built on SNode.C—without becoming a second persistence or
> semantic authority.

### Primary call to action

**Build the bridge and connect a client**

### Secondary calls to action

- Explore the typed C++ API.
- Understand the multi-client architecture.

## Narrative principles

- Lead with developer value before terms such as authority, facade, projection,
  or telemetry.
- Define what AISuite owns and deliberately does not own.
- Distinguish generated protocol coverage from behavioral compatibility.
- Treat the Codex app-server schema/revision as a pinned compatibility input.
- Explain raw JSON access as an escape hatch, not as a failure of the typed API.
- Make the independent-project relationship to OpenAI explicit.

## Page architecture

### 1. Hero

Include:

- AISuite name, maturity, and exact version;
- headline and concise value statement;
- release, CI, and license badges only;
- one multi-client architecture graphic;
- links to `Quick start`, `C++ API`, and `Compatibility`.

### 2. What AISuite contains

Use a compact component table:

| Component | Purpose | Consumer |
| --- | --- | --- |
| `AISuite::OpenAICodex` | typed backend/frontend SDK and transport adapters | C++ applications |
| `@snodec/codex-frontend` | Future package, absent from current master; omit from current page | browser/Node clients |
| `codex-bridge` | one provider connection exposed to multiple clients | operators and UIs |
| `codex-bridge-client` | interactive reference client | evaluators/developers |
| generated protocol views | lossless typed access over recorded schema inputs | C++ SDK |

### 3. Quick start

Provide one clean current-master path:

1. build/install current SNode.C master and record its tested SHA;
2. configure and build AISuite;
3. run focused tests;
4. start `codex-bridge` with one documented local transport;
5. connect `codex-bridge-client`;
6. submit one harmless request;
7. show expected request, response, and telemetry output.

Use current `master`/`HEAD` for AISuite and SNode.C and record their exact tested
SHAs. If the Codex app-server requires its own authentication/setup, link to
official instructions and state
which data crosses each process boundary.

### 4. Minimal C++ integration

Show a concise, compilable example demonstrating:

- creation/configuration of the relevant client facade;
- one typed operation;
- asynchronous success/error handling;
- lifecycle/ownership expectations;
- CMake consumption with `find_package(AISuite CONFIG REQUIRED)`.

Link to a complete example and tests. Avoid an example that depends on private
internal headers or workspace-relative paths.

### 5. Future TypeScript integration — omit until merged to master

Show package installation or workspace consumption, connection construction,
one typed call, event handling, cleanup, and the required WebSocket subprotocol.
State browser versus Node assumptions and package publication status.

### 6. Architecture and authority

Use an SVG with explicit boundaries:

```text
Native C++ controller / observer clients
             │ typed frontend transport
             ▼
        codex-bridge
             │ provider transport
             ▼
       Codex app-server
```

Annotate:

- app-server owns semantics and persistence;
- bridge owns transport adaptation, routing, controller coordination, and
  bounded telemetry;
- clients own presentation and local interaction state;
- AISuite does not create a second conversation database or semantic cache.

### 7. Multi-client behavior

Explain controller versus observer capabilities, connection lifecycle,
routing, correlation, backpressure/bounds, disconnect/reconnect behavior,
provider loss, and error propagation. Link every significant guarantee to a
test or architecture contract.

### 8. Typed protocol generation

Explain:

- pinned input schema and operation bindings;
- generated C++ views and TypeScript declarations;
- lossless `getRaw()` access;
- raw JSON-RPC submission path;
- source/equality checks between languages;
- regeneration command and review expectations.

Avoid “covers every message” unless the scope and selected schema are stated in
the same sentence.

### 9. Integrated browser listener

Describe static asset and WebSocket serving as an optional bridge deployment
mode. Document routes, subprotocol, security assumptions, bind-address defaults,
TLS/reverse-proxy expectations, and how static delivery can be disabled.

### 10. Compatibility and versioning

Publish a first-class table:

| AISuite | SNode.C | Codex schema/revision | TypeScript package | CodexUI | Status |
| --- | --- | --- | --- | --- | --- |

Current master declares CMake `0.7.0` and has no npm package. Treat future npm
metadata as a separate branch scope until merged and re-audited. Define how
protocol updates affect SemVer and supported branches.

### 11. Security and trust boundaries

State:

- authentication ownership;
- local versus remote listener defaults;
- whether TLS is native or expected at a proxy;
- controller authorization assumptions;
- telemetry contents and bounds;
- static file root handling;
- sensitive logging guidance;
- vulnerability reporting path.

### 12. Ecosystem, support, and contribution

Explain SNode.C as the networking foundation and CodexUI as the primary visual
consumer. Link internal drafts while developing and production pages only when
publishing. Route protocol questions, bugs, security reports, generated-code
changes, and transport extensions separately.

## Approved final section map

The detailed requirements above consolidate into the shared nine-section
product-page system:

1. `What AISuite enables`;
2. `Quick start`;
3. `What AISuite contains`;
4. `Developer integration`;
5. `Typed and multi-client behavior`;
6. `Architecture and authority`;
7. `Installation, compatibility, and security`;
8. `Quality evidence and ecosystem`;
9. `Documentation and project routes`.

C++ integration and the reference client share one section and a combined
visual footprint. Listener, generation, support, security, contribution, and license requirements
remain concise subsections so the page matches the other products in depth.

## Visual requirements

The shared visual language, dimensions, screenshot hygiene, theme behavior, and
source-asset rules come from the [page system](../PAGE-SYSTEM.md). Diagrams
prioritize process, protocol, and authority boundaries; generic AI imagery is
not permitted.

### Visual inventory and placement

| Slot | Asset | Exact placement | Required content |
| --- | --- | --- | --- |
| V1 — Hero | `assets/aisuite-hero.svg` | Immediately below the hero links and independent-project notice | Native C++ controller, observer, and reference clients converging on `codex-bridge`, then the Codex app-server; typed access and multi-client routing are the visual focus |
| V2 — First success | `assets/bridge-terminal.png` | Directly after the bridge/client quick-start expected output | Three panes for provider connection, `codex-bridge` status/routing, and `codex-bridge-client` request/response; show controller/observer or bounded telemetry only when it clarifies success |
| V3 — Architecture | `assets/authority-boundaries.svg` | After the opening paragraph of `Architecture and authority` | Explicit client, AISuite bridge, and app-server boundaries, labeled with their owned state and responsibilities; show that AISuite is not a second semantic or persistence authority |
| V4 — Product detail | `assets/typed-generation-flow.svg` | Immediately after `Typed protocol generation` | Recorded schema and operation inputs → generation → C++ views → manifest/equality coverage, with raw JSON access as a secondary escape path |
| Social preview | `assets/social-preview.png` | Repository metadata | C++ symbols, bridge topology, approved outcome statement, and protocol-violet accent |

Terminal captures use a neutral synthetic workspace and harmless qualification
request. They must contain no token, authentication value, filesystem identity,
private prompt, provider secret, or unrelated log history. Capture all panes
from the same compatible master commits used by the README.

## Copy and format rules

- Define `Codex app-server` on first use.
- Use `typed view`, `frontend proxy`, `provider`, `controller`, and `observer`
  consistently with architecture documents.
- State the independent open-source relationship to OpenAI near the first Codex
  description and in the footer.
- Use at most three hero badges.
- Keep deep object graphs and exhaustive APIs in documentation.
- All code samples must compile or execute in CI.
- Avoid vague “AI platform” language; describe exact protocol behavior.

## Use of existing documentation

1. Treat the live README and architecture contract as read-only knowledge
   sources during this workflow.
2. Verify candidate API, generation, routing, listener, and authority claims
   against the recorded current-master SHA and tests.
3. Rewrite the landing page independently in this workspace without preserving
   the current README structure or wording.
4. Link stable architecture, API/declaration, operator, SDK, security, and
   compatibility references rather than duplicating them.
5. Do not modify the live local repository during this workflow.

## Evidence checklist

- Master source version and explicit maturity wording.
- Exact SNode.C and Codex schema compatibility.
- C++ generation and manifest/equality tests.
- Routing, callback, framing, and reconnect tests.
- Multi-client/controller/observer behavior tests.
- Backpressure and telemetry bounds.
- Clean install plus downstream CMake consumer.
- Security review of listeners and static file delivery.
- Independent-project wording and license verification.

## Review scenarios

1. A C++ developer finds a compilable typed request example quickly.
2. A web developer understands how to use the frontend proxy package.
3. An operator understands listener exposure and security requirements.
4. A protocol reviewer identifies the exact supported schema/revision.
5. A CodexUI developer finds the supported AISuite combination.

## Implementation sequence

1. Confirm current master source version and maturity wording.
2. Record current SNode.C, schema, and CodexUI compatibility.
3. Qualify the clean C++ quick start.
4. Build multi-client and authority diagrams.
5. Draft hero, component overview, and minimal examples.
6. Publish generation, compatibility, listener, and security sections.
7. Connect architecture and API reference documentation.
8. Add ecosystem, support, security, contribution, and license routes.
9. Run code sample, link, visual, and clean-install automation.
10. Review claims against the recorded current-master SHAs before publication.

## Acceptance criteria

- [ ] A visitor can explain AISuite’s benefit without reading architecture docs.
- [ ] C++ examples are minimal, typed, and automatically tested.
- [ ] Version and maturity wording matches current master and release evidence.
- [ ] Exact SNode.C and Codex schema compatibility is published.
- [ ] Multi-client roles and authority boundaries are unambiguous.
- [ ] Listener and security assumptions are explicit.
- [ ] Generated coverage claims define their schema scope.
- [ ] Support, security, contribution, and licensing are easy to find.
- [ ] Assets pass accessibility and light/dark review.
- [ ] V1–V4 and the social preview match the approved inventory and placement.
- [ ] The final section count and prose weight meet the shared product-page target.
- [ ] All commands work from clean current-master checkouts.

## Open decisions

- Public maturity wording for master source version `0.7.0`.
- Future package publication strategy for `@snodec/codex-frontend` after merge.
- Canonical Codex schema/revision naming in user-facing copy.
- Default supported listener deployment and TLS guidance.
- Controller/observer terminology for first-time users.
- Which request is safe and compelling for the quick-start demonstration.
