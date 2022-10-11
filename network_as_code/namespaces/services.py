from uuid import UUID
from typing import List
from . import Namespace
from ..models import Service


class Services(Namespace):
    async def get(self, service_id: "UUID|str") -> Service:
        """Get information about a single 5G Core service.

        Args:
            service_id (UUID|str): The UUID of the service

        Returns:
            A `Service` object representing the requested service.
        """
        _id = str(service_id)
        data = await self.api.services.get_service(_id)
        return Service(api=self.api, **data)

    async def list(self) -> List[Service]:
        """Get the list of current services and their details.

        Returns:
            A list of `Service` objects or an empty list if no services are available.
        """
        data = await self.api.services.get_all_services()
        return [Service(api=self.api, **d) for d in data]
