import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";

export const configureClient = (): NetworkAsCodeApiClient => {
    const apiKey = process.env["NAC_TOKEN"] as string;

    const rapidapiHost = process.env["RAPIDAPI_HOST"] ?? "network-as-code.nokia.rapidapi.com";

    const client = new NetworkAsCodeApiClient({
        apiKey,
        rapidapiHost,
    });

    return client;
};

export const configureNotificationServerUrl = (): string => {
    const notificationUrl = `${process.env["SDK_NOTIFICATION_SERVER_URL"]}typescript`;
    return notificationUrl;
};
