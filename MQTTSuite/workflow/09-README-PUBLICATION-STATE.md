# MQTTSuite README publication state

**Status:** README publication-shaped Landingpages state authorized 31 August 2026  
**Supersedes as a publication gate:** `08-PRODUCT-IMPLEMENTATION-DECISIONS.md` Decisions A–H  
**Documentation architecture:** application-suite-first Step-6 architecture remains accepted

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

- `MqttMapper::findMatchingTopicLevel()` now treats terminal `#` as a true MQTT multi-level wildcard;
- `#` consumes zero or more remaining topic levels;
- `parent/#` can match `parent` itself when the parent has no own subscription mapping;
- `+` remains single-level;
- no mapping schema, configuration, or unrelated behavior changed.

The former publication statement that Integrator `#` matched only one level is therefore **obsolete and superseded**. Reader-facing documentation must use the post-fix semantics.

Examples of other current behavior that remain visible in the publication documentation include:

- MQTTBroker HTTP administration/event routes have no application authentication in the reviewed source and currently use permissive CORS on the API surface;
- Broker client event state can contain MQTT password material and live event JSON can reach normal logs;
- MQTTIntegrator startup contains an inline demo mapping before the supported configuration parse, so implicit/default mapping selection must not be oversimplified;
- MQTTIntegrator administration uses the known Basic Auth defaults `admin/admin` without a supported application configuration path for replacing them in the reviewed wiring;
- MQTTSuite still declares CMake 3.14 while current SNode.C requires 3.18; the documented whole-source workflow therefore uses 3.18+;
- clean arbitrary custom-prefix execution of the installed suite remains `UNVERIFIED-RUNTIME`;
- MQTTStore projection configuration is loaded during MQTT context creation; the exact malformed-plan process/reconnect consequence remains `UNVERIFIED-RUNTIME`.

These are documentation boundaries, not promises to implement the reverted corrections.

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

No MQTTSuite or SNode.C implementation repository is modified by this publication-state change.
