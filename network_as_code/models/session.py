
from pydantic import BaseModel, PrivateAttr

from typing import Union

from network_as_code.api.client import APIClient

from qos_client.model.ports_spec import PortsSpec
from qos_client.model.ports_spec import PortsSpecRangesInner

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
        self._api.sessions.delete_qos_sessions_resource_id_delete(path_params={'resource_id': self.id})

    @staticmethod
    def convert_session_model(api, ip, session):
        return Session(api=api, id=session["id"], device_ip=ip, device_ports=None, service_ip="", service_ports=None, profile=session["qos"], status=session["qosStatus"]) 
