from .Device import Device
from .RequestHandler import RequestHandler


class DeviceLocation:
    def __init__(self, device: Device) -> None:
        self.device = device
        self._refresh_info()

    def _refresh_info(self):
        res = RequestHandler.instance.get_location(self.device)
        if res.status_code == 200:
            self.latitude, self.longitude, self.altitude, self.timestamp = res.json()

    def refresh(self):
        self._refresh_info()
