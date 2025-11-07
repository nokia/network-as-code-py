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

from datetime import datetime
from typing import List, Union, Optional, Any

from ..errors import error_handler
from .utils import httpx_client


class DeviceStatus:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def create_subscription(
        self,
        device,
        sink: str,
        event_type: List[str],
        sink_credential: Any = None,
        subscription_expire_time: Union[datetime , str, None] = None,
        subscription_max_events: Optional[int] = None,
        initial_event: Optional[bool] = None
    ):
        assert device.network_access_id != "None"

        body: dict = {
            "protocol": "HTTP",
            "sink": sink,
            "types": event_type,
            "config": {
                "subscriptionDetail": {
                    "device": device.model_dump(mode='json', by_alias=True, exclude_none=True)
                }
            }
        }
        if sink_credential:
            body["sinkCredential"] = {
                **sink_credential.model_dump(mode='json', by_alias=True)
            }

        if subscription_expire_time:
            body["config"]["subscriptionExpireTime"] = subscription_expire_time

        if subscription_max_events:
            body["config"]["subscriptionMaxEvents"] = subscription_max_events

        if initial_event is not None:
            body["config"]["initialEvent"] = initial_event

        res = self.client.post(url="/subscriptions", json=body)

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

class ReachabilityAPI(DeviceStatus):

    def get_reachability(self, device: dict):
        status_url = str(self.client.base_url).replace(
            "/device-reachability-status-subscriptions/v0.7/",
            "/device-reachability-status/v1")
        res = self.client.post(f"{status_url}/retrieve", json={"device": device})

        error_handler(res)

        return res.json()

class RoamingAPI(DeviceStatus):

    def get_roaming(self, device: dict):
        status_url = str(self.client.base_url).replace(
            "/device-roaming-status-subscriptions/v0.7/",
            "/device-roaming-status/v1")
        res = self.client.post(f"{status_url}/retrieve", json={"device": device})

        error_handler(res)

        return res.json()