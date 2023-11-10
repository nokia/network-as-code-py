from .api import APIClient
from .namespaces import Devices
from .namespaces import Sessions
from .namespaces import Slices
from .namespaces import Connectivity


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
