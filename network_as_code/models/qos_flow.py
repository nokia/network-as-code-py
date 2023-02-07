
from pydantic import BaseModel, PrivateAttr

from network_as_code.api.client import APIClient

class QosFlow(BaseModel):
    _api: APIClient = PrivateAttr()
    ue_ip: str
    service_ip: str
    service_tier: str

    def delete(self):
        "TODO"
