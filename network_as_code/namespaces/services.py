from typing import List
from network_as_code.models import Service
from network_as_code.namespaces import Namespace


class Services(Namespace):
    async def get(self, service_id: str) -> Service:
        data = await self.api.services.get_service(service_id)
        return Service(**data)

    async def list(self) -> List[Service]:
        data = await self.api.services.get_all_services()
        return [Service(**d) for d in data]
