# AGENTS.md — SNode.C landing page

These instructions supplement the root [`AGENTS.md`](../AGENTS.md) for all work
under `SNode.C/`. Follow the shared [page system](../PAGE-SYSTEM.md) and this
directory's [proposal](PROPOSAL.md).

## What it solves

SNode.C reduces the low-level infrastructure required to build event-driven C++
network clients and servers. It provides a recurring model for connection
lifecycle, event dispatch, protocol layering, encryption, configuration, and
multiple address families so applications do not need to rebuild those concerns
around raw socket APIs.

## Project focus

Focus explicitly on SNode.C as an event-driven C++ networking framework. Lead
with its programming model, network application development, layered
architecture, transports, protocols, configuration model, and extension points.

Present MQTTSuite, AISuite, and CodexUI only as concise ecosystem examples.
SNode.C is the networking foundation; it is not primarily an MQTT product, an AI
integration, or a user interface.

## Project boundaries

- Do not attribute an application's features to SNode.C unless the framework
  itself exposes and supports the capability.
- Keep MQTTSuite operational workflows, AISuite protocol semantics, and CodexUI
  user experience on their own landing pages.
- Keep exhaustive constructors, callbacks, configuration options, and API
  walkthroughs out of the landing page.
- Describe Node.js only as inspiration for an event-driven programming model;
  never imply API, package, runtime, or JavaScript compatibility.
- Do not imply that composable network layers mean every combination is tested.

## Reader outcome

A qualified visitor should be able to:

1. explain the `SocketServer`/`SocketClient` → `SocketContextFactory` →
   `SocketContext` relationship;
2. build and run the approved echo first success;
3. distinguish network, transport, connection, and application layers;
4. find verified protocol, platform, compiler, and dependency scope;
5. decide whether SNode.C fits a C++ networking project.

## Audience priority

1. C++ developers building network servers, clients, gateways, and services.
2. Systems developers evaluating event-driven networking frameworks.
3. IoT, embedded Linux, ARM, and OpenWrt developers.
4. Contributors, educators, students, and downstream ecosystem developers.

## Terminology

- Product: **SNode.C**. Preserve punctuation and capitalization in prose.
- Canonical repository casing in URLs: `snode.c`.
- Use exact class names: `SocketServer`, `SocketClient`,
  `SocketContextFactory`, and `SocketContext`.
- Define **instance**, **event loop**, **connection layer**, and **application
  protocol** on first use.
- Use **single-threaded** and **single-tasking** only with precise operational
  explanation and verified scope.
- Prefer `Unix domain socket` in prose and the actual namespace/class spelling
  in code.

## Source and destination

- Read-only live source: `/home/voc/projects/snodec/snode.c`.
- Working public-copy surface: `SNode.C/README.md`.
- Project specification: `SNode.C/PROPOSAL.md`.
- Eventual destination: `SNodeC/snode.c/README.md`.
- Candidate repository URL — verify: `https://github.com/SNodeC/snode.c`.
- Candidate API documentation — verify:
  `https://snodec.github.io/snode.c-doc/html/index.html`.

## Approved decisions

- Primary outcome: build event-driven network applications in modern C++.
- Primary first success: a compact echo server/client example.
- Use the approved nine-section final map and shared product-page word target.
- V1 is a code-to-result hero; V2 is real echo terminal proof; V3 is the
  programming model; V4 is the layer architecture.
- Capabilities must distinguish available, tested, optional, and planned scope.
- Performance or footprint appears only when reproducible evidence is ready.
- Existing live README material is knowledge input only; rewrite independently.

## Source-code alignment and proof

Every statement about the programming model, event loop, layers, address
families, transports, TLS, protocols, configuration, dependencies, installation,
or platform support must be traced to the exact selected SNode.C revision.
Record the relevant public headers/classes, CMake targets and options, source
implementation, and unit/component/policy tests.

A class or namespace existing in source does not prove that every advertised
combination is built, installed, tested, or supported. Prove examples with clean
builds and runtime output, platform claims with CI or reproducible qualification,
and availability with tagged artifacts. When documentation and source disagree,
source plus tests and release metadata control the public statement.

## Candidate facts — verify

The live source currently suggests the following; verify all against the chosen
release, build configuration, tests, and documentation before public use:

- C++20 implementation with GCC and Clang support.
- Event-driven, layer-based, modular, single-threaded architecture.
- IPv4, IPv6, Unix domain, Bluetooth RFCOMM, and Bluetooth L2CAP address
  families.
- Connection-oriented stream transport and TLS support.
- HTTP, WebSocket, MQTT 3.1.1, MQTT over WebSocket, and Express-style APIs.
- API, command-line, and configuration-file configuration paths.
- Linux, x86-64, ARM, OpenWrt, and Android/Termux claims.
- OpenSSL, nlohmann/json, BlueZ, libmagic, MariaDB, CLI11, and spdlog dependency
  roles and minimum versions.
- `MIT OR LGPL-3.0-or-later` licensing.

## Commands and examples

Use this only as the command shape to qualify, not approved public copy:

- Reuse the isolated checkout's `cmake-build-release` directory for Release
  qualification and `cmake-build-debug` for Debug/test work while the SHA,
  compiler, generator, dependencies, and CMake options remain unchanged.
- Install into the shared isolated qualification prefix used by downstream
  MQTTSuite, AISuite, and CodexUI builds; never build or install in the live
  local SNode.C repository.

```sh
cmake -S . -B "$BUILD_DIR" -DCMAKE_BUILD_TYPE=Release
cmake --build "$BUILD_DIR" --parallel
ctest --test-dir "$BUILD_DIR" --output-on-failure
cmake --install "$BUILD_DIR" --prefix "$INSTALL_PREFIX"
```

Before publication, replace variables with clearly introduced paths, use the
current public master head, record its exact SHA, document mandatory and
optional dependencies, and test the
echo commands and downstream `find_package` consumer from clean environments.
Do not reuse moving-branch clone/install instructions as a stable quick start.
The transport examples must include a qualified mutual-TLS echo path as well
as concise plain IPv4, IPv6, and Unix-domain variants; do not reduce SNode.C's
networking presentation to clear-text TCP alone.

## Common misconceptions

- SNode.C is not Node.js rewritten in C++ and does not provide Node.js API
  compatibility.
- SNode.C is not synonymous with MQTTSuite.
- Protocol layers being present does not prove all transports and address
  families support every protocol combination.
- Event-driven and single-threaded do not automatically prove higher
  performance or lower memory use.
- OpenWrt or ARM relevance does not equal current support for every device or
  architecture.

## Open facts

- Exact release, maturity, release date, supported branch, and version source.
- Canonical echo excerpt and tested expected output.
- Tested compiler, platform, architecture, dependency, and protocol matrix.
- ABI/API stability and deprecation policy.
- Current OpenWrt targets and package ownership.
- Benchmark methodology and whether results qualify for launch.
- Canonical documentation, examples, support, security, roadmap, and
  contribution URLs.

## Validation

- Build and run the echo path from a clean temporary checkout of current master.
- Confirm the first example communicates the object model without horizontal
  scrolling or unexplained internal types.
- Verify every capability-table cell against build/test evidence.
- Ensure MQTT, AISuite, and CodexUI remain brief ecosystem examples.
- Check Node.js wording for false compatibility implications.
- Verify license identifiers, commands, links, V1–V4 assets, and alt text.
