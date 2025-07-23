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
from enum import Enum
from typing import Optional, List, Union
from pydantic import BaseModel, PrivateAttr, Field
from network_as_code.api.client import APIClient

class EventType(Enum):
    """
    Enum class containing the string constant values for the different supported event types.
    """

    AREA_ENTERED = "org.camaraproject.geofencing-subscriptions.v0.area-entered"
    AREA_LEFT = "org.camaraproject.geofencing-subscriptions.v0.area-left"

class AccessTokenCredential(BaseModel):
    credential_type: str = Field(default="ACCESSTOKEN", serialization_alias="credentialType")
    access_token: str = Field(..., serialization_alias="accessToken")
    access_token_expires_utc: Union[datetime, str] = Field(..., serialization_alias="accessTokenExpiresUtc")
    access_token_type: str = Field(..., serialization_alias="accessTokenType")

class PlainCredential(BaseModel):
    credential_type: str = Field(default="PLAIN", serialization_alias="credentialType")
    identifier: str = Field(..., serialization_alias="identifier")
    secret: str = Field(..., serialization_alias="secret")

class GeofencingSubscription(BaseModel):
    event_subscription_id: str
    _api: APIClient = PrivateAttr()
    protocol: Optional[str] = None
    sink: str
    types: List[str]
    latitude: float
    longitude: float
    radius: Union[int, float]
    starts_at: datetime
    sink_credential: Union[PlainCredential, AccessTokenCredential, None] = None
    def __init__(self, api: APIClient, **data):
        super().__init__(**data)
        self._api = api

    def delete(self):
        """Delete Geofencing subscription"""
        self._api.geofencing.delete_subscription(self.event_subscription_id)

    @staticmethod
    def from_json(api: APIClient, json_data) -> 'GeofencingSubscription':
        starts_at = (
            datetime.fromisoformat(json_data["startsAt"])
            if json_data.get("startsAt", False)
            else None
        )
        return GeofencingSubscription(
            event_subscription_id = json_data["id"],
            api=api,
            sink=json_data["sink"],
            types=json_data["types"],
            latitude =json_data["config"].get("subscriptionDetail").get("area").get("center").get("latitude"),
            longitude=json_data["config"].get("subscriptionDetail").get("area").get("center").get("longitude"),
            radius=json_data["config"].get("subscriptionDetail").get("area").get("radius"),
            starts_at=starts_at,
        )
