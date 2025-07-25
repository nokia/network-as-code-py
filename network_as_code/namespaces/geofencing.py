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

from typing import List, Union, Optional
from datetime import datetime
from . import Namespace
from ..models.device import Device
from ..models.geofencing import GeofencingSubscription, PlainCredential, AccessTokenCredential, EventType

class Geofencing(Namespace):

    def subscribe(
        self, device: Device,
        sink: str,
        types: Union[List[EventType] | List[str]],
        latitude: float,
        longitude: float,
        radius: Union[int, float],
        sink_credential: Union[PlainCredential, AccessTokenCredential, None] = None,
        subscription_expire_time: Union[datetime , str, None] = None,
        subscription_max_events: Optional[int] = None,
        initial_event: Optional[bool] = None,
    ) -> GeofencingSubscription:

        subscription_expire_time = (
            subscription_expire_time.isoformat()
            if isinstance(subscription_expire_time, datetime)
            else subscription_expire_time
        )

        typelist = []
        for item in types:
            if isinstance(item, EventType):
                typelist.append(item.value)
            else:
                typelist.append(item)

        json_data = self.api.geofencing.create_subscription(
            device,
            sink,
            typelist,
            latitude,
            longitude,
            radius,
            sink_credential,
            subscription_expire_time,
            subscription_max_events,
            initial_event,
        )

        return GeofencingSubscription.from_json(self.api, json_data)

    def get(self, subscription_id:str) -> GeofencingSubscription:

        json_data = self.api.geofencing.get_subscription(subscription_id)

        return GeofencingSubscription.from_json(self.api, json_data)

    def get_all(self) -> List[GeofencingSubscription]:

        json_data = self.api.geofencing.get_subscriptions()

        return list(map(lambda json_object: GeofencingSubscription.from_json(self.api, json_object), json_data))
