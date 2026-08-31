# MQTTSuite README Review Handoff

**Status:** Reconciled review handoff for the correction and revision phase  
**Purpose:** Canonical input for product/code decisions and the subsequent README revision  
**Important:** Do **not** start by rewriting the READMEs. Resolve the product/code decisions and runtime-verification items first.

---

## 1. Scope and evidence baseline

This handoff reconciles three review passes:

1. the frozen MQTTSuite Step 6 README candidates;
2. Claude's independent source-aligned review;
3. ChatGPT's meta-review of that review and Claude's subsequent response to the meta-review.

The review is intentionally **source-driven**.

The existing READMEs must **not** be treated as the feature inventory. The implementation must be inspected independently and the documentation compared against that implementation-derived inventory.

### Documentation repository

Repository:

`SNodeC/SNode.C-Landingpages`

The Step 6 candidate content was frozen at:

`3807159213f094512398c962b853f5dfec22adfa`

A later repository state observed during the review was:

`dfebcdf427824793f0c7d40fd47f5a8db9a058df`

That later state duplicated the five application README candidates into another workflow location rather than removing the original copies. Treat this as **workflow hygiene**, not as a README-content defect.

Primary candidate documents:

- `MQTTSuite/workflow/06-README-DRAFT.md`
- `MQTTSuite/workflow/06-DOCUMENTATION-ARCHITECTURE.md`
- the five application README candidates for:
  - MQTTBroker
  - MQTTIntegrator
  - MQTTBridge
  - MQTTCli
  - MQTTStore

### Implementation repositories

Primary MQTTSuite implementation baseline:

`SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`

Foundation baseline:

`SNodeC/snode.c@60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`

If implementation changes are made in response to this review, pin new source commits and revalidate affected documentation claims against those commits.

---

# 2. Governing review principles

## 2.1 MQTTSuite is an application suite first

MQTTSuite is primarily an **application suite** consisting of:

- MQTTBroker
- MQTTIntegrator
- MQTTBridge
- MQTTCli
- MQTTStore

The public documentation must primarily help users:

- understand what the suite does;
- understand why each application exists;
- choose the right application or combination;
- install the suite;
- configure the applications;
- run them;
- combine them;
- operate them;
- troubleshoot them.

MQTTSuite is **not primarily a reusable framework/library repository**.

The implementation is deliberately extensible and has framework-like qualities, but that is the **secondary documentation perspective**.

Therefore:

**Primary narrative:** five usable applications and their workflows.

**Secondary narrative:** how those applications can be extended and used as foundations for specialized solutions.

Do not let internal architecture or extensibility displace the application-suite story.

## 2.2 Correctness and completeness are independent requirements

The documentation must satisfy both.

### Correctness

Public claims must be:

- technically true;
- precise;
- current;
- source-aligned;
- consistent with actual runtime behavior where runtime behavior matters.

### Completeness

All user-relevant implemented:

- capabilities;
- configuration mechanisms;
- operational behavior;
- extension points;
- constraints;
- important inherited SNode.C capabilities

must be documented somewhere appropriate.

A feature is **not adequately documented merely because it is mentioned**.

The intended reader must understand what it does and, where appropriate, be able to use or configure it without reverse-engineering the source.

## 2.3 Current source behavior is not automatically the desired public contract

Source code is authoritative for establishing:

> **what the current implementation actually does.**

It is **not automatically authoritative for deciding**:

> **what the application ought to do and what should become the documented public contract.**

When code appears:

- unsafe;
- accidental;
- inconsistent;
- surprising;
- defective;
- or inconsistent with intended semantics,

do **not** automatically rewrite the README to memorialize the defect.

Use:

- `FIX CODE`, or
- `DECISION REQUIRED`

first.

Only after the intended contract is settled should the final README wording be written.

## 2.4 GitHub README scope must remain disciplined

Completeness does not mean placing every source-derived fact into the README.

Use layered documentation.

### Root README

Own:

- what MQTTSuite is;
- why it is useful;
- application chooser;
- installation;
- shared concepts;
- first success;
- major combined workflows;
- concise common configuration model;
- navigation.

### Application README

Own:

- complete application-level purpose;
- usage;
- application configuration;
- major operational behavior;
- representative examples;
- application-specific troubleshooting.

### Shared configuration reference

Own exhaustive common SNode.C/MQTTSuite configuration behavior.

### Integrator mapping reference

Own exhaustive mapping grammar and semantics.

### Broker HTTP/event API reference

Own the external Broker HTTP/SSE/admin contract.

### Developer/extensibility documentation

Own implementation architecture and extension contracts.

### Code/issues

Own defects that should be fixed rather than taught as user-facing behavior.

---

# 3. Evidence and disposition vocabulary

Future review/correction work should classify material findings using the following evidence classes.

### `[CODE]`

Directly established from executable source logic.

### `[DECL]`

Established from:

- schema;
- configuration declaration;
- CMake declaration;
- installation rule;
- or another declarative source.

### `[INFER]`

A reasonable conclusion from source, but not directly demonstrated end-to-end.

### `[UNVERIFIED-RUNTIME]`

Runtime behavior still needs actual execution/testing.

Every significant finding should also receive one disposition:

- `FIX CODE`
- `FIX DOC`
- `DECISION REQUIRED`
- `ADD REFERENCE DOCUMENTATION`
- `WORKFLOW CLEANUP`

These categories must not be conflated.

---

# 4. Executive verdict

## Overall assessment

**Current Step 6 documentation quality:** approximately **7/10**

**Publication readiness:** **not publication-ready**

**Structural rewrite required:** **no**

**Application-suite framing:** **correct**

The Step 6 work established a strong overall documentation architecture and produced substantial technically useful content.

The central failure is **not** that Step 6 misunderstood what MQTTSuite is.

The central failure is that the source audit was not deep enough before the README candidates were frozen.

The next phase should therefore **not restart the README design**.

It should:

1. resolve product/security/code issues;
2. close source-alignment gaps;
3. deepen configuration documentation;
4. validate runtime behavior;
5. execute the documented examples;
6. add a small number of dedicated reference documents;
7. revise the existing README architecture rather than replacing it.

## Largest issues

1. MQTTBroker credentials are serialized into client-state JSON and exposed through operational surfaces; live client events also place the serialized data into normal information-level logs.
2. MQTTIntegrator has mapping semantics/default-behavior questions that require product/code decisions before documentation can be finalized.
3. The inherited SNode.C configuration system is significantly under-documented for MQTTSuite users.
4. MQTTIntegrator mapping documentation is not yet deep enough for a reader to design a substantial mapping independently.
5. The documented build/install workflow has compatibility and installed-tree runtime-resolution issues requiring real validation.
6. Some usage examples describe application output/lifecycle inaccurately.
7. Workflow state currently contains duplicate application candidate locations.

---

# 5. Track 1 — Product / security / implementation issues

These findings must be handled **before final README wording is frozen**.

## P0 — Broker credential serialization and disclosure

**Evidence:** `[CODE]`  
**Affected:** MQTTBroker  
**Disposition:** `FIX CODE`  
**Publication blocker:** **yes**

### Established implementation behavior

In:

`mqttbroker/lib/MqttModel.cpp`

the JSON serialization of an MQTT client contains, among other fields:

- `username`;
- `password`;
- username/password flags;
- client ID;
- connection information;
- session information.

That serialized representation is used by the Broker's client-state/event infrastructure.

Two separate disclosure channels exist.

### A. Event-stream disclosure

When a new event receiver is attached, the Broker replays currently connected client state.

That client state currently contains the serialized MQTT password.

Both reviewed event-stream routes are unauthenticated at the application level.

The modern:

`/api/mqtt/events`

route explicitly emits permissive cross-origin headers.

The legacy:

`/sse`

route is also unauthenticated but does not itself set the same explicit cross-origin header in the reviewed route implementation.

### B. Live log disclosure

Live client connect/disconnect events use the broadcast `sendJsonEvent(...)` path.

That overload writes the serialized event JSON through:

`brokerLog().info()`

before broadcasting it.

Because the serialized JSON contains the password, live client events can therefore place MQTT passwords into ordinary information-level logs.

This does **not** require access to the Broker's HTTP event stream.

Anyone with access to:

- logs;
- centralized log collection;
- support bundles;
- archived service output

may receive the credential.

### Important distinction

The per-response event replay path used when an event-stream client first connects does **not** use the same information-level broadcast log operation.

Therefore:

- event replay leaks through the event stream;
- live connect/disconnect leaks through the event stream **and** the normal log path.

### Required action

Do **not** solve this primarily by adding README warnings.

The implementation should be changed so that:

- passwords are not part of normal client-state/event JSON;
- passwords are never written to normal logs;
- secret-bearing objects have an explicit redaction policy.

After fixing the implementation, document the resulting event/API trust model.

Also perform a suite-wide credential-handling audit.

## P0/P1 — Broker mutating administration endpoints lack an application authentication layer

**Evidence:** `[CODE]`  
**Affected:** MQTTBroker  
**Disposition:** `DECISION REQUIRED`, probably followed by `FIX CODE`  
**Publication blocker:** **yes until the public trust model is explicit**

The reviewed Broker router exposes mutating operations including actions equivalent to:

- disconnect a client;
- unsubscribe a client;
- release a retained message;
- subscribe a client.

No application-level authentication layer protects those actions in the reviewed implementation.

A product/security decision is required.

Possible intended models include:

- authenticated administration;
- deliberately trusted-local administration;
- binding/listener restrictions;
- deployment-level protection.

The README must not present an ambiguous management surface.

Do not merely add a warning if the intended product contract should instead provide protection.

## P1 — Integrator `#` matching semantics conflict with the current documentation

**Evidence:** `[CODE]`  
**Affected:** MQTTIntegrator/shared mapping layer  
**Disposition:** `DECISION REQUIRED`  
**Publication blocker:** **yes**

`MqttMapper::findMatchingTopicLevel(...)` treats:

- literal names;
- `+`;
- `#`

as matching candidate level names.

However, the reviewed recursion only returns that matching node when there is no further unconsumed topic level.

The current README describes `#` as representing the remaining subtree.

That prose cannot ship against the reviewed implementation.

### Do not automatically rewrite the README

A product decision is required:

#### Option A — implementation defect

If multi-level wildcard behavior is intended, fix the matcher and document the corrected semantics.

#### Option B — intentional MQTTSuite semantics

If the current behavior is intentional, describe it explicitly and avoid implying normal MQTT multi-level wildcard behavior.

Current source establishes the discrepancy.

It does **not** decide which behavior should become the public contract.

## P1 — Integrator contains an inline mapping that overrides the initially selected mapping

**Evidence:** `[CODE]`  
**Affected:** MQTTIntegrator  
**Disposition:** `DECISION REQUIRED`  
**Publication blocker:** **yes because effective default behavior is ambiguous**

In:

`mqttintegrator/mqttintegrator.cpp`

the application establishes a mapping file/default and subsequently invokes an inline `setMapping(...)` call.

The source itself describes that inline mapping as overriding the mapping loaded from the file.

This should not automatically be documented as a feature.

It first requires a product decision.

Determine whether the inline mapping is:

1. development/demo residue that should be removed;
2. an intentional shipped example/default;
3. a deliberate application contract.

The documentation should follow that decision.

Also note:

`--mqtt-mapping-file`

is part of the normal configuration mechanism. Its activation must not be described as command-line-only behavior.

## P1 — Integrator administration uses fixed default credentials in the reviewed application wiring

**Evidence:** `[CODE]` / `[DECL]`  
**Affected:** MQTTIntegrator  
**Disposition:** `DECISION REQUIRED`, likely `FIX CODE`  
**Publication blocker:** **yes if the administration surface is intended for real deployment**

`MappingAdminRouter::AdminOptions` defaults to credentials equivalent to:

`admin / admin`

and the reviewed Integrator main creates the router using default `AdminOptions{}`.

The documentation must not tell users to “change the credentials” unless a supported application configuration path actually exists.

Prefer exposing a supported configuration mechanism or redesigning the administration trust model before publication.

## P1 — Installed-tree runtime resolution is not yet demonstrated for the documented installation workflow

**Evidence:** `[UNVERIFIED-RUNTIME]` for exact MQTTSuite applicability; a minimal empirical reproducer exists  
**Affected:** suite build/install  
**Disposition:** `DECISION REQUIRED` plus runtime verification  
**Publication blocker:** **yes for installation claims**

During the review, a minimal CMake test produced:

- a shared library installed into the installation library directory;
- an installed executable without a usable runtime search path for a custom installation prefix;
- runtime failure because the dynamic loader could not locate the shared library.

This supersedes the earlier incorrect claim that shared libraries are simply not installed.

### Required MQTTSuite test

Test the actual suite rather than extrapolating from the minimal reproducer.

1. configure MQTTSuite using the documented workflow;
2. build;
3. install into a clean non-system prefix;
4. inspect installed binaries/libraries;
5. inspect RPATH/RUNPATH;
6. execute all five installed applications;
7. verify that execution does not accidentally depend on build-tree paths;
8. establish the supported deployment policy.

Possible policies include:

- loader-known installation locations;
- loader-cache update;
- install RPATH/RUNPATH;
- packaging policy;
- documented environment configuration.

### Important distinction

Changing:

`RUNTIME`

to:

`LIBRARY`

in an install rule is **not by itself a solution for runtime library discovery**.

Artifact destination semantics and runtime loader resolution are separate questions.

### Historical CMake semantics

The reviewers observed an unresolved discrepancy between:

- empirical behavior of a minimal test using older/newer CMake versions;
- interpretations of published historical artifact-kind documentation.

Do not base user documentation on a broad historical semantic claim.

Focus on the behavior of the actual supported MQTTSuite build/install matrix.

## P1 — Declared CMake minimum contradicts documented use of `cmake --install`

**Evidence:** `[DECL]`  
**Affected:** suite build/install  
**Disposition:** `FIX CODE` or `FIX DOC`  
**Publication blocker:** **yes**

The project declares:

`cmake_minimum_required(VERSION 3.14)`

The documented installation workflow uses:

`cmake --install`

which requires a newer CMake version than 3.14.

Choose a coherent contract:

- raise the required CMake version; or
- provide an installation method compatible with the declared minimum.

Do not publish both claims simultaneously.

## P2 — MQTTCli logs sensitive session values at debug level

**Evidence:** `[CODE]`  
**Affected:** MQTTCli  
**Disposition:** `FIX CODE` or explicit credential-redaction policy  
**Publication blocker:** not independently, but fix before publication if possible

The reviewed CLI implementation logs session values including:

- username;
- password

at debug level.

This should become part of the broader suite-wide credential audit.

Recommended product rule:

> Secrets are never logged as plaintext, regardless of log level.

This should be solved in implementation, not described as normal diagnostic behavior.

## P2 — MQTTStore projection failure lifecycle requires runtime verification

**Evidence:** `[CODE]` for load location; `[INFER]` for process/reconnect consequence  
**Affected:** MQTTStore  
**Disposition:** runtime verification followed by `FIX DOC` and possibly `FIX CODE`  
**Publication blocker:** **yes for the current failure-behavior claim**

Established from source:

`StoragePlan::fromFile(...)`

is invoked from:

`MQTTStore::SocketContextFactory::create(...)`

Therefore projection validation does not happen where the current README implies if it describes an earlier general application-startup validation phase.

Not established yet:

- whether the exception terminates the process;
- whether only connection/context creation fails;
- whether reconnect/retry causes repeated attempts;
- exact exit code;
- exact user-visible log sequence.

Test a malformed projection file and document the real lifecycle.

---

# 6. Track 2 — Documentation correctness issues

## D1 — Root/CLI Quick Start output is not literal application output

**Evidence:** `[CODE]`  
**Affected:** root README, MQTTCli README  
**Disposition:** `FIX DOC`  
**Publication blocker:** **yes**

The CLI formats received MQTT messages using its logging/output formatter and includes information such as:

- topic;
- QoS;
- retain state;
- duplicate state;
- formatted payload.

The Step 6 expected-output block is much simpler and can be mistaken for literal terminal output.

Either:

- use real captured output;
- or explicitly label simplified output as conceptual.

The first-success example must be observationally trustworthy.

## D2 — CLI publish/disconnect/reconnect lifecycle is described too vaguely

**Evidence:** `[CODE]`  
**Affected:** MQTTCli  
**Disposition:** `FIX DOC`  
**Publication blocker:** **yes where examples depend on lifecycle**

The CLI has specific behavior around:

- subscriptions;
- publish QoS;
- acknowledgement;
- disconnect;
- reconnect/retry.

The documentation should explain:

- when a publish-only invocation disconnects;
- how QoS acknowledgement affects lifetime;
- how subscriptions keep the client active;
- how outer reconnect configuration affects subsequent connection attempts.

Avoid vague wording such as “if it reconnects” when the configuration establishes retry/reconnect behavior.

## D3 — MQTTStore projection-validation timing is inaccurate

**Evidence:** `[CODE]` plus pending runtime verification  
**Affected:** MQTTStore  
**Disposition:** `FIX DOC` after runtime test  
**Publication blocker:** **yes**

Correct:

- when projection configuration is loaded;
- when validation errors appear;
- exact resulting process/connection behavior.

Do not overstate the consequence until tested.

## D4 — Integrator `#` documentation cannot be finalized before product decision

**Evidence:** `[CODE]`  
**Affected:** MQTTIntegrator/mapping reference  
**Disposition:** `DECISION REQUIRED`, then either `FIX CODE` or `FIX DOC`  
**Publication blocker:** **yes**

Current code and prose conflict.

Resolve semantics before final wording.

## D5 — Integrator mapping-source/precedence documentation must follow the inline-mapping decision

**Evidence:** `[CODE]`  
**Affected:** MQTTIntegrator  
**Disposition:** `DECISION REQUIRED`, then `FIX DOC`  
**Publication blocker:** **yes**

Do not document a questionable inline default as permanent product behavior until the decision is closed.

## D6 — Integrator administrative credential guidance must correspond to a real configuration path

**Evidence:** `[CODE]` / `[DECL]`  
**Affected:** MQTTIntegrator  
**Disposition:** likely `FIX CODE`, then `FIX DOC`  
**Publication blocker:** **yes**

Never instruct users to change configuration through a mechanism the application does not actually expose.

## D7 — Installation claims require actual installed-tree verification

**Evidence:** `[UNVERIFIED-RUNTIME]`  
**Affected:** root and application build/install sections  
**Disposition:** runtime test, then `FIX DOC`  
**Publication blocker:** **yes**

Do not state that installation creates directly runnable installed applications until this has been tested with the documented procedure.

## D8 — Broker trust/exposure documentation must be written after security/code decisions

**Evidence:** `[CODE]`  
**Affected:** MQTTBroker and future API reference  
**Disposition:** `FIX CODE` first, then `FIX DOC`  
**Publication blocker:** **yes**

Do not build permanent documentation around avoidable plaintext secret exposure.

After implementation changes, document the final:

- administration trust boundary;
- event trust boundary;
- authentication model;
- CORS behavior;
- supported external API contract.

---

# 7. Track 3 — Documentation completeness and architecture

The current documentation contains substantial material but does **not yet meet the target** that a technically competent reader can construct non-trivial MQTTSuite configurations without reading source.

## 7.1 Root README

### Preserve

The root README already has the correct narrative architecture.

Preserve:

- application-suite introduction;
- five-application chooser;
- first-success path;
- explanation of why five applications exist;
- representative combinations/workflows;
- concise relationship to SNode.C;
- links to application documentation.

### Expand

Add/deepen:

- common configuration mental model;
- configuration precedence;
- instance/subcommand hierarchy;
- enabling/disabling instances;
- configuration-file vs command-line interaction;
- effective-configuration inspection;
- writing/exporting configuration where supported;
- practical semantic logging;
- support/getting-help route;
- status/version/maintenance information;
- verified build/install behavior.

### Do not expand into

The root README should **not** become:

- a complete schema manual;
- full SNode.C CLI reference;
- API reference;
- implementation class reference.

Link to dedicated references instead.

## 7.2 Shared SNode.C/MQTTSuite configuration reference — new document required

**Disposition:** `ADD REFERENCE DOCUMENTATION`

This is one of the largest genuine gaps.

The shared reference should explain the SNode.C configuration system as MQTTSuite users encounter it.

Minimum subjects:

- configuration hierarchy;
- application/root command;
- instances;
- sections;
- nested sections;
- command-line values;
- configuration files;
- precedence;
- defaults vs explicitly active values;
- enabling/disabling instances;
- `--config-file`;
- writing/persisting configuration where supported;
- viewing effective configuration;
- configuration/command-line reconstruction modes;
- expanded help/introspection;
- retry/reconnect concepts;
- socket local/remote configuration model;
- TLS configuration model at a user-facing level;
- semantic logging:
  - level;
  - application/framework origin;
  - relevant scope/boundary;
  - component/instance-specific levels where supported;
  - output format where supported;
- supported service/daemon/user/group behavior where relevant.

The root README should teach the mental model and link here.

Application READMEs should explain their concrete trees and link here for common behavior.

## 7.3 MQTTBroker README

The current Broker draft contains useful material but does not yet fully document the application contract.

Required coverage:

- application purpose;
- direct listener families actually compiled/supported;
- plain/encrypted variants;
- IPv4/IPv6/Unix listeners where supported;
- WebSocket MQTT entry points;
- default ports where source-backed;
- session-store behavior;
- retained-message behavior;
- subscription behavior;
- dashboard;
- administration functions;
- event stream;
- final listener/admin trust model;
- Web asset configuration;
- operational logging;
- mapping/integration capability if intentionally public;
- troubleshooting/failure behavior.

### New Broker HTTP/event API reference

**Disposition:** `ADD REFERENCE DOCUMENTATION`

Because the Broker README encourages use of the HTTP/event interfaces, the external contract should be addressable somewhere.

Reference:

- routes;
- methods;
- request bodies;
- responses;
- event names;
- event payloads;
- initial replay;
- heartbeat behavior;
- `Last-Event-ID` behavior;
- CORS;
- authentication/trust assumptions;
- API compatibility/stability statement.

Details such as the current heartbeat interval or ignored event-resumption identifier belong here, not necessarily in the Broker README narrative.

## 7.4 MQTTIntegrator README

MQTTIntegrator requires the largest documentation expansion.

The application README should teach the mapping model progressively.

Required sequence:

1. what Integrator solves;
2. MQTT connection/session model;
3. how subscriptions are derived;
4. topic-tree matching;
5. matching/array ordering;
6. static mapping;
7. value/text mapping;
8. JSON mapping;
9. template input model;
10. mapped topic generation;
11. QoS behavior;
12. retain behavior;
13. multiple outputs/fan-out;
14. delay/suppression where implemented;
15. malformed/non-JSON input behavior;
16. plugins/callbacks;
17. validation;
18. live deploy/update;
19. history/rollback where implemented;
20. reconnect/resubscription consequences;
21. administration API lifecycle;
22. transport variants;
23. troubleshooting/logging.

The test is:

> Can a technically competent reader design a non-trivial mapping without opening `MqttMapper.cpp` or the schema?

The current answer is not yet yes.

### New Integrator mapping reference

**Disposition:** `ADD REFERENCE DOCUMENTATION`

This reference should own the exhaustive mapping grammar.

Cover:

- root structure;
- connection object;
- mapping object;
- `topic_level`;
- subscription;
- defaults;
- required/optional fields;
- allowed values;
- static mapping;
- value mapping;
- JSON mapping;
- template context;
- output topic;
- QoS;
- retain;
- array/fan-out behavior;
- delays;
- suppression;
- plugins;
- plugin callback contract at the appropriate level;
- matching order;
- wildcard semantics after the product decision;
- schema-declared but currently inactive fields;
- validation behavior;
- deploy/reload effects;
- reconnect implications.

The Integrator README should contain progressive examples and link here.

## 7.5 MQTTBridge README

MQTTBridge is currently the strongest of the five application README candidates.

Use it as a **quality benchmark**, not as a template.

Strengths already present:

- Bridge-vs-Integrator distinction;
- practical two-broker scenario;
- definition hierarchy;
- topic construction explanation;
- source exclusion/loop caveats;
- schema/runtime discrepancy honesty;
- live/admin configuration explanation.

Remaining work:

- final administration trust/security model;
- verify configuration defaults;
- verify all examples;
- concise troubleshooting;
- retain explicit schema/runtime discrepancies until implementation is reconciled.

Avoid moving excessive internal factory/class detail into the user narrative.

## 7.6 MQTTCli README

MQTTCli should serve as both:

- first-success companion;
- serious diagnostic utility.

Required coverage:

- available transport instances;
- why client instances are disabled/enabled;
- selecting a transport;
- remote/local settings;
- client ID;
- session-retention/clean-session behavior;
- keepalive;
- credentials;
- will;
- default QoS;
- subscription;
- publication;
- `##qos` topic suffix;
- retained publication;
- simultaneous subscribe/publish;
- real output formatting;
- JSON pretty printing;
- publish acknowledgement/disconnect lifecycle;
- reconnect/retry lifecycle;
- diagnostic scenarios;
- common failure examples.

Do not promote internal formatter details such as fallback terminal width into normal README prose unless they explain a meaningful user-visible constraint.

## 7.7 MQTTStore README

The Store draft is relatively strong but still needs a complete configuration/lifecycle contract.

Required coverage:

- purpose;
- MQTT client/session behavior;
- subscriptions;
- database connection;
- raw archival;
- raw-table auto-creation;
- raw table fields;
- payload classification;
- JSON/text/binary behavior;
- projection structure;
- projection matching;
- JSON Pointer extraction;
- topic-level extraction;
- literal values;
- required/missing fields;
- projection table requirements;
- identifier/table constraints;
- database privileges/bootstrap;
- write ordering;
- transaction/atomicity limits;
- malformed projection lifecycle;
- examples for:
  - raw archive;
  - typed projection;
  - optional/missing fields;
  - malformed data/configuration.

Implementation internals such as SQL escaping strategy belong in code/security review unless they materially constrain public behavior.

## 7.8 Developer/extensibility documentation

MQTTSuite is intentionally extensible. That deserves public documentation, but at secondary priority.

Developer-oriented material should explain:

- application architecture;
- socket/context factories;
- MQTT context/session specialization;
- mapping extension;
- plugin callback extension;
- schema-driven configuration;
- administration-router extension;
- SNode.C transport abstractions;
- how an existing application can act as a foundation for a specialized solution.

The root README should contain a concise **Extending MQTTSuite** section and link to this material.

Do not make it the primary front-page story.

---

# 8. Track 4 — Workflow/repository hygiene

## W1 — Duplicate application candidate trees

**Disposition:** `WORKFLOW CLEANUP`  
**Publication-content blocker:** no  
**Workflow blocker before further editing:** yes

A later repository operation created another set of application candidate paths without removing the originals.

Before further revision:

- designate exactly one canonical candidate location;
- remove/archive the duplicate;
- ensure all links/workflow instructions point to the canonical tree.

Do not allow two candidate copies to diverge.

## W2 — Preserve evidence boundaries after implementation changes

If code is changed in response to this review:

1. pin new MQTTSuite commit;
2. pin new SNode.C commit if foundation behavior changed;
3. update technical-facts/evidence documentation;
4. re-establish affected claims;
5. only then revise final README wording.

Do not silently reuse evidence from the previous implementation baseline.

## W3 — Keep corrections in workflow candidates until validation closes

Do not update the public README surfaces until:

- product decisions are closed;
- implementation fixes are pinned;
- runtime tests pass;
- examples are executed;
- independent review is complete.

---

# 9. Corrected documentation ownership/completeness matrix

Legend:

- **OWNED HERE** — authoritative in this document;
- **SUMMARY + LINK** — enough local explanation with link to authoritative detail;
- **COVERED ELSEWHERE** — intentionally delegated;
- **GENUINELY MISSING** — no adequate public owner exists yet;
- **N/A** — not applicable.

`PARTIAL` means the ownership is appropriate but the current content is incomplete.

| Capability | Root | Broker | Integrator | Bridge | CLI | Store | Authoritative owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| What MQTTSuite is / why useful | OWNED HERE | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | Root |
| Five-application chooser | OWNED HERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | Root |
| Build prerequisites | OWNED HERE — PARTIAL | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | Root |
| Install/runtime result | OWNED HERE — PARTIAL | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | Root |
| Shared SNode.C configuration | SUMMARY + LINK — PARTIAL | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | **GENUINELY MISSING shared reference** |
| Effective-config inspection | SUMMARY + LINK — PARTIAL | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | **GENUINELY MISSING shared reference** |
| Shared semantic logging | SUMMARY + LINK — PARTIAL | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | **GENUINELY MISSING shared reference** |
| Service/deployment semantics | SUMMARY + LINK — PARTIAL | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | Shared configuration/deployment reference |
| First successful MQTT flow | OWNED HERE — PARTIAL | SUMMARY + LINK | COVERED ELSEWHERE | COVERED ELSEWHERE | SUMMARY + LINK — PARTIAL | COVERED ELSEWHERE | Root + CLI |
| Broker transports/listeners | SUMMARY + LINK | OWNED HERE — PARTIAL | N/A | N/A | N/A | N/A | Broker |
| Broker dashboard/admin | SUMMARY + LINK | OWNED HERE — PARTIAL | N/A | N/A | N/A | N/A | Broker |
| Broker HTTP/event contract | SUMMARY + LINK | SUMMARY + LINK — PARTIAL | N/A | N/A | N/A | N/A | **GENUINELY MISSING API reference** |
| Integrator mapping concepts | SUMMARY + LINK | N/A | OWNED HERE — PARTIAL | N/A | N/A | N/A | Integrator |
| Exhaustive mapping grammar | COVERED ELSEWHERE | N/A | SUMMARY + LINK — PARTIAL | N/A | N/A | N/A | **GENUINELY MISSING mapping reference** |
| Integrator live deployment/reload | COVERED ELSEWHERE | N/A | OWNED HERE — PARTIAL | N/A | N/A | N/A | Integrator + mapping reference |
| Bridge topology/configuration | SUMMARY + LINK | N/A | N/A | OWNED HERE | N/A | N/A | Bridge |
| Bridge forwarding/prefix/filter semantics | SUMMARY + LINK | N/A | N/A | OWNED HERE | N/A | N/A | Bridge |
| CLI session/sub/pub syntax | SUMMARY + LINK | N/A | N/A | N/A | OWNED HERE — PARTIAL | N/A | CLI |
| CLI diagnostic lifecycle/output | SUMMARY + LINK | N/A | N/A | N/A | OWNED HERE — PARTIAL | N/A | CLI |
| Store raw archival | SUMMARY + LINK | N/A | N/A | N/A | N/A | OWNED HERE — PARTIAL | Store |
| Store projections | SUMMARY + LINK | N/A | N/A | N/A | N/A | OWNED HERE — PARTIAL | Store |
| Extensibility architecture | SUMMARY + LINK — PARTIAL | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | SUMMARY + LINK | Developer docs |
| Getting help | OWNED HERE — MISSING | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | Root |
| Version/status/maintenance | OWNED HERE — MISSING/PARTIAL | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | COVERED ELSEWHERE | Root |

The key principle:

> An application README is not incomplete merely because shared information is owned elsewhere.

It is incomplete when:

- no document owns the capability;
- or the application README lacks sufficient local context/navigation to use the shared material.

---

# 10. Product/code decisions required before README rewriting

Freeze explicit decisions for the following.

## Decision A — Broker secret model

Required end-state:

- passwords absent from public client-state/event JSON;
- passwords absent from logs;
- explicit redaction policy.

## Decision B — Broker administration trust model

Choose and implement/document:

- authenticated administration;
- deliberately trusted-local administration;
- another explicit protection model.

## Decision C — Integrator `#`

Choose intended matching semantics and align code + documentation.

## Decision D — Integrator inline/default mapping

Decide whether it is:

- removed;
- formalized as example/default;
- retained deliberately.

## Decision E — Integrator admin credentials

Provide a supported configuration mechanism or redesign the administration model.

## Decision F — installed-tree runtime policy

Define and test how installed executables locate MQTTSuite libraries.

## Decision G — minimum CMake version

Make source declarations and public commands consistent.

## Decision H — MQTTStore malformed-projection lifecycle

Execute and record actual behavior; decide whether that behavior is desirable.

---

# 11. Implementation backlog

Keep this separate from documentation work.

## Highest priority

1. Remove Broker password serialization from public/event client models.
2. Remove Broker plaintext password logging.
3. Define/implement Broker administration/event protection.
4. Audit plaintext credential logging across all applications.
5. Decide/fix Integrator `#` semantics.
6. Decide/remove/formalize Integrator inline mapping.
7. Add configurable Integrator administration credentials or redesign the interface.
8. Resolve installed-tree runtime library discovery.
9. Align minimum CMake version with supported build/install commands.

## Secondary

10. Verify/fix MQTTStore malformed-projection lifecycle if needed.
11. Treat input-validation gaps such as QoS validation as code-quality issues rather than documentation requirements.
12. Reconcile remaining schema/runtime discrepancies where appropriate.

After changes, pin a new implementation baseline.

---

# 12. Documentation backlog

## Root

1. Correct Quick Start behavior/output.
2. Deepen shared configuration model.
3. Add practical logging/effective-config guidance.
4. Document only verified installation behavior.
5. Add help/status/maintenance navigation.
6. Preserve application-suite chooser.
7. Keep extensibility secondary.

## Shared documentation

8. Add shared SNode.C/MQTTSuite configuration reference.

## Broker

9. Rewrite exposure/trust documentation after code fixes.
10. Complete listener/session/admin configuration.
11. Add Broker HTTP/event API reference.

## Integrator

12. Rebuild mapping explanation as a progressive teaching sequence.
13. Add exhaustive mapping reference.
14. Resolve/document wildcard semantics.
15. Resolve/document mapping source/precedence.
16. Explain deploy/reload/reconnect lifecycle.
17. Correct administration authentication/configuration.
18. Add progressive mapping examples.

## Bridge

19. Preserve existing strong conceptual structure.
20. Execute all examples.
21. Add concise trust/troubleshooting material.
22. Retain honest schema/runtime caveats where unresolved.

## CLI

23. Replace simplified literal-looking output.
24. Explain publish/subscription/disconnect/reconnect lifecycle.
25. Expand diagnostic scenarios.

## Store

26. Correct projection validation/failure behavior.
27. Complete raw/projection examples.
28. Clarify write ordering/atomicity/table requirements.

## Developer documentation

29. Add extension architecture/reference material outside the main application narrative.

---

# 13. Publication blockers

The following must be closed before publication.

1. Broker password serialization and information-level log disclosure.
2. Broker administration/event trust model.
3. Integrator `#` code/document contract mismatch.
4. Integrator inline/default mapping ambiguity.
5. Integrator administration credential contract.
6. CMake minimum-version contradiction.
7. Installed-tree runtime execution not validated.
8. Root/CLI first-success output/lifecycle inaccuracies.
9. MQTTStore projection failure behavior not runtime-verified.
10. Shared SNode.C configuration documentation is insufficient for the stated usability goal.
11. Integrator mapping documentation is insufficient for independent non-trivial solution design.
12. One canonical workflow candidate tree must be established before revision resumes.

These blockers **do not imply a structural rewrite of the README architecture**.

---

# 14. Non-blocking improvements

After publication blockers are closed:

- badges/status indicators where useful;
- navigation polish;
- additional transport examples where they teach a distinct concept;
- API/reference polish;
- accessibility/visual integration;
- minor schema/default clarifications;
- deeper developer-extension examples;
- prose/formatting cleanup.

Do not inflate the root README simply to make every completeness-matrix cell appear “complete.”

---

# 15. Recommended execution order

## Phase 1 — Freeze this handoff

Treat this document as the correction-phase source of truth.

Do **not** rewrite README prose yet.

## Phase 2 — Product/security decision pass

Resolve Decisions A–H.

For every decision record:

- intended public contract;
- implementation change;
- runtime test;
- documentation consequence.

## Phase 3 — Implementation corrections

Apply approved changes in:

`SNodeC/mqttsuite`

and only where necessary:

`SNodeC/snode.c`

Pin new commits.

## Phase 4 — Runtime verification

At minimum test:

- clean configure/build;
- clean custom-prefix install;
- execution of all five installed applications;
- installed shared-library resolution;
- Broker admin/event behavior;
- Broker credential/log redaction;
- Integrator mapping-file/default behavior;
- Integrator matcher cases including `+` and `#`;
- CLI first-success sequence;
- CLI publish/subscription/reconnect lifecycle;
- Store malformed projection;
- representative Bridge topology.

Record exact commands and observed results.

## Phase 5 — Refresh technical facts

Update the evidence/technical-facts material against the new pinned implementation.

Any claim changed by implementation corrections must be re-established.

## Phase 6 — Add missing reference surfaces

Before overloading the READMEs, add:

- shared configuration reference;
- Integrator mapping reference;
- Broker HTTP/event API reference;
- developer/extensibility reference as appropriate.

## Phase 7 — Revise existing README candidates

Revise:

- root README candidate;
- five application README candidates.

Do **not** redesign the application-suite narrative.

Use MQTTBridge as a quality benchmark, not a structural template.

## Phase 8 — Execute examples

Every command presented as executable must be run against the pinned implementation.

Every expected-output block must be either:

- real output;
- or explicitly labelled conceptual.

## Phase 9 — GitHub README quality review

Verify that the documentation system clearly answers:

- what the project does;
- why it is useful;
- how to get started;
- how to use it;
- where to get deeper configuration/reference information;
- where to get help.

Long reference material should remain outside the root README.

## Phase 10 — Independent final review

Repeat a fresh source-driven audit for:

- correctness;
- feature completeness;
- configuration completeness;
- example validity;
- application-suite framing;
- GitHub README alignment;
- operational/security boundaries.

Only then proceed to publication.

---

# 16. Directive for the next execution chat

The next chat must **not begin by rewriting the Step 6 READMEs**.

Its first task is to close the product/security/code decision register and establish a new verified implementation baseline.

The current README architecture is worth preserving.

The target is:

**Complete, source-aligned, application-oriented GitHub documentation that teaches readers how to understand, run, configure, combine, operate and extend the five MQTTSuite applications, while moving exhaustive configuration/API/developer detail into clearly linked reference documentation.**

The application suite remains the primary story.

Extensibility remains the secondary story.

Source code establishes current behavior.

Questionable current behavior must be fixed or explicitly accepted before it becomes the documented public contract.
