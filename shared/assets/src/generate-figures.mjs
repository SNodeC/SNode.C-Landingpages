import {mkdirSync, writeFileSync} from "node:fs";
import {dirname, resolve} from "node:path";

const root = resolve(import.meta.dirname, "../../..");
const C = {
    bg: "#0b1220",
    bg2: "#111b2e",
    panel: "#14223a",
    panel2: "#192a46",
    line: "#38506f",
    text: "#f5f8ff",
    muted: "#a9b8cd",
    blue: "#58a6ff",
    green: "#56d364",
    violet: "#bc8cff",
    amber: "#e3b341",
    cyan: "#39c5cf",
    red: "#ff7b72",
};

const esc = (value) => String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");

function defs(accent) {
    return `<defs>
      <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="${C.bg}"/><stop offset="1" stop-color="${C.bg2}"/>
      </linearGradient>
      <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="${accent}" stop-opacity=".95"/>
        <stop offset="1" stop-color="${accent}" stop-opacity=".35"/>
      </linearGradient>
      <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
        <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity=".035"/>
      </pattern>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0 0L10 5L0 10Z" fill="${accent}"/>
      </marker>
      <marker id="arrow-muted" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
        <path d="M0 0L10 5L0 10Z" fill="${C.muted}"/>
      </marker>
    </defs>`;
}

function base(width, height, accent, body, label) {
    return `<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 ${width} ${height}">
  <title id="title">${esc(label)}</title>
  <desc id="desc">${esc(label)}</desc>
  ${defs(accent)}
  <rect width="${width}" height="${height}" rx="30" fill="url(#bg)"/>
  <rect width="${width}" height="${height}" rx="30" fill="url(#grid)"/>
  <path d="M0 ${height - 8}H${width}" stroke="${accent}" stroke-width="8" opacity=".9"/>
  ${body}
</svg>\n`;
}

function heading(kicker, title, subtitle, accent, x = 80, y = 74) {
    const titleSize = title.length > 55 ? 34 : title.length > 45 ? 38 : title.length > 36 ? 42 : 48;
    return `<text x="${x}" y="${y}" fill="${accent}" font-family="Inter,ui-sans-serif,system-ui" font-size="20" font-weight="700" letter-spacing="3">${esc(kicker.toUpperCase())}</text>
    <text x="${x}" y="${y + 62}" fill="${C.text}" font-family="Inter,ui-sans-serif,system-ui" font-size="${titleSize}" font-weight="750">${esc(title)}</text>
    <text x="${x}" y="${y + 105}" fill="${C.muted}" font-family="Inter,ui-sans-serif,system-ui" font-size="22">${esc(subtitle)}</text>`;
}

function node(x, y, w, h, title, detail, accent, options = {}) {
    const radius = options.radius ?? 18;
    const icon = options.icon ? `<text x="${x + 24}" y="${y + 38}" fill="${accent}" font-family="ui-monospace,monospace" font-size="24" font-weight="700">${esc(options.icon)}</text>` : "";
    const tx = x + (options.icon ? 64 : 24);
    const lines = Array.isArray(detail) ? detail : [detail];
    return `<g>
      <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${radius}" fill="${options.fill ?? C.panel}" stroke="${options.stroke ?? accent}" stroke-width="${options.strong ? 3 : 1.5}"/>
      ${icon}
      <text x="${tx}" y="${y + 38}" fill="${C.text}" font-family="Inter,ui-sans-serif,system-ui" font-size="22" font-weight="700">${esc(title)}</text>
      ${lines.map((line, i) => `<text x="${x + 24}" y="${y + 72 + i * 25}" fill="${C.muted}" font-family="Inter,ui-sans-serif,system-ui" font-size="17">${esc(line)}</text>`).join("\n")}
    </g>`;
}

function pill(x, y, text, accent, width = 150) {
    return `<g><rect x="${x}" y="${y}" width="${width}" height="36" rx="18" fill="${accent}" fill-opacity=".13" stroke="${accent}"/>
      <text x="${x + width / 2}" y="${y + 24}" text-anchor="middle" fill="${accent}" font-family="Inter,ui-sans-serif,system-ui" font-size="14" font-weight="700">${esc(text)}</text></g>`;
}

function arrow(x1, y1, x2, y2, accent, label = "", dashed = false) {
    const ly = (y1 + y2) / 2 - 10;
    return `<g><path d="M${x1} ${y1}L${x2} ${y2}" fill="none" stroke="${accent}" stroke-width="3" ${dashed ? 'stroke-dasharray="10 9"' : ""} marker-end="url(#${accent === C.muted ? "arrow-muted" : "arrow"})"/>
      ${label ? `<text x="${(x1 + x2) / 2}" y="${ly}" text-anchor="middle" fill="${C.muted}" font-family="Inter,ui-sans-serif,system-ui" font-size="14">${esc(label)}</text>` : ""}</g>`;
}

function pathArrow(d, accent, label = "", lx = 0, ly = 0, dashed = false) {
    return `<g><path d="${d}" fill="none" stroke="${accent}" stroke-width="3" ${dashed ? 'stroke-dasharray="10 9"' : ""} marker-end="url(#${accent === C.muted ? "arrow-muted" : "arrow"})"/>
      ${label ? `<text x="${lx}" y="${ly}" text-anchor="middle" fill="${C.muted}" font-family="Inter,ui-sans-serif,system-ui" font-size="14">${esc(label)}</text>` : ""}</g>`;
}

function codePanel(x, y, w, h, lines, accent, title = "example.cpp") {
    return `<g><rect x="${x}" y="${y}" width="${w}" height="${h}" rx="20" fill="#0a101c" stroke="${C.line}"/>
      <circle cx="${x + 25}" cy="${y + 25}" r="6" fill="${C.red}"/><circle cx="${x + 45}" cy="${y + 25}" r="6" fill="${C.amber}"/><circle cx="${x + 65}" cy="${y + 25}" r="6" fill="${C.green}"/>
      <text x="${x + w - 22}" y="${y + 31}" text-anchor="end" fill="${C.muted}" font-family="ui-monospace,monospace" font-size="14">${esc(title)}</text>
      ${lines.map((line, i) => `<text x="${x + 25}" y="${y + 72 + i * 30}" fill="${line.startsWith("//") ? C.muted : C.text}" font-family="ui-monospace,SFMono-Regular,monospace" font-size="17"><tspan fill="${accent}" opacity=".95">${String(i + 1).padStart(2, " ")}</tspan><tspan dx="18">${esc(line)}</tspan></text>`).join("\n")}
    </g>`;
}

function write(relative, svg) {
    const file = resolve(root, relative);
    mkdirSync(dirname(file), {recursive: true});
    writeFileSync(file, svg);
}

function productMark(name, role, accent, glyph, relative) {
    const body = `<circle cx="84" cy="100" r="52" fill="${accent}" fill-opacity=".12" stroke="${accent}" stroke-width="3"/>
      <text x="84" y="114" text-anchor="middle" fill="${accent}" font-family="ui-monospace,monospace" font-size="38" font-weight="800">${esc(glyph)}</text>
      <text x="160" y="86" fill="${C.text}" font-family="Inter,ui-sans-serif,system-ui" font-size="34" font-weight="760">${esc(name)}</text>
      <text x="160" y="122" fill="${C.muted}" font-family="Inter,ui-sans-serif,system-ui" font-size="17">${esc(role)}</text>
      <rect x="160" y="146" width="160" height="5" rx="2.5" fill="${accent}"/>`;
    write(relative, base(480, 220, accent, body, `${name}: ${role}`));
}

// Organization assets.
write("SNode.C-orga/assets/organization-hero.svg", base(1600, 800, C.blue, `
  ${heading("SNodeC ecosystem", "Build from the network up", "Independent layers. Focused projects. Two honest evaluation tracks.", C.blue)}
  <g transform="translate(80 245)">
    ${node(0, 0, 430, 300, "Networking foundations", ["Event-driven C++ building blocks", "Address, transport, connection, protocol"], C.blue, {icon: "<>"})}
    ${node(505, 0, 430, 300, "Protocols & integrations", ["MQTT systems and typed Codex access", "Composable, independently versioned"], C.green, {icon: "⇄"})}
    ${node(1010, 0, 430, 300, "Applications & interfaces", ["Focused tools and visible workflows", "Native and browser presentations"], C.amber, {icon: "▣"})}
    ${arrow(430, 150, 505, 150, C.blue, "build on")}
    ${arrow(935, 150, 1010, 150, C.blue, "present")}
  </g>
  <text x="800" y="670" text-anchor="middle" fill="${C.muted}" font-family="Inter,ui-sans-serif,system-ui" font-size="18">The categories stay stable as the catalog grows.</text>
`, "SNodeC ecosystem categories"));

productMark("SNode.C", "Networking foundation", C.blue, "S.", "SNode.C-orga/assets/product-snodec.svg");
productMark("MQTTSuite", "Protocols and integrations", C.green, "MQ", "SNode.C-orga/assets/product-mqttsuite.svg");
productMark("AISuite", "Typed protocol integration", C.violet, "AI", "SNode.C-orga/assets/product-aisuite.svg");
productMark("CodexUI", "Applications and interfaces", C.amber, "UI", "SNode.C-orga/assets/product-codexui.svg");

write("SNode.C-orga/assets/ecosystem-architecture.svg", base(1200, 675, C.blue, `
  ${heading("Ecosystem architecture", "Stable layers, independent releases", "Solid arrows: runtime communication · Dashed arrows: build/package dependency", C.blue, 55, 50)}
  ${node(70, 220, 285, 125, "SNode.C", ["event loop · sockets", "HTTP · WebSocket · TLS"], C.blue, {icon: "S."})}
  ${node(455, 160, 285, 125, "MQTTSuite", ["broker · CLI · mapping", "bridge · persistence"], C.green, {icon: "MQ"})}
  ${node(455, 370, 285, 125, "AISuite", ["typed SDKs · routing", "controller / observer"], C.violet, {icon: "AI"})}
  ${node(840, 370, 285, 125, "CodexUI", ["native Qt · browser", "visible workflows"], C.amber, {icon: "UI"})}
  ${arrow(355, 282, 455, 222, C.muted, "package", true)}
  ${arrow(355, 282, 455, 432, C.muted, "package", true)}
  ${arrow(740, 432, 840, 432, C.violet, "frontend")}
  ${pill(470, 545, "MQTT track", C.green, 180)}
  ${pill(785, 545, "Typed Codex track", C.violet, 220)}
`, "SNodeC ecosystem runtime and build relationships"));

write("SNode.C-orga/assets/evaluation-routes.svg", base(1200, 675, C.cyan, `
  ${heading("Evaluation routes", "Choose the outcome you want to see", "The tracks share a foundation, not an invented runtime integration.", C.cyan, 55, 50)}
  ${pill(70, 185, "NETWORKING + MQTT", C.green, 230)}
  ${node(70, 245, 250, 120, "SNode.C", ["run echo", "observe connection"], C.blue, {icon: "1"})}
  ${node(420, 245, 250, 120, "MQTTSuite", ["publish QoS 1", "observe message"], C.green, {icon: "2"})}
  ${arrow(320, 305, 420, 305, C.green, "then")}
  ${pill(70, 440, "VISIBLE OUTCOME", C.green, 190)}
  <text x="285" y="465" fill="${C.text}" font-family="Inter,ui-sans-serif,system-ui" font-size="19">Echo + local MQTT message flow</text>
  ${pill(730, 185, "TYPED CODEX CLIENT", C.violet, 230)}
  ${node(730, 245, 185, 120, "SNode.C", ["networking", "components"], C.blue, {icon: "1"})}
  ${node(960, 245, 185, 120, "AISuite", ["bridge", "typed access"], C.violet, {icon: "2"})}
  ${node(845, 430, 185, 120, "CodexUI", ["native / web", "workflow"], C.amber, {icon: "3"})}
  ${arrow(915, 305, 960, 305, C.violet)}
  ${pathArrow("M1052 365C1052 405 1015 430 990 445", C.violet)}
`, "Two separate SNodeC evaluation routes"));

// SNode.C assets.
write("SNode.C/assets/snodec-hero.svg", base(1600, 800, C.blue, `
  ${heading("SNode.C", "Event-driven C++ networking", "One programming model from listener configuration to per-connection callbacks.", C.blue)}
  ${codePanel(80, 225, 690, 410, [
      "using EchoSocketServer =",
      "    net::NET::stream::legacy::SocketServer<",
      "        EchoServerSocketContextFactory>;",
      "",
      "EchoSocketServer getServer() {",
      "    return EchoSocketServer(\"echoserver\");",
      "}",
  ], C.blue, "apps/echo/model/servers.h · excerpt")}
  ${node(900, 245, 600, 110, "LISTENING", ["IPv4 loopback · event loop ready"], C.blue, {icon: "01", strong: true})}
  ${node(900, 390, 600, 110, "CONNECTED", ["SocketContext created · callback dispatched"], C.cyan, {icon: "02"})}
  ${node(900, 535, 600, 110, "ECHO", ["message returned · connection remains event-driven"], C.green, {icon: "03"})}
  ${arrow(1200, 355, 1200, 390, C.blue)}${arrow(1200, 500, 1200, 535, C.blue)}
`, "SNode.C code-to-result hero"));

write("SNode.C/assets/programming-model.svg", base(1200, 675, C.blue, `
  ${heading("Programming model", "Configuration becomes connection-local behavior", "Factories create one context per accepted or established connection.", C.blue, 55, 50)}
  ${node(70, 230, 260, 130, "SocketServer", ["accepts connections", "owns listener instance"], C.blue, {icon: "S"})}
  ${node(70, 420, 260, 130, "SocketClient", ["initiates connection", "owns client instance"], C.cyan, {icon: "C"})}
  ${node(465, 325, 280, 145, "SocketContextFactory", ["selects application context", "constructs per connection"], C.violet, {icon: "F", strong: true})}
  ${node(875, 325, 260, 145, "SocketContext", ["connected · data · close", "application callbacks"], C.green, {icon: "CTX", strong: true})}
  ${pathArrow("M330 295C395 295 410 365 465 380", C.blue, "accepted", 395, 300)}
  ${pathArrow("M330 485C395 485 410 430 465 415", C.blue, "established", 398, 486)}
  ${arrow(745, 397, 875, 397, C.blue, "create")}
`, "SNode.C SocketServer and SocketClient programming model"));

write("SNode.C/assets/layer-architecture.svg", base(1200, 675, C.blue, `
  ${heading("Layer architecture", "Compose behavior without hiding boundaries", "Availability does not imply that every theoretical combination is qualified.", C.blue, 55, 48)}
  ${node(80, 205, 1040, 70, "Application protocol", ["MQTT 3.1.1 · HTTP applications · Express-style routing"], C.violet, {icon: "05"})}
  ${node(80, 290, 1040, 70, "Connection and upgrade", ["HTTP parsing · WebSocket upgrade · connection lifecycle"], C.cyan, {icon: "04"})}
  ${node(80, 375, 1040, 70, "Transport and encryption", ["stream transport · OpenSSL TLS where configured"], C.green, {icon: "03"})}
  ${node(80, 460, 1040, 70, "Network and address", ["IPv4 · IPv6 · Unix domain · optional Bluetooth families"], C.blue, {icon: "02"})}
  ${node(80, 545, 1040, 70, "Event loop and operating system", ["epoll multiplexer · timers · descriptors · signals"], C.amber, {icon: "01"})}
`, "SNode.C layered networking architecture"));

// MQTTSuite assets.
write("MQTTSuite/assets/mqttsuite-hero.svg", base(1600, 800, C.green, `
  ${heading("MQTTSuite · MQTT 3.1.1", "Five focused applications, one message flow", "Broker, inspect, transform, forward, and persist without collapsing the roles.", C.green)}
  ${node(70, 240, 270, 190, "MQTTBroker", ["accept clients", "serve Web UI"], C.green, {icon: "B", strong: true})}
  ${node(370, 240, 270, 190, "MQTTCli", ["publish", "subscribe / inspect"], C.cyan, {icon: ">_"})}
  ${node(670, 240, 270, 190, "MQTTIntegrator", ["map topics", "transform payloads"], C.violet, {icon: "{}"})}
  ${node(970, 240, 270, 190, "MQTTBridge", ["connect brokers", "filter / prefix"], C.blue, {icon: "⇄"})}
  ${node(1270, 240, 270, 190, "MQTTStore", ["raw envelope", "MariaDB projection"], C.amber, {icon: "DB"})}
  ${pathArrow("M205 430C205 550 1405 550 1405 430", C.green, "one suite · explicit process boundaries", 805, 582)}
  ${pill(645, 650, "MQTT 3.1.1", C.green, 310)}
`, "MQTTSuite five-application hero"));

write("MQTTSuite/assets/integration-scenario.svg", base(1200, 675, C.green, `
  ${heading("Integration scenario", "From edge measurement to routed and stored data", "Synthetic topic: edge-lab/room-01/temperature · QoS 1", C.green, 55, 48)}
  ${node(45, 270, 190, 125, "Sensor", ["21.7 °C", "JSON payload"], C.cyan, {icon: "°C"})}
  ${node(315, 270, 220, 125, "MQTTBroker", ["MQTT 3.1.1", "Web UI"], C.green, {icon: "B", strong: true})}
  ${node(610, 160, 230, 125, "MQTTIntegrator", ["normalize topic", "transform payload"], C.violet, {icon: "{}"})}
  ${node(925, 135, 230, 125, "MQTTBridge", ["filter / prefix", "remote broker"], C.blue, {icon: "⇄"})}
  ${node(610, 400, 230, 125, "MQTTStore", ["raw envelope", "typed projection"], C.amber, {icon: "DB"})}
  ${node(925, 425, 230, 125, "MariaDB", ["operator schema", "persistence"], C.amber, {icon: "SQL"})}
  ${node(315, 475, 220, 105, "MQTTCli", ["verify publish / subscribe"], C.cyan, {icon: ">_"})}
  ${arrow(235, 332, 315, 332, C.green, "publish")}
  ${pathArrow("M535 300C565 300 580 230 610 222", C.green, "subscribe", 570, 252)}
  ${pathArrow("M535 350C565 350 580 445 610 462", C.green, "store", 565, 410)}
  ${arrow(840, 222, 925, 197, C.green, "forward")}
  ${arrow(840, 462, 925, 487, C.green, "persist")}
  ${pathArrow("M425 475L425 395", C.cyan, "inspect", 458, 438)}
`, "MQTTSuite complete synthetic integration scenario"));

// AISuite assets.
write("AISuite/assets/aisuite-hero.svg", base(1600, 800, C.violet, `
  ${heading("AISuite", "Typed clients, one bounded bridge", "C++ and browser integrations share routing without becoming a second Codex authority.", C.violet)}
  ${node(70, 235, 340, 130, "Native C++ client", ["AISuite::OpenAICodex", "typed asynchronous views"], C.blue, {icon: "C++"})}
  ${node(70, 410, 340, 130, "Browser client", ["@snodec/codex-frontend", "typed WebSocket lifecycle"], C.amber, {icon: "TS"})}
  ${node(620, 290, 380, 210, "codex-bridge", ["bounded framing and queues", "routing · correlation", "controller / observer policy"], C.violet, {icon: "BR", strong: true})}
  ${node(1210, 320, 320, 150, "Codex app-server", ["protocol semantics", "conversation persistence"], C.cyan, {icon: "AS", strong: true})}
  ${pathArrow("M410 300C500 300 530 350 620 365", C.violet, "frontend envelopes", 515, 292)}
  ${pathArrow("M410 475C500 475 530 435 620 420", C.violet, "codex subprotocol", 515, 488)}
  ${arrow(1000, 395, 1210, 395, C.violet, "native JSON-RPC")}
  ${pill(655, 575, "TRANSIENT ROUTING — NOT PERSISTENCE", C.violet, 410)}
`, "AISuite C++ and browser clients converging on codex-bridge"));

write("AISuite/assets/authority-boundaries.svg", base(1200, 675, C.violet, `
  ${heading("Architecture and authority", "Each layer owns one kind of state", "Transport boundaries do not transfer semantic or persistence authority.", C.violet, 55, 48)}
  <rect x="55" y="190" width="310" height="390" rx="24" fill="${C.panel}" stroke="${C.blue}" stroke-width="2"/>
  <text x="85" y="230" fill="${C.blue}" font-family="Inter,ui-sans-serif,system-ui" font-size="17" font-weight="700">CLIENT BOUNDARY</text>
  ${node(85, 260, 250, 115, "Controller", ["presentation", "local interaction"], C.blue, {icon: "C"})}
  ${node(85, 410, 250, 115, "Observer", ["allowed reads", "visible role"], C.cyan, {icon: "O"})}
  <rect x="445" y="190" width="310" height="390" rx="24" fill="${C.panel}" stroke="${C.violet}" stroke-width="2"/>
  <text x="475" y="230" fill="${C.violet}" font-family="Inter,ui-sans-serif,system-ui" font-size="17" font-weight="700">AISUITE BRIDGE</text>
  ${node(475, 260, 250, 265, "Transient coordination", ["transport adaptation", "routing / correlation", "controller assignment", "bounded telemetry", "no conversation database"], C.violet, {icon: "BR", strong: true})}
  <rect x="835" y="190" width="310" height="390" rx="24" fill="${C.panel}" stroke="${C.cyan}" stroke-width="2"/>
  <text x="865" y="230" fill="${C.cyan}" font-family="Inter,ui-sans-serif,system-ui" font-size="17" font-weight="700">APP-SERVER</text>
  ${node(865, 260, 250, 265, "Semantic authority", ["Codex operations", "thread / turn meaning", "conversation state", "persistence", "provider lifecycle"], C.cyan, {icon: "AS", strong: true})}
  ${arrow(365, 385, 445, 385, C.violet, "frontend")}${arrow(755, 385, 835, 385, C.violet, "provider")}
`, "AISuite client bridge and app-server authority boundaries"));

write("AISuite/assets/typed-generation-flow.svg", base(1200, 675, C.violet, `
  ${heading("Typed generation", "One input set, two language surfaces", "Equality tests detect drift; raw JSON remains a bounded escape path.", C.violet, 55, 48)}
  ${node(55, 250, 235, 145, "Recorded inputs", ["JSON schema", "Rust operation bindings"], C.cyan, {icon: "IN"})}
  ${node(385, 250, 235, 145, "Generator", ["deterministic output", "source hashes"], C.violet, {icon: "GEN", strong: true})}
  ${node(725, 165, 220, 145, "C++ views", ["typed access", "getRaw()"], C.blue, {icon: "C++"})}
  ${node(725, 365, 220, 145, "TypeScript", ["typed declarations", "browser SDK"], C.amber, {icon: "TS"})}
  ${node(1015, 250, 150, 145, "Equality", ["names · maps", "counts · hashes"], C.green, {icon: "="})}
  ${arrow(290, 322, 385, 322, C.violet)}
  ${pathArrow("M620 300C665 300 680 235 725 235", C.violet)}
  ${pathArrow("M620 345C665 345 680 437 725 437", C.violet)}
  ${pathArrow("M945 235C980 235 980 300 1015 310", C.green)}
  ${pathArrow("M945 437C980 437 980 350 1015 340", C.green)}
`, "AISuite shared C++ and TypeScript protocol generation"));

// CodexUI assets.
write("CodexUI/assets/presentation-architecture.svg", base(1200, 675, C.amber, `
  ${heading("Presentation architecture", "Two clients, one bridge contract", "Native and browser paths converge without sharing an implementation runtime.", C.amber, 55, 48)}
  <rect x="55" y="190" width="480" height="390" rx="24" fill="${C.panel}" stroke="${C.blue}" stroke-width="2"/>
  <text x="85" y="230" fill="${C.blue}" font-family="Inter,ui-sans-serif,system-ui" font-size="17" font-weight="700">NATIVE PROCESS</text>
  ${node(85, 265, 190, 120, "Qt GUI", ["widgets", "presentation state"], C.amber, {icon: "QT"})}
  ${node(315, 265, 190, 120, "SNode.C thread", ["AISuite client", "selected transport"], C.blue, {icon: "C++"})}
  ${arrow(275, 325, 315, 325, C.blue, "bounded JSONL")}
  ${node(85, 430, 420, 100, "Native-only integrations", ["local Git · filesystem · desktop · non-WebSocket transports"], C.blue, {icon: "+"})}
  <rect x="595" y="190" width="250" height="390" rx="24" fill="${C.panel}" stroke="${C.amber}" stroke-width="2"/>
  <text x="625" y="230" fill="${C.amber}" font-family="Inter,ui-sans-serif,system-ui" font-size="17" font-weight="700">BROWSER</text>
  ${node(625, 265, 190, 160, "CodexWebUI", ["React presentation", "TypeScript SDK", "WebSocket / WSS"], C.amber, {icon: "WEB", strong: true})}
  ${node(625, 460, 190, 70, "No Node runtime", ["static artifact"], C.green, {icon: "✓"})}
  ${node(925, 250, 220, 130, "codex-bridge", ["routing", "controller policy"], C.violet, {icon: "BR", strong: true})}
  ${node(925, 445, 220, 105, "Codex app-server", ["semantics · persistence"], C.cyan, {icon: "AS"})}
  ${pathArrow("M505 325C700 325 770 290 925 305", C.amber, "frontend transport", 710, 290)}
  ${arrow(845, 345, 925, 345, C.amber, "/codex")}
  ${arrow(1035, 380, 1035, 445, C.violet, "provider")}
`, "CodexUI native and browser presentation architecture"));

write("CodexUI/assets/state-and-reconnect.svg", base(1200, 675, C.amber, `
  ${heading("Interaction model", "Keep intent visible through background work and reconnect", "Selection does not silently redirect commands; reconnect rehydrates provider state.", C.amber, 55, 48)}
  <rect x="55" y="185" width="520" height="420" rx="24" fill="${C.panel}" stroke="${C.amber}" stroke-width="2"/>
  <text x="85" y="225" fill="${C.amber}" font-family="Inter,ui-sans-serif,system-ui" font-size="17" font-weight="700">SIMULTANEOUS UI STATE</text>
  ${node(85, 260, 210, 110, "Target", ["receives commands"], C.amber, {icon: "T", strong: true})}
  ${node(335, 260, 210, 110, "Active turn", ["current target work"], C.green, {icon: "A"})}
  ${node(85, 410, 210, 110, "Running", ["background activity"], C.violet, {icon: "R"})}
  ${node(335, 410, 210, 110, "Inspected", ["current view only"], C.blue, {icon: "I"})}
  <rect x="625" y="185" width="520" height="420" rx="24" fill="${C.panel}" stroke="${C.blue}" stroke-width="2"/>
  <text x="655" y="225" fill="${C.blue}" font-family="Inter,ui-sans-serif,system-ui" font-size="17" font-weight="700">RECOVERY SEQUENCE</text>
  ${node(655, 260, 190, 90, "Connected", ["role visible"], C.green, {icon: "1"})}
  ${node(925, 260, 190, 90, "Provider loss", ["failure visible"], C.red, {icon: "2"})}
  ${node(655, 435, 190, 90, "Reattach", ["fresh frontend"], C.amber, {icon: "3"})}
  ${node(925, 435, 190, 90, "Resynchronize", ["provider authority"], C.blue, {icon: "4"})}
  ${arrow(845, 305, 925, 305, C.amber)}
  ${pathArrow("M1020 350C1020 400 850 400 750 435", C.amber)}
  ${arrow(845, 480, 925, 480, C.amber)}
`, "CodexUI target state and reconnect sequence"));

function socialSource(name, kicker, statement, accent, glyph, tags) {
    return base(1280, 640, accent, `
      <circle cx="140" cy="150" r="70" fill="${accent}" fill-opacity=".13" stroke="${accent}" stroke-width="4"/>
      <text x="140" y="169" text-anchor="middle" fill="${accent}" font-family="ui-monospace,monospace" font-size="52" font-weight="800">${esc(glyph)}</text>
      <text x="245" y="135" fill="${accent}" font-family="Inter,ui-sans-serif,system-ui" font-size="18" font-weight="750" letter-spacing="3">${esc(kicker.toUpperCase())}</text>
      <text x="245" y="195" fill="${C.text}" font-family="Inter,ui-sans-serif,system-ui" font-size="48" font-weight="780">${esc(name)}</text>
      <text x="80" y="340" fill="${C.text}" font-family="Inter,ui-sans-serif,system-ui" font-size="48" font-weight="760">${esc(statement)}</text>
      ${tags.map((tag, index) => pill(80 + index * 250, 425, tag, accent, 220)).join("\n")}
      <text x="80" y="550" fill="${C.muted}" font-family="Inter,ui-sans-serif,system-ui" font-size="18">github.com/SNodeC</text>
    `, `${name}: ${statement}`);
}

write("SNode.C-orga/assets/src/social-preview.svg", socialSource("SNodeC ecosystem", "Open-source C++ systems", "Build from the network up", C.blue, "S.", ["Foundations", "Integrations", "Interfaces"]));
write("SNode.C/assets/src/social-preview.svg", socialSource("SNode.C", "Networking foundation", "Event-driven C++ networking", C.blue, "S.", ["Event loop", "Sockets", "Protocols"]));
write("MQTTSuite/assets/src/social-preview.svg", socialSource("MQTTSuite", "MQTT 3.1.1", "Five focused applications. One flow.", C.green, "MQ", ["Broker", "Integrate", "Persist"]));
write("AISuite/assets/src/social-preview.svg", socialSource("AISuite", "Typed Codex integration", "Typed clients. One bounded bridge.", C.violet, "AI", ["C++", "TypeScript", "Routing"]));
write("CodexUI/assets/src/social-preview.svg", socialSource("CodexUI", "Native + browser", "Codex, clearly.", C.amber, "UI", ["Qt", "Browser", "Inspector"]));

console.log("Generated 17 SVG figures and 5 editable social-preview sources.");
