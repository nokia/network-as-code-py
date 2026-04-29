import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("Number Recycling", () => {
    it("should return a boolean result", async () => {
        const result = await client.numberRecycling.check({
            phoneNumber: "+99999991000",
            specifiedDate: "2024-10-31",
        });

        expect(result).toBeDefined();
        expect(typeof result.phoneNumberRecycled).toBe("boolean");
    });

    it("should indicate the number has been recycled", async () => {
        // A date well in the past should indicate the number has been recycled
        const result = await client.numberRecycling.check({
            phoneNumber: "+99999991000",
            specifiedDate: "2020-01-01",
        });

        expect(result.phoneNumberRecycled).toBe(true);
    });

    it("should indicate the number has not been recycled", async () => {
        // A very recent date should indicate no recycling has occurred
        const result = await client.numberRecycling.check({
            phoneNumber: "+99999991001",
            specifiedDate: "2020-01-01",
        });

        expect(result.phoneNumberRecycled).toBe(false);
    });

    it("should throw an error for an invalid phone number", async () => {
        try {
            await client.numberRecycling.check({
                phoneNumber: "+12345678",
                specifiedDate: "2024-10-31",
            });
            expect(true).toBe(false);
        } catch (error) {
            expect(error).toBeDefined();
        }
    });
});
