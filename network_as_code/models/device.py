from pydantic import BaseModel, EmailStr, PrivateAttr
from typing import List
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

    def create_session(self, service_ip, service_tier):
        # TODO: This should call an API
        self._sessions.append(Session(device_ip=self.ip, service_ip=service_ip, service_tier=service_tier))

    def sessions(self) -> List[Session]:
        # TODO: This should query an API
        return self._sessions

    def clear_sessions(self):
        # TODO: This should run delete on all QoS Flows
        self._sessions.clear()
