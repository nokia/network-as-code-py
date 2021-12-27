import requests
from .Device import Device
from .NetworkSlice import NetworkSlice


class RequestHandler:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Hardcoded for prototyping
            cls._instance.url = "https://sdk-gateway.ext.dynamic.nsn-net.nokia.com"
            cls._instance.port = 8000

        return cls._instance

    def get_location(self, device: Device):
        res = requests.get(
            f"{self.url}:{self.port}/api/{device.imsi}",
            {"sdk_token": device.sdk_token},
        )
        res.raise_for_status()
        return res.json()

    def create_network_slice(self, slice: NetworkSlice):
        res = requests.post(
            f"{self.url}:{self.port}/api/networkslices",
            {
                "slice": slice,
                "sdk_token": slice.device.sdk_token
            },
        )
        res.raise_for_status()
        return res.json().id

    def update_network_slice(self, slice: NetworkSlice):
        res = requests.put(
            f"{self.url}:{self.port}/api/networkslices/{slice.id}",
            {
                "slice": slice,
                "sdk_token": slice.device.sdk_token
            },
        )
        res.raise_for_status()

    def delete_network_slice(self, slice: NetworkSlice):
        res = requests.delete(
            f"{self.url}:{self.port}/api/networkslices/{slice.id}",
            {
                "sdk_token": slice.device.sdk_token
            },
        )
        res.raise_for_status()
