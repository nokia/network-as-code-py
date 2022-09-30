from .api import APIClient
from .models import (
    NetworkSliceCollection,
    SubscriptionCollection,
    NotificationCollection,
)


class NetworkAsCodeClient:
    """A client for working with Network as Code.

    ### Example:
    ```python
    from network_as_code import NetworkAsCodeClient

    client = NetworkAsCodeClient(token="your_api_token")
    ```

    ### Args:
        token (str): Authentication token for the Network as Code API.
        Any additional keyword arguments will be directly passed to the underlying HTTPX client.
    """

    def __init__(self, token: str, **kwargs):
        self._api = APIClient(token=token, **kwargs)
        self._slicing = NetworkSliceCollection(self._api)
        self._subscriptions = SubscriptionCollection(self._api)
        self._notifications = NotificationCollection(self._api)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def close(self):
        """Closes the API client.

        After this no more API requests can be made using this client.
        """
        await self._api.aclose()

    #### NAMESPACES
    @property
    def slicing(self):
        """Namespace containing functionalities related to network slicing.

        TODO: Write some documentation about the slice namespace here.
        """
        return self._slicing

    @property
    def subscriptions(self):
        """Namespace containing functionalities related to mobile subscriptions.

        TODO: Write some documentation about the subscription namespace here.
        """
        return self._subscriptions

    @property
    def notifications(self):
        """Namespace containing functionalities related to various notifications from Network as Code.

        TODO: Write some documentation about the notifications namespace here.
        """
        return self._notifications

    #### TOP-LEVEL METHODS
    async def connected(self):  # Just and example of a top-level method
        """
        Check whether this client can reach the Network as Code API gateway and backend.
        """
        connection_status = await self._api.admin.check_api_connection()
        return True if connection_status == "up" else False
