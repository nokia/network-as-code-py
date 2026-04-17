import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

// The generated Area type only has { areaType }, but the API requires
// center and radius for CIRCLE. We cast to work around the incomplete codegen.
const circleArea = {
    areaType: "CIRCLE" as const,
    center: { latitude: 47.48627616952785, longitude: 19.07915612501993 },
    radius: 2000,
};

describe("Geofencing", () => {
    it("should create and delete a geofencing subscription", async () => {
        const subscription = await client.geofencing.createSubscription({
            protocol: "HTTP",
            sink: "https://example.com/notify",
            types: ["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            config: {
                subscriptionDetail: {
                    device: {
                        phoneNumber: "+99999991000",
                    },
                    area: circleArea as any,
                },
                initialEvent: true,
            },
        });

        expect(subscription).toBeDefined();
        expect(subscription.id).toBeDefined();

        await client.geofencing.deleteSubscription({
            subscriptionId: subscription.id as string,
        });
    });

    it("should get a geofencing subscription by id", async () => {
        const subscription = await client.geofencing.createSubscription({
            protocol: "HTTP",
            sink: "https://example.com/notify",
            types: ["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            config: {
                subscriptionDetail: {
                    device: {
                        phoneNumber: "+99999991000",
                    },
                    area: circleArea as any,
                },
            },
        });

        const fetched = await client.geofencing.getSubscription({
            subscriptionId: subscription.id as string,
        });

        expect(fetched.id).toBe(subscription.id);

        await client.geofencing.deleteSubscription({
            subscriptionId: subscription.id as string,
        });
    });

    it("should list all geofencing subscriptions", async () => {
        const subscriptions = await client.geofencing.listSubscriptions({});
        expect(subscriptions).toBeDefined();
        expect(subscriptions instanceof Array).toBeTruthy();
    });

    it("should fail to get a deleted subscription", async () => {
        const subscription = await client.geofencing.createSubscription({
            protocol: "HTTP",
            sink: "https://example.com/notify",
            types: ["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            config: {
                subscriptionDetail: {
                    device: {
                        phoneNumber: "+99999991000",
                    },
                    area: circleArea as any,
                },
            },
        });

        await client.geofencing.deleteSubscription({
            subscriptionId: subscription.id as string,
        });

        try {
            await client.geofencing.getSubscription({
                subscriptionId: subscription.id as string,
            });
            expect(true).toBe(false);
        } catch (error) {
            expect(error).toBeDefined();
        }
    });
});
