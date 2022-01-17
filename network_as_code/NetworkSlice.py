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
        self._check_attributes(
            index=index,
            qos=qos,
            bandwidth=bandwidth,
            default=default,
        )
        res = RequestHandler.instance.create_network_slice(
            device,
            index=index,
            qos=qos,
            bandwidth=bandwidth,
            default=default,
        )
        data = res.json()
        self.__id = data["_id"]
        self._set_attributes(data)

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
        self.update(index=value)

    @property
    def qos(self) -> int:
        return self._qos

    @qos.setter
    def qos(self, value: int):
        self.update(qos=value)

    @property
    def bandwidth(self) -> int:
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value: int):
        self.update(bandwidth=value)

    @property
    def default(self) -> bool:
        return self._default

    @default.setter
    def default(self, value: bool):
        self.update(default=value)

    def _check_attributes(self, *, index, qos, bandwidth, default):
        if index < 0 or index > 7:
            raise ValueError("Network slice index must be between 0 and 7")
        if qos < 0 or qos > 4:
            raise ValueError("Network slice QoS value must be between 0 and 4")
        if bandwidth < 0:
            raise ValueError("Bandwidth of a slice below 0 is not possible")
        if not isinstance(default, bool):
            raise TypeError(
                "The 'default' attribute of a network slice must be of type bool"
            )

    def _set_attributes(self, attributes: dict):
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
        Update one or more parameters of the network slice.

        Arguments:
            index (int): New index of the slice. Range: [0..7].
            qos (int): Quality of Service options. One of: 'low-latency', ...
            bandwidth (int): How much bandwidth should be reserved in Mbps.
            default (bool): Whether this is the default slice for this device.
        """
        params = {
            "index": self.index if index is None else index,
            "qos": self.qos if qos is None else qos,
            "bandwidth": self.bandwidth if bandwidth is None else bandwidth,
            "default": self.default if default is None else default,
        }
        self._check_attributes(**params)
        res = RequestHandler.instance.update_network_slice(self.device, **params)
        self._set_attributes(res.json())

    def destroy(self):
        """Delete the network slice from the network."""
        RequestHandler.instance.delete_network_slice(self)
        return True
