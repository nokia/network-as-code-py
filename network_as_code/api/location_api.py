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

from typing import cast

from network_as_code.api.utils import httpx_client

from ..errors import error_handler



class LocationVerifyAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def verify_location(self, latitude, longitude, device, radius, max_age=60):
        body = {
            "device": device.model_dump(mode='json', by_alias=True, exclude_none=True),
            "area": {
                "areaType": "CIRCLE",
                "center": {"latitude": latitude, "longitude": longitude},
                "radius": radius,
            },
        }

        if max_age:
            body["maxAge"] = cast(int, max_age)

        response = self.client.post(url="/verify", json=body)

        error_handler(response)

        return response.json()


class LocationRetrievalAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def get_location(self, device, max_age=60):
        body = {"device": device.model_dump(mode='json', by_alias=True, exclude_none=True)}

        if max_age:
            body["maxAge"] = cast(int, max_age)

        response = self.client.post(url="/retrieve", json=body)

        error_handler(response)

        return response.json()
