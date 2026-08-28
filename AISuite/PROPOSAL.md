# Proposal — AISuite Repository Landing Page

[← Working landing page](README.md) · [Launch roadmap](../README.md)

## Purpose

Present AISuite as a usable integration product rather than an internal
architecture report. The page must explain the value of typed asynchronous C++
and TypeScript access to the Codex app-server, the role of the stateless
multi-client bridge, exact compatibility, and the quickest path to a successful
request.

## Audience and jobs to be done

### Primary audiences

- C++ developers integrating Codex into applications or tools;
- TypeScript/browser developers consuming the frontend proxy SDK;
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
- How do I build, install, and use the C++ or TypeScript API?

## Positioning

### Working headline

> Typed asynchronous Codex integration for C++ and TypeScript clients.

### Supporting statement

> AISuite adapts the Codex app-server protocol into generated typed views,
> asynchronous C++ facades, a framework-neutral TypeScript proxy, and a bounded
> multi-client bridge built on SNode.C—without becoming a second persistence or
> semantic authority.

### Primary call to action

**Build the bridge and connect a client**

### Secondary calls to action

- Explore the typed C++ API.
- Use the TypeScript frontend package.
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
- links to `Quick start`, `C++ API`, `TypeScript API`, and `Compatibility`.

### 2. What AISuite contains

Use a compact component table:

| Component | Purpose | Consumer |
| --- | --- | --- |
| `AISuite::OpenAICodex` | typed backend/frontend SDK and transport adapters | C++ applications |
| `@snodec/codex-frontend` | framework-neutral frontend proxy and declarations | browser/Node clients |
| `codex-bridge` | one provider connection exposed to multiple clients | operators and UIs |
| `codex-bridge-client` | interactive reference client | evaluators/developers |
| generated protocol views | lossless typed access over pinned schema | both SDKs |

### 3. Quick start

Provide one released, clean path:

1. install the exact supported SNode.C version;
2. configure and build AISuite;
3. run focused tests;
4. start `codex-bridge` with one documented local transport;
5. connect `codex-bridge-client`;
6. submit one harmless request;
7. show expected request, response, and telemetry output.

Do not make `master`/HEAD a stable launch prerequisite. If the Codex app-server
requires its own authentication/setup, link to official instructions and state
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

### 5. Minimal TypeScript integration

Show package installation or workspace consumption, connection construction,
one typed call, event handling, cleanup, and the required WebSocket subprotocol.
State browser versus Node assumptions and package publication status.

### 6. Architecture and authority

Use an SVG with explicit boundaries:

```text
Native / browser / observer clients
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

Resolve the current CMake `0.7.0` versus npm `1.0.0` conflict before writing
stable claims. Define how protocol updates affect SemVer and supported branches.

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

## Visual requirements

### Required assets

- `assets/aisuite-hero.svg`
- `assets/multi-client-architecture.svg`
- `assets/authority-boundaries.svg`
- `assets/typed-generation-flow.svg`
- `assets/bridge-terminal.png`
- `assets/social-preview.png`

Diagrams should prioritize process and authority boundaries. Avoid generic AI
brain imagery. Terminal screenshots use synthetic thread/project names and no
tokens, filesystem identities, or private prompts.

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

## Documentation migration

1. Keep the complete architecture contract as authoritative detailed material.
2. Extract quick-start, API examples, compatibility, security, and operations
   into discoverable guides.
3. Add a generated API/declaration reference index.
4. Separate operator deployment from SDK consumption.
5. Link the landing page to stable headings and released documentation.

## Evidence checklist

- Unified version source and tagged release.
- Exact SNode.C and Codex schema compatibility.
- C++/TypeScript generation equality tests.
- Routing, callback, framing, and reconnect tests.
- Multi-client/controller/observer behavior tests.
- Backpressure and telemetry bounds.
- Clean install plus downstream CMake consumer.
- TypeScript clean package build/test.
- Security review of listeners and static file delivery.
- Independent-project wording and license verification.

## Review scenarios

1. A C++ developer finds a compilable typed request example quickly.
2. A web developer understands how to use the frontend proxy package.
3. An operator understands listener exposure and security requirements.
4. A protocol reviewer identifies the exact supported schema/revision.
5. A CodexUI developer finds the supported AISuite combination.

## Implementation sequence

1. Resolve product version and package-version mismatch.
2. Freeze SNode.C, schema, and CodexUI compatibility.
3. Qualify clean C++ and TypeScript quick starts.
4. Build multi-client and authority diagrams.
5. Draft hero, component overview, and minimal examples.
6. Publish generation, compatibility, listener, and security sections.
7. Connect architecture and API reference documentation.
8. Add ecosystem, support, security, contribution, and license routes.
9. Run code sample, link, visual, and clean-install automation.
10. Review claims against the tagged release before publication.

## Acceptance criteria

- [ ] A visitor can explain AISuite’s benefit without reading architecture docs.
- [ ] C++ and TypeScript examples are minimal, typed, and automatically tested.
- [ ] Version metadata is consistent across CMake, npm, docs, and releases.
- [ ] Exact SNode.C and Codex schema compatibility is published.
- [ ] Multi-client roles and authority boundaries are unambiguous.
- [ ] Listener and security assumptions are explicit.
- [ ] Generated coverage claims define their schema scope.
- [ ] Support, security, contribution, and licensing are easy to find.
- [ ] Assets pass accessibility and light/dark review.
- [ ] All commands work from a clean checkout of the release tag.

## Open decisions

- Whether AISuite launches as `1.0.0` or a consistent pre-1.0 release.
- Package publication strategy for `@snodec/codex-frontend`.
- Canonical Codex schema/revision naming in user-facing copy.
- Default supported listener deployment and TLS guidance.
- Controller/observer terminology for first-time users.
- Which request is safe and compelling for the quick-start demonstration.
