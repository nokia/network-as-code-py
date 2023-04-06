
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

    def delete(self):
        self._api.sessions.delete_qos_sessions_resource_id_delete(path_params={'resource_id': self.id})
