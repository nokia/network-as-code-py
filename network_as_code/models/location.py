
from pydantic import BaseModel
from typing import Optional

class CivicAddress(BaseModel):
    country: Optional[str] 
    a1: Optional[str]
    a2: Optional[str]
    a3: Optional[str] 
    a4: Optional[str]
    a5: Optional[str]
    a6: Optional[str]

class Location(BaseModel):
    longitude: float
    latitude: float
    civic_address: Optional[CivicAddress]

