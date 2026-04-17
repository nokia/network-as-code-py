import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("Congestion Insights", () => {
    const expirationDate = new Date(Date.now() + 5 * 60 * 1000);
    expirationDate.setMilliseconds(0);

    it("can create and delete a congestion subscription", async () => {
        const subscription = await client.congestionInsights.createSubscription({
            device: {
                phoneNumber: "+3670123456",
            },
            webhook: {
                notificationUrl: "https://example.com/notify",
                notificationAuthToken: "c8974e592c2fa383d4a3960714",
            },
            subscriptionExpireTime: expirationDate.toISOString(),
        });

        expect(subscription).toBeDefined();
        expect(subscription.subscriptionId).toBeDefined();

        await client.congestionInsights.deleteSubscription({
            resource_id: subscription.subscriptionId as string,
        });
    });

    it("can get a subscription by id", async () => {
        const subscription = await client.congestionInsights.createSubscription({
            device: {
                phoneNumber: "+3670123456",
            },
            webhook: {
                notificationUrl: "https://example.com/notify",
                notificationAuthToken: "c8974e592c2fa383d4a3960714",
            },
            subscriptionExpireTime: expirationDate.toISOString(),
        });

        const fetched = await client.congestionInsights.getSubscription({
            resource_id: subscription.subscriptionId as string,
        });

        expect(fetched.subscriptionId).toBe(subscription.subscriptionId);

        await client.congestionInsights.deleteSubscription({
            resource_id: subscription.subscriptionId as string,
        });
    });

    it("can list subscriptions", async () => {
        const subscriptions = await client.congestionInsights.listSubscriptions();
        expect(subscriptions).toBeDefined();
        expect(subscriptions instanceof Array).toBeTruthy();
    });

    it("can query congestion level for a device", async () => {
        const congestion = await client.congestionInsights.query({
            device: {
                phoneNumber: "+99999991000",
            },
        });

        expect(congestion).toBeDefined();
        expect(congestion instanceof Array).toBeTruthy();
    });
});
