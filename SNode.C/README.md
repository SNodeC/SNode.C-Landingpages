<div align="center">

# SNode.C

### Event-driven network applications in modern C++

Build clients, servers, gateways, and protocol services from reusable address,
transport, connection, and application layers.

[Quick start](#quick-start) · [Programming model](#programming-model) ·
[API documentation](https://snodec.github.io/snode.c-doc/html/index.html) ·
[Examples](https://github.com/SNodeC/snode.c/tree/master/src/apps)

</div>

> [!NOTE]
> This page follows current public `master`. The most recently qualified source
> was commit [`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240),
> whose CMake source version is `2.0.0`. That commit is newer than the latest
> public tag; the version number is not a maturity or release-status claim.

## Why SNode.C

Network applications repeatedly solve the same infrastructure problems:
address handling, connection lifecycle, event dispatch, buffering, encryption,
protocol upgrades, configuration, and orderly shutdown. SNode.C provides those
concerns as C++20 building blocks so application code can concentrate on the
protocol and the state attached to each connection.

The framework is organized around a small recurring model. A `SocketServer` or
`SocketClient` owns connection establishment. A `SocketContextFactory` creates
one `SocketContext` for each accepted or established connection. The context
then receives lifecycle and data events through the framework event loop.

## Quick start

The shortest evaluation path builds the supplied IPv4 echo pair. The commands
use a canonical out-of-tree build and an isolated install directory so the same
checkout can be rebuilt incrementally.

Prerequisites are a C++20 compiler, CMake 3.18 or newer, Ninja, OpenSSL,
nlohmann/json, CLI11, and spdlog development packages.

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
export PATH="$PWD/cmake-build-release/src/apps/echo:$PATH"
```

Start the listener in one terminal:

```sh
echoserver-legacy-in echoserver local --host 127.0.0.1 --port 18001
```

Connect from a second terminal:

```sh
echoclient-legacy-in echoclient remote --host 127.0.0.1 --port 18001
```

The server reports a listener on `127.0.0.1:18001`; the client reports a
successful connection and both processes attach an echo context. Stop both with
<kbd>Ctrl</kbd>+<kbd>C</kbd>.

### Change the transport, not the application

The echo applications expose the same context through several compiled network
and stream combinations. These variants were qualified on loopback with the
same source revision:

```sh
cmake --build cmake-build-release --parallel --target \
  echoserver-legacy-in6 echoclient-legacy-in6 \
  echoserver-legacy-un echoclient-legacy-un \
  echoserver-tls-in echoclient-tls-in
```

| Variant | Server endpoint | Client endpoint |
| --- | --- | --- |
| IPv6 stream | `echoserver-legacy-in6 echoserver local --host ::1 --port 18002` | `echoclient-legacy-in6 echoclient remote --host ::1 --port 18002` |
| Unix domain | `echoserver-legacy-un echoserver local --sun-path /tmp/snode-echo.sock` | `echoclient-legacy-un echoclient remote --sun-path /tmp/snode-echo.sock` |
| Mutual TLS over IPv4 | `echoserver-tls-in echoserver local --host 127.0.0.1 --port 18443 tls --cert server.crt --cert-key server.key --ca-cert ca.crt` | `echoclient-tls-in echoclient remote --host 127.0.0.1 --port 18443 tls --cert client.crt --cert-key client.key --ca-cert ca.crt` |

The TLS pair requires separate server and client certificates signed by the CA
named in `--ca-cert`. Do not reuse development keys in deployed systems. Run
`echoserver-tls-in --help=expanded` for certificate, cipher, verification, and
timeout options. The qualified demo did not enable its application-specific SNI
mapping.

## Programming model

```text
SocketServer / SocketClient
            │ establishes a connection
            ▼
 SocketContextFactory
            │ creates one context
            ▼
      SocketContext
            │ lifecycle + data callbacks
            ▼
      application logic
```

An **instance** is a named, configurable client or server endpoint. Its command
line and configuration-file sections describe the local or remote address,
connection limits, socket behavior, and—where applicable—TLS. Applications can
therefore expose several address families or transports without duplicating
their protocol logic.

SNode.C uses an event-driven execution model. That is an architectural fact,
not a performance claim: throughput, latency, memory use, and suitability for a
specific workload still need measurements in that workload.

## Layers and capabilities

| Layer | Current-master source scope | Qualification boundary |
| --- | --- | --- |
| Address families | IPv4, IPv6, Unix domain, Bluetooth RFCOMM, Bluetooth L2CAP | Echo qualification covers IPv4, IPv6, and Unix domain on Linux; Bluetooth needs suitable hardware and a separate run |
| Streams | Plain connection-oriented stream and OpenSSL-backed TLS | Plain and mutual-TLS echo paths were run; not every address/layer combination is asserted |
| Web | HTTP, WebSocket, Express-style routing and upgrades | Component sources and tests exist; consult the API docs for exact targets |
| IoT | MQTT 3.1.1 protocol components and MQTT-over-WebSocket composition | MQTTSuite owns the end-user broker/integration workflows |
| Configuration | API setters, command-line sections, and configuration files | `--help=expanded`, `--show-config`, and `--command-line` expose the effective surface |
| Packaging | Component CMake exports for downstream `find_package` consumers | Current master installed successfully in the recorded qualification environment |

Source availability does not mean that every layer can be combined with every
address family, or that every combination has the same test coverage. Select
the exact CMake components your application needs and verify that combination.

## Choosing the right abstraction

Start at the highest layer that owns the behavior you actually need. Use the
stream socket layer when your application defines its own framing and protocol.
Use HTTP or WebSocket components when their parsers, upgrade lifecycle, and
message boundaries are part of the requirement. Use the MQTT components when
you are implementing an MQTT peer; use MQTTSuite when you want ready-made
broker, integration, bridge, CLI, or storage processes.

Keep connection-local state in a `SocketContext` rather than in a process-wide
callback. Let the factory construct that state when the connection becomes
usable, and treat disconnect/shutdown callbacks as part of the normal
lifecycle. When exposing multiple instances, give each one a stable name so its
address, TLS, retry, timeout, and queue policy remain inspectable.

Configuration defaults are application decisions. A loopback host, unlimited
timeout, reconnect policy, or permissive certificate setting that is useful for
a local example is not automatically appropriate for a deployed service.

## Build and consume

For library development, keep `cmake-build-release` and
`cmake-build-debug` as reusable canonical build directories. Reconfigure when
the compiler, generator, dependency prefix, CMake options, or source revision
changes.

After installation, downstream projects can request SNode.C components with
CMake rather than relying on sibling checkout paths. Component names and
examples are documented in the
[API documentation](https://snodec.github.io/snode.c-doc/html/index.html) and
the repository's [`src`](https://github.com/SNodeC/snode.c/tree/master/src)
tree.

The source requests C++20. The recorded launch qualification used Debian
GNU/Linux forky/sid, x86-64, GCC 16.2.0, CMake 4.3.4, and Ninja 1.13.2. This is
a reproducible observation, not a declaration that other distributions,
compilers, architectures, Android/Termux, or OpenWrt targets are supported.

## Troubleshooting the first build

- If CMake cannot find a dependency, install its development package or pass a
  reviewed prefix through `CMAKE_PREFIX_PATH`; do not point examples at an
  unrelated live checkout.
- If a listener cannot bind, choose an unused port or remove a stale Unix
  socket only after confirming that no process owns it.
- If TLS negotiation fails, verify the CA chain, certificate purpose, private
  key pairing, validity period, and host/SNI policy on both peers. Do not bypass
  verification merely to make the example connect.
- Use `--help=expanded` for the exact compiled instance and
  `--command-line=standard` to print the effective non-default configuration.

For a development checkout, add tests in `cmake-build-debug` and run
`ctest --test-dir cmake-build-debug --output-on-failure`. The launch
qualification above intentionally proves selected echo paths; it is not a
claim that every repository test passed in the same Release directory.

## Ecosystem

SNode.C is the networking foundation for several separate applications and
libraries:

- [MQTTSuite](https://github.com/SNodeC/mqttsuite) builds broker, integration,
  bridge, CLI, and storage applications around MQTT 3.1.1.
- [AISuite](https://github.com/SNodeC/AISuite) adds typed C++ access and a
  multi-client bridge for the Codex app-server protocol.
- [CodexUI](https://github.com/SNodeC/CodexUI) is a native Qt client built on
  AISuite and SNode.C.

These projects have independent versions and responsibilities. Their features
are not automatically SNode.C framework features.

## Project routes

- Read the [API documentation](https://snodec.github.io/snode.c-doc/html/index.html).
- Report reproducible defects in [Issues](https://github.com/SNodeC/snode.c/issues).
- Ask usage questions in [Discussions](https://github.com/SNodeC/snode.c/discussions).
- Inspect [releases](https://github.com/SNodeC/snode.c/releases) before relying
  on packaged artifacts rather than current source.
- Review the dual-license terms: `MIT OR LGPL-3.0-or-later`.

The repository does not currently publish dedicated `SECURITY.md`,
`SUPPORT.md`, or `CONTRIBUTING.md` routes. Until those exist, do not disclose a
security issue in a public ticket if it would expose users; contact the
maintainer through an agreed private channel first.
