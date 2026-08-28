<div align="center">

# CodexUI

### A native Qt interface for visible, multi-client Codex workflows

Navigate threads and turns, submit prompts, follow tool activity and plans,
inspect Git changes, and keep connection state visible while work continues.

[First run](#build-and-first-run) · [Workflow](#the-native-workflow) ·
[Bridge transports](#select-the-bridge-transport-from-the-command-line) ·
[UI behavior](https://github.com/SNodeC/CodexUI/blob/master/docs/ui-behavior.md)

</div>

> [!IMPORTANT]
> CodexUI is an independent open-source application. It is not an official
> OpenAI application. It uses AISuite to communicate with a separately running
> `codex-bridge`, which in turn communicates with the Codex app-server.

This page follows current public `master`. The last qualified source was
[`3632adc`](https://github.com/SNodeC/CodexUI/commit/3632adcf63b287aeec4bfa9da4b2f8881d526d34),
built with AISuite
[`b6b4635`](https://github.com/SNodeC/AISuite/commit/b6b463575b0f587fe9ed97ddd8509050d05bd4ca)
and SNode.C
[`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240).
CodexUI currently declares no project version and has no public tag. Current
master is native Qt only; browser and `1.0` claims are excluded.

## The native workflow

CodexUI presents one normalized view of the app-server state and the local
interaction state needed to use it:

1. connect to a bridge and see whether the client is controller or observer;
2. select an existing thread or create a new one with explicit runtime options;
3. submit a prompt and keep the pending submission visible;
4. observe turns, streaming activity, plans, agents, requests, and tool output;
5. inspect conversation detail and live Git changes without changing the
   command target accidentally;
6. reconnect and resynchronize after a provider or transport interruption.

The UI distinguishes the command **target**, the target's **active turn**,
threads with **running** background work, and the currently
**selected/inspected** item. Those states may refer to different threads. This
prevents navigation from silently redirecting an action.

## Build and first run

Build and install current SNode.C and AISuite first. CodexUI requires C++20,
Qt 6 Widgets, Threads, libgit2, CMake, and the installed dependency prefix.

```sh
git clone https://github.com/SNodeC/CodexUI.git
cd CodexUI

cmake -S . -B cmake-build-release -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_PREFIX_PATH=/path/to/snode-and-aisuite-install \
  -DCMAKE_INSTALL_PREFIX="$PWD/cmake-install-release"
cmake --build cmake-build-release --parallel
ctest --test-dir cmake-build-release --output-on-failure
cmake --install cmake-build-release
```

Start AISuite's `codex-bridge` in another terminal, then launch the installed
application:

```sh
./cmake-install-release/bin/codex-ui
```

The default connection is the bridge's runtime Unix-domain socket. The status
area should progress through connecting to connected when the bridge is
available. Select or create a thread, submit a non-sensitive evaluation prompt,
and confirm that the pending card and resulting activity appear. Conversation
availability and model operations depend on the selected Codex home,
authentication, and app-server state.

At the qualified commits, the build passed all seven CTest targets: socketpair
contract, presentation pipeline, conversation projection, conversation cards,
application layout, live Git changes, and shell integration. Installation
produced `codex-ui`, the scalable application icon, and the desktop entry.

## Select the bridge transport from the command line

CodexUI uses SNode.C's named client instances. Exactly one outgoing bridge
transport must be enabled. Unix is enabled by default; when choosing another
transport, disable `codex-ui-unix` and enable the selected instance.

### Unix-domain socket

Use the runtime default simply with `codex-ui`, or set an explicit path:

```sh
codex-ui codex-ui-unix remote --sun-path /tmp/codex-bridge.sock
```

### IPv4 stream

```sh
codex-ui \
  codex-ui-unix --disabled \
  codex-ui-ipv4 --disabled=false \
  remote --host 127.0.0.1 --port 4500
```

The bridge must expose the matching frontend listener:

```sh
codex-bridge \
  codex-bridge --disabled \
  codex-bridge-ipv4 --disabled=false \
  local --host 127.0.0.1 --port 4500
```

### IPv6 stream

```sh
codex-ui \
  codex-ui-unix --disabled \
  codex-ui-ipv6 --disabled=false \
  remote --host ::1 --port 4500
```

### WebSocket over IPv4

```sh
codex-ui \
  codex-ui --bridge-websocket-endpoint /codex \
  codex-ui-unix --disabled \
  codex-ui-websocket-ipv4 --disabled=false \
  remote --host 127.0.0.1 --port 4502
```

Enable `codex-bridge-websocket-ipv4` on the bridge at the same address and
port. IPv6 WebSocket uses the corresponding `*-websocket-ipv6` instances.

Compiled builds can also expose IPv4/IPv6 TLS, WSS, RFCOMM, and RFCOMM TLS
instances. TLS and WSS require matching CA verification and certificate/key
options on the bridge and client; selecting an instance does not configure
trust automatically. Inspect the exact build with:

```sh
codex-ui --help=expanded
codex-ui --command-line=standard
```

The connection dialog can change the selected compiled transport and endpoint
for the current session. Command-line configuration remains the reproducible
way to define startup behavior.

## Architecture

```text
Qt GUI thread
    │ normalized bounded JSONL
    ▼
nonblocking Unix socketpair
    │
    ▼
SNode.C client thread ── selected transport ──► AISuite codex-bridge
                                                     │
                                                     ▼
                                              Codex app-server
```

Qt owns widgets and presentation state. The SNode.C thread owns the external
transport and AISuite frontend connection. A bounded, nonblocking Unix
socketpair separates the two ownership graphs inside the process. The external
transport can be Unix, IP stream, TLS, WebSocket, WSS, or RFCOMM where compiled;
changing it does not change normalized UI semantics.

AISuite owns typed protocol adaptation and bridge routing. The app-server owns
conversation semantics and persistence. CodexUI does not maintain an implicit
long-term conversation cache to fill gaps when the provider cannot materialize
history.

## Behavior, privacy, and limits

| Area | Current native behavior | Boundary |
| --- | --- | --- |
| Threads and turns | Normalized hierarchy, target/active/running/selected distinctions | Provider data remains authoritative |
| Prompt admission | Local pending state makes accepted submissions visible | Delivery or completion is not invented when disconnected |
| Activity | Plans, agents, requests, tool output, diagnostics, and Git changes have dedicated presentation paths | Rendering depends on messages actually received |
| Reconnect | Visible failure/retrying states and explicit resynchronization | Reconnect is not local conversation persistence |
| Multi-client use | Controller/observer state comes from AISuite bridge events | Observers cannot be described as equivalent controllers |
| Browser | Not present on current master | No native/browser parity or hosted deployment claim |

There is no CodexUI-specific bearer-token layer for bridge access. Loopback or
Unix defaults reduce exposure but do not replace endpoint permissions, TLS
verification, network controls, Codex authentication, and log/privacy review.
Screenshots and bug reports must exclude private prompts, repository secrets,
tokens, personal paths, and conversation history.

The recorded build used Debian GNU/Linux forky/sid, x86-64, GCC 16.2.0, Qt
6.10.2, and libgit2 1.9.7. This does not establish a broad Linux distribution,
desktop, architecture, or package support matrix.

## Interaction and recovery model

A prompt card becomes locally pending when CodexUI admits the submission. It
remains distinguishable from provider-confirmed user input and from a completed
turn. If a submission is rejected or the connection fails, the UI reports that
state instead of synthesizing a successful response. Tool requests and other
items that require attention remain visible in their owning thread.

Selecting a thread is an inspection action. Changing the command target is a
separate decision, particularly while another thread has a running turn. The
interface keeps those distinctions visible so a user can inspect background
work and return without redirecting the next command unintentionally.

Transport loss produces a disconnected, retrying, or failure state. Reconnect
creates a fresh frontend attachment and resynchronizes from provider data. It
does not prove that CodexUI persisted missing conversation history locally.
When the provider reports that items are not loaded or cannot materialize an
older thread, the UI must surface that limitation.

## Evaluate the real desktop safely

Use a disposable workspace containing synthetic files and a non-sensitive
prompt. Exercise connect, thread creation/selection, prompt admission, visible
activity, a Git diff, disconnect, reconnect, and orderly shutdown. Verify that
the target, active turn, running indicators, and selected inspector remain
correct throughout.

Before taking a launch screenshot, replace account and repository identifiers,
remove tokens and personal paths, clear unrelated history, and confirm that all
visible state came from the qualified build. Capture light and dark themes at a
repeatable window size, but keep every workflow understandable in Markdown when
the image is unavailable.

If the UI cannot connect, first print the effective configuration with
`--command-line=standard`. Confirm that exactly one transport is enabled and
that its path/host/port matches the bridge listener. For TLS/WSS, verify the CA
and certificate chain; for Unix sockets, verify runtime-directory ownership and
that no stale listener is being mistaken for a running bridge.

## Project routes

- Read the [architecture](https://github.com/SNodeC/CodexUI/blob/master/docs/codex-architecture.md)
  and [UI behavior](https://github.com/SNodeC/CodexUI/blob/master/docs/ui-behavior.md).
- Inspect [Issues](https://github.com/SNodeC/CodexUI/issues) and
  [releases](https://github.com/SNodeC/CodexUI/releases).
- Review AISuite's [bridge contract](https://github.com/SNodeC/AISuite/blob/master/src/ai/openai/codex/docs/architecture.md).
- Review the dual-license terms: `LGPL-3.0-or-later OR MIT`.

Dedicated public security, support, and contribution policy files are not yet
present. Do not include sensitive workspace or account data in a public issue.
