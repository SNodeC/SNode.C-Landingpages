import {writeFileSync} from "node:fs";

const [url, destination, widthArg = "1600", heightArg = "900", delayArg = "1800", scaleArg = "2"] = process.argv.slice(2);

if (!url || !destination) {
    throw new Error("usage: capture-page.mjs <url> <destination.png> [width] [height] [delay-ms]");
}

const width = Number(widthArg);
const height = Number(heightArg);
const delay = Number(delayArg);
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

await send("Page.enable");
await send("Emulation.setDeviceMetricsOverride", {width, height, deviceScaleFactor: scale, mobile: false});
await send("Page.navigate", {url});
await new Promise((resolve) => setTimeout(resolve, delay));
const result = await send("Page.captureScreenshot", {format: "png", captureBeyondViewport: false, fromSurface: true});
writeFileSync(destination, Buffer.from(result.data, "base64"));
socket.close();
await fetch(`${endpoint}/json/close/${target.id}`);
