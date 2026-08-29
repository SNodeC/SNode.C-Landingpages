# Canonical AI-assisted README workflow

This document defines the canonical handoff workflow for redesigning the GitHub
landing pages for the SNode.C organization and the SNode.C, MQTTSuite, AISuite,
and CodexUI repositories.

The existing `SNode.C-Landingpages` repository is the starting point and remains
the working repository. Existing facts, evidence, qualification results,
commands, screenshots, figures, and drafts are research inputs; they are not
automatically approved final presentation material.

## Canonical handoff rule

**No AI step may rely on previous chat history. Every step must read its declared
Markdown inputs from this repository and save its complete result to the declared
output Markdown file.**

This makes the workflow reproducible and allows ChatGPT, Codex, and Claude to
hand work to one another without depending on conversation context.

The first two steps are global. Steps 3–7 are repeated for each presentation in
this order:

1. SNode.C
2. MQTTSuite
3. AISuite
4. CodexUI
5. SNode.C organization profile

Finish SNode.C completely first. It establishes the quality bar and visual
language for the remaining pages; reuse the design language and workflow, not an
identical README template.

Recommended workflow artifact layout:

```text
SNode.C-Landingpages/
├── workflow/
│   ├── 01-REPOSITORY-AUDIT.md
│   ├── 02-ECOSYSTEM-POSITIONING.md
│   └── README-WORKFLOW.md
├── SNode.C/
│   ├── workflow/
│   │   ├── 03-TECHNICAL-FACTS.md
│   │   ├── 04-README-DESIGN.md
│   │   ├── 05-VISUALS.md
│   │   ├── 06-README-DRAFT.md
│   │   └── 07-FINAL-REVIEWS.md
│   ├── README.md
│   └── assets/
├── MQTTSuite/
│   └── workflow/...
├── AISuite/
│   └── workflow/...
├── CodexUI/
│   └── workflow/...
└── SNode.C-orga/
    └── workflow/...
```

---

# 1. Preserve the current Landingpages repository as research material

**AI:** Codex  
**Reasoning:** High  
**Purpose:** Decide what existing work is valuable and what is disposable. Do
not rewrite the landing pages yet.

## Read before starting

```text
Entire SNode.C-Landingpages repository
```

## Save result to

```text
workflow/01-REPOSITORY-AUDIT.md
```

This file becomes an authoritative input for all later steps.

## Prompt

```text
Inspect the complete current SNode.C-Landingpages repository.

We are restarting the README design, but we do not want to lose useful work.
Identify what should be:
- preserved as verified research,
- preserved but simplified,
- replaced,
- or removed.

Focus especially on FACTS/EVIDENCE, qualification results, commands,
screenshots, figures and existing README content.

Save the complete result to:
workflow/01-REPOSITORY-AUDIT.md

Do not modify the READMEs or assets yet.
```

---

# 2. Define the ecosystem story once

**AI:** ChatGPT  
**Reasoning:** High  
**Purpose:** Establish the common editorial foundation for all five pages.

## Read before starting

```text
workflow/01-REPOSITORY-AUDIT.md

and the existing relevant files in:
SNode.C-Landingpages/
```

## Save result to

```text
workflow/02-ECOSYSTEM-POSITIONING.md
```

Every subsequent README-design step must read this file.

## Prompt

```text
Read:
workflow/01-REPOSITORY-AUDIT.md

Using the current SNode.C-Landingpages repository as supporting research,
define the editorial positioning of the SNode.C ecosystem.

Cover:
- what SNode.C fundamentally is,
- why the ecosystem exists,
- who it is for,
- what makes it technically interesting,
- and how SNode.C, MQTTSuite, AISuite and CodexUI relate.

Avoid generic open-source marketing language.
Do not write the individual READMEs yet.

Save the result to:
workflow/02-ECOSYSTEM-POSITIONING.md
```

This is the only global strategy step required before working product by product.

---

# Repeat steps 3–7 for each project

Recommended order:

```text
SNode.C
MQTTSuite
AISuite
CodexUI
SNode.C-orga
```

Finish SNode.C completely before proceeding to the other pages.

---

# 3. Verify the project's technical facts

**AI:** Codex  
**Reasoning:** Max / xhigh  
**Purpose:** Establish technical truth from the actual repository HEAD.

The example below uses SNode.C. Substitute the corresponding project and source
repository for MQTTSuite, AISuite, and CodexUI. For the organization profile,
verify its ecosystem claims against all relevant repositories.

## Read before starting

```text
workflow/01-REPOSITORY-AUDIT.md
workflow/02-ECOSYSTEM-POSITIONING.md

SNode.C/ existing material in SNode.C-Landingpages

Current HEAD of:
SNodeC/snode.c
```

## Save result to

```text
SNode.C/workflow/03-TECHNICAL-FACTS.md
```

Use the corresponding presentation directory for the other pages.

## Prompt

```text
Read first:
workflow/01-REPOSITORY-AUDIT.md
workflow/02-ECOSYSTEM-POSITIONING.md

We are redesigning the GitHub README for SNode.C.

Use the existing SNode.C-Landingpages/SNode.C material as research,
but verify all important information against the current SNode.C repository HEAD.

Summarize only facts relevant to a professional README:
purpose, architecture, programming model, important capabilities,
protocols/transports, dependencies, examples, limitations,
ecosystem relationships and genuine differentiators.

Flag unsupported or outdated claims in the current landing-page draft.

Do not write the new README yet.

Save the complete verified result to:
SNode.C/workflow/03-TECHNICAL-FACTS.md
```

This is one of the stages where the highest reasoning budget is justified.

---

# 4. Design the README and its visuals together

**AI:** ChatGPT  
**Reasoning:** High  
**Purpose:** Decide the story before generating prose or graphics.

## Read before starting

```text
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
workflow/01-REPOSITORY-AUDIT.md
```

Also inspect the existing README and assets, but treat them as drafts rather than
constraints on the new presentation.

## Save result to

```text
<Project>/workflow/04-README-DESIGN.md
```

The document should contain at least:

```text
headline
value proposition
audience
reader journey
section order
main centerpiece
quick-start concept
visual inventory
content to move out of README
calls to action
```

## Prompt

```text
Read first:
workflow/02-ECOSYSTEM-POSITIONING.md
SNode.C/workflow/03-TECHNICAL-FACTS.md
workflow/01-REPOSITORY-AUDIT.md

Using those verified facts and the common SNode.C ecosystem positioning,
design the new SNode.C GitHub README.

Define:
- headline and one-sentence value proposition,
- reader journey and section order,
- the main technical centerpiece,
- the quickest useful first-success example,
- 2–3 meaningful visuals,
- and what detailed material should be linked out instead.

This must be a GitHub landing page, not a technical manual.
Do not write the complete README yet.

Save the complete result to:
SNode.C/workflow/04-README-DESIGN.md
```

Use these product-specific centerpieces:

```text
SNode.C
→ programming model

MQTTSuite
→ MQTT applications and message flows

AISuite
→ typed AI middleware / bridge architecture

CodexUI
→ actual user workflow and UI

SNode.C organization
→ ecosystem navigation
```

---

# 5. Create the diagrams and real screenshot scenarios

This step deliberately involves two AI systems, but all results go into one
Markdown handoff document.

## Output file

```text
<Project>/workflow/05-VISUALS.md
```

It should eventually contain entries such as:

```text
Visual 1
- purpose
- design
- approved technical semantics
- implementation notes
- asset filename

Visual 2
...

Screenshot 1
- intended state
- reproduction commands
- fixture/test data
- capture requirements
- asset filename
```

## 5a. Visual design

**AI:** ChatGPT  
**Reasoning:** High

### Read before starting

```text
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
```

### Prompt

```text
Read first:
workflow/02-ECOSYSTEM-POSITIONING.md
SNode.C/workflow/03-TECHNICAL-FACTS.md
SNode.C/workflow/04-README-DESIGN.md

Design the visual concepts required by the approved SNode.C README structure.

For each proposed figure or screenshot specify:
- the single idea it should communicate,
- visual hierarchy and composition,
- components and labels,
- arrows/data flows where relevant,
- what information should deliberately be omitted,
- and what the reader should understand within about five seconds.

Avoid generic boxes-and-arrows diagrams and decorative imagery.
Aim for calm, modern, professional technical graphics.

Create:
SNode.C/workflow/05-VISUALS.md

Mark all technical relationships as PENDING CODEX VALIDATION.
```

## 5b. Technical validation and screenshot reproduction

**AI:** Codex  
**Reasoning:** High

### Read before starting

```text
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md
```

Also inspect the actual current source repository HEAD.

### Prompt

```text
Read first:
SNode.C/workflow/03-TECHNICAL-FACTS.md
SNode.C/workflow/04-README-DESIGN.md
SNode.C/workflow/05-VISUALS.md

Review every proposed SNode.C figure and screenshot scenario
against the current source repository HEAD.

Verify every architecture component, dependency, ownership boundary,
protocol relationship and runtime arrow.

For screenshots, define a deterministic real application scenario
using synthetic data and current functionality.
Do not fake functionality for presentation purposes.

Update:
SNode.C/workflow/05-VISUALS.md

Preserve the visual design intent but add technical corrections,
reproduction instructions and a final VALIDATED status for each visual.
```

After the AI work, visually inspect the final figures/screenshots and add a human
approval field before proceeding:

```text
Human approval: APPROVED
```

---

# 6. Write the complete README

**AI:** ChatGPT  
**Reasoning:** High  
**Purpose:** Turn approved facts, story, and visuals into the public-facing page.

## Read before starting

```text
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md
```

The visuals referenced in `05-VISUALS.md` should already exist under:

```text
<Project>/assets/
```

## Save working result to

```text
<Project>/workflow/06-README-DRAFT.md
```

Do not overwrite `README.md` immediately. The final review must operate on one
frozen candidate.

## Prompt

```text
Read first:
workflow/02-ECOSYSTEM-POSITIONING.md
SNode.C/workflow/03-TECHNICAL-FACTS.md
SNode.C/workflow/04-README-DESIGN.md
SNode.C/workflow/05-VISUALS.md

Now write the complete professional SNode.C README.

Use only the verified technical facts, approved ecosystem positioning,
approved README design and validated visual assets.

Treat README.md as a GitHub landing page:
orient the reader, explain the differentiator, show proof,
provide a fast useful entry point, then link to deeper documentation.

Prefer omission over completeness.
Do not reproduce qualification bookkeeping, exhaustive dependency details,
or implementation trivia unless essential.
Never invent technical claims.

Save the complete candidate README to:
SNode.C/workflow/06-README-DRAFT.md

Do not overwrite SNode.C/README.md yet.
```

---

# 7. Run one technical review and one editorial review

All review findings go into:

```text
<Project>/workflow/07-FINAL-REVIEWS.md
```

Use clearly separated sections:

```text
# Codex technical audit

...

# Claude editorial audit

...

# Accepted changes

...

# Rejected findings and reasons

...

# Final status

...
```

## 7a. Technical review

**AI:** Codex  
**Reasoning:** Max / xhigh

### Read before starting

```text
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md
<Project>/workflow/06-README-DRAFT.md
```

Also inspect the actual current source repository HEAD.

### Prompt

```text
Read first:
SNode.C/workflow/03-TECHNICAL-FACTS.md
SNode.C/workflow/04-README-DESIGN.md
SNode.C/workflow/05-VISUALS.md
SNode.C/workflow/06-README-DRAFT.md

Perform a strict technical audit of the README draft
against the current SNode.C repository HEAD.

Check every factual statement, architecture relationship,
example, command, capability, dependency and limitation.

Report only:
- incorrect claims,
- unsupported claims,
- stale information,
- misleading wording,
- broken commands,
- or important technical limitations that must be stated.

Do not rewrite the README for style.

Create or update:
SNode.C/workflow/07-FINAL-REVIEWS.md

Write your findings under:
# Codex technical audit
```

## 7b. Editorial review

**AI:** Claude  
**Reasoning:** High

### Read before starting

```text
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/06-README-DRAFT.md
<Project>/workflow/07-FINAL-REVIEWS.md
```

Claude should see the technical findings but should not reinterpret technical
truth.

### Prompt

```text
Read first:
workflow/02-ECOSYSTEM-POSITIONING.md
SNode.C/workflow/04-README-DESIGN.md
SNode.C/workflow/06-README-DRAFT.md
SNode.C/workflow/07-FINAL-REVIEWS.md

Review the README draft as the landing page of a serious professional
open-source C++ project.

Identify:
- generic AI-generated wording,
- boring or overlong passages,
- weak hierarchy,
- unnecessary qualification,
- repetition,
- poor visual/text balance,
- weak calls to action,
- and material that belongs in deeper documentation instead.

Be aggressive about what should be shortened or removed.
Do not expand the README and do not override Codex's technical findings.

Append your findings to:
SNode.C/workflow/07-FINAL-REVIEWS.md

under:
# Claude editorial audit
```

## 7c. Final controlled rewrite

This remains part of Step 7 rather than becoming another workflow stage.

**AI:** ChatGPT  
**Reasoning:** High

### Read before starting

```text
workflow/02-ECOSYSTEM-POSITIONING.md
<Project>/workflow/03-TECHNICAL-FACTS.md
<Project>/workflow/04-README-DESIGN.md
<Project>/workflow/05-VISUALS.md
<Project>/workflow/06-README-DRAFT.md
<Project>/workflow/07-FINAL-REVIEWS.md
```

### Output

```text
<Project>/README.md
```

Also update `<Project>/workflow/07-FINAL-REVIEWS.md` with accepted/rejected
findings and completion status.

### Prompt

```text
Read all workflow artifacts:
workflow/02-ECOSYSTEM-POSITIONING.md
SNode.C/workflow/03-TECHNICAL-FACTS.md
SNode.C/workflow/04-README-DESIGN.md
SNode.C/workflow/05-VISUALS.md
SNode.C/workflow/06-README-DRAFT.md
SNode.C/workflow/07-FINAL-REVIEWS.md

Apply the accepted findings from the Codex technical audit
and Claude editorial review.

Technical corrections from Codex take precedence.
Preserve the approved structure and visual hierarchy.
Remove verbosity rather than adding material.
Do not reintroduce qualification detail that was deliberately moved out.

Write the final result to:
SNode.C/README.md

Also update:
SNode.C/workflow/07-FINAL-REVIEWS.md

with:
# Accepted changes
# Rejected findings and reasons
# Final status
```

---

# Complete handoff pipeline

```text
                         EXISTING REPOSITORY
                                │
                                ▼
                     CODEX / HIGH
             01-REPOSITORY-AUDIT.md
                                │
                                ▼
                    CHATGPT / HIGH
           02-ECOSYSTEM-POSITIONING.md
                                │
              ┌─────────────────┴─────────────────┐
              │          per project              │
              ▼                                   │
          CODEX / MAX                             │
     03-TECHNICAL-FACTS.md                        │
              │                                   │
              ▼                                   │
        CHATGPT / HIGH                            │
      04-README-DESIGN.md                         │
              │                                   │
              ▼                                   │
        CHATGPT / HIGH                            │
          visual design                           │
              │                                   │
        CODEX / HIGH                              │
     technical validation                         │
              │                                   │
              ▼                                   │
         05-VISUALS.md                            │
              │                                   │
        HUMAN APPROVAL                            │
              │                                   │
              ▼                                   │
        CHATGPT / HIGH                            │
     06-README-DRAFT.md                           │
              │                                   │
       ┌──────┴──────┐                            │
       ▼             ▼                            │
 CODEX / MAX      CLAUDE / HIGH                   │
 technical           editorial                    │
       └──────┬──────┘                            │
              ▼                                   │
     07-FINAL-REVIEWS.md                          │
              │                                   │
              ▼                                   │
        CHATGPT / HIGH                            │
          final edit                              │
              │                                   │
              ▼                                   │
           README.md                              │
              └───────────────────────────────────┘
```

## Responsibility split

- **Codex:** repository understanding, source verification, technical claim
  validation, architecture checks, reproducible commands and screenshot states.
- **ChatGPT:** ecosystem positioning, editorial structure, visual art direction,
  README storytelling, cross-project consistency, and final controlled editing.
- **Claude:** independent editorial attack on the near-final README, especially
  verbosity, generic AI prose, hierarchy, and unnecessary material.
- **Human maintainer:** product identity, technical intent, visual taste, and
  final approval.

The workflow deliberately keeps technical verification separate from editorial
judgment. The goal is to preserve the rigor of the existing research while
removing process-driven, formulaic README content.