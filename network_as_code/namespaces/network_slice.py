from uuid import UUID
from typing import List
from . import Namespace
from ..models import Slice


class NetworkSlices(Namespace):
    async def get(self, service_id: "UUID|str", slice_id: "UUID|str") -> Slice:
        """Get a specific slice from a service.

        Args:
            service_id (UUID|str): The UUID of the service
            slice_id (UUID|str): The UUID of the slice

        Returns:
            A `Slice` object representing the requested slice.
        """
        _service = str(service_id)
        _slice = str(slice_id)
        data = await self.api.services.get_slice(_service, _slice)
        return Slice(**data)

    async def list(self, service_id: str) -> List[Slice]:
        """List all slices belonging to a service.

        Args:
            service_id (str): The UUID of the service

        Returns:
            A list of `Slice` objects or an empty list if no slices are available.
        """
        data = await self.api.services.get_service(service_id)
        if "slices" in data:
            return [Slice(**d) for d in data["slices"]]
        raise RuntimeError("The backend API did not specify any 'slices'")

    async def create(self, **kwargs) -> Slice:
        # TODO: Add the long list of parameters (see api/endpoints/services.py)
        data = await self.api.services.create_slice(**kwargs)
        return Slice(**data)
