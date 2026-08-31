# MQTTSuite README publication state

**Status:** post-review text-correction state established 31 August 2026  
**Supersedes as a publication gate:** `08-PRODUCT-IMPLEMENTATION-DECISIONS.md` Decisions A–H  
**Documentation architecture:** application-suite-first Step-6 architecture remains accepted  
**Current visual-production scope:** [`10-VISUAL-PRODUCTION-PLAN.md`](10-VISUAL-PRODUCTION-PLAN.md)

## Human decision

The previously frozen implementation Decisions A–H were explicitly reverted as prerequisites for the README publication workflow. They are **not blockers for README revision or Landingpages publication**, and their proposed implementation changes are not scheduled as part of this documentation pass.

`08-PRODUCT-IMPLEMENTATION-DECISIONS.md` remains historical decision/review evidence. Its statements that README revision or publication is blocked by A–H are superseded by this artifact.

Documentation must therefore describe the **actual current implementation**, including user-relevant limitations and trust boundaries, instead of documenting desired future behavior as though it existed.

## Subsequent narrow implementation correction

After this publication state was first established, MQTTIntegrator wildcard handling was corrected in `SNodeC/mqttsuite` PR #22.

Current source baseline:

```text
master: 6c0ff62c612694a6111ff971c446327938130cf0
PR #22 implementation commit: d15f70a2818d291638c50aa2e2116a9e49ebd9e1
```

The correction is deliberately narrow:

- `MqttMapper::findMatchingTopicLevel()` treats terminal `#` as a true MQTT multi-level wildcard;
- `#` consumes zero or more remaining topic levels;
- `parent/#` can match `parent` itself when the parent has no own subscription mapping;
- `+` remains single-level;
- no mapping schema, configuration, or unrelated behavior changed.

The former publication statement that Integrator `#` matched only one level is **obsolete and superseded**. Reader-facing documentation uses the post-fix semantics.

## Post-review documentation correction pass

Two independent reviews were reconciled against the current Landingpages tree and current MQTTSuite source. The resulting correction pass is complete in the reader-facing documentation.

Closed correctness/consistency items include:

1. Integrator mapping examples now nest `static`, `value`, and `json` inside `subscription`, matching the unchanged schema.
2. The SNode.C configuration reference route no longer depends on the Landingpages sibling-directory layout.
3. MQTTBridge commands scope `--definition` and `--html-dir` under the required `bridge` subcommand.
4. MQTTStore no longer overclaims malformed projection files as guaranteed process-startup failure; loading/validation is located at MQTT context creation and the whole-process consequence remains `[UNVERIFIED-RUNTIME]`.
5. MQTTIntegrator documentation no longer implies that fixed `admin/admin` administration credentials can be changed through a supported application configuration option.
6. The stale implementation-repository MQTTStore user-guide route is no longer canonical publication guidance.
7. Quick-start output wording follows the real MQTTCli formatter/capture rather than a reconstructed four-line transcript, and Broker quick starts use debug-level logging where listener-state visibility is expected.
8. Shared documentation states the actual client-side remote-port defaults, including direct TLS client instances defaulting to `1883`, and distinguishes application-local HTTP/admin instance names and ports.
9. MQTTStore documents `--auto-create-raw-table=true` as the default, the explicit `false` DBA-managed-table mode, and the non-empty MariaDB socket default/help semantics.
10. MQTTCli documents publish-topic `##<qos>` overrides as well as subscription overrides.
11. Broker, Integrator, Bridge, and Store application documentation routes directly to the relevant deeper references.
12. Bridge/Store signpost pages are described honestly as routing pages rather than falsely as independent deep owners.
13. The Integrator mapping reference documents exact template context names and the retained-empty suppression carve-out.
14. Integrator UI/catch-all routing is consistent between mapping and HTTP references.
15. The root README states project/release positioning and the `nlohmann_json >= 3.7.0` build requirement.

These corrections do not constitute new runtime qualification beyond the evidence classes stated in the individual documents.

## Visual-production state

The original [`05-VISUALS.md`](05-VISUALS.md) is preserved as the historical Step-5A validation/provenance record for V1–V3 and its runtime-capture evidence. Its original “three visuals only” production scope is **not** the current figure-count/ownership plan after the later README/reference expansion.

The canonical post-review production scope is [`10-VISUAL-PRODUCTION-PLAN.md`](10-VISUAL-PRODUCTION-PLAN.md):

- **24** reader-facing canonical figure briefs;
- duplicate mapping-pipeline, Integrator-admin, Bridge-restart/SSE, Store-raw-persistence, and root-topology briefs consolidated;
- a missing subscription-QoS-versus-publish-QoS brief added;
- explicit figure ownership assigned by document;
- the three trust-boundary figures retained as separate application-specific instances of one shared visual template.

Figure production is gated on the final documentation audit. If that audit changes a contract, the relevant brief must be updated before Figma production.

## Current behavior that remains intentionally visible

Examples of current implementation boundaries that remain in the publication documentation include:

- MQTTBroker HTTP administration/event routes have no application authentication in the reviewed source and use permissive CORS on the documented API/event surface;
- Broker client event state can contain MQTT password material and live event JSON can reach normal logs;
- MQTTIntegrator startup contains an inline demo mapping before the supported configuration parse, so implicit/default mapping selection must not be oversimplified;
- MQTTIntegrator administration uses the known fixed Basic Auth defaults `admin/admin` without a supported application configuration path for replacing them in the reviewed wiring;
- MQTTSuite declares CMake 3.14 while current SNode.C requires 3.18; the documented whole-source workflow therefore uses 3.18+;
- clean arbitrary custom-prefix execution of the installed suite remains `UNVERIFIED-RUNTIME`;
- MQTTStore projection configuration is loaded during MQTT context creation; the exact malformed-plan process/reconnect consequence remains `UNVERIFIED-RUNTIME`;
- MQTTBridge schema/runtime discrepancies and bounded loop-prevention behavior remain documented rather than hidden.

These are documentation boundaries, not promises to implement additional corrections.

## Publication-shaped canonical paths

The canonical README/documentation copy in this repository is shaped to match the eventual `SNodeC/mqttsuite` destination:

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

README draft copies are no longer canonical workflow artifacts and are removed from `MQTTSuite/workflow/`. Workflow remains the home for governance, technical facts, design decisions, visual instructions, reviews, handoffs, limitations, and publication state.

## Evidence baselines

- Current MQTTSuite source behavior: `SNodeC/mqttsuite@6c0ff62c612694a6111ff971c446327938130cf0`.
- Narrow Integrator wildcard correction: PR #22 / `d15f70a2818d291638c50aa2e2116a9e49ebd9e1`.
- SNode.C implementation surface reviewed for shared behavior: `SNodeC/snode.c@5d6453c21df4894083b445cce00b627e7794932a`.
- Recorded runtime qualification: MQTTSuite `52de563...` rebuilt/installed against SNode.C `60f26d9...` on the environment recorded in `05-VISUALS.md`; this qualification predates PR #22.

No MQTTSuite or SNode.C implementation repository was modified by this documentation correction pass.
