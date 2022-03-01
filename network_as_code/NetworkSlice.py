from .Device import Device
from .RequestHandler import RequestHandler


class NetworkProfile:
    def __init__(
        self,
        device: Device,
        bandwidth_profile: str,
    ):
        self._device = device
        self._bandwidth_profile = bandwidth_profile
        # self._check_attributes(
        #     bandwidth=bandwidth,
        # )
        res = RequestHandler.instance.set_network_profile(
            self._device,
            bandwidthID=bandwidth_profile,
        )

    @property
    def device(self) -> Device:
        return self._device

    @property
    def bandwidth_profile(self) -> str:
        return self._bandwidth_profile

    @bandwidth_profile.setter
    def bandwidth_profile(self, value: str):
        self.update(bandwidth_profile=value)

    # def _check_attributes(self, *, index, qos, bandwidth, default):
    #     if index < 0 or index > 7:
    #         raise ValueError("Network slice index must be between 0 and 7")
    #     if qos < 0 or qos > 4:
    #         raise ValueError("Network slice QoS value must be between 0 and 4")
    #     if bandwidth < 0:
    #         raise ValueError("Bandwidth of a slice below 0 is not possible")
    #     if not isinstance(default, bool):
    #         raise TypeError(
    #             "The 'default' attribute of a network slice must be of type bool"
    #         )

    def _set_attributes(self, attributes: dict):
        self._bandwidth = attributes["bandwidth"]

    def update(
        self,
        bandwidth_profile: str = None,
    ):
        """
        Update one or more parameters of the network slice.

        Arguments:
            bandwidth_profile (str): How much bandwidth should be reserved in Mbps.
        """
        params = {
            "bandwidth_profile": self.bandwidth_profile if bandwidth_profile is None else bandwidth_profile,
        }
        # self._check_attributes(**params)
        res = RequestHandler.instance.set_network_profile(self.device, bandwidthID=bandwidth_profile)

    # def destroy(self):
    #     """Delete the network slice from the network."""
    #     RequestHandler.instance.delete_network_slice(self)
    #     return True
