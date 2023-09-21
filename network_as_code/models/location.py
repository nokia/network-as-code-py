
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
    """
    A class representing the `Location` model.
    
    #### Public Attributes:
            longitude (float): the `longitude` of a location object.
            latitude (float): the `latitude` of a location object.
            civic_address (Optional[CivicAddress]): the `civic_address` of a location object.
    """
    longitude: float
    latitude: float
    civic_address: Optional[CivicAddress]

