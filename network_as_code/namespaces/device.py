from typing import List
from . import Namespace
from ..models import Device
from ..errors import DeviceNotFound, AuthenticationException, ServiceError, InvalidParameter
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
        """

        # Error Case: Creating and Getting device
        try:
            global ret_device
            ret_device = Device(api=self.api, sid = id, ipv4_address = ipv4_address, ipv6_address = ipv6_address, phone_number = phone_number)
        except HTTPError as e:
            if e.code == 403:
                raise AuthenticationException(e)
            elif e.code == 404:
                raise DeviceNotFound(e)
            elif e.code >= 500:
                raise ServiceError(e)
        except ValidationError as e:
            raise InvalidParameter(e)
        
        # ret_device = Device(api=self.api, sid = id, ip = ip)
        # res = self.api.subscriptions.get_subscription(id)
        return ret_device

