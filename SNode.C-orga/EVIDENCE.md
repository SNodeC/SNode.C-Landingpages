# SNode.C organization-profile evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

The organization profile derives its technical summaries from the four product
registers. It does not broaden a product claim or use an architecture figure as
a substitute for accessible navigation.

## Entry ledger

| Entry | Eligible role statement | Evidence source | Current qualification |
| --- | --- | --- | --- |
| SNode.C | C++20 networking foundation for event-driven clients and servers | [`SNode.C/EVIDENCE.md`](../SNode.C/EVIDENCE.md) | Build/install plus selected plain and TLS echo paths qualified |
| MQTTSuite | Five-application MQTT 3.1.1 integration toolkit built on SNode.C | [`MQTTSuite/EVIDENCE.md`](../MQTTSuite/EVIDENCE.md) | Five executables built; broker/CLI QoS 1 flow qualified |
| AISuite | C++ Codex app-server integration and multi-client bridge | [`AISuite/EVIDENCE.md`](../AISuite/EVIDENCE.md) | 26/26 tests passed; TypeScript excluded on master |
| CodexUI | Native Qt 6 interface using AISuite and SNode.C | [`CodexUI/EVIDENCE.md`](../CodexUI/EVIDENCE.md) | Build/install and 7/7 tests passed; browser and 1.0 excluded |

## Relationship evidence

- MQTTSuite CMake requires SNode.C 2.0.0 components.
- AISuite CMake requires SNode.C 2.0 components.
- CodexUI CMake requires AISuite and SNode.C 2.0 components.
- No source evidence creates an MQTTSuite → AISuite/CodexUI runtime path.

The organization page may therefore show the two approved evaluation tracks,
but must not imply a single four-product pipeline. Current-master compilation
and the core CLI/test paths are qualified at the exact recorded SHAs. Final
sanitized product screenshots and authenticated UI capture remain pending.

## Navigation and public-route facts

The four public repositories and their Issues routes are reachable. SNode.C and
MQTTSuite have hosted API documentation; AISuite and CodexUI currently rely on
repository documentation. No shared security, support, or contribution policy
file was found. Organization description, pins, contact, website, Discussions,
and final publication metadata remain open until checked at publication time.

## Profile publication gate

- Every project entry uses the same fields and visual weight.
- Version/maturity labels come directly from `FACTS.md`, including `Open` where
  policy is absent.
- Demo links point only to qualified current-master workflows.
- Codex-related entries carry the independent-project notice.
- A hypothetical fifth project fits the category directory without redesign.
- Product repository, docs, support, security, contribution, and license links
  are checked immediately before publication.
