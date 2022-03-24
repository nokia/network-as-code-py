from .RequestHandler import RequestHandler
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoids cyclic imports for type hints
    from .Device import Device


class NetworkProfile:
    """Representation of a network configuration selected from a list of available
    network tiers.

    This class allows the creation of a network profile instance, which can then be
    applied to one or many Device instances.

    #### Example usage:
    ```python
    device = Device(id="string@registered.domain")
    profile = NetworkProfile("gold")
    device.apply(profile)
    ````
    """

    def __init__(self, bandwidth_profile: str, priority: str = None):
        self.bandwidth_profile = bandwidth_profile
        self.priority = priority

    @property
    def bandwidth_profile(self) -> str:
        return self._bandwidth_profile

    @bandwidth_profile.setter
    def bandwidth_profile(self, value: str):
        self._bandwidth_profile = value

    def apply(self, device: "Device"):
        """Apply this `NetworkProfile` to the given device.

        Args:
            device: An instance of the `Device` class, to which the network profile
            is applied.
        """
        RequestHandler.set_network_profile(device, bandwidth=self.bandwidth_profile)

    @classmethod
    def get(cls, device: "Device"):
        """
        Get a `NetworkProfile` of a given device.

        Args:
            device: An instance of the `Device` class.

        Returns:
            New instance of `NetworkProfile` that matches the current network profile of
            the given device.
        """
        json = RequestHandler.get_network_profile(device).json()
        attributes = [
            attribute["value"]["value"]
            for attribute in reversed(json[0]["customData"]["entry"])
        ]
        return cls(*attributes)
