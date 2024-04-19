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

from datetime import datetime
from pydantic import BaseModel, PrivateAttr
from typing import Optional
from network_as_code.api.client import APIClient

from network_as_code.models.device import Device

class CongestionSubscription(BaseModel):
    id: Optional[str]
    _api: APIClient = PrivateAttr()
    starts_at: Optional[datetime]
    expires_at: Optional[datetime]

    def __init__(self, api: APIClient, **data):
        super().__init__(**data)
        self._api = api

    def delete(self):
        self._api.congestion.delete_subscription(self.id)
