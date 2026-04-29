import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("QoD", () => {
    it("should create and delete a session (v0)", async () => {
        const session = await client.qod.createSession({
            device: {
                networkAccessIdentifier: "testdevice@testcsp.net",
                ipv4Address: {
                    publicAddress: "1.1.1.2",
                    privateAddress: "1.1.1.2",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "5.6.7.8",
            },
            qosProfile: "QOS_L",
            duration: 3600,
        });

        expect(session).toBeDefined();
        expect(session.sessionId).toBeDefined();
        expect(session.qosProfile).toEqual("QOS_L");

        await client.qod.deleteSession({
            sessionId: session.sessionId as string,
        });
    });

    it("should create and delete a session (v1)", async () => {
        const session = await client.qod.createSessionV1({
            device: {
                phoneNumber: "+99999991001",
                ipv4Address: {
                    publicAddress: "233.252.0.2",
                    privateAddress: "192.0.2.25",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "8.8.8.8",
            },
            qosProfile: "DOWNLINK_M_UPLINK_L",
            duration: 60,
        });

        expect(session).toBeDefined();
        expect(session.sessionId).toBeDefined();

        await client.qod.deleteSessionV1({
            sessionId: session.sessionId as string,
        });
    });

    it("should get a session by id (v0)", async () => {
        const session = await client.qod.createSession({
            device: {
                networkAccessIdentifier: "testdevice@testcsp.net",
                ipv4Address: {
                    publicAddress: "1.1.1.2",
                    privateAddress: "1.1.1.2",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "5.6.7.8",
            },
            qosProfile: "QOS_E",
            duration: 3600,
        });

        const fetched = await client.qod.getSession({
            sessionId: session.sessionId as string,
        });

        expect(fetched.sessionId).toEqual(session.sessionId);

        await client.qod.deleteSession({
            sessionId: session.sessionId as string,
        });
    });

    it("should list all sessions (v0)", async () => {
        const sessions = await client.qod.listSessions();
        expect(sessions).toBeDefined();
        expect(sessions instanceof Array).toBeTruthy();
    });

    it("should list all sessions (v1)", async () => {
        const sessions = await client.qod.listSessionsV1();
        expect(sessions).toBeDefined();
        expect(sessions instanceof Array).toBeTruthy();
    });

    it("should retrieve sessions for a device (v1)", async () => {
        const session = await client.qod.createSessionV1({
            device: {
                phoneNumber: "+99999991001",
                ipv4Address: {
                    publicAddress: "233.252.0.2",
                    privateAddress: "192.0.2.25",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "8.8.8.8",
            },
            qosProfile: "DOWNLINK_M_UPLINK_L",
            duration: 60,
        });

        const sessions = await client.qod.retrieveSessionsV1({
            device: {
                phoneNumber: "+99999991001",
            },
        });

        expect(sessions.length).toBeGreaterThan(0);

        await client.qod.deleteSessionV1({
            sessionId: session.sessionId as string,
        });
    });

    it("should create a session with device and service ports (v0)", async () => {
        const session = await client.qod.createSession({
            device: {
                networkAccessIdentifier: "testdevice@testcsp.net",
                ipv4Address: {
                    publicAddress: "1.1.1.2",
                    privateAddress: "1.1.1.2",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "5.6.7.8",
            },
            qosProfile: "QOS_L",
            duration: 3600,
            devicePorts: { ports: [80] },
            applicationServerPorts: { ranges: [{ from: 80, to: 443 }] },
        });

        expect(session).toBeDefined();
        expect(session.qosProfile).toEqual("QOS_L");

        await client.qod.deleteSession({
            sessionId: session.sessionId as string,
        });
    });

    it("should create a session with webhook (v0)", async () => {
        const session = await client.qod.createSession({
            device: {
                networkAccessIdentifier: "testdevice@testcsp.net",
                ipv4Address: {
                    publicAddress: "1.1.1.2",
                    privateAddress: "1.1.1.2",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "5.6.7.8",
            },
            qosProfile: "QOS_L",
            duration: 3600,
            webhook: {
                notificationUrl: "https://example.com/notify",
                notificationAuthToken: "my-token",
            },
        });

        expect(session).toBeDefined();

        await client.qod.deleteSession({
            sessionId: session.sessionId as string,
        });
    });

    it("should extend a session (v0)", async () => {
        const session = await client.qod.createSession({
            device: {
                networkAccessIdentifier: "testdevice@testcsp.net",
                ipv4Address: {
                    publicAddress: "1.1.1.2",
                    privateAddress: "1.1.1.2",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "5.6.7.8",
            },
            qosProfile: "QOS_L",
            duration: 60,
        });

        const extended = await client.qod.extendSession({
            sessionId: session.sessionId as string,
            requestedAdditionalDuration: 60,
        });

        expect(extended).toBeDefined();
        expect(extended.duration).toBeGreaterThanOrEqual(60);

        await client.qod.deleteSession({
            sessionId: session.sessionId as string,
        });
    });

    it("should fail to get a deleted session", async () => {
        const session = await client.qod.createSession({
            device: {
                networkAccessIdentifier: "testdevice@testcsp.net",
                ipv4Address: {
                    publicAddress: "1.1.1.2",
                    privateAddress: "1.1.1.2",
                    publicPort: 80,
                },
            },
            applicationServer: {
                ipv4Address: "5.6.7.8",
            },
            qosProfile: "QOS_E",
            duration: 3600,
        });

        await client.qod.deleteSession({
            sessionId: session.sessionId as string,
        });

        try {
            await client.qod.getSession({
                sessionId: session.sessionId as string,
            });
            expect(true).toBe(false);
        } catch (error) {
            expect(error).toBeDefined();
        }
    });
});
