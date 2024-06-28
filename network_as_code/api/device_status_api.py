# Copyright 2023 Nokia
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


from ..errors import error_handler
from .utils import delete_none, httpx_client




class DeviceStatusAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.client = httpx_client(base_url, rapid_key, rapid_host)


    def create_subscription(
        self,
        device,
        event_type: str,
        notification_url: str,
        notification_auth_token: Optional[str],
        max_number_of_reports: Optional[int] = None,
        subscription_expire_time: Optional[str] = None,
    ):
        assert device.network_access_id != "None"

        res = self.client.post(
            "/subscriptions",
            json=delete_none(
                {
                    "subscriptionDetail": {
                        "device": device.model_dump(mode='json', by_alias=True),
                        "type": event_type,
                    },
                    "maxNumberOfReports": max_number_of_reports,
                    "subscriptionExpireTime": subscription_expire_time,
                    "webhook": {
                        "notificationUrl": notification_url,
                        "notificationAuthToken": notification_auth_token,
                    },
                }
            ),
        )
        error_handler(res)

        return res.json()

    def get_subscription(self, id: str):
        res = self.client.get(f"/subscriptions/{id}")

        error_handler(res)

        return res.json()

    def get_subscriptions(self):
        res = self.client.get("/subscriptions")

        error_handler(res)

        return res.json()

    def delete_subscription(self, id: str):
        res = self.client.delete(f"/subscriptions/{id}")

        error_handler(res)

    def get_connectivity(self, device: dict):
        res = self.client.post("/connectivity", json={"device": device})

        error_handler(res)

        return res.json()

    def get_roaming(self, device: dict):
        res = self.client.post("/roaming", json={"device": device})

        error_handler(res)

        return res.json()
