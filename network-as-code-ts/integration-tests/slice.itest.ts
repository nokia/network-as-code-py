import { beforeAll, describe, expect, it } from "@jest/globals";
import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";
import { configureClient } from "./configClient.js";

let client: NetworkAsCodeApiClient;

beforeAll(() => {
    client = configureClient();
});

describe("Slicing", () => {
    it("should create and delete a slice", async () => {
        const random = Math.floor(Math.random() * 1000) + 1;

        const result = await client.slice.createSlice({
            networkIdentifier: { mcc: "236", mnc: "30" },
            sliceInfo: { serviceType: 1, differentiator: "444444" },
            notificationUrl: "https://notify.me/here",
            name: `slice${random}`,
            notificationAuthToken: "my-token",
        });

        expect(result).toBeDefined();
        expect(result.csi_id).toBeDefined();

        await client.slice.deleteSlice({
            id: result.name,
        });
    });

    it("should create a slice with optional args", async () => {
        const random = Math.floor(Math.random() * 1000) + 1;

        const result = await client.slice.createSlice({
            networkIdentifier: { mcc: "236", mnc: "30" },
            sliceInfo: { serviceType: 1, differentiator: "444444" },
            notificationUrl: "https://notify.me/here",
            name: `slice${random}`,
            notificationAuthToken: "my-token",
            areaOfService: {
                polygon: [
                    { lat: 47.344, lon: 104.349 },
                    { lat: 35.344, lon: 76.619 },
                    { lat: 12.344, lon: 142.541 },
                    { lat: 19.43, lon: 103.53 },
                ],
            },
            sliceDownlinkThroughput: { guaranteed: 3415, maximum: 1234324 },
            sliceUplinkThroughput: { guaranteed: 3415, maximum: 1234324 },
            deviceUplinkThroughput: { guaranteed: 3415, maximum: 1234324 },
            deviceDownlinkThroughput: { guaranteed: 3415, maximum: 1234324 },
            maxDataConnections: 10,
            maxDevices: 5,
        });

        expect(result).toBeDefined();

        await client.slice.deleteSlice({
            id: result.name,
        });
    });

    it("should get a slice by name", async () => {
        const random = Math.floor(Math.random() * 1000) + 1;
        const name = `slice${random}`;

        const created = await client.slice.createSlice({
            networkIdentifier: { mcc: "236", mnc: "30" },
            sliceInfo: { serviceType: 1, differentiator: "444444" },
            notificationUrl: "https://notify.me/here",
            name,
            notificationAuthToken: "my-token",
        });

        const fetched = await client.slice.getSlice({ id: created.name });
        expect(fetched).toBeDefined();

        await client.slice.deleteSlice({ id: created.name });
    });

    it("should list slices", async () => {
        const slices = await client.slice.listSlices();
        expect(slices).toBeDefined();
        expect(slices instanceof Array).toBeTruthy();
    });
});
