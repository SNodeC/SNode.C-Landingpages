# MQTTSuite Product & Implementation Decisions

**Status:** Product/security decisions frozen; implementation correction required before README revision  
**Workflow role:** Post-review implementation handoff  
**Input:** `MQTTSuite/workflow/07-README-REVIEW-HANDOFF.md`  
**Important:** This artifact does **not** authorize README rewriting. The accepted application-suite-first documentation architecture remains unchanged.

---

## 1. Scope and evidence baseline

This pass resolves Decisions A–H from the reconciled README review handoff and prepares the implementation-correction phase.

The four tracks remain separate:

1. product/security/implementation;
2. documentation correctness;
3. documentation completeness/architecture;
4. workflow/repository hygiene.

No README architecture change is required by this pass. No workflow-tree cleanup is performed here.

### Observed repository baselines

- `SNodeC/SNode.C-Landingpages@4c91798b1b5ac2f7dc900124e829fd617d882da7` — starting documentation/workflow state for this decision pass.
- `SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d` — current MQTTSuite implementation head observed for this pass; unchanged from the Step 7 handoff baseline.
- `SNodeC/snode.c@5d6453c21df4894083b445cce00b627e7794932a` — current SNode.C implementation head observed for this pass; this advances the older Step 7 foundation baseline.

No implementation repository was modified in this decision pass. The next implementation phase must re-check heads before editing and pin the resulting implementation commits after changes.

### Evidence vocabulary

- `[CODE]` — directly established from executable source logic.
- `[DECL]` — established from a declaration, schema, CMake rule, or configuration declaration.
- `[INFER]` — architectural conclusion supported by source but not demonstrated end-to-end.
- `[UNVERIFIED-RUNTIME]` — requires actual execution/build/runtime evidence.

### Runtime-verification limitation in this pass

The available execution environment could inspect the repositories through GitHub but could not obtain a runnable checkout for local build/install qualification. The MQTTSuite GitHub workflow inspected in this pass is a README-TOC workflow rather than a build/install qualification workflow. Therefore Decisions F and H deliberately retain explicit runtime tests for the implementation phase rather than converting source inspection into runtime claims.

---

# 2. Frozen product/security principles

The following are product decisions, not README wording decisions.

1. **Secrets are write-only operational inputs.** Plaintext passwords or equivalent secrets must not appear in ordinary logs, public/event JSON, diagnostic exceptions containing full configuration objects, or read-back administration responses.
2. **Administrative and operational-observation HTTP surfaces are protected surfaces.** MQTTSuite must not rely on an undocumented assumption that a remotely reachable management/event endpoint is trusted merely because it is intended for operators.
3. **Shipped examples must not silently override user configuration.** Example mappings belong in example files/documentation, not unconditional production startup code.
4. **MQTT wildcard behavior should match MQTT semantics unless the product explicitly defines otherwise.** MQTTSuite has no architectural reason to invent a conflicting meaning for `#`.
5. **An installed suite should have a coherent, testable loader policy.** A clean custom-prefix installation must not accidentally depend on build-tree paths.
6. **Static invalid configuration should fail early and deterministically.** A malformed projection plan is configuration failure, not a condition that should be rediscovered inside a reconnect lifecycle.

---

# 3. Decision summary

| Decision | Resolution | Disposition | Publication state |
| --- | --- | --- | --- |
| A — Broker secret model | Remove password material from client/event/log/read-back surfaces; establish suite redaction rule | `FIX CODE` | Blocked until implemented/tested |
| B — Broker administration/event trust model | Authenticate management and operational event surfaces; same-origin CORS by default; no shipped known credential | `FIX CODE` | Blocked until implemented/tested |
| C — Integrator `#` | Implement MQTT multi-level wildcard semantics locally and validate legal placement | `FIX CODE` | Blocked until implemented/tested |
| D — Integrator inline/default mapping | Remove unconditional inline demo override; make supported configuration the mapping source | `FIX CODE` | Blocked until implemented/tested |
| E — Integrator admin credentials | Configure authentication through supported application/SNode.C configuration; remove `admin/admin` product default | `FIX CODE` | Blocked until implemented/tested |
| F — installed-tree runtime policy | Use a self-resolving install RUNPATH policy for suite artifacts and prove it in a clean prefix | `FIX CODE` + runtime verification | Blocked; `[UNVERIFIED-RUNTIME]` |
| G — minimum CMake version | Raise MQTTSuite requirement to at least CMake 3.18, matching required current SNode.C and supporting `cmake --install` | `FIX CODE` | Blocked until build matrix passes |
| H — malformed projection lifecycle | Validate/load projection configuration before MQTT connection startup and fail process startup clearly on invalid static configuration | `FIX CODE` + runtime verification | Blocked; current consequence `[UNVERIFIED-RUNTIME]` |

There are no remaining product-choice questions among A–H. Runtime evidence remains outstanding for F and for the exact pre-fix/current behavior relevant to H, but the desired public contracts are now decided.

---

# 4. Decision A — Broker secret model

## Current behavior

**Evidence:** `[CODE]`

`mqttbroker/lib/MqttModel.cpp` contains the client JSON serializer:

- `static void to_json(nlohmann::json&, const Mqtt*)`

The serialized object includes both:

- `username` / `usernameFlag`;
- `password` / `passwordFlag`.

`MqttModel::addEventReceiver(...)` replays connected client objects through the event stream. `MqttModel::connectClient(...)` and `disconnectClient(...)` use the broadcast `sendJsonEvent(...)` path. The broadcast overload writes the serialized JSON through `brokerLog().info()` before sending it to receivers.

Therefore the reviewed implementation exposes an MQTT password through two independent paths:

1. client/event JSON, including initial event-stream replay;
2. ordinary information-level logs for live connect/disconnect events.

## Intended public contract

Passwords are never part of the Broker's client-state model exposed outside the MQTT protocol transaction itself. A public/operational representation may expose whether a password was supplied, but never its value.

Suite-wide rule:

> Secret values must not be serialized into observational models, ordinary logs, validation messages containing complete secret-bearing configuration, or read-back administration payloads.

Redaction by replacing the value with a fixed marker is acceptable for narrowly scoped diagnostics only when the key itself is useful. Omission or a boolean `configured`/flag is preferable for public state.

## Required implementation changes

Primary files/symbols:

- `mqttbroker/lib/MqttModel.cpp`
  - `to_json(nlohmann::json&, const Mqtt*)`
  - `MqttModel::sendJsonEvent(...)`
  - replay/broadcast paths using the client serializer.
- `mqttbroker/lib/MqttModel.h` if the public model API must change.

Cross-cutting follow-up from the same product rule:

- `mqttcli/lib/Mqtt.cpp` currently logs plaintext `Password:` at debug level — remove it.
- `mqttbridge/lib/Mqtt.cpp` currently logs plaintext `Password:` at debug level — remove it.
- `lib/MqttMapper.cpp::setMapping(...)` currently includes the complete mapping JSON in validation exceptions; because the mapping contains connection credentials, replace this with non-secret-bearing diagnostics.
- `lib/MappingAdminRouter.cpp` read-back/config error paths must not make stored secrets retrievable through GET/error detail. Define write-only secret semantics for administration configuration.

The implementation phase must perform a repository-wide credential/logging/error audit rather than assuming the listed call sites are exhaustive.

## Required tests

1. Connect a client using a unique sentinel password.
2. Observe live `/api/mqtt/events` and legacy `/sse` client events; assert the sentinel and plaintext password field are absent.
3. Attach an event receiver after the client is already connected; assert replay contains no secret.
4. Capture Broker info/debug/trace output for connect/disconnect; assert sentinel absent at every level.
5. Exercise MQTTCli and MQTTBridge with sentinel credentials at their most verbose supported logging; assert sentinel absent.
6. Submit an invalid Integrator mapping containing a sentinel password; assert validation/API/log diagnostics do not echo it.
7. Read administration configuration; assert secrets are omitted/redacted/write-only.

## Documentation consequence

After implementation is pinned, Broker/API and shared security documentation may state that operational client state exposes credential presence but not secret values. Do not document the pre-fix leakage as a supported behavior.

---

# 5. Decision B — Broker administration and event trust model

## Current behavior

**Evidence:** `[CODE]`

`mqttbroker/mqttbroker.cpp` exposes mutating JSON routes such as:

- disconnect client;
- unsubscribe client;
- release retained message;
- subscribe client.

The reviewed route tree does not apply an application authentication layer to these operations.

The same router exposes:

- `/api/mqtt/events` as an unauthenticated event stream with `Access-Control-Allow-Origin: *`;
- legacy `/sse` as an unauthenticated event stream.

The event stream is not harmless public telemetry: it exposes connected-client and broker-operational state and is part of the same administrative dashboard domain.

## Intended public contract

**Decision:** Broker administration and operational event surfaces are authenticated surfaces.

- Mutating `/api/mqtt/*` administration routes require authentication.
- Operational SSE/client-state routes require the same protection class.
- The shipped product has no known reusable default credential such as `admin/admin`.
- CORS is same-origin by default. Do not emit wildcard `Access-Control-Allow-Origin: *` by default.
- If cross-origin administration is later required, allowed origins must be explicit configuration rather than an unconditional wildcard.
- MQTT protocol listeners and MQTT-over-WebSocket routes are separate product surfaces and must not accidentally inherit HTTP administration authentication.

Basic Authentication is an acceptable initial mechanism because SNode.C already provides it and MQTTSuite already uses it for the Integrator administration router. The important contract is explicit protection and configurable non-default credentials, not a specific long-term auth scheme.

## Required implementation changes

Primary file:

- `mqttbroker/mqttbroker.cpp`
  - JSON administration router construction;
  - `/api/mqtt/events`;
  - `/sse`;
  - dashboard/admin route scoping;
  - CORS header behavior.

Configuration support will likely touch:

- `lib/ConfigApplication.h`
- `lib/ConfigApplication.cpp`

or a Broker-specific configuration class if that yields cleaner ownership.

Do not place BasicAuthentication around the entire server router if that would protect MQTT WebSocket protocol routes unintentionally. Scope it to administration/dashboard/event resources.

## Required tests

1. No credentials -> `401` for every management mutation and operational event route.
2. Wrong credentials -> `401`.
3. Configured credentials -> mutation/event access succeeds.
4. Default startup does not accept `admin/admin` or another documented universal credential.
5. `/api/mqtt/events` does not emit wildcard CORS by default.
6. An explicitly configured allowed-origin policy, if implemented, is enforced exactly.
7. MQTT TCP/TLS/WebSocket protocol connection paths remain unaffected by HTTP admin authentication.
8. Dashboard behavior is tested according to whether static assets themselves are protected or only their APIs are protected; freeze that choice in the implementation artifact.

## Documentation consequence

After code is fixed, document the Broker administration/event trust boundary, authentication configuration, CORS default, and exposure guidance. Do not present the current unauthenticated surface as an intentional deployment model.

---

# 6. Decision C — MQTTIntegrator `#` semantics

## Current behavior

**Evidence:** `[CODE]`

`lib/MqttMapper.cpp::findMatchingTopicLevel(...)` treats a literal name, `+`, and `#` as candidate matches for the current topic level. However, when more topic levels remain, it only recurses into a nested `topic_level`; the `#` node is not returned simply because it represents the remaining subtree.

At the same time, `extractSubscription(...)` can emit a configured `#` into an MQTT subscription filter. The broker therefore applies MQTT wildcard semantics while the local post-receive mapper does not. This is an internal semantic contradiction, not a useful MQTTSuite-specific feature.

## Intended public contract

**Decision:** `#` has MQTT multi-level wildcard semantics in MQTTSuite mappings.

- `#` matches the remaining subtree as an MQTT topic filter does.
- Its legal placement follows MQTT filter rules: it is terminal and occupies an entire level.
- `+` remains a single-level wildcard.

## Required implementation changes

Primary files/symbols:

- `lib/MqttMapper.cpp`
  - `MqttMapper::findMatchingTopicLevel(...)`
  - `extractSubscription(...)` / `extractSubscriptions(...)` as needed for consistent validation/behavior.
- `lib/mapping-schema.json` and/or explicit semantic validation if the schema does not currently enforce legal wildcard placement.

Preserve deterministic behavior when literal, `+`, and `#` candidates coexist. If array order currently determines precedence, tests must make that contract explicit or the implementation should adopt a deliberate precedence rule before documentation.

## Required tests

At minimum:

- literal exact match;
- `+` one-level match and non-match across multiple levels;
- `#` matching the parent topic and deeper descendants according to MQTT semantics;
- multiple trailing levels under `#`;
- illegal non-terminal `#` rejected;
- representative competing literal/`+`/`#` definitions produce deterministic selection;
- extracted subscription and local mapper agree for the same mapping tree.

## Documentation consequence

The Integrator mapping reference can use normal MQTT terminology for `+` and `#` after these tests pass. The current contradictory behavior must not be documented as the contract.

---

# 7. Decision D — Integrator inline/default mapping

## Current behavior

**Evidence:** `[CODE]`

In `mqttintegrator/mqttintegrator.cpp::main(...)` the application first calls:

- `configMqttIntegrator->setMappingFile("mapping.json")`

and then unconditionally calls:

- `configMqttIntegrator->setMapping(...)`

with an inline demonstration mapping. The source comment explicitly states that this overrides the mapping loaded from the file.

`lib/ConfigApplication.cpp` already exposes `--mqtt-mapping-file` through the normal SNode.C configuration mechanism. The unconditional in-code mapping therefore defeats the intended user-selected mapping source.

## Intended public contract

**Decision:** the inline mapping is development/demo residue and must be removed from production startup.

Examples belong in maintained example mapping files and documentation. Runtime mapping selection belongs to the supported SNode.C/MQTTSuite configuration mechanism.

There must be no hidden fallback in-code transformation that silently changes user traffic.

The implementation phase should also remove the misleading hard-coded `mapping.json` production default unless an installed, well-defined default file is deliberately provided. Prefer one of these explicit states:

- a configured mapping file is required for a useful Integrator run; or
- no mapping means an explicit no-op/empty mapping state.

Do not silently substitute a demo mapping.

## Required implementation changes

- `mqttintegrator/mqttintegrator.cpp::main(...)` — remove the unconditional inline `setMapping(...)`; reconcile the `setMappingFile("mapping.json")` default.
- `lib/ConfigApplication.cpp` / `.h` — retain `--mqtt-mapping-file` as the supported source and make missing/empty behavior explicit.
- example mapping files as implementation/test fixtures only; do not make them hidden runtime defaults.

## Required tests

1. Supply mapping file A and prove A is effective.
2. Supply mapping file B and prove B is effective rather than an inline mapping.
3. Select the mapping through a SNode.C configuration file, not only command line, and prove the same result.
4. Start with no mapping selection and verify the decided explicit behavior; assert the old `value -> mapping/json` demonstration does not appear.
5. Admin deploy/persist/reload must continue to operate on the same selected mapping source.

## Documentation consequence

Later Integrator documentation must describe one real mapping-source/precedence model and link examples as examples. It must not teach an unconditional hidden default.

---

# 8. Decision E — Integrator administration credentials

## Current behavior

**Evidence:** `[CODE]` / `[DECL]`

`lib/MappingAdminRouter.h::AdminOptions` declares defaults equivalent to:

- user `admin`;
- password `admin`;
- realm `mqttsuite-admin`.

`mqttintegrator/mqttintegrator.cpp::main(...)` constructs the administration router with `AdminOptions{}`. `lib/MappingAdminRouter.cpp::makeMappingAdminRouter(...)` correctly applies SNode.C `BasicAuthentication`, but the application provides only the known default credentials.

## Intended public contract

**Decision:** administration credentials are supported application configuration and have no universal shipped secret.

- Username/password are supplied through the normal SNode.C configuration model.
- The password is treated as sensitive configuration and must not appear in effective-config dumps/logs/read-back APIs.
- If an administration listener is enabled, missing required authentication material must fail configuration or keep the administration listener disabled; it must not fall back to `admin/admin`.
- A realm may retain a harmless default.

## Required implementation changes

Primary files/symbols:

- `lib/MappingAdminRouter.h::AdminOptions` — remove known credential defaults.
- `lib/ConfigApplication.h` / `.cpp` or an Integrator-specific admin config section — add supported admin-auth configuration.
- `mqttintegrator/mqttintegrator.cpp::main(...)` — construct `AdminOptions` from configuration.
- SNode.C sensitive-option support if the current configuration API cannot prevent secret echoing. If foundation support is needed, make the smallest generic SNode.C change and pin a new SNode.C baseline.

Option names are deliberately not frozen in this decision artifact; the implementation phase should choose names consistent with existing SNode.C configuration conventions and record them in technical facts.

## Required tests

- no/wrong credentials -> `401`;
- configured credentials -> success;
- `admin/admin` has no special validity unless explicitly configured by the user;
- CLI/config-file configuration paths agree;
- effective-config/log output does not reveal the secret;
- GET/config/read-back surfaces do not reveal the secret;
- credential changes behave predictably across restart/reload according to the chosen configuration lifecycle.

## Documentation consequence

Only after implementation exists may the Integrator README instruct users how to configure administration authentication. Do not publish advice to “change admin/admin” without a real supported path.

---

# 9. Decision F — installed-tree runtime library policy

## Current evidence

**Evidence:** `[DECL]` + `[UNVERIFIED-RUNTIME]`

The actual MQTTSuite CMake tree builds shared application libraries, for example `mqtt-broker`, links installed executables against them, and installs executables/libraries into GNUInstallDirs locations. In the inspected Broker rules:

- `mqttbroker` is installed to `${CMAKE_INSTALL_BINDIR}`;
- `mqtt-broker` is a shared library installed under `${CMAKE_INSTALL_LIBDIR}`.

No explicit MQTTSuite install RPATH/RUNPATH policy was found in the inspected root/Broker CMake declarations.

This pass did **not** execute the actual installed tree, so it does not repeat the earlier minimal-reproducer result as if it proved MQTTSuite runtime behavior.

## Intended public contract

**Decision:** a normal MQTTSuite installation into a clean non-system prefix is self-resolving for MQTTSuite-owned shared libraries without:

- build-tree RPATHs;
- `LD_LIBRARY_PATH` as a required user step;
- `ldconfig`/global loader-cache modification merely to run from that prefix.

Use an install RUNPATH based on `$ORIGIN` (with paths derived correctly from GNUInstallDirs) for MQTTSuite executables/shared objects. Keep packaging free to override the policy where a distro/package manager supplies a system loader policy.

SNode.C dependency resolution must be tested in the same prefix scenario. If SNode.C itself is installed beside MQTTSuite and requires an additional loader-policy change, fix that at the correct ownership layer rather than hiding it in README shell setup.

## Required implementation changes

Audit every MQTTSuite executable/shared/plugin target, not only Broker:

- root and per-application `CMakeLists.txt`;
- `mqttbroker/lib/CMakeLists.txt`;
- Integrator/Bridge/CLI/Store shared-library targets;
- mapping/plugin targets where dynamic loading is involved.

Define coherent `INSTALL_RPATH`/RUNPATH behavior and ensure build-tree paths are not retained in installed artifacts.

Do not treat `RUNTIME` versus `LIBRARY` destination spelling as a substitute for loader resolution. Artifact installation and dynamic-loader search are separate concerns.

## Required runtime/build test

From clean source states pinned for the implementation phase:

1. install SNode.C into a fresh custom prefix;
2. configure/build MQTTSuite against only that prefix;
3. install MQTTSuite into the same fresh prefix;
4. inspect every installed executable and MQTTSuite shared object with `readelf -d` or equivalent;
5. assert RUNPATH/RPATH contains no build-tree path;
6. run `ldd`/equivalent and prove MQTTSuite + required SNode.C libraries resolve from the intended install tree;
7. with `LD_LIBRARY_PATH` unset and without loader-cache modification, execute all five installed applications at least through loader-complete `--help`/configuration startup;
8. run one minimal functional startup per application where prerequisites permit;
9. repeat under the packaging/system-prefix policy if that is a separately supported installation mode.

## Documentation consequence

The root/application installation sections may promise directly runnable installed applications only after this exact test is recorded. Until then the claim remains a publication blocker.

---

# 10. Decision G — minimum CMake version

## Current behavior/declarations

**Evidence:** `[DECL]`

`SNodeC/mqttsuite@52de563.../CMakeLists.txt` declares:

- `cmake_minimum_required(VERSION 3.14)`.

Several MQTTSuite subdirectories repeat the same floor.

The public workflow uses generator-neutral `cmake --install`, which is newer than CMake 3.14.

More importantly, current required foundation `SNodeC/snode.c@5d6453c.../CMakeLists.txt` declares:

- `cmake_minimum_required(VERSION 3.18)`.

Therefore a nominal MQTTSuite 3.14 floor is not a coherent supported end-to-end build floor for the required current SNode.C dependency.

## Intended public contract

**Decision:** MQTTSuite requires **CMake 3.18 or newer** at the current baseline.

This matches the actual current foundation requirement and supports the intended `cmake --install` workflow. There is no product value in retaining a lower declaration that cannot build the required dependency stack.

## Required implementation changes

- Raise the root MQTTSuite `cmake_minimum_required` to 3.18.
- Audit and align repeated per-directory `cmake_minimum_required(VERSION 3.14)` declarations so they do not advertise a contradictory floor.
- Keep `cmake --install` as the generator-neutral supported installation command.

If SNode.C raises its minimum again before implementation lands, use the higher effective dependency floor and re-pin it.

## Required tests

- configure SNode.C + MQTTSuite with CMake 3.18 in the supported build shape;
- build and install successfully;
- test with the current primary CMake version as well;
- ensure the documented configure/build/install commands use no feature requiring a higher version than the declared floor unless that higher floor is intentionally adopted.

## Documentation consequence

Later requirements text should state the verified effective CMake minimum once the build matrix passes. The current 3.14 claim must not survive publication.

---

# 11. Decision H — MQTTStore malformed-projection lifecycle

## Current behavior

**Evidence:** `[CODE]` for load point; `[UNVERIFIED-RUNTIME]` for process/retry consequence.

`mqttstore/SocketContextFactory.cpp::SocketContextFactory::create(...)` calls:

- `StoragePlan::fromFile(storageOptions.projectionFile)`

inside socket-context creation. On exception it logs `MQTTStore startup failed` and rethrows.

This proves projection loading/validation occurs during connection-context construction, not in an earlier application-wide configuration preflight.

Source inspection alone in this pass does not prove whether the rethrow currently terminates the process, only fails a connection attempt, or participates in retry/reconnect behavior.

## Intended public contract

**Decision:** malformed static projection configuration is a startup configuration error and must be detected before MQTT connection attempts begin.

For an enabled Store instance with an invalid configured projection file:

- fail startup/configuration deterministically;
- emit one clear non-secret diagnostic identifying the projection configuration problem;
- return a non-zero process/configuration failure status;
- do not enter a connection/retry loop that repeatedly reparses the same invalid static file.

Runtime message payload errors remain operational data errors and are a different lifecycle.

## Required implementation changes

Primary files/symbols:

- `mqttstore/SocketContextFactory.cpp::create(...)` — remove static projection-file parsing from per-connection context construction.
- `mqttstore/mqttstore.cpp::main(...)` / instance setup — preflight enabled Store configuration before starting connections.
- `mqttstore/lib/StoragePlan.h` / `.cpp` — support validated plan construction/injection as needed.
- `mqttstore/lib/ConfigSections.*` if per-instance ownership requires a preflight hook.

Pass the validated plan into the factory/context rather than reopening the same static configuration on every connection creation.

## Required runtime tests

1. missing required projection file;
2. malformed JSON;
3. schema-invalid projection;
4. valid empty/no-projection configuration where supported;
5. valid projection.

For invalid static configuration, assert:

- non-zero process/config failure;
- one clear diagnostic;
- no MQTT connection attempt;
- no retry/reconnect loop;
- no database connection attempt caused by that invalid instance.

Then restart with corrected configuration and prove normal startup/storage behavior.

## Documentation consequence

After implementation, MQTTStore documentation should state that projection configuration is validated during startup before MQTT operation and that invalid static configuration prevents startup. Do not document the current per-context load point as the intended contract.

---

# 12. Cross-cutting credential audit result

This pass confirmed more than the original Broker leak.

### Confirmed plaintext/secret-bearing paths

- `[CODE]` Broker client serializer includes MQTT password: `mqttbroker/lib/MqttModel.cpp`.
- `[CODE]` Broker broadcast event logger prints that serialized client object at info level: `mqttbroker/lib/MqttModel.cpp`.
- `[CODE]` MQTTCli constructor prints plaintext password at debug level: `mqttcli/lib/Mqtt.cpp`.
- `[CODE]` MQTTBridge constructor prints plaintext password at debug level: `mqttbridge/lib/Mqtt.cpp`.
- `[CODE]` Integrator mapping validation exception embeds complete mapping JSON, which can include connection password: `lib/MqttMapper.cpp::setMapping(...)`.
- `[CODE]` Integrator administration GET/config and error-detail paths can expose secret-bearing configuration unless read-back semantics are changed: `lib/MappingAdminRouter.cpp`.

### Checked contrasting behavior

- `[CODE]` MQTTStore's inspected MQTT constructor logs only whether a username is configured, not its password: `mqttstore/lib/Mqtt.cpp`.
- `[CODE]` MQTTStore's inspected MariaDB wrapper construction passes the DB password to the database layer but its MQTTSuite-level state logs shown in `mqttstore/lib/MariaDbStorage.cpp` do not print it.

These contrasting checks are not proof that every inherited SNode.C path is secret-safe. The implementation phase must run a full source/log/error audit across MQTTSuite and any touched SNode.C configuration/database code.

---

# 13. Revised publication blockers

## Implementation/security blockers

The following decisions are closed, but their implementation remains a publication blocker:

1. Broker/public model secret removal and suite-wide redaction policy — A.
2. Broker admin/event authentication and CORS default — B.
3. MQTT-standard Integrator `#` behavior — C.
4. Removal of hidden Integrator inline/default override — D.
5. Configurable, non-default Integrator administration credentials — E.
6. Clean installed-tree loader policy and actual installed-tree qualification — F.
7. CMake minimum aligned at 3.18 or the then-current higher SNode.C floor — G.
8. Fail-fast MQTTStore projection preflight — H.

## Runtime blockers

- F remains `[UNVERIFIED-RUNTIME]` until the actual SNode.C + MQTTSuite install tree is built, inspected, and executed.
- H's current pre-fix process/retry consequence remains `[UNVERIFIED-RUNTIME]`; the post-fix fail-fast contract must be proved by runtime test.

## Documentation blockers retained from Step 7

These are separate from implementation severity and remain for the later documentation phase:

- first-success/CLI literal output and lifecycle correctness;
- shared SNode.C/MQTTSuite configuration reference depth;
- complete Integrator mapping reference depth;
- Broker HTTP/event API reference after the trust model is implemented;
- MQTTStore operational/storage detail after lifecycle correction;
- final help/status/maintenance routes.

## Workflow hygiene retained separately

The duplicate application candidate trees identified as W1 in Step 7 remain workflow cleanup. They are **not** security defects and were intentionally not modified in this pass.

---

# 14. Implementation backlog — execution order

The next execution phase should modify implementation repositories, not READMEs.

1. **Introduce/establish secret-handling policy and tests.** Remove plaintext secret logging in CLI/Bridge; remove secret-bearing full-object diagnostics/read-back behavior.
2. **Fix Broker client-state serialization/logging.** Remove password from event/client JSON and prove replay/live/log safety.
3. **Protect Broker management/event surfaces.** Add configurable authentication, remove wildcard CORS default, scope protection so MQTT protocol WebSocket endpoints are unaffected.
4. **Fix Integrator wildcard semantics.** Implement/test MQTT `#` behavior and legal placement.
5. **Remove Integrator demo override.** Establish one explicit mapping-source lifecycle and test config-file selection.
6. **Implement Integrator admin credential configuration.** Remove `admin/admin`; make secret configuration non-echoing.
7. **Align CMake floor.** Raise MQTTSuite to the effective SNode.C floor (currently 3.18) throughout the tree.
8. **Implement install RUNPATH policy.** Cover all suite shared libraries, plugins, and executables; do not use environment-variable workarounds as the product default.
9. **Move MQTTStore projection validation to startup preflight.** Inject a validated plan into connection contexts.
10. **Run full build/install/runtime qualification.** Execute the F and H tests plus affected security/behavior tests on clean checkouts and a clean custom prefix.
11. **Pin implementation commits.** Record the new MQTTSuite SHA and, if foundation code changed, new SNode.C SHA. Update technical-facts evidence before README editing.

A single implementation change set may cover several adjacent items, but test evidence must remain attributable to each decision.

---

# 15. Documentation consequences — no rewriting in this stage

Once implementation corrections are merged and pinned:

- **Root README:** update only verified prerequisites/install behavior and shared security/configuration summaries.
- **MQTTBroker:** document redacted client state, authentication, event/admin trust boundary, CORS policy, and API contract.
- **MQTTIntegrator:** document MQTT wildcard semantics, one mapping-source/precedence model, real admin-auth configuration, and deploy/reload lifecycle.
- **MQTTBridge/MQTTCli:** do not describe plaintext credential logging; it is being removed as a defect.
- **MQTTStore:** document startup projection validation only after fail-fast behavior is verified.
- **Shared configuration reference:** explain secret handling without exposing values in examples/effective-config output.

The existing application-suite-first documentation architecture remains accepted. Extensibility remains secondary.

---

# 16. Next execution handoff

## Recommended chat

**1.8 — MQTTSuite — Implementation Corrections**

This should be a fresh implementation-focused execution session. It must read this artifact and the Step 7 handoff from the repository rather than relying on this chat.

### Distilled execution prompt

```text
We are continuing the canonical MQTTSuite README publication workflow.

This is:

1.8 — MQTTSuite — Implementation Corrections

Implementation repositories:
- SNodeC/mqttsuite
- SNodeC/snode.c (only if a generic foundation change is actually required)

Documentation/workflow repository:
- SNodeC/SNode.C-Landingpages

Start from current repository heads and read as authoritative:
- MQTTSuite/workflow/07-README-REVIEW-HANDOFF.md
- MQTTSuite/workflow/08-PRODUCT-IMPLEMENTATION-DECISIONS.md
- the repository governance/AGENTS material required by those repositories.

Do not rewrite any README.
Do not redesign documentation architecture.
Do not perform workflow-candidate cleanup in the implementation/security change set.

Implement the frozen Decisions A–H from 08-PRODUCT-IMPLEMENTATION-DECISIONS.md in execution order, including:
- remove Broker password serialization and all confirmed plaintext secret logging/error/read-back exposure;
- protect Broker administration and operational event surfaces with configurable authentication and safe default CORS behavior;
- implement MQTT-standard Integrator # semantics and tests;
- remove the unconditional Integrator inline/demo mapping override and establish one explicit mapping-source contract;
- replace Integrator admin/admin with supported non-echoing configuration;
- raise MQTTSuite's CMake floor to the effective SNode.C requirement (3.18 at the decision baseline, or higher if current SNode.C has advanced);
- implement a clean-prefix install RUNPATH policy for all MQTTSuite runtime artifacts;
- move MQTTStore projection parsing/validation to fail-fast startup preflight.

Run focused tests after each correction and then perform the full clean build/install/runtime qualification required by Decisions F and H. Use a clean non-system prefix, keep LD_LIBRARY_PATH unset for the installed-tree proof, inspect RUNPATH/RPATH and dynamic dependencies, and execute all five installed applications far enough to prove loader-complete startup.

Keep evidence classified as [CODE], [DECL], [INFER], and [UNVERIFIED-RUNTIME]. Do not claim a runtime result you did not execute.

Commit implementation changes to the appropriate implementation repository/repositories. Then update the landingpages workflow evidence with:
- exact new MQTTSuite/SNode.C SHAs;
- exact files/symbols changed per Decision A–H;
- tests and commands executed;
- runtime/install results;
- any remaining blocker with precise reason.

Do not edit the root or application READMEs yet.
```
