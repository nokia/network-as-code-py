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
from enum import Enum
from typing import Optional
from pydantic import BaseModel, PrivateAttr

from ..api import APIClient
from ..models.device import Device


class EventType(Enum):
    """
    Enum class containing the string constant values for the different supported event types.
    """

    CONNECTIVITY_DATA = "org.camaraproject.device-status.v0.connectivity-data"
    CONNECTIVITY_SMS = "org.camaraproject.device-status.v0.connectivity-sms"
    CONNECTIVITY_DISCONNECTED = "org.camaraproject.device-status.v0.connectivity-disconnected"
    ROAMING_STATUS = "org.camaraproject.device-status.v0.roaming-status"
    ROAMING_ON = "org.camaraproject.device-status.v0.roaming-on"
    ROAMING_OFF = "org.camaraproject.device-status.v0.roaming-off"
    ROAMING_CHANGE_COUNTRY = "org.camaraproject.device-status.v0.roaming-change-country"


class EventSubscription(BaseModel):
    """
    A class representing the `ConnectivitySubscription` model.

    #### Private Attributes:
        _api(APIClient): An API client object.

    #### Public Attributes:
        id (str): It represents the subscription identifier.
        max_num_of_reports (str): Number of notifications until the subscription is available
        event_type (str): The status type you want to check, which can be connectivity or roaming.
        notification_url (str): Notification URL for session-related events.
        notification_auth_token (optional): Authorization token for notification sending.
        device (Device): Identifier of the device
        starts_at (optional): It represents when this subscription started.
        expires_at (optional): It represents when this subscription should expire.
    #### Public Methods:
        delete (None): Deletes device connectivity status subscription.
    """

    id: str = ''
    _api: APIClient = PrivateAttr()
    max_num_of_reports: Optional[int] = None
    event_type: str
    notification_url: str
    notification_auth_token: Optional[str] = None
    device: Device
    starts_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

    def delete(self) -> None:
        """Delete device connectivity status"""

        # Error Case: Delete connectivity status
        self._api.devicestatus.delete_subscription(self.id)
