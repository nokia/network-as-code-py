from pydantic import BaseModel, EmailStr, PrivateAttr
from typing import List, Union

from qos_client.model.create_session import CreateSession
from qos_client.model.ports_spec import PortsSpec
from qos_client.schemas import unset
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
        session = session.body

        self._sessions.append(Session(api=self._api, id=session["id"], device_ip=self.ip, device_ports=device_ports, service_ip=service_ip, service_ports=service_ports, profile=session["qos"], status=session["qosStatus"]))

    def sessions(self) -> List[Session]:
        sessions = self._api.sessions.get_all_qos_sessions_get(query_params={"id": self.sid})
        return list(map(lambda session : self.__convert_session_model(session), sessions.body))

    def clear_sessions(self):
        for session in self.sessions():
            session.delete()

    def __convert_session_model(self, session) -> Session:
       return Session(api=self._api, id=session["id"], device_ip=self.ip, device_ports=None, service_ip="", service_ports=None, profile=session["qos"], status=session["qosStatus"]) 
