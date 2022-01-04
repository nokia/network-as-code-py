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
        self.default = default
        self.active = False

        self._setup()

    def _setup(self):
        res = RequestHandler.instance.create_network_slice(self)
        body = res.json()
        self.id = body["slice_id"]
        self.active = True

    def _update(self):
        res = RequestHandler.instance.update_network_slice(self)
        if res.status_code == 200:
            self.active = True

    def update(self, index: int, qos, bandwidth, default: bool):
        self.index = index
        self.qos = qos
        self.bandwidth = bandwidth
        self.default = default

        self._update()

    def destroy(self):
        RequestHandler.instance.delete_network_slice(self)
        self.active = False
