import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("Call Forwarding Signal", () => {
    it("should check unconditional call forwarding", async () => {
        const result = await client.callForwardingSignal.retrieveUnconditionalCallForwarding({
            phoneNumber: "+99999991111",
        });

        expect(result).toBeDefined();
        expect(result.active).toBeDefined();
    });

    it("should retrieve call forwarding services", async () => {
        const result = await client.callForwardingSignal.retrieveCallForwarding({
            phoneNumber: "+999999991111",
        });

        expect(result).toBeDefined();
        expect(result instanceof Array).toBeTruthy();
    });
});
