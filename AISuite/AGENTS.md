# AGENTS.md — AISuite landing page

These instructions supplement the root [`AGENTS.md`](../AGENTS.md) for all work
under `AISuite/`. Follow the shared [page system](../PAGE-SYSTEM.md) and this
directory's [proposal](PROPOSAL.md).

## What it solves

AISuite reduces the work required to integrate C++ and browser clients with the
Codex app-server protocol. Current master provides typed asynchronous C++
access, a framework-neutral TypeScript SDK, transport adaptation, and one
multi-client bridge so consumers do not each need to implement raw JSON-RPC,
routing, correlation, and protocol generation independently.

## Project focus

Focus on developer integration and the bridge's clearly bounded role. Lead with
typed C++ and TypeScript access, then show a successful bridge and client
interaction. Explain multi-client controller/observer behavior, shared
generation, browser delivery, and authority boundaries in plain language.

Use CodexUI as the primary visual consumer example, but do not let UI behavior
dominate the AISuite page.

## Project boundaries

- The Codex app-server owns protocol semantics and conversation persistence.
- AISuite owns transport adaptation, routing, controller coordination, typed
  facades/views, and bounded telemetry only where verified.
- Client applications own presentation and local interaction state.
- AISuite must not be described as another conversation database, semantic
  authority, or official OpenAI SDK.
- Keep CodexUI widgets, state presentation, and native UX on the CodexUI page.
  AISuite may document its browser SDK and static listener without claiming that
  it builds or releases a CodexWebUI application.

## Reader outcome

A qualified visitor should be able to:

1. explain what AISuite adds beyond raw JSON-RPC;
2. identify the C++, bridge, reference-client, and generated-view
   components;
3. build the bridge, connect a client, and perform one safe request;
4. understand provider, controller, observer, persistence, and trust boundaries;
5. find the exact SNode.C, schema, package, and CodexUI compatibility information.

## Audience priority

1. C++ and browser developers integrating Codex into tools or applications.
2. Systems engineers operating one provider connection for multiple clients.
3. Protocol, code-generation, security, and CodexUI contributors.

## Terminology

- Product: **AISuite**.
- CMake target/component: `AISuite::OpenAICodex`.
- TypeScript source package: `@snodec/codex-frontend`; distinguish its manifest
  version, tested source contents, packability, and registry publication.
- Services/tools: `codex-bridge` and `codex-bridge-client`.
- Use **Codex app-server** on first reference and define its role.
- Use **provider**, **controller**, **observer**, **typed view**, **frontend
  proxy**, **raw JSON-RPC**, and **bounded telemetry** consistently with the
  architecture contract.
- Use `getRaw()` exactly when describing lossless raw JSON access.

## Source and destination

- Read-only live source:
  `/home/voc/projects/drafts/AISuite-extraction/AISuite-final`.
- Working public-copy surface: `AISuite/README.md`.
- Project specification: `AISuite/PROPOSAL.md`.
- Eventual destination: `SNodeC/AISuite/README.md`.
- Candidate repository URL — verify: `https://github.com/SNodeC/AISuite`.
- Architecture source in the live repository — verify path and stable public
  destination: `src/ai/openai/codex/docs/architecture.md`.

## Approved decisions

- Primary CTA: build `codex-bridge` and connect a client.
- The page leads with developer value before internal authority terminology.
- Current-master examples use the installed C++ target/reference client and the
  tested TypeScript source package without implying registry publication.
- V1 shows multiple client types converging on the bridge and app-server.
- V2 proves provider/bridge/client success; V3 shows authority boundaries; V4
  shows the typed-generation and equality-test flow.
- Carry a concise independent-project notice near the first Codex description
  and in the final project routes.
- Use the approved nine-section map and shared word target.

## Source-code alignment and proof

Every statement about typed coverage, generation, routing, provider/controller/
observer behavior, framing, reconnect, bounds, telemetry, listener routes, or
security assumptions must be traced to the exact selected AISuite revision,
pinned Codex schema, and compatible SNode.C revision. Record generator inputs,
public targets/headers, bridge implementation, and focused equality, routing,
transport, and lifecycle tests.

Generated types existing in source do not prove compatibility with an unnamed
app-server revision. A configured route does not prove safe deployment. Support
behavior claims with tests and reproducible bridge/client runs, and support
availability claims with tagged packages and artifacts.

## Candidate facts — verify

The live source currently suggests the following; verify all against the chosen
release, pinned schema, tests, and documentation:

- Generated typed C++ views derived from recorded schema and operation inputs.
- Lossless `getRaw()` access and a raw JSON-RPC submission path.
- One provider connection exposed to controller and observer clients.
- Routing, framing, callback, reconnect, telemetry, and backpressure behavior.
- Integrated static-file and `/codex` WebSocket listener using the `codex`
  subprotocol.
- TypeScript sources, shared generation, WebSocket lifecycle, and browser-client
  behavior are on master; public-registry publication is absent.
- Static Web UI root and `/codex` upgrade behavior; do not infer that AISuite
  builds or installs the Web UI artifact.
- Public namespace/header layout and CMake package consumption.
- Any license claim; do not infer it from related projects.

## Commands and examples

Use these only as qualification shapes, not approved public copy:

- Reuse the isolated checkout's `cmake-build-release` directory for Release
  qualification and `cmake-build-debug` for Debug/test work while the SHA,
  compiler, generator, SNode.C prefix, and CMake options remain unchanged.
- Keep the SNode.C/AISuite install prefixes and AISuite build outside both live
  local repositories. Run the TypeScript package commands from the same
  isolated current-master checkout.

```sh
cmake -S . -B "$BUILD_DIR" \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_PREFIX_PATH="$SNODEC_PREFIX" \
  -DAISUITE_BUILD_APPS=ON \
  -DAISUITE_BUILD_CODEX_TESTS=ON
cmake --build "$BUILD_DIR" --parallel
ctest --test-dir "$BUILD_DIR" -L codex --output-on-failure
cmake --install "$BUILD_DIR" --prefix "$INSTALL_PREFIX"
npm ci --prefix packages/codex-frontend
npm test --prefix packages/codex-frontend
```

Public commands must use current SNode.C and AISuite master heads and record
their exact tested SHAs. The quick-start request must be harmless, reproducible, and
documented with expected response and telemetry. C++ samples must compile in CI
and must not use private headers or sibling paths.

Document transport selection on both independent bridge boundaries:

- provider side, from `codex-bridge` to the Codex app-server (`stdio`, Unix
  WebSocket, IPv4 WebSocket, and IPv6 WebSocket);
- frontend side, from CodexUI or `codex-bridge-client` to `codex-bridge`
  (qualified stream, TLS, WebSocket, and WSS instances).

Do not collapse the two directions into one transport list or imply that
provider-side TLS exists when the current app-server listener has no WSS mode.

## Common misconceptions

- AISuite is not CodexUI; it is the integration and bridge layer.
- Typed schema coverage does not automatically prove behavioral compatibility
  with every app-server revision.
- Stateless bridge design does not mean the bridge has no transient routing,
  connection, controller, or telemetry state.
- Raw JSON access does not replace the typed API as the primary integration path.
- A local default does not make remote listener exposure secure automatically.
- AISuite is independent open source, not an official OpenAI product.

## Open facts

- Master source version is `0.7.0`; maturity and release wording remain open.
- Exact SNode.C release and Codex schema/revision compatibility.
- Release policy and future publication destination for
  `@snodec/codex-frontend`; public npm publication is currently absent.
- Exact controller/observer guarantees and terminology for first-time readers.
- Listener defaults, authentication ownership, TLS/reverse-proxy guidance, and
  remote-exposure policy.
- License, security, support, roadmap, API, package, and release URLs.
- The exact safe request used in the quick start.

## Validation

- Build, test, install, and consume AISuite from clean current-master checkouts.
- Run the C++ generation/equality tests and state their schema
  scope accurately.
- Execute the bridge/reference-client quick start and compare V2 with reality.
- Review every arrow and ownership label in V1, V3, and V4 against the
  architecture contract and tests.
- Check listener, controller, telemetry, logging, and exposure language with a
  security reviewer.
- Verify independent-project wording, exact names, links, alt text, and assets.
