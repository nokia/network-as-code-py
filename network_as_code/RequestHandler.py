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
            cls._instance.url = "https://apigee-api-test.nokia-solution.com/nac"

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
        json = { "externalid": device.ext_id }
        return self._make_request("GET", f"/subscriber/location", headers, json)

    def get_network_profile(self, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token}
        json["id"] = device.ext_id
        return self._make_request("POST", "/subscriber/bandwidth", headers, json)

    def set_network_profile(self, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token}
        json["id"] = device.ext_id
        return self._make_request("PATCH", "/subscriber/bandwidth", headers, json)

    def check_api_connection(self, device):
        headers = {"x-apikey": device.sdk_token}
        res = self._make_request("GET", f"/hello", headers, None)
        return res.status_code
