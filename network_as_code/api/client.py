import sys
from ..api.slice_api import SliceAPI

from network_as_code.api.device_api import DeviceAPI

import location_client.api_client as location_api_client

from location_client.apis.tags import location_api

import slice_client.api_client as slice_api_client

from slice_client.apis.tags import slice_api

import devicestatus_client.api_client as devicestatus_api_client

from devicestatus_client.apis.tags import default_api as devicestatus_api

from .location_api import LocationAPI 

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
        slice_base_url: str = "https://network-slicing.p-eu.rapidapi.com",
        devicestatus_base_url: str = "https://device-status.p-eu.rapidapi.com",
        **kwargs,
    ):

        self.sessions = DeviceAPI(
            key=token,
            host="qos-on-demand.nokia-dev.rapidapi.com",
            url=qos_base_url
        )

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

        slice_config = slice_api_client.Configuration(
            host=slice_base_url,
            api_key={
                "RapidApiKey": token
            }
        )

        self._slice_client = slice_api_client.ApiClient(
            slice_config,
            header_name="X-RapidAPI-Host",
            header_value="network-slicing.nokia-dev.rapidapi.com"
        )

        self.slice = slice_api.SliceApi(self._slice_client)

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

        self.location = LocationAPI(token)
        self.slice_new = SliceAPI(
            base_url=slice_base_url, 
            rapid_key=token,
            rapid_host="network-slicing.nokia-dev.rapidapi.com"
        )
