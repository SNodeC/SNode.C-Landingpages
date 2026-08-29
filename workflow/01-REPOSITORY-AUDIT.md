# Step 1 — Repository audit

**Audit date:** 29 August 2026

**Workspace revision:** `3b17362` (`main`)

**Scope:** all 73 tracked files: 29 Markdown files, 11 PNGs, 24 SVGs, and
9 capture/generation scripts.

This is a classification of the current landing-page workspace, not a fresh
technical qualification of the four live repositories. The recorded product
evidence was observed on 28 August 2026 and must be refreshed when a public
`master` head changes.

## Overall finding

The repository contains a strong technical research layer and a weakly
separated presentation layer. Preserve the fact registers, claim ledgers,
qualification results, exact revisions, tested command paths, and capture
automation. Rebuild the five READMEs and the visual system rather than editing
their current prose and graphics into a new design.

The root and scoped `AGENTS.md` files and
[`README-WORKFLOW.md`](README-WORKFLOW.md) remain governing instructions, not
public-copy inputs. Their product boundaries, terminology, misconceptions, and
open facts are nevertheless valuable checklists for later technical review.

## KEEP AS RESEARCH

| Material | Value to preserve | Qualification or limitation |
| --- | --- | --- |
| [`FACTS.md`](../FACTS.md) | Best shared source: exact reviewed SHAs and dates; source-version versus release distinctions; all-master compatibility result; qualified Debian/GCC/CMake/Ninja environment; dependency roles; license expressions; public routes; and shared launch gaps. | Snapshot dated 28 August 2026. It proves the named revisions in one environment, not current moving heads, a support matrix, maturity, or release compatibility. |
| `SNode.C/EVIDENCE.md` | Claim IDs `SN-01`–`SN-13`, implementation anchors, selected echo qualification, configuration model, HTTP-to-WebSocket context replacement, and explicit excluded claims. | IPv4, IPv6, Unix-domain, and one mutual-TLS IPv4 echo path ran. The complete CTest suite and broader family/platform matrix were not qualified by this pass. |
| `MQTTSuite/EVIDENCE.md` | Five executable/application identities, exact SNode.C dependency, genuine QoS 1 broker/subscriber/publisher run, dependency/submodule facts, and the MQTTSuite license-text defect. | No MQTTSuite test directory or build/test CI job exists at the baseline. Mapping, bridge, loop, storage, transport matrix, and most MQTT behavior remain runtime-pending. |
| `AISuite/EVIDENCE.md` | C++ and TypeScript surfaces, 27/27 C++ and 20/20 TypeScript results, install/package dry-run, tested provider/frontend transport distinction, bridge authority boundaries, static Web UI routing, and npm-publication check. | The terminal proof uses a synthetic provider. The source manifest does not identify an exact Codex app-server revision; authentication, remote exposure, maturity, and release policy remain open. |
| `CodexUI/EVIDENCE.md` | Native 7/7 and web 30/30 results, all-master native build/install, exact pinned web SDK, static-artifact verification, native/browser boundary, transport parsing, and license/dependency facts. | No public tag/release or broad platform/browser matrix. The full npm audit has four high and one moderate build-tool findings; the production-dependency audit is clear. Authenticated live acceptance is pending. |
| `SNode.C-orga/EVIDENCE.md` | Concise eligible role statements and build/runtime relationships for the four products. It explicitly rejects an MQTTSuite → AISuite/CodexUI runtime path. | Organization metadata, policies, maturity labels, and final public routes remain open. |
| `SNode.C/docs/{architecture,capabilities,configuration}.md` | Useful source-linked technical analysis: object ownership, event/runtime layers, context replacement, configuration precedence, evidence vocabulary, dependencies, and deployment cautions. | These are commit-pinned research documents, not automatically maintained public docs. Revalidate their source anchors and decide later where deep documentation should live. |
| Capture automation and fixtures under `*/assets/src/` and `shared/assets/src/` | Reproducible command shapes, Xvfb isolation, synthetic data, 2× capture intent, and real-process evidence. Preserve especially the echo, MQTT, AISuite, native CodexUI, browser, and synthetic app-server scripts. | They are not self-contained qualification manifests: several assume prebuilt binaries, a running bridge/browser debugger, fixed displays/ports, sleeps, and external orchestration. Add revision/toolchain/fixture manifests before reuse. |

### Research to extract from the current README files

The README files themselves are classified as **REPLACE**, but do not lose
these already-researched elements while replacing them:

- `SNode.C/README.md`: the echo command sequence; the
  `SocketServer`/`SocketClient` → `SocketContextFactory` → `SocketContext`
  explanation; the Node.js non-compatibility boundary; and source-versus-tested
  capability distinctions.
- `MQTTSuite/README.md`: exact five-application names and roles; the isolated
  broker/MQTTCli QoS 1 commands and expected result; MQTT 3.1.1 scope; and the
  absence of application tests/CI.
- `AISuite/README.md`: the provider-side versus frontend-side transport split;
  controller/observer and persistence boundaries; the source-only TypeScript
  package status; and the harmless reference-client evaluation shape.
- `CodexUI/README.md`: the native/browser product distinction; target, active,
  running, and inspected state; reconnect-versus-persistence boundary; install
  result; and build-tool audit status.
- `SNode.C-orga/README.md`: category-based navigation, equal project roles,
  two separate demo tracks, and the independent-project notice.

These items should be sourced from `FACTS.md`/`EVIDENCE.md` in later steps,
not copied from README prose.

## KEEP BUT REWORK

| Material | Keep | Rework |
| --- | --- | --- |
| [`PAGE-SYSTEM.md`](../PAGE-SYSTEM.md) | Editorial standard, image-independent comprehension, restrained badges, screenshot hygiene, diagram semantics, synthetic data, separate MQTT/Codex tracks, accessible organization navigation, and product-specific centerpieces. | Treat the fixed nine-section/word-count/V1–V4 system as a prior design proposal, not an unquestioned creative answer. The canonical workflow asks Step 4 to choose a reader journey and 2–3 meaningful visuals. This conflict requires an explicit decision before design work. |
| Five `PROPOSAL.md` files | Audience questions, boundaries, terminology, centerpieces, primary first-success ideas, acceptance checks, and open decisions are valuable briefs. | They repeat page architecture, implementation sequence, exact filenames/placements, section counts, and generic hero rules. Reduce each later to product-specific requirements after ecosystem positioning and current technical facts are settled. |
| Six evidence screenshots: `echo-terminal.png`, `quick-start-terminal.png`, `broker-web-ui.png`, `bridge-terminal.png`, `codexui-hero.png`, and `first-workflow.png` | They derive from real qualified binaries or real UI builds using synthetic state; dimensions are consistently 1600×900. Preserve them and their scripts as provenance/reference. | Recapture from refreshed heads. Terminal composites are log-dense or mostly empty and too small at GitHub width. AISuite displays synthetic `/workspace/...` values. CodexUI captures show workspace-like paths, loopback endpoints, and a personal footer. The broker UI is useful real-product evidence but still needs freshness, state, theme, and privacy review. |
| Five editable social-preview SVG sources | Correct 1280×640 target and a reusable accent concept. | Identity marks, tag pills, headlines, and palette remain provisional and visually generic; redesign after positioning. |

## REPLACE

### Public-copy drafts

Replace all five working landing pages in their later workflow stages:

- `SNode.C/README.md`;
- `MQTTSuite/README.md`;
- `AISuite/README.md`;
- `CodexUI/README.md`;
- `SNode.C-orga/README.md`.

They are credible technical drafts, but they predate the canonical restart and
mix landing-page copy with qualification bookkeeping, dependency inventories,
deployment cautions, and manual-like transport/configuration detail. SNode.C is
especially long; the other product pages still inherit the same rigid template.
Their structure, headlines, and wording must not become hidden constraints on
Step 4 or Step 6.

### Exported presentation assets

Replace the 19 page-facing SVG figures and all five social-preview PNGs. The
current figures use one dark, card-based boxes-and-arrows template, carry too
much small text, and make four technically different products look like one
generic diagram family. Several semantics are useful, but those semantics
belong in the later visual specification, not in the existing composition.

This includes the organization hero/product marks/architecture/routes; all
product heroes and architecture/detail diagrams; and the extra SNode.C
configuration/context-upgrade figures. Do not assume the current initials,
colors, headlines, box hierarchy, or exact filenames are approved brand work.

## REMOVE/ARCHIVE

Nothing is to be removed during Step 1. The following material should be
excluded from future landing-page reasoning and archived only after its useful
facts or provenance have been migrated:

- [`LAUNCH-ROADMAP.md`](../LAUNCH-ROADMAP.md): a superseded seven-stage process
  with 28–29 August launch timing, state claims, and publication gates that now
  overlap the canonical seven-step AI workflow.
- The launch-campaign phases, social-channel schedule, measurement plan, and
  time-specific “Day 0” commitments in the root [`README.md`](../README.md).
  Keep a short workspace index later, but do not use this document as ecosystem
  positioning. Its quoted product story also uses unqualified `lightweight`.
- `shared/assets/src/generate-figures.mjs` after visual semantics have been
  transferred. It is a monolithic generator for the old 17-figure template and
  can accidentally recreate replaced assets.
- Old exported figures, social previews, and screenshot composites after their
  approved replacements and provenance records exist. Do not keep ambiguous
  “final”, alternate, or stale-master assets in the active asset tree.
- Repeated implementation checklists and exact V1–V4 placement rules in the
  root/scoped instructions, page system, proposals, roadmap, and old READMEs.
  They should eventually have one owner; until governance is deliberately
  updated, the instruction files remain authoritative and must not be edited or
  ignored.

## Issues Step 2 must inherit

1. **Freshness:** the technical baseline is one day old and follows moving
   `master`. Step 2 may use it for bounded positioning, but Step 3 must compare
   public heads and refresh affected evidence before making README claims.
2. **Governance conflict:** the root instructions call the nine-section,
   four-visual system and proposal filenames approved; the later canonical
   workflow tells the redesign step to treat existing assets as drafts and
   select 2–3 meaningful visuals. Do not silently choose. Obtain or record an
   explicit decision before Step 4.
3. **Ecosystem claim:** preserve two independent tracks—SNode.C → MQTTSuite and
   SNode.C → AISuite → CodexUI. There is no verified all-four runtime scenario.
   Avoid the old root README's unsupported `lightweight` positioning.
4. **Release and maturity:** SNode.C master is newer than its latest tag;
   MQTTSuite master is newer than `v1.0.1`; AISuite has no public tag/npm
   package; CodexUI has no public tag/release. Source version is not maturity or
   availability.
5. **Compatibility and proof gaps:** exact Codex schema/revision compatibility,
   broad compiler/platform/browser matrices, MQTTSuite application behavior
   beyond the basic flow, SNode.C full-test status, authenticated Codex
   workflows, and release-level cross-project compatibility remain unresolved.
6. **Trust routes:** no project- or organization-level `SECURITY.md`,
   `SUPPORT.md`, or `CONTRIBUTING.md` was found at the audit baseline. Do not
   promise those destinations. AISuite/CodexUI also require concise independent-
   project wording and explicit listener/authentication boundaries.
7. **Visual proof:** current screenshots are evidence references, not approved
   final art. Final visuals need refreshed source revisions, deterministic
   manifests, privacy review, GitHub-width legibility, light/dark/mobile checks,
   meaningful alt text, and human approval.

## Handoff summary

1. **Research that must be preserved:** `FACTS.md`, all five `EVIDENCE.md`
   ledgers, exact SHAs/environment/results, tested command paths, source-linked
   SNode.C analysis, capture scripts, synthetic fixtures, product terminology,
   authority boundaries, limitations, and open-fact lists.
2. **Presentation work to discard and rebuild:** all five README drafts as
   prose/structure, all current exported SVG figures and social previews, and
   the final composition of every screenshot. Preserve genuine captures only
   as provenance/reference until refreshed replacements exist.
3. **What Step 2 must know:** evidence freshness is temporary; release,
   maturity, trust, compatibility, and several runtime claims remain open; the
   two ecosystem tracks must stay separate; and the old fixed V1–V4/page-system
   constraints conflict with the newer canonical redesign workflow and require
   an explicit governance decision before visual/README design.
