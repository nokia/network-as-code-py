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

from .utils import httpx_client
from ..errors import error_handler

class KYCMatchAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def match_customer(self, body: dict):

        response = self.client.post("/match", json=body)

        error_handler(response)

        return response.json()

class KYCAgeAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def verify_age(self, body: dict):

        response = self.client.post("/verify", json=body)

        error_handler(response)

        return response.json()

class KYCTenureAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def check_tenure(self, body: dict):

        response = self.client.post("/check-tenure", json=body)

        error_handler(response)

        return response.json()

class KYCFillInAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str):
        self.client = httpx_client(base_url, rapid_key, rapid_host)

    def request_customer_info(self, phone_number: str):
        body: dict = {
            "phoneNumber": phone_number
        }

        response = self.client.post("/fill-in", json=body)

        error_handler(response)

        return response.json()
