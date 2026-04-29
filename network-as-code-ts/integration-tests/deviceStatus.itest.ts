import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("Device Status", () => {
    it("can poll device roaming status", async () => {
        const status = await client.deviceStatus.retrieveRoamingStatus({
            device: {
                phoneNumber: "+99999991000",
            },
        });

        expect(status).toBeDefined();
        expect(status.roaming).toBeDefined();
    });

    it("can poll device reachability status", async () => {
        const status = await client.deviceStatus.retrieveReachabilityStatus({
            device: {
                phoneNumber: "+99999991000",
            },
        });

        expect(status).toBeDefined();
        expect(status.reachable).toBeDefined();
    });

    it("can check connectivity", async () => {
        const status = await client.deviceStatus.checkConnectivity({
            device: {
                phoneNumber: "+99999991000",
            },
        });

        expect(status).toBeDefined();
        expect(status.connectivityStatus).toBeDefined();
    });

    it("can check roaming (v0)", async () => {
        const status = await client.deviceStatus.checkRoaming({
            device: {
                phoneNumber: "+99999991000",
            },
        });

        expect(status).toBeDefined();
        expect(status.roaming).toBeDefined();
    });

    it("can create and delete a roaming subscription", async () => {
        const subscription = await client.deviceStatus.createRoamingSubscription({
            protocol: "HTTP",
            sink: "https://example.com/notify",
            types: ["org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"],
            config: {
                subscriptionDetail: {
                    device: {
                        phoneNumber: "+99999991000",
                    },
                },
                initialEvent: true,
            },
        });

        expect(subscription.id).toBeDefined();

        await client.deviceStatus.deleteRoamingSubscription({
            subscriptionId: subscription.id as string,
        });
    });

    it("can create and delete a reachability subscription", async () => {
        const subscription = await client.deviceStatus.createReachabilitySubscription({
            protocol: "HTTP",
            sink: "https://example.com/notify",
            types: ["org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"],
            config: {
                subscriptionDetail: {
                    device: {
                        phoneNumber: "+99999991000",
                    },
                },
                initialEvent: true,
            },
        });

        expect(subscription.id).toBeDefined();

        await client.deviceStatus.deleteReachabilitySubscription({
            subscriptionId: subscription.id as string,
        });
    });

    it("can get a roaming subscription by id", async () => {
        const subscription = await client.deviceStatus.createRoamingSubscription({
            protocol: "HTTP",
            sink: "https://example.com/notify",
            types: ["org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"],
            config: {
                subscriptionDetail: {
                    device: {
                        phoneNumber: "+99999991000",
                    },
                },
                initialEvent: true,
            },
        });

        const fetched = await client.deviceStatus.getRoamingSubscription({
            subscriptionId: subscription.id as string,
        });

        expect(fetched.id).toBe(subscription.id);

        await client.deviceStatus.deleteRoamingSubscription({
            subscriptionId: subscription.id as string,
        });
    });

    it("can list subscriptions", async () => {
        const subscriptions = await client.deviceStatus.listSubscriptions();
        expect(subscriptions).toBeDefined();
        expect(subscriptions instanceof Array).toBeTruthy();
    });
});
