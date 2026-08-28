<div align="center">

# CodexUI

### Native Qt and browser interfaces for visible, multi-client Codex workflows

Navigate threads and turns, submit prompts, follow tool activity and plans,
inspect Git changes, and keep connection state visible while work continues.

[First run](#build-and-first-run) · [Workflow](#one-workflow-two-presentations) ·
[Bridge transports](#select-the-bridge-transport-from-the-command-line) ·
[Native behavior](https://github.com/SNodeC/CodexUI/blob/master/docs/ui-behavior.md) ·
[Web contract](https://github.com/SNodeC/CodexUI/blob/master/docs/web-1.0-contract.md)

</div>

> [!IMPORTANT]
> CodexUI is an independent open-source application. It is not an official
> OpenAI application. It uses AISuite to communicate with a separately running
> `codex-bridge`, which in turn communicates with the Codex app-server.

This page follows current public `master`. The last qualified source was
[`8791923`](https://github.com/SNodeC/CodexUI/commit/8791923e5475e39222ea4fc7674ca623bc02b4de),
with the native build qualified against AISuite
[`c3cce28`](https://github.com/SNodeC/AISuite/commit/c3cce28d813b4f48376a2a0c6ac74131bf443f65)
and SNode.C
[`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240).
CodexWebUI pins AISuite SDK
[`5aeedb2`](https://github.com/SNodeC/AISuite/commit/5aeedb2c21d7da0d611219365294cc3fb052cddf).
Native CMake and the private CodexWebUI manifest declare source version `1.0.0`,
but no public tag or GitHub release exists. The browser artifact is reproducibly
buildable from source; this evidence does not make it a published release.

## One workflow, two presentations

The native Qt application and CodexWebUI present the same normalized app-server
and local interaction model. The native application connects through SNode.C;
the browser uses AISuite's TypeScript SDK over the bridge's `/codex` WebSocket.
Both let a user:

1. connect to a bridge and see whether the client is controller or observer;
2. select an existing thread or create a new one with explicit runtime options;
3. submit a prompt and keep the pending submission visible;
4. observe turns, streaming activity, plans, agents, requests, and tool output;
5. inspect conversation detail and live Git changes without changing the
   command target accidentally;
6. reconnect and resynchronize after a provider or transport interruption.

Each presentation distinguishes the command **target**, the target's **active turn**,
threads with **running** background work, and the currently
**selected/inspected** item. Those states may refer to different threads. This
prevents navigation from silently redirecting an action.

## Build and first run

### Install dependencies

These Debian/Ubuntu packages cover CodexUI's direct CMake requirements and the
base packages consumed through installed AISuite and SNode.C targets:

```sh
sudo apt update
sudo apt install --yes \
  build-essential ca-certificates cmake git ninja-build pkgconf \
  libssl-dev nlohmann-json3-dev qt6-base-dev libgit2-dev
```

The Git dependency is **libgit2**, supplied by `libgit2-dev`; there is no
`libgit3-dev` requirement. `qt6-base-dev` supplies Qt 6 Widgets and pulls its
matching base development tools. CMake's Threads package is provided by the
compiler and system C library rather than a separate Debian package.

The following packages are optional for compiling CodexUI, but required when
the associated end-to-end path is selected:

```sh
# Optional bridge transport/runtime tools. Rebuild SNode.C and AISuite after
# adding Bluetooth support; openssl supports TLS certificate setup.
sudo apt install --yes libbluetooth-dev openssl

# Optional for the CodexUI build; required behind codex-bridge for a real
# app-server workflow. Use a managed Node/npm installation.
sudo apt install --yes npm
npm install --global --prefix "$HOME/.local" @openai/codex
export PATH="$HOME/.local/bin:$PATH"
codex --version
```

Build and install current SNode.C and AISuite first, using the same dependency
prefix or listing both prefixes in `CMAKE_PREFIX_PATH`. CodexUI's CMake files do
not discover Doxygen or IWYU, so neither is a CodexUI build dependency.

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

## CodexWebUI artifact

`web/` contains the React/TypeScript browser presentation and records its exact
AISuite SDK revision. Its release task builds TypeScript, runs seven web test
files, profiles the presentation model, creates a relocatable Vite bundle, and
verifies the artifact. At the qualified head, all 30 Node test cases passed and
`web/app-dist/` contained a generated entry page plus two non-empty assets.

CMake can install that prebuilt directory at `share/codexui/web`.
`codex-bridge` then serves the static files and `/codex` WebSocket from one
listener; no Node process runs in the installed deployment. The browser has no
bridge router, controller authority, persistent Codex state, or implied access
to provider-side paths. The exact build layout, native/browser contract, and
exceptions are maintained in the linked web documentation.

This is release-candidate evidence, not proof of a downloadable or hosted
release. A full npm audit reports five build-tool findings—four high and one
moderate—while `npm audit --omit=dev` reports none for production dependencies.
The build-tool findings still require review before release.

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
Native Qt: GUI ── bounded JSONL ── SNode.C/AISuite client ─┐
                                                           ├─► codex-bridge
Browser: React presentation ── AISuite TypeScript SDK ─────┘        │
                                                                    ▼
                                                             Codex app-server
```

In the native process, Qt owns widgets and presentation state while a SNode.C
thread owns the external transport and AISuite connection; a bounded,
nonblocking Unix socketpair separates them. The browser owns its React
presentation and connects directly to the same bridge through AISuite's typed
WebSocket lifecycle. It does not reproduce the native process boundary.

AISuite owns typed protocol adaptation and bridge routing. The app-server owns
conversation semantics and persistence. CodexUI does not maintain an implicit
long-term conversation cache to fill gaps when the provider cannot materialize
history.

## Behavior, privacy, and limits

| Area | Qualified behavior | Boundary |
| --- | --- | --- |
| Threads and turns | Normalized hierarchy, target/active/running/selected distinctions | Provider data remains authoritative |
| Prompt admission | Local pending state makes accepted submissions visible | Delivery or completion is not invented when disconnected |
| Activity | Plans, agents, requests, tool output, diagnostics, and Git changes have dedicated presentation paths | Rendering depends on messages actually received |
| Reconnect | Visible failure/retrying states and explicit resynchronization | Reconnect is not local conversation persistence |
| Multi-client use | Controller/observer state comes from AISuite bridge events | Observers cannot be described as equivalent controllers |
| Browser | Shared normalization, presentation, prompt, settings, request, reconnect, and viewport behavior covered by seven web test files | Equality is behavioral, not pixel identity; native-only exceptions remain documented |

There is no CodexUI-specific bearer-token layer for bridge access. Loopback or
Unix defaults reduce exposure but do not replace endpoint permissions, TLS
verification, network controls, Codex authentication, and log/privacy review.
Screenshots and bug reports must exclude private prompts, repository secrets,
tokens, personal paths, and conversation history.

The recorded build used Debian GNU/Linux forky/sid, x86-64, GCC 16.2.0, Qt
6.10.2, libgit2 1.9.7, Node 24.19.0, and npm 11.16.0. The native 7/7 and web
30/30 tests passed. This does not establish a broad platform, browser, or
package support matrix.

## Interaction and recovery model

A locally pending prompt remains distinct from provider-confirmed input and a
completed turn; rejection or disconnect never becomes synthetic success.
Inspection also remains separate from the command target, so viewing background
work does not redirect the next command.

Transport loss produces visible disconnected, retrying, or failure state.
Reconnect creates a fresh attachment and resynchronizes provider data; it is not
local conversation persistence. Unavailable provider history stays unavailable.

## Evaluate the real desktop safely

Evaluate with synthetic files and a non-sensitive prompt. Exercise connect,
thread selection, prompt admission, activity, Git change, disconnect, reconnect,
and shutdown while checking target/active/running/inspected distinctions. Remove
identities, tokens, personal paths, and unrelated history from captures.

For connection failures, print `--command-line=standard`, confirm exactly one
transport and a matching bridge endpoint, then check the TLS chain or Unix
runtime-directory ownership as applicable.

## Project routes

- Read the [architecture](https://github.com/SNodeC/CodexUI/blob/master/docs/codex-architecture.md)
  and [UI behavior](https://github.com/SNodeC/CodexUI/blob/master/docs/ui-behavior.md).
- Review the [web 1.0 contract](https://github.com/SNodeC/CodexUI/blob/master/docs/web-1.0-contract.md),
  [qualification](https://github.com/SNodeC/CodexUI/blob/master/docs/web-qualification.md),
  and [release gate](https://github.com/SNodeC/CodexUI/blob/master/docs/web-release.md).
- Inspect [Issues](https://github.com/SNodeC/CodexUI/issues) and
  [releases](https://github.com/SNodeC/CodexUI/releases).
- Review AISuite's [bridge contract](https://github.com/SNodeC/AISuite/blob/master/src/ai/openai/codex/docs/architecture.md).
- Review the dual-license terms: `LGPL-3.0-or-later OR MIT`.

Dedicated public security, support, and contribution policy files are not yet
present. Do not include sensitive workspace or account data in a public issue.
