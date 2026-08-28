# Proposal — SNode.C Repository Landing Page

[← Working landing page](README.md) · [Launch roadmap](../README.md)

## Purpose

Transform the SNode.C root README from a long technical manual into a focused
landing page for a modern event-driven C++ networking framework. Preserve the
existing technical depth by moving it into structured documentation, while the
root README answers what SNode.C is, why it matters, how it feels to use, and
how to achieve a first success.

## Audience and jobs to be done

### Primary audiences

- C++ developers building network servers, clients, gateways, and services;
- systems developers comparing asynchronous/event-driven frameworks;
- IoT and embedded Linux engineers needing extensible transport stacks.

### Secondary audiences

- students and educators learning layered networking architecture;
- MQTTSuite, AISuite, and CodexUI contributors;
- OpenWrt and ARM integrators;
- reviewers evaluating maturity, performance, and maintainability.

### Visitor questions

- What does SNode.C make easier than direct socket programming?
- What does “in the spirit of Node.js” mean—and not mean?
- Which transports and application protocols exist today?
- What is the programming model?
- Can I build and install it on my platform?
- Is there measured evidence for footprint and performance?

## Positioning

### Working headline

> Build event-driven network applications in modern C++.

### Supporting statement

> SNode.C combines a single-threaded event model with composable network layers,
> configurable clients and servers, and reusable HTTP, WebSocket, MQTT, TLS,
> database, and transport building blocks where supported.

### Primary call to action

**Build and run the echo example**

### Secondary calls to action

- Explore supported protocols.
- Read the architecture.
- See applications built with SNode.C.

## Narrative principles

- Lead with developer outcome, not project history.
- Demonstrate the programming model before listing every API.
- Define “single-threaded” and “single-tasking” precisely and explain the
  operational implications.
- Describe the Node.js inspiration as an event-model analogy, not compatibility.
- Separate tested support from theoretically buildable configurations.
- Link deep reference material instead of embedding it wholesale.

## Page architecture

### 1. Hero

Include:

- SNode.C mark/name and stable version;
- headline and two-sentence description;
- at most three badges: release, CI, and license;
- links to `Quick start`, `Documentation`, and `Examples`;
- a compact architecture or code-to-result visual.

### 2. First success in 60 seconds

Show the smallest example that communicates the framework’s character. The code
should include only the essential server/client, factory, and context concepts.
Beside or immediately below it, show:

- build command;
- run command;
- expected output;
- link to the complete example;
- tested SNode.C release and platform.

If the true first build takes longer, label the section honestly as a five-
minute quick start rather than making an unrealistic promise.

### 3. Why SNode.C

Use four or five evidence-backed differentiators:

- event-driven programming model;
- composable network/application layers;
- consistent configuration through API, CLI, and files;
- transport and protocol extensibility;
- suitability for Linux, ARM, and OpenWrt where proven.

Each differentiator should connect to a concrete example or reference section.

### 4. Programming model

Explain the recurring object relationship:

```text
SocketServer / SocketClient
          │
          ▼
SocketContextFactory
          │ creates per connection
          ▼
SocketContext / application protocol
```

Add one paragraph on callbacks, connection lifecycle, event dispatch, and where
application state belongs. Link to the full API reference.

### 5. Capability matrix

Present a compact, verified table with columns for capability, client/server,
transport/address families, encryption, maturity, and documentation. Candidate
rows include:

- TCP and Unix domain stream sockets;
- IPv4 and IPv6;
- TLS;
- HTTP and expressive routing;
- WebSocket;
- MQTT primitives;
- Bluetooth RFCOMM/L2CAP if currently supported and tested;
- MariaDB integration;
- configuration and logging.

Do not imply all combinations are tested merely because layers are composable.

### 6. Architecture

Use one layered SVG:

```text
Application protocols and middleware
Connection and upgrade layers
Transport and encryption layers
Socket/address families
Event loop and operating system
```

Explain extension points and ownership/lifetime at a conceptual level. Link to
detailed architecture and generated API documentation.

### 7. Installation

Offer paths in priority order:

1. released source build on Debian/Ubuntu;
2. CMake package consumption;
3. OpenWrt packages/feed where current;
4. other verified platforms.

Commands must use a release tag, an out-of-tree build, `cmake --build`,
`ctest`, and `cmake --install`. Clearly list minimum CMake, compiler, language
standard, and required/optional dependencies.

### 8. Ecosystem and examples

Show SNode.C as a foundation, with internal links to the developed presentations
for MQTTSuite, AISuite, and CodexUI during drafting. Production links are swapped
only at publication.

Use two or three examples that demonstrate different layers rather than a large
undifferentiated list.

### 9. Performance and footprint

Include this section only after producing reproducible measurements. Publish:

- hardware, OS, compiler, build type, and dependency versions;
- benchmark source and commands;
- latency/throughput or memory metrics relevant to stated use cases;
- date and comparison limitations.

Never use “lightweight” as an unsupported comparative claim.

### 10. Compatibility and support

State:

- supported release branches;
- tested compiler/platform matrix;
- ABI/API stability expectations;
- relationship to MQTTSuite/AISuite versions;
- where to ask questions, report bugs, and disclose vulnerabilities.

### 11. Contribution and license

Link contribution guide, code style, tests, architecture, good first issues,
code of conduct, security policy, and dual MIT/LGPL licensing explanation.

## Visual requirements

### Required assets

- `assets/snodec-hero.svg`
- `assets/programming-model.svg`
- `assets/layer-architecture.svg`
- `assets/echo-terminal.png`
- `assets/social-preview.png`

The hero should show code or architecture, not a generic network stock image.
Diagrams must use the organization’s shared visual grammar and remain readable
at GitHub’s content width.

## Copy and style rules

- Use `SNode.C` consistently in prose and the canonical repository casing in
  URLs and commands.
- Prefer concrete verbs: build, listen, connect, route, upgrade, configure.
- Define framework-specific classes on first use.
- Keep the first code example short enough to understand without horizontal
  scrolling.
- Move exhaustive tables and full API walkthroughs into `docs/`.
- Avoid project-history detail before the quick start; retain a concise origin
  section near the end.
- Use at most three hero badges and no vanity counters.

## Documentation migration

The existing long README must not be discarded. During implementation:

1. inventory every current heading and anchor;
2. map each item to landing page, guide, reference, example, or archive;
3. preserve useful stable anchors through redirects/compatibility links where
   practical;
4. move detailed configuration, transport APIs, callbacks, and examples into
   `docs/`;
5. check all inbound repository links before replacing the root README.

## Evidence checklist

- Exact current version and release date.
- Clean-build CI matrix.
- Install and downstream CMake consumer test.
- Supported transport/protocol combinations.
- Compiler and platform minimums.
- Benchmark methodology for performance claims.
- OpenWrt version and architecture evidence.
- License and security-policy links.

## Review scenarios

1. A C++ developer must understand the object model from the first example.
2. A framework evaluator must find supported protocols without reading the API.
3. An embedded engineer must distinguish tested ARM/OpenWrt support from plans.
4. A downstream developer must find a working `find_package` example.
5. An existing user must still locate detailed configuration documentation.

## Implementation sequence

1. Audit existing README content and inbound links.
2. Freeze release/version and tested platform matrix.
3. Select and qualify the canonical first example.
4. Draft hero, value statement, and quick start.
5. Build programming-model and layer diagrams.
6. Publish capability, compatibility, and installation sections.
7. Migrate detailed manual content into structured docs.
8. Add ecosystem, support, contribution, security, and license routes.
9. Run clean-machine and downstream-consumer tests.
10. Review mobile, dark mode, links, code copying, and accessibility.

## Acceptance criteria

- [ ] A first-time visitor reaches a successful example within ten minutes.
- [ ] Programming model is understandable without reading implementation code.
- [ ] Capabilities distinguish available, tested, and planned support.
- [ ] Installation uses a tagged release and clean build.
- [ ] All technical claims link to evidence.
- [ ] Detailed existing documentation remains discoverable.
- [ ] Ecosystem relationships are accurate and concise.
- [ ] Support, security, contribution, and licensing are easy to find.
- [ ] Images and diagrams pass light/dark and accessibility review.
- [ ] All commands are tested verbatim before publication.

## Open decisions

- Canonical first example and acceptable line count.
- Exact stable version and supported branch policy.
- Which protocol combinations belong in the landing-page matrix.
- Whether performance evidence is ready for launch.
- Canonical documentation location and migration strategy.
- Final wording for Node.js inspiration and single-threaded behavior.
