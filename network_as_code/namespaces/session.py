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

from . import Namespace
from ..models import QoDSession
from ..models import Device


class Sessions(Namespace):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    def get(self, id: str) -> QoDSession:
        """Get a QoS Session by its ID.

        Args:
            id (str): ID of the QoS Session
        """
        session_object = self.api.sessions.get_session(id)
        device_json = session_object.json()['device']
        device = Device.convert_to_device_model(self.api, device_json)
        return QoDSession.convert_session_model(self.api, device, session_object.json())
    