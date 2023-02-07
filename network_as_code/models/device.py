from pydantic import BaseModel, EmailStr, PrivateAttr
from typing import List
from ..api import APIClient
from ..models.qos_flow import QosFlow

class Device(BaseModel):
    _api: APIClient = PrivateAttr()
    _qos_flows: List[QosFlow] = PrivateAttr()
    sid: EmailStr
    ip: str

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        self._qos_flows = []

    @property
    def id(self):
        return str(self.sid)

    def create_qos_flow(self, service_ip, service_tier):
        # TODO: This should call an API
        self._qos_flows.append(QosFlow(ue_ip=self.ip, service_ip=service_ip, service_tier=service_tier))

    def qos_flows(self) -> List[QosFlow]:
        # TODO: This should query an API
        return self._qos_flows

    def clear_qos_flows(self):
        # TODO: This should run delete on all QoS Flows
        self._qos_flows.clear()
