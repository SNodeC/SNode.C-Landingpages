# V3 raw MQTTBroker dashboard capture provenance

These PNG files are uncomposed source captures for Step 5B. They contain only
real pixels rendered by the dashboard shipped with the qualified MQTTBroker
build. They are not final publication assets.

## Qualified source and build

- MQTTSuite: `52de5631245c6318bfa5b7cca700f0754014f34d`
- SNode.C: `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`
- Reused Step 5A qualification root: `mqttsuite-step5a.MDg8gq/`
- MQTTSuite source/build directories within that root:
  `mqttsuite-current/` and `mqttsuite-build/`
- SNode.C source/build/install directories within that root:
  `snode-current/`, `snode-build/`, and `prefix/`
- The existing Step 5A binaries were reused without rebuilding. Both public
  `master` heads were checked immediately before capture and still matched the
  SHAs above.

The environment was Debian GNU/Linux forky/sid on x86-64. The dashboard was
captured with Google Chrome 151.0.7922.137 through Playwright 1.62.1.

## Exact launch and fixture commands

Run from the qualification root.

Broker:

```sh
./mqttsuite-build/mqttbroker/mqttbroker --config-file /dev/null --log-level 3 \
  in-mqtt local --host 127.0.0.1 --port 18885 \
  in-mqtts --disabled \
  in6-mqtt --disabled \
  in6-mqtts --disabled \
  un-mqtt --disabled \
  un-mqtts --disabled \
  in-http local --host 127.0.0.1 --port 18080 \
  in-https --disabled \
  in6-http --disabled \
  in6-https --disabled \
  un-http --disabled \
  un-https --disabled
```

Persistent subscriber:

```sh
./mqttsuite-build/mqttcli/mqttcli --config-file /dev/null --log-level 3 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-subscriber --qos 1 \
  sub --topic edge-lab/room-01/temperature
```

One retained publication:

```sh
./mqttsuite-build/mqttcli/mqttcli --config-file /dev/null --log-level 3 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-publisher --qos 1 \
  pub --topic edge-lab/room-01/temperature \
      --message '{"value":21.7,"unit":"C"}' --retain=true
```

The publisher received Ctrl-C/SIGINT immediately after its first retained
publication, before the qualified reconnect/republish interval. The subscriber
remained connected during both browser captures.

## Route, state, and live updates

The browser opened `http://127.0.0.1:18080/clients`, which resolved through the
qualified `/clients` redirect to `/clients/index.html`. The served application
identified itself as dashboard v439.

Both fresh browser contexts received HTTP 200 from `/api/mqtt/events`. The
rendered state showed:

- `Clients: 1` with `landing-subscriber`;
- `Topics: 3` as reported by the current dashboard;
- `Subscriptions: 1` for `edge-lab/room-01/temperature` at QoS 1;
- `Retained: 1` with the unchanged compact payload
  `{"value":21.7,"unit":"C"}` at QoS 1;
- three activity cards: client connected, client subscribed, and retained
  message set.

The existing `MQTTSuite/assets/broker-web-ui.png` was not used.

## Viewports and capture method

Each capture used a new headless Chromium context with browser chrome absent,
device scale factor 2, light color scheme, and reduced motion.

- `dashboard-desktop-raw.png`: application rendered at a `1600 × 1000` CSS
  viewport. A real top-of-viewport `1600 × 900` CSS-pixel clip excludes the
  product footer while retaining the complete dashboard evidence. The high-
  density PNG is `3200 × 1800` pixels.
- `dashboard-620-raw.png`: application genuinely rendered at a `620 × 1100`
  CSS viewport. The real responsive `Activity` tab was selected before capture.
  This is not a desktop crop. The high-density PNG is `1240 × 2200` pixels.

No control, count, card, topic, payload, responsive state, or application glyph
was redrawn or modified.

Capture files and SHA-256:

```text
0e624210fd99ab58dce2e85327fb8caafac6db74271201efe6e95635b092f62c  dashboard-desktop-raw.png
f43e53188ee71b466bd651606a75f917008262ca1d18205eeac653c9647c2981  dashboard-620-raw.png
```

## Teardown and privacy review

After capture, both browser/SSE contexts closed, followed by subscriber and
broker Ctrl-C/SIGINT teardown. Ports `18885` and `18080` were closed and no
qualification process remained.

The images expose no browser tabs, URL bar, bookmarks, extensions, credentials,
private network address, maintainer username, home path, or unrelated desktop
content. The desktop viewport clip excludes the dashboard's product footer;
the responsive Activity capture does not expose it. Visible identities and data
are limited to the synthetic client/topic/payload and loopback-qualified state.
