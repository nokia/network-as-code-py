from .api import APIClient
from .models import SubscriptionCollection, NetworkSliceCollection
from .models.notification import NotificationCollection


class NetworkAsCodeClient:
    """
    A client for communication with Network as Code.

    ### Example:
    ```python
    import network_as_code as nac

    client = nac.NetworkAsCodeClient(token="your_api_token")
    ```

    ### Args:
        token (str): Authentication token for the Network as Code API.
        timeout (int): Default timeout for API calls, in seconds. By default 5s.
        base_url (str): Base URL for the Network as Code API. Note that a default base URL is already set.
        testmode (bool): Whether to use simulated or real resources, such as devices. False by default.
    """

    def __init__(self, *args, **kwargs):
        self._api = APIClient(*args, **kwargs)
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
        return NotificationCollection(client=self)

    # TOP-LEVEL METHODS
    def connected(self):  # Just and example of a top-level method
        """Check whether this client can reach the Network as Code API gateway and backend."""
        return True if self._api.admin.check_api_connection() == "up" else False


class NetworkAsCodeAsyncClient:
    pass
