import sys
import json as JSON
import httpx
from textwrap import indent
from .admin import AdminAPI
from .services import ServicesAPI
from .subscription import SubscriptionAPI
from ..errors import APIError


class APIClient(
    httpx.Client,
    AdminAPI,
    ServicesAPI,
    SubscriptionAPI,
):
    """A client for communicating with Network as Code APIs.

    ### Args:
        sdk_token (str): Authentication token for the Network as Code API.
        timeout (int): Default timeout for API calls, in seconds.
        base_url (str): Base URL for the Network as Code API.
        testmode (bool): Whether to use simulated or real resources.
    """

    def __init__(
        self,
        token: str,
        timeout: int = 5,
        base_url: str = None,
        testmode: bool = False,
    ):
        super().__init__()

        self.timeout = timeout
        self.base_url = (
            "https://apigee-api-test.nokia-solution.com/nac/v4"
            if base_url is None
            else base_url
        ).rstrip("/")

        # Set the default headers for all API requests
        self.headers.update(
            {
                "x-apikey": token,
                "x-testmode": "true" if testmode else "false",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    # TODO: Don't Repeat Yourself...
    def _get(self, path: str, **kwargs):
        return self._request("GET", path, **kwargs)

    def _post(self, path: str, **kwargs):
        return self._request("POST", path, **kwargs)

    def _put(self, path: str, **kwargs):
        return self._request("PUT", path, **kwargs)

    def _patch(self, path: str, **kwargs):
        return self._request("PATCH", path, **kwargs)

    def _delete(self, path: str, **kwargs):
        return self._request("DELETE", path, **kwargs)

    def _request(self, method: str, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"

        try:
            res = self.request(method, url, timeout=self.timeout, **kwargs)
            return res
        except httpx.ReadTimeout as e:
            print(f"ERROR: The API gateway did not respond in {self.timeout} seconds.")
            sys.exit(1)  # TODO: Should this raise another error instead?

    def _result(self, response: httpx.Response, json=False, raw=False):
        assert not (json and raw)  # Can't have both output types selected
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            # TODO: Parse errors instead of simply printing their body content
            print("ERROR: The API gateway returned the following error:")
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
