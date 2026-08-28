# SNode.C Ecosystem — Professional Launch Workspace

This repository is the drafting and implementation workspace for the professional
presentation and coordinated launch of the **SNode.C ecosystem**:

- [SNode.C](SNode.C/README.md) — event-driven C++ networking
  framework;
- [MQTTSuite](MQTTSuite/README.md) — MQTT broker, integration,
  bridge, CLI, and storage applications;
- [AISuite](AISuite/README.md) — typed asynchronous C++ integration and a
  multi-client bridge for the Codex app-server;
- [CodexUI](CodexUI/README.md) — native Qt interface built on AISuite.

The objective is not merely to improve documentation. The organization profile
and every repository README will become a professional GitHub-native landing
page, backed by qualified releases, a coherent visual identity, reproducible
demos, trustworthy project infrastructure, and a responsible launch campaign.

## Success criteria

A technically qualified visitor should be able to answer these questions within
five minutes:

1. What problem does this ecosystem solve?
2. Which component should I use?
3. Why should I trust it?
4. How can I run a useful example?
5. Where do I get help or contribute?

The main call to action will be: **Run a demo.** The destination will offer a
networking/MQTT track and a typed Codex-client track, as defined by the shared
[page system](PAGE-SYSTEM.md).

The approved execution sequence and auditable source baseline are maintained in
the [implementation roadmap](LAUNCH-ROADMAP.md) and shared
[fact register](FACTS.md).

## Landing-page workspaces

Each presentation has a working README and a detailed specification. All
development happens here; approved READMEs are copied to their production
repositories only after review.

| Presentation | Working landing page | Proposal | Evidence | Eventual destination |
| --- | --- | --- | --- | --- |
| SNode.C organization | [Open draft](SNode.C-orga/README.md) | [Proposal](SNode.C-orga/PROPOSAL.md) | [Evidence](SNode.C-orga/EVIDENCE.md) | `SNodeC/.github/profile/README.md` |
| SNode.C | [Open draft](SNode.C/README.md) | [Proposal](SNode.C/PROPOSAL.md) | [Evidence](SNode.C/EVIDENCE.md) | `SNodeC/snode.c/README.md` |
| MQTTSuite | [Open draft](MQTTSuite/README.md) | [Proposal](MQTTSuite/PROPOSAL.md) | [Evidence](MQTTSuite/EVIDENCE.md) | `SNodeC/mqttsuite/README.md` |
| AISuite | [Open draft](AISuite/README.md) | [Proposal](AISuite/PROPOSAL.md) | [Evidence](AISuite/EVIDENCE.md) | `SNodeC/AISuite/README.md` |
| CodexUI | [Open draft](CodexUI/README.md) | [Proposal](CodexUI/PROPOSAL.md) | [Evidence](CodexUI/EVIDENCE.md) | `SNodeC/CodexUI/README.md` |

Shared positioning, visual assets, compatibility information, and launch
decisions should stay consistent across these workspaces. The working READMEs
must not depend on unpublished files in the production repositories. Product-
specific drafts can evolve independently until they pass the roadmap gates.

## Approved landing-page system

The shared editorial, structural, and visual decisions are maintained in the
[SNode.C landing-page system](PAGE-SYSTEM.md). It is the source of truth for:

- equal content and visual weight across the four product pages;
- the common nine-part repository landing-page structure;
- the four visual slots and social-preview system;
- screenshot, diagram, accessibility, theme, and synthetic-data rules;
- an organization profile that can grow beyond the current project catalog;
- two honest evaluation tracks instead of an artificial all-product demo;
- the boundary between this drafting workspace and read-only live repositories.

Each presentation proposal defines only its product-specific content and visual
inventory. The five working landing-page READMEs remain public-copy surfaces and
must not accumulate planning notes. Approval of the page system does not approve
unverified versions, maturity, compatibility, platform, performance, security,
or protocol claims.

## Current baseline

The initial audit on 28 August 2026 found:

- the SNodeC organization has no public organization profile README;
- its public pins do not yet present the complete four-product system;
- SNode.C and MQTTSuite contain extensive technical material, but their root
  READMEs function more like manuals than product landing pages;
- AISuite has no public GitHub release, topics, website, or repository
  description;
- CodexUI has no public release or declared project version; current master is
  native-only and cannot carry a `1.0` or browser claim;
- AISuite master declares `0.7.0` and contains no TypeScript package; the
  separate development-branch package is excluded from the current baseline;
- historical Codex UI versions exist beside the new canonical CodexUI product,
  so canonical naming and links must be unambiguous.

These are launch blockers, not cosmetic details.

## Product story

Working ecosystem statement:

> SNode.C is a lightweight, event-driven C++ networking foundation. MQTTSuite
> turns it into an MQTT integration platform, while AISuite and CodexUI extend
> the same architecture into typed, multi-client AI workflows.

| Product | Role | Primary audience | Primary action |
| --- | --- | --- | --- |
| SNode.C | Event-driven C++ networking framework | C++ and systems developers | Build a first network app |
| MQTTSuite | MQTT broker, bridge, integration, CLI, and storage suite | IoT and edge engineers | Run the MQTT quick start |
| AISuite | Typed asynchronous C++ bridge | AI tooling and C++ developers | Build and call the bridge |
| CodexUI | Native Qt interface | Codex users and UI developers | See the workflow and install |

Claims such as “production-ready,” performance superiority, small footprint,
protocol coverage, and supported platforms must be linked to reproducible tests
or measurements.

## Roadmap

### Phase 0 — Ownership and launch decisions

**Estimated duration:** 2–3 days

- Identify the canonical repository, default branch, maintainer, documentation
  owner, and release owner for every product.
- Confirm the public product names and capitalization.
- Use independent semantic versions for components; do not force all products
  to share one version.
- Define an ecosystem compatibility matrix separately.
- Confirm the primary audiences:
  1. C++ networking and systems developers;
  2. IoT, MQTT, and embedded Linux engineers;
  3. developers building local or multi-client Codex workflows.
- Use GitHub Discussions for usage questions and ideas; reserve Issues for
  reproducible bugs and accepted work.
- Write a one-page positioning brief and launch definition of done.

**Gate:** Names, canonical repositories, owners, audiences, and the primary call
to action are fixed.

### Phase 1 — Product and release readiness

**Estimated duration:** 1–2 weeks

#### Version normalization

- Inventory versions in CMake, package manifests, headers, generated files,
  documentation, CLI output, install metadata, and dependency pins.
- Establish exactly one version source of truth per repository.
- Current master establishes AISuite source version `0.7.0`; TypeScript package
  `1.0.0` exists only outside master and is excluded from current public copy.
- CodexUI master has no project version and is native-only. A future `1.0` or
  browser claim requires the relevant code, installation, compatibility, and
  acceptance evidence to reach master first.
- Create annotated or signed `vX.Y.Z` tags and GitHub Releases.
- Maintain human-readable changelogs and release notes.
- Publish the compatibility matrix, including CodexUI, AISuite, SNode.C, and
  the exact supported Codex app-server schema or revision.
- Document SemVer, deprecation, security-fix, and supported-branch policies.

#### Fresh-install qualification

CI must test clean configure, compilation, tests, installation, downstream
`find_package` consumption, and a runtime smoke test. Validate every advertised
combination, including:

- Debian stable and current Ubuntu;
- GCC and Clang where supported;
- x86-64 and an ARM target for advertised edge support;
- native Qt CodexUI builds; browser builds only after they reach master;
- OpenWrt if it remains a launch claim.

#### Qualified evaluation tracks

Maintain one `Run a demo` destination with two technically coherent tracks:

1. **Networking and MQTT:** install or build SNode.C, start a useful MQTTSuite
   scenario, and verify a visible message flow.
2. **Typed Codex client:** install or build SNode.C and AISuite, start the
   AISuite bridge, open native CodexUI, and complete a visible
   workflow.

Target 5–10 minutes per track with copy/paste commands, expected output,
teardown, and troubleshooting. A script or container workflow may supplement,
but not replace, native build documentation. Do not imply a runtime relationship
between the MQTT and Codex tracks unless a real integration is implemented and
qualified.

#### Trust and project hygiene

Every public repository needs:

- correct license and SPDX presentation;
- `SECURITY.md`, `SUPPORT.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md`;
- issue forms and a pull-request template;
- dependency and secret scanning where available;
- reproducible release instructions;
- release artifacts and SHA-256 checksums;
- an SBOM when practical;
- no credentials, personal data, local paths, build outputs, or stale binaries.

**Gate:** Version metadata agrees, clean CI passes, advertised claims have
evidence, releases and known limitations are documented, and an independent
tester can complete the quick start without help.

### Phase 2 — Brand and visual system

**Estimated duration:** 4–7 days, overlapping late Phase 1

Create one restrained design system rather than four unrelated presentations:

- organization mark and wordmark in SVG and PNG;
- accessible color palette, typography policy, spacing, and icon style;
- one accent color or identifier for each product;
- reusable README hero templates;
- ecosystem architecture graphic in SVG with editable source;
- 1280×640 social-preview card for the organization and each repository;
- article, social post, and presentation-cover templates.

Avoid decorative badge walls, animated typing banners, excessive centered HTML,
and text-heavy screenshots. The visual standard is clarity, consistency,
accessibility, technical precision, and fast loading.

#### Screenshot and video inventory

- **Ecosystem:** dependency and runtime architecture.
- **SNode.C:** concise code-to-running-server sequence and terminal result.
- **MQTTSuite:** broker Web UI, client/topic view, and a complete integration
  scenario.
- **AISuite:** bridge telemetry and a multi-client flow diagram.
- **CodexUI:** polished native hero plus a representative thread/turn workflow.
- **Launch:** a 60–90 second narrated demo and a silent 10–20 second social clip.

Use consistent resolution, theme, window treatment, synthetic test data, crop,
and alt text. Remove usernames and secrets. Store optimized assets and editable
sources under version control.

**Gate:** Assets are sharp, compressed, licensed, accessible, and readable in
GitHub light and dark themes.

### Phase 3 — GitHub landing pages

**Estimated duration:** 1–2 weeks

#### Organization profile

Create the public `.github` repository with `profile/README.md` containing:

1. compact branded hero and ecosystem value statement;
2. three concrete “What you can build” use cases;
3. an extensible project directory with equal entries for current projects;
4. ecosystem architecture;
5. evaluation-route chooser;
6. supported platforms, tests, documentation, licenses, and releases;
7. support and community routes;
8. roadmap and contribution call to action.

Update the organization avatar, short description, website, contact details,
and public pins. Recommended pin order:

1. `snode.c`
2. `mqttsuite`
3. `AISuite`
4. `CodexUI`
5. documentation or demo repository, if useful

#### Repository landing-page structure

Every root `README.md` will share this information architecture:

1. hero with outcome, verified maturity/version, restrained badges, links, and
   visual V1;
2. three to five user outcomes or differentiators;
3. one fast, qualified quick start with expected result and visual V2;
4. one product-specific centerpiece;
5. capabilities plus explicit limitations and non-goals;
6. compact architecture, ownership, and ecosystem relationship with visual V3;
7. installation, tested platforms, and compatibility;
8. examples, deployment, or quality evidence with visual V4;
9. documentation, support, security, contribution, roadmap, and licenses.

The live READMEs are read-only technical knowledge sources during this workflow;
their structures and wording are not preserved. The new drafts should orient
and convert, while qualified detailed documentation remains linked separately.
Nothing in this workspace modifies the live local repositories.

#### Product-specific priorities

- **SNode.C:** smallest compelling network application, supported
  transports/protocols, event-loop model, verified performance/footprint, and
  precise relationship to Node.js without implying API compatibility.
- **MQTTSuite:** five-application diagram, runnable IoT scenario, MQTT 3.1.1
  scope, transport matrix, Web UI screenshot, and explicit MQTT 5 limitations.
- **AISuite:** benefits before internal implementation terminology, typed C++
  access, multi-client bridge, recorded schema, minimal example, and lifecycle
  limitations.
- **CodexUI:** native screenshot and workflow, prerequisites, security
  boundaries, install artifacts, and exact compatibility.

For every repository, configure its description, website, topics, social
preview, releases, support routing, and accurate cross-links.

**Gate:** Review all pages signed out, on mobile, and in GitHub light/dark modes.
Validate links, images, alt text, commands, badges, topics, release links, and
quick starts.

### Phase 4 — Launch content package

**Estimated duration:** 1 week

Create reusable facts, then write native content for each audience:

- 50-, 150-, and 400-word ecosystem descriptions;
- one sentence and one paragraph for each product;
- maintainer story explaining why the system exists;
- technical deep dives for the SNode.C architecture, an MQTT integration
  scenario, and AISuite/CodexUI multi-client architecture;
- launch article containing demo, limitations, roadmap, and contribution needs;
- press/community kit with logos, screenshots, captions, links, licenses,
  author biography, and contact;
- FAQ covering platforms, MQTT version, licensing, security, stability,
  data handling, and the relationship to OpenAI/Codex;
- channel-specific titles, images, disclosures, and tagged links.

State clearly that these are independent open-source projects and not official
OpenAI products wherever the Codex naming might cause confusion.

**Gate:** A second reviewer checks technical accuracy, terminology, grammar,
links, licensing, attribution, images, and disclosures.

### Phase 5 — Community warm-up

**Estimated duration:** 2–4 weeks before launch

- Enable and seed GitHub Discussions with Welcome, Help, Ideas, and Show and
  Tell categories.
- Triage existing issues and publish genuinely approachable `good first issue`
  tasks.
- Participate constructively in target communities before announcing.
- Ask 5–10 relevant people to test privately and provide honest feedback; never
  ask for coordinated votes or comments.
- Publish one educational technical article before the announcement.
- Prepare response owners and answers for predictable questions.

### Phase 6 — Staggered public launch

**Estimated duration:** 2 weeks, followed by technical content

#### Tier 1 — Owned and high-intent channels

- GitHub Releases and organization Discussions;
- project website, blog, and documentation fronts;
- LinkedIn maintainer story plus technical carousel or demo;
- existing opt-in followers or contacts.

#### Tier 2 — Developer announcement channels

- **Hacker News / Show HN:** only after people can run the system immediately;
  lead with what was built, why, and the demo, and remain available to answer.
- **Reddit:** use only relevant C++, open-source, self-hosting, embedded Linux,
  IoT, and MQTT communities. Check current community rules, contact moderators
  when unclear, disclose authorship, and write a distinct useful post for each
  audience.
- **DEV Community or technical blog:** publish a useful deep dive rather than a
  press release.
- **Product Hunt:** only if CodexUI has downloadable artifacts or a frictionless
  demo and its audience is a match.

#### Tier 3 — Specialist and relationship channels

- C++/IoT/MQTT forums, Discord, Slack, Matrix, mailing lists, and user groups
  only where project sharing is permitted;
- LinkedIn and Facebook specialist groups after checking rules or receiving
  administrator permission;
- Linux, C++, IoT, university, and local technology meetups;
- conference CFPs and open-source showcases.

#### Stack Overflow

Stack Overflow is not an announcement or advertising channel. Mention a project
only when writing a complete answer to a genuine, on-topic technical question.
Disclose affiliation, and make the answer useful without requiring the link.

#### Suggested launch sequence

- **Day 0:** releases, landing pages, documentation, demo, Discussion.
- **Day 1:** maintainer article and LinkedIn.
- **Days 2–4:** first best-fit technical community and active responses.
- **Days 5–7:** second audience using a different use case and article.
- **Week 2:** Show HN or broader announcement after incorporating early feedback.
- **Weeks 3–6:** tutorial, benchmark evidence, feedback report, roadmap update.

Do not mass-cross-post, buy engagement, coordinate votes, message strangers, or
argue with criticism. Turn recurring questions into better documentation.

### Phase 7 — Measurement and iteration

Capture a pre-launch baseline, then review after 24 hours, 7 days, and 30 days.

Primary measurements:

- quick-start completion and time to first success;
- release downloads and successful installation usage;
- documentation entry and quick-start traffic;
- substantive Discussions, issues, pull requests, and returning contributors;
- privacy-respecting channel-to-demo conversion;
- questions that identify missing documentation.

Stars, forks, followers, and social engagement are secondary. Maintain a launch
log with the audience, URL, date, rules checked, content version, responses,
referrals, lessons, and follow-up actions.

## Professional launch definition of done

- [ ] Canonical repositories and owners are documented.
- [ ] All versions are internally consistent and tagged.
- [ ] Compatibility and supported-version matrices are published.
- [ ] CI proves clean builds, tests, installation, consumer use, and smoke tests.
- [ ] An independent tester completes each evaluation track unaided.
- [ ] Releases contain notes, artifacts, checksums, and known limitations.
- [ ] Security, support, contribution, conduct, issue, and PR files exist.
- [ ] The organization profile README and launch-facing pins are live.
- [ ] All four repository READMEs follow the shared landing-page system.
- [ ] Detailed manuals no longer dominate the landing-page narrative.
- [ ] Brand, diagrams, screenshots, video, and social previews pass visual QA.
- [ ] Repository descriptions, topics, sites, licenses, and support routes are set.
- [ ] Launch article, FAQ, press kit, and channel-native posts are reviewed.
- [ ] Community rules are checked immediately before every post.
- [ ] Maintainers are available to respond during launch.
- [ ] Baseline measurements and 7-/30-day reviews are scheduled.

## Immediate implementation order

1. Audit and decide exact versions for all four canonical repositories.
2. Publish the compatibility matrix and qualify both evaluation tracks.
3. Finalize the positioning brief and naming rules.
4. Create the visual system and shot list.
5. Build the organization profile README.
6. Rebuild SNode.C and MQTTSuite READMEs as concise landing pages.
7. Rebuild AISuite and CodexUI READMEs around working demos and releases.
8. Complete project hygiene and signed release candidates.
9. Capture screenshots and video from those exact release candidates.
10. Run independent quick-start, visual, and editorial reviews.
11. Publish releases and landing pages.
12. Execute the staggered launch and improve it from real feedback.

## Workspace convention

Drafts, shared assets, templates, checklists, and review notes belong in this
repository. Production changes should ultimately be applied to their canonical
repositories through reviewed pull requests. Decisions that affect messaging,
versions, compatibility, or launch claims must be recorded here so the launch
does not depend on missing chat history.
