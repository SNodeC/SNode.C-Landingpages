# Landing-page implementation roadmap

[← Workspace roadmap](README.md) · [Page system](PAGE-SYSTEM.md) ·
[Fact register](FACTS.md)

**Status:** Approved working sequence, 28 August 2026

This is the operational roadmap from approved planning to launch-ready GitHub
presentations. It complements the broader launch phases in `README.md` and does
not replace the page specifications.

## Source policy

All landing pages track the current public `master` branch at `HEAD`. At every
review, record the exact observed commit SHA and date in `FACTS.md` and the
project's `EVIDENCE.md`. The SHA is an audit record, not a request to freeze the
website to an old release. Refresh affected claims whenever `master` changes.

Never fetch into, check out, build in, or modify the live local repositories.
Use committed Git objects or a clean temporary clone for source review and
qualification.

## The seven stages

| Stage | Deliverable | Completion gate | Current state |
| --- | --- | --- | --- |
| 1. Approve the presentation system | Shared structure, visual grammar, project proposals, and scoped instructions | Planning documents agree; draft READMEs remain untouched | Complete; optional checkpoint commit remains unrequested |
| 2. Establish the source baseline | Public `master`/`HEAD` policy plus an exact observed SHA for every project | Remote heads, source dates, and dependency policy are recorded | Complete |
| 3. Build the fact and evidence registers | One shared register and one scoped register for every landing page | Versions, maturity, compatibility, platforms, dependencies, capabilities, licenses, links, tests, runtime proof, and open claims are represented | Complete and updated with the first runtime qualification |
| 4. Qualify the four quick starts | Verbatim commands, expected output, environment, teardown, and troubleshooting | Each path passes from clean current-master checkouts with compatible dependencies | Core qualification unchanged: SNode.C/MQTTSuite runtime flows, AISuite 27/27 C++ + 20/20 TypeScript, CodexUI native 7/7; web 30/30 + artifact verification added; authenticated capture remains stage 6 |
| 5. Resolve launch wording and maturity | Evidence-backed version, maturity, compatibility, and limitation language | No public claim depends on a feature branch, absent artifact, or undocumented policy | Current-master source scope resolved; public npm/release wording and CodexUI build-tool audit review remain gated |
| 6. Qualify screenshots and figures | Approved V1–V4 inputs and social previews from the same qualified builds | Captures are genuine, sanitized, reproducible, accessible, and source-aligned | Pending |
| 7. Write, review, and prepare publication | Five new landing-page presentations with consistent weight and navigation | Fresh scoped Codex runs load nested instructions; copy, links, visuals, commands, and claims pass review | Copy drafted; final visual assets, publication-route files, and owner review remain |

## Stage 3 maintenance rule

`FACTS.md` owns ecosystem-wide facts and cross-project compatibility. Each
project directory owns an `EVIDENCE.md` claim ledger. A claim may enter public
copy only when its ledger row identifies implementation evidence and any
required test, runtime, or artifact evidence. Missing proof remains visible as
`Pending` or `Open`; it is never filled with an inference.

## Stage 4 qualification record

For each quick start, record:

- the four project SHAs and dependency SHAs actually used;
- operating system, architecture, compiler, CMake, and required runtime tools;
- commands copied exactly as a visitor will run them;
- expected and observed output;
- elapsed time, teardown, and cleanup;
- failures, environmental assumptions, and the troubleshooting destination.

The four primary paths are SNode.C echo, MQTTSuite broker/subscriber/publisher,
AISuite bridge/reference client, and CodexUI first workflow. AISuite's
TypeScript package and CodexWebUI artifact are additional qualified source
paths; launch still requires genuine sanitized captures and release artifacts.

## Stage 5 decisions already established

- AISuite `master` declares CMake source version `0.7.0` and contains
  `@snodec/codex-frontend` source-package version `1.0.0`. These independently
  versioned surfaces do not conflict. Source build, tests, and package contents
  qualify; public npm release and registry installation do not.
- CodexUI `master` declares native/web source version `1.0.0`; native 7/7 and
  web 30/30 tests pass and the web artifact verifies. Do not call it a public
  `1.0` release until tags/artifacts and remaining audit gates pass.
- Source-version numbers do not establish maturity, stability, support, or
  release availability.

## Change handling

Before drafting or refreshing a page:

1. query the public remote `master` head without changing a live repository;
2. compare it with the SHA in `FACTS.md`;
3. review changed source, tests, manifests, workflows, and documentation;
4. update affected evidence rows;
5. rerun only the qualification paths affected by the change;
6. update public copy and captures together.
