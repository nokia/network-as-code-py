from uuid import UUID
from typing import List
from pydantic import BaseModel, PrivateAttr
from .slice import Slice
from ..api import APIClient


class Region(BaseModel):
    name: str
    latitude: int
    longitude: int


class Service(BaseModel):
    _api: APIClient = PrivateAttr()
    id: UUID
    name: str
    regions: List[Region]
    slices: List[Slice]

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
