from pydantic import BaseModel, Field

class Location(BaseModel):
    age: int = Field(..., alias="ageOfLocationInfo")
    tracking_area: str = Field(..., alias="trackingAreaId")
    plmn_id: int = Field(..., alias="plmnId")
    latitude: float = Field(..., alias="lat")
    longitude: float = Field(..., alias="long")
    elevation: float = Field(..., alias="elev")
