import os
import pprint
import requests
from .errors import ApiError, GatewayConnectionError

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoids cyclic imports for type hints
    from .Device import Device


class RequestHandler:
    api_version = "v2"
    api_url = f"https://apigee-api-test.nokia-solution.com/nac/{api_version}"
    accept_header = "application/json"

    @classmethod
    def _request(cls, method: str, path: str, headers: dict, json: dict, **kwargs):
        path = path.lstrip("/")
        url = f"{cls.api_url}/{path}"

        if os.getenv("TESTMODE"):
            headers["x-testmode"] = "true"

        try:
            res = requests.request(
                method, url, headers=headers, json=json, timeout=5, **kwargs
            )
            if os.getenv("DEBUG"):
                print(f"{method} /{path} ({json})")
                pprint.pprint(res.json(), width=88, compact=True)

            if not res.ok:
                res_data = res.json()
                error_msg = (
                    res_data["error"]
                    if "error" in res_data
                    else "Received an uknown error from the API"
                )
                raise ApiError(error_msg)

            return res
        except requests.ConnectionError as e:
            raise GatewayConnectionError(str(e))

    @classmethod
    def get_location(cls, device: "Device"):
        headers = {"x-apikey": device.sdk_token, "Accept": cls.accept_header}
        json = {"id": device.id}
        return cls._request("POST", "/subscriber/location", headers, json)

    @classmethod
    def get_network_profile(cls, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token, "Accept": cls.accept_header}
        json["id"] = device.id
        return cls._request("POST", "/subscriber/bandwidth", headers, json)

    @classmethod
    def set_network_profile(cls, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token, "Accept": cls.accept_header}
        json["id"] = device.id
        return cls._request("PATCH", "/subscriber/bandwidth", headers, json)

    @classmethod
    def get_custom_network_profile(cls, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token, "Accept": cls.accept_header}
        json["id"] = device.id
        return cls._request("POST", "/subscriber/bandwidth/custom", headers, json)

    @classmethod
    def set_custom_network_profile(cls, device: "Device", **json: dict):
        headers = {"x-apikey": device.sdk_token, "Accept": cls.accept_header}
        json["id"] = device.id
        return cls._request("PATCH", "/subscriber/bandwidth/custom", headers, json)

    @classmethod
    def check_api_connection(cls, device: "Device"):
        headers = {"x-apikey": device.sdk_token, "Accept": cls.accept_header}
        res = cls._request("GET", "/hello", headers, None)
        return res.status_code
