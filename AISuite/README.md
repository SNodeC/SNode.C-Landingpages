<div align="center">

# AISuite

### Typed C++ access and multi-client routing for the Codex app-server

Connect native clients through one bounded bridge without making every
application implement raw JSON-RPC, correlation, and transport adaptation.

[Quick start](#quick-start) · [Transport model](#two-independent-transport-boundaries) ·
[Architecture](https://github.com/SNodeC/AISuite/blob/master/src/ai/openai/codex/docs/architecture.md) ·
[C++ source](https://github.com/SNodeC/AISuite/tree/master/src/ai/openai/codex)

</div>

> [!IMPORTANT]
> AISuite is an independent open-source project. It is not an official OpenAI
> SDK or product. Codex and the Codex app-server define the upstream protocol
> semantics; AISuite adapts and presents that protocol to C++ consumers.

Current public `master` is a C++20 implementation. The most recently qualified
source was [`b6b4635`](https://github.com/SNodeC/AISuite/commit/b6b463575b0f587fe9ed97ddd8509050d05bd4ca),
whose CMake source version is `0.7.0`, built against SNode.C
[`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240).
There is no tagged AISuite release on this baseline. TypeScript and npm-package
claims are intentionally excluded because those sources are not on `master`.

## What AISuite provides

| Surface | Responsibility |
| --- | --- |
| `AISuite::OpenAICodex` | Installed CMake target for typed asynchronous C++ integration |
| Generated protocol views | Typed access to recorded protocol shapes while retaining lossless `getRaw()` JSON access |
| `codex-bridge` | One provider connection, bounded framing/queues, frontend routing, and controller/observer coordination |
| `codex-bridge-client` | Interactive reference client for inspection, safe reads, thread operations, and raw JSON-RPC escape-path evaluation |
| Acceptance tests | Deterministic and real-app-server coverage across provider and frontend transports |

The bridge does not become a second conversation database. The app-server owns
protocol meaning and persistence. AISuite owns transport adaptation, transient
routing/correlation state, controller assignment, and the explicitly bounded
telemetry described in its architecture contract.

## Quick start

Build and install SNode.C first. Then build AISuite in a canonical reusable
directory and run its qualified transport suite:

```sh
git clone https://github.com/SNodeC/AISuite.git
cd AISuite

cmake -S . -B cmake-build-release -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_PREFIX_PATH=/path/to/snode-install \
  -DCMAKE_INSTALL_PREFIX="$PWD/cmake-install-release" \
  -DAISUITE_BUILD_APPS=ON \
  -DAISUITE_BUILD_CODEX_TESTS=ON
cmake --build cmake-build-release --parallel
ctest --test-dir cmake-build-release --output-on-failure
cmake --install cmake-build-release
```

At the qualified commits, this runs 26 tests. They cover framing, typed frontend
access, routing, stdio provider behavior, stream and WebSocket frontend paths,
TLS/WSS frontend paths, and nine real-app-server end-to-end cases.

For an interactive local evaluation, ensure the `codex` executable is on
`PATH`, then start the bridge in terminal 1:

```sh
./cmake-build-release/src/apps/codex-bridge/codex-bridge \
  --log-level 4 \
  codex --app-server-transport stdio
```

The default provider mode launches and owns `codex app-server`; the default
frontend listener is a private runtime Unix-domain socket. In terminal 2:

```sh
./cmake-build-release/src/apps/codex-bridge-client/codex-bridge-client \
  --log-level 4 codex-client
```

After `connected using Unix JSONL`, enter `threads` for a harmless list request,
then `quit`. The result depends on the selected Codex home and authentication
state; an empty list is valid. Avoid using real prompts or credentials in
screenshots and logs.

## Two independent transport boundaries

AISuite has two directions with different capabilities. They must not be merged
into one generic transport claim.

### 1. `codex-bridge` → Codex app-server

Select this boundary with the `codex` application option:

| Provider mode | Bridge argument | Ownership and wire path |
| --- | --- | --- |
| stdio | `codex --app-server-transport stdio` | Bridge launches `codex app-server`; JSONL over child stdin/stdout |
| Unix | `codex --app-server-transport unix` | Bridge connects to an independently started app-server WebSocket on the default Unix endpoint |
| IPv4 | `codex --app-server-transport websocket-ipv4` | Bridge connects to app-server WebSocket on `127.0.0.1:4501` by default |
| IPv6 | `codex --app-server-transport websocket-ipv6` | Bridge connects to app-server WebSocket on `[::1]:4501` by default |

External modes require an independently managed `codex app-server --listen`
endpoint matching the selected address. Current app-server listener evidence
contains `stdio://`, `unix://`, and `ws://` forms, not `wss://`. AISuite does
not claim provider-side TLS.

### 2. CodexUI/reference clients → `codex-bridge`

The bridge registers named listener instances. Unix is enabled by default;
other compiled instances are disabled until explicitly selected.

| Frontend listener | Bridge command fragment | Matching reference-client instance |
| --- | --- | --- |
| Unix stream | `codex-bridge` (default) | `codex-bridge-client-unix` (default) |
| IPv4 stream | `codex-bridge --disabled codex-bridge-ipv4 --disabled=false local --host 127.0.0.1 --port 4500` | `codex-bridge-client-ipv4 --disabled=false remote --host 127.0.0.1 --port 4500` |
| IPv6 stream | `codex-bridge --disabled codex-bridge-ipv6 --disabled=false local --host ::1 --port 4500` | `codex-bridge-client-ipv6 --disabled=false remote --host ::1 --port 4500` |
| WebSocket | enable `codex-bridge-websocket-ipv4` or `-ipv6` | enable the matching `codex-bridge-client-websocket-*` instance |
| TLS / WSS | enable the matching `tls-*` or `wss-*` listener | configure CA verification and client credentials on the matching client |

When selecting an alternative, disable the default Unix instance and enable
exactly one client instance. Use each binary's `--help=expanded` and
`--command-line=standard` output to confirm the effective address, path,
certificate, timeout, retry, and queue settings. TLS protects the transport; it
does not add application authentication or change controller authority.

## Architecture and authority

```text
native C++ client ─┐
CodexUI ───────────┼─ frontend envelopes ─► codex-bridge
observer client ───┘                         │
                                             │ native app-server JSON-RPC
                                             ▼
                                      Codex app-server
```

The first frontend can become controller when the default policy is enabled.
Additional frontends are observers; explicitly classified reads can be allowed
by policy. Mutating operations remain controller-governed. The bridge routes
responses and notifications but does not reinterpret app-server semantics.

All exposed boundaries are bounded: encoded message size, app-server input
queue, transport write queues, parser limits, retained diagnostics, and work per
event-loop pass. Bounds reduce uncontrolled resource growth; they are not a
complete security model.

## Typed protocol access

Generated C++ views are derived from recorded schema and operation inputs.
Their manifest stores source hashes, and equality tests guard typed/raw
behavior. Typed APIs are the primary integration path; `getRaw()` preserves the
original JSON when a consumer needs fields outside a current view. A raw
JSON-RPC submission path exists as an escape hatch, not as a substitute for the
typed surface.

The manifest does not name a universal compatible Codex release. Re-run
generation and equality/acceptance tests whenever the upstream schema or Codex
CLI changes.

## Client integration lifecycle

A native consumer links the installed `AISuite::OpenAICodex` target, creates a
frontend connection over one selected transport, registers typed response and
notification handlers, and submits requests only after attachment. Callbacks
are asynchronous: application state must distinguish admission, transport
delivery, app-server response, and later notifications instead of treating a
queued write as completed work.

Use typed views for known operations and retain raw JSON only where forward
compatibility or diagnostics require it. Preserve correlation identifiers and
handle unknown fields without rewriting the provider message. On disconnect,
keep authoritative state until an explicit remove or replacement event says
otherwise; a temporary loss of discovery is not evidence that the underlying
thread disappeared.

For multi-client use, design controller changes explicitly. Observers may
inspect allowed state, but a UI should never hide whether it currently owns
mutation authority. Test provider loss, frontend loss, reconnect, duplicate
requests, oversized messages, slow consumers, and shutdown while requests are
outstanding.

## Qualification and limits

The recorded launch build used Debian GNU/Linux forky/sid, x86-64, GCC 16.2.0,
CMake 4.3.4, Ninja 1.13.2, and the installed SNode.C head above. All 26
configured tests passed and both applications installed. This is exact-revision
evidence, not a broad platform or maturity claim.

Remote listener exposure needs an explicit trust design. AISuite does not add a
bearer-token authentication layer to the frontend protocol. Bind addresses,
TLS verification, network access controls, Codex credentials, logs, and process
ownership must be reviewed together.

## Troubleshooting and evaluation hygiene

- If `codex-bridge` cannot create its runtime socket, check runtime-directory
  ownership and permissions rather than moving the listener to a public bind.
- If stdio startup closes immediately, run the configured `codex` executable
  directly and verify that its selected `CODEX_HOME` is writable and valid.
- If a WebSocket provider does not connect, match the app-server `--listen`
  address to the selected Unix/IPv4/IPv6 mode; provider-side WSS is not present.
- If a frontend connects but cannot mutate, inspect controller/observer events
  before retrying the operation.
- Use JSON output from the reference client for automation, but sanitize it
  before retaining logs or attaching evidence.

## Project routes

- Read the complete [architecture contract](https://github.com/SNodeC/AISuite/blob/master/src/ai/openai/codex/docs/architecture.md).
- Inspect [Issues](https://github.com/SNodeC/AISuite/issues) and
  [releases](https://github.com/SNodeC/AISuite/releases).
- Use [CodexUI](https://github.com/SNodeC/CodexUI) as the native visual client.
- Review the dual-license terms: `MIT OR LGPL-3.0-or-later`.

Dedicated public security, support, and contribution policy files are not yet
present. Do not publish credentials, private prompts, conversation data, or
remote endpoint details in an issue.
