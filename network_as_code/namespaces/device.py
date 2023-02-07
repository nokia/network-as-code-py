from typing import List
from . import Namespace
from ..models import Device


class Devices(Namespace):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    def get(self, id: str, ip = None) -> Device:
        """Get a subscription by its external ID.

        Args:
            id (str): External ID of the subscription. Email-like.
        """
        # res = self.api.subscriptions.get_subscription(id)
        return Device(api=self.api, sid = id, ip = ip)

