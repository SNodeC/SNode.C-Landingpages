# Codex technical audit

**Review target:** `MQTTSuite/workflow/06-README-DRAFT.md`<br>
**Frozen commit:** `815480724e735574f86bc903f050ef3a39cdff21`

## Verdict

**CHANGES REQUIRED.** The frozen README's written technical claims and all three
quick-start commands align with the canonical evidence, but two approved visual
compositions convey incorrect sequence or message-flow semantics. The
first-success visual is a publication blocker because following its numbered
order can miss the demonstrated non-retained message.

Finding counts: **1 BLOCKER, 1 IMPORTANT, 0 MODERATE, 0 POLISH.**

## Findings

### BLOCKER

#### 1. The first-success visual puts the publisher before the subscriber

- **README section/phrase:** `## Run the first message`, the `<picture>` using
  `assets/first-success-terminal.png` and
  `assets/first-success-terminal-mobile.png`. The desktop composition shows
  `Broker → Publisher → Subscriber`; the mobile composition numbers the panes
  `1 MQTT Broker`, `2 MQTT Publisher`, `3 MQTT Subscriber`.
- **Problem:** Those visual sequences contradict both the written walkthrough and
  the qualified run. This publication uses `Retain: false`; if a reader starts
  the publisher before the subscriber as the mobile numbering directs, the
  subscriber can miss the one publication. The desktop arrows are also wrong
  whether read as startup order (Broker → Subscriber → Publisher) or message
  delivery (Publisher → Broker → Subscriber). This is an actual technical
  error in the primary runtime-proof visual, not a stylistic preference.
- **Authoritative evidence:** `MQTTSuite/workflow/05-VISUALS.md`, V2 `Exact
  qualified commands`, starts Terminal 2 as the subscriber and Terminal 3 as the
  publisher; its recorded subscriber output is `Retain: false`. The frozen
  README itself preserves that qualified order in lines 100–117.
- **Required correction direction:** Recompose both V2 assets with one
  unambiguous semantic. For process order, use **Broker → Subscriber →
  Publisher** and number the mobile panes in that order. If the desktop arrows
  instead represent message delivery, use **Publisher → Broker → Subscriber**
  and label them as message flow. Preserve the same qualified raw captures,
  canonical topic/payload, QoS 1, and `Retain: false` / `Dup: false` evidence.

### IMPORTANT

#### 1. The mobile application-role figure visually connects MQTTBridge to MQTTStore

- **README section/phrase:** `## One MQTT message, five roles`, the mobile source
  `assets/application-message-flow-mobile.svg` selected by the `<picture>`.
- **Problem:** In the mobile composition, a connector enters the top of
  MQTTBridge and another connector exits the bottom of MQTTBridge into
  MQTTStore. This depicts or strongly implies `MQTTBroker → MQTTBridge →
  MQTTStore`. MQTTStore is not downstream of MQTTBridge in the validated role
  model; it subscribes as its own outbound MQTT client. The small footer about
  the broker anchor does not remove the explicit box-to-box connection. The
  desktop figure and adjacent README prose have the correct relationship.
- **Authoritative evidence:** `MQTTSuite/workflow/03-TECHNICAL-FACTS.md` §§2, 7,
  and 9 define MQTTBridge and MQTTStore as separate outbound-client roles.
  `MQTTSuite/workflow/05-VISUALS.md`, V1 `Exact content`, requires relationship
  5 as `MQTTBroker → MQTTStore` and relationship 6 as `MQTTStore → MariaDB`;
  it never defines a Bridge → Store path.
- **Required correction direction:** Give MQTTStore a visibly independent
  `MQTTBroker A → MQTTStore` subscribed-publication connector, using a repeated
  broker anchor if needed for the vertical layout. Remove any line that touches
  both the MQTTBridge and MQTTStore boxes. Keep `MQTTStore → MariaDB` and the
  raw-envelope-first / JSON-dependent projection labels unchanged.

### MODERATE

None.

### POLISH

None.

## Verified without issue

- **Product and application roles:** The copy consistently presents five
  separately runnable applications. MQTTIntegrator remains a standalone
  outbound client; optional in-broker mapping is distinct. MQTTBridge is not
  described as a broker or transformation engine. MQTTStore remains
  raw-envelope-first with JSON/configuration-dependent typed projections to
  MariaDB.
- **Quick-start commands:** All three commands match the qualified executable
  names, subcommand hierarchy, option placement, disabled-listener set,
  loopback host/port, client IDs, QoS, topic, payload, and non-retained result.
  The README accurately warns that the publisher reconnects and republishes and
  gives the qualified Ctrl-C teardown order.
- **Protocol and transports:** MQTT 3.1.1 is explicit. The README makes no MQTT
  5, full-conformance, Bluetooth, or tested transport-matrix claim. It correctly
  separates source inventory from the one plain-IPv4 runtime proof.
- **Mapping, bridge, and storage boundaries:** Mapping forms and output controls
  remain within the Step 3 source evidence. Bridge selection, prefixes,
  forwarding to other connected members, exact-source-member suppression, and
  non-standard origin-reflection limits are correctly bounded. No schema
  lifecycle, retention, backup, access-policy, transactional, or retry guarantee
  is invented for MQTTStore.
- **Trust boundaries:** The README does not turn CONNECT credential fields into
  broker authentication, TLS into authorization, or the broker/bridge admin
  surfaces into remote-safe interfaces. It states MQTTIntegrator's current
  default BasicAuth credentials and the credential/raw-payload exposure
  boundaries.
- **Release, packaging, platform, and license:** The historical `v1.0.1` release
  is distinguished from current master. OpenWrt is accurately limited to the
  older four-application package set whose `mqttsuite-full` omits MQTTStore. No
  binary/container/broad platform claim is made. The upstream license expression
  is correctly `MIT OR GPL-3.0-or-later`.
- **Other visual semantics:** V1 desktop preserves the validated application
  roles and source-only evidence label. V3 is presented only as the genuine
  MQTTBroker dashboard with staged synthetic broker state; the prose does not
  treat it as suite-wide UI, authentication proof, complete admin-operation
  proof, or Integrator/Bridge/Store runtime evidence.
- **Links:** The internal heading anchors and all six responsive asset paths
  resolve at the frozen commit. The public repository, application-directory,
  MQTTStore guide, issues, releases, license, and SNode.C destinations exist and
  point to the intended technical targets.
- **Freshness:** At audit time, public MQTTSuite `master` remained
  `52de5631245c6318bfa5b7cca700f0754014f34d`, public SNode.C `master` remained
  `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`, and `v1.0.1` remained the latest
  public MQTTSuite GitHub release.

## Technical publication recommendation

Do not publish the frozen candidate with the current V2 assets. Correct and
targetedly revalidate the two visual relationships above against the existing
Step 5 evidence. No technical rewrite of the README prose or quick-start command
blocks is required by this audit.
