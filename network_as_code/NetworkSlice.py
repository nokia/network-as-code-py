from .Device import Device
from .RequestHandler import RequestHandler


class NetworkProfile:
    def __init__(
        self,
        device: Device,
        bandwidth_profile: str,
    ):
        self._device = device
        self.bandwidth_profile = bandwidth_profile

    @property
    def device(self) -> Device:
        return self._device

    @property
    def bandwidth_profile(self) -> str:
        return self._bandwidth_profile

    @bandwidth_profile.setter
    def bandwidth_profile(self, value):
        self._bandwidth_profile = value
        self.update(bandwidth_profile=value)

    def update(
        self,
        bandwidth_profile: str = None,
    ):
        """
        Update one or more parameters of the network slice.

        Arguments:
            bandwidth_profile (str): How much bandwidth should be reserved in Mbps.
        """

        res = RequestHandler.instance.set_network_profile(self.device, bandwidthID=bandwidth_profile)
