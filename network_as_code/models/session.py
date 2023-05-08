
from pydantic import BaseModel, PrivateAttr, Field

from typing import Union, List

from network_as_code.api.client import APIClient

ALIASES = {
    "start": "from",
    "end": "to"
}

def alias_generator(name: str) -> str:
    return ALIASES.get(name, name)

class PortRange(BaseModel, allow_population_by_field_name = True, alias_generator=alias_generator):
    start: int
    end: int

class PortsSpec(BaseModel):
    ranges: List[PortRange] = []
    ports: List[int] = []

class Session(BaseModel, arbitrary_types_allowed = True):
    _api: APIClient = PrivateAttr()
    id: str
    device_ip: str
    device_ports: Union[PortsSpec, None]
    service_ip: str
    service_ports: Union[PortsSpec, None] 
    profile: str
    status: str

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

    def delete(self):
        self._api.sessions.delete_session(path_params={'sessionId': self.id})

    @staticmethod
    def convert_session_model(api, ip, session):
        return Session(api=api, id=session["id"], device_ip=ip, device_ports=None, service_ip="", service_ports=None, profile=session["qosProfile"], status=session["qosStatus"]) 


