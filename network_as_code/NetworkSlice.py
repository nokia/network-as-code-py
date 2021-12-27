from .Device import Device
from .RequestHandler import RequestHandler


class NetworkSlice:
    def __init__(
        self,
        device: Device,
        index: int,
        qos,
        bandwidth,
        default: bool,
    ) -> None:
        self.device = device
        self.index = index
        self.qos = qos
        self.bandwidth = bandwidth
        self.active = False

        self._setup()

    def _setup(self):
        res = RequestHandler.instance().create_network_slice(self)
        if res.status_code == 200:
            self.id = res.json()
            self.active = True

    def update(
        self,
        index: int,
        qos,
        bandwidth,
        default: bool
    ):
        self.index = index
        self.qos = qos
        self.bandwidth = bandwidth
        self.default = default

        self._update()

    def _update(self):
        res = RequestHandler.instance().update_network_slice(self)
        if res.status_code == 200:
            self.id = res.json()
            self.active = True

    def destroy(self):
        res = RequestHandler.instance().delete_network_slice(self)
        if res.status_code == 200:
            self.active = False
