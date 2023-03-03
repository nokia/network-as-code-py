
from pydantic import BaseModel, PrivateAttr

from typing import Union

from network_as_code.api.client import APIClient

class Session(BaseModel):
    _api: APIClient = PrivateAttr()
    id: str
    device_ip: str
    device_ports: Union[str, None]
    service_ip: str
    service_ports: Union[str, None] 
    profile: str
    status: str

    def delete(self):
        "TODO"
