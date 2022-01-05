from .Device import Device
from .RequestHandler import RequestHandler


class NetworkSlice:
    def __init__(
        self, device: Device, index: int, qos: int, bandwidth: int, default: bool
    ):
        # These will be run through the property setters below
        self._device = device
        self.index = index
        self.qos = qos
        self.bandwidth = bandwidth
        self.default = default

        # Make a request to the gateway to create the actual network slice
        res = RequestHandler.instance.create_network_slice(self)
        data = res.json()
        self._id = data["slice_id"]  # Save the slice id for future requests

    @property
    def device(self) -> Device:
        return self._device

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int):
        if value < 0 or value > 7:  # This is a placeholder check
            raise ValueError("Network slice index must be between 0 and 7")
        self._index = value

    @property
    def qos(self) -> int:
        return self._qos

    @index.setter
    def qos(self, value: int):
        if value < 0 or value > 4:  # This is a placeholder check
            raise ValueError("Network slice QoS value must be between 0 and 4")
        self._qos = value

    @property
    def bandwidth(self) -> int:
        return self._bandwidth

    @index.setter
    def bandwidth(self, value: int):
        if value < 0:  # This is a placeholder check
            raise ValueError("Bandwidth below 0 is not possible")
        self._bandwidth = value

    @property
    def default(self) -> bool:
        return self._default

    @index.setter
    def default(self, value: bool):
        self._default = value

    def update(self, index: int, qos: int, bandwidth: int, default: bool):
        """
        Update all parameters of the network slice at once.

        Arguments:
            index: New index of the slice
            qos: Quality of Service options
            bandwidth: New Mbps value of the slice
            default: Whether this is should default slice for this device
        """
        params = {
            "_id": self._id,
            "index": index,
            "qos": qos,
            "bandwidth": bandwidth,
            "default": default,
        }
        res = RequestHandler.instance.update_network_slice(params)

        data = res.json()
        self.index = data["index"]
        self.qos = data["qos"]
        self.bandwidth = data["bandwidth"]
        self.default = data["default"]

    def destroy(self):
        """
        Deletes the network slice from the network.
        """
        RequestHandler.instance.delete_network_slice(self)
