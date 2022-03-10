
from .RequestHandler import RequestHandler

from .NetworkProfile import NetworkProfile

class Device:
    def __init__(self, ext_id: str, sdk_token: str) -> None:
        self.ext_id = ext_id
        self.sdk_token = sdk_token

    def check_api_connection(self):
        res = RequestHandler.instance.check_api_connection(self)
        return res == 200

    def get_network_profile(self):
        json = RequestHandler.instance.get_network_profile(self).json()

        return NetworkProfile(json["serviceTier"][0])

    def apply(self, configuration):
        """Apply a configuration change to this device.

        Args:
            configuration: An network configuration object, such as a NetworkProfile"""
        configuration.apply(self)
