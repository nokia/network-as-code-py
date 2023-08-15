import sys
from ..api.slice_api import AttachAPI, SliceAPI

from network_as_code.api.device_api import DeviceAPI

from .location_api import LocationAPI 
from .device_status_api import DeviceStatusAPI

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
        qos_base_url: str = "https://quality-of-service-on-demand.p-eu.rapidapi.com",
        location_base_url: str = "https://device-location.p-eu.rapidapi.com",
        slice_base_url: str = "https://network-slicing.p-eu.rapidapi.com",
        slice_attach_base_url: str = "https://device-attach-norc.p-eu.rapidapi.com",
        devicestatus_base_url: str = "https://device-status.p-eu.rapidapi.com",
        **kwargs,
    ):

        self.sessions = DeviceAPI(base_url=qos_base_url, rapid_key=token, rapid_host="quality-of-service-on-demand.nokia.rapidapi.com")

        self.devicestatus = DeviceStatusAPI(base_url=devicestatus_base_url, rapid_key=token, rapid_host="device-status.nokia.rapidapi.com")

        self.location = LocationAPI(base_url=location_base_url, rapid_key=token, rapid_host="device-location.nokia.rapidapi.com")

        self.slice_new = SliceAPI(base_url=slice_base_url, rapid_key=token, rapid_host="network-slicing.nokia.rapidapi.com")

        self.slice_attach = AttachAPI(base_url=slice_attach_base_url, rapid_key=token, rapid_host="device-attach-norc.nokia.rapidapi.com")
