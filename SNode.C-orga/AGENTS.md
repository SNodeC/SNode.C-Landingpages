# AGENTS.md — SNode.C organization profile

These instructions supplement the root [`AGENTS.md`](../AGENTS.md) for all work
under `SNode.C-orga/`. Follow the shared [page-system principles](../PAGE-SYSTEM.md),
the canonical [README workflow](../workflow/README-WORKFLOW.md), and the
[README governance](../workflow/README-GOVERNANCE.md). This directory's
[proposal](PROPOSAL.md) is research/design input rather than a fixed layout.

## What it solves

The organization profile solves a discovery and orientation problem. Visitors
arrive at several technically different repositories and need to understand the
ecosystem, choose the right project, find a credible evaluation path, and reach
the correct documentation or support route without learning repository history.

## Project focus

Focus on navigation, project selection, ecosystem relationships, evidence, and
clear next actions. Present the organization as a coherent but extensible home
for networking foundations, protocols and integrations, applications and
interfaces, and future tools or examples.

The profile is a front door, not a product manual. Give current projects clear
and balanced representation while making future additions structurally routine.

## Project boundaries

- Do not duplicate project installation guides, API descriptions, configuration
  manuals, or compatibility details beyond a compact verified summary.
- Do not present the architecture figure as the project directory; navigation
  must remain accessible Markdown.
- Do not encode a permanent project count in the headline, hero, navigation, or
  social preview.
- Do not imply that the MQTT and Codex tracks form one runtime system.
- Do not let one mature or visually rich project dominate the catalog.

## Reader outcome

Within five minutes, a visitor should be able to:

1. describe the ecosystem at a high level;
2. choose the correct project for a networking, MQTT, integration, or UI need;
3. select one qualified demo track;
4. find evidence, documentation, support, security, and contribution routes;
5. understand that Codex-related projects are independent open source.

## Audience priority

1. C++ networking and systems developers.
2. IoT, MQTT, edge Linux, and OpenWrt engineers.
3. Developers and users evaluating typed multi-client Codex workflows.
4. Contributors, educators, students, and technical evaluators.

## Terminology

- **SNodeC** — organization name when referring to the GitHub organization.
- **SNode.C ecosystem** — collective public name for the related projects.
- **SNode.C** — networking foundation, never shorthand for the whole
  organization when that would be ambiguous.
- **MQTTSuite**, **AISuite**, and **CodexUI** — use exact capitalization.
- Use **project**, not `component`, for directory entries unless discussing a
  technical dependency.
- Use **Run a demo** for the organization-level CTA.

## Source and destination

- Working public-copy surface: `SNode.C-orga/README.md`.
- Project specification: `SNode.C-orga/PROPOSAL.md`.
- Shared rules: `PAGE-SYSTEM.md`.
- Eventual destination: `SNodeC/.github/profile/README.md`.
- Candidate organization URL — verify before publication:
  `https://github.com/SNodeC`.
- There is no live local organization-profile README to preserve or copy.

## Approved decisions

- The organization profile is an extensible ecosystem navigator; Step 4 decides
  its final reader journey, section count, prose length, and visual inventory.
- Use category-based, repeatable project entries with identity, category,
  verified maturity, outcome, best-fit audience, repository, documentation, and
  quick-start links where those facts/routes are verified.
- Initial categories are `Foundations`, `Protocols and integrations`, and
  `Applications and interfaces`; add `Tools and examples` when populated.
- The current directory begins with SNode.C, MQTTSuite, AISuite, and CodexUI but
  must be able to grow without redesign.
- Use one `Run a demo` destination with two routes:
  1. SNode.C → MQTTSuite;
  2. SNode.C → AISuite → CodexUI.
- Earlier organization hero, project identity, architecture, route, and social
  preview concepts are candidate visual/design inputs rather than mandatory
  V1–V4 slots or filenames. Step 4/Step 5 choose and validate the final set.
- Draft the organization profile early if useful, but finalize and publish it
  after product destinations and proof links are stable.

## Source-code alignment and proof

Every technical statement in a project entry, use case, architecture label, or
evaluation route must be backed by the corresponding project's exact tagged or
selected source and evidence. Verify product roles and dependency arrows against
build manifests and public targets; verify runtime arrows against implementation
and integration tests; verify visible outcomes with reproducible runs.

Do not infer ecosystem behavior merely because repositories are related or use
similar terminology. The profile may summarize verified project evidence, but
it must not broaden its scope. Record stable source, test, release, and
documentation links for every material summary claim before publication.

## Candidate facts — verify

- Each current project's role, maturity, release, supported platforms, license,
  CI status, documentation, and quick-start destination.
- The relationship of AISuite and CodexUI to SNode.C at build time and runtime.
- The organization baseline, metadata, pins, website, contact, and Discussions
  configuration at publication time.
- Any use of `lightweight`, `stable`, `supported`, or protocol lists.

## Commands and examples

The organization profile should not contain project build commands. It may show
one short dispatcher command or link for each qualified demo route, but the
maintained project quick starts own the actual commands, prerequisites,
expected output, teardown, and troubleshooting.

## Common misconceptions

- The organization is not one monolithic product or one shared-version release.
- MQTTSuite is not the whole SNode.C ecosystem.
- AISuite is the integration layer; CodexUI is the presentation layer.
- Codex-related projects are not official OpenAI products.
- Current featured projects are not a permanent limit on the catalog.

## Open facts

- Final headline and organization description.
- Canonical documentation, demo, support, security, roadmap, and contact URLs.
- Verified maturity and release labels for each current project.
- Final logo, palette values, avatar, and product identity assets.
- Whether a dedicated demo or documentation repository is created.
- Final public pins and publication order.

## Validation

- Add a hypothetical fifth project and confirm the directory still works.
- Confirm all current projects are clear and discoverable without forcing equal
  word or visual quotas.
- Confirm every directory action leads to a production destination.
- Confirm architecture/route figures do not act as the only navigation.
- Confirm no fixed project count or false all-product runtime flow appears.
- Test signed-out, mobile, light-mode, dark-mode, and image-disabled rendering.
- Verify approved Step 4/Step 5 visuals, captions, alt text, and links.
