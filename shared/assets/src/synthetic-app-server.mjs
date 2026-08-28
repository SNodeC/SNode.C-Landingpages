#!/usr/bin/env node

import {createInterface} from "node:readline";

const threads = [
    {
        id: "landing-transport-review",
        name: "Transport boundary review",
        preview: "Transport boundary review",
        cwd: "/workspace/aisuite",
        status: {type: "idle"},
        updatedAt: 1787918400,
        createdAt: 1787914800,
    },
    {
        id: "landing-release-checklist",
        name: "Release checklist",
        preview: "Release checklist",
        cwd: "/workspace/codexui",
        status: {type: "idle"},
        updatedAt: 1787911200,
        createdAt: 1787907600,
    },
];

const detailedThread = {
    ...threads[0],
    turns: [{
        id: "landing-turn-1",
        status: "completed",
        items: [
            {
                id: "landing-user-1",
                type: "userMessage",
                content: [{type: "text", text: "Inspect the transport boundary and summarize the connection path."}],
            },
            {
                id: "landing-command-1",
                type: "commandExecution",
                command: "cmake --build cmake-build-release --parallel 8",
                cwd: "/workspace/codexui",
                status: "completed",
                aggregatedOutput: "[100%] Built target codex-ui\n",
                exitCode: 0,
            },
            {
                id: "landing-agent-1",
                type: "agentMessage",
                phase: "final_answer",
                text: "The browser uses WebSocket to codex-bridge. The bridge owns transient routing; app-server remains the semantic authority.",
            },
        ],
    }],
};

function resultFor(method, params) {
    if (method === "thread/list") return {data: threads, nextCursor: null};
    if (method === "thread/read") {
        const selected = params?.threadId === threads[1].id
            ? {...threads[1], turns: []}
            : detailedThread;
        return {thread: selected};
    }
    if (method === "model/list") return {data: []};
    if (method === "config/read") return {config: {}};
    if (method === "account/read") return {account: null};
    if (method === "account/rateLimits/read") return {rateLimits: null};
    if (method === "account/tokenUsage/read") return {tokenUsage: null};
    return {data: []};
}

const input = createInterface({input: process.stdin, crlfDelay: Infinity});
process.stderr.write("synthetic app-server: stdio provider ready\n");
input.on("line", (line) => {
    let request;
    try {
        request = JSON.parse(line);
    } catch {
        process.exitCode = 2;
        return;
    }
    if (request.id === undefined) return;
    process.stderr.write(`synthetic app-server: request ${request.method}\n`);
    const response = {
        jsonrpc: "2.0",
        id: request.id,
        result: resultFor(request.method, request.params),
    };
    process.stdout.write(`${JSON.stringify(response)}\n`);
});
