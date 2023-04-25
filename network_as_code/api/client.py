import sys

import qos_client.api_client as qos_api_client

from qos_client.apis.tags import qos_api

import location_client.api_client as location_api_client

from location_client.apis.tags import location_api

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
        qos_base_url: str = "https://qos-poc.p.rapidapi.com",
        location_base_url: str = "https://qos-poc.p.rapidapi.com",
        **kwargs,
    ):
        qos_config = qos_api_client.Configuration(
            host=qos_base_url,
            api_key={
                "RapidApiKey": token
            }
        )

        self._qos_client = qos_api_client.ApiClient(
            qos_config,
            header_name="X-RapidAPI-Host",
            header_value="qos-poc.nokia-evaluation.rapidapi.com"
        )

        self.sessions = qos_api.QosApi(self._qos_client)

        location_config = location_api_client.Configuration(
            host=location_base_url,
            api_key={
                "RapidApiKey": token
            }
        )

        self._location_client = location_api_client.ApiClient(
            location_config,
            header_name="X-RapidAPI-Host",
            header_value="qos-poc.nokia-evaluation.rapidapi.com"
        )

        self.location = location_api.LocationApi(self._location_client)
