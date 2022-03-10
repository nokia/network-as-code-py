import requests
from .errors import GatewayConnectionError

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoids cyclic imports for type hints
    from .Device import Device


class RequestHandler:
    api_url = "https://apigee-api-test.nokia-solution.com/nac"

    @classmethod
    def _request(cls, method: str, path: str, headers: dict, json: dict, **kwargs):
        path = path.lstrip("/")
        url = f"{cls.api_url}/{path}"
        try:
            res = requests.request(method, url, headers=headers, json=json, **kwargs)
            res.raise_for_status()  # Raises an exception if status_code is in [400..600)
        except:
            raise GatewayConnectionError("Can't connect to the backend service")
        return res

    @classmethod
    def get_location(cls, device: "Device"):
        headers = {"x-apikey": device.sdk_token}
        json = {"id": device.id}
        return cls._request("POST", "/subscriber/location", headers, json)

    @classmethod
    def get_network_profile(cls, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token}
        json["id"] = device.id
        return cls._request("POST", "/subscriber/bandwidth", headers, json)

    @classmethod
    def set_network_profile(cls, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token}
        json["id"] = device.id
        return cls._request("PATCH", "/subscriber/bandwidth", headers, json)

    @classmethod
    def check_api_connection(cls, device):
        headers = {"x-apikey": device.sdk_token}
        res = cls._request("GET", "/hello", headers, None)
        return res.status_code
