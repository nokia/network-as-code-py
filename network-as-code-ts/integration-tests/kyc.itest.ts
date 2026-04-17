import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("KYC Age Verification", () => {
    it("should verify age", async () => {
        const result = await client.kyc.verifyAge({
            phoneNumber: "+99999991000",
            ageThreshold: 18,
        });

        expect(result).toBeDefined();
    });

    it("should verify age with all optional params", async () => {
        const result = await client.kyc.verifyAge({
            phoneNumber: "+99999991000",
            ageThreshold: 18,
            idDocument: "66666666q",
            name: "Federica Sanchez Arjona",
            givenName: "Federica",
            familyName: "Sanchez Arjona",
            middleNames: "Sanchez",
            familyNameAtBirth: "YYYY",
            birthdate: "1978-08-22",
            email: "federicaSanchez.Arjona@example.com",
        });

        expect(result).toBeDefined();
    });
});

describe("KYC Match", () => {
    it("should match customer", async () => {
        const result = await client.kyc.match({
            phoneNumber: "+999999991000",
            idDocument: "66666666q",
            name: "Federica Sanchez Arjona",
            givenName: "Federica",
            familyName: "Sanchez Arjona",
            middleNames: "Sanchez",
            familyNameAtBirth: "YYYY",
            address: "Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
            streetName: "Nicolas Salmeron",
            streetNumber: "4",
            postalCode: "1028460",
            region: "Tokyo",
            locality: "ZZZZ",
            country: "JP",
            houseNumberExtension: "VVVV",
            birthdate: "1978-08-22",
            email: "abc@example.com",
            gender: "OTHER",
        });

        expect(result).toBeDefined();
        expect(result.idDocumentMatch).toBeDefined();
    });

    it("wrong phone number should return error", async () => {
        try {
            await client.kyc.match({
                phoneNumber: "+12345678",
                idDocument: "123456",
            });
            expect(true).toBe(false);
        } catch (error) {
            expect(error).toBeDefined();
        }
    });
});
