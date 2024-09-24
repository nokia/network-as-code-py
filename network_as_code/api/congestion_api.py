# Copyright 2024 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import Optional

from network_as_code.api.utils import httpx_client

from ..errors import error_handler


class CongestionAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def fetch_congestion(self, device, start: Optional[str] = None, end: Optional[str] = None) -> dict:
        body = {
            "device": device.model_dump(mode='json', by_alias=True, exclude_none=True)
        }

        if start:
            body["start"] = start

        if end:
            body["end"] = end

        response = self.client.post(url="/query", json=body)

        error_handler(response)

        return response.json()

    def subscribe(
        self,
        device,
        notification_url: str,
        subscription_expire_time: str,
        notification_auth_token: Optional[str] = None,
    ) -> dict:
        body = {
            "device": device.model_dump(mode='json', by_alias=True, exclude_none=True),
            "webhook": {
                "notificationUrl": notification_url
            },
            "subscriptionExpireTime": subscription_expire_time
        }

        if notification_auth_token:
            body["webhook"]["notificationAuthToken"] = notification_auth_token

        response = self.client.post(url="/subscriptions", json=body)

        error_handler(response)

        return response.json()

    def delete_subscription(self, subscription_id):
        response = self.client.delete(url=f"/subscriptions/{subscription_id}")

        error_handler(response)

    def get_subscription(self, subscription_id: str):
        response = self.client.get(url=f"/subscriptions/{subscription_id}")

        error_handler(response)

        return response.json()

    def get_subscriptions(self):
        response = self.client.get(url="/subscriptions")

        error_handler(response)

        return response.json()
