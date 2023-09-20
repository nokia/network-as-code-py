from typing import List
from . import Namespace
from ..models import Device, DeviceIpv4Addr
from urllib.error import HTTPError
from pydantic import ValidationError

class Devices(Namespace):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    def get(self, id: str, ipv4_address = None, ipv6_address = None, phone_number = None) -> Device:
        """Get a subscription by its external ID.

        Args: 
            id (str): External ID of the subscription. Email-like.
            ipv4_address (Any | None): ipv4 address of the subscription.
            ipv6_address (Any | None): ipv6 address of the subscription.
            phone_number (Any | None): phone number of the subscription.
        """

        #Check if ipv4_address is a simple string and convert it into the desired format (DeviceIpv4Addr)
        if ipv4_address and isinstance(ipv4_address, str):
            ipv4_address = DeviceIpv4Addr(public_address=ipv4_address, private_address=None, public_port=None)

        ret_device = Device(api=self.api, sid = id, ipv4_address = ipv4_address, ipv6_address = ipv6_address, phone_number = phone_number)
        return ret_device

