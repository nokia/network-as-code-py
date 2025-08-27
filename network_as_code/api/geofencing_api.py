# Copyright 2025 Nokia
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
from network_as_code.api.utils import httpx_client
from ..errors import error_handler

class GeofencingAPI:

    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def create_subscription(
        self,
        device,
        sink: str,
        typelist: List[str],
        latitude: float,
        longitude: float,
        radius: Union[int, float],
        sink_credential: Any = None,
        subscription_expire_time: Union[datetime , str, None] = None,
        subscription_max_events: Optional[int] = None,
        initial_event: Optional[bool] = None
    ):

        body: dict = {
            "protocol": "HTTP",
            "sink": sink,
            "types": typelist,
            "config": {
                "subscriptionDetail": {
                    "device": device.model_dump(mode='json', by_alias=True, exclude_none=True),
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": latitude,
                            "longitude": longitude
                        },
                        "radius": radius
                    }
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

        response = self.client.post(url="/subscriptions", json=body)

        error_handler(response)

        return response.json()

    def delete_subscription(self,subscription_id):
        resp = self.client.delete(url=f"/subscriptions/{subscription_id}")

        error_handler(resp)

    def get_subscription(self, subscription_id: str):
        resp = self.client.get(url=f"/subscriptions/{subscription_id}")

        error_handler(resp)

        return resp.json()

    def get_subscriptions(self):
        resp = self.client.get(url="/subscriptions")

        error_handler(resp)

        return resp.json()
