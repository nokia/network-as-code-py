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
            cls._instance.url = "https://apigee-api-test.nokia-solution.com/network-as-code"

        return cls._instance

    def _make_request(self, method: str, path: str, headers: dict, json: dict):
        path = path.lstrip("/")
        url = f"{self.url}/{path}"
        try:
            res = requests.request(method, url, headers=headers, json=json)
            res.raise_for_status()  # Raises an exception if status_code is in [400..600)
        except:
            raise GatewayConnectionError("Can't connect to the backend service")
        return res

    def get_location(self, device: "Device"):
        headers = {"x-apikey": device.sdk_token}
        return self._make_request("GET", f"/location/{device.imsi}", headers, None)

    def create_network_slice(self, device: "Device", **data: dict):
        headers = {"x-apikey": device.sdk_token}
        data["imsi"] = device.imsi
        return self._make_request("POST", "networkslices", headers, data)

    def update_network_slice(self, device: "Device", **data: dict):
        headers = {"x-apikey": device.sdk_token}
        data["imsi"] = device.imsi
        return self._make_request("PUT", f"/networkslices/{slice.id}", headers, data)

    def delete_network_slice(self, slice: "NetworkSlice"):
        headers = {"x-apikey": slice.device.sdk_token}
        data = {"_id": slice.id, }
        res = self._make_request("DELETE", f"/networkslices/{slice.id}", headers, data)
        return res.status_code

    def check_api_connection(self, device):
        headers = {"x-apikey": device.sdk_token}
        res = self._make_request("GET", f"/hello", headers, None)
        return res.status_code
