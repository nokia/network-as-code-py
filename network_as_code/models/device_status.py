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
from typing import List, Optional, Union
from pydantic import BaseModel, ConfigDict, PrivateAttr

from network_as_code.api.utils import to_camel

from ..api import APIClient
from ..models.device import Device


class EventType(Enum):
    """
    Enum class containing the string constant values for the different supported event types.
    """

    ROAMING_STATUS= "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-status"
    ROAMING_ON= "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"
    ROAMING_OFF= "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-off"
    ROAMING_CHANGE_COUNTRY= "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-change-country"
    REACHABILITY_DATA= "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
    REACHABILITY_SMS= "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
    REACHABILITY_DISCONNECTED= "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-disconnected"

# pylint: disable=duplicate-code
class AccessTokenCredential(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    credential_type: str = "ACCESSTOKEN"
    access_token: str
    access_token_expires_utc: Union[datetime, str]
    access_token_type: str

class PlainCredential(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    credential_type: str = "PLAIN"
    identifier: str
    secret: str
# pylint: enable=duplicate-code

class EventSubscription(BaseModel):
    """
    A class representing the `EventSubscription` model.

    #### Private Attributes:
        _api(APIClient): An API client object.

    #### Public Attributes:
        id (str): It represents the subscription identifier.
        max_num_of_reports (int): Number of notifications until the subscription is available
        event_type (List[str]): The status type you want to check, which can be reachability or roaming.
        sink (str): Notification URL for session-related events.
        sink_credential (optional): Authorization token for notification sending.
        device (Device): Identifier of the device
        starts_at (optional): It represents when this subscription started.
        expires_at (optional): It represents when this subscription should expire.
        status (optional): Current status of the subscription.
    #### Public Methods:
        delete (None): Deletes device status event subscription.
    """

    id: str = ''
    _api: APIClient = PrivateAttr()
    protocol: Optional[str] = None
    max_num_of_reports: Optional[int] = None
    event_type: List[str]
    sink: str
    device: Device
    starts_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    sink_credential: Union[PlainCredential, AccessTokenCredential, None] = None
    status: Optional[str] = None

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

class ReachabilitySubscription(EventSubscription):

    def __init__(self, *args, **kwargs): # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)

    def delete(self) -> None:
        """Delete device reachability status"""

        self._api.reachability_status.delete_subscription(self.id)

class RoamingSubscription(EventSubscription):

    def __init__(self, *args, **kwargs): # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)

    def delete(self) -> None:
        """Delete device roaming status"""

        self._api.roaming_status.delete_subscription(self.id)
