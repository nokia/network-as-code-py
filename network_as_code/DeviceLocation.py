
from dateutil.parser import parse

from .RequestHandler import RequestHandler

class DeviceLocation:
    def __init__(
        self,
        latitude: float,
        longitude: float,
        elevation: float,
        timestamp
    ):
        self._latitude = latitude
        self._longitude = longitude
        self._elevation = elevation
        self._timestamp = timestamp

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
    def timestamp(self) -> float:
        return self._timestamp

    @classmethod
    def get(cls, device):
        res = RequestHandler.get_location(device)
        info = res.json()
        location_info = info["locationInfo"]

        return cls(float(location_info["lat"]), float(location_info["long"]), float(location_info["elev"]), parse(info["eventTime"]))
