# SNode.C Step 10 — reader-first publication pass

**Publication-pass date:** 29 August 2026
**Landingpages input revision:** `d3a8d3977ff4fbefff196a503b3b447d97f53938`
**Validated SNode.C source baseline:** `bf01683a53b48220a840522e8ccaf3b48e58c240`
**Scope:** SNode.C reader-facing publication material only

## Reader-experience problems found

- The README identified the project accurately but moved into API roles before
  clearly stating the broader networking problem SNode.C addresses or why its
  connection-local model is useful to an experienced C++ reader.
- The capability section still sounded partly like an internal qualification
  record. Evidence boundaries were correct, but the presentation made the
  bookkeeping more prominent than the developer fit-check.
- The architecture section contained useful detail without first framing how the
  layers relate to the programming model.
- The closing routes were comprehensive but not prioritized by reader intent.

## Structural and editorial decisions

- Expanded the first screen into a compact orientation: project category,
  recurring networking concerns, the connection-local architectural idea, and
  four obvious evaluation routes.
- Kept the programming model as the technical centerpiece, but framed it as the
  first concept to understand rather than the first thing the reader encounters.
- Kept the validated echo path early and preserved its commands and visible
  output semantics.
- Recast the capability inventory as an evaluator-facing summary with
  `Available surface` and `What has been exercised` columns.
- Made the architecture section start from composition and extension points,
  then use HTTP → WebSocket context replacement as the concrete consequence.
- Replaced the generic final link list with a goal-oriented next-step table,
  followed by a concise ecosystem orientation and an intentional code-first /
  architecture-first closing choice.

## Material condensed or relocated

- Removed repeated evidence/qualification phrasing where the same boundary is
  already carried by the capability summary or linked capability map.
- Kept detailed platform, protocol, configuration, lifecycle, and deployment
  material in `docs/architecture.md`, `docs/configuration.md`, and
  `docs/capabilities.md` rather than duplicating it in the README.
- No validated command, expected-output line, source baseline, protocol version,
  release boundary, or security/platform limitation was broadened.

## Technical and evidence boundaries

The rewrite remains bounded by `03-TECHNICAL-FACTS.md`,
`07-FINAL-REVIEWS.md`, and the Step 8/9 publication records. In particular:

- `start()` remains described as synchronous caller-thread event-loop execution;
  no operational `tick()` claim or worker-pool claim was introduced.
- `epoll` remains the exercised default; `poll` and `select` are described only
  as configure-time alternatives.
- IPv4, IPv6, Unix-domain, TLS, Bluetooth, HTTP, WebSocket, SSE, and MQTT wording
  preserves the established evidence distinctions.
- MQTT remains MQTT 3.1.1; HTTP remains HTTP/1.0 and HTTP/1.1; WebSocket remains
  version 13; no HTTP/2, MQTT 5, broad platform, performance, footprint,
  production-readiness, or generic security claim was added.
- Current `master` remains source-buildable/local-installable wording, not a
  claim of a current tagged 2.0 release or binary package.
- Ecosystem routes remain two distinct paths rather than an all-project runtime
  pipeline.

## Figure usage

The responsive Figma-derived publication figures are unchanged.

- README: Programming model — desktop/mobile `<picture>` pair.
- README and architecture guide: HTTP → WebSocket context replacement —
  desktop/mobile `<picture>` pair.
- Architecture guide: Architecture by composition — desktop/mobile `<picture>`
  pair.
- Configuration guide: Configuration model — desktop/mobile `<picture>` pair.
- Visual 2 / authentic echo screenshot remains **ABSENT**. No historical or
  synthetic terminal image was introduced.

## Final reader journey

**Orientation and value → programming model and code → verified echo run →
capability fit-check → architecture/context replacement → prioritized
documentation, source, examples, and ecosystem routes.**

## Files changed

- `SNode.C/README.md`
- `SNode.C/workflow/10-READER-FIRST-PUBLICATION.md`

No deeper publication document or visual asset required a corresponding edit.

## Validation performed

- Rechecked Landingpages `main` at the declared Step 10 baseline before editing.
- Rechecked public `SNodeC/snode.c` `master` at the validated source baseline.
- Compared material README claims against Steps 3, 7, 8, and 9.
- Verified every touched local Markdown link and both responsive README
  `<picture>` pairs against the publication tree.
- Verified the four desktop/mobile conceptual figure pairs referenced by the
  complete publication set.
- Checked heading/fragment targets, Markdown fences, HTML picture/source/img
  structure, trailing whitespace, and final newline.
- Checked the public README for accidental `workflow/`, `EVIDENCE.md`, local
  absolute paths, Visual-2 references, or other internal publication
  dependencies.
- Re-read the complete rewritten README in publication order, not only as a
  diff.

## Remaining publication concern

The technical/editorial pass is complete. The genuine remaining gate is
maintainer visual/publication approval of the already integrated responsive
figures and the final reader experience before any separate live
`SNodeC/snode.c` publication. Step 10 does not modify or authorize publication
to that live repository.
