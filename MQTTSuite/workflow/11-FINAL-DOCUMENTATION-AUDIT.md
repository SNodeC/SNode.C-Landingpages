# MQTTSuite final documentation audit

**Audit date:** 31 August 2026  
**Landingpages audit input HEAD:** `24a1951493584a896986e30f45db6f288b656732`  
**MQTTSuite implementation baseline:** `6c0ff62c612694a6111ff971c446327938130cf0`  
**PR #22 implementation commit:** `d15f70a2818d291638c50aa2e2116a9e49ebd9e1`  
**Result:** PASS — no remaining text/documentation publication blocker found in the combined review register

## Scope

This audit rechecked the current canonical MQTTSuite reader-facing tree against the two independent review registers and the post-PR-#22 implementation state. It covered:

- root README;
- all five application READMEs;
- every file in `MQTTSuite/docs/`;
- current publication/visual workflow state;
- source-level contracts implicated by the review findings.

The audit distinguishes current source behavior from the older recorded runtime qualification. It does not convert source-reviewed behavior into runtime-exercised evidence.

## Blocker closure

### 1. Integrator mapping structure — PASS

`docs/integrator-mapping.md` now states and follows the schema relationship:

```text
topic_level
  └─ subscription
       ├─ qos
       └─ static | value | json
```

The representative skeleton, mapping-mode fragments, subscription examples, branch examples, and non-trivial fan-out example place mapping rules inside `subscription`.

### 2. SNode.C configuration link — PASS

`docs/configuration.md` no longer depends on `../../SNode.C/...`. The framework-level SNode.C configuration route is an absolute, commit-pinned public Landingpages URL and remains valid when the MQTTSuite docs are copied into `SNodeC/mqttsuite`.

### 3. MQTTBridge command hierarchy — PASS

Documented Bridge invocations scope application options under the required subcommand:

```text
mqttbridge ... bridge --definition ... [--html-dir ...]
```

The two-broker quick start, installed-Web-assets example, persisted-config example, and complete three-broker example follow this hierarchy. Documentation also states that `bridge --definition <file>` is required.

### 4. MQTTStore projection failure boundary — PASS

The Store README no longer claims that malformed projection configuration is guaranteed to terminate the process at initial startup. It locates loading/validation in `SocketContextFactory::create()` when an MQTT transport reaches context creation, and keeps the whole-process/retry/reconnect consequence `[UNVERIFIED-RUNTIME]`.

### 5. MQTTIntegrator administration credentials — PASS

The Integrator README states that current `admin/admin` Basic Auth defaults are fixed in the current wiring and that there is no supported MQTTSuite/SNode.C application configuration option to replace them. Deployment guidance uses trusted binding, firewall, reverse-proxy, and external access controls rather than inventing a built-in credential setting.

### 6. Stale MQTTStore user guide — PASS

The application README no longer routes operators to the older implementation-repository `docs/mqttstore-user-guide.md`. The canonical publication route is the reviewed Store README plus `docs/store-storage.md`. The old guide is explicitly non-canonical because it predates the current evidence boundaries/commands.

## Required-item closure

### Quick-start output fidelity — PASS

The root README no longer presents a reconstructed four-line block as observed MQTTCli output. It describes the real formatter shape and links the preserved raw subscriber terminal capture and provenance.

### Broker startup observability — PASS

The documented root and Broker quick starts use debug log level `5` where listener-state visibility is expected. The historical runtime-capture provenance retains its original executed log level rather than being rewritten.

### Client remote-port defaults — PASS

The shared configuration reference explicitly records:

```text
in-mqtt / in6-mqtt       1883
in-mqtts / in6-mqtts     1883
in-wsmqtt / in6-wsmqtt   8080
in-wsmqtts / in6-wsmqtts 8088
```

It warns that `mqtts` does not imply a default remote port of 8883.

### Application-local HTTP/admin names — PASS

The shared reference distinguishes Broker `in-http:8080`, Integrator `in-http:8085`, and Bridge `admin-legacy:8081` / `admin-tls:8082`, plus the corresponding encrypted listeners.

### Store auto-create default — PASS

The Store README states that `--auto-create-raw-table` defaults to `true`, gives explicit `true`/`false` forms, and requires `storage --auto-create-raw-table=false` for the DBA-created raw-table permission profile.

### Store MariaDB socket default — PASS

The Store README states the non-empty default `/run/mysqld/mysqld.sock` and quotes the source help contract that the socket “overrides host and port when set”, while retaining the appropriate underlying-client/effective-configuration caveat.

### MQTTCli publish `##<qos>` — PASS

The CLI README documents both subscription and publication overrides. A concrete publish example explains that `demo/value##2` is sent as MQTT topic `demo/value` at QoS 2.

### Deep-reference navigation — PASS

- Broker README → Broker HTTP/SSE reference.
- Integrator README → mapping, sibling example, HTTP API.
- Bridge README → definition routing page, three-broker example, HTTP/SSE reference.
- Store README → Store storage routing page.
- `docs/README.md` indexes every file in `MQTTSuite/docs/`.

### Bridge/Store reference ownership — PASS

`docs/README.md` explicitly labels `bridge-definition.md` and `store-storage.md` as routing pages rather than pretending they independently own the complete deep content.

### Integrator template context/suppression semantics — PASS

The mapping reference documents exact keys:

```text
message
topic
qos
retain
package_identifier
mapped_topic
```

and the retained-empty suppression carve-out: an empty retained publish is allowed through even when `""` is in `suppressions`, preserving retained-message deletion semantics.

### Integrator UI/fallback routing — PASS

The Integrator HTTP and mapping references agree on:

```text
/   -> /ui
/ui -> /ui/index.html
*   -> /ui/index.html  (final GET catch-all)
```

and distinguish those redirects from the non-portable maintainer-local static UI root.

### Version/release/dependency positioning — PASS

The root README distinguishes:

- CMake project version `1.0.1`;
- published GitHub release `v1.0.1` from 7 March 2025;
- newer current `master` source behavior;
- `nlohmann_json >= 3.7.0`;
- practical whole-suite CMake floor 3.18 because of current SNode.C.

## MQTTIntegrator wildcard audit — PASS

All obsolete one-level-`#` publication guidance is superseded. Current reader-facing documentation states:

- `+` matches exactly one topic level;
- terminal `#` matches zero or more remaining levels;
- `parent/#` can match `parent` when the parent has no own subscription mapping;
- sibling branches remain first-match in document order;
- specific literals should precede broader `+` / `#` fallbacks when they overlap.

The complete sibling-topic example and mapping reference agree with PR #22.

## HTTP/SSE audit — PASS

The dedicated references remain the strongest contract documents in the set:

- Broker: REST/admin routes, CORS, SSE snapshot/event vocabulary, ignored `Last-Event-ID`, 39-second keepalive, credential-sensitive client representation.
- Integrator: Basic-authenticated route matrix, exact status/error behavior, draft/deploy/history/rollback, no SSE route, UI fallback.
- Bridge: GET/PATCH config, persistence/restart semantics, SSE vocabulary, actual runtime emission status, replay list, ignored `Last-Event-ID`, 39-second heartbeat.

The Bridge reference continues to distinguish `bridges_stopped` as defined by the distributor but without a runtime call site in the reviewed source.

## Destination-relative source links — PASS by publication model

Application READMEs contain relative source links such as `../lib/mapping-schema.json`, `lib/bridge-schema.json`, and `lib/projection-schema.json`. These are intentionally **destination-relative** because the canonical tree is shaped for copying into `SNodeC/mqttsuite`, where those paths exist. They are not treated like the former `../../SNode.C/...` link, which would remain broken after publication and therefore had to become absolute.

## Visual audit — PASS

Direct inspection of the current reader-facing files finds **24 canonical figure placeholders**, down from 29 before consolidation:

```text
Root README                 5
MQTTBroker README           3
MQTTIntegrator README       3
MQTTBridge README           4
MQTTCli README              1
MQTTStore README            1
Configuration reference     2
Integrator mapping          0
Broker HTTP/SSE             1
Integrator HTTP             2
Bridge HTTP/SSE             2
                           --
Total                      24
```

Duplicate ownership is removed:

- mapping pipeline → MQTTIntegrator README;
- Integrator admin lifecycle → Integrator HTTP reference;
- Bridge PATCH/restart/SSE lifecycle → Bridge HTTP/SSE reference;
- root Store raw/projection split → root README;
- detailed Store projection extraction → Store README;
- redundant root deployment-topology figure omitted because adjacent text/ASCII already answers the question.

The missing subscription-QoS-versus-publish-QoS brief has been added to the shared configuration reference.

The canonical post-review visual scope is `10-VISUAL-PRODUCTION-PLAN.md`. Historical Step-5A V1/V2/V3 runtime/capture provenance remains in `05-VISUALS.md` and is not rewritten as new qualification.

## Audit-time corrections

The final audit itself found and corrected two small consistency issues:

1. `docs/configuration.md` still called the older `52de563...` runtime qualification a “current-head” build after `master` had advanced to `6c0ff62...`; the wording now separates current source verification from the recorded older runtime run.
2. The SNode.C configuration link was absolute but mutable (`main`); it is now commit-pinned as requested by the review.

## Final disposition

**Text/documentation completeness and consistency review: PASS.**

No remaining blocker from either supplied review register is present in the current canonical reader-facing documentation. Figure production may proceed from `10-VISUAL-PRODUCTION-PLAN.md`, subject to the existing rule that runtime-proof figures use real captures and that any future implementation change invalidating a documented contract must be reconciled before publication.
