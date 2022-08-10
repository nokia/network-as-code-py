import requests
from .info import InfoAPI
from .subscription import SubscriptionAPI


class APIClient(requests.Session, InfoAPI, SubscriptionAPI):
    """A client for communicating with Network as Code APIs.

    ### Args:
        sdk_token (str): Authentication token for the Network as Code API.
        timeout (int): Default timeout for API calls, in seconds.
        base_url (str): Base URL for the Network as Code API.
    """

    def __init__(self, token: str, timeout: int = 5, base_url: str = None):
        super().__init__()

        self.timeout = timeout
        self.base_url = (
            "https://apigee-api-test.nokia-solution.com/nac/v2"
            if base_url is None
            else base_url
        )

        # Set the default headers for all API requests
        self.headers.update(
            {
                "x-apikey": token,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    # TODO: Don't Repeat Yourself...
    def _get(self, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.get(url, timeout=self.timeout, **kwargs)

    def _post(self, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.post(url, timeout=self.timeout, **kwargs)

    def _put(self, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.put(url, timeout=self.timeout, **kwargs)

    def _delete(self, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.delete(url, timeout=self.timeout, **kwargs)

    def _result(self, response, json=False, raw=False):
        assert not (json and raw)

        # TODO: Add API error handling using response.raise_for_status()

        if json:
            return response.json()
        if raw:
            return response.content
        return response.text
