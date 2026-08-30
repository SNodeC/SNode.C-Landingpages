# SNode.C

**Event-driven network clients and servers in C++20**

SNode.C is a C++20 networking framework for building network clients, servers,
and protocol endpoints around a shared event-driven runtime. It centralizes
connection lifecycle, event dispatch, stream/TLS mechanics, and hierarchical
endpoint/application configuration so protocol code can stay focused on what
happens on one connection.

SNode.C is designed primarily for machine-to-machine (M2M) communication and
IoT-oriented network applications, while its connection and protocol model is
general-purpose.

The core model is connection-local: a configured server or client establishes a
connection, and that connection gets one active protocol/application context.
The next section names those objects and shows how the same model underpins
custom stream protocols, HTTP, WebSocket, EventSource/SSE, and MQTT 3.1.1.

**C++20** ·
[MIT OR LGPL-3.0-or-later](https://github.com/SNodeC/snode.c/blob/master/LICENSE)

**[Run the echo pair](#run-the-echo-pair)** ·
**[See the programming model](#the-programming-model)** ·
**[Check capabilities](#capabilities-at-a-glance)** ·
**[Open the API reference](https://snodec.github.io/snode.c-doc/html/index.html)**

## The programming model

Start with the lifecycle rather than the protocol list. A `SocketServer` follows
the listen/accept path and a `SocketClient` follows the connect path. Each
endpoint flow retains its own `SocketContextFactory`. Once a transport
connection is established, its `SocketConnection` calls that retained factory
with `create(this)`; the returned `SocketContext` becomes the connection-local
protocol/application behavior. One context is active for a connection at a time.

<picture>
  <source media="(max-width: 600px)" srcset="assets/programming-model-mobile.svg">
  <img src="assets/programming-model.svg" alt="Diagram of the SNode.C programming model: a SocketServer accepts or a SocketClient completes a connection, the SocketConnection calls its endpoint flow's SocketContextFactory to create one active per-connection SocketContext, and the caller-thread event loop dispatches lifecycle and I/O callbacks.">
</picture>

<sub>Each endpoint flow retains its own context factory; the established connection owns one active connection-local context.</sub>

| Role | Responsibility |
| --- | --- |
| `SocketServer` / `SocketClient` | Configure and initiate the server or client endpoint flow. |
| `SocketConnection` | Own the established stream and its active context. |
| `SocketContextFactory` | Create connection-local behavior for that endpoint flow. |
| `SocketContext` | Handle protocol/application callbacks for one connection. |
| Event loop | Dispatch descriptor, timer, lifecycle, and data work. |

The standalone [external echo example](https://github.com/SNodeC/snode.c/tree/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79/examples/echo)
uses the concrete installed IPv4/plain-stream types directly. Its server is:

```cpp
using EchoSocketServer =
    net::in::stream::legacy::SocketServer<echo::EchoServerSocketContextFactory>;
```

The shared [echo context](https://github.com/SNodeC/snode.c/blob/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79/examples/echo/EchoSocketContext.cpp)
shows what connection-local behavior looks like:

```cpp
void EchoSocketContext::onConnected() {
    if (role == Role::CLIENT) {
        log().info("Echo client: sending initial greeting: '{}'",
                   "Hello peer! Nice to see you!!!");
        sendToPeer("Hello peer! Nice to see you!!!");
    }
}

std::size_t EchoSocketContext::onReceivedFromPeer() {
    char chunk[4096];
    const std::size_t chunklen = readFromPeer(chunk, sizeof(chunk));

    if (chunklen > 0) {
        const char* roleName = role == Role::CLIENT ? "client" : "server";
        log().info("Echo {}: data to reflect: {}", roleName,
                   std::string(chunk, chunklen));
        sendToPeer(chunk, chunklen);
    }

    return chunklen;
}
```

At the HTTP layer, current source exposes an Express-style `WebApp` above the
HTTP server context. A health route can be registered as:

```cpp
const express::legacy::in::WebApp app;

app.use(express::middleware::VerboseRequest());

app.get("/health", [] APPLICATION(req, res) {
    res->json({{"ok", true}});
});
```

`APPLICATION(req, res)` supplies the request/response callback parameters used
by route handlers. The [current example source](https://github.com/SNodeC/snode.c/blob/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79/src/apps/main.cpp)
also shows middleware, parameterized routes, nested routers, and SSE on this
surface.

`start()` runs the framework event loop synchronously on the thread that calls
it. SNode.C does not create a framework worker pool, so a blocking or
long-running callback delays other work on that loop. Applications may introduce
their own concurrency.

Because the context is separate from the connection, SNode.C can replace the
active context while retaining the established `SocketConnection`. The
[HTTP-to-WebSocket transition](#architecture-and-extension-points) below is a
concrete use of that mechanism.

## Run the echo pair

[`examples/echo`](https://github.com/SNodeC/snode.c/tree/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79/examples/echo)
is a complete standalone CMake project that consumes an **installed** SNode.C
package. It builds one plain-IPv4 server and client and therefore exercises the
same downstream integration path an external application uses.

For a source installation, use Git, a C++20 compiler, CMake 3.18+, Ninja,
pkg-config, OpenSSL development files, and nlohmann/json 3.11+. On the recorded
Debian qualification environment, the base packages were:

```sh
sudo apt install --yes \
  build-essential ca-certificates cmake git ninja-build pkgconf \
  libssl-dev nlohmann-json3-dev
```

Use the equivalent packages on other distributions. A fresh default configure
also needs network access for its pinned dependency fetch.

Clone and install current `master` into an isolated prefix:

```sh
git clone https://github.com/SNodeC/snode.c.git
cd snode.c

cmake -S . -B build-snodec -G Ninja \
  -DCMAKE_BUILD_TYPE=Release
cmake --build build-snodec --parallel
cmake --install build-snodec --prefix "$PWD/.snodec"
```

Then configure the external example against that installed package:

```sh
cmake -S examples/echo -B build-echo -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=ON \
  -DCMAKE_PREFIX_PATH="$PWD/.snodec"
cmake --build build-echo --parallel
```

Its CMake contract is intentionally small:

```cmake
find_package(snodec REQUIRED COMPONENTS net-in-stream-legacy)

target_link_libraries(
    echo-context PUBLIC
    snodec::net-in-stream-legacy
)
```

The source also includes SNode.C through the installed public header layout,
for example:

```cpp
#include <core/SNodeC.h>
#include <core/socket/State.h>
#include <net/in/stream/legacy/SocketServer.h>
```

On Linux, when using a non-system install prefix, expose its library directory
to the runtime loader before running the example or its CTests:

```sh
export LD_LIBRARY_PATH="$PWD/.snodec/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
```

Start the server:

```sh
./build-echo/echoserver \
  echoserver local --host 127.0.0.1 --port 18001
```

Then start the client in a second terminal:

```sh
./build-echo/echoclient \
  echoclient remote --host 127.0.0.1 --port 18001
```

To isolate this walkthrough from existing user configuration and make the shown
logging independent of terminal color support, create `build-echo/echo-config`,
set `XDG_CONFIG_HOME="$PWD/build-echo/echo-config"`, and add
`--monochrom=true` before the instance subcommand. Those controls are
reproducibility aids, not requirements of the echo application.

The application logger makes the protocol behavior visible. Representative
message bodies from the current example include:

```text
Echo server context attached
Echo client context attached
Echo client: sending initial greeting: 'Hello peer! Nice to see you!!!'
Echo server: data to reflect: Hello peer! Nice to see you!!!
Echo client: data to reflect: Hello peer! Nice to see you!!!
```

The same project defines four application-level CTests covering its generated
configuration surface, the real server against a deterministic external peer,
the real client against a deterministic external peer, and a bounded real-pair
smoke run:

```sh
ctest --test-dir build-echo --output-on-failure
```

Current public `master` at
[`60f26d9`](https://github.com/SNodeC/snode.c/commit/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79)
configures and builds this external consumer in the observed
[`gcc-debug` job](https://github.com/SNodeC/snode.c/actions/runs/33293707417/job/99209664201).
The main repository CTest step passes 181/181. The separate external-echo CTest
step is currently red because the installed shared-library directory is not
available to that job's runtime loader; this publication therefore does not
claim that those four external-example tests passed on current `master`.

Recorded qualification from the preceding source baseline also covers plain
IPv6 loopback, a Unix-domain plain stream path, and one mutual-TLS IPv4 echo
arrangement. See the [capability map](docs/capabilities.md#network-and-connection-variants)
for their exact evidence scope; those transport runs were not repeated by this
closure pass.

## Capabilities at a glance

For a framework evaluation, it matters both what SNode.C implements and how far
that surface has been exercised. This is a fit-check, not a claim that every
address-family × connection-mode × protocol combination has equivalent test
coverage.

- **Event runtime.** **Available:** Descriptor/timer loop; server/client stream
  endpoints; connection-local contexts. `epoll` is the default; `poll` and
  `select` are configure-time alternatives. **Exercised:** the current public
  `master` [`gcc-debug` job](https://github.com/SNodeC/snode.c/actions/runs/33293707417/job/99209664201)
  built the repository and passed the main 181-test CTest suite. Current
  CI/runtime evidence exercised default `epoll` only.
- **Configuration.** **Available:** Typed `SubCommand` hierarchy for framework
  and application settings, with API defaults, configuration-file values, and
  generated CLI/help/inspection surfaces. **Exercised:** the echo application
  and downstream MQTTSuite application configuration use the same model.
- **Plain streams.** **Available:** IPv4, IPv6, and Unix-domain server/client
  paths. **Exercised:** Component tests plus recorded echo runs for all three;
  the current external example is concrete plain IPv4.
- **TLS streams.** **Available:** OpenSSL-backed TLS connection layer and
  configuration. **Exercised:** TLS state/ownership/shutdown tests plus one
  recorded mutual-TLS IPv4 echo run. Trust, hostname, certificate, and cipher
  policy remain application/operator responsibilities.
- **Bluetooth.** **Available:** Conditional RFCOMM and L2CAP stream layers with
  BlueZ. **Exercised:** The reviewed CI build included BlueZ; no hardware runtime
  qualification.
- **Web protocols.** **Available:** HTTP/1.0 and HTTP/1.1, Express-style
  routing/middleware, WebSocket version 13, and EventSource/SSE. **Exercised:**
  Broad plain-IPv4 HTTP tests, smaller IPv6/Unix HTTP and WebSocket paths, and
  plain-IPv4 SSE tests. No HTTP/2 claim; “Express-style” is not Node.js Express
  compatibility.
- **MQTT.** **Available:** MQTT 3.1.1 client/server and MQTT-over-WebSocket
  components. **Exercised:** Packet/lifecycle tests; MQTTSuite has a separately
  qualified IPv4 QoS 1 path. No MQTT 5; MQTT-over-WebSocket network evidence is
  narrower.

The reviewed `master` is source-buildable and locally installable, but it is
newer than the latest GitHub release, `v1.0.2`, and is not represented by a
current tagged 2.0 release or a published current-head binary package. Current
platform evidence includes one Linux/GCC CI lane and one Debian/x86-64 Release
qualification; it does not establish a broad operating-system, compiler, or
architecture support matrix. No throughput, latency, or footprint claim is made
here.

See the [capability map](docs/capabilities.md) for detailed protocol, transport,
build, platform, and evidence scope, including optional components and tooling.

## Architecture and extension points

A concrete endpoint selects a compatible address/network family, plain or
OpenSSL-backed TLS stream mode, server or client role, and application context
around the shared event runtime. Custom `SocketContextFactory` and
`SocketContext` implementations are the direct extension point. The
[architecture guide](docs/architecture.md) shows the full composition and its
boundaries.

The connection/context split also supports a protocol transition without opening
a second transport connection.

<picture>
  <source media="(max-width: 600px)" srcset="assets/http-websocket-context-switch-mobile.svg">
  <img src="assets/http-websocket-context-switch.svg" alt="HTTP-to-WebSocket context switch in SNode.C: an accepted HTTP Upgrade stages a WebSocket context; after the current HTTP read callback, the HTTP context detaches for ContextSwitch, the new context attaches, and the same SocketConnection remains established.">
</picture>

<sub>The replacement is staged while HTTP remains active; the same established connection continues through the switch.</sub>

During an HTTP-to-WebSocket upgrade, the replacement is staged while HTTP is
still active and becomes the active context only after the current HTTP read
callback returns; the established `SocketConnection` is retained. The
[architecture guide](docs/architecture.md#5-context-replacement-and-protocol-upgrades)
carries the identifier-level chronology. SSE/EventSource follows a different
HTTP-layer path: it keeps the HTTP context and streams server-to-client events
rather than replacing the active protocol context.

SNode.C's configuration tree is also an extension point. Named endpoints
contribute typed sections, and applications can attach their own `SubCommand`
subclasses to the same root hierarchy. Configurable values then share the same
three surfaces:

**Highest precedence first:** command line > configuration file > API/default

The [configuration guide](docs/configuration.md) covers application-owned
subcommands, named instances, role-specific sections, inspection commands, TLS
policy, and the responsive configuration figure. SNode.C also installs
componentized namespaced CMake targets; tests include selected installed
consumers.

## Choose your next step

| If you want to… | Go here |
| --- | --- |
| Understand ownership, lifecycle, composition, and extension points | [Architecture](docs/architecture.md) |
| Configure endpoints and application settings, CLI/file overrides, retry, reconnect, or TLS | [Configuration](docs/configuration.md) |
| Check exact protocol, transport, build, platform, and qualification scope | [Capabilities](docs/capabilities.md) |
| Inspect classes, namespaces, and generated Doxygen documentation | [API reference](https://snodec.github.io/snode.c-doc/html/index.html) |
| Start from a standalone installed-package example | [External echo example](https://github.com/SNodeC/snode.c/tree/master/examples/echo) |
| Explore additional application sources | [In-tree applications](https://github.com/SNodeC/snode.c/tree/master/src/apps) |
| Inspect or discuss the project | [Source](https://github.com/SNodeC/snode.c) · [Issues](https://github.com/SNodeC/snode.c/issues) · [Discussions](https://github.com/SNodeC/snode.c/discussions) · [Releases](https://github.com/SNodeC/snode.c/releases) |

SNode.C is the networking foundation for two distinct ecosystem paths.
[MQTTSuite](https://github.com/SNodeC/mqttsuite) provides MQTT broker,
integration, bridge, CLI, and storage applications.
[AISuite](https://github.com/SNodeC/AISuite) provides typed Codex integration and
bridging, with [CodexUI](https://github.com/SNodeC/CodexUI) as the
native/browser presentation project in that path. These are related projects,
not one shared-version distribution or one all-project runtime pipeline. AISuite
and CodexUI are independent open-source projects, not official OpenAI products.

If the connection/context split matches the architecture you want, continue with
the [architecture guide](docs/architecture.md). If you prefer to evaluate by
code, start with the standalone [external echo example](https://github.com/SNodeC/snode.c/tree/master/examples/echo).
