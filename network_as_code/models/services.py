from uuid import UUID
from typing import List
from pydantic import BaseModel, Field


class Slice(BaseModel):
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


class Region(BaseModel):
    name: str
    latitude: int
    longitude: int


class Service(BaseModel):
    id: UUID
    name: str
    regions: List[Region]
    slices: List[Slice]
