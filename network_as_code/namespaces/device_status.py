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
from typing import List, Union, Optional, Any

from . import Namespace
from ..models.device import Device
from ..models.device_status import (
    PlainCredential,
    AccessTokenCredential,
    EventSubscription,
    ReachabilitySubscription,
    RoamingSubscription,
    EventType
    )


class DeviceStatus(Namespace):
    """Representation of the status of a device.

    Through this class many of the parameters of a
    device status can be configured and managed.
    """

    def subscribe(
        self,
        event_type: Union[List[EventType], List[str]],
        sink: str,
        device: Device,
        max_num_of_reports: Optional[int] = None,
        sink_credential: Union[PlainCredential, AccessTokenCredential, None] = None,
        subscription_expire_time: Union[datetime, str, None] = None,
        initial_event: Optional[bool] = None
    ) -> EventSubscription:
        """Create subscription for device reachabilty or roaming status.

        Args:
            event_type (Union[EventType, str]): Event type of the subscription.
            sink (str): Notification URL for session-related events.
            sink_credential (optional): Authorization token for notification sending.
            device (Device): Identifier of the device.
            max_num_of_reports (Optional[int]): Number of notifications until the subscription is available.
            initial_event (Optional[bool]): Set to `True` to get an event as soon as the subscription is created 
            and current situation reflects event request.
            subscription_expire_time (Union[datetime, str, None]): The expiry time of the subscription. 
            Either a datetime object or ISO formatted date string

        Returns: EventSubscription
        """

        # Handle conversion
        if isinstance(subscription_expire_time, datetime):
            subscription_expire_time = subscription_expire_time.isoformat()

        typelist = []
        for item in event_type:
            if isinstance(item, EventType):
                typelist.append(item.value)
            else:
                typelist.append(item)
        if self.__is_roaming(typelist):
            api_type: Any = self.api.roaming_status
            subscription_type: Any = RoamingSubscription
        else:
            api_type = self.api.reachability_status
            subscription_type = ReachabilitySubscription

        connectivity_data = api_type.create_subscription(
            device,
            sink,
            typelist,
            sink_credential,
            subscription_expire_time,
            max_num_of_reports,
            initial_event
        )
        connectivity_subscription = subscription_type(
            api=self.api,
            max_num_of_reports=max_num_of_reports,
            event_type = typelist,
            sink=sink,
            device=device,
            sink_credential=sink_credential,
            starts_at=(connectivity_data["startsAt"] if "startsAt" in connectivity_data else None),
            expires_at=(
                connectivity_data["expiresAt"] if "expiresAt" in connectivity_data else None
            ),
        )

        connectivity_subscription.id = connectivity_data["id"]

        return connectivity_subscription

    def get_reachability_subscription(self, id: str) -> EventSubscription:
        """Retrieve a single Device Status reachability event subscription by ID

        #### Args:
            id (str): Resource ID

        #### Example:
            ```python
            subscription = client.device_status.get_reachability_subscription(id="some-subscription-id")
            ```
        """

        connectivity_data = self.api.reachability_status.get_subscription(id)

        return self.__parse_event_subscription(connectivity_data)

    def get_roaming_subscription(self, id: str) -> EventSubscription:
        """Retrieve a single Device Status roaming event subscription by ID

        #### Args:
            id (str): Resource ID

        #### Example:
            ```python
            subscription = client.device_status.get_roaming_subscription(id="some-subscription-id")
            ```
        """

        connectivity_data = self.api.roaming_status.get_subscription(id)

        return self.__parse_event_subscription(connectivity_data)

    def get_subscriptions(self) -> List[EventSubscription]:
        """Retrieve list of active Device Status Subscriptions

        #### Example:
             '''python
             subscriptions = client.device_status.get_subscriptions()
             '''

        Returns: List[EventSubscription]
        """
        reachability_json = self.api.reachability_status.get_subscriptions()
        roaming_json = self.api.roaming_status.get_subscriptions()
        subscriptions = reachability_json + roaming_json

        return list(map(self.__parse_event_subscription, subscriptions))

    def __is_roaming(self, types: List) -> bool:
        return types[0] in (
            EventType.ROAMING_CHANGE_COUNTRY.value,
            EventType.ROAMING_OFF.value,
            EventType.ROAMING_ON.value,
            EventType.ROAMING_STATUS.value
            )

    def __parse_event_subscription(self, data: dict) -> EventSubscription:
        device_data = data["config"].get("subscriptionDetail").get("device")

        device = Device.convert_to_device_model(self.api, device_data)

        if self.__is_roaming(data["types"]):
            return RoamingSubscription(
                id=data["id"],
                api=self.api,
                max_num_of_reports=data["config"].get("subscriptionMaxEvents"),
                event_type=data["types"],
                sink=data["sink"],
                device=device,
                status=data["status"]
            )
        return ReachabilitySubscription(
                id=data["id"],
                api=self.api,
                max_num_of_reports=data["config"].get("subscriptionMaxEvents"),
                event_type=data["types"],
                sink=data["sink"],
                device=device,
                status=data["status"]
            )
