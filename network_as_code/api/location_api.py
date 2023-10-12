import httpx

from ..errors import error_handler

from typing import cast

class LocationVerifyAPI:
    def __init__(self, base_url: str, rapid_key:str, rapid_host: str):
        self.client = httpx.Client(
            base_url=base_url, 
            headers={"X-RapidAPI-Host": rapid_host, "X-RapidAPI-Key": rapid_key
        })

    def verify_location(self, latitude, longitude, device, radius, max_age):
        body = {
            "device": device.to_json_dict(),
            "area": {
                "areaType": "Circle",
                "center": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "radius": radius
            }
        }

        if max_age:
            body["maxAge"] = cast(int, max_age)

        response = self.client.post(
            url = "/verify",
            json=body
        )

        return response.json()["verificationResult"] == "TRUE"


class LocationRetrievalAPI:
    def __init__(self, base_url: str, rapid_key:str, rapid_host: str):
        self.client = httpx.Client(
            base_url=base_url, 
            headers={"X-RapidAPI-Host": rapid_host, "X-RapidAPI-Key": rapid_key
        })

    def get_location(self, device, max_age):
        body = {
            "device": device.to_json_dict()
        }

        if max_age:
            body["maxAge"] = cast(int, max_age)

        response = self.client.post(
            url = "/retrieve",
            json=body
        )

        error_handler(response)

        return response.json()
