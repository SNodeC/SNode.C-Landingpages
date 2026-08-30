# Canonical AI-assisted README workflow

This document defines the canonical handoff, chat/session topology, and
publication workflow for the SNode.C ecosystem landing pages.

SNode.C itself established the quality bar, evidence discipline, visual language,
Figma workflow, responsive-figure rules, publication validation, and closure
pattern. The remaining presentations reuse that foundation instead of repeating
SNode.C's exploratory work.

The accelerated execution order is:

1. **MQTTSuite**
2. **AISuite**
3. **CodexUI**
4. **SNode.C organization profile** after the three product destinations are stable

SNode.C is the completed reference implementation. Reuse its **quality, evidence
standard, prose discipline, responsive/Figma practices, and publication
hygiene**. Do not copy its section order or visual composition mechanically.

---

# 1. Canonical handoff rule

**No AI step may depend on previous chat history. Every step must read its
specified repository artifacts and save its complete result to the specified
repository artifact.**

A conversation may provide convenience and continuity, but repository Markdown
is the handoff source of truth. If chat memory and a repository artifact differ,
the repository artifact wins.

The standard per-project artifact set is:

```text
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md
<Project>/workflow/06-README-DRAFT.md
<Project>/workflow/07-FINAL-REVIEWS.md
<Project>/README.md
<Project>/assets/
<Project>/assets/src/
```

Do not create extra workflow stages merely because SNode.C needed additional
closure passes while the process itself was still being invented. For the
remaining projects, Steps 4–7 are deliberately compressed operationally.

---

# 2. AI roles, models, and reasoning

| Task | AI | Model policy | Reasoning |
| --- | --- | --- | --- |
| Technical truth / source verification | Codex | strongest current Codex model | **xhigh** |
| README structure / visual storyboard | ChatGPT | GPT-5.6 Sol or current successor | **High** |
| Visual semantics / command validation | Codex | strongest current Codex model | **High** |
| Figma production / screenshot composition | ChatGPT + Figma | GPT-5.6 Sol or current successor | **High** |
| README draft | ChatGPT | GPT-5.6 Sol or current successor | **High** |
| Final technical audit | Codex | strongest current Codex model | **xhigh** |
| Final editorial audit | Claude | strongest available Opus-class model | **High** |
| Final controlled edit / publication | ChatGPT | GPT-5.6 Sol or current successor | **High** |

Do **not** use Max/Ultra by default. Escalate Codex to Max only when Step 3 or
Step 7 exposes conflicting source/test/release evidence that xhigh cannot resolve
cleanly. Ultra is not part of the normal publication workflow.

Role shorthand:

```text
Codex   → Is it true?
ChatGPT → What should we communicate, and how?
Claude  → What is weak, generic, verbose, or badly presented?
Human   → Is this actually the project, and does it look professional?
```

---

# 3. Global foundation — already completed

Steps 1 and 2 are one-time ecosystem work. They are not repeated for each
remaining repository.

## 0.1 — Global — Repository Audit

**AI:** Codex  
**Reasoning:** High  
**Artifact:** `workflow/01-REPOSITORY-AUDIT.md`  
**Status:** completed

## 0.2 — Global — Ecosystem Positioning

**AI:** ChatGPT  
**Reasoning:** High  
**Artifact:** `workflow/02-ECOSYSTEM-POSITIONING.md`  
**Status:** completed

Do not rerun either step unless the ecosystem itself changes materially.

## SNode.C reference publication

SNode.C is complete and serves as the reference implementation for this
workflow. Its later workflow files document how the quality bar, Figma source
of truth, responsive figures, evidence boundaries, independent review, and
closure hygiene were established.

Do **not** rerun the SNode.C workflow merely to make its historical chat/session
numbering match the scheme below.

---

# 4. Reproducible chat/session topology

The remaining work uses a deliberate chat tree. The purpose is to preserve a
clean project-level workspace while preventing one execution step from silently
depending on the prose or reasoning of the previous step.

## 4.1 One fresh Workflow Root chat per project

For every remaining presentation, start **one completely fresh ChatGPT chat**.
It is the parent/control chat for that project and does no substantive drafting.

Names:

```text
1.0 — MQTTSuite — Workflow Root
2.0 — AISuite — Workflow Root
3.0 — CodexUI — Workflow Root
4.0 — SNode.C Organization — Workflow Root
```

The root chat should receive only the bootstrap prompt below.

### Workflow Root bootstrap prompt

```text
We are executing the canonical accelerated README publication workflow for
<Project> in:

SNodeC/SNode.C-Landingpages

Read and follow:
- AGENTS.md
- workflow/README-GOVERNANCE.md
- workflow/README-WORKFLOW.md
- workflow/01-REPOSITORY-AUDIT.md
- workflow/02-ECOSYSTEM-POSITIONING.md
- <Project>/AGENTS.md

This is the Workflow Root chat for <Project>. Do not perform a workflow step in
this root chat. Its purpose is only to be the stable parent for the ChatGPT
execution branches defined by workflow/README-WORKFLOW.md.

Repository artifacts are authoritative; no child step may depend on inherited
chat history for technical or editorial decisions.
```

## 4.2 Forking rule for ChatGPT steps

Every substantive ChatGPT step is a **new fork/branch from the project's `.0`
Workflow Root chat**.

Do **not** fork Step 6 from Step 4, or Step 7c from Step 6. Always fork from `.0`.
The new branch then reads the latest repository workflow artifacts produced by
all preceding systems.

This gives practical project continuity without making one execution chat a
hidden dependency of the next.

## 4.3 Codex and Claude sessions are always fresh

Codex and Claude do not need the ChatGPT tree. Start a **fresh independent
session** for every Codex or Claude stage and provide the exact canonical prompt
for that stage.

They must read the repository handoff files. Do not paste previous AI reasoning
as substitute context.

## 4.4 Parallel review rule

`<n>.7A` and `<n>.7B` are started independently and may run in parallel because
both review the same frozen Step 6 candidate.

Do not let Claude rewrite the draft before Codex sees it, and do not let Codex's
technical findings become an editorial rewrite before Claude reviews the same
candidate.

## 4.5 Chat naming convention

Use the following exact form:

```text
<ProjectIndex>.<WorkflowStep><OptionalLetter> — <Project> — <Purpose>
```

Example:

```text
1.3  — MQTTSuite — Technical Truth
1.4  — MQTTSuite — README + Visual Design
1.5A — MQTTSuite — Visual Technical Validation
1.5B — MQTTSuite — Figma + Capture Production
1.6  — MQTTSuite — Frozen README Draft
1.7A — MQTTSuite — Final Technical Audit
1.7B — MQTTSuite — Final Editorial Audit
1.7C — MQTTSuite — Finalization + Publish
```

This numbering is repeated exactly for AISuite (`2.x`), CodexUI (`3.x`), and the
organization profile (`4.x`).

---

# 5. Generic accelerated per-project workflow

The normal per-project flow is:

```text
fresh project Workflow Root (.0)
        │
        ├── fresh Codex (.3) ───────────────→ 03-TECHNICAL-FACTS.md
        │
        ├── fork ChatGPT from .0 (.4) ─────→ 04-README-DESIGN.md
        │                                      05-VISUALS.md initial
        │
        ├── fresh Codex (.5A) ─────────────→ 05-VISUALS.md VALIDATED
        │
        ├── fork ChatGPT from .0 (.5B) ─────→ Figma / captures / assets
        │                                      Human approval
        │
        ├── fork ChatGPT from .0 (.6) ──────→ 06-README-DRAFT.md
        │
        ├── fresh Codex (.7A) ───────┐
        │                             ├────────→ 07-FINAL-REVIEWS.md
        ├── fresh Claude (.7B) ──────┘
        │
        └── fork ChatGPT from .0 (.7C) ─────→ README.md + final validation
                                               commit/push when requested
```

This is the canonical compression of Steps 4–7. It removes exploratory review
loops while preserving independent technical and editorial gates.

---

# 6. Step 3 — Technical truth

**Session type:** fresh Codex  
**Reasoning:** xhigh  
**Output:** `<Project>/workflow/03-TECHNICAL-FACTS.md`

This remains the deep, non-negotiable step. Speed comes from presentation reuse,
not weaker source verification.

Read:

```text
AGENTS.md
workflow/README-GOVERNANCE.md
workflow/README-WORKFLOW.md
workflow/01-REPOSITORY-AUDIT.md
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/AGENTS.md
relevant existing <Project>/ material
current public source repository HEAD
```

Stop when a later writer can produce the README without reopening the source
repository for ordinary claims. Explicit unresolved facts are allowed.

---

# 7. Step 4 — README design + visual storyboard

**Session type:** ChatGPT fork from `<n>.0` Workflow Root  
**Reasoning:** High  
**Outputs:**

```text
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md  # initial storyboard
```

The story and visuals are designed together in one pass.

Read:

```text
workflow/01-REPOSITORY-AUDIT.md
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/AGENTS.md
SNode.C/README.md
SNode.C/workflow/09-FIGMA-RESPONSIVE-FIGURES.md
```

SNode.C is a quality/style reference only.

Decide:

- headline and value proposition;
- primary audience;
- reader journey and section order;
- centerpiece;
- fastest useful first success;
- highest-value API/product surface to show;
- proof to keep in README versus deeper docs;
- CTA/next-step routing;
- visual/text rhythm;
- only the visuals that materially help comprehension.

No separate abstract “visual ideas” stage follows Step 4.

---

# 8. Step 5 — One visual-validation gate, then production

## 8.1 Step 5A — Codex validation

**Session type:** fresh Codex  
**Reasoning:** High  
**Output:** updated `<Project>/workflow/05-VISUALS.md`

Validate once:

- every component/ownership boundary;
- every dependency/runtime arrow;
- protocol/version wording;
- screenshot state;
- commands and fixture data;
- what the screenshot actually proves;
- responsive variants and filenames.

Mark each final visual `VALIDATED`.

## 8.2 Step 5B — Figma + capture production

**Session type:** ChatGPT fork from `<n>.0` Workflow Root  
**Reasoning:** High

Read the now-validated `05-VISUALS.md` and produce the assets immediately.

### Figures

- create/edit in **Figma**;
- Figma is the editable source of truth;
- publication exports go under `<Project>/assets/`;
- source/export counterparts go under `<Project>/assets/src/`;
- use desktop/mobile art direction only when needed;
- do not hand-edit SVG geometry after Figma export;
- verify mobile readability, fallback-font clearance, light/dark behavior,
  accessibility title/description, and provenance.

### Screenshots

- capture real source-aligned builds only;
- use deterministic synthetic data;
- never use live/private account or desktop state;
- keep capture scripts/fixtures/provenance in `assets/src/` or `05-VISUALS.md`;
- Figma may compose/crop/annotate but must not fake functionality.

### Human gate

Record once:

```text
Human approval: APPROVED
```

A rejected visual is corrected locally. It does not reopen README structure
unless the centerpiece itself is wrong.

---

# 9. Step 6 — Frozen README candidate

**Session type:** ChatGPT fork from `<n>.0` Workflow Root  
**Reasoning:** High  
**Output:** `<Project>/workflow/06-README-DRAFT.md`

Use only verified facts, approved structure, validated visuals, and approved
captures.

Rules:

- README = landing page, not qualification report;
- orient → differentiate → proof → first success → fit-check → route deeper;
- show the most attractive relevant API/product surface once;
- prefer omission over completeness;
- keep evidence boundaries explicit but not repetitive;
- remove workflow/governance vocabulary from public prose;
- do not self-review in another ChatGPT stage.

Freeze the candidate and proceed directly to Step 7.

---

# 10. Step 7 — Parallel reviews + one finalization

## 10.1 Step 7A — Final technical audit

**Session type:** fresh Codex  
**Reasoning:** xhigh

Review only:

- incorrect/unsupported/stale claims;
- broken commands;
- wrong visual semantics;
- over-broad evidence boundaries;
- release/package/platform claims not supported by evidence.

Write under `# Codex technical audit` in
`<Project>/workflow/07-FINAL-REVIEWS.md`.

## 10.2 Step 7B — Final editorial audit

**Session type:** fresh Claude  
**Reasoning:** High

Review only:

- generic or AI-sounding wording;
- weak hierarchy;
- excessive qualification/process language;
- duplication/verbosity;
- poor visual/text rhythm;
- missing high-value product/API demonstration;
- avoidable quick-start friction;
- weak CTA/ending.

Write under `# Claude editorial audit` in the same artifact.

## 10.3 Step 7C — Finalization + publish

**Session type:** ChatGPT fork from `<n>.0` Workflow Root  
**Reasoning:** High

Read every canonical artifact plus both audits. Apply accepted findings once.
Technical corrections from Codex take precedence.

Write:

```text
<Project>/README.md
```

Complete `07-FINAL-REVIEWS.md` with:

```text
# Accepted changes
# Rejected findings and reasons
# Validation
# Final status
```

Then perform repository-native publication validation and, when explicitly
requested, commit/push the complete package.

Do not start another review cycle unless the re-review trigger rules in this file
are met.

---

# 11. Full project plan — MQTTSuite

**Project index:** `1`  
**Landingpages directory:** `MQTTSuite/`  
**Public source:** `SNodeC/mqttsuite`  
**Narrative center:** five MQTT applications and the real message/integration flow

Expected total workflow effort after foundation reuse: **about 2–3 hours**.

## 1.0 — MQTTSuite — Workflow Root

**System:** ChatGPT  
**Chat:** completely fresh  
**Purpose:** parent/control chat only

Use the Workflow Root bootstrap prompt from §4.1 with `<Project> = MQTTSuite`.

## 1.3 — MQTTSuite — Technical Truth

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh  
**Output:** `MQTTSuite/workflow/03-TECHNICAL-FACTS.md`

Verify specifically:

- MQTTBroker, MQTTIntegrator, MQTTBridge, MQTTCli, MQTTStore roles;
- MQTT 3.1.1 scope and important non-claims;
- actual broker/client/integrator/bridge/store relationships;
- topic/payload mapping semantics;
- bridge forwarding/loop-prevention semantics;
- MQTTStore raw envelope versus typed projection behavior;
- Web UI behavior relevant to screenshots;
- exact first-success broker/subscriber/publisher path;
- transport/application-role evidence boundaries;
- TLS/credentials/storage/operator-owned policy;
- current compatible SNode.C relationship;
- release/package/platform evidence.

### Prompt

```text
Continue the canonical accelerated README workflow for MQTTSuite.

Read and follow:
- AGENTS.md
- workflow/README-GOVERNANCE.md
- workflow/README-WORKFLOW.md
- workflow/01-REPOSITORY-AUDIT.md
- workflow/02-ECOSYSTEM-POSITIONING.md
- MQTTSuite/AGENTS.md

Perform Step 3 only.

Verify README-relevant technical truth against current public
SNodeC/mqttsuite HEAD and any required compatible SNode.C evidence.

Establish the exact roles and relationships of MQTTBroker, MQTTIntegrator,
MQTTBridge, MQTTCli and MQTTStore; MQTT 3.1.1 and transport scope; mapping,
bridging, loop-prevention and storage behavior; the Web UI; the shortest real
broker/subscriber/publisher first success; dependencies, release/package/platform
scope, security/credential/storage boundaries and genuine differentiators.

Flag stale or unsupported existing Landingpages claims. Do not redesign or write
the README.

Save the self-contained result to:
MQTTSuite/workflow/03-TECHNICAL-FACTS.md
```

## 1.4 — MQTTSuite — README + Visual Design

**System:** ChatGPT  
**Chat:** fork from `1.0`, not from any previous execution chat  
**Reasoning:** High

Design around:

- immediate identity as a toolkit of five focused MQTT applications;
- application chooser early enough that the reader knows which executable fits;
- one fastest broker → subscriber → publisher success path;
- centerpiece showing broker/integrator/bridge/store message flow;
- Web UI as real product evidence, not as the whole product identity;
- clear MQTT 3.1.1 and evidence boundaries without a giant matrix.

Likely visual inventory:

1. one application/message-flow figure;
2. one genuine Web UI screenshot if it materially proves the product;
3. optional second flow/topology only if needed for bridge/integrator semantics.

### Prompt

```text
Perform accelerated Step 4 for MQTTSuite.

Read the canonical workflow inputs and
MQTTSuite/workflow/03-TECHNICAL-FACTS.md.
Use SNode.C only as the established quality/style reference.

Design the README reader journey and visual storyboard together.

The narrative center is the five applications and a real MQTT message/integration
flow. Make project selection obvious, provide one fast broker/subscriber/publisher
success path, and show the Web UI only as real supporting evidence.

Save the complete README design to:
MQTTSuite/workflow/04-README-DESIGN.md

Create/update the initial visual plan in:
MQTTSuite/workflow/05-VISUALS.md

Mark technical visual semantics PENDING CODEX VALIDATION.
Do not write the full README yet.
```

## 1.5A — MQTTSuite — Visual Technical Validation

**System:** Codex  
**Session:** fresh  
**Reasoning:** High

Validate every message-flow arrow, topic/payload transformation, bridge direction,
storage relation, screenshot state, fixture, and command. Update
`MQTTSuite/workflow/05-VISUALS.md` to `VALIDATED`.

## 1.5B — MQTTSuite — Figma + Capture Production

**System:** ChatGPT + Figma  
**Chat:** fork from `1.0`  
**Reasoning:** High

Create validated diagrams in Figma and capture the real Web UI from a qualified
synthetic scenario if approved. Record source counterparts and human approval.

## 1.6 — MQTTSuite — Frozen README Draft

**System:** ChatGPT  
**Chat:** fork from `1.0`  
**Reasoning:** High  
**Output:** `MQTTSuite/workflow/06-README-DRAFT.md`

Show the toolkit, application choice, real first success, central message flow,
evidence boundaries, and next steps. Avoid turning the page into five manuals.

## 1.7A — MQTTSuite — Final Technical Audit

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh

## 1.7B — MQTTSuite — Final Editorial Audit

**System:** Claude  
**Session:** fresh  
**Reasoning:** High

Run 1.7A and 1.7B in parallel against the same frozen Step 6 draft.

## 1.7C — MQTTSuite — Finalization + Publish

**System:** ChatGPT  
**Chat:** fork from `1.0`  
**Reasoning:** High

Apply accepted findings, validate dependency closure, update
`MQTTSuite/README.md`, complete `07-FINAL-REVIEWS.md`, and commit/push when
requested.

---

# 12. Full project plan — AISuite

**Project index:** `2`  
**Landingpages directory:** `AISuite/`  
**Public source:** `SNodeC/AISuite`  
**Narrative center:** typed integration plus provider/bridge/client authority
boundaries

Expected total workflow effort: **about 2–3.5 hours**.

## 2.0 — AISuite — Workflow Root

**System:** ChatGPT  
**Chat:** completely fresh

Use the Workflow Root bootstrap prompt with `<Project> = AISuite`.

## 2.3 — AISuite — Technical Truth

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh  
**Output:** `AISuite/workflow/03-TECHNICAL-FACTS.md`

Verify specifically:

- what AISuite adds beyond raw JSON-RPC;
- typed C++ access and TypeScript SDK/package reality;
- generator/schema/revision boundaries;
- `getRaw()` and raw submission paths where relevant;
- codex-bridge and reference-client roles;
- provider/controller/observer semantics;
- one-provider/multi-client routing boundaries;
- persistence and semantic authority ownership;
- provider-side versus frontend-side transports without conflation;
- listener/static-file/WebSocket behavior;
- harmless first-success request and expected result;
- SNode.C compatibility and package/install surface;
- release/license/npm/package evidence and open gaps;
- independent-project/OpenAI wording.

### Prompt

```text
Continue the canonical accelerated README workflow for AISuite.

Read and follow the canonical workflow/governance files and AISuite/AGENTS.md.
Perform Step 3 only.

Verify README-relevant facts against current public SNodeC/AISuite HEAD and the
required compatible SNode.C/schema evidence.

Establish typed C++ and TypeScript integration surfaces, generation/schema scope,
raw access, codex-bridge/reference-client roles, provider/controller/observer
behavior, routing and authority boundaries, provider-side versus frontend-side
transports, listener behavior, first-success path, package/release/license scope,
and independent-project boundaries.

Flag stale/unsupported Landingpages claims. Do not write or redesign the README.

Save:
AISuite/workflow/03-TECHNICAL-FACTS.md
```

## 2.4 — AISuite — README + Visual Design

**System:** ChatGPT  
**Chat:** fork from `2.0`  
**Reasoning:** High

Design around:

- developer value before protocol jargon;
- typed access and bridge purpose immediately visible;
- one harmless bridge/reference-client first success;
- centerpiece that makes provider/bridge/client authority boundaries obvious;
- typed generation/SDK surface shown only where it aids evaluation;
- CodexUI as a concise consumer example, not the protagonist;
- independent-project notice placed naturally, not defensively.

Likely visual inventory:

1. one bridge/authority-boundary figure;
2. one typed-generation or C++/TS integration figure only if it explains a real
   differentiator;
3. optional real terminal/client proof if it is compact and useful.

### Prompt

```text
Perform accelerated Step 4 for AISuite.

Read the canonical inputs and AISuite/workflow/03-TECHNICAL-FACTS.md.
Use SNode.C only as the established quality/style reference.

Design the README and visual storyboard together. Lead with developer value:
typed C++/TypeScript access and a bounded multi-client bridge. Make provider,
bridge, controller/observer, persistence and client authority boundaries clear
without leading with protocol-internal terminology.

Define one harmless reproducible bridge/client first success and only the visuals
needed to explain the architecture and typed integration.

Save:
AISuite/workflow/04-README-DESIGN.md
AISuite/workflow/05-VISUALS.md

Mark visual semantics PENDING CODEX VALIDATION. Do not write the full README.
```

## 2.5A — AISuite — Visual Technical Validation

**System:** Codex  
**Session:** fresh  
**Reasoning:** High

Validate authority labels, provider/client directions, controller/observer
semantics, transport separation, schema/generation arrows, and any terminal
scenario. Update `AISuite/workflow/05-VISUALS.md` to `VALIDATED`.

## 2.5B — AISuite — Figma + Capture Production

**System:** ChatGPT + Figma  
**Chat:** fork from `2.0`  
**Reasoning:** High

Produce validated figures in Figma and real terminal/client capture only where
approved. Preserve source counterparts and independent-project wording.

## 2.6 — AISuite — Frozen README Draft

**System:** ChatGPT  
**Chat:** fork from `2.0`  
**Reasoning:** High

Write one landing page that shows what developers actually integrate, why the
bridge exists, what it owns/does not own, one quick success, and where deeper
protocol/compatibility material lives.

## 2.7A — AISuite — Final Technical Audit

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh

## 2.7B — AISuite — Final Editorial Audit

**System:** Claude  
**Session:** fresh  
**Reasoning:** High

Run in parallel against the same frozen candidate.

## 2.7C — AISuite — Finalization + Publish

**System:** ChatGPT  
**Chat:** fork from `2.0`  
**Reasoning:** High

Finalize once, validate, update `AISuite/README.md`, complete the review artifact,
and commit/push when requested.

---

# 13. Full project plan — CodexUI

**Project index:** `3`  
**Landingpages directory:** `CodexUI/`  
**Public source:** `SNodeC/CodexUI`  
**Narrative center:** the actual native/browser user workflow and visible product
state

Expected total workflow effort: **about 3–4.5 hours**, mainly because genuine
native/browser screenshots and state correctness require more care.

## 3.0 — CodexUI — Workflow Root

**System:** ChatGPT  
**Chat:** completely fresh

Use the Workflow Root bootstrap prompt with `<Project> = CodexUI`.

## 3.3 — CodexUI — Technical Truth

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh  
**Output:** `CodexUI/workflow/03-TECHNICAL-FACTS.md`

Verify specifically:

- native Qt and browser presentation reality;
- thread/turn/prompt/tool/background-work workflow;
- target, active turn, running, selected/inspected distinctions;
- controller/observer behavior as exposed to the UI;
- reconnect and state-restoration boundaries;
- what AISuite owns versus what CodexUI owns;
- what the Codex app-server owns;
- native/browser shared behavior and genuine differences;
- current install/package/release paths;
- SNode.C/AISuite/schema compatibility;
- real screenshotable states and synthetic fixture;
- privacy/logging/credential boundaries;
- independent-project wording.

### Prompt

```text
Continue the canonical accelerated README workflow for CodexUI.

Read the canonical workflow/governance files and CodexUI/AGENTS.md.
Perform Step 3 only.

Verify README-relevant facts against current public SNodeC/CodexUI HEAD plus the
required compatible AISuite/SNode.C evidence.

Establish the real native and browser workflows, thread/turn/prompt/tool state,
target/active/running/selected distinctions, controller/observer and reconnect
behavior, ownership boundaries, native/browser differences, install/release
scope, compatibility, privacy/exposure boundaries, and deterministic synthetic
states suitable for genuine screenshots.

Flag stale or unsupported Landingpages claims. Do not write or redesign the
README.

Save:
CodexUI/workflow/03-TECHNICAL-FACTS.md
```

## 3.4 — CodexUI — README + Visual Design

**System:** ChatGPT  
**Chat:** fork from `3.0`  
**Reasoning:** High

Design around:

- user experience before architecture terminology;
- actual native/browser workflow as centerpiece;
- one clear path from connection → select/create thread → prompt → observe work;
- screenshot-first proof rather than diagram-first explanation;
- native/browser differences stated only where they matter;
- architecture shown only to explain the visible workflow and boundaries;
- installation/first-run path that matches current package reality.

Likely visual inventory:

1. genuine native hero/workflow screenshot;
2. genuine browser screenshot or matched native/browser comparison when useful;
3. at most one compact state/reconnect/architecture figure if screenshots alone
   cannot explain a crucial distinction.

### Prompt

```text
Perform accelerated Step 4 for CodexUI.

Read the canonical inputs and CodexUI/workflow/03-TECHNICAL-FACTS.md.
Use SNode.C only as the quality/style reference.

Design the README and visual storyboard together around the real user workflow,
not protocol internals: connect, select/create a thread, submit a prompt, observe
turn/tool/background activity, and understand relevant state/reconnect behavior.

Make real native/browser screenshots the primary proof. Add a diagram only if it
explains a distinction the screenshots cannot.

Save:
CodexUI/workflow/04-README-DESIGN.md
CodexUI/workflow/05-VISUALS.md

Mark visual/screenshot semantics PENDING CODEX VALIDATION.
Do not write the full README.
```

## 3.5A — CodexUI — Visual Technical Validation

**System:** Codex  
**Session:** fresh  
**Reasoning:** High

Validate every visible state, target/active/running/selection relationship,
controller/observer status, reconnect implication, native/browser equality or
difference, and fixture/capture instruction. Update
`CodexUI/workflow/05-VISUALS.md` to `VALIDATED`.

## 3.5B — CodexUI — Figma + Capture Production

**System:** ChatGPT + Figma  
**Chat:** fork from `3.0`  
**Reasoning:** High

Capture real native/browser builds with the approved synthetic fixture. Use an
isolated display for native capture. Use Figma for approved composition/cropping
and any compact explanatory figure. Never reconstruct UI content in Figma.

## 3.6 — CodexUI — Frozen README Draft

**System:** ChatGPT  
**Chat:** fork from `3.0`  
**Reasoning:** High

Write the product story around what the user sees and does. Keep AISuite/backend
architecture subordinate. Route installation, compatibility, privacy/security,
and detailed behavior to deeper docs.

## 3.7A — CodexUI — Final Technical Audit

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh

## 3.7B — CodexUI — Final Editorial Audit

**System:** Claude  
**Session:** fresh  
**Reasoning:** High

Run in parallel against the same frozen candidate.

## 3.7C — CodexUI — Finalization + Publish

**System:** ChatGPT  
**Chat:** fork from `3.0`  
**Reasoning:** High

Finalize once, validate screenshots/assets/dependency closure, update
`CodexUI/README.md`, complete `07-FINAL-REVIEWS.md`, and commit/push when
requested.

---

# 14. Full project plan — SNode.C organization profile

**Project index:** `4`  
**Landingpages directory:** `SNode.C-orga/`  
**Eventual public destination:** `SNodeC/.github/profile/README.md`  
**Narrative center:** ecosystem/project navigation

Execute this **after MQTTSuite, AISuite, and CodexUI are publication-stable** so
its links and project summaries point at final product destinations.

Expected effort: **about 1.5–2.5 hours**.

## 4.0 — SNode.C Organization — Workflow Root

**System:** ChatGPT  
**Chat:** completely fresh

Use the Workflow Root bootstrap prompt with `<Project> = SNode.C-orga`.

## 4.3 — SNode.C Organization — Technical Truth

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh  
**Output:** `SNode.C-orga/workflow/03-TECHNICAL-FACTS.md`

Verify across final current product states:

- exact role of SNode.C, MQTTSuite, AISuite, CodexUI;
- dependency/relationship claims;
- no false all-product runtime pipeline;
- current public README/docs/demo/release routes;
- concise maturity/release wording only where established;
- two ecosystem paths without implying one distribution;
- organization-level support/discussion/contribution routes if they exist;
- independent-project/OpenAI notice for Codex-related projects;
- extensibility for future projects.

### Prompt

```text
Continue the canonical accelerated README workflow for the SNode.C organization
profile.

Read the canonical workflow/governance files, SNode.C-orga/AGENTS.md, and the
final publication artifacts for SNode.C, MQTTSuite, AISuite and CodexUI.

Perform Step 3 only.

Verify the organization-level project roles, real build/runtime relationships,
public destinations, demo routes, release/maturity wording and ecosystem
boundaries against the current product repositories.

Do not imply one all-product runtime pipeline or one shared-version distribution.
Keep the organization model extensible beyond the current four projects.

Save:
SNode.C-orga/workflow/03-TECHNICAL-FACTS.md
```

## 4.4 — SNode.C Organization — README + Visual Design

**System:** ChatGPT  
**Chat:** fork from `4.0`  
**Reasoning:** High

Design around:

- immediate ecosystem orientation;
- project selection by user need;
- concise project cards/entries in accessible Markdown;
- one or two demo/evaluation routes only when real;
- category structure that can accept a fifth project without redesign;
- visual navigation supporting, never replacing, text navigation.

Likely visual inventory:

- **zero or one** ecosystem/navigation figure by default;
- no screenshots unless they materially help project selection;
- no architecture diagram pretending all projects form one runtime stack.

### Prompt

```text
Perform accelerated Step 4 for the SNode.C organization profile.

Read the canonical inputs and
SNode.C-orga/workflow/03-TECHNICAL-FACTS.md.
Use the now-final product landing pages as destination and style references.

Design an extensible ecosystem navigator. A visitor should understand what each
project is for and choose the right repository without reading architecture
first.

Do not encode a permanent project count and do not imply one all-product runtime
pipeline. Use accessible Markdown as the primary navigation; any figure is
supporting only.

Save:
SNode.C-orga/workflow/04-README-DESIGN.md
SNode.C-orga/workflow/05-VISUALS.md

Mark any relationship arrows PENDING CODEX VALIDATION.
Do not write the full profile yet.
```

## 4.5A — SNode.C Organization — Visual Technical Validation

**System:** Codex  
**Session:** fresh  
**Reasoning:** High

If Step 4 chooses a visual, validate every project relation and demo route. If no
visual is needed, validate the navigation/project-routing plan and record that no
figure is required.

## 4.5B — SNode.C Organization — Figma Production

**System:** ChatGPT + Figma  
**Chat:** fork from `4.0`  
**Reasoning:** High

Only execute if an actual organization visual is approved. Otherwise this chat
records `No visual required` and proceeds.

## 4.6 — SNode.C Organization — Frozen README Draft

**System:** ChatGPT  
**Chat:** fork from `4.0`  
**Reasoning:** High

Write the organization front door, not another technical manual. Emphasize
project selection, concise evidence-aware summaries, demo routes, and stable
product links.

## 4.7A — SNode.C Organization — Final Technical Audit

**System:** Codex  
**Session:** fresh  
**Reasoning:** xhigh

## 4.7B — SNode.C Organization — Final Editorial Audit

**System:** Claude  
**Session:** fresh  
**Reasoning:** High

Run in parallel.

## 4.7C — SNode.C Organization — Finalization + Publish

**System:** ChatGPT  
**Chat:** fork from `4.0`  
**Reasoning:** High

Finalize, validate all project links/routes and extensibility, update
`SNode.C-orga/README.md`, complete the review artifact, and publish to the
organization destination when explicitly requested.

---

# 15. Standard prompts for Steps 5A, 6, 7A, 7B, 7C

The project-specific Step 3/4 prompts above define the narrative. Use these
standard prompts with the project path substituted.

## Step 5A — Visual validation prompt

```text
Read:
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md

Also inspect the current public source HEAD required by the project.

Validate every proposed figure and screenshot scenario against source/test/runtime
evidence. Check architecture relationships, ownership boundaries, runtime arrows,
protocol/version wording, commands, deterministic synthetic fixture data, visible
state, and what each visual actually proves.

Preserve the approved art direction. Correct only technical semantics and
reproduction details.

Update:
<Project>/workflow/05-VISUALS.md

Mark every final visual VALIDATED.
```

## Step 6 — Draft prompt

```text
Read:
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md

Write the complete professional <Project> README candidate using only verified
facts, approved structure, validated visuals and approved captures.

Treat it as a GitHub landing page: orient, differentiate, show proof, provide one
fast useful success path, expose important evidence boundaries, and route deeper
documentation.

Use SNode.C as a quality/style reference only. Prefer omission over completeness.
Remove workflow/governance language from reader-facing prose.

Save the frozen candidate to:
<Project>/workflow/06-README-DRAFT.md

Do not overwrite <Project>/README.md yet.
```

## Step 7A — Codex technical audit prompt

```text
Read the complete canonical workflow artifacts for <Project>, especially:
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/05-VISUALS.md
<Project>/workflow/06-README-DRAFT.md

Perform a strict technical audit against current relevant public source HEADs.

Report only incorrect, unsupported, stale or misleading claims, broken commands,
incorrect visual semantics, over-broad evidence boundaries, or release/package/
platform statements that are not established.

Do not rewrite for style.

Write findings under:
# Codex technical audit

in:
<Project>/workflow/07-FINAL-REVIEWS.md
```

## Step 7B — Claude editorial audit prompt

```text
Read the canonical workflow/design artifacts and the frozen README candidate for
<Project>.

Review it as the landing page of a serious professional open-source project.
Identify generic/AI-sounding prose, weak hierarchy, unnecessary qualification or
process language, repetition, poor visual/text rhythm, missing high-value
product/API demonstration, avoidable first-success friction, weak calls to
action, and material that belongs in deeper documentation.

Be aggressive about shortening/removal, but do not expand the README and do not
override technical truth.

Write findings under:
# Claude editorial audit

in:
<Project>/workflow/07-FINAL-REVIEWS.md
```

## Step 7C — Finalization prompt

```text
Read all canonical workflow artifacts for <Project>, including both independent
audits in <Project>/workflow/07-FINAL-REVIEWS.md.

Apply accepted findings in one controlled finalization pass.
Technical corrections from Codex take precedence.
Do not reopen the approved reader journey unless a finding is a real blocker.
Prefer removing verbosity over adding material. Preserve evidence boundaries and
validated visuals.

Write the final result to:
<Project>/README.md

Complete <Project>/workflow/07-FINAL-REVIEWS.md with:
# Accepted changes
# Rejected findings and reasons
# Validation
# Final status

Then validate the complete publication dependency closure and, when explicitly
requested, commit and push the final package.
```

---

# 16. Publication validation — one gate, not another design phase

Before commit/push validate the complete dependency closure:

- Markdown structure and code fences;
- all relative links and heading anchors;
- all external publication routes;
- asset existence and matching filenames;
- responsive `<picture>` paths;
- figure accessibility title/description/alt/caption;
- Figma/source counterpart provenance;
- screenshot/capture provenance and privacy;
- source/evidence alignment;
- README commands from the exact qualified context;
- image-disabled readability;
- mobile readability and fallback-font clearance;
- `git diff --check` and repository-native checks when a native checkout is
  available;
- exact starting/ending SHAs when committing/pushing.

A validation correction does not become a new numbered workflow step unless it
requires a new substantive design/evidence decision.

---

# 17. Re-review trigger rules

Do **not** automatically create another review cycle after Step 7.

Re-review only if one of these occurs:

1. a technical blocker remains;
2. a new material technical claim is added;
3. a visual's technical semantics change materially;
4. the README reader journey is structurally rewritten;
5. source HEAD moves in a way relevant to published claims/commands;
6. final publication validation exposes a substantive inconsistency.

Ordinary typo, spacing, caption, link, provenance, or small copy corrections do
not reopen the workflow.

When source HEAD moves late:

```text
old verified HEAD
        ↓ compare
new HEAD
        ↓
only relevant implementation/tests/examples changed?
        ├─ no  → preserve evidence boundary; update pin
        └─ yes → targeted revalidation of affected claims only
```

Never restart the whole workflow solely because `master` advanced.

---

# 18. Expected cadence and total effort

Approximate human/AI workflow effort after the SNode.C foundation:

| Presentation | Expected effort |
| --- | ---: |
| MQTTSuite | **2–3 h** |
| AISuite | **2–3.5 h** |
| CodexUI | **3–4.5 h** |
| SNode.C organization profile | **1.5–2.5 h** |

Typical per-product cadence:

```text
Step 3 facts                  30–60 min
Step 4 design + storyboard    15–30 min
Step 5 validation/production  30–90 min
Step 6 draft                  20–30 min
Step 7 reviews/finalization   30–60 min
```

CodexUI is expected to be slower because genuine native/browser screenshots and
state correctness require more care. The organization profile should be lighter
because it consumes the already-final product destinations rather than proving a
new runtime system.

---

# 19. Definition of done

A project is complete when:

```text
03 facts are current and evidence-scoped
04 reader journey is fixed
05 visuals are validated and human-approved
06 frozen draft exists
07 Codex + Claude reviews are resolved
README.md is final
assets and assets/src are complete
publication validation passes
requested commit/push is complete
```

Then **stop**.

Do not manufacture additional review stages merely because SNode.C accumulated
extra numbered closure artifacts while this workflow was being invented.
