import sys
import httpx

import json as JSON

from .endpoints.admin import AdminAPI
from .endpoints.services import ServicesAPI
from .endpoints.subscriptions import SubscriptionsAPI
from .endpoints.notifications import NotificationsAPI

class APIClient(
    httpx.Client,
):
    """A client for communicating with Network as Code APIs.

    ### Args:
        token (str): Authentication token for the Network as Code API.
        timeout (int): Default timeout for API calls, in seconds.
        base_url (str): Base URL for the Network as Code API.
        testmode (bool): Whether to use simulated or real resources.
    """

    def __init__(
        self,
        token: str,
        timeout: int = 5,
        base_url: str = "https://network-as-code-poc.p.rapidapi.com",
        testmode: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.timeout = timeout
        self.base_url = base_url

        # Set the default headers for all API requests
        self.headers = {
            "x-apikey": token,
            "x-testmode": "true" if testmode else "false",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self.admin = AdminAPI(self)
        self.services = ServicesAPI(self)
        self.subscriptions = SubscriptionsAPI(self)
        self.notifications = NotificationsAPI(self)

    def __del__(self):
        """
        Makes sure that the connection will be closed properly before the object gets deleted.
        """
        self.close()

    # TODO: Handling request exceptions. Maybe through a HTTPX middleware?

    def _result(self, response: httpx.Response, json=False, raw=False):
        assert not (json and raw)  # Can't have both output types selected
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            # TODO: Parse errors instead of simply printing their body content
            print("ERROR: The API gateway returned the following error:", end="")
            try:
                print(JSON.dumps(response.json(), indent=2))
            except Exception:
                print(response.text)
            sys.exit(1)  # TODO: Should this raise APIError instead?

        if json:
            return response.json()
        if raw:
            return response.content
        return response.text


class AsyncAPIClient(httpx.AsyncClient):
    pass
