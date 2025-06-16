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
from typing import List, Union, Optional
from . import Namespace
from ..models.device import Device
from ..models.congestion import CongestionSubscription


class NetworkInsights(Namespace):
    """Gain insights from network analytics"""

    def subscribe_to_congestion_info(
        self,
        device: Device,
        notification_url: str,
        subscription_expire_time: Union[datetime, str],
        notification_auth_token: Optional[str] = None,
    ) -> CongestionSubscription:
        """Subscribe to congestion notifications

        #### Args:
             device (Device): device which may be affected by congestion
             notification_url (str): server to be notified on change in congestion
             subscription_expire_time (Union[datetime, str]): when this subscription should expire
             notification_auth_token (Optional[str]): Token that will be sent by NaC server in the notification
        #### Returns:
             Subscription object"""
        subscription_expire_time = (
            subscription_expire_time.isoformat()
            if isinstance(subscription_expire_time, datetime)
            else subscription_expire_time
        )

        json_data = self.api.congestion.subscribe(
            device, notification_url, subscription_expire_time, notification_auth_token
        )

        return self._parse_congestion_subscription(json_data)

    def get_congestion_subscription(self, subscription_id: str) -> CongestionSubscription:
        """Retrieve an active congestion subscription by id

        #### Args:
             subscription_id (str): the ID of the congestion subscription
        #### Returns:
             Subscription object"""
        json_data = self.api.congestion.get_subscription(subscription_id)

        return self._parse_congestion_subscription(json_data)

    def get_congestion_subscriptions(self) -> List[CongestionSubscription]:
        """Retrieve list of all active congestion subscriptions

        #### Returns:
             List of Subscription objects"""

        json_data = self.api.congestion.get_subscriptions()

        return list(map(self._parse_congestion_subscription, json_data))

    def _parse_congestion_subscription(self, json_data) -> CongestionSubscription:
        return CongestionSubscription(
            api=self.api,
            id=json_data.get("subscriptionId"),
            starts_at=(
                datetime.fromisoformat(json_data.get("startedAt"))
                if json_data.get("startedAt")
                else None
            ),
            expires_at=(
                datetime.fromisoformat(json_data.get("expiresAt"))
                if json_data.get("expiresAt")
                else None
            )
        )
