from pydantic import BaseModel, EmailStr, PrivateAttr
from typing import List

from openapi_client.model.qo_s_resource import QoSResource
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

    def create_session(self, service_ip, profile, device_ports = None, service_ports = None):
        qos_resource = QoSResource(
            qos=profile,
            id=self.sid,
            ip=self.ip,
            ports=device_ports if device_ports is not None else unset,
            appIp=service_ip,
            appPorts=service_ports if service_ports is not None else unset,
        )

        self._api.sessions.send_subscribe_sessions_post(qos_resource)

        self._sessions.append(Session(device_ip=self.ip, device_ports=device_ports, service_ip=service_ip, service_ports=service_ports, profile=profile))

    def sessions(self) -> List[Session]:
        # TODO: This should query an API
        return self._sessions

    def clear_sessions(self):
        # TODO: This should run delete on all QoS Flows
        self._sessions.clear()
