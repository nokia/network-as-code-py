import sys

from qos_client.api_client import Configuration, ApiClient

from qos_client.apis.tags import qos_api

# import httpx
# import json as JSON
# # from .endpoints import AdminAPI, ServicesAPI, NotificationsAPI, SubscriptionsAPI

class APIClient:
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
        base_url: str = "https://qos-poc.p.rapidapi.com",
        **kwargs,
    ):
        headers = {
            "X-RapidAPI-Key": token,
            "X-RapidAPI-Host": "qos-poc.nokia-evaluation.rapidapi.com",
            "x-testmode": "true" if testmode else "false",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        config = Configuration(
            host=base_url,
            api_key={
                "RapidApiKey": token
            }
        )

        self._qos_client = ApiClient(
            config,
            header_name="X-RapidAPI-Host",
            header_value="qos-poc.nokia-evaluation.rapidapi.com"
        )

        self.sessions = qos_api.QosApi(self._qos_client)
