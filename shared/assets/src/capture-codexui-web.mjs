import {writeFileSync} from "node:fs";

const [destination, bridgePort = "14582", scaleArg = "2"] = process.argv.slice(2);
if (!destination) throw new Error("usage: capture-codexui-web.mjs <destination.png> [bridge-port] [scale]");
const scale = Number(scaleArg);

const endpoint = "http://127.0.0.1:9223";
const target = await fetch(`${endpoint}/json/new?${encodeURIComponent("about:blank")}`, {method: "PUT"}).then((response) => response.json());
const socket = new WebSocket(target.webSocketDebuggerUrl);
let sequence = 0;
const pending = new Map();

await new Promise((resolve, reject) => {
    socket.addEventListener("open", resolve, {once: true});
    socket.addEventListener("error", reject, {once: true});
});

socket.addEventListener("message", (event) => {
    const message = JSON.parse(event.data);
    const request = pending.get(message.id);
    if (!request) return;
    pending.delete(message.id);
    if (message.error) request.reject(new Error(message.error.message));
    else request.resolve(message.result);
});

function send(method, params = {}) {
    const id = ++sequence;
    socket.send(JSON.stringify({id, method, params}));
    return new Promise((resolve, reject) => pending.set(id, {resolve, reject}));
}

const wait = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));
const evaluate = (expression) => send("Runtime.evaluate", {expression, awaitPromise: true, returnByValue: true});

await send("Page.enable");
await send("Runtime.enable");
await send("Emulation.setDeviceMetricsOverride", {width: 1600, height: 900, deviceScaleFactor: scale, mobile: false});
await send("Page.navigate", {url: `http://127.0.0.1:${bridgePort}/`});
await wait(700);
await evaluate("document.querySelector('.connection-control button')?.click()");
await wait(900);
await evaluate("document.querySelector('.thread-row')?.click()");
await wait(900);
const result = await send("Page.captureScreenshot", {format: "png", captureBeyondViewport: false, fromSurface: true});
writeFileSync(destination, Buffer.from(result.data, "base64"));
socket.close();
await fetch(`${endpoint}/json/close/${target.id}`);
