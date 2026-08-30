# Architecture and extension points

[← SNode.C](../README.md) · [Configuration](configuration.md) ·
[Capability map](capabilities.md) ·
[API reference](https://snodec.github.io/snode.c-doc/html/index.html)

SNode.C separates five decisions that are commonly tangled together in a
network application: when work is ready, which address family identifies a
peer, whether an endpoint listens or connects, how an established stream is
managed, and which protocol behavior is attached to that stream.

The result is not an arbitrary “mix every layer with every other layer” system.
It is a typed composition model with explicit extension points. A concrete
application still has to select compatible components, build them, and qualify
the path it intends to deploy.

<picture>
  <source media="(max-width: 600px)" srcset="../assets/layer-architecture-mobile.svg">
  <img src="../assets/layer-architecture.svg" alt="SNode.C composition map showing the event runtime, address families, endpoint roles, connection modes, and application contexts">
</picture>

<sub>The stack separates application behavior from endpoint and connection mechanics; highlighted qualification boundaries remain part of the documentation.</sub>

## 1. Event runtime

`core::SNodeC::start()` enters the framework event loop. The loop delegates
descriptor readiness and timer publication to an `EventMultiplexer`, queues the
resulting events, and dispatches them to their receivers. Current source
contains select, poll, and epoll multiplexer implementations.

This is the shared runtime underneath clients, servers, timers, and stream
connections. Application contexts react to events; they do not run their own
accept or polling loop. That keeps protocol code focused, but it does not by
itself establish performance, fairness, or workload suitability. Those require
measurements and tests for the concrete build and traffic pattern.

Source anchors:

- [`EventLoop`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventLoop.h)
- [`EventMultiplexer`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventMultiplexer.h)
- [multiplexer implementations](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/multiplexer)

## 2. Address family and endpoint role

Address-family layers provide the concrete socket and address types. Current
source trees exist for IPv4, IPv6, Unix-domain, Bluetooth RFCOMM, and Bluetooth
L2CAP communication. Stream clients and servers are then composed above the
selected family:

- a `SocketServer` owns listener setup and accepts connections;
- a `SocketClient` owns connection attempts and client-side reconnect policy;
- both create a `SocketConnection` after the underlying operation succeeds.

The role affects configuration. A server requires a local listener endpoint and
learns remote addresses from accepted peers. A client requires a remote
destination and may optionally bind a local endpoint. The framework reflects
those differences in its configuration sections rather than forcing both roles
through an undifferentiated address object.

The source tree is broader than the launch qualification. The published echo
evidence covers IPv4, IPv6, and Unix-domain plain streams plus mutual TLS over
IPv4. RFCOMM and L2CAP remain source-verified paths requiring suitable hardware
and their own runtime qualification.

## 3. Connection layer

`SocketConnection` owns the established connection and the mechanics shared by
protocols: local and remote addresses, connection identity, reads and writes,
queue accounting, timeouts, shutdown, and the currently attached context.

Plain stream and OpenSSL-backed TLS variants provide different connection
mechanics below the same application-context boundary. TLS is therefore a
selected and configured connection mode, not an automatic property of a server
or client. Certificates, keys, trust anchors, verification policy, ciphers,
timeouts, and SNI still need deliberate configuration.

The connection exposes both ordinary send operations and `trySendToPeer`
results. Current configuration also includes maximum queued bytes and high/low
watermarks. Those mechanisms make queue policy visible to applications, but
their existence should not be turned into an unqualified backpressure or
resource-bound guarantee. A deployed protocol still needs an explicit policy
for full queues, slow peers, and shutdown.

Source anchors:

- [`SocketConnection`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.h)
- [`SocketContext`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.h)
- [`ConfigConnection`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config/ConfigConnection.h)

## 4. Factory and per-connection context

When a connection becomes usable, its `SocketContextFactory` creates the
application-facing `SocketContext`. The context is attached to exactly that
connection and receives lifecycle and data callbacks.

```text
configured client/server instance
              │
        accept or connect
              │
              ▼
       SocketConnection
              │
     SocketContextFactory
              │ creates
              ▼
        SocketContext
```

The echo application demonstrates the minimum useful implementation. Separate
server and client factories construct the same `EchoSocketContext` with a
different role. The client sends its initial greeting from `onConnected()`;
`onReceivedFromPeer()` reads and reflects data; `onDisconnected()` observes why
the context was detached.

The context owns protocol behavior, not the physical socket. It sends, reads,
sets timeouts, and closes through its `SocketConnection`. That boundary allows
the application model to remain stable while the endpoint family or connection
mode changes underneath it.

Source anchors:

- [`SocketContextFactory`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContextFactory.h)
- [echo context and factories](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.h)
- [echo callback implementation](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.cpp)

## 5. Context replacement and protocol upgrades

A `SocketConnection` can replace its attached context. The previous context is
detached with `DetachReason::ContextSwitch`; the next context attaches to the
same established connection. HTTP-to-WebSocket upgrade is the clearest example.

<picture>
  <source media="(max-width: 600px)" srcset="../assets/http-websocket-context-switch-mobile.svg">
  <img src="../assets/http-websocket-context-switch.svg" alt="HTTP-to-WebSocket context switch in SNode.C: an accepted HTTP Upgrade stages a replacement WebSocket context; after the current HTTP read callback, the HTTP context detaches for ContextSwitch, is removed, and the WebSocket SocketContextUpgrade attaches to the same established SocketConnection.">
</picture>

<sub>The replacement is staged while HTTP remains active; the same established connection continues through the switch.</sub>

The server-side HTTP upgrade path is protocol-generic. `Response::upgrade()`
first requires the request's `Connection` header to contain `Upgrade`. The
upgrade selector then reads the comma-separated values of the `Upgrade` header,
normalizes each protocol name, ignores an optional `/version` suffix for
selection, and chooses the first matching `SocketContextUpgradeFactory`. A
factory may be linked into the application or, when dynamic loading is allowed,
loaded by protocol name. The selected factory receives the HTTP request and
response and creates the protocol-specific `SocketContextUpgrade`; WebSocket is
the concrete implementation shown in the figure, not the only possible upgrade
target.

Once the selected factory creates a replacement context,
`setSocketContext(new)` stages it while the HTTP context is still active. The
protocol-specific factory is responsible for preparing the switching response.
For WebSocket, the current factory validates WebSocket version 13 and the
requested subprotocol, sets the WebSocket upgrade/accept headers, and selects
`101 Switching Protocols`. The upgrade-status or application callback calls
`response->end()` to queue the prepared response; the framework does not invoke
that call automatically.

The context switch itself is protocol-independent. After the current HTTP read
callback returns, the old HTTP context detaches with
`DetachReason::ContextSwitch` and is removed, the active-context pointer changes
to the staged replacement, and the selected `SocketContextUpgrade` attaches to
the same established `SocketConnection`. No second transport connection is
created.

For WebSocket specifically, the attached upgrade context adds WebSocket frame
receiver/transmitter behavior and selects a subprotocol where configured.
Upgrade factories can be linked into the application and the current selector
also supports protocol-named dynamic loading when enabled; WebSocket subprotocol
factories have their own linked/loadable extension paths.

Those loadable extension paths execute code inside the process. Packaging,
search paths, ownership, version compatibility, and allowed plugin names belong
to the deployment threat model. Do not describe dynamic discovery as a security
boundary.

Source anchors:

- [`SocketContextUpgradeFactory`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/SocketContextUpgradeFactory.h)
- [server-side upgrade selection](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/server/Response.cpp)
- [WebSocket upgrade context](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket/SocketContextUpgrade.h)

## 6. Higher protocol layers

SNode.C supplies source components above the stream layer:

- HTTP client and server contexts with request and response parsing;
- Express-style server routing and middleware above the HTTP server context;
- SSE/EventSource support layered on HTTP, including event-stream parsing,
  event dispatch, event IDs, and reconnect handling;
- WebSocket client/server upgrades and subprotocol infrastructure;
- MQTT 3.1.1 client/broker protocol components, including composition through
  WebSocket.

These layers do not all have the same role. Express-style routing is an
application-facing API above the HTTP server. SSE/EventSource remains inside
HTTP rather than using the protocol-upgrade mechanism described above. On the
client, `requestEventSource()` advertises `Accept: text/event-stream`; after a
matching HTTP response, the existing HTTP `SocketContext` installs the SSE
receive path instead of being replaced. `EventSourceT` parses the `data`,
`event`, `id`, and `retry` fields, exposes message/custom-event, open, and error
listeners plus `CONNECTING`, `OPEN`, and `CLOSED` state, retains the last event
ID for `Last-Event-ID` on reconnect, and applies `retry` values to reconnect
timing. On the server side, SSE stays a long-lived streamed HTTP response; it
does not require a `SocketContextUpgrade`.

WebSocket follows a deliberately different lifecycle: a successful HTTP Upgrade
replaces the HTTP context with a framed, bidirectional protocol context. MQTT
supplies protocol framework components and can also be composed through
WebSocket; MQTTSuite owns the ready-made broker, integration, bridge, CLI, and
storage application workflows.

Choose the highest layer that already owns the semantics the program needs. Use
the stream context for a custom byte protocol, HTTP for ordinary request/response
semantics, SSE/EventSource for one-way server-to-client event streams that stay
inside HTTP and need event-ID/reconnect semantics, WebSocket for framed
bidirectional messages, and MQTT components for an MQTT peer. Avoid wrapping a
higher-level protocol in a second, competing lifecycle abstraction.

Source anchors:

- [`EventSource`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/client/tools/EventSource.h)
- [SSE request path](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/client/Request.cpp)
- [HTTP client context](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/client/SocketContext.cpp)
- [HTTP server response streaming](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/server/Response.cpp)

## Extension checklist

Before adding a transport or protocol context, answer these questions:

1. Which object owns the connection, context, and application state?
2. What creates one context for each connection?
3. Which events attach, deliver data, signal failure, and detach the context?
4. How are partial reads, queued writes, slow peers, and orderly shutdown handled?
5. Which settings belong to local, remote, connection, socket, or TLS sections?
6. Which combinations are built and tested rather than merely expressible?
7. If a plugin is loaded, who controls its path and compatibility?

For endpoint policy and inspection commands, continue with the
[configuration guide](configuration.md). For qualified versus source-only
scope, use the [capability map](capabilities.md).
