from pydantic import BaseModel, Field, PrivateAttr
from uuid import UUID
from ..api import APIClient


class Slice(BaseModel):
    _api: APIClient = PrivateAttr()
    service_id: UUID = Field(..., alias="serviceId")
    name: str
    list_name: str = Field(..., alias="listName")
    plmn: str = Field(..., alias="plmnName")
    set_id: str = Field(..., alias="setId")
    region_id: str = Field(..., alias="regionId")
    access_point_name: str = Field(..., alias="apnName")
    slice_type: str = Field(..., alias="sliceTypeId")
    slice_service_type: str = Field(..., alias="SliceServiceType")
    slice_differentiator: str = Field(..., alias="sd")
    data_network_name: str = Field(..., alias="dataNetworkName")
    data_network_list_name: str = Field(..., alias="dnnList")
    packet_data_network_gateway_id: str = Field(..., alias="pdnGwId")

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

    async def delete(self):
        self._api.services.delete_slice(self.service_id, self.service_id)
