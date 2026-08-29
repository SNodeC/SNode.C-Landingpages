# Codex technical audit

- **Audit date:** 29 August 2026
- **Reviewed public source:** [`SNodeC/snode.c` `master` at `bf01683a53b48220a840522e8ccaf3b48e58c240`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240)
- **Baseline result:** unchanged from the Step 3/5 validated baseline

## IMPORTANT — Relative draft links do not yet have final README publication destinations

- **Severity:** **IMPORTANT**
- **Location:** draft lines 24 and 205 use
  `../assets/programming-model.svg` and
  `../assets/http-websocket-context-switch.svg`; lines 174, 221, 230, 232,
  and 234 use `../docs/capabilities.md`, `../docs/configuration.md`, and
  `../docs/architecture.md`.
- **What is wrong or unsupported:** those paths correctly resolve from the
  frozen workflow draft, but copying them unchanged to `SNode.C/README.md`
  would resolve outside the SNode.C publication root. The two assets and three
  landing-page documents also do not exist at those destination paths in the
  reviewed public `snode.c` commit, so rebasing alone is not enough unless the
  targets are co-published.
- **Authoritative evidence/source:** the relative paths are visible in the
  frozen [Step 6 draft](06-README-DRAFT.md). A recursive tree inspection of the
  reviewed commit finds none of the five destination files; the public
  [`docs` tree at the reviewed commit](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/docs)
  likewise has no `architecture.md`, `configuration.md`, or `capabilities.md`.
  Root publication rules require stable production destinations rather than
  workflow-relative links.
- **Minimum required correction:** in Step 7c, rebase the two asset links to
  `assets/...` and every document link to `docs/...`. Co-publish the final
  approved asset versions and all three documents with the README, or replace
  or omit any link whose stable public destination will not exist. This is a
  path/destination finding, not a rejection of the two technically validated
  working SVGs while their human publication approval remains pending.

## MINOR — The multiplexer row does not scope qualification to the selected default

- **Severity:** **MINOR**
- **Location:** draft line 155, capabilities table, event-runtime row:
  “`epoll` default with selectable `poll` and `select`,” followed by the generic
  exact-head CI and focused-test evidence.
- **What is wrong or unsupported:** the availability statement is true, but it
  omits that selection occurs at CMake configure time and that `core` links one
  selected multiplexer. The reviewed CI and qualification used the default
  `epoll`; they did not separately exercise `core` linked against `poll` or
  `select`. The row can therefore be read more broadly than its evidence.
- **Authoritative evidence/source:** [`src/core/CMakeLists.txt`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/CMakeLists.txt#L42-L51)
  defines the configure-time choice, and the same file
  [links `core` to one selected implementation](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/CMakeLists.txt#L149-L152).
  The exact-head [CI configure command](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/.github/workflows/ci.yml#L43-L44)
  does not override the default. Step 3 records no comparative multiplexer
  qualification.
- **Minimum required correction:** say that `epoll` is the default and that
  `poll` and `select` are configure-time alternatives; state in the evidence or
  boundary cell that current CI/runtime qualification exercised default
  `epoll` only.

## MINOR — The programming-model factory association can imply one shared factory

- **Severity:** **MINOR**
- **Location:** the programming-model figure embedded at draft line 24,
  specifically the single association rail labeled “endpoint flow retains
  factory” that joins both endpoint-role cards to one `SocketContextFactory`.
- **What is wrong or unsupported:** the surrounding draft prose correctly says
  “the endpoint flow's” retained factory, but the shared visual rail can imply
  that a server flow and a client flow retain one global factory. Each endpoint
  flow instead constructs and retains its own factory in its own shared flow
  context.
- **Authoritative evidence/source:** the server flow stores its factory in
  [`SocketServer.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketServer.h#L86-L100)
  and [constructs that flow with its own factory](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketServer.h#L170-L181).
  The client flow independently stores its factory in
  [`SocketClient.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketClient.h#L91-L105)
  and [constructs its own](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketClient.h#L205-L216).
  The validated [Step 5 semantics](05-VISUALS.md) explicitly prohibit implying
  one shared global factory.
- **Minimum required correction:** during the pending visual refinement, split
  the association by endpoint or label it unambiguously as “each endpoint flow
  retains its own factory.” Use that corrected, human-approved asset in the
  final README.

## MINOR — The upgrade figure omits explicit replacement-context creation

- **Severity:** **MINOR**
- **Location:** the HTTP-to-WebSocket figure embedded at draft line 205,
  specifically its numbered staged-switch sequence: “WebSocket factory
  selected” → “101 Switching Protocols response prepared” →
  `setSocketContext(new)` → `response->end()`.
- **What is wrong or unsupported:** draft lines 196–203 preserve the exact
  server-side order, but the figure skips the factory's creation of the
  replacement context between factory selection and `101` preparation. It also
  does not identify `response->end()` as the action taken by the upgrade-status
  callback/application path, so the compact visual can suggest more automatic
  framework behavior than the source implements.
- **Authoritative evidence/source:** server
  [`Response::upgrade()`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/server/Response.cpp#L276-L307)
  selects the factory and calls its creation surface. The WebSocket
  [`SocketContextUpgradeFactory`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket/server/SocketContextUpgradeFactory.cpp#L66-L95)
  allocates the replacement before preparing the `101`; the tested application
  callback then calls
  [`response->end()`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/tests/component/websocket/WebSocketServerClientTextEchoTest.h#L217-L230).
  The post-callback detach → pointer change → attach order is implemented in
  [`SocketConnection.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.hpp#L360-L379).
- **Minimum required correction:** make the first visual stage “WebSocket
  factory selected; replacement context created,” and identify the fourth as
  the upgrade-status callback/application calling `response->end()` to queue
  the `101`. Preserve the existing staging, callback-return, context-switch,
  active-pointer, attach, and same-connection ordering.

## Audit summary

- **Current reviewed SNode.C `master` SHA:**
  `bf01683a53b48220a840522e8ccaf3b48e58c240`.
- **Step 3/5 baseline changed:** no.
- **Finding count:** **0 BLOCKER / 1 IMPORTANT / 3 MINOR**.
- **Commands technically reproducible as written:** yes. The target names,
  explicit binary paths, isolated `XDG_CONFIG_HOME`, global-option placement,
  instance/section hierarchy, loopback endpoint, client-line punctuation, and
  information-level listener/transport evidence all match the exact-revision
  qualification. The visible output does not overclaim payload proof.
- **Architecture/programming-model semantics:** correct in the draft prose and
  code excerpt. Endpoint/factory ownership, connection-driven `create(this)`,
  one active context, synchronous caller-thread `start()` dispatch, absence of
  a `tick()` claim, and the same-connection HTTP-to-WebSocket switch order are
  source-aligned. The two diagram findings above require only publication-level
  semantic clarification.
- **Release/platform/protocol evidence boundaries:** respected overall. The
  draft correctly bounds current release/package availability, Linux/GCC and
  Debian/x86-64 evidence, Bluetooth, TLS/security policy, HTTP 1.0/1.1,
  WebSocket 13, SSE, MQTT 3.1.1, MQTT over WebSocket, and downstream-project
  scope. Only the alternate-multiplexer qualification needs the minor explicit
  qualifier above.
- **Visual-status boundary:** `programming-model.svg` and
  `http-websocket-context-switch.svg` are technically validated working assets
  suitable for the draft; human publication approval and the two semantic
  refinements remain pending. `echo-connection-evidence.png` does not exist and
  is not referenced or treated as evidence by the draft.
- **Readiness for Claude Step 7b:** yes. There are no technical blockers. The
  draft may proceed to the independent editorial audit; Step 7c must resolve
  the publication links and apply the three precision corrections before the
  final README is publication-ready.

# Claude editorial audit

- **Audit date:** 29 August 2026
- **Reviewed artifact:** frozen [Step 6 draft](06-README-DRAFT.md) (257 lines, ~1,690 words)
- **Scope:** editorial only. The Codex technical audit above is fixed input; no
  technical claim, evidence boundary, command, or diagram semantic is
  reinterpreted here.
- **Working assets:** `programming-model.svg` and `http-websocket-context-switch.svg`
  are treated as current working assets; `echo-connection-evidence.png` is absent
  by design and the draft is structurally valid without it.

## Measured starting point

| Section | Words | Share |
| --- | --- | --- |
| Hero | 47 | 2.8% |
| Programming model | 322 | 19.0% |
| Run the echo pair | 333 | 19.7% |
| Capabilities and evidence | 469 | 27.7% |
| Architecture and extension points | 368 | 21.8% |
| Documentation, examples, and ecosystem routes | 150 | 8.9% |

The capabilities section is the heaviest block by words; the echo section is the
heaviest by lines (76 of 257). Both are dominated by material that is stated
elsewhere on the same page.

---

## HIGH — Qualification bookkeeping occupies the first viewport

- **Priority:** HIGH
- **Location:** draft line 9, metadata row: `**C++20** · [exact-head CI](…/actions/runs/33189174904) · [MIT OR LGPL-3.0-or-later]`
- **Problem:** `exact-head` is internal workflow vocabulary, and the link points
  at one historical run ID rather than a branch status. The first thing a
  visiting C++ developer reads after the value proposition is provenance
  bookkeeping they cannot interpret. Commit provenance is already stated
  correctly at lines 142–144, where it belongs.
- **Recommended action:** cut. Reduce the row to `**C++20** · [MIT OR LGPL-3.0-or-later]`,
  or substitute the ordinary branch CI status badge if one is wanted in the hero.
- **Reason:** the hero should carry product identity and license, not audit
  trail; the provenance note later in the page is the searchable, updatable home
  for the reviewed commit.

## HIGH — The programming model is explained four times before the code excerpt

- **Priority:** HIGH
- **Location:** draft lines 18–22 (intro paragraph, 38 w), line 24 (figure, whose
  in-image labels already read `configured endpoint flow`,
  `established connection object`, `application-supplied creation boundary`,
  `per connection / one active context`, `Event loop — start()`), lines 26–28
  (caption, 28 w), lines 30–36 (role table, 84 w)
- **Problem:** the same five relationships are asserted in prose, in the figure,
  in the caption, and again in the table — roughly 150 words plus a full-viewport
  graphic before the reader reaches a line of C++. The caption is the purest
  duplicate: it repeats convergence, `create(this)`, and `start()` from the
  paragraph directly above it.
- **Recommended action:** cut lines 26–28 entirely. Keep the table (it is the
  images-disabled fallback the shared page system requires) but shorten every
  Responsibility cell to a fragment of at most ten words — for example
  `SocketConnection` → "Established connection: addresses, stream mechanics,
  timeouts, active context."
- **Reason:** the reader reaches the code — the part that shows what writing
  SNode.C actually feels like — a screen earlier, and the section stops sounding
  like it is checking whether the point landed.

## HIGH — The first-success path leads with determinism scaffolding and never says why

- **Priority:** HIGH
- **Location:** draft lines 95–97 (`rm -rf` / `mkdir -p` config directory) and
  lines 102–105 / 112–115 (`XDG_CONFIG_HOME=…` prefix plus
  `--log-level 4 --log-format text --monochrom=true`)
- **Problem:** the commands are technically correct and Codex has confirmed them
  as reproducible; the editorial problem is presentation. Four lines of capture
  hygiene carry the same visual weight as the two commands that actually start a
  server and a client, and nothing tells the reader that the isolation and log
  flags exist to pin the output shown below. An evaluator skimming this block
  concludes that running SNode.C requires environment surgery.
- **Recommended action:** rewrite narrowly, without changing command semantics.
  Collapse the config-directory preparation to a single `mkdir -p` line inside
  the build block, and add one clause before the server command: "The isolated
  config directory and explicit log options pin the output shown below." Keep
  every option Codex validated.
- **Reason:** the reader distinguishes framework requirements from
  reproducibility scaffolding in one pass, which is the difference between "this
  looks fiddly" and "this is a controlled demonstration."

## HIGH — The "not a support matrix" boundary is stated eight times

- **Priority:** HIGH
- **Location:** lines 139–140; 149–151; 156; 157; 160; 161; 193–194; 224
- **Problem:** the same non-claim — source breadth does not equal tested
  combinations — appears in the echo section, the capabilities intro, four
  boundary cells, the architecture extension paragraph, and the configuration
  paragraph. Stated once it reads as discipline; stated eight times it reads as
  anxiety, and it trains the reader to skip the boundary column entirely.
- **Recommended action:** cut seven of the eight. Keep the capabilities intro
  statement (lines 149–151) as the single canonical version, shortened, and
  delete the restatements at 139–140, 156, 157, 160, 161, 193–194, and 224.
- **Reason:** a boundary stated once and clearly is believed; a boundary repeated
  in every section is filtered out as boilerplate, which is the opposite of the
  intended credibility effect.

## HIGH — Caveat mass dominates the capabilities section

- **Priority:** HIGH
- **Location:** lines 148–151 (intro, 41 w), the Boundary column of the table
  (90 w across nine rows), lines 165–175 (post-table caveats, 90 w)
- **Problem:** about 220 words — roughly 13% of the whole README — are negative
  statements, concentrated in one section, and several are duplicated inside it:
  the performance non-claim appears at line 155 and again at lines 172–173; the
  TLS-policy boundary at line 157 and again at line 173; release/package
  availability at line 163 and again at lines 165–167. The section that should
  answer "what can I build with this?" currently answers "what may I not
  conclude?" first and at greater length.
- **Recommended action:** shorten. Cut Boundary cells to at most six words each
  and delete the three duplicated pairs; compress lines 165–175 to two sentences
  (release/package status; platform breadth) and let
  [`docs/capabilities.md`](../docs/capabilities.md) hold the rest.
- **Reason:** an evaluator can read the breadth in one pass and still meet every
  boundary once, instead of reading a disclaimer beside every capability.

## HIGH — The HTTP-to-WebSocket sequence is stated three times

- **Priority:** HIGH
- **Location:** lines 196–203 (prose, 77 w), line 205 (figure, which already
  carries numbered stages 1–4 plus the post-callback detach → pointer change →
  attach annotations), lines 207–211 (caption, 44 w)
- **Problem:** the caption is a near-verbatim restatement of the paragraph above
  it, and both restate the figure's own labels. The page spends ~120 words plus a
  figure on an API call ordering that belongs in architecture documentation,
  while the point a landing-page reader needs — the connection survives the
  protocol change — is buried inside the sequence.
- **Recommended action:** shorten the prose to the mechanism and its consequence
  ("During an HTTP upgrade the WebSocket factory creates a replacement context;
  the HTTP context detaches with `DetachReason::ContextSwitch` and the WebSocket
  context attaches to the same `SocketConnection`."), move the
  staging/`response->end()`/callback-return ordering to
  [`docs/architecture.md`](../docs/architecture.md), and cut the caption to one
  line ("Same connection, new active context.").
- **Reason:** the differentiator lands immediately instead of arriving at the end
  of a four-step API narration. This does not weaken the Codex finding on the
  figure: the corrected figure remains the place where the full validated
  ordering is shown, and the retained prose still states the mechanism, so the
  page stays complete with images disabled.

---

## MEDIUM — The tagline is marked up as a section heading

- **Priority:** MEDIUM
- **Location:** draft line 3, `## Event-driven network clients and servers in C++20`
- **Problem:** the tagline becomes an entry in GitHub's README outline and an
  anchor target, so the document structure reads as six sections where the first
  one has no content of its own.
- **Recommended action:** rewrite narrowly as a bold line or blockquote directly
  under `# SNode.C`.
- **Reason:** the outline then lists only real destinations, which matters for
  the in-page anchors the hero already uses.

## MEDIUM — The value proposition repeats the headline and omits the consequence

- **Priority:** MEDIUM
- **Location:** draft lines 3–7
- **Problem:** "Build C++20 network clients and servers" restates the headline
  verbatim, so the first two lines spend 40 words establishing the category
  twice. What is missing is the reason the model matters, which the design
  identifies as the section takeaway but which never reaches the first viewport:
  application behaviour is connection-local, socket and event mechanics are not.
- **Recommended action:** rewrite narrowly, keeping the approved meaning — e.g.
  "One recurring model: configure an endpoint, take the connection it
  establishes, and attach protocol behaviour to that connection while the event
  loop drives lifecycle and I/O. Application code stays connection-local; socket
  and dispatch mechanics stay outside it."
- **Reason:** an experienced networking developer learns in one screen not only
  what SNode.C is but why its object model is worth another minute.

## MEDIUM — Design rationale leaks into the code-excerpt lead-in

- **Priority:** MEDIUM
- **Location:** draft lines 38–40
- **Problem:** "without exposing the endpoint template stack" explains an
  editorial decision to the reader, and "abridged excerpt from the verified echo
  source" spends words on provenance that the link itself carries.
- **Recommended action:** shorten to one line: "The supplied echo context shows
  how a context handles its connection:" with the same link.
- **Reason:** the code follows immediately instead of after a paragraph about why
  the code looks the way it does.

## MEDIUM — Prerequisites carry dependency detail the landing page does not need

- **Priority:** MEDIUM
- **Location:** draft lines 75–78
- **Problem:** seven prerequisites plus a conditional network-access note for a
  pinned transitive dependency, delivered as a 44-word block before the reader
  has run anything. The spdlog clause in particular is build-system detail with a
  hedge attached.
- **Recommended action:** shorten to one line naming the compiler, CMake, Ninja,
  OpenSSL, and nlohmann/json requirement; move the spdlog fetch note to the
  deeper build documentation.
- **Reason:** the reader reaches the first command sooner and meets edge cases
  only if the build actually raises them.

## MEDIUM — The output-boundary paragraph re-narrates code already shown

- **Priority:** MEDIUM
- **Location:** draft lines 130–135 (103 w)
- **Problem:** the paragraph re-describes the client greeting and the
  read-and-reflect behaviour that the excerpt at lines 42–59 already showed
  literally, then adds the payload-visibility boundary and the teardown
  instruction. The boundary is the only part the reader cannot get elsewhere.
- **Recommended action:** shorten to two sentences: "These lines prove the
  listener started and one plain IPv4 loopback connection formed; at the default
  log level the reflected payload is not printed. The pair keeps echoing until
  you stop both with Ctrl-C."
- **Reason:** the honesty note becomes prominent instead of being diluted by a
  retelling of the source.

## MEDIUM — The variants sentence re-litigates the support-matrix boundary

- **Priority:** MEDIUM
- **Location:** draft lines 139–140, second sentence
- **Problem:** the first sentence usefully records that IPv6, Unix-domain, and one
  mutual-TLS path were also qualified. The second immediately withdraws the
  implication, one paragraph before the capabilities section makes the same point
  as its opening statement.
- **Recommended action:** cut the second sentence (see the consolidated HIGH
  finding above).
- **Reason:** the page stops apologising for information it just supplied.

## MEDIUM — The provenance note is written from inside the workflow

- **Priority:** MEDIUM
- **Location:** draft lines 142–144
- **Problem:** "At draft time, public `master` still resolves to that commit"
  exposes the drafting stage to the public reader, and three lines are spent on a
  fact that needs one.
- **Recommended action:** shorten to a single line: "Commands and output verified
  against [`bf01683`](…) on 29 August 2026."
- **Reason:** the provenance stays credible and updatable without narrating the
  editorial process.

## MEDIUM — Configuration and installed consumption are each stated twice

- **Priority:** MEDIUM
- **Location:** table rows at lines 162 and 163 versus the architecture paragraph
  at lines 213–224
- **Problem:** configuration precedence appears as a Boundary cell at line 162 and
  again as a bold standalone line at 218; installed CMake components appear as a
  table row at 163 and again at lines 222–224. Neither pair adds anything the
  other lacks.
- **Recommended action:** cut both rows from the capabilities table and keep the
  architecture paragraph, which explains the same facts in context.
- **Reason:** the capability table stays about networking and protocol breadth,
  which is what an evaluator scans it for.

## MEDIUM — Ledger vocabulary appears in public copy

- **Priority:** MEDIUM
- **Location:** lines 9, 155, 222 (`exact-head`); line 155 ("root-configured CTest
  suite"); line 156 ("preserved echo runtime runs"); line 157 ("one mutual-TLS
  IPv4 echo arrangement"); line 223 ("staged installed consumers")
- **Problem:** these are the internal evidence register's terms. A reader who has
  not seen the workflow cannot tell whether "exact-head" is a branch, a build
  mode, or a policy, so precise scoping reads as jargon rather than rigour.
- **Recommended action:** rewrite narrowly to plain equivalents with identical
  scope — "CI on this commit ran the full test suite"; "component tests plus
  recorded echo runs"; "one mutual-TLS IPv4 echo run"; "tests that install the
  library and build against it".
- **Reason:** the same evidence boundaries survive, but they are now legible to
  the audience they are meant to protect.

## MEDIUM — The generic layer table asks questions the page has already answered

- **Priority:** MEDIUM
- **Location:** draft lines 182–189 (86 w, six rows)
- **Problem:** the table lists questions without answering them, and two rows —
  Event runtime and Application context — restate the programming-model section
  in weaker form. It reads as a taxonomy exercise placed between two sections
  that are doing real work.
- **Recommended action:** shorten to the three rows the page has not already
  covered (address/network family, physical stream, connection mode), or replace
  the table with the single sentence at lines 179–180 plus a link to
  [`docs/architecture.md`](../docs/architecture.md).
- **Reason:** the architecture section gets to its actual payload — the context
  switch — without an intervening abstraction layer.

## MEDIUM — The page ends on a disclaimer instead of a next action

- **Priority:** MEDIUM
- **Location:** draft lines 244–257
- **Problem:** the final three sentences are boundary statements, two of which
  duplicate clauses already inside the bullets above them ("where configured",
  "belongs to CodexUI, not SNode.C"). The approved journey ends at "choose the
  next route", but the last thing the reader sees is what the ecosystem is not.
- **Recommended action:** merge into one closing sentence — "AISuite and CodexUI
  are independent open-source projects, not official OpenAI products; the two
  current paths are SNode.C → MQTTSuite and SNode.C → AISuite → CodexUI." — and
  drop the duplicated clauses from the bullets, so the route list is the final
  beat.
- **Reason:** the page closes on where to go next, which is the section's job.

## MEDIUM — "Current" is doing compliance work, not editorial work

- **Priority:** MEDIUM
- **Location:** page-wide; `current` appears 17 times, `qualif*` 9, `evidence` 8
- **Problem:** the qualifier is mostly redundant — a page that states its reviewed
  commit is by definition describing the current source — and its density gives
  the copy the cadence of an audit report rather than a framework landing page.
- **Recommended action:** cut roughly two-thirds of the instances, keeping it only
  where it contrasts with a past or future state (release status, MQTT version
  scope).
- **Reason:** shorter sentences, same precision, and the remaining instances
  regain their meaning.

---

## LOW — Filler qualifiers

- **Priority:** LOW
- **Location:** line 64 ("where appropriate"); line 149 ("deliberately"); line 118
  ("the verified run contains these diagnostic signals")
- **Problem:** each softens or annotates a sentence that is stronger without it.
- **Recommended action:** cut. "Applications remain free to introduce their own
  concurrency."; "The table is not a support matrix"; "Ignoring timestamps and
  logger prefixes, the run produces:".
- **Reason:** the technical-product voice tightens without any loss of meaning.

## LOW — The context-replacement preview should be a link

- **Priority:** LOW
- **Location:** draft lines 66–68
- **Problem:** the sentence points forward to "the HTTP-to-WebSocket upgrade later
  in this README" as plain text, so the reader who wants it immediately has to
  scroll and search.
- **Recommended action:** rewrite narrowly as an anchor link to
  `#architecture-and-extension-points`.
- **Reason:** the page's most interesting consequence becomes reachable at the
  moment it is promised.

## LOW — Visual 1's canvas is nearly square where the design calls for wide and shallow

- **Priority:** LOW
- **Location:** `assets/programming-model.svg`, 920 × 940 viewBox, embedded at
  draft line 24
- **Problem:** a near-1:1 figure consumes most of a viewport immediately after the
  hero and pushes the role table and code excerpt below the fold. The Step 4/5
  intent is one wide, shallow lifecycle figure.
- **Recommended action:** note for the deferred publication refinement pass; no
  Step 7c action. Aspect ratio only — semantics and labels are unaffected.
- **Reason:** page flow, not artwork quality; recorded here only because it
  affects how much of the centerpiece section is visible at once.

## LOW — The figure-free stretch is a length problem, not a missing-visual problem

- **Priority:** LOW
- **Location:** draft lines 26–205 (echo and capabilities sections)
- **Problem:** roughly 110 lines separate the two figures. The absence of Visual 2
  is not the cause; the length of the echo and capabilities sections is.
- **Recommended action:** no new visual. Applying the HIGH and MEDIUM cuts above
  closes the gap on its own.
- **Reason:** the page balance resolves through subtraction, and the draft's
  design intent of working without the echo capture is confirmed.

---

## Editorial summary

**Overall editorial verdict:** structurally sound, editorially over-qualified.
The approved architecture is right, the centerpiece is in the right place, the
code excerpt is the right size and arrives at the right moment, and the primary
CTA is clear. What weakens the page is not what it says but how many times it
says it: every major mechanism and every evidence boundary is stated in prose, in
a figure, in a caption, and in a table cell. Step 7c should be a subtraction
pass. No re-architecture, no new sections, and no new visuals are recommended.

**Finding counts:** **6 HIGH / 12 MEDIUM / 4 LOW** (22 total).

**Largest source of unnecessary length and friction:** duplicated evidence
boundaries. The support-matrix non-claim alone appears eight times, and the
capabilities section devotes about 220 words — roughly 13% of the README — to
negative statements, three pairs of which duplicate each other. The
second-largest source is the programming-model and context-switch material, each
stated three or four times across prose, figure, caption, and table. Applying the
cuts above removes an estimated 300–400 words, about 20% of the page, without
losing a single technical claim or boundary.

**Does the approved reader journey still work?** Yes. All six stages are present
and in order: orient, understand the model, run a real path, assess breadth, see
the deeper consequence, choose a route. The journey is slowed rather than broken —
stage 3 is delayed by determinism scaffolding presented without explanation, and
stage 4 leads with disclaimers before breadth. Both are length and sequencing
problems inside approved sections, not journey failures.

**Ready for the controlled Step 7c rewrite?** Yes. There is no editorial blocker
and no finding that requires reopening Step 4 or Step 5. Step 7c should apply the
Codex technical corrections first — publication link destinations, the
multiplexer qualifier, and the two diagram semantics — and then treat this audit
as a subtraction list, preserving every evidence boundary in exactly one place
rather than removing any of them.
