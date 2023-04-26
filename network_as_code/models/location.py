
from pydantic import BaseModel
from typing import Optional

class CivicAddress(BaseModel):
    country: str
    a1: str
    a2: str
    a3: str
    a4: str
    a5: str
    a6: str

class Location(BaseModel):
    longitude: float
    latitude: float
    civic_address: Optional[CivicAddress]

