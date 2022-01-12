from .Device import Device
from .RequestHandler import RequestHandler


class NetworkSlice:
    def __init__(
        self,
        device: Device,
        index: int,
        qos: int,
        bandwidth: int,
        default: bool,
    ):
        self._device = device
        self.index = index
        self.qos = qos
        self.bandwidth = bandwidth
        self.default = default

        res = RequestHandler.instance.create_network_slice(
            device,
            index=index,
            qos=qos,
            bandwidth=bandwidth,
            default=default,
        )
        data = res.json()
        self.__id = data["_id"]

    @property
    def device(self) -> Device:
        return self._device

    @property
    def _id(self) -> int:
        return self.__id

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int):
        if value < 0 or value > 7:
            raise ValueError("Network slice index must be between 0 and 7")
        self._index = value

    @property
    def qos(self) -> int:
        return self._qos

    @qos.setter
    def qos(self, value: int):
        if value < 0 or value > 4:
            raise ValueError("Network slice QoS must be between 0 and 4")
        self._qos = value

    @property
    def bandwidth(self) -> int:
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value: int):
        if value < 0:
            raise ValueError("Bandwidth below 0 is not possible")
        self._bandwidth = value

    @property
    def default(self) -> bool:
        return self._default

    @default.setter
    def default(self, value: bool):
        self._default = value

    def update(
        self,
        index: int = None,
        qos: int = None,
        bandwidth: int = None,
        default: bool = None,
    ):
        """
        Update one or more parameters of the network slice.

        Arguments:
            index (int): New index of the slice. Range: [0..7].
            qos (int): Quality of Service options. One of: 'low-latency', ...
            bandwidth (int): How much bandwidth should be reserved in Mbps.
            default (bool): Whether this is the default slice for this device.
        """
        # Initial values
        params = {
            "index": self.index,
            "qos": self.qos,
            "bandwidth": self.bandwidth,
            "default": self.default,
        }
        # Perform value checks and
        # replace values that are going to be updated
        if index is not None:
            self.index = index
            params["index"] = index
        if qos is not None:
            self.qos = qos
            params["qos"] = qos
        if bandwidth is not None:
            self.bandwidth = bandwidth
            params["bandwidth"] = bandwidth
        if default is not None:
            self.default = default
            params["default"] = default

        res = RequestHandler.instance.update_network_slice(self.device, **params)
        data = res.json()

        self.index = data["index"]
        self.qos = data["qos"]
        self.bandwidth = data["bandwidth"]
        self.default = data["default"]

    def destroy(self):
        """Delete the network slice from the network."""
        RequestHandler.instance.delete_network_slice(self)
        return True
