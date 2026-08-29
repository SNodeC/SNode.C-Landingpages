# SNode.C

**Event-driven network clients and servers in C++20**

One recurring model: configure an endpoint, take the connection it establishes,
and attach protocol behavior to that connection while the event loop drives
lifecycle and I/O. Application behavior stays connection-local; socket and
dispatch mechanics stay outside it.

**C++20** ·
[MIT OR LGPL-3.0-or-later](https://github.com/SNodeC/snode.c/blob/master/LICENSE)

**[Run the echo pair](#run-the-echo-pair)** ·
**[Programming model](#programming-model)** ·
**[Browse examples](https://github.com/SNodeC/snode.c/tree/master/src/apps)**

## Programming model

A configured `SocketServer` follows `listen → accept`; a `SocketClient` follows
the connect path. Each endpoint flow retains its own `SocketContextFactory`, and
both paths converge on an established `SocketConnection`. The connection calls
its retained factory with `create(this)`; the factory returns the per-connection
`SocketContext`. One context is active for a connection at a time.

<picture>
  <source media="(max-width: 600px)" srcset="assets/programming-model-mobile.svg">
  <img src="assets/programming-model.svg" alt="Diagram of the SNode.C programming model: a SocketServer accepts or a SocketClient completes a connection, the SocketConnection calls its endpoint flow's SocketContextFactory to create one active per-connection SocketContext, and the caller-thread event loop dispatches lifecycle and I/O callbacks.">
</picture>

| Role | Responsibility |
| --- | --- |
| `SocketServer` / `SocketClient` | Configured endpoints; each flow retains its own factory. |
| `SocketConnection` | Established stream and owner of the active context. |
| `SocketContextFactory` | Creates connection-local behavior for its connection. |
| `SocketContext` | Per-connection protocol and application callbacks. |
| Event loop | `start()` dispatches descriptor, timer, lifecycle, and data work. |

The supplied [echo context](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.cpp)
shows how a context handles its connection:

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
it. SNode.C does not create a framework worker pool, so a blocking or
long-running callback delays other work on that loop. Applications may introduce
their own concurrency.

A connection can replace its active context without replacing the underlying
`SocketConnection`; the [HTTP-to-WebSocket upgrade](#architecture-and-extension-points)
below is a concrete implementation of that mechanism.

## Run the echo pair

The shortest independently qualified path is the supplied plain IPv4 echo server
and client on loopback.

For this source-build path, provide Git, a project-accepted C++20 compiler,
CMake 3.18+, Ninja, pkg-config, OpenSSL development files, and nlohmann/json
3.11+. A fresh default configure also needs network access for its pinned
dependency fetch.

Clone `master` and build only the two echo targets:

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

mkdir -p cmake-build-release/echo-config
```

The isolated configuration directory and explicit information-level, text,
monochrome logging options make the output below reproducible; they are not
ordinary mandatory runtime setup.

Start the server:

```sh
XDG_CONFIG_HOME="$PWD/cmake-build-release/echo-config" \
  ./cmake-build-release/src/apps/echo/echoserver-legacy-in \
  --log-level 4 --log-format text --monochrom=true \
  echoserver local --host 127.0.0.1 --port 18001
```

Then start the client from the same checkout in a second terminal:

```sh
XDG_CONFIG_HOME="$PWD/cmake-build-release/echo-config" \
  ./cmake-build-release/src/apps/echo/echoclient-legacy-in \
  --log-level 4 --log-format text --monochrom=true \
  echoclient remote --host 127.0.0.1 --port 18001
```

Ignoring timestamps and logger prefixes, the run produces:

```text
role=server inst=echoserver — listener started
echoserver: listening on '127.0.0.1:18001'
role=server inst=echoserver conn=1 — transport connected

echoclient: connected to '127.0.0.1:18001 (127.0.0.1)'
role=client inst=echoclient conn=1 — transport connected
```

These lines prove that the listener started and one plain IPv4 loopback
connection formed; the selected information-level output does not print the
reflected payload. The supplied source-defined contexts do reflect bytes, and
the pair keeps echoing until you stop both processes with Ctrl-C.

Separate qualification also covered plain IPv6 loopback, a Unix-domain plain
stream path, and one mutual-TLS IPv4 echo arrangement.

Commands and output were verified against
[`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240)
on 29 August 2026.

## Capabilities and evidence

Implementation and composability do not imply that every address-family ×
connection-mode × protocol combination has equivalent test or support evidence.
Each item below keeps implementation, strongest evidence, and boundary together
without requiring a wide table.

- **Event runtime and stream model.** Descriptor/timer event loop; server/client
  stream endpoints; connection-local contexts. `epoll` is the default; `poll`
  and `select` are configure-time alternatives, and `core` links one selected
  implementation. **Evidence:** CI on the reviewed commit ran the root test
  suite; focused context-lifecycle testing also passed. **Boundary:** CI/runtime
  used default `epoll` only.
- **Plain streams.** IPv4, IPv6, and Unix-domain server/client paths.
  **Evidence:** component tests plus recorded echo runs for all three.
  **Boundary:** scoped runtime evidence.
- **TLS streams.** OpenSSL-backed TLS connection layer and configuration surface.
  **Evidence:** TLS state/ownership/shutdown tests plus one mutual-TLS IPv4 echo
  run. **Boundary:** security policy is application/operator-owned.
- **Bluetooth.** Conditional RFCOMM and L2CAP stream layers when BlueZ is
  available. **Evidence:** the reviewed CI configuration built with BlueZ.
  **Boundary:** no hardware runtime qualification.
- **HTTP and routing.** HTTP/1.0 and HTTP/1.1 client/server components;
  Express-style routing and middleware. **Evidence:** broad plain-IPv4 HTTP
  tests, smaller IPv6/Unix sets, and routing/middleware tests. **Boundary:** no
  HTTP/2 or Node.js/Express compatibility.
- **WebSocket and SSE.** WebSocket version 13; EventSource/SSE. **Evidence:**
  WebSocket unit/component tests with plain IPv4 plus smaller IPv6/Unix coverage;
  SSE plain-IPv4 tests. **Boundary:** no conformance certification.
- **MQTT.** MQTT 3.1.1 client/server components; MQTT-over-WebSocket components.
  **Evidence:** MQTT packet/lifecycle tests; a separate MQTTSuite IPv4 QoS 1 run.
  **Boundary:** no MQTT 5; MQTT-over-WebSocket evidence is narrower.

`master` is source-buildable and locally installable, but the reviewed head is
not represented by a current tagged 2.0/current-head release or published binary
package; the latest GitHub release is older. One Linux/GCC CI lane and one
Debian/x86-64 Release qualification do not establish broad Linux, compiler,
architecture, OpenWrt, Android, or other-platform support. No performance or
footprint claim is made.

See the [capability and evidence notes](docs/capabilities.md) for detailed scope.

## Architecture and extension points

Concrete endpoint types compose an address/network family, physical stream,
plain or OpenSSL-backed TLS connection mode, server/client role, and application
context around the shared event runtime. Custom `SocketContextFactory` and
`SocketContext` implementations are the direct extension point for
connection-local behavior.

The connection/context split also permits a protocol transition without opening
a second transport connection. After an HTTP Upgrade is accepted, the WebSocket
upgrade factory is selected and creates the replacement `SocketContextUpgrade`;
the HTTP path prepares the `101 Switching Protocols` response.
`setSocketContext(new)` stages the replacement while the HTTP context remains
active, and the upgrade-status/application callback calls `response->end()` to
queue the `101`. After the current HTTP read callback returns, the HTTP context
detaches with `DetachReason::ContextSwitch` and is removed, the active-context
pointer changes to the staged replacement, and the WebSocket
`SocketContextUpgrade` attaches. The same `SocketConnection` remains established;
no second transport connection is created.

<picture>
  <source media="(max-width: 600px)" srcset="assets/http-websocket-context-switch-mobile.svg">
  <img src="assets/http-websocket-context-switch.svg" alt="HTTP-to-WebSocket context switch in SNode.C: an accepted HTTP Upgrade stages a WebSocket context; after the current HTTP read callback, the HTTP context detaches for ContextSwitch, the new context attaches, and the same SocketConnection remains established.">
</picture>

*Same connection, new active context.*

A named endpoint exposes its typed configuration hierarchy through C++ API
defaults, a configuration file, and generated command-line sections. Effective
precedence is:

**command line > configuration file > API/default**

See the [configuration guide](docs/configuration.md) for the full hierarchy.
SNode.C also installs componentized namespaced CMake targets; tests on the
reviewed commit include selected installed-consumer builds.

## Documentation, examples, and ecosystem routes

For deeper evaluation:

- [Architecture](docs/architecture.md) — object/lifecycle and layer
  responsibilities.
- [Configuration](docs/configuration.md) — named instances, files, generated CLI
  sections, and precedence.
- [Capabilities and evidence](docs/capabilities.md) — detailed scope and
  qualification boundaries.
- [Example sources](https://github.com/SNodeC/snode.c/tree/master/src/apps) —
  echo, HTTP/WebSocket, and other maintained examples.
- [Repository source](https://github.com/SNodeC/snode.c) ·
  [Issues](https://github.com/SNodeC/snode.c/issues) ·
  [Discussions](https://github.com/SNodeC/snode.c/discussions) ·
  [Releases](https://github.com/SNodeC/snode.c/releases) ·
  [License](https://github.com/SNodeC/snode.c/blob/master/LICENSE).

Related projects keep their domain-specific behavior outside SNode.C:

- [MQTTSuite](https://github.com/SNodeC/mqttsuite) is the downstream MQTT
  application toolkit; its broker, integration, bridge, CLI, and storage
  behavior belongs to MQTTSuite.
- [AISuite](https://github.com/SNodeC/AISuite) is the downstream typed Codex
  integration and bridge project; its Codex protocol and controller/bridge
  behavior belongs to AISuite.
- [CodexUI](https://github.com/SNodeC/CodexUI) is the native/browser presentation
  project in the AISuite path; its UI behavior belongs to CodexUI.

AISuite and CodexUI are independent open-source projects, not official OpenAI
products. The two ecosystem paths are SNode.C → MQTTSuite and
SNode.C → AISuite → CodexUI.

Next: **[read the architecture](docs/architecture.md)** or
**[browse the examples](https://github.com/SNodeC/snode.c/tree/master/src/apps)**.
