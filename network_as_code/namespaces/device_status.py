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

from typing import List
import math
from . import Namespace
from ..models.device import Device, DeviceIpv4Addr
from ..models.device_status import EventSubscription

from urllib.error import HTTPError
from pydantic import ValidationError
from typing import Optional


class Connectivity(Namespace):
    """Representation of the status of a device.

    Through this class many of the parameters of a
    device status can be configured and managed.
    """

    def subscribe(
        self,
        event_type: str,
        notification_url: str,
        device: Device,
        max_num_of_reports: Optional[int] = None,
        notification_auth_token: Optional[str] = None,
        subscription_expire_time: Optional[str] = None,
    ) -> EventSubscription:
        """Create subscription for device connectivity status.

        Args:
            event_type (str): Event type of the subscription.
            max_num_of_reports (int): Number of notifications until the subscription is available
            notification_url (str): Notification URL for session-related events.
            notification_auth_token (optional): Authorization token for notification sending.
            device (Device): Identifier of the device
            subscription_expire_time (Optional[str]): The expiry time of the subscription.
        """

        connectivity_subscription = EventSubscription(
            api=self.api,
            max_num_of_reports=max_num_of_reports,
            notification_url=notification_url,
            notification_auth_token=notification_auth_token,
            device=device,
        )

        # Error Case: Creating Connectivity Subscription
        try:
            connectivity_data = self.api.devicestatus.create_subscription(
                device,
                event_type,
                notification_url,
                notification_auth_token,
                max_num_of_reports,
                subscription_expire_time,
            )
            connectivity_subscription.id = connectivity_data["subscriptionId"]

        except HTTPError as e:
            if e.code == 403:
                raise AuthenticationException(e)
            elif e.code == 404:
                raise DeviceNotFound(e)
            elif e.code >= 500:
                raise ServiceError(e)
        except ValidationError as e:
            raise InvalidParameter(e)

        return connectivity_subscription

    def get_subscription(self, id: str) -> EventSubscription:
        """Retrieve a single Device Status event subscription by ID

        #### Args:
            id (str): Resource ID

        #### Example:
            ```python
            subscription = client.connectivity.get_subscription(id="some-subscription-id")
            ```
        """

        connectivity_data = self.api.devicestatus.get_subscription(id)

        return self.__parse_event_subscription(connectivity_data)

    def get_subscriptions(self) -> List[EventSubscription]:
        """Retrieve list of active Device Status subscriptions

        #### Example:
             '''python
             subscriptions = client.connectivity.get_subscriptions()
             '''
        """
        json = self.api.devicestatus.get_subscriptions()

        return list(map(lambda subscription: self.__parse_event_subscription(subscription), json))

    def __parse_event_subscription(self, data: dict) -> EventSubscription:
        device_data = data["subscriptionDetail"]["device"]

        device = Device(api=self.api)

        device.network_access_identifier = device_data.get("networkAccessIdentifier")

        device.phone_number = device_data.get("phoneNumber")

        device.ipv6_address = device_data.get("ipv6Address")

        if "ipv4Address" in device_data:
            device.ipv4_address = DeviceIpv4Addr(
                public_address=device_data["ipv4Address"].get("publicAddress"),
                private_address=device_data["ipv4Address"].get("privateAddress"),
                public_port=device_data["ipv4Address"].get("publicPort")
            )

        return EventSubscription(
            id=data["subscriptionId"],
            api=self.api,
            max_num_of_reports=data.get("maxNumberOfReports"),
            notification_url=data["webhook"].get("notificationUrl"),
            notification_auth_token=data["webhook"].get("notificationAuthToken"),
            device=device,
        )
