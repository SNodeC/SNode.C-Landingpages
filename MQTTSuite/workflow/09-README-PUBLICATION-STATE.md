# MQTTSuite README publication state

**Status:** post-review text-correction and editorial-reduction state established 1 September 2026  
**Supersedes as a publication gate:** `08-PRODUCT-IMPLEMENTATION-DECISIONS.md` Decisions A–H  
**Documentation architecture:** application-suite-first Step-6 architecture remains accepted  
**Current visual-production scope:** [`10-VISUAL-PRODUCTION-PLAN.md`](10-VISUAL-PRODUCTION-PLAN.md)

## Human decision

The previously frozen implementation Decisions A–H were explicitly reverted as prerequisites for the README publication workflow. They are **not blockers for README revision or Landingpages publication**. Documentation describes the actual current implementation, including user-relevant limitations and trust boundaries, instead of documenting desired future behavior as though it existed.

`08-PRODUCT-IMPLEMENTATION-DECISIONS.md` remains historical decision/review evidence.

## Current implementation baseline

```text
SNodeC/mqttsuite master: 6c0ff62c612694a6111ff971c446327938130cf0
PR #22 implementation commit: d15f70a2818d291638c50aa2e2116a9e49ebd9e1
```

PR #22 corrected MQTTIntegrator terminal `#` matching to MQTT multi-level semantics while leaving `+` single-level. No mapping schema change accompanied that correction.

Shared SNode.C behavior used by the reader-facing documentation remains pinned from the source revisions named by the individual references. The recorded runtime qualification remains MQTTSuite `52de563...` against SNode.C `60f26d9...`; it predates PR #22 and is not rewritten as current runtime evidence.

## Completed correctness pass

The post-review correction pass closed the previously identified publication defects, including:

1. schema-valid Integrator mapping examples;
2. publication-safe SNode.C configuration routing;
3. correct MQTTBridge subcommand hierarchy;
4. correct MQTTStore projection-validation/runtime boundary wording;
5. correct MQTTIntegrator fixed-admin-credential guidance;
6. removal of the stale Store user-guide route;
7. real quick-start output wording and Broker debug visibility;
8. actual client-side port defaults and application-local admin listener names;
9. Store auto-create/socket defaults and DBA-managed mode;
10. MQTTCli publication `##<qos>` overrides;
11. direct application → deep-reference navigation;
12. explicit Bridge/Store routing-page ownership;
13. exact Integrator template/suppression semantics in the deep mapping reference;
14. aligned Integrator HTTP/UI routing;
15. project/release/dependency positioning.

The effective dependency wording is now explicit: MQTTSuite itself declares nlohmann/json `3.7.0`, while the current SNode.C MQTT component requires `3.11+`; therefore the complete current SNode.C + MQTTSuite source workflow documents `3.11+`.

## Post-audit editorial reduction

After `11-FINAL-DOCUMENTATION-AUDIT.md` passed the correctness/completeness review, the reader-facing tree received a non-structural **de-forensics / progressive-disclosure pass**.

Purpose:

- remove review chronology and audit rationale from public-facing prose;
- keep source evidence behind the claims rather than narrating the review process;
- let the root README remain an application-suite landing page;
- let application READMEs stay operationally complete without duplicating deep references;
- keep exhaustive mapping/API/configuration contracts in the documents that own them;
- preserve all user-relevant limitations, trust boundaries, commands, defaults, examples, and figure briefs.

Files materially reduced:

```text
MQTTSuite/README.md
MQTTSuite/mqttintegrator/README.md
MQTTSuite/mqttstore/README.md
MQTTSuite/mqttcli/README.md
MQTTSuite/docs/configuration.md
```

MQTTBroker and MQTTBridge were intentionally not broadly reduced in this pass because their current detail remains primarily application-operational rather than review-forensic.

This editorial pass does **not** constitute new runtime qualification and does not change the accepted documentation architecture or the current 24-figure production inventory.

## Relationship to the final audit

[`11-FINAL-DOCUMENTATION-AUDIT.md`](11-FINAL-DOCUMENTATION-AUDIT.md) is the historical final correctness/completeness audit for its recorded input HEAD. Its technical closure remains valid as review evidence, but its exact prose inventory predates the editorial reduction above.

Future publication validation must therefore run against the current reader-facing tree, not assume byte-for-byte identity with the audit input.

## Current visual-production state

The original [`05-VISUALS.md`](05-VISUALS.md) remains the historical Step-5A runtime/capture provenance record.

The canonical figure-production scope remains [`10-VISUAL-PRODUCTION-PLAN.md`](10-VISUAL-PRODUCTION-PLAN.md):

- 24 reader-facing figure briefs;
- single conceptual ownership;
- source-only vs runtime-qualified evidence kept visually distinct where relevant;
- real product output required for runtime-proof terminal/UI figures.

## Current behavior that remains intentionally visible

Reader-facing documentation continues to expose material current boundaries, including:

- unauthenticated Broker and Bridge administration surfaces;
- fixed source-known Integrator `admin/admin` credentials with no built-in replacement option;
- credential-sensitive logs/configuration state;
- MQTTIntegrator startup-mapping ambiguity unless a mapping file is selected explicitly;
- current Bridge schema/runtime transport discrepancies;
- Store projection loading during MQTT context creation with exact whole-process/retry behavior remaining `[UNVERIFIED-RUNTIME]`;
- clean arbitrary custom-prefix execution remaining outside the recorded runtime qualification.

These are current product/documentation boundaries, not promises to implement additional corrections.

## Publication-shaped canonical paths

```text
MQTTSuite/README.md
MQTTSuite/mqttbroker/README.md
MQTTSuite/mqttintegrator/README.md
MQTTSuite/mqttbridge/README.md
MQTTSuite/mqttcli/README.md
MQTTSuite/mqttstore/README.md
MQTTSuite/docs/README.md
MQTTSuite/docs/configuration.md
MQTTSuite/docs/capabilities.md
MQTTSuite/docs/integrator-mapping.md
MQTTSuite/docs/integrator-sibling-topics-example.md
MQTTSuite/docs/broker-http-api.md
MQTTSuite/docs/integrator-http-api.md
MQTTSuite/docs/bridge-definition.md
MQTTSuite/docs/bridge-multi-broker-example.md
MQTTSuite/docs/bridge-http-api.md
MQTTSuite/docs/store-storage.md
```

README draft copies in `MQTTSuite/workflow/` are not canonical publication content.
