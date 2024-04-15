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

from .api import APIClient
from .namespaces import Devices
from .namespaces import Sessions
from .namespaces import Slices
from .namespaces import Connectivity
from .namespaces import NetworkInsights

class NetworkAsCodeClient:
    """A client for working with Network as Code.

    ### Example:
    ```python
    from network_as_code import NetworkAsCodeClient

    client = NetworkAsCodeClient(token="your_api_token")
    sub = client.subscriptions.get("user@example.com")
    print(sub.location())
    ```

    ### Args:
        token (str): Authentication token for the Network as Code API.
        Any additional keyword arguments will be directly passed to the underlying HTTPX client.
    """

    def __init__(self, token: str, **kwargs):
        self._api = APIClient(token=token, **kwargs)
        self._devices = Devices(self._api)
        self._sessions = Sessions(self._api)
        self._slices = Slices(self._api)
        self._connectivity = Connectivity(self._api)
        self._insights = NetworkInsights(self._api)

    #### NAMESPACES

    @property
    def devices(self):
        """Namespace containing functionalities related to mobile subscriptions.

        TODO: Write some documentation about the subscription namespace here.
        """
        return self._devices

    @property
    def sessions(self):
        """Namespace containing functionalities related to mobile subscriptions.

        TODO: Write some documentation about the subscription namespace here.
        """
        return self._sessions

    @property
    def slices(self):
        return self._slices

    @property
    def connectivity(self):
        return self._connectivity

    @property
    def insights(self):
        return self._insights
