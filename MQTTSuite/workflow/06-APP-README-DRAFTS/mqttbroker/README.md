# MQTTBroker

MQTTBroker is the MQTTSuite MQTT 3.1.1 server application. It accepts MQTT client connections, delegates MQTT session/subscription/retained-message behavior to the SNode.C broker implementation, and adds MQTTSuite-specific observability, Web routes, and an optional in-process mapper.

Use MQTTBroker when you need the MQTT server role. Use [MQTTIntegrator](../mqttintegrator/README.md) when transformation should run as a separate client service, [MQTTBridge](../mqttbridge/README.md) when selected traffic should cross broker domains, [MQTTCli](../mqttcli/README.md) to inspect or verify traffic, and [MQTTStore](../mqttstore/README.md) to persist it.

The suite-level build, common configuration model, and first-success flow are documented in the [MQTTSuite README](../README.md). This README focuses on operating `mqttbroker`.

## Quick Start

The following command starts one isolated plain MQTT/IPv4 listener on `127.0.0.1:18885` and disables the other built-in listener/Web instances for a predictable local test:

```bash
mqttbroker \
  --config-file /dev/null \
  --log-level 4 \
  in-mqtt local --host 127.0.0.1 --port 18885 \
  in-mqtts --disabled \
  in6-mqtt --disabled \
  in6-mqtts --disabled \
  un-mqtt --disabled \
  un-mqtts --disabled \
  in-http --disabled \
  in-https --disabled \
  in6-http --disabled \
  in6-https --disabled \
  un-http --disabled \
  un-https --disabled
```

Subscribe from another terminal:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18885 \
    session --client-id broker-check-sub --qos 1 \
    sub --topic edge-lab/room-01/temperature
```

Publish from a third:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18885 \
    session --client-id broker-check-pub --qos 1 \
    pub --topic edge-lab/room-01/temperature \
        --message '{"value":21.7,"unit":"C"}'
```

A successful subscriber output identifies the topic, QoS 1, retain/dup flags, and JSON payload. Stop the one-shot publisher with `Ctrl-C` after the first successful result if its configured client path reconnects.

## How the Broker is assembled

MQTTBroker uses the server side of the same SNode.C composition model used throughout MQTTSuite.

Each enabled SNode.C server endpoint owns a `mqtt::mqttbroker::SocketContextFactory`. When a stream connection is established, the factory creates an MQTT socket context and injects the Broker application's MQTT behavior:

```cpp
return new iot::mqtt::SocketContext(
    socketConnection,
    new mqtt::mqttbroker::lib::Mqtt(
        socketConnection->getConnectionName(), broker, mqttMapper));
```

The shared `broker` object is the SNode.C MQTT server/broker model. MQTTSuite's `mqttbroker::lib::Mqtt` observes client connect/disconnect, publish, subscribe, and unsubscribe activity for its live model and can pass publishes through the shared MQTTSuite mapper when one is configured.

> **Figure placeholder — Listener families around one broker core.** Show direct MQTT and HTTP/WebSocket listener instances converging on one shared broker/session model, with per-connection MQTT contexts created by the Broker factory.

## Build and install result

`mqttbroker` is built by the repository's top-level CMake project. Do not treat `mqttbroker/` as a separate standalone build.

A complete suite installation places the executable in `${CMAKE_INSTALL_PREFIX}/bin` and copies the Broker's HTML/CSS/JavaScript resources to:

```text
${CMAKE_INSTALL_PREFIX}/var/www/mqttsuite/mqttbroker
```

The executable compiles the chosen SNode.C MQTT server, stream, HTTP/Express, TLS, and WebSocket components according to the Broker CMake options.

For the complete prerequisite and build command sequence, see [Build and install](../README.md#build-and-install).

## MQTT listener instances

When the corresponding build options are enabled, MQTTBroker contains these direct MQTT listener paths:

| Instance | Transport | Source default |
| --- | --- | --- |
| `in-mqtt` | plain IPv4 stream | port `1883` |
| `in-mqtts` | TLS over IPv4 stream | port `8883` |
| `in6-mqtt` | plain IPv6 stream | port `1883`, IPv6-only listener |
| `in6-mqtts` | TLS over IPv6 stream | port `8883`, IPv6-only listener |
| `un-mqtt` | plain Unix-domain stream | `/tmp/<application>-<instance>` unless reconfigured |
| `un-mqtts` | TLS over Unix-domain stream | `/tmp/<application>-<instance>` unless reconfigured |

Listener addresses are configured under the instance's `local` section. For example:

```bash
mqttbroker \
  in-mqtt local --host 0.0.0.0 --port 1883
```

For a Unix-domain listener, configure the path explicitly when it needs to be stable for another process:

```bash
mqttbroker \
  un-mqtt local --sun-path /run/mqttsuite/broker.sock
```

The enclosing directory must already exist and the process needs appropriate filesystem permissions.

### TLS listener variants

Choose the `*-mqtts` instance to use the SNode.C TLS stream stack. Certificate/private-key/trust settings belong to that instance's SNode.C TLS configuration section; inspect the expanded help for the exact options provided by the installed SNode.C version:

```bash
mqttbroker in-mqtts --help=expanded
```

TLS changes transport protection. It does not add MQTT authorization by itself.

## Broker state and sessions

The broker core is shared across the enabled Broker endpoints. That is why a client connected through one listener can participate in the same broker state as clients using another listener.

The SNode.C broker implementation owns MQTT concepts including:

- connected MQTT clients;
- subscriptions and subscription QoS;
- retained messages;
- MQTT session state;
- routing of publishes to matching subscribers.

MQTTSuite's `MqttModel` mirrors the live application-visible state needed by the dashboard and event stream.

### Persistent broker session store

The Broker application subcommand exposes `--mqtt-session-store`. Configure a file when broker session state should survive application restarts:

```bash
mqttbroker \
  broker --mqtt-session-store /var/lib/mqttsuite/mqttbroker-session.json \
  in-mqtt local --host 127.0.0.1 --port 1883
```

The parent directory and file permissions are operator-owned. Treat the session store as application state rather than a disposable log file.

### Persist the listener configuration

Once the explicit command is correct, write the SNode.C configuration and exit:

```bash
mqttbroker \
  --config-file /dev/null \
  in-mqtt local --host 127.0.0.1 --port 1883 \
  in-mqtts --disabled \
  in6-mqtt --disabled \
  in6-mqtts --disabled \
  un-mqtt --disabled \
  un-mqtts --disabled \
  in-http --disabled \
  in-https --disabled \
  in6-http --disabled \
  in6-https --disabled \
  un-http --disabled \
  un-https --disabled \
  --write-config ./mqttbroker.conf
```

Then start from the saved file:

```bash
mqttbroker --config-file ./mqttbroker.conf
```

## MQTT over WebSocket and the Web surface

MQTTBroker creates HTTP/HTTPS server instances in addition to direct MQTT listeners:

| Instance | Stack | Source default |
| --- | --- | --- |
| `in-http` | HTTP over IPv4 | `8080` |
| `in-https` | HTTPS over IPv4 | `8088` |
| `in6-http` | HTTP over IPv6 | `8080`, IPv6-only |
| `in6-https` | HTTPS over IPv6 | `8088`, IPv6-only |
| `un-http` | HTTP over Unix-domain stream | application/instance path |
| `un-https` | HTTPS over Unix-domain stream | application/instance path |

Those HTTP servers share one Express-style router that serves three purposes:

1. the Broker dashboard;
2. JSON/SSE operational routes;
3. MQTT WebSocket upgrades.

### MQTT WebSocket upgrade

A client requesting the WebSocket subprotocol `mqtt` can upgrade on:

```text
/ws
/mqtt
/
```

MQTTCli, MQTTIntegrator, MQTTBridge, and MQTTStore use `/ws` as their normal Broker-compatible target.

For a local WebSocket check:

```bash
mqttcli \
  --config-file /dev/null \
  in-wsmqtt --disabled=false \
    remote --host 127.0.0.1 --port 8080 \
    http --target /ws \
    session --client-id broker-ws-check --qos 1 \
    sub --topic edge-lab/#
```

This assumes the Broker's `in-http` instance is listening at that address/port.

### Dashboard

The installed Broker Web assets are served below `/clients`. The router redirects:

```text
/clients -> /clients/index.html
```

and serves the configured Broker HTML root beneath that path.

The dashboard receives live broker/model updates through server-sent events. The current source exposes SSE on:

```text
GET /api/mqtt/events
GET /sse
```

A request must accept `text/event-stream`; otherwise the router redirects toward the client view.

### JSON operations

The current router includes mutating POST endpoints for:

```text
POST /api/mqtt/disconnect
POST /api/mqtt/unsubscribe
POST /api/mqtt/release
POST /api/mqtt/subscribe
```

They let the Web surface disconnect a client, change a client's subscriptions, or release retained state. These are operational controls, not merely read-only status endpoints.

> **Figure placeholder — Dashboard, SSE, API, and MQTT WebSocket relationship.** Show the HTTP router serving static client pages, SSE live state, mutating JSON operations, and the `/ws` MQTT upgrade beside the direct MQTT listeners.

## Optional embedded mapping

MQTTBroker and MQTTIntegrator use the same shared `MqttMapper` implementation.

Configure the Broker application subcommand with a mapping file:

```bash
mqttbroker \
  broker --mqtt-mapping-file ./mapping.json \
  in-mqtt local --host 127.0.0.1 --port 1883
```

With a mapper present, each incoming publish is first observed as normal Broker traffic. The Broker then asks `MqttMapper` for zero or more mapped publishes. Immediate outputs are routed back through the same broker; delayed outputs are timer-queued and routed when due.

This is not a hidden child `mqttintegrator` process. It is the mapper library running inside MQTTBroker.

Use embedded mapping when one Broker process should own both brokerage and mapping for a compact deployment. Use standalone [MQTTIntegrator](../mqttintegrator/README.md) when the transformation lifecycle should be an independently deployable MQTT client service with its own mapping-admin API and reconnect/resubscribe behavior.

> **Figure placeholder — Optional embedded mapper.** Show normal broker routing with a side branch through `MqttMapper`, then mapped publishes re-entering the broker without a second process.

The full mapping format belongs to the [MQTTIntegrator README](../mqttintegrator/README.md#mapping-files).

## Representative deployments

### Plain local broker

Enable `in-mqtt`, bind to a loopback or selected interface, and disable listener families you do not need. Verify with two MQTTCli terminals before adding persistent sessions or mapping.

### Broker with dashboard and WebSocket clients

Enable `in-mqtt` and `in-http`. Native MQTT clients can use the direct listener, while browser/WebSocket clients use the same Broker through `/ws`; the dashboard uses `/clients` and SSE on the HTTP listener.

### Encrypted remote listener

Use `in-mqtts` and/or `in-https` with the SNode.C TLS options appropriate to your certificate/trust model. Keep plain listener instances disabled when the deployment does not require them.

### Same-host local IPC

Use `un-mqtt` with a stable socket path, then point a client application at the same path:

```bash
mqttcli \
  --config-file /dev/null \
  un-mqtt --disabled=false \
    remote --sun-path /run/mqttsuite/broker.sock \
    session --client-id local-inspector \
    sub --topic '#'
```

## Trust and exposure boundaries

A few distinctions matter when putting the Broker on a real network:

- The Broker accepts MQTT CONNECT username/password fields as protocol data, but the reviewed MQTTSuite Broker layer does not establish a general authentication/authorization backend from those fields.
- TLS protects an encrypted connection when configured correctly; it does not decide which MQTT client may publish/subscribe.
- The dashboard router and mutating `/api/mqtt/*` operations do not add an application-level authentication layer in the current source.
- The API middleware allows broad cross-origin request headers. Do not treat the Web surface as a harmless static dashboard.
- Session-store and mapping files may contain operational state or credentials. Protect them with filesystem permissions.
- Debug/trace output may expose connection or application data. Review logs before sharing them.

A practical pattern is to bind administrative HTTP access to a trusted interface or place it behind an access-controlled reverse proxy/firewall boundary while exposing only the MQTT listeners required by clients.

## Troubleshooting

### The listener does not start

Check:

- the selected instance is not disabled;
- the bind address belongs to the host;
- the port is not already in use;
- the Unix socket directory exists and is writable;
- TLS files/options are valid for encrypted instances.

Run the relevant expanded help to inspect the current SNode.C instance options:

```bash
mqttbroker in-mqtt --help=expanded
```

### A client connects but receives no messages

Confirm:

- publisher and subscriber are connected to the same Broker process/state;
- topic filter matches exactly or via valid MQTT wildcards;
- subscription QoS is accepted;
- the publisher is actually sending after CONNACK;
- retained-message expectations match the retain flag.

MQTTCli is the simplest way to separate broker routing from application-specific logic.

### The dashboard is blank or unavailable

Check:

- the intended HTTP/HTTPS instance is enabled;
- its bind address and port are reachable;
- `broker --html-root` points at the installed Broker Web directory if the default install-prefix path is not correct for the current deployment;
- `/clients/index.html` exists there;
- SSE requests to `/api/mqtt/events` or `/sse` remain connected.

### Mapping output is missing

First verify the original message reaches normal broker subscribers. Then validate the mapping file against [`../lib/mapping-schema.json`](../lib/mapping-schema.json) and use the standalone Integrator documentation to reason about topic-tree matching and mapping rules.

## Related documentation

- [MQTTSuite overview and build](../README.md)
- [MQTTIntegrator](../mqttintegrator/README.md)
- [MQTTBridge](../mqttbridge/README.md)
- [MQTTCli](../mqttcli/README.md)
- [MQTTStore](../mqttstore/README.md)
- [SNode.C](https://github.com/SNodeC/snode.c)

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```
