# AGENTS.md — SNode.C landing pages

These instructions apply to the complete `SNode.C-Landingpages` workspace.
Nested `AGENTS.md` files add project-specific facts and may narrow these rules
for their subtree. They do not authorize changes outside this repository.

## Required scoped-instruction loading

When a run starts from the repository root, do not rely on native instruction
discovery to find sibling or descendant guidance. Before analyzing, planning,
editing, or reviewing project content, read all five scoped instruction files
completely:

1. `SNode.C-orga/AGENTS.md`;
2. `SNode.C/AGENTS.md`;
3. `MQTTSuite/AGENTS.md`;
4. `AISuite/AGENTS.md`;
5. `CodexUI/AGENTS.md`.

This requirement applies to single-project and multi-project requests so a
root-started thread remains safe when its scope expands later. Apply each
scoped file only to its own subtree; do not let one project's facts,
terminology, commands, links, or exceptions govern another project.

If native discovery already loaded one or more scoped files, still read any
missing files from the list before project work begins. After an instruction
file changes, read the updated file again before continuing. If any required
file is missing or unreadable, stop project work and report the problem rather
than proceeding without its guidance.

## Scope and safety

- Work only in `/home/voc/projects/drafts/SNode.C-Landingpages`.
- The live local repositories are read-only knowledge sources. Never edit,
  format, generate into, install into, or commit in them.
- Do not copy a live README's structure or wording. Extract candidate facts,
  verify them, and write new presentation copy.
- Do not edit the five working landing-page READMEs until the user explicitly
  approves the writing stage. Planning belongs in `PAGE-SYSTEM.md` and the
  relevant `PROPOSAL.md`.
- Do not publish or copy files into canonical repositories from this workspace.
  Production publication is a later, reviewed operation.
- Preserve unrelated user changes. Never use destructive Git commands.

Read-only source locations currently used by this workspace:

| Product | Live local source |
| --- | --- |
| SNode.C | `/home/voc/projects/snodec/snode.c` |
| MQTTSuite | `/home/voc/projects/mqttsuite/mqttsuite` |
| AISuite | `/home/voc/projects/drafts/AISuite-extraction/AISuite-final` |
| CodexUI | `/home/voc/projects/drafts/CodexUI/codexui` |

The organization profile has no live local README source.

## Instruction and source hierarchy

Use sources in this order:

1. this file and the nearest nested `AGENTS.md`;
2. [`PAGE-SYSTEM.md`](PAGE-SYSTEM.md) for approved shared structure and visuals;
3. the relevant `PROPOSAL.md` for project-specific content and acceptance;
4. verified current-master source, tests, CI, release metadata, and maintained
   technical docs;
5. live README content as a hint only.

When sources conflict, do not silently choose the most convenient claim. Record
the conflict in the proposal or fact inventory and leave public copy neutral
until it is resolved.

## Fact-status vocabulary

Use these labels in planning and review notes:

- **Approved decision** — editorial, structural, or visual choice fixed in the
  page system or a proposal.
- **Candidate fact — verify** — statement observed in source, a live README, or
  technical documentation that still needs release-specific evidence.
- **Open fact** — required information not yet established, such as a version,
  maturity label, support matrix, or canonical support link.

Never turn a candidate or open fact into an unqualified public claim.

## Source-code alignment and proof

Every technical documentation statement must align strictly with current public
`master` at `HEAD`. Record the exact observed commit and review date even though
the maintained landing pages continue to track the moving branch. A live
README, proposal, issue, comment, or architecture document may identify a
candidate fact, but it is not sufficient proof by itself.

For every material technical claim, record enough evidence during drafting to
identify:

- repository, `master` branch, exact observed commit, and review date;
- relevant source file, public symbol, schema, manifest, or build option;
- supporting unit, integration, acceptance, or equality test where behavior is
  claimed;
- reproducible runtime output where a user-visible result is claimed;
- release artifact or installed package evidence where availability is claimed.

Source code proves that an implementation exists; tests and reproducible runs
prove its qualified behavior; release metadata proves that users can obtain it.
Do not substitute one type of evidence for another. If source, tests,
documentation, and release metadata disagree, treat the statement as unresolved
and omit or qualify it until the conflict is fixed.

Do not expose local absolute source paths in public copy. Audit links should
point to the exact reviewed commit; visitor navigation may point to maintained
`master` documentation. Use release links only for released-artifact claims.

## Editorial standard

- Act as a senior technical product writer and open-source launch editor.
- Write for experienced developers and technical evaluators.
- Lead with user outcome, evidence, and the shortest useful evaluation path.
- Use concise, precise, natural language and GitHub-native Markdown.
- Define project-specific terminology before relying on it.
- Prefer concrete verbs such as build, connect, route, publish, inspect, and
  integrate.
- Avoid hype, vague superlatives, vanity counters, badge walls, and generic
  promotional language.
- Never invent versions, maturity, compatibility, performance, security,
  protocol coverage, release artifacts, or platform support.
- Words such as `lightweight`, `production-ready`, `secure`, `complete`,
  `full`, `fast`, and `supported` require current, linked evidence and scope.
- State limitations and non-goals with the same precision as capabilities.

## Shared page system

The four product pages use the approved nine-section architecture and target
approximately 1,300–1,600 prose words, excluding commands, tables, and captions.
Each receives equal editorial and visual weight regardless of project age or
complexity.

Each product page has:

- one outcome-led hero with no more than three meaningful badges;
- one principal quick start and visible expected result;
- one product-specific centerpiece;
- one capabilities/limitations table;
- one compatibility or requirements table;
- visual slots V1–V4 and one social preview;
- one compact documentation/support/security/contribution/license ending.

The organization profile targets approximately 900–1,100 words. It is a
scalable navigator and may be shorter than the product pages.

## Required scoped-instruction structure

Every presentation subdirectory has its own `AGENTS.md`. Keep these files
consistent and operational. Each must define:

1. **What it solves** — the visitor problem addressed by the project or profile.
2. **Project focus** — what deserves the most editorial attention.
3. **Project boundaries** — what belongs to another project or documentation
   layer.
4. **Reader outcome** — what a visitor should understand or accomplish.
5. **Audience priority** — primary audience first, secondary audiences second.
6. **Terminology** — exact product, component, executable, package, protocol,
   and state names.
7. **Source and destination** — read-only technical source and eventual public
   destination.
8. **Approved decisions** — fixed content, CTA, quick start, structure, and
   visuals.
9. **Candidate facts — verify** — technically plausible source material that is
   not yet approved launch copy.
10. **Source-code alignment and proof** — project-specific implementation,
    test, runtime, and release evidence required for technical statements.
11. **Commands and examples** — qualification shapes and project-specific
    restrictions.
12. **Common misconceptions** — interpretations the page must prevent.
13. **Open facts** — missing release, compatibility, support, or evidence data.
14. **Validation** — project-specific checks in addition to the shared review.

Do not turn scoped files into alternative proposals. They should tell a future
writer how to reason about the project, where to look, what to emphasize, and
what not to claim. Detailed page requirements remain in `PROPOSAL.md`.

## Visual and asset rules

- Follow the exact V1–V4 filenames, content, and placement in each proposal.
- Use the shared diagram grammar, accents, dimensions, screenshot hygiene, and
  accessibility rules in `PAGE-SYSTEM.md`.
- Use real qualified builds for product screenshots. Never label a mockup as
  shipped functionality.
- Keep editable sources under the presentation's `assets/src/` directory.
- Provide information-bearing alt text and a short caption for every meaningful
  figure.
- Test visuals in GitHub light and dark modes and at mobile width.
- Pages must remain understandable when images fail to load.
- Do not add extra visual slots merely because a project has more features.

## Links and publication boundaries

- Drafts may link within this workspace for review.
- Before publication, replace every draft-only link with a stable production
  destination.
- Prefer canonical repository, maintained master documentation, applicable
  releases, security, support, and contribution links.
- The landing pages and quick starts track current public `master`/`HEAD` by
  user decision. Preserve reproducibility by recording the exact tested SHAs in
  `FACTS.md` and the relevant `EVIDENCE.md`.
- Do not link claims to search results, personal workspaces, local paths, or
  ephemeral CI artifacts.
- The Codex-related pages must carry a concise independent-project notice and
  must not imply official OpenAI ownership or endorsement.

## Commands and examples

- Treat command blocks copied from live READMEs as candidate material.
- Test public commands verbatim from clean temporary checkouts of the exact
  current compatible master heads.
- Keep one reusable isolated checkout per project and use its canonical
  out-of-tree build directories (for example `cmake-build-release` and
  `cmake-build-debug`). Reuse an incremental build only while the recorded
  commit, compiler, generator, dependency prefix, and CMake options still
  match; otherwise reconfigure or create the appropriate canonical variant.
- Never gain incremental-build speed by configuring, compiling, installing,
  or generating files in a live local repository. Reusable qualification
  checkouts and their install prefix must remain isolated from those sources.
- Use out-of-tree builds, `cmake --build`, `ctest` where tests exist, and
  `cmake --install` where installation is advertised.
- Avoid local sibling-directory assumptions in end-user instructions.
- Show expected output, teardown, and a troubleshooting route.
- Never include real credentials, tokens, private prompts, hostnames, usernames,
  home directories, LAN addresses, or certificates.
- Use the shared synthetic data from `PAGE-SYSTEM.md` where applicable.

## Approved ecosystem decisions

- The organization CTA is `Run a demo`.
- The demo destination offers two coherent tracks:
  1. SNode.C → MQTTSuite;
  2. SNode.C → AISuite → CodexUI.
- Do not fabricate an all-four-product runtime scenario.
- The organization directory is category-based and must not encode a permanent
  project count.
- Current product accents are foundation blue, IoT green, protocol violet, and
  interface amber, subject to final contrast testing.

## Required validation

Before handing off planning or copy changes:

1. run `git diff --check`;
2. verify all relative Markdown links resolve;
3. confirm no unintended landing-page README changed during planning;
4. confirm every public claim is approved or clearly marked for verification;
5. confirm section count and prose weight match the shared system;
6. confirm V1–V4 and the social preview match the scoped proposal;
7. inspect the diff for accidental local paths, secrets, draft-only links, and
   live-repository changes.

Do not commit unless the user explicitly requests a commit.
