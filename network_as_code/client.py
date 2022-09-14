from .api.client import APIClient
from .models.subscription import SubscriptionCollection


class NetworkAsCodeClient:
    """
    A client for communication with Network as Code.

    ### Example:
    ```python
    import network_as_code as nac

    client = nac.NetworkAsCodeClient(token="your_api_token")
    ```

    ### Args:
        sdk_token (str): Authentication token for the Network as Code API.
        timeout (int): Default timeout for API calls, in seconds. By default 5s.
        base_url (str): Base URL for the Network as Code API. Note that a default base URL is already set.
        testmode (bool): Whether to use simulated or real resources, such as devices. False by default.
    """

    def __init__(self, *args, **kwargs):
        self.api = APIClient(*args, **kwargs)


    # RESOURCES
    @property
    def subscriptions(self):
        """An object for managing mobile subscriptions.

        See the `<subscriptions>` documentation for full details.
        """

        return SubscriptionCollection(client=self)

    # TOP-LEVEL METHODS
    def connected(self):  # Just and example of an top-level method
        """
        Check whether this client is connected to the Network as Code API gateway and backend.
        """
        return True if self.api.check_api_connection() == "up" else False
