# MQTTSuite

**Five focused MQTT 3.1.1 applications for brokerage, integration, bridging,
inspection, and storage.**

MQTTSuite separates practical MQTT work into five independently runnable
applications. **MQTTBroker** accepts and distributes client traffic,
**MQTTIntegrator** subscribes, maps, and republishes, **MQTTBridge** forwards
selected traffic between broker connections, **MQTTCli** publishes, subscribes,
and inspects from a terminal, and **MQTTStore** persists MQTT messages to
MariaDB.

Use the applications independently or combine only the responsibilities a
deployment needs. They are separate executables, not modes or plugins of
MQTTBroker.

**C++20** · **MQTT 3.1.1** ·
[MIT OR GPL-3.0-or-later](https://github.com/SNodeC/mqttsuite/blob/master/LICENSE)

**[Run the first message](#run-the-first-message)** ·
**[Choose an application](#choose-the-application)** ·
**[Browse the source](https://github.com/SNodeC/mqttsuite)**

## Choose the application

Start with the responsibility you need. The applications share the MQTT domain,
but each owns a distinct operational boundary.

| Need | Application | Role |
| --- | --- | --- |
| Accept and distribute MQTT client traffic | **MQTTBroker** | MQTT 3.1.1 broker/server with a browser dashboard and optional shared in-process mapping |
| Transform topics or payloads and republish | **MQTTIntegrator** | Outbound MQTT client driven by mapping configuration |
| Forward selected traffic between brokers | **MQTTBridge** | Logical bridge made from outbound MQTT client connections |
| Publish, subscribe, and inspect | **MQTTCli** | Terminal MQTT client and the shortest evaluation path |
| Persist messages | **MQTTStore** | MQTT subscriber that stores raw envelopes first, with optional JSON projections to MariaDB |

A deployment does not need all five. Start with MQTTBroker and MQTTCli when you
want a local broker/client path, then add Integrator, Bridge, or Store only when
that responsibility is required.

## One MQTT message, five roles

A single publication is enough to show how the responsibilities differ. The
examples and visuals use one synthetic message throughout:

```text
Topic:   edge-lab/room-01/temperature
Payload: {"value":21.7,"unit":"C"}
```

MQTTBroker is the representative broker for the local domain. MQTTCli can
publish to it, subscribe from it, or inspect received publications.
MQTTIntegrator is a separate outbound MQTT client process: its subscriptions
come from mapping configuration, and mapped results are republished over its
connected MQTT client path. MQTTBridge owns outbound client connections to
configured brokers and forwards selected publications to other connected
members. MQTTStore subscribes and writes the original MQTT envelope before any
optional typed projection.

<picture>
  <source media="(max-width: 600px)" srcset="assets/application-message-flow-mobile.svg">
  <img src="assets/application-message-flow.svg" alt="MQTTSuite message-flow diagram showing MQTTBroker at the center, MQTTCli publishing, subscribing and inspecting, MQTTIntegrator mapping and republishing, MQTTBridge forwarding selected publications between configured brokers, and MQTTStore writing raw MQTT envelopes and optional JSON projections to MariaDB.">
</picture>

<sub>The diagram describes the implemented application roles around one MQTT 3.1.1 message; it is not an all-five-application runtime transcript.</sub>

The distinctions matter when composing a system. Mapping and forwarding are not
the same operation: MQTTIntegrator can change a topic or payload according to
mapping rules, while MQTTBridge forwards selected publications between its
connected broker members. Storage has a different boundary again: MQTTStore
keeps the raw MQTT envelope as the primary record and only attempts configured
typed projections when a payload is JSON.

## Run the first message

The shortest demonstrated path uses one MQTTBroker, one MQTTCli subscriber, and
one MQTTCli publisher on IPv4 loopback at QoS 1. The commands below assume a
Release build in `cmake-build-release` from current MQTTSuite source against a
compatible installed SNode.C package. They deliberately disable every broker
listener except the one used by this example.

Start the broker in terminal 1:

```sh
./cmake-build-release/mqttbroker/mqttbroker --config-file /dev/null --log-level 4 \
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

In terminal 2, subscribe to the synthetic temperature topic at QoS 1:

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-subscriber --qos 1 \
  sub --topic edge-lab/room-01/temperature
```

In terminal 3, publish the matching JSON payload:

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-publisher --qos 1 \
  pub --topic edge-lab/room-01/temperature \
      --message '{"value":21.7,"unit":"C"}'
```

The subscriber receives `edge-lab/room-01/temperature`, pretty-prints the JSON,
and reports `QoS: 1`, `Retain: false`, and `Dup: false`. The stable message
portion from the demonstrated run is:

```text
MQTT Publish ┬ edge-lab/room-01/temperature │
│                                                │ QoS: 1 │ Retain: false │ Dup: false
│                                                ├ {
│                                                │   "unit": "C",
│                                                │   "value": 21.7
│                                                └ }
```

The application prints the parsed JSON with `unit` before `value`; the input
command itself uses the compact `{"value":21.7,"unit":"C"}` form. The broker had
only `127.0.0.1:18885` listening for this run, so the result is deliberately
scoped to one local plain-IPv4 MQTT 3.1.1 broker/client exchange at QoS 1.

<picture>
  <source media="(max-width: 600px)" srcset="assets/first-success-terminal-mobile.png">
  <img src="assets/first-success-terminal.png" alt="Three real terminal views showing a local MQTTBroker, an MQTTCli publisher sending the edge-lab temperature JSON message at QoS 1, and an MQTTCli subscriber receiving the same topic and payload with Retain false and Dup false.">
</picture>

<sub>One local broker, one subscriber, one publisher, and the `edge-lab/room-01/temperature` message delivered at QoS 1.</sub>

The current publisher reconnects and republishes after its publish callback
closes the connection. For this one-message walkthrough, stop the publisher with
<kbd>Ctrl</kbd>+<kbd>C</kbd> immediately after the first subscriber result, then
stop the subscriber and broker the same way.

## Integrate, bridge, and store

The first-message path establishes the broker/client model. The three specialist
applications add transformation, broker-to-broker forwarding, or persistence
without turning those responsibilities into broker modes.

### MQTTIntegrator — map and republish

MQTTIntegrator connects as an MQTT client. Its mapping configuration determines
what it subscribes to; matching publications are mapped and republished through
that connected client path. Current mappings include static payload mappings,
scalar-value templates, and JSON templates. Configured outputs can change the
topic or payload and can select output QoS, retain behavior, and delay.

The same mapping engine can also run in process inside MQTTBroker. That is an
optional broker capability, not a hidden MQTTIntegrator child process, and the
standalone `mqttintegrator` remains its own application.

### MQTTBridge — forward selected traffic

MQTTBridge is not a broker. It owns outbound MQTT client connections to
configured brokers and groups those connections into logical bridges.
Subscriptions on each broker member select incoming traffic; configured
prefixes contribute to the forwarded topic, and a received publication is sent
to the other connected members rather than immediately back over the exact
source member.

That source-member rule is deliberately narrow. It is not a general promise
that arbitrary cyclic topologies cannot loop, and the optional SNode.C
origin-reflection mechanism used by MQTTSuite is non-standard. Topologies that
depend on loop suppression or third-party broker behavior need to be evaluated
explicitly.

### MQTTStore — raw envelope first

MQTTStore subscribes as an MQTT client and writes received publications to
MariaDB. The raw record preserves the source connection name, MQTT topic,
original payload, QoS, retain flag, DUP flag, and packet identifier. JSON
parsing does not replace that primary record.

When the payload is valid JSON and a configured projection matches, MQTTStore
can also insert typed values into an operator-defined projection table. It does
not establish automatic lifecycle management for those projection tables,
retention, backup, access policy, cross-insert atomicity, or database-retry
guarantees.

## See the broker state

MQTTBroker also ships a browser dashboard for its own live broker state. The
staged view below shows one synthetic connected client, its
`edge-lab/room-01/temperature` QoS 1 subscription, one retained publication for
the same topic and payload, and the corresponding activity entries.

<picture>
  <source media="(max-width: 600px)" srcset="assets/broker-web-ui-mobile.png">
  <img src="assets/broker-web-ui.png" alt="MQTTBroker browser dashboard showing the synthetic landing-subscriber client, its edge-lab temperature subscription, one retained publication, and associated broker activity.">
</picture>

<sub>MQTTBroker's real browser dashboard shows the broker state for the synthetic `edge-lab` scenario; it is a broker surface, not a suite-wide Web UI.</sub>

The dashboard is an operational surface, not an authorization boundary. The
broker's Web API includes state-changing operations, and the reviewed broker
router does not establish application-level authentication for them. Keep that
surface inside an explicit trusted or externally protected boundary; HTTPS/TLS
can protect transport but does not supply authorization by itself.

## Fit check

MQTTSuite exposes more source-level capability than the small first-message run
demonstrates. The distinctions below are the important ones to keep in mind
before choosing a deployment path.

| Area | Current boundary |
| --- | --- |
| **Protocol** | MQTTSuite targets MQTT 3.1.1. The first-message run demonstrates connect, subscribe, publish, and delivery at QoS 1. Source also contains QoS 2, retained-message, will, persistent-session, offline-queue, and wildcard paths, but this example does not establish those combinations or complete conformance. No MQTT 5 claim is made. |
| **Transports** | Current source contains IPv4, IPv6, and Unix-domain direct MQTT paths with plain/TLS variants, plus MQTT over WebSocket/WSS paths across the applications. The demonstrated path above is plain IPv4 MQTTBroker + MQTTCli only. This is not a tested transport matrix, and Bluetooth RFCOMM/L2CAP are not current MQTTSuite transports. |
| **Trust and credentials** | MQTT client CONNECT fields can carry username/password values, but the reviewed MQTTBroker path does not establish a credential-verification backend. MQTTBroker and MQTTBridge administration need an explicit trusted/external protection boundary. MQTTIntegrator's administration uses BasicAuth, with current defaults `admin` / `admin`. Configuration/history files and debug logs can contain credentials. |
| **Stored state** | MQTTStore persists raw payloads without automatic redaction. Projection-schema lifecycle, retention, backup, data classification, and database access policy remain operator responsibilities. |
| **Build and release** | Current source requires C++20 and a compatible SNode.C installation and contains build/install rules for all five applications. The latest public GitHub release is the historical `v1.0.1` source release; current master is substantially newer. No current-head binary release, container image, distribution repository, or broad package-manager publication is established. |
| **OpenWrt and platforms** | Public OpenWrt package source exists for an older four-application package set containing Broker, Integrator, Bridge, and CLI; `mqttsuite-full` does not include MQTTStore and does not represent current-master five-application state. The recorded current-source build/run environment is Debian x86-64 with GCC, not a broad OS/compiler/architecture support matrix. |

## Choose the next route

Use the first-message path to prove the broker/client core, then go directly to
the application that owns the next responsibility.

| If you want to… | Go here |
| --- | --- |
| Prove MQTTSuite locally with MQTTBroker + MQTTCli | [Run the first message](#run-the-first-message) |
| Operate or inspect MQTTBroker | [MQTTBroker source](https://github.com/SNodeC/mqttsuite/tree/master/mqttbroker) |
| Transform and republish MQTT traffic | [MQTTIntegrator source](https://github.com/SNodeC/mqttsuite/tree/master/mqttintegrator) |
| Forward traffic between broker connections | [MQTTBridge source](https://github.com/SNodeC/mqttsuite/tree/master/mqttbridge) |
| Publish, subscribe, or script MQTT interactions | [MQTTCli source](https://github.com/SNodeC/mqttsuite/tree/master/mqttcli) |
| Persist MQTT messages and inspect the storage model | [MQTTStore source](https://github.com/SNodeC/mqttsuite/tree/master/mqttstore) · [storage guide](https://github.com/SNodeC/mqttsuite/blob/master/docs/mqttstore-user-guide.md) |
| Inspect current implementation or report a defect | [Source](https://github.com/SNodeC/mqttsuite) · [Issues](https://github.com/SNodeC/mqttsuite/issues) · [Releases](https://github.com/SNodeC/mqttsuite/releases) |
| Understand the networking foundation | [SNode.C](https://github.com/SNodeC/snode.c) |

Start with MQTTBroker and MQTTCli. Add MQTTIntegrator for transformation,
MQTTBridge for forwarding, or MQTTStore for persistence only when that
responsibility belongs in the deployment.
