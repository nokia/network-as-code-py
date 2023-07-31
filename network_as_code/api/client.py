import sys

import qos_client.api_client as qos_api_client

from qos_client.apis.tags import default_api as qos_api

import location_client.api_client as location_api_client

from location_client.apis.tags import location_api

import devicestatus_client.api_client as devicestatus_api_client

from devicestatus_client.apis.tags import default_api as devicestatus_api

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
        qos_base_url: str = "https://qos-on-demand.p-eu.rapidapi.com",
        location_base_url: str = "https://location-verification.p-eu.rapidapi.com",
        devicestatus_base_url: str = "https://device-status.p-eu.rapidapi.com",
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
            header_value="qos-on-demand.nokia-dev.rapidapi.com"
        )

        self.sessions = qos_api.DefaultApi(self._qos_client)

        location_config = location_api_client.Configuration(
            host=location_base_url,
            api_key={
                "RapidApiKey": token
            }
        )

        self._location_client = location_api_client.ApiClient(
            location_config,
            header_name="X-RapidAPI-Host",
            header_value="location-verification.nokia-dev.rapidapi.com"
        )

        self.location = location_api.LocationApi(self._location_client)

        devicestatus_config = devicestatus_api_client.Configuration(
            host=devicestatus_base_url,
            api_key={
                "RapidApiKey": token
            }
        )

        self._devicestatus_client = devicestatus_api_client.ApiClient(
            devicestatus_config,
            header_name="X-RapidAPI-Host",
            header_value="device-status.nokia-dev.rapidapi.com"
        )

        self.devicestatus = devicestatus_api.DefaultApi(self._devicestatus_client)
