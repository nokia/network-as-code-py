from pydantic import BaseModel, EmailStr, PrivateAttr
from typing import List, Union

from openapi_client.model.create_session import CreateSession
from openapi_client.model.ports_spec import PortsSpec
from openapi_client.schemas import unset
from ..api import APIClient
from ..models.session import Session

class Device(BaseModel):
    _api: APIClient = PrivateAttr()
    _sessions: List[Session] = PrivateAttr()
    sid: EmailStr
    ip: str 

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        self._sessions = []

    @property
    def id(self):
        return str(self.sid)

    def create_session(self, service_ip, profile, device_ports: Union[None, PortsSpec] = None, service_ports: Union[None, PortsSpec] = None):
        session_resource = CreateSession(
            qos=profile,
            id=self.sid,
            ip=self.ip,
            ports=device_ports if device_ports is not None else unset,
            appIp=service_ip,
            appPorts=service_ports if service_ports is not None else unset,
        )

        session = self._api.sessions.create_qos_sessions_post(session_resource)

        self._sessions.append(Session(id=session.id, device_ip=self.ip, device_ports=device_ports, service_ip=service_ip, service_ports=service_ports, profile=session.qos, status=session.status))

    def sessions(self) -> List[Session]:
        # TODO: This should query an API
        return self._sessions

    def clear_sessions(self):
        # TODO: This should run delete on all QoS Flows
        self._sessions.clear()
