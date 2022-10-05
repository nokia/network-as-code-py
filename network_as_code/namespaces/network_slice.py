from typing import List
from ..models import Slice
from .namespace import Namespace

class NetworkSlices(Namespace):
    async def get(self, service_id: str, slice_id: str) -> Slice:
        data = await self.api.services.get_slice(service_id, slice_id)
        return Slice(**data)

    async def list(self) -> List[Slice]:
        raise NotImplementedError

    async def create(self, attrs=None) -> Slice:
        raise NotImplementedError
