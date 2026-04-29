import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("SIM Swap", () => {
    it("should retrieve SIM swap date", async () => {
        const response = await client.simSwap.retrieveDate({
            phoneNumber: "+99999991000",
        });

        expect(response).toBeDefined();
        expect(response.latestSimChange).toBeTruthy();
    });

    it("should check SIM swap without max age", async () => {
        const response = await client.simSwap.check({
            phoneNumber: "+99999991000",
        });

        expect(response).toBeDefined();
        expect(response.swapped).toBe(true);
    });

    it("should check SIM swap with max age", async () => {
        const response = await client.simSwap.check({
            phoneNumber: "+99999991000",
            maxAge: 120,
        });

        expect(response).toBeDefined();
        expect(response.swapped).toBe(true);
    });

    it("should check SIM swap - True", async () => {
        const response = await client.simSwap.check({
            phoneNumber: "+99999991000",
            maxAge: 120,
        });

        expect(response.swapped).toBe(true);
    });

    it("should check SIM swap - False", async () => {
        const response = await client.simSwap.check({
            phoneNumber: "+99999991001",
            maxAge: 120,
        });

        expect(response.swapped).toBe(false);
    });
});
