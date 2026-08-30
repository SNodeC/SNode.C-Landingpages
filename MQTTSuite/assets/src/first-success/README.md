# V2 raw terminal capture provenance

These PNG files are uncomposed source captures for Step 5B. They are real
terminal pixels from the qualified runtime; they are not final publication
assets and contain no reconstructed application output.

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

The build and capture environment was Debian GNU/Linux forky/sid on x86-64,
with GCC/G++ 16.2.0, CMake 4.3.4, Ninja 1.13.2, and the dependency versions
recorded in `MQTTSuite/workflow/05-VISUALS.md`.

## Exact runtime commands

Run from the qualification root.

Broker:

```sh
./mqttsuite-build/mqttbroker/mqttbroker --config-file /dev/null --log-level 4 \
  in-mqtt local --host 127.0.0.1 --port 18885 \
  in-mqtts --disabled \
  in6-mqtt --disabled \
  in6-mqtts --disabled \
  un-mqtt --disabled \
  un-mqtts --disabled \
  in-http --disabled \
  in-https --disabled \
  in6-http --disabled \
  in6-https --disabled \
  un-http --disabled \
  un-https --disabled
```

Subscriber:

```sh
./mqttsuite-build/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-subscriber --qos 1 \
  sub --topic edge-lab/room-01/temperature
```

Publisher:

```sh
./mqttsuite-build/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-publisher --qos 1 \
  pub --topic edge-lab/room-01/temperature \
      --message '{"value":21.7,"unit":"C"}'
```

`ss -ltn` confirmed that `127.0.0.1:18885` was the only broker listener.
HTTP/admin, TLS, IPv6, and Unix-domain listeners were disabled.

## Capture method and timing

- Isolated display: Xvfb with TCP disabled; no live desktop was used.
- Terminal emulator: xterm.
- Geometry: `132 × 38` character cells for every terminal.
- Font: DejaVu Sans Mono, 14 point.
- Raw PNG size: `1588 × 916` pixels for every terminal.
- Capture tool: ImageMagick `import` against each live xterm window.
- The command line was emitted by the live shell's execution trace. All
  application output was rendered directly by the running executable. No
  command or output glyph was inserted, retyped, filtered, or edited after
  capture.

The broker was started first. `broker-raw.png` was captured after the real
`listener started` result and before client event JSON added unnecessary noise.
The subscriber was then connected and subscribed, followed by the publisher.
The publisher command received the Ctrl-C/SIGINT signal immediately after the
first successful delivery and before its approximately one-second
reconnect/republish interval. The raw terminal session contained exactly one
subscriber `MQTT Publish` result.

## Observed result

The subscriber received `edge-lab/room-01/temperature` and the application
pretty-printed the canonical JSON with `unit` before `value`. The same live
result visibly reports `QoS: 1`, `Retain: false`, and `Dup: false` in
`subscriber-raw.png`.

Capture files and SHA-256:

```text
b7b3c15fa67ec0a57cbfa8658a0e4ca43b9d99748a453814f8391fe42e59cf28  broker-raw.png
acde6dc51a2020417daa67cc7381ff0b67e9dfde230c89bcfb29b8fa9e613dff  subscriber-raw.png
d33a42fd2f9c07743894a96bfa06d28534093cea5c0d5bdf757d8e214d8114cb  publisher-raw.png
```

## Teardown and privacy review

Teardown order was publisher, subscriber, then broker. All received the normal
Ctrl-C/SIGINT path; `127.0.0.1:18885` was closed and no qualification process
remained.

No MQTT username/password, certificate, will, real hostname, LAN address,
maintainer username, home path, shell history, or unrelated desktop content is
visible. Only loopback addresses, synthetic client IDs, the canonical synthetic
topic/payload, relative qualification paths, and application logs appear.
