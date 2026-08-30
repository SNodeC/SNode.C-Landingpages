# Canonical AI-assisted README workflow

This document defines the canonical handoff and publication workflow for the
SNode.C ecosystem landing pages.

SNode.C itself established the quality bar, evidence discipline, visual language,
Figma workflow, responsive-figure rules, and publication/closure pattern. The
remaining product repositories should reuse that foundation rather than repeat
SNode.C's exploratory work.

The current accelerated order is:

1. **MQTTSuite**
2. **AISuite**
3. **CodexUI**
4. **SNode.C organization profile** after the product destinations are stable

Reuse the **design language and quality standard**, not the literal SNode.C
section order or visual composition.

---

## Canonical handoff rule

**No AI step may depend on previous chat history. Every step must read its
specified repository artifacts and save its complete result to the specified
repository artifact.**

A conversation may provide convenience and continuity, but repository Markdown
is the handoff source of truth. If chat memory and a repository artifact differ,
the repository artifact wins.

The standard per-project artifact set remains:

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

# AI roles and reasoning policy

Use the role best suited to the decision rather than one AI for everything.

| Task | AI | Model policy | Reasoning |
| --- | --- | --- | --- |
| Repository audit / inventory | Codex | strongest current Codex model | High |
| Ecosystem/editorial positioning | ChatGPT | GPT-5.6 Sol or current successor | High |
| Technical truth / source verification | Codex | strongest current Codex model | **xhigh** by default |
| README structure / visual art direction / final copy | ChatGPT | GPT-5.6 Sol or current successor | High |
| Visual semantics / commands / reproducibility validation | Codex | strongest current Codex model | High |
| Final technical audit | Codex | strongest current Codex model | **xhigh** |
| Final editorial audit | Claude | strongest available Opus-class model | High |

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

# Global foundation — Steps 1 and 2

Steps 1 and 2 are **one-time ecosystem work**. They already exist and should not
be repeated for every repository.

## Step 1 — Repository audit

**AI:** Codex  
**Reasoning:** High  
**Artifact:** `workflow/01-REPOSITORY-AUDIT.md`

Purpose: distinguish durable evidence/research from presentation material that
should be rebuilt.

Do not rerun Step 1 unless the Landingpages repository changes so fundamentally
that the preserved/rebuild classification is no longer useful.

## Step 2 — Ecosystem positioning

**AI:** ChatGPT  
**Reasoning:** High  
**Artifact:** `workflow/02-ECOSYSTEM-POSITIONING.md`

Purpose: establish the common ecosystem story, terminology, project roles,
audiences, and boundaries once.

Do not rerun Step 2 merely because a product README changes. Update it only when
the ecosystem relationship itself materially changes.

---

# Per-project workflow

For each remaining repository, execute Step 3 rigorously and Steps 4–7 in the
accelerated production loop below.

The practical target is **one technical-facts pass, one design/visual pass, one
visual-validation gate, one draft, one parallel final review, and one finalization
pass**.

---

# Step 3 — Verify technical truth

**AI:** Codex  
**Reasoning:** xhigh  
**Output:** `<Project>/workflow/03-TECHNICAL-FACTS.md`

This remains the non-negotiable deep step. Speed must come from presentation
reuse, not from weakening technical verification.

## Read first

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

## Verify only README-relevant facts

Establish:

- fundamental purpose and audience;
- actual architecture/programming model;
- current applications/components;
- important protocols/transports/integrations;
- installation/build/package surface;
- first-success path;
- important configuration/runtime behavior;
- genuine differentiators;
- ecosystem relationships;
- evidence boundaries and limitations;
- release/version/platform/package status relevant to public claims.

Do not turn Step 3 into a complete source-code audit. Verify enough to make the
landing page correct.

## Prompt template

```text
Continue the canonical README workflow for <Project>.

Read and follow:
- AGENTS.md
- workflow/README-GOVERNANCE.md
- workflow/README-WORKFLOW.md
- workflow/01-REPOSITORY-AUDIT.md
- workflow/02-ECOSYSTEM-POSITIONING.md
- <Project>/AGENTS.md

Perform Step 3 only.

Verify all material README-relevant facts against the current public source
repository HEAD. Use existing Landingpages material as research, not as proof.

Establish purpose, architecture/programming model, important capabilities,
first-success path, dependencies/package surface, limitations, release/platform
scope, ecosystem relationships and genuine differentiators.

Flag stale or unsupported existing claims. Preserve explicit evidence boundaries.
Do not write or redesign the README.

Save the complete self-contained result to:
<Project>/workflow/03-TECHNICAL-FACTS.md
```

### Stop condition

Step 3 is complete when a later writer can produce the README without reopening
the source repository for ordinary claims. Unresolved facts may remain, but they
must be explicitly marked as unresolved or excluded.

---

# Accelerated Steps 4–7

The original SNode.C workflow separated every design, visual, drafting, review,
and closure activity while the publication system was being invented. That is
no longer necessary.

For MQTTSuite, AISuite and CodexUI, use the following operational compression.

---

# Step 4 — Design the README and visual storyboard in one pass

**AI:** ChatGPT  
**Reasoning:** High  
**Outputs:**

```text
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md   # initial design/art-direction section
```

This replaces separate exploratory README-design and visual-art-direction chats.
The story and visuals should be designed together.

## Read first

```text
workflow/01-REPOSITORY-AUDIT.md
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/AGENTS.md
SNode.C/README.md                  # quality/style reference only
SNode.C/workflow/09-FIGMA-RESPONSIVE-FIGURES.md
```

SNode.C is a **quality and design-language reference**, not a template to copy.

## Decide in this one pass

`04-README-DESIGN.md` should fix:

- headline and one-sentence value proposition;
- primary audience;
- reader journey and section order;
- centerpiece;
- quickest useful first success;
- which proof belongs in README versus deeper docs;
- calls to action / next-step routing;
- intended visual/text rhythm.

At the same time, initialize `05-VISUALS.md` with only the visuals that materially
help the reader. For each visual state:

- one idea it communicates;
- desktop/mobile need;
- content and labels;
- technical relationships/arrows;
- source/capture requirement;
- intended asset name;
- what is deliberately omitted.

Do not create decorative quota-filling visuals.

## Product centerpieces

```text
MQTTSuite
→ the five applications and real MQTT/message flow

AISuite
→ typed integration plus provider/bridge/client authority boundaries

CodexUI
→ actual native/browser user workflow and visible product state

SNode.C organization
→ ecosystem/project navigation, not another product architecture page
```

## Prompt template

```text
Read the canonical workflow inputs and <Project>/workflow/03-TECHNICAL-FACTS.md.

Perform the accelerated Step 4 for <Project>.

In one pass:
1. define the README structure and reader journey;
2. define the small visual storyboard that supports that journey.

Use SNode.C only as the established quality/style reference. Do not copy its
section structure mechanically.

Save the complete README design to:
<Project>/workflow/04-README-DESIGN.md

Create/update the initial visual plan in:
<Project>/workflow/05-VISUALS.md

Mark technical visual semantics and runtime arrows PENDING CODEX VALIDATION.
Do not write the full README yet.
```

### Speed rule

Do not conduct a separate general “visual ideas” review after Step 4. If the
storyboard communicates the approved centerpiece clearly, proceed directly to
Step 5.

---

# Step 5 — Validate once, then produce the visuals

**AI:** Codex for technical validation; ChatGPT/Figma for figure execution; real
application capture for screenshots  
**Reasoning:** Codex High  
**Output:** `<Project>/workflow/05-VISUALS.md` plus actual assets

This is one validation gate, not a design cycle.

## 5a — Codex validates the complete storyboard once

Read:

```text
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md
current public source HEAD
```

Validate:

- every component and ownership boundary;
- every dependency/runtime arrow;
- protocol/version wording;
- commands and screenshot states;
- deterministic fixture/synthetic data;
- what a screenshot actually proves;
- filenames and required responsive variants.

Update `05-VISUALS.md` in place with corrections and `VALIDATED` status.

### Codex prompt

```text
Validate <Project>/workflow/05-VISUALS.md against current public source HEAD.

Check every architecture relationship, dependency/runtime arrow, protocol claim,
command and screenshot state. Define deterministic reproduction steps for real
screenshots using synthetic data.

Preserve the approved visual design intent. Correct only technical semantics and
reproduction details.

Update <Project>/workflow/05-VISUALS.md and mark each final visual VALIDATED.
```

## 5b — Produce the actual assets immediately

After Codex validation, do not open another abstract visual-design phase.

### Designed diagrams / explanatory figures

- create and edit them in **Figma**;
- Figma is the editable visual source of truth;
- keep publication exports under `<Project>/assets/`;
- keep repository source/export counterparts under `<Project>/assets/src/`;
- use responsive desktop/mobile compositions only where the content needs art
  direction at GitHub mobile width;
- do not hand-edit publication SVG geometry after Figma export;
- verify light/dark/mobile rendering and text clearance.

### Product screenshots

- capture real source-aligned builds only;
- use deterministic synthetic data;
- never capture the maintainer's live/private desktop or account state;
- record reproduction commands/fixtures under `assets/src/` or `05-VISUALS.md`;
- use Figma only for approved composition/cropping/annotation, never to fake
  application functionality.

### Human gate

The maintainer performs one visual check and records:

```text
Human approval: APPROVED
```

A rejected visual is corrected locally; rejection does **not** reopen README
structure unless the centerpiece itself was wrong.

---

# Step 6 — Write one frozen candidate

**AI:** ChatGPT  
**Reasoning:** High  
**Output:** `<Project>/workflow/06-README-DRAFT.md`

Write the complete candidate once the validated/approved assets exist.

## Read first

```text
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md
```

## Rules

- treat the README as a landing page, not a qualification report;
- orient → differentiate → show proof → first success → fit-check → route deeper;
- prefer omission over completeness;
- use the established SNode.C prose discipline: concrete, calm, precise;
- do not repeat evidence caveats in every section;
- do not add claims merely to fill space;
- make the best/highest-level project API or user surface visible where that is
  central to evaluation;
- keep deeper technical matrices and exhaustive options in linked docs.

## Prompt template

```text
Using the verified facts, approved README design and validated visuals, write the
complete professional <Project> README.

Use SNode.C as the quality/style reference only.

The README must orient a first-time technical evaluator, explain the project's
specific differentiator, show credible proof, provide one fast useful success
path, expose important evidence boundaries, and route deeper documentation.

Prefer omission over completeness and remove workflow/governance vocabulary from
reader-facing prose.

Save the frozen candidate to:
<Project>/workflow/06-README-DRAFT.md

Do not overwrite <Project>/README.md yet.
```

### Speed rule

Do not ask ChatGPT to self-review the draft in a separate stage. Freeze it and
send it directly to the two independent Step 7 reviewers.

---

# Step 7 — Parallel reviews, one controlled finalization, then publish

This is the largest operational compression.

The technical and editorial reviews should run **in parallel against the same
frozen Step 6 candidate**. They are independent reviews, not sequential rewrite
cycles.

All findings go into:

```text
<Project>/workflow/07-FINAL-REVIEWS.md
```

Use sections:

```text
# Codex technical audit
# Claude editorial audit
# Accepted changes
# Rejected findings and reasons
# Validation
# Final status
```

## 7a — Technical audit

**AI:** Codex  
**Reasoning:** xhigh

Review only technical correctness and reproducibility:

- wrong/unsupported/stale claims;
- commands that no longer work;
- incorrect visual semantics;
- evidence boundaries that are too broad;
- release/package/platform claims not established by evidence.

Do not rewrite for style.

## 7b — Editorial audit

**AI:** Claude  
**Reasoning:** High

Review only publication quality:

- generic or AI-sounding prose;
- weak hierarchy;
- unnecessary qualification/process language;
- duplication and verbosity;
- weak visual/text rhythm;
- missing high-value API/product demonstration;
- poor first-success friction;
- weak calls to action or ending.

Claude may read Codex's findings for awareness but must not override technical
truth.

## 7c — Finalize once

**AI:** ChatGPT  
**Reasoning:** High

Read all project workflow artifacts plus both audits. Apply accepted findings in
one controlled edit.

Technical corrections from Codex take precedence. Preserve the approved reader
journey and visual hierarchy unless a reviewer found an actual blocker.

Write:

```text
<Project>/README.md
```

and complete `07-FINAL-REVIEWS.md` with accepted/rejected findings, validation,
and final status.

### Finalization prompt

```text
Read all canonical workflow artifacts for <Project>, including the Codex and
Claude audits in <Project>/workflow/07-FINAL-REVIEWS.md.

Apply the accepted findings in one controlled finalization pass.

Technical corrections from Codex take precedence. Do not reopen the approved
structure unless a finding is a real blocker. Prefer removing verbosity over
adding explanation. Preserve evidence boundaries and validated visuals.

Write the final README to:
<Project>/README.md

Update <Project>/workflow/07-FINAL-REVIEWS.md with:
- Accepted changes
- Rejected findings and reasons
- Validation
- Final status

Then perform repository-native publication validation and, when explicitly
requested, commit and push the complete package.
```

---

# Publication validation — one gate, not another design phase

Before committing/pushing, validate the complete dependency closure once.

At minimum check:

- current Landingpages `main` baseline before writing;
- current relevant public source HEAD(s);
- `git diff --check` when a native checkout is available;
- Markdown links and heading anchors;
- every referenced local asset exists;
- public figure/source counterparts are synchronized;
- Figma/source-of-truth provenance is current for designed figures;
- responsive/mobile assets render legibly;
- real screenshots match recorded reproduction state;
- commands are aligned with the reviewed source revision;
- no private paths, credentials or live-user data;
- no unsupported release/platform/security/performance claims;
- no workflow-only links or draft paths in the public dependency closure.

Record validation in `07-FINAL-REVIEWS.md`. Do not create a new numbered
workflow stage merely to record routine closure.

If a networked native checkout is unavailable, state that limitation explicitly
instead of claiming local checks that were not run.

---

# Moving-HEAD rule

A source or Landingpages branch moving during the workflow does **not** trigger a
full restart.

If the public source HEAD changes:

1. compare old and new source revisions;
2. identify whether changed paths affect public claims, commands or visuals;
3. revalidate only affected claims;
4. update the Step 3 evidence baseline and downstream wording only where needed.

If Landingpages `main` changes while preparing the final commit:

1. stop before pushing;
2. preserve the concurrent change;
3. rebase/rebuild the candidate on current `main`;
4. compare the resulting one-commit diff;
5. fast-forward only; never force-push over unrelated work.

This rule exists specifically to avoid repeating an entire publication workflow
for a small concurrent change.

---

# Remaining project emphasis

## MQTTSuite

Primary story:

```text
five focused MQTT applications
→ broker / transform / bridge / CLI / store
→ real MQTT message flow
```

Likely highest-value evidence:

- short broker/subscriber/publisher first success;
- one clear application/message-flow figure;
- one genuine Web UI/product screenshot if it materially helps evaluation.

Do not turn the README into five application manuals.

## AISuite

Primary story:

```text
typed C++ / TypeScript integration
→ one bounded bridge
→ provider/controller/observer authority
```

Likely highest-value evidence:

- typed API example;
- bridge/authority figure;
- one deterministic bridge/client success path.

Do not let CodexUI presentation behavior dominate AISuite.

## CodexUI

Primary story:

```text
real native/browser workflow
→ threads / turns / prompt / activity / reconnect state
```

Likely highest-value evidence:

- genuine native/browser product captures;
- shared user-workflow explanation;
- architecture only where needed to explain visible behavior/boundaries.

Do not lead with reducer/protocol/internal implementation terminology.

---

# Expected operational cadence per remaining repository

The accelerated workflow should normally require:

```text
1. Codex xhigh    → Step 3 technical facts
2. ChatGPT High   → Step 4 README + visual storyboard
3. Codex High     → Step 5 validation
4. Figma/capture  → actual visuals + one human approval
5. ChatGPT High   → Step 6 frozen draft
6. Codex xhigh + Claude High in parallel → Step 7 reviews
7. ChatGPT High   → Step 7 finalization + validation + requested push
```

The same ChatGPT conversation may continue from Step 4 through Step 6 and later
Step 7c, because the repository artifacts—not conversation history—carry the
canonical state.

The goal is not to reduce quality. The goal is to remove repeated exploratory
loops now that SNode.C has already established the system.

---

# Stop rule

After Step 7 finalization and publication validation, **stop**.

Do not automatically request another Codex/Claude review cycle. Reopen review
only when one of these is true:

- a technical blocker remains;
- a new material claim was introduced after review;
- a visual's technical semantics changed after validation;
- the README structure was materially changed after the frozen draft;
- the public source moved in a way that affects published claims.

Polish findings that do not materially improve first-time-reader understanding,
technical correctness, credibility, accessibility or actionability are not a
reason for another cycle.

This is the canonical accelerated workflow for the remaining SNode.C ecosystem
landing pages.