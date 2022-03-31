from .RequestHandler import RequestHandler
from .Configuration import Configuration
from enum import IntEnum

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoids cyclic imports for type hints
    from .Device import Device


class Unit(IntEnum):
    BIT = 1
    KBIT = 1000
    MBIT = 1000 * 1000

    def convert_from(self, old_unit: "Unit", value: int):
        value_in_bits = value * old_unit.value
        return value_in_bits / self.value


class CustomNetworkProfile(Configuration):
    """Representation of a network configuration with user-specified download and upload bandwidth.

    This class allows the creation of a network profile instance, which can then be
    applied to one or many Device instances.

    #### Example usage:
    ```python
    device = Device(id="string@registered.domain")
    profile = CustomNetworkProfile(download=1024000, upload=4096000)
    device.apply(profile)
    ````
    """

    def __init__(self, download: int, upload: int, unit: Unit = Unit.BIT):
        """Constructor for initializing CustomNetworkProfile with desired values.

        Args:
            download: A value representing the bits per second of maximum download speed
            upload: A value representing the bits per second of maximum upload speed
        """
        self._bandwidth_profile = "custom"
        self.download = int(Unit.BIT.convert_from(unit, download))
        self.upload = int(Unit.BIT.convert_from(unit, upload))
        self.unit = unit

    def __repr__(self) -> str:
        return (
            "CustomNetworkProfile("
            f"download={repr(self.download)}, "
            f"upload={repr(self.upload)}, "
            f"unit={repr(self.unit)})"
        )

    @property
    def bandwidth_profile(self) -> str:
        return self._bandwidth_profile

    @property
    def download(self) -> int:
        return self._download

    @download.setter
    def download(self, value: int):
        self._download = value

    @property
    def upload(self) -> int:
        return self._upload

    @upload.setter
    def upload(self, value: int):
        self._upload = value

    @classmethod
    def get(cls, device: "Device"):
        """
        NOT IMPLEMENTED, DO NOT USE

        Get a `CustomNetworkProfile` of a given device.

        Args:
            device: An instance of the `Device` class.

        Returns:
            New instance of `CustomNetworkProfile` that matches the current network profile of
            the given device.
        """
        # json = RequestHandler.get_custom_network_profile(device).json()
        # print(json)

        # return cls(json["download"][0], json["upload"][0])
        raise NotImplementedError(
            "Feature disabled temporarily due to upstream API incompatibility"
        )

    def apply(self, device: "Device"):
        """Apply this `CustomNetworkProfile` to the given device.

        Args:
            device: An instance of the `Device` class, to which the network profile
            is applied.
        """
        RequestHandler.set_custom_network_profile(
            device, download=self.download, upload=self.upload
        )
