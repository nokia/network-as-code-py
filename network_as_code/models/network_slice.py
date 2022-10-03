from typing import List
from .resource import Model, Collection


class NetworkSlice(Model):
    """Representation of a Network Slice."""

    @property
    def id(self) -> str:
        raise NotImplementedError

class NetworkSliceCollection(Collection):
    """Representation of a set of Network Slices."""
    model = NetworkSlice

    async def get(self, id: str) -> NetworkSlice:
        raise NotImplementedError

    async def list(self) -> List[NetworkSlice]:
        raise NotImplementedError

    async def create(self, attrs=None) -> NetworkSlice:
        raise NotImplementedError
