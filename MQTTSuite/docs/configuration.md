# MQTTSuite configuration reference

MQTTSuite applications inherit SNode.C's hierarchical configuration system and add their own MQTT- and application-specific sections. This page documents the operating model that matters to MQTTSuite users. For the framework-level design and complete SNode.C option surface, see the [SNode.C configuration reference](https://github.com/SNodeC/SNode.C-Landingpages/blob/main/SNode.C/docs/configuration.md).

**Evidence baseline:** [`SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/tree/52de5631245c6318bfa5b7cca700f0754014f34d) with [`SNodeC/snode.c@5d6453c21df4894083b445cce00b627e7794932a`](https://github.com/SNodeC/snode.c/tree/5d6453c21df4894083b445cce00b627e7794932a).

## Configuration hierarchy

The command line mirrors the configuration tree. A typical client command is:

```text
mqttcli
  in-mqtt
    remote --host 127.0.0.1 --port 1883
    session --client-id inspector --qos 1
    sub --topic sensors/#
```

Read this as:

1. `mqttcli` — application root;
2. `in-mqtt` — named connection instance;
3. `remote` — peer address for that instance;
4. `session` — MQTT CONNECT/session behavior;
5. `sub` — application action after the MQTT session is established.

Server applications use analogous `local` address sections. WebSocket clients add an HTTP section. MQTTStore adds `db` and nested `storage`; MQTTBroker and MQTTIntegrator extend the root with mapper-related options; MQTTBridge builds its outbound client instances from a separate bridge-definition document.

> **Figure placeholder — MQTTSuite configuration hierarchy.** Show application → named connection instance → address/transport/TLS → MQTT session → application-specific action, with the same hierarchy feeding command-line, config-file, and inspection output.

## Values and precedence

SNode.C supplies configurable values from three layers:

```text
API / compiled defaults
        < configuration file
        < command line
```

A command-line value therefore overrides the corresponding configuration-file value, and a configuration-file value overrides an API/default value. This precedence is implemented in SNode.C's configuration layer and applies to MQTTSuite connection and application options.

The `-c` / `--config-file` option accepts more than one file. When deliberately layering files with overlapping values, use `--show-config` to inspect the effective result rather than relying on an undocumented assumption about a particular multi-file merge pattern.

For isolated experiments, `--config-file /dev/null` is useful because it avoids inheriting ordinary persisted settings.

## Named instances

A connection instance is an independently configurable endpoint inside one process. Instance names are part of the command hierarchy and also become useful operational identifiers in logs and application state.

Typical MQTTSuite client instances, when their corresponding build features are enabled, include:

```text
in-mqtt       in-mqtts
in6-mqtt      in6-mqtts
un-mqtt       un-mqtts
in-wsmqtt     in-wsmqtts
in6-wsmqtt    in6-wsmqtts
un-wsmqtt     un-wsmqtts
```

MQTTCli and MQTTStore create their client instances disabled; enable the one you intend to use with `--disabled=false`. MQTTIntegrator configures reconnecting clients as part of its application startup. MQTTBridge differs: its connection instances are materialized from the bridge-definition document rather than primarily authored as ordinary command-line connection instances.

MQTTBroker exposes server instances for direct MQTT and HTTP/HTTPS listener roles. Common **server** defaults include direct IPv4 MQTT on `1883`, MQTT/TLS on `8883`, HTTP on `8080`, and HTTPS on `8088`; the exact available instances depend on build-time feature switches.

### Client-side remote-port defaults

Do not infer a client default from a server convention or from the `mqtts` suffix. In the current MQTTIntegrator, MQTTCli, and MQTTStore startup code, the source defaults are:

| Client instance family | Stack | Source default remote port |
| --- | --- | ---: |
| `in-mqtt`, `in6-mqtt` | direct MQTT over plain stream | `1883` |
| `in-mqtts`, `in6-mqtts` | direct MQTT over TLS stream | **`1883`** |
| `in-wsmqtt`, `in6-wsmqtt` | MQTT over WebSocket | `8080` |
| `in-wsmqtts`, `in6-wsmqtts` | MQTT over secure WebSocket | `8088` |

The non-obvious point is the TLS-client default: **`in-mqtts` and `in6-mqtts` default to remote port `1883`, not `8883`.** If the target broker listens for MQTT/TLS on `8883`, set `remote --port 8883` explicitly. Unix-domain client instances do not use a TCP port.

MQTTBridge members are different again: their host/port/path is supplied by each member's bridge-definition `network` object rather than by these ordinary client-instance defaults.

### HTTP/admin instance names are application-local

Instance names are not globally unique across different executables. In particular, Broker and Integrator both use names such as `in-http`, but those are separate application-local listeners with different roles and defaults:

| Application | Instance | Role | Source default |
| --- | --- | --- | ---: |
| MQTTBroker | `in-http` | dashboard/admin/SSE/WebSocket HTTP | `8080` |
| MQTTBroker | `in-https` | dashboard/admin/SSE/WebSocket HTTPS | `8088` |
| MQTTIntegrator | `in-http` | mapping administration HTTP | `8085` |
| MQTTIntegrator | `in-https` | mapping administration HTTPS | `8086` |
| MQTTBridge | `admin-legacy` | bridge administration HTTP/SSE | `8081` |
| MQTTBridge | `admin-tls` | bridge administration HTTPS/SSE | `8082` |

So `in-http` in a Broker command and `in-http` in an Integrator command do **not** refer to one shared/global endpoint. Always interpret an instance name in the context of the executable that owns it.

## Inspect before you run

The SNode.C command tree provides introspection on the root and nested subcommands:

```bash
mqttcli --help=expanded
mqttcli --show-config
mqttcli --command-line=standard
mqttcli --command-line=active
mqttcli --command-line=complete
mqttcli --command-line=required
```

Use them for different questions:

| Command | Best use |
| --- | --- |
| `--help=expanded` | discover the complete descendant command/section tree |
| `--show-config` | inspect effective configurable state |
| `--command-line=standard` | reconstruct non-default and required options |
| `--command-line=active` | reconstruct active options including effective values |
| `--command-line=complete` | inspect the complete option set including defaults |
| `--command-line=required` | isolate options that remain required |

These modes are particularly useful when a connection family has many nested TLS/HTTP/session settings or when a saved configuration is being combined with command-line overrides.

## Persist a known-good configuration

`-w` / `--write-config` writes configurable state and exits. A practical workflow is:

1. make an explicit command work;
2. inspect it with `--show-config` or `--command-line=active`;
3. persist it;
4. review the file, including credentials;
5. start the service from the saved configuration.

Example:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id inspector --qos 1 \
    sub --topic sensors/# \
  --write-config ./mqttcli.conf
```

Then:

```bash
mqttcli --config-file ./mqttcli.conf
```

Configuration files can contain MQTT, database, TLS, or other credentials. Treat them as secret-bearing operational files and set ownership/permissions accordingly.

## MQTT session sections

MQTTCli and MQTTStore expose explicit `session` sections with the same core MQTT concepts:

- client ID;
- default QoS (`0..2`);
- keepalive;
- persistent-session selection (`--retain-session`, which sets `clean_session=false`);
- will topic, message, QoS, and retain flag;
- username and password;
- local session-store path where the application exposes that option.

MQTTIntegrator obtains the analogous connection/session values from its mapping document. MQTTBridge stores them per broker member in its bridge definition.

MQTT username/password fields are CONNECT inputs. Current MQTTBroker source parses those fields but this documentation does not claim a credential-verification backend or broker-side authorization policy.

## Subscription QoS versus publish QoS

Keep the two meanings separate:

- **subscription QoS** asks the broker for a maximum delivery QoS for a topic filter;
- **publish QoS** is the QoS used for an outgoing PUBLISH.

MQTTCli and MQTTStore use a default session QoS and allow a per-topic override with the `##<qos>` suffix. For example:

```text
sensors/+/temperature##1
alerts/###2
```

The second value means MQTT filter `alerts/#` with requested subscription QoS 2. MQTTCli uses the same suffix convention on its publish topic to override publish QoS for that publication.

> **Figure placeholder — Subscription QoS versus publish QoS.** Show one incoming subscription filter with its requested/max delivery QoS on the left and one outgoing PUBLISH with its independently selected publish QoS on the right. Include MQTTIntegrator's `subscription.qos` versus mapped-output `qos`, and MQTTCli's session default plus `##<qos>` override, so readers can see that subscribe QoS never silently becomes publish QoS.

## Direct MQTT and MQTT over WebSocket

Direct MQTT client paths are built on SNode.C stream/TLS connections. WebSocket paths insert HTTP and a WebSocket upgrade before the MQTT `mqtt` subprotocol.

MQTTCli and MQTTStore expose an HTTP `--target` for WebSocket clients and default it to `/ws`. MQTTIntegrator and MQTTBridge currently request `/ws`. MQTTBroker accepts the MQTT WebSocket subprotocol on `/ws`, `/mqtt`, and `/`.

TLS protects the transport. It does not by itself add MQTT authorization or HTTP administration authorization.

## Retry and reconnect

SNode.C distinguishes retrying an initial/failed connection from reconnecting after an established connection is lost. MQTTSuite client applications enable retry/reconnect on their network clients.

This matters operationally:

- a subscriber can remain available across connection loss;
- MQTTIntegrator and MQTTBridge can re-establish configured broker connections;
- MQTTStore can reconnect to its MQTT source;
- MQTTCli's publisher path can reconnect after completing a nominally one-shot publish, so an interactive one-shot test should be stopped after the first verified result when that behavior is not desired.

Persistent MQTT session behavior is a separate concern from transport reconnect. Use a stable client ID, persistent-session configuration, and the application's session-store option where the workflow requires state across process restarts.

## TLS configuration

TLS options live in the selected SNode.C connection instance. Exact certificate, CA, verification, and socket settings depend on the chosen server/client stack; inspect them with:

```bash
<application> <instance> --help=expanded
```

Do not treat an `mqtts`, `https`, or `wsmqtts` instance name as proof that application authorization has been configured. TLS is one layer of the deployment trust model.

## Logging and diagnostics

Current SNode.C exposes both the legacy global logging controls and semantic filters used by MQTTSuite:

```text
--log-level <0..6|off|critical|error|warn|info|debug|trace>
--verbose-level <0..10>
--log-file <path>
--log-format <text|json>
--log-origin-level=origin=level
--log-boundary-level=boundary=level
--log-component-level=component=level
--log-instance-level=instance=level
--monochrom
--quiet
--enforce-log-file
```

Semantic threshold precedence is:

```text
instance > component > boundary > origin > global
```

`--log-origin-level`, `--log-boundary-level`, `--log-component-level`, and `--log-instance-level` are repeatable and also accept comma-separated `key=level` lists.

A useful troubleshooting shape is:

```bash
mqttcli \
  --log-level info \
  --log-instance-level=in-mqtt=debug \
  ...
```

Use verbose logging carefully. Current MQTTSuite source still contains secret-bearing debug paths, including plaintext password logging in MQTTCli and MQTTBridge, and Broker event/log representations that can contain a supplied MQTT password. Do not collect or publish verbose logs from credential-bearing deployments without reviewing/redacting them.

## Daemon and service-related options

SNode.C supplies root daemon/service controls, including daemonization, log-file handling, process ownership/user/group support, and related runtime paths. The exact options should be discovered from the executable's current `--help=expanded` output because they belong to SNode.C rather than an MQTTSuite-specific service manager.

OpenWrt packaging and init/service integration are separate packaging concerns. The presence of daemon options does not imply that every distribution/service manager is qualified by this documentation pass.

## MQTTSuite domain configuration files

Do not confuse SNode.C application configuration with the domain documents used by individual applications:

| Document | Application | Purpose |
| --- | --- | --- |
| mapping JSON | MQTTIntegrator; optional Broker mapper | subscribe/match/transform/republish behavior |
| bridge-definition JSON | MQTTBridge | logical bridges, broker members, subscriptions, prefixes and MQTT sessions |
| projection JSON | MQTTStore | optional extraction of topic/JSON values into typed MariaDB tables |

Those documents have separate schemas and lifecycles:

- [MQTTIntegrator mapping reference](integrator-mapping.md)
- [MQTTBridge definition reference](bridge-definition.md)
- [MQTTStore storage reference](store-storage.md)

## Evidence and limits

**Available in source:** hierarchical configuration, named instances, config files, command-line overrides, introspection, config writing, retry/reconnect, TLS/HTTP/WebSocket composition, semantic logging, and application-specific extension sections.

**Exercised by the landing-page qualification:** current-head SNode.C/MQTTSuite build and install plus the plain-IPv4 MQTTBroker + MQTTCli first-success path. The complete configuration/transport matrix was not exercised.

Do not infer from this reference that every address-family × TLS × WebSocket × application combination is equally qualified. Use the [capability and evidence boundaries](capabilities.md) and the application README for the scope that is actually established.

## Source anchors

- [SNode.C `SubCommand.cpp` — help/config/command reconstruction and multi-file config option](https://github.com/SNodeC/snode.c/blob/5d6453c21df4894083b445cce00b627e7794932a/src/utils/SubCommand.cpp)
- [SNode.C `Config.cpp` — root logging/configuration behavior](https://github.com/SNodeC/snode.c/blob/5d6453c21df4894083b445cce00b627e7794932a/src/utils/Config.cpp)
- [MQTTSuite `ConfigApplication.cpp` — mapper/session-store extension](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/ConfigApplication.cpp)
- [MQTTCli configuration sections](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttcli/lib/ConfigSections.cpp)
- [MQTTStore configuration sections](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/lib/ConfigSections.cpp)