from .api import APIClient, AsyncAPIClient
from .models import SubscriptionCollection, NetworkSliceCollection, NotificationCollection


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
        self._subscriptions = SubscriptionCollection(self._api)
        self._slicing = NetworkSliceCollection(self._api)

    # NAMESPACES
    @property
    def subscriptions(self):
        """Namespace containing functionalities related to mobile subscriptions.

        TODO: Write some documentation about the subscription namespace here.
        """
        return self._subscriptions

    @property
    def slicing(self):
        """Namespace containing functionalities related to network slicing.

        TODO: Write some documentation about the slice namespace here.
        """
        return self._slicing

    @property
    def notifications(self):
        return NotificationCollection(self._api)

    # TOP-LEVEL METHODS
    def connected(self):  # Just and example of a top-level method
        """Check whether this client can reach the Network as Code API gateway and backend."""
        return True if self._api.admin.check_api_connection() == "up" else False


class NetworkAsCodeAsyncClient:
    """A client for working with Network as Code in asynchronous code.

    ### Example:
    ```python
    from network_as_code import NetworkAsCodeAsyncClient

    client = NetworkAsCodeAsyncClient(token="your_api_token")
    ```

    ### Args:
        token (str): Authentication token for the Network as Code API.
        Any additional keyword arguments will be directly passed to the underlying HTTPX client.
    """
    def __init__(self, token: str, **kwargs):
        self._api = AsyncAPIClient(token=token, **kwargs)
        self._subscriptions = SubscriptionCollection(self._api)
        self._slicing = NetworkSliceCollection(self._api)
