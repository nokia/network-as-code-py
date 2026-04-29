import "dotenv/config";
import { NetworkAsCodeApiClient } from "../network_as_code/Client.js";

export const configureClient = (): NetworkAsCodeApiClient => {
    const apiKey = process.env["NAC_TOKEN"] as string;

    const client = new NetworkAsCodeApiClient({
        apiKey,
        rapidapiHost: "network-as-code.nokia.rapidapi.com",
    });

    return client;
};

export const configureNotificationServerUrl = (): string => {
    const notificationUrl = `${process.env["SDK_NOTIFICATION_SERVER_URL"]}typescript`;
    return notificationUrl;
};
