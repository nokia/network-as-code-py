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
    radius: 10_000,
};

describe("Location retrieval and verification", () => {
    it("should retrieve location of a test device", async () => {
        const location = await client.location.retrieve({
            device: {
                phoneNumber: "+36719991001",
            },
            maxAge: 60,
        });

        expect(location).toBeDefined();
        expect(location.area).toBeDefined();
    });

    it("should verify location of a test device (v0)", async () => {
        const result = await client.location.verify({
            device: {
                phoneNumber: "+99999991000",
            },
            area: circleArea as any,
        });

        expect(result).toBeDefined();
        expect(result.verificationResult).toBeDefined();
    });

    it("should verify location of a test device (v1)", async () => {
        const result = await client.location.verifyV1({
            device: {
                phoneNumber: "+99999991000",
            },
            area: circleArea as any,
        });

        expect(result).toBeDefined();
        expect(result.verificationResult).toBeDefined();
    });
});
