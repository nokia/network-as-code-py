from typing import List
from network_as_code.models import Slice
from network_as_code.namespaces import Namespace


class NetworkSlices(Namespace):
    async def get(self, service_id: str, slice_id: str) -> Slice:
        data = await self.api.services.get_slice(service_id, slice_id)
        return Slice(**data)

    async def list(self, service_id: str) -> List[Slice]:
        data = await self.api.services.get_service()

    async def create(self, slice: Slice) -> Slice:
        data = await self.api.services.create_slice(slice)
