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

import httpx

from typing import Optional
import datetime

from ..errors import error_handler


def delete_none(_dict):
    """Delete None values recursively from all of the dictionaries"""
    for key, value in list(_dict.items()):
        if isinstance(value, dict):
            delete_none(value)
        elif value is None:
            del _dict[key]
        elif isinstance(value, list):
            for v_i in value:
                if isinstance(v_i, dict):
                    delete_none(v_i)

    return _dict


class DeviceStatusAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.client = httpx.Client(
            base_url=base_url,
            headers={
                "content-type": "application/json",
                "X-RapidAPI-Key": rapid_key,
                "X-RapidAPI-Host": rapid_host,
            },
        )

    def create_subscription(
        self,
        device,
        event_type: str,
        notification_url: str,
        notification_auth_token: str,
        max_number_of_reports: Optional[int] = None,
        subscription_expire_time: Optional[str] = None,
    ):
        assert device.network_access_id != "None"

        res = self.client.post(
            "/event-subscriptions",
            json=delete_none(
                {
                    "subscriptionDetail": {
                        "device": {
                            "phoneNumber": device.phone_number,
                            "networkAccessIdentifier": device.network_access_identifier,
                            "ipv4Address": {
                                "publicAddress": device.ipv4_address.public_address,
                                "privateAddress": device.ipv4_address.private_address,
                                "publicPort": device.ipv4_address.public_port,
                            }
                            if device.ipv4_address
                            else None,
                            "ipv6Address": device.ipv6_address,
                        },
                        "eventType": event_type,
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
        res = self.client.get(f"/event-subscriptions/{id}")

        error_handler(res)

        return res.json()

    def delete_subscription(self, id: str):
        res = self.client.delete(f"/event-subscriptions/{id}")

        error_handler(res)
