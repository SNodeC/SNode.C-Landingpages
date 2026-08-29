# SNode.C

## Event-driven network clients and servers in C++20

Build C++20 network clients and servers around one recurring model: configure an
endpoint, establish a connection, and attach per-connection protocol behavior
while the event loop drives lifecycle and I/O.

**C++20** · [exact-head CI](https://github.com/SNodeC/snode.c/actions/runs/33189174904) ·
[MIT OR LGPL-3.0-or-later](https://github.com/SNodeC/snode.c/blob/master/LICENSE)

**[Run the echo pair](#run-the-echo-pair)** ·
**[Programming model](#programming-model)** ·
**[Browse examples](https://github.com/SNodeC/snode.c/tree/master/src/apps)**

## Programming model

A configured `SocketServer` listens and accepts, while a `SocketClient` initiates
a connection. Both paths converge on an established `SocketConnection`. That
connection calls the endpoint flow's `SocketContextFactory` with `create(this)`;
the factory returns the per-connection `SocketContext` that owns
application/protocol behavior.

![Diagram of the SNode.C programming model: a SocketServer accepts or a SocketClient completes a connection, the SocketConnection calls its endpoint flow's SocketContextFactory to create one active per-connection SocketContext, and the caller-thread event loop dispatches lifecycle and I/O callbacks.](../assets/programming-model.svg)

*Server and client establishment paths converge on the same connection-local
context model; the event loop is driven by `start()` and the connection calls the
retained factory with `create(this)`.*

| Role | Responsibility |
| --- | --- |
| `SocketServer` / `SocketClient` | Configured endpoint handles that own the server or client flow and retain the context factory. |
| `SocketConnection` | The established connection: addresses, stream mechanics, queues, timeouts, identity, and the active application context. |
| `SocketContextFactory` | The application-supplied creation boundary for connection-local behavior. |
| `SocketContext` | Protocol/application callbacks for one connection. |
| Event loop | Descriptor, timer, lifecycle, and data dispatch around the connection/context model. |

The supplied echo context shows the programming style without exposing the
endpoint template stack. This is an abridged excerpt from the
[verified echo source](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.cpp):

```cpp
void EchoSocketContext::onConnected() {
    if (role == Role::CLIENT) {
        sendToPeer("Hello peer! Nice to see you!!!");
    }
}

std::size_t EchoSocketContext::onReceivedFromPeer() {
    char chunk[4096];
    const std::size_t chunklen = readFromPeer(chunk, 4096);

    if (chunklen > 0) {
        sendToPeer(chunk, chunklen);
    }

    return chunklen;
}
```

`start()` runs the framework event loop synchronously on the thread that calls
it. SNode.C does not create a framework worker pool: a blocking or long-running
callback delays other work on that loop. Applications remain free to introduce
their own concurrency where appropriate.

A connection has one active context. SNode.C can replace that context without
replacing the underlying `SocketConnection`; the HTTP-to-WebSocket upgrade later
in this README is the concrete implemented example.

## Run the echo pair

The shortest independently qualified path is the supplied plain IPv4 echo server
and client on loopback.

For the shown source-build path, provide a C++20 compiler accepted by the
project's CMake checks, CMake 3.18+, Ninja, Git, pkg-config, OpenSSL development
files, and nlohmann/json 3.11+. A fresh default configure also needs network
access for the pinned spdlog dependency unless it is already provided.

Clone current `master` and build only the two echo targets:

```sh
git clone https://github.com/SNodeC/snode.c.git
cd snode.c

cmake -S . -B cmake-build-release -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DSNODEC_BUILD_APPS=ON \
  -DSNODEC_BUILD_TESTS=OFF \
  -DCHECK_INCLUDES=OFF

cmake --build cmake-build-release --parallel \
  --target echoserver-legacy-in echoclient-legacy-in

rm -rf cmake-build-release/echo-config
mkdir -p cmake-build-release/echo-config
```

Start the server from the `snode.c` checkout:

```sh
XDG_CONFIG_HOME="$PWD/cmake-build-release/echo-config" \
  ./cmake-build-release/src/apps/echo/echoserver-legacy-in \
  --log-level 4 --log-format text --monochrom=true \
  echoserver local --host 127.0.0.1 --port 18001
```

Then, from the same checkout in a second terminal, start the client with the same
isolated configuration directory:

```sh
XDG_CONFIG_HOME="$PWD/cmake-build-release/echo-config" \
  ./cmake-build-release/src/apps/echo/echoclient-legacy-in \
  --log-level 4 --log-format text --monochrom=true \
  echoclient remote --host 127.0.0.1 --port 18001
```

Ignoring timestamps and logger prefixes, the verified run contains these
diagnostic signals:

```text
role=server inst=echoserver — listener started
echoserver: listening on '127.0.0.1:18001'
role=server inst=echoserver conn=1 — transport connected

echoclient: connected to '127.0.0.1:18001 (127.0.0.1)'
role=client inst=echoclient conn=1 — transport connected
```

Those lines prove that the listener became active and that one plain IPv4
loopback transport connection formed. They do **not** visibly prove application
payload reflection. The source-defined client sends
`Hello peer! Nice to see you!!!`, and both contexts read available bytes and
send the same bytes back, so the supplied pair keeps reflecting data until it is
interrupted. Stop the client and server with Ctrl-C.

The same qualification baseline also includes plain IPv6 loopback, a
Unix-domain plain stream path, and one mutual-TLS IPv4 echo arrangement. Those
are separate scoped runs, not evidence that every family, TLS mode, and
application protocol combination is qualified.

The commands and evidence above were verified against
[`bf01683a53b48220a840522e8ccaf3b48e58c240`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240)
on 29 August 2026. At draft time, public `master` still resolves to that commit.

## Capabilities and evidence

SNode.C separates implementation breadth from test and runtime evidence. The
table below is deliberately **not** a support matrix: a component existing in
source does not mean every address-family, connection-mode, and protocol
combination has been tested or promised as a supported configuration.

| Area | Current implementation | Strongest current evidence | Boundary |
| --- | --- | --- | --- |
| Event runtime and stream model | Descriptor/timer event loop; configurable server/client stream endpoints; connection-local contexts; `epoll` default with selectable `poll` and `select` | Exact-head public CI passed the root-configured CTest suite; focused context-lifecycle test passed | No performance, fairness, real-time, or worker-thread claim |
| Plain streams | IPv4, IPv6, and Unix-domain server/client paths | Automated component tests plus preserved echo runtime runs for all three | Strongest current networking evidence; not a platform-support matrix |
| TLS streams | OpenSSL-backed TLS connection layer and configuration surface | TLS state/ownership/shutdown tests plus one mutual-TLS IPv4 echo run | No universal family/protocol matrix; peer, hostname, certificate, trust, and cipher policy remain application/operator responsibilities |
| Bluetooth | Conditional RFCOMM and L2CAP stream layers when BlueZ is available | Current configured CI build included BlueZ | No targeted Bluetooth hardware runtime qualification |
| HTTP and routing | HTTP/1.0 and HTTP/1.1 client/server components; Express-style routing and middleware | Broad plain-IPv4 HTTP tests and smaller IPv6/Unix sets; routing/middleware tests | No HTTP/2; “Express-style” is not Node.js Express compatibility |
| WebSocket and SSE | WebSocket version 13; EventSource/SSE | WebSocket unit/component tests including plain IPv4 and smaller IPv6/Unix coverage; SSE plain-IPv4 tests | No conformance certification or universal TLS/family matrix |
| MQTT | MQTT 3.1.1 client/server protocol components; MQTT-over-WebSocket components | MQTT packet/lifecycle tests; downstream MQTTSuite has a separately qualified IPv4 QoS 1 path | No SNode.C MQTT network matrix; MQTT 5 is not a current capability; MQTT-over-WebSocket has no targeted SNode.C network qualification |
| Configuration | C++ API defaults, configuration files, generated CLI sections, and inspection/export surfaces | Source plus configuration tests | Effective precedence is command line > configuration file > API/default |
| Installed consumption | Componentized namespaced CMake targets and install/export metadata | Passing staged installed-consumer tests and recorded downstream builds | Local source installation is not current package-manager or binary-release availability |

Current `master` is source-buildable and locally installable, but the reviewed
head is not represented by a current tagged 2.0/current-head release or published
binary package. The latest GitHub release is older than the reviewed `master`.
Likewise, one current Linux/GCC CI lane and one Debian/x86-64 Release
qualification do not establish broad Linux, compiler, architecture, OpenWrt,
Android, or other-platform support.

There is no current benchmark corpus behind throughput, latency, footprint, or
“lightweight” claims, and TLS availability is not a deployment security policy.
See the [capability and evidence notes](../docs/capabilities.md) for the deeper
qualification boundaries.

## Architecture and extension points

The programming model sits on explicit responsibility boundaries rather than one
monolithic socket abstraction.

| Layer | Question it answers |
| --- | --- |
| Event runtime | When are descriptor and timer events dispatched? |
| Address/network family | How are local and remote endpoints represented? |
| Physical stream | How is a connection accepted or established and read/written? |
| Connection mode | Is the stream plain or OpenSSL-backed TLS? |
| Endpoint role | Is this a server/listener or client/connector flow? |
| Application context | Which protocol/application behavior owns this connection now? |

Custom `SocketContextFactory` and `SocketContext` implementations are the
direct extension point for connection-local behavior. Concrete endpoint types
assemble the selected networking layers around them; composition does not imply
that every theoretically possible combination has equivalent test coverage.

The connection/context split also permits a real protocol transition without
replacing the established connection. During an HTTP-to-WebSocket upgrade, the
WebSocket factory is selected and creates the replacement context; the HTTP path
prepares the `101 Switching Protocols` response. `setSocketContext(new)` stages
the replacement; `response->end()` then queues the `101` through the still-active
HTTP context. After the current HTTP read callback returns, the HTTP context
detaches with `DetachReason::ContextSwitch`, the active pointer changes, and the
WebSocket context attaches to the same `SocketConnection`.

![HTTP-to-WebSocket context switch in SNode.C: an accepted HTTP Upgrade stages a WebSocket context; after the current HTTP read callback, the HTTP context detaches for ContextSwitch, the new context attaches, and the same SocketConnection remains established.](../assets/http-websocket-context-switch.svg)

*An HTTP Upgrade prepares the replacement context and `101 Switching Protocols`
response; `setSocketContext(new)` stages the replacement before `response->end()`
queues the response. After the current read callback, the old context is removed,
the active pointer changes, and the WebSocket context attaches to the same
connection.*

Configuration follows the endpoint hierarchy rather than living inside protocol
callbacks. A named endpoint can expose the same typed configuration structure
through C++ API defaults, a configuration file, and generated command-line
sections, with verified precedence:

**command line > configuration file > API/default**

The full option hierarchy belongs in the
[configuration guide](../docs/configuration.md), not in this landing page.
SNode.C also installs componentized CMake targets; current exact-head tests
exercise selected staged installed consumers rather than claiming every exported
combination.

## Documentation, examples, and ecosystem routes

For deeper evaluation:

- [Architecture](../docs/architecture.md) — object/lifecycle and layer
  responsibilities.
- [Configuration](../docs/configuration.md) — named instances, files, generated
  CLI sections, and precedence.
- [Capabilities and evidence](../docs/capabilities.md) — detailed scope and
  qualification boundaries.
- [Example sources](https://github.com/SNodeC/snode.c/tree/master/src/apps) —
  echo, HTTP/WebSocket, and other maintained examples.
- [Repository source](https://github.com/SNodeC/snode.c) ·
  [Issues](https://github.com/SNodeC/snode.c/issues) ·
  [Discussions](https://github.com/SNodeC/snode.c/discussions) ·
  [Releases](https://github.com/SNodeC/snode.c/releases) ·
  [License](https://github.com/SNodeC/snode.c/blob/master/LICENSE).

The wider ecosystem keeps domain-specific behavior in separate projects:

- [MQTTSuite](https://github.com/SNodeC/mqttsuite) builds MQTT broker,
  integration, bridge, CLI, and storage applications on SNode.C components.
- [AISuite](https://github.com/SNodeC/AISuite) uses SNode.C event-loop,
  transport, and web infrastructure for typed Codex integration and bridging
  where configured.
- [CodexUI](https://github.com/SNodeC/CodexUI) is the user-facing native/browser
  project in the AISuite path; its UI behavior belongs to CodexUI, not SNode.C.

These are related projects, not one shared-version distribution or one
all-project runtime pipeline. The two current ecosystem paths are
SNode.C → MQTTSuite and SNode.C → AISuite → CodexUI. AISuite and CodexUI are
independent open-source projects, not official OpenAI products.
