import sys
import httpx
import json as JSON
from .endpoints import AdminAPI, ServicesAPI, NotificationsAPI, SubscriptionsAPI


class APIClient(httpx.AsyncClient):
    """A client for communicating with Network as Code APIs.

    ### Args:
        token (str): Authentication token for the Network as Code API.
        base_url (str): Base URL for the Network as Code API.
        testmode (bool): Whether to use simulated or real resources.
    """

    def __init__(
        self,
        token: str,
        testmode: bool = False,
        base_url: str = "https://network-as-code-poc.p.rapidapi.com",
        **kwargs,
    ):
        headers = {
            "X-RapidAPI-Key": token,
            "X-RapidAPI-Host": "poc4.nokia-evaluation.rapidapi.com",
            "x-testmode": "true" if testmode else "false",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        super().__init__(headers=headers, base_url=base_url, **kwargs)

        self.admin = AdminAPI(self)
        self.services = ServicesAPI(self)
        self.subscriptions = SubscriptionsAPI(self)
        self.notifications = NotificationsAPI(self)

    @classmethod
    def result(cls, response: httpx.Response, json=False, raw=False):
        """Helper function to extract and parse the result of an API response.

        ### Args:
            response (Response): A HTTPX Response object representing a response from the API
            json (bool): Whether to parse the response body as JSON
            raw (bool): Whether to return the response body as raw bytes

        If neither `json` nor `raw` is set to `True` the response body will be returned as a `string`.
        """
        # TODO: Handling request exceptions. Maybe through a HTTPX middleware?
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
