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


from typing import Optional, Any

from network_as_code.api.utils import httpx_client

from ..errors import error_handler


class SimSwapAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def fetch_sim_swap_date(self, phone_number):
        body = {"phoneNumber": phone_number}

        response = self.client.post(url="/retrieve-date", json=body)

        error_handler(response)

        return response.json()

    def verify_sim_swap(self, phone_number: str, max_age: Optional[int]) -> bool:
        body: dict[str, Any] = {
            "phoneNumber": phone_number,
        }

        if max_age:
            body["maxAge"] = max_age

        response = self.client.post(url="/check", json=body)

        error_handler(response)

        return bool(response.json()['swapped'])
