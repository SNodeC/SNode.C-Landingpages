# MQTTSuite README publication state

**Status:** README publication-shaped Landingpages state authorized 31 August 2026  
**Supersedes as a publication gate:** `08-PRODUCT-IMPLEMENTATION-DECISIONS.md` Decisions A–H  
**Documentation architecture:** application-suite-first Step-6 architecture remains accepted

## Human decision

The previously frozen implementation Decisions A–H were explicitly reverted as prerequisites for the README publication workflow. They are **not blockers for README revision or Landingpages publication**, and their proposed implementation changes are not scheduled as part of this documentation pass.

`08-PRODUCT-IMPLEMENTATION-DECISIONS.md` remains historical decision/review evidence. Its statements that README revision or publication is blocked by A–H are superseded by this artifact.

Documentation must therefore describe the **actual current implementation**, including user-relevant limitations and trust boundaries, instead of documenting the desired A–H behavior as though it existed.

Examples of current behavior that remain visible in the publication documentation include:

- MQTTBroker HTTP administration/event routes have no application authentication in the reviewed source and currently use permissive CORS on the API surface;
- Broker client event state can contain MQTT password material and live event JSON can reach normal logs;
- MQTTIntegrator mapper-level `#` does not implement MQTT multi-level wildcard semantics;
- MQTTIntegrator startup contains an inline demo mapping before the supported configuration parse, so implicit/default mapping selection must not be oversimplified;
- MQTTIntegrator administration uses the known Basic Auth defaults `admin/admin` without a supported application configuration path for replacing them in the reviewed wiring;
- MQTTSuite still declares CMake 3.14 while current SNode.C requires 3.18; the documented whole-source workflow therefore uses 3.18+;
- clean arbitrary custom-prefix execution of the installed suite remains `UNVERIFIED-RUNTIME`;
- MQTTStore projection configuration is loaded during MQTT context creation; the exact malformed-plan process/reconnect consequence remains `UNVERIFIED-RUNTIME`.

These are documentation boundaries, not promises to implement the reverted corrections.

## Publication-shaped canonical paths

The canonical README/documentation copy in this repository is now shaped to match the eventual `SNodeC/mqttsuite` destination:

```text
MQTTSuite/README.md
MQTTSuite/mqttbroker/README.md
MQTTSuite/mqttintegrator/README.md
MQTTSuite/mqttbridge/README.md
MQTTSuite/mqttcli/README.md
MQTTSuite/mqttstore/README.md
MQTTSuite/docs/configuration.md
MQTTSuite/docs/capabilities.md
MQTTSuite/docs/integrator-mapping.md
MQTTSuite/docs/broker-http-api.md
```

README draft copies are no longer canonical workflow artifacts and are removed from `MQTTSuite/workflow/`. Workflow remains the home for governance, technical facts, design decisions, visual instructions, reviews, handoffs, limitations, and publication state.

## Evidence baselines

- MQTTSuite implementation: `SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`.
- SNode.C implementation surface reviewed for shared behavior: `SNodeC/snode.c@5d6453c21df4894083b445cce00b627e7794932a`.
- SNode.C head observed during publication: `1f8725173c04acd7bc964aa9d6ead289def509e5`; the only commit above `5d6453c...` at this check adds a documentation-only organization logging inventory.
- Recorded runtime qualification: MQTTSuite `52de563...` rebuilt/installed against SNode.C `60f26d9...` on the environment recorded in `05-VISUALS.md`.

No MQTTSuite or SNode.C implementation repository is modified by this publication-state change.