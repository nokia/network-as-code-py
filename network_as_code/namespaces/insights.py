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
from typing import List, Union
from . import Namespace
from ..models.device import Device
from ..models.congestion import CongestionSubscription

class NetworkInsights(Namespace):
    """Gain insights from network analytics"""

    def get_congestion(self, device: Device, start: Union[datetime, str, None] = None, end: Union[datetime, str, None] = None) -> str:
        """Fetch the congestion level of the device"""
        start = start.isoformat() if isinstance(start, datetime) else start
        end = end.isoformat() if isinstance(end, datetime) else end

        return self.api.congestion.fetch_congestion(device, start=start, end=end)

    def subscribe_to_congestion_info(self, device: Device, notification_url: str) -> CongestionSubscription:
        json_data = self.api.congestion.subscribe(device, notification_url)

        return self._parse_congestion_subscription(json_data)

    def get_congestion_subscription(self, subscription_id: str) -> CongestionSubscription:
        json_data = self.api.congestion.get_subscription(subscription_id)

        return self._parse_congestion_subscription(json_data)

    def get_congestion_subscriptions(self) -> List[CongestionSubscription]:
        json_data = self.api.congestion.get_subscriptions()

        return list(map(lambda entry: self._parse_congestion_subscription(entry), json_data))

    def _parse_congestion_subscription(self, json_data) -> CongestionSubscription:
        return CongestionSubscription(
            api=self.api,
            id=json_data.get("subscriptionId"),
            starts_at=datetime.fromisoformat(json_data.get("startsAt")) if json_data.get("startsAt") else None,
            expires_at=datetime.fromisoformat(json_data.get("expiresAt")) if json_data.get("expiresAt") else None,
        )
