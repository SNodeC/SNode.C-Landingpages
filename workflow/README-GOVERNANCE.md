# README redesign governance

This document resolves the presentation-governance conflict identified by
`workflow/01-REPOSITORY-AUDIT.md`.

It applies to the AI-assisted redesign of the SNode.C organization profile and
the SNode.C, MQTTSuite, AISuite, and CodexUI GitHub landing pages.

## Authority

For the README redesign, use this order when presentation rules conflict:

1. root `AGENTS.md` and `workflow/README-WORKFLOW.md`;
2. this governance document;
3. the nearest scoped `AGENTS.md` for project facts, terminology, boundaries,
   source locations, proof requirements, and misconceptions;
4. `PAGE-SYSTEM.md` for shared editorial, visual, capture, accessibility, and
   asset principles;
5. project `PROPOSAL.md` files and existing READMEs/assets as research inputs.

The canonical workflow owns the redesign process and handoffs. Scoped
instructions may narrow technical or project-specific requirements, but they do
not impose a fixed README template when that conflicts with the canonical
workflow.

## Superseded fixed-format rules

The following requirements from the earlier landing-page system are no longer
mandatory for the redesign:

- a fixed nine-section product-page architecture;
- fixed 1,300–1,600 word targets for product READMEs;
- a fixed 900–1,100 word target for the organization profile;
- mandatory V1–V4 visual slots;
- mandatory exact V1–V4 filenames or placements;
- exactly four in-page visuals per product;
- equal editorial or visual weight regardless of project needs;
- proposal-defined section counts or visual layouts treated as immutable.

Any conflicting statement in `PAGE-SYSTEM.md`, a scoped `AGENTS.md`, a
`PROPOSAL.md`, `LAUNCH-ROADMAP.md`, or an existing README is historical planning
input and is superseded for the redesign by this document and the canonical
workflow.

## What remains mandatory

The redesign keeps the strong principles from the earlier system:

- technical claims must be source-aligned and evidence-backed;
- landing pages are orientation and evaluation surfaces, not complete manuals;
- lead with user outcome, proof, and the shortest useful evaluation path;
- each project keeps a distinct technical centerpiece;
- real product screenshots come from qualified builds and use synthetic data;
- screenshot scenes must be reproducible and privacy-reviewed;
- diagrams must represent verified architecture and must not imply unsupported
  combinations or runtime relationships;
- visuals need information-bearing alt text and useful captions;
- pages must remain understandable when images fail to load;
- visuals must be legible at GitHub content width and checked in light, dark,
  and mobile rendering;
- editable visual/capture sources stay under the relevant `assets/src/` tree;
- the organization profile remains extensible and must not encode a permanent
  project count;
- the two ecosystem demo tracks remain separate unless a real qualified
  all-product scenario exists.

## Step 4 design freedom

`<Project>/workflow/04-README-DESIGN.md` decides the actual reader journey for
that project.

The Step 4 designer should normally propose **2–3 meaningful in-page visuals**,
but this is a design default rather than a quota. Fewer or more are acceptable
when the storyboard provides a clear reason. A social preview is separate from
the in-page visual count.

Likewise, section count and prose length are outcomes of the reader journey, not
compliance targets. Keep the page as short as possible while still allowing an
experienced technical visitor to understand the product, see credible proof,
reach first success, understand important boundaries, and find deeper routes.

Useful content elements such as a hero, first-success path, centerpiece,
capabilities/limitations summary, architecture explanation, requirements, and
project routes remain available building blocks. They do not have to appear as
nine fixed top-level sections or in the old order.

## Product individuality

The pages share a design language, not a copied template:

- **SNode.C:** programming model;
- **MQTTSuite:** MQTT applications and message flows;
- **AISuite:** typed AI middleware and bridge architecture;
- **CodexUI:** real user workflow and UI;
- **SNode.C organization:** ecosystem navigation.

Do not force a technically different project into a layout merely to make the
pages look symmetrical.

## Existing assets and proposals

Existing screenshots, figures, social previews, proposals, and README drafts
remain research/provenance material until their replacement is approved. Do not
delete them merely because their previous layout rules are superseded.

Old exported graphics may be archived only after useful semantics and capture
provenance have been transferred to the new workflow artifacts and approved
replacements exist. Git history remains the historical record of the superseded
fixed-format system.

## Resolution status

The governance conflict recorded in Step 1 is **RESOLVED** by this document.
Step 2 may use the preserved research immediately, and Step 4 must follow this
governance together with `workflow/README-WORKFLOW.md` rather than the old fixed
V1–V4/page-count system.
