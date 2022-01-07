import requests
from .errors import GatewayConnectionError

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoids cyclic imports for type hints
    from .Device import Device
    from .NetworkSlice import NetworkSlice


class RequestHandler:
    _instance = None

    @classmethod
    @property
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Hardcoded for prototyping
            cls._instance.url = "https://sdk-gateway.ext.dynamic.nsn-net.nokia.com"
            cls._instance.port = 8000

        return cls._instance

    def _make_request(self, method: str, path: str, json: dict):
        path = path.lstrip("/")
        url = f"{self.url}:{self.port}/api/{path}"
        try:
            res = requests.request(method, url, json=json)
            res.raise_for_status()  # Raises an exception if status_code is in [400..600)
        except:
            raise GatewayConnectionError("Can't connect to the backend service")
        return res

    def get_location(self, device: "Device"):
        data = {"sdk_token": device.sdk_token}
        res = self._make_request("GET", device.imsi, data)
        return res

    def create_network_slice(self, slice: "NetworkSlice"):
        data = {"imsi": slice.device.imsi, "sdk_token": slice.device.sdk_token}
        res = self._make_request("POST", "networkslices", data)
        return res

    def update_network_slice(self, slice: "NetworkSlice"):
        data = {"some": "parameter", "sdk_token": slice.device.sdk_token}
        res = self._make_request("PUT", f"networkslices/{slice.id}", data)
        return res

    def delete_network_slice(self, slice: "NetworkSlice"):
        data = {"slice_id": slice.id, "sdk_token": slice.device.sdk_token}
        res = self._make_request("DELETE", f"networkslices/{slice.id}", data)
        return res.status_code
