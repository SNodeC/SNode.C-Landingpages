# SNode.C

**Event-driven network clients and servers in C++20**

SNode.C is a C++20 networking framework for clients, servers, and protocol endpoints around one event-driven runtime. It separates endpoint role, address family, connection mechanics, configuration, and connection-local protocol behavior instead of baking them into one application-specific stack.

The framework is general-purpose, with a strong machine-to-machine and IoT focus. Current source provides IPv4, IPv6, Unix-domain, RFCOMM, and L2CAP families; plain and OpenSSL-backed TLS stream modes; HTTP/1.x, Express-style routing, SSE/EventSource, WebSocket 13, MQTT 3.1.1, and MQTT over WebSocket components. Availability does **not** imply that every cross-product is built, tested, or runtime-qualified.

**C++20** · [MIT OR LGPL-3.0-or-later](https://github.com/SNodeC/snode.c/blob/master/LICENSE)

**[Run the echo pair](#run-the-echo-pair)** · **[See the programming model](#the-programming-model)** · **[Check capabilities](#capabilities-at-a-glance)** · **[Open the API reference](https://snodec.github.io/snode.c-doc/html/index.html)**

## The programming model

A `SocketServer` follows the listen/accept path and a `SocketClient` follows the connect path. Each endpoint flow retains its own `SocketContextFactory`. When a transport connection becomes usable, its `SocketConnection` invokes that retained factory with `create(this)` and installs the returned `SocketContext` as the connection-local protocol/application behavior. One context is active for a connection at a time.

<picture>
  <source media="(max-width: 600px)" srcset="assets/programming-model-mobile.svg">
  <img src="assets/programming-model.svg" width="809" alt="SNode.C programming model with separate server and client endpoint flows. Each flow establishes its own SocketConnection, the connection calls the retained SocketContextFactory with create(this), and the returned SocketContext becomes the one active context for that connection. The event loop dispatches descriptor, timer, lifecycle, and data callbacks on the caller thread.">
</picture>

<sub>Server and client flows use the same connection-local model while retaining independent factories and connections.</sub>

| Concept | Responsibility |
| --- | --- |
| `SocketServer` / `SocketClient` | Configure and initiate the server or client endpoint flow. |
| `SocketConnection` | Own the established stream and its active context. |
| `SocketContextFactory` | Create behavior for one established connection. |
| `SocketContext` | Handle protocol/application callbacks for one connection. |
| Event loop | Dispatch readiness, timer, lifecycle, and data work synchronously on the thread running `start()`. |

A minimal server endpoint can use the installed IPv4/plain-stream component directly:

```cpp
using EchoSocketServer =
    net::in::stream::legacy::SocketServer<echo::EchoServerSocketContextFactory>;
```

A `SocketContext` then implements connection-local behavior, for example reading bytes from the peer and sending a response through the same connection. The endpoint family and plain/TLS connection mode can change without moving that protocol behavior into the endpoint object itself.

At the HTTP layer, SNode.C also exposes an Express-style `WebApp` above the HTTP server context:

```cpp
const express::legacy::in::WebApp app;

app.get("/health", [] APPLICATION(req, res) {
    res->json({{"ok", true}});
});
```

`start()` runs the event loop synchronously on the thread that calls it. SNode.C does not create a framework worker pool; blocking or long-running callbacks therefore delay other work on that loop unless the application introduces its own concurrency.

## Run the echo pair

[`examples/echo`](https://github.com/SNodeC/snode.c/tree/master/examples/echo) is a standalone CMake project that consumes an **installed** SNode.C package. It builds a plain-IPv4 server and client, so it exercises the same package-consumption path an external application uses.

On a Debian-style system, a minimal source-build environment includes a C++20 compiler, CMake, Ninja or Make, pkg-config, OpenSSL development files, and nlohmann/json:

```sh
sudo apt install --yes \
  build-essential ca-certificates cmake git ninja-build pkgconf \
  libssl-dev nlohmann-json3-dev
```

Clone, build, and install SNode.C into an isolated prefix:

```sh
git clone https://github.com/SNodeC/snode.c.git
cd snode.c

cmake -S . -B build-snodec -G Ninja \
  -DCMAKE_BUILD_TYPE=Release
cmake --build build-snodec --parallel
cmake --install build-snodec --prefix "$PWD/.snodec"
```

Then build the external example against that installed package:

```sh
cmake -S examples/echo -B build-echo -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=ON \
  -DCMAKE_PREFIX_PATH="$PWD/.snodec"
cmake --build build-echo --parallel
```

Its package contract is intentionally small:

```cmake
find_package(snodec REQUIRED COMPONENTS net-in-stream-legacy)

target_link_libraries(
    echo-context PUBLIC
    snodec::net-in-stream-legacy
)
```

For a non-system installation on Linux, expose the installed shared-library directory before running the pair:

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

Representative application messages include:

```text
Echo server context attached
Echo client context attached
Echo client: sending initial greeting: 'Hello peer! Nice to see you!!!'
Echo server: data to reflect: Hello peer! Nice to see you!!!
Echo client: data to reflect: Hello peer! Nice to see you!!!
```

The exact public source head reviewed for this landing-page pass is [`1f0f728`](https://github.com/SNodeC/snode.c/commit/1f0f728fc9b3b45174f2cd790d83b2f493e58af1). Its public [`gcc-debug` CI job](https://github.com/SNodeC/snode.c/actions/runs/33489538669/job/99797488461) completed successfully, including the main CTest step and the installed-package external echo CTests. Earlier recorded runtime qualification covered additional plain IPv6, Unix-domain plain-stream, and mutual-TLS IPv4 paths; those observations remain scoped to their recorded baselines rather than being silently promoted to the newer source head. The [capability map](docs/capabilities.md) keeps source, CI, and runtime evidence separate.

## Capabilities at a glance

For framework evaluation, distinguish **available in source** from **runtime-qualified on a concrete path**. This table is intentionally not a transport × protocol cross-product claim.

| Area | Available in current source | Evidence boundary |
| --- | --- | --- |
| Event runtime | Descriptor/timer event loop; `epoll`, `poll`, `select` backends; server/client stream endpoints; connection-local contexts | Exact-head public CI is green; current runtime qualification is narrower than the source surface. |
| Configuration | Typed `SubCommand` hierarchy; API/default, config-file, CLI surfaces; generated inspection/export commands | Used by SNode.C examples and downstream applications; exact option sets depend on concrete endpoint type. |
| Plain streams | IPv4, IPv6, Unix-domain; conditional RFCOMM/L2CAP source paths | Recorded runtime qualification covers IPv4, IPv6, Unix-domain; Bluetooth remains source/build evidence without hardware qualification here. |
| TLS streams | OpenSSL-backed TLS connection layer and TLS configuration | Recorded mutual-TLS IPv4 path; trust, hostname, certificate, and cipher policy remain deployment responsibilities. |
| Web | HTTP/1.0 and HTTP/1.1, Express-style routing/middleware, SSE/EventSource, WebSocket 13 | Protocol and integration tests exist, but breadth differs by family/mode. No HTTP/2 claim. |
| MQTT | MQTT 3.1.1 client/server and MQTT-over-WebSocket components | Packet/lifecycle tests and downstream MQTTSuite qualification; no MQTT 5 claim. |

See [Capabilities](docs/capabilities.md) for the detailed transport, protocol, build, platform, and evidence map.

## Architecture and extension points

A concrete endpoint combines compatible choices for address family, endpoint role, connection mode, and protocol/application context around the shared runtime. The composition is typed; component presence does not mean every theoretical cross-product is built, tested, or deployment-qualified.

The connection/context split also allows a protocol transition without opening a second transport connection. HTTP-to-WebSocket upgrade is the clearest example:

<picture>
  <source media="(max-width: 600px)" srcset="assets/http-websocket-context-switch-mobile.svg">
  <img src="assets/http-websocket-context-switch.svg" width="809" alt="HTTP-to-WebSocket context replacement inside the same established SocketConnection. The HTTP context remains active while the WebSocket replacement is staged; after the current HTTP read callback returns, the HTTP context detaches with ContextSwitch, the staged context is selected and attached, and WebSocket becomes active without replacing the transport connection.">
</picture>

<sub>The replacement is staged first; the active context changes only after the current HTTP read callback returns.</sub>

SSE/EventSource follows a different path: it remains within HTTP rather than replacing the active context. MQTT may attach directly to a stream or compose as a WebSocket subprotocol. The [architecture guide](docs/architecture.md) shows these relationships separately so they are not flattened into a misleading protocol stack.

SNode.C's configuration tree is also extensible. Named endpoints contribute typed sections, applications can add their own `SubCommand` branches, and effective values resolve with this precedence:

**command line > configuration file > API/default**

The [configuration guide](docs/configuration.md) covers the hierarchy, inspection commands, retry versus reconnect, and TLS deployment responsibilities.

## Choose your next step

| If you want to… | Go here |
| --- | --- |
| Understand runtime dispatch, typed endpoint composition, context ownership, upgrades, and protocol relationships | [Architecture](docs/architecture.md) |
| Configure endpoint/application settings, precedence, inspection, retry, reconnect, or TLS | [Configuration](docs/configuration.md) |
| Check exact protocol, transport, build, platform, and qualification scope | [Capabilities](docs/capabilities.md) |
| Inspect classes, namespaces, and generated API documentation | [API reference](https://snodec.github.io/snode.c-doc/html/index.html) |
| Start from an installed-package consumer | [External echo example](https://github.com/SNodeC/snode.c/tree/master/examples/echo) |
| Explore implementation examples | [In-tree applications](https://github.com/SNodeC/snode.c/tree/master/src/apps) |
| Inspect or discuss the project | [Source](https://github.com/SNodeC/snode.c) · [Issues](https://github.com/SNodeC/snode.c/issues) · [Discussions](https://github.com/SNodeC/snode.c/discussions) · [Releases](https://github.com/SNodeC/snode.c/releases) |

SNode.C is the networking foundation for two distinct ecosystem paths. [MQTTSuite](https://github.com/SNodeC/mqttsuite) provides MQTT broker, integration, bridge, CLI, and storage applications. [AISuite](https://github.com/SNodeC/AISuite) provides typed Codex integration and bridging, with [CodexUI](https://github.com/SNodeC/CodexUI) as the native/browser presentation project in that path. These are related projects, not one shared-version distribution or one all-project runtime pipeline.
