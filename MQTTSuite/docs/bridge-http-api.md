# MQTTBridge HTTP administration API and SSE

MQTTBridge exposes an operator-facing HTTP surface for reading and patching the active bridge definition, serving its configuration UI, and streaming bridge/broker lifecycle state through Server-Sent Events (SSE). This reference documents the current contract implemented by [`mqttbridge/mqttbridge.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/mqttbridge.cpp), [`mqttbridge/lib/BridgeStore.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/BridgeStore.cpp), and [`mqttbridge/lib/SSEDistributor.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/SSEDistributor.cpp) at `SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`.

The bridge-definition model itself is introduced in [Bridge definition and forwarding](bridge-definition.md). This page owns the HTTP/SSE contract.

## Listener and trust boundary

MQTTBridge creates two IPv4 administration listeners around the same router:

| Instance | Transport | Source default |
| --- | --- | ---: |
| `admin-legacy` | HTTP | `8081` |
| `admin-tls` | HTTPS/TLS | `8082` |

Both listeners enable retry and address reuse.

The current Bridge router uses JSON middleware but applies **no application-level authentication middleware**. A source search also finds no Bridge-specific `Access-Control-*` response policy.

This matters because `GET /api/bridge/config` returns the full active bridge definition, including broker MQTT username/password values when configured, while `PATCH /api/bridge/config` can alter connection targets, subscriptions, prefixes, credentials and session behavior and then restart the bridge clients.

Treat both admin listeners as trusted operational surfaces. HTTPS protects traffic in transit; it does not authorize the caller.

Recommended deployment controls include loopback/private binding, firewalling, or an authenticated reverse proxy in front of the Bridge administration listener.

> **Figure placeholder — Bridge administration trust boundary.** Show outbound MQTT broker connections as the data plane and the HTTP/HTTPS configuration + SSE surface as a separate trusted operator plane with no current application authentication.

## Route summary

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/api/bridge/config` | return active bridge-definition JSON |
| `PATCH` | `/api/bridge/config` | apply JSON Patch, validate/stage it, then restart/activate |
| `GET` | `/api/bridge/sse` | stream/replay bridge and broker lifecycle events |
| `GET` | `/config` | redirect to `/config/index.html` |
| static | `/config/*` | serve configured Bridge Web assets |
| fallback | `*` | redirect to `/config/index.html` |

There is no POST/PUT/DELETE configuration API in the reviewed route tree.

## `GET /api/bridge/config`

Returns the active normalized bridge-definition JSON.

```bash
curl http://127.0.0.1:8081/api/bridge/config
```

The active object is the same configuration held by `BridgeStore` and can include:

- logical bridge names/prefixes/disabled state;
- broker member network addresses;
- MQTT client IDs/session values;
- subscriptions and QoS;
- session-store paths;
- MQTT usernames and passwords;
- loop-prevention setting.

Because credentials are part of the bridge definition, this is **secret-bearing configuration read-back** in the current implementation.

The route directly sends `BridgeStore::getBridgesConfigJson().dump(4)` and does not define an application-specific error body for the normal read path.

## `PATCH /api/bridge/config`

The request body is interpreted as JSON Patch through the router's JSON middleware.

Example: disable one logical bridge whose array position is known:

```bash
curl \
  -X PATCH \
  -H 'Content-Type: application/json' \
  --data '[
    {"op":"replace","path":"/bridges/0/disabled","value":true}
  ]' \
  http://127.0.0.1:8081/api/bridge/config
```

The route accepts a patch only while no previous restart is in progress.

### Successful patch

`BridgeStore::patch(...)`:

1. applies the JSON Patch to the current active object;
2. validates the staged result against the bridge schema;
3. applies schema defaults to the staged object.

If that succeeds, the route returns:

```json
{"success":true,"message":"Bridge config patch applied"}
```

The application then begins closing the current bridge connections. If no active flow controller needs asynchronous teardown, activation/restart happens immediately; otherwise the staged configuration is activated when the remaining flows complete.

A successful HTTP response therefore means the patch was accepted/staged and restart processing began. It does **not** mean every new broker member is already connected when the HTTP response reaches the caller. Use the SSE lifecycle stream to observe the restart.

### Patch/validation failure — HTTP 404

If `BridgeStore::patch(...)` fails:

```json
{"success":false,"message":"Bridge config patch failed to applie"}
```

The spelling above is the literal current response text.

The 404 status is the current implementation contract even though the failure is validation/patch-related rather than resource absence.

### Restart already in progress — HTTP 409

```json
{
  "success": false,
  "message": "Bridge is in restarting state. Patch not applied"
}
```

This protects the single staged/restart lifecycle from overlapping API mutations.

### JSON attribute/type failure — HTTP 400

The JSON middleware attribute error callback returns plain text:

```text
Attribute type not found: <key>
```

Clients must therefore not assume every Bridge API error body is JSON.

## What activation changes

`BridgeStore::activateStaged()` replaces the in-memory active bridge map, writes the normalized staged JSON back to the configured `--definition` file, reconstructs logical bridge/member objects, and then the application starts the new outbound clients.

This means the API is not merely an in-memory control surface: a successful staged activation **persists** the changed definition to disk.

The definition file can contain credentials and should be protected with appropriate ownership/permissions.

## Debug-log sensitivity during patching

Current `BridgeStore::patch(...)` debug diagnostics can log the active configuration or supplied patch when validation/patching fails. `mqttbridge.cpp` also logs broker username/password values at debug level during client creation.

Do not collect or publish verbose Bridge logs from credential-bearing deployments without reviewing/redacting them.

## Configuration UI routes

The router redirects:

```text
/config -> /config/index.html
```

and serves `/config/*` from the directory configured by:

```text
--html-dir <directory>
```

The repository installs Bridge Web assets below the selected install prefix, but the reviewed runtime does not automatically establish that installed location as an application default. Supply `--html-dir` explicitly when using the shipped UI.

The catch-all route redirects unmatched requests to `/config/index.html`.

## SSE: `GET /api/bridge/sse`

A request is treated as SSE when its `Accept` header contains `text/event-stream`.

```bash
curl -N \
  -H 'Accept: text/event-stream' \
  http://127.0.0.1:8081/api/bridge/sse
```

For an SSE request, the route sets:

```text
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive
```

and registers the response with `SSEDistributor`.

If the request does not accept `text/event-stream`, the current route redirects to `/clients`. MQTTBridge does not define a dedicated `/clients` page; the later catch-all routing ultimately redirects unmatched paths toward `/config/index.html`.

## SSE wire format

Each event uses ordinary SSE fields:

```text
event:<event-name>
id:<numeric-id>
data:<json-object>

```

The JSON `data` object always includes an `at` timestamp string for lifecycle events. Bridge- and broker-specific events add identifiers such as `name`, `bridge`, and `instance`.

Example shape:

```text
event:broker_connected
id:17
data:{"at":"2026-08-31 18:00:00 UTC","bridge":"lab","instance":"lab+broker-a"}

```

The timestamp format is generated in UTC as:

```text
YYYY-MM-DD HH:MM:SS UTC
```

## SSE event vocabulary

### Suite-of-bridges lifecycle

| Event | Payload fields | Meaning |
| --- | --- | --- |
| `bridges_starting` | `at` | a bridge start/restart sequence begins |
| `bridges_started` | `at` | current active bridge set reached the distributor's all-connected condition |
| `bridges_stopping` | `at` | bridge shutdown/restart teardown begins |
| `bridges_stopped` | `at` | bridge set stopped |

### Logical bridge lifecycle

| Event | Payload fields | Meaning |
| --- | --- | --- |
| `bridge_disabled` | `at`, `name` | configured logical bridge is disabled |
| `bridge_starting` | `at`, `name` | logical bridge startup begins |
| `bridge_started` | `at`, `name` | logical bridge reached its started state |
| `bridge_stopping` | `at`, `name` | logical bridge teardown begins |
| `bridge_stopped` | `at`, `name` | logical bridge stopped |

### Broker-member lifecycle

| Event | Payload fields | Meaning |
| --- | --- | --- |
| `broker_disabled` | `at`, `bridge`, `instance` | broker member is disabled |
| `broker_connecting` | `at`, `bridge`, `instance` | outbound MQTT connection is starting |
| `broker_connected` | `at`, `bridge`, `instance` | broker member connected |
| `broker_disconnecting` | `at`, `bridge`, `instance` | disconnect/teardown begins |
| `broker_disconnected` | `at`, `bridge`, `instance` | broker member disconnected |

The event names use underscores exactly as shown; they are not the Broker application's hyphenated event vocabulary.

## SSE replay behavior

`SSEDistributor` keeps an in-process `replayEvents` list.

When `bridgesStarting()` runs, that list is cleared. Every subsequent emitted lifecycle event is appended to it. When a new SSE receiver attaches, the distributor sends every event currently present in that list before the receiver begins observing future live events.

This is therefore a **current restart-cycle event replay**, not an unbounded durable event log.

A reconnecting observer can receive the sequence of events accumulated since the current `bridges_starting` boundary.

## `Last-Event-ID`

The HTTP route passes the incoming `Last-Event-ID` header to `SSEDistributor::addEventReceiver(...)`, but the current implementation marks that argument unused.

Consequences:

- event IDs are emitted;
- a client may send `Last-Event-ID` according to SSE conventions;
- the server does **not** filter replay based on that ID;
- the server replays the distributor's whole current `replayEvents` list instead.

Do not promise resumable “events after ID N” semantics at this revision.

## SSE heartbeat

Each attached event receiver owns a repeating timer that sends:

```text
:keep-alive

```

every **39 seconds**.

This keeps the stream active through intermediaries that tolerate SSE comment heartbeats. It is not an application-state event and has no event ID.

## SSE receiver lifecycle

When the HTTP socket disconnects, the distributor removes the corresponding receiver. Event responses are held through weak references, so disconnected clients do not remain permanent delivery targets.

The replay list itself remains in memory until the next `bridges_starting` call clears it or the process exits.

## Using SSE to observe a PATCH restart

A useful operator sequence is:

1. connect to `/api/bridge/sse`;
2. submit `PATCH /api/bridge/config`;
3. observe `bridges_stopping` / bridge/broker disconnect events;
4. observe `bridges_starting` / bridge/broker connect events;
5. wait for the expected connected/started state.

The HTTP PATCH acknowledgement alone is deliberately not the whole operational proof.

> **Figure placeholder — Bridge PATCH + SSE lifecycle.** Show JSON Patch acceptance → staged configuration → disconnect/close → activate/persist → restart clients, with SSE events spanning stopping, starting and connected states.

## Security and secret handling

Current Bridge administration behavior requires special care:

- no application authentication middleware protects the REST or SSE routes;
- `GET /api/bridge/config` can return MQTT passwords;
- PATCH can change credential-bearing bridge configuration;
- the definition file is overwritten with the activated configuration;
- current debug logging can print broker passwords and configuration material;
- SSE lifecycle events expose bridge/member topology names and operational state;
- HTTPS protects transport but does not authorize callers.

Do not expose this interface to an untrusted network without an external access-control boundary.

## CORS behavior

No Bridge-specific `Access-Control-*` header configuration is present in the reviewed source. This differs from MQTTBroker's current permissive API CORS behavior.

Do not assume the three MQTTSuite HTTP APIs share one CORS contract.

## Response-format notes

The current Bridge API mixes JSON and plain-text errors:

- successful GET/PATCH bodies are JSON text;
- patch failure/restart conflict bodies are JSON text;
- middleware attribute/type failure is plain text;
- SSE uses `text/event-stream`.

Automation should always check HTTP status and `Content-Type` rather than assuming one universal body schema.

## What this interface does not provide

This surface does not establish:

- user/role/ACL management;
- application-level authentication;
- arbitrary MQTT publish/subscribe through HTTP;
- POST/PUT replacement of the whole definition;
- durable SSE history;
- `Last-Event-ID` delta replay;
- transactional multi-node configuration;
- proof that an accepted patch resulted in every remote broker remaining healthy.

## Evidence boundary

**Source-verified:** REST route set, status/response cases, listener defaults, lack of application authentication/CORS policy, staged patch/restart/persistence behavior, SSE event vocabulary, replay semantics, ignored `Last-Event-ID`, and 39-second heartbeat.

**Not separately runtime-exercised by the landing-page qualification:** the Bridge REST/SSE route matrix, live multi-broker PATCH restart, long-running SSE reconnect, HTTPS certificate policy, or adversarial malformed-request testing.

## Source anchors

- [Bridge router, PATCH lifecycle and admin listeners](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/mqttbridge.cpp)
- [Bridge configuration validation/staging/persistence](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/BridgeStore.cpp)
- [Bridge SSE distributor](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/SSEDistributor.cpp)
- [Bridge application configuration](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/ConfigBridge.cpp)
- [Bridge definition and forwarding](bridge-definition.md)
