from .Device import Device
from .RequestHandler import RequestHandler


class NetworkSlice:
    def __init__(
        self, device: Device, index: int, qos: int, bandwidth: int, default: bool
    ):
        self._device = device
        res = RequestHandler.instance.create_network_slice(
            device, index=index, qos=qos, bandwidth=bandwidth, default=default
        )
        data = res.json()
        self.__id = data["_id"]
        self._update_slice_attributes(data)

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
        if value < 0 or value > 7:  # This is a placeholder check
            raise ValueError("Network slice index must be between 0 and 7")
        self.update(index=value)

    @property
    def qos(self) -> int:
        return self._qos

    @qos.setter
    def qos(self, value: int):
        if value < 0 or value > 4:  # This is a placeholder check
            raise ValueError("Network slice QoS value must be between 0 and 4")
        self.update(qos=value)

    @property
    def bandwidth(self) -> int:
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value: int):
        if value < 0:  # This is a placeholder check
            raise ValueError("Bandwidth below 0 is not possible")
        self.update(bandwidth=value)

    @property
    def default(self) -> bool:
        return self._default

    @default.setter
    def default(self, value: bool):
        self.update(default=value)

    def _update_slice_attributes(self, attributes: dict):
        self._index = attributes["index"]
        self._qos = attributes["qos"]
        self._bandwidth = attributes["bandwidth"]
        self._default = attributes["default"]

    def update(
        self,
        index: int = None,
        qos: int = None,
        bandwidth: int = None,
        default: bool = None,
    ):
        """
        Update one or more parameters of the network slice at once.

        Arguments:
            index: New index of the slice
            qos: Quality of Service options
            bandwidth: New Mbps value of the slice
            default: Whether this is should default slice for this device
        """
        params = {
            "index": self.index if index is None else index,
            "qos": self.qos if qos is None else qos,
            "bandwidth": self.bandwidth if bandwidth is None else bandwidth,
            "default": self.default if default is None else default,
        }
        res = RequestHandler.instance.update_network_slice(self.device, **params)
        self._update_slice_attributes(res.json())

    def destroy(self):
        """Delete the network slice from the network."""
        RequestHandler.instance.delete_network_slice(self)
        return True
