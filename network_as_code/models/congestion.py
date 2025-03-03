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
from typing import Optional
from pydantic import BaseModel, PrivateAttr
from network_as_code.api.client import APIClient



class Congestion(BaseModel):
    """
    A class representing the `Congestion` model.

    #### Public Attributes:
            level (str): Congestion level experienced by the device ranging from "None", "Low", "Medium" and "High"
            start (datetime): Start timestamp for retrieving congestion data.
            stop (datetime): End timestamp for retrieving congestion data.
            confidence (Optional[int]): Level of confidence when dealing with a congestion level prediction, 
            ranging from 0 to 100.
    """
    level: str
    start: datetime
    stop: datetime
    confidence: Optional[int]

    @classmethod
    def from_json(cls, json) -> "Congestion":
        level = json["congestionLevel"]
        confidence = json.get("confidenceLevel")
        start = datetime.fromisoformat(json["timeIntervalStart"])
        stop = datetime.fromisoformat(json["timeIntervalStop"])

        return cls(level=level, confidence=confidence, start=start, stop=stop)

class CongestionSubscription(BaseModel):
    """
    A class representing the `CongestionSubscription` model.

    #### Private Attributes:
        _api(APIClient): An API client object.

    #### Public Attributes:
        id (optional): It represents the subscription identifier.
        starts_at (optional): It represents when this subscription started.
        expires_at (optional): It represents when this subscription should expire.
    #### Public Methods:
        delete (None): Delete congestion insights subscription.
    """
    id: Optional[str] = None
    _api: APIClient = PrivateAttr()
    starts_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None

    def __init__(self, api: APIClient, **data):
        super().__init__(**data)
        self._api = api

    def delete(self):
        """Delete congestion insights subscription"""
        self._api.congestion.delete_subscription(self.id)
