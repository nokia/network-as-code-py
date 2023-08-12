import httpx

from typing import Optional
import datetime

class DeviceStatusAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.rapid_key = rapid_key
        self.rapid_host = rapid_host
        self.client = httpx.Client(base_url=base_url, verify=False)   

    def create_subscription(self,
                            device,
                            event_type: str,
                            notification_url: str,
                            notification_auth_token: str,
                            max_number_of_reports: Optional[int] = None,
                            subscription_expire_time: Optional[datetime.datetime] = None):
        res = self.client.post(
            "/event-subscriptions",
            json={
                "subscriptionDetail": {
                    "device": {
                        "phoneNumber": device.phone_number,
                        "networkAccessIdentifier": device.network_access_id,
                        "ipv4Address": {
                            "publicAddress": device.ipv4_address.public_address,
                            "privateAddress": device.ipv4_address.private_address,
                            "publicPort": device.ipv4_address.public_port
                        },
                        "ipv6Address": device.ipv6_address
                    },
                    "eventType": event_type
                },
                "maxNumberOfReports": max_number_of_reports,
                "subscriptionExpireTime": subscription_expire_time,
                "webhook": {
                    "notificationUrl": notification_url,
                    "notificationAuthToken": notification_auth_token
                }
            }
        )

        res.raise_for_status()

        return res.json()

    def get_subscription(self, id: str):
        res = self.client.get("/event-subscriptions/", params={"id": id})

        res.raise_for_status()

        return res.json()

    def delete_subscription(self, id: str):
        res = self.client.delete("/event-subscriptions/", params={"id": id})

        res.raise_for_status()
