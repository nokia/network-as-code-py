from .Device import Device
from .RequestHandler import RequestHandler


class DeviceLocation:
    def __init__(self, device: Device):
        self.device = device
        self._get_location()

    def _get_location(self):
        res = RequestHandler.instance.get_location(self.device)
        if res.status_code == 200:
            location = res.json()["location"]
            self.latitude = location["latitude"]
            self.longitude = location["longitude"]
            self.altitude = location["altitude"]
            self.timestamp = location["timestamp"]

    def refresh(self):
        self._get_location()
