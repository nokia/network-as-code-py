from typing import List
from ..models import Service
from .namespace import Namespace

class Services(Namespace):
    async def get(self, service_id: str) -> Service:
        data = await self.api.services.get_service(service_id)
        return Service(**data)

    async def list(self) -> List[Service]:
        data = await self.api.services.get_all_services()
        return [Service(**d) for d in data]
