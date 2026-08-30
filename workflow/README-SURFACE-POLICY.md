# Canonical README and GitHub Pages surface policy

This document records the canonical content-surface decision for the SNode.C ecosystem publication workflow.

It applies to SNode.C, MQTTSuite, AISuite, CodexUI, and later ecosystem repositories unless a project-specific artifact explicitly overrides it.

## 1. Primary publication surface: repository README

The current README publication workflow produces **GitHub repository README content**.

A repository README is not treated as a decorative marketing landing page. It is the repository's front door and must explain enough for a technically capable reader to understand:

- what the project or application is;
- why and when it is useful;
- how its major concepts fit together;
- how to build or install it when applicable;
- how to achieve a first useful result;
- how it is configured at the level needed for first deployment/use;
- how the important deployment or usage variants work;
- where to continue for application-specific or deeper material.

The workflow phrase `README = landing page` therefore means **repository front door**, not **short promotional page**.

Do not interpret `prefer omission over completeness` as permission to omit information required to understand or use the project. Omit low-value reference detail, duplicated internals, exhaustive API listings, and qualification-process prose; do not omit the operational and conceptual material that makes the software usable.

## 2. Application suites require layered repository READMEs

When a repository contains multiple substantial runnable applications, the preferred GitHub structure is layered:

1. **Root repository README** — suite identity, application selection, shared architecture, shared build/install, first success, common configuration/deployment concepts, representative examples, and routes to each application.
2. **Application README beside each application** — usage, deployment, configuration, application-specific examples, verification, operational boundaries, and troubleshooting for that executable.

The root README must establish enough shared foundation that the application READMEs do not each need to repeat the complete suite-level explanation.

The application READMEs must nevertheless stand on their own sufficiently that a reader entering an application directory can understand what the executable does and how to start using/deploying it.

For MQTTSuite, this means a root README plus application READMEs for:

- MQTTBroker;
- MQTTIntegrator;
- MQTTBridge;
- MQTTCli;
- MQTTStore.

## 3. Appropriate depth for repository READMEs

Repository README depth is determined by reader need and project shape, not by a fixed word-count target.

A framework README may legitimately spend substantial space on its programming model, extension points, build/installation path, and a concrete first application.

An application README may legitimately spend substantial space on command structure, configuration files, deployment topologies, connection variants, examples, and operator-facing behavior.

A suite root README may be broader than a single-application README because it must explain both the common foundation and how the applications relate, while still routing detailed operation to the per-application READMEs.

Longer is not automatically better. The criterion is whether the document helps the reader understand and use the software without forcing them to reconstruct essential behavior from source code.

## 4. GitHub Pages is a secondary documentation surface

GitHub Pages is **not the deliverable of the current README workflow**.

Pages may later provide a unified documentation portal with navigation across:

- repository READMEs;
- application READMEs;
- deeper tutorials and guides;
- architecture material;
- generated API/reference documentation;
- larger cross-project documentation sets.

If GitHub Pages is added later, prefer repository Markdown and other repository documentation as canonical source material rather than maintaining a second independently authored description of the same behavior.

Pages is therefore a **presentation/navigation layer for deeper documentation**, not a replacement for useful repository READMEs.

A user should not need to leave a GitHub repository merely to discover what a contained application does, how to build/install the project, or how to start using the application.

## 5. SNode.C reference classification

The completed `SNode.C/README.md` in `SNodeC/SNode.C-Landingpages` is a **GitHub repository README publication**, not a GitHub Pages chapter.

Its programming-model explanation, build/install walkthrough, echo first-success path, capability discussion, architecture/extension discussion, and task-oriented routing are therefore valid evidence that ecosystem GitHub READMEs may contain substantial technical and usage material.

SNode.C may link from its README to separately rendered/generated documentation such as the API reference. Such linked documentation can live on GitHub Pages without changing the classification of the README itself.

The correct lesson from SNode.C is not that every README must copy its structure. The lesson is that a GitHub README can be a substantial, technically useful front door while deeper reference material remains elsewhere.

## 6. Content ownership rule

Use this default ownership model:

### Root README owns

- identity and value proposition;
- audience/application selection;
- shared conceptual architecture;
- shared build/install path;
- first useful success;
- shared configuration model;
- representative deployment/usage patterns;
- important cross-application concepts;
- concise fit/trust/release boundaries;
- routes to application READMEs and deeper documentation.

### Application README owns

- application purpose and deployment role;
- executable-specific quick start;
- configuration hierarchy and files;
- connection/transport examples supported by that application;
- operational workflows;
- application-specific data/configuration models;
- multiple practical examples where needed;
- verification/troubleshooting;
- application-specific trust/credential/storage boundaries.

### Deeper documentation / possible future Pages material owns

- exhaustive schemas and field-by-field reference when too large for an application README;
- long tutorials spanning several applications;
- full API/reference material;
- generated Doxygen/reference documentation;
- broad architecture material not required for ordinary use;
- historical design rationale.

An application README may still include a substantial explanation of a complex feature such as MQTTSuite mapping when that explanation is necessary to use the application. The deeper reference should extend that README rather than excuse an unusably thin README.

## 7. Figure policy across README and Pages surfaces

Figures belong in repository READMEs whenever they materially improve comprehension of architecture, topology, configuration, lifecycle, mapping, or data flow.

Do not minimize figures merely because a README is rendered on GitHub. Conversely, do not add decorative figures that do not teach anything.

During content drafting, plan figure positions and write short placeholders describing the intended visual and the question it should answer. Produce final visuals only after the prose and information architecture are stable enough to determine what each figure truly needs to explain.

A later GitHub Pages site may reuse these figures and may add deeper/reference visuals, but Pages must not be required for the repository README to remain understandable.

## 8. Consequence for the accelerated workflow

For application or suite projects, Step 4 and Step 6 must not mechanically apply the compact `orient → differentiate → proof → first success → fit-check → route deeper` sequence as a page-length constraint.

That sequence remains useful as the **reader-entry rhythm**, but Step 6 may and should continue into substantial build/install, use, configuration, deployment, and application-specific explanation where the project requires it.

For a multi-application suite, Step 6 may produce multiple coordinated README candidates rather than only one root candidate.

The canonical quality target is:

**A polished GitHub front door that is broad enough to understand and use the project, with deeper application READMEs where the repository contains substantial runnable applications.**

GitHub Pages, if later desired, is planned and executed as a separate documentation-site workflow after the repository README system is stable.
