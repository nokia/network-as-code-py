from dateutil.parser import parse
from .RequestHandler import RequestHandler
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoids cyclic imports for type hints
    from .Device import Device
    from datetime import datetime


class DeviceLocation:
    """Class for representing and storing information about a device's location.

    Objects of this class are not intended to be initialized by third party developers
    and are instead created by calls like Device.location(). The objects will have
    knowledge of latitude and longitude and elevation. The objects should also be
    considered immutable.

    #### Example usage:
    ```python
    device = Devide(id="string@registered.domain", sdk_token="some_sdk_token")
    location = device.location()

    lon = location.longitude
    lat = location.longitude
    elev = location.elevation
    ```
    """

    def __init__(
        self,
        latitude: float,
        longitude: float,
        elevation: float,
        timestamp: "datetime|str",
    ):
        self._latitude = latitude
        self._longitude = longitude
        self._elevation = elevation
        self._timestamp = parse(timestamp) if isinstance(timestamp, str) else timestamp

    def __repr__(self) -> str:
        return (
            "DeviceLocation("
            f"latitude={repr(self.latitude)}, "
            f"longitude={repr(self.longitude)}, "
            f"elevation={repr(self.elevation)}, "
            f"timestamp={repr(self.timestamp)})"
        )

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def elevation(self) -> float:
        return self._elevation

    @property
    def timestamp(self) -> "datetime":
        return self._timestamp

    @classmethod
    def get(cls, device: "Device"):
        res = RequestHandler.get_location(device)
        info = res.json()
        location_info = info["locationInfo"]

        return cls(
            float(location_info["lat"]),
            float(location_info["long"]),
            float(location_info["elev"]),
            parse(info["eventTime"]),
        )
