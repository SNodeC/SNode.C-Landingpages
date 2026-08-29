# Step 2 — SNode.C ecosystem positioning

**Positioning date:** 29 August 2026

**Workflow stage:** Step 2 of the canonical AI-assisted README redesign

**Purpose:** establish the shared external story for the SNode.C organization and
its current project landing pages. This document is an editorial handoff, not a
fresh technical qualification. Step 3 must reverify project-specific claims
against current public source before they become final README copy.

## Basis and status

This positioning follows the repository-wide instructions, the canonical
workflow, the Step 1 audit, and the README governance resolution. It uses the
preserved fact/evidence layer and scoped project instructions as research.
Existing READMEs, proposals, figures, screenshots, and the former fixed page
system remain research/provenance inputs rather than presentation constraints.

The presentation-governance conflict recorded in Step 1 is resolved by
`workflow/README-GOVERNANCE.md`: the redesign keeps the source-alignment,
accessibility, reproducibility, and visual-quality principles, but does not keep
mandatory section counts, word targets, V1–V4 slots, or equal visual weight.

## Core positioning

The **SNode.C ecosystem** is a family of open-source C++ projects for building
and operating event-driven networked systems. **SNode.C** provides the reusable
networking foundation. **MQTTSuite** applies that foundation to practical MQTT
broker, integration, bridging, command-line, and persistence workflows.
**AISuite** applies the same event-driven approach to typed Codex app-server
integration and multi-client bridging. **CodexUI** provides native and browser
presentations for those Codex workflows.

The ecosystem should therefore be presented as a set of related but distinct
projects connected by a common engineering approach, not as one monolithic
product, one shared-version distribution, or one runtime pipeline.

The shortest durable external description is:

> **Event-driven C++ infrastructure, integrations, and applications for
> networked systems.**

This is a positioning statement, not necessarily final hero copy. Later README
design may express it differently while preserving the meaning.

## Problem space

The ecosystem addresses a recurring systems-development problem: useful network
applications require much more than opening a socket. They need connection
lifecycle handling, event dispatch, protocol layering, transport choices,
configuration, integration boundaries, operational tools, and user-facing
applications.

The current projects occupy different levels of that problem space:

- **network foundations** — reusable event-driven C++ networking and protocol
  infrastructure;
- **protocols and integrations** — focused applications and middleware that turn
  protocol capabilities into deployable workflows;
- **applications and interfaces** — user-facing software built on those
  integration layers.

This category model is intentionally broader than the current project list. New
protocol integrations, tools, examples, gateways, applications, or interfaces
can be added without redefining the ecosystem story.

## Primary audiences

The organization-level story should prioritize these audiences in this order:

1. **C++ networking and systems developers** evaluating an event-driven
   foundation for servers, clients, gateways, services, and integrations.
2. **IoT, MQTT, edge Linux, and OpenWrt engineers** looking for practical MQTT
   infrastructure and integration tools.
3. **AI-tooling and application developers** looking for typed Codex integration,
   shared bridge access, and native/browser clients without operating raw
   protocol messages directly.
4. **Contributors, educators, students, and technical evaluators** interested in
   event-driven architecture, networking, protocol integration, or the current
   applications built on the ecosystem.

Individual project pages may narrow or reorder these audiences. The organization
profile should help a visitor choose the relevant project quickly rather than
trying to make every project equally relevant to every reader.

## Ecosystem philosophy

The common story is architectural rather than marketing-led.

### Event-driven by default

SNode.C establishes the event-driven programming foundation. Downstream projects
reuse that model instead of building unrelated blocking or thread-per-connection
stacks around each domain.

### Layer responsibilities explicitly

The ecosystem separates networking foundation, protocol/integration behavior,
and presentation concerns. A project should own its layer clearly and link to
another project rather than absorbing its documentation or claiming its
capabilities.

### Compose focused projects instead of a monolith

MQTTSuite, AISuite, and CodexUI are not feature modes of one executable. Each
project has its own purpose, audience, release surface, tests, limitations, and
landing page. Their relationship should make selection easier, not erase those
boundaries.

### Prefer typed and reusable integration boundaries

Where the ecosystem wraps a complex external protocol, the editorial emphasis
should be on reusable integration surfaces and explicit ownership boundaries,
not on exposing raw wire messages as the primary developer experience. AISuite
is the clearest current example of this principle.

### Make claims traceable

Technical credibility is part of the product story. Public claims should follow
verified source, tests, reproducible runs, and release evidence. Source versions,
release maturity, supported platforms, compatibility, and security properties
must remain distinct concepts.

## Project roles

### SNode.C — networking foundation

**Role:** the foundation project for event-driven C++ networking.

SNode.C should be positioned around the programming model and the recurring
networking concerns it centralizes: connection lifecycle, event dispatch,
network/transport/application layering, configuration, protocol integration, and
multiple network families where verified.

Its landing page should answer: **How does SNode.C help me build a networked C++
application, and what programming model will I use?**

MQTTSuite, AISuite, and CodexUI are ecosystem examples, not the definition of
SNode.C itself.

### MQTTSuite — MQTT applications and integration toolkit

**Role:** a set of focused MQTT applications for deploying, integrating,
observing, bridging, and persisting MQTT workflows.

The current project identity is broader than MQTTBroker. The five application
names must remain distinct: **MQTTBroker**, **MQTTIntegrator**,
**MQTTBridge**, **MQTTCli**, and **MQTTStore**. The positioning should emphasize
how an operator or integrator chooses and combines those applications for MQTT
work rather than presenting one large daemon.

Its landing page should answer: **Which MQTTSuite application solves my MQTT
problem, and how do the applications fit into a practical message flow?**

SNode.C owns the underlying networking framework; MQTTSuite owns the MQTT-facing
operational and integration experience.

### AISuite — typed AI integration and bridge layer

**Role:** middleware for integrating C++ and browser clients with the Codex
app-server through typed asynchronous interfaces and a bounded multi-client
bridge.

AISuite should be positioned as the integration layer between client software
and the Codex app-server, not as a user interface, conversation database, or
semantic authority. Its developer value comes before internal controller,
observer, routing, or telemetry terminology.

Its landing page should answer: **What does AISuite save me from implementing
myself when I integrate Codex into a C++ or browser application?**

The Codex app-server remains the external protocol/semantic authority. AISuite
is independent open source and must not be presented as an official OpenAI SDK
or product.

### CodexUI — native and browser presentation layer

**Role:** user-facing native Qt and browser presentations for Codex workflows
through AISuite.

CodexUI should be positioned through the visible workflow: connect, select or
create work, submit a prompt, inspect activity, and understand current state.
Architecture explains that experience but should not lead the story.

Its landing page should answer: **What is it like to use Codex through CodexUI,
and what are the verified native/browser capabilities and boundaries?**

AISuite owns bridge/protocol integration; the Codex app-server owns conversation
semantics and persistence; CodexUI owns presentation and local interaction state
where verified. CodexUI is independent open source, not an official OpenAI
application.

## How the projects relate

The organization must preserve two honest evaluation tracks rather than invent
an all-product runtime story:

1. **Networking and MQTT:** SNode.C → MQTTSuite.
2. **Typed Codex client:** SNode.C → AISuite → CodexUI.

These arrows are useful shorthand for ecosystem orientation, not a substitute
for Step 3 verification of exact build-time and runtime relationships.

There is currently no verified reason to present MQTTSuite as part of the
AISuite/CodexUI runtime path, and no reason to imply that users need all current
projects together.

At organization level, the relationship should therefore be explained as a
shared foundation and engineering approach with separate application domains.
At repository level, each page should mention only the dependencies and sibling
projects needed to understand that project.

## Technically credible differentiators

The following are the strongest current differentiators to preserve in the
editorial strategy. Step 3 must still verify their exact project-specific scope
before final public wording.

1. **A reusable event-driven C++ networking foundation beneath real downstream
   projects.** The ecosystem demonstrates the framework through independently
   useful MQTT, AI-integration, and UI software rather than only isolated sample
   code.
2. **Layered separation from transport to application concerns.** The projects
   consistently distinguish networking infrastructure, protocol/integration
   behavior, and presentation responsibilities instead of collapsing them into
   one product.
3. **A practical MQTT toolkit rather than broker-only positioning.** MQTTSuite
   spans brokerage, transformation/integration, broker-to-broker bridging,
   command-line interaction, and persistence through separate applications.
4. **Typed Codex integration rather than raw JSON-RPC as the primary client
   surface.** AISuite provides C++ and TypeScript-facing integration surfaces and
   a shared bridge boundary while retaining raw access where verified.
5. **A visible application layer for the same AI integration path.** CodexUI
   provides native and browser user experiences that make the AISuite boundary
   concrete without turning AISuite into a UI project.
6. **Source-aligned documentation discipline.** The landing-page workflow treats
   implementation presence, tested behavior, release availability, and maturity
   as different evidence classes. This is a credibility mechanism, not a slogan.

Do not convert these differentiators into unqualified superlatives such as
`lightweight`, `complete`, `full`, `production-ready`, `secure`, or `fast`.

## Organization-level story

The organization profile is the front door and decision surface. It should
communicate only enough to let a visitor:

- understand the ecosystem in one short explanation;
- identify the relevant category and project;
- understand the two current evaluation tracks;
- see that the projects share an engineering foundation without assuming a
  monolithic release;
- reach the correct repository, documentation, demo, or verified trust route.

Use extensible categories rather than a fixed project count. The current
categories are:

- **Foundations** — currently SNode.C;
- **Protocols and integrations** — currently MQTTSuite and AISuite;
- **Applications and interfaces** — currently CodexUI;
- **Tools and examples** — available when maintained projects justify it.

The organization-level CTA remains **Run a demo**, with the two tracks kept
separate.

The organization profile should not duplicate build instructions, detailed
transport matrices, API walkthroughs, bridge semantics, UI state definitions, or
project-specific compatibility tables.

## Repository-level positioning boundaries

Each repository landing page owns one primary question and one primary
centerpiece:

| Project | Primary question | Narrative centerpiece |
| --- | --- | --- |
| SNode.C | How do I build an event-driven network application with this framework? | Programming model |
| MQTTSuite | Which application solves my MQTT task and how do the applications work together? | MQTT applications and message flows |
| AISuite | How do I integrate Codex without reimplementing raw protocol plumbing? | Typed AI middleware and bridge architecture |
| CodexUI | What user workflow do the native/browser presentations provide? | Real user workflow and UI |

Repository pages may mention the ecosystem briefly, but must not retell the
organization profile or absorb another project's implementation detail.

Detailed reference material belongs in maintained project documentation once a
stable destination exists. README copy should prioritize orientation, proof,
first success, important limitations, and routes to deeper material.

## Canonical terminology

Use these names consistently across later workflow artifacts and public copy:

- **SNodeC** — the GitHub organization name.
- **SNode.C ecosystem** — the collective name for the related projects.
- **SNode.C** — the event-driven C++ networking foundation; preserve punctuation
  and capitalization.
- **MQTTSuite** — the MQTT toolkit/project.
- **MQTTBroker**, **MQTTIntegrator**, **MQTTBridge**, **MQTTCli**,
  **MQTTStore** — exact MQTTSuite application names.
- **AISuite** — the typed integration and bridge layer for Codex-related clients.
- **CodexUI** — the user-facing native/browser application project.
- **Codex app-server** — the external provider/protocol authority; use this term
  on first reference in Codex-related pages.
- **codex-bridge** — AISuite service, not the CodexUI semantic backend.
- **CodexWebUI** — browser artifact name where source/release evidence supports
  that exact term.
- **project** — preferred organization-directory term; use `component` only for
  a technical component inside a project.
- **Run a demo** — organization-level CTA.

For AISuite/CodexUI, use a concise independent-project notice and do not imply
OpenAI ownership or endorsement.

Avoid using `SNode.C` as shorthand for the entire organization when that would
be ambiguous. Avoid generic `AI platform`, `MQTT platform`, or `full-stack`
labels that erase project boundaries.

## Claims and questions requiring later verification

Step 2 intentionally does not resolve the following. Step 3 must verify them
against current public source, tests, runtime qualification, and release
metadata before they become public claims.

### Shared

- Current public `master` heads and whether the 28 August evidence baseline has
  changed.
- Exact current build-time and runtime dependency relationships between projects.
- Release/maturity labels, compatibility policy, supported platforms, compiler
  ranges, architectures, and packaging status.
- Canonical support, security, contribution, roadmap, and documentation routes.
- Any performance, footprint, security, stability, production-readiness, or
  broad support claim.

### SNode.C

- Exact current scope of address families, transports, TLS, protocols,
  configuration surfaces, compiler/platform support, and tested combinations.
- Current first-success echo commands and expected output.
- Full-test status, install/release availability, and compatibility guarantees.

### MQTTSuite

- Exact MQTT 3.1.1 behavior and conformance scope, including QoS, retain,
  sessions, will, credentials, and wildcards.
- Per-application transport matrix and runtime qualification beyond the basic
  broker/subscriber/publisher path.
- Mapping, bridging, loop prevention, persistence, MariaDB, Web UI, OpenWrt, and
  packaging behavior.

### AISuite

- Exact current SNode.C and Codex schema/app-server compatibility.
- Typed operation coverage, raw access, controller/observer guarantees,
  provider/frontend transport matrices, reconnect/backpressure/telemetry
  behavior, and listener exposure assumptions.
- Authentication/security ownership, public package/release status, and final
  license/support routes.

### CodexUI

- Exact current CodexUI/AISuite/SNode.C compatibility.
- Native/browser feature and limitation matrix, target/active/running/inspected
  semantics, reconnect behavior, and persistence boundaries.
- Public release/artifact status, supported Linux/browser environments,
  dependency-audit disposition, installation routes, and privacy/security
  boundaries.

## Handoff to Step 3

### 1. Canonical ecosystem positioning Step 3 must preserve

The SNode.C ecosystem is a family of related, independently useful C++ projects
for event-driven networked systems. SNode.C is the networking foundation;
protocol/integration projects and user-facing applications build on that
engineering approach without becoming one monolithic product or shared release.
The organization should help visitors choose the correct project and one of two
honest evaluation tracks rather than imply an all-project runtime system.

### 2. Current project roles

- **SNode.C:** event-driven C++ networking foundation; centerpiece is the
  programming model.
- **MQTTSuite:** focused MQTT applications and integration toolkit; centerpiece
  is applications plus message flow.
- **AISuite:** typed Codex integration and multi-client bridge layer; centerpiece
  is middleware/bridge architecture and developer integration.
- **CodexUI:** native/browser presentation layer for Codex workflows through
  AISuite; centerpiece is the real user workflow and UI.
- **SNodeC organization profile:** extensible ecosystem navigator and project
  selection surface, not another product manual.

### 3. Terminology that must remain consistent

Preserve the exact product/application names and capitalization defined in
`Canonical terminology`. Use **SNode.C ecosystem** for the collective project
family, **SNodeC** for the GitHub organization, and **SNode.C** for the networking
foundation. Keep **Codex app-server** distinct from **AISuite**, keep
**codex-bridge** owned by AISuite, and keep **CodexUI** as the presentation
project. Codex-related projects require independent-project wording.

### 4. Unresolved factual questions Step 3 must verify

Step 3 must refresh source heads and verify the project-specific capability,
dependency, compatibility, runtime, release, maturity, support, security, and
platform claims listed in `Claims and questions requiring later verification`.
It must not weaken the project boundaries in order to produce a simpler story.
If current source evidence contradicts this positioning at a factual level,
record the conflict explicitly and return it for editorial resolution rather
than silently rewriting the ecosystem relationship.
