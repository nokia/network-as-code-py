from .Device import Device
from .RequestHandler import RequestHandler


class NetworkProfile:
    """Representation of a network configuration selected from a list of available network tiers.

    This class allows the creation of a network profile instance, which can then be applied to
    one or many Device instances.

    #### Example usage:
    ```python
    device = Device(ext_id="string@registered.domain")

    profile = NetworkProfile("gold")

    device.apply(profile)
    ````
    """

    def __init__(
        self,
        bandwidth_profile: str,
    ):
        self.bandwidth_profile = bandwidth_profile

    @property
    def bandwidth_profile(self) -> str:
        return self._bandwidth_profile

    @bandwidth_profile.setter
    def bandwidth_profile(self, value):
        self._bandwidth_profile = value

    def apply(
        self,
        device
    ):
        """
        Apply this Network Profile to a given device

        Args:
            device: An instance of the Device class, to which the network profile is applied
        """

        res = RequestHandler.instance.set_network_profile(device, bandwidthID=self.bandwidth_profile)
