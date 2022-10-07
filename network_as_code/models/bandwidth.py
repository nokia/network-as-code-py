from pydantic import BaseModel, Field


class Bandwidth(BaseModel):
    priority: str
    service_tier: str = Field(..., alias="serviceTier")


class CustomBandwidth(BaseModel):
    service_tier: str = Field("custom", const=True)
    upload: int
    download: int
