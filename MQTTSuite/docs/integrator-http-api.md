# MQTTIntegrator HTTP administration API

MQTTIntegrator exposes an operator-facing HTTP administration interface for its mapping configuration. This reference documents the current external contract implemented by [`lib/MappingAdminRouter.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/MappingAdminRouter.cpp), [`lib/MappingAdminRouter.h`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/MappingAdminRouter.h), and [`mqttintegrator/mqttintegrator.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttintegrator/mqttintegrator.cpp) at `SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`.

The API manages the same mapping model described in the [Integrator mapping reference](integrator-mapping.md). It is a configuration/operations interface, not an MQTT data-plane API.

## Listener and trust boundary

MQTTIntegrator creates two IPv4 administration listeners around the same router:

| Instance | Transport | Source default |
| --- | --- | ---: |
| `in-http` | HTTP | `8085` |
| `in-https` | HTTPS/TLS | `8086` |

Both listeners use the same route tree. The TLS listener protects transport when configured correctly; it does not change the application authorization model.

The router applies:

1. JSON middleware;
2. HTTP Basic Authentication.

Current `AdminOptions` defaults are hard-coded in source:

```text
username: admin
password: admin
realm:    mqttsuite-admin
```

`mqttintegrator.cpp` constructs the router with those defaults and does not currently wire them to an MQTTSuite/SNode.C configuration option. Treat `admin/admin` as a known development credential, not as an adequate remote-management policy.

No application-specific CORS headers are emitted by `MappingAdminRouter.cpp` in the reviewed source. Do not infer from that fact that the interface is safe to expose broadly; the active mapping and its history can contain MQTT credentials and operational configuration.

Practical deployment controls include binding the listener to a trusted interface, firewalling it, or placing it behind an authenticated reverse proxy that supplies the deployment's real access-control policy.

> **Figure placeholder — Integrator administration trust boundary.** Show the MQTT data-plane client connection separately from the HTTP/HTTPS mapping administration listener, with Basic Auth and secret-bearing mapping state inside a trusted operator boundary.

## Route summary

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/schema` | return the mapping JSON schema |
| `GET` | `/config` | return the active mapping |
| `PATCH` | `/config` | apply JSON Patch to active mapping and save a draft |
| `POST` | `/config` | replace the draft with a supplied mapping object |
| `POST` | `/config/validate` | validate a supplied mapping without deploying it |
| `GET` | `/config/validateDraft` | validate the current draft file |
| `POST` | `/config/deploy` | deploy the current draft and reload subscriptions/connections |
| `GET` | `/config/history` | list retained deployed versions |
| `POST` | `/config/rollback` | restore a retained version and reload |
| `GET` | `/` | redirect to `/ui` |
| `GET` | `/ui` | redirect to `/ui/index.html` |
| `GET` | `*` | catch-all redirect to `/ui/index.html` |

All routes are behind the router's Basic Authentication middleware, including the UI redirects/fallback because the authentication middleware is installed before those routes.

## Authentication example

On a deliberately trusted local listener using the current source defaults:

```bash
curl -u admin:admin \
  http://127.0.0.1:8085/config
```

Because those credentials are globally known from the source, this example is for local evaluation only. The reviewed application has no built-in option that turns them into deployment-specific credentials.

## `GET /schema`

Returns the current MQTTSuite mapping schema with HTTP 200.

```bash
curl -u admin:admin \
  http://127.0.0.1:8085/schema
```

Use this endpoint when an administration client needs the exact schema compiled into the running Integrator rather than assuming a separately installed schema file is identical.

The response is the mapper schema representation returned by `MqttMapper::getSchema()`.

## `GET /config`

Returns the active in-memory mapping with HTTP 200:

```bash
curl -u admin:admin \
  http://127.0.0.1:8085/config
```

The returned object can contain the mapping `connection` block, including MQTT username/password fields. Treat this endpoint as **secret-bearing configuration read-back** in the current implementation.

If loading the active mapping representation throws, the route returns HTTP 500:

```json
{
  "error": "Failed to load configuration",
  "details": "..."
}
```

Do not expose or log those `details` fields blindly; implementation exceptions can contain deployment-specific information.

## `PATCH /config` — create/update a draft with JSON Patch

Request body is a JSON Patch document. The route:

1. parses the body as JSON;
2. obtains the current active mapping;
3. applies JSON Patch to that object;
4. writes the result as the draft beside the selected mapping file.

Example:

```bash
curl -u admin:admin \
  -X PATCH \
  -H 'Content-Type: application/json' \
  --data '[
    {"op":"replace","path":"/connection/keep_alive","value":30}
  ]' \
  http://127.0.0.1:8085/config
```

Success, HTTP 200:

```json
{
  "status": "patched",
  "path": "<active-mapping-file>"
}
```

The response `path` is the active mapping filename recorded by `ConfigApplication`; the draft itself is stored at the draft path derived by `JsonMappingReader`.

Error behavior:

| Status | Meaning |
| ---: | --- |
| `400` | request body could not be parsed as JSON |
| `422` | patch application or draft-save operation failed |

Representative 400 body:

```json
{
  "error": "Invalid JSON body",
  "details": "..."
}
```

Representative 422 body:

```json
{
  "error": "Patch application failed",
  "details": "..."
}
```

PATCH **does not deploy** the mapping. It creates/updates the draft lifecycle state.

## `POST /config` — replace the draft

Use this when the administration client wants to submit a complete mapping object instead of a JSON Patch.

```bash
curl -u admin:admin \
  -X POST \
  -H 'Content-Type: application/json' \
  --data-binary @mapping.json \
  http://127.0.0.1:8085/config
```

The request must parse as JSON and the top-level value must be an object.

Success, HTTP 200:

```json
{
  "status": "replaced",
  "path": "<active-mapping-file>"
}
```

Errors:

- HTTP 400 — malformed JSON body;
- HTTP 422 — top-level value is not an object;
- HTTP 422 — draft replacement/save failed.

Like PATCH, this writes a draft and does not activate it.

## `POST /config/validate` — validate an arbitrary mapping

This route validates the supplied JSON document against the mapper schema without changing active or draft state.

```bash
curl -u admin:admin \
  -X POST \
  -H 'Content-Type: application/json' \
  --data-binary @mapping.json \
  http://127.0.0.1:8085/config/validate
```

Valid document, HTTP 200:

```json
{"valid":true}
```

Schema-invalid document, HTTP 422:

```json
{
  "valid": false,
  "error": "Validation failed"
}
```

Parse/validation exception, HTTP 400:

```json
{
  "error": "Validation exception",
  "details": "..."
}
```

This endpoint is suitable for a draft editor's preflight check, but successful schema validation is not a runtime qualification of the mapping's intended data transformation.

## `GET /config/validateDraft`

Validates the current draft file derived from the active mapping filename.

```bash
curl -u admin:admin \
  http://127.0.0.1:8085/config/validateDraft
```

Possible results:

### Valid draft — HTTP 200

```json
{
  "valid": true,
  "path": "<draft-path>"
}
```

### No draft — HTTP 404

```json
{
  "valid": false,
  "error": "No draft configuration available",
  "path": "<draft-path>"
}
```

### Draft cannot be opened — HTTP 500

```json
{
  "valid": false,
  "error": "Cannot open draft configuration",
  "path": "<draft-path>"
}
```

### Schema-invalid draft — HTTP 422

```json
{
  "valid": false,
  "error": "Draft validation failed",
  "path": "<draft-path>"
}
```

Other validation/read exceptions use HTTP 400 with a `details` field.

## `POST /config/deploy`

Deploys the current draft.

```bash
curl -u admin:admin \
  -X POST \
  http://127.0.0.1:8085/config/deploy
```

The route calls the draft deployment helper, applies the resulting mapping to `MqttMapper`, persists the active mapping, then calls the Integrator reload callback.

Success, HTTP 200:

```json
{
  "status": "deploy-ack",
  "reload_mode": "...",
  "instances": 0,
  "subscribed": 0,
  "unsubscribed": 0
}
```

The counters/mode come from `MQTTIntegrator::updateSubscriptions(...)`.

Operationally there are two important classes of reload:

- mapping/subscription changes that can be handled through subscription deltas;
- mapping `connection` changes that require reconnect behavior.

A `deploy-ack` is an acknowledgement of the application's deploy/reload operation. It is not evidence that downstream MQTT consumers accepted every mapped publication or that a newly reconnected remote broker is healthy indefinitely.

Any exception in draft deploy, mapper validation/application, persistence, or reload handling returns HTTP 500:

```json
{
  "error": "Deploy failed",
  "details": "..."
}
```

## `GET /config/history`

Returns retained mapping versions as a JSON array:

```bash
curl -u admin:admin \
  http://127.0.0.1:8085/config/history
```

Each entry contains:

```json
{
  "id": "...",
  "comment": "...",
  "date": "..."
}
```

The history is local filesystem state managed by `JsonMappingReader`, not a separate remote configuration database.

Failure returns HTTP 500:

```json
{"error":"Failed to fetch history"}
```

The error response intentionally omits the caught exception details on this route.

## `POST /config/rollback`

Request body must contain `version_id`:

```bash
curl -u admin:admin \
  -X POST \
  -H 'Content-Type: application/json' \
  --data '{"version_id":"<id-from-history>"}' \
  http://127.0.0.1:8085/config/rollback
```

Missing `version_id` returns HTTP 400:

```json
{"error":"Missing version_id"}
```

On success, the selected version is restored, applied to the mapper, persisted as active configuration, and passed through the same reload callback used by deploy.

Success uses the same acknowledgement shape as deployment:

```json
{
  "status": "deploy-ack",
  "reload_mode": "...",
  "instances": 0,
  "subscribed": 0,
  "unsubscribed": 0
}
```

Rollback exceptions return HTTP 500 with `error: "Rollback failed"` and a `details` field.

## Draft/history lifecycle

The administration API is deliberately stateful:

```text
active mapping
   │
   ├─ PATCH /config ─┐
   └─ POST /config ──┴─► draft
                         │
                         ├─ validateDraft
                         └─ deploy
                              │
                              ├─ active mapping persisted
                              ├─ prior version retained by mapping-history logic
                              └─ subscriptions/reconnect reloaded

history ──► rollback ──► active mapping + reload
```

The mapping/history files can contain MQTT credentials. Protect their filesystem location as secret-bearing configuration state.

> **Figure placeholder — Mapping administration lifecycle.** Show active → draft via PATCH/POST → validate → deploy → history, plus rollback back to active and the reload branch to subscription delta or reconnect.

## UI routes

The router redirects:

```text
/   -> /ui
/ui -> /ui/index.html
*   -> /ui/index.html   # final GET catch-all
```

and mounts a static UI below `/ui`. The catch-all is registered after the explicit routes/static mount, so unmatched GET paths are redirected to the UI entry point.

At the reviewed revision, the static root is a hard-coded maintainer-local path:

```text
/home/voc/tmp/integrator/mqtt-integrator-ui/dist/mqtt-integrator-ui/browser
```

No portable installed MQTTIntegrator Web UI is established by this source tree. The JSON administration routes are the stable implementation evidence; `/ui` availability must not be treated as an installation promise.

## No SSE interface in MQTTIntegrator

The reviewed MQTTIntegrator route tree does **not** expose an SSE endpoint. Searches of the application source find no `/sse` route. Mapping administration responses are request/response HTTP operations.

Do not assume that Broker or Bridge SSE conventions also apply to Integrator. A client that needs to observe deploy/reload effects must use the deploy response plus MQTT/application observation rather than subscribing to an Integrator event stream.

## Security and secret handling

Current behavior has several deployment consequences:

- Basic Auth is present, but credentials default to the source-known `admin/admin` pair and are not configurable through the reviewed application surface;
- `GET /config` can return MQTT connection credentials stored in the mapping;
- mapping draft/history files can contain the same credentials;
- error `details` fields may expose implementation/deployment information;
- mapper validation/application diagnostics elsewhere in the current source can include credential-bearing mapping material;
- HTTPS protects transport only; it does not compensate for a globally known application credential.

Use a trusted network boundary and do not publish raw mapping/admin responses or verbose diagnostics from credential-bearing deployments.

## Response-format notes

The administration routes primarily use JSON responses. Clients should still check HTTP status independently from body content.

Do not assume one universal error schema: some routes include `details`, some include `valid` and `path`, while `/config/history` deliberately returns a shorter error object.

## What this API does not provide

This interface does not establish:

- MQTT message publishing/subscribing through HTTP;
- a general user/role/ACL administration system;
- configurable Integrator API credentials in current main;
- SSE/event-log streaming;
- distributed/transactional configuration storage;
- remote secret-vault semantics;
- proof that a schema-valid mapping produces the intended application-level result.

## Evidence boundary

**Source-verified:** route tree including the final GET catch-all, HTTP status/response shapes, Basic Auth defaults, listener defaults, draft/deploy/history/rollback workflow, lack of Integrator SSE, and current UI path.

**Not separately runtime-exercised by the landing-page qualification:** the full administration route matrix, authentication failure cases, deploy/rollback through a live broker reconnect, malformed-request fuzzing, or HTTPS certificate policy.

## Source anchors

- [Mapping administration router](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/MappingAdminRouter.cpp)
- [Administration options and reload result](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/MappingAdminRouter.h)
- [MQTTIntegrator listener/router construction](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttintegrator/mqttintegrator.cpp)
- [Shared mapping application configuration](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/ConfigApplication.cpp)
- [Mapping reference](integrator-mapping.md)