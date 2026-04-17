import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("Device Swap", () => {
    it("should retrieve device swap date", async () => {
        const response = await client.deviceSwap.retrieveDate({
            phoneNumber: "+99999991000",
        });

        expect(response).toBeDefined();
        expect(response.latestDeviceChange).toBeTruthy();
    });

    it("should check device swap without max age", async () => {
        const response = await client.deviceSwap.check({
            phoneNumber: "+99999991000",
        });

        expect(response).toBeDefined();
        expect(response.swapped).toBe(true);
    });

    it("should check device swap with max age", async () => {
        const response = await client.deviceSwap.check({
            phoneNumber: "+99999991000",
            maxAge: 250,
        });

        expect(response).toBeDefined();
        expect(response.swapped).toBe(true);
    });

    it("should check device swap - False", async () => {
        const response = await client.deviceSwap.check({
            phoneNumber: "+99999991001",
            maxAge: 120,
        });

        expect(response.swapped).toBe(false);
    });
});
