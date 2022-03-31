import random  # Temporarily using random to generate events in the absence of a proper source
from .Device import Device
from .RequestHandler import RequestHandler


class GeoZone:
    def __init__(self, device: Device, area):
        self._area = area
        self._device = device
        # Handle rest of the initializations...

    def __repr__(self) -> str:
        return f"GeoZone(device={repr(self._device)}, area={repr(self._area)})"

    def monitor(self):
        # Register a new event stream with the API and return a listener object to user
        return GeoZoneEventStream()


class GeoZoneEventStream:
    def __repr__(self) -> str:
        return "GeoZoneEventStream()"

    def __iter__(self):
        for i in range(0, 2):
            yield random.choice(["enter", "leave"])
