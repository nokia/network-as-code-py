from .api import APIClient
from .namespaces import Devices

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

    #### NAMESPACES

    @property
    def devices(self):
        """Namespace containing functionalities related to mobile subscriptions.

        TODO: Write some documentation about the subscription namespace here.
        """
        return self._devices

    #### TOP-LEVEL METHODS
    def connected(self):  # Just and example of a top-level method
        """
        Check whether this client can reach the Network as Code API gateway and backend.
        """
        connection_status = self._api.admin.check_api_connection()
        return True if connection_status == "up" else False
